
import time

import machine
from Systems import components

print("hej")

components.ledStrip.start()
components.ledStrip.setLight(512)


time.sleep(2)
components.ledStrip.testMaxLight()
components.ledStrip.testMinAndMaxDuty()



    
