

import time
<<<<<<< HEAD

import machine
from Systems import components

while True:
    
    data = {
                "temp": components.temperatureSensor.getTemperature(),
                "od": components.odSensor.getOD(),
                }
    
    components.wifiConnecter.connectToWifi()
    components.adafruitIOClient.connectToAdafruitIO()
    components.dataPublisher.publishOnline(data)
    
    time.sleep(20)
=======
import machine
from Systems import components


components.largeDCMotor.start()
components.largeDCMotor.currentDutyCycle(1023)
    
    
>>>>>>> ba198947ef0e347ee4d5b5b01c7c07ce979e0164
    



