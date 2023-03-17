#!/usr/bin/python
# Read temperatures (using multiple MAX31855), log to a text file, and the cloud (through Thingspeak)
# Author contributions: Jason Stafford (Imperial College, University of Birmingham), Tony DiCola (Adafruit tutorial) 
# Updated by JS on 26-Dec-2021 (j.stafford@bham.ac.uk)

# For MAX31855 Adafruit tutorial snippets:
# Copyright (c) 2014 Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# Can enable debug output by uncommenting:
#import logging
#logging.basicConfig(level=logging.DEBUG)

import time
from datetime import datetime
import Adafruit_GPIO.SPI as SPI
import Adafruit_MAX31855.MAX31855 as MAX31855


# Uncomment one of the blocks of code below to configure your Pi to use
# software or hardware SPI.

# Raspberry Pi software SPI configuration.
CLK = 25
CS1  = 4
DO  = 18

CS2 = 24
CS3 = 12

sensor1 = MAX31855.MAX31855(CLK, CS1, DO)
sensor2 = MAX31855.MAX31855(CLK, CS2, DO)
sensor3 = MAX31855.MAX31855(CLK, CS3, DO)


# Raspberry Pi hardware SPI configuration.
#SPI_PORT   = 0
#SPI_DEVICE = 0
#sensor = MAX31855.MAX31855(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


# Loop printing measurements every second.

while True:
    T1 = sensor1.readTempC()
    T1_internal = sensor1.readInternalC()
    T2 = sensor2.readTempC()
    T2_internal = sensor2.readInternalC()
    T3 = sensor3.readTempC()
    T3_internal = sensor3.readInternalC()

    # get time with HH:MM:SS.%f
    t = datetime.now().strftime('%H:%M:%S.%f')

    # Open the data file and append to it
    fh = open("TemperatureData.txt", 'a+')

    # Arrange the data to be written
    data = "{} {} {} {} {} {} {}\n".format(t, T1, T2, T3, T1_internal, T2_internal, T3_internal)

    # Write data to file
    fh.write(data)
    # sleep for 1 seconds
    time.sleep(1)
    # Close the file
    fh.close
