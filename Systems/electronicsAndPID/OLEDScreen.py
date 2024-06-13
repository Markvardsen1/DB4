import time

import ssd1306
from machine import I2C, Pin


class OLEDScreen:

    DEFAULT_FREQUENCY = 100000

    def __init__(self, sclPin, sdaPin):
        self.i2c = I2C(scl=Pin(sclPin), sda=Pin(sdaPin), freq=self.DEFAULT_FREQUENCY)
        self.oled = ssd1306.SSD1306_I2C(128, 32, self.i2c)
        self.items_list = []  # Initialize with an empty list
        self.current_index = 0
    
        
    def display(self, data_dict: dict) -> None:
        # Convert dictionary to a list of tuples (key, value)
        self.items_list = list(data_dict.items())
        self.oled.fill(0)
        
        # Calculate the number of lines to display
        num_lines = min(len(self.items_list), 4)
        
        for i in range(num_lines):
            index = (self.current_index + i) % len(self.items_list)
            key, value = self.items_list[index]
            self.oled.text(f"{key}: {value}", 0, i * 8)
        
        self.oled.show()

        # Increment current_index for the next call
        self.current_index = (self.current_index + 1) % len(self.items_list)
        
    def getAdress(self):
        return self.i2c.scan()

    def stop(self) -> None: 
        self.oled.fill(0)
        self.oled.show()
        
    def start(self) -> None:
        self.display("Starting")
        
        
        
        


