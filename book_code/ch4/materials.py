def air(λ, T=20, P=101325):
    """Calculates refractive index of air.

    Parameters
    ----------
    λ : float
        Vacuum wavelength in µm.
    T : float
        Temperature in °C.
    P : float
        Presure in Pa.

    Returns
    -------
    n : float
        Refractive index of material at λ, T, and P.

    References
    ----------
    K. Schwertz and J. H. Burge, Field Guide to Optomechanical Design and Analysis, p. 102.
    W. J. Smith, Modern Optical Engineering, 4th Ed, p. 4.
    """
    ns = (
        8342.54
        + 2406147 / (130 - 1 / λ**2)
        + 15998 / (38.9 - 1 / λ**2)
    ) * 1e-8

    n = 1 + P * ns / 96095.43 * (
        1 + 1e-8 * (0.601 - 9.72e-3 * T) * P
    ) / (1 + 3.661e-3 * T)
    return n


def nbk7(λ, T=20, P=101325):
    """Calculates refractive index of Schott N-BK7 in air.

    Parameters
    ----------
    λ : float
        Wavelength in µm.
        Valid for 365 nm to 1.06 μm
    T : float
        Temperature of glass in °C.
    P : float
        Pressure of surrounding air in Pa.

    Returns
    -------
    n : float
        Refractive index of material at λ.

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
        + B1 * λ**2 / (λ**2 - C1)
        + B2 * λ**2 / (λ**2 - C2)
        + B3 * λ**2 / (λ**2 - C3)
    ) ** 0.5

    # Temperature dependence:
    D0 = 1.86e-6
    D1 = 1.31e-8
    D2 = -1.37e-11
    E0 = 4.34e-7
    E1 = 6.27e-10
    λtk = 0.17  # in μm
    ΔT = T - 20
    Δn = (
        (n**2 - 1)
        / (2 * n)
        * (
            D0 * ΔT
            + D1 * ΔT**2
            + D2 * ΔT**3
            + (E0 * ΔT + E1 * ΔT**2) / (λ**2 - λtk**2)
        )
    )
    n = n + Δn

    # In air:
    n = n / air(λ, T, P)
    return n


def sio2(λ, T=25, P=101325):
    """Calculates refractive index of thin film silicon dioxide in air.
    Fit from 350nm to 1000nm

    Parameters
    ----------
    λ : float
        Wavelength in µm.
    T : float
        Temperature of glass in °C.
    P : float
        Pressure of surrounding air in Pa.

    Returns
    -------
    n : float
        Refractive index of material at λ.

    References
    ----------
    https://refractiveindex.info/?shelf=main&book=SiO2&page=Rodriguez-de_Marcos
    Fit using findcurves.com
    """

    # Absolute index:
    A = 1.4561565279730799e00
    B = 1.4530718441661201e-06
    C = 2.9253913539533088e-03
    D = 2.6864676705345106e-05
    E = 4.0554151579192171e-07
    n = A + B * λ**2 + C / λ**2 + D / λ**4 + E / λ**6

    # In air:
    n = n / air(λ, T, P)
    return n


def tio2(λ, T=25, P=101325):
    """Calculates refractive index of thin film titanium dioxide in air.
    Fit from 350nm to 1000nm

    Parameters
    ----------
    λ : float
        Wavelength in µm.
    T : float
        Temperature of glass in °C.
    P : float
        Pressure of surrounding air in Pa.

    Returns
    -------
    n : float
        Refractive index of material at λ.

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
    n = A + B / λ**2 + C * λ**2 / (λ**2 - D**2)

    # In air:
    n = n / air(λ, T, P)
    return n


def mgf2(λ, T=25, P=101325):
    """Calculates refractive index of Magnesium Fluoride in air.

    Parameters
    ----------
    λ : float
        Wavelength in µm.
    T : float
        Temperature of glass in °C.
    P : float
        Pressure of surrounding air in Pa.

    Returns
    -------
    n : float
        Refractive index of material at λ.

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
    n = A + B / (C - λ) + D / (E - λ)

    # In air:
    n = n / air(λ, T, P)
    return n
