# Contents of boot.py:

"""
import board
import digitalio
import storage

switch = digitalio.DigitalInOut(board.D0)

switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

# If the switch pin is connected to ground CircuitPython can write to the drive
storage.remount("/", switch.value)
"""

# Contents of code.py:
import board
import digitalio

pin = digitalio.DigitalInOut(board.D12)
pin.direction = digitalio.Direction.OUTPUT
# Uncomment to switch GPIO pin:
# while True:
#     pin.value = True
#     pin.value = False

#################

import time
import pwmio
from adafruit_motor import servo

pwm1 = pwmio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50)
serv = servo.Servo(pwm1)
serv.angle = 90
time.sleep(1)

for angle in range(0, 180, 5):
    serv.angle = angle
    time.sleep(0.05)
for angle in range(180, 0, -5):
    serv.angle = angle
    time.sleep(0.05)
serv.angle = 180
time.sleep(1)
serv.angle = 0
time.sleep(1)
serv.angle = 90

#################

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

dur = 0.1
for _ in range(10):
    led.value = True
    time.sleep(dur)
    led.value = False
    time.sleep(dur)

import adafruit_dotstar as dotstar

dots = dotstar.DotStar(
    board.DOTSTAR_CLOCK, board.DOTSTAR_DATA, 1, brightness=1
)

dur = 0.5
dots[0] = (255, 0, 0)
time.sleep(dur)
dots[0] = (0, 255, 0)
time.sleep(dur)
dots[0] = (0, 0, 255)
time.sleep(dur)
dots[0] = (255, 255, 0)
time.sleep(dur)
dots[0] = (255, 0, 255)
time.sleep(dur)
dots[0] = (0, 255, 255)
time.sleep(dur)
dots[0] = (255, 255, 255)
time.sleep(dur)
dots[0] = (0, 0, 0)

#################

# ulab provides NumPy-like arrays:
from ulab import numpy as np
from analogio import AnalogIn

analog_in = AnalogIn(board.A0)

L = 200
arr = np.empty((L, 2))

duty_cycle = 50
duty_cycle_int = int(duty_cycle / 100 * 65535)
pwm2 = pwmio.PWMOut(
    board.D2, frequency=int(1e5), duty_cycle=duty_cycle_int
)
time.sleep(0.1)

led.value = True
start = time.monotonic_ns()
for i in range(L):
    arr[i, 0] = time.monotonic_ns() - start
    arr[i, 1] = analog_in.value
led.value = False

# The error handling is derived from Adafruit's
# example on file writing:
try:
    dots[0] = (0, 255, 0)
    with open("/lock_in.txt", "w") as fout:
        fout.write("Time (ns),Voltage (V)\n")
        fout.flush()
        for i in range(L):
            fout.write("{0:f},{1:f}\n".format(
                arr[i, 0],
                arr[i, 1] * 3.3 / 65536)
            )
            fout.flush()
    dots[0] = (0, 0, 0)
except OSError as e:  # Occurs if  the file system is not writeable
    dots[0] = (255, 0, 0)
    if e.args[0] == 28:  # Occurs if the file system is full
        dots[0] = (0, 0, 255)
    while True:
        continue

