"""
Filename: ad_spend_barchart.py
Date: 2019-08-21 10:35:41 AM
Author: David Oniani
E-mail: onianidavid@gmail.com

License:
    The code is licensed under GNU General Public License v3.0.
    Please read the LICENSE file in this distribution for details
    regarding the licensing of this code.

Description:
    Generate a barchart for ad_spend.
"""

"""
DATA
----
Generated by the command `./ad_spend`.

By year...
Year 2015: RUB 1878750.880, $0.000
Year 2016: RUB 3097013.630, $74.000
Year 2017: RUB 899158.460, $35.330

By year (quarters)...
Year 2015 (Quarter 1): RUB 408337.520, $0.000
Year 2015 (Quarter 2): RUB 660555.300, $0.000
Year 2015 (Quarter 3): RUB 809858.060, $0.000

Year 2016 (Quarter 1): RUB 582244.630, $0.000
Year 2016 (Quarter 2): RUB 899897.390, $0.000
Year 2016 (Quarter 3): RUB 599936.310, $74.000
Year 2016 (Quarter 4): RUB 1014935.300, $0.000

Year 2017 (Quarter 1): RUB 563214.650, $35.330
Year 2017 (Quarter 2 April): RUB 198182.600, $0.000
Year 2016 (Quarter 2 May): RUB 95110.730, $0.000
Year 2016 (Quarter 3): RUB 42650.480, $0.000
"""


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from barchart_labeling import show_values_on_bars


def main() -> None:
    """The main function."""

    sns.set(
        color_codes=True, rc={"figure.figsize": (15.0, 9.0)}, style="darkgrid"
    )

    ad_spend_RU = [
        408337.520,
        660555.300,
        809858.060,
        582244.630,
        899897.390,
        599936.310,
        1014935.300,
        563214.650,
        198182.600,
        95110.730,
        42650.480,
    ]

    labels = [
        "2015 Quarter 2",
        "2015 Quarter 3",
        "2015 Quarter 4",
        "2016 Quarter 1",
        "2016 Quarter 2",
        "2016 Quarter 3",
        "2016 Quarter 4",
        "2017 Quarter 1",
        "2017 Quarter 2 April",
        "2017 Quarter 2 May",
        "2017 Quarter 3",
    ]

    # Plot and save the barchart
    _, _ = plt.subplots(1, 1)
    sns_plot = sns.barplot(ad_spend_RU, labels)
    sns_plot.set_title(
        "Distribution of Ad Spendings Over Years 2015, 2016, and 2017 (in Rubles)"
    )
    show_values_on_bars(sns_plot, space=max(ad_spend_RU) * 0.5 / 100)
    figure = sns_plot.get_figure()
    figure_name = "barchart_ad_spend_RU_distribution.png"
    figure.savefig(figure_name)


if __name__ == "__main__":
    main()