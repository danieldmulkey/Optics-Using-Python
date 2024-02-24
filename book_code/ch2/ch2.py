# Uncomment to make high-resolution images for print:
# import matplotlib
# matplotlib.rcParams['figure.dpi'] = 300

#####################
print()
print("MATERIALS 1:")
#####################

import math


def no_numpy_nbk7(microns):
    b1 = 1.03961212
    b2 = 0.231792344
    b3 = 1.01046945
    c1 = 0.00600069867
    c2 = 0.0200179144
    c3 = 103.560653
    n = math.sqrt(
        1
        + b1 * microns ** 2 / (microns ** 2 - c1)
        + b2 * microns ** 2 / (microns ** 2 - c2)
        + b3 * microns ** 2 / (microns ** 2 - c3)
    )
    return n


print(f"Should be around 1.51680: {no_numpy_nbk7(0.5876):g}")

import numpy as np
import sympy as sm

vis = np.linspace(400, 700, 10)
λ = sm.symbols("λ")

print(f"For a single number: {no_numpy_nbk7(0.5)}")
try:
    print(f"For a NumPy array: {no_numpy_nbk7(vis)}")
except TypeError as e:
    print("NumPy did not work:")
    print(e)
try:
    print(f"For a SymPy symbol: {no_numpy_nbk7(λ)}")
except TypeError as e:
    print("SymPy did not work:")
    print(e)

#####################
print()
print("MATERIALS 2:")
#####################

import materials as mats

print("For a single number:")
print(f"{mats.nbk7(0.5)}")
print("For a NumPy array:")
print(f"{mats.nbk7(vis)}")
print("For a SymPy symbol:")
print(f"{mats.nbk7(λ)}")

#####################
print()
print("EQUATIONS 1:")
#####################

import equations

limit = equations.rayleigh_resolution(0.5, 8)
print(f"Resolution limit of f/8 lens at 500 nm: {limit} µm")

#####################
print()
print("EQUATIONS 2:")
#####################

params = [
    1550e-9,
    10.4e-6 / 2,
    10.4e-6 / 2,
]
should_be_1 = equations.fiber_coupling_efficiency(*params)
print(f"Perfect coupling: {should_be_1=:g}")

params = [
    1550e-9,
    10.4e-6 / 2 * 0.9,
    10.4e-6 / 2,
    1e-6,
    1e-6,
    math.degrees(1e-3),
]
should_be_worse = equations.fiber_coupling_efficiency(*params)
print(f"Imperfect coupling: {should_be_worse=:g}")

################################
print()
print("PARAXIAL APPROXIMATION:")
################################

import numpy as np
import matplotlib.pyplot as plt

# using cubehelix palette to mitigate problems for
# black & white print or colorblind readers:
colors = [
    "#162C40",
    "#2D7337",
    "#A6774E",
    "#D996CE",
    "#C4DDF2",
]

angles = np.linspace(1e-6, np.pi / 4, 1000)
sin_error = abs((angles - np.sin(angles)) / np.sin(angles)) * 100
tan_error = abs((angles - np.tan(angles)) / np.tan(angles)) * 100

plt.figure()
plt.semilogy(
    np.degrees(angles),
    sin_error,
    color=colors[0],
    linestyle="solid",
    label=r"$\left | \frac{θ - \sin{θ}}{\sin{θ}} \right |$",
)
plt.semilogy(
    np.degrees(angles),
    tan_error,
    color=colors[1],
    linestyle="dashed",
    label=r"$\left | \frac{θ - \tan{θ}}{\tan{θ}} \right |$",
)
plt.xlabel("Angle (degrees)")
plt.ylabel("Error (%)")
plt.legend()
plt.grid()
plt.title("Accuracy of Paraxial Approximation")
plt.show()


def degrees_from_percent(p):
    index_near_p = np.abs(tan_error - p).argmin()
    return np.degrees(angles[index_near_p])


print("Paraxial approximation is accurate to A at B, C, or D:")
print("A (%)   B (°)   C (mrad) D (NA)")
for per in [10, 1, 0.1, 0.01]:
    a = per
    b = degrees_from_percent(per)
    c = np.radians(b) * 1e3
    d = np.sin(c / 1e3)
    print(f"{a:.3g}\t{b:.3g}\t{c:.3g}\t{d:.3g}")


##########################
print()
print("BASIC RAYTRACING:")
##########################

# Tracing marginal ray to the focus of a refractive surface:
y = 1e-3
nu = 0

print("Marginal ray starting conditions:")
print(f"{y=:g}")
print(f"{nu=:g}")
print()

