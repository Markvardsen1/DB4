import time

from Systems.electronicsAndPID import *
from Systems.runOFFLINE import *
from Systems.runONLINE import *


def runOFFLINE():

    iter = 0
    while True:
        
        
        temperature = components.temperatureSensor.getTemperature()
        OD = components.odSensor.getOD()
        #voltageLED = led.getVoltage #TODO
        #PID controllers #TODO

        if iter == 200: #TODO Make iter large enough, so that it wont break the ping limit.
            
            #publishing data
            
            data = {
                "temp": temperature
                #"od": OD
                #TODO add voltage of LED
                }
            
            writeToFile(data)
                        
            #displaying stuff on OLED
            oledScreen.display(data)
            
            
            try:
                web.connectToWifi(WIFI_SSID, WIFI_PASSWORD)
                client_OFFLINE = web.connectToServer(ADAFRUIT_USERNAME, ADAFRUIT_IO_KEY)
                publishFileToAdafruitIO(client_OFFLINE) #TODO this one does not work, "file is being used elsewhere"
                runONLINE.run(client_OFFLINE)
    
            except ConnectionError:
                runOFFLINE.run()

        iter+=1