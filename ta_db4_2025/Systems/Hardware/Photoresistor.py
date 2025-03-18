import time
import machine

class Photoresistor:
    
    def __init__(self, pin):
        self.pin = pin
        self.FixedResistor = 10000  # Value of the fixed resistor (10k Ohm in this case)
        self.adc = machine.ADC(machine.Pin(self.pin))
        self.adc.atten(machine.ADC.ATTN_11DB)  # Set the ADC attenuation to measure a wider range
        
    def readADC(self):
        return self.adc.read()  # Get the ADC value (0-4095 for a 12-bit ADC)
        
    def getResistance(self):
        adc_value = self.readADC()
        if adc_value == 0:
            return float('inf')  # Prevent division by zero
        return self.FixedResistor * (4095 / adc_value - 1)  # Calculate resistance of photoresistor
    
    def getLightIntensity(self):
        resistance = self.getResistance()
        # Here you can calibrate the resistance to light intensity ratio based on your needs
        # You can return the raw ADC value or perform some calculation to estimate the light intensity
        # Example: you could map the resistance to a normalized value (e.g., 0 to 100)
        # For simplicity, let's return the ADC value directly as a light intensity representation
        return self.readADC()
    
    def getMedianLightIntensity(self):
        sampleSize = 31
        intensity_list = [None] * sampleSize
        for i in range(sampleSize):
            intensity_list[i] = self.getLightIntensity()
        intensity_list.sort()
        return intensity_list[int((sampleSize - 1) / 2)]  # Return the median intensity
        
    def stop(self):
        self.adc.atten(machine.ADC.ATTN_0DB)  # Disable the ADC to save power if needed
        
    def start(self):
        self.adc.atten(machine.ADC.ATTN_11DB)  # Re-enable ADC with full range
        
    def testSensor(self):
        print("Running light sensor test...")
        for i in range(5):
            print(f"Light intensity: {self.getMedianLightIntensity()}")
            time.sleep(1)
        print("Test is done")
