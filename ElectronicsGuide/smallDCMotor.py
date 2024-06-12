import time

import machine

InA = machine.Pin(21, machine.Pin.OUT)
InB = machine.Pin(17, machine.Pin.OUT)
EnA = machine.Pin(16, machine.Pin.OUT)

InA.value(0)
InB.value(1)

delay = 0.5 

pwmA = machine.PWM(EnA)
pwmA.freq(1000)
pwmA.duty(450)


while True:
        print("running")
        time.sleep(1)
        