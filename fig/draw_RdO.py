#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
RdO Emblem Generation.
RdO stands for La Regno de Omnijo (in Esperanto/E++).

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
def draw_RdO(
    # noext means no extension
    output_path_noext: str = "./RdO",
    # size of the drawing pad
    scale: float = 1.0,
    verbose: bool = True,
):
    """Draw the RdO emblem."""
    # plot
    fig, ax = plt.subplots(figsize=[4*scale, 4*scale])
    # debug
    if verbose: print("Drawing...")
    # --- arcs
    # draw O
    draw_arc(ax, radius=11/16, thetas=ts( 5.50, 19.50), color=colors_dict['O'])
    # draw R
    # 2.36 = 4 - acos(cos((4-3.5)/8*pi)*11/13.5)/pi*8
    draw_arc(ax, radius=13.5/16, thetas=ts( 2.36, -2.36), color=colors_dict['O'], linewidth_fac=15/16)
    
    # format and save
    ax.set_xlim(-scale+1.5/16, scale+1.5/16)
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
    draw_RdO()
