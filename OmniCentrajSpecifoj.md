<!-- -*- coding: utf-8 -*- -->

OmniCentraj Specifoj  
OmniCentro Specifications
===============================================================================

-------------------------------------------------------------------------------

Background stories and technical specifications
for my upcoming fictional Cities: Skylines 2 city *OmniCentro*.

PDX Mod Link: ***TBD***


Malgarantio  
Disclaimer
-------------------------------------------------------------------------------

This is ***a work of fiction***.
Names, characters, businesses, places, events and incidents
are either the products of the author's imagination
or used in a fictitious manner.
Any resemblance to actual persons, living or dead, or actual events
is purely coincidental.

This work © 2024 by \_HomeOnMars\_ is licensed under CC BY-NC-SA 4.0.
To view a copy of this license, visit https://creativecommons.org/licenses/by-nc-sa/4.0/

-------------------------------------------------------------------------------









Detalaj Informoj  
Detailed Information
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------

***Again, everything here is fictional.***




### Bulletin

-------------------------------------------------------------------------------


#### Summary

| Settings          |  Acronym | Name                |
| :---------------- | :------: | :-----------------: |
| City Name         | OC   | OmniCentro              |
| Country Name      | RdO  | Regno de Omnijo         |
| Government Name   | OCR  | Omnija Centra Registaro |
| Local Authority   | OCG  | OmniCentra    Gvidado   |

| [Fictional] Background | Name |
| :---------------- | ---- |
| City Background   | Planned New Capital |
| Official Language | Esperanto (transitioning from English in the next 20 years) |
| Country Leader    | Reĝino Serena de Omnijo |
| City Designers    | Ĉuĉjo la Arkitekto  kaj  Ĝejnjo la Suverenino |


#### Government Structure (Part)

| Departments                  |  Acronym | Name |
| ---------------------------- | :------: | ---- |
| Department of Defence        | OCFD | Omnija Centra Fako de Defendo |
| Department of Education      | OCFE | Omnija Centra Fako de Edukado |
| Department of Fire and Rescue| OCFF | Omnija Centra Fako de Fajro kaj Savo |
| Department of Infrastructure | OCFI | Omnija Centra Fako de Infrastrukturo |
| Department of Police         | OCFP | Omnija Centra Fako de Polico  |
| Department of Health         | OCFS | Omnija Centra Fako de Sano    |

| Offices                      |  Acronym | Name |
| ---------------------------- | :------: | ---- |
| Office of Finance            | OCOF | Omnija Centra Oficejo de Fisko |
| Office of Foreign Affairs    | OCOE | Omnija Centra Oficejo de Eksteraj Aferoj |
| Office of Home    Affairs    | OCOI | Omnija Centra Oficejo de Internaj Aferoj |


#### Single letter abbreviations

| Acronym | Esperanto     | English  |
| ------- | ------------- | -------- |
|    N    | **N**orda     | Northern |
|    S    | **S**uda      | Southern |
|    R    | o**R**ienta   | Eastern  |
|    K    | o**K**cidenta | Western  |
|    L    | **L**iva      | Left     |
|    C    | **C**entra    | Center   |
|    D    | **D**ekstra   | Right    |
|    P    | **P**lus / Maldekstruma / S->N / K->R | Plus / Counterclockwise / S->N / W->E |
|    M    | **M**inus / Dekstruma / N->S / R->K   | Minus /       Clockwise / N->S / E->W |









Teknikaj specifoj  
Technical Specifications
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------

***Warning:
Information here is gathered from the internet for gameplay purposes,
so not much effort has been spent on ensuring its accuracy.
Some maybe incorrect or outdated.
Some are just chosen arbitrarily.
Use at your own risk.***




### Networks

-------------------------------------------------------------------------------


#### Roads

