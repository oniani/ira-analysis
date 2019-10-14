#!/usr/bin/env python3
# encoding: UTF-8

"""
Filename: test_correlation_ad_spend_text_length.py
Date: 2019-10-13 08:24:24 PM
Author: David Oniani
E-mail: onianidavid@gmail.com

License:
    The code is licensed under GNU General Public License v3.0.
    Please read the LICENSE file in this distribution for details
    regarding the licensing of this code.

Description:
    This is a description of the file.
"""

import pandas as pd
import seaborn as sns
import scipy.stats as stats


def main() -> None:
    """The main function."""

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

    m, b, corr, p_value, std_err = stats.linregress(
        list(map(float, ad_text_lengths)), list(map(float, ad_spend_RU))
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

    print()

    ###########################################################################

    print("------------------------------------------------------------------")
    print("| USD")
    print("------------------------------------------------------------------")

    m, b, corr, p_value, std_err = stats.linregress(
        list(map(float, ad_text_lengths_USD)), list(map(float, ad_spend_USD))
    )
    print(m, b, corr, p_value, std_err)

    print("Slope", m)
    print("Intercept", b)
    print("R-squared", corr ** 2)
    print("P-value", p_value)
    print("Standard Error", std_err)


if __name__ == "__main__":
    main()
