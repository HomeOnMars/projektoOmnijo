#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
OCG Emblem Generation.
OCG stands for Omnija Centra Gvidantaro (in Esperanto/E++).

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

# main func
def draw_OCG(
    # noext means no extension
    output_path_noext: str = "./OCG",
    # size of the drawing pad
    scale: float = 27/40,    # 1.0 => 400px x 400px
    verbose: bool = True,
):
    """Draw the OCG emblem."""
    # plot
    fig, ax = plt.subplots(figsize=[4*scale, 4*scale])
    # debug
    if verbose: print("Drawing...")
    # params for G
    t_g_2, r_g_1 = 14, 7/16
    # --- arcs
    # draw O
    draw_arc(ax, scale, radius=11/16, thetas=ts( 5.50, 19.50), color=colors_dict['O'])
    # draw C
    draw_arc(ax, scale, radius= 9/16, thetas=ts( 2.25, 14.25), color=colors_dict['C'])
    # draw G
    draw_arc(ax, scale, radius=r_g_1, thetas=ts( 2.25, t_g_2), color=colors_dict['G'])
    center_tg3 = (cos(t_g_2/8*pi)*r_g_1/2, sin(t_g_2/8*pi)*r_g_1/2)
    center_tg3 = (    # shift a little to remove the white gap in-between
        center_tg3[0] + center_tg3[1]/128,
        center_tg3[1] - center_tg3[0]/128)
    draw_arc(ax, scale, radius=[r_g_1/2, r_g_1/8*5], thetas=ts(0, 8),
             center=center_tg3, angle=t(t_g_2), color=colors_dict['G'],
    )
    # --- hats
    a = draw_hat(ax, scale, radius=14.5/16, length=9/16,
             angle=t(4), theta=t(50/9), color=colors_dict['x0'])
    for i in range(1, 3):
        draw_hat(ax, scale, radius=15/16, length=7/16,
                 angle=t(4+i*16/3), color=colors_dict[f'x{i}'])
    
    # format and save
    ax.set_xlim(-1, 1)
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
    draw_OCG()
