"""
Filename: regression.py
Modified: 2019-06-14
Author: David Oniani
E-mail: onianidavid@gmail.com

License:
    The code is licensed under GNU General Public License v3.0.
    Please read the LICENSE file in this distribution for details
    regarding the licensing of this code.

Description:
    A program to plot a linear regression.
"""

import argparse

import pandas as pd
import seaborn as sns
import scipy.stats as stats
import matplotlib.pyplot as plt


def plot_regression(
    filepath: str,
    independent: str,
    dependent: str,
    title: str = "Linear Regression",
) -> None:
    """The function to visualize scatterplots.

    Parameters:
        filepath: specifies the filepath
        independent: specifies the name of the independent variable
        dependent: specifies the name of the dependent variable
        title: specifies the title of the linear regression
    """
    sns.set(
        color_codes=True, rc={"figure.figsize": (15.0, 9.0)}, style="darkgrid"
    )

    reader = pd.read_csv(filepath, thousands=",", na_filter=False)
    columns = reader[[independent, dependent]]

    columns = [
        [float(str(value).replace(",", "")) for value in values]
        for values in columns.values
    ]

    columns = pd.DataFrame.from_records(
        columns, columns=[independent, dependent]
    )

    columns = columns.reset_index(drop=True)

    correlation_coefficient = stats.pearsonr(
        reader[independent], reader[dependent]
    )[0]

    sns_plot = sns.regplot(x=independent, y=dependent, data=columns)
    sns_plot.set_title(title)
    sns_plot.annotate(
        f"r = {correlation_coefficient:.3f}",
        xy=(min(reader[independent]), max(reader[dependent])),
        fontsize=16,
        weight="bold",
    )

    figure = sns_plot.get_figure()
    figure_name = "-".join(map(lambda x: x.lower(), title.split()))
    figure.savefig(figure_name)


def main() -> None:
    """The main function."""
    parser = argparse.ArgumentParser(description="Process the arguments.")

    parser.add_argument("--filepath", type=str, help="specifies the filepath.")

    parser.add_argument(
        "--independent",
        type=str,
        help="specifies the name of the independent variable.",
    )

    parser.add_argument(
        "--dependent",
        type=str,
        help="specifies the name of the dependent variable.",
    )

    parser.add_argument(
        "--title",
        type=str,
        help="specifies the title of the linear regression.",
    )

    args = parser.parse_args()

    filepath = args.filepath
    independent = args.independent
    dependent = args.dependent
    title = args.title

    plot_regression(filepath, independent, dependent, title)


if __name__ == "__main__":
    main()