n = 1.5  # index of glass
dn = n - 1  # from air into glass
R = 50e-3  # 50 mm
nu = nu - y * dn / R  # refraction

t = -y * n / nu  # calculating distance to focus
print(f"Distance to focus {t*1e3:g} mm")
y = y + t * nu / n  # transfer

print("Ending conditions")
print(f"{y=:g}")
print(f"{nu=:g}")
print()

# Tracing chief ray to the focus of a refractive surface:
y = 0
nu = 0.1

print("Chief ray starting conditions:")
print(f"{y=:g}")
print(f"{nu=:g}")
print()

nu = nu - y * dn / R  # refraction
y = y + t * nu / n  # transfer

print("Ending conditions")
print(f"{y=:g}")
print(f"{nu=:g}")

###################################
print()
print("RAYTRACING WITH FUNCTIONS:")
###################################


def refract(y, nu, Δn, R):
    return nu - y * Δn / R


def transfer(y, nu, t, n):
    return y + t * nu / n


# Tracing marginal ray to the focus of a thin lens:
y = 1e-3
nu = 0

print("Marginal ray starting conditions:")
print(f"{y=:g}")
print(f"{nu=:g}")
print()

nu = refract(y, nu, dn, R)  # into lens
nu = refract(y, nu, -dn, -R)  # out of lens

t = -y / nu  # calculating distance to focus
print(f"Distance to focus {t*1e3:g} mm")
y = transfer(y, nu, t, 1)

print("Ending conditions")
print(f"{y=:g}")
print(f"{nu=:g}")
print()

# Tracing chief ray to the focus of a thin lens:
y = 0
nu = 0.1

print("Chief ray starting conditions:")
print(f"{y=:g}")
print(f"{nu=:g}")
print()

nu = refract(y, nu, dn, R)  # into lens
nu = refract(y, nu, -dn, -R)  # out of lens
y = transfer(y, nu, t, 1)

print("Ending conditions")
print(f"{y=:g}")
print(f"{nu=:g}")


###############################
print()
print("PYTHON CLASS FOR RAYS:")
###############################

import abcd

marginal = abcd.Ray(0, 0.1)
print(f"Result of __repr__:\n{marginal}")
print(f"ray.y attribute: {marginal.y=}")
print(f"ray.u attribute: {marginal.u=}")
print(f"ray.n attribute: {marginal.n=}")

axis = abcd.Ray()  # default values
print(f"Should return false: {axis == marginal=}")

print(f"Should return true: {marginal.wavelength == axis.wavelength=}")
print()

# Trying NumPy:
angles = np.linspace(0, 0.1, 11)
np_rays = abcd.Ray(0, angles)
print(f"Shows correct height and angles:\n{np_rays}")
print()

# Trying SymPy:
angle = sm.symbols("u")
sm_ray = abcd.Ray(0, angle)
print(f"Shows correct height and symbolic angle:\n{sm_ray}")

#########################################
print()
print("PYTHON CLASS FOR GAUSSIAN BEAMS:")
#########################################

gb = abcd.GaussianBeam(z=0, zR=1e-3)
print(gb)
print(f"{gb.z=}")
print(f"{gb.zR=}")
print()

gb = abcd.GaussianBeam(R=math.inf, w=13e-6)
print(gb)
print(f"{gb.R=}")
print(f"{gb.w=}")
print()

# Child class still has parent's attributes:
print(f"{gb.y=:g}")
print(f"{gb.u=:g}")
print(f"{gb.n=:g}")
print(f"{gb.wavelength=:g}")
print()

# We can compare properties over wavelength:
gb_red = abcd.GaussianBeam(R=math.inf, w=50e-6, wavelength=632e-9)
gb_blue = abcd.GaussianBeam(R=math.inf, w=50e-6, wavelength=405e-9)
print("Red should diverge more than blue:")
print(f"{gb_blue.divergence < gb_red.divergence=}")
print(f"{gb_red.zR < gb_blue.zR=}")
print()

# We can compare properties over index:
gb_air = abcd.GaussianBeam(R=math.inf, w=50e-6)
gb_glass = abcd.GaussianBeam(R=math.inf, w=50e-6, n=1.5)
print("In-air should diverge more than in-glass:")
print(f"{gb_glass.divergence < gb_air.divergence=}")
print(f"{gb_air.zR < gb_glass.zR=}")

########################################
print()
print("PYTHON CLASS FOR ABCD MATRICES:")
########################################

identity = abcd.ABCD()
print("Identity matrix:")
print(f"{identity}")
print()

