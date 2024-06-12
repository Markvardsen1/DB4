import time

import web
from electronicsAndPID import *

#VARIABLES TO CHANGE:

WIFI_SSID         = "dsfasGg"
WIFI_PASSWORD     = "bahamondes"

ADAFRUIT_USERNAME = "felimondes"
ADAFRUIT_IO_KEY   = ""


#OBJECTS TO USE:
#temp sensor
temp_pin = 25
FixedResistor = 10000
tempSensor = TemperatureSensor(temp_pin, FixedResistor)

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

#Temperature PID controller #TODO temperature PID or flow rate / cooler PID???
temperaturePID = PIDController()

#OD PID controller #TODO OD PID or light lamp PID???
odPID = PIDController()

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


iter = 0
while True:
        
    temperature = tempSensor.getTemperature()
    light = lightSensor.getLightIntensity()
    
    #PID controllers #TODO
    
    
    #Subscribing
    web.subscribeToServer(ADAFRUIT_USERNAME, "InputFeed", client) #this calls the cb function above
    
    

    if iter == 200: #TODO Make iter large enough, so that it wont break the ping limit.
        
        #publishing data
        web.publish(temperature,ADAFRUIT_USERNAME,"tempTracker", client)
        web.publish(od,ADAFRUIT_USERNAME,"odTracker", client)
        web.publish(flow,ADAFRUIT_USERNAME,"flowTracker", client) #repetitve code, maybe do list of feeds to publish to
        
        #displaying stuff on OLED
        
        #TODO make some nice OLED if time.
        algaeConcentration = calculateAlageConcentration(light, dimensionsOfTube) #TODO talk to others how this can be calculated. 
        foodFlow = calculateFoodFlow(pumpFrequency, pumpDutyCyle, algaeConcentration) #TODO this would be nice to have


    iter+=1
    
    
    
    
    


    
    








