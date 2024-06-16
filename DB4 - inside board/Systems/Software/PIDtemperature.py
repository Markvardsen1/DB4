from PID import PID
from SmallDCMotor import SmallDCMotor
from TemperatureSensor import TemperatureSensor

inputA = 21
inputB = 17
EnableA = 16
smallDCMotor = SmallDCMotor(inputA, inputB, EnableA)

temp_pin = 25
FixedResistor = 10000
tempSensor = TemperatureSensor(temp_pin, FixedResistor)

Kp = 1
Ki = 0
Kd = 0

pid = PID(
    Kp=Kp,
    Ki=Ki,
    Kd=Kd,
    setpoint=20,
    sample_time=0.1,
    scale='s',
    output_limits=(0, 100)
    )


while True: 
    curentPIDValue = pid(tempSensor.getTemperature())
    
    if curentPIDValue >= 10: 
        smallDCMotor.setDutyCycle(curentPIDValue * 10)
        print('PID Value:', curentPIDValue)
        print('Temperature:', tempSensor.getTemperature())
    else:
        smallDCMotor.setDutyCycle(0)
        
    