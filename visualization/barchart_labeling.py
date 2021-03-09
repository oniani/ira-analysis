"""
Filename: barchart_labeling.py
Date: 2019-08-13 10:08:03 PM
Author: David Oniani
E-mail: onianidavid@gmail.com

License:
    The code is licensed under MIT License. Please read the LICENSE file in
    this distribution for details regarding the licensing of this code.

Description:
    Label horizontal and vertical barchart graphs in sns.
    Adapted from the following link:
    https://stackoverflow.com/questions/43214978/seaborn-barplot-displaying-values
"""

import numpy as np


def show_values_on_bars(axs, h_v="h", space=0.5):
    """Label a barchart."""

    def _show_on_single_plot(ax):
        """Helper function."""
        if h_v == "v":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() / 2
                _y = p.get_y() + p.get_height()
                value = int(p.get_height())
                ax.text(_x, _y, value, ha="center")
        elif h_v == "h":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() + float(space)
                _y = p.get_y() + p.get_height()
                value = int(p.get_width())
                ax.text(_x, _y, value, ha="left")

    if isinstance(axs, np.ndarray):
        for idx, ax in np.ndenumerate(axs):
            _show_on_single_plot(ax)
    else:
        _show_on_single_plot(axs)
