import time 
import machine 


# L298N motor driver needs 2 input pins and 1 enabler pin 
InA = machine.Pin(26, machine.Pin.OUT)
InB = machine.Pin(15, machine.Pin.OUT)
EnA = machine.Pin(32, machine.Pin.OUT)

InA.value(1)
InB.value(0)

delay = 0.5 

pwmA = machine.PWM(EnA)
pwmA.freq(1000)
pwmA.duty(450)


while True:
        print("running")
        time.sleep(1)
        