thin_lens = abcd.ABCD(C=-1 / 10e-3)
print("Thin lens:")
print(f"{thin_lens}")
print(f"{thin_lens.F1=}")
print(f"{thin_lens.F2=}")
print(f"{thin_lens.P1=}")
print(f"{thin_lens.P2=}")
print(f"{thin_lens.N1=}")
print(f"{thin_lens.N2=}")
print(f"{thin_lens.f1=}")
print(f"{thin_lens.f2=}")
print()

chief_ray = abcd.Ray(1, 0)
print(f"Before lens: {chief_ray}")
focused_ray = thin_lens @ chief_ray
print(f"After lens: {focused_ray}")

##################
print()
print("SURFACES:")
##################

# Transfer
L = 15e-3
n = 1.5
mtx = abcd.ABCD(B=L / n)
print(f"Matrix for transfer:\n{mtx}")

ray = abcd.Ray(u=0.1)
print(f"Before transfer:\n{ray}")

new_ray = mtx @ ray
print(f"After transfer:\n{new_ray}")
print()

# Dielectric interface
dn = 1 - 1.5  # from glass to air
R = -5e-3
mtx = abcd.ABCD(C=-dn / R)
print(f"Matrix for refraction:\n{mtx}")

ray = abcd.Ray(y=1e-3, u=0.1)
print(f"Before refraction:\n{ray}")

new_ray = mtx @ ray
print(f"After refraction:\n{new_ray}")
print()

# Reflection
R = -50e-3
mtx = abcd.ABCD(C=2 / R)
print(f"Matrix for reflection:\n{mtx}")

ray = abcd.Ray(y=1e-3)
print(f"Before reflection:\n{ray}")

new_ray = mtx @ ray
print(f"After reflection:\n{new_ray}")


######################
print()
print("COMPONENTS 1:")
######################

# We can use SymPy symbols to calculate
# the analytical equation for a thick lens:
R1, R2, n, t = sm.symbols("R1 R2 n t")

front = abcd.Refraction(R=R1, n1=1, n2=n)
middle = abcd.Transfer(t, n)
back = abcd.Refraction(R=R2, n1=n, n2=1)
thick_lens = back @ middle @ front

# SymPy objects support a method called
# simplify, which attempts to simplify the
# final expression:
print("Thick lens:")
print(f"A: {thick_lens.A.simplify()}")
print(f"B: {thick_lens.B.simplify()}")
print(f"C: {thick_lens.C.simplify()}")
print(f"D: {thick_lens.D.simplify()}")
print()

# The thin lens is a special case of the
# thick lens where the thickness is zero:
front = abcd.Refraction(R=R1, n1=1, n2=n)
middle = abcd.Transfer(0, n)
back = abcd.Refraction(R=R2, n1=n, n2=1)
thin_lens = back @ middle @ front

print("Thin lens:")
print(f"A: {thin_lens.A.simplify()}")
print(f"B: {thin_lens.B.simplify()}")
print(f"C: {thin_lens.C.simplify()}")
print(f"D: {thin_lens.D.simplify()}")

######################
print()
print("COMPONENTS 2:")
######################

heights = np.linspace(0, 1e-3, 11)
angles = np.linspace(0, 0.1, 11)

# A == 0:
focuser = abcd.Transfer(10e-3) @ abcd.ThinLens(10e-3)
print(f"{focuser.A == 0=}")
rays = abcd.Ray(heights, 0.1)
ending_rays = focuser @ rays
print("Different ray heights at a given angle map to the same point:")
# Using np.diff to calculate difference between consecutive ray heights:
print(f"{np.all(np.diff(ending_rays.y) == 0)=}")
# Rays end in the rear focal plane.
print()

# B == 0:
imager = (
    abcd.Transfer(20e-3) @ abcd.ThinLens(10e-3) @ abcd.Transfer(20e-3)
)
print(f"{imager.B == 0=}")
rays = abcd.Ray(0.1, angles)
ending_rays = imager @ rays
print("Magnification is A term:")
print(f"{np.all(ending_rays.y == rays.y * imager.A)=}")
print("Different angles from a given point map to the same point:")
print(f"{np.all(np.diff(ending_rays.y) == 0)=}")
# Rays move from object plane to image plane.
print()

# C == 0:
afocal = (
    abcd.ThinLens(5e-3) @ abcd.Transfer(15e-3) @ abcd.ThinLens(10e-3)
)
print(f"{afocal.C == 0=}")
rays = abcd.Ray(heights, 0.1)
ending_rays = afocal @ rays
print("Angular magnification is D term")
print(f"{np.all(ending_rays.u == rays.u * afocal.D)=}")
print("Different ray heights at a given angle map to the same angle:")
print(f"{np.all(np.diff(ending_rays.u) == 0)=}")
print()

