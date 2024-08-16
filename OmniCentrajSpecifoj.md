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



### Bulletin

-------------------------------------------------------------------------------


#### Summary

(Again, everything here is fictional.)

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
| City Designers    | Ĉuĉjo la Arkitekto  kaj  Ĝejnjo la Suvereno |


#### Government Structure (Part)

| Departments                  |  Acronym | Name |
| ---------------------------- | :------: | ---- |
| Department of Defence        | OCFD | OmniCentra Fako de Defendo |
| Department of Education      | OCFE | OmniCentra Fako de Edukado |
| Department of Fire and Rescue| OCFF | OmniCentra Fako de Fajro kaj Savo |
| Department of Infrastructure | OCFI | OmniCentra Fako de Infrastrukturo |
| Department of Police         | OCFP | OmniCentra Fako de Polico  |
| Department of Health         | OCFS | OmniCentra Fako de Sano    |

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



### Networks

-------------------------------------------------------------------------------


#### Roads

TBD.


#### Rails

- Freight and old Passenger Railways
  - Gradient  limit:
    - [Recommended] $ \leq 1.5\% $.
    - [Mandatory] $ < 3.5\% $ (liberties have been taken due to steep terrain in the map- also it's more fun).
    - Source: [2024-08-16] https://en.wikipedia.org/wiki/List_of_steepest_gradients_on_adhesion_railways#
  - Curvature limit:
    - [Recommended] $ \geq 640 \mathrm{m} $.
      - This translates to a curve of (512m, 512m, $ \geq 102.7\deg $).
      - ... or a curve of (256m, 256m, $ \geq 136.4\deg $).
      - ... or a curve of (128m, 128m, $ \geq 157.4\deg $).
      - ... or a curve of (640m, 640m, $  =   90.0\deg $).
      - Supporting $ v_\mathrm{max} \simeq 120 \mathrm{km/h} $.
      - Source: [2024-08-16] https://en.wikipedia.org/wiki/Minimum_railway_curve_radius#Speed_and_cant
    - [Mandatory] $ \geq 160 \mathrm{m} $.
      - This translates to a curve of (512m, 512m, $ \geq 34.8\deg $).
      - ... or a curve of (256m, 256m, $ \geq 64.1\deg $).
      - ... or a curve of (128m, 128m, $ \geq 102.7\deg $).
      - ... or a curve of ( 64m,  64m, $ \geq 136.4\deg $).
      - ... or a curve of (160m, 160m, $  =   90.0\deg $).
      - Supporting $ v_\mathrm{max} \simeq 40 \mathrm{km/h} $.
      - Source: [2024-08-16] https://en.wikipedia.org/wiki/Minimum_railway_curve_radius#List_of_selected_minimum_curve_radii
        (Lithgow Zig Zag)
  - Speed limit: [TBD]
- High Speed Railways
  - Gradient  limit:
    - [Recommended] $ \leq 3.5\% $;
    - [Mandatory] $ < 4\% $.
    - Source: [2024-08-16] https://en.wikipedia.org/wiki/List_of_steepest_gradients_on_adhesion_railways#
  - Curvature limit:
    - [Recommended] $ \geq 4000 \mathrm{m} $.
      - This translates to a curve of (512m, 512m, $ \geq 165.5\deg $).
      - Supporting $ v_\mathrm{max} \simeq 300 \mathrm{km/h} $.
    - [Mandatory] $ \geq 3500 \mathrm{m} $ (Except near stations).
      - This translates to a curve of (512m, 512m, $ \geq 163.4\deg $).
      <!--- Angle equation: 2*np.atan(3500/512)/np.pi*180 --->
      - Supporting $ v_\mathrm{max} \simeq 250 \mathrm{km/h} $.
    - Source: [2024-08-16] https://en.wikipedia.org/wiki/Minimum_railway_curve_radius#List_of_selected_minimum_curve_radii
  - Speed limit: $ 300 \mathrm{km/h} $
- Metro / Subway / Passenger Railways
  - Gradient  limit:
    - [Recommended] $ \leq 5.5\% $.
    - [Mandatory] $ < 7\% $.
    - Source: [2024-08-16] https://en.wikipedia.org/wiki/List_of_steepest_gradients_on_adhesion_railways
      (Höllentalbahn (Black Forest), Germany; Bernina Railway, Switzerland.)
  - Curvature limit:
    - TBD.
  - Speed limit: $ 100 \mathrm{km/h} $
- Trams
  - Gradient  limit:
    - [Recommended] $ \leq 10\% $.
    - [Mandatory] $ < 13.5\% $.
  - Speed limit: $ 90 \mathrm{km/h} $
  - Source: [2024-08-16] https://en.wikipedia.org/wiki/List_of_steepest_gradients_on_adhesion_railways#Examples
    (Sheffield Supertram, Sheffield, England; Lisbon Tramways, Portugal.)




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

(Coming soon.)