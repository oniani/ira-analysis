#!/usr/bin/env python3
# encoding: UTF-8

"""
Filename: hello.py
Date: 2019-10-13 01:23:55 PM
Author: David Oniani
E-mail: onianidavid@gmail.com

License:
    The code is licensed under MIT License. Please read the LICENSE file in
    this distribution for details regarding the licensing of this code.

Description:
    Get the basic statistics.
"""

import argparse
import json
import os


def main():
    """The main function"""

    parser = argparse.ArgumentParser(description="Process the arguments.")

    # Number of slots in the Galton board
    parser.add_argument("--filepath", type=str, help="specify the filepath")

    # Get the argparse.Namespace class to obtain the values of the arguments
    args = parser.parse_args()

    # Get the data
    with open(args.filepath) as file:
        answers = json.load(file)["answers"]

    # Get the acuracy scores
    scores = [answers[number]["score"] for number, _ in enumerate(answers)]

    # Get the average accuracy
    print(f"Average percentage chance: {sum(scores) / len(scores) * 100:.4f}%")


if __name__ == "__main__":
    main()
