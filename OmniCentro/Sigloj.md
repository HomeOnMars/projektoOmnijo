<!-- -*- coding: utf-8 -*- -->

OmniCentraj Specifoj - Sigloj
===============================================================================

> OmniCentro Specifications - Acronyms

Specifications for my fictional Cities: Skylines 2 city *OmniCentro*.

Legal
-------------------------------------------------------------------------------

> [!WARNING]
> This is ***a work of fiction***.
> Names, characters, businesses, places, events and incidents
> are either the products of the author's imagination or used in a fictitious manner.
> Any resemblance to actual persons, living or dead, or actual events is purely coincidental.

<p xmlns:cc="http://creativecommons.org/ns#" >This work by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/HomeOnMars">HomeOnMars</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC-SA 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" alt=""></a></p>

Sigloj
-------------------------------------------------------------------------------

> Acronyms
> <br>
> [Back to OmniCentro Content](../OmniCentro.md#detalaj-informoj)

### Direktoj

> Directions

| Siglo  <br>Acronym | En esperanto  <br>In Esperanto | En la angla  <br>In English |
| :-----: | ------------- | -------- |
|    N    | **N**orda     | Northern |
|    S    | **S**uda      | Southern |
|    R    | o**R**ienta   | Eastern  |
|    K    | o**K**cidenta | Western  |
|    L    | **L**iva      | Left     |
|    C    | **C**entra    | Center   |
|    D    | **D**ekstra   | Right    |
|    P    | **P**lus  / Pozitiva /  <br>Maldekstruma /  <br>S->N / K->R | Plus  / Positive /  <br>Counterclockwise /  <br>S->N / W->E |
|    M    | **M**inus / Negativa /  <br>Dekstruma    /  <br>N->S / R->K | Minus / Negative /  <br>       Clockwise /  <br>N->S / E->W |

Note: P/M follows positive and negative directions in mathematics (thus P for counterclockwise directions).

### Vojoj kaj Stratetoj

> Roads and Lanes

| Siglo  <br>Acronym | Strateta Tipo  <br>(en esperanto) | Lane Type  <br>(in English) | Strateta Larĝeco  <br>Lane Width |
| :-----: | ------------------- | ------------------- | :---------: |
|    H    | **H**omo/Piediranto | Human/Pedestrian    | $\geq$ 3.5m |
|    B    | **B**iciklo         | Bike                |        ?    |
|    J    | parke**J**o         | Parking Space       | $\geq$ 2m   |
|  Ŭ / Ux | a**Ŭ**tomobilo      | Car                 |        3m   |
|    U    | b**U**so            | Bus                 |        3m   |
|    T    | **T**ramo           | Tram                |        3m   |
|    E    | f**E**rvojo/m**E**troo | Railway/Metro    |        4m   |
|    V    | **V**agonaro/Trajno | Train               |        4m   |
|    G    | Neŭtrala **G**rundo  <br>Meza Strio | Neutral Ground  <br>Median Strip | $\geq$ 1m   |
|    O    | l**O**kokupilo      | Placeholder         | -           |
|    i    | **i**nverse         | vice versa          | -           |

De-capitalize for lanes with inverted directions.

Road name format examples:

- HBA2gi
  - pedestrain path (H) - bike (B) - 2 car lanes (A2) - central median (g) - same for the other half of the road (i)
  - Median road with bike
- Ha2Tgi
  - pedestrain path (H) - 2 inverted car lanes (A2) - transit lane (T) - central median (g) - same for the other half (i)
  - Median road for diverging diamond interchanges
- HA3a2h
  - pedestrain path (H) - 3 car lanes (A3) - 2 inverted car lanes (A2) - inverted pedestrain path (h)
  - Asymmetrical median road

See also:

- (2024-09-12) [Road Builder mod](https://mods.paradoxplaza.com/mods/87190/Windows) by TDW

### Publika Transportaj Linioj

> Public Transit Lines

Note that the letters are overlapping other acronyms in other categories - and they are not necessarily the same.

| Siglo  <br>Acronym | Nomo  <br>(en esperanto) | Name  <br>(in English) | Rimarkoj  <br>Remarks |
| :-----: | ------------------- | ------------------- | ----------- |
|    A    | **A**viadilo        | Airplane            | |
|    B    | **B**iciklo         | Bike                | |
|  Ŭ / Ux | a**Ŭ**tovojo        | Motorway            | |
|    U    | b**U**so            | Bus                 | |
|    T    | **T**ramo           | Tram                | Regiona  <br>Regional |
|    E    | f**E**rvojo/m**E**troo | Railway/Metro  <br>Monorail  <br>Train | Malaltrapida \($\leq$  200 km/h\)  <br>Low-speed |
|    V    | **V**agonaro/Trajno | Train               | Altrapida \(\> 200 km/h\)  <br>High-speed |
|    P    | **P**ramo           | Ferry               | Regiona  <br>Regional |
|  Ŝ / Sx | **Ŝ**ipo            | Ship                | |
|    H-   | **H**omo-/Pasaĝero- | Human-/Passenger-   | |
|    K-   | **K**argo-          | Cargo-              | |

> [!NOTE]
>
> 1. H prefix is usually omitted.
> 2. All Line numbers are ***hexadecimal*** (see [ONKIO table](../teknikajxoj/ONKIO.md#onkio-tablo) `0x3_` column for respective symbols of 10~15: `Δ λ Π Σ Υ Ψ`).

Examples:

- Bus route 431 (i.e. 0x1af): `U1ΔΨ` (short for HB1ΔΨ)
- High-speed Train line 3: `V3` (short for HV3)
- Motorway 13 N->S: `ŬΣm` (or `UxDm` for ASCII encoding; m for Negative.)
- Cargo train line 12: `KVΠ`
- Cargo barge route 4: `KP4`
- Cargo container ship route 14: `KŜΥ` (or KSxE for ASCII encoding; Becareful `Υ` is the upper-case version of greek letter `γ`, not English Y.)
- Cargo Airline 5: `KA5`

### Mallongigoj

> Abbreviations

| Mallongigo  <br>Abbreviation | En Epopo  <br>In Epopo | En la angla  <br>In English |
| :-----: | -------------------- | ---------------- |
||| <!-- Major Geological/Engineering Features -->  |
|    Ab   | **A**kvo**b**araĵo   | Dam              |
|    Mt   | **M**on**t**o        | Mountain         |
|    Am   | **A**ntaŭ**m**onto   | Foothill         |
|    Me   | **M**ont**e**to      | Hill             |
|    Lg   | **L**a**g**o         | Lake             |
|    Rv   | **R**i**v**ero       | River            |
|  ~~Mr~~ | **M**a**r**o         | Sea  <br>(Deprecated - Use full form instead) |
||| <!-- District types --> |
|    Dt   | **D**is**t**rikto    | District         |
|    Ia   | **I**ndustri**a**reo | Industrial Area  |
|  ~~Hv~~ | ~~**H**a**v**eno~~   | Port  <br>(Deprecated) |
|   Mhv   | **M**ar**h**aveno    | Seaport          |
|   Fhv   | **F**lug**h**aveno   | Airport          |
|   Khv   | **K**osma**h**aveno  | Space Port       |
|    Vd   | **V**i**d**o         | Vista            |
|    Vĝ   | **V**ila**ĝ**o       | Village          |
||| <!-- Road types --> |
|  ~~Vj~~ | ~~**V**o**j**o~~     | [Road](../teknikajxoj/Retoj.md#vojoj)  <br>(Deprecated[^Deprecated-Vj]) |
|    Ej   | f**E**rvo**j**o      | [Railway](../teknikajxoj/Retoj.md#metrooj--personaj-fervojoj) |
|  Ej-K   | Ej-**K**argo         | [Cargo railway](../teknikajxoj/Retoj.md#kargaj-kaj-malnovaj-personaj-fervojoj) |
|  Ej-AR  | Ej-**A**lt**R**apido | [High-speed railway](../teknikajxoj/Retoj.md#altrapidaj-fervojoj) |
|  Ej-SL  | Ej-**S**upraj**L**inioj | Regular railway (powered by overhead lines) |
|  Ej-TR  | Ej-**T**ria**R**elo  | Subway railway (powered by third rail) |
|  Ej-T   | Ej-**T**ramo         | [Tramway](../teknikajxoj/Retoj.md#tramoj)          |
|    Ŭj   | a**Ŭ**tovo**j**o     | [Motorway](../teknikajxoj/Retoj.md#aŭtovojoj) |
|    St   | **S**tra**t**o       | [Street](../teknikajxoj/Retoj.md#stratoj) |
|  St-Dt  | St-**D**is**t**ribuo | Distributor Roads |
|  St-Ĉf  | St-**Ĉ**e**f**o      | Main  Roads      |
|  St-Lk  | St-**L**o**k**o      | Local Roads      |
|  St-H   | St-**H**omo          | Pedestrian Roads |
||| <!-- Edu types --> |
|    Bl   | **B**az**l**ernejo   | Elementary School |
|    Ml   | **M**ez**l**ernejo   | High School      |
|    Al   | **A**lt**l**ernejo   | College          |
|   Uni   | **Uni**versitato     | University       |
||| <!-- Misc types --> |
|    Ĉf   | **Ĉ**e**f**o         | Main             |
|    Pt   | **P**ar**t**o        | Part, Segment    |
|    v    | **v**ersio           | version          |
|   Skp   | **S**av**k**o**p**io | Backup           |
|    Ŝn   | **Ŝ**anĝo**n**oto    | Changelog        |

[^Deprecated-Vj]: Deprecated.
  Vojo as a concept is too broad,
  as it could mean anything from motorways and rails to alleys and paths.
  Do not use.

Naming rules examples:

- `Ab-O#1` (Good) as a short version  
  of `Ab-Olivkronaĵo #1` (Good),  
  or `Akvobaraĵo-Olivkronaĵo #1` (Meh),  
  or `Olivkronaĵa Akvobaraĵo #1` (Good);
- `Mt-O` (Good) as a short version  
  of `Mt-Olivkronaĵo` (Good),  
  or `Monto-Olivkronaĵo` (Good),  
  or `Olivkronaĵa Monto` (Meh);
- `Ŭj#Σm` for Motorway 13 N->S `ŬΣm`,  
  or `Aŭtovojo #Σm`;
- `St-Olivkronaĵo #123` as a short version  
  of `Olivkronaĵa Strato #123`,  
  or `123 Olivkronaĵo St`;
- `Stacidomo #E` and `Stacidomo #U` for train and bus station respectively;

### Distrikto Numerada Sistemo

> District Numbering System

Using the leading digit for identifying districts and areas:

| Areo Numero | Proksimuma Loko | Siglo | Plena Nomo | Koloro |
| --- | ---- | ----- | ----- | -------------- |
| `0` |      |       | Interdistrikto (sen eksteraj konektoj)  <br>Interdistrict (no outside connections) | <span style="color:Tan">█ #D2B48C</span> |
| `1` |  SK  | Vĝ-P  | Vilaĝo-Pioniro | |
| `2` |  SC  | Am-H  | Am-Hejmecaĵo   | |
| `3` |  SR  | Mt-O  | Mt-Olivkronaĵo | <span style="color:DarkSeaGreen">█ #8FBC8F</span> |
| ... |      |       |                | |
| `Ψ` |      |       | Eksteraj Konektoj  <br>Outside connections | |
| ... |      |       |                | |
| TBD |  SK  | Mt-K  | Mt-Kuraĝecaĵo  | <span style="color:Red">█ #FF0000</span> |
| TBD |  CC  | Mt-H  | Mt-Hejmecaĵo   | |
| TBD |  CR  | Mt-E  | Mt-Esperecaĵo  | <span style="color:Beige">█ #F5F5DC</span> |
| TBD |  NR  | Mt-R  | Mt-Raciecaĵo   | <span style="color:DeepSkyBlue">█ #00BFFF</span> |
| TBD |  NK  | Mt-F  | Mt-Fortikecaĵo | <span style="color:MediumPurple">█ #9370DB</span> |
| TBD |  NC  | Mt-U  | Mt-Unukornaĵo  | <span style="color:Thistle">█ #D8BFD8</span> |
| N/A |  NC  | Mt-A  | Mt-Asteriaĵo   | |

### Konstruaj Nomoj

> Building names (translation lookup table)

| En esperanto  <br>In Esperanto | En la angla  <br>In English |
| ------------------------ | ------------------------ |
| Buso-Korto               | Bus Depot                |
| Fervojo-Korto            | Rail Yard                |
| Metroo-Korto             | Subway Yard              |
| Tramo-Korto              | Tram Depot               |
| Stacidomo                | Train Station            |
|||
| Bazlernejo / ***Bl***    | Elementary School        |
| Mezlernejo / ***Ml***    | High School / Middle School |
| Altlernejo / ***Al***    | College / Higher Education  |
| Universitato / ***Uni*** | University               |
|||
| Policejo                 | Police Station           |
| Fajrobrigado             | Fire Station/Brigade/Department |
| Bunkro                   | Shelter                  |
| Kliniko                  | Clinic                   |
| Hospitalo                | Hospital                 |
| Tombejo                  | Cemetery                 |
| Bio-Reciklada Fabrikejo  <br>Kremaciejo | Bio-Recycling Plant  <br>Crematorium |
| Rubodeponejo             | Landfill                 |
| Reciklada Fabrikejo      | Recycling Plant          |
|||
| Minejo                   | Mine                     |
| \- Ŝtono                 | \- Stone                 |
| \- Karbo                 | \- Coal                  |
| \- Erco                  | \- Ore                   |
|||
| Transformilejo           | Transformer station      |
| Akumulatorejo            | (Emergency) Battery Station |
| Akvobaraĵo               | Dam                      |

References:

- School system: <https://esperanto.stackexchange.com/questions/6199/middle-school-vs-high-school>