# D == 0:
collimator = abcd.ThinLens(10e-3) @ abcd.Transfer(10e-3)
print(f"{collimator.D == 0=}")
rays = abcd.Ray(0.1, angles)
ending_rays = collimator @ rays
print("Different angles from a given point map to the same angle:")
print(f"{np.all(np.diff(ending_rays.u) == 0)=}")
# Rays begin in the front focal plane

######################
print()
print("COMPONENTS 3:")
######################

# Focal length & distance over λ
wavelengths = np.linspace(0.4, 0.7, 100)  # in µm
efls = []
bfls = []
for n in mats.nbk7(wavelengths):
    lens = abcd.ThickLens(50e-3, math.inf, 2e-3, n)

    efls.append(-1 / lens.C * 1e3)  # in mm
    bfls.append(lens.F2 * 1e3)  # in mm

plt.plot(
    wavelengths, efls, color=colors[3], label="EFL", linestyle="solid"
)
plt.plot(
    wavelengths,
    bfls,
    color=colors[1],
    label="BFL",
    linestyle="dashed",
)
plt.xlabel("Wavelength (µm)")
plt.ylabel("Distance (mm)")
plt.title(
    "Change in effective focal length and focal distance\n"
    "over wavelength for an N-BK7 singlet"
)
plt.grid()
plt.legend()
plt.show()

# Focal distance over T
temperatures = np.linspace(0, 60, 100)  # in µm
cte = 7.1e-6  # N-BK7 ppm / °C per Schott
wave = 0.532  # µm
T0 = 20  # assume EFL specified at 20 °C
f0 = 100e-3

Δbfls = []
for T in temperatures:
    n = mats.nbk7(wave, T)
    dndT = mats.nbk7(wave, T + 0.5) - mats.nbk7(wave, T - 0.5)
    Δf = f0 * (T - T0) * (cte - dndT / (n - 1))
    f = f0 + Δf
    lens = abcd.ThinLens(f)

    Δbfls.append(lens.F2 * 1e3 - f0 * 1e3)  # in mm

plt.plot(
    temperatures,
    Δbfls,
    color=colors[1],
    label="BFL",
    linestyle="dashed",
)
plt.xlabel("Temperature (°C)")
plt.ylabel("Change in focal distance (mm)")
plt.title(
    "Change in focal distance\n"
    "over temperature for an N-BK7 singlet"
)
plt.grid()
plt.legend()
plt.show()

#################
print()
print("MODULES:")
#################

# Achromatic doublet
# First, we need an approximate lens design:
λC = 0.6563  # µm
λD = 0.5893  # µm
λF = 0.4861  # µm

na = mats.nbk7(λD)
nb = mats.nsf5(λD)
va = (mats.nbk7(λD) - 1) / (mats.nbk7(λF) - mats.nbk7(λC))
vb = (mats.nsf5(λD) - 1) / (mats.nsf5(λF) - mats.nsf5(λC))
EFL = 100e-3

# This equation solves for surface curvatures:
solutions = equations.achromatic_doublet(EFL, na, va, nb, vb)

# We grab one of the solutions:
R1 = 1 / solutions[0]["C1"]
R2 = 2 / (solutions[0]["C2"] + solutions[0]["C3"])
R3 = 1 / solutions[0]["C4"]

# Now we can check focal length over wavelength:
waves = np.linspace(0.4, 0.7, 100)  # in µm
efls = []
for n1, n2 in zip(mats.nbk7(waves), mats.nsf5(waves)):
    el1 = abcd.ThickLens(R1, R2, 2e-3, n1)
    el2 = abcd.ThickLens(R2, R3, 2e-3, n2)
    lens = el2 @ el1
    efls.append(-1 / lens.C * 1e3)  # in mm

plt.plot(waves, efls, color=colors[3], label="EFL", linestyle="solid")
plt.xlabel("Wavelength (µm)")
plt.ylabel("Focal length (mm)")
plt.title(
    "Change in effective focal length\n"
    "over wavelength for an N-BK7 & N-SF5 achromat"
)
plt.grid()
plt.legend()
plt.show()


# Microscope
# Aspheres made of N-SF5 are available from catalog suppliers.
f_obj = 10e-3
nsf5_d_line = 1.67271
R_obj = -(nsf5_d_line - 1) * f_obj

# N-BK7 is commonly available.
f_tube = 100e-3
nbk7_d_line = 1.51680
R_tube = (nbk7_d_line - 1) * f_tube

