import time

import machine


def handleCommand(msg):

    from Systems.components import (cooler, dataPublisher, fan, largeDCMotor,
                                    ledStrip, offlineClient, oledScreen,
                                    valveSwitch)

    if msg == "ERASE":
        offlineClient.deleteFile()
        oledScreen.displayMessage("ERASING :D")

    if msg == "PUBLISH":
        dataPublisher.importOfflineDataToOnline()
        oledScreen.displayMessage("Publishing :D")
        

    if msg.startswith("cooler("):
        content_str = (msg[len("cooler("):-1])

        if content_str == "on":
            cooler.start()
            
        elif content_str == "off":
            cooler.stop()
    
    if msg.startswith("fan("):
        content_str = (msg[len("fan("):-1])

        if content_str == "on":
            fan.startFan()
            
        elif content_str == "off":
            fan.stopFan()

    if msg.startswith("pump("):
        content_str = (msg[len("pump("):-1])
        largeDCMotor.setSpeedPercentage(int(content_str))
        

    if msg.startswith("led("):
        content_str = (msg[len("led("):-1])
        ledStrip.setSpeedPercentage(int(content_str))


    if msg.startswith("switch("):
        content_str = (msg[len("cooler("):-1])

        if content_str == "on":
            valveSwitch.ON()
            
        elif content_str == "off":
            valveSwitch.OFF()

        
    

