print("Hello, world!")

# fmt: off
#################
print()
print('STRINGS:')
#################

print("A simple string.")
print("The newline character\ninserts a line,")
print("but things may be more readable"
    + "\n"
    + "if split using string addition.")
print('Strings can be single-quoted '
    + "or double-quoted.")
print(
    """Triple-quotes give you
    multi-line strings."""
)

'A backslash before a quote tells Python that'
'your string isn\'t over yet. You can put a string'
'in a script, but without printing it won\'t show up.'
'If you start a string with single-quotes, you can put'
'double-quotes inside without ending the string.'
'Using the backslash is called "escaping," where you'
'escape the character\'s normal behavior.'

# Text that comes after a pound symbol is a comment. 
# Python doesn't execute comments,
# so they act as notes to the developer.
print()  # printing without arguments adds a newline to the output

f'This is called an f-string. Notice the f at the start'
f'The novelty here is that you can insert non-strings.'
f'Put whatever Python expression you want between curly braces'
f'and it will be evaluated and inserted.'
print(f'For example, {2} + {2} = {2 + 2}')
print(f'String formatting is powerful and deep.')

# fmt: on
################
print()
print("FLOATS:")
################

print(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1)
print(1)

#################
print()
print("COMPLEX:")
#################

print(1j)
print(1j ** 2)
print((-1) ** 0.5)

print(5j)
print(5j ** 2)

print(1 + 5j)
print((1 + 5j) * (1 - 5j))

###############
print()
print("BOOLS:")
###############

# True and False are special keywords
# Capitalization is required
print(True)
print(False)

# Comparisons return a Bool
print("These should all be True:")
print(3 < 5)
print(5 > 2)
print(3 <= 3)  # less-or-equal
print(4 >= 4)  # greater-or-equal
print(5 == 5)  # double-equal to compare
print(7 != 5)  # not-equal

# Comparisons work on strings too.
# This shows that double- and single-quotes
# give identical strings:
# fmt: off
print('foo' == "foo")
# fmt: on

# Besides equality, you can use "is" to compare
# object identity. This is often the same as
# equality, but it really means, "are these the
# same location in memory?" You could have two
# different lists of numbers whose values match
# but are different locations in memory, leading to
# equality being True but identity being False
print(f"Equality: {[10] == [10]}")
print(f"Identity: {[10] is [10]}")

# There are keywords defined for working with Bools
# "and," "or," and "not" act as logical operators
print(f"Should be True: {True or False}")
print(f"Should be False: {True and False}")
print(f"Should be True: {True and not False}")

# You can also cascade comparisons
# These lines are equivalent
print(3 < 5 and 5 >= 2)
print(3 < 5 >= 2)

# Objects can also be evaluated as if they are Boolean
# Said another way, objects are inherently "truthy."
# You can use the function bool() to cast something to
# a Bool and see whether it would be True or False
print(f"Should be true: {bool(10)}")
print(f'Should be true: {bool("foo")}')
print(f"Should be false: {bool(0)}")
print(f'Should be false: {bool("")}')

# This may seem arbitrary, but it will become extremely
# useful when we discuss flow control.

###################
print()
print("VARIABLES:")
###################

# read the equals sign as "gets"
# so this line says "foo gets 'text'"
foo = "text"

print("These lines give the same result:")
print("text")
print(foo)

# The backslashes escape the newline, as discussed earlier:
foo = "You can assign "
bar = """any \
type \
of \
string """
baz = f"to a variable."

# All the same operations that work on objects
# work on the variable assigned to them too.
# For example, here's string addition:
print("Addition of string variables:")
print(foo + bar + baz)

# When using a variable in an f-string,
# you can use an equals sign to see both
# the variable's name and value:
print("f-strings with equals sign:")
print(f"{foo=}")
print(f"{bar=}")
print(f"{baz=}")

# Math works as expected:
foo = 10
bar = 3
baz = 3.14
print(foo * bar - baz)

# To make an imaginary number out of a variable,
# multiply by 1j:
print(f"{foo=}")
print(f"{foo * 1j=}")

# You can also assign Bools to variables.
# This provides an easy way to check conditions.

first_number = 10
second_number = 5

first_is_larger = first_number > second_number
numbers_are_equal = first_number == second_number
second_is_larger = first_number < second_number

print(f"First number is larger: {first_is_larger}")
print(f"Numbers are equal: {numbers_are_equal}")
print(f"Second number is larger: {second_is_larger}")

# One example application would be to check the
# position of a motorized stage against some limit:

min_pos = 0
max_pos = 10
current_pos = 5

stage_within_limits = min_pos <= current_pos <= max_pos
print(f"{stage_within_limits=}")

##########################
print()
print("TUPLES AND LISTS:")
##########################


# Tuples and lists use commas between items
# Tuples have parentheses:
layout = ("LED", "lens", "object", "lens", "camera")
# Lists have brackets:
wavelengths = [400, 500, 600, 700]

# The data types can be mixed:
indices = ["nD", "nF", "nC", 1, 1.5]

# To get items out of a tuple or list, you can "slice" them.
# To slice a sequence, you use square brackets.
# Python uses zero-based indexing, meaning the first item
# in your sequence is at position 0. Additionally, both of
# these types preserve order. That means that the order of
# their contents during creation is their order thereafter.
# This is not true of every Python type.
print("These should return True:")
print(layout[0] == "LED")
print(layout[1] == "lens")

