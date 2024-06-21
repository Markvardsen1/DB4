import time

import machine
from Systems import components

# TODO set Kp, Ki, Kd at arbitrary values
Kp, Ki, Kd = 1.0, 0, 0

components.PIDtemperature.pidForTemperatureSensor.tunings = (Kp, Ki, Kd)

components.pidTemperatureController
components.PIDtemperature.runTest()
