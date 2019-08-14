"""
Filename: count_words.py
Date: 2019-07-21
Author: David Oniani
E-mail: onianidavid@gmail.com

License:
    The code is licensed under GNU General Public License v3.0.
    Please read the LICENSE file in this distribution for details
    regarding the licensing of this code.

Description:
    Various visualizations by textual analysis of words.
"""


from collections import Counter
from typing import List

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from barchart_labeling import show_values_on_bars


ARTICLES = ["a", "an", "the"]

CONJUNCTIONS = ["for", "and", "nor", "but", "or", "yet", "so"]

LINKING_VERBS = [
    "am",
    "is",
    "are",
    "was",
    "were",
    "has",
    "became",
    "become",
    "seem",
    "seemed",
    "appear",
    "appeared",
    "smell",
    "sound",
    "taste",
    "feel",
]

PREPOSITIONS = [
    "about",
    "above",
    "according to",
    "across",
    "after",
    "against",
    "ahead of",
    "along",
    "amidst",
    "among",
    "amongst",
    "apart from",
    "around",
    "as",
    "as far as",
    "as well as",
    "aside from",
    "at",
    "barring",
    "because of",
    "before",
    "behind",
    "below",
    "beneath",
    "beside",
    "besides",
    "between",
    "beyond",
    "by",
    "by means of",
    "circa",
    "concerning",
    "despite",
    "down",
    "due to",
    "during",
    "in",
    "in accordance with",
    "in addition to",
    "in case of",
    "in front of",
    "in lieu of",
    "in place of",
    "in spite of",
    "in to",
    "inside",
    "instead of",
    "into",
    "except",
    "except for",
    "excluding",
    "for",
    "following",
    "from",
    "like",
    "minus",
    "near",
    "next",
    "next to",
    "past",
    "per",
    "prior to",
    "round",
    "since",
    "off",
    "on",
    "on account of",
    "on behalf of",
    "on to",
    "on top of",
    "onto",
    "opposite",
    "out",
    "out from",
    "out of",
    "outside",
    "over",
    "owing to",
    "plus",
    "than",
    "through",
    "throughout",
    "till",
    "times",
    "to",
    "toward",
    "towards",
    "under",
    "underneath",
    "unlike",
    "until",
    "unto",
    "up",
    "upon",
    "via",
    "with",
    "with a view to",
    "within",
    "without",
]

PRONOUNS = [
    "i",
    "you",
    "he",
    "she",
    "it",
    "we",
    "they",
    "what",
    "who",
    "me",
    "him",
    "her",
    "it",
    "us",
    "you",
    "them",
    "whom",
    "mine",
    "yours",
    "his",
    "hers",
    "ours",
    "theirs",
    "this",
    "that",
    "these",
    "those",
    "who",
    "whom",
    "which",
    "what",
    "whose",
    "whoever",
    "whatever",
    "whichever",
    "whomever",
    "who",
    "whom",
    "whose",
    "which",
    "that",
    "what",
    "whatever",
    "whoever",
    "whomever",
    "whichever",
    "myself",
    "yourself",
    "himself",
    "herself",
    "itself",
    "ourselves",
    "themselves",
    "myself",
    "yourself",
    "himself",
    "herself",
    "itself",
    "ourselves",
    "themselves",
    "each other",
    "one another",
]

REST = [
    "of",
    "our",
    "be",
    "not",
    "have",
    "has",
    "your",
    "if",
    "while",
    "therefore",
    "hence",
    "thus",
    "so",
    "will",
    "would",
    "no",
    "yes",
    "it's",
    "one",
    "two",
    "it",
    "yours",
    "their",
    "they",
    "its",
    "when",
    "just",
    "because",
    "my",
]


def most_common_words(filepath: str, number: int) -> List[str]:
    """Count the number of occurences of the certain word in a file.

    Parameters:
        filepath: a full path to the file
        number: number of most common words
    """
    data = pd.read_csv(filepath, na_filter=False, thousands=",")

    ad_text = [text.split() for text in data["Ad Text"]]
    ad_text_words = [
        item.lower() for text_list in ad_text for item in text_list
    ]

    ad_text_words = [word for word in ad_text_words if word not in ARTICLES]

    ad_text_words = [
        word for word in ad_text_words if word not in CONJUNCTIONS
    ]

    ad_text_words = [
        word for word in ad_text_words if word not in LINKING_VERBS
    ]

    ad_text_words = [word for word in ad_text_words if word not in PRONOUNS]

    ad_text_words = [
        word for word in ad_text_words if word not in PREPOSITIONS
    ]

    ad_text_words = [word for word in ad_text_words if word not in REST]

    return Counter(ad_text_words).most_common(number)


def word_counter(filepath: str, word: str) -> int:
    """Count the number of occurences of the certain word in a file.

    Parameters:
        filepath: a full path to the file
        word: a word to be counted
    """
    data = pd.read_csv(filepath, na_filter=False, thousands=",")

    count = 0
    for ad_text in data["Ad Text"]:
        if word in ad_text:
            count += 1

    return count


def main() -> None:
    """The main function."""
    top_25 = most_common_words("../data/csv/all/all.csv", 25)
    word_counts = [i[1] for i in top_25]
    word_names = [i[0] for i in top_25]

    sns.set(
        color_codes=True, rc={"figure.figsize": (15.0, 9.0)}, style="darkgrid"
    )

    # Plot and save the barchart
    _, _ = plt.subplots(1, 1)
    sns_plot = sns.barplot(word_counts, word_names)
    sns_plot.set_title("Most Common Words in 2015, 2016, and 2017 Combined")
    show_values_on_bars(sns_plot, space=max(word_counts) * 0.5 / 100)
    figure = sns_plot.get_figure()
    figure_name = "barchart_word_counts.png"
    figure.savefig(figure_name)


if __name__ == "__main__":
    main()
