import time

import machine


class LEDStrip:
        
        defaultFrequency = 1000
        currentDutyCycle = 0
        
        maxCycles = 1023
        minCycles = 0
        
        def __init__(self, inputA, inputB, EnableAbleA):
                self.inputA = machine.Pin(inputA, machine.Pin.OUT)
                self.inputB = machine.Pin(inputB, machine.Pin.OUT)
                self.EnableA = machine.Pin(EnableAbleA, machine.Pin.OUT)
                self.pwmA = machine.PWM(self.EnableA)
                
        def start(self):
                self.inputA.value(0)
                self.inputB.value(1)
                
        
        def stop(self):
                self.inputA.value(0)
                self.inputB.value(0)
                
        
        
        def setLight(self, dutyCycle):
                self.pwmA.duty(dutyCycle)
        
        
        def setLightPercentage(self, percentage):
                self.currentDutyCycle = self.percentageToDutyCycle(percentage)
                self.pwmA.duty(self.currentDutyCycle)

        def getLightPercentage(self):
                percentage = self.dutyCycleToPercentage(self.currentDutyCycle)
                return percentage
        
        def dutyCycleToPercentage(self, dutyCycle):
                percentage = 100 * ((dutyCycle - self.minCycles)/(self.maxCycles - self.minCycles))
                return percentage
        
        def percentageToDutyCycle(self, percentage):
                dutyCycle = ((self.maxCycles - self.minCycles)*percentage/100) + self.minCycles
                return dutyCycle

                
        def testMinAndMaxDuty(self):
                print("running LED testMinAndMaxDuty....")
                self.start()
                duty = 0
                while duty < self.maxCycles:
                        self.setLight(duty)
                        time.sleep(0.01)
                        duty += 1
                
                print("Test is done")
                time.sleep(3)
                
        def testMaxLight(self):
                
                print("running LED testMaxLight....")
                
                self.start()
                iter = 0
                while iter < 1000:
                        print("running at max light")
                        self.setLight(self.maxCycles)
                        time.sleep(0.01)
                        iter +=1
                
                print("Test is done")

        
        