import time

import machine


#TODO FIX FUNCTION NAMES
class ValveSwitch:
        
        DEFAULT_delay = 0.1
        DEFAULT_frequency = 1000
        DEFAULT_duty_cycle = 0
        
        minCycles = 450 #TODO TEST THIS VALUE
        maxCycles = 1023 #TODO TEST THIS VALUE
        
        
        
        defaultFrequency = 1000
        currentDutyCycle = 0
        
        
        maxCycles = 1023
        minCycles = 450 #adjust this according to system
        
        def __init__(self, step_pin_number: int, dir_pin_number : int):
                self.step_pin = machine.Pin(step_pin_number, machine.Pin.OUT)
                self.dir_pin = machine.Pin(dir_pin_number, machine.Pin.OUT)
                
                self.delay = self.DEFAULT_delay
                self.frequency = self.DEFAULT_frequency
                self.duty_cycle = self.DEFAULT_duty_cycle
                self.direction = 0 #clockwise
                
                self.pwm = machine.PWM(step_pin_number)
                
        def start(self):
                self.pwm.duty(self.duty_cycle)

        def stop(self):
                self.pwm.duty(0)

        def setSpeedCycle(self, dutyCycle : int):
                self.duty_cycle = dutyCycle
                self.pwm.duty(dutyCycle)
        
        
        
        def setSpeedPercentage(self, percentage : int):
                self.duty_cycle = self.percentageToDutyCycle(percentage)
                self.pwm.duty(self.duty_cycle)

        def getSpeedPercentage(self):
                percentage = self.dutyCycleToPercentage(self.duty_cycle)
                return percentage
                        
        def percentageToDutyCycle(self, percentage):
                dutyCycle = ((self.maxCycles - self.minCycles)*percentage/100) + self.minCycles
                return dutyCycle

        def dutyCycleToPercentage(self, dutyCycle):
                percentage = 100 * ((dutyCycle - self.minCycles)/(self.maxCycles - self.minCycles))
                return percentage


        def testMinAndMaxDuty(self):
                print("running StepperMotor testMinAndMaxDuty....")
                duty = 0
                while duty < self.maxCycles:
                        self.setSpeedCycle(duty)
                        time.sleep(0.01)
                        duty += 1
                
                print("Test is done")
                time.sleep(3)
        
        def testMaxSpeed(self):
                print("running StepperMotor testMaxSpeed....")
                iter = 0
                while iter < 1000:
                        print("running at max speed")
                        self.setSpeedCycle(self.maxCycles)
                        time.sleep(0.01)
                        iter +=1