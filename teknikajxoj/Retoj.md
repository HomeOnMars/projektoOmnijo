<!-- -*- coding: utf-8 -*- -->

Retaj normoj por vojoj kaj reloj
===============================================================================

> Networks standards for roads and rails

Technical specifications for my fictional Cities: Skylines 2 city *OmniCentro*.

Legal
-------------------------------------------------------------------------------

> [!CAUTION]
> Information collected/generated here is intended for gameplay purposes,
> *so not much effort has been spent on ensuring its accuracy*.  
> Some maybe incorrect or outdated.
> Some are just chosen arbitrarily.  
> Standards here may also be updated without notices.  
> ***Use at your own risk.***

<p xmlns:cc="http://creativecommons.org/ns#" >This work by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/HomeOnMars">HomeOnMars</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></a></p>

Retoj
-------------------------------------------------------------------------------

> Networks
> <br>
> [Back to OmniCentro Content](../OmniCentro.md#teknikaj-specifoj)

-------------------------------------------------------------------------------

> [!NOTE]
> Both trains' and trucks' engine power has been exaggerated by 40\% to 110\%
> compared to real life, since *RdO* enjoys technological superiority.  
> See [below verification section](#networks-specification-details-and-verification)
> for calculations.

### Vojoj

> Roads

#### Aŭtovojoj

> Motorways

- Gradient $s$ and Curve radius $R$ limit:

  |             |  max Gradient $s$ |  min Curve radius $R$        | Speed limit $v_\mathrm{max}$ | $\theta_\mathrm{64u}$ | $\theta_\mathrm{32u}$ | $\theta_\mathrm{16u}$ | $\theta_\mathrm{8u}$ | Notes |
  | ----------- | :-------: | :----------: | :--------: | --- | --- | --- | --- | ----- |
  | -           |  4   \%   |  552m (69u)  |  125 km/h  |  $95\degree$ | $131\degree$ | $154\degree$ | $167\degree$ | |
  | Recommended |  6   \%   |  352m (44u)  |  100 km/h  | -            | $108\degree$ | $141\degree$ | $160\degree$ | |
  | Soft Limit  |  8   \%   |  224m (28u)  |   80 km/h  | -            | -            | $121\degree$ | $149\degree$ | For ramps / In mountains |
  | -           | 10   \%   |  144m (18u)  |   65 km/h  | -            | -            |  $97\degree$ | $133\degree$ | Mountains Only |
  | Hard Limit  | 10   \%   |   32m  (4u)  |   30 km/h  | -            | -            | -            |  -           | Mountains Only |

  - $\theta_{d}$ refers to the angle displayed when building a 2-phase curve of $d$ - $d$ in game.
    i.e., $\theta_\mathrm{64u}$ is the angle displayed in game when building a curve with 1 bend and the shorter one of the two arms of the curve is at least 64u (512m).
  - Source: (2024-08-17) [Wikipedia](https://en.wikipedia.org/wiki/Grade_(slope)#Roads): US
  - Source: (2024-08-17) [Wikipedia](https://en.wikipedia.org/wiki/International_E-road_network#Road_design_standards): EU
    - According to the source,
      $R \geq 1000 \mathrm{m}$ for $v_\mathrm{max} \simeq 140 \mathrm{km/h}$; and
      $R \geq  120 \mathrm{m}$ for $v_\mathrm{max} \simeq  60 \mathrm{km/h}$.
    - ~~Assuming the Curve radius limit $R \propto v_\mathrm{max}^2$,
      i.e. $R \approx v_\mathrm{max}^2 / (30 \mathrm{mh/km})$ for lower  limit,
      and  $R \approx v_\mathrm{max}^2 / (20 \mathrm{mh/km})$ for higher limit~~.
  - Source: (2024-08-23) [Xin et al. (2021)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0256301): for $R$
    - [figure 8](https://doi.org/10.1371/journal.pone.0256301.g008): Predictions of speed thresholds of the truck in a sharp turn

#### Stratoj

> Streets

Stratoj here generally refers to roads with pedestrian access (i.e. sidewalks),
regardless of it being a road or a street.

Arterial / Collector / Local Roads:

- Gradient  limit:
  (Arbitrarily set to:)

  |             | max Gradient $s$ | Speed limit $v_\mathrm{max}$ | Notes |
  | ----------- | :-------: | :-------: | ----------- |
  | Recommended |  10  \%   |  65 km/h  | `St-Dt` Distributor (2+ Ŭ lanes per direction, No parking, No zoning, tram tracks in the middle)   |
  |||||
  | Recommended |  15  \%   |  45 km/h  | `St-Ĉf` Local roads (Main or Low Ped Activity, tram tracks on the sides) |
  | Recommended |  20  \%\* |  35 km/h  | `St-Lk` Local roads (High Ped Activity) |
  | Hard Limit  |  30  \%\* |  20 km/h  | `St-Lk` Local roads |
  |||||
  | Recommended |  30  \%\* |  10 km/h  | `St-H`  Pedestrian Roads |

  \* Note that vanilla game by default only allow up to $20 \%$ gradient.

- Regarding Speed limits,
  See also:
  - [Units](Unuoj.md#rapido) page;
  - (2025-01-26) [Hussain et al. (2019)](https://doi.org/10.1016/j.aap.2019.05.033) Meta-analysis on pedestrian fatality vs vehicle speed.
- Parking:
  - Default **Price**:
    - Cars: `O$32` per day/month per spot.
    - Motorcycles: `O$16` per day/month per spot.
    - Bicycles: Free.
  - Price can be higher
    near high density transit centers
    or wherever deemed necessary.
    No limit has been set on the maximum price.
  - Default **Restrictions** near residential areas:
    - *Maximum* 1 spot per 1u2 (1 grid cell) ground footprint,
      *regardless of builing height or density*.
    - In medium/high density zones, most parking space should be *accessible*,
      since they are expected to be used mostly by the disabled,
      who enjoys subsidies for the parking space costs-
      even though few of them live on the island.

#### Biciklovojoj

> Bike paths

- TBD

#### Piedvojoj

> Pedestrian paths

- TBD

### Reloj

> Rails

#### Kargaj kaj malnovaj personaj fervojoj

> Cargo and old passenger railways

- Gradient $s$ and Curve radius $R$ limit:

  |             | max Gradient $s$ | min Curve radius $R$ | Speed limit $v_\mathrm{max}$ | $\theta_\mathrm{64u}$ | $\theta_\mathrm{32u}$ | $\theta_\mathrm{16u}$ | $\theta_\mathrm{8u}$ | Real world examples |
  | ----------- | :--------------: | :------------------: | :--------------------------: | --- | --- | --- | --- | ------------------- |
  | Recommended |  1.5 \%  | 1024m (128u) |  180 km/h  | $127\degree$ | $152\degree$ | $166\degree$ | $173\degree$ | (Note: 200km/h for passenger trains; 135km/h for cargo trains) |
  | -           |  1.5 \%  |  576m (72u)   |  135 km/h  |  $97\degree$ | $133\degree$ | $155\degree$ | $168\degree$ | |
  | Hard Limit  |  3.5 \%  |  144m  (18u)  |   65 km/h  | -            | -            |  $97\degree$ | $133\degree$ | Lithgow Zig Zag |

  - $\theta_{d}$ refers to the angle displayed when building a 2-phase curve of $d$ - $d$ in game.
    i.e., $\theta_\mathrm{64u}$ is the angle displayed in game when building a curve with 1 bend and the shorter one of the two arms of the curve is at least 64u.
  - Curve radius is obtained by $R \propto v_\mathrm{max}^2$ (See [Wikipedia](https://en.wikipedia.org/wiki/Minimum_railway_curve_radius#Speed_and_cant).)
  - Assuming tilting trains.
  - Source: (2024-08-16) [Wikipedia](https://en.wikipedia.org/wiki/Minimum_railway_curve_radius#Speed_and_cant): $R$ info
  - Source: (2024-08-16) [Wikipedia](https://en.wikipedia.org/wiki/Minimum_railway_curve_radius#List_of_selected_minimum_curve_radii): $R$ examples (see Lithgow Zig Zag)
  - Source: (2024-08-16) [Wikipedia](https://en.wikipedia.org/wiki/List_of_steepest_gradients_on_adhesion_railways#): $s$ examples
  - Note: Liberties have been taken for the hard limit of $s$ due to steep terrain in the map. Also steeper is more fun.
- Length / Power
  - train length: 25 (16m/2u-long) cars (**400m/50u**): 1 engine + 24 trailers.
  - For track intersections: $\geq$ 448m/56u.

#### Altrapidaj fervojoj

> High-speed railways

- Gradient $s$ and Curve radius $R$ limit:

  |             | max Gradient $s$ | min Curve radius $R$ | Speed limit $v_\mathrm{max}$ | $\theta_\mathrm{64u}$ | $\theta_\mathrm{32u}$ | $\theta_\mathrm{16u}$ | $\theta_\mathrm{8u}$ | Real world examples |
  | ----------- | :------: | :------------: | :--------: | --- | --- | --- | --- | ------------------- |
  | -           |  1.2 \%  |  7000m (875u)  |  400 km/h  | $172\degree$ | $176\degree$ | $178\degree$ | $179\degree$ | |
  | Recommended |  1.7 \%  |  5700m (712u)  |  360 km/h  | $170\degree$ | $175\degree$ | $178\degree$ | $179\degree$ | |
  | Soft Limit  |  2.2 \%  |  4480m (560u)  |  320 km/h  | $167\degree$ | $174\degree$ | $177\degree$ | $179\degree$ | |
  | -           |  2.7 \%  |  3440m (430u)  |  280 km/h  | -            | -            | -            | -            | |
  | Hard Limit  |  3.4 \%  |  2520m (315u)  |  240 km/h  | $158\degree$ | $169\degree$ | $175\degree$ | $178\degree$ | |
  | -           |  4.2 \%  |  1760m (220u)  |  200 km/h  | -            | -            | -            | -            | |

  - Source: (2024-08-16) [Wikipedia](https://en.wikipedia.org/wiki/List_of_steepest_gradients_on_adhesion_railways#): $s$ examples
  - Source: (2024-08-16) [Wikipedia](https://en.wikipedia.org/wiki/Minimum_railway_curve_radius#List_of_selected_minimum_curve_radii): $R$ examples
- Length / Power
  - Assumed EMU (Electric Multiple Unit).
  - Train length
    <!-- - 12 (20m/2.5u-long) train cars (**240m/30u**). -->
    - 16 (24m/3.0u-long) train cars (**384m/48u**)
    - 20 (20m/2.5u-long) train cars (**400m/50u**)
    - 25 (16m/2.0u-long) train cars (**400m/50u**)
    - Half length permitted
  - For track intersections: $\geq$ 448m/56u.
  - Assumed power consumption:
  1600hp/1.2MW per (24m/3u-long) train car - 19.2MW for a full length train.

#### Metrooj / personaj fervojoj

> Metro / subway / passenger railways

- Gradient $s$ and Curve radius $R$ limit:

  |             | max Gradient $s$ | min Curve radius $R$  | Speed limit $v_\mathrm{max}$ | $\theta_\mathrm{64u}$ | $\theta_\mathrm{32u}$ | $\theta_\mathrm{16u}$ | $\theta_\mathrm{8u}$ | Real world examples |
  | ----------- | :--------------: | :------------------------: | :----------------------------: | --- | --- | --- | --- | ------------------- |
  | -           |  3.5 \%  | 1024m (128u) |  180 km/h  | $127\degree$ | $152\degree$ | $166\degree$ | $173\degree$ | (Note: overhead-wire-powered tracks only (No third rail metro tracks)) |
  | Recommended |  5   \%  |  576m (72u)  |  135 km/h  | $97\degree$ | $133\degree$ | $155\degree$ | $168\degree$ | ($s$) Höllentalbahn (Black Forest), Germany;  <br>($R$) Assuming tilting trains. |
  | Hard Limit  |  7   \%  |  320m (40u)  |  100 km/h  | -                 | $103\degree$ | $137\degree$  | $158\degree$ | ($s$) Bernina Railway, Switzerland;  <br>($R$) Bay Area Rapid Transit, United States. |

  - Assuming tilting trains: see [Wikipedia](https://en.wikipedia.org/wiki/Minimum_railway_curve_radius#Speed_and_cant).
  - Note: curve radius restrictions may be relaxed when exiting / entering stations where speed is slow.
  - Source: (2024-08-16) [Wikipedia](https://en.wikipedia.org/wiki/List_of_steepest_gradients_on_adhesion_railways#): $s$ examples
  - Source: (2024-08-17) [Wikipedia](https://en.wikipedia.org/wiki/Minimum_railway_curve_radius#List_of_selected_minimum_curve_radii): $R$ examples
    - Note: $R$ can go as low as 64m (8u) as seen in Central line, London Underground, United Kingdom; but that's probably too tight.
  - Source: (2024-08-27) [Wikipedia](https://en.wikipedia.org/wiki/Minimum_railway_curve_radius#Speed_and_cant): $R$ info.
- Length / Power
  - Assumed EMU (Electric Multiple Unit).
  - Train length
    <!-- - 12 (20m/2.5u-long) train cars (**240m/30u**). -->
    - 8  (24m/3.0u-long) train cars (**192m/24u**)
    - 10 (20m/2.5u-long) train cars (**200m/25u**)
    - 12 (16m/2.0u-long) train cars (**192m/24u**)
    - Half length permitted
  - For track intersections: $\geq$ 240m/30u.
  - Assumed power consumption:
    1200hp/0.9MW per (24m/3u-long) train car - 7.2MW for a full length train.
- Additional Notes
  - Due to proper designs,
    metros in OmniCentro are capable of (and generally are) running 24/7:
    The wide separation of the tracks
    (track center separation $\geq$ 6m for overhead-wire-powered systems;
    $\geq$ 7m for third-rail-powered systems)
    allows maintenance to be done for one side of the dual tracks at night,
    while the night metro running on the other at a reduced frequency.
    Sides alternate each night.
    This is much akin to the real life
    [Copenhagen Metro](https://en.wikipedia.org/wiki/Copenhagen_Metro)
    (2025-02-04).

#### Tramoj

> Trams

- Gradient $s$ limit:

  |             | max Gradient $s$ | min Curve radius $R$ (without slowing)  | Speed limit $v_\mathrm{max}$ | Real world examples |
  | ----------- | :--------------: | :--------------: | :--------------------------: | ------------------- |
  | -           |   8   \%  |  448m (56u)  | 100 km/h  | |
  | Recommended |  10   \%  |  288m (36u)  |  80 km/h  | Sheffield Supertram, Sheffield |
  | -           |  12.5 \%  |  192m (24u)  |  65 km/h  | Lisbon Tramways, Portugal |
  | Hard Limit  |  18   \%  |   96m (12u)  |  45 km/h  | |

  - Note: Faster than 65 km/h speed can only be achieved on separated tracks.
  - Curve radius limit here can be ignored, as trams slow down near intersections.
    It is larger than metro when speed is fast,
    because tram tracks are assumed to be non-tilting.
  - 13.8% is about as steep as real-life trams go,
    but why not go even steeper?
    It's a game afterall-
    and RdO enjoys technological superiority by lore anyway.
  - Source: (2024-08-16) [Wikipedia](https://en.wikipedia.org/wiki/List_of_steepest_gradients_on_adhesion_railways#): $s$ examples
- Length / Power
  - Assumed EMU (Electric Multiple Unit).
  - Assuming non-tilting trains.
  - Assumed power consumption: 800hp/0.6MW per (16m/2u-long) train car.

#### Monoreloj

> Monorails

- Gradient $s$ and Curve radius $R$ limit:

|             | max Gradient $s$ | min Curve radius $R$  | Speed limit $v_\mathrm{max}$ | $\theta_\mathrm{64u}$ | $\theta_\mathrm{32u}$ | $\theta_\mathrm{16u}$ | $\theta_\mathrm{8u}$ | Real world examples |
| ----------- | :--------------: | :------------------------: | :----------------------------: | --- | --- | --- | --- | ------------------- |
| Recommended |  10  \%  |  TBD                     |  80 km/h  | -                 | -                 | -                 | -                 | TBD               |
| Hard Limit  |  12  \%  |  TBD                     |  70 km/h  | -                 | -                 | -                 | -                 | TBD               |

- Source: (2024-09-28) [Miller et al. (2014)](https://www.researchgate.net/publication/301302321_Monorails_for_sustainable_transportation_-_a_review)
  - Table 4.1 $s$ info (Multiplied by 2 since its estimated values seems too conservative in general- see above; same as the speed limit $v_\mathrm{max}$. Also it's a game and steeper/faster is more fun.)

### Networks specification details and verification

> For nerds (like me) only.

#### Angle $\theta_{d}$ equation

$\theta_{d} = 2 \tan^{-1}{\frac{R}{d}}$

```python
    # python code
    import numpy as np
    # Remember to translate radian into degree
    theta_deg = lambda R, d: np.ceil(2*np.atan(R/d)/np.pi*180)
    get_R = lambda theta_deg, d: np.tan(theta_deg/2/180*np.pi)*d
    # Example
    print([(d, theta_deg(R=720, d=d)) for d in (512, 256, 128, 64)])
    print(theta_deg(R=4000, d=512), get_R(theta_deg=166, d=512))
```

#### Analysis of train/truck engine's ability to haul cars

See my python code [here](Retoj.py).
