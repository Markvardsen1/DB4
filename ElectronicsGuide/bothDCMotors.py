

import time 
import machine 


# L298N motor driver needs 2 input pins and 1 enabler pin 
InA = machine.Pin(21, machine.Pin.OUT)
InB = machine.Pin(17, machine.Pin.OUT)
EnA = machine.Pin(16, machine.Pin.OUT)
InD = machine.Pin(14, machine.Pin.OUT)
InC = machine.Pin(15, machine.Pin.OUT)
EnB = machine.Pin(32, machine.Pin.OUT)

InD.value(0)
InC.value(0)

InA.value(0)
InB.value(0)

delay = 0.5 

pwmA = machine.PWM(EnA)
pwmA.freq(1000)
pwmA.duty(450)

pwmB = machine.PWM(EnB)
pwmB.freq(1000)
pwmB.duty(750)


while True:
        print("running")
        time.sleep(1)
        
