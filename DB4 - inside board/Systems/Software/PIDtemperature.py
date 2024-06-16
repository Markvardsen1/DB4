
import components
from PID import PID
from Systems.Hardware import *
from Systems import components

Kp = 1
Ki = 0
Kd = 0

pid = PID(
    Kp=Kp,
    Ki=Ki,
    Kd=Kd,
    setpoint=20,
    sample_time=0.1,
    scale='s',
    output_limits=(0, 100)
    )

while True: 
    curentPIDValue = pid(components.temperatureSensor.getTemperature())
    
    if curentPIDValue >= 10: 
        components.smallDCMotor.setDutyCycle(curentPIDValue * 10)
        print('PID Value:', curentPIDValue)
        print('Temperature:', components.temperatureSensor.getTemperature())
    else:
        components.smallDCMotor.setDutyCycle(0)
        
    