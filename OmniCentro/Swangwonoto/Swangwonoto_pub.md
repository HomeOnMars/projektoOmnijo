Ŝanĝonoto - Publika Versio
===============================================================================

> Changelog - Public Version

<!-- markdownlint-disable-next-line no-inline-html line-length -->
<p xmlns:cc="http://creativecommons.org/ns#" >This work by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/HomeOnMars">HomeOnMars</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></a></p>

Content
-------------------------------------------------------------------------------

### v3.0 <-- v2.0 | `2025-06-21`

> Northern Solstice update.  
>
> Infrastructure expansions of rails, roads, and 7 more dams.

- `Meta::GameVer`: v1.3.3f1;
- `Mods::Required`:
  - 'Anarchy' (74604);
  - 'Plop the Growables' (75826);
  - 'Road Builder' (87190);
- `Mods::Optional`:
  - 'Better Bulldozer' (75250);
  - 'Carto' (87428);
  - 'Map Texture Replacer' (76050);
    - 'Alpine Theme' (76828);
    - 'Volchoria Map Theme' (76896);
  - 'Move It' (74324);
  - 'Recolor' (84638);
  - 'Skyve' (75804);
  - 'Traffic' (80095);
  - 'Transport Policy Adjuster' (78622);
  - 'Tree Controller' (75993);
  - 'Water Features' (75613);
- `Expansion::Services`,`District::Ab-Racieco`,`Fixes`:
  - Expanded Ab-R Dams power connections;
