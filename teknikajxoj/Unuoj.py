#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
RdO Standard Units Calculations and Hexadecimal Utilities

Code author: HomeOnMars



-------------------------------------------------------------------------------

3-Clause BSD License

Copyright 2025 HomeOnMars

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

-------------------------------------------------------------------------------
"""

import numpy as np
from numpy import pi, e
from astropy import units
from astropy import constants as const



# === Hexadecimal ===



HX_SYMBOLS_ASCII = {
    k: int(k, base=16) for k in '0123456789ABCDEFabcdef'
}
HX_SYMBOLS_ONKIO = {
    k: i for i, k in enumerate('0123456789ΔλΠΣΥΨ')
}
HX_SYMBOLS_ONKIO_inv = {v: k for k, v in HX_SYMBOLS_ONKIO.items()}
HX_SYMBOLS = HX_SYMBOLS_ASCII | HX_SYMBOLS_ONKIO
# translate Epopo characters to ASCII characters using x notation
ASCIIIFY_CHR = {
    'Ĉ': 'Cx','ĉ': 'cx',
    'Ĝ': 'Gx','ĝ': 'gx',
    'Ĵ': 'Jx','ĵ': 'jx',
    'Ŝ': 'Sx','ŝ': 'sx',
    'Ŭ': 'Ux','ŭ': 'ux',
    '⚻': 'tago',
    '⚝': 'Sx',
    '☾': 'Monato',
    '⚡': 'potenco',
}
ASCIIIFY = {ord(k): v for k, v in ASCIIIFY_CHR.items()}



def Hx(n: str, base:int=0x10, symbols:dict=HX_SYMBOLS, d_sep='.', k_seps=" ,", e_sep='p') -> float:
    """Convert Hexadecimal str to float.

    d_sep: decimal separator
    k_seps: thousands separators (characters to be ignored)
    e_sep: exponent separator
    """
    if not isinstance(n, str):
        raise TypeError("Input 'n' should be a str.")
    n = n.translate({ord(k): None for k in k_seps})
    n = n.lstrip()

    # sign (+/-)
    sign = 1.
    if n and n[0] in {'+'}:
        # remove plus sign
        n = n[1:]
    elif n and n[0] in {'-', chr(0x2212)}:
        sign = -1.
        n = n[1:]
    
    # exponent parts
    ns = n.split(e_sep)
    if len(ns) > 2:
        raise ValueError("Multiple exponent separator detected")
    if len(ns) > 1:
        unit = float(base)**Hx(ns[1], base=base, symbols=symbols, d_sep=d_sep, k_seps=k_seps, e_sep=e_sep)
        n = ns[0]
    else:
        unit = 1.
        n = ns[0]
        
    # decimal parts
    ns = n.split(d_sep)
    if len(ns) > 2:
        raise ValueError("Multiple decimal separator detected")
    ans = 0.
    for i, v in enumerate(ns[0]):
        p = len(ns[0]) - i - 1
        ans += symbols[v] * base**p
    if len(ns) > 1:
        for i, v in enumerate(ns[1]):
            p = -i - 1
            ans += symbols[v] * base**p
            
    ans *= sign * unit
    return ans



def presi_Hx(
    n: float,
    sc: int = 0x80,
    stop_when_precise: bool = True,
    base: int = 0x10,
    symbols_inv: dict = HX_SYMBOLS_ONKIO_inv,
    d_sep: str = '.',
    e_sep: str = 'p'
) -> str:
    """Convert Hexadecimal float to str.

    To output without p-notation, set e_sep=''

    Warning: last digit may be an underestimate
    Warning: NOT suitable for long large integers when e_sep=''

    with p-notation (e_sep='p'), max supported numbers are about ~'F.FFFF FFFF FF pFF'
        min ~'1p-10C'
    
    sc: signifaj ciferoj, or significant digits
    d_sep: decimal separator
    e_sep: exponent separator
    """
    if sc < 1: raise ValueError("Significant digits 'sc' must >= 1.")

    n = np.float64(n)
    sign = n >= 0
    n = abs(n)
    if n == 0:
        return f"0{e_sep}+0" if e_sep else "0"
    base = np.float64(base)
    log2_base = np.log2(base)
    # grandordo = order of magnitude
    grandordo = np.int64(np.floor(np.log2(n) / log2_base))

    if len(grandordo.shape):
        # input is an array
        raise NotImplementedError("Array input not yet implemented.")

    ans = "" if sign else "-"

    for i in range(sc if e_sep else max(grandordo+1, sc)):
        
        unit = base**(grandordo-i)
        v = int(np.floor(n / unit))
        n -= v * unit
        ans += symbols_inv[v]
        if stop_when_precise and not n and (e_sep or i >= grandordo):
            break
        if (e_sep and i == 0) or (not e_sep and i == grandordo):
            ans += d_sep
        
    if e_sep:
        ans += f"{e_sep}{presi_Hx(
            grandordo, sc=0x100, stop_when_precise=True,
            base=base, symbols_inv=symbols_inv, d_sep=d_sep, e_sep='')}"
    
    return ans



# === Unit System ===



# si units
u_si_defs : dict[str, units.UnitBase] = {
    v: getattr(units, v)
    for v in [
        'm', 'cm', 'km', 'Rearth', 'au', 'lyr', 'pc',
        'kg', 'g', 
        's', 'd', 'yr',
        'K',
    ]
}
units.def_unit('kph', units.km / units.h, namespace=u_si_defs)
units.def_unit('mph', units.imperial.mi / units.h, namespace=u_si_defs)

# natural units
# https://en.wikipedia.org/wiki/Natural_units#Planck_units

# u_nat_dict: Planck natural units
u_nat_base : dict[str, units.UnitBase] = {}
u_nat_defs : dict[str, units.UnitBase] = {}
u_nat_base['dist'] = units.def_unit(
    'l_P', (const.hbar * const.G / const.c**3)**0.5,
    namespace=u_nat_defs, format={'latex': r' l_P '})
u_nat_base['mass'] =  units.def_unit(
    'm_P', (const.hbar * const.c / const.G   )**0.5,
    namespace=u_nat_defs, format={'latex': r' m_P '})
u_nat_base['time'] =  units.def_unit(
    't_P', (const.hbar * const.G / const.c**5)**0.5,
    namespace=u_nat_defs, format={'latex': r' t_P '})
u_nat_base['temp'] =  units.def_unit(
    'T_P', (const.hbar * const.c**5 / const.G)**0.5 / const.k_B,
    namespace=u_nat_defs, format={'latex': r' T_P '})

# u_rdo: RdO standard units
u_rdo_prefixes = [
    ('h', ['hek'],   0x10),
    ('j', ['jent'],  0x100),
    ('g', ['gil'],   0x1000),
    ('M', ['Munio'], 0x10000),
]
u_rdo_base : dict[str, units.UnitBase] = u_nat_base.copy()
u_rdo_defs : dict[str, units.UnitBase] = {}
#    defs
u_rdo_base['dist'] = units.def_unit(
    # note: 1149807 / 3.0 = 383269
    ['U', 'Utro'], 383269 * 2**100 * u_nat_base['dist'],
    prefixes=u_rdo_prefixes, namespace=u_rdo_defs)
u_rdo_base['mass'] = units.def_unit(
    ['p', 'pakmo'], 2**24 * u_nat_base['mass'],
    prefixes=u_rdo_prefixes, namespace=u_rdo_defs)
u_rdo_base['time'] = units.def_unit(
    ['ŝ', 'ŝekunto'], 1149807 * 2**124 * u_nat_base['time'],    #71863 * 2**128
    prefixes=u_rdo_prefixes, namespace=u_rdo_defs)
u_rdo_base['temp'] = units.def_unit(
    ['Z', 'Zoro'], 10011 * 2**(-120) * u_nat_base['temp'],
    prefixes=u_rdo_prefixes, namespace=u_rdo_defs)
#    extra defs: prefixes
for prefix_sn, prefix_tab, scale in u_rdo_prefixes:
    if prefix_sn not in {'h', 'g'}:    # avoid name collisions with SI units
        units.def_unit(
            [prefix_sn, *prefix_tab],
            scale*units.dimensionless_unscaled,
            namespace=u_rdo_defs)



# derive more units
def normalize(u: dict[str, units.UnitBase]) -> dict[str, units.UnitBase]:
    # derived units
    u['speed']  = u['dist'] / u['time']
    u['accel']  = u['dist'] / u['time']**2
    u['energy'] = u['mass'] * u['dist']**2 / u['time']**2
    u['power']  = u['energy'] / u['time']
    # constants
    u['hbar'] = u['dist']**2 * u['mass'] / u['time']
    u['c'] = u['dist'] / u['time']
    u['G'] = u['dist']**3 / (u['mass'] * u['time']**2)
    u['k_B'] = u['dist']**2 * u['mass'] / (u['time']**2 * u['temp'])
    return u

normalize(u_nat_base)
normalize(u_rdo_base)



# rdo unit extra defs
#    time
units.def_unit(
    ['ĉ', 'ĉimuto'],   0x40 * u_rdo_base['time'], namespace=u_rdo_defs)
units.def_unit(
    ['ĝ', 'ĝoro'],   0x1000 * u_rdo_base['time'], namespace=u_rdo_defs)
units.def_unit(
    ['⚻', 'tago'], u_rdo_defs['Mŝ'], namespace=u_rdo_defs)
units.def_unit(
    ['⚝', 'Semajno'], 7 * u_rdo_defs['tago'], namespace=u_rdo_defs)
units.def_unit(
    ['☾', 'Monato'],  4 * u_rdo_defs['Semajno'], namespace=u_rdo_defs)
units.def_unit(
    ['Ĵ', 'Ĵaro'], 365.25 * u_rdo_defs['Mŝ'],
    prefixes=u_rdo_prefixes, namespace=u_rdo_defs)
#    speed
units.def_unit('Uoŝ', u_rdo_defs[ 'U']/u_rdo_defs['ŝ'], namespace=u_rdo_defs)
units.def_unit('joĝ', u_rdo_defs['jU']/u_rdo_defs['ĝ'], namespace=u_rdo_defs)
#    power
units.def_unit(
    ['⚡', 'M?'], 0x10000 *u_rdo_base['power'], namespace=u_rdo_defs)



# Extra
class Unuoj:
    """Units System."""
    def __init__(
        self,
        units_base: dict[str, units.UnitBase] = {},
        units_defs: dict[str, units.UnitBase] = {},
    ):
        self._base: dict[str, units.UnitBase] = normalize(units_base)
        self._defs: dict[str, units.UnitBase] = units_defs
        for k, v in units_defs.items():
            setattr(self, k.translate(ASCIIIFY), v)

    def enable(self):
        return units.add_enabled_units(self._defs)

unitsRdO = Unuoj(u_rdo_base, u_rdo_defs)
unitsNat = Unuoj(u_nat_base, u_nat_defs)    # testing
u_rdo = unitsRdO
u_nat = unitsNat
u = Unuoj(u_rdo_base, u_rdo_defs | u_nat_defs | u_si_defs)

# track gauges
track_standard_gauge = (4*units.imperial.foot + 8.5 * units.imperial.inch).si
track_rdo_gauge = np.e/16 * u_nat_base['dist'] # i.e., np.pi*np.e/6 * u_rdo['dist']



if __name__ == '__main__':
    # temperature reference points
    temp_refs_C = [0., 22.85, 36.85, 100.] * units.deg_C
    temp_refs_K = temp_refs_C.to(units.K, equivalencies=units.equivalencies.temperature())

    # output
    print("\n".join([
        f"{k:4} unit: {(1*u_rdo_base[k]).si:8.6f} \t [naturalUnit: {(1*v).si:.4e}]"
        for k, v in u_nat_base.items()]))
    print()
    print(f"dist: {track_standard_gauge = } is {track_standard_gauge.to(u_rdo_base['dist']):6.4f}")
    print(f"temp: {temp_refs_C} is {temp_refs_K}, which is {temp_refs_K.to(u_rdo_base['temp'])} ")

    # sidereal year <https://en.wikipedia.org/wiki/Sidereal_year> (2025-02-28)
    #u_yr = units.d * 365.256363004
    u_yr = units.yr
    u_yr_b = (u_rdo.Msx / (1*u_yr - 1*u_rdo.Jx)).si * units.yr
    print(f"\n# of years before needing to subtract a day: {u_yr_b:.1f}")
    print(f"Added seconds per day: {(1*u_rdo.Msx - 1*units.day).to(units.s):.3f}")
    print(f"Added minutes per year: {(1*u_rdo.Jx - 1*units.year).to(units.min):.3f}")

    print("\nTesting name collision with SI units... ", end='')
    # units.add_enabled_units(u_rdo_defs)
    u_nat.enable()
    u_rdo.enable()
    print("Done.")
