"""
Filename: write_counts.py
Date: 2019-08-14 07:00:57 PM
Author: David Oniani
E-mail: onianidavid@gmail.com

License:
    The code is licensed under GNU General Public License v3.0.
    Please read the LICENSE file in this distribution for details
    regarding the licensing of this code.

Description:
    Write text file with words for the wordcloud generation.
"""

WORDS = {
    "BLACK": 1597,
    "POLICE": 801,
    "PEOPLE": 476,
    "ALL": 423,
    "STOP": 397,
    "JOIN": 388,
    "DON'T": 310,
    "MORE": 305,
    "CAN": 294,
    "DO": 284,
    "AMERICAN": 280,
    "MATTERS": 264,
    "MAN": 262,
    "BM": 259,
    "ONLY": 254,
    "FREE": 248,
    "WHITE": 239,
    "COMMUNITY": 224,
    "FOLLOW": 223,
    "SHOULD": 222,
    "HOW": 214,
    "MAKE": 206,
    "NEW": 203,
    "WANT": 197,
    "VIDEO": 197,
}


def main() -> None:
    """The main function."""
    with open("top25.txt", "w") as file:
        for key, value in WORDS.items():
            for _ in range(value):
                file.write(f"{key}\n")


if __name__ == "__main__":
    main()
