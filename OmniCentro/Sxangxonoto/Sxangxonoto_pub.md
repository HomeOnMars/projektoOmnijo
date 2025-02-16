Ŝanĝonoto - Publika Versio
===============================================================================

> Changelog - Public Version

Content
-------------------------------------------------------------------------------

### v1.0 <-- v0.0 | `2025-02-16`

> Built 2 dams, a cargo port, 3 mines, and a vista in the Southeast.

- `Meta::GameVer`: v1.2.3f1;
- `Meta::Mods`: Added:
    - 'Recolor' (84638);
    - 'Road Builder' (87190);
    - 'City Controller' (89495);
- `Meta::Mods::PlopTheGrowables`:
    'Plop the Growables' (75826) Settings Changed:
    Now non-plopped buildings require zoning;
- `Meta::Mods::CityController`,`Note`:
    Added Money (O$7M) with 'City Controller',
    Removed Money (O$90M) with 'City Controller',
    Interest rate 1185.7%;
- `Meta::Mods::RoadBuilder`:
    Added numerous Road Builder roads and rails;
- `District::Ab-Olivkronajxo`,`Expansion::(Zoning, Services)`:
    - Added 2 dams near Mt-Olivkronajxo, with
        electricity generation max capacity of 9GW+ with 150% budget;
    - Built utilities/village on the hill near the dam;
- `District::Mhv-Olivkronajxo`,`Expansion::(Industry, Road, Rail)`,`Detailing`:
    - Added a cargo port,
        a parclo interchange, and
        several signature factories;
    - Expanded the rail network near the cargo port;
- `District::Ia-Olivkronajxo`,`Expansion::Industry`:
    Added an industrial area with 3 mines (Stone & Ore & Coal);
- `District::Vd-Olivhaveno`,`Expansion::(Zoning, Parks, Road)`,`Detailing`:
    - Added district 'Vido-Olivhaveno'
        to house the workers for the cargo port and the industrial area;
    - Added a trumpet interchange;
- `District::(Vd-Olivhaveno, Ab-Olivkronajxo)`,`Expansion::Rail`,`Transit`:
    Added a tram line between the dam foothill vista ('Vd-Olivhaveno')
    and the dam hill ('Ab-Olivkronajxo');
- `District::Am-Olivkronajxo`,`Expansion::Rail`,`Transit`:
    - Expanding Rail network near Am-O;
- `District::Vilagxo-Pioniro`,`Expansion::(Zoning, Services, Industry)`:
    Added more housing and services, and a Grain farm;
- `Redevelop::Rail`,`Transit`: Updating the map original rail network
    from single-rail to bi-directional;
    Added a passenger train line.
- `Transit`:
    Set up basic bus transit network;
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
- `Expansion::Utility`: Added basic utilities (a transformer).
    Now city has outside connections of power and water;
- `Naming`,`Fixes`: Set outside connections (road, rail, air, ship) names;
- `Fixes`: Fixed 'Road required' problems from the map;

-------------------------------------------------------------------------------
