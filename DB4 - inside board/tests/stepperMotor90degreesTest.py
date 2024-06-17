import time 
import machine
from Systems.Software.StepperClass import Stepper

stepperMotor = Stepper(33, 27, None, 400, 10, False, -1)

def turn90degreesAndBack() -> None:
    stepperMotor.target_deg(90)
    time.sleep(1)
    stepperMotor.target_deg(0)
    time.sleep(1)

def turning90degreesTest() -> None:
    turn90degreesAndBack()
    stepperMotor.stop()

if __name__ == '__main__':
    turning90degreesTest()
    
