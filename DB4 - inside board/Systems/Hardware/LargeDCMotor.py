import time

import machine


class LargeDCMotor: #TODO rename this 
        
        frequency = 1000
        currentDutyCycle = 0
        
        maxCycles = 1023
        minCycles = 450 #adjust this according to system
        
        
        def __init__(self, inputD, inputC, EnableB) -> None:
                self.inputD = machine.Pin(inputD, machine.Pin.OUT)
                self.inputC = machine.Pin(inputC, machine.Pin.OUT)
                self.EnableB = machine.Pin(EnableB, machine.Pin.OUT)
                self.pwmB = machine.PWM(self.EnableB)
                
                self.pwmB.freq(self.frequency )




        def start(self):
                self.inputD.value(1)
                self.inputC.value(0)
                
        def stop(self):
                self.inputD.value(0)
                self.inputC.value(0)

        def setSpeedCycles(self, dutyCycles):
                self.currentDutyCycle = dutyCycles
                self.pwmB.duty(dutyCycles)
        
        def setSpeedPercentage(self, percentage):
                self.currentDutyCycle = self.percentageToDutyCycle(percentage)
                self.pwmB.duty(int(self.currentDutyCycle))

        def getSpeedPercentage(self):
                percentage = self.dutyCycleToPercentage(self.currentDutyCycle)
                return percentage
        
        
        def dutyCycleToPercentage(self, dutyCycle):
                percentage = 100 * ((dutyCycle - self.minCycles)/(self.maxCycles - self.minCycles))
                return percentage
        
        def percentageToDutyCycle(self, percentage):
                dutyCycle = ((self.maxCycles - self.minCycles)*percentage/100) + self.minCycles
                return dutyCycle
        
        def testMinAndMaxDuty(self):
                print("running large DC testMinAndMaxDuty....")
                
                self.start()
                duty = 0
                while duty < self.maxCycles:
                        self.setSpeedCycles(duty)
                        time.sleep(0.01)
                        duty += 1
                
                print("Test is done")
                time.sleep(3)
                self.stop()

        def testMaxSpeed(self):
                
                print("running large DC testMaxSpeed....")
                self.start()
                iter = 0
                while iter < 1000:
                        print("running at max speed")
                        self.setSpeedCycles(self.maxCycles)
                        time.sleep(0.01)
                        iter +=1
                
                print("Test is done")
                self.stop()
