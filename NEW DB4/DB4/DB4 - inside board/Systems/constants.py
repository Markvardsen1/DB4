from Systems.Software.AdafruitIOClient import AdafruitIOClient
from Systems.Software.DataPublisher import *
from Systems.Software.OfflineClient import *
from Systems.Software.WifiConnecter import *

#variables to change:
WIFI_SSID         = "dsfasGg"
WIFI_PASSWORD     = "bahamondes"

ADAFRUIT_USERNAME = "felimondes"
ADAFRUIT_IO_KEY   = ""


DATAFILE = 'data.txt'
PATH_TO_DATAFILE_FOLDER = r"C:\Users\felim\OneDrive\Skrivebord\DB4\DB4\DB4 - inside board"



listOfDataFeeds = [
                        "temp",
                        "od",
                        "pump"
                        "pump1"
                        ]

commandFeed = "commands"

secBetweenPublishes = 30

