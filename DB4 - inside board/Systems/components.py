from Systems.Hardware import *

temperatureSensorPin = 25
FixedResistor = 10000
temperatureSensor= TemperatureSensor(temperatureSensorPin)


stepper_pin = 33
direction_pin = 27
stepperMotor = StepperMotor(stepper_pin, direction_pin)


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
fan_pin_Inp2 = 12
cooler = Cooler(cooling_pin_Inp1)


fan_pin_Inp2 = 12
fan = Fan(fan_pin_Inp2)


sclPin = 22
sdaPin = 23
oledScreen = OLEDScreen(sclPin, sdaPin)


ODSensorPin = 26
odSensor = ODSensor(ODSensorPin)

