import time

import machine
from Systems import components
from Systems.Software import PID, PIDtemperature

# TODO set Kp, Ki, Kd at arbitrary values
Kp, Ki, Kd = 1.0, 0, 0

PIDtemperature.pidForTemperatureSensor.tunings = (Kp, Ki, Kd)
PIDtemperature.runTest()
