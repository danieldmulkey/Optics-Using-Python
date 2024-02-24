from pyb import Pin

p_out = Pin('P7', Pin.OUT_PP)
# Uncomment this to test GPIO:
# while True:
    # p_out.high()
    # p_out.low()

#################

import time
from pyb import Timer

p = Pin('P4') # P4 has TIM2, CH3
tim = Timer(2, freq=int(1e6))
ch = tim.channel(3, Timer.PWM, pin=p)
ch.pulse_width_percent(50)

i = 10
sign = 1
# Uncomment this to test PWM:
# while True:
#     ch.pulse_width_percent(i)
#     i += sign
#     if i < 10 or i > 90:
#         sign *= -1
#     time.sleep(0.01)

#################

from pyb import LED

leds = LED(1), LED(2), LED(3)# , LED(4)
for L in leds * 3:
    L.toggle()
    time.sleep(0.25)

#################

import sensor

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.VGA)
sensor.skip_frames()

start = time.time()
while time.time() - start < 10:
    img = sensor.snapshot()

# If you add an SD card, OpenMV can save images:
# img.save("dots.bmp")

#################

# This is based OpenMV's "Single Color Grayscale Blob Tracking" example
import math

sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.VGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False)  # off for color tracking
sensor.set_auto_whitebal(False)  # off for color tracking
clock = time.clock()

thresholds = (127, 255)
while(True):
    clock.tick()
    img = sensor.snapshot()
    for blob in img.find_blobs([thresholds], pixels_threshold=100, 
                            area_threshold=100, merge=True):
        if blob.elongation() > 0.5:
            img.draw_edges(blob.min_corners(), color=0)
            img.draw_line(blob.major_axis_line(), color=0)
            img.draw_line(blob.minor_axis_line(), color=0)
        img.draw_rectangle(blob.rect(), color=127)
        img.draw_cross(blob.cx(), blob.cy(), color=127)
        img.draw_keypoints([(blob.cx(), blob.cy(), 
                            int(math.degrees(blob.rotation())))], 
                            size=40, color=127)
    print(clock.fps())

