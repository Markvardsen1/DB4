import time

import machine
from Systems import components

while True:
    

    components.largeDCMotor.start()
    components.largeDCMotor.setSpeedCycles(1023)
    time.sleep(5)
    components.largeDCMotor.stop()
    
    time.sleep(0.2)
    components.valveSwitch.start()
    components.valveSwitch.switch()
    components.valveSwitch.stop()
    time.sleep(5)
    




