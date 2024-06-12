import time

import machine

cooling_pin = machine.Pin(12, machine.Pin.OUT)

class Cooler:
    
    def __init__(self, cooling_pin):
        self.cooling_pin = machine.Pin(cooling_pin, machine.Pin.OUT)
        
    def twevleVCooling(self) -> None:
        self.cooling_pin.value(1)
        
    def fiveVCooling(self) -> None:
        self.cooling_pin.value(0)
        
    # def cooling(self):
    #     self.startCooling()
    #     time.sleep(5)
    #     self.stopCooling()
    #     time.sleep(5)


# while True:
#     cooling_pin.value(1)
#     time.sleep(5)
#     cooling_pin.value(0)
#     time.sleep(5)