import time

import machine
from Systems import components
from Systems.Hardware import *

components.valveSwitch.setSpeedCycle(1000)


time.sleep(3)


print("starting switch test")

print("turning on")
components.valveSwitch.ON()


components.valveSwitch.setSpeedCycle(0)

time.sleep(2)
components.valveSwitch.setSpeedCycle(1000)
print("turning off")
components.valveSwitch.OFF()

components.valveSwitch.setSpeedCycle(0)

