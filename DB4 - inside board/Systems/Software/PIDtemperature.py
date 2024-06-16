import time
import components
from PID import PID
from Systems.Hardware import *
from Systems import components

Kp = 1
Ki = 0
Kd = 0

pidForTemperatureSensor = PID(
    Kp=Kp,
    Ki=Ki,
    Kd=Kd,
    setpoint=20,
    sample_time=0.1,
    scale='s',
    output_limits=(0, 100)
    )

def runPIDforTemperatureSensor():
    while True: 
        curentPIDValue = pidForTemperatureSensor(components.temperatureSensor.getTemperature())
        
        if curentPIDValue >= 10: 
            components.smallDCMotor.setDutyCycle(curentPIDValue * 10)
            print('PID Value:', curentPIDValue)
            print('Temperature:', components.temperatureSensor.getTemperature())
        else:
            components.smallDCMotor.setDutyCycle(0)
        
def runTest():
    while True: 
        latestTemperatureOutput = components.temperatureSensor.getTemperature()
        latestPIDOutput = PIDtemperature.pidForTemperatureSensor(latestTemperatureOutput)
        Pterm, Dterm, Iterm = PIDtemperature.pidForTemperatureSensor.components
        print("Temperature: ", latestTemperatureOutput)
        print("PID output: ", latestPIDOutput)
        print("Pterm: ", Pterm)
        print("Dterm: ", Dterm)
        print("Iterm: ", Iterm)
        time.sleep(2)
        
if __name__ == '__main__':
    runPIDforTemperatureSensor()
        
        