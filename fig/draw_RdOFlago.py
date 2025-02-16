#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
RdO Flag Generation.
RdO stands for La Regno de Omnijo (in Esperanto/E++).

Author: HomeOnMars

This work © 2024 by HomeOnMars is licensed under CC BY-NC-SA 4.0.
To view a copy of this license, visit <https://creativecommons.org/licenses/by-nc-sa/4.0/>

-------------------------------------------------------------------------------
"""


# imports (built-in)
from math import pi, sin, cos, acos, tan
# imports (3rd party)
import matplotlib as mpl; mpl.use('svg')
import matplotlib.pyplot as plt
# imports (my libs)
from lib_gen_emblemo import t, ts, draw_arc, colors_dict, PHI

RATIO_XY : float = 25/16  #PHI

# main func
def draw_RdOFlago(
    # noext means no extension
    output_path_noext: str = "./RdOFlago",
    output_exts: list = ['.svg', '.png'],
    # size of the drawing pad
    scale: float = 256/400,    # 1.0 => 400px x 400px
    ratio_xy: float = RATIO_XY,
    verbose: bool = True,
):    # plot
    """
    ---------------------------------------------------------------------------
    """
    fig, ax = plt.subplots(figsize=[4*scale*ratio_xy, 4*scale])
    offset_x = 22/256
    xlims = [-ratio_xy+offset_x, ratio_xy+offset_x]
    ylims = [-1., 1.]
    # debug
    if verbose: print("Drawing...")

    # --- background
    dx = tan((t(5.5)-90)/180*pi)
    dx0 = 27/4096
    ax.add_patch(
        mpl.patches.Polygon([
            [xlims[0], ylims[1]],
            [xlims[0], ylims[0]],
            # [xlims[1], ylims[0]],
            [dx0+dx, ylims[0]],
            [dx0-dx, ylims[1]],
            ], color=colors_dict['C'],
    ))
    ax.add_patch(
        mpl.patches.Polygon([
            [xlims[1], ylims[0]],
            [xlims[1], ylims[1]],
            # [xlims[0], ylims[1]],
            [dx0-dx, ylims[1]],
            [dx0+dx, ylims[0]],
            ], color=colors_dict['G'],
    ))
    

    # --- arcs
    # draw O
    draw_arc(ax, scale, radius=11/16, thetas=ts( 5.5, 19.50), color=colors_dict['O'], linewidth_fac=16/16)
    # draw R
    # 2.36 = 4 - acos(cos((4-3.5)/8*pi)*11/13.5)/pi*8
    draw_arc(ax, scale, radius=14/16, thetas=ts( 2.5, -2.5), color=colors_dict['O'], linewidth_fac=16/16)


    # format and save
    ax.set_xlim(xlims)
    ax.set_ylim(ylims)
    ax.set_axis_off()
    ax.set_position([0, 0, 1, 1])
    for ext in output_exts:
        output_path = f"{output_path_noext}{ext}"
        if verbose: print(f"Saving to '{output_path}'...", end=' ')
        fig.savefig(output_path, transparent=True)
        if verbose: print(f"Done.")
    if verbose: print(f"Done.")

    return fig, ax

def draw_RdOFlago_emb():
    return draw_RdOFlago(
        output_path_noext="./RdOFlago.emb",
        output_exts=['.png'],
        scale=1080/400,
        ratio_xy=1.0,
    )

if __name__ == '__main__':
    draw_RdOFlago()
    draw_RdOFlago_emb()
