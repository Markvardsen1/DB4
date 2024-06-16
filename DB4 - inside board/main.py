import time

from Systems.components import *
from Systems.runOFFLINE import runOFFLINE
from Systems.runONLINE import runONLINE

#variables to change:
WIFI_SSID         = "dsfasGg"
WIFI_PASSWORD     = "bahamondes"

ADAFRUIT_USERNAME = "felimondes"
ADAFRUIT_IO_KEY   = ""

filePathToFolder = r'C:\Users\User\Desktop\DB4\DB4\Systems\data'
dataFile = 'data.txt'

listOfFeeds = [
                        "Temperature",
                        
                        
                        
                        ]

commandFeed = "Command feed"




def main():
    
    try:
        wifiConnecter.connectToWifi(WIFI_SSID, WIFI_PASSWORD)
        adafruitIOClient.connectToAdafruitIO()
        runONLINE()
        
        
    except ConnectionError:
        runOFFLINE()
        
        