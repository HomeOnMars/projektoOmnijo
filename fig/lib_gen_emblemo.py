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
from math import pi, sin, cos, sqrt
from collections.abc import Callable
# imports (3rd party)
import numpy as np
import matplotlib as mpl

# params
PHI : float = (sqrt(5)+1)/2    # golden ratio
PHI_INV : float = PHI - 1
KOLOROJ : dict[str, str] = {
    # see also: <https://xkcd.com/color/rgb/>
    'O' : '#E6DAA6',  # Beige  E6DAA6 / Gold  FFD700 / Silver  C0C0C0
    'C' : '#00BFFF',  # Blue
    'G' : '#9370DB',  # Purple
    'R' : '#5E9B8A',  # Green
    'x0': '#B7E1A1',  # ^ light grey green  B7E1A1 / beige  E6DAA6
    'x1': '#D6B4FC',  # < light violet  D6B4FC
    'x2': '#95D0FC',  # > light blue  95D0FC
    'Radio': '#FFD700', # Gold
}
colors_dict = KOLOROJ.copy()

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
    scale  : float,
    radius : float|tuple[float, float],
    thetas : tuple[float, float],
    center : tuple[float, float] = (0., 0.),
    angle  : float = 0.,
    color  : None = None,
    linewidth_fac: float = PHI_INV, #11/16,
    linewidth_unit: float = 18,    # 18 will leave no gap (== 1/8 in the ax coordinate system)
    **kwargs,
) -> list[mpl.patches.Arc]:
    """Draw an arc in ax."""
    # init pars
    try: len(radius)
    except TypeError: radius_is_tuple = False
    else: radius_is_tuple = True
    width  = radius[0]*2 if radius_is_tuple else radius*2
    height = radius[1]*2 if radius_is_tuple else radius*2
    linewidth = linewidth_fac * linewidth_unit
    return [    # draw
        ax.add_patch(
            mpl.patches.Arc(
                center, width=width, height=height, angle=angle,
                theta1=min(thetas), theta2=max(thetas),
                color=color, linewidth=linewidth*scale,
                **kwargs,
        ))
    ]

def draw_hat(
    ax : mpl.axes.Axes,
    scale  : float,
    radius : float,
    length : float = 1.,
    center : tuple[float, float] = (0., 0.),
    angle  : float = 0.,      # the rotation of the whole system
    theta  : float = 120.,    # the 'openness' of the hat
    color  : None = None,
    linewidth_fac: float = PHI_INV, #11/16,
    linewidth_unit: float = 18,    # 18 will leave no gap (== 1/8 in the ax coordinate system)
    **kwargs,
) -> list[mpl.lines.Line2D]:
    """Draw the hat symbol in ax."""
    angle_rad, theta_2_rad = angle*(pi/180), theta/2*(pi/180)
    mid_pt = (
        center[0] + cos(angle_rad)*radius,
        center[1] + sin(angle_rad)*radius)
    linewidth = linewidth_fac * linewidth_unit
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
                color=color, linewidth=linewidth*scale,
                **kwargs,
        ))
    ]


def draw_band(
    ax : mpl.axes.Axes,
    scale  : float,
    no_t: int = 0x10,
    ts: None|list[float] = None,
    xdata_func: Callable[[float], list[float]] =  lambda t: [-1.+t, t],
    ydata_func: Callable[[float], list[float]] =  lambda t: [-1., 1.],
    color_func: Callable[[float], tuple[float, float, float, float]] =  lambda t: (t, t, t, 1.),    # RGBA
    linewidth_fac_func: Callable[[float], float] = lambda t: 1.,
    linewidth_unit: float = 132.,
    **kwargs,
) -> list[mpl.lines.Line2D]:
    """Draw a band in ax, with color transitioning among list of colors.
    
    Parameters
    ----------

    no_t:
        no of parallel lines (aka resolution)

    xdata_func, ydata_func:
        functions that takes in t (from 0 to 1) and returns the x and y coordinates of the line

    linewidth_fac_func:
        function that returns width factor of lines at t
        should be in the order of magnitude of the total width of the band

    linewidth_unit: float
        linewidth of a line with a width of 1.0
        in the ax coordinate system.
        Default is the case for figsize=(4, 4) and xylim=(-1, 1).
        Do Not change these unless you know what you are doing.
    """
    if ts is None:
        ts = np.linspace(0., 1., no_t) if no_t > 1 else [0.5]
    # linewidth multiplier
    # 8 because linewidth_unit is 1/8 in the ax coordinate system
    linewidth_multi = linewidth_unit * scale / max(no_t-1, 1)
    return [
        ax.add_line(
            mpl.lines.Line2D(
                xdata = xdata_func(t),
                ydata = ydata_func(t),
                color = color_func(t),
                linewidth = linewidth_fac_func(t) * linewidth_multi,
                **kwargs,
        ))
        for t in ts]

def draw_band_linear_x(
    ax : mpl.axes.Axes,
    scale  : float,
    no_t: int = 0x10,
    xdata_center: list[float] =  [-0.5, 0.5],
    xdata_halfwid: float|list[float] = 0.5,
    ydata: list[float] =  [-1., 1.],
    colors: tuple[None, None] = ['#000000', '#ffffff'],    # 2 colors only
    linewidth_unit: float = 132.,
    **kwargs,
) -> list[mpl.lines.Line2D]:
    """Draw a band in ax, with color transitioning among list of colors.
    
    Parameters
    ----------

    no_t:
        no of parallel lines (aka resolution)
    xdata_halfwid:
        half width of the line. if 0 or negative, will abort.
    
    """
    # init
    try:
        len(xdata_halfwid)
    except TypeError:
        if xdata_halfwid > 0:
            xdata_halfwid = [xdata_halfwid] * len(xdata_center)
        else:
            return []
    colors = tuple([mpl.colors.to_rgba(c) for c in colors])

    return draw_band(
        ax, scale, no_t,
        xdata_func = lambda t: [
            xi + dxi*(2*t-1.)
            for xi, dxi in zip(xdata_center, xdata_halfwid)],
        ydata_func = lambda t: ydata,
        color_func = lambda t: tuple([
            colors[0][i]*(1-t) + colors[1][i]*t
            for i in range(len(colors[0]))]),
        linewidth_fac_func = lambda t: max(xdata_halfwid)*2,
        linewidth_unit = linewidth_unit,
        **kwargs,
    )
