import math
import copy

import numpy as np

# This is to handle abcd being imported within directory (e.g. by ch2.py)
# and as part of a module (e.g. by test suite)
if not __package__:
    import equations
else:
    from . import equations


class Ray:
    def __init__(self, y=0, u=0, n=1, wavelength=532e-9):
        self.y = y
        self.u = u
        self.n = n
        self.wavelength = wavelength

    def __repr__(self):
        return f"[[{self.y}]\n [{self.n * self.u}]]"

    def __eq__(self, other):
        return (
            np.all(self.y == other.y)
            and np.all(self.u == other.u)
            and np.all(self.n == other.n)
            and np.all(self.wavelength == other.wavelength)
        )

    # to enable (self @= other) syntax
    def __imatmul__(self, other):
        # other assumed to be ABCD
        return other @ self

class GaussianBeam(Ray):
    def __init__(
        self,
        *,
        wavelength=532e-9,
        n=1,
        sign=1,
        q=None,
        R=None,
        w=None,
        z=None,
        zR=None,
    ):
        """Creates a GaussianBeam class. Pick any two beam 
        parameters and provide them as keyword arguments. 
        Arguments are always physical values (e.g. z is 
        distance as measured, not air-equivalent thickness 
        and q is z + 1j * zR, not reduced q).

        The reduced q value is what can be used for ABCD 
        calculations. While this is used internally, the 
        properties of GaussianBeam always return physical 
        values (including the non-reduced q)."""

        # As a convenience:
        if R == 0:
            R = math.inf

        if w == 0 or zR == 0:
            raise ValueError("Invalid argument w or zR")

        # Conditionals structured to allow values to be zero
        if q is not None:
            qr = q / n
        elif R is not None and w is not None:
            qr = equations.q_from_R_w(R, w, wavelength, n)
        elif z is not None and zR is not None:
            qr = equations.q_from_z_zR(z, zR, n)
        elif R is not None and z is not None:
            qr = equations.q_from_R_z(R, z, n)
        elif R is not None and zR is not None:
            qr = equations.q_from_R_zR(R, zR, n, sign)
        elif w is not None and z is not None:
            qr = equations.q_from_w_z(w, z, wavelength, n, sign)
        elif w is not None and zR is not None:
            qr = equations.q_from_w_zR(w, zR, wavelength, n, sign)
        else:
            raise ValueError("No valid configuration for beam found")
        super().__init__(1, 1 / (n * qr), n, wavelength)

    def __repr__(self):
        return (
            f"R & w: {self.R * 1e3:g} mm & {self.w * 1e3:g} mm\n"
            f"z & zR: {self.z * 1e3:g} mm & {self.zR * 1e3:g} mm\n"
            f"w0 & θ: {self.w0 * 1e3:g} mm & {self.divergence * 1e3:g} mrad\n"
            f"q: {self.q * 1e3:g} mm"
        )

    @property
    def q(self):
        return self.y / self.u

    @property
    def R(self):
        try:
            real = (1 / self.q).real
            return 1 / real
        except ZeroDivisionError:
            return math.inf

    @property
    def w(self):
        imag = (self.n / self.q).imag
        return (-math.pi / self.wavelength * imag) ** (-0.5)

    @property
    def z(self):
        return self.q.real

    @property
    def zR(self):
        return self.q.imag

    @property
    def w0(self):
        return (self.wavelength * self.zR / (self.n * math.pi)) ** 0.5

    @property
    def divergence(self):
        return self.w0 / self.zR


class ABCD:
    def __init__(
        self, A=1, B=0, C=0, D=1, n1=1, n2=1, decenter=0, tilt=0, length=0, E=None, F=None
    ):
        self.n1 = n1
        self.n2 = n2
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.E = (1 - A) * decenter + (length - n1 * B) * tilt if E is None else E
        self.F = -C * decenter + (n2 - n1 * D) * tilt if F is None else F

    def __repr__(self):
        return (
            f"[[{self.A:g} {self.B:g} {self.E:g}]\n"
            f" [{self.C:g} {self.D:g} {self.F:g}]\n"
            f" [0 0 1]]"
        )

    def __eq__(self, other):
        return (
            (self.A == other.A)
            and (self.B == other.B)
            and (self.C == other.C)
            and (self.D == other.D)
            and (self.E == other.E)
            and (self.F == other.F)
        )

    # to enable (self @ other) syntax
    def __matmul__(self, other):
        # self @ other
        if isinstance(other, ABCD):
            A = self.A * other.A + self.B * other.C
            B = self.A * other.B + self.B * other.D
            C = self.C * other.A + self.D * other.C
            D = self.C * other.B + self.D * other.D
            E = self.A * other.E + self.B * other.F + self.E
            F = self.C * other.E + self.D * other.F + self.F
            return ABCD(A=A, B=B, C=C, D=D, n1=other.n1, n2=self.n2, E=E, F=F)
        # self @ Ray
        elif isinstance(other, Ray):
            y = self.A * other.y + self.B * other.n * other.u + self.E
            u = (
                self.C * other.y + self.D * other.n * other.u + self.F
            ) / self.n2

            ret = copy.deepcopy(other)  # so "other" unchanged
            ret.y = y
            ret.u = u
            ret.n = copy.deepcopy(self.n2)
            return ret

    # to enable (self @= other) syntax
    def __imatmul__(self, other):
        return other @ self

    def add_misalignments(self, decenter, tilt, length):
        self.E = (1 - self.A) * decenter + (length - self.n1 * self.B) * tilt 
        self.F = -self.C * decenter + (self.n2 - self.n1 * self.D) * tilt

    @property
    def F1(self):
        try:
            return self.n1 * self.D / self.C
        except ZeroDivisionError:
            return -math.inf

    @property
    def P1(self):
        try:
            return self.n1 * (self.D - 1) / self.C
        except ZeroDivisionError:
            return -math.inf

    @property
    def N1(self):
        try:
            return (self.D * self.n1 - self.n2) / self.C
        except ZeroDivisionError:
            return -math.inf

    @property
    def f1(self):
        try:
            return -self.n1 / self.C
        except ZeroDivisionError:
            return math.inf

    @property
    def F2(self):
        try:
            return -self.n2 * self.A / self.C
        except ZeroDivisionError:
            return math.inf

    @property
    def P2(self):
        try:
            return self.n2 * (1 - self.A) / self.C
        except ZeroDivisionError:
            return math.inf

    @property
    def N2(self):
        try:
            return (self.n1 - self.A * self.n2) / self.C
        except ZeroDivisionError:
            return math.inf

    @property
    def f2(self):
        try:
            return -self.n2 / self.C
        except ZeroDivisionError:
            return math.inf


