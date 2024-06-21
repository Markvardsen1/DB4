import time

import machine
from Systems import components

while True:
    components.fan.stopFan()
    print("fan for 3 sec")
    time.sleep(10)
    print("fan for 3 sec")
    components.fan.startFan()
    time.sleep(10)