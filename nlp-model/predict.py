#!/usr/bin/env python3
# encoding: UTF-8

"""
Filename: predict.py
Date: 2019-11-16 11:41:58 PM
Author: David Oniani
E-mail: onianidavid@gmail.com

License:
    The code is licensed under MIT License. Please read the LICENSE file in
    this distribution for details regarding the licensing of this code.

Description:
    Predict whether the text is similar to that of IRA ads or not.
"""

import re
import pickle
import string

from typing import Any

import nltk

import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer


def text_length(text: str) -> int:
    """The length of the text.

    This is one of the features.
    """
    return len(text) - text.count(" ")


def count_punctuation(text: str) -> float:
    """Count punctuation.

    This is one of the features.
    """
    if text:
        count = sum([1 for char in text if char in string.punctuation])
        return round(count / (len(text) - text.count(" ")), 3) * 100

    return 0


def weight_value(text: str) -> float:
    """Return a weight depending on TOP 25 common words.

    This is one of the features.
    """
    common_words_dict = {
        "black": 1597,
        "police": 801,
        "people": 476,
        "all": 423,
        "stop": 397,
        "join": 388,
        "don't": 310,
        "more": 305,
        "can": 294,
        "do": 284,
        "american": 280,
        "matters": 264,
        "man": 262,
        "bm": 259,
        "only": 254,
        "free": 248,
        "white": 239,
        "community": 224,
        "follow": 223,
        "should": 222,
        "how": 214,
        "make": 206,
        "new": 203,
        "want": 197,
        "video": 197,
    }

    total = sum(common_words_dict.values())

    weights_dict = {}
    for key, value in common_words_dict.items():
        weights_dict[key] = round(value / total, 3)

    weight_total = 0.0
    for word in re.split("\\W+", text):
        if word in weights_dict:
            weight_total += weights_dict[word]

    return weight_total


def load_model(filename: str) -> Any:
    """Load the model."""
    return pickle.load(open(filename, "rb"))


def predict(input_text: str) -> str:
    """The main function."""
    # Data preparation
    text = pd.Series([input_text])
    data = pd.DataFrame({"text": text})

    # Apply the lambda functions and create feature-columns
    data["text_length"] = data["text"].apply(text_length)
    data["punctuation%"] = data["text"].apply(count_punctuation)
    data["weight"] = data["text"].apply(weight_value)

    # Create a data frame
    data_frame = data[["text_length", "punctuation%", "weight"]]
    for i in range(9078):
        data_frame[f"{i}"] = 0

    # Load the model
    rf_model = load_model("../nlp-model/model.pickle")

    # Make a prediction
    y_pred = rf_model.predict(data_frame)
    prediction = y_pred[0]

    # Return the result
    return f'Text "{input_text}" is {prediction}'