class Transfer(ABCD):
    def __init__(self, t, n=1, **kwargs):
        super().__init__(1, t / n, 0, 1, **kwargs)


class Refraction(ABCD):
    """ABCD matrix for refraction at dielectric interface.
    AOI is angle-of-incidence of axial ray in radians
    (e.g. coming in to lens at a non-normal angle) 
    and T_or_S specifies tangential or saggital. R is
    positive for a convex surface, typical of geometrical
    optics but counter to Siegman."""

    def __init__(self, R, n1, n2, AOI=0, T_or_S="T", **kwargs):
        AOE = math.asin(n1 * math.sin(AOI) / n2)
        C1 = math.cos(AOI)
        C2 = math.cos(AOE)

        if T_or_S.lower() == "t":
            denominator = C1 * C2
            A = C2 / C1
            D = C1 / C2
        elif T_or_S.lower() == "s":
            denominator = 1
            dne = n2 * C2 - n1 * C1
            A = D = 1
        else:
            raise ValueError(f"Unknown T_or_S: {T_or_S}")
        numerator = n2 * C2 - n1 * C1
        dne = numerator / denominator
        B = 0
        C = -dne / R
        super().__init__(A, B, C, D, n1, n2, **kwargs)


class Mirror(ABCD):
    """ABCD matrix for reflection at mirror.
    AOI is angle-of-incidence of axial ray in radians
    (e.g. coming in to mirror at a non-normal angle) 
    and T_or_S specifies tangential or saggital. R is
    positive for a convex surface, typical of geometrical
    optics but counter to Siegman."""

    def __init__(self, R, AOI=0, T_or_S="T", **kwargs):
        if T_or_S.lower() == "t":
            Re = R * math.cos(AOI)
        elif T_or_S.lower() == "s":
            Re = R / math.cos(AOI)
        else:
            raise ValueError(f"Unknown T_or_S: {T_or_S}")
        super().__init__(1, 0, 2 / Re, 1, **kwargs)


class Duct(ABCD):
    """ABCD matrix for media with radially varying index as
    n(y) = n0 - n2 * y**2 / 2. For example, a GRIN fiber or
    index variation caused by thermal lensing."""

    def __init__(self, t, n0, n2, **kwargs):
        g = (n2 / n0) ** 0.5
        A = math.cos(g * t)
        B = math.sin(g * t) / (n0 * g)
        C = -n0 * g * math.sin(g * t)
        D = math.cos(g * t)
        super().__init__(A, B, C, D, **kwargs)


class Grating(ABCD):
    """ABCD matrix for diffraction grating per Siegman. 
    Grating lines run in the x / saggital direction with 
    grating spacing d in the y / tangential direction. 
    Diffraction takes place in the YZ plane.
    Calling diffraction order m. Assumed to be reflective
    with positive R convex. sign == 1 is for the convention
    sin(θ1) - sin(θ2) whereas sign == -1 specifies
    sin(θ1) + sin(θ2)"""

    def __init__(
        self,
        R,
        m=-1,
        d=1e-6,
        wavelength=532e-9,
        AOI=0,
        T_or_S="T",
        sign=1,
        **kwargs,
    ):
        sign = 1 if sign >= 0 else -1
        AOE = math.asin(m * wavelength / d + sign * math.sin(AOI))
        C1 = math.cos(AOI)
        C2 = math.cos(AOE)

        if T_or_S.lower() == "t":
            # "Lasers" is missing the 2x here:
            Rt = 2 * R * C1 * C2 / (C1 + C2)
            M = C2 / C1
            A = M
            B = 0
            C = 2 / Rt
            D = 1 / M
        elif T_or_S.lower() == "s":
            Rs = 2 * R / (C1 + C2)
            A = D = 1
            B = 0
            C = 2 / Rs
        else:
            raise ValueError(f"Unknown T_or_S: {T_or_S}")
        super().__init__(A, B, C, D, **kwargs)


class ThinLens(ABCD):
    def __init__(self, f, **kwargs):
        super().__init__(1, 0, -1 / f, 1, **kwargs)


class ThickLens(ABCD):
    def __init__(self, R1, R2, t, n_glass, n_ambient=1, **kwargs):
        r1 = Refraction(R1, n_ambient, n_glass)
        t = Transfer(t, n_glass)
        r2 = Refraction(R2, n_glass, n_ambient)
        net = r2 @ t @ r1
        super().__init__(
            net.A, net.B, net.C, net.D, net.n1, net.n2, **kwargs
        )

