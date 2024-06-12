import time
import machine

step_pin = machine.Pin(33, machine.Pin.OUT)
dir_pin = machine.Pin(27, machine.Pin.OUT)

delay = 0.5

frequency = 1000
duty_cycle = 512 

pwm = machine.PWM(step_pin)
pwm.freq(frequency)
pwm.duty(duty_cycle)

sum = 0
dir = 0
print("trying to run")
while True:
        step_pin.off()
        time.sleep(delay)
        step_pin.on()
        time.sleep(delay)
        sum = sum + 1 
        if sum == 10: 
                sum = 0 
                if dir % 2 == 0:
                        dir = dir + 1
                        print("Turning right")
                        dir_pin.value(dir % 2)
                elif dir % 2 == 1:
                        dir = dir + 1
                        print("Turning left")
                        dir_pin.value(dir % 2)
                
        
        
        
        
                
                
                
        
        
