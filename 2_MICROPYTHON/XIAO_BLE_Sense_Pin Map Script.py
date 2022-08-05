'''
SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
SPDX-License-Identifier: MIT
Adapted by Marcelo Rovai @August22

CircuitPython Essentials Pin Map
'''
import microcontroller
import board

board_pins = []
for pin in dir(microcontroller.pin):
    if isinstance(getattr(microcontroller.pin, pin), microcontroller.Pin):
        pins = []
        for alias in dir(board):
            if getattr(board, alias) is getattr(microcontroller.pin, pin):
                pins.append("board.{}".format(alias))
        if len(pins) > 0:
            board_pins.append(" ".join(pins))
for pins in sorted(board_pins):
    print(pins)