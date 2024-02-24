def air(wavelength, temperature=20, pressure=101325):
    """Calculates refractive index of air.

    Parameters
    ----------
    wavelength : float
        Vacuum wavelength in µm.
    temperature : float
        Temperature in °C.
    pressure : float
        Presure in Pa.

    Returns
    -------
    n : float
        Refractive index of material at wavelength, temperature, and pressure.

    References
    ----------
    K. Schwertz and J. H. Burge, Field Guide to Optomechanical Design and Analysis, p. 102.
    W. J. Smith, Modern Optical Engineering, 4th Ed, p. 4.
    """
    ns = (
        8342.54
        + 2406147 / (130 - 1 / wavelength**2)
        + 15998 / (38.9 - 1 / wavelength**2)
    ) * 1e-8

    n = 1 + pressure * ns / 96095.43 * (
        1 + 1e-8 * (0.601 - 9.72e-3 * temperature) * pressure
    ) / (1 + 3.661e-3 * temperature)
    return n


def nbk7(wavelength, temperature=20, pressure=101325):
    """Calculates refractive index of Schott N-BK7 in air.

    Parameters
    ----------
    wavelength : float
        Wavelength in µm.
        Valid for 365 nm to 1.06 μm
    temperature : float
        Temperature of glass in °C.
    pressure : float
        Pressure of surrounding air in Pa.

    Returns
    -------
    n : float
        Refractive index of material at wavelength.

    References
    ----------
    https://shop.schott.com/advanced_optics/en/SCHOTT-N-BK7/c/glass-SCHOTT%20N-BK7%C2%AE
    """

    # Absolute index:
    B1 = 1.03961212
    B2 = 0.231792344
    B3 = 1.01046945
    C1 = 0.00600069867
    C2 = 0.0200179144
    C3 = 103.560653
    n = (
        1
        + B1 * wavelength**2 / (wavelength**2 - C1)
        + B2 * wavelength**2 / (wavelength**2 - C2)
        + B3 * wavelength**2 / (wavelength**2 - C3)
    ) ** 0.5

    # Temperature dependence:
    D0 = 1.86e-6
    D1 = 1.31e-8
    D2 = -1.37e-11
    E0 = 4.34e-7
    E1 = 6.27e-10
    wavelength_tk = 0.17  # in μm
    ΔT = temperature - 20
    Δn = (
        (n**2 - 1)
        / (2 * n)
        * (
            D0 * ΔT
            + D1 * ΔT**2
            + D2 * ΔT**3
            + (E0 * ΔT + E1 * ΔT**2)
            / (wavelength**2 - wavelength_tk**2)
        )
    )
    n = n + Δn

    # In air:
    n = n / air(wavelength, temperature, pressure)
    return n


def nsf5(wavelength, temperature=20, pressure=101325):
    """Calculates refractive index of Schott N-SF5 in air.

    Parameters
    ----------
    wavelength : float
        Wavelength in µm.
        Valid for 405 nm to 2.326 μm
    temperature : float
        Temperature of glass in °C.
    pressure : float
        Pressure of surrounding air in Pa.

    Returns
    -------
    n : float
        Refractive index of material at wavelength.

    References
    ----------
    https://www.schott.com/shop/advanced-optics/en/Optical-Glass/N-SF5/c/glass-N-SF5
    """

    # Absolute index:
    B1 = 1.52481889
    B2 = 0.187085527
    B3 = 1.427290150
    C1 = 0.01125475600
    C2 = 0.0588995392
    C3 = 129.1416750
    n = (
        1
        + B1 * wavelength**2 / (wavelength**2 - C1)
        + B2 * wavelength**2 / (wavelength**2 - C2)
        + B3 * wavelength**2 / (wavelength**2 - C3)
    ) ** 0.5

    # Temperature dependence:
    D0 = -2.51e-07
    D1 = 1.07e-08
    D2 = -2.40e-11
    E0 = 7.85e-07
    E1 = 1.15e-09
    wavelength_tk = 0.278  # in μm
    ΔT = temperature - 20
    Δn = (
        (n**2 - 1)
        / (2 * n)
        * (
            D0 * ΔT
            + D1 * ΔT**2
            + D2 * ΔT**3
            + (E0 * ΔT + E1 * ΔT**2)
            / (wavelength**2 - wavelength_tk**2)
        )
    )
    n = n + Δn

    # In air:
    n = n / air(wavelength, temperature, pressure)
    return n


