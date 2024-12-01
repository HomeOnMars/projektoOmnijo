#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
OCR Emblem Generation.
OCR stands for Omnija Centra Registaro (in Esperanto/E++).

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
def draw_OCR(
    # noext means no extension
    output_path_noext: str = "./OCR",
    # size of the drawing pad
    scale: float = 1.0,
    verbose: bool = True,
):
    """Draw the OCR emblem."""
    # plot
    fig, ax = plt.subplots(figsize=[4*scale, 4*scale])
    # debug
    if verbose: print("Drawing...")
    # --- arcs
    # draw O
    draw_arc(ax, radius=11/16, thetas=ts( 5.50, 19.50), color=colors_dict['O'])
    # draw C
    draw_arc(ax, radius= 9/16, thetas=ts( 2.25, 14.25), color=colors_dict['C'])
    # draw R
    draw_arc(ax, radius=6.75/16,thetas=ts(  4.0, -5.0 ), color=colors_dict['R'], linewidth_fac=15/16)
    
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
    draw_OCR()
