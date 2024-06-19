
from Systems.Hardware import *
from Systems.Hardware.Cooler import Cooler
from Systems.Hardware.Fan import Fan
from Systems.Hardware.LargeDCMotor import LargeDCMotor
from Systems.Hardware.LEDStrip import LEDStrip
from Systems.Hardware.ODSensor import ODSensor
from Systems.Hardware.OLEDScreen import OLEDScreen
from Systems.Hardware.TemperatureSensor import TemperatureSensor
from Systems.Hardware.ValveSwitch import ValveSwitch
from Systems.Software.AdafruitIOClient import AdafruitIOClient
from Systems.Software.DataPublisher import DataPublisher
from Systems.Software.OfflineClient import OfflineClient
from Systems.Software.WifiConnecter import WifiConnecter
from Systems.Software.PIDandlinearization.PID import PID

#notes

#yellow = 12v
#red = 5v
#white = 3v
#green ground


#relay :
#vcc = 12v 


#HARDWARE

temperatureSensorPin = 25
FixedResistor = 10000
temperatureSensor= TemperatureSensor(temperatureSensorPin)


stepper_pin = 33
direction_pin = 27
valveSwitch = ValveSwitch(stepper_pin, direction_pin)


#inputA = 21
#inputB = 17
#EnableA = 16
#smallDCMotor = SmallDCMotor(inputA, inputB, EnableA)


inputA = 21
inputB = 17
EnableA = 16
ledStrip = LEDStrip(inputA, inputB, EnableA)


inputC = 15
inputD = 14
EnableB = 32
largeDCMotor = LargeDCMotor(inputC, inputD, EnableB)


cooling_pin_Inp1 = 13
cooler = Cooler(cooling_pin_Inp1)


fan_pin_Inp2 = 12
fan = Fan(fan_pin_Inp2)


sclPin = 22
sdaPin = 23
oledScreen = OLEDScreen(sclPin, sdaPin)


ODSensorPin = 26
odSensor = ODSensor(ODSensorPin)





#SOFTWARE:


#TODO Mathis fix this 
pidTemperatureController = PID(Kp=1.5, Ki=0.5, Kd=1.5, setpoint=18, sample_time=0.1, output_limits=(-100, 0))
#pidODController = PIDController()

wifiConnecter = WifiConnecter()
adafruitIOClient = AdafruitIOClient()
offlineClient = OfflineClient()
dataPublisher = DataPublisher(adafruitIOClient, offlineClient)