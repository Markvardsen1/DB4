import time

import machine
from Systems import components
from Systems.Hardware import *

components.valveSwitch.start()
components.valveSwitch.setSpeedCycle(800)


while True:
    print("hej:DDD")
    time.sleep(0.1)