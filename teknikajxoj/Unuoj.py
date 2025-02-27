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
        if stop_when_precise and not n:
            break
        if (e_sep and i == 0) or (not e_sep and i == grandordo):
            ans += d_sep
        
    if e_sep:
        ans += f"{e_sep}{presi_Hx(
            grandordo, sc=0x100, stop_when_precise=True,
            base=base, symbols_inv=symbols_inv, d_sep=d_sep, e_sep='')}"
    
    return ans



# === Unit System ===




# natural units
# https://en.wikipedia.org/wiki/Natural_units#Planck_units

# u_nat: Planck natural units
u_nat : dict[str, units.UnitBase|units.Quantity] = {}
u_nat['dist'] = ((const.hbar * const.G / const.c**3)**0.5).si
u_nat['mass'] = ((const.hbar * const.c / const.G   )**0.5).si
u_nat['time'] = ((const.hbar * const.G / const.c**5)**0.5).si
u_nat['temp'] = ((const.hbar * const.c**5 / const.G)**0.5 / const.k_B).si

# u_rdo: RdO standard units
u_rdo = {k: u_nat[k].copy() for k in u_nat.keys()}
u_rdo['dist'] *= 3 * 2**117
u_rdo['mass'] *= 2**24
u_rdo['time'] *= 71863 * 2**128
# u_rdo['temp'] = ((const.hbar * const.c**5 / const.G)**0.5 / const.k_B).si

# derive more units
def normalize(u: dict):
    u['speed']  = (u['dist'] / u['time']).to(units.m / units.s)
    u['energy'] = (u['mass'] * u['dist']**2 / u['time']**2).to(units.J)
    u['power']  = (u['energy'] / u['time']).to(units.W)
normalize(u_nat)
normalize(u_rdo)

# Extra
class Units_RdO:
    """RdO Units System."""
    def __init__(self, units_dict:dict=u_rdo.copy()):
        self.units: dict = units_dict.copy()

        # dist
        self.u = (self.units['dist']).to(units.m)
        self.hu = (0x10     * self.u).to(units.m)
        self.ju = (0x100    * self.u).to(units.km)
        self.gu = (0x1000   * self.u).to(units.km)
        self.Mu = (0x10000  * self.u).to(units.km)

        # mass
        self.p = (self.units['mass']).to(units.kg)
        self.Mp = (0x10000  * self.p).to(units.t)

        # time
        self.sx = (self.units['time']).to(units.s)
        self.cx = (0x40     * self.sx).to(units.min)
        self.gx = (0x40     * self.cx).to(units.h)
        self.T  = (0x10     * self.gx).to(units.day)
        self.S  = (0x7      * self.T).to(units.week)
        self.M  = (0x4      * self.S).to(units.week)
        self.J  = (0xD      * self.M).to(units.year)

        # speed
        self.uosx = self.u /self.sx
        self.jogx = self.ju/self.gx
        self.gogx = self.gu/self.gx    # note: gogx == uosx

units_RdO = Units_RdO()

# track gauges
track_standard_gauge = (4*units.imperial.foot + 8.5 * units.imperial.inch).si
track_rdo_gauge = np.e/16 * u_nat['dist'] # i.e., np.pi*np.e/6 * u_rdo['dist']

if __name__ == '__main__':
    # temperature reference points
    temp_refs_C = [0., 22.85, 36.85, 100.] * units.deg_C
    temp_refs_K = temp_refs_C.to(units.K, equivalencies=units.equivalencies.temperature())

    # output
    print("\n".join([
        f"{k:4} unit: {u_rdo[k]:8.6f} \t [naturalUnit: {v:.4e}]"
        for k, v in u_nat.items()]))
    print()
    print(f"dist: {track_standard_gauge = } is {track_standard_gauge.to(u_rdo['dist']):6.4f}")
    print(f"dist: proposed new gauge: {track_rdo_gauge:6.4f} \t i.e.  (1024/6101*pi*e) u_dist ({track_rdo_gauge==((1024/6101)*np.pi*np.e*u_rdo['dist'])});",
          f"\t Deviation from std gauge: {(track_rdo_gauge-track_standard_gauge).to(units.mm):4.1f}")
    print(f"temp: {temp_refs_C} is {temp_refs_K}, which is {temp_refs_K.to(u_rdo['temp'])} ")
