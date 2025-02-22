<!-- -*- coding: utf-8 -*- -->

Sistemo de Unuoj
===============================================================================

> System of Units

Technical specifications for my fictional Cities: Skylines 2 city *OmniCentro*.

Legal
-------------------------------------------------------------------------------

> [!WARNING]
> Standards here may also be updated without notices.  

<p xmlns:cc="http://creativecommons.org/ns#" >This work by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/HomeOnMars">HomeOnMars</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></a></p>

Informoj
-------------------------------------------------------------------------------

> Information (regarding the unit system)
> <br>
> [Back to OmniCentro Content](../OmniCentro.md#teknikaj-specifoj)

-------------------------------------------------------------------------------

The unit system of Omnijo is based on **Planck natural units**-
See [Wikipedia](https://en.wikipedia.org/wiki/Natural_units#Planck_units).

> [!TIP]
> $l_P \equiv \sqrt{\frac{\hbar G}{c^3}}$
> is the [Planck length](https://simple.wikipedia.org/wiki/Planck_length#);  
> Planck mass $m_P \equiv \sqrt{\frac{\hbar c}{G}}$;  
> Planck time $t_P \equiv \sqrt{\frac{\hbar G}{c^5}}$;  
> $c$ is the speed of light;  
> $\hbar$ is the reduced Planck constant;  
> $G$ is the gravitational constant;  
> $e$ is the natural constant.

See also [Lingvo](../OmniCentro/Lingvo.md#algebro) page for prefix acronyms
$h~j~g~m~n_2$ for Hx10, Hx100, Hx1000, Hx 1 0000, Hx 1000 0000, etc,
and for Hexadecimal pre/surfix *H* vs Decimal pre/surfix *D*.

### Longeco

> Length

> [!IMPORTANT]
> Default length unit: ***Utro*** `u` (Omnija meters)
> $$u \equiv \pi 2^{117_D}~l_P \approx 8.437_D~m$$

1u is 1 cell width in-game.

$$ju \equiv 256_D~u \approx 2.160~km$$

#### Trakmezurilo

> Track gauge

Track gauge in *RdO* for trains, metros, and trams are the same:
$$d_\mathrm{gauge}
    \equiv \frac{e}{16}~u
    = \pi e~2^{113_D}~l_P
    \approx 1.4333_D~m$$
which is compatible with the standard gauge ($1.4351~m$)
with a difference of only $2~mm$.
(Hopefully that's small enough...)

### Maso

> Mass

> [!IMPORTANT]
> Default mass unit: ***?*** `?` (Omnija kilogram- Name TBD)
> $$??
    \equiv 2^{24_D}~m_P
    \approx 0.365_D~kg$$

A munio of said unit mass is a Omnija ton:
$$m? \equiv 2^{16_D}~? \approx 23.930_D~t$$
which happens to be about 1 FEU container equivalent of goods.

### Tempo

> Time

> [!IMPORTANT]
> Default time unit: ***Ŝekuntoj*** `ŝ` (Omnija seconds)
> $$1~ŝ \equiv 71863_D~2^{128_D}~t_P \approx 1.318_D~s$$
<!-- 1~ŝ = 1.518_H~s -->

The Ŝekuntoj is calilbrated such that each Earth day is about $16_D^4~ŝ$.

- `J`: ***Jaroj***    | years
- `M`: ***Monatoj***  | Months
- `S`: ***Semajnoj*** | Weeks
- `T`: ***Tagoj***    | Days
  - Here we assume one year is 13 months exactly,
    and each months has 4 weeks exactly
    (except leap year which happens every 4 years,
    and has 5 extra days (all considered holidays)):
    $$1J = 13_D M = 52_D S = 364_D T$$
    ($D$ for decimal, $H$ for Hexadecimal)
  - Winter Solstice[^Tagoj-Solstico] always happens
    in the first week of the year for the Y+\* calendars.
    The leap year (Y+\* years ends with $3_H, 7_H, λ_H, Ψ_H$) adds extra days at the end of the year,
    and the year immediately after the leap year have the solstice
    happening at the (evening of the) first day of the year.
    The first week of the year
    (together with the days added by leap years if any)
    are holidays.
  - Solstices and Equinoxes are national holidays.
<!-- - h: ***Horoj***    | Hours
- m: ***Minutoj***  | Minutes
- s: ***Sekundoj*** | Seconds -->
- `ĝ`: ***Ĝoroj***    | Omnija Hours
  - 1 Ĝoro is    $24_D/16_D = 1.5_D$ SI Hours.
- `ĉ`: ***Ĉimutoj***  | Omnija Minutes
  - 1 Ĉimuto is  $1440_D/1024_D = 1.40625_D$ SI Minutes.
- `ŝ`: ***Ŝekuntoj*** | Omnija Seconds
  - Conversion rate:
    $$1T = 16_D ĝ = 1024_D ĉ = 65536_D ŝ$$
    i.e.,
    $1T = 10_H ĝ = 400_H ĉ = 10000_H ŝ $;
    $1ĝ = 40_H ĉ$,
    $1ĉ = 40_H ŝ$;
  - 1 Ŝekunto is $86400_D/65536_D = 1.318359375_D$ SI Seconds.

[^Tagoj-Solstico] a.k.a. Northern Solstice, since *la Omnija-Insulo* is located in the Southern Hemisphere.

### Rapido

> Speed

Standard: utro por ŝekuntoj, or u/ŝ / upŝ for short:
$$upŝ \equiv u/ŝ \approx 6.40_D~m/s$$

ju por ĝoro (or ju/ĝ / jpĝ for short)
$$jpĝ \equiv ju/ĝ = 1/16_D~upŝ \approx 1.44~kph$$

- Speed limits examples:
    - Hx 100 jpĝ ~ Dx 369 kph  <!-- Dx 370 kph -->
    - Hx  80 jpĝ ~ Dx 184 kph  <!-- Dx 185 kph -->
    - Hx  58 jpĝ ~ Dx 126 kph    <!-- Dx 125 kph -->
    - Hx  50 jpĝ ~ Dx 115 kph  <!-- Dx 115 kph -->
    - Hx  48 jpĝ ~ Dx 104 kph    <!-- Dx 105 kph -->
    - Hx  40 jpĝ ~ Dx  92 kph  <!-- Dx  90 kph -->
    - Hx  38 jpĝ ~ Dx  81 kph    <!-- Dx  80 kph -->
    - Hx  30 jpĝ ~ Dx  69 kph  <!-- Dx  70 kph -->
    - Hx  28 jpĝ ~ Dx  58 kph    <!-- Dx  60 kph -->
    - Hx  20 gpĝ ~ Dx  45 kph  <!-- Dx  45 kph -->
    - Hx  18 jpĝ ~ Dx  35 kph    <!-- Dx  35 kph -->
    - Hx  10 gpĝ ~ Dx  23 kph  <!-- Dx  25 kph -->
    - Hx   8 gpĝ ~ Dx  12 kph    <!-- Dx  10 kph -->

### Code illustrations

```python
    # natural units
    # https://en.wikipedia.org/wiki/Natural_units#Planck_units

    from astropy import units
    from astropy import constants as const
    from numpy import pi, e
    import numpy as np

    # u_nat: Planck natural units
    u_nat : dict[str, units.UnitBase|units.Quantity] = {}
    u_nat['dist'] = ((const.hbar * const.G / const.c**3)**0.5).si
    u_nat['mass'] = ((const.hbar * const.c / const.G   )**0.5).si
    u_nat['time'] = ((const.hbar * const.G / const.c**5)**0.5).si
    u_nat['temp'] = ((const.hbar * const.c**5 / const.G)**0.5 / const.k_B).si

    # u_rdo: RdO standard units
    u_rdo = {k: u_nat[k].copy() for k in u_nat.keys()}
    u_rdo['dist'] *= pi * 2**117
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
    gx = (64*64*u_rdo['time']).to(units.h)
    ju = (u_rdo['dist']*256).to(units.km)
    jpgx = ju/gx

    # track gauges
    track_standard_gauge = (4*units.imperial.foot + 8.5 * units.imperial.inch).si
    track_rdo_gauge = np.e/16 * u_nat['dist'] # i.e., np.pi*np.e/6 * u_rdo['dist']
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
```
