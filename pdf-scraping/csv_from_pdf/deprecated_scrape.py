"""
Filename: scrape.py
Modified: 2019-06-07
Author: David Oniani
E-mail: onianidavid@gmail.com

License:
    The code is licensed under GNU General Public License v3.0.
    Please read the LICENSE file in this distribution for details
    regarding the licensing of this code.

Description:
    This is a description of the file.
"""

from typing import List, Dict

import os
import csv
import pdftotext


def pdf_scraper(filename: str, categories: Dict[str, int]) -> List[List[str]]:
    """Scraper to get the data out of PDF files

    Parameters:
        filename: Specifies a name of the PDF file to be scraped
        categories: Specifies a name-start-index mapping
    """
    with open(filename, "rb") as file:
        pdf = pdftotext.PDF(file)
        page = pdf[0]

    # Nicely formatted page data
    page_data = [line.strip() for line in page.split("\n")]

    # This is a dictionary of CSV name-value pairs
    contents = dict(zip(list(categories), ["N/A"] * len(categories)))

    # Populate the dicitonary
    for line in page_data:
        for key, value in categories.items():
            if key in line:
                contents[key] = line[value:].strip()

    return list(contents.values())


def main() -> None:
    """This is a main function."""
    # All category names mapped to the start index of the data related to it
    categories = {"Ad ID": 6,
                  "Ad Landing Page": 16,
                  "Ad Targeting Location": 23,
                  "Excluded Connections": 22,
                  "Age": 5,
                  "Language": 10,
                  "Placements": 12,
                  "Ad Impressions": 15,
                  "Ad Clicks": 10,
                  "Ad Spend": 9,
                  "Ad Creation Date": 17}

    # Get the list of keys out of the dicitonary
    csv_data = [list(categories)]

    # Directory name
    directory = "./data/..."

    for filename in os.listdir(directory):
        csv_data.append(pdf_scraper(f"{directory}{filename}", categories))

    with open("data.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)


if __name__ == "__main__":
    main()
