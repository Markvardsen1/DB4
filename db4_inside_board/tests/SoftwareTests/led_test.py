import time

from machine import Pin

led = Pin(13, Pin.OUT)

while True:
    led.value(not led.value())
    time.sleep(1)
