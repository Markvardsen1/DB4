import time

import machine
from Systems import components

dirr = 0
while True:
    components.valveSwitch.switch()
    time.sleep(1)

