# Uncomment to make high-resolution images for print:
# import matplotlib
# matplotlib.rcParams['figure.dpi'] = 300

###############################
print()
print("VENDOR-AGNOSTIC LIBRARIES:")
###############################

"""
import time
import serial

print('Open the serial device')
ser = serial.Serial('COM4', baudrate=9600, timeout=1)

print('Send the command to set rotation velocity')
term = '\r'
cmd = '/1V20000R'
ser.write(f'{cmd}{term}'.encode('utf-8'))
time.sleep(0.1)

print('Send the command to rotate forwards 10000 encoder counts')
term = '\r'
cmd = '/1P10000R'
ser.write(f'{cmd}{term}'.encode('utf-8'))
time.sleep(0.1)

input()  # Hit enter once move finishes

print('Send the command to rotate backwards 10000 encoder counts')
term = '\r'
cmd = '/1D10000R'
ser.write(f'{cmd}{term}'.encode('utf-8'))
time.sleep(0.1)

input()  # Hit enter once move finishes
"""

###################################
print()
print("VENDOR-SPECIFIC LIBRARIES:")
###################################

"""
# Largely based on ps2000BlockExample.py from 
# PicoTech's picosdk-python-wrappers repository

import ctypes
import numpy as np
from picosdk.ps2000 import ps2000 as ps
import matplotlib.pyplot as plt
from picosdk.functions import adc2mV, assert_pico2000_ok

status = {"openUnit": ps.ps2000_open_unit()}
assert_pico2000_ok(status["openUnit"])
chandle = ctypes.c_int16(status["openUnit"])

# Set up channel A
channel = ps.PS2000_CHANNEL["PS2000_CHANNEL_A"]
enabled = True
coupling_type = ps.PICO_COUPLING["AC"]
chARange = ps.PS2000_VOLTAGE_RANGE["PS2000_5V"]
status["setChA"] = ps.ps2000_set_channel(
    chandle, channel, enabled, coupling_type, chARange
)
assert_pico2000_ok(status["setChA"])

# Set up single trigger
source = ps.PS2000_CHANNEL["PS2000_CHANNEL_A"]
threshold = 0  # ADC counts
direction = 0  # PS2000_RISING
delay = 0  # s
auto_Trigger = 1000  # ms
status["trigger"] = ps.ps2000_set_trigger(
    chandle, source, threshold, direction, delay, auto_Trigger
)
assert_pico2000_ok(status["trigger"])

# Set number of pre and post trigger samples to be collected
preTriggerSamples = 1000
postTriggerSamples = 1000
maxSamples = preTriggerSamples + postTriggerSamples

# Get timebase information
timebase = 8
timeInterval = ctypes.c_int32()
timeUnits = ctypes.c_int32()
oversample = ctypes.c_int16(1)
maxSamplesReturn = ctypes.c_int32()
status["getTimebase"] = ps.ps2000_get_timebase(
    chandle,
    timebase,
    maxSamples,
    ctypes.byref(timeInterval),
    ctypes.byref(timeUnits),
    oversample,
    ctypes.byref(maxSamplesReturn),
)
assert_pico2000_ok(status["getTimebase"])

# Run block capture
timeIndisposedms = ctypes.c_int32()
status["runBlock"] = ps.ps2000_run_block(
    chandle,
    maxSamples,
    timebase,
    oversample,
    ctypes.byref(timeIndisposedms),
)
assert_pico2000_ok(status["runBlock"])

# Check for data collection to finish
ready = ctypes.c_int16(0)
check = ctypes.c_int16(0)
while ready.value == check.value:
    status["isReady"] = ps.ps2000_ready(chandle)
    ready = ctypes.c_int16(status["isReady"])

# Create buffers ready for data
bufferA = (ctypes.c_int16 * maxSamples)()
bufferB = (ctypes.c_int16 * maxSamples)()

# Get data from scope
cmaxSamples = ctypes.c_int32(maxSamples)
status["getValues"] = ps.ps2000_get_values(
    chandle,
    ctypes.byref(bufferA),
    ctypes.byref(bufferB),
    None,
    None,
    ctypes.byref(oversample),
    cmaxSamples,
)
assert_pico2000_ok(status["getValues"])

maxADC = ctypes.c_int16(32767)
adc2mVChA = adc2mV(bufferA, chARange, maxADC)
ChA_in_V = [mV / 1000 for mV in adc2mVChA]

time = np.linspace(
    0, (cmaxSamples.value) * timeInterval.value, cmaxSamples.value
)

plt.plot(time / 1e6, ChA_in_V)
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (V)")
plt.grid()
plt.show()

import pathlib

script_dir = pathlib.Path(__file__).parent
file_name = script_dir / "scope_trace.csv"
import csv

with open(file_name, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Time (ms)", "Voltage (V)"])
    for row in zip(time / 1e6, ChA_in_V):
        writer.writerow(row)

# Stop the scope
status["stop"] = ps.ps2000_stop(chandle)
assert_pico2000_ok(status["stop"])

# Close the scope
status["close"] = ps.ps2000_close_unit(chandle)
assert_pico2000_ok(status["close"])
"""

