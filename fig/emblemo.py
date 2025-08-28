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
from os.path import sep
from math import sqrt, pi, sin, cos, tan, acos
from collections.abc import Callable
# imports (3rd party)
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.lines import Line2D
mpl.use('svg')

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
    ax : Axes,
    scale  : float,
    radius : float|tuple[float, float],
    thetas : tuple[float, float],
    center : tuple[float, float] = (0., 0.),
    angle  : float = 0.,
    color  : None = None,
    linewidth_fac: float = PHI_INV/8, #11/128,
    linewidth_unit: float = 144.,    # 144 will leave no gap (== 1.0 in the ax coordinate system)
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
    ax : Axes,
    scale  : float,
    radius : float,
    length : float = 1.,
    center : tuple[float, float] = (0., 0.),
    angle  : float = 0.,      # the rotation of the whole system
    theta  : float = 120.,    # the 'openness' of the hat
    color  : None = None,
    linewidth_fac: float = PHI_INV/8, #11/128,
    linewidth_unit: float = 144,    # 144 will leave no gap (== 1.0 in the ax coordinate system)
    **kwargs,
) -> list[Line2D]:
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
    ax : Axes,
    scale  : float,
    no_t: int = 0x10,
    ts: None|list[float] = None,
    xdata_func: Callable[[float], list[float]] =  lambda t: [-1.+t, t],
    ydata_func: Callable[[float], list[float]] =  lambda t: [-1., 1.],
    color_func: Callable[[float], tuple[float, float, float, float]] =  lambda t: (t, t, t, 1.),    # RGBA
    linewidth_fac_func: Callable[[float], float] = lambda t: 1.,
    linewidth_unit: float = 144.,    #132.,
    **kwargs,
) -> list[Line2D]:
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
            Line2D(
                xdata = xdata_func(t),
                ydata = ydata_func(t),
                color = color_func(t),
                linewidth = linewidth_fac_func(t) * linewidth_multi,
                **kwargs,
        ))
        for t in ts]

def draw_band_linear_x(
    ax : Axes,
    scale  : float,
    no_t: int = 0x10,
    xdata_center: list[float] =  [-0.5, 0.5],
    xdata_halfwid: float|list[float] = 0.5,
    ydata: list[float] =  [-1., 1.],
    colors: list[float] | dict[float, None] = {
        0.0: '#000000',
        1.0: '#ffffff',
    },
    linewidth_unit: float = 144.,    #132.,
    **kwargs,
) -> list[Line2D]:
    """Draw a band in ax, with color transitioning among list of colors.
    
    Parameters
    ----------

    no_t:
        no of parallel lines (aka resolution)
    xdata_halfwid:
        half width of the line. if 0 or negative, will abort.
    colors_comp: dict
        in format of 't: color'
    """
    # init
    try:
        len(xdata_halfwid)
    except TypeError:
        if xdata_halfwid > 0:
            xdata_halfwid = [xdata_halfwid] * len(xdata_center)
        else:
            return []
        

    # init colors
    if isinstance(colors, dict):
        colors_ts = list(colors.keys())
        colors_ts.sort()
    else:
        # colors is list
        colors_ts = np.linspace(0., 1., len(colors))
        colors = {t: c for t, c in zip(colors_ts, colors)}
    colors = tuple([mpl.colors.to_rgba(colors[t]) for t in colors_ts])
    colors_vec = [x for x in zip(*colors)]
    if colors_ts is None:
        colors_ts = np.linspace(0., 1., len(colors))

    return draw_band(
        ax, scale, no_t,
        xdata_func = lambda t: [
            xi + dxi*(2*t-1.)
            for xi, dxi in zip(xdata_center, xdata_halfwid)],
        ydata_func = lambda t: ydata,
        color_func = lambda t: tuple([
            np.interp(t, colors_ts, colors_veci)
            for colors_veci in colors_vec]),
        linewidth_fac_func = lambda t: max(xdata_halfwid)*2,
        linewidth_unit = linewidth_unit,
        **kwargs,
    )



