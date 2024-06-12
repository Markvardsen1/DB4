

import time

import machine

InD = machine.Pin(14, machine.Pin.OUT)
InC = machine.Pin(15, machine.Pin.OUT)
EnB = machine.Pin(32, machine.Pin.OUT)

InD.value(0)
InC.value(1)

delay = 0.5 


pwmB = machine.PWM(EnB)
pwmB.freq(1000)
pwmB.duty(750)


while True:
        print("running")
        time.sleep(1)
        
