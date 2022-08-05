"""
Example for XIAO BLE. Blinks the built-in REG LED.
Marcelo Rovai @Aug22
"""

import time
import board
import digitalio

ledR = digitalio.DigitalInOut(board.LED_RED)
ledR.direction = digitalio.Direction.OUTPUT

ledG = digitalio.DigitalInOut(board.LED_GREEN)
ledG.direction = digitalio.Direction.OUTPUT

ledB = digitalio.DigitalInOut(board.LED_BLUE)
ledB.direction = digitalio.Direction.OUTPUT

def led_off():
    ledR.value = True
    ledG.value = True
    ledB.value = True

led_off()
while True:
    ledR.value = False
    print("Red On")
    time.sleep(1.0)
    led_off()
    time.sleep(1.0)
    ledG.value = False
    print("Green On")
    time.sleep(1.0)
    led_off()
    time.sleep(1.0)
    ledB.value = False
    print("Blue On")
    time.sleep(1.0)
    led_off()
    time.sleep(1.0)
