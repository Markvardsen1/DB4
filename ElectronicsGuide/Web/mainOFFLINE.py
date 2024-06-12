import writeToFile
from mainNEW import *


def run():

    iter = 0
    while True:
            
        temperature = tempSensor.getTemperature()
        light = lightSensor.getLightIntensity()
        
        #PID controllers #TODO

        if iter == 200: #TODO Make iter large enough, so that it wont break the ping limit.
            
            #publishing data
            data = {
                "temp": temperature,
                "od": light
                }
            
            writeToFile._(data)
                        
            #displaying stuff on OLED
            
            #TODO make some nice OLED if time.
            algaeConcentration = calculateAlageConcentration(light, dimensionsOfTube) #TODO talk to others how this can be calculated. 
            foodFlow = calculateFoodFlow(pumpFrequency, pumpDutyCyle, algaeConcentration) #TODO this would be nice to have

        iter+=1