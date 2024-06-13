
import time

import machine

InD = machine.Pin(14, machine.Pin.OUT)
InC = machine.Pin(15, machine.Pin.OUT)
EnB = machine.Pin(32, machine.Pin.OUT)


freq = 1400
duty = 1023

InC.value(1)
InD.value(0)


pwmB = machine.PWM(EnB)

pwmB.freq(freq)
pwmB.duty(duty)


while True:
        print("ssuckmaidgd")
        print("freq: " + str(freq))
        print("duty: " + str(duty))
        time.sleep(1)