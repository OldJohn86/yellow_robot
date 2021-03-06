# Simple demo of reading each analog input from the ADS1x15 and printing it to
# the screen.
# Author: Tony DiCola
# License: Public Domain
import time

# Import the ADS1x15 module.
import Adafruit_ADS1x15

coeff = 76.29 # ADC 16 bits 76.29uv

# Create an ADS1115 ADC (16-bit) instance.

adc = Adafruit_ADS1x15.ADS1115(address=0x50, busnum=2)

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1

# Main loop.
while True:
    values = adc.read_adc(3, gain=GAIN)

    voltage = (values)*(510+1000)/1000 # Vbatt = Vmes(R1+R2)/R2 ( Resistance1 = 510; R2 = 1000k)
    # Print the ADC values.
    print("Voltage du robot : ", voltage, " v")
    # Pause for half a second.
    time.sleep(0.5)
