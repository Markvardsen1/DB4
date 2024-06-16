import time

import machine


#TODO FIX FUNCTION NAMES
class StepperMotor:
        
        DEFAULT_delay = 0.1
        DEFAULT_frequency = 0
        DEFAULT_duty_cycle = 0
        
        minCycles = 450 #TODO TEST THIS VALUE
        maxCycles = 1023 #TODO TEST THIS VALUE
        
        
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

        def step(self, steps: int):
                self.start()
                for _ in range(steps):
                        self.pwm.freq(self.frequency)
                        time.sleep(self.delay)
                        self.stop()

        def setSpeedCycle(self, dutyCycle : int):
                self.duty_cycle = dutyCycle
                self.pwm.duty(dutyCycle)

        def setSpeedPercentage(self, percentage : int):
                self.duty_cycle = self.percentageToDutyCycle(percentage)
                self.pwm.duty(self.duty_cycle)

        def getSpeedPercentage(self):
                percentage = self.dutyCycleToPercentage(self.duty_cycle)
                return percentage
        
        def setFreq(self, frequency : int ):
                self.frequency = frequency
                self.pwm.freq(frequency)
                

        def setDirection(self, direction):
                if direction== 0 or direction==1:
                        self.direction=direction
                        self.dir_pin.value(direction)
                else:
                        print("Please provide a direction that is either 0 or 1 :)")

        def increase_speed(self, start_freq, end_freq, step, delay):
                for freq in range(start_freq, end_freq, step):
                        self.frequency = freq
                        self.pwm.freq(freq)
                        time.sleep(delay)
                        print(freq)

        def decrease_speed(self, start_freq, end_freq, step, delay):
                for freq in range(start_freq, end_freq, -step):
                        self.frequency = freq
                        self.pwm.freq(freq)
                        time.sleep(delay)
                        print(freq)
                        

        def percentageToDutyCycle(self, percentage):
                dutyCycle = ((self.maxCycles - self.minCycles)*percentage/100) + self.minCycles
                return dutyCycle

        
        def dutyCycleToPercentage(self, dutyCycle):
                percentage = 100 * ((dutyCycle - self.minCycles)/(self.maxCycles - self.minCycles))
                return percentage