from Systems.Hardware import *
from Systems.Hardware.Cooler import Cooler
from Systems.Hardware.Fan import Fan
from Systems.Hardware.LargeDCMotor import LargeDCMotor
from Systems.Hardware.LEDStrip import LEDStrip
from Systems.Hardware.ODSensor import ODSensor
from Systems.Hardware.OLEDScreen import OLEDScreen
from Systems.Hardware.TemperatureSensor import TemperatureSensor
from Systems.Hardware.ValveSwitch import ValveSwitch
from Systems.Software.PIDandlinearization.PID import PID
from Systems.Hardware.Photoresistor import Photoresistor

# notes

# yellow = 12v
# red = 5v
# white = 3v
# green ground


# relay :
# vcc = 12v


# HARDWARE
temperatureSensorPin = 39
FixedResistor = 10000
temperatureSensor = TemperatureSensor(temperatureSensorPin)

# voltage_pin = 13
# stepper_pin = 33
# direction_pin = 27
# valveSwitch = ValveSwitch(stepper_pin, direction_pin, voltage_pin)


# inputA = 21
# inputB = 17
# EnableA = 16
# smallDCMotor = SmallDCMotor(inputA, inputB, EnableA)


inputC = 16  # rx
inputD = 17  # tx
EnableB = 21  # 21
foodPump = LargeDCMotor(inputC, inputD, EnableB)


inputA = 32
inputB = 15
EnableA = 14
coolPump = LargeDCMotor(inputA, inputB, EnableA)


cooling_pin_Inp2 = 12
cooler = Cooler(cooling_pin_Inp2)


fan_pin_Inp1 = 27
fan = Fan(fan_pin_Inp1)


sclPin = 22
sdaPin = 23
oledScreen = OLEDScreen(sclPin, sdaPin)


# ODSensorPin = 34
# odSensor = ODSensor(ODSensorPin)

Photo_resistor_pin = 34
photoresistor = Photoresistor(Photo_resistor_pin)

# SOFTWARE:


pidTemperatureController = PID(
    Kp=1.5, Ki=0.5, Kd=1.5, setpoint=18, sample_time=0.1, output_limits=(-100, 0)
)
# pidODController = PIDController()

# wifiConnecter = WifiConnecter()
# adafruitIOClient = AdafruitIOClient()
# offlineClient = OfflineClient()
# dataPublisher = DataPublisher(adafruitIOClient, offlineClient)

# inputC = 15f
# inputD = 14
# EnableB = 32
# # Green = Output D
# # Yellow = Output C
# ledStrip = LEDStrip(inputC, inputD, EnableB)