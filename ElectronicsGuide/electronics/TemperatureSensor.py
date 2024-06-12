import math
import time

import machine


class Temperature:
    
    def __init__(self, pin, FixedResistor):
        self.pin = pin
        self.FixedResistor = FixedResistor
        self.adc = machine.ADC(machine.Pin(self.pin))
        self.adc.atten(machine.ADC.ATTN_11DB)
        
    def read(self):
        return self.adc.read()
        
    def getResistance(self):
        return self.FixedResistor * (1023 / self.read() - 1)

    def getTemperature(self):
        return 1 / (1 / 298.15 + 1 / 3950 * math.log(abs(self.get_resistance()) / 10000)) - 298.15 #OBS: CALIBRATE HERE




