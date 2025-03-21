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
> Planck temperature $T_P \equiv \sqrt{\frac{\hbar c^5}{G k_B^2}}$;  
> $c$ is the [speed of light](https://en.wikipedia.org/wiki/Speed_of_light) in vaccum;  
> $\hbar$ is the [reduced Planck constant](https://en.wikipedia.org/wiki/Planck_constant#Reduced_Planck_constant) (\~ photon energy per frequency);  
> $G$ is the [gravitational constant](https://en.wikipedia.org/wiki/Gravitational_constant) (\~ strength of gravity per mass);  
> $k_B$ is the [Boltzmann constant](https://en.wikipedia.org/wiki/Boltzmann_constant) (molecular energy scale per temperature).

See also [Lingvo](../teknikajxoj/Lingvo.md#algebro) page for prefix acronyms
$h \  j \  g \  M \  D \  T \  R \  I$ for
Hx10, Hx100, Hx1000, Hx 1 0000, Hx 1 0000 0000 = 1p8, 1pΠ, 1p10, 1p14, etc;
also for Hexadecimal pre/surfix *H* vs Decimal pre/surfix *D*.

### Longeco

> Length

> [!IMPORTANT]
> Base length unit: ***Utroj*** `U` (Omnija meters)

$$
  \textrm{U}
  \equiv 383269_D \times 2^{100_D} \  l_P
  = 5Σ925_H 2^{64_H} \  l_P
  \approx 7.8526_D \  \textrm{m}
$$

The Utroj is calilbrated such that 1U is approximately 8 meters,
while the speed of light $c = 300 \ 0000_H \textrm{U/ŝ}$ precisely
under the [time definition ŝ](#tempo).

Notes:

- $383269_D = 1149807_D / 3$.
- 1 cell width in-game (Cities Skylines 2) is set as 1U exactly.
  This is an assumption imposed by me for RdO-related cities only.
- Using `U` instead of `u` to avoid name clash
with SI unit of the 'unified atomic mass unit'.

*jentUtro* (`jU`):

$$
  \textrm{jU}
  \equiv 256_D \  \textrm{U}
  \approx 2.0103_D \  \textrm{km}
$$

*gilUtro* (`gU`):

$$
  \textrm{gU}
  \equiv 16_D^3 \  \textrm{U}
  \approx 32.164_D \  \textrm{km}
$$

*MunioUtro*  (`MU`):

$$
  \textrm{MU}
  \equiv 16_D^4 \  \textrm{U}
  \approx 514.63_D \  \textrm{km}
$$

Consequentially, one Earth radius is approximately

$$
  R_{\oplus}
  \approx Π.64Π4_H \  \textrm{MU}
  \approx 6378.1_D \  \textrm{km}
$$

One astronomical unit is approximately

$$
  \textrm{au}
  \approx 4 6Ψ83 8018.9_H \  \textrm{U}
  \approx 4.6Ψ84_H \  \textrm{DU}
$$

One light-year is approximately

$$
  \textrm{lyr}
  \approx 4.47Π0_H \times 10_H^Π \  \textrm{U}
  \approx 4.47Π0_H \  \textrm{TU}
$$

#### Trakmezurilo

> Track gauge

Track gauge in *RdO* for trains, metros, and trams are the same:

$$
  d_\mathrm{gauge}
  \equiv \frac{3}{16_D} \  \textrm{U}
  = 1149807_D \times  2^{96_D} \  l_P
  \approx 1.4724_D \  m
$$

Yes this is incompatible with the standard gauge (Dx 1.4351 m)
with a difference of 3.7 cm.
This is part of Omnijo's intentional effort
to technologically isolate itself from the rest of the world,
without directly imposing on people's freedom...
Basically one of the main points of
coming up with its own unit system in the first place.
(The other being satisfying
the <span style="color:Beige">Queen</span>'s OCD tendencies.)

### Maso

> Mass

> [!IMPORTANT]
> Base mass unit: ***pakmoj*** `p` (Omnija kilogram)

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
> Base time unit: ***ŝekuntoj*** `ŝ` (Omnija seconds)

$$
  1 \  ŝ
  \equiv 1149807_D \times 2^{124_D} \  t_P
  \approx 1.3184_D \  s
$$
<!-- 1 \  ŝ = 1.518_H \  s -->

The ŝekuntoj is calilbrated such that each Earth day is about $16_D^4 \  ŝ$
(with an approximate difference of only Dx 0.043 SI seconds per day).

- `ŝ`: ***Ŝekuntoj*** | Omnija Seconds
- `ĉ`: ***Ĉimutoj***  | Omnija Minutes
  - 1 Ĉimuto is  $1440_D/1024_D = 1.40625_D$ SI Minutes.
- `ĝ`: ***Ĝoroj***    | Omnija Hours
  - 1 Ĝoro is    $24_D/16_D = 1.5_D$ SI Hours.
- `⚻` or `Mŝ`: ***Tagoj*** / *Munioŝekuntoj* | Omnija Days
  - Conversion rate:
    $$1⚻ = 1\textrm{Mŝ} = 16_D ĝ = 1024_D ĉ = 65536_D ŝ$$
    i.e.,
    $1\textrm{Mŝ} = 10_H ĝ = 400_H ĉ = 10000_H ŝ $;  
    $1ĝ = 40_H ĉ$,  
    $1ĉ = 40_H ŝ$;
  - 1 Ŝekunto is therefore
    approximately $86400_D/65536_D = 1.318359375_D$ SI Seconds.
  - ($D$ for decimal, $H$ for Hexadecimal)
- `⚝`: ***Semajnoj*** | Omnija Weeks
- `☾`: ***Monatoj***  | Omnija Months
- `Ĵ`: ***Ĵaroj***    | Omnija Unit Years
  - Unit year - Length is precisely Dx365.25 (Hx16Σ.4) Omnija Days.
- `J`: ***Jaroj***    | Omnija Calendar Years (Earth-specific)
  - Calendar year - Length varies depending on which year it is.
  - Here we assume one non-leap year (*komunjaro*) is 13 months exactly,
    and each months has 4 weeks exactly

    $$1J_\textrm{komun} = Σ_H ☾ = 34_H ⚝ = 16Π_H ⚻ = 364_D ⚻$$

    except leap year (*superjaro*), which happens every 4 years,
    and has 5 extra days (all considered holidays):

    $$1J_\textrm{super} \simeq Σ ☾ + 5 ⚻ = 171_H ⚻ = 369_D ⚻$$

  - Winter Solstice[^Tagoj-Solstico] always happens
    in the first week of the year for the Y+\* calendars.
    The leap year (Y+\* years ends with $3_H, 7_H, λ_H, Ψ_H$) adds extra days at the end of the year,
    and the year immediately after the leap year have the solstice
    happening at the (evening of the) first day of the year.
    The first week of the year
    (together with the days added by leap years if any)
    are holidays.
  - Solstices and Equinoxes are national holidays.
  - Any changes to the calendar years system
    (such as adding leap seconds to sync with Earth's orbit,
    or more drastic changes in the event of
    Earth's rotation period or orbit changes significantly)
    should in principle only be applied at the end of the leap years.

[^Tagoj-Solstico]: a.k.a. Northern Solstice, since *la Insulo-Omnijo* is located in the Southern Hemisphere.

### Temperaturo

> Temperature

> [!IMPORTANT]
> Base temperature unit: ***Zoroj*** `Z` (Omnija Kelvin)

$$
  \textrm{Z}
  \equiv 10011_D \times 2^{-120_D} \  T_P
  \approx 1.067_D \  \textrm{K}
$$

The Zoroj is calilbrated such that
Hx100 Z is approximately the [triple point of water](https://en.wikipedia.org/wiki/Triple_point#Triple_point_of_water):

$$
  \textrm{jZ}
  \equiv 100_H \textrm{Z}
  \approx 273.16_D \  \textrm{K}
  \approx 0.013_D \  \degree \textrm{C}
$$

The boiling point of water is approximately

$$
  100_D \degree \textrm{C}
  \approx 15Σ.λ_H \textrm{Z}
$$

$\textrm{Z} = 0$ is exactly the absolute zero temperature.

> [!NOTE]
> Useful temperature unit: ***Zorumaj gradoj*** `°z` (Omnija degree Celsius)

$$
  X \degree \textrm{z}
  = 100_H + X \textrm{Z}
$$

Normal body temperature ranges approximately
from $122_H \textrm{Z} = 22_H \degree \textrm{z} \approx 36.3_D \degree \textrm{C}$
to   $123_H \textrm{Z} = 23_H \degree \textrm{z} \approx 37.4_D \degree \textrm{C}$.

Ideal room temperature ranges approximately
from $111_H \textrm{Z} = 11_H \degree \textrm{z} \approx 18.2_D \degree \textrm{C}$
to   $114_H \textrm{Z} = 14_H \degree \textrm{z} \approx 21.4_D \degree \textrm{C}$.

### Rapido

> Speed

Standard: Utro por ŝekuntoj, or Uoŝ:

$$
  \textrm{Uoŝ}
  \equiv \textrm{U/ŝ}
  = \textrm{gU/ĝ}
  \approx 5.9563_D \  \textrm{m/s}
  \approx 21.443_D \  \textrm{kph}
$$

> [!NOTE]
> Useful speed unit: ***jU/ĝ*** `joĝ` (jU por ĝoro, similar to km/h)

$$
  \textrm{joĝ}
  \equiv \textrm{jU/ĝ}
  = 1/16_D \  \textrm{U/ŝ}
  \approx 1.3402_D \  \textrm{kph}
$$

The speed of light is exactly

$$
  c
  =  300 \ 0000_H \textrm{U/ŝ}
  = 3000 \ 0000_H \textrm{joĝ}
  =         300_H \textrm{MU/ŝ}
$$

So when speed exceeds 1 MU/ŝ (or Hx 10 0000 joĝ, or \~0.13\%c),
relativistic effects should be considered.

- Speed limits examples:
  (kph limit is corrected with a multiplication factor of `8m/U`)

  | joĝ | kph (proksimumo) | kph (limo) |
  | :--------- | :----: | ---------: |
  |   Hx 100   | Dx 343 |   Dx 350   |
  |   Hx  80   | Dx 172 |   Dx 175   |
  |   Hx  60   | Dx 129 |   Dx 130   |
  |   Hx  58   | Dx 118 |   Dx 120   |
  |   Hx  50   | Dx 107 |   Dx 110   |
  |   Hx  48   | Dx  96 |   Dx 100   |
  |   Hx  40   | Dx  86 |   Dx  90   |
  |   Hx  38   | Dx  75 |   Dx  75   |
  |   Hx  30   | Dx  64 |   Dx  65   |
  |   Hx  28   | Dx  54 |   Dx  55   |
  |   Hx  20   | Dx  43 |   Dx  45   |
  |   Hx  18   | Dx  32 |   Dx  35   |
  |   Hx  10   | Dx  21 |   Dx  20   |
  |   Hx   8   | Dx  11 |   Dx  10   |

### Potenco

> Power

> [!NOTE]
> Useful Power unit: ***MunioLumro*** `⚡` (0x26A1) (Omnija MWs)

$$
  ⚡
  \equiv 10000_H \textrm{Lu}
  = 10000_H \textrm{U}^2 \textrm{p} / \textrm{ŝ}^3
  \approx 0.64398_D \  \textrm{MW}
$$

while the power unit ***Lumro*** is defined as

$$
  \textrm{Lu}
  \equiv \textrm{U}^2 \textrm{p} / \textrm{ŝ}^3
  \approx 9.8263_D \  \textrm{W}
$$

OC's target power poduction is
about Hx8000⚡(Dx21GW) to Hx10000⚡(Dx42GW).

The output of the sun is

$$
  L_\odot
  \approx 20.396_H \textrm{ILu}
  \approx 2.0396_H \times 10_H^{11_H} ⚡
  \approx 20 3961 1201 8174 0000_H ⚡
$$

The solar energy received by Earth is approximately

$$
  \frac{\pi R_{\oplus}^2}{4 \pi (\textrm{au})^2} L_\odot
  \approx 1.74_D \times 10_D^8 \textrm{GW}
  \approx 3Υ.Υ_H \textrm{TLu}
  \approx 3.ΥΥ_H \times 10_H^9 ⚡
  \approx 3Υ Υ000 0000_H ⚡
$$

<!-- \approx 3Υ Υ501 0Π25_H ⚡ -->

### Konstantoj

> Constants

Some helpful constants and factors:

As mentioned before for [Utro](#longeco),
  the speed of light is exactly

$$
  c
  = l_P / t_P
  = 300_H \  \textrm{MU/ŝ}
$$

Earth surface gravity is approximately

$$
  g_0
  \approx 2.2Π_H \  \textrm{U}/\textrm{ŝ}^2
  = 9.81 \  \textrm{m}/\textrm{s}^2
$$

Boltzmann constant is exactly

$$
  k_B
  = c^2 m_P / T_P
  = 1.5ΨΨ3 \times 10_H^{{-14}_H} \  \textrm{U}^2\textrm{p}/(\textrm{ŝ}^2\textrm{Z})
$$

(Note: $15ΨΨ3_H = 3^2 \times 10011_D$.)

### Monero

> Currency

> [!NOTE]
> Currency unit: ***Sejroj*** `💲` (0x1F4B2) (Omnija dollars)

How much is 1 Sejro worth?
Using energy price as calibration:
In CSL2 game, each MW gives 💲Dx2500 per hour when exported,
though in-game we assume 1 day is 1 month (or 1/12 of a year).
This means approximately **💲Dx0.082 per kWh**.

Considering the energy price in EU after tax in 2024 are
around 0.1 €/kWh to 0.4 €/kWh
(Reference see Figure 1 in [this eurostat webpage](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Electricity_price_statistics) (2025-03-15)),
this means 1💲 is approximately somewhere in between 1 € and 4 €.

Due to energies are mostly generated cheaply from hydropower,
it's probably more responsible to say that
the currency situation in RdO should be more akin to Iceland,
i.e.,
**💲1 ≈ €2**.

### Code illustrations

See the corresponding [python script](Unuoj.py).
