import time
from machine import ADC, Pin

#TODO VALTYR KOMMER MED NYY

class ODSensor:
    
    OPTIMAL_DAC = 232
    
    def __init__(self):
        pin = machine.Pin(25)

        self.dac = DAC(pin, bits=8)
        self.dac.write(self.optimal_DAC)

        self.adc = ADC(pin)
        self.adc.atten(ADC.ATTN_11DB)
        
    def getOD(self):
        return self.adc.read()

    def start(self):
        self.dac.write(self.optimal_DAC)
    
    def stop(self):
        self.dac.write(0)
    
    


    