t = 25e-3
bfls = []
mags = []
marginal = abcd.Ray(0, 0.1)
waves = np.linspace(0.4, 0.7, 100)  # in µm
for n1, n2 in zip(mats.nsf5(waves), mats.nbk7(waves)):
    obj_side = abcd.Transfer(f_obj)
    obj = abcd.ThickLens(math.inf, R_obj, 0, n1)
    prop = abcd.Transfer(t)
    tube = abcd.ThickLens(R_tube, math.inf, 0, n2)

    # Calculate distance to image plane:
    microscope = tube @ prop @ obj @ obj_side
    refracted = microscope @ marginal
    focal_dist = -refracted.y / refracted.u

    # Add image-plane propagation to microscope:
    img_side = abcd.Transfer(focal_dist)
    microscope @= img_side

    bfls.append(focal_dist * 1e3)  # in mm
    mags.append(microscope.A)

plt.plot(waves, bfls, color=colors[1], linestyle="dashed")
plt.xlabel("Wavelength (µm)")
plt.ylabel("Distance (mm)")
plt.title(
    "Change in focal distance\n"
    "over wavelength for a simple microscope"
)
plt.grid()
plt.show()

plt.plot(waves, mags, color=colors[2], linestyle="solid")
plt.xlabel("Wavelength (µm)")
plt.ylabel("Magnification")
plt.title(
    "Change in magnification\n"
    "over wavelength for a simple microscope"
)
plt.grid()
plt.show()


# Telescope
R1 = -200e-3
t = 75e-3
R2 = 60e-3

marginal = abcd.Ray(25e-3 / 2)
primary = abcd.Mirror(R1)
to_sec = abcd.Transfer(t)
secondary = abcd.Mirror(R2)
telescope = secondary @ to_sec @ primary

temp = telescope @ marginal
height_at_sec = temp.y
print(f"Height at secondary mirror: {height_at_sec * 1e3:g} mm")

dist_to_focus = telescope.F2
print(f"Distance to focus: {dist_to_focus * 1e3:g} mm")

to_primary = abcd.Transfer(t)
telescope @= to_primary
temp = telescope @ marginal
height_at_prim = temp.y
print(f"Hole size at primary: {height_at_prim * 1e3:g} mm")

to_focus = abcd.Transfer(dist_to_focus - t)
telescope @= to_focus

print(f"Confirming imaging condition: {telescope.A < 1e-15}")
print(f"Telescope focal length: {telescope.f2 * 1e3:g} mm")

#######################
print()
print("MISALIGNMENTS:")
#######################

# Thin lens:
f = 100e-3
displacement = 0.1
lens = abcd.ThinLens(f, decenter=displacement)
axis = abcd.Ray()
refracted = lens @ axis
# An axial ray hitting a displaced lens should
# be equivalent to a ray with a height equal
# to the displacement:
print(f"{refracted.u == displacement/f =}")
print()

# Microscope:
f_obj = 10e-3
t = 25e-3
f_tube = 100e-3

obj_side = abcd.Transfer(f_obj)
obj = abcd.ThinLens(f_obj)
prop = abcd.Transfer(t)
tube = abcd.ThinLens(f_tube)
img_side = abcd.Transfer(f_tube)
perfect_microscope = img_side @ tube @ prop @ obj @ obj_side

displacement = 100e-6
tilt = 0.001  # radians
obj = abcd.ThinLens(f_obj, decenter=displacement)
tube = abcd.ThinLens(f_tube, tilt=tilt)
misaligned_microscope = img_side @ tube @ prop @ obj @ obj_side

print("All imaging properties are identical:")
print(f"{perfect_microscope.A == misaligned_microscope.A=}")
print(f"{perfect_microscope.B == misaligned_microscope.B=}")
print(f"{perfect_microscope.C == misaligned_microscope.C=}")
print(f"{perfect_microscope.D == misaligned_microscope.D=}")
print()

print("The image is displaced by E and tilted by F:")
print(f"Displacement: {misaligned_microscope.E * 1e3:g} mm")
print(f"Tilt: {misaligned_microscope.F * 1e3:g} mrad")
print()

# Telescope
R1 = -200e-3
t = 75e-3
R2 = 60e-3
displacement = 100e-6

primary = abcd.Mirror(R1, decenter=displacement)
to_sec = abcd.Transfer(t)
secondary = abcd.Mirror(R2)
telescope = secondary @ to_sec @ primary
to_focus = abcd.Transfer(telescope.F2)
telescope @= to_focus

