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
import time
import pickle
import string

import nltk

import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import precision_recall_fscore_support as score


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


def save_model(model: object, filename: str) -> None:
    """Load the model."""
    pickle.dump(model, open(filename, "wb"))


def load_model(filename: str) -> object:
    """Load the model."""
    return pickle.load(open(filename, "rb"))


def main() -> None:
    """The main function."""
    # Prepare the data
    ira_text = pd.read_csv(
        "../data/csv/all/all.csv", na_filter=False, thousands=","
    )["Ad Text"]

    non_ira_text = [
        line.rstrip()
        for line in open("../data/txt/non_IRA_data.txt", "r").readlines()
    ]

    total_text = ira_text.append(pd.Series(non_ira_text))

    labels_1 = ["ira"] * 3517
    labels_2 = ["non-ira"] * 3517
    labels_1.extend(labels_2)

    data = pd.DataFrame({"text": total_text, "label": labels_1})

    # Apply the lambda functions
    data["text_length"] = data["text"].apply(lambda x: len(x) - x.count(" "))
    data["punctuation%"] = data["text"].apply(lambda x: count_punct(x))

    # Do the 80/20 split
    X_train, X_test, y_train, y_test = train_test_split(
        data[["text", "text_length", "punctuation%"]],
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
            X_train[["text_length", "punctuation%"]].reset_index(drop=True),
            pd.DataFrame(tfidf_train.toarray()),
        ],
        axis=1,
    )

    X_test_vect = pd.concat(
        [
            X_test[["text_length", "punctuation%"]].reset_index(drop=True),
            pd.DataFrame(tfidf_test.toarray()),
        ],
        axis=1,
    )

    # Train the model using random forest classifier
    # n_jobs=-1 parallelizes the execution
    rf = RandomForestClassifier(n_estimators=150, max_depth=None, n_jobs=-1)

    start = time.time()
    rf_model = rf.fit(X_train_vect, y_train)
    end = time.time()
    fit_time = end - start

    # Make prediction and test the model
    start = time.time()
    y_pred = rf_model.predict(X_test_vect)
    end = time.time()
    pred_time = end - start

    precision, recall, fscore, train_support = score(
        y_test, y_pred, pos_label="ira", average="binary"
    )

    # Print the results
    print(
        f"Fit time: {round(fit_time, 3)}\n"
        f"Predict time: {round(pred_time, 3)}\n"
        f"Precision: {round(precision, 3)}\n"
        f"Recall: {round(recall, 3)}\n"
        f"Accuracy: {round((y_pred == y_test).sum() / len(y_pred), 3)}"
    )

    # Save the model
    save_model(rf_model, "model.pickle")


if __name__ == "__main__":
    main()
