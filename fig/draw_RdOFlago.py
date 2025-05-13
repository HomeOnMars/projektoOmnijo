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
import numpy as np
import matplotlib as mpl; mpl.use('svg')
import matplotlib.pyplot as plt
# imports (my libs)
from lib_gen_emblemo import (
    t, ts, draw_arc, draw_band_linear_x, colors_dict, PHI,
)

RATIO_XY : float = 16/9  #PHI

# main func
def draw_RdOFlago(
    # noext means no extension
    output_path_noext: str = "./RdOFlago",
    output_exts: list = ['.svg', '.png'],
    # size of the drawing pad
    # scale_y: 1.0 => 400px x 400px; 256/400 => height is 256px
    scale_y: float = 225/400,
    ratio_xy: float = RATIO_XY,
    verbose: bool = True,
):    # plot
    """
    ---------------------------------------------------------------------------
    """
    fig, ax = plt.subplots(figsize=[4*scale_y*ratio_xy, 4*scale_y])
    offset_x = 22/256
    xlims = [-ratio_xy+offset_x, ratio_xy+offset_x]
    ylims = [-1., 1.]
    # debug
    if verbose: print("Drawing...")

    # --- background
    dx = tan((t(5.5)-90)/180*pi)  # slash position changes (half)
    ddx = 68/256 * 2.0            # color transition band width
    dx0 = 8/4096 # + ddx/8       # dx bias

    ax.add_patch(
        mpl.patches.Polygon([
            [xlims[0], ylims[1]],
            [xlims[0], ylims[0]],
            # [xlims[1], ylims[0]],
            [dx0+dx, ylims[0]],
            [dx0-dx, ylims[1]],
            ], color=colors_dict['C'], zorder=0,
    ))
    ax.add_patch(
        mpl.patches.Polygon([
            [xlims[1], ylims[0]],
            [xlims[1], ylims[1]],
            # [xlims[0], ylims[1]],
            [dx0-dx, ylims[1]],
            [dx0+dx, ylims[0]],
            ], color=colors_dict['G'], zorder=0,
    ))


    # --- color transition
    colors_comp : dict[float, dict[None, float]] = {
        # t: ({color: weight}, alpha)
        0.0: ({'C': 1}, 0.0),
        0.5-1/0x1000: ({'C': 0, 'x2': 1, 'x1': 0, 'G': 0}, 1.0),
        0.5+1/0x1000: ({'C': 0, 'x2': 0, 'x1': 1, 'G': 0}, 1.0),
        1.0: ({'G': 1}, 0.0),
    }

    # compile colors_comp into colors
    colors = {}
    for ti, d in colors_comp.items():
        c_d, alpha = d
        c_ks = list(c_d.keys())
        ws = np.asarray([c_d[c_k] for c_k in c_ks])

        colors[ti] = (    # weighted average
            np.sum(np.asarray([
                mpl.colors.to_rgb(colors_dict[c_k])
                for c_k in c_ks
            ]) * ws[:, np.newaxis],
            axis=0) / np.sum(ws)
        ).tolist() + [alpha]

    # draw
    draw_band_linear_x(
        ax, scale_y, no_t=0x100,
        xdata_center  = [dx0-dx, dx0+dx],
        xdata_halfwid = abs(ddx),
        ydata = [ylims[1], ylims[0]],
        colors=colors,
        linewidth_unit=256,
    )

    # Debug
    if False:
        draw_band_linear_x(
            ax, scale_y, no_t=1,
            xdata_center  = [dx0-dx+ddx, dx0+dx+ddx],
            xdata_halfwid = 0.01,
            ydata = [ylims[1], ylims[0]],
            colors=[colors_dict['O'], colors_dict['O']],
            linewidth_unit=256,
        )
        draw_band_linear_x(
            ax, scale_y, no_t=1,
            xdata_center  = [dx0-dx-ddx, dx0+dx-ddx],
            xdata_halfwid = 0.01,
            ydata = [ylims[1], ylims[0]],
            colors=[colors_dict['O'], colors_dict['O']],
            linewidth_unit=256,
        )
    

    # --- arcs
    # draw O
    draw_arc(
        ax, scale_y, radius=11/16, thetas=ts( 5.5, 19.50),
        color=colors_dict['O'], linewidth_fac=16/128, zorder=0x1001)
    # draw R
    # 2.36 = 4 - acos(cos((4-3.5)/8*pi)*11/13.5)/pi*8
    draw_arc(
        ax, scale_y, radius=14/16, thetas=ts( 2.5, -2.5),
        color=colors_dict['O'], linewidth_fac=16/128, zorder=0x1000)


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
        scale_y=2160/400,
        ratio_xy=1.0,
    )

def draw_RdOFlago_full():
    return draw_RdOFlago(
        output_path_noext="./RdOFlago.full",
        output_exts=['.png'],
        scale_y=2160/400,
    )

if __name__ == '__main__':
    draw_RdOFlago()
    draw_RdOFlago_emb()
    draw_RdOFlago_full()