print(f"Confirming imaging condition: {telescope.A == 0=}")
print(f"Telescope focal length: {telescope.f2 * 1e3:g} mm")
print()

print("Impact of 100μm motion of primary:")
print(f"Image motion: {telescope.E * 1e3:g} mm")
print(f"Image tilt: {telescope.F * 1e3:g} mrad")

# Tolerancing a thick lens:
R1 = 50e-3
R2 = 75e-3
ct = 3e-3
n = 1.5
disp = 100e-6
tilt = 1e-3

means = [R1, R2, ct, n, 0, 0, 0, 0]
tols = np.array([0, 0, 50e-6, 1e-3, disp, tilt, disp, tilt])
tols = np.identity(len(tols)) * tols
covs = tols ** 2

from scipy.stats import qmc  # Quasi Monte Carlo

eng = qmc.MultivariateNormalQMC(mean=means, cov=covs)
num_trials = 2 ** (len(tols) + 1)
trials = eng.random(num_trials)
img_shifts = []
img_tilts = []
for tr in trials:
    R1, R2, ct, n, d1, t1, d2, t2 = tr

    s1 = abcd.Refraction(R1, 1, n, decenter=d1, tilt=t1)
    through = abcd.Transfer(ct, n)
    s2 = abcd.Refraction(R2, n, 1, decenter=d2, tilt=t2)
    lens = s2 @ through @ s1

    to_focus = abcd.Transfer(lens.F2)
    focuser = to_focus @ lens

    img_shifts.append(focuser.E * 1e3)
    img_tilts.append(focuser.F * 1e3)

plt.hist(img_shifts, bins=13)
plt.title(
    f"Results from Quasi Monte Carlo run with {num_trials} trials"
)
plt.xlabel("Image motion (mm)")
plt.ylabel("Number of trials")
plt.grid()
plt.show()

plt.hist(img_tilts, bins=13)
plt.title(
    f"Results from Quasi Monte Carlo run with {num_trials} trials"
)
plt.xlabel("Image tilt (mrad)")
plt.ylabel("Number of trials")
plt.grid()
plt.show()

#########################
print()
print("COMPLEX MODULES:")
#########################

# Equilateral prism oriented with its bottom parallel to u == 0
n = 1.5
mags = []
angs = np.linspace(-2, 50, 101)
for ang in angs:
    u0 = np.radians(ang)
    tilt = np.radians(-30)

    aoi1 = u0 - tilt
    aoe1 = np.arcsin(np.sin(aoi1) / n)
    u1 = aoe1 + tilt

    aoi2 = u1 + tilt
    aoe2 = np.arcsin(np.sin(aoi2) * n)
    u2 = aoe2 - tilt

    front = abcd.Refraction(math.inf, 1, n, AOI=aoi1, T_or_S="t")
    through = abcd.Transfer(15e-3, n)
    rear = abcd.Refraction(math.inf, n, 1, AOI=aoi2, T_or_S="t")
    prism = rear @ through @ front
    angular_mag = prism.D
    spatial_mag = 1 / angular_mag
    mags.append(spatial_mag)

plt.plot(angs, mags)
plt.xlabel("Angle of beam relative to u=0 (°)")
plt.ylabel("Afocal beam magnification out of prism")
plt.title("Magnification of beam by equilateral prism")
plt.grid()
plt.show()


# Curved diffraction grating
aoi = np.radians(30)
d = 1e-6
R = -200e-3
waves = np.linspace(400e-9, 700e-9, 101)

# Switching to matplotlib's object-oriented interface:
_, aoe_axes = plt.subplots()
_, bfl_axes = plt.subplots()
_, mag_axes = plt.subplots()
for plane in ["T", "S"]:
    aoes = []
    bfls = []
    mags = []
    for w in waves:
        grating = abcd.Grating(R, d=d, wavelength=w, AOI=aoi, T_or_S=plane)
        aoe = math.asin(-w / d + math.sin(aoi))

        aoes.append(np.degrees(aoe))
        bfls.append(grating.F2 * 1e3)
        mags.append(grating.A)

    aoe_axes.plot(waves * 1e9, aoes, label=plane)
    bfl_axes.plot(waves * 1e9, bfls, label=plane)
    mag_axes.plot(waves * 1e9, mags, label=plane)

aoe_axes.grid()
aoe_axes.legend()
aoe_axes.set_xlabel("Wavelength (nm)")
aoe_axes.set_ylabel("Angle out of grating (°)")
aoe_axes.set_title(
    f"Exit angle from {d * 1e6:g} µm pitch grating\n"
    f"for {np.degrees(aoi):g}° angle-of-incidence"
)

