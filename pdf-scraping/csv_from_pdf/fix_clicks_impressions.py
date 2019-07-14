"""
Filename: template.py
Modified: YYYY-MM-DD
Author: David Oniani
E-mail: onianidavid@gmail.com

License:
    The code is licensed under GNU General Public License v3.0.
    Please read the LICENSE file in this distribution for details
    regarding the licensing of this code.

Description:
    This is a description of the file.
"""

import argparse
import csv


def main() -> None:
    parser = argparse.ArgumentParser(description="Process the arguments.")
    parser.add_argument("--path", type=str, default=".", help="specify the directory.")
    args = parser.parse_args()
    path = args.path

    reader = csv.reader(open(path, "r"))
    data = list(reader)

    for row in data[1:]:
        if "." in row[10]:
            row[10] = row[10].replace(".", ",")

        if "." in row[11]:
            row[11] = row[11].replace(".", ",")

        if " " in row[10]:
            row[10] = row[10].replace(" ", "")

        if " " in row[11]:
            row[11] = row[11].replace(" ", "")

        if ";" in row[10]:
            row[10] = row[10].replace(";", ",")

        if ";" in row[11]:
            row[11] = row[11].replace(";", ",")

        if "\n" in row[10]:
            row[10] = row[10].replace("\n", "")

        if "\n" in row[11]:
            row[11] = row[11].replace("\n", "")

        if "O" in row[10]:
            row[10] = row[10].replace("O", "0")

        if "O" in row[11]:
            row[11] = row[11].replace("O", "0")

    writer = csv.writer(open(path, "w"))
    writer.writerows(data)


if __name__ == "__main__":
    main()
