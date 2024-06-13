import time

import machine


class SmallDCMotor:
        
        DEFAULT_FREQUENCY = 1000
        DEFAULT_DUTY_CYCLE = 450
        
        def __init__(self, inputA, inputB, EnableA):
                self.InA = machine.Pin(inputA, machine.Pin.OUT)
                self.InB = machine.Pin(inputB, machine.Pin.OUT)
                self.EnA = machine.Pin(EnableA, machine.Pin.OUT)
                
                self.pwmA = machine.PWM(self.EnA)
                self.pwmA.freq(self.DEFAULT_FREQUENCY)
                self.pwmA.duty(self.DEFAULT_DUTY_CYCLE)
                self.InA.value(0)
                self.InB.value(1)
                
        def setDutyCycle(self, dutyCycle):
                self.pwmA.duty(dutyCycle) #Test of it can stop with duty cycle 0
        
        
        def getDutyCycle(self):
                return self.pwmA.duty()