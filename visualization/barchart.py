"""
Filename: barchart.py
Created: 2019/07/14 09:32:11 PM
Author: David Oniani
E-mail: onianidavid@gmail.com

License:
    The code is licensed under GNU General Public License v3.0.
    Please read the LICENSE file in this distribution for details
    regarding the licensing of this code.

Description:
    A program to plot a barchart.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def main() -> None:
    """The main function."""

    sns.set(
        color_codes=True, rc={"figure.figsize": (15.0, 9.0)}, style="darkgrid"
    )

    filenames = [
        "../data/csv/year-2015/2015-Quarter-2.csv",
        "../data/csv/year-2015/2015-Quarter-3.csv",
        "../data/csv/year-2015/2015-Quarter-4.csv",
        "../data/csv/year-2016/2016-Quarter-1.csv",
        "../data/csv/year-2016/2016-Quarter-2.csv",
        "../data/csv/year-2016/2016-Quarter-3.csv",
        "../data/csv/year-2016/2016-Quarter-4.csv",
        "../data/csv/year-2017/2017-Quarter-1.csv",
        "../data/csv/year-2017/2017-Quarter-2-April.csv",
        "../data/csv/year-2017/2017-Quarter-2-May.csv",
        "../data/csv/year-2017/2017-Quarter-3.csv",
    ]

    lengths = []
    labels = []

    for filename in filenames:
        data = pd.read_csv(open(filename, "r"), thousands=",", na_filter=False)
        lengths.append(len(data))
        labels.append(" ".join(filename.split("/")[-1][:-4].split("-")))

    sns_plot = sns.barplot(lengths, labels)
    sns_plot.set_title("Distribution of Posts Over Years 2015, 2016, and 2017")
    figure = sns_plot.get_figure()
    figure_name = "barchart.png"
    figure.savefig(figure_name)


if __name__ == "__main__":
    main()
