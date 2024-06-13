import time

from machine import ADC, Pin

#TODO VALTYR KOMMER MED NYY

class ODSensor:
    
    def __init__(self):
        optimal_DAC = 232
        pin = machine.Pin(25)

        self.dac = DAC(pin, bits=8)
        self.dac.write(optimal_DAC)

        self.adc = ADC(pin)
        self.adc.atten(ADC.ATTN_11DB)
        
    def getOD(self):
        return self.adc.read()


    

