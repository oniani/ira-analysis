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
        - Using a unit testing library like pytest or hypothesis
"""

import os
import pdftotext

import pandas as pd


def check_num_of_lines(path_csv: str, path_pdf: str) -> bool:
    """Checks whether all the files were parsed.

    Parameters:
        path_csv: path to the CSV file
        path_pdf: path to the PDF file(s)
    """
    return len(os.listdir(path_pdf)) == len(pd.read_csv(path_csv))


def verify_ad_end_date(path_csv: str, path_pdf: str) -> bool:
    """Checks whether the Ad End Date column was parsed correctly.

    Unfortunately, the parsing program was defective.
    pdftotext library also had problems parsing PDF files.
    This function is provided in order to assist in manual
    removal of redundant Ad End Dates.

    Parameters:
        path_csv: path to the CSV file
        path_pdf: path to the PDF file(s)
    """
    rows = pd.read_csv(path_csv, keep_default_na=False)

    path_csv = path_csv.lower()

    pdf_text = []
    for filename in os.listdir(path_pdf):
        with open(f"{path_pdf}/{filename}", "rb") as file:
            pdf_text.append(pdftotext.PDF(file)[0])

    without_ad_end_date = []
    for text in pdf_text:
        if "Ad End Date" not in text:
            idx = text.find("Ad ID")
            # 11 characters are enough
            without_ad_end_date.append(text[idx + 5 : idx + 15].strip())

    if path_csv == "../data/csv/year-2015/2015-quarter-2.csv":
        for _, row in rows.iterrows():
            if str(row["Ad ID"]) in without_ad_end_date:
                if str(row["Ad End Date"]) != "N/A":
                    return False

            # Note that #3394, for some reason, was not parsed by pdftotext
            elif (
                str(row["Ad End Date"]) == "N/A"
                and str(row["Ad ID"]) != "3394"
            ):
                return False

    elif path_csv == "../data/csv/year-2015/2015-quarter-3.csv":
        for _, row in rows.iterrows():
            # Note that #131 is not parsed by pdftotext (as we only parse the first page)
            if (
                str(row["Ad ID"]) in without_ad_end_date
                and str(row["Ad ID"]) != "131"
            ):
                if str(row["Ad End Date"]) != "N/A":
                    return False

            elif str(row["Ad End Date"]) == "N/A":
                return False

    elif path_csv == "../data/csv/year-2016/2016-quarter-2.csv":
        for _, row in rows.iterrows():
            # Note that #131 is not parsed by pdftotext (as we only parse the first page)
            if (
                str(row["Ad ID"]) in without_ad_end_date
                and str(row["Ad ID"]) != "131"
            ):
                if str(row["Ad End Date"]) != "N/A":
                    return False

            # This is all because pdftotext fails to parse correctly
            elif str(row["Ad End Date"]) == "N/A" and str(
                row["Ad ID"]
            ) not in {
                "3499",
                "3495",
                "3496",
                "3490",
                "3424",
                "3485",
                "3445",
                "3403",
                "3404",
                "3397",
                "3449",
                "3399",
                "3402",
                "3398",
                "3395",
                "3400",
                "3441",
                "3479",
                "3458",
                "3461",
                "3463",
                "3444",
                "3484",
                "3483",
                "3405",
                "3464",
                "3457",
                "3428",
            }:
                print(path_csv, path_pdf, "MISSING\n", row)
                return False

    elif path_csv == "../data/csv/year-2016/2016-quarter-4.csv":
        for _, row in rows.iterrows():
            # Note that #131 is not parsed by pdftotext (as we only parse the first page)
            if (
                str(row["Ad ID"]) in without_ad_end_date
                and str(row["Ad ID"]) != "131"
            ):
                if str(row["Ad End Date"]) != "N/A":
                    return False

            # This is all because pdftotext fails to parse correctly
            elif str(row["Ad End Date"]) == "N/A" and str(
                row["Ad ID"]
            ) not in {"2745", "3004", "2747", "2742"}:
                return False

    elif path_csv == "../data/csv/year-2017/2017-quarter-1.csv":
        for _, row in rows.iterrows():
            if str(row["Ad ID"]) in without_ad_end_date:
                if str(row["Ad End Date"]) != "N/A":
                    return False

            elif (
                str(row["Ad End Date"]) == "N/A"
                and str(row["Ad ID"]) != "3245"
            ):
                return False

    else:
        for _, row in rows.iterrows():
            if str(row["Ad ID"]) in without_ad_end_date:
                if str(row["Ad End Date"]) != "N/A":
                    # Debugging
                    print(
                        path_csv,
                        path_pdf,
                        "\033[0;31mMISSING N/A\033[0m\n\n",
                        row,
                    )
                    # return False

            elif str(row["Ad End Date"]) == "N/A":
                # Debugging
                print(
                    path_csv,
                    path_pdf,
                    "\033[0;31mREDUNDANT N/A\033[0m\n\n",
                    row,
                )
                # return False

    return True


def check_for_dupe_id(filename: str) -> bool:
    """Check if duplicate IDs are present"""
    data = list(pd.read_csv(open(filename, "r"))["Ad ID"])
    if len(data) == len(set(data)):
        return True
    print(f"\n{filename}\n")
    return False


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
    # Verify that the number of lines match!
    # #########################################################################

    # #########################################################################
    # Y E A R  2 0 1 5
    # #########################################################################

    # 2015 Quarter 2
    assert (
        check_num_of_lines(
            "../data/csv/year-2015/2015-Quarter-2.csv", _2015[0]
        )
        is True
    )

    # 2015 Quarter 3
    assert (
        check_num_of_lines(
            "../data/csv/year-2015/2015-Quarter-3.csv", _2015[1]
        )
        is True
    )

    # 2015 Quarter 4
    assert (
        check_num_of_lines(
            "../data/csv/year-2015/2015-Quarter-4.csv", _2015[2]
        )
        is True
    )

    # #########################################################################
    # Y E A R  2 0 1 6
    # #########################################################################

    # 2016 Quarter 1
    assert (
        check_num_of_lines(
            "../data/csv/year-2016/2016-Quarter-1.csv", _2016[0]
        )
        is True
    )

    # 2016 Quarter 2
    assert (
        check_num_of_lines(
            "../data/csv/year-2016/2016-Quarter-2.csv", _2016[1]
        )
        is True
    )

    # 2016 Quarter 3
    assert (
        check_num_of_lines(
            "../data/csv/year-2016/2016-Quarter-3.csv", _2016[2]
        )
        is True
    )

    # 2016 Quarter 4
    assert (
        check_num_of_lines(
            "../data/csv/year-2016/2016-Quarter-4.csv", _2016[3]
        )
        is True
    )

    # #########################################################################
    # Y E A R  2 0 1 7
    # #########################################################################

    # 2017 Quarter 1
    assert (
        check_num_of_lines(
            "../data/csv/year-2017/2017-Quarter-1.csv", _2017[0]
        )
        is True
    )

    # 2017 Quarter 2 April
    assert (
        check_num_of_lines(
            "../data/csv/year-2017/2017-Quarter-2-April.csv", _2017[1]
        )
        is True
    )

    # 2017 Quarter 2 May
    assert (
        check_num_of_lines(
            "../data/csv/year-2017/2017-Quarter-2-May.csv", _2017[2]
        )
        is True
    )

    # 2017 Quarter 3
    assert (
        check_num_of_lines(
            "../data/csv/year-2017/2017-Quarter-3.csv", _2017[3]
        )
        is True
    )

    # #########################################################################
    # Verify that Ad End Dates match!
    # #########################################################################

    # #########################################################################
    # Y E A R  2 0 1 5
    # #########################################################################

    # 2015 Quarter 2
    assert (
        verify_ad_end_date(
            "../data/csv/year-2015/2015-quarter-2.csv", _2015[0]
        )
        is True
    )

    # 2015 Quarter 3
    assert (
        verify_ad_end_date(
            "../data/csv/year-2015/2015-quarter-3.csv", _2015[1]
        )
        is True
    )

    # 2015 Quarter 4
    assert (
        verify_ad_end_date(
            "../data/csv/year-2015/2015-quarter-4.csv", _2015[2]
        )
        is True
    )

    # #########################################################################
    # Y E A R  2 0 1 6
    # #########################################################################

    # 2016 Quarter 1
    assert (
        verify_ad_end_date(
            "../data/csv/year-2016/2016-Quarter-1.csv", _2016[0]
        )
        is True
    )

    # 2016 Quarter 2
    assert (
        verify_ad_end_date(
            "../data/csv/year-2016/2016-Quarter-2.csv", _2016[1]
        )
        is True
    )

    # 2016 Quarter 3
    assert (
        verify_ad_end_date(
            "../data/csv/year-2016/2016-Quarter-3.csv", _2016[2]
        )
        is True
    )

    # 2016 Quarter 4
    assert (
        verify_ad_end_date(
            "../data/csv/year-2016/2016-Quarter-4.csv", _2016[3]
        )
        is True
    )

    # #########################################################################
    # Y E A R  2 0 1 7
    # #########################################################################

    # 2017 Quarter 1
    assert (
        verify_ad_end_date(
            "../data/csv/year-2017/2017-Quarter-1.csv", _2017[0]
        )
        is True
    )

    # 2017 Quarter 2 April
    assert (
        verify_ad_end_date(
            "../data/csv/year-2017/2017-Quarter-2-April.csv", _2017[1]
        )
        is True
    )

    # 2017 Quarter 2 May
    assert (
        verify_ad_end_date(
            "../data/csv/year-2017/2017-Quarter-2-May.csv", _2017[2]
        )
        is True
    )

    # 2017 Quarter 3
    assert (
        check_num_of_lines(
            "../data/csv/year-2017/2017-Quarter-3.csv", _2017[3]
        )
        is True
    )

    # #########################################################################
    # Verify that there are no duplicate AD IDs!
    # #########################################################################

    # #########################################################################
    # Y E A R  2 0 1 5
    # #########################################################################

    # 2015 Quarter 2
    assert (
        check_for_dupe_id("../data/csv/year-2015/2015-quarter-2.csv") is True
    )

    # 2015 Quarter 3
    assert (
        check_for_dupe_id("../data/csv/year-2015/2015-quarter-3.csv") is True
    )

    # 2015 Quarter 4
    assert (
        check_for_dupe_id("../data/csv/year-2015/2015-quarter-4.csv") is True
    )

    # #########################################################################
    # Y E A R  2 0 1 6
    # #########################################################################

    # 2016 Quarter 1
    assert (
        check_for_dupe_id("../data/csv/year-2016/2016-Quarter-1.csv") is True
    )

    # 2016 Quarter 2
    assert (
        check_for_dupe_id("../data/csv/year-2016/2016-Quarter-2.csv") is True
    )

    # 2016 Quarter 3
    assert (
        check_for_dupe_id("../data/csv/year-2016/2016-Quarter-3.csv") is True
    )

    # 2016 Quarter 4
    assert (
        check_for_dupe_id("../data/csv/year-2016/2016-Quarter-4.csv") is True
    )

    # #########################################################################
    # Y E A R  2 0 1 7
    # #########################################################################

    # 2017 Quarter 1
    assert (
        check_for_dupe_id("../data/csv/year-2017/2017-Quarter-1.csv") is True
    )

    # 2017 Quarter 2 April
    # assert (
    #     check_for_dupe_id("../data/csv/year-2017/2017-Quarter-2-April.csv") is True
    # )

    # 2017 Quarter 2 May
    # assert (
    #     check_for_dupe_id("../data/csv/year-2017/2017-Quarter-2-May.csv") is True
    # )

    # 2017 Quarter 3
    # assert (
    #     check_for_dupe_id("../data/csv/year-2017/2017-Quarter-3.csv") is True
    # )


if __name__ == "__main__":
    main()
