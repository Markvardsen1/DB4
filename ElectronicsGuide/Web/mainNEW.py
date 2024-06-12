import time

import board  # the structure of the board is to be determined
import web

#VARIABLES TO CHANGE:

WIFI_SSID         = "dsfasGg"
WIFI_PASSWORD     = "bahamondes"

ADAFRUIT_USERNAME = "felimondes"
ADAFRUIT_IO_KEY   = ""



#Connecting to wifi and getting client
web.connectToWifi(WIFI_SSID, WIFI_PASSWORD)
client = web.connectToServer(ADAFRUIT_USERNAME, ADAFRUIT_IO_KEY) #Uncertain if this can work


def cb(topic, msg):
    
        #the strings in the if-statements are commands written from Arduino IO
        if msg.startswith("set.dtemp("):
            temp_str = msg[len("set.dtemp("):-1]
            board.PID_temperature(int(temp_str))
            board.displayOLED(temp_str)
        
        if msg.startswith("set.dOD("):
            temp_str = msg[len("set.dOD("):-1]
            board.PID_flow(int(temp_str))
            board.displayOLED(int(temp_str))
            
        if msg.startswith("funni("):
            temp_str = msg[len("funni("):-1]
            board.displayOLED(temp_str)

while True:
    
    temperature = board.getTemperature()
    od = board.getOD()
    flow = board.getFlow()
    
    
    #publishing
    web.publish(temperature,ADAFRUIT_USERNAME,"tempTracker", client)
    web.publish(od,ADAFRUIT_USERNAME,"odTracker", client)
    web.publish(flow,ADAFRUIT_USERNAME,"flowTracker", client) #repetitve code, maybe do list of feeds to publish to
    

    #displaying the new data
    board.displayOLED([temperature,od,flow])
    
    web.subscribeToServer(ADAFRUIT_USERNAME, "InputFeed", client)
    #this calls the cb function above
    
    time.sleep(30) #30 sec due to 3 different publishes
    
    
    
    
    


    
    








