import time
import board
import digitalio
import busio


# Save this to a CircuitPython microcontroller as code.py.
# Uncomment the region you want to use and save the changes.
# These were demonstrated on an M4 Express board.

###################
print()
print("GPIO DEMO:")
###################

# pin = digitalio.DigitalInOut(board.D12)
# pin.direction = digitalio.Direction.OUTPUT

# while True:
#     pin.value = True
#     pin.value = False

##################
print()
print("PWM DEMO:")
##################

# import pwmio

# duty_cycle = 10
# converted_duty_cycle = int(duty_cycle * 65535 / 100)
# pin1 = pwmio.PWMOut(board.D12, frequency=int(100e3), duty_cycle=converted_duty_cycle)

# duty_cycle = 40
# converted_duty_cycle = int(duty_cycle * 65535 / 100)
# pin2 = pwmio.PWMOut(board.D13, frequency=int(100e3), duty_cycle=converted_duty_cycle)

# while True:
#     pass

###################
print()
print("UART DEMO:")
###################

# import adafruit_us100

# uart = busio.UART(board.TX, board.RX, baudrate=9600)
# us100 = adafruit_us100.US100(uart)

# duration = 0.01
# while True:
#     temp = us100.temperature
#     time.sleep(duration)
#     dist = us100.distance
#     if dist > 1000:
#         dist = 0
#     print((temp, dist))

##################
print()
print("I2C DEMO:")
##################

# import adafruit_mcp4728

# i2c = busio.I2C(board.SCL, board.SDA)
# mcp4728 = adafruit_mcp4728.MCP4728(i2c)
# MAX_VALUE = 65535

# channels = [
#     mcp4728.channel_a,
#     mcp4728.channel_b,
#     mcp4728.channel_c,
#     mcp4728.channel_d
# ]

# duration = 0.1
# while True:
#     for c in channels:
#         c.value = MAX_VALUE
#         time.sleep(duration)
#         c.value = 0
#         time.sleep(duration)

##################
print()
print("SPI DEMO:")
##################

# import adafruit_lis3dh

# spi = board.SPI()
# # For CS, have to pick any open digital pin:
# cs = digitalio.DigitalInOut(board.D7)
# lis3dh = adafruit_lis3dh.LIS3DH_SPI(spi, cs)

# duration = 0.1
# while True:
#     x, y, z = lis3dh.acceleration
#     print((x, y, z))
#     time.sleep(duration)

