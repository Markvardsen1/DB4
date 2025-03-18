import time
import machine 

from Systems import components
from Systems.constants import secBetweenPublishes
from Systems.Hardware import *
from Systems.Software import *


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
        

    
    def onlineMode(self):
        self.currentMode = "Online"
        
                
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
                
                except ZeroDivisionError:
                    self.offlineMode()



    def startMuscleFarm(self):
        components.fan.startFan()
        components.cooler.highCooling()
        components.foodPump.start()
            
    def setLargeDCMotorForAlgae(self, ODValue):
        percentage = components.odSensor.mappingODSensorToPercentage(ODValue)
        components.foodPump.setSpeedPercentage(percentage)