def fs7980(wavelength, temperature=22, pressure=101325):
    """Calculates refractive index of Corning High Purity Fused Silica 7980 in air.

    Parameters
    ----------
    wavelength : float
        Wavelength in µm.
        Valid for 185 nm to 1.129 μm
    temperature : float
        Temperature of glass in °C.
        Valid for 22 °C to 25 °C
    pressure : float
        Pressure of surrounding air in Pa.

    Returns
    -------
    n : float
        Refractive index of material at wavelength.

    References
    ----------
    https://www.corning.com/media/worldwide/csm/documents/5bf092438c5546dfa9b08e423348317b.pdf
    """

    # Absolute index:
    A0 = 2.104025406e00
    A1 = -1.456000330e-04
    A2 = -9.049135390e-03
    A3 = 8.801830992e-03
    A4 = 8.435237228e-05
    A5 = 1.681656789e-06
    A6 = -1.675425449e-08
    A7 = 8.326602461e-10

    n = (
        A0
        + A1 * wavelength**4
        + A2 * wavelength**2
        + A3 * wavelength**-2
        + A4 * wavelength**-4
        + A5 * wavelength**-6
        + A6 * wavelength**-8
        + A7 * wavelength**-10
    ) ** 0.5

    # Temperature dependence:
    C0 = 9.390590
    C1 = 0.235290
    C2 = -1.318560e-03
    C3 = 3.028870e-04
    ΔT = temperature - 22
    Δn = (
        (
            C0
            + C1 / wavelength**2
            + C2 / wavelength**4
            + C3 / wavelength**6
        )
        * ΔT
        * 1e-6
    )
    n = n + Δn

    # In air:
    n = n / air(wavelength, temperature, pressure)
    return n


def noa61(wavelength):
    """Calculates absolute refractive index of Norland Optical Adhesive 61.
    Gives absolute index, rather than relative, as it's assumed that the
    adhesive is used between glass surfaces. Calculated for T = 25 °C only.

    Parameters
    ----------
    wavelength : float
        Wavelength in μm.

    Returns
    -------
    n : float
        Refractive index of material at wavelength.

    References
    ----------
    https://www.norlandprod.com/adhesives/noa61pg2.html
    """

    # Absolute index:
    n = (
        1.5375
        + 8290.45 / (wavelength * 1e3) ** 2
        - 2.11046e8 / (wavelength * 1e3) ** 4
    )
    return n


def znse(wavelength, temperature=20, pressure=101325):
    """Calculates refractive index of II-VI Zinc Selenide.

    Parameters
    ----------
    wavelength : float
        Wavelength in µm.
    temperature : float
        Temperature of glass in °C.
    pressure : float
        Pressure of surrounding air in Pa.

    Returns
    -------
    n : float
        Refractive index of material at wavelength.

    References
    ----------
    Index vs wavelength data from https://ii-vi.com/product/zinc-selenide-znse/
    Coefficients calculated using findcurves.com for SELLMOD6 2D equation
    Data was n, fit was to n**2, so removed ()**0.5 around n below.
    """

    # Absolute index:
    A = 2.4111569588609116
    B = 0.59479976285565850
    C = -0.28953183849065445
    D = 1204.4848710547462
    E = 45.910794001839250
    n = (
        A
        + B * wavelength**2 / (wavelength**2 - C**2)
        + D / (wavelength**2 - E**2)
    )

    # Temperature dependence:
    dndT = 61e-6  # at 10.6 μm, higher at lower wavelength
    ΔT = temperature - 20
    Δn = dndT * ΔT
    n = n + Δn

    # In air:
    n = n / air(wavelength, temperature, pressure)
    return n


def mgf2(wavelength, temperature=25, pressure=101325):
    """Calculates refractive index of Magnesium Fluoride in air.

    Parameters
    ----------
    wavelength : float
        Wavelength in µm.
    temperature : float
        Temperature of glass in °C.
    pressure : float
        Pressure of surrounding air in Pa.

    Returns
    -------
    n : float
        Refractive index of material at wavelength.

    References
    ----------
    https://refractiveindex.info/?shelf=main&book=MgF2&page=Rodriguez-de_Marcos
    Fit using findcurves.com
    """

    # Absolute index:
    A = 1.4177428299172710e00
    B = 1.1505948761303543e-02
    C = -3.4962526545629879e-01
    D = -8.0656421284475994e-03
    E = 9.5656756857168387e-02
    n = A + B / (C - wavelength) + D / (E - wavelength)

    # In air:
    n = n / air(wavelength, temperature, pressure)
    return n


def tio2(wavelength, temperature=25, pressure=101325):
    """Calculates refractive index of Titanium Dioxide in air.

    Parameters
    ----------
    wavelength : float
        Wavelength in µm.
    temperature : float
        Temperature of glass in °C.
    pressure : float
        Pressure of surrounding air in Pa.

    Returns
    -------
    n : float
        Refractive index of material at wavelength.

    References
    ----------
    https://refractiveindex.info/?shelf=main&book=TiO2&page=Sarkar
    Fit using findcurves.com
    """

    # Absolute index:
    A = 1.9226445269428725e00
    B = 2.0802606609567842e-02
    C = 1.2005327946672779e-01
    D = -3.0426606351792251e-01
    n = (
        A
        + B / wavelength**2
        + C * wavelength**2 / (wavelength**2 - D**2)
    )

    # In air:
    n = n / air(wavelength, temperature, pressure)
    return n
