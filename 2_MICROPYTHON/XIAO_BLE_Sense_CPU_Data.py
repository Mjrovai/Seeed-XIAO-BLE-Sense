"""
XIAO BLE Sense - CPU data
"""
import microcontroller
print("\n")
print ("pin/status\n")
for i in dir(microcontroller):
    print(i)
print("\n")
for i in dir(microcontroller.cpu):
    print(i)
print("\n")

print("CPU Clock Freq: {} Mega Hertz".format(microcontroller.cpu.frequency/1000000))
print("CPU Voltage: {} volts".format(round(microcontroller.cpu.voltage, 1)))
print("CPU Temp: {} oC".format(microcontroller.cpu.temperature))