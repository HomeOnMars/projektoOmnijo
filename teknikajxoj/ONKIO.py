#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ONKIO table and ASCII table generation.
ONKIO: Omnija Norma Kodo por Informo-Interŝanĝo,
i.e. a fictional ASCII-equivalent table for Esperanto/E++.
(ASCII: American Standard Code for Information Interchange.)

Note: Esperanto letter hx/Hx is not present in this table,
    since we eliminated it in E++.

Code author: HomeOnMars



-------------------------------------------------------------------------------

3-Clause BSD License

Copyright 2024 HomeOnMars

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

-------------------------------------------------------------------------------
"""


# ONKIO vs ASCII
#    ONKIO: Omnija Norma Kodo por Informo-Interŝanĝo (fictional)
#    ASCII: American Standard Code for Information Interchange

# print both ONKIO and ASCII tables as markdown tables
#------------------------------------------------------------------------------

from math import nan, isnan

# escapable characters for markdown formatting
MARKDOWN_ESCAPABLES : set = {
    '\\', '`', '*', '_', '#', '+', '-', '.', '!', '|',
    '{', '}', '[', ']', '<', '>' , '(', ')', '@',
}

# Translate ONKIO char to ASCII char
ONKIO_2_ASCII_DICT = {chr(ascii_c): chr(ascii_c) for ascii_c in range(128)}
# Differences
#    Letters
ONKIO_2_ASCII_DICT[chr(0x40)] = chr(0x20)     # @ -> SPACE
ONKIO_2_ASCII_DICT[chr(0x60)] = chr(0x2011)   # ` -> ‑
ONKIO_2_ASCII_DICT[chr(0x5b)] = chr(0x108)    # [ -> Ĉ
ONKIO_2_ASCII_DICT[chr(0x7b)] = chr(0x109)    # { -> ĉ
ONKIO_2_ASCII_DICT[chr(0x5c)] = chr(0x11c)    # \ -> Ĝ
ONKIO_2_ASCII_DICT[chr(0x7c)] = chr(0x11d)    # | -> ĝ
ONKIO_2_ASCII_DICT[chr(0x5d)] = chr(0x134)    # ] -> Ĵ
ONKIO_2_ASCII_DICT[chr(0x7d)] = chr(0x135)    # } -> ĵ
ONKIO_2_ASCII_DICT[chr(0x5e)] = chr(0x15c)    # ^ -> Ŝ
ONKIO_2_ASCII_DICT[chr(0x7e)] = chr(0x15d)    # ~ -> ŝ
ONKIO_2_ASCII_DICT[chr(0x5f)] = chr(0x16c)    #  _  -> Ŭ    # Ctrl-Shift-\ + U
ONKIO_2_ASCII_DICT[chr(0x7f)] = chr(0x16d)    # DEL -> ŭ    # Ctrl-Shift-\ + u
#    Hexadecimal characters
ONKIO_2_ASCII_DICT[chr(0x3a)] = chr(0x3b1)    # : -> α
ONKIO_2_ASCII_DICT[chr(0x3b)] = chr(0x394)    # ; -> Δ
ONKIO_2_ASCII_DICT[chr(0x3c)] = chr(0x3c9)    # < -> ω
ONKIO_2_ASCII_DICT[chr(0x3d)] = chr(0x3a7)    # = -> Χ
ONKIO_2_ASCII_DICT[chr(0x3e)] = chr(0x3b3)    # > -> γ
ONKIO_2_ASCII_DICT[chr(0x3f)] = chr(0x3b6)    # ? -> ζ
#     Punctuation & Symbols
ONKIO_2_ASCII_DICT[chr(0x10)] = chr(0x5c)    # 0x10 -> \
ONKIO_2_ASCII_DICT[chr(0x11)] = chr(0x7b)    # 0x11 -> {
ONKIO_2_ASCII_DICT[chr(0x12)] = chr(0x7c)    # 0x12 -> |
ONKIO_2_ASCII_DICT[chr(0x13)] = chr(0x7d)    # 0x13 -> }
ONKIO_2_ASCII_DICT[chr(0x14)] = chr(0x7e)    # 0x14 -> ~
ONKIO_2_ASCII_DICT[chr(0x15)] = chr(0x60)    # 0x15 -> `
ONKIO_2_ASCII_DICT[chr(0x16)] = chr(0x5e)    # 0x16 -> ^
ONKIO_2_ASCII_DICT[chr(0x17)] = chr(0x40)    # 0x17 -> @
ONKIO_2_ASCII_DICT[chr(0x18)] = chr(0x5b)    # 0x18 -> [
ONKIO_2_ASCII_DICT[chr(0x19)] = chr(0x5d)    # 0x19 -> ]
ONKIO_2_ASCII_DICT[chr(0x1a)] = chr(0x3a)    # 0x1a -> :
ONKIO_2_ASCII_DICT[chr(0x1b)] = chr(0x3b)    # 0x1b -> ;
ONKIO_2_ASCII_DICT[chr(0x1c)] = chr(0x3c)    # 0x1c -> <
ONKIO_2_ASCII_DICT[chr(0x1d)] = chr(0x3d)    # 0x1d -> =
ONKIO_2_ASCII_DICT[chr(0x1e)] = chr(0x3e)    # 0x1e -> >
ONKIO_2_ASCII_DICT[chr(0x1f)] = chr(0x3f)    # 0x1f -> ?
ONKIO_2_ASCII_DICT[chr(0x20)] = chr(0x5f)    # SPACE -> _
#    Control Sequences (limit to 0x0_)
ONKIO_2_ASCII_DICT[chr(0x0d)] = chr(0x1a)    # 0x0d -> SUB
ONKIO_2_ASCII_DICT[chr(0x0e)] = chr(0x1b)    # 0x0e -> ESC
ONKIO_2_ASCII_DICT[chr(0x0f)] = chr(0x7f)    # 0x0f -> DEL



#    normalize
for c_str in tuple(ONKIO_2_ASCII_DICT.keys()):    # translate char code ver too
    ONKIO_2_ASCII_DICT[ord(c_str)] = ord(ONKIO_2_ASCII_DICT[c_str])
#    get ASCII_2_ONKIO_DICT
ASCII_2_ONKIO_DICT = {
    ONKIO_2_ASCII_DICT[c]: c for c in ONKIO_2_ASCII_DICT.keys()}
#    get ASCII string of ONKIO-style hex representations
deksesumigxas = lambda x: ''.join([
    chr(ONKIO_2_ASCII_DICT[ ord(s) - ord('a') + ord('9') + 1 ])
    if s in set('abcdef') else s
    for s in hex(x)
])    # hex-ify string / deksesumigxas signovico
b16s = deksesumigxas


# formatting and printing as markdown tables
def formatter(c: int|str = '', highlight: bool = False) -> str:
    """Add formatting."""
    if isinstance(c, str):
        if c:
            return '***'+c+'***' if highlight else '*'+c+'*'
        return ''
    elif isnan(c):
        return ''
    else:
        txt = '\\' + chr(c) if chr(c) in MARKDOWN_ESCAPABLES else chr(c)
        if highlight:
            txt = '**'+txt+'**'
        return txt
            
def chr_2_txt_ascii(c: int, highlight: bool = False) -> str:
    """Return markdown text description of ASCII code for char c"""
    if c <= 32:
        if c == 0x00:
            return formatter('NULL', highlight)
        elif c == 0x04:    # End of Transmission
            return formatter('EOT',  highlight)
        elif c == 0x07:    # Alert
            return formatter('BELL', highlight)
        elif c == 0x08:    # Backspace
            return formatter(r'BS \\b', highlight)
        elif c == 0x09:    # horizontal tab
            return formatter(r'HT \\t', highlight)
        elif c == 0x0A:    # line feed
            return formatter(r'LF \\n', highlight)
        elif c == 0x0B:    # vertical tab
            return formatter(r'VT \\v', highlight)
        elif c == 0x0C:    # form feed / clear screen / next page
            return formatter(r'FF \\f', highlight)
        elif c == 0x0D:    # carriage return
            return formatter(r'CR \\r', highlight)
        elif c == 0x1A:    # Windows end-of-file
            return formatter('SUB', highlight)
        elif c == 0x1B:    # GCC escape sequence initializer
            return formatter('ESC', highlight)
        elif c == 0x20:
            return formatter('SPACE', highlight)
        else:    # uncommon control char
            # return formatter('0x'+hex(i)[-1]+hex(j)[-1]+'')
            return formatter()
    elif c == 127:
        return formatter('DEL', highlight)
    return formatter(c, highlight)



def chr_2_txt_onkio(c: int, highlight: bool = False) -> str:
    """Return markdown text description of ONKIO code for char c"""
    return chr_2_txt_ascii(ONKIO_2_ASCII_DICT[c], highlight)



def get_md_table(
    chr_2_txt: type(abs) = chr_2_txt_ascii,
    highlight_func: None|type(abs) = None,
    title: str = '',
    nrow: int = 16,
    ncol: int = 8,
) -> str:
    """Get ascii table in markdown format."""
    # init paras
    entry = lambda s='': f"|{s:^13}"
    
    txt  = entry(title) + ''.join(
        [entry(hex(i) + '\\_') for i in range(ncol)]
    ) + '|\n'
    txt += entry(":-------:") + ''.join(
        [entry(":-----:") for i in range(ncol)]
    ) + '|\n'
    for j in range(nrow):    # row
        txt += entry('**0x\\_'+hex(j)[-1]+'**')
        for i in range(ncol):    # col
            c = i*nrow+j  # character code
            highlight = False if highlight_func is None else highlight_func(c)
            txt += entry(chr_2_txt(c, highlight=highlight))
        txt += '|\n'
    return txt



if __name__ == '__main__':
    txt_ascii = get_md_table(chr_2_txt_ascii, title='ASCII')
    txt_onkio = get_md_table(
        chr_2_txt_onkio, title='ONKIO',
        highlight_func=lambda c: ONKIO_2_ASCII_DICT[c] != c)
    print(txt_ascii)
    print('\n\n\n')
    print(txt_onkio)

#------------------------------------------------------------------------------