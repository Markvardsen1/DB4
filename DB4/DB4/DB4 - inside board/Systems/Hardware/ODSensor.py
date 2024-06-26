import time

from machine import ADC, DAC, Pin
from Systems import components


class ODSensor:
    
    OPTIMAL_DAC = 232
    maxValue = 4095
    
    def __init__(self, pin):
        pin = Pin(pin)
        # self.dac = DAC(pin, bits=8)
        self.adc = ADC(pin)
        self.adc.atten(ADC.ATTN_11DB)
        
    def getOD(self):
        components.ledStrip.stop()

        time.sleep(1.5)
        val =  self.adc.read()
        time.sleep(1.5)

        components.ledStrip.start()
        return val


    # def start(self):
    #     self.dac.write(self.OPTIMAL_DAC)
    
    # def stop(self):
    #     self.dac.write(0)

        
    def testODSensor(self):
        print("running test  OD sensor")
        for i in range(10):
            print(self.getOD())
            time.sleep(1)
        print("Test is done")

    def mappingODSensorToPercentage(self, value): 
        map = value * (100 / 4095)
        return map
    
    


    

