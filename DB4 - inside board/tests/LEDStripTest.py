
import time

import machine
from Systems import components
from Systems.electronicsAndPID import *

components.ledStrip.testMaxLight()
components.ledStrip.testMinAndMaxDuty()

