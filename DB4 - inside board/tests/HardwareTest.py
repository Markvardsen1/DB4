import time

import machine
from Systems import components

#Used for running tests

components.fan.startFan()
components.cooler.highCooling()

procent = 2

components.largeDCMotor.start()
components.largeDCMotor.setSpeedPercentage(procent)

while True:
    print("Testing")
    print(procent)
    time.sleep(0.5)