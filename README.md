# py-tokentweet
A light utility to tokenize tweet corpora and run basic frequency analyses.

**corpusScrubber.py** takes Twitter corpora in JSON format and looks for tweets. It then scrubs these tweets, leaving raw text which is then tokenized and reincorporated to the corpus.

**corpusAnalyzer.py** uses the corpus output by _corpusScrubber.py_ and runs frequency analyses on the tokenized data.
These include basic and relative frequency counts, calculating the lexical diversity of the corpus and returning the top n words, where n is specified by the user.
