import machine 
import time
import numpy as np

class Temperature:
    
    def __init__(self, pin, FixedResistor):
        self.pin = pin
        self.FixedResistor = FixedResistor
        self.adc = machine.ADC(machine.Pin(self.pin))
        self.adc.atten(machine.ADC.ATTN_11DB)
        
    def read(self):
        return self.adc.read()
        
    def get_resistance(self):
        return self.FixedResistor * (1023 / self.read() - 1)

