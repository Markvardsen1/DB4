import time
import machine


def handleCommand(msg):
    
    command = msg.decode("utf-8") 
    print(command)
    print(type(command))
    from Systems.components import (cooler, dataPublisher, fan, foodPump,
                                    ledStrip, offlineClient, oledScreen,
                                    valveSwitch)

    if command.startswith("cooler("):
        content_str = (command[len("cooler("):-1])

        if content_str == "on":
            cooler.start()
            
        elif content_str == "off":
            cooler.stop()
    
    if command.startswith("fan("):
        content_str = (command[len("fan("):-1])

        if content_str == "on":
            print("starting fan")
            fan.startFan()
            
        elif content_str == "off":
            fan.stopFan()

    if command.startswith("pump("):
        content_str = (command[len("pump("):-1])
        foodPump.setSpeedPercentage(int(content_str))
        

    if command.startswith("led("):
        content_str = (command[len("led("):-1])
        ledStrip.setSpeedPercentage(int(content_str))


    if command.startswith("switch("):
        content_str = (command[len("cooler("):-1])

        if content_str == "on":
            valveSwitch.ON()
            
        elif content_str == "off":
            valveSwitch.OFF()
            
    if command.startswith("oled("):
        content_str = (command[len("oled"):-1])
        oledScreen.displayMessage(content_str)