# Negative numbers enable you to select from the end:
# For example, index -1 is always the last item:
print(wavelengths[-1] == 700)
print(wavelengths[-2] == 600)

# To select multiple items, you use a colon.
# When slicing multiple items, Python will
# include the value at the first index,
# but it excludes the value at the last index.
print(("object", "lens") == layout[2:4])

# This "first-inclusive and last-exclusive" behavior
# is common in programming languages. It is also
# worth noting that slicing multiple items from a list
# returns another list, leaving the original list intact
# Slicing creates a new list, rather than stealing from
# the original list.

# By omitting the first or last index, you can
# slice all values starting from an index, up to
# an index, or the entire sequence.
print("Variations on slicing:")
print(layout[2:])
print(layout[:2])
print(layout[:])

# Because tuples are immutable, you can't change
# their values after creation. If uncommented,
# the next line would raise a TypeError and
# interrupt your program:
# layout[0] = 'Laser'

# As lists are mutable, you can change their contents.
print(f"Original: {wavelengths=}")
wavelengths[0] = 350
wavelengths[-1] = 750
print(f"Updated: {wavelengths=}")

# You can also construct tuples and lists over multiple lines:
# fmt: off
foo = [
    1, 
    2, 
    3
]
bar = (
    "a", 
    "b", 
    "c"
)
# fmt: on

# These are the same as if they were constructed on one line.

# While it may look vertical, this is not a method for creating
# vectors. It's purely a way to organize code. If you have a
# very long list, this may be more readable. When we get to the
# NumPy library, we will discuss creating row and column arrays.

# In many situations, you can omit the parentheses for a tuple.
# The safest method for determining whether or not it works
# is to try it:
foo = 1, 2, 3

# Lastly, the "in" keyword can be used to test
# whether an object is in a tuple or list.
print('Using "in" on a tuple:')
print(f'{"LED" in layout=}')
print(f'{"laser" in layout=}')


######################
print()
print("DICTIONARIES:")
######################

# Instead of parentheses or square brackets, dictionaries use
# curly braces. Each item has a colon separating the key from
# the value, and the items are delimited by commas:

wavelength_to_color = {633: "red", 532: "green", 450: "blue"}

# Like tuples and lists, you use square brackets to
# look up values in dictionary. You pass in the key
# and it returns the corresponding value:

color = wavelength_to_color[532]
print(f'Color is equal to green: {color == "green"}')

# Like tuples and lists, you can make multi-line dictionaries.
# This example also demonstrates how the "value" can be a list:

# Start the dictionary
materials = {
    # Each item will be string: list
    # Start the first item
    "N-BK7": [
        # Recall that lists can contain mixed types:
        "Sellmeier",
        1.03961212,
        0.231792344,
        1.01046945,
        0.00600069867,
        0.0200179144,
        103.560653,
    ],  # End the first item
    # Start the second item
    "FS7980": [
        "Sellmeier",
        0.68374049400,
        0.42032361300,
        0.58502748000,
        0.00460352869,
        0.01339688560,
        64.49327320000,
    ],  # End the second item
}  # end the dictionary

# We can add to a dictionary using a syntax
# similar to indexing. We supply the new key
# as the "index" and assign the new value:
materials["N-LASF9"] = [
    "Sellmeier",
    2.00029547,
    0.298926886,
    1.806918430,
    0.01214260170,
    0.0538736236,
    156.5308290,
]

name = "N-BK7"
glass = materials[name]
print(f"{name=}")
print(f"{glass=}")

# recall that the value we retrieved is a list,
# so we can index it:
equation = glass[0]
coefficients = glass[1:]

print(f"Glass {name} has a {equation} equation")
print(f"Coefficients are: {coefficients}")

##############
print()
print("SETS:")
##############

# Like dictionaries, sets can be created using curly braces.
# The difference is that the items in the set have no colon.
lens_shapes = {"PCX", "BCX", "PCV", "DCV", "ASP", "ACH"}

# Sets do not preserve order. This means that the order in which
# we put items in the set may not be the order in which they are
# stored. Compare the order at creation to the order when printed:
print("As created: {'PCX', 'BCX', 'PCV', 'DCV', 'ASP', 'ACH'}")
print(f"As stored: {lens_shapes}")

# Like the keys of a dictionary, the items in a set can be
# strings, floats, integers, Bools, or any hashable type:
wavelengths = {400, 500, 600, 700}

# Let's imagine you have a list of lists as an optical layout:
layout = [
    # Format is [radius, thickness, material]
    [0, 10, "air"],
    [0, 2, "N-BK7"],  # first lens
    [-20, 5, "air"],
    [0, 3, "FS7980"],  # filter
    [0, 5, "air"],
    [40, 2, "N-BK7"],  # second lens
    [0, 20, "air"],
]

# If you wanted to know all the materials in your layout,
# you could slice layout and create a set from the results.
# Since layout is a list of lists, we slice once to grab an
# item from layout, then we slice again to grab an item from
# the list retrieved from layout:
materials_in_layout = {
    layout[0][2],
    layout[1][2],
    layout[2][2],
    layout[3][2],
    layout[4][2],
    layout[5][2],
    layout[6][2],
}
print(f"Materials in layout: {materials_in_layout}")

# While we made that set manually, there are more elegant ways
# that we will discuss in the section on flow control.

# You can also use "in" to check whether an object is in the set:
print(f'Is N-BK7 in the layout? {"N-BK7" in materials_in_layout}')
print(f'Is N-SF11 in the layout? {"N-SF11" in materials_in_layout}')


