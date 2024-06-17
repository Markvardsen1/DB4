import time

import machine
from Systems import components
from Systems.Hardware import *

components.valveSwitch.start()
components.valveSwitch.setSpeedCycle()


while True:
    print("hej:DDD")