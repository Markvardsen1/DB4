import ssd1306
from machine import I2C, Pin


class OLEDScreen:
    
    DEFAULT_FREQUENCY = 100000
    
    def __init__(self, sclPin, sdaPin):
        self.i2c = I2C(scl=Pin(sclPin), sda=Pin(sdaPin), freq=self.DEFAULT_FREQUENCY)
        self.oled = ssd1306.SSD1306_I2C(128, 32, self.i2c)
        
        self.slots = {
            "temp": "",
            "od": "",
            "Ki": "",
            "Kp": "",
            "Kd": "",
        }
        
        
    def getAdress(self):
        return self.i2c.scan()
    
    def display(self, text: str, key: str):
        
        self.slots[key] = text
        
        x , y = 0, 8
        
        self.oled.fill(0)
        for i in self.slots:
            self.oled.text(self.slots[i].key, 0, 8)
            self.oled.text(self.slots[i].value, 0+8, y)
            y+=8
            
    def display(self, text:str):
        self.oled.text("this!", 16, 24)
        self.oled.show()
        
        
        


# i2c = I2C(scl=Pin(22), sda=Pin(23), freq=100000)

# device_address = i2c.scan()

# if device_address:
#     print("Device address: ", device_address)
# else:
#     print("No device found")

# oled = ssd1306.SSD1306_I2C(128, 32, i2c)
# oled.fill(0)
# oled.text("I", 0, 8)
# oled.text("wrote", 8, 16)
# oled.text("this!", 16, 24)
# oled.show()