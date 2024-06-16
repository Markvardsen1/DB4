import time

import machine


class Fan:
    
    def __init__(self, fanPin):
        self.fanPin = machine.Pin(fanPin, machine.Pin.OUT)
        
    def startFan(self):
        self.fanPin.value(1)
        
    def stopFan(self):
        self.fanPin.value(0)

    def testFan(self):
        print("turning fan on")
        time.sleep(3)
        self.fanPin.value(1)
        time.sleep(10)
        print("turning fan off")
        self.fanPin.value(0)



        