import time

import machine
from Systems import components

components.cooler.highCooling()
components.fan.startFan()
#components.largeDCMotor.start()
# components.largeDCMotor.setSpeedCycles(1023)

while True:
    

    components.largeDCMotor.start()
    components.largeDCMotor.setSpeedCycles(1023)
    time.sleep(5)
    components.largeDCMotor.stop()
    
    time.sleep(0.2)
    components.valveSwitch.start()
    components.valveSwitch.switch()
    components.valveSwitch.stop()
    time.sleep(5)
    




while True:
    
    od = components.odSensor.getOD()
    temperature = components.temperatureSensor.getTemperature()
    print("OD:" + str(od))
    print("temperature:" + str(temperature))
    time.sleep(1)
