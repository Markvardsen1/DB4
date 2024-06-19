import time

from Systems import components
from Systems.constants import secBetweenPublishes


class MuscleFarmRunner:
    
    
    def __init__(self):
        self.timeSinceLastPublish = time.time()
        
        self.currentMode = None
        self.data = None
        self.oledDisplay = None
    
    
    def makeOledDisplay(self) -> dict:
        self.oledDisplay = {
                "mode": self.currentMode
                }
        
        return self.oledDisplay.update(self.data)
        
        
        
    def takeData(self) -> dict:
        self.data = {
                "temp": components.temperatureSensor.getTemperature(),
                "od": components.odSensor.getOD(),
                }
        
    def isTimeToNextPublish(self):
                difference = time.time() - self.timeSinceLastPublish
                return difference > secBetweenPublishes
    
    

    def onlineMode(self):
        self.currentMode = "Online"
        
        if components.offlineClient.doesDataExist():
                components.oledScreen.displayMessage("COMMANED NEEDED! Do you want to save or erase datafile?")
                components.adafruitIOClient.waitCommand()
                
        while True:
            #pidTemperatureController.adjust()
            #pidODController.adjust()
            
            components.adafruitIOClient.checkCommand() #TODO what happens if no new message has been sent??? does it do the command twice?
            
            if self.isTimeToNextPublish():
                self.takeData()
                components.dataPublisher.publishOnline(self.data)
                
                oledDisplay = self.getOledDisplay()
                components.oledScreen.displayData(oledDisplay)
                
                self.timeSinceLastPublish = time.time()


    def offlineMode(self):
        self.currentMode = "Online"
        components.oledScreen.displayMessage("CONNECTION LOST, running OFFLINE MODE")
        
        while True:
            
            #PID controllers #TODO
            #pidTemperatureController.adjust()
            #pidODController.adjust()
        
            if self.isTimeToNextPublish():
                
                data = self.takeData()
                
                components.dataPublisher.publishOffline(data)
                components.oledScreen.displayData(data)
                
                try:
                    components.wifiConnecter.connectToWifi()
                    components.adafruitIOClient.connectToAdafruitIO()
                    self.onlineMode()
                
                except ConnectionError:
                    self.offlineMode()

    