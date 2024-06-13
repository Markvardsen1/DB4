import time

import machine


class LargeDCMotor:
        
        DEFAULT_FREQUENCY = 1000
        DEFAULT_DUTY_CYCLE = 750
        
        def __init__(self, inputD, inputC, EnableB) -> None:
                self.InD = machine.Pin(inputD, machine.Pin.OUT)
                self.InC = machine.Pin(inputC, machine.Pin.OUT)
                self.EnB = machine.Pin(EnableB, machine.Pin.OUT)
                self.pwmB = machine.PWM(self.EnB)
                self.pwmB.freq(self.DEFAULT_FREQUENCY)
                self.pwmB.duty(self.DEFAULT_DUTY_CYCLE)
        
        def start(self):
                self.InD.value(0)
                self.InC.value(1)
                self.pwmB.duty(self.DEFAULT_DUTY_CYCLE)
                
        
        def stop(self):
                self.InD.value(0)
                self.InC.value(0)
                self.pwmB.duty(0)
        
        
        def speed(self, dutyCycle, frequency):
                self.pwmB.duty(dutyCycle)
                self.pwmB.freq(frequency)



        def getDutyCycle(self):
                return self.pwmB.duty()
        
        def getFrequency(self):
                return self.pwmB.freq()
        

