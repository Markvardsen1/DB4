import time

import machine


class Fan:
    
    def __init__(self, fanPin):
        self.fanPin = machine.Pin(fanPin, machine.Pin.OUT)
        
    def startFan(self):
        self.fanPin.value(1)
        
    def stopFan(self):
        self.fanPin.value(0)



        