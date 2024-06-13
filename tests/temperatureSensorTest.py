
import time

from DB4.ElectronicsGuide.electronicsAndPID.TemperatureSensor import \
    TemperatureSensor

#OBJECTS TO USE:
#temp sensor
temp_pin = 25
FixedResistor = 10000
temperatureSensor= TemperatureSensor(temp_pin, FixedResistor)


while True:
    time.sleep(1)
    print(temperatureSensor.getTemperature())
    
    
    
    


