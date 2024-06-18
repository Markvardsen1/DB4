import time

import machine


class ValveSwitch:

        def __init__(self, step_pin_number: int, dir_pin_number : int):
                
                self.step_pin = machine.Pin(step_pin_number, machine.Pin.OUT)
                self.dir_pin = machine.Pin(dir_pin_number, machine.Pin.OUT)
                
                
                        
        def switch(self, direction):
                
                if direction == 1:
                        self.dir_pin(1)
                else:
                        self.dir_pin(0)
                        
                self.doSteps(50) #90 degrees
        
        def doSteps(self, totalSteps):
                
                stepsLeft= totalSteps
                while stepsLeft > 0:
                        self.step_pin(1)
                        self.step_pin(0)
                        time.sleep(0.01)
                        stepsLeft -= 1
                        
        def switchTest(self):
                print("running switch test..")
                time.sleep(3)
                
                for i in range(5):
                        print("switching off")
                        self.switch(0)
                        
                        time.sleep(3)
                        
                        print("switching on")
                        self.switch(1)
                
                
                        
                        
                        
                
                
                
                
        