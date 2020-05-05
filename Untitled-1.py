"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Getting started with CPX and CircuitPython intro on:
https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library

Find example code for CPX on:
https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples
"""

import time
from adafruit_circuitplayground import cp

cp.pixels.auto_write = False
cp.pixels.brightness = 0.3

# Set these based on your ambient temperature in Celsius for best results!
minimum_temp = 24
maximum_temp = 30


def scale_range(value):
    """Scale a value from the range of minimum_temp to maximum_temp (temperature range) to 0-10
    (the number of NeoPixels). Allows remapping temperature value to pixel position."""
    return int((value - minimum_temp) / (maximum_temp - minimum_temp) * 10)


while True:
    peak = scale_range(cp.temperature)
    print(cp.temperature)
    print(int(peak))

    for i in range(10):
        if i <= peak:
            if peak < 5:
                print("cold!")
                cp.pixels[i] = (0, 255, 255)
            else:
                print("NOT cold yet")
                cp.pixels[i] = (255, 0, 0)
        else:
            cp.pixels[i] = (0, 0, 0)
    cp.pixels.show()
    time.sleep(0.05)
