import time

import machine
from Systems import components

while True:
    od=components.odSensor.getOD()
    print(od)
    time.sleep(1)
