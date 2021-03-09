"""
Filename: ad_spend.py
Date: 2019-08-19 01:12:19 PM
Author: David Oniani
E-mail: onianidavid@gmail.com

License:
    The code is licensed under MIT License. Please read the LICENSE file in
    this distribution for details regarding the licensing of this code.

Description:
    Calculating ad spent.
"""

import argparse
import pandas as pd


def main() -> None:
    """The main function."""
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Process the arguments.")

    # Number of slots in the Galton board
    parser.add_argument("--filename", type=str, help="specify a filename")

    # Get the argparse.Namespace class to obtain the values of the arguments
    args = parser.parse_args()

    # Work with data
    data = pd.read_csv(args.filename, na_filter=False, thousands=",")

    # Has to be converted to list due to bulk replacements
    ad_spend = list(data["Ad Spend"])

    for index, entry in enumerate(ad_spend):
        if entry.count(".") == 2:
            ad_spend[index] = ad_spend[index].replace(".", "", 1)

    ad_spend_RU = sum(
        [
            float(
                x.replace(",", "")
                .replace(" ", "")
                .replace(";", "")
                .replace("RUB", "")
            )
            for x in ad_spend
            if x != "None" and "RUB" in x
        ]
    )

    ad_spend_USD = sum(
        [
            float(
                x.replace(",", "")
                .replace(" ", "")
                .replace(";", "")
                .replace("USD", "")
            )
            for x in ad_spend
            if x != "None" and "USD" in x
        ]
    )

    print(f"RUB {ad_spend_RU:.3f}, ${ad_spend_USD:.3f}")


if __name__ == "__main__":
    main()
