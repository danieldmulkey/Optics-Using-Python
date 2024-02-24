import board
import digitalio

pin = digitalio.DigitalInOut(board.D6)
pin.direction = digitalio.Direction.OUTPUT
# Uncomment this to test GPIO:
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

import adafruit_hts221

i2c = board.I2C()
hts = adafruit_hts221.HTS221(i2c)

while True:
    rh = hts.relative_humidity
    T = hts.temperature
    print("Relative Humidity: {:.2f} % rH".format(rh))
    print("Temperature: {:.2f} C".format(T))
    print("")
    time.sleep(1)
