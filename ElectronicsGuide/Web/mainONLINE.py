from mainNEW import *


def run(client_ONLINE):

    def cb(topic, msg):
        
            if msg.startswith("set.dtemp("):
                content_str = msg[len("set.dtemp("):-1]
                temperaturePID.setDesiredValue(int(content_str))
                
            if msg.startswith("set.dOD("):
                content_str = msg[len("set.dOD("):-1]
                odPID.setDesiredValue(int(content_str))
                
            if msg.startswith("test("):
                content_str = msg[len("funni("):-1]
                OLEDScreen.display(content_str)

    iter = 0
    while True:
            
        temperature = tempSensor.getTemperature()
        OD = ODSensor.getOD()
        
        #PID controllers #TODO
        
        #Subscribing
        web.subscribeToServer(ADAFRUIT_USERNAME, "InputFeed", client_ONLINE) #this calls the cb function above

        if iter == 200: #TODO Make iter large enough, so that it wont break the ping limit.
            
            #publishing data
            web.publish(temperature,ADAFRUIT_USERNAME,"tempTracker", client_ONLINE)
            web.publish(OD,ADAFRUIT_USERNAME,"odTracker", client_ONLINE)
            
            
            #displaying stuff on OLED
            #TODO make some nice OLED if time.
            #algaeConcentration = calculateAlageConcentration(light, dimensionsOfTube) #TODO talk to others how this can be calculated. 
            #foodFlow = calculateFoodFlow(pumpFrequency, pumpDutyCyle, algaeConcentration) #TODO this would be nice to have


        iter+=1