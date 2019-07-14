"""
Filename: scrape.py
Modified: 2019-06-17
Author: David Oniani
E-mail: onianidavid@gmail.com

License:
    The code is licensed under GNU General Public License v3.0.
    Please read the LICENSE file in this distribution for details
    regarding the licensing of this code.

Description:
    Checking CSV files for validity.
    This is a very crude checker.
    It is not:
        - Efficient
        - Written in idiomatic Python3
        - PEP 8-compliant
        - Beautiful (code-wise)
        - Using a unit testing library like pytest
"""

import os
import pdftotext

import pandas as pd


pd.set_option("display.max_rows", 50000)
pd.set_option("display.max_columns", 50000)
pd.set_option("display.width", 50000)


def check_ad_id(path: str):
    """A simple checker."""
    pdf_text = []
    for file in os.listdir(path):
        with open(f"{path}/{file}", "rb") as pdf:
            data = pdftotext.PDF(pdf)[0]
        pdf_text.append(data)

    ad_id = []
    for datapoint in pdf_text:
        idx = datapoint.find("Ad ID")
        ad_id.append(datapoint[idx + 5 : idx + 10].strip("\n").strip())
    ad_id = pd.DataFrame(ad_id)
    ad_id.style.hide_index()
    return ad_id


def main() -> None:
    """The main function."""
    # 2015
    _2015 = [
        "/Users/oniani/Documents/csv_from_pdf/data/year-2015/2015-Quarter-2/",
        "/Users/oniani/Documents/csv_from_pdf/data/year-2015/2015-Quarter-3/",
        "/Users/oniani/Documents/csv_from_pdf/data/year-2015/2015-Quarter-4/",
    ]

    # 2016
    _2016 = [
        "/Users/oniani/Documents/csv_from_pdf/data/year-2016/2016-Quarter-1/",
        "/Users/oniani/Documents/csv_from_pdf/data/year-2016/2016-Quarter-2/",
        "/Users/oniani/Documents/csv_from_pdf/data/year-2016/2016-Quarter-3/",
        "/Users/oniani/Documents/csv_from_pdf/data/year-2016/2016-Quarter-4/",
    ]

    # 2017
    _2017 = [
        "/Users/oniani/Documents/csv_from_pdf/data/year-2017/2017-Quarter-1/",
        "/Users/oniani/Documents/csv_from_pdf/data/year-2017/2017-Quarter-2-April/",
        "/Users/oniani/Documents/csv_from_pdf/data/year-2017/2017-Quarter-2-May/",
        "/Users/oniani/Documents/csv_from_pdf/data/year-2017/2017-Quarter-3/",
    ]

    # #########################################################################
    # C H E C K I N
    # #########################################################################

    print(check_ad_id(_2015[1]))


if __name__ == "__main__":
    main()
