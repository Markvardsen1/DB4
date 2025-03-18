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
            
            print("Starting fan test..")
            
            time.sleep(1)
            for i in range(3):
                
                print("turning fan on")
                time.sleep(0.3)
                self.startFan()
                time.sleep(2)
                print("turning fan off")
                time.sleep(0.3)
                self.stopFan()
                time.sleep(2)



        