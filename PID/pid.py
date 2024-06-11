import sys
import os
import time
#import machine

class PIDController:
    def __init__(self, pgain, igain, dgain):
        self.pgain = pgain
        self.igain = igain
        self.dgain = dgain
        self.errorsum = 0.0
        self.previous_value = 0.0
    
    def update(self, sensor_value, reference_value):
        error = reference_value - sensor_value
        
        # Proportional term
        pterm = self.pgain * error
        
        # Integral term
        self.errorsum += error
        iterm = self.igain * self.errorsum
        
        # Derivative term
        difference = sensor_value - self.previous_value
        dterm = self.dgain * difference
        
        # Update previous value
        self.previous_value = sensor_value
        
        # Compute the new value
        updated_value = pterm + iterm + dterm
        
        return updated_value

sensor_value = 1.0
reference_value = 18.0

pid_controller = PIDController(pgain=0.5, igain=0.0, dgain=0.3)

while True:
    print("Sensor Value:", sensor_value)
    print("Reference Value:", reference_value)
    
    # Update the sensor value using the PID controller
    sensor_value = pid_controller.update(sensor_value, reference_value)
    
    time.sleep(0.5)
    
    # Adding a break condition for demonstration purposes to avoid an infinite loop
    if sensor_value == reference_value:
        break








































