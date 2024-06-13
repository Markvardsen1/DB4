import time

import mainOFFLINE
import mainONLINE
import web
from electronicsAndPID import *

#VARIABLES TO CHANGE:

WIFI_SSID         = "dsfasGg"
WIFI_PASSWORD     = "bahamondes"

ADAFRUIT_USERNAME = "felimondes"
ADAFRUIT_IO_KEY   = ""

filePathToData = r'C:\Users\User\Desktop\DB4\DB4\ElectronicsGuide\Web'

#OBJECTS TO USE:
#temp sensor
temp_pin = 25
FixedResistor = 10000
temperatureSensor= TemperatureSensor(temp_pin, FixedResistor)

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
oledScreen = OLEDScreen(sclPin, sdaPin)

# ODSensor
ODSensorPin = 36
odSensor = ODSensor(ODSensorPin) #TODO VALTYR GIMME GIMME MORE

#Temperature PID controller #TODO temperature PID or flow rate / cooler PID???
temperaturePID = PIDController()

#OD PID controller #TODO OD PID or light lamp PID???
odPID = PIDController()



#Connecting to wifi and getting client
try:
    web.connectToWifi(WIFI_SSID, WIFI_PASSWORD)
    client = web.connectToServer(ADAFRUIT_USERNAME, ADAFRUIT_IO_KEY) #Uncertain if this can work
    mainONLINE.run(client)
    
except ConnectionError:
    mainOFFLINE.run()
    
    
    
    