#####################
print()
print("FUNCTIONS 1:")
#####################


def foo(arg1, arg2):
    """This is the docstring, a space designated for text
    describing what the function does. If you defined this
    function and then called `help(foo)` in a terminal,
    this dosctring is shown.

    Proper docstrings will include some description of the
    arguments, what the function does, and the return value.

    This function will sum the two arguments and return
    the result."""

    result = arg1 + arg2

    # "return" prescribes what the function should output.
    # When triggered, it also exits the function.
    return result

    # Even if you add more indented code, Python will never
    # execute it because the function already returned.
    # VS Code may flag this as "unreachable code."
    print("This never prints")


# Having reverted our indentation, we are outside the function again.
result_from_function = foo(2, 2)
print("Note that the unreachable code did not run")
print(f"Should be 4: {result_from_function}")

# Here is a more optical example:
def rayleigh_resolution(λ, fno):
    """Calculates the Rayleigh resolution criterion.
    λ is wavelength in microns, fno is the optic's
    f-number, and the returned resolution is in microns"""
    # Note that you do not need to assign the return value
    # to a variable. You can "inline" the return instead:
    return 1.22 * λ * fno


# If you want an easy way to use Greek letters,
# install Greek as a second language for your keyboard.
λ = 0.532
fno = 10
# The :g inside the last bracket tells Python to
# format the number nicely for printing:
print(
    f"Resolution at {λ} μm and f/{fno}: "
    f"{rayleigh_resolution(λ, fno):g} μm"
)

# If uncommented, this will print or open the
# docstring (depending on your environment):
# help(rayleigh_resolution)


#####################
print()
print("FUNCTIONS 2:")
#####################


def foo():
    print("Running function with no explicit return")


value = foo()
print(f"Result of function with no explicit return: {value=}")
print()


def foo(arg1, arg2, arg3):
    return arg1 * arg2 * arg3


three_numbers = [1, 3, 5]
print("List unpacking:")
print(three_numbers)


# If uncommented, this would raise an error because
# foo expects three arguments. We gave it a single list,
# even though it contains three items.
# print(foo(three_numbers))

# Instead, using an asterisk will unpack the list into
# its separate items:
print(foo(*three_numbers))

#####################
print()
print("FUNCTIONS 3:")
#####################

print("Should all equal 15:")
print(foo(1, 3, 5))
print(foo(arg1=1, arg2=3, arg3=5))

# Order does not matter for keyword arguments:
print(foo(arg3=5, arg2=3, arg1=1))

#####################
print()
print("FUNCTIONS 4:")
#####################


# positional_only, /, either, *, keyword_only
def foo(a, b, /, c, d, *, e, f):
    print(f"Positional-only: {a}, {b}")
    print(f"Positional or keyword: {c}, {d}")
    print(f"Keyword-only: {e}, {f}")
    print()


print("Positional-only and keyword-only arguments:")
foo(1, 2, 3, 4, e=5, f=6)
foo(1, 2, c=3, d=4, e=5, f=6)

# If uncommented, the following would raise an error.

# Entering keyword argument for positional-only:
# print(foo(a=1, a=2, 3, 4, e=5, f=6))

# Entering positional argument for keyword-only:
# print(foo(1, 2, 3, 4, 5, 6))


def thin_lens_refraction(y, u, f, n=1):
    u = (n*u - y/f) / n
    print(f"{y=}")
    print(f"{u=}")
    print(f"{f=}")
    print(f"{n=}")
    print()


print("No n provided, so it will use default:")
thin_lens_refraction(1, 0.1, 100)

#####################
print()
print("FUNCTIONS 5:")
#####################

def foo(a, b, *args, **kwargs):
    print(a)
    print(b)
    print("The args tuple:")
    print(args)
    print("The kwargs dictionary:")
    print(kwargs)

foo(
    "arg a",
    "arg b",
    "extra pos 1",
    "extra pos 2",
    extra_kw_1=5,
    extra_kw_2=6,
)

def variable_sum(*args):
    print(sum(args))

print("Summing two arguments:")
variable_sum(1, 2)
print("Summing five arguments:")
variable_sum(1, 2, 3, 4, 5)

#####################
print()
print("FUNCTIONS 6:")
#####################

variable = "foo"

def access_only():
    # A function can access objects outside itself...
    print(f"Within access_only(): {variable=}")

def try_to_change():
    # ...but it can't change objects outside itself. This only
    # redefines "variable" within the function:
    variable = "bar"
    print(f"Within try_to_change(): {variable=}")

access_only()
try_to_change()
print(f"Outside function again: {variable=}")
print()

#####################
print()
print("FUNCTIONS 7:")
#####################

def try_to_modify_argument(variable):
    print("Within try_to_modify_argument():")
    print(f"Before: {variable=}")
    variable[0] = 5
    print(f"After: {variable=}")

def try_to_reassign_argument(variable):
    print("Within try_to_reassign_argument():")
    print(f"Before: {variable=}")
    variable = [1, 2, 3]
    print(f"After: {variable=}")

variable = [1, 2, 3]
try_to_modify_argument(variable)
try_to_reassign_argument(variable)
print(f"Outside function again: {variable=}")
print()

#####################
print()
print("FUNCTIONS 8:")
#####################

# If you run `python ch1.py` in a terminal,
# the script will pause here:
print("Hitting breakpoint:")
# breakpoint()

