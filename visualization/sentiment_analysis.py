#!/usr/bin/env python3
# encoding: UTF-8
"""
Filename: sentiment_analysis.py
Date: 2019-09-05 07:35:09 PM
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
import textblob as tb


def analyze_negativity(data, subjectivity) -> float:
    """Determine sentiment."""

    data = [text.replace("\n", " ") for text in data if text != "N/A"]

    neg_polarity = 0
    for text in data:
        analysis = tb.TextBlob(text)
        if (
            analysis.sentiment.polarity < 0
            and analysis.sentiment.subjectivity < subjectivity
        ):
            neg_polarity += 1

    print(f"Negative: {neg_polarity}")


def sentiment_stats_numerical(data) -> None:
    """Determine sentiment."""

    data = [text.replace("\n", " ") for text in data if text != "N/A"]

    pos_polarity = 0
    neg_polarity = 0
    neu_polarity = 0
    for text in data:
        analysis = tb.TextBlob(text)
        if analysis.sentiment.polarity > 0:
            pos_polarity += 1
        elif analysis.sentiment.polarity < 0:
            neg_polarity += 1
        else:
            neu_polarity += 1

    print(f"Positive: {pos_polarity}")
    print(f"Negative: {neg_polarity}")
    print(f"Neutral:  {neu_polarity}")


def main() -> None:
    """The main function."""

    print("Sentiment Analysis")
    print("==================\n")

    # Everything altogether
    data_all = pd.read_csv(
        "../data/csv/all/all.csv", na_filter=False, thousands=","
    )["Ad Text"]

    print("All Years")
    sentiment_stats_numerical(data_all)

    print("\n==================")

    # Year 2015
    data_2015 = pd.read_csv(
        "../data/csv/by-year/year-2015.csv", na_filter=False, thousands=","
    )["Ad Text"]

    print("\nYear 2015")
    sentiment_stats_numerical(data_2015)

    # Year 2016
    data_2016 = pd.read_csv(
        "../data/csv/by-year/year-2016.csv", na_filter=False, thousands=","
    )["Ad Text"]

    print("\nYear 2016")
    sentiment_stats_numerical(data_2016)

    # Year 2017
    data_2017 = pd.read_csv(
        "../data/csv/by-year/year-2017.csv", na_filter=False, thousands=","
    )["Ad Text"]

    print("\nYear 2017")
    sentiment_stats_numerical(data_2017)

    print("\n==================")

    # Year 2015 Quarter 2
    data_2015_q2 = pd.read_csv(
        "../data/csv/year-2015/2015-Quarter-2.csv",
        na_filter=False,
        thousands=",",
    )["Ad Text"]

    print("\nYear 2015 Quarter 2")
    sentiment_stats_numerical(data_2015_q2)

    # Year 2015 Quarter 3
    data_2015_q3 = pd.read_csv(
        "../data/csv/year-2015/2015-Quarter-3.csv",
        na_filter=False,
        thousands=",",
    )["Ad Text"]

    print("\nYear 2015 Quarter 3")
    sentiment_stats_numerical(data_2015_q3)

    # Year 2015 Quarter 4
    data_2015_q4 = pd.read_csv(
        "../data/csv/year-2015/2015-Quarter-4.csv",
        na_filter=False,
        thousands=",",
    )["Ad Text"]

    print("\nYear 2015 Quarter 4")
    sentiment_stats_numerical(data_2015_q4)

    print("\n==================")

    # Year 2016 Quarter 1
    data_2016_q1 = pd.read_csv(
        "../data/csv/year-2016/2016-Quarter-1.csv",
        na_filter=False,
        thousands=",",
    )["Ad Text"]

    print("\nYear 2016 Quarter 1")
    sentiment_stats_numerical(data_2016_q1)

    # Year 2016 Quarter 2
    data_2016_q2 = pd.read_csv(
        "../data/csv/year-2016/2016-Quarter-2.csv",
        na_filter=False,
        thousands=",",
    )["Ad Text"]

    print("\nYear 2016 Quarter 2")
    sentiment_stats_numerical(data_2016_q2)

    # Year 2016 Quarter 3
    data_2016_q3 = pd.read_csv(
        "../data/csv/year-2016/2016-Quarter-3.csv",
        na_filter=False,
        thousands=",",
    )["Ad Text"]

    print("\nYear 2016 Quarter 3")
    sentiment_stats_numerical(data_2016_q3)

    # Year 2016 Quarter 4
    data_2016_q4 = pd.read_csv(
        "../data/csv/year-2016/2016-Quarter-4.csv",
        na_filter=False,
        thousands=",",
    )["Ad Text"]

    print("\nYear 2016 Quarter 4")
    sentiment_stats_numerical(data_2016_q4)

    # Year 2017 Quarter 1
    data_2017_q1 = pd.read_csv(
        "../data/csv/year-2017/2017-Quarter-1.csv",
        na_filter=False,
        thousands=",",
    )["Ad Text"]

    print("\n==================")

    print("\nYear 2017 Quarter 1")
    sentiment_stats_numerical(data_2017_q1)

    # Year 2017 Quarter 2 April
    data_2017_q2_a = pd.read_csv(
        "../data/csv/year-2017/2017-Quarter-2-April.csv",
        na_filter=False,
        thousands=",",
    )["Ad Text"]

    print("\nYear 2017 Quarter 2 April")
    sentiment_stats_numerical(data_2017_q2_a)

    # Year 2017 Quarter 2 May
    data_2017_q2_m = pd.read_csv(
        "../data/csv/year-2017/2017-Quarter-2-May.csv",
        na_filter=False,
        thousands=",",
    )["Ad Text"]

    print("\nYear 2017 Quarter 2 May")
    sentiment_stats_numerical(data_2017_q2_m)

    # Year 2017 Quarter 3
    data_2017_q3 = pd.read_csv(
        "../data/csv/year-2017/2017-Quarter-3.csv",
        na_filter=False,
        thousands=",",
    )["Ad Text"]

    print("\nYear 2017 Quarter 3")
    sentiment_stats_numerical(data_2017_q3)

    ###########################################################################

    # Negativity

    print("\nAnalyzing Negativity")
    print("==================\n")

    subjectivity = 1.0
    print(f"Minimum Level of Subjectivity is {subjectivity}\n")

    print("Year 2015")
    analyze_negativity(data_2015, subjectivity)

    print("\nYear 2016")
    analyze_negativity(data_2016, subjectivity)

    print("\nYear 2017")
    analyze_negativity(data_2017, subjectivity)

    ###########################################################################

    subjectivity = 0.75
    print(f"\nMinimum Level of Subjectivity is {subjectivity}\n")

    print("Year 2015")
    analyze_negativity(data_2015, subjectivity)

    print("\nYear 2016")
    analyze_negativity(data_2016, subjectivity)

    print("\nYear 2017")
    analyze_negativity(data_2017, subjectivity)

    ###########################################################################

    subjectivity = 0.5
    print(f"\nMinimum Level of Subjectivity is {subjectivity}\n")

    print("Year 2015")
    analyze_negativity(data_2015, subjectivity)

    print("\nYear 2016")
    analyze_negativity(data_2016, subjectivity)

    print("\nYear 2017")
    analyze_negativity(data_2017, subjectivity)

    ###########################################################################

    subjectivity = 0.25
    print(f"\nMinimum Level of Subjectivity is {subjectivity}\n")

    print("Year 2015")
    analyze_negativity(data_2015, subjectivity)

    print("\nYear 2016")
    analyze_negativity(data_2016, subjectivity)

    print("\nYear 2017")
    analyze_negativity(data_2017, subjectivity)

    ###########################################################################

    subjectivity = 0.15
    print(f"\nMinimum Level of Subjectivity is {subjectivity}\n")

    print("Year 2015")
    analyze_negativity(data_2015, subjectivity)

    print("\nYear 2016")
    analyze_negativity(data_2016, subjectivity)

    print("\nYear 2017")
    analyze_negativity(data_2017, subjectivity)

    ###########################################################################

    subjectivity = 0.10
    print(f"\nMinimum Level of Subjectivity is {subjectivity}\n")

    print("Year 2015")
    analyze_negativity(data_2015, subjectivity)

    print("\nYear 2016")
    analyze_negativity(data_2016, subjectivity)

    print("\nYear 2017")
    analyze_negativity(data_2017, subjectivity)

    ###########################################################################

    subjectivity = 0.05
    print(f"\nMinimum Level of Subjectivity is {subjectivity}\n")

    print("Year 2015")
    analyze_negativity(data_2015, subjectivity)

    print("\nYear 2016")
    analyze_negativity(data_2016, subjectivity)

    print("\nYear 2017")
    analyze_negativity(data_2017, subjectivity)

    ###########################################################################

    print("\nCalculating Sentiment Values and Subjectivities")
    print("===============================================\n")

    print("Treating everything as a single text (Years 2015, 2016, 2017)")
    polarity, subjectivity = tb.TextBlob(" ".join(data_all)).sentiment
    print(f"Polarity:     {polarity}")
    print(f"Subjectivity: {subjectivity}\n")

    print("Treating everything as a single text (Year 2015)")
    polarity, subjectivity = tb.TextBlob(" ".join(data_2015)).sentiment
    print(f"Polarity:     {polarity}")
    print(f"Subjectivity: {subjectivity}\n")

    print("Treating everything as a single text (Year 2016)")
    polarity, subjectivity = tb.TextBlob(" ".join(data_2016)).sentiment
    print(f"Polarity:     {polarity}")
    print(f"Subjectivity: {subjectivity}\n")

    print("Treating everything as a single text (Year 2017)")
    polarity, subjectivity = tb.TextBlob(" ".join(data_2017)).sentiment
    print(f"Polarity:     {polarity}")
    print(f"Subjectivity: {subjectivity}")


if __name__ == "__main__":
    main()
