import sys

sys.path.append("/db4_inside_board")
from Systems.components import oledScreen, temperatureSensor

if __name__ == "__main__":
    # Create a system with a single component
    oledScreen.runTest()
    temperatureSensor.testTempeartureSensor()

    print("Test should have been run on the OLED screen by now")
