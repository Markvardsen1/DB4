
from Systems.components import *
from Systems.Hardware import *
from Systems.Software import *

#variables to change:
WIFI_SSID         = "dsfasGg"
WIFI_PASSWORD     = "bahamondes"

ADAFRUIT_USERNAME = "felimondes"
ADAFRUIT_IO_KEY   = ""


dataFile = 'data.txt'
pathToDataFileFolder = r"C:\Users\User\Desktop\DB4\DB4\DB4 - inside board\Systems" + "\\" + dataFile



listOfFeeds = [
                        "Temperature",
                        
                        
                        
                        ]


commandFeed = "SKRIV COMMANDS HER :D"

wifiConnecter = WifiConnecter()
adafruitIOClient = AdafruitIOClient()
offlineClient = OfflineClient()
dataPublisher = DataPublisher(adafruitIOClient, offlineClient)


def main():
    muscleFarmRunner = MuscleFarmRunner()

    try:
        wifiConnecter.connectToWifi()
        adafruitIOClient.connectToAdafruitIO()
        
        if offlineClient.doesDataExist():
            dataPublisher.importOfflineDataToOnline()
        
        muscleFarmRunner.onlineMode()
        
        
    except ConnectionError:
        
        muscleFarmRunner.offlineMode()
        
        