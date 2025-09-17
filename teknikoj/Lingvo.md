<!-- -*- coding: utf-8 -*- -->

OmniCentraj Specifoj - Lingvo
===============================================================================

> OmniCentro Specifications - Language

Background stories for my fictional Cities: Skylines 2 city *OmniCentro*.

Legal
-------------------------------------------------------------------------------

> [!WARNING]
> This is ***a work of fiction***.
> Names, characters, businesses, places, events and incidents
> are either the products of the author's imagination or used in a fictitious manner.
> Any resemblance to actual persons, living or dead, or actual events is purely coincidental.

 <p xmlns:cc="http://creativecommons.org/ns#" >This work by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/HomeOnMars">HomeOnMars</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></a></p>

Lingvo
-------------------------------------------------------------------------------

> Language
> <br>
> [Back to OmniCentro Content](../OmniCentro.md#detalaj-informoj)

The official language in [RdO](Bulteno.md#fonrakonta-bulteno) is
***Esperanto++*** (often written as `E++` or `Epopo`),
a fictional variant of L. L. Zamenhof's artificial language
[*Esperanto*](https://lernu.net/esperanto) (1887),
with multiple changes specified by
<span style="color:Beige">Reĝino Serena</span> herself,
aiming to offer even more regularity for easier learning
while conforming to the existing world as much as possible.
<span style="color:Beige">Queen Serena</span> declared `Epopo`
as the new official language of RdO about three months in her reign,
set to gradually replace English in the next *hekjaro* (hexcade, i.e. 16 years)
in all RdO official documentations and communications.

One would think that such random order
is surely going to cause massive civil unrest,
but by that time the people have already gotten used to the <span style="color:Beige">Queen</span>'s ridiculous style;
plus, they also have the chaotic implementation of
her new UBI (universal basic income) policy to worry about.

Changes of Esperanto++ from Esperanto include:

### Alfabeto

> Alphabet

- Officially eliminated `ĥ` from the *Epopo* alphabet
  (mostly replaced with `k`);
- Adding `Q` (tɕʰ), `X` (ɕ), `Ž` (ʈʂ)
  for more diverse sounds (inspired by pinyin).  
  No words from *Epopo* are using those three letters yet;
  for now they are only used in naming.
- Pronunciation Guides  
  See also International Phonetic Alphabet (IPA)
  - [lernu: Esperanto Alphabet](https://lernu.net/gramatiko/skribo)
  - [Wikipedia: IPA/Esperanto](https://en.wikipedia.org/wiki/Help:IPA/Esperanto)
  - [Wikipedia: IPA/Mandarin](https://en.wikipedia.org/wiki/Help:IPA/Mandarin)
- Total *Epopo* alphabet: 30 letters.
  - vs English:  2 letters less (no WY) and 6 letters more (ĈĜĴŜŬŽ)
  - vs Esperanto: 1 letters less (no Ĥ) and 3 letters more (QXŽ)
  - Characters:
    - `ABCDEFGHIJKLMNOPQRSTUVXZĈĜĴŜŬŽ`
    - `abcdefghijklmnopqrstuvxzĉĝĵŝŭž`
    - `0123456789ΔλΠΣΥΨ`

### Interpunkcio

> Punctuation

- '‐' (Hyphen) and '-' (Minus)
  - Differentiate between hyphen (linking words)
    and minus (subtracting numbers).  
    This is to help computer code differentiate variable names and operations.
- '–' (En dash)
  - No space around en dash.
- '—' (Em dash)
  - Add space around em dash.  
    This to help markdown formatting (allowing splitting lines around em dash.)
- See also
  - [Hyphen / En dash / Em dash Guideline](https://www.sjsu.edu/writingcenter/docs/handouts/Hyphens%20Dashes.pdf).

### Algebro

> Algebra

- Decimal separator in *E++* is `.` instead of `,`;<br>
  Thousands separator (decimal) / ten-thousands separator (hexadecimal) is
  space(` `) instead of `.`;<!-- markdownlint-disable-line no-space-in-code -->
- Marking numbers as decimal ('Dekuma') or hexadecimal ('Hekuma'):
  - Dekuma  (base Dx10): prefixing `Dx`, or add a subscript $?_D$;
  - Hekuma  (base Dx16): prefixing `Hx`, or add a subscript $?_H$;
  - Trekuma (base Dx32): prefixing `Tx`, or add a subscript $?_T$;
- Built-in support for *hexadecimal* algebra:
  - `Δ λ Π Σ Υ Ψ` written/pronounced as `del lom nak sig gan fus`;
  - `hek`    (H) for Dx           16 (= 2^Dx4,  or Hx          10);
  - `jent`   (J) for Dx          256 (= 2^Dx8,  or Hx         100);
  - `gil`    (G) for Dx        4 096 (= 2^Dx12, or Hx        1000);
  - `muni`   (M) for Dx       65 536 (= 2^Dx16 = Dx65536^1, or Hx      1 0000);
  - `duni`   (D) for Dx4 294 967 296 (= 2^Dx32 = Dx65536^2, or Hx 1 0000 0000);
  - `trini`  (T) for Dx65536^3 (= Hx10000^3 = 1pΠ);
  - `hekni`  (I) for Dx65536^Dx16 (= Hx10000^Hx10 = 1p40,
    or approximately 1.158e77);
  - ~~`heknia muni` for Dx65536^Dx17 (= Hx10000^Hx11 = 1p44 ≈ 7.59e81 );~~
    - Warning:
      This way to say extremely large numbers is **deprecated**
      and only listed here for technical completion reasons,
      since it would be very wordy for larger numbers such as
      `kvarnia gilnia trinia jentnia dunia heknia munio` (Hx10000^Hx4321).  
      **It is recommended to use instead `p`-notation**
      **for extremely large or extremely small numbers.**
  - `hekon`  (h) for   1/Dx16 (1p-1);
  - `jenton` (j) for  1/Dx256 (1p-2);
  - `gilon`  (g) for 1/Dx4096 (1p-3);
  - `munion` (m) for 1/Dx65536 (1p-4);
  - `dunion` (d) for 1/Dx65536^2 (1p-8);
  - `trinion` (t) for 1p-Π;
  - `heknion` (i) for 1p-40;
  - ~~`hekniona munion` for 1p-44;~~
    - Warning: **Deprecated** for the same reason as above.
      use `p`-notation instead for extremely large or small numbers.
  - etc. etc.
  - When saying one `hek`, one `jent`, or one `gil`,
    always add prefix `u` to signify it as a number instead of a unit.  
    E.g., say `ujent uhek` to express Hx110 (=Dx272);  
    say `dujent uhek Utroj` to express Hx210U (=Dx528U).  
    This is to differentiate cases between e.g.
    ~~`jent HekUtroj`~~ (should be said as `ujent HekUtroj`)
    and ~~`jent hek Utroj`~~ (should be said as `ujent uhek Utroj`).
  - As a reference,
    Dx 9 100 000 000 = Hx 2 1Υ66 Ψλ00,
    pronounced as
    `du duni, ugil ganjent seshek ses muni, fusgil lomjent`.
  - When saying one `muni`, one `duni`, etc, always add `unu` in front of it.
  - Both `unu munio da Utroj` and `unu muni Utroj`
    are acceptable ways of saying Dx 65 536 U.
  - Also you can just say `unu MuniUtro` directly, as 1 MU = Dx65536 U.
  - But for fractoins, use `munioneUtro` instead of ~~`munionUtro`~~
    for more redunandencies in pronunciations
    (So people don't mix `munioneUtro` up with `MuniUtro`).
  - For prefix shorthands,
    always use no-hat capital letters for numbers \> 1
    (e.g. H for Hx10 and J for Hx100 etc.)
    and no-hat lowercase for numbers \< 1
    (e.g. h for Hx0.1 and j for Hx0.01 etc.)
  - For full list of prefix shorthands,
    see `u_rdo_prefixes` `dict` in [unuoj.py](unuoj.py) file.
  - For units shorthands (letter-based),
    always use capital letter (hat or not) as the first letter,
    and lowercase for the following letters.
    This helps to differentiate between
    the units part and prefix part of the shorthands.
    E.g. [*Lu*](Unuoj.md#potenco) would be a unit by itself,
    while *LU* would indicate the prefix 'L' (=1p38≈2.7e67)
    combined with the unit [*U*](Unuoj.md#longeco).
  - Always use letter-based unit symbols for base units
    such as length ('U'), mass ('P'), time ('Ŝ'), etc.
- `p`-notation:
  - Similar to the [`e`-notation](https://en.wikipedia.org/wiki/Scientific_notation#E_notation)
    of the decimal system, except **both sides of `p` are hexadecimal**.
  - `p` must be lower case for better visibility,
    i.e. easier to tell it from the numbers.
    `p` is chosen over `h` or other letters for exactly this reason.
  - E.g., `Hx 7 89Δλ ΠΣΥΨ 0000` can be shortened
    as `7.89ΔλΠΣΥΨp+Π` or `7.89ΔλΠΣΥΨpΠ`;
  - Pronunciation:
    TBD.

### Sekso

> Gender

- Pronouns
  - `li` is now gender-neutral
    (its old meaning of 'he' has been removed,
    leaving only 'them (singular)' alone);
  - `hi` now means 'he' (third person who is male);
  - `ŝi` remains meaning 'she' (third person who is female).
  - It is encouraged to use `li` in scenarios
    where sex is unknown/unspecified/explicitly-required-to-be-irrelevant,
    such as workplaces.
    Consider using `hi`/`ŝi` in most other situations,
    especially in causal conversations or romance novels
    to perserve information.
    This is more of a guideline than a rule.
- All nouns are now gender-neutral by default,
  unless added surfix `-in-` for female and `-iĉ-` for male.
  - E.g., `viro` is replaced by `viriĉo` for man,
    and `virino` remains to be woman.
- See also [Wikipedia](https://en.wikipedia.org/wiki/Gender_reform_in_Esperanto#Common_elements_to_regularizing_Esperanto_gender).

### Tempo

> Time

- Units and *`Omnijaro`* Calendar System (Ø+\* years)  
  See also the [Units](../teknikoj/Unuoj.md#tempo) page for explanation, and the
  [(***Spoilers***) Timeline](../intrigmalkasxo/Kronologio.md#kronologio) page
  for usage.

  | Siglo | Formo   | Nomo           |
  | --- | --------- | -------------- |
  | `Ĝ` | `Ĝoro`    | Omnija horo    |
  | `Ĉ` | `Ĉimuto`  | Omnija minuto  |
  | `Ŝ` | `Ŝekunto` | Omnija sekundo |

- Name for the months
  - `Unuamonato`: $☾_1$
  - `Duamonato`:  $☾_2$
  - ...
  - `Sigamonato`: $☾_Σ$
  - `Ganamonato`: $☾_Υ$
    (fake last month that has 1 or 2 day(s) plus potential extra seconds
    for time corrections with respect to Earth's orbit)

#### Others

- etc. etc.
