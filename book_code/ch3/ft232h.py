import os
os.environ["BLINKA_FT232H"] = "1"

import time
import digitalio
import board

pin = digitalio.DigitalInOut(board.C0)
pin.direction = digitalio.Direction.OUTPUT

start = time.time()
while time.time() - start < 2:
    pin.value = not pin.value
pin.value = False

import busio
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)
mcp = MCP.MCP3008(spi, cs)
chan = AnalogIn(mcp, MCP.P0)

start = time.time()
while time.time() - start < 1:
    print(f"Raw ADC Value: {chan.value:g}")
    print(f"ADC Voltage: {chan.voltage:g} V")
    print()
    time.sleep(0.1)
