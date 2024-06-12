import time

import board  # the structure of the board is to be determined
import web
from OLEDScreen import *
from smallDCMotor import *
from stepperMotor import *
from TemperatureSensor import *

from ElectronicsGuide.electronicsparts.cooler import *
from ElectronicsGuide.electronicsparts.largeDCmotor import *
from ElectronicsGuide.electronicsparts.LightSensortsl257 import *

#VARIABLES TO CHANGE:

WIFI_SSID         = "dsfasGg"
WIFI_PASSWORD     = "bahamondes"

ADAFRUIT_USERNAME = "felimondes"
ADAFRUIT_IO_KEY   = ""


#OBJECTS TO USE:
#temp sensor
temp_pin = 25
FixedResistor = 10000
temp_sensor = Temperature(temp_pin, FixedResistor)

# Stepper Motor
stepper_pin = 33
direction_pin = 27
stepperMotor = StepperMotor(stepper_pin, direction_pin)

# smallDCMotor
inputA = 21
inputB = 17
EnableA = 16
smallDCMotor = SmallDCMotor(inputA, inputB, EnableA)

# largeDCMotor maybe pins are swapped
inputC = 15
inputD = 14
EnableB = 32
largeDCMotor = LargeDCMotor(inputC, inputD, EnableB)

# cooler - check with voltmeter if self.cooling_pin.value(1) is 12V or not
cooling_pin = 12
cooler = Cooler(cooling_pin)

# OLEDScreen 
sclPin = 22
sdaPin = 23
oled = OLEDScreen(sclPin, sdaPin)

# LightSensor
lightSensorPin = 36 
lightSensor = LightSensor(lightSensorPin)


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
        
    temperature = temp_sensor.getTemperature()
    
    
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
    
    
    
    
    


    
    








