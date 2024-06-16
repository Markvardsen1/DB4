from Software import (AdafruitIOClient, DataPublisher, OfflineClient,
                      WifiConnecter)

#variables to change:
WIFI_SSID         = "dsfasGg"
WIFI_PASSWORD     = "bahamondes"

ADAFRUIT_USERNAME = "felimondes"
ADAFRUIT_IO_KEY   = ""


DATAFILE = 'data.txt'
PATH_TO_DATAFILE_FOLDER = r"C:\Users\User\Desktop\DB4\DB4\DB4 - inside board\Systems" + "\\" + DATAFILE


LIST_OF_FEEDS = [
                        "Temperature",
                        
                        
                        
                        ]


COMMAND_FEED = "SKRIV COMMANDS HER :D"


wifiConnecter = WifiConnecter()
adafruitIOClient = AdafruitIOClient()
offlineClient = OfflineClient()
dataPublisher = DataPublisher(adafruitIOClient, offlineClient)
