import time

from Systems.components import largeDCMotor

# largeDCMotor.testMaxSpeed()
# Create a system with a single component
# oledScreen.runTest()
# largeDCMotor.testMinAndMaxDuty()
while True:
    largeDCMotor.start()
    c, d = largeDCMotor.get_input_C_D()
    print(f" C : {c} D : {d}")

    largeDCMotor.setSpeedCycles(1000)
    print(f"Speed : {largeDCMotor.getSppedCycles()}")
    time.sleep(2)
    # print(temperatureSensor.readADC())
    # print(f" R : {temperatureSensor.getResistance()}")
    # print(f" T :{temperatureSensor.getTemperature()}")
    largeDCMotor.stop()
    time.sleep(1)

print("Test should have been run on the OLED screen by now")
