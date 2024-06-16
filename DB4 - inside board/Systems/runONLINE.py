import time

from Systems.components import *

timeSinecLastPublish = time.time()

def runONLINE():

    
    while True:
        
        #Get measurements
        temperature = temperatureSensor.getTemperature()

        #PID controllers #TODO
        
        #Check if any new command has been sent
        adafruitIOClient.checkCommand()
        
        
        
        
        
        if isTimeToPublish():
            #publishing data
            
            data = {
                "temp": temperature
    
                }
            
            dataPublisher.publishOnline(data)
            
            
            
        
        
        #displaying stuff on OLED
        #TODO make some nice OLED if time.
        #algaeConcentration = calculateAlageConcentration(light, dimensionsOfTube) #TODO talk to others how this can be calculated. 
        #foodFlow = calculateFoodFlow(pumpFrequency, pumpDutyCyle, algaeConcentration) #TODO this would be nice to have


def isTimeToPublish():
    
    difference = time.time() - timeSinecLastPublish
    
    return difference > 30


