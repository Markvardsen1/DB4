import time

from Systems.components import *
from Systems.electronicsAndPID import *
from Systems.runOFFLINE import *


class OfflineClient:
    
    
    def __init__(self):
        self.timeSinceLastPublish = time.time()
    
    
    def runOFFLINE(self):

        
        while True:
            
            #Get measurements
            temperature = temperatureSensor.getTemperature()
            
            #PID controllers #TODO
            
            if self.ïsTimeToDoActions():
                data = {
                        "temp": temperature
                    }
                    
                dataPublisher.publishOffline(data)
                
                oledScreen.displayData(data)
                
                try:
                    wifiConnecter.connectToWifi()
                    adafruitIOClient.connectToAdafruitIO()
            
                    if offlineClient.doesDataExist():
                        dataPublisher.importOfflineDataToOnline()
                        OnlineClient.run()

                except ConnectionError:
                    runOFFLINE.run()

    def ïsTimeToDoActions(self):
                difference = time.time() - self.timeSinceLastPublish
                return difference > 30