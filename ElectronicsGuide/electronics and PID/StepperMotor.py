import time

import machine

#OBS: this run the motor in one direction, and then swaps direction after steps



class StepperMotor:
        
        DEFAULT_delay = 0.01
        DEFAULT_frequency = 1000
        DEFAULT_duty_cycle = 0
        
        
        def __init__(self, step_pin, dir_pin):
                self.step_pin = machine.Pin(step_pin, machine.Pin.OUT)
                self.dir_pin = machine.Pin(dir_pin, machine.Pin.OUT)
                
                self.delay = self.DEFAULT_delay
                self.frequency = self.DEFAULT_frequency
                self.duty_cycle = self.DEFAULT_duty_cycle
                self.direction = 0 #clockwise
                
                self.pwm = machine.PWM(step_pin)
                
                
        def setDutyCycle(self, dutyCycle):
                self.pwm.duty(dutyCycle)
                

        def setDirection(self, direction):
                if direction== 0 or direction==1:
                        self.direction=direction
                else:
                        print("Please provide a direction that is either 0 or 1 :)")