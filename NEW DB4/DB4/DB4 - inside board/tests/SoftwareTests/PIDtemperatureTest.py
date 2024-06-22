import time

import machine
from Systems import components
from Systems.Software.PIDandlinearization import PID

if __name__ == '__main__':
    components.cooler.highCooling()
    components.fan.startFan()
    components.largeDCMotor.start()
    while True:
        components.pidTemperatureController.runPIDforTemperatureSensor()
        print("Temperature: ", components.temperatureSensor.getAverageTemperature())
        print("Duty Cycle: ", components.largeDCMotor.getSppedCycles())