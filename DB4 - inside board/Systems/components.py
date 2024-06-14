from Systems.electronicsAndPID import *

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
#inputA = 21
#inputB = 17
#EnableA = 16
#smallDCMotor = SmallDCMotor(inputA, inputB, EnableA)


# LED strip
inputA = 21
inputB = 17
EnableA = 16
ledStrip = LEDStrip(inputA, inputB, EnableA)


# largeDCMotor maybe pins are swapped
inputC = 15
inputD = 14
EnableB = 32
largeDCMotor = LargeDCMotor(inputC, inputD, EnableB)


# cooler - check with voltmeter if self.cooling_pin.value(1) is 12V or not
cooling_pin_Inp1 = 13
fan_pin_Inp2 = 12
cooler = Cooler(cooling_pin_Inp1)

# fan 
fan_pin_Inp2 = 12
fan = Fan(fan_pin_Inp2)

# OLEDScreen
sclPin = 22
sdaPin = 23
oledScreen = OLEDScreen(sclPin, sdaPin)

# ODSensor
ODSensorPin = 26
odSensor = ODSensor(ODSensorPin) #TODO VALTYR GIMME GIMME MORE

#Temperature PID controller #TODO temperature PID or flow rate / cooler PID???
#temperaturePID = PIDController()

#OD PID controller #TODO OD PID or light lamp PID???
#odPID = PIDController()

