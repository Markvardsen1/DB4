<<<<<<< HEAD


from Systems.components import *

data = {
                "temp": 5,
                "od": 6,
                }

wifiConnecter.connectToWifi()
adafruitIOClient.connectToAdafruitIO()
dataPublisher.publishOnline(data)

=======
import gc
import os
import sys
import time

import network
from Systems import components, constants
from umqtt.robust import MQTTClient


while True:
    
    print("am i here?")
    try:
        client.publish(mqtt_feedname,
                bytes(str("COCK"), 'utf-8'),
                qos=0)
        
        time.sleep(PUBLISH_PERIOD_IN_SEC)
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        client.disconnect()
        sys.exit()
>>>>>>> ba198947ef0e347ee4d5b5b01c7c07ce979e0164
