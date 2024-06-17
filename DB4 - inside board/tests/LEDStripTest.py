
import time

import machine
from Systems import components

#components.ledStrip.testMaxLight()
#components.ledStrip.testMinAndMaxDuty()

#components.ledStrip.testMinAndMaxDuty()

components.ledStrip.start()
components.ledStrip.setLight(1023)

while True:
    print("hej .)")
    
