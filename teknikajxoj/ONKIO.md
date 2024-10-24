<!-- -*- coding: utf-8 -*- -->

ONKIO
===============================================================================

ONKIO: Omnija Norma Kodo por Informo-Interŝanĝo (fictional).

Malgarantio  
Disclaimer
-------------------------------------------------------------------------------

This is ***a work of fiction***.
Names, characters, businesses, places, events and incidents
are either the products of the author's imagination
or used in a fictitious manner.
Any resemblance to actual persons, living or dead, or actual events
is purely coincidental.

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/HomeOnMars/projektoOmnijo/blob/master/teknikajxoj/ONKIO.md">ONKIO</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/HomeOnMars">HomeOnMars</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></a></p>

-------------------------------------------------------------------------------









ONKIO Tablo
-------------------------------------------------------------------------------

Table generation code see [here](ONKIO.py).

Differences from the ASCII table are highlighted with **bold** text.

|    ONKIO    |    0x0\_    |    0x1\_    |    0x2\_    |    0x3\_    |    0x4\_    |    0x5\_    |    0x6\_    |    0x7\_    |
|  :-------:  |   :-----:   |   :-----:   |   :-----:   |   :-----:   |   :-----:   |   :-----:   |   :-----:   |   :-----:   |
|  **0x\_0**  |   *NULL*    |   **\\**    |   *SPACE*   |      0      |    **Ŭ**    |      P      |    **ŭ**    |      p      |
|  **0x\_1**  |             |   **\|**    |     \!      |      1      |      A      |      Q      |      a      |      q      |
|  **0x\_2**  |             |   **\{**    |      "      |      2      |      B      |      R      |      b      |      r      |
|  **0x\_3**  |             |   **\}**    |     \#      |      3      |      C      |      S      |      c      |      s      |
|  **0x\_4**  |             |   **\@**    |      $      |      4      |      D      |      T      |      d      |      t      |
|  **0x\_5**  |             |   **\`**    |      %      |      5      |      E      |      U      |      e      |      u      |
|  **0x\_6**  |             |    **^**    |      &      |      6      |      F      |      V      |      f      |      v      |
|  **0x\_7**  |   *BELL*    |    **~**    |      '      |      7      |      G      |      W      |      g      |      w      |
|  **0x\_8**  |  *BS \\b*   |   **\[**    |     \(      |      8      |      H      |      X      |      h      |      x      |
|  **0x\_9**  |  *HT \\t*   |   **\]**    |     \)      |      9      |      I      |      Y      |      i      |      y      |
|  **0x\_a**  |  *LF \\n*   |    **:**    |   **\_**    |    **Ă**    |      J      |      Z      |      j      |      z      |
|  **0x\_b**  |  *VT \\v*   |    **;**    |     \+      |    **Ř**    |      K      |    **Ĉ**    |      k      |    **ĉ**    |
|  **0x\_c**  |  *FF \\f*   |   **\<**    |      ,      |    **Č**    |      L      |    **Ĝ**    |      l      |    **ĝ**    |
|  **0x\_d**  |  *CR \\r*   |    **=**    |   **\***    |    **Ď**    |      M      |    **Ĵ**    |      m      |    **ĵ**    |
|  **0x\_e**  |  ***SUB***  |   **\>**    |     \.      |    **Ě**    |      N      |    **Ŝ**    |      n      |    **ŝ**    |
|  **0x\_f**  |  ***ESC***  |    **?**    |      /      |    **Ğ**    |      O      |   **\-**    |      o      |    *DEL*    |









ASCII Table
-------------------------------------------------------------------------------

For comparison:

- Reference: (2024-10-18) [Wikipedia](https://en.wikipedia.org/wiki/ASCII).

|             |    0x0\_    |    0x1\_    |    0x2\_    |    0x3\_    |    0x4\_    |    0x5\_    |    0x6\_    |    0x7\_    |
|  :-------:  |   :-----:   |   :-----:   |   :-----:   |   :-----:   |   :-----:   |   :-----:   |   :-----:   |   :-----:   |
|  **0x\_0**  |   *NULL*    |             |   *SPACE*   |      0      |      @      |      P      |      `      |      p      |
|  **0x\_1**  |             |             |      !      |      1      |      A      |      Q      |      a      |      q      |
|  **0x\_2**  |             |             |      "      |      2      |      B      |      R      |      b      |      r      |
|  **0x\_3**  |             |             |      #      |      3      |      C      |      S      |      c      |      s      |
|  **0x\_4**  |             |             |      $      |      4      |      D      |      T      |      d      |      t      |
|  **0x\_5**  |             |             |      %      |      5      |      E      |      U      |      e      |      u      |
|  **0x\_6**  |             |             |      &      |      6      |      F      |      V      |      f      |      v      |
|  **0x\_7**  |   *BELL*    |             |      '      |      7      |      G      |      W      |      g      |      w      |
|  **0x\_8**  |  *BS \\b*   |             |      (      |      8      |      H      |      X      |      h      |      x      |
|  **0x\_9**  |  *HT \\t*   |             |      )      |      9      |      I      |      Y      |      i      |      y      |
|  **0x\_a**  |  *LF \\n*   |    *SUB*    |     \*      |      :      |      J      |      Z      |      j      |      z      |
|  **0x\_b**  |  *VT \\v*   |    *ESC*    |      +      |      ;      |      K      |      [      |      k      |      {      |
|  **0x\_c**  |  *FF \\f*   |             |      ,      |      <      |      L      |     \\      |      l      |     \|      |
|  **0x\_d**  |  *CR \\r*   |             |      -      |      =      |      M      |      ]      |      m      |      }      |
|  **0x\_e**  |             |             |      .      |      >      |      N      |      ^      |      n      |      ~      |
|  **0x\_f**  |             |             |      /      |      ?      |      O      |     \_      |      o      |    *DEL*    |
