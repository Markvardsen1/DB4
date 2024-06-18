import time

from Systems.components import *
from Systems.constants import *


class MuscleFarmRunner:
    
    
    def __init__(self):
        self.timeSinceLastPublish = time.time()
        self.currentMode = None
    
    
    def getData(self) -> dict:
        
        data = {
                "temp": temperatureSensor.getTemperature(),
                "od": odSensor.getOD(),
                "Mode": self.currentMode
                }
        
        return data
        
                
    
    def isTimeToNextPublish(self):
                difference = time.time() - self.timeSinceLastPublish
                return difference > 30
    
    def onlineMode(self):

        self.currentMode = "Online"
        
        if offlineClient.doesDataExist():
                oledScreen.displayMessage("COMMANED NEEDED! Do you want to save or erase datafile?")
                adafruitIOClient.waitCommand()
                
        while True:
            pidTemperatureController.adjust()
            pidODController.adjust()
            
            adafruitIOClient.checkCommand() #TODO what happens if no new message has been sent??? does it do the command twice?
            
            if self.isTimeToNextPublish():
                
                data=self.getData()
                dataPublisher.publishOnline(data)
                
                self.timeSinceLastPublish = time.time()
                oledScreen.displayData(data)
    
    
    def offlineMode(self):
        
        
        self.currentMode = "Online"
    
        oledScreen.displayMessage("CONNECTION LOST, running OFFLINE MODE")
        
        while True:
            #Get measurements
            temperature = temperatureSensor.getTemperature()
            
            #PID controllers #TODO
            pidTemperatureController.adjust()
            pidODController.adjust()
        
            if self.isTimeToNextPublish():
                
                data = self.getData()
                
                dataPublisher.publishOffline(data)
                oledScreen.displayData(data)
                
                try:
                    wifiConnecter.connectToWifi()
                    adafruitIOClient.connectToAdafruitIO()
                    self.onlineMode()
                
                except ConnectionError:
                    self.offlineMode()

    