#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Library for Emblem Generation.

Author: HomeOnMars

This work © 2024 by HomeOnMars is licensed under CC BY-NC-SA 4.0.
To view a copy of this license, visit <https://creativecommons.org/licenses/by-nc-sa/4.0/>

-------------------------------------------------------------------------------
"""


# imports (built-in)
from math import pi, sin, cos
# imports (3rd party)
import matplotlib as mpl

# params
colors_dict = {
    # see also: <https://xkcd.com/color/rgb/>
    'O' : '#C0C0C0',  # Silver
    'C' : '#00BFFF',  # Blue
    'G' : '#9370DB',  # Purple
    'R' : '#5E9B8A',  # Green
    'x0': '#B7E1A1',  # ^ light grey green  B7E1A1 / beige  E6DAA6
    'x1': '#D6B4FC',  # < light violet  D6B4FC
    'x2': '#95D0FC',  # > light blue  95D0FC
}

# funcs
# theta units convert (hex -> deg)
def t(theta: float) -> float:
    """Convert angle from hex to deg."""
    return theta*(360/16)
def ts(theta1: float, theta2: float) -> tuple[float, float]:
    """Convert angles from hex to deg."""
    return (t(theta1), t(theta2))
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
                theta1=min(thetas), theta2=max(thetas),
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
