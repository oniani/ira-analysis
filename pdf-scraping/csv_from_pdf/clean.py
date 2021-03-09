"""
Filename: clean.py
Created:  2019/06/21 07:27:12 AM
Author: David Oniani
E-mail: onianidavid@gmail.com

License:
    The code is licensed under MIT License. Please read the LICENSE file in
    this distribution for details regarding the licensing of this code.

Description:
    This program does a generic as well as the data-specific
    cleanup of the CSV files.
"""

import csv
import argparse


def main() -> None:
    """The main function."""
    # Parse the command line argument(s)
    parser = argparse.ArgumentParser(description="Process the arguments.")
    parser.add_argument("--path", type=str, help="specifies the path.")
    args = parser.parse_args()
    path = args.path

    # Read the data
    with open(path, "r") as file:
        data = csv.reader(file)
        data = list(data)

    # Remove extra spaces in the beginning and in the end
    data = [[entry.strip() for entry in row] for row in data]

    # Join the link if it is split into multiple pieces (N/A for empty cells)
    for row in data[1:]:
        row[2] = row[2].replace(" ", "")
        if row[2] == "" or row[2] == " ":
            row[2] = "N/A"

    # Replace https:H in links with https:// (if such parsing error is present)
    for row in data[1:]:
        if row[2].find("https:H") == 0:
            row[2] = f"https://{row[2][7:]}"

    # Format the Ad Spend column nicely (the way it is in the PDF files)
    for row in data[1:]:
        if row[12].find("RUB") == 0:
            row[12] = f"{row[12][3:]} RUB"

    # Write the data
    with open(path, "w") as file:
        writer = csv.writer(file)
        writer.writerows(data)


if __name__ == "__main__":
    main()
