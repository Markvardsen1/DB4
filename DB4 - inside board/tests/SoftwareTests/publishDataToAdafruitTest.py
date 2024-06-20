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