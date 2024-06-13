import time
import machine


#OBS: this run the motor in one direction, and then swaps direction after steps

step_pin = machine.Pin(33, machine.Pin.OUT)
dir_pin = machine.Pin(27, machine.Pin.OUT)

delay = 0.01

frequency = 1000
duty_cycle = 1000 

pwm = machine.PWM(step_pin)
pwm.freq(frequency)
pwm.duty(duty_cycle)

sum = 1000
dir = 0
print("trying to run")
while True:
        print("duty_cycle: ", duty_cycle)       
        if duty_cycle == 100:
                time.sleep(1)
                duty_cycle = 1000
                sum = 1000
        duty_cycle = sum 
        pwm.duty(duty_cycle)
        time.sleep(delay)
        sum -= 1