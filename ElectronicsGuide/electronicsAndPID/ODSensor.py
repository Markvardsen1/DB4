import time

from machine import ADC, Pin

#TODO VALTYR KOMMER MED NYY

class ODSensor:
    
    
    def __init__(self, pinNumber):
        self.adc = ADC(Pin(pinNumber))
        self.adc.atten(ADC.ATTN_11DB)
        
    def getOD(self):
        return self.adc.read()
    
    
    

