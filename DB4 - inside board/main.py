from Systems.components import *

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


commandFeed = "Command feed"




def main():
    
    
    muscleFarmRunner = MuscleFarmRunner()
    

    try:
        wifiConnecter.connectToWifi(WIFI_SSID, WIFI_PASSWORD)
        adafruitIOClient.connectToAdafruitIO()
        
        
        if offlineClient.doesDataExist():
            dataPublisher.importOfflineDataToOnline()
        
        muscleFarmRunner.onlineMode()
        
        

    except ConnectionError:
        
        muscleFarmRunner.onlineMode()
        
        