bfl_axes.grid()
bfl_axes.legend()
bfl_axes.set_xlabel("Wavelength (nm)")
bfl_axes.set_ylabel("Distance to focus (mm)")
bfl_axes.set_title(
    f"Focal distance for {R * 1e3:g} mm radius grating"
)

mag_axes.grid()
mag_axes.legend()
mag_axes.set_xlabel("Wavelength (nm)")
mag_axes.set_ylabel("Magnification")
mag_axes.set_title(f"Anamorphic magnification out of grating")

plt.show()

#########################
print()
print("EXAMPLE SYSTEMS:")
#########################

# Grating spectrometer:

# First we need a doublet design for collimation and focusing.
# This is the same procedure we used earlier:
λC = 0.6563  # µm
λD = 0.5893  # µm
λF = 0.4861  # µm
na = mats.nbk7(λD)
nb = mats.nsf5(λD)
va = (mats.nbk7(λD) - 1) / (mats.nbk7(λF) - mats.nbk7(λC))
vb = (mats.nsf5(λD) - 1) / (mats.nsf5(λF) - mats.nsf5(λC))
focal_length = 25e-3
solutions = equations.achromatic_doublet(focal_length, na, va, nb, vb)

# Here is our rough doublet prescription in a focusing configuration:
R1 = 1 / solutions[0]["C1"]
R2 = 2 / (solutions[0]["C2"] + solutions[0]["C3"])
R3 = 1 / solutions[0]["C4"]
ct = 2e-3

# Grating properties:
AOI = np.radians(45)
d = 1.6e-6
# Exit angle at 550 nm is roughly 21.3°:
center_ang = np.radians(21.3)

# Airspaces set by investigation of achromat focal planes:
to_collimator = abcd.Transfer(23.7e-3)
to_grating = abcd.Transfer(24.66e-3)
to_focuser = abcd.Transfer(24.66e-3)
to_image = abcd.Transfer(23.7e-3)

waves = np.linspace(400e-9, 700e-9, 100)
image_dists = []
image_NAs = []
image_sizes = []
image_heights = []
for w in waves:
    # Materials expect wavelength in µm:
    n1, n2 = mats.nbk7(w * 1e6), mats.nsf5(w * 1e6)

    # Collimating doublet (reversed):
    el1 = abcd.ThickLens(-R3, -R2, ct, n2)
    el2 = abcd.ThickLens(-R2, -R1, ct, n1)
    collimator = el2 @ el1

    # Grating (assuming tangential only):
    AOE = math.asin(-w / d + math.sin(AOI))
    # Approximating change in exit angle as paraxial angular shift:
    F = AOE - center_ang
    grating = abcd.Grating(math.inf, d=d, wavelength=w, AOI=AOI, F=F)

    # Focusing doublet:
    el1 = abcd.ThickLens(R1, R2, ct, n1)
    el2 = abcd.ThickLens(R2, R3, ct, n2)
    focuser = el2 @ el1

    # Now put it all together:
    spectrometer = (
        to_image
        @ focuser
        @ to_focuser
        @ grating
        @ to_grating
        @ collimator
        @ to_collimator
    )

    # Now trace a marginal and chief ray:
    # Values from Thorlabs FG025LJA fiber
    size = 12.5e-6
    NA = 0.1
    axis = abcd.Ray(wavelength=w)
    marginal = abcd.Ray(0, NA, wavelength=w)
    chief = abcd.Ray(size, 0, wavelength=w)

    axis @= spectrometer
    marginal @= spectrometer
    chief @= spectrometer

    image_dists.append(
        (marginal.y - axis.y) / (marginal.u - axis.u) * 1e3
    )
    image_NAs.append(abs(marginal.u - axis.u))
    image_sizes.append(abs((chief.y - axis.y) * 1e3))
    image_heights.append(axis.y * 1e3)

# Depth of focus in mm:
depths_of_focus = [1e-3 / (2 * na) ** 2 for na in image_NAs]
# Reframing focus over wavelength as multiples of depth of focus:
focus_error = [b / d for b, d in zip(image_dists, depths_of_focus)]

plt.plot(waves * 1e9, focus_error, color=colors[1])
plt.ylabel("Focus error (multiples of depth of focus)")
plt.xlabel("Wavelength (nm)")
plt.title("Focus variation at image plane over wavelength")
plt.grid()
plt.show()

