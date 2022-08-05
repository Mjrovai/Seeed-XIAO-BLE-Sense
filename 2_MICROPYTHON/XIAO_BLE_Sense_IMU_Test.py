'''
SPDX-FileCopyrightText: Copyright (c) 2020 Bryan Siepert for Adafruit Industries
SPDX-License-Identifier: MIT
Adapted by Marcelo Rovai @August22

XIAO BLE Sense IMU Test

NOTE: Important  to install library lib/adafruit_lsm6ds/
You can use CircUp CLI Tool to install and update libraries on your device. Follow instructions:
https://learn.adafruit.com/keep-your-circuitpython-libraries-on-devices-up-to-date-with-circup

'''
import time
import board
import digitalio
import busio
from adafruit_lsm6ds.lsm6ds3trc import LSM6DS3TRC

# On the Seeed XIAO Sense the LSM6DS3TR-C IMU is connected on a separate
# I2C bus and it has its own power pin that we need to enable.
imupwr = digitalio.DigitalInOut(board.IMU_PWR)
imupwr.direction = digitalio.Direction.OUTPUT
imupwr.value = True
time.sleep(0.1)

imu_i2c = busio.I2C(board.IMU_SCL, board.IMU_SDA)
sensor = LSM6DS3TRC(imu_i2c)

# To see data on Serial Monitor:
while True:
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (sensor.acceleration))
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f radians/s" % (sensor.gyro))
    print("")
    time.sleep(0.5)

# To see gyro signal on Plotter
#while True:
#    print(sensor.gyro)
#    time.sleep(0.1)

# To see accelerometer signal on Plotter
#while True:
#    print(sensor.acceleration)
#    time.sleep(0.1)


