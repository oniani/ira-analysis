"""
Filename: age_targeted.py
Date: 2019-08-11 08:46:39 PM
Author: David Oniani
E-mail: onianidavid@gmail.com

License:
    The code is licensed under GNU General Public License v3.0.
    Please read the LICENSE file in this distribution for details
    regarding the licensing of this code.

Description:
    Find out the most common ages that were targeted.
"""

from collections import Counter

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from barchart_labeling import show_values_on_bars


def main() -> None:
    """The main function."""
    sns.set(
        color_codes=True, rc={"figure.figsize": (15.0, 9.0)}, style="darkgrid"
    )

    ages = []
    labels = []

    data = pd.read_csv(
        "../data/csv/all/all.csv", na_filter=False, thousands=","
    )

    most_common_ages = Counter(data["Age"]).most_common()

    # Clean the data

    # Cleanup step 1
    del most_common_ages[4]
    most_common_ages[0] = ("18 - 65+", 2298 + 60)

    # Cleanup step 2
    most_common_ages[11] = ("13 - 30", 25)

    # Cleanup step 3
    del most_common_ages[14]
    most_common_ages[12] = ("15 - 25", 24 + 20)

    # Cleanup step 4
    del most_common_ages[24]
    most_common_ages[5] = ("14 - 40", 37 + 8)

    # Cleanup step 5
    most_common_ages[24] = ("14 - 17", 8)

    # Cleanup step 6
    most_common_ages[25] = ("45 - 64", 8)

    # Cleanup step 7
    most_common_ages[26] = ("17 - 65", 8)

    # Cleanup step 8
    del most_common_ages[28]
    most_common_ages[20] = ("25 - 65+", 10 + 7)

    # Cleanup step 9
    del most_common_ages[30]
    most_common_ages[0] = ("18 - 65+", 2358 + 6)

    # Cleanup step 10
    del most_common_ages[37]
    most_common_ages[0] = ("18 - 65+", 2364 + 4)

    # Cleanup step 11
    del most_common_ages[54]
    most_common_ages[0] = ("18 - 65+", 2368 + 1)

    # Cleanup step 12
    del most_common_ages[62]
    most_common_ages[2] = ("16 - 65+", 355 + 1)

    # Cleanup step 13
    del most_common_ages[62]
    most_common_ages[12] = ("15 - 25", 44 + 1)

    # Cleanup step 14
    del most_common_ages[62]
    most_common_ages[0] = ("18 - 65+", 2369 + 1)

    del most_common_ages[48]
    most_common_ages[4] = ("18 - 51", 48 + 2)

    age_dictionary = {i: 0 for i, _ in most_common_ages}
    for age, number in most_common_ages:
        age_dictionary[age] += number

    # Get TOP 10 results
    results = Counter(age_dictionary).most_common(10)

    labels = [x for x, _ in results]
    numbers = [y for _, y in results]

    # Plot and save the barchart
    _, _ = plt.subplots(1, 1)
    sns_plot = sns.barplot(numbers, labels)
    sns_plot.set_title("TOP 10 Targeted Audience Ages")
    show_values_on_bars(sns_plot, space=max(numbers) * 0.5 / 100)
    figure = sns_plot.get_figure()
    figure_name = "barchart_targeted_age.png"
    figure.savefig(figure_name)


if __name__ == "__main__":
    main()
