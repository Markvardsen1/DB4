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

def runPIDforODSensor():
    while True: 
        curentPIDValue = pidForODSensor(components.ODSensor.getOD())
        
        if curentPIDValue >= 10: 
            components.ledStrip.setLightPercentage(curentPIDValue)
            print('PID Value:', curentPIDValue)
            print('OD:', components.ODSensor.getOD())
        else:
            components.ledStrip.setLightPercentage(0)

def runTest():
    while True: 
        latestODOuput = components.ODSensor.getOD()
        latestPIDOutput = pidForODSensor(latestODOuput)
        Pterm, Dterm, Iterm = pidForODSensor.components
        print("OD: ", latestODOuput)
        print("PID output: ", latestPIDOutput)
        print("Pterm: ", Pterm)
        print("Dterm: ", Dterm)
        print("Iterm: ", Iterm)
        time.sleep(2)
        
if __name__ == '__main__':
    runPIDforODSensor()
    