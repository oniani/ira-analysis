#!/usr/bin/env python3
# encoding: UTF-8

"""
Filename: model.py
Date: 2019-11-16 07:24:12 PM
Author: David Oniani
E-mail: onianidavid@gmail.com

License:
    The code is licensed under GNU General Public License v3.0.
    Please read the LICENSE file in this distribution for details
    regarding the licensing of this code.

Description:
    A model for IRA Facebook ad classification.
"""

import re
import pickle
import string

import nltk

import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import precision_recall_fscore_support as score


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


def weight_value(text: str) -> str:
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

    weight_total = 0
    for word in re.split("\\W+", text):
        if word in weights_dict:
            value += weights_dict[word]

    return weight_total


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


def save_model(model: object, filename: str) -> None:
    """Load the model."""
    pickle.dump(model, open(filename, "wb"))


def main() -> None:
    """The main function."""
    # Data preparation
    ira_text = pd.read_csv(
        "../data/csv/all/all.csv", na_filter=False, thousands=","
    )["Ad Text"]

    non_ira_text = [
        line.rstrip()
        for line in open("../data/txt/non_IRA_data.txt", "r").readlines()
    ]

    total_text = ira_text.append(pd.Series(non_ira_text))

    labels_1, labels_2 = ["ira"] * 3517, ["non-ira"] * 3517
    labels_1.extend(labels_2)

    data = pd.DataFrame({"text": total_text, "label": labels_1})

    # Apply the lambda functions and create feature-columns
    data["text_length"] = data["text"].apply(lambda x: text_length(x))
    data["punctuation%"] = data["text"].apply(lambda x: count_punctuation(x))
    data["weight"] = data["text"].apply(lambda x: weight_value(x))

    # Do the 80/20 split
    X_train, X_test, y_train, y_test = train_test_split(
        data[["text", "text_length", "punctuation%", "weight"]],
        data["label"],
        test_size=0.2,
    )

    # Vectorization
    tfidf_vect = TfidfVectorizer(analyzer=clean_text)
    tfidf_vect_fit = tfidf_vect.fit(X_train["text"])

    tfidf_train = tfidf_vect_fit.transform(X_train["text"])
    tfidf_test = tfidf_vect_fit.transform(X_test["text"])

    X_train_vect = pd.concat(
        [
            X_train[["text_length", "punctuation%", "weight"]].reset_index(
                drop=True
            ),
            pd.DataFrame(tfidf_train.toarray()),
        ],
        axis=1,
    )

    X_test_vect = pd.concat(
        [
            X_test[["text_length", "punctuation%", "weight"]].reset_index(
                drop=True
            ),
            pd.DataFrame(tfidf_test.toarray()),
        ],
        axis=1,
    )

    # Train the model using random forest classifier
    # n_jobs=-1 parallelizes the execution
    rf = RandomForestClassifier(n_estimators=180, max_depth=None, n_jobs=-1)

    # Fit the model
    rf_model = rf.fit(X_train_vect, y_train)

    # Make prediction and test the model
    y_pred = rf_model.predict(X_test_vect)

    # Report the results
    precision, recall, fscore, train_support = score(
        y_test, y_pred, pos_label="ira", average="binary"
    )

    # Print the results
    print(
        f"Precision: {round(precision, 3)}\n"
        f"Recall: {round(recall, 3)}\n"
        f"Accuracy: {round((y_pred == y_test).sum() / len(y_pred), 3)}"
    )

    # Save the model
    save_model(rf_model, "model.pickle")


if __name__ == "__main__":
    main()
