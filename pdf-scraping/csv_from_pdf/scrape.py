"""
Filename: scrape.py
Modified: 2019-06-09
Author: David Oniani
E-mail: onianidavid@gmail.com

License:
    The code is licensed under GNU General Public License v3.0.
    Please read the LICENSE file in this distribution for details
    regarding the licensing of this code.

Description:
    This is a Python program that parses the PDF file of the specific
    format. The format was specified at the Direction of Ranking Member
    of the US House Permanent Select Committee on Intelligence.
"""

from typing import List, Dict

import os
import csv
import argparse
import pdftotext


def scrape_by_keyword(text: List[str], keyword: str, until: str) -> str:
    """A parsing function.

    In general, it is a terrible idea to have a mutable keyword
    formal parameter, but we are aware of it here.
    """
    text = [
        line.strip() + "\n" for line in text.strip().split("\n") if line != ""
    ]

    parsed = ""

    for index, line in enumerate(text):
        if keyword in line and until not in line:
            parsed = line[line.find(keyword) + len(keyword) + 1 :]
            for j in range(index + 1, len(text)):
                if until not in text[j]:
                    parsed += text[j]
                else:
                    return parsed

        # Probably the trickiest bit: keywords can be on the same line
        elif keyword in line and until in line:
            keyword_idx = line.find(keyword)
            until_idx = line.find(until)
            parsed += line[len(keyword) + keyword_idx + 2 : until_idx - 2]
            return parsed

    return parsed


def get_available_keywords(text: str, keywords: List[str]) -> List[str]:
    """A function to get the list of available keywords

    In general, it is a terrible idea to have a mutable keyword
    formal parameter, but we are aware of it here.

    Parameters:
        text: A text to be parsed
        categories: A list of available keywords
    """
    sequence = []

    for keyword in keywords:
        if keyword in text:
            sequence.append(keyword)

    return sequence


def get_data(filepath: str, categories: Dict[str, str]) -> List[str]:
    """A function to get the data out.

    In general, it is a terrible idea to have a mutable keyword
    formal parameter, but we are aware of it here.

    Parameters:
        full_filename: A full filepath to the file
        categories: Categories
    """
    with open(filepath, "rb") as file:
        page = pdftotext.PDF(file)[0]

    keywords = get_available_keywords(page, categories)
    all_keywords = list(categories.keys())
    unavailable_keys = []

    for key in all_keywords:
        if key not in keywords:
            unavailable_keys.append(key)

    for key in unavailable_keys:
        categories[key] = "N/A"

    for keyword, until in zip(keywords, keywords[1:]):
        categories[keyword] = scrape_by_keyword(page, keyword, until)

    return [filepath] + list(categories.values())


def main() -> None:
    """The main function."""
    parser = argparse.ArgumentParser(description="Process the arguments.")

    parser.add_argument(
        "--dir", type=str, default=".", help="specify the directory."
    )

    args = parser.parse_args()

    categories = {
        "Ad ID": "N/A",
        "Ad Text": "N/A",
        "Ad Landing Page": "N/A",
        "Ad Targeting Location": "N/A",
        "Excluded Connections": "N/A",
        "Age": "N/A",
        "Language": "N/A",
        "Placements": "N/A",
        "People Who Match": "N/A",
        "Friends of connections": "N/A",
        "Ad Impressions": "N/A",
        "Ad Clicks": "N/A",
        "Ad Spend": "N/A",
        "Ad Creation Date": "N/A",
        "Ad End Date": "N/A",
        "Redactions Completed": "True (this is just a placeholder)",
    }

    directory = args.dir

    # Make sure that the backslash in the end does not crash the program
    if directory[-1] == "/":
        directory = directory[:-1]

    csv_data = [list(categories.keys())]

    for filename in os.listdir(directory):
        csv_data.append(get_data(f"{directory}/{filename}", categories))

    with open("data.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)


if __name__ == "__main__":
    main()
