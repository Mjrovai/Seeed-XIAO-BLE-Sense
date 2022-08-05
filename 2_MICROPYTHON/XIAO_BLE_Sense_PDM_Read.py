'''
SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
SPDX-License-Identifier: MIT
Adapted by Marcelo Rovai @August22
'''

import time
import array
import math
import board
import digitalio
import audiobusio

# turn on the microphone
micpwr = digitalio.DigitalInOut(board.MIC_PWR)
micpwr.direction = digitalio.Direction.OUTPUT
micpwr.value = True
time.sleep(0.1)

# Remove DC bias before computing RMS.
def mean(values):
    return sum(values) / len(values)

# Calculate the Normalized RMS value of samples
def normalized_rms(values):
    minbuf = int(mean(values))
    samples_sum = sum(
        float(sample - minbuf) * (sample - minbuf)
        for sample in values
    )
    return math.sqrt(samples_sum / len(values))

# Main program
mic = audiobusio.PDMIn(board.PDM_CLK, board.PDM_DATA, sample_rate=16000, bit_depth=16)
samples = array.array('H', [0] * 160)

while True:
    mic.record(samples, len(samples))
    magnitude = normalized_rms(samples)
    print((magnitude,))
    time.sleep(0.1)
