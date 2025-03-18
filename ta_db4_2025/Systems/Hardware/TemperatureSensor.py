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
        
        if not(self.getResistance() == 0):
            # print("temperature sensor works")
            for _ in range(10):
                try:
                    temp = 1 / (1 / 298.15 + 1 / 3950 * math.log(abs(self.getResistance()) / 10000)) - 298.15 + 3.1 #OBS: CALIBRATE HERE
                    if 10 < temp < 40:
                        return temp 
                except Exception as e:
                    print(e)
        else:
            print("temperature sensor doesent work fix")
            return 0


    def getMedianTemperature(self):
        sampleSize = 31
        templist = [None] * sampleSize
        for i in range(sampleSize):
            templist[i] = self.getTemperature()
        templist.sort()
        return templist[int((sampleSize - 1) / 2)]
        
        
    def stop(self):
        self.adc.atten(machine.ADC.ATTN_0DB)
        
    def start(self):
        self.adc.atten(machine.ADC.ATTN_11DB)
        
    def testTempeartureSensor(self):
        print("running test temperature")
        for i in range(5):
            print(self.getMedianTemperature())
            time.sleep(1)
        print("Test is done")
    