# You can type "help" into the prompt to see some of the
# available actions. To execute the next line of code,
# type "next" or "n" and press enter. This can be done
# repeatedly to step through each line of your program.
# To resume your script, type "continue" or "c" and press enter.

def try_to_reassign_argument(variable):
    print("Within try_to_reassign_argument():")
    print(f"Before: {variable=}")
    # breakpoint()
    variable = [1, 2, 3]
    print(f"After: {variable=}")

# The id() function returns the memory address of the object.
# We can use this to compare "variable" before and after
# assigning inside the function. Try it in the breakpoint.
try_to_reassign_argument(variable)
print(f"Outside function again: {variable=}")
print()

#####################
print()
print("FUNCTIONS 9:")
#####################

# len() tries to calculate the length of an object and return it:
print(f"Length of layout list from earlier: {len(layout)}")
print(f"Length of lens shape set from earlier: {len(lens_shapes)}")

# range() gives numbers from zero to N-1 when given N:
print(f"List of 10 numbers: {list(range(10))}")

# input() provides the simplest form of user interaction.
# The argument to input() is the text prompt you'd like
# the user to see:
# wavelength = input("What wavelength (in nm)?\n> ")
# print(f"User provided: {wavelength} nm")

# Python has absolute value, minimum,
# maximum, and rounding functions:
print(f"{abs(-10)=}")
print(f"{min([1, 2, 3, 4, 5])=}")
print(f"{max([1, 2, 3, 4, 5])=}")
print(f"{round(3.1415927, 3)=}")

# There are also functions to create all
# the object types we introduced earlier:
print(f"{str(123)=}")
print(f'{float("123")=}')
print(f"{complex(1, 5)=}")
print(f'{int("123")}')
print(f"{bool(10)=}")
print(f"{tuple([1, 2, 3])=}")
print(f"{list((1, 2, 3))=}")
print(f'{dict([("key1", "value1"), ("key2", "value2")])=}')
print(f"{set([1, 2, 3, 2, 1])=}")

# type() tells you what type an object is:
print(f"{type(123)=}")
print(f'{type("123")=}')
print(f"{type(True)=}")

#################
print()
print("METHODS:")
#################

name = "Cooke triplet"
print("The dir() function prints the methods available for a string:")
print(dir(name))
print()

# As with any other functions, methods have a docstring
# you can access using help()
# help(name.upper)
print(name.upper())
print()

# help(name.lower)
print(name.lower())
print()

# help(name.find)
print(f'The letter k is number {name.find("k") + 1} in our string')
print()

# We can use the materials dictionary that we defined earlier.
print("Dictionary methods:")
print(dir(materials))
print()
print('Use the method "keys()" to grab and print glass names:')
print(f"{materials.keys()=}")

###################
print()
print("CLASSES 1:")
###################


class ThickLens:
    def __init__(self, front_radius, rear_radius, thickness, index):
        self.R1 = front_radius
        self.R2 = rear_radius
        self.CT = thickness
        self.n = index

    def __repr__(self):
        # Using the :g format specifier for pretty printing:
        return f"ThickLens with focal length {self.focal_length():g}"

    def focal_length(self):
        """Calculates the lens focal length using the lensmaker equation"""
        diopter = (self.n - 1) * (
            1 / self.R1
            - 1 / self.R2
            + (self.n - 1) * self.CT / (self.n * self.R1 * self.R2)
        )
        return 1 / diopter


# Approximating plano face as radius 10**9
pcx_singlet = ThickLens(10, 1e9, 3, 1.5)
bcx_singlet = ThickLens(20, -20, 3, 1.5)

print(pcx_singlet)
print(f"{pcx_singlet.R1=}")
print(f"{pcx_singlet.R2=}")
print(f"{pcx_singlet.focal_length()=}")
print(bcx_singlet)
print(f"{bcx_singlet.R1=}")
print(f"{bcx_singlet.R2=}")
print(f"{bcx_singlet.focal_length()=}")


###################
print()
print("CLASSES 2:")
###################

# The parentheses mean ThinLens
# "inherits from" ThickLens
class ThinLens(ThickLens):
    """Assumes a thin, biconvex lens with n=1.5.
    Provides a simplified way to make a ThickLens
    with a known focal length."""

    def __init__(self, f):
        R = f
        # super() calls the parent class.
        # We essentially grab __init__()
        # from ThickLens and pass in
        # calculated values.
        super().__init__(R, -R, 0, 1.5)


thin_lens = ThinLens(100)
print("Created ThinLens with f=100")
print(f"Should return 100: {thin_lens.focal_length()=}")

print("ThinLens has all the attributes inherited from ThickLens")
print(f"{thin_lens.R1=}")
print(f"{thin_lens.R2=}")
print(f"{thin_lens.CT=}")
print(f"{thin_lens.n=}")

########################
print()
print("FLOW CONTROL 1:")
########################

lens_diameter = 25
threshold_1 = 10
threshold_2 = 20
threshold_3 = 30

if lens_diameter < threshold_1:
    print(f"Lens is smaller than {threshold_1}")

elif threshold_1 <= lens_diameter < threshold_2:
    print(f"Lens is between {threshold_1} and {threshold_2}")

elif threshold_2 <= lens_diameter < threshold_3:
    print(f"Lens is between {threshold_2} and {threshold_3}")

else:
    print(f"Lens is larger than {threshold_3}")

########################
print()
print("FLOW CONTROL 2:")
########################

