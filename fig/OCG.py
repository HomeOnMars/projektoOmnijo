#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
O.C.G. Emblem Generation.
O.C.G. stands for Omnija Centra Gvidado (in esperanto).

Author: HomeOnMars

This work © 2024 by HomeOnMars is licensed under CC BY-NC-SA 4.0.
To view a copy of this license, visit <https://creativecommons.org/licenses/by-nc-sa/4.0/>

-------------------------------------------------------------------------------
"""


# imports (built-in)
from math import pi, sin, cos
# imports (3rd party)
import matplotlib as mpl
import matplotlib.pyplot as plt

# params
output_path = "./OCG.svg"
colors_dict = {
    # see also: https://xkcd.com/color/rgb/
    'O' : '#C0C0C0',
    'C' : '#00BFFF',
    'G' : '#9370DB',
    'x0': '#B7E1A1',  # ^ light grey green  B7E1A1
    'x1': '#D6B4FC',  # < light violet  D6B4FC
    'x2': '#95D0FC',  # > light blue  95D0FC
}

# funcs
# theta units convert (hex -> deg)
t  = lambda theta: theta*(360/16)
ts = lambda theta1, theta2: (t(theta1), t(theta2))
#------------------------------------------------------------------------------
def draw_arc(
    ax : mpl.axes.Axes,
    radius : float|tuple[float, float],
    thetas : tuple[float, float],
    center : tuple[float, float] = (0., 0.),
    angle  : float = 0.,
    color  : None = None,
    linewidth: float = 18 * (11/16),    # 18 will leave no gap
    **kwargs,
) -> list[mpl.patches.Arc]:
    """Draw an arc in ax."""
    # init pars
    try: len(radius)
    except TypeError: radius_is_tuple = False
    else: radius_is_tuple = True
    width  = radius[0]*2 if radius_is_tuple else radius*2
    height = radius[1]*2 if radius_is_tuple else radius*2
    return [    # draw
        ax.add_patch(
            mpl.patches.Arc(
                center, width=width, height=height, angle=angle,
                theta1=thetas[0], theta2=thetas[1],
                color=color, linewidth=linewidth,
                **kwargs,
        ))
    ]

def draw_hat(
    ax : mpl.axes.Axes,
    radius : float,
    length : float = 1.,
    center : tuple[float, float] = (0., 0.),
    angle  : float = 0.,      # the rotation of the whole system
    theta  : float = 120.,    # the 'openness' of the hat
    color  : None = None,
    linewidth: float = 18 * (11/16),    # 18 will leave no gap
    **kwargs,
) -> list[mpl.lines.Line2D]:
    """Draw the hat symbol in ax."""
    angle_rad, theta_2_rad = angle*(pi/180), theta/2*(pi/180)
    mid_pt = (
        center[0] + cos(angle_rad)*radius,
        center[1] + sin(angle_rad)*radius)
    return [    # draw
        ax.add_line(
            mpl.lines.Line2D(
                xdata = [
                    mid_pt[0] + cos(angle_rad+pi-theta_2_rad)*length,
                    mid_pt[0],
                    mid_pt[0] + cos(angle_rad+pi+theta_2_rad)*length,
                ],
                ydata = [
                    mid_pt[1] + sin(angle_rad+pi-theta_2_rad)*length,
                    mid_pt[1],
                    mid_pt[1] + sin(angle_rad+pi+theta_2_rad)*length,
                ],
                color=color, linewidth=linewidth,
                **kwargs,
        ))
    ]
        
if __name__ == '__main__':
    
    # plot
    fig, ax = plt.subplots(figsize=[4, 4])
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
    fig.savefig(output_path, transparent=True)
