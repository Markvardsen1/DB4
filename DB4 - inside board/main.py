import time

from Systems.runOFFLINE import *
from Systems.runONLINE import *

#variables to change:

WIFI_SSID         = "dsfasGg"
WIFI_PASSWORD     = "bahamondes"

ADAFRUIT_USERNAME = "felimondes"
ADAFRUIT_IO_KEY   = ""

filePathToData = r'C:\Users\User\Desktop\DB4\DB4\Systems\data'


listOfFeeds = [
                        "temp",
                        
                        
                        
                        ]

def main():
    
    try:
        web.connectToWifi(WIFI_SSID, WIFI_PASSWORD)
        client = web.connectToServer(ADAFRUIT_USERNAME, ADAFRUIT_IO_KEY) #Uncertain if this can work
        runONLINE.run(client)
        
    except ConnectionError:
        runOFFLINE.run()
        
        