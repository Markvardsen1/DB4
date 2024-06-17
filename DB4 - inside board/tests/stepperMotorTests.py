import time 

import machine
from Systems import components
from Systems.Hardware import *

components.stepperMotor.testMinAndMaxDuty()
components.stepperMotor.testRunnningBothDirections90degrees()
components.stepperMotor.testMaxSpeed()
