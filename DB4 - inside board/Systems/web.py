import os
import sys
import time

import network
from runONLINE import cb
from umqtt.robust import MQTTClient


def subscribeToServer(ADAFRUIT_USERNAME, ADAFRUIT_IO_FEEDNAME, client):
            
    mqtt_feedname = bytes('{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, ADAFRUIT_IO_FEEDNAME), 'utf-8')
    client.set_callback(cb)
    client.subscribe(mqtt_feedname) 

    mqtt_feedname_get = bytes('{:s}/get'.format(mqtt_feedname), 'utf-8')
    client.publish(mqtt_feedname_get, '\0')
        
        
    try:
            client.check_msg() #TODO: maybe we have to do wait.msg instead... also code is different when using "check" vs "wait"
    
    except Exception:
            raise ConnectionError
        