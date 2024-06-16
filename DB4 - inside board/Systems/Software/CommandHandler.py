import time

import machine
from components import *


def handleCommand(msg):

    if msg.startswith("cooler("):
        content_str = (msg[len("cooler("):-1])

        
        if content_str == "on":
            cooler.start()
            
        elif content_str == "off":
            cooler.stop()
        
        #if msg.startswith("pump("): #TODO names in this functions are wrong
        #    content_int = int ( (msg[len("pump("):-1]))

        #    if content_int <= 100 and content_int >= 0:
        #        StepperMotor.setSpeed(content_int)
        #    else:
        #        OLEDScreen.displayData("Input needs to be: 0 to 100")
                
        #if msg.startswith("led("):
        #    content_int = int ( (msg[len("led("):-1]))

        #    if content_int <= 100 and content_int >= 0:
        #        LED.setLight(content_int)
        #    else:
        #        OLEDScreen.displayData("Input needs to be: 0 to 100")
        
        
    if msg.startswith("open"):
        content_str = (msg[len("open("):-1])

        #match content_str:
            #case "MW": StepperMotor.turnOnMW #TODO these functions need to be made
            #case "CW": StepperMotor.turnOnCW #TODO these functions need to be made
    
    if msg.startswith("oled("):
        content_str = (msg[len("open("):-1])
        oledScreen.displayTemporary(content_str)