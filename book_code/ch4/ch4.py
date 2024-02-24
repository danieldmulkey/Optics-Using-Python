import matplotlib
# Uncomment to make high-resolution images for print:
# matplotlib.rcParams['figure.dpi'] = 300

import numpy as np
import matplotlib.pyplot as plt

#####################
print()
print("RAY TRACING:")
#####################

# SA and coma vs bending parameter for single lens:
from rayoptics.environment import *

def generate_layout(bending, efl=200):
    c1 = (bending+1)/efl
    c2 = (bending-1)/efl

    opm = OpticalModel()
    sm  = opm['seq_model']
    osp = opm['optical_spec']
    osp['pupil'] = PupilSpec(osp, key=['object', 'pupil'], value=25)
    osp['fov'] = FieldSpec(osp, key=['object', 'angle'], value=1, flds=[0, 2**0.5/2, 1], is_relative=True)
    osp['wvls'] = WvlSpec([('d', 1.0)])

    opm.radius_mode = True
    sm.gaps[0].thi=1e10
    sm.add_surface([0, 0])
    sm.set_stop()
    sm.add_surface([1/c1, 2, 'N-BK7', 'Schott'])
    sm.add_surface([1/c2, 200])

    opm.update_model()
    return opm

N = 31
seidel_spherical = []
seidel_coma = []
bending_parameters = np.linspace(-3, 4, N)
for B in bending_parameters:
    opm = generate_layout(B)

    third_order = compute_third_order(opm)
    seidel_spherical.append(third_order['S-I']['sum'])
    seidel_coma.append(third_order['S-II']['sum'])
    
plt.plot(bending_parameters, seidel_spherical, label='SA')
plt.plot(bending_parameters, seidel_coma, label='Coma')
plt.title('Spherical Aberration and Coma of a Singlet')
plt.xlabel(r'Bending parameter $\frac{\Sigma C}{\Delta C}$')
plt.ylabel('Seidel aberration sum')
plt.legend()
plt.grid()

shape = bending_parameters[np.argmin(seidel_spherical)]
optimal_layout = generate_layout(shape)
layout_plt = plt.figure(FigureClass=InteractiveLayout, opt_model=optimal_layout).plot()
plt.show()

matplotlib.rcParams.update(matplotlib.rcParamsDefault)
# matplotlib.rcParams['figure.dpi'] = 300

###############################
print()
print("WAVE PROPAGATION:")
###############################

# Clipped Airy as approximation of Gaussian
import LightPipes as lp

grid_size = 5 * lp.mm
grid_dimension = 1024
λ = 500 * lp.nm
field = lp.Begin(grid_size, λ, grid_dimension)

R = 1 * lp.mm
field = lp.CircAperture(field, R)
plt.figure()
plt.imshow(lp.Intensity(field))
plt.title("Initial Flat-Top Beam")

f = 1 * lp.m
field = lp.Lens(field, f)
field = lp.Fresnel(field, f)
plt.figure()
plt.imshow(np.log10(lp.Intensity(field)))
plt.title("Log scale: Beam at Focus")

R = 300 * lp.um
field = lp.CircAperture(field, R)
plt.figure()
plt.imshow(np.log10(lp.Intensity(field)))
plt.title("Log scale: Clipped to Central Lobe")

field = lp.Fresnel(field, f)
plt.figure()
plt.imshow(lp.Intensity(field))
plt.title("Filtered Beam After Propagation")

wx, wy = lp.D4sigma(field)
clipped_airy_slice = lp.Intensity(field, 1)[grid_dimension // 2, :]
gaussian = lp.GaussBeam(field, wx / 2)
gaussian_slice = lp.Intensity(gaussian, 1)[grid_dimension // 2, :]
plt.figure()
plt.plot(clipped_airy_slice, "b-", label="Clipped Airy")
plt.plot(gaussian_slice, "r--", label="Gaussian")
plt.title("Slice through center of beam")
plt.legend()
plt.grid()
plt.show()

######################
print()
print("POLARIZATION:")
######################

import py_pol.stokes
import py_pol.mueller

retardance_values = np.linspace(0, np.pi, 11)

S = py_pol.stokes.Stokes('H source')
S.linear_light()
M1 = py_pol.mueller.Mueller('Half-wave plate')
M1.retarder_linear(retardance_values, np.pi/8)
S_hwp = M1 * S
fig1 = S_hwp.draw_poincare(kind='scatterline')
fig1.show()


waveplate_angles = np.linspace(0, np.pi/2, 21)
M2 = py_pol.mueller.Mueller('Rotating quarter-wave plate')
M2.quarter_waveplate(waveplate_angles)
S_qwp = M2 * S
fig2 = S_qwp.draw_poincare(kind='scatterline')
fig2.show()

###############################
print()
print("TRANSFER MATRIX METHOD:")
###############################

# Used https://lightmachinery.com/optical-design-center/thin-film-cloud/
# to generate a coating design. The plot here varies somewhat from their
# calculated response due to differences in material index models

import tmm
from materials import mgf2 as L
from materials import tio2 as H
from materials import nbk7, air

lambda_list = np.linspace(350, 850, 500)  # in nm
angle_of_incidence = 0

# In nm:
layer_thicknesses = [np.inf,  # N-BK7 substrate
    9.84, 42.29, 29.12, 18.39, 79.35, 14.78, 26.90, 102.65,
    np.inf,  # air
]

R_list = []
for lambda_vac in lambda_list:
    layer_indices = (
        [nbk7(lambda_vac/1e3)] 
        + 4*[H(lambda_vac/1e3), L(lambda_vac/1e3)] 
        + [air(lambda_vac/1e3)]
    )
    
    R_list.append(
        100 * tmm.coh_tmm(
            "s", 
            layer_indices, 
            layer_thicknesses, 
            angle_of_incidence,
            lambda_vac)["R"]
    )

plt.figure()
plt.plot(lambda_list, R_list)
plt.xlabel("Wavelength (nm)")
plt.ylabel("Percent of power reflected (%)")
plt.title("Reflection at normal incidence")
plt.grid()
plt.show()

###############################
print()
print("FIELD SOLVERS:")
###############################

# Run on a Linux virtual machine (e.g. Ubuntu):

# import os
# import meep as mp

# RAP_vertices = [
#     mp.Vector3(-2, -3, -3),
#     mp.Vector3(-2, 3, -3),
#     mp.Vector3(4, -3, -3),
# ]

# # N-BK7 right-angle prism:
# glass = mp.Medium(epsilon=1.5214**2)
# RAP = mp.Prism(RAP_vertices, height=6, axis=mp.Vector3(0, 0, 1), material=glass)

# # Calcite prism with extraordinary axis in Y:
# no = 1.666
# ne = 1.4897
# calcite = mp.Medium(epsilon_diag=mp.Vector3(no**2, ne**2, no**2))
# birefringent_RAP = mp.Prism(
#     RAP_vertices, height=6, axis=mp.Vector3(0, 0, 1), material=calcite
# )

# size = 14
# resolution = 50
# dpml = 2
# cell_size = mp.Vector3(size, size)
# boundary_layers = [mp.PML(thickness=dpml)]
# beam_x0 = mp.Vector3(0, 3)  # beam focus (relative to source center)
# beam_kdir = mp.Vector3(0, 1, 0)
# beam_w0 = 0.8  # beam waist radius
# beam_E0 = mp.Vector3(1, 0, 0)
# center_freq = 1 / 0.5
# sources = [
#     mp.GaussianBeamSource(
#         src=mp.ContinuousSource(center_freq),
#         center=mp.Vector3(1, -size / 2 + dpml + 1),
#         size=mp.Vector3(size),
#         beam_x0=beam_x0,
#         beam_kdir=beam_kdir,
#         beam_w0=beam_w0,
#         beam_E0=beam_E0,
#     )
# ]

# for material, prism in zip(("BK7", "Calcite"), (RAP, birefringent_RAP)):
#     sim = mp.Simulation(
#         resolution=resolution,
#         cell_size=cell_size,
#         boundary_layers=boundary_layers,
#         sources=sources,
#         geometry=[prism],
#     )

#     sim.run(
#         mp.at_end(mp.output_tot_pwr, mp.output_epsilon),
#         until=20,
#     )

#     os.system(
#         '/usr/bin/h5topng -Zc dkbluered ' 
#         + f'-o "book_code/ch4/{material}.png" '
#         + '-C ch4-eps-000020.00.h5 ' 
#         + 'ch4-energy-000020.00.h5 '
#     )


###############################
print()
print("MATERIALS:")
###############################

from opticalglass import rindexinfo
nbk7_url = 'https://refractiveindex.info/database/data-nk/glass/schott/N-BK7.yml'
yaml, name, catalog = rindexinfo.read_rii_url(nbk7_url)
nbk7 = rindexinfo.create_material(yaml, name, catalog)

waves = np.linspace(400, 700, 100)  # in nm
index_data = nbk7.calc_rindex(waves)

plt.plot(waves, index_data)
plt.title('Index data from calc_rindex()')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Relative refractive index')
plt.grid()
plt.show()

###############################
print()
print("COLOR AND RADIOMETRY:")
###############################

from pyradi import ryplanck
from pyradi import ryutils

waves = np.linspace(0.2, 2, 1000)  # in μm
plt.figure()
for T in [300, 1000, 2000, 3000, 4000, 5000, 6000]:
    blackbody = ryplanck.planck(waves, T)
    plt.plot(waves, blackbody, label=f'{T} K')
plt.title('Radiant Exitance of Blackbodies at Different Temperatures')
plt.xlabel('Wavelength (μm)')
plt.ylabel(r'Radiant Exitance $\frac{W}{m^2 \mu m}$')
plt.legend()
plt.grid()

waves = np.linspace(0.2, 16, 1000)  # in μm
plt.figure()
for T in [300, 1000, 2000, 3000, 4000, 5000, 6000]:
    blackbody = ryplanck.planck(waves, T)
    normalized = blackbody / np.max(blackbody)
    plt.semilogx(waves, normalized, label=f'{T} K')
plt.title('Normalized Exitance of Blackbodies at Different Temperatures')
plt.xlabel('Wavelength (μm)')
plt.ylabel('Normalized Exitance')
plt.legend()
plt.grid()

waves = np.linspace(0.4, 2, 1000)
freq = ryutils.convertSpectralDomain(waves, 'lf') / 1e12  # in THz
wavenumber = ryutils.convertSpectralDomain(waves, 'ln')  # in 1/cm

plt.figure()
plt.plot(waves, freq)
plt.title('Conversion from Wavelength to Frequency')
plt.xlabel('Wavelength (μm)')
plt.ylabel('Frequency (THz)')
plt.grid()

plt.figure()
plt.plot(waves, wavenumber)
plt.title('Conversion from Wavelength to Wavenumber')
plt.xlabel('Wavelength (μm)')
plt.ylabel(r'Wavenumber ($cm^{-1}$)')
plt.grid()

plt.figure()
plt.plot(wavenumber, freq)
plt.title('Conversion from Wavenumber to Frequency')
plt.xlabel(r'Wavenumber ($cm^{-1}$)')
plt.ylabel('Frequency (THz)')
plt.grid()
plt.show()

