import machine 
import time
import math

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

    def get_temperature(self):
        return 1 / (1 / 298.15 + 1 / 3950 * math.log(abs(self.get_resistance()) / 10000)) - 298.15
        
# pin = 25
# FixedResistor = 10000
# temp = Temperature(pin, FixedResistor)
# while True:
#     print(temp.read())
 #    print(temp.get_resistance())
 #    print("temperature: " + str(temp.get_temperature()) + " c")
  #   time.sleep(1)


