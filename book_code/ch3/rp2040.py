import board
import digitalio

pin = digitalio.DigitalInOut(board.D1)
pin.direction = digitalio.Direction.OUTPUT
# Uncomment to switch GPIO pin:
# while True:
#     pin.value = True
#     pin.value = False

#################

import time
import pwmio

duty_cycle = 10
duty_cycle_int = int(duty_cycle * 65535 / 100)
pwm = pwmio.PWMOut(
    board.D1, frequency=int(1e6), duty_cycle=duty_cycle_int
)

i = 10
sign = 1
# Uncomment this to test PWM:
# while True:
#     pwm.duty_cycle = int(i * 65535 / 100)
#     i += sign
#     if i < 10 or i > 90:
#         sign *= -1
#     time.sleep(0.01)

#################

print()
print()
trials = 300000
start = time.monotonic_ns()
for _ in range(trials):
    integer = 1 + 2
stop = time.monotonic_ns()
print("Integer math time (s):")
print((stop - start) / 1e9)

start = time.monotonic_ns()
for _ in range(trials):
    floating_point = 1.0 + 2.0
stop = time.monotonic_ns()
print("Floating-point math time (s):")
print((stop - start) / 1e9)
print()
# Pause to read values in terminal:
time.sleep(2)

#################

import busio
import math

i2c = busio.I2C(board.SCL, board.SDA)
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

ads = ADS.ADS1015(i2c)
chan = AnalogIn(ads, ADS.P3)

V_bias = 3.3

# Thermistor properties:
R_ref = 470e3
R25 = 470e3
A1 = 3.354016e-03
B1 = 2.264097e-04
C1 = 3.278184e-06
D1 = 1.097628e-07


def R_to_T(Rth):
    return (
        A1
        + B1 * math.log(Rth / R25)
        + C1 * math.log(Rth / R25) ** 2
        + D1 * math.log(Rth / R25) ** 3
    ) ** -1


for _ in range(10):
    V_meas = chan.voltage
    Rth_meas = R_ref * (V_bias / V_meas - 1)

    T_meas = R_to_T(Rth_meas)
    T_meas = T_meas - 273.15  # K to °C

    print("Thermistor measured temperature (°C) {}".format(T_meas))
    time.sleep(0.1)
