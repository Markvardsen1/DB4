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
        
        def forward(self):
                self.InD.value(0)
                self.InC.value(1)
                self.pwmB.duty(750)
                
        def backward(self):
                self.InD.value(1)
                self.InC.value(0)
                self.pwmB.duty(750)
        
        def setDutyCycle(self, dutyCycle):
                self.pwmB.duty(dutyCycle)
                
        def setFrequency(self, frequency):
                self.pwmB.freq(frequency)
        
        def getDutyCycle(self):
                return self.pwmB.duty()
        
        def getFrequency(self):
                return self.pwmB.freq()
        
        def stop(self):
                self.InD.value(0)
                self.InC.value(0)
                self.pwmB.duty(0)


# InD = machine.Pin(14, machine.Pin.OUT)
# InC = machine.Pin(15, machine.Pin.OUT)
# EnB = machine.Pin(32, machine.Pin.OUT)

# InD.value(0)
# InC.value(1)

# delay = 0.5 


# pwmB = machine.PWM(EnB)
# pwmB.freq(1000)
# pwmB.duty(750)


# while True:
#         print("running")
#         time.sleep(1)
        
