import time
import machine
from Systems import components
from PID import PID
from Systems.Hardware import *


pidForODSensor = PID(
    setpoint=2000,
    sample_time=0.1,
    scale='s',
    output_limits=(0, 1000)
    )

while True:
    latestODOuput = components.ODSensor.getOD()
    latestPIDOutput = pidForODSensor(latestODOuput)
    
    if latestPIDOutput >= components.ODSensor.maxValue / 2:
        print("too many algaes have grown --> reducing light\n")
        components.ledStrip.setLightPercentage(20)
        
    else: 
        print("too few algaes have grown --> increasing light\n")
        components.ledStrip.setLightPercentage(80)
    
    time.sleep(2)