- `Expansion::Services`,
  `District::(Mt-Kuraĝo,Mt-Hejmeco,Is-Niksino,Mt-Espero)`:
  7 more dams:
  - Added the 'Mt-Kuraĝo Akvobaraĵo #0' (Ab-K#0) Dam;
  - Added the 'Mt-Hejmeco Akvobaraĵo #0' (Ab-H#0) Dam;
  - Added the 'Bs-Niksina Akvobaraĵo' Dams (Ab-N#0, Ab-N#1),
    creating the 'Baseno-Niksinaĵo' ('Mermaid Reservoir');
  - Added the 'Mt-Espero Akvobaraĵo' Dams (Ab-E#0, Ab-E#1);
  - Built 'Mt-Hejmecaĵa Defluejo' spillway,
    with a small dam built-in (Ab-H#D);
- `Expansion::Rail`:
  - Expanded and retrofitted high speed rail tracks:
    Now have 2 sets of high speed rail tracks,
    Designed for speed limit of 350kph and 220kph respectively;
  - Expanded cargo rail network;
  - Added a railyard in Vd-O;
  - Added 2 fancy new bridges from the recent free update;
-`Expansion::Road`:
  - Added dams access roads;
  - Added Bus/Tram-only roads in Mt-H, Mt-E, and over the reservoir of Ab-O;
  - Added a highway service interchange at Me-H;
  - Updated the bridge at the main water outlet
    (the lake in between Vĝ-P and Am-H);
  - Updated highways from Vanilla to 'Ŭj-7' (part);
- `District::Vd-Fortikeco`,`Expansion::Zoning`:
  - Built 'La Kora Tenero' Villa;
- `District::La-Pordego`,`Expansion::Services`:
  - Added
    a recycling plant,
    a wastewater treatment plant, and
    a bus depot;
- `District::Ab-Olivkrono`,`Fixes`:
  - Fixes water pipe under the mountain roads;
- `Detailing::Water`,`Terrain`,`Fixes`:
  - Tweaked border river spawners size and height;
  - Reduced sea water spawner height from 128m to 120m  
    (original sea water spawner kept at 128m with decreased radius
    for backup sea level height reference);
  - Fixed overflowing water in Am-H;
- `Transit`,`Fixes`:
  - Updated high-speed trains symbol from 'E' to 'V';
  - Updated Bus numbering system from 2-digits to 3-digits;
  - Added Transit lines;
- `Naming`,`Fixes`:
  - Simplified mountain names
    e.g. from 'Mt-Kuraĝecaĵo' to 'Mt-Kuraĝo';

-------------------------------------------------------------------------------

### v2.0 <-- v1.0 | `2025-03-27`

> Northward Equinox update.  
> (Delayed one week due to the anniversaery patch and real-life commitments.)
>
> One more dam! (or three)  
> Infrastructure expansions in the Northwest corner of the map.

- `Meta::GameVer`: v1.2.5f1;
- `Mods::Required`:
  - 'Anarchy' (74604);
  - 'Recolor' (84638);
  - 'Road Builder' (87190);
  - 'Plop the Growables' (75826);
  - 'Traffic' (80095);
  - 'Water Features' (75613);
- `Mods::RoadBuilder`,`Naming`,`Fixes`:
  - Update RoadBuilder roads and rails name and speed limit;
- `Mods::CityController`,`Note`:
  - Removed Money (O$22M) with 'City Controller',
    total return O$112M,
    Interest rate 1500%;
- `District::(Ab-Fortikeco,Ab-Racieco)`,`Expansion::Services`:
  - Built 3 more dams;
- `District::Am-Racieco`,`Expansion::(Road,Rail,Services)`:
  - New outside connections;
  - Highway extension;
  - Two new service interchanges (parclo);
  - Built 'La Pordego' service complex;
- `Detailing::Water`,`Fixes`:
  - Increased Northwest border river water spawner height and size;

-------------------------------------------------------------------------------

### v1.0 <-- v0.0 | `2025-02-16`

> Built 2 dams, a cargo port, 3 mines, and a vista in the Southeast.

- `Meta::GameVer`: v1.2.3f1;
- `Mods::Added`:
  - 'Recolor' (84638);
  - 'Road Builder' (87190);
  - 'City Controller' (89495);
- `Mods::PlopTheGrowables`:
  - 'Plop the Growables' (75826) Settings Changed:
    Now non-plopped buildings require zoning;
- `Mods::CityController`,`Note`:
  - Added Money (O$7M) with 'City Controller',
    Removed Money (O$90M) with 'City Controller',
    Interest rate 1185.7%;
- `Mods::RoadBuilder`:
  - Added numerous Road Builder roads and rails;
- `District::Ab-Olivkrono`,`Expansion::(Zoning, Services)`:
  - Added 2 dams near Mt-Olivkronaĵo, with
    electricity generation max capacity of 9GW+ with 150% budget;
  - Built utilities/village on the hill near the dam;
- `District::Mhv-Olivkrono`,`Expansion::(Industry, Road, Rail)`,`Detailing`:
  - Added a cargo port,
    a parclo interchange, and
    several signature factories;
  - Expanded the rail network near the cargo port;
- `District::Ia-Olivkrono`,`Expansion::Industry`:
    Added an industrial area with 3 mines (Stone & Ore & Coal);
- `District::Vd-Olivhaveno`,`Expansion::(Zoning,Parks,Road)`,`Detailing`:
  - Added district 'Vido-Olivhaveno'
    to house the workers for the cargo port and the industrial area;
  - Added a trumpet interchange;
- `District::(Vd-Olivhaveno,Ab-Olivkrono)`,`Expansion::Rail`,`Transit`:
  - Added a tram line between the dam foothill vista ('Vd-Olivhaveno')
    and the dam hill ('Ab-Olivkronaĵo');
- `District::Am-Olivkrono`,`Expansion::Rail`,`Transit`:
  - Expanding Rail network near Am-O;
- `District::Vilaĝo-Pioniro`,`Expansion::(Zoning,Services,Industry)`:
  - Added more housing and services, and a Grain farm;
- `Redevelop::Rail`,`Transit`:
  - Updating the map original rail network
    from single-rail to bi-directional;
  - Added a passenger train line.
- `Transit`:
  - Set up basic bus transit network;
- `Detailing::Water`,`Fixes`:
  - Added a border river spawner near the SR map border;
  - Added a sea water spawner to fix the gap near the sea border;
- `Naming`,`Fixes`:
  - Changed Outside Connection Names (Road, Rail, Sea);
  - Set missing outside connections (road) name ('Akvofalvalo');
- `Taxes`,`Note`:
  Adjusted tax rate
  - Residents now enjoy subsidies instead of taxes
    to represent Queen Serena's UBI policy;
  - Reduced commericial, industrial, officies tax rate to 6%;
  - Increased vehicle commercial tax rate by 12%;
- `Transit`,`Note`:
  Defaults (still need to be set by hand; enforcement are not strict):
  - All public transport (excluding taxis) are free;
  - Default parking fee: O$32 for cars and O$16 for motorcycle;
  - Maximum parking spaces in residential area:
    1 per building-occupied grid cell
    (regardless of building density or height);

-------------------------------------------------------------------------------

### v0.0 <-- v0.0 | `2024-12-21`

> Initial State.

- `Meta::GameVer`: v1.2.0f1;
- `Meta::PDXMods`: Published (ID 97163);
- `Meta::CityName`: Set as 'OmniCentro';
- `Expansion::Utility`:
  - Added basic utilities (a transformer).
    Now city has outside connections of power and water;
- `Naming`,`Fixes`:
  - Set outside connections (road, rail, air, ship) names;
- `Fixes`:
  - Fixed 'Road required' problems from the map;

-------------------------------------------------------------------------------
