from time import sleep
from electronicsAndPID import * 

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
odSensor = ODSensor(ODSensorPin)


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
    tempSensor.stop()
    stepperMotor.stop()
    cooler.stop()
    oled.stop()
    odSensor.stop()
    smallDCMotor.stop()
    largeDCMotor.stop()

    
def startDevices():
    print("Oled")
    oled.start()
    sleep(3)
    
    print("Cooler")
    cooler.start()
    sleep(3)
    
    
    print("Large")
    largeDCMotor.start()
    sleep(3)
    
    print("ODSensor")
    odSensor.start()
    sleep(3)
    
    
    print("SmallDCMotor")
    smallDCMotor.start()
    sleep(3)
    
    print("StepperMotor")
    stepperMotor.start()
    sleep(3)
    
    
    print("starting temperature Sesnor ")
    tempSensor.start()
    sleep(10)
    
def test():
    stopAllDevies()
    sleep(1)
    
    startDevices()
    stopAllDevies()
    
test()