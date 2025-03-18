import time

from Systems.components import foodPump, oledScreen, cooler, fan, photoresistor, temperatureSensor, coolPump


# print("Waking up system")
# time.sleep(2)
# fan.stopFan()
# cooler.lowCooling()
# foodPump.stop()
# coolPump.stop()

print("stopped all components")
print("starting tests")
# oledScreen.runTest()
fan.testFan()
cooler.testCooler()
photoresistor.testSensor()
# temperatureSensor.testTempeartureSensor()

# a,b = coolPump.get_input_C_D()
# print(a,b)
# coolPump.testMaxSpeed()
# print(a,b)


# c,d = foodPump.get_input_C_D()
# print(c,d)
# foodPump.testMaxSpeed()
# print(c,d)



#foodPump.testMinAndMaxDuty() run when system is done 


