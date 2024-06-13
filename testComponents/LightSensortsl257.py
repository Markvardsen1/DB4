from machine import ADC, Pin
import time

# Initialize ADC on GPIO 34
adc = ADC(Pin(36))
adc.atten(ADC.ATTN_11DB)  # Configure the attenuation (0dB to 11dB) to scale the input range (0-3.3V)

# Read and print the sensor value
while True:
    light_value = adc.read()  # Read the analog value (0-4095)
    print("Light Intensity:", light_value)
    time.sleep(1)
