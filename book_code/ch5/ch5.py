import pathlib
import subprocess

################################
print()
print("FORMATTING AND LINTING:")
################################

# This turns off black for these lines:
# fmt: off
a = ['1',
'2',
                  '3',
            '4']
print(
a
)

b=    2   + 2
print(b==4)

# This turns black on again:
# fmt: on
# This originally was the same code as above:
a = ["1", "2", "3", "4"]
print(a)

b = 2 + 2
print(b == 4)

#####################
print()
print("REFACTORING:")
#####################

# sourcery skip: list-comprehension
# before refactoring
y = []
for x in range(10):
    y.append(x ** 2)

# after refactoring
y = [x ** 2 for x in range(10)]

###############################
print()
print("TESTING:")
###############################

# Run `pytest` from repository top directory
# Tests are in book_code/test

###########################
print()
print("SHARING LIBRARIES:")
###########################

# See PyPI library "paraxial"

###############################
print()
print("SHARING APPLICATIONS:")
###############################

###############################
print()
print("OPTIMIZATION:")
###############################

import time

start = time.perf_counter_ns()
for _ in range(10000000):
    foo = 2 + 2
stop = time.perf_counter_ns()
print(f'Took {(stop-start)/1e9:g} seconds')

###############################
print()
print("COMMAND LINE INTERFACES:")
###############################

import sys

command_line_arguments = sys.argv
for arg in command_line_arguments:
    print(arg)

# run `python -m book_code.ch5.typer_demo [glass name] [wavelength]`
# For example `python -m book_code.ch5.typer_demo nbk7 0.5`

###############################
print()
print("GRAPHICAL USER INTERFACES:")
###############################

# run `python -m book_code.ch5.qt_demo`

# #########################################
# print()
# print("DRIVING OPTICAL DESIGN PROGRAMS:")
# #########################################

