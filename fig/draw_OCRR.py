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
    scale: float = 1.0,
    verbose: bool = True,
):
    """Draw the OCRR emblem."""
    # plot
    fig, ax = plt.subplots(figsize=[4*scale, 4*scale])
    # debug
    if verbose: print("Drawing...")
    # --- arcs
    # draw O
    draw_arc(ax, radius=11/16, thetas=ts( 5.50, 19.50), color=colors_dict['O'])
    # draw C
    draw_arc(ax, radius= 9/16, thetas=ts( 2.25, 14.25), color=colors_dict['R'])
    # draw R
    # 2.49 = 4 - acos(cos((4-3.5)/8*pi)*11/13)/pi*8
    draw_arc(ax, radius=13/16, thetas=ts( 2.49, -2.49), color=colors_dict['x2'])
    # 2.04 = 4 - acos(cos((4-3.5)/8*pi)*11/15)/pi*8
    draw_arc(ax, radius=15/16, thetas=ts( 2.04, -2.04), color=colors_dict['x1'])
    
    # format and save
    ax.set_xlim(-scale, scale)
    ax.set_ylim(-scale, scale)
    ax.set_axis_off()
    ax.set_position([0, 0, 1, 1])
    for ext in ['.svg', '.png']:
        output_path = f"{output_path_noext}{ext}"
        if verbose: print(f"Saving to '{output_path}'...", end=' ')
        fig.savefig(output_path, transparent=True)
        if verbose: print(f"Done.")
    if verbose: print(f"Done.")

if __name__ == '__main__':
    draw_OCRR()
