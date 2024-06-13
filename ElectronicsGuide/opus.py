from time import sleep

from ElectronicsGuide.electronicsAndPID import *

temp_pin = 25
FixedResistor = 10000
tempSensor = TemperatureSensor(temp_pin, FixedResistor)

# Stepper Motor
stepper_pin = 33
direction_pin = 27
stepperMotor = StepperMotor(stepper_pin, direction_pin)

# cooler - check with voltmeter if self.cooling_pin.value(1) is 12V or not
cooling_pin = 12
cooler = Cooler(cooling_pin)

# OLEDScreen
sclPin = 22
sdaPin = 23
oled = OLEDScreen(sclPin, sdaPin)

# ODSensor
ODSensorPin = 36
ODSensor = ODSensor(ODSensorPin)


# smallDCMotor
inputA = 21
inputB = 17
EnableA = 16
smallDCMotor = SmallDCMotor(inputA, inputB, EnableA)

# largeDCMotor maybe pins are swapped
inputC = 15
inputD = 14
EnableB = 32
largeDCMotor = LargeDCMotor(inputD,inputC,EnableB)


StepperMotor.stop()

def stopAllDevies():
    TemperatureSensor.stop()
    StepperMotor.stop()
    Cooler.stop()
    OLEDScreen.stop()
    ODSensor.stop()
    SmallDCMotor.stop()
    LargeDCMotor.stop()

    
def startDevices():
    print("Oled")
    OLEDScreen.start()
    sleep(3)
    
    print("Cooler")
    Cooler.start()
    sleep(3)
    
    
    print("Large")
    LargeDCMotor.start()
    sleep(3)
    
    print("ODSensor")
    ODSensor.start()
    sleep(3)
    
    
    print("SmallDCMotor")
    SmallDCMotor.start()
    sleep(3)
    
    print("StepperMotor")
    print("starting temperature Sesnor ")