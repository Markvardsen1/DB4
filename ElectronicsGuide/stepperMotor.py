from machine import pin
import utime
import time

class stepper:
    def __init__(self, step_pin, dir_pin, enable_pin=none):
        self.step_pin = pin(step_pin, pin.out)
        self.dir_pin = pin(dir_pin, pin.out)
        self.enable_pin = pin(enable_pin, pin.out) if enable_pin else none
        self.position = 0
        self.delay = 0.01  # default delay, can be set by set_speed

    def set_step_high(self):
        self.step_pin.value(1)
        
    def set_step_low(self):
        self.step_pin.value(0)
        

    def set_speed(self, speed):
        # calculate delay time based on the desired speed (steps per second)
        self.delay = 1 / abs(speed)  # delay in seconds

    def set_direction(self, direction):
        self.dir_pin.value(direction)

    def enable(self):
        if self.enable_pin:
            self.enable_pin.value(0)  # assuming active low enable

    def disable(self):
        if self.enable_pin:
            self.enable_pin.value(1)  # assuming active low enable

    def move_to(self, position):
        steps = position - self.position
        direction = 1 if steps > 0 else 0
        self.set_direction(direction)
        steps = abs(steps)

        for _ in range(steps):
            self.step_pin.value(1)
            utime.sleep(self.delay / 2)
            self.step_pin.value(0)
            utime.sleep(self.delay / 2)

        self.position = position

# define the pins (adjust the gpio numbers as needed)
step_pin = 33  # gpio number where step pin is connected
dir_pin = 27   # gpio number where dir pin is connected
enable_pin = none  # gpio number where enable pin is connected
# initialize stepper
stepper = stepper(step_pin, dir_pin, enable_pin)
stepper.enable()  # enable the stepper motor driver

def loop():
    while true:

        stepper.set_step_high()
        stepper.set_step_low()
        time.sleep(0.01)
        
        
        
if __name__ == '__main__':
    loop()

























































































