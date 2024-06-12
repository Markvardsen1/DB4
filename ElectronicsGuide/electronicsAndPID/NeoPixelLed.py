import time

import machine
import neopixel
from machine import ADC, Pin

pot=ADC(Pin(34))


np = neopixel.NeoPixel(machine.Pin(32), 2)


while True:
    pot_value=pot.read_u16() 
    pot_value=pot.read_u16()
    
    ratio=pot_value/4095
    
    
    #mulitply the ratio on our color components. Its only gonna be red.
    red=int(round(255*ratio))
    green=int(0*ratio)
    blue=int(0*ratio)
    
    print(red)
    
    np[0]=(red,green,blue) 
    np[1]=(red,green,blue) 
    
    np.write()
    
    time.sleep(0.1)