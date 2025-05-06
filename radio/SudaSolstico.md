<!-- -*- coding: utf-8 -*- -->

OmniCentra RadioReto - Suda Solstico
===============================================================================

> OmniCentra Radio Network - Southern Solstice Radio

Documents for my fictional radio station
for my ficitional Cities: Sylines 2 city *OmniCentro*.

Legal
-------------------------------------------------------------------------------

> [!WARNING]
> This is ***a work of fiction***.
> Names, characters, businesses, places, events and incidents
> are either the products of the author's imagination or used in a fictitious manner.
> Any resemblance to actual persons, living or dead, or actual events is purely coincidental.

<p xmlns:cc="http://creativecommons.org/ns#" >This work by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/HomeOnMars">HomeOnMars</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC-SA 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" alt=""></a></p>

Most content (especially lines) in this page will be created with ChatGPT,
or inspired by my discussions with it.

Scenaroj
-------------------------------------------------------------------------------

> Settings

### Radio-gastiganto

> Radio host

#### Karla Revin

- Base
  - Based on DJ Cara GTA V's Non-Stop-Pop FM (as voiced by Cara Delevingne).
  - Most of Karla's lines will be AI generated using <https://www.djcara.com/>.
- Background

Replikoj
-------------------------------------------------------------------------------

> Lines

```bash
# bash
# cut first 5sec and last 15sec
# TYPE: "Radio Channel ID" / "Radio ID + Blurbs" / "Clean Blurbs"
ffmpeg -y -ss 00:00:05 -to 00:00:24 -i Karla_.raw.mp3 -acodec libvorbis -ar 48000 -metadata ARTIST="Karla Revin" -metadata ALBUM="Suda Solstico Radio" -metadata RADIO\ STATION="OmniCentra RadioReto" -metadata RADIO\ CHANNEL="Suda Solstico" -metadata ORGANIZATION="HomeOnMars" -metadata TYPE="Clean Blurbs" -fflags +igndts -loglevel error -vn Karla_.ogg
```

Note: Use "Revinn" instead of "Revin" to force correct pronunciation.

### Enkondukoj

> Intros

- `Karla_E0`  
  Welcome to Southern Solstice Radio. I’m your hostess, Karla Revinn.

- `Karla_E1`  
  You’ve tuned in to Southern Solstice Radio. I’m your hostess Karla Revinn, broadcasting live from our brand new capital OmniCentro, where every sunrise smells like grand ambition and wet concrete.

### Finoj

> Outros

- `Karla_F0`  
  As the artificial stars flicker on and the city tucks itself in under scaffolding and synthetic dreams, remember: you are not alone, you’re just statistically insignificant. This is Karla Revinn, signing off from Southern Solstice— where the revolution is already won, and the only thing left to do is dance to it.
