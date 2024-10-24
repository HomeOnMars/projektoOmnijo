#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
OmniCentro Climate Calculations.

Author: HomeOnMars



-------------------------------------------------------------------------------

MIT License

Copyright (c) 2024 HomeOnMars

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

-------------------------------------------------------------------------------
"""

import numpy as np
from astropy import units as u

# Climate of [Reykjavik](https://en.wikipedia.org/wiki/Reykjav%C3%ADk#Climate) (2024-10-23)

# record temperature max by month
Tr_max= np.array([11.6, 10.2, 14.2, 17.1, 20.6, 22.4, 25.7, 24.8, 20.1, 15.7, 12.7, 12.0])*u.deg_C + 2.0*u.deg_C
# average temperature max by month
T_max = np.array([ 3.2,  3.3,  4.2,  6.9, 10.1, 13.0, 14.9, 14.1, 11.4,  7.6,  4.7,  3.3])*u.deg_C + 1.5*u.deg_C
# record temperature min by month
Tr_min= np.array([-24.5, -17.6, -16.4, -16.4, -7.7, -0.7, 1.4, -0.4, -4.4, -10.6, -15.1, -16.8])*u.deg_C + 0.0*u.deg_C
# average temperature min by month
T_min = np.array([-1.7, -1.9, -1.3,  1.0,  4.0,  7.2,  9.1,  8.6,  6.2,  2.7, -0.1,  1.6])*u.deg_C + 0.5*u.deg_C
# average temperature by month
T_avg = np.array([ 0.7,  0.5,  1.2,  3.7,  6.7,  9.8, 11.6, 11.0,  8.5,  4.9,  2.2,  0.8])*u.deg_C + 1.0*u.deg_C
# chance of rain
p_rain=(np.array([15.3, 15.0, 14.2, 12.0, 10.8,  9.3, 10.3, 11.6, 15.0, 13.1, 13.7, 14.6]) / 30) * 100*u.percent * 0.75
# amount of rain
v_rain= np.array([87.1, 90.6, 80.7, 59.0, 52.6, 43.3, 49.9, 64.5, 87.0, 79.8, 86.5, 94.9])*u.mm




ss = {
    'vintro'   : {'indeksoj': [11,  0,  1]},
    'printempo': {'indeksoj': [ 2,  3,  4]},
    'somero'   : {'indeksoj': [ 5,  6,  7]},
    'auxtuno'  : {'indeksoj': [ 8,  9, 10]},
}

for k in ss.keys():
    ss[k]['T_min_v'] = np.min(T_min[ss[k]['indeksoj']])*0.75 + np.mean(T_min[ss[k]['indeksoj']])*0.25
    ss[k]['T_min_d'] = np.std(T_min[ss[k]['indeksoj']]) + np.mean((T_avg - Tr_min)[ss[k]['indeksoj']])/(2*np.e)
    ss[k]['T_max_v'] = np.max(T_max[ss[k]['indeksoj']])*0.75 + np.mean(T_max[ss[k]['indeksoj']])*0.25
    ss[k]['T_max_d'] = np.std(T_max[ss[k]['indeksoj']]) + np.mean((Tr_max - T_avg)[ss[k]['indeksoj']])/(2*np.e)
    ss[k]['rain_p' ] = np.mean(p_rain[ss[k]['indeksoj']])
    ss[k]['rain_v' ] = np.mean(v_rain[ss[k]['indeksoj']])
    ss[k]['rain_d' ] = (np.std(v_rain[ss[k]['indeksoj']])*0.75+np.std(v_rain)*0.25)

if __name__ == '__main__':
    for k in ss.keys():
        print(f"{k}")
        print(f"\tT_min: \t{ss[k]['T_min_v'] :5.2f} +/- {ss[k]['T_min_d'] :5.2f}")
        print(f"\tT_max: \t{ss[k]['T_max_v'] :5.2f} +/- {ss[k]['T_max_d'] :5.2f}")
        print(f"\train : \t({ss[k]['rain_p'] :6.2f} )  {ss[k]['rain_v'] :6.2f} +/- {ss[k]['rain_d'] :5.2f}")
