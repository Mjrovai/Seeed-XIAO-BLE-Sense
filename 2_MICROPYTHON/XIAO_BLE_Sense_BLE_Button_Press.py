'''
SPDX-FileCopyrightText: 2019 Kattni Rembor for Adafruit Industries
SPDX-License-Identifier: MIT
Adapted by Marcelo Rovai @August22

Receiving Controlling PAD Via BLE  
Using Bluefruit LE Connect for iOS and Android
https://learn.adafruit.com/bluefruit-le-connect

The Bluefruit LE Connect app has a control pad with 8 buttons:
UP, DOWN, LEFT, RIGHT,
1, 2, 3, and 4.
This demo will show you how to access those buttons,
and use them to print a message to the serial console.
https://learn.adafruit.com/circuitpython-nrf52840/button-press

'''

from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

from adafruit_bluefruit_connect.packet import Packet
from adafruit_bluefruit_connect.button_packet import ButtonPacket

ble = BLERadio()
uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)

while True:
    ble.start_advertising(advertisement)
    while not ble.connected:
        pass

    # Now we're connected

    while ble.connected:
        if uart.in_waiting:
            packet = Packet.from_stream(uart)
            if isinstance(packet, ButtonPacket):
                if packet.pressed:
                    if packet.button == ButtonPacket.BUTTON_1:
                        # The 1 button was pressed.
                        print("1 button pressed!")
                    elif packet.button == ButtonPacket.BUTTON_2:
                        # The 2 button was pressed.
                        print("2 button pressed!")
                    elif packet.button == ButtonPacket.BUTTON_3:
                        # The 3 button was pressed.
                        print("3 button pressed!")
                    elif packet.button == ButtonPacket.BUTTON_4:
                        # The 4 button was pressed.
                        print("4 button pressed!")   
                    elif packet.button == ButtonPacket.UP:
                        # The UP button was pressed.
                        print("UP button pressed!")
                    elif packet.button == ButtonPacket.DOWN:
                        # The DOWN button was pressed.
                        print("DOWN button pressed!")
                    elif packet.button == ButtonPacket.LEFT:
                        # The LEFT button was pressed.
                        print("LEFT button pressed!")
                    elif packet.button == ButtonPacket.RIGHT:
                        # The RIGHT button was pressed.
                        print("RIGHT button pressed!") 

    # If we got here, we lost the connection. Go up to the top and start
    # advertising again and waiting for a connection.

