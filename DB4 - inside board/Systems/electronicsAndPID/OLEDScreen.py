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

    def stop(self) -> None: 
        self.oled.fill(0)
        self.oled.show()
        
    def start(self) -> None:
        self.display(self.intializer)
        
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
            self.display(data)
            time.sleep(1)
        
    
        
        
        
        


