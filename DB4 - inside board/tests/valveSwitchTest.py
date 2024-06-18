import time

import machine
from Systems import components
from Systems.Hardware import *

print("stopping fan")

# components.valveSwitch.testDelay()

for dir in range(10):
    components.valveSwitch.testRotate(dir % 2)
    dir =+ 1
    time.sleep(2)

