import time

from machine import I2C, Pin
from Systems import ssd1306


class OLEDScreen:

    DEFAULT_FREQUENCY = 100000

    intializer = {
        "I am turned ": "on "
    }
    
    def __init__(self, sclPin, sdaPin):
        self.i2c = I2C(scl=Pin(sclPin), sda=Pin(sdaPin), freq=self.DEFAULT_FREQUENCY)
        self.oled = ssd1306.SSD1306_I2C(128, 32, self.i2c)
        
        #helper to display
        self.items_list = []  # Initialize with an empty list
        self.current_index = 0
    
    def displayMessage(self, message, scroll=False, delay=0.1):
        # Clear the display
        self.oled.fill(0)
        
        # Center the text
        width = 128
        height = 32
        text_length = len(message) * 8  # Approximate width of text in pixels
        x = (width - text_length) // 2
        y = (height - 8) // 2
        
        if scroll and text_length > width:
            for start in range(0, text_length - width + 1):
                self.oled.fill(0)
                self.oled.text(message, -start, y)
                self.oled.show()
                time.sleep(delay)
            for start in range(text_length - width, -1, -1):
                self.oled.fill(0)
                self.oled.text(message, -start, y)
                self.oled.show()
                time.sleep(delay)
        else:
            self.oled.text(message, x, y)
            self.oled.show()
        
    def displayData(self, data_dict: dict) -> None:
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

    def stop(self) -> None: 
        self.oled.fill(0)
        self.oled.show()
        
    def start(self) -> None:
        self.displayData(self.intializer)
        
    def runTest(self):
        data = {
        "Temperature": "N",
        "Humidity": "45%",
        "Pressure": "1013hPa",
        "Altitude": "500m",
        "Wind Speed": "I",
        "Wind Direction": "NE",
        "Rainfall": "2mm",
        "UV Index": "3",
        "Visibility": "G",
        "Dew Point": "12C",
        "Cloud Cover": "G",
        "Air Quality": "Good",
        "Ozone Level": "300DU",
        "CO2 Level": "400ppm",
        "PM2.5": "A",
        "PM10": "20µg/m³",
        "Solar Radiation": "800W/m²",
        "Soil Moisture": "30%",
        "Soil Temperature": "20C",
        "Leaf Wetness": "5%",
        "Heat Index": "25C",
        "Wind Chill": "20C",
        "Precipitation": "0mm",
        "Snow Depth": "0cm"
    }

        print("running OLED runTest..")
    
        for i in range(10):
            self.displayData(data)
            time.sleep(1)
        
        
        print("test stopped, turning off OLED.")
        self.stop()
    
        
        
        
        


