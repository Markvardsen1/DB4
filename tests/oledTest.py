
import time

import machine
from electronicsAndPID import *

print("running main...")
sclPin = 22
sdaPin = 23
oledScreen = OLEDScreen(sclPin, sdaPin)
print("wtf?")

data = {
    "Temperature": "22C",
    "Humidity": "45%",
    "Pressure": "1013hPa",
    "Altitude": "500m",
    "Wind Speed": "10km/h",
    "Wind Direction": "NE",
    "Rainfall": "2mm",
    "UV Index": "3",
    "Visibility": "10km",
    "Dew Point": "12C",
    "Cloud Cover": "20%",
    "Air Quality": "Good",
    "Ozone Level": "300DU",
    "CO2 Level": "400ppm",
    "PM2.5": "15µg/m³",
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

while True:
    oledScreen.display(data)
    time.sleep(0.5)
    print("running")