- Highways
  - Gradient $ s $ and Curvature $ R $ limit:
    
    |             | Gradient $ s $    | Curvature $ R $            | Speed limit $ v_\mathrm{max} $ | $ \theta_\mathrm{512m} $ | $ \theta_\mathrm{256m} $ | $ \theta_\mathrm{128m} $ | $ \theta_\mathrm{64m} $ | Notes |
    | ----------- | :---------------: | :------------------------: | :----------------------------: | --- | --- | --- | --- | ----- |
    | Soft Limit  |  $ \leq  4  \% $  |  $ \geq  720 \mathrm{m} $  |  $ \simeq 120 \mathrm{km/h} $  | $ \geq 110\degree $ | $ \geq 141\degree $ | $ \geq 160\degree $ | $ \geq 170\degree $ | |
    | Recommended |  $ \leq  6  \% $  |  $ \geq  400 \mathrm{m} $  |  $ \simeq 100 \mathrm{km/h} $  | -                   | $ \geq 115\degree $ | $ \geq 145\degree $ | $ \geq 162\degree $ | |
    | Soft Limit  |  $ \leq  8  \% $  |  $ \geq  216 \mathrm{m} $  |  $ \simeq  80 \mathrm{km/h} $  | -                   | -                   | $ \geq 119\degree $ | $ \geq 147\degree $ | For ramps / In mountains |
    | Mandatory   |  $ \leq 10  \% $  |  $ \geq  128 \mathrm{m} $  |  $ \simeq  60 \mathrm{km/h} $  | -                   | -                   | -                     | $ \geq 124\degree $ | For ramps / In mountains |
    
    - $ \theta_{d} $ refers to the angle displayed when building a 2-phases curve of $d$ - $d$ in game.
      i.e., $ \theta_\mathrm{512m} $ is the angle displayed in game when building a curve with 1 bend and both radius being 512m and 512m.
    - Source: [2024-08-17] (US) https://en.wikipedia.org/wiki/Grade_(slope)#Roads
    - Source: [2024-08-17] (EU) https://en.wikipedia.org/wiki/International_E-road_network#Road_design_standards
      - According to the source,
        $ R \geq 1000 \mathrm{m} $ for $ v_\mathrm{max} \simeq 140 \mathrm{km/h} $; and
        $ R \geq  120 \mathrm{m} $ for $ v_\mathrm{max} \simeq  60 \mathrm{km/h} $.
      - Assuming the curvature limit $ R \propto v_\mathrm{max}^2 $,
        i.e. $ R \approx v_\mathrm{max}^2 / (30 \mathrm{mh/km}) $ for lower  limit,
        and  $ R \approx v_\mathrm{max}^2 / (20 \mathrm{mh/km}) $ for higher limit.
- Arterial / Collector / Local Roads
  - Gradient  limit:
    (Arbitrarily set to:)
    
    |             | Gradient $ s $    | Curvature $ R $            | Speed limit $ v_\mathrm{max} $ | Notes |
    | ----------- | :---------------: | :------------------------: | :----------------------------: | ----- |
    | Recommended |  $ \leq 10  \% $  |  -                         |  $ \simeq  60 \mathrm{km/h} $  | Arterial |
    | Mandatory   |  $ \leq 36  \% $  |  -                         |  $ \simeq  25 \mathrm{km/h} $  | Local roads |
    
- Bike paths
  - TBD
- Ped  paths
  - TBD


#### Rails

- Freight and old Passenger Railways
  - Gradient $ s $ and Curvature $ R $ limit:
    
    |             | Gradient $ s $    | Curvature $ R $            | Speed limit $ v_\mathrm{max} $ | $ \theta_\mathrm{512m} $ | $ \theta_\mathrm{256m} $ | $ \theta_\mathrm{128m} $ | $ \theta_\mathrm{64m} $ | Real world examples |
    | ----------- | :---------------: | :------------------------: | :----------------------------: | --- | --- | --- | --- | ------------------- |
    | Recommended |  $ \leq  1.5\% $  |  $ \geq  640 \mathrm{m} $  |  $ \simeq 120 \mathrm{km/h} $  | $ \geq 103\degree $ | $ \geq 137\degree $ | $ \geq 158\degree $ | $ \geq 169\degree $ | |
    | Mandatory   |  $ \leq  3.5\% $  |  $ \geq  160 \mathrm{m} $  |  $ \simeq  40 \mathrm{km/h} $  | -                   | -                   | $ \geq 103\degree $ | $ \geq 137\degree $ | Lithgow Zig Zag |
    
    - $ \theta_{d} $ refers to the angle displayed when building a 2-phases curve of $d$ - $d$ in game.
      i.e., $ \theta_\mathrm{512m} $ is the angle displayed in game when building a curve with 1 bend and both radius being 512m and 512m.
    - Angle $ \theta_{d} $ equation:
      $ \theta_{d} = 2 \tan^{-1}{\frac{R}{d}} $
      ```
          # python code
          import numpy as np
          # Remember to translate radian into degree
          theta_deg = lambda R, d: np.ceil(2*np.atan(R/d)/np.pi*180)
          # Example
          print([(d, theta_deg(R=720, d=d)) for d in (512, 256, 128, 64)])
          print(theta_deg(R=4000, d=512))
      ```
    - Source: [2024-08-16] ($ R $) https://en.wikipedia.org/wiki/Minimum_railway_curve_radius#Speed_and_cant
    - Source: [2024-08-16] ($ R $) https://en.wikipedia.org/wiki/Minimum_railway_curve_radius#List_of_selected_minimum_curve_radii (Lithgow Zig Zag)
    - Source: [2024-08-16] ($ s $) https://en.wikipedia.org/wiki/List_of_steepest_gradients_on_adhesion_railways#
    - Note: Liberties have been taken for the mandatory limit of $s$ due to steep terrain in the map. Also steeper is more fun.
  - Length limit (for track intersections): $ > 500\mathrm{m} $ (25 cars with 20m per car)