###############################
print()
print("STICKING POINTS:")
###############################

print(f"Should be true: {255 == 0xff == 0b11111111}")

# If you uncomment these, Python may not run the file:
# foo = 0b2
# bar = 0xg

print("Should all be int:")
print(type(0b1111))
print(type(0xF))
print(type(15))

print(f"Math with hex: {0x2} + {0xa} = {0x2 + 0xa}")
print(f"More math with hex: {0x2} x {0xa} = {0x2 * 0xa}")
print(f"Math with binary: {0b0110} + {0b0010} = {0b0110 + 0b0010}")

print('Typing "10" in different bases:')
print(f"0b10: {0b10}")
print(f"0o10: {0o10}")
print(f"10: {10}")
print(f"0x10: {0x10}")


a = [10, 20, 30, 40]
print(bytes(a))

print("Output of chr(13):")
print(chr(13))

# We need the double-slash here so we print the literal text "\r":
print('Output of ord("\\r"):')
print(ord("\r"))

for c in a:
    print(repr(chr(c)))

maybe_a_number = b"384"
print(int(maybe_a_number))
print(list(maybe_a_number))

maybe_a_number = b"abc"
try:
    print(int(maybe_a_number))
except ValueError:
    print("Casting to int failed")
print(list(maybe_a_number))


print(0xDEADBEEF)
list_of_values = [0xDE, 0xAD, 0xBE, 0xEF]
print(list_of_values)
print(bytes(list_of_values))
print(bytes(list_of_values).hex())
print(int(bytes(list_of_values).hex(), base=16))
print()


number = 1635
print(f"In plain form: {number}")
# Use the format specifier "x" to turn
# a number into a hex string in one step:
print(f"Hex string version: {number:x}")
print(f"These are equivalent: {0x663 == number = }")
print()

print(f"Result of calling hex on number: {hex(number)}")
# Similar to base-10 numbers, we can split this into two parts:
print(f"{0x663 == 0x600 + 0x63 = }")
# We can use the divmod function to split the number for us:
print(f"{divmod(number, 0x100) = }")
# divmod split it into an 0x100 term (0x600) and
# a remainder 0x10 term (0x63):
print(f"{number == 0x100 * 6 + 99 = }")
print()

# Now we can turn this split number into bytes:
print(bytes(divmod(number, 0x100)))
# If we cast to a list, we see the same factors from divmod:
print(list(bytes(divmod(number, 0x100))))
# We can go back and forth between numbers and bytes:
number_as_bytes = bytes(divmod(number, 0x100))
print(number_as_bytes)
print(list(number_as_bytes))
back_to_list = list(number_as_bytes)
print(f"{back_to_list[0] * 0x100 + back_to_list[1] == number = }")
print()

from cProfile import label
import struct

num = 2**32 - 1
print(num)
num_split_into_bytes = struct.pack("<I", num)
print(num_split_into_bytes)
back_to_num = struct.unpack("<I", num_split_into_bytes)
print(back_to_num)
print()

# Works as expected:
print(0xA)

# When creating bytes, Python demands two values after \x:
# print(b'\xa')  # raises SyntaxError if uncommented
print(b"\x0a")  # using 0 to satisfy format requirement

# We can use list() to get a cleaner output:
print(list(b"\x0a"))

# If we replace \ with 0 as works for numbers, Python no
# longer interprets the value as a byte:
print(list(b"0x0a"))

###################################
print()
print("EMBEDDED DEVICE PROTOCOLS:")
###################################

# See protocols.py

############################
print()
print("EMBEDDED PLATFORMS:")
############################

# See files for relevant platforms

###############################
print()
print("SIGNAL PROCESSING 1:")
###############################

# Read sine trace using csv module:
import csv
import time
import pathlib
import numpy as np

# Grab the directory with chapter three's data:
data_dir = pathlib.Path(__file__).parent / "data"