try:
    print(lens_name)
except NameError as e:  # that is, lens_name does not exist
    print(f"Caught error: {e}")
    lens_name = "Double Gauss"
    print(lens_name)
print()

surface_power = 0
try:
    radius = 1 / surface_power
except ZeroDivisionError as e:  # cannot divide by zero
    print(f"Caught error: {e}")
    # Approximating plano as 10**9
    radius = 1e9
print(radius)
print()

a = 2  # int
b = "2"  # str
try:
    print(a + b)
except TypeError as e:  # cannot add strings and ints
    print(f"Caught error: {e}")
    print(a + int(b))
print()

########################
print()
print("FLOW CONTROL 3:")
########################


# __file__ is a built-in variable pointing to
# the path of the file currently running. Here
# we shall slice it to grab the current folder.
# There are more elegant ways of doing this
# to be discussed later.
this_folder = __file__[:-6]
path_to_text_file = this_folder + "foo.txt"
try:
    print("Trying to open and write to file")
    # One common file convention is "fout" for "file out"
    fout = open(path_to_text_file, "w")  # "w" for "write"
    radius = 1 / 0
    fout.write(str(radius))
except ZeroDivisionError:
    print("Caught the error")
    radius = 1e9
    fout.write(str(radius))
    fout.write("\n")  # newline
finally:
    print("Closing the file")
    fout.close()
print("Done!")

########################
print()
print("FLOW CONTROL 4:")
########################

with open(path_to_text_file, "a") as fout:  # "a" for "append"
    radius = 20
    fout.write(str(radius))

# Another common file convention is "fin" for "file in"
with open(path_to_text_file, "r") as fin:  # "r" for "read"
    print(fin.read())

########################
print()
print("FLOW CONTROL 5:")
########################

value = 1
previous = 1
while value < 1e6:
    value, previous = value + previous, value
print(f"First Fibonacci number greater than 10^6: {value}")

########################
print()
print("FLOW CONTROL 6:")
########################

for surface in layout:
    print(surface)
print()

# A for loop on a dictionary iterates through the keys.
# You can also do "for name in materials.keys():"
for name in materials:
    print(name)
    # As name is the key, you can index to get the value:
    print(materials[name])
print()

# You can directly access the values with a dictionary method:
for equation in materials.values():
    print(equation)
print()

# Because materials.items() returns tuples, you can
# unpack each tuple into k and v on each iteration of the loop:
for k, v in materials.items():
    print(k, v)
print()

# This example uses zip() to duplicate what the dictionary method
# items() does. This enables you to simultaneously iterate over
# otherwise separate sequences:
for k, v in zip(materials.keys(), materials.values()):
    print(k, v)
print()

########################
print()
print("FLOW CONTROL 7:")
########################

print("Using continue to print only odd numbers:")
for n in range(10):
    is_even = n % 2 == 0
    if is_even:
        continue
    print(n)
print()

threshold = 5
print("Using break to exit a loop once a value is found:")
for n in range(10):
    if threshold <= n:
        break
print(f"First number >= {threshold} was {n}")
print()

########################
print()
print("FLOW CONTROL 8:")
########################

# A "while" loop that can escape:
counter = 0
while True:  # runs forever
    counter += 1
    if 100 <= counter:
        break

# Use try-except to convert surface prescriptions:
lens_powers = [-1, -0.1, 0, 0.1, 1]
radii = []
for p in lens_powers:
    try:
        radii.append(1 / p)
    except ZeroDivisionError:
        radii.append(1e9)
print(radii)

# Use continue to only print glass surfaces:
for surface in layout:
    is_air = surface[2] == "air"
    if is_air:
        continue
    print(f"{surface[1]}mm of {surface[2]} glass")
print()

# write a sag table to a text file:
def spherical_sag(y, R):
    return R - (R ** 2 - y ** 2) ** 0.5


heights = [0, 0.2, 0.4, 0.6, 0.8, 1]
radius = 10
path_to_pretend_sag_table = this_folder + "sag.csv"
with open(path_to_pretend_sag_table, "w") as fout:
    for h in heights:
        s = spherical_sag(h, radius)
        fout.write(f"{h}, {s}")
        fout.write("\n")

with open(path_to_pretend_sag_table, "r") as fin:
    print(fin.read())

########################
print()
print("FLOW CONTROL 9:")
########################

# for-in loop:
y_loop = []
for x in range(10):
    if x % 2 == 0:
        y_loop.append(x ** 2)

# List comprehension:
y_comp = [x ** 2 for x in range(10) if x % 2 == 0]

print("The loop and comprehension create the same list:")
print(f"{y_loop=}")
print(f"{y_comp=}")
print()

# Thanks to their support for "if" statements,
# comprehensions can be used to filter lists:
files_in_dir = [
    "ch1.py",
    "demo.csv",
    "foo.txt",
    "mats.json",
    "sag.csv",
]
only_csv_files = [f for f in files_in_dir if ".csv" in f]
print(f"{only_csv_files=}")
print()

# In the section on sets we said there were
# more efficient ways to create the set of
# all materials. Here is a for-in loop version:
mats_for_loop = set()
for l in layout:
    mats_for_loop.add(l[2])

# The set comprehension is even more concise:
mats_set_comp = {l[2] for l in layout}

print("For-in loop vs set comprehension:")
print(f"{mats_for_loop=}")
print(f"{mats_set_comp=}")
print()

