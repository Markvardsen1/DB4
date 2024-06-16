import time 
import machine
from Systems import components
from Systems.Software import PID
from Systems.Software import PIDtemperature
from Systems.Hardware import *


# TODO set Kp, Ki, Kd at arbitrary values
Kp, Ki, Kd = 1.0, 0, 0

PIDtemperature.pidForTemperatureSensor.tunings = (Kp, Ki, Kd)
PIDtemperature.runTest()
