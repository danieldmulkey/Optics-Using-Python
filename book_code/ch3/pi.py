import time
from gpiozero import OutputDevice

pin = OutputDevice(21)
start = time.time()
while time.time() - start < 2:
    pin.on()
    pin.off()

from picamera import PiCamera
camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
time.sleep(5)
camera.capture('big_squares.png')
camera.stop_preview()
camera.close()

import numpy as np
from gpiozero import MCP3008

pin = MCP3008(channel=0)

L = 128
raw_times = np.empty(L)
raw_data = np.empty(L)
for idx in range(L):
    raw_times[idx] = time.time_ns()
    raw_data[idx] = pin.value

raw_times -= raw_times[0]  # start from 0
raw_times *= 1e-9  # ns to s

signal = np.hstack((raw_times.reshape(-1, 1),
    raw_data.reshape(-1, 1)))
np.savetxt('mcp3008_trace.txt', signal)
