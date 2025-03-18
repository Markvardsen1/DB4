import time

import machine


class Cooler:
    
    def __init__(self, coolingPin):
        self.coolingPin = machine.Pin(coolingPin, machine.Pin.OUT)
        
    def highCooling(self) -> None:
        self.coolingPin.value(0)
        
    def lowCooling(self) -> None:
        self.coolingPin.value(1)

    def testCooler(self):
        
        print("Starting cooler test.. LISTEN FOR THE CLICK!!!!")
        time.sleep(3)
        for i in range(3):
            
            print("turning cooler on") # YES ITS A 0, ITS FLIPPED
            self.coolingPin.value(0)
            time.sleep(3)
            
            print("turning cooler off") # YES ITS A 1, ITS FLIPPED
            self.coolingPin.value(1)
            time.sleep(3)



        