
from Systems.components import adafruitIOClient, wifiConnecter
from Systems.Software.MuscleFarmRunner import MuscleFarmRunner
import testingFile

import os
import sys
import time

import network
from Systems.components import (largeDCMotor, odSensor, oledScreen,
                                temperatureSensor, cooler, fan, ledStrip, valveSwitch,
                                pidTemperatureController)
from Systems.Software.MuscleFarmRunner import MuscleFarmRunner
from umqtt.robust import MQTTClient




def main():


    whenToSwitch = 0 
    muscleFarmRunner = MuscleFarmRunner()
    muscleFarmRunner.startMuscleFarm()

    ledStrip.start()
    ledStrip.setLightPercentage(50)

    while True:

        if whenToSwitch < 3300:
            pidTemperatureController.runPIDforTemperatureSensor()

        elif whenToSwitch == 3300:
            largeDCMotor.stop()
            time.sleep(0.5)
            valveSwitch.switch()
            time.sleep(0.5)
            largeDCMotor.start()

        elif whenToSwitch > 3300 and whenToSwitch < 3600:
            muscleFarmRunner.setLargeDCMotorForAlgae(odSensor.getOD())

        elif whenToSwitch == 3600:
            largeDCMotor.stop()
            time.sleep(0.5)
            valveSwitch.switch()
            time.sleep(0.5)
            largeDCMotor.start()

            whenToSwitch = 0

        whenToSwitch += 1