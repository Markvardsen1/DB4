def runONLINE(client_ONLINE):

    def callBack(topic, msg):

            msg = msg.lower()
            
            if msg.startswith("cooler("):
                content_str = (msg[len("cooler("):-1])

                match content_str:
                    case "on": cooler.start()
                    case "off": cooler.stop()
            
            #if msg.startswith("pump("): #TODO names in this functions are wrong
            #    content_int = int ( (msg[len("pump("):-1]))

            #    if content_int <= 100 and content_int >= 0:
            #        StepperMotor.setSpeed(content_int)
            #    else:
            #        OLEDScreen.display("Input needs to be: 0 to 100")
                    
            #if msg.startswith("led("):
            #    content_int = int ( (msg[len("led("):-1]))

            #    if content_int <= 100 and content_int >= 0:
            #        LED.setLight(content_int)
            #    else:
            #        OLEDScreen.display("Input needs to be: 0 to 100")
            
            
            if msg.startswith("open"):
                content_str = (msg[len("open("):-1])

                #match content_str:
                    #case "MW": StepperMotor.turnOnMW #TODO these functions need to be made
                    #case "CW": StepperMotor.turnOnCW #TODO these functions need to be made
            
            if msg.startswith("oled("):
                content_str = (msg[len("open("):-1])
                oledScreen.displayTemporary(content_str)
                
            
    iter = 0
    while True: 
        temperature = temperatureSensor.getTemperature()
        OD = odSensor.getOD()
        #voltageLED = led.getVoltage #TODO 
        
        #PID controllers #TODO
        
        #Subscribing
        web.subscribeToServer(ADAFRUIT_USERNAME, "InputFeed", client_ONLINE) #this calls the callBack function above

        if iter == 200: #TODO Make iter large enough, so that it wont break the ping limit.
            
            #publishing data
            web.publish(temperature,ADAFRUIT_USERNAME,"tempTracker", client_ONLINE)
            web.publish(OD,ADAFRUIT_USERNAME,"odTracker", client_ONLINE)
            
            
            #displaying stuff on OLED
            #TODO make some nice OLED if time.
            #algaeConcentration = calculateAlageConcentration(light, dimensionsOfTube) #TODO talk to others how this can be calculated. 
            #foodFlow = calculateFoodFlow(pumpFrequency, pumpDutyCyle, algaeConcentration) #TODO this would be nice to have


        iter+=1