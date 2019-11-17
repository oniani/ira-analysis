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


def text_length(text: str) -> int:
    """The length of the text.

    This is one of the features.
    """
    return len(text) - text.count(" ")


def count_punct(text: str) -> int:
    """Count punctuation.

    This is one of the features.
    """
    if text:
        count = sum([1 for char in text if char in string.punctuation])
        return round(count / (len(text) - text.count(" ")), 3) * 100

    return 0


def clean_text(text: str) -> str:
    """Clean up the text."""
    ps = nltk.PorterStemmer()
    stopwords = nltk.corpus.stopwords.words("english")

    text = "".join(
        [word.lower() for word in text if word not in string.punctuation]
    )

    tokens = re.split("\\W+", text)
    text = [ps.stem(word) for word in tokens if word not in stopwords]

    return text


def load_model(filename: str) -> object:
    """Load the model."""
    return pickle.load(open(filename, "rb"))


def predict(input_text: str) -> None:
    """The main function."""
    text = pd.Series([input_text])
    data = pd.DataFrame({"text": text})

    # Apply the lambda functions and create feature-columns
    data["text_length"] = data["text"].apply(lambda x: text_length(x))
    data["punctuation%"] = data["text"].apply(lambda x: count_punct(x))

    # Create a data frame
    df = data[["text_length", "punctuation%"]]

    for i in range(9038):
        df[f"{i}"] = 0

    # Load the model
    rf_model = load_model("../nlp-model/model.pickle")

    # Make a prediction
    y_pred = rf_model.predict(df)
    prediction = y_pred[0]

    # Print the result
    return f'Text "{input_text}" is {prediction}'