start = time.time_ns()
with open(data_dir / "scope_trace.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)
    data_csv = []
    header = next(reader)
    for row in reader:
        data_csv.append([float(r) for r in row])
data_csv = np.array(data_csv)
stop = time.time_ns()

print(data_csv)
print(data_csv.shape)
print(header)
print(f"Took {(stop-start) / 1e9:g} s to read")
print()

# Can use pandas to do it in fewer lines:
import pandas

start = time.time_ns()
df = pandas.read_csv(data_dir / "scope_trace.csv")
data_pandas = df.values
stop = time.time_ns()

print(f"Took {(stop-start) / 1e9:g} s to read")
print(f"Results match: {np.allclose(data_csv, data_pandas)}")
print()

import matplotlib.pyplot as plt

x, y = data_pandas.T
plt.figure()
plt.plot(x, y, "b")
plt.title("Trace of basic sine generator")
plt.xlabel(header[0])
plt.ylabel(header[1])
plt.grid()
# plt.show()

# Fit the curve with a sine and give some figure of merit:
colors = ["#162C40", "#2D7337", "#A6774E", "#D996CE", "#C4DDF2"]
import scipy.optimize as spo


def fit_func(x, a, b, c, d):
    return a * np.sin(2 * np.pi * b * x - c) + d


p0 = [np.max(y), 1, 0.1, 0.1]  # initial parameters
bounds = ((0, 0, 0, -np.inf), (np.inf, np.inf, 360, np.inf))
popt, pcov = spo.curve_fit(fit_func, x, y, p0=p0, bounds=bounds)

y_fit = fit_func(x, *popt)

print(
    f"Fit parameters:\n"
    f"    Amplitude: {popt[0]:g} V\n"
    f"    Frequency: {popt[1]:g} kHz\n"
    f"    Phase offset: {np.rad2deg(popt[2]):g}°\n"
    f"    Amplitude offset: {popt[3] * 1e3:g} mV\n"
)

plt.figure()
plt.plot(x, y, label="Data", color=colors[0])
plt.plot(x, y_fit, label="Fit", color=colors[3])
plt.title("Curve fit of basic sine generator")
plt.xlabel(header[0])
plt.ylabel(header[1])
plt.legend()
plt.grid()
# plt.show()

# Plot the residuals of the curve fit:
resid = y - y_fit

plt.figure()
plt.plot(x, resid, color=colors[1])
plt.title("Residuals of curve fit")
plt.xlabel(header[0])
plt.ylabel(header[1])
plt.grid()
plt.show()

# You can calculate the standard deviation:
print(f"{np.sqrt(np.mean(resid**2)):g} V")
# NumPy also has a built-in function for it:
print(f"{np.std(resid):g} V")
print()

counts, bins = np.histogram(resid, bins=32)
plt.hist(bins[:-1], bins, weights=counts)
plt.title("Histogram of curve fit residuals")
plt.xlabel(header[1])
plt.ylabel("Counts")
plt.grid()
plt.show()

# Plot the frequency spectrum:
# We can use a loop to plot the same data on two figures at different scales:
x /= 1e3  # ms to s
dt = x[1] - x[0]
df = 1 / dt
zero_padding = 2**13

import scipy.signal as sig

titles = ["Magnitude spectrum", "Zoomed in magnitude spectrum"]
horiz_limits = [(0, 200e3), (0, 10e3)]
for idx in range(2):
    plt.figure()
    plt.magnitude_spectrum(
        y_fit,
        Fs=df,
        pad_to=zero_padding,
        scale="dB",
        label="Fit",
        color=colors[3],
    )
    plt.magnitude_spectrum(
        y_fit * sig.windows.hann(len(y_fit)),
        Fs=df,
        pad_to=zero_padding,
        scale="dB",
        label="Windowed fit",
        color=colors[2],
    )
    plt.magnitude_spectrum(
        resid,
        Fs=df,
        pad_to=zero_padding,
        scale="dB",
        label="Residuals",
        color=colors[1],
    )
    plt.magnitude_spectrum(
        y,
        Fs=df,
        pad_to=zero_padding,
        scale="dB",
        label="Sine trace",
        color=colors[0],
    )
    plt.grid()
    plt.legend()
    plt.xlabel("Hz")
    plt.ylim(-90, 10)
    plt.yticks([-90, -80, -70, -60, -50, -40, -30, -20, -10, 0, 10])
    plt.xlim(horiz_limits[idx])
    plt.title(titles[idx])
plt.show()

###############################
print()
print("SIGNAL PROCESSING 2:")
###############################

# Repeat on sine from PicoScope measured by Pi:
with open(data_dir / "mcp3008_trace.txt", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=" ")
    next(reader)
    data_csv = [[float(r) for r in row] for row in reader]
data_csv = np.array(data_csv)
x, y = data_csv.T
x *= 1e3  # s to ms

p0 = [np.max(y), 0.5, 0.1, np.mean(y)]
bounds = ((0, 0, 0, -np.inf), (np.inf, np.inf, 360, np.inf))
popt, pcov = spo.curve_fit(fit_func, x, y, p0=p0, bounds=bounds)

y_fit = fit_func(x, *popt)

print(
    f"Fit parameters:\n"
    f"    Amplitude: {popt[0]:g} V\n"
    f"    Frequency: {popt[1]:g} kHz\n"
    f"    Phase offset: {np.rad2deg(popt[2]):g}°\n"
    f"    Amplitude offset: {popt[3] * 1e3:g} mV\n"
)

plt.figure()
plt.plot(x, y, ".", label="Data", color=colors[0])
plt.plot(x, y_fit, label="Fit", color=colors[3])
plt.title("Trace measured using MCP3008")
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (V)")
plt.legend()
plt.grid()

resid = y - y_fit

plt.figure()
plt.plot(x, resid, color=colors[1])
plt.title("Residuals of curve fit")
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (V)")
plt.grid()
plt.show()

counts, bins = np.histogram(resid, bins=32)
plt.hist(bins[:-1], bins, weights=counts)
plt.title("Histogram of curve fit residuals")
plt.xlabel("Voltage (V)")
plt.ylabel("Counts")
plt.grid()
plt.show()

f = np.linspace(0.001, 1 * 2 * np.pi, 1024)
psd = sig.lombscargle(
    x.astype(np.float64),
    y.astype(np.float64),
    f.astype(np.float64),
    precenter=True,
    normalize=True,
)
plt.figure()
plt.plot(f / (2 * np.pi), psd, color=colors[0])
plt.title("Power Spectral Density by Lomb-Scargle Algorithm")
plt.xlabel("Frequency (kHz)")
plt.ylabel("Normalized amplitude")
plt.grid()
plt.show()

peak_freq = f[np.argmax(psd)] / (2 * np.pi)
print(f"Frequency from Lomb-Scargle: {peak_freq:g} kHz")

############################
print()
print("IMAGE PROCESSING 1:")
############################

import cv2
img = cv2.imread(str(data_dir / "openmv images" / "laser diode.bmp"))
cv2.imshow("Beam from laser diode", img)
cv2.waitKey()
cv2.destroyAllWindows()

############################
print()
print("IMAGE PROCESSING 2:")
############################

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

h, w = gray.shape
vert = np.linspace(-h // 2, h // 2, h)
horiz = np.linspace(-w // 2, w // 2, w)

plt.plot(horiz, gray[h // 2, :], label="Horizontal slice")
plt.plot(vert, gray[:, w // 2], label="Vertical slice")
plt.xlabel("Pixel number")
plt.ylabel("Pixel brightness")
plt.title("Beam slices")
plt.legend()
plt.grid()
plt.show()

############################
print()
print("IMAGE PROCESSING 3:")
############################

# Set pixels with value 30 or lower to zero:
mask = gray < 30
gray[mask] = 0

hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.semilogy(hist, label='Original')
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
plt.semilogy(hist, label='Masked')
plt.xlabel("Pixel brightness")
plt.ylabel("Number of pixels")
plt.title("Histogram of masked beam")
plt.legend()
plt.grid()
plt.show()

############################
print()
print("IMAGE PROCESSING 4:")
############################

beam_moments = cv2.moments(gray)
cen_x = beam_moments["m10"] / beam_moments["m00"]
cen_y = beam_moments["m01"] / beam_moments["m00"]
print(f'Beam centroid: {cen_x:g}, {cen_y:g}')

# Mark the centroid with a red cross:
thickness = 2
cv2.line(
    img,
    (int(cen_x) - 5, int(cen_y)),
    (int(cen_x) + 5, int(cen_y)),
    (0, 0, 255),
    thickness,
)
cv2.line(
    img,
    (int(cen_x), int(cen_y) - 5),
    (int(cen_x), int(cen_y) + 5),
    (0, 0, 255),
    thickness,
)

# Threshold the image from grayscale to only values of 0 and 255:
_, thresh = cv2.threshold(gray, 25, 255, 0)
cv2.imshow('Thresholded image', thresh)
cv2.waitKey()
cv2.destroyAllWindows()

# Use the threshold image to find contours:
cont, _ = cv2.findContours(
    thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
)

# Filter to remove any spurious small contours:
main_cont = [c for c in cont if cv2.contourArea(c) > 100]

# Draw the contour on the image in blue:
cv2.drawContours(img, main_cont, 0, (255, 0, 0), 2)

# Fit an ellipse to the contour:
ellipse = cv2.fitEllipse(main_cont[0])
center = ellipse[0]
dims = ellipse[1]
roll = ellipse[2]
print('Ellipse fit to beam edges:')
print(f'{center = }')
print(f'{dims = }')
print(f'{roll = }')

# Draw the ellipse on the image in green:
cv2.ellipse(img, ellipse, (0, 255, 0), 2)
cv2.imshow("Annotated beam", img)
cv2.waitKey()
cv2.destroyAllWindows()

############################
print()
print("IMAGE PROCESSING 5:")
############################

test_image = np.ones(gray.shape) * 20
test_image[h//4:3*h//4, w//4:3*w//4] = 200
test_image += np.random.normal(0, 10, test_image.shape)
test_image = test_image.astype(np.uint8)

scale = 11
gaussian_blur = cv2.GaussianBlur(test_image, (scale, scale), None)
median_blur = cv2.medianBlur(test_image, scale)
bilat_blur = cv2.bilateralFilter(test_image, 9, scale, scale)

# Plot the filtered images:
cv2.imshow('Bilateral filter', bilat_blur)
cv2.imshow('Gaussian filter', gaussian_blur)
cv2.imshow('Original', test_image)
cv2.imshow('Median filter', median_blur)
cv2.waitKey()
cv2.destroyAllWindows()

# View superimposed image slices:
plt.plot(vert, test_image[:, w // 2], label="Original")
plt.plot(vert, gaussian_blur[:, w // 2], label="Gaussian filter")
plt.plot(vert, median_blur[:, w // 2], label="Median filter")
plt.plot(vert, bilat_blur[:, w // 2], label="Bilateral filter")
plt.xlabel("Pixel number")
plt.ylabel("Pixel brightness")
plt.title("Beam slices")
plt.xlim(90, 150)
plt.legend()
plt.grid()
plt.show()

############################
print()
print("IMAGE PROCESSING 6:")
############################

# Reload the image to remove annotations:
img = cv2.imread(str(data_dir / "openmv images" / "laser diode.bmp"))
cv2.imshow('Image', img)
cv2.imshow('Image + 60', img+60)
cv2.imshow('Image + 200', img+200)
cv2.waitKey()
cv2.destroyAllWindows()

###########################
print()
print("EXAMPLE SYSTEMS 1:")
###########################

# Lock-In Measurement: see last section of m4e.py
data = pandas.read_csv(data_dir / "lock_in.txt", skiprows=1).values
seconds = data[:, 0] / 1e9  # ns to s
volts = data[:, 1]

plt.figure()
plt.plot(seconds, volts, '.-')
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('Lock-In Measurement of Chopped Signal')

# Trouble is, the sample spacing is non-uniform:
spacing = np.diff(seconds)
plt.figure()
plt.plot(spacing * 1e6, '.')
plt.xlabel('Sample number')
plt.ylabel('Time between measurements (µs)')
plt.grid()
plt.title('Variation in sample spacing over time')

# All samples are either 122µs or 244µs apart.
# Boards that support the analogbufio module can
# ensure uniform sample spacing, but we can use the 
# Lomb-Scargle transform for simplicity:
f = np.linspace(0.001, 1e3 * 2 * np.pi, 1024)
psd = sig.lombscargle(
    seconds.astype(np.float64),
    volts.astype(np.float64),
    f.astype(np.float64),
    precenter=True,
    normalize=True,
)
plt.figure()
plt.plot(f / (2 * np.pi), psd, color=colors[0])
plt.title("Power Spectral Density by Lomb-Scargle Algorithm")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Normalized amplitude")
plt.grid()
plt.show()
peak_freq = f[np.argmax(psd)] / (2 * np.pi)
print(f"Frequency from Lomb-Scargle: {peak_freq:g} Hz")

###########################
print()
print("EXAMPLE SYSTEMS 2:")
###########################

# MTF measurement from Air Force target
# Image was recorded using OpenMV IDE
img = cv2.imread(str(data_dir / "openmv images" / "usaf.png"))
cv2.imshow("USAF Resolution Test Target", img)
cv2.waitKey()
cv2.destroyAllWindows()

h, w, _ = img.shape
print(f"Image is {h} x {w} with BGR channels: {img.shape}")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(f"Grayscale has same dimensions but 1 channel: {gray.shape}")
print()

# Use large center black square to set normalization:
black_roi = (35, 80, 105, 140)
white_roi = (150, 190, 70, 100)

# First slicing index is columns (y), second is rows (x)
black_square = gray[
    black_roi[0] : black_roi[1], black_roi[2] : black_roi[3]
]
white_square = gray[
    white_roi[0] : white_roi[1], white_roi[2] : white_roi[3]
]
norm_min = np.mean(black_square)
norm_max = np.mean(white_square)
DC_contrast = (norm_max - norm_min) / (norm_max + norm_min)
print(f"Measured baseline contrast: {DC_contrast:g}")

# Spatial frequencies of bar sections:
freqs = [2 ** (G + E / 6) for G in [-2, -1] for E in range(6)]

# Only doing the horizontal sections for simplicity:
# Ordered as column1, column2, row1, row2
regions = [
    (160, 200, 160, 190),
    (25, 63, 10, 35),
    (70, 105, 10, 30),
    (110, 140, 10, 30),
    (145, 172, 10, 28),
    (175, 196, 12, 25),
    (27, 48, 183, 196),
    (53, 72, 184, 195),
    (76, 93, 185, 195),
    (97, 112, 186, 195),
    (114, 129, 185, 196),
    (130, 143, 188, 194),
]

# cv2.rectangle() uses x, y ordering:
cv2.rectangle(
    img,
    (black_roi[2], black_roi[0]),
    (black_roi[3], black_roi[1]),
    (255, 0, 0),
    2,
)
cv2.rectangle(
    img,
    (white_roi[2], white_roi[0]),
    (white_roi[3], white_roi[1]),
    (0, 0, 255),
    2,
)
cv2.imshow("Regions used to set contrast at 0 lp/mm", img)
cv2.waitKey()
cv2.destroyAllWindows()

for roi in regions:
    cv2.rectangle(
        img, (roi[2], roi[0]), (roi[3], roi[1]), (0, 255, 0), 2
    )
    cv2.imshow("Sections of USAF to sample MTF", img)
    cv2.waitKey()
cv2.destroyAllWindows()

# Essentially a sine wave with an amplitude limit
def fit_func(x, amp, freq, phase, offset, clamp_amp):
    ret = amp * np.sin(2 * np.pi * freq * x - phase) + offset
    ret[ret > offset + clamp_amp] = offset + clamp_amp
    ret[ret < offset - clamp_amp] = offset - clamp_amp
    return ret

mtf = []

bounds = ((0, 0, -np.pi, 0, 0), (np.inf, np.inf, np.pi, 255, 255))

for idx, roi in enumerate(regions):
    sample = gray[roi[0] : roi[1], roi[2] : roi[3]]
    summed_columns = np.mean(sample, axis=-1)

    x = np.array(range(len(summed_columns)))
    y = summed_columns

    amp_est = clamp_est = (np.max(y) - np.min(y)) / 2
    freq_est = 3 / len(y)
    phase_est = (np.mean(y) - y[0]) / np.mean(y) * np.pi / 2
    offset_est = np.mean(y)
    p0 = (amp_est, freq_est, phase_est, offset_est, clamp_est)

    popt, _ = spo.curve_fit(fit_func, x, y, p0=p0, bounds=bounds)
    y_fit = fit_func(x, *popt)

    plt.figure()
    plt.plot(
        x,
        y,
        "x",
        color=colors[0],
    )
    plt.plot(x, y_fit, "-", color=colors[2], label="Curve fit")
    plt.xlabel('Pixel number')
    plt.ylabel('Pixel value')
    plt.title(f"Contrast of slice of {freqs[idx]:.3g} lp/mm")
    plt.legend()
    plt.grid()
    plt.show()

    contrast = popt[-1] / popt[-2]
    normalized_contrast = contrast / DC_contrast
    mtf.append(normalized_contrast)

freqs = [0] + freqs
mtf = [1] + mtf
plt.plot(freqs, mtf, "x-", color=colors[1])
plt.title("Measurement of square-wave MTF")
plt.xlabel("Spatial frequency (lp/mm)")
plt.ylabel("Contrast")
plt.ylim([0, 1.1])
plt.grid()
plt.show()
