
def getTemperature():
    return 18

def getOD():
    return 200

def getFlow():
    return 2

def displayOLED(data:list): #need to make some mapping here, so OLED knows how to display data proberly
    i2c = i2c(scl=Pin(22), sda=Pin(23), freq=100000)

    device_address = i2c.scan()

    if device_address:
        print("Device address: ", device_address)
    else:
        print("No device found")

    oled = ssd1306.SSD1306_I2C(128, 32, i2c)
    
    oled.fill(0)
    
    oled.text("temperature" + list[0], 0, 8)
    oled.text("OD" + list[1], 0, 8)
    oled.text("flow" + list[2], 0, 8)
    
    
    oled.show()
    
    
def PID_temperature(desired_temperature):
    print("desired temperature set")
    
def PID_flow(desired_temperature):
    print("desired temperature set")