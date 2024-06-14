import os
import sys
import time

import network
from runONLINE import cb
from umqtt.robust import MQTTClient

        

def connectToServer(ADAFRUIT_USERNAME: str, ADAFRUIT_IO_KEY: str):

    # create a random MQTT clientID
    random_num = int.from_bytes(os.urandom(3), 'little')
    mqtt_client_id = bytes('client_' + str(random_num), 'utf-8')

    # Adafruit IO URL and feed name
    ADAFRUIT_IO_URL = b'io.adafruit.com'
    ADAFRUIT_IO_FEEDNAME = b'freeHeap'

    # Convert parameters to bytes
    ADAFRUIT_USERNAME = bytes(ADAFRUIT_USERNAME, 'utf-8')
    ADAFRUIT_IO_KEY = bytes(ADAFRUIT_IO_KEY, 'utf-8')

    # create an MQTT client instance
    client = MQTTClient(client_id=mqtt_client_id,
                        server=ADAFRUIT_IO_URL,
                        user=ADAFRUIT_USERNAME,
                        password=ADAFRUIT_IO_KEY,
                        ssl=False)
    try:
        client.connect()
    except Exception:
        raise ConnectionError
    
    return client


def publish(data: str, ADAFRUIT_USERNAME:str , ADAFRUIT_IO_FEEDNAME: str, client):
    # publish free heap statistics to Adafruit IO using MQTT
    #
    # format of feed name:  
    #   "ADAFRUIT_USERNAME/feeds/ADAFRUIT_IO_FEEDNAME"
    mqtt_feedname = bytes('{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, ADAFRUIT_IO_FEEDNAME), 'utf-8')
    
    try:
            client.publish(mqtt_feedname,    
                    bytes(data, 'utf-8'), 
                    qos=0)  
            
    except Exception:
            raise ConnectionError
        

def subscribeToServer(ADAFRUIT_USERNAME, ADAFRUIT_IO_FEEDNAME, client):
            
    mqtt_feedname = bytes('{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, ADAFRUIT_IO_FEEDNAME), 'utf-8')
    client.set_callback(cb)
    client.subscribe(mqtt_feedname) 

    mqtt_feedname_get = bytes('{:s}/get'.format(mqtt_feedname), 'utf-8')
    client.publish(mqtt_feedname_get, '\0')
        
        
    try:
            client.check_msg() #TODO: maybe we have to do wait.msg instead... also code is different when using "check" vs "wait"
    
    except Exception:
            raise ConnectionError
        