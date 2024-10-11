#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
RdO Emblem Generation.

Author: HomeOnMars

This work © 2024 by HomeOnMars is licensed under CC BY-NC-SA 4.0.
To view a copy of this license, visit <https://creativecommons.org/licenses/by-nc-sa/4.0/>

-------------------------------------------------------------------------------
"""


# imports (built-in)
from math import pi, sin, cos
# imports (3rd party)
import matplotlib as mpl; mpl.use('svg')
import matplotlib.pyplot as plt
# imports (my libs)
from lib_gen_emblemo import t, ts, draw_arc, draw_hat, colors_dict

# params
output_path: str = "./RdO.svg"
verbose: bool = True
        
if __name__ == '__main__':
    
    # plot
    fig, ax = plt.subplots(figsize=[4, 4])
    # debug
    if verbose: print("Drawing...")
    # params for G
    t_g_2, r_g_1 = 14, 7/16
    # --- arcs
    draw_arc(ax, radius=11/16, thetas=ts( 5.50, 19.50), color=colors_dict['O'])
    draw_arc(ax, radius= 9/16, thetas=ts( 2.25, 14.25), color=colors_dict['C'])
    draw_arc(ax, radius=r_g_1, thetas=ts( 2.25, t_g_2), color=colors_dict['G'])
    center_tg3 = (cos(t_g_2/8*pi)*r_g_1/2, sin(t_g_2/8*pi)*r_g_1/2)
    center_tg3 = (    # shift a little to remove the white gap in-between
        center_tg3[0] + center_tg3[1]/128,
        center_tg3[1] - center_tg3[0]/128)
    draw_arc(ax, radius=[r_g_1/2, r_g_1/8*5], thetas=ts(0, 8),
             center=center_tg3, angle=t(t_g_2), color=colors_dict['G'],
    )
    # --- hats
    a = draw_hat(ax, radius=14.5/16, length=9/16,
             angle=t(4), theta=t(50/9), color=colors_dict['x0'])
    for i in range(1, 3):
        draw_hat(ax, radius=15/16, length=7/16,
                 angle=t(4+i*16/3), color=colors_dict[f'x{i}'])
    
    # format and save
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_axis_off()
    ax.set_position([0, 0, 1, 1])
    if verbose: print(f"Saving to '{output_path}'...")
    fig.savefig(output_path, transparent=True)
    if verbose: print(f"Done.")