# We can divide our wavelength span by our image height span
# to get a sensitivity in nm / mm:
wave_span = (np.max(waves) - np.min(waves)) * 1e9  # nm
height_span = np.max(image_heights) - np.min(image_heights)  # mm
image_plane_sens = wave_span / height_span  # nm / mm
# Then we can multiply the image height for a given wavelength
# by our nm / mm sensitivity:
res_over_wave = [image_plane_sens * s for s in image_sizes]  # nm

plt.plot(waves * 1e9, res_over_wave, color=colors[2])
plt.ylabel("Resolution (nm)")
plt.xlabel("Wavelength (nm)")
plt.title("Spectral resolution over wavelength")
plt.grid()
plt.show()


# Fiber-coupled tunable filter:
n0 = mats.fs7980(1550e-9 * 1e6)
R2 = (1 - n0) * 15e-3
filter_thickness = 2e-3
fiber_mode_radius = 5e-6
center_wavelength = 1600e-9
neff = 1.7  # estimated filter effective index
fwhm = 2e-9
std = fwhm / (2 * np.sqrt(2 * np.log(2)))

AOIs = np.radians(np.linspace(0, 35, 301))
waves = np.linspace(1500e-9, center_wavelength, 301)
coupling = np.zeros((len(waves), len(AOIs)))

# Nominal values are at 1550 nm:
to_collimator = abcd.Transfer(13.6146e-3)
to_fiber = abcd.Transfer(13.6146e-3)
to_filter = abcd.Transfer(10e-3)
to_focuser = abcd.Transfer(10e-3)

for i, w in enumerate(waves):
    # Materials expect wavelength in µm:
    n = mats.fs7980(w * 1e6)

    collimator = abcd.ThickLens(math.inf, R2, 2e-3, n)
    focuser = abcd.ThickLens(-R2, math.inf, 2e-3, n)

    for j, AOI in enumerate(AOIs):
        # We can estimte the filter transmission and scale 
        # the coupling efficiency to account for it.
        # We shift the center wavelength using the effective index:
        eff_cwl = center_wavelength * np.sqrt(1 - (np.sin(AOI) / neff) ** 2)
        fil_trans = np.exp(-(((w - eff_cwl) / (2 * std)) ** 2))

        # If the filter transmission is minimal, we can skip
        # the rest of the calculation to save time:
        if fil_trans < 0.001:
            coupling[i, j] = 0
            continue

        filter_front = abcd.Refraction(math.inf, 1, n, AOI=AOI)
        filter_prop = abcd.Transfer(filter_thickness)
        filter_back = abcd.Refraction(math.inf, n, 1, AOI=AOI / n)
        tilted_filter = (filter_back @ filter_prop @ filter_front)

        # Because the filter is tilted, we need to calculate
        # how much the tilt changes the image at the output fiber.
        # Beam displacement of a tilted window per Thorlabs:
        beam_displacement = (
            filter_thickness
            * np.sin(AOI)
            * (1 - np.cos(AOI) / np.sqrt(n ** 2 - np.sin(AOI) ** 2))
        )
        image_tilt = beam_displacement / focuser.f2

        # Now we can calculate the transverse properties:
        tunable_filter = (
            to_fiber
            @ focuser
            @ to_focuser
            @ tilted_filter
            @ to_filter
            @ collimator
            @ to_collimator
        )

        beam = abcd.GaussianBeam(wavelength=w, z=0, w=5e-6)
        beam @= tunable_filter

        params = [
            w,  # wavelength
            beam.w,  # incoming beam size
            fiber_mode_radius,  # fiber beam size
            0,  # transverse misalignment
            beam.z,  # longitudinal misalignment
            image_tilt,  # angular misalignment
        ]

        fiber_overlap = equations.fiber_coupling_efficiency(*params)
        coupling[i, j] = fiber_overlap * fil_trans

# Adapted from the matplotlib example for projecting contour profiles:
X, Y = np.meshgrid(np.degrees(AOIs), waves * 1e9)
Z = coupling
from matplotlib import cm

ax = plt.figure().add_subplot(projection="3d")
ax.plot_surface(X, Y, Z, alpha=0.35)

ax.contour(X, Y, Z, zdir="z", offset=0, cmap=cm.coolwarm)
ax.contour(X, Y, Z, zdir="x", offset=np.min(X), cmap=cm.coolwarm)
ax.contour(X, Y, Z, zdir="y", offset=np.max(Y), cmap=cm.coolwarm)

ax.set(
    xlabel="Filter tilt (°)",
    ylabel="Wavelength (nm)",
    zlabel="Coupling efficiency",
    zlim=(0, 1),
)

plt.title("Angle-tuning curve for filter")
plt.show()

