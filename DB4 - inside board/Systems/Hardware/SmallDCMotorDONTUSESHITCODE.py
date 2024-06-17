import time

import machine


class SmallDCMotor:
        
        DEFAULT_FREQUENCY = 1000
        DEFAULT_DUTY_CYCLE = 450
        
        maxCycles = 1023
        minCycles = 450 #FIGURE OUT THE MINIMUM DUTY CYCLE FOR THE MOTOR
        
        def __init__(self, inputA, inputB, EnableA):
                self.InA = machine.Pin(inputA, machine.Pin.OUT)
                self.InB = machine.Pin(inputB, machine.Pin.OUT)
                self.EnA = machine.Pin(EnableA, machine.Pin.OUT)
                
                self.pwmA = machine.PWM(self.EnA)
                self.pwmA.freq(self.DEFAULT_FREQUENCY)
                self.pwmA.duty(self.DEFAULT_DUTY_CYCLE)
                self.InA.value(0)
                self.InB.value(1)
                
        def setDutyCycle(self, dutyCycle):
                self.pwmA.duty(dutyCycle) #Test of it can stop with duty cycle 0
        
        
        def getDutyCycle(self):
                return self.pwmA.duty()

                
        def start(self):
                self.InA.value(0)
                self.InB.value(1)
                self.pwmA.duty(self.DEFAULT_DUTY_CYCLE)
        
        def stop(self):
                self.InA.value(0)
                self.InB.value(0)
                self.pwmA.duty(0)
        
        
        def testMinAndMaxDuty(self):
                print("running small DC testMinAndMaxDuty....")
                duty = 0
                while duty < self.maxCycles:
                        self.setSpeedCycles(duty)
                        time.sleep(0.01)
                        duty += 1
                
                print("Test is done")
                time.sleep(3)

        def testMaxSpeed(self):
                
                print("running small DC testMaxSpeed....")
                iter = 0
                while iter < 1000:
                        print("running at max speed")
                        self.setSpeedCycles(self.maxCycles)
                        time.sleep(0.01)
                        iter +=1
                
                print("Test is done")