- High Speed Railways
  - Gradient $ s $ and Curvature $ R $ limit:
    
    |             | Gradient $ s $    | Curvature $ R $            | Speed limit $ v_\mathrm{max} $ | $ \theta_\mathrm{512m} $ | $ \theta_\mathrm{256m} $ | $ \theta_\mathrm{128m} $ | $ \theta_\mathrm{64m} $ | Real world examples |
    | ----------- | :---------------: | :------------------------: | :----------------------------: | --- | --- | --- | --- | ------------------- |
    | Recommended |  $ \leq  3.5\% $  |  $ \geq 4000 \mathrm{m} $  |  $ \simeq 300 \mathrm{km/h} $  | $ \geq 166\degree $ | $ \geq 173\degree $ | $ \geq 177\degree $ | $ \geq 179\degree $ | |
    | Mandatory   |  $ \leq  4  \% $  |  $ \geq 3500 \mathrm{m} $  |  $ \simeq 250 \mathrm{km/h} $  | $ \geq 164\degree $ | $ \geq 172\degree $ | $ \geq 176\degree $ | $ \geq 178\degree $ | |
    
    - Source: [2024-08-16] https://en.wikipedia.org/wiki/List_of_steepest_gradients_on_adhesion_railways#
    - Source: [2024-08-16] https://en.wikipedia.org/wiki/Minimum_railway_curve_radius#List_of_selected_minimum_curve_radii
- Metro / Subway / Passenger Railways
  - Gradient $ s $ and Curvature $ R $ limit:
    
    |             | Gradient $ s $    | Curvature $ R $            | Speed limit $ v_\mathrm{max} $ | $ \theta_\mathrm{512m} $ | $ \theta_\mathrm{256m} $ | $ \theta_\mathrm{128m} $ | $ \theta_\mathrm{64m} $ | Real world examples |
    | ----------- | :---------------: | :------------------------: | :----------------------------: | --- | --- | --- | --- | ------------------- |
    | Recommended |  $ \leq  5.5\% $  |  $ \geq  128 \mathrm{m} $  |  $ \simeq 120 \mathrm{km/h} $  | -                   | -                   | $ \geq   90\degree $  | $ \geq 127\degree $ | [$ s $] Höllentalbahn (Black Forest), Germany;<br>[$ R $] Bay Area Rapid Transit, United States. |
    | Mandatory   |  $ \leq  7  \% $  |  $ \geq   64 \mathrm{m} $  |  $ \simeq 100 \mathrm{km/h} $  | -                   | -                   | -                     | $ \geq  90\degree $ | [$ s $] Bernina Railway, Switzerland;<br>[$ R $] Central line, London Underground, United Kingdom. |
    
  - Source: [2024-08-16] ($ s $) https://en.wikipedia.org/wiki/List_of_steepest_gradients_on_adhesion_railways
  - Source: [2024-08-17] ($ R $) https://en.wikipedia.org/wiki/Minimum_railway_curve_radius#List_of_selected_minimum_curve_radii
- Trams
  - Gradient $ s $ limit:
    
    |             | Gradient $ s $    | Speed limit $ v_\mathrm{max} $ | Real world examples |
    | ----------- | :---------------: | :----------------------------: | ------------------- |
    | Recommended |  $ \leq 10  \% $  |  $ \simeq  90 \mathrm{km/h} $  | Sheffield Supertram, Sheffield |
    | Mandatory   |  $ \leq 13.5\% $  |  $ \simeq  70?\mathrm{km/h} $  | Lisbon Tramways, Portugal |
    
  - Source: [2024-08-16] https://en.wikipedia.org/wiki/List_of_steepest_gradients_on_adhesion_railways#Examples




### Trees

-------------------------------------------------------------------------------


#### Brushes Configuration

- Brush W-D: Altitude  100m to  600m
  - Briches
  - etc.
- Brush   2: Altitude  600m to 1000m
  - Briches
  - Pines
- Brush   1: Altitude 1000m to 1400m
  - Briches
  - Pines
  - Spruces
- Brush E-G: Altitude 1400m to 2500m
  - Pines
  - Spruces
- Brush N/A: Very steep terrain
  - Spruces


#### Species

- Briches
  - Esperanto Name: Betulo
  - Altitude:  600m to 1400m
  - Source: https://www.srs.fs.usda.gov/pubs/misc/ag_654/volume_2/betula/lenta.htm
- Pines
  - Esperanto Name: Pino
  - Altitude: 1100m to 4000m
  - Source: https://research.fs.usda.gov/rmrs/projects/high-elevation-white-pines
- Spruces
  - Esperanto Name: Piceo
  - Altitude: 2000m to 3500m
  - Source: https://csfs.colostate.edu/colorado-trees/colorados-major-tree-species/


#### See Also

- https://en.wikipedia.org/wiki/Tree_line#Tree_species_near_tree_line









Fonaj Rakontoj  
Background Stories
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------

***Again, everything here is fictional.***

(Coming soon.)