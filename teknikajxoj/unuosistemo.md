<!-- -*- coding: utf-8 -*- -->

Sistemo de Unuoj  
System of Units
===============================================================================

Background stories and technical specifications
for my upcoming fictional Cities: Skylines 2 city *OmniCentro*.

Malgarantio  
Disclaimer
-------------------------------------------------------------------------------

This is ***a work of fiction***.
Names, characters, businesses, places, events and incidents
are either the products of the author's imagination
or used in a fictitious manner.
Any resemblance to actual persons, living or dead, or actual events
is purely coincidental.

This work © 2024 by HomeOnMars is licensed under CC BY-NC-SA 4.0.
To view a copy of this license, visit <https://creativecommons.org/licenses/by-nc-sa/4.0/>

-------------------------------------------------------------------------------









Informoj  
Information
-------------------------------------------------------------------------------

Based on [Planck natural units](https://en.wikipedia.org/wiki/Natural_units#Planck_units).

Track gauge in *RdO* for trains, metros, and trams are the same:
$$d_\mathrm{gauge} \equiv \pi e ~ 2^{113} ~ l_P = 1.4333 \mathrm{m},$$
which is compatible with the standard gauge ($1.4351 \mathrm{m}$)
with a difference of only $2 \mathrm{mm}$.
(Hopefully that's small enough...)

-------------------------------------------------------------------------------

Note:
$l_P \equiv \sqrt{\frac{\hbar G}{c^3}}$
is the [Planck length](https://simple.wikipedia.org/wiki/Planck_length#):
$c$
is the speed of light,
$\hbar$ is the reduced Planck constant, and
$G$
is the gravitational constant.

-------------------------------------------------------------------------------




### Code illustrations

-------------------------------------------------------------------------------


```python
    # natural units
    # https://en.wikipedia.org/wiki/Natural_units#Planck_units

    from astropy import units
    from astropy import constants as const
    from numpy import pi
    import numpy as np


    # u_nat: Planck natural units
    u_nat : dict[str, units.UnitBase|units.Quantity] = {}
    u_nat['dist'] = ((const.hbar * const.G / const.c**3)**0.5).si
    u_nat['mass'] = ((const.hbar * const.c / const.G   )**0.5).si
    u_nat['time'] = ((const.hbar * const.G / const.c**5)**0.5).si
    u_nat['temp'] = ((const.hbar * const.c**5 / const.G)**0.5 / const.k_B).si

    # u_rdo: RdO standard units
    # exponent
    u_rdo_exp : dict[str, int] = {k: np.ceil(-np.log2(v.si.value)) for k, v in u_nat.items()} # default
    u_rdo_exp['dist'] = 116   # = 2**2 * 29
    u_rdo_exp['mass'] = 26    # = 2    * 13
    u_rdo_exp['time'] = 144   # = 2**4 * 3**2
    u_rdo_exp['temp'] =-106   # = 2    * 53
    # coefficient  - note: 32768 == 2**15
    u_rdo_eff : dict[str, float] = {k: 1.0 for k, v in u_nat.items()} # default
    u_rdo_eff['dist'] = 24404/32768  # 12/16  #  96/128  #
    u_rdo_eff['mass'] = 22435/32768  # 11/16  #  88/128  #
    u_rdo_eff['time'] = 27255/32768  # 13/16  # 106/128  #
    u_rdo_eff['temp'] = 18764/32768  #  9/16  #  73/128  #

    u_rdo = {k: u_nat[k] * u_rdo_eff[k] * 2**u_rdo_exp[k] for k in u_nat.keys()}

    # track gauges
    track_standard_gauge = (4*units.imperial.foot + 8.5 * units.imperial.inch).si
    track_rdo_gauge = np.pi * np.e * 2**113 * u_nat['dist'] # i.e., np.pi*np.e/6 * u_rdo['dist']
    temp_refs_C = [0., 22.85, 36.85, 100.] * units.deg_C
    temp_refs_K = temp_refs_C.to(units.K, equivalencies=units.equivalencies.temperature())

    # output
    print("\n".join([
        f"{k:4} unit: {u_rdo[k]:8.6f} \t ==  {u_rdo_eff[k]:17.15f} * 2**{u_rdo_exp[k]: 4d} * [naturalUnit: {v:.4e}]"
        for k, v in u_nat.items()]))
    print()
    print(f"dist: {track_standard_gauge = } is {track_standard_gauge.to(u_rdo['dist']):6.4f}")
    print(f"dist: proposed new gauge: {track_rdo_gauge:6.4f} \t i.e.  (1024/6101*pi*e) u_dist ({track_rdo_gauge==((1024/6101)*np.pi*np.e*u_rdo['dist'])});",
          f"\t Deviation from std gauge: {(track_rdo_gauge-track_standard_gauge).to(units.mm):4.1f}")
    print(f"temp: {temp_refs_C} is {temp_refs_K}, which is {temp_refs_K.to(u_rdo['temp'])} ")
```

Results

```python
    dist unit: 1.000001 m 	 ==  0.744750976562500 * 2** 116 * [naturalUnit: 1.6163e-35 m]
    mass unit: 1.000004 kg 	 ==  0.684661865234375 * 2**  26 * [naturalUnit: 2.1764e-08 kg]
    time unit: 1.000011 s 	 ==  0.831756591796875 * 2** 144 * [naturalUnit: 5.3912e-44 s]
    temp unit: 0.999999 K 	 ==  0.572631835937500 * 2**-106 * [naturalUnit: 1.4168e+32 K]
    
    dist: track_standard_gauge = <Quantity 1.4351 m> is 1.4351 1 m
    dist: proposed new gauge: 1.4333 m 	 i.e.  (1024/6101*pi*e) u_dist (True); 	 Deviation from std gauge: -1.8 mm
    temp: [  0.    22.85  36.85 100.  ] deg_C is [273.15 296.   310.   373.15] K, which is [273.15022499 296.00024381 310.00025534 373.15030735] 0.999999 K
```
