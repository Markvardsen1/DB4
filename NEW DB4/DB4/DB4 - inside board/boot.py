# boot.py -- run on boot-up
print("BOOOOOOOOOTING UPPPPPP!!!!")


import time

import machine
from Systems import components

components.fan.stopFan()
time.sleep(0.01)
components.cooler.lowCooling()
time.sleep(0.01)
components.largeDCMotor.stop()
time.sleep(0.01)
components.ledStrip.stop()
time.sleep(0.01)



