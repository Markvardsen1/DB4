import ssd1306
from machine import I2C, Pin


class OLEDScreen:

    DEFAULT_FREQUENCY = 100000

    def init(self, sclPin, sdaPin):
        self.i2c = I2C(scl=Pin(sclPin), sda=Pin(sdaPin), freq=self.DEFAULT_FREQUENCY)
        self.oled = ssd1306.SSD1306_I2C(128, 32, self.i2c)
        

    def getAdress(self):
        return self.i2c.scan()

    def display(self, text: str, key: str) -> None:
        if key in self.slots:
            self.slots[key] = text

        self.oled.fill(0)

        y = 0
        for key in self.slots:
            value = self.slots[key]
            self.oled.text(f"{key}: {value}", 0, y)
            y += 8

        self.oled.show()
        
    def display(self, text:str):
        
        self.oled.fill(0)
        self.oled.text(text, 0, 8)
        self.oled.show()
        
        
    def display(self, map):
        items_list = list(map.items())
        current_position = 0  # Initial vertical position

        while True:
            self.display_items(items_list, current_position)
            current_position -= 1  # Move up
            if current_position < -10:  # Reset position after one line height
                current_position = 0
            time.sleep(0.05)  # Adjust speed of scrolling

    def stop(self) -> None: 
        self.oled.fill(0)
        self.oled.show()
        
    def start(self) -> None:
        self.display("Starting")
        
        
        
        


