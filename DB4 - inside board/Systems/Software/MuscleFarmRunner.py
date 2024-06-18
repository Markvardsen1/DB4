import time

from Systems.components import *
from Systems.constants import *


class MuscleFarmRunner:
    
    
    def __init__(self):
        self.timeSinceLastPublish = time.time()
    
    
    def isTimeToDoActions(self):
                difference = time.time() - self.timeSinceLastPublish
                return difference > 30
    
    def onlineMode(self):

        if offlineClient.doesDataExist():
                oledScreen.displayMessage("COMMANED NEEDED! Do you want to save or errase datafile?")
                adafruitIOClient.waitCommand()
                


        while True:
            
            temperature = temperatureSensor.getTemperature()
            od = odSensor.getOD()

            #PID controllers #TODO
            
            adafruitIOClient.checkCommand()
            
            if self.isTimeToDoActions():
                data = {
                    "temp": temperature,
                    "od": od,
                    "Mode": "online"
                    }
                
                dataPublisher.publishOnline(data)
                self.timeSinceLastPublish = time.time()
                
                oledScreen.displayData(data)
    
    
    def offlineMode(self):

        
        while True:
            
            #Get measurements
            temperature = temperatureSensor.getTemperature()
            
            #PID controllers #TODO
            
            if self.isTimeToDoActions():
                data = {
                        "temp": temperature
                    }
                    
                dataPublisher.publishOffline(data)
                
                oledScreen.displayData(data)
                
                try:
                    wifiConnecter.connectToWifi()
                    adafruitIOClient.connectToAdafruitIO()
                    self.onlineMode()
                
                except ConnectionError:
                    self.offlineMode()

    