# In addition to list and set comprehensions, Python
# also supports dictionary comprehensions:
print({x: x ** 2 for x in range(5)})
print({x: y for x, y in zip(range(5), range(10, 15))})

#########################
print()
print("FLOW CONTROL 10:")
#########################


def foo(*args, **kwargs):
    for a in args:
        print(a)
    for k, v in kwargs:
        print(k, v)


###################
print()
print("IMPORTS 1:")
###################

print(f"{sum([0.1] * 10)=}")
import math

print(f"{math.fsum([0.1] * 10)=}")

# You can import a function from a module:
from math import fsum

# Now you can skip "math." since "fsum" was directly imported:
print(f"{fsum([0.1] * 10)=}")

# You can use "as" to assign a new name
# to your imported module or function:
import math as m

print(f"{m.fsum([0.1] * 10)=}")
from math import fsum as fs

print(f"{fs([0.1] * 10)=}")
# This is often done in order to use a shorter alias.

###################
print()
print("IMPORTS 2:")
###################

# Directly importing functions makes them collide:
from math import sqrt
from cmath import sqrt

print(f"Import the function: only one survives")
print(f"{sqrt=}")

# Importing modules allows the functions to coexist:
import math
import cmath

print(f"Import the module: both can exist")
print(f"{math.sqrt=}")
print(f"{cmath.sqrt=}")

# Avoid doing this:
from math import *

# The "*" means you import
# everything from that module.

###################
print()
print("IMPORTS 3:")
###################

# sys can tell you some details about your computer:
import sys
print(f"Biggest possible float: {sys.float_info.max}")
print(f"Smallest possible float: {sys.float_info.min}")
print()

# pathlib provides a nice interface for working with file names
import pathlib
this_folder = pathlib.Path(__file__).parent
print(f"{this_folder=}")
# Because file paths have slashes in them, pathlib's
# Path supports division to specify where a file is.
# Recall that __file__ is defined automatically by Python
# as the file currently running:
print(f'{__file__ == str(this_folder / "ch1.py")=}')
print()

# time can help with some simple profiling or add pauses:
import time
start = time.time()
for _ in range(5):
    time.sleep(0.1)
stop = time.time()
print(f"Took {stop - start:.3g} s to sleep 0.1 five times")
print()

# warnings provides a way to warn users if something is amiss:
import warnings
material_index = 0.5
if material_index < 1:
    warnings.warn(
        f"Material has lower index than air: {material_index}"
    )
print()

# winsound allows you to emit a sound through the computer speakers.
# If not on Windows, printing the \a character emits a simple beep.
# This can be used to notify the user at the end of a long-running task:
try:
    import winsound
    winsound.Beep(440, 500)
except ModuleNotFoundError:
    print("\a", end="")

# random provides psuedo-random numbers through several convenient functions:
import random
print(f"{random.random()=}")
print(f"{random.randint(1, 10)=}")
print()

# secrets provides "cryptographically secure" random numbers:
import secrets
print(f"{secrets.randbelow(10)=}")
print(f"{secrets.token_urlsafe(32)=}")
print()

# platform can help identify the current operating system:
import platform
computer = platform.platform()
print(f"{computer=}")
print()

# os can provide access to environment variables and other details:
import os
if "win" in computer.lower():
    print(f'{os.environ["USERPROFILE"]=}')
elif "mac" in computer.lower():
    print(f'{os.environ["HOME"]=}')
print()

# collections has objects beyond lists, tuples, dictionaries, and sets.
# One is the deque, or "double-ended queue," which is like a two-sided list:
import collections
d = collections.deque([1, 2, 3, 4])
print(f"{d=}")
d.pop()
d.append(5)
print(f"{d=}")
d.popleft()
d.appendleft(0)
print(f"{d=}")
print()

# statistics offers functions beyond those in the math module:
import statistics
print(f"{statistics.median(d)=}")
print(f"{statistics.mean(d)=}")
print(f"{statistics.stdev(d)=}")
print()

# logging makes it easy to discretely save information to a file:
log_file = this_folder / "ch1_log.log"
import logging
logging.basicConfig(filename=log_file, level=logging.DEBUG)
something_went_wrong = True
if something_went_wrong:
    logging.debug(f"Issue occurred: {something_went_wrong=}")

# struct can help when working with binary representations
# of numbers. This comes up on occasion when working with
# files or talking to test equipment:
import struct
number_as_bytes = struct.pack("<I", 256)
print(f"{number_as_bytes=}")
print()
# The format code depends on the file or equipment you
# use, so look up the Python documentation on struct for
# more information.

# As mentioned early in our chapter, the decimal module
# provides more exact math than can be achieved with floats:
from decimal import Decimal
dec_from_string = Decimal("0.1")  # exactly 0.1
dec_from_float = Decimal(0.1)  # floating-point approximation of 0.1
print(f"{dec_from_string=}")
print(f"{dec_from_float=}")
print("Classic floating-point sum error shown earlier:")
print(sum((0.1 for _ in range(10))))
print("Same calculation done using the decimal module:")
print(sum((Decimal("0.1") for _ in range(10))))
print()

# cmath provides math functions that support complex numbers:
try:
    print(math.sqrt(-1))
except ValueError as e:
    print(f"Caught error: {e}")
    print("Use the cmath module instead:")
    import cmath
    print(cmath.sqrt(-1))
print()

# The csv module provides a nice interface for reading
# and writing comma-separated value (CSV) files.
import csv
path_to_csv_file = this_folder / "demo.csv"
with open(path_to_csv_file, "w") as csvfile:
    writer = csv.writer(csvfile)
    row = [1, 2, 3, 4]
    writer.writerow(row)

# Read the file we just wrote to:
with open(path_to_csv_file, "r") as csvfile:
    reader = csv.reader(csvfile)
    print(f"Rows in {path_to_csv_file.name}:")
    for row in reader:
        print(row)
print()

# read a CSV file of index data, skipping lines for brevity:
path_to_index_file = (
    this_folder.parent / "data" / "schott_nbk7_data.csv"
)
with open(path_to_index_file) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    print(header)
    skipper = 0
    for row in reader:
        skipper += 1
        if skipper % 5 != 0:
            continue
        print([float(r) for r in row])
print()

# While CSVs are great for structured data,
# JSON files are good for unstructured data.
# You can write a dictionary, such as "materials"
# from earlier, directly to a JSON file:
import json
path_to_materials_database = this_folder / "mats.json"
with open(path_to_materials_database, "w") as mat_db:
    json.dump(materials, mat_db)

# ctypes provides a way to interact with C objects. This enables
# Python code to drive DLLs, such as those used to control test
# equipment. Using ctypes requires some familiarity with C paradigms:
import ctypes
if "win" in computer.lower():
    dll = ctypes.windll.msvcrt
    print("Print a ctypes object using Microsoft's Visual C++ runtime:")
elif "mac" in computer.lower():
    dll = ctypes.cdll.LoadLibrary("libSystem.dylib")
    print("Print a ctypes object using the standard library on macOS:")
ctypes_number = ctypes.c_int(256)
dll.printf(b"%d\n", ctypes_number)

###################
print()
print("IMPORTS 4:")
###################

# numpy provides very fast arrays for math, 
# often using a MATLAB-like syntax:
import numpy as np
x = np.linspace(-5, 5, 31)  # array of numbers
y = np.exp(-x**2)  # roughly a Gaussian

# scipy builds upon numpy to bring additional
# computational functionality, such as interpolation:
from scipy import interpolate
interp_fct = interpolate.interp1d(x, y, kind='cubic')
x_more = np.linspace(-5, 5, 101)
y_interp = interp_fct(x_more)

# pandas is also build on numpy, but focuses
# specifically on data analysis. It also happens
# to have one of the fastest functions for 
# reading CSV files:
import pandas as pd
# df for a pandas DataFrame:
df = pd.read_csv(path_to_index_file, index_col=0)
# DataFrame has a numpy array inside:
data = df.values

# sympy provides a way to do symbolic math in Python.
# It can even handle tricky problems like the integration
# of a Gaussian, useful for laser problems:
import sympy as sm
# Have to define a variable that sympy knows 
# it can use for symbolic math, along with how
# we want it printed:
t = sm.symbols('t')
f = sm.exp(-t**2)
F = sm.integrate(f, t)

# matplotlib is the gold-standard plotting library.
# There are many others with various use cases, but 
# matplotlib is a great place to start:

# Uncomment to make high-resolution images for print:
# import matplotlib
# matplotlib.rcParams['figure.dpi'] = 300

import matplotlib.pyplot as plt
plt.plot(x, y, 'b.', label='Data')
plt.plot(x_more, y_interp, 'r-', label='Interpolated')
plt.legend()
plt.grid()
plt.title('Close this plot to continue')
# Having created the plot, we now need to show it:
plt.show()

# Our DataFrame from the pandas demo works with matplotlib:
df.plot(grid=True, title='Close this plot to continue')
plt.show()

# sympy can generate plots with some sensible defaults chosen:
sm.plot(f, title='Close this plot to continue')
plt.show()
sm.plot(F, title='Close this plot to continue')
plt.show()

# scikit-image provides tools for image processing beyond
# what scipy has in its ndimage module:
import skimage
checkerboard = skimage.data.checkerboard()
plt.imshow(checkerboard, cmap=plt.cm.gray)
plt.title('Close this plot to continue\nNo known license restrictions')
plt.show()
coffee = skimage.data.coffee()
plt.imshow(coffee)
plt.title('Close this plot to continue\nImage by Rachel Michetti licensed under Creative Commons Zero')
plt.show()
rescaled = skimage.exposure.equalize_adapthist(coffee)
plt.imshow(rescaled)
plt.title('Close this plot to continue')
plt.show()

###################
print()
print("IMPORTS 5:")
###################

# using pip / conda...

# OpenCV is the de-factor image processing library. It
# has a very steep learning curve, but it rewards you.
# To install OpenCV, run `pip install opencv-python`
# in a terminal. You can then import `cv2`:
coin_image = skimage.data.coins()
import cv2
cv2.imshow('British Museum, Greek coins, no known copyright restrictions', coin_image)
cv2.waitKey(0)

blurred = cv2.medianBlur(coin_image, 3)
cv2.imshow('Median filtered - press any key to continue', blurred)
cv2.waitKey(0)

edges = cv2.Canny(blurred, 150, 200)
cv2.imshow('Edges - press any key to continue', edges)
cv2.waitKey(0)

coin_contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, 
    cv2.CHAIN_APPROX_SIMPLE)
