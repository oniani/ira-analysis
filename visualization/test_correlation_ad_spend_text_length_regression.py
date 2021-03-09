#!/usr/bin/env python3
# encoding: UTF-8

"""
Filename: test_correlation_ad_spend_text_length_regression.py
Date: 2019-10-14 08:06:52 AM
Author: David Oniani
E-mail: onianidavid@gmail.com

License:
    The code is licensed under MIT License. Please read the LICENSE file in
    this distribution for details regarding the licensing of this code.

Description:
    This is a description of the file.
"""

import math

import pandas as pd
import seaborn as sns
import scipy.stats as stats


def main() -> None:
    """The main function."""

    # Seaborn settings
    sns.set(
        color_codes=True, rc={"figure.figsize": (15.0, 9.0)}, style="darkgrid"
    )

    # Read in the data
    data = pd.read_csv(
        "./../data/csv/all/all.csv", na_filter=False, thousands=","
    )

    # Independent
    ad_text_lengths = list(map(len, data["Ad Text"]))

    # Dependent
    ad_spend = data["Ad Spend"]

    # Zip these two up
    ad_text_ad_spend = list(zip(ad_text_lengths, ad_spend))

    ad_text_ad_spend_USD = [
        (text, spend)
        for text, spend in ad_text_ad_spend
        if spend is not None
        and spend != "None"
        and spend != ""
        and spend != 0
        and spend != 0.0
        and "USD" in spend
    ]

    ad_text_ad_spend = [
        (text, spend)
        for text, spend in ad_text_ad_spend
        if spend is not None
        and spend != "None"
        and spend != ""
        and spend != 0
        and spend != 0.0
        and "RUB" in spend
    ]

    ad_text_lengths = [tup[0] for tup in ad_text_ad_spend]
    ad_spend = [tup[1] for tup in ad_text_ad_spend]

    ad_text_lengths_USD = [tup[0] for tup in ad_text_ad_spend_USD]
    ad_spend_USD = [tup[1] for tup in ad_text_ad_spend_USD]

    # Clean up
    for index, entry in enumerate(ad_spend):
        if entry.count(".") == 2:
            ad_spend[index] = ad_spend[index].replace(".", "", 1)

    for index, entry in enumerate(ad_spend_USD):
        if entry.count(".") == 2:
            ad_spend_USD[index] = ad_spend_USD[index].replace(".", "", 1)

    ad_spend_RU = [
        float(
            x.replace(",", "")
            .replace(" ", "")
            .replace(";", "")
            .replace("RUB", "")
        )
        for x in ad_spend
        if x != "None" and "RUB" in x
    ]

    ad_spend_USD = [
        float(
            x.replace(",", "")
            .replace(" ", "")
            .replace(";", "")
            .replace("USD", "")
        )
        for x in ad_spend_USD
        if x != "None" and "USD" in x
    ]

    assert (
        len(list(ad_spend_RU)) == len(list(ad_spend)) == len(ad_text_lengths)
    )

    # Normalize
    ad_text_lengths = list(map(float, ad_text_lengths))
    ad_spend_RU = list(map(float, ad_spend_RU))

    min_val_text = min([i for i in ad_text_lengths if i > 0]) / 2.0
    min_val_spend_RU = min([i for i in ad_text_lengths if i > 0]) / 2.0

    for idx, val in enumerate(ad_text_lengths):
        if val == 0:
            ad_text_lengths[idx] = min_val_text

    for idx, val in enumerate(ad_spend_RU):
        if val == 0:
            ad_spend_RU[idx] = min_val_spend_RU

    ad_text_lengths = list(map(math.log, map(float, ad_text_lengths)))
    ad_spend_RU = list(map(math.log, map(float, ad_spend_RU)))

    m, b, corr, p_value, std_err = stats.linregress(
        ad_text_lengths, ad_spend_RU
    )

    print("------------------------------------------------------------------")
    print("| RUB")
    print("------------------------------------------------------------------")

    print(m, b, corr, p_value, std_err)

    print("Slope", m)
    print("Intercept", b)
    print("R-squared", corr ** 2)
    print("P-value", p_value)
    print("Standard Error", std_err)

    # Create a dataframe with log transform
    columns = pd.DataFrame(
        {
            "Log Ad Text Length": ad_text_lengths,
            "Log Money Spent (RUB)": ad_spend_RU,
        }
    )

    columns = columns.reset_index(drop=True)

    sns_plot = sns.regplot(
        x="Log Ad Text Length", y="Log Money Spent (RUB)", data=columns
    )
    sns_plot.set_title("Money Spent VS Ad Text Length (Log-transformed)")

    figure = sns_plot.get_figure()
    figure_name = "ad_spend_text_length_regression.png"
    figure.savefig("ad_spend_text_length_regression.png")


if __name__ == "__main__":
    main()
