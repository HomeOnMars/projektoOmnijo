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

See also [Lingvo](../teknikoj/Lingvo.md#algebro) page for prefix acronyms
$H \  J \  G \  M \  D \  T \ I$ for
Hx10, Hx100, Hx1000, Hx 1 0000 = 1p4, 1p8, 1pΠ, 1p40, etc;
also for Hexadecimal pre/surfix *H* vs Decimal pre/surfix *D*.

Bazaj Unuoj
-------------------------------------------------------------------------------

> Base units

### Longeco

> Length

> [!IMPORTANT]
> Base length unit: ***Utro*** `U` (Omnija meter)

$$
  \textrm{U}
  \equiv 11977_D \times 2^{105_D} \  l_P
  % = 2ΥΠ9_H \times 2^{69_H} \  l_P
  = 5.Σ92_H \times 10_H^{{1Σ}_H} \  l_P
  \approx 7.8525_D \  \textrm{m}
$$

Utroj are calilbrated such that 1U is approximately 8 meters,
while the speed of light $c = 300 \ 0000_H \textrm{U/Ŝ}$ precisely
under the [time definition Ŝ](#tempo).

Notes:

- $11977_D = 35931_D / 3$;  
  (also $11977_D = 7 \times 29_D \times 59_D$.)
- 1 cell width in-game (Cities Skylines 2) is set as 1U exactly.
  This is an assumption imposed by me for RdO-related cities only.
- Using `U` instead of `u`, as the [convention](Lingvo.md#algebro) here is
  to use capital letter as the first letter.

*JentUtro* (`JU`):

$$
  \textrm{JU}
  \equiv 256_D \  \textrm{U}
  \approx 2.0102_D \  \textrm{km}
$$

*GilUtro* (`GU`):

$$
  \textrm{GU}
  \equiv 16_D^3 \  \textrm{U}
  \approx 32.164_D \  \textrm{km}
$$

*MuniUtro*  (`MU`):

$$
  \textrm{MU}
  \equiv 16_D^4 \  \textrm{U}
  \approx 514.62_D \  \textrm{km}
$$

Consequentially, one Earth radius is approximately

$$
  R_{\oplus}
  \approx Π.64ΠΨ_H \  \textrm{MU}
  \approx 6378.1_D \  \textrm{km}
$$

One astronomical unit is approximately

$$
  \textrm{au}
  \approx 4.6Ψ87_H \  \textrm{DU}
  \approx 1.4960_D \times 10_D^{8} \  \textrm{km}
$$

One light-year is approximately

$$
  \textrm{lyr}
  \approx 4.47Π3_H \  \textrm{TU}
  \approx 9.4607_D \times 10_D^{12_D} \  \textrm{km}
$$

*hekonUtro* (`hU`):

$$
  \textrm{hU}
  \equiv \frac{1}{16_D} \  \textrm{U}
  \approx 0.49078_D \  \textrm{m}
$$

Nanosvarmo scale *dunionUtro*  (`dU`):

$$
  \textrm{uU}
  \equiv 10_H^{-8} \  \textrm{U}
  \approx 1.8283_D \  \textrm{nm}
$$

#### Trakmezurilo

> Track gauge

Track and loading gauges in *RdO* are:

- Track gauge  
  3 hU (≈ Dx1.4723 m $= 35931_D \times  2^{101_D} \  l_P$)
- Loading gauge (max width)
  - *Tram*  
    6 hU (≈ Dx2.9447 m)
  - *Train/Metro*  
    7 hU (≈ Dx3.4354 m)
- Loading gauge (max height, overhead wires, measured in-game in CSL2)  
  - *Tram*  
    9 hU (≈ Dx4.4170 m)
    - Tram track are fully embedded at ground level.
  - *Train*  
    Π hU (≈ Dx5.8894 m) (above ground)
    - This includes 2 jU (≈ Dx6.13 cm) height of the train track.  
      The pure height difference from top of the track to the overhead wires
      is λ.Υ hU (≈ Dx5.8280 m).
- Loading gauge (max height excl. pantograph)  
  - *Tram/Metro*  
    8 hU (≈ Dx3.9262 m)
  - *Train*  
    λ hU (≈ Dx5.3986 m)
  - Note:
    keep a minimum 3/4 hU electrical clearance
    inbetween the top of trains and the overhead wires.
- Capacity  
  Assuming each seat is 1 hU wide and 2 hU long, and the cabin is 5 hU tall,
  This implies a capacity of passengers per U car length of
  - *Tram*:
    <!-- single floor, longitudinal seating layout,
    2 seats + 2 standing per 1 hU length, i.e.   -->
    Dx64 passengers/U (excluding driver's cabins at both ends),  
    or Dx224 passengers per 4U-long tram.
  - *Metro*:
    <!-- single floor, longitudinal seating layout, driverless,
    2 seats + 3 standing per 1 hU length, i.e.   -->
    Dx80 passengers/U,  
    or Dx960 passengers per 12U-long metro train.
  - *Train (local)*:
    <!-- double-decker, transverse seating layout, driverless,
    6 seats per 2 hU length (plus 1 empty hU for corridors),
    1 U single-decker (same stats as metro) +
    ½ U for stairs/toilets + 1½ U double-decker, i.e.   -->
    Average \~Dx74.67 passengers/U (excluding driver's cabins),  
    or Dx224 passengers per 3U-long train car,  
    or Dx1792 passengers per 24U-long train.
  - *Train (high speed)*:
    <!-- single floor, transverse seating layout, driverless,
    6 seats per 2 hU length (plus 1 empty hU for corridors), i.e.   -->
    Dx48 passengers/U
    (excluding driver's cabins, toilets, first class, etc),  
    or Dx120 passengers per 3U-long train car,  
    or Dx960 passengers per 24U-long train.

Yes, the RdO track gauge is incompatible
with the standard gauge (Dx 1.4351 m) with a difference of 3.7 cm.
This is part of Omnijo's intentional effort
to technologically isolate itself from the rest of the world,
without directly imposing on people's freedom…
Basically one of the main points of
coming up with its own unit system in the first place.
(The other being satisfying
the <span style="color:Beige">Queen</span>'s OCD tendencies.)

The RdO loading gauge for trains is \~29cm wider and \~75cm taller than the
[European standards](https://en.wikipedia.org/wiki/Loading_gauge#European_standards), and
\~4cm wider and \~60cm taller than the
[Chinese standards](https://en.wikipedia.org/wiki/Loading_gauge#China).

#### Kontnera Mezurilo

> Container dimensions

Standard RdO container dimensions:

| Name | Width (External, Hx jU) | Height (External, Hx jU) | Length (External, Hx jU) | Internal Dimensions (Hx jU) | Internal Volume (Hx hU^3) | Expected Net weight (Hx MP) | Max Net weight (Hx MP) | Max Gross weight (Hx MP) |
| ---- | --: | --: | --: | :-------------: | :-----: | :-: | :--: | :-: |
|  NKU |  54 |  54 |  Δ8 |  4Ψ x  4Π x  Δ0 |   ΥΔ.88 | 0.8 | 1.08 | 1.2 |
|  DKU |  54 |  54 | 150 |  4Ψ x  4Π x 148 |  1Υ0.ΠΔ | 1.0 | 1.18 | 1.4 |

- Width (External)
  - Hx 5.4 hU (≈ Dx2.5766 m)
    - \~Dx0.1382 m wider than ISO standard.
    - This is constrained by the
      [standard truck width](https://en.wikipedia.org/wiki/Lane#Lane_width) (2025-10-24)
      (which is in turn limited by lane width for roads), which is Dx2.6m.
    - Assume a gap of 1jU and a wall thickness of 1½jU on either side,
      this means an internal width of 4.ΨhU (≈ Dx2.4232 m).
- Height (External)
  - Hx 5.4 hU (≈ Dx2.5766 m)
    - \~Dx0.0142 m shorter than ISO standard.
    - This allows cargo trains to vertically stack 2 containers per car.
    - The matching width and height allows the containers to be
      potentially stacked sideways
      (with special inter-direction connecting units in-between),
      which would hopefully benefit us once we get to space
      where there is no more definitive concept of the "down" direction.
    - Assume a gap of 4jU thick of wall + interlocking mechanism
      on either side, this means an internal height of 4.ΠhU (≈ Dx2.3312 m).
- Length (External)
  - Hx Δ.8 hU (≈ Dx5.1532 m)
    - > Container name: **NKU** (Norma KontenerUnuo)
    - \~Dx0.9047 m shorter than ISO [TEU](https://en.wikipedia.org/wiki/Twenty-foot_equivalent_unit) (2025-10-24) standard.
    - Assume a gap of 1jU and a 3jU thick of wall + door locking mechanism
      on either side, this means an internal length of Δ.0hU (≈ Dx4.9078 m).
    - Internal volume: Hx ΥΔ.88 hU^3 (≈ Dx27.72 m^3)
  - Hx 15 hU (≈ Dx10.3064 m)
    - > Container name: **DKU** (Duobla KontenerUnuo)
    - \~Dx1.8856 m shorter than ISO FEU standard.
    - Precisely 4 times longer than its widths and heights,
      for easier stacking in any directions (e.g. in space)
      (Now you can build a fort out of it!).
    - Assume a gap of 1jU and a 3jU thick of wall + door locking mechanism
      on either side, this means an internal length of 14.8hU (≈ Dx10.0610 m).
    - Internal volume: Hx 1Υ0.ΠΔ hU^3 (≈ Dx56.84 m^3)

The <span style="color:Beige">Queen</span> only really starts
to push this standard (both on and off the island)
after her 8th coronation anniversary, apparently triggered
by the following short period of near-worldwide embargo on her island…
But that's another story.  
From there, the RdO containers standard gradually spreads across the world.

TBD: decide if I should cave and set the NKU dimensions to be 1:2.5 instead of 1:2.

### Maso

> Mass

> [!IMPORTANT]
> Base mass unit: ***Pakmoj*** `P` (Omnija kilogram)

$$
  \textrm{P}
  \equiv 2^{24_D} \  m_P
  = 10_H^{6} m_P
  % = \mathrm{JM} m_P
  \approx 0.365_D \  \textrm{kg}
$$

A munio of said unit mass is a Omnija ton:

$$
  \textrm{MP}
  \equiv 2^{16_D} \  \textrm{P}
  \approx 23.930_D \  \textrm{t}
$$

which happens to be about 1 FEU container equivalent of goods.

### Tempo

> Time

> [!IMPORTANT]
> Base time unit: ***Ŝekunto*** `Ŝ` (Omnija second)

$$
  1 \  Ŝ
  \equiv 35931_D \times 2^{129_D} \  t_P
  = 1.18λ6_H \times 10_H^{{24}_H} \  t_P
  % = 1.18λ6_H \mathrm{K} t_P
  \approx 1.3183_D \  s
$$
<!-- 1 \  Ŝ \approx 1.518_H \  s -->

Ŝekuntoj are calilbrated such that each Earth day is about $16_D^4 \  Ŝ$,
with an approximate difference of only Dx 1.17 SI seconds per day.  
(Note that this difference is much larger than the old def
of $1149807 \times 2^{124_D}$,
which has only Dx 0.043 SI seconds difference per day.
I changed it from 1149807 to 35931 because
the arbitrary factor is smaller (within one Muni!);
and that the 1s difference is still small enough for day-to-day usage
(high precision usage like for astronomical purposes
will have to use alternative timing system anyway);
and that RdO will expand beyond Earth one day, so the simplicity of def
should take priority over aligning percisely to Earth's rotation cycle,
which is also slowing down over millennia.)

- `Ŝ`: ***Ŝekunto*** | Omnija Second
  - Side note: munionŜekuntoj `mŜ`
    is $1 \  \textrm{mŜ} = 0.0001_H Ŝ \approx 0.02_D \  \textrm{ms}$
- `Ĉ`: ***Ĉimuto***  | Omnija Minute
  - 1 Ĉimuto is about $1440_D/256_D = 5.625_D$ SI Minutes.
- `Ĝ`: ***Ĝoro***    | Omnija Hour
  - 1 Ĝoro is about $24_D/16_D = 1.5_D$ SI Hours.
- `⚻` or `MŜ`: ***Tago*** / *MuniŜekuntoj* | Omnija Day
  - Conversion rate:
    $$1⚻ = 1\textrm{MŜ} = 16_D Ĝ = 256_D Ĉ = 65536_D Ŝ$$
    i.e.,
    $1\textrm{MŜ} = 10_H Ĝ = 100_H Ĉ = 10000_H Ŝ $;  
    $1Ĝ = 10_H Ĉ$,  
    $1Ĉ = 100_H Ŝ$;
  - 1 Ŝekunto is therefore
    approximately $86400_D/65536_D = 1.318359375_D$ SI Seconds.
  - ($D$ for decimal, $H$ for Hexadecimal)
  - Omnijo labour law enforces 7.5-hour (5-Ĝora) workday
    (30 hours / Hx14Ĝ work per week, as each week have 4 workdays).  
    Each day is divided into 3 shifts:  
    0Ĝ (00:00) -> 6Ĝ (09:00) -> λĜ (16:30) -> Hx10Ĝ (00:00)
    (midnight next day).  
    Companies have the freedom to shift the beginning of the workday
    to be up to 1Ĝ earlier.
  - Seven days of the week  
    The symbols are selected to avoid
    the ones already used in the base-32 ONKIO character set
    (see [unuoj.py](unuoj.py) `TX_SYMBOLS_DICT['ONKIO']` dict),  

    | Siglo | Epopo | Esperanto | English |
    | :-: | ------ | -------- | --------- |
    | L | Lundo    | Lundo    | Monday    |
    | A | Mardo    | Mardo    | Tuesday   |
    | B | Berkredo | Merkredo | Wednesday |
    | Ʌ | Ʌaŭdo    | Ĵaŭdo    | Thursday  |
    | V | Vendredo | Vendredo | Friday    |
    | S | Sabato   | Sabato   | Saturday  |
    | Z | Zimanĉo  | Dimanĉo  | Sunday    |

- `⚝`: ***Semajno*** | Omnija Week
  - Four weeks of the month:
    labeled as `O`, `I`, `Q`, `U` in that order.
- `☾`: ***Monato***  | Omnija Month
- `Ĵ`: ***Ĵaro***    | Omnija Unit Year
  - Unit year - Length is precisely Dx365.25 (Hx16Σ.4) Omnija Days.
- `J`: ***Jaro***    | Omnija Calendar Year (Earth-specific)
  - Calendar year - Length varies depending on which year it is.
- `DŜ`: ***DuniŜekunto*** | Omnija Century (kinda)
  - 1 DŜ = Hx10000⚻ ≈ Dx 179.43 yr

#### Omnijaro

> `Omnijaro` Calendar System (Ø+\* (0xD8))

##### Omnijara Difino

> Omnijaro definition

- Each non-leap year (*`komunjaro`*) has 13 months plus 1 day exactly,
  and each months has 4 weeks exactly

  $$1J_\textrm{komun} = Σ_H ☾ + 1⚻ = 34_H ⚝ + 1⚻ = 16Σ_H ⚻ = 365_D ⚻$$
- Name for the months see [Lingvo](Lingvo.md#tempo) page.
- Leap year (*`superjaro`*) has 2 extra days outside the normal 13 months:

  $$1J_\textrm{super} \simeq Σ ☾ + 2 ⚻ = 16Υ_H ⚻ = 366_D ⚻$$
- Leap year happens every 4 years, except every Dx128 years.
  (So ~3 skipped leap years per 400 years-
  the nice coincidence of hexadecimal system.)  
  More specifically,
  it happens at Ø+\* years ending with $0_H, 4_H, 8_H, Π_H$,
  except Ø+\* years ending with $00_H, 80_H$.  
  This is to sync the *Omnijaro* Calendar with
  [Solar Year](https://en.wikipedia.org/wiki/Tropical_year),
  so that solstices happens at around the same days in the year.
- Winter Solstice[^Tagoj-Solstico] always happens
  on the first or last day of the year in the *Omnijaro* calendar.
  The 1 or 2 extra days are added at the end of the year
  as the "fake" Dx13th Month ($☾_Σ$, or *`Sigamonato`*),
  which has only 1 or 2 days (plus potential extra seconds).
- Ø+\* years ending with $00_H, 80_H$ (i.e. the special non-leapyear)
  have the solstice happening at approximately midnight
  between the old and the new year.  
  Because of this, one can imagine Ø+0 is set as 2026-06-22,
  though I'd really rather left the definition open for interpretation.
- Dx13th Month $☾_Σ$ and the first week of the year are holidays.
- Solstices and Equinoxes are national holidays.
- Any changes to the calendar years system
  (such as adding leap seconds to sync with Earth's orbit,
  or more drastic changes in the event of
  Earth's rotation period or orbit changes significantly)
  should in principle only be added / removed in Dx13th Month $☾_Σ$.
- In other words, extra seconds may be added or substracted in $☾_Σ$
  to keep the days in sync with
  [Mean Solar Time](https://en.wikipedia.org/wiki/Solar_time#Mean_solar_time).
  Usually this means adding $\sim 7.1$ minutes or Hx1Ĉ44Ŝ.
- This means that on average, one Omnija Calendar Year is approximately
  $1 J \approx 365.24713_D ⚻$ currently,
  considering both leap years and added seconds.

[^Tagoj-Solstico]: a.k.a. Northern Solstice, since *la Insulo-Omnijo* is located in the Southern Hemisphere.

##### Omnijara Notacio

> Omnijaro Notations

> [!IMPORTANT]
> **Omnija Epoch**: `2026-06-21T08:24:00+00:00` (ISO 8601 format)  
> Serena's coronation day, which also happens to be Northern Solstice 2026.

See also [unuoj.py](unuoj.py) `Datotempo` class.

Two styles:

- Tempstampo (timestamp) style:  
  Using the number of mŜ (in hexadecimal) after the Omnija Epoch.  
  The benefits of the Omnija time unit system is that
  one can easily read the number of days from the timestamp.

  E.g. 2024-12-21T09:20:00+00:00 (Southern Solstice 2024):

  > -222 Ψ7Ψ0 Σλ8Π

  Here, '-222' is the number of days since the Omnija Epoch in hexadecimal,
  and 'Ψ:7:Ψ0' is the Ĝoro:Ĉimuto:Ŝekunto in Omnija timezone,
  and 'Σλ8Π' is the munionŜekuntoj left over.

  Code Illustration:

  ```python
  from projektoOmnijo.teknikoj.unuoj import Datotempo, datetime, UTC, presi_Hx
  tempstampo = Datotempo(datetime(2024, 12, 21, 9, 20, tzinfo=UTC)).tempstampo
  print(f"Dx {tempstampo}")
  print(presi_Hx(tempstampo, e_sep=''))
  ```

  Result:

  ```text
  Dx -2349211900812 mŜ
  Hx -222Ψ7Ψ0Σλ8Π mŜ
  ```

- ONKIO style (Earth-specific):  
  Aiming for being more naturally readable.  
  Start with the 'Ø' symbol to signify the ONKIO Omnijaro calendar format
  (if dates are included),
  followed by '-/+' sign and the calendar year (not unit year) number;  
  use hyphen to connect year, month, and week-day;  
  use letters instead of numbers to represent week and day;  
  use 'ⅎ' to separate the dates from time;  
  Write Ĝoro:Ĉimuto:Ŝekunto.
  Ŝekunto has 2 digits while the other 2 has 1,
  so you can easily tell which ones are which.
  I.e. this helps differentiate between Δ:97 (ΔĈ 97Ŝ) and Δ:9 (ΔĜ 9Ĉ).

  Default timezone is Omnijo timezone.

  > [!NOTE]
  > How to add time zone info: TBD.

  E.g. 2024-12-21T09:20:00+00:00 (Southern Solstice 2024):

  > Ø-2‐6‐QAⅎ0:Δ:97.247Π

  Code Illustration:

  ```python
  from projektoOmnijo.teknikoj.unuoj import Datotempo, datetime, UTC
  t = Datotempo(datetime(2024, 12, 21, 9, 20, tzinfo=UTC))
  print(t.iso)
  print(t.onkio)
  ```

  Result:

  ```text
  2024-12-21T09:20:00.000007+00:00
  Ø-2‐6‐QAⅎ0:Δ:97.247Π
  ```

### Temperaturo

> Temperature

> [!IMPORTANT]
> Base temperature unit: ***Zoro*** `Z` (Omnija Kelvin)

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
> Useful temperature unit: ***Zorumgrado*** `°Ž` (0x017D)
> (Omnija degree Celsius)

(Add a caron above 'Z' to make sure people don't confuse `°Ž` with `Z`.)

$$
  X \degree \textrm{Ž}
  = 100_H + X \textrm{Z}
$$

Normal body temperature ranges approximately
from $122_H \textrm{Z} = 22_H \degree \textrm{Ž} \approx 36.3_D \degree \textrm{C}$
to   $123_H \textrm{Z} = 23_H \degree \textrm{Ž} \approx 37.4_D \degree \textrm{C}$.

Ideal room temperature (for thermostat) ranges approximately
from $112_H \textrm{Z} = 12_H \degree \textrm{Ž} \approx 19.2_D \degree \textrm{C}$
to   $116_H \textrm{Z} = 16_H \degree \textrm{Ž} \approx 23.5_D \degree \textrm{C}$.  
When quoting room temperature in Omnijo, generally it is referring
to   $114_H \textrm{Z} = 14_H \degree \textrm{Ž} \approx 21.4_D \degree \textrm{C}$.

### Ŝargo

> Charge

> [!IMPORTANT]
> Base electric charge unit: ***Elektrio*** `E` (Omnija Coulomb)

$$
  \textrm{E}
  \equiv \frac{1}{3} \times 65536_D^4 \  e
  \approx 0.98516_D \  \textrm{C}
$$

Multiplied by 1/3 because quarks have -1/3 e or 2/3 e charges.
Elektrio is short for Elektronkvarnitriono.

### Angulo

> Angle

> [!IMPORTANT]
> Base angle unit: ***Cirklo*** `Ck` (Circle)

$$
  \textrm{Ck}
  \equiv 2 \pi \  \textrm{rad}
  = 360_D \degree
$$

Ck is just a full circle.

*hekonCirklo* (`hCk`):

$$
  \textrm{hCk}
  \equiv \frac{1}{10_H} \  \textrm{Ck}
  = 22.5_D \degree
$$

*jentonCirklo* (`jCk`):

$$
  \textrm{jCk}
  \equiv \frac{1}{100_H} \  \textrm{Ck}
  = 1.40625_D \degree
$$

*gilonCirklo* (`gCk`):

$$
  \textrm{gCk}
  \equiv \frac{1}{1000_H} \  \textrm{Ck}
  \approx 5.2734_D \  \textrm{arcmin}
$$

*munionCirklo*  (`mCk`):

$$
  \textrm{mCk}
  \equiv \frac{1}{10000_H} \  \textrm{Ck}
  \approx 19.775_D \  \textrm{arcsec}
$$

*dunionCirklo*  (`dCk`):
(mas means milliarcsecond)

$$
  \textrm{dCk}
  \equiv \frac{1}{10000_H^2} \  \textrm{Ck}
  \approx 0.30175_D \  \textrm{mas}
$$

Note: The angular diameter of the closest star, Proxima Centauri,
is Dx1.02 ± 0.08 mas, or approximately Hx3.61 dCk.
(Reference see this ESO article
"[How Small are Small Stars Really?](https://www.eso.org/public/news/eso0232/)"
(2025-05-21))

### Nombro

> Dimensionless quantities / pure numbers

> [!IMPORTANT]
> Base dimensionless unit: ***Nuo*** `_` (i.e. one)

$$
  \textrm{Nuo}
  \equiv 1
$$

*Projento*  (`ⅎ`):
Hexadecimal equivalent of percent

$$
  1 ⅎ
  \equiv \frac{1}{100_H}
  = \frac{1}{256_D}
  % = 0.00390625_D
  = 0.390625 \  \% (\textrm{percent})
$$

### Bito

> Bits and bytes

> [!IMPORTANT]
> Base Bit unit: ***Bito*** `Bit` (Bit, or `B`)  
> (Avoid using `B` to avoid confusion with SI byte $\textrm{B}_\textrm{SI}$.)

> [!NOTE]
> Byte unit: ***Bajto*** `Baj` (Byte)  
> (Avoid using this altogether to avoid confusion with *Bito*.)

$$
  \textrm{Baj}
  \equiv \textrm{B}_\textrm{SI}
  = 8 \textrm{Bit}
  = 8 \textrm{b}_\textrm{SI}
$$

*GilBito*  (`GBit`):

$$
  \textrm{GBit}
  \equiv 1000_H \  \textrm{Bit}
  = ½ \  \textrm{kB}_\textrm{SI}
$$

*MuniBito*  (`MBit`):

$$
  \textrm{MBit}
  \equiv 10000_H \  \textrm{Bit}
  = 8 \  \textrm{kB}_\textrm{SI}
$$

*DuniBito*  (`DBit`):

$$
  \textrm{DBit}
  \equiv 10000_H^2 \  \textrm{Bit}
  = ½ \  \textrm{GB}_\textrm{SI}
$$

*TriniBito*  (`TBit`):

$$
  \textrm{TBit}
  = 32_D \  \textrm{TB}_\textrm{SI}
$$

*KvarniBito*  (`RBit`):

$$
  \textrm{RB}
  = 2 \  \textrm{EB}_\textrm{SI}
$$

Derivitaj Unuoj
-------------------------------------------------------------------------------

> Derived units

### Rapido

> Speed

Standard: Utro por Ŝekuntoj, or UoŜ:

$$
  \textrm{UoŜ}
  \equiv \textrm{U/Ŝ}
  = \textrm{GU/Ĝ}
  \approx 5.9563_D \  \textrm{m/s}
  \approx 21.443_D \  \textrm{kph}
$$

> [!NOTE]
> Useful speed unit: ***JU/Ĝ*** `JoĜ` (JU por Ĝoro, similar to km/h)

$$
  \textrm{JoĜ}
  \equiv \textrm{JU/Ĝ}
  = 1/16_D \  \textrm{U/Ŝ}
  \approx 1.3402_D \  \textrm{kph}
$$

#### Speed of light

The speed of light (in vacuum) is exactly

$$
  c
  =  300 \ 0000_H \textrm{U/Ŝ}
  = 3000 \ 0000_H \textrm{JoĜ}
  =         300_H \textrm{MU/Ŝ}
$$

So when speed exceeds 1 MU/Ŝ (or Hx 10 0000 JoĜ, or \~0.13\%c),
relativistic effects should be considered.
Also, this means that light in vacuum travels precisely 3 JU in 1 mŜ.

#### Human walking speed

Human walking speed $\approx 4 \  \textrm{JoĜ} \approx 5.4_D \textrm{kph}$,
or $3 \sim 4.8_H \  \textrm{JoĜ}$ ($4.0_D \sim 6.0_D \textrm{kph}$).  
Source: (2025-07-03)
[Wikipedia](https://en.wikipedia.org/wiki/Preferred_walking_speed).  
A 1Ĉ (≈5.6min) walking distance can thus be defined as Hx40U or **Dx64U**,
which is approximately Dx503m (or Dx512 CSL meters)

Human jogging speed ranges
from $5 \  \textrm{JoĜ}$ ($\approx 6.7_D \textrm{kph}$)
to   $7 \  \textrm{JoĜ}$ ($\approx 9.4_D \textrm{kph}$).  
Source: (2025-07-03)
[Wikipedia](https://en.wikipedia.org/wiki/Jogging#Definition).

Walkable distances:

| Time (Dxmin) | Time (HxĈ) | Distance (HxU) | Distance (DxU) | Distance (Dxkm_CSL) |
| :-------- | :----: | :-----: | :-----: | ---------: |
| Dx  6 min | Hx  1Ĉ | Hx  40U | Dx  64U | Dx  0.5 km |
| Dx 11 min | Hx  2Ĉ | Hx  80U | Dx 128U | Dx  1.0 km |
| Dx 17 min | Hx  3Ĉ | Hx  Π0U | Dx 192U | Dx  1.5 km |

#### Speed limits examples

(kph limit is corrected with a multiplication factor of `8m/U`)

| JoĜ | CSL kph (proksimumo) | CSL kph (limo) |
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
> Useful Power unit: ***MuniLumro*** `⚡` (0x26A1) (Omnija MWs)

$$
  ⚡
  \equiv 10000_H \textrm{Lu}
  = 10000_H \textrm{U}^2 \textrm{P} / \textrm{Ŝ}^3
  \approx 0.64399_D \  \textrm{MW}
$$

while the power unit ***Lumro*** is defined as

$$
  \textrm{Lu}
  \equiv \textrm{U}^2 \textrm{P} / \textrm{Ŝ}^3
  \approx 9.8264_D \  \textrm{W}
$$

OC's target power poduction is
about Hx8000⚡(Dx21.1GW) to Hx10000⚡(Dx42.2GW).

Notably, Hx10⚡≈ Dx10MW.

The output of the sun is

$$
  L_\odot
  \approx 3.828_D \times 10_D^{17_D} \textrm{GW}
  \approx 20.394_H \textrm{VLu}
  \approx 2.0394_H \times 10_H^{11_H} ⚡
  \approx 20 \  3945 \  851Π \  039Π \  0000_H ⚡
$$

The solar energy received by Earth
(including those reflected into space before reaching ground)
is approximately

$$
  \frac{\pi R_{\oplus}^2}{4 \pi (\textrm{au})^2} L_\odot
  \approx 1.74_D \times 10_D^8 \textrm{GW}
  \approx 3Υ.5_H \textrm{TLu}
  \approx 3.Υ5_H \times 10_H^9 ⚡
  \approx 3Υ \  Υ4Πλ \  466λ_H ⚡
$$

<!-- \approx 3Υ Υ501 0Π25_H ⚡ -->

Kromaĵo
-------------------------------------------------------------------------------

> Extra

### Konstantoj

> Constants

Some helpful constants and factors:

As mentioned before for [Utro](#longeco),
  the speed of light is exactly

$$
  c
  = l_P / t_P
  = 300_H \  \textrm{MU/Ŝ}
$$

Boltzmann constant is exactly

$$
  k_B
  = c^2 \  m_P / T_P
  = 1.5ΨΨ3 \times 10_H^{{-14}_H} \  \textrm{U}^2\textrm{P}/(\textrm{Ŝ}^2\textrm{Z})
$$

(Note: $15ΨΨ3_H = 3^2 \times 10011_D$.)

Reduced Planck constant is

$$
  \hbar
  = c \  l_P \  m_P
  = \frac{3}{5Σ92_H} \times 10_H^{{-1Δ}_H} \  \textrm{U}^2\textrm{P}/\textrm{Ŝ}
  \approx 6.1748_D \times 10_D^{{-36}_D} \  \textrm{U}^2\textrm{P}/\textrm{Ŝ}
$$

(Unfortunately the seemingly arbitrary number
here Hx5Σ92 = Dx23954 = 2 \* Dx11977
comes from the length of a day from the rotation of the Earth-
it cannot be removed easily without other trade-offs.)

Gravitational constant is

$$
  G
  = c^2 \  l_P / m_P
  = \frac{9}{5Σ92_H} \times 10_H^{{-8}} \  \textrm{U}^3/\textrm{P}\textrm{Ŝ}^2
  \approx 8.7479_D \times 10_D^{{-14}_D} \  \textrm{U}^3/\textrm{P}\textrm{Ŝ}^2
$$

Earth surface gravity is approximately

$$
  g_0
  \approx 2.2Π_H \  \textrm{U}/\textrm{Ŝ}^2
  = 9.81 \  \textrm{m}/\textrm{s}^2
$$

### Monero

> Currency

> [!NOTE]
> Currency unit: ***Sejro*** `🪙` (0x1FA99) (Omnija dollar)

<!-- `💲` (0x1F4B2) -->
<!-- `🪙` (0x1FA99) -->

How much is 1 Sejro worth?
Using energy price as calibration:
In CSL2 game, each MW gives 🪙Dx2500 per month when exported,
which means approximately **🪙Dx0.0034 per kWh**.

Considering the energy price in EU after tax in 2024 are
around 0.1 €/kWh to 0.4 €/kWh
(Reference see Figure 1 in [this eurostat webpage](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Electricity_price_statistics) (2025-03-15)),
this means 1🪙 is approximately somewhere in between 30 € and 120 €.

<!-- As we presume that OmniCentro's money-making mechanism of exporting electricity
here is through computation in data centers for world modeling and manipulation, -->
Let us assume the energy price in RdO is somewhat akin to Iceland
(which is also dominated by hydropower),
i.e., **🪙1 ≈ € Dx60**.

On the other hand,
wage in CSL2 seems to be 🪙Dx2000 per month for Educated employees.
Given that minimum wages in Europe is approximately € Dx2000 per month,
it would be reasonable to assume **🪙1 ≈ €2**? (I am very confused.)

Perhaps the energy price in CSL2 was meant to be 🪙Dx2500 per hour, not month?
In this case, since CSL2 assumes 1 day equals 1 month,
it would imply **🪙1 ≈ €2**, and the world makes sense again.

### Code illustrations

See the corresponding [python script](unuoj.py).
