import time
from pyb import Pin

pin = Pin("X1", Pin.OUT_PP)
# This runs fastest with a "while True" statement,
# but that never terminates so here it is altered:
# while True:
now = time.time()
while (time.time() - now) < 5:
    # These are cascaded so you can see the delay 
    # caused by the check inside the "while loop"
    pin.high()
    pin.low()
    pin.high()
    pin.low()


from pyb import Timer

p = Pin("X1")
t = Timer(2, freq=int(1e6))
ch = t.channel(1, Timer.PWM, pin=p)
i = 10
sign = 1
now = time.time()
while (time.time() - now) < 5:
    ch.pulse_width_percent(i)
    i += sign
    if i < 10 or i > 90:
        sign *= -1
    time.sleep(0.01)


from pyb import LED

for v in list(range(4)) * 4:
    led = LED(v + 1)
    led.toggle()
    time.sleep(0.1)


from pyb import Accel

accel = Accel()
with open("acc.txt", "w") as fout:
    fout.write("X Y Z\n")
    led = LED(1)
    now = time.time()
    while (time.time() - now) < 5:
        fout.write(str(accel.x()) 
            + " " + str(accel.y()) 
            + " " + str(accel.z()) + "\n")
        led.toggle()
        time.sleep(0.5)


from pyb import DAC, ADC

dac = DAC(Pin("X5"))
adc = ADC(Pin("X6"))

v_out = 2
val_out = int(round(v_out / 3.3 * 255))
dac.write(val_out)
val_in = adc.read()
v_in = val_in / 4095 * 3.3

with open("dac_to_adc.txt", "w") as fout:
    fout.write("DAC output (V) " + str(v_out) + "\n")
    fout.write("ADC input (V) " + str(v_in))

