import time

import machine


class ValveSwitch:
        
        delay = 1
        frequency = 800
        currentDutyCycle = 0
        currentDirection = 0
        
        minCycles = 450
        maxCycles = 1023


        def __init__(self, step_pin_number: int, dir_pin_number : int):
                self.step_pin = machine.Pin(step_pin_number, machine.Pin.OUT)
                self.dir_pin = machine.Pin(dir_pin_number, machine.Pin.OUT)

                self.pwm = machine.PWM(step_pin_number)
                self.pwm.freq(self.frequency) 
                

        def setSpeedCycle(self, dutyCycle):
                
                self.currentDutyCycle = dutyCycle
                self.duty_cycle = dutyCycle
                self.pwm.duty(dutyCycle)

        

                        
        def rotate(self, steps, direction):
                self.dir_pin.value(direction)
                for _ in range(steps):
                        self.step_pin.value(1)
                        print("running")
                        time.sleep(self.delay)
                        self.step_pin.value(0)
                        time.sleep(self.delay)

        

        def testMaxSpeed(self):
                print("running StepperMotor testMaxSpeed....")
                iter = 0
                while iter < 250:
                        print("running at max speed")
                        self.setSpeedCycle(self.maxCycles)
                        time.sleep(0.01)
                        iter +=1
        
        def testDelay(self):
                print("running StepperMotor test delay!!!!!!!!!....")
                
                self.setSpeedCycle(0)
                delay = 0.3
                
                timeStart = print(time.time)
                while delay > 0:
                        print(delay)
                        self.step_pin.value(1)
                        time.sleep(delay)
                        self.step_pin.value(0)
                        time.sleep(delay)
                        delay -= 0.01
        
                        
                        
                                
                        
                        
        

                        
                        
                        
