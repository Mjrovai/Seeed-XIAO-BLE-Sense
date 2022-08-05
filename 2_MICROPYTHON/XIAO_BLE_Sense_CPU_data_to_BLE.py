'''
SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
SPDX-License-Identifier: MIT
Adapted by Marcelo Rovai @August22

Sending CPU data via BLE Connect UART

- To use, start this program, and start the Adafruit Bluefruit LE Connect app.
- Connect, and then select UART at app. Any text received FROM the connected device
  will be displayed. if the text received is:
  - "temperature", CPU temperature will be sent to app
  - "voltage", CPU voltage will be sent to app
  - "frequency", CPU frequency clock will be sent to app
'''

import microcontroller
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

ble = BLERadio()
uart_server = UARTService()
advertisement = ProvideServicesAdvertisement(uart_server)

while True:
    print("WAITING...")
    # Advertise when not connected.
    ble.start_advertising(advertisement)
    while not ble.connected:
        pass

    # Connected
    ble.stop_advertising()
    print("CONNECTED")

    # Loop and read packets
    while ble.connected:
        # INCOMING (RX) check for incoming text
        if uart_server.in_waiting:
            raw_bytes = uart_server.read(uart_server.in_waiting)
            text = raw_bytes.decode().strip().lower()
            # print("raw bytes =", raw_bytes)
            print("RX:", text)
            if text == 'temperature':
                text = "CPU Temp: {} oC\r\n".format(microcontroller.cpu.temperature)
                print("TX:", text.strip())
            elif text == 'voltage':
                text = "CPU Voltage: {} volts\r\n".format(round(microcontroller.cpu.voltage, 1))
                print("TX:", text.strip())
            elif text == 'frequency':
                text = "CPU Frequency: {} MHz\r\n".format(microcontroller.cpu.frequency/1000000)
                print("TX:", text.strip())
            uart_server.write(text.encode())

    # Disconnected
    print("DISCONNECTED")
