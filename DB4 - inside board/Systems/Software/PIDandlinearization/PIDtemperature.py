import time
import math

from Systems.Software.PIDandlinearization import PID
from Systems import components
from Systems.Hardware import *

Kp = 1.5
Ki = 0.5
Kd = 1.5

pidForTemperatureSensor = PID.PID(
    Kp=Kp,
    Ki=Ki,
    Kd=Kd,
    setpoint=18,
    sample_time=0.1,
    scale='s',
    output_limits=(-100, 100)
    )

def runPIDforTemperatureSensor():
        if components.temperatureSensor.getAverageTemperature() >= 18:
            curentPIDValue = int(abs(pidForTemperatureSensor((components.temperatureSensor.getAverageTemperature()))))
        else:
            curentPIDValue = 0

        components.largeDCMotor.setSpeedPercentage(int(curentPIDValue/2))
        print('PID Value:' , curentPIDValue)
        print('Temperature:' , components.temperatureSensor.getAverageTemperature())
        time.sleep(0.5)

def runTest():
    while True: 
        latestTemperatureOutput = components.temperatureSensor.getAverageTemperature()
        latestPIDOutput = pidForTemperatureSensor(latestTemperatureOutput)
        Pterm, Dterm, Iterm = pidForTemperatureSensor.components()
        print("Temperature: ", latestTemperatureOutput)
        print("PID output: ", latestPIDOutput)
        print("Pterm: ", Pterm)
        print("Dterm: ", Dterm)
        print("Iterm: ", Iterm)
        time.sleep(2)

if __name__ == '__main__':
    components.cooler.highCooling()
    components.fan.startFan()
    components.largeDCMotor.start()
    while True:
        runPIDforTemperatureSensor()