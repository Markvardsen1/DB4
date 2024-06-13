import time 
import machine 

cooling_pin = machine.Pin(12, machine.Pin.OUT)

while True:
    cooling_pin.value(1)
    time.sleep(5)
    cooling_pin.value(0)
    time.sleep(5)