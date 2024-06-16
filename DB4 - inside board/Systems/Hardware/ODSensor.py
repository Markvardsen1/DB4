import time

from machine import ADC, DAC, Pin


class ODSensor:
    

    #TODO test if this works
    OPTIMAL_DAC = 232
    
    def __init__(self, pin):
        pin = Pin(pin)
        self.dac = DAC(pin, bits=8)
        self.adc = ADC(pin)
        self.adc.atten(ADC.ATTN_11DB)
        
    def getOD(self):
        return self.adc.read()

    def start(self):
        self.dac.write(self.OPTIMAL_DAC)
    
    def stop(self):
        self.dac.write(0)
        
    def testODSensor(self):
        print("running test  OD sensor")
        for i in range(10):
            print(self.getOD())
            time.sleep(1)
        print("Test is done")
    
    


    

