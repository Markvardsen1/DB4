# boot.py -- run on boot-up
print("BOOOOOOOOOTING UPPPPPP!!!!")


import time

import machine
from Systems import components

components.fan.stopFan()
time.sleep(1)
print("stopping fan")
components.cooler.lowCooling()
time.sleep(1)
components.largeDCMotor.stop()
time.sleep(1)
components.oledScreen.displayMessage("STARTING UP")
time.sleep(1)
components.ledStrip.stop()
time.sleep(1)
print("stopping switch")
components.valveSwitch.setSpeedCycle(0)

