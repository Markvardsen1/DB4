import time

import machine
from Systems import components
from Systems.Software import PIDodSensor

Kp, Ki, Kd = 1.0, 0, 0
PIDodSensor.pidForODSensor.tunings = (Kp, Ki, Kd)
PIDodSensor.runTest()
