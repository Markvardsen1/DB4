import time

import machine


class ValveSwitch:

<<<<<<< HEAD
        def __init__(self, step_pin_number: int, dir_pin_number : int):
                
                self.step_pin = machine.Pin(step_pin_number, machine.Pin.OUT)
                self.dir_pin = machine.Pin(dir_pin_number, machine.Pin.OUT)
                
=======
        def __init__(self, step_pin_number: int, dir_pin_number : int, enable_pin_number ):
                
                self.step_pin = machine.Pin(step_pin_number, machine.Pin.OUT)
                self.dir_pin = machine.Pin(dir_pin_number, machine.Pin.OUT)
                self.enable_pin = machine.Pin(enable_pin_number, machine.Pin.OUT)
>>>>>>> ba198947ef0e347ee4d5b5b01c7c07ce979e0164
                self.place = 0
                
                self.pwm = machine.PWM(self.enable_pin)
        
        
        def stop(self):
                self.enable_pin.value(1)  # Set the enable pin high to disable the motor

        def start(self):
                self.enable_pin.value(0)  
                self.pwm.freq(1000)
                self.pwm.duty(1023)

                
                        
        def switch(self): # this is a solution in order to switch the valves without checking the direction... WORKS 
                
                if self.place == 0:
                        self.doSteps(50) #90 degrees
                        self.place = 1
                        
                        print("Left turn")
                        
                elif self.place == 1:
                        self.doSteps(150) #270 degrees
                        self.place = 0
                        print("Right turn")
                else:
                        print("Not valid place")
                        
        
        def doSteps(self, totalSteps):
                self.dir_pin.value(1)
                stepsLeft= totalSteps
                while stepsLeft > 0:
                        print("steps left:" , stepsLeft)
                        self.step_pin.value(1)
                        self.step_pin.value(0)
                        time.sleep(0.01)
                        stepsLeft -= 1

                
                        
                        
                        
                
                
                
                
        