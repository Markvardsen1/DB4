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
    output_limits=(-100, 0)
    )

def runPIDforTemperatureSensor():
        if components.temperatureSensor.getMedianTemperature() >= 18:
            curentPIDValue = int(abs(pidForTemperatureSensor((components.temperatureSensor.getMedianTemperature()))))
        else:
            curentPIDValue = 0

        if curentPIDValue == 0: 
             components.foodPump.setSpeedCycles(0)
        else:      
            components.foodPump.setSpeedPercentage(int(curentPIDValue))
        # print('PID Value:' , curentPIDValue)
        # print('Temperature:' , components.temperatureSensor.getMedianTemperature())
        time.sleep(0.5)

def runTest():
    while True: 
        latestTemperatureOutput = components.temperatureSensor.getMedianTemperature()
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
    components.foodPump.start()
    while True:
        runPIDforTemperatureSensor()