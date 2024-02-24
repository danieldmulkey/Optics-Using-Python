import math

"""Docstring for the equations.py module.

This module contains a small collection of optical equations
to demonstrate some possible Python implementations.
"""


def rayleigh_resolution(wavelength, fno):
    """Calculates the image-space resolution of a lens
    using the Rayleigh criterion.

    Parameters
    ----------
    wavelength : float
        Vacuum wavelength in µm.
    fno : float
        f/# of the lens.

    Returns
    -------
    Z : float
        Minimum resolved distance at image in µm

    References
    ----------
    W. Smith, Modern Optical Engineering, 4th ed, p. 193.
    """
    Z = 1.22 * wavelength * fno
    return Z


def diffraction_angle(
    wavelength, period, angle_in=0, order=-1, sign=1
):
    """Calculates the diffraction angle from a grating.

    Parameters
    ----------
    wavelength : float
        Vacuum wavelength in µm.
    period : float
        Grating period in μm.
    angle_in : float
        Angle of incident wave in degrees.
    order : float
        Diffraction order of interest.
    sign : float
        +1 selects the convention sin(θ1) - sin(θ2),
        whereas -1 is for sin(θ1) + sin(θ2)

    Returns
    -------
    angle_out : float
        Angle of diffracted wave in degrees.

    References
    ----------
    B. E. A. Saleh and M. C. Teich, Fundamentals of Photonics, p. 56.
    """
    sign = 1 if sign >= 0 else -1
    S1 = math.sin(math.radians(angle_in))
    return math.degrees(
        math.asin(order * wavelength / period + sign * S1)
    )


def fiber_coupling_efficiency(
    wavelength,
    incoming_waist,
    fiber_waist,
    transverse=0,
    longitudinal=0,
    angular=0,
    n=1,
):
    """Calculates fiber coupling efficiency assuming
    incoming mode and fiber mode are Gaussians.

    Parameters
    ----------
    incoming_waist : float
        1/e^2 irradiance radius of incoming mode at
        focus in µm.
    fiber_waist : float
        1/e^2 irradiance radius of best-fit Gaussian
        to fiber mode in µm.
    transverse : float
        Transverse distance between incoming and fiber
        focii in µm.
    longitudinal : float
        Longitudinal distance between incoming and fiber
        focii in µm.
    angular : float
        Angle between propagation directions of incoming
        and fiber focii in degrees.
    wavelength : float
        Vacuum wavelength in µm.
    n : float
        Index of material surrounding fiber, defaults to air.

    Returns
    -------
    η : float
        Coupling efficiency ranging from 0 to 1.

    References
    ----------
    F. C. Allard, Fiber Optics Handbook for Engineers
    and Scientists, pp. 3.12
    """
    k = math.tau * n / wavelength
    A = (k * incoming_waist) ** 2 / 2
    D = (fiber_waist / incoming_waist) ** 2
    F = 2 * transverse / (k * incoming_waist**2)
    G = 2 * longitudinal / (k * incoming_waist**2)
    B = G**2 + (D + 1) ** 2
    C = (
        (D + 1) * F**2
        + 2 * D * F * G * math.sin(math.radians(angular))
        + D * (G**2 + D + 1) * math.sin(math.radians(angular)) ** 2
    )
    η = 4 * D / B * math.exp(-A * C / B)
    return η


def critical_angle(index):
    """Calculates the angle for total internal reflection
    inside a glass suspended in air.

    Parameters
    ----------
    index : float
        Index of refraction of glass relative to air.

    Returns
    -------
    angle : float
        Critical angle in degrees.

    References
    ----------
    F. C. Allard, Fiber Optics Handbook for Engineers
    and Scientists, pp. 1.3
    """
    angle = math.degrees(math.asin(1 / index))
    return angle


def NA_from_indices(core_index, cladding_index):
    """Calculates numerical aperture of a step-index fiber
    using core and cladding indices.

    Parameters
    ----------
    core_index : float
        Index of refraction of fiber core.
    cladding_index : float
        Index of refraction of fiber cladding.

    Returns
    -------
    NA : float
        Numerical aperture of fiber based on critical
        angle between fiber indices.

    References
    ----------
    F. C. Allard, Fiber Optics Handbook for Engineers
    and Scientists, pp. 1.3
    """
    NA = (core_index**2 - cladding_index**2) ** 0.5
    return NA


def best_fit_waist(
    core_index, cladding_index, core_radius, wavelength
):
    """Calculates 1/e^2 irradiance radius of a Gaussian
    beam best matched to the real fiber mode given by
    `core_index,` `cladding_index,` and `wavelength.`

    Parameters
    ----------
    core_index : float
        Index of refraction of fiber core.
    cladding_index : float
        Index of refraction of fiber cladding.
    core_radius : float
        Radius of the fiber core in µm.
    wavelength : float
        Vacuum wavelength in µm.

    Returns
    -------
    w : float
        1/e^2 irradiance radius of best-fit Gaussian in µm.

    References
    ----------
    F. C. Allard, Fiber Optics Handbook for Engineers
    and Scientists, pp. 3.12
    """
    V = (
        math.tau
        * core_radius
        / wavelength
        * (core_index**2 - cladding_index**2) ** 0.5
    )
    w = core_radius * (0.65 + 1.619 / V**1.5 + 2.879 / V**6)
    return w


def fresnel_reflection(n1=1, n2=1.5, AOI=0, S_or_P="P"):
    """Calculates the field reflection coefficient ρ
    for an interface between materials with indices n1 and n2.
    For the reflected power, calcluate ρ**2. AOI is in degrees.
    S refers to polarization perpendicular to the plane of incidence.
    P refers to polarization lying inside the plane of incidence.
    Using the form from Electromagnetic Waves and Antennas by S. Orfanidis where
    the equation is recast into only n1, n2, and the angle of incidence
    """
    AOI = math.radians(AOI)
    if S_or_P.lower() == "p":
        return (
            math.sqrt((n2 / n1) ** 2 - math.sin(AOI) ** 2)
            - (n2 / n1) ** 2 * math.cos(AOI)
        ) / (
            math.sqrt((n2 / n1) ** 2 - math.sin(AOI) ** 2)
            + (n2 / n1) ** 2 * math.cos(AOI)
        )
    elif S_or_P.lower() == "s":
        return (
            math.cos(AOI)
            - math.sqrt((n2 / n1) ** 2 - math.sin(AOI) ** 2)
        ) / (
            math.cos(AOI)
            + math.sqrt((n2 / n1) ** 2 - math.sin(AOI) ** 2)
        )


def q_from_R_w(R, w, wavelength=532e-9, n=1):
    """Calculates the reduced q value of a Gaussian beam
    when given radius R and size w"""
    return 1 / (n / R - 1j * wavelength / (math.pi * w**2))


def q_from_z_zR(z, zR, n=1):
    """Calculates the reduced q value of a Gaussian beam
    when given position z and Rayleigh range zR"""
    return z / n + 1j * zR / n


def q_from_R_z(R, z, n=1):
    """Calculates the reduced q value of a Gaussian beam when given
    radius R and position z based on the equation for R(z)"""
    if z == 0 or R == math.inf:
        raise ValueError(
            "Cannot have z == 0 or R == infinity "
            "when specifying R and z"
        )
    zR = ((R - z) * z) ** 0.5
    if isinstance(zR, complex) or zR == 0:
        raise ValueError("Must have |z| < |R|")
    return (z + 1j * zR) / n


def q_from_R_zR(R, zR, n=1, sign=1):
    """Calculates the reduced q value of a Gaussian beam when given
    radius R and Rayleigh range zR based on the equation for R(z) by
    solving 0 == z**2 - R*z + zR**2.
    sign == 1 corresponds to z such that R is in the near-field.
    sign == -1 corresponds to z such that R is in the far-field"""
    sign = 1 if sign >= 0 else -1
    # Flipping sign so this and the w & z equation match:
    z = (R - sign * (R**2 - 4 * zR**2) ** 0.5) / 2
    if isinstance(z, complex):
        raise ValueError("Must have 2 * zR <= R")
    return (z + 1j * zR) / n


def q_from_w_z(w, z, wavelength=532e-9, n=1, sign=1):
    """Calculates the reduced q value of a Gaussian beam when given
    size w and position z based on the equation for w(z) by
    solving 0 == zR**2 - n*pi*w**2/λ0 * zR + z**2
    sign == 1 corresponds to zR such that w is in the near-field.
    sign == -1 corresponds to zR such that w is in the far-field"""
    b = -n * math.pi * w**2 / wavelength
    discrim = b**2 - 4 * z**2
    sign = 1 if sign >= 0 else -1
    zR = (-b + sign * discrim**0.5) / 2
    if isinstance(zR, complex):
        raise ValueError("Must have |z| <= |n * π * w**2 / λ0|")
    return (z + 1j * zR) / n


def q_from_w_zR(w, zR, wavelength=532e-9, n=1, sign=1):
    """Calculates the reduced q value of a Gaussian beam when given
    size w and Rayleigh range zR based on equation for w(z)
    sign == 1 corresponds to z such that the beam is
        leaving the waist.
    sign == -1 corresponds to z such that the beam is
        approaching the waist"""
    sign = 1 if sign >= 0 else -1
    z = sign * ((n * math.pi * w**2 / wavelength - zR) * zR) ** 0.5
    if isinstance(z, complex):
        raise ValueError("Must have zR <= n * π * w**2 / λ0")
    return (z + 1j * zR) / n


def achromatic_doublet(focal_length, na, va, nb, vb):
    """Given effective focal length and refractive index and Abbe V# of materials A and B,
    calculate the four necessary curvatures for a doublet with no spherical aberration,
    no coma, and no axial color. Uses thin-lens G-sums. Based on the procedure from
    Lens Design by Milton Laikin."""
    Fa = (va - vb) * focal_length / va
    Fb = (vb - va) * focal_length / vb
    Ca = 1 / (Fa * (na - 1))
    Cb = 1 / (Fb * (nb - 1))

    H = G8(nb) * Cb**2 - G8(na) * Ca**2 - G7(nb) * Cb / focal_length
    I = G5(na) * Ca / 4
    K = G5(nb) * Cb / 4
    A = (
        G1(na) * Ca**3
        + G1(nb) * Cb**3
        - G3(nb) * Cb**2 / focal_length
        + G6(nb) * Cb / focal_length**2
    )
    B = -G2(na) * Ca**2
    E = G4(na) * Ca
    J = G4(nb) * Cb
    D = G2(nb) * Cb**2 - G5(nb) * Cb / focal_length
    P = A + H * (J * H / K - D) / K
    Q = B + I * (2 * J * H / K - D) / K
    R = E + J * (I / K) ** 2
    root = Q**2 - 4 * P * R
    if root < 0:
        return

    s1 = {"C1": (-Q + math.sqrt(root)) / (2 * R)}
    s1["C4"] = -(H + I * s1["C1"]) / K
    s1["C2"] = s1["C1"] - Ca
    s1["C3"] = Cb + s1["C4"]
    sols = [s1]
    if root == 0:
        return sols

    s2 = {"C1": (-Q - math.sqrt(root)) / (2 * R)}
    s2["C4"] = -(H + I * s2["C1"]) / K
    s2["C2"] = s2["C1"] - Ca
    s2["C3"] = Cb + s2["C4"]
    sols.append(s2)
    return sols


def G1(n):
    return n**2 * (n - 1) / 2


def G2(n):
    return (2 * n + 1) * (n - 1) / 2


def G3(n):
    return (3 * n + 1) * (n - 1) / 2


def G4(n):
    return (n + 2) * (n - 1) / (2 * n)


def G5(n):
    return 2 * (n**2 - 1) / n


def G6(n):
    return (3 * n + 2) * (n - 1) / (2 * n)


def G7(n):
    return (2 * n + 1) * (n - 1) / (2 * n)


def G8(n):
    return n * (n - 1) / 2
