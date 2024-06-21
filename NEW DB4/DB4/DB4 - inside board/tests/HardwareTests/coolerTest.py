import time

import machine
from Systems import components

while True:
    components.cooler.highCooling()
    print("cooling for 3 sec")
    time.sleep(10)
    print("low for 3 sec")
    components.cooler.lowCooling()
    time.sleep(10)
