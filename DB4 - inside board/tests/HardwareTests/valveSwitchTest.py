import time

import machine
from Systems import components

dirr = 0
while True:
    
    components.valveSwitch.start()
    for i in range(3):
        print("dab")
        components.valveSwitch.switch()
        time.sleep(0.2)
    
    components.valveSwitch.stop()
    time.sleep(3)
    
    

