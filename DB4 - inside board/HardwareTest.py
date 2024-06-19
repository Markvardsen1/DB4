import time

import machine
from Systems import components

#Used for running tests

components.fan.startFan()
components.cooler.highCooling()

procent = 100

components.largeDCMotor.start()
components.largeDCMotor.setSpeedPercentage(procent)
# components.largeDCMotor.setSpeedCycles(512)


while True:
    print("Testing")
    print("h")
    time.sleep(0.1)