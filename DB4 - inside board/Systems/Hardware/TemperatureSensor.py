import math
import time

import machine


class TemperatureSensor:
    
    def __init__(self, pin):
        self.pin = pin
        self.FixedResistor = 10000
        self.adc = machine.ADC(machine.Pin(self.pin))
        self.adc.atten(machine.ADC.ATTN_11DB)
        
    def readADC(self):
        return self.adc.read()
        
    def getResistance(self):
        return self.FixedResistor * (1023 / self.readADC() - 1)

    def getTemperature(self):
        return 1 / (1 / 298.15 + 1 / 3950 * math.log(abs(self.getResistance()) / 10000)) - 298.15 #OBS: CALIBRATE HERE


    def stop(self):
        self.adc.atten(machine.ADC.ATTN_0DB)
        
    def start(self):
        self.adc.atten(machine.ADC.ATTN_11DB)
        
    def testTempeartureSensor(self):
        print("running test temperature")
        for i in range(10):
            print(self.getTemperature())
            time.sleep(1)
        print("Test is done")
    


