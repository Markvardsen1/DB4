import time

import machine

class Cooler:
    
    def __init__(self, cooling_pin):
        self.cooling_pin = machine.Pin(cooling_pin, machine.Pin.OUT)
        
    def twevleVCooling(self) -> None:
        self.cooling_pin.value(1)
        
    def fiveVCooling(self) -> None:
        self.cooling_pin.value(0)

    def stop(self) -> None:
        self.fiveVCooling()
        
    def start(self) -> None:
        self.twevleVCooling()
