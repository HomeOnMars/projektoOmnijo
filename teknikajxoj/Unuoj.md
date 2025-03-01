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

See also [Lingvo](../teknikajxoj/Lingvo.md#algebro) page for prefix acronyms
$h \  j \  g \  M \  N_2 \  N_3 \  N_4$ for
Hx10, Hx100, Hx1000, Hx 1 0000, Hx 1 0000 0000 = 1p8, 1pΠ, 1p10, etc;
also for Hexadecimal pre/surfix *H* vs Decimal pre/surfix *D*.

### Longeco

> Length

> [!IMPORTANT]
> Default length unit: ***Utroj*** `U` (Omnija meters)

$$
  \textrm{U}
  \equiv 3_D \times 2^{117_D} \  l_P
  \approx 8.056_D \  \textrm{m}
$$

The Utroj is calilbrated such that 1U is approximately 8 meters.
Note: using `U` instead of `u` to avoid name clash
with SI unit of the 'unified atomic mass unit'.

1 cell width in-game is 1U.

*jentUtro* (`jU`):

$$
  \textrm{jU}
  \equiv 256_D \  \textrm{U}
  \approx 2.062_D \  \textrm{km}
$$

*gilUtro* (`gU`):

$$
  \textrm{gU}
  \equiv 16_D^3 \  \textrm{U}
  \approx 33.000_D \  \textrm{km}
$$

*MunioUtro*  (`MU`):

$$
  \textrm{MU}
  \equiv 16_D^4 \  \textrm{U}
  \approx 527.98_D \  \textrm{km}
$$

Consequentially, One Earth radius is approximately

$$
  R_{\oplus}
  \approx Π.148_H \  \textrm{MU}
  \approx 6378_D \  \textrm{km}
$$

#### Trakmezurilo

> Track gauge

Track gauge in *RdO* for trains, metros, and trams are the same:

$$
  d_\mathrm{gauge}
  \equiv \frac{\pi e}{48_D} \  \textrm{U}
  = \pi e \  2^{113_D} \  l_P
  \approx 1.4333_D \  m
$$

which is compatible with the standard gauge ($1.4351_D \  m$)
with a difference of only $2 \  mm$.
(Hopefully that's small enough...)

### Maso

> Mass

> [!IMPORTANT]
> Default mass unit: ***pakmoj*** `p` (Omnija kilogram)

$$
  \textrm{p}
  \equiv 2^{24_D} \  m_P
  \approx 0.365_D \  \textrm{kg}
$$

A munio of said unit mass is a Omnija ton:

$$
  \textrm{Mp}
  \equiv 2^{16_D} \  \textrm{p}
  \approx 23.930_D \  \textrm{t}
$$

which happens to be about 1 FEU container equivalent of goods.

### Tempo

> Time

> [!IMPORTANT]
> Default time unit: ***ŝekuntoj*** `ŝ` (Omnija seconds)

$$
  1 \  ŝ
  \equiv 9198461_D \times 2^{121_D} \  t_P
  \approx 1.318_D \  s
$$
<!-- 1 \  ŝ = 1.518_H \  s -->

The ŝekuntoj is calilbrated such that each Earth day is about $16_D^4 \  ŝ$.

- `ŝ`: ***ŝekuntoj*** | Omnija Seconds
- `ĉ`: ***Ĉimutoj***  | Omnija Minutes
  - 1 Ĉimuto is  $1440_D/1024_D = 1.40625_D$ SI Minutes.
- `ĝ`: ***Ĝoroj***    | Omnija Hours
  - 1 Ĝoro is    $24_D/16_D = 1.5_D$ SI Hours.
- `Mŝ`: *Munioŝekuntoj* / ***Tagoj***    | Omnija Days
  - Conversion rate:
    $$1\textrm{Mŝ} = 16_D ĝ = 1024_D ĉ = 65536_D ŝ$$
    i.e.,
    $1\textrm{Mŝ} = 10_H ĝ = 400_H ĉ = 10000_H ŝ $;
    $1ĝ = 40_H ĉ$,
    $1ĉ = 40_H ŝ$;
  - i.e. $1 \  \textrm{tago} = 1 \textrm{Mŝ}$;
  - 1 Ŝekunto is therefore
    approximately $86400_D/65536_D = 1.318359375_D$ SI Seconds.
  - ($D$ for decimal, $H$ for Hexadecimal)
- `Ŝ`: ***Ŝemajnoj*** | Omnija Weeks
- `O`: ***Monatoj***  | Omnija Months
- `Ĵ`: ***Ĵaroj***    | Omnija Unit years
  - Unit year - Length is precisely Dx365.25 Omnija Days.
- `J`: ***Jaroj***    | Omnija Calendar years
  - Calendar year - Length varies depending on which year it is.
  - Here we assume one non-leap year (*komunjaro*) is 13 months exactly,
    and each months has 4 weeks exactly

    $$1J_\textrm{komun} = Σ_H O = 34_H Ŝ = 16Π_H \textrm{Mŝ} = 364_D \textrm{Mŝ}$$

    except leap year (*superjaro*), which happens every 4 years,
    and has 5 extra days (all considered holidays):

    $$1J_\textrm{super} = Σ O + 5 \textrm{Mŝ} = 171_H \textrm{Mŝ} = 369_D \textrm{Mŝ}$$

  - Winter Solstice[^Tagoj-Solstico] always happens
    in the first week of the year for the Y+\* calendars.
    The leap year (Y+\* years ends with $3_H, 7_H, λ_H, Ψ_H$) adds extra days at the end of the year,
    and the year immediately after the leap year have the solstice
    happening at the (evening of the) first day of the year.
    The first week of the year
    (together with the days added by leap years if any)
    are holidays.
  - Solstices and Equinoxes are national holidays.

[^Tagoj-Solstico]: a.k.a. Northern Solstice, since *la Insulo-Omnijo* is located in the Southern Hemisphere.

### Temperaturo

> Temperature

> [!IMPORTANT]
> Default temperature unit: ***Zoroj*** `Z` (degree Zoro) (prrovisional name)

$$
  \textrm{Z}
  \equiv 10011_D \times 2^{-120_D} \  T_P
  \approx 1.067_D \  \textrm{K}
$$

The Zoroj is calilbrated such that
Hx100 Z is approximately the [triple point of water](https://en.wikipedia.org/wiki/Triple_point#Triple_point_of_water):

$$
  \textrm{jZ}
  \equiv 100_H Z
  \approx 273.16_D \  \textrm{K}
  \approx 0.013_D \  \degree \textrm{C}
$$

The boiling point of water is approximately

$$
  100_D \degree \textrm{C}
  \approx 15Σ.λ_H \textrm{Z}
$$

$\textrm{Z} = 0$ is exactly the absolute zero temperature.

Normal body temperature ranges approximately
from $122_H \textrm{Z} \approx 36.3_D \degree \textrm{C}$
to   $123_H \textrm{Z} \approx 37.4_D \degree \textrm{C}$.

Ideal room temperature ranges approximately
from $111_H \textrm{Z} \approx 18.2_D \degree \textrm{C}$
to   $114_H \textrm{Z} \approx 21.4_D \degree \textrm{C}$.

### Rapido

> Speed

Standard: Utro por ŝekuntoj, or Uoŝ:

$$
  \textrm{Uoŝ}
  \equiv \textrm{U/ŝ}
  = \textrm{gU/ĝ}
  \approx 6.11_D \  \textrm{m/s}
  \approx 22.0_D \  \textrm{kph}
$$

jU por ĝoro (or jU/ĝ / joĝ for short)

$$
  \textrm{joĝ}
  \equiv \textrm{jU/ĝ}
  = 1/16_D \  \textrm{U/ŝ}
  \approx 1.375_D \  \textrm{kph}
$$

- Speed limits examples:

  | joĝ | kph (proksimumo) | kph (limo) |
  | :--------- | :----: | ---------: |
  |   Hx 100   | Dx 352 |   Dx 360   |
  |   Hx  80   | Dx 176 |   Dx 180   |
  |   Hx  60   | Dx 132 |   Dx 135   |
  |   Hx  58   | Dx 121 |   Dx 125   |
  |   Hx  50   | Dx 110 |   Dx 110   |
  |   Hx  48   | Dx  99 |   Dx 100   |
  |   Hx  40   | Dx  88 |   Dx  90   |
  |   Hx  38   | Dx  77 |   Dx  80   |
  |   Hx  30   | Dx  66 |   Dx  65   |
  |   Hx  28   | Dx  55 |   Dx  55   |
  |   Hx  20   | Dx  44 |   Dx  45   |
  |   Hx  18   | Dx  33 |   Dx  35   |
  |   Hx  10   | Dx  22 |   Dx  20   |
  |   Hx   8   | Dx  11 |   Dx  10   |

### Code illustrations

See the corresponding [python script](Unuoj.py).