coin_image = cv2.cvtColor(coin_image, cv2.COLOR_GRAY2BGR)
cv2.drawContours(coin_image, coin_contours, -1, (0, 255, 0), 2)
cv2.imshow('Contours on image - press any key to continue', coin_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# PyQtGraph is an alternative to matplotlib. Its novelty is
# that it is significantly faster and smaller than matplotlib.
# To install it, run `conda install pyqtgraph` in a terminal:
import pyqtgraph as pg
title = 'Image by Rachel Michetti licensed under Creative Commons Zero'
pg.image(coffee.T, title=title)
# Boilerplate to make this work in a script:
pg.QtGui.QGuiApplication.exec_()

# Uncomment these to open the example library:
# import pyqtgraph.examples
# pyqtgraph.examples.run()

###########################
print()
print("STICKING POINTS 1:")
###########################

sample_text = 'Quick Brown Fox'
print(f'{sample_text.lower=}')
print(f'{sample_text.upper=}')
print(f'{sample_text.lower()=}')
print(f'{sample_text.upper()=}')
print()

components = ["Laser", "Free Space", "Lens", "Free Space", "Detector"]
for comp in components:
    # Compares a method to a string:
    if comp.lower == "laser":
        print("Found laser first try")

for comp in components:
    # Now, compares a string to a string:
    if comp.lower() == "laser":
        print("Found laser second try")
print()

###########################
print()
print("STICKING POINTS 2:")
###########################

import random
class MultiMeter:
    def measure(self):
        return str(random.random())

meter = MultiMeter()
print(f"Value returned from meter: {meter.measure()}")

data = []
for _ in range(10):
    data.append(meter.measure())
# This could also be a one-liner:
# data = [meter.measure() for _ in range(10)]

try:
    print('Trying to average the data')
    average = sum(data) / len(data)
except TypeError as e:
    print('Caught an exception:')
    print(e)
    print('Using a comprehension to make a list of floats:')
    data_as_float = [float(d) for d in data]
    average = sum(data_as_float) / len(data_as_float)
    print(f'{average=}')

###########################
print()
print("STICKING POINTS 3:")
###########################

short_list = [3, 2, 1]
print('sorted returns a list:')
print(f'{sorted(short_list)=}')
print('The sort method returns None but updates the list:')
print(f'{short_list.sort()=}')
print(f'{short_list=}')

looks_like_a_list = [3, 2, 1].sort()
print(f"Should be None: {looks_like_a_list}")

really_is_a_list = sorted([3, 2, 1])
print(f"Should be [1, 2, 3]: {really_is_a_list}")

short_list = [3, 2, 1]
looks_like_a_list = short_list.sort()
try:
    print(len(looks_like_a_list))
except TypeError as e:
    print(f"Caught an exception:")
    print(e)

###########################
print()
print("STICKING POINTS 4:")
###########################

# It looks like this list always starts empty:
def updates_own_arguments(arg=[]):
    arg.append(1)
    print(arg)

# Testing shows us the changes persist:
updates_own_arguments()
updates_own_arguments()
updates_own_arguments()

###########################
print()
print("STICKING POINTS 4:")
###########################

# Pretend you made this list, then decided 
# to add the '5' but forgot the comma:
list_missing_a_comma = [
    '1',
    '2',
    '3',
    '4'
    '5'
]
print('4 and 5 were concatenated:')
print(list_missing_a_comma)
print()

# You can safely add a comma to reduce
# the risk of errors in the future:
list_with_trailing_comma = [
    '1',
    '2',
    '3',
    '4',
    '5',
]
print('Python handles the extra comma:')
print(list_with_trailing_comma)

###########################
print()
print("STICKING POINTS 5:")
###########################

# Python's integers can go as high or
# low as your computer can handle:
print(400 ** 8)

# Uncomment this if you feel adventurous:
# print(2 ** 32 ** 4)

# When creating an array, NumPy picks a
# datatype that suits the values you enter. 
# We can force it to calculate a number bigger
# than that datatype can handle, causing it to
# wrap around to negative numbers:
too_big = np.array([400]) ** 8
print(f'{too_big[0] == 400 ** 8=}')

# If we tell NumPy to use floats or a larger
# integer, then it can handle the calculation:
now_as_float = np.array([400.]) ** 8
print(f'{now_as_float[0] == 400 ** 8=}')
now_as_larger_int = np.array([400], dtype=np.float64) ** 8
print(f'{now_as_larger_int[0] == 400 ** 8=}')

###########################
print()
print("STICKING POINTS 6:")
###########################

start = 5
stop = 15
step = 1
num_points = int((stop - start) / step + 1)

print('These take different arguments but give the same numbers:')
print('range and arange exclude the stop value:')
print(f'{list(range(start, stop+step, step))=}')
print(f'{np.arange(start, stop+step, step)=}')
print('linspace includes the stop value:')
print(f'{np.linspace(start, stop, num_points)=}')
print()

step = 0.5
num_points = int((stop - start) / step + 1)
try:
    range(start, stop, step)
except TypeError as e:
    print('range only accepts integer steps:')
    print(e)
print(f'{np.arange(start, stop+step, step)=}')
print(f'{np.linspace(start, stop, num_points)=}')
print()

# When using a step size that gives a non-integer number of points,
# arange will sacrifice the stop value while linspaces gives up the
# step size:
step = 1.1
num_points = int((stop - start) / step + 1)
print(f'{np.arange(start, stop+step, step)=}')
print(f'{np.linspace(start, stop, num_points)=}')
print()

# Alternatively, you can change your arguments to arange
# and it will not exceed your stop values:
print(f'{np.arange(start, stop, step)=}')

