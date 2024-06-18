import time

import machine
from Systems import components

#Used for running tests

components.fan.startFan()
components.cooler.highCooling()

components.largeDCMotor.start()
components.largeDCMotor.setSpeedPercentage(100)