class Emblemo:
    """Drawing Emblems."""

    def __init__(self, name:str="", colors:dict=KOLOROJ, **kwargs):
        self.fig = None
        self.ax  = None
        self.name: str = name
        self.scale_y: float = 256/400
        self.ratio_xy: float = 1.
        self.colors: dict[str, str] = colors.copy()
        if name:
            attr = f'_set_as_{name}'
            if attr not in dir(self):
                raise ValueError(f"Unrecognized Emblem Name '{name}'.")
            getattr(self, attr)(**kwargs)

    def __del__(self):
        if self.fig is not None:
            plt.close(self.fig)

    @property
    def figax(self):
        return self.fig, self.ax

    @property
    def scale(self):
        return self.scale_y

    @property
    def scale_x(self):
        return self.scale_y * self.ratio_xy

    def init_figax(
        self,
        scale_y: float,    # = 256/400,
        ratio_xy: float = 1.,
        xlim: tuple[float, float] = (-1., 1.),
        ylim: tuple[float, float] = (-1., 1.),
    ):
        self.scale_y  = scale_y
        self.ratio_xy = ratio_xy
        self.fig, self.ax = plt.subplots(
            figsize=[4*self.scale_x, 4*self.scale_y])
        self.ax.set_xlim(xlim)
        self.ax.set_ylim(ylim)
        self.ax.set_axis_off()
        self.ax.set_position([0, 0, 1, 1])
        return self

    def save(
        self,
        # noext means no extension
        output_path_noext: None|str = None,
        output_exts: list[str] = ['.svg', '.png'],
        verbose: bool = True,
    ):
        """Output to files."""
        if self.fig is None:
            if verbose: print("Error: No figure to be saved.")
            return
        if output_path_noext is None:
            output_path_noext = f'.{sep}{self.name}'
        for ext in output_exts:
            output_path = f"{output_path_noext}{ext}"
            if verbose: print(f"Saving to '{output_path}'...", end=' ')
            self.fig.savefig(output_path, transparent=True)
            if verbose: print(f"Done.")
        if verbose: print(f"Done.")
        return



    def _set_as_RdO(
        self,
        # size of the drawing pad
        scale: float = 256/400,    # 1.0 => 400px x 400px
    ):
        """Draw the RdO emblem."""

        self.init_figax(scale, xlim=(-1+1.5/16, 1+1.5/16))
        self._draw_RdO()
        return self

    def _draw_RdO(self):
        # --- arcs
        # draw O
        draw_arc(
            self.ax, self.scale, radius=11/16, thetas=ts( 5.5, 19.50),
            color=self.colors['O'], linewidth_fac=16/128, zorder=0x1001)
        # draw R
        # 2.36 = 4 - acos(cos((4-3.5)/8*pi)*11/13.5)/pi*8
        draw_arc(
            self.ax, self.scale, radius=14/16, thetas=ts( 2.5, -2.5),
            color=self.colors['O'], linewidth_fac=16/128, zorder=0x1000)
        return self



    def _set_as_RdOFlago(
        self,
        # size of the drawing pad
        # scale_y: 1.0 => 400px x 400px; 225/400 => height is 225px
        scale_y: float = 225/400, # 2160/400
        ratio_xy: float = 16/9,
        offset_x: float = 22/256,
    ):    # plot
        """Draw the RdO Flag."""

        xlims = (-ratio_xy+offset_x, ratio_xy+offset_x)
        ylims = (-1., 1.)
        self.init_figax(scale_y, ratio_xy, xlim=xlims)
        ax = self.ax

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
                ], color=self.colors['C'], zorder=0,
        ))
        ax.add_patch(
            mpl.patches.Polygon([
                [xlims[1], ylims[0]],
                [xlims[1], ylims[1]],
                # [xlims[0], ylims[1]],
                [dx0-dx, ylims[1]],
                [dx0+dx, ylims[0]],
                ], color=self.colors['G'], zorder=0,
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
                    mpl.colors.to_rgb(self.colors[c_k])
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
                colors=[self.colors['O'], self.colors['O']],
                linewidth_unit=256,
            )
            draw_band_linear_x(
                ax, scale_y, no_t=1,
                xdata_center  = [dx0-dx-ddx, dx0+dx-ddx],
                xdata_halfwid = 0.01,
                ydata = [ylims[1], ylims[0]],
                colors=[self.colors['O'], self.colors['O']],
                linewidth_unit=256,
            )
        self._draw_RdO()
        return self



    def _set_as_OCG(
        self,
        # size of the drawing pad
        scale: float = 256/400,    # 1.0 => 400px x 400px
    ):
        """Draw the OCG emblem."""

        self.init_figax(scale)
        ax = self.ax

        # params for G
        t_g_2, r_g_1 = 14, 7/16
        # --- arcs
        # draw O
        draw_arc(
            ax, scale, radius=11/16, thetas=ts( 5.50, 19.50),
            color=self.colors['O'])
        # draw C
        draw_arc(
            ax, scale, radius= 9/16, thetas=ts( 2.25, 14.25),
            color=self.colors['C'])
        # draw G
        draw_arc(
            ax, scale, radius=r_g_1, thetas=ts( 2.25, t_g_2),
            color=self.colors['G'])
        center_tg3 = (cos(t_g_2/8*pi)*r_g_1/2, sin(t_g_2/8*pi)*r_g_1/2)
        center_tg3 = (    # shift a little to remove the white gap in-between
            center_tg3[0] + center_tg3[1]/128,
            center_tg3[1] - center_tg3[0]/128)
        draw_arc(ax, scale, radius=[r_g_1/2, r_g_1/8*5], thetas=ts(0, 8),
                center=center_tg3, angle=t(t_g_2), color=self.colors['G'],
        )
        # --- hats
        a = draw_hat(ax, scale, radius=14.5/16, length=9/16,
                angle=t(4), theta=t(50/9), color=self.colors['x0'])
        for i in range(1, 3):
            draw_hat(ax, scale, radius=15/16, length=7/16,
                    angle=t(4+i*16/3), color=self.colors[f'x{i}'])
        return self



    def _set_as_OCR(
        self,
        # size of the drawing pad
        scale: float = 256/400,    # 1.0 => 400px x 400px
    ):
        """Draw the OCR emblem."""

        self.init_figax(scale)
        ax = self.ax

        # --- arcs
        # draw O
        draw_arc(
            ax, scale, radius=11/16, thetas=ts( 5.50, 19.50),
            color=self.colors['O'])
        # draw C
        draw_arc(
            ax, scale, radius= 9/16, thetas=ts( 2.25, 14.25),
            color=self.colors['C'])
        # draw R
        draw_arc(
            ax, scale, radius=6.75/16, thetas=ts(  4.0, -5.0 ),
            color=self.colors['R'], linewidth_fac=(PHI_INV*1.5)/8)



    def _set_as_OCRR(
        self,
        # size of the drawing pad
        scale: float = 256/400,    # 1.0 => 400px x 400px
    ):
        """Draw the OCRR emblem."""

        self.init_figax(scale, xlim=(-1+3/16, 1+3/16))
        ax = self.ax

        # --- arcs
        # draw O
        draw_arc(
            ax, scale, radius=11/16, thetas=ts( 5.50, 19.50),
            color=self.colors['x0'], linewidth_fac=14/128)
        # draw C
        draw_arc(
            ax, scale, radius= 8/16, thetas=ts( 2.25, 14.25),
            color=self.colors['Radio'], linewidth_fac=16/128)
        # draw R
        # 2.24 = 4 - acos(cos((4-3.5)/8*pi)*11/14)/pi*8
        draw_arc(
            ax, scale, radius=13.75/16, thetas=ts( 2.25, -2.25),
            color=self.colors['x2'], linewidth_fac=15/128)
        # 1.69 = 4 - acos(cos((4-3.5)/8*pi)*11/17.5)/pi*8
        draw_arc(
            ax, scale, radius=16.75/16, thetas=ts( 1.8, -1.8),
            color=self.colors['x1'], linewidth_fac=16/128)



if __name__ == '__main__':
    Emblemo("OCG").save()
    Emblemo("OCR").save()
    Emblemo("OCRR").save()
    Emblemo("RdO").save()
    Emblemo("RdOFlago").save()
    Emblemo("RdOFlago", scale_y=2160/400, ratio_xy=1.0).save(
        "RdOFlago.emb", [".png"])
    Emblemo("RdOFlago", scale_y=2160/400).save(
        "RdOFlago.plen", [".png"])
