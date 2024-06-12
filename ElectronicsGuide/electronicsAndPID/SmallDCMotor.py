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
        


# InA = machine.Pin(21, machine.Pin.OUT)
# InB = machine.Pin(17, machine.Pin.OUT)
# EnA = machine.Pin(16, machine.Pin.OUT)

# InA.value(0)
# InB.value(1)

# delay = 0.5

# pwmA = machine.PWM(EnA)
# pwmA.freq(1000)
# pwmA.duty(450)


# while True:
#         print("running")
#         time.sleep(1)
        