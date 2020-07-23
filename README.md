# Textual and Statistical Analysis of Russian IRA Facebook Advertisements

## Organization

```zsh
.
├── LICENSE        # A license for the project
├── data           # Data storage
├── koppel11       # Implementation of the paper "koppel11"
├── nlp-model      # NLP model for binary classification of IRA ad texts
├── paper          # Paper
├── pdf-scraping   # Tools for PDF scraping
├── visualization  # Programs and scripts for statistical visualizations
└── web-app        # Web application using the pre-trained NLP model
```

## Working with Data

The recommended way of working with the CSV data is using the `pandas` library.
`pandas` provides a user-friendly environment for working with data in the
tabular format. See an example below. Alternatively, one could also use
Python's built-in `csv` module (or other programming language of preference and
its tools).

```python3
Python 3.7.3 (default, Mar 27 2019, 09:23:15)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.5.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import pandas as pd

In [2]:

In [2]: data = pd.read_csv("./data/csv/year-2015/2015-Quarter-2.csv", na_filter=False, thousands=",")

In [3]:

In [3]: data.columns
Out[3]:
Index(['Ad ID', 'Ad Text', 'Ad Landing Page', 'Ad Targeting Location',
       'Excluded Connections', 'Age', 'Language', 'Placements',
       'People Who Match', 'Friends of Connections', 'Ad Impressions',
       'Ad Clicks', 'Ad Spend', 'Ad Creation Date', 'Ad End Date'],
      dtype='object')

In [4]:

In [4]: data.dtypes
Out[4]:
Ad ID                      int64
Ad Text                   object
Ad Landing Page           object
Ad Targeting Location     object
Excluded Connections      object
Age                       object
Language                  object
Placements                object
People Who Match          object
Friends of Connections    object
Ad Impressions             int64
Ad Clicks                  int64
Ad Spend                  object
Ad Creation Date          object
Ad End Date               object
dtype: object
```

## References

- [Authorship attribution in the wild](https://www.researchgate.net/publication/220147732_Authorship_attribution_in_the_wild)
- [Who Wrote the Web? Revisiting Influential Author Identification Research Applicable to Information Retrieval](https://www.researchgate.net/publication/309025021_Who_Wrote_the_Web_Revisiting_Influential_Author_Identification_Research_Applicable_to_Information_Retrieval)
- [Authorship Attribution of Micro-Messages](https://www.aclweb.org/anthology/D13-1193)
- [Design and Implementation of a Machine Learning-Based Authorship Identification Model](https://www.hindawi.com/journals/sp/2019/9431073/)
- [Exposing Russia’s Effort to Sow Discord Online: The Internet Research Agency and Advertisements](https://intelligence.house.gov/social-media-content/)
- [The Tactics & Tropes of the Internet Research Agency](https://disinformationreport.blob.core.windows.net/disinformation-report/NewKnowledge-Disinformation-Report-Whitepaper.pdf)
- [How Russian Trolls Used Meme Warfare to Divide America](https://www.wired.com/story/russia-ira-propaganda-senate-report/)
- [Racist cop Facebook posts are a public safety problem | Editorial](https://www.inquirer.com/opinion/editorials/philadelphia-police-facebook-posts-plain-view-project-racist-20190605.html)
- [Facebook Ad Library](https://www.facebook.com/ads/library)

## License

[GNU General Public License v3.0](LICENSE)
