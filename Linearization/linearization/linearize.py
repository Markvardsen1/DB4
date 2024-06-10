# NOTES:
# Connect pin 25 (A1) with pin 32 (the one to linearize)
# Set DAC_Vmax (should be 3.15 in all devices, but...)
# Set the desired ADC_MAX = 2^ADC_BIT_WIDTH-1 and the proper adc.width(ADC.WIDTH_10BIT)

import gc
from machine import Pin, ADC, DAC
import utime

ADC_DELAY = 10
DAC_DELAY = 5

ADC_PIN_NO = 32
DAC_PIN_NO = 25

NUM_SAMPLES = 50
ADC_MAX = 1023
DAC_MAX = 255

DAC_Vmax = 3.15
DAC_Vmin = 0.09  # Not used!

DAC_QUANTUM = DAC_Vmax / DAC_MAX

def initialize_adc(pin_no):
    adc = ADC(Pin(pin_no))
    adc.atten(ADC.ATTN_11DB)
    adc.width(ADC.WIDTH_10BIT)
    return adc

def initialize_dac(pin_no):
    return DAC(Pin(pin_no), bits=8)

def measure(adc, dac):
    adc_read = []
    for i in range(DAC_MAX + 1):
        print('Samples acquired: ' + str(i) + '/' + str(DAC_MAX))
        dac.write(i)
        utime.sleep_ms(ADC_DELAY)
        raw_read = []
        for _ in range(NUM_SAMPLES):
            raw_read.append(adc.read())
            utime.sleep_ms(DAC_DELAY)
        adc_read.append(round(sum(raw_read) / NUM_SAMPLES))
    return adc_read

def process_adc_readings(adc_read):
    adc_V_lookup = []
    for i in range(ADC_MAX + 1):
        gc.collect()
        gc.mem_free()
        print('Processing index ' + str(i))
        if adc_read.count(i) == 1:
            print('  1 to 1 match!')
            adc_V_lookup.append(DAC_QUANTUM * adc_read.index(i))
        elif adc_read.count(i) == 0:
            print('  No match!')
            range_min, range_max = find_interpolation_ranges(adc_read, i)
            print('  i_min: ' + str(i-1) + ' range_min: ' + str(range_min) + ' i_max: ' + str(i+1) + ' range_max: ' + str(range_max))
            adc_V_lookup.append(DAC_QUANTUM * (range_min + ((range_max - range_min) / (i + 1 - (i - 1))) * (i - (i - 1))))
        else:
            print('  Multiple matches!')
            range_min, range_max = find_collapsing_ranges(adc_read, i)
            adc_V_lookup.append(DAC_QUANTUM * ((range_max - range_min) / 2 + range_min))
        print('  adc_V :' + str(adc_V_lookup[i]) + ' V')
    return adc_V_lookup

def find_interpolation_ranges(adc_read, i):
    range_min = -1
    i_min = i - 1
    while range_min == -1:
        if i_min < min(adc_read):
            range_min = adc_read.index(min(adc_read))
        elif i_min in adc_read:
            range_min = adc_read.index(i_min)
        else:
            i_min -= 1

    range_max = -1
    i_max = i + 1
    while range_max == -1:
        if i_max > max(adc_read):
            range_max = adc_read.index(max(adc_read))
        elif i_max in adc_read:
            range_max = adc_read.index(i_max)
        else:
            i_max += 1

    return range_min, range_max

def find_collapsing_ranges(adc_read, i):
    tmp_range = [j for j in range(DAC_MAX + 1) if adc_read[j] == i]
    return min(tmp_range), max(tmp_range)

def main():
    adc = initialize_adc(ADC_PIN_NO)
    dac = initialize_dac(DAC_PIN_NO)
    adc_read = measure(adc, dac)
    adc_V_lookup = process_adc_readings(adc_read)
    print('----------------------------------------------------')
    print('----------------------------------------------------')
    print(adc_V_lookup)

