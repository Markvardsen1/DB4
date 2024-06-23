
import os
import sys
import time

import network
from Systems.components import (largeDCMotor, odSensor, oledScreen,
                                temperatureSensor)
from umqtt.robust import MQTTClient


def connectWifi():
    
    
    # turn off the WiFi Access Point
    
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)

    # connect the device to the WiFi network
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(WIFI_SSID, WIFI_PASSWORD)
    wifiStatus = True
    # wait until the device is connected to the WiFi network
    MAX_ATTEMPTS = 5
    attempt_count = 0
    while not wifi.isconnected() and attempt_count < MAX_ATTEMPTS:
        attempt_count += 1
        print("attempt to get on wifi:" + str(attempt_count))
        time.sleep(1)

    if attempt_count == MAX_ATTEMPTS:
        print('could not connect to the WiFi network')
        wifi.active(False)
        wifiStatus = False
    
    print("waiting for wifi...")
    time.sleep(100)
    return wifi, wifiStatus
        
def createClient():
    # create a random MQTT clientID
    random_num = int.from_bytes(os.urandom(3), 'little')
    mqtt_client_id = bytes('client_'+str(random_num), 'utf-8')

    ADAFRUIT_IO_URL = b'io.adafruit.com'

    client = MQTTClient(client_id=mqtt_client_id,
                        server=ADAFRUIT_IO_URL,
                        user=ADAFRUIT_USERNAME,
                        password=ADAFRUIT_IO_KEY,
                        ssl=False)
                        
    try:
        client.connect()
        clientStatus = True
    except Exception as e:
        print('could not connect to MQTT server {}{}'.format(type(e).__name__, e))
        clientStatus = False
        pass
        
    return client, clientStatus
        
def pubAndSub(feedName, data):
    
    ADAFRUIT_IO_FEEDNAME = feedName.encode('utf-8')
    
    # the following function is the callback which is
    # called when subscribed data is received
    def cb(topic, msg):
        print("message was recieved :)")

    # publish 'FEEDNAME' statistics to Adafruit IO using MQTT
    # subscribe to 'COMMAND FEED'
    #
    # format of feed name:
    #   "ADAFRUIT_USERNAME/feeds/ADAFRUIT_IO_FEEDNAME"
    
    mqtt_commandFeed = bytes('{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, b'commandFeed'), 'utf-8') #TODO COMMAND FEED IS ADDED HERE
    mqtt_feedname = bytes('{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, ADAFRUIT_IO_FEEDNAME), 'utf-8')
    client.set_callback(cb)
    
    client.subscribe(mqtt_commandFeed)
        
        
    try:
            client.publish(mqtt_feedname,
                        bytes(str(data), 'utf-8'),
                        qos=0) 
            
            
            # Subscribe.  Non-blocking check for a new message.
            client.check_msg()
            time.sleep(SUBSCRIBE_CHECK_PERIOD_IN_SEC)

    except Exception as e:
        print('could not publish data to MQTT server {}{}'.format(type(e).__name__, e))
        
def delete_file():
    """Check if the data file exists and delete it."""
    try:
        os.remove(filePath)
        print(f"{filePath} has been removed.")
    except OSError as e:
        if e.args[0] == 2:  # File not found error
            print(f"File {filePath} does not exist.")
        else:
            print(f"Failed to remove data file: {e}")

def publish_offline(feedName, data):
    """Publish data to the file."""
    try:
        with open(filePath, 'a') as file:
            file.write(f"{feedName}:{data}\n")
            print(f"Written to file: {feedName}:{data}")
        
    except OSError as e:
        print(f"Failed to write to file: {e}")

def getDataMap():

        try:
            temperature = temperatureSensor.getTemperature()
        except Exception as e:
            print('Could not get temperature, due to {}{}'.format(type(e).__name__, e))
            temperature = None
            
        try:
            od = odSensor.getOD()
        except Exception as e:
            print('Could not get OD, due to {}{}'.format(type(e).__name__, e))
            od = None

        try:
            pumpSpeed = largeDCMotor.getSpeedPercentage()

        except Exception as e:
            print('Could not get pump speed, due to: {}{}'.format(type(e).__name__, e))
            pumpSpeed = None
            
        data = {
            "temperature": temperature,
            "od": od,
            "pumpSpeed": pumpSpeed
        }
        
        try:
            oledScreen.displayData(data)
        
        except Exception as e:
            print('Oled doesent works due to {}{}'.format(type(e).__name__, e))
        
        return data
        
def getNextPublish(dataMap):

    nextPublishName = publishOrder[publishIndex]
    nextPublishValue = dataMap[nextPublishName]
    print(f"Next item to publish: {nextPublishName}, value: {nextPublishValue}")
    
    return nextPublishName, nextPublishValue

def import_and_publish():
    """Import data from the data.txt file and publish each line."""
    
    try:
        with open(filePath, 'r') as file:
            
            for line in file:
                # Split line into name and data
                parts = line.strip().split(':')
                if len(parts) == 2:
                    feedName, data = parts[0], parts[1]
                    print("trying to publish: ", data, feedName)
                    pubAndSub(feedName, data)
                    time.sleep(2.5)
                    
                else:
                    print(f"Ignoring invalid line: {line}")
                    
        # After publishing, optionally delete the file
        os.remove(filePath)
        print(f"{filePath} has been imported and deleted.")
        
    except OSError as e:
        if e.errno == 2:  # FileNotFoundError
            print(f"File {filePath} does not exist.")
        else:
            print(f"Failed to import data file: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Constants
WIFI_SSID = "dsfasGg"
WIFI_PASSWORD = "bahamondes"


ADAFRUIT_USERNAME = b'felimondes'
PUBLISH_PERIOD_IN_SEC = 10
SUBSCRIBE_CHECK_PERIOD_IN_SEC = 0.5
RECONNECT_PERIOD_IN_SEC = 15
#commandFeed is preset

DATAFILE = "data.txt"
PATH_TO_DATAFILE_DIRECTORY = ""
filePath = PATH_TO_DATAFILE_DIRECTORY + '/' + DATAFILE


publishOrder = ["temperature", "od", "pumpSpeed"] #change this to change what to publish to
wifi, wifiStatus = connectWifi()
client, clientStatus = createClient()



publishIndex = 0
nextPublishTime = time.time() + PUBLISH_PERIOD_IN_SEC
nextReconnectTime = time.time() + RECONNECT_PERIOD_IN_SEC
while True:
    
    isTimeToPublish = nextPublishTime - time.time() < 0
    if isTimeToPublish:
        
        
        print("Measureing data with sensors...")
        dataMap = getDataMap()

        print("Finding what to publish...")
        feedName, data = getNextPublish(dataMap)
        
        if wifiStatus and clientStatus:
            
            pubAndSub(feedName, data)
            
                
        else:
            publish_offline(feedName, data)
            wifiStatus = False
            clientStatus = False
        
        publishIndex = (publishIndex + 1) % len(publishOrder)
        nextPublishTime = time.time() + PUBLISH_PERIOD_IN_SEC
    
    
    isTimeToReconnect = nextReconnectTime - time.time() < 0
    if (not wifiStatus) and (not clientStatus) & isTimeToReconnect:
        
        try:
            
            print("Reconnecting to wifi and mqtt...")
            wifi, wifiStatus = connectWifi()
            print("Connect to client...")
            client.connect()
            clientStatus = True
            
            import_and_publish()

        except Exception as e:
            print('SomeConnection or importing problem: {}{}'.format(type(e).__name__, e))
            
        nextReconnectTime = time.time() + RECONNECT_PERIOD_IN_SEC
        time.sleep(1)