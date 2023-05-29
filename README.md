## joycean_neos

This is a small repo which shows the code used to build and maintain the twitter account @JoyNeos
which generates neologisms in the style of James Joyce' Ulysses using nltk and POS modelling.

- see notebook for full construction code
- new tweets are generated **Thursdays at 0600** EST, 
  from random combinations of tags from `neo_tags.json` combined with lemmatized English words in `english_words.txt`
- hosted on GCP cloud instance, with cloud function

twitter: https://twitter.com/JoyNeos
