#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Emblems Generation.

Author: HomeOnMars

This work © 2024 by HomeOnMars is licensed under CC BY-NC-SA 4.0.
To view a copy of this license, visit <https://creativecommons.org/licenses/by-nc-sa/4.0/>

-------------------------------------------------------------------------------
"""


# imports (my libs)
from draw_OCG  import draw_OCG
from draw_OCR  import draw_OCR
from draw_OCRR import draw_OCRR
from draw_RdO  import draw_RdO
from draw_RdOFlago import draw_RdOFlago

if __name__ == '__main__':
    draw_OCG()
    draw_RdO()
    draw_OCR()
    draw_OCRR()
    draw_RdOFlago()
