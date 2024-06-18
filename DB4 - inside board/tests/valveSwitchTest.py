import time

import machine
from Systems import components
from Systems.Hardware import *

print("stopping fan")
components.valveSwitch.setSpeedCycle(0)

components.valveSwitch.rotate(90,0)



