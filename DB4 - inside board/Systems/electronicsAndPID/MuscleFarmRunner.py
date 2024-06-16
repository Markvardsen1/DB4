import time

from Systems.components import *
from Systems.electronicsAndPID import *
from Systems.runOFFLINE import *


class MuscleFarmRunner:
    
    
    def __init__(self):
        self.timeSinceLastPublish = time.time()
    
    
    def isTimeToDoActions(self):
                difference = time.time() - self.timeSinceLastPublish
                return difference > 30
    
    def onlineMode(self):

        while True:
            
            temperature = temperatureSensor.getTemperature()

            #PID controllers #TODO
            
            adafruitIOClient.checkCommand()
            
            if self.isTimeToDoActions():
                data = {
                    "temp": temperature
                    }
                
                dataPublisher.publishOnline(data)
                self.timeSinceLastPublish = time.time()
                
                oledScreen.displayData(data)
    def offlineMode(self):

        
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
                        self.onlineMode()

                except ConnectionError:
                    self.offlineMode()

    