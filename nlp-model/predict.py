#!/usr/bin/env python3
# encoding: UTF-8

"""
Filename: predict.py
Date: 2019-11-16 11:41:58 PM
Author: David Oniani
E-mail: onianidavid@gmail.com

License:
    The code is licensed under GNU General Public License v3.0.
    Please read the LICENSE file in this distribution for details
    regarding the licensing of this code.

Description:
    This is a description of the file.
"""

import re
import pickle
import string

import nltk

import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer


def count_punct(text: str) -> int:
    """Count punctuation.

    This is one of the features.
    """
    if text:
        count = sum([1 for char in text if char in string.punctuation])
        return round(count / (len(text) - text.count(" ")), 3) * 100

    return 0


def load_model(filename: str) -> object:
    """Load the model."""
    return pickle.load(open(filename, "rb"))


def main() -> None:
    """The main function."""
    text = "Hello there"  # input("Enter a text: ")
    vectorizer = TfidfVectorizer(analyzer=clean_text)
    vectorizer_fit = vectorizer.fit([text])
    print(vectorizer_fit)

    # model = load_model("./model.pickle")

    # print(model.predict(vectorizer_fit))


if __name__ == "__main__":
    main()
