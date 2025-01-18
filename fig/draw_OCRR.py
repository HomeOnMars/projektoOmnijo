#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
OCRR Emblem Generation.
OCRR stands for OmniCentra RadioReto (in Esperanto/E++).

Author: HomeOnMars

This work © 2024 by HomeOnMars is licensed under CC BY-NC-SA 4.0.
To view a copy of this license, visit <https://creativecommons.org/licenses/by-nc-sa/4.0/>

-------------------------------------------------------------------------------
"""


# imports (built-in)
from math import pi, sin, cos, acos
# imports (3rd party)
import matplotlib as mpl; mpl.use('svg')
import matplotlib.pyplot as plt
# imports (my libs)
from lib_gen_emblemo import t, ts, draw_arc, draw_hat, colors_dict

# main func
def draw_OCRR(
    # noext means no extension
    output_path_noext: str = "./OCRR",
    # size of the drawing pad
    scale: float = 256/400,    # 1.0 => 400px x 400px
    verbose: bool = True,
):
    """Draw the OCRR emblem."""
    # plot
    fig, ax = plt.subplots(figsize=[4*scale, 4*scale])
    # debug
    if verbose: print("Drawing...")
    # --- arcs
    # draw O
    draw_arc(ax, scale, radius=11/16, thetas=ts( 5.50, 19.50), color=colors_dict['x0'], linewidth_fac=14/16)
    # draw C
    draw_arc(ax, scale, radius= 8/16, thetas=ts( 2.25, 14.25), color=colors_dict['Radio'], linewidth_fac=16/16)
    # draw R
    # 2.24 = 4 - acos(cos((4-3.5)/8*pi)*11/14)/pi*8
    draw_arc(ax, scale, radius=13.75/16, thetas=ts( 2.25, -2.25), color=colors_dict['x2'], linewidth_fac=15/16)
    # 1.69 = 4 - acos(cos((4-3.5)/8*pi)*11/17.5)/pi*8
    draw_arc(ax, scale, radius=16.75/16, thetas=ts( 1.8, -1.8), color=colors_dict['x1'], linewidth_fac=16/16)
    
    # format and save
    ax.set_xlim(-1+3/16, 1+3/16)
    ax.set_ylim(-1, 1)
    ax.set_axis_off()
    ax.set_position([0, 0, 1, 1])
    for ext in ['.svg', '.png']:
        output_path = f"{output_path_noext}{ext}"
        if verbose: print(f"Saving to '{output_path}'...", end=' ')
        fig.savefig(output_path, transparent=True)
        if verbose: print(f"Done.")
    if verbose: print(f"Done.")
    
    return fig, ax

if __name__ == '__main__':
    draw_OCRR()
