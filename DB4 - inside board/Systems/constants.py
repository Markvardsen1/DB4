from Systems.Software.AdafruitIOClient import AdafruitIOClient
from Systems.Software.DataPublisher import DataPublisher
from Systems.Software.OfflineClient import OfflineClient
from Systems.Software.WifiConnecter import WifiConnecter

#variables to change:
WIFI_SSID         = "dsfasGg"
WIFI_PASSWORD     = "bahamondes"

ADAFRUIT_USERNAME = "felimondes"
ADAFRUIT_IO_KEY   = ""


DATAFILE = 'data.txt'
PATH_TO_DATAFILE_FOLDER = r"C:\Users\User\Desktop\DB4\DB4\DB4 - inside board" + "\\" + DATAFILE



listOfDataFeeds = [
                        "temp",
                        "od",
                        ]

commandFeed = "SKRIV COMMANDS HER :D"

secBetweenPublishes = len(listOfDataFeeds)*10


