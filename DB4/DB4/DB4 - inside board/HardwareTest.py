import time 
import machine 
from Systems.Hardware import *
from Systems.Software import *
from Systems import components

# #TODO - make a component for PIDTemperature
# #TODO - run PidController with largeDCMotor for 10 seconds
# #TODO - switch once and then run largeDCMotor for 5 seconds 
# #TODO - switch again and run largeDCMotor for 10seconds. 

# def testCoolingWaterAndSwitching():
#     components.cooler.highCooling()
#     components.fan.startFan()
#     components.largeDCMotor.start()

#     for _ in range(10):
#         components.pidTemperatureController.runPIDforTemperatureSensor()
#         time.sleep(1)

#     components.largeDCMotor.stop()
#     time.sleep(1)
#     components.valveSwitch.start()
#     components.valveSwitch.switch()
#     components.valveSwitch.stop()
#     time.sleep(1)
#     components.largeDCMotor.start()

#     for _ in range(5):
#         components.largeDCMotor.setSpeedPercentage(50)
#         time.sleep(1)
        
#     components.largeDCMotor.stop()
#     time.sleep(1)
#     components.valveSwitch.start()
#     components.valveSwitch.switch()
#     components.valveSwitch.stop()
#     time.sleep(1)

# if __name__ == '__main__':
#     components.cooler.highCooling()
#     components.fan.startFan()
#     components.largeDCMotor.start()
#     while True:
#         # testCoolingWaterAndSwitching()
#         print("Time: " , time.time() , "," , "Temp: " , components.temperatureSensor.getMedianTemperature())

#         for _ in range(10):
#             components.pidTemperatureController.runPIDforTemperatureSensor()
#             time.sleep(0.3)
            


if __name__ == '__main__':
    components.ledStrip.start()
    components.ledStrip.setLightPercentage(50)

    while True: 
        time.sleep(3)
        print(components.odSensor.getOD())
