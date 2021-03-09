"""
Filename: normalize.py
Modified: 2019-06-14
Author: David Oniani
E-mail: onianidavid@gmail.com

License:
    The code is licensed under MIT License. Please read the LICENSE file in
    this distribution for details regarding the licensing of this code.

Description:
    A normalization of the files in the CSV format.
"""

from typing import List

import csv
import argparse


def normalize(filename: str) -> List[List[str]]:
    """A function for CSV normalization.

    Parameters:
        filename: A filename of the CSV file to be normalized.
    """
    with open(filename, "r") as file:
        reader = csv.reader(file)
        data = [line for line in reader]

    new_data = []

    for row in data:
        new_row = []

        for item in row:
            if len(item) > 0:
                if item[-1] == "\n":
                    new_row.append(item[:-1].strip())
                else:
                    new_row.append(item.strip())

        new_data.append(new_row)

    return new_data


def main() -> None:
    """The main function."""
    parser = argparse.ArgumentParser(description="Process the arguments.")

    parser.add_argument("--filename", type=str, help="specifies the filename.")

    args = parser.parse_args()

    filename = args.filename

    with open("./test.csv", "w") as test:
        writer = csv.writer(test)
        writer.writerows(normalize(filename))


if __name__ == "__main__":
    main()
