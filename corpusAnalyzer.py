###  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  ###
###    SCRIPT TO ANALYZE A TWEET CORPUS
###
###    THIS SCRIPT READS DATA FROM A JSON FILE AND OFFERS THE USER
###    THE FOLLOWING FOUR FUNCTIONS:
###        - baseFreq() RETURNS UNIQUE WORDS IN THE CORPUS AS A 
###          DICTIONARY WITH THE WORDS' RESPECTIVE FREQUENCIES.
###
###        - relFreq() RETURNS A DICTIONARY OF UNIQUE WORDS AND
###          THEIR FREQUENCIES RELATIVE TO THE TOTAL # OF WORDS.
###
###        - lexDiver() RETURNS THE LEXICAL DIVERSITY OF THE CORPUS,
###          A RATIO OF UNIQUE WORDS TO TOTAL WORDS IN THE CORPUS.
###
###        - topFreq(n) RETURNS THE TOP n WORDS IN THE CORPUS AND
###          THE PROPORTION OF THE CORPUS THEY ACCOUNT FOR.
###          n MUST BE SPECIFIED BY THE USER.
###
###
###    WRITTEN BY Alberto M.H. FOR LINGUIST492A, FEBRUARY 2016
###  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  ###
import ast
import json
import operator
from collections import Counter
from collections import OrderedDict

###    LOAD SCRUBBED CORPUS FROM JSON FILE.
with open('output50k.json') as json_corpus:    
    l_corpus = json.load(json_corpus)


n = range(len(l_corpus)) ### n IS THE NUMBER OF TWEETS IN THE CORPUS.


###    CREATE THE LIST l_lex AND POPULATE IT USING THE CONTENTS OF
###    THE FIELD 'parsed_tweet' FROM THE JSON GENERATED BY THE SCRUBBER.
l_lex = []

for twt in n:
    l_lex.extend(ast.literal_eval(l_corpus[twt]['parsed_tweet']))


###    CREATE THE SET OF UNIQUE WORDS IN CORPUS.
unique_lex = set(l_lex)

###    USE SET TO CREATE LIST OF UNIQUE WORDS IN ALPHABETICAL ORDER.
unique_lex = list(unique_lex)
unique_lex.sort()

###    c_lex IS A DICTIONARY OF THE FORM {'unique_word': word_count}
count = Counter(l_lex)
c_lex = dict(count)

###    LIST OF ('unique_word': word_count) TUPLES SORTED BY DECREASING FREQUENCY.
###    //ATTRIBUTION:// DICTIONARY SORTING BASED ON CODE FOUND AT: http://bit.ly/1KvaLod  
count_sort = sorted(c_lex.items(), key=operator.itemgetter(1), reverse=True)
count_dict = dict(count_sort)
###    // // // // // // // // // // // // // // //


###    THE FUNCTION baseFreq PRINTS A DICTIONARY OF THE WORDS USED IN THE CORPUS
###    AND THE NUMBER OF TIMES THEY ARE USED.
def baseFreq():

    count_sort = sorted(c_lex.items(), key=operator.itemgetter(1), reverse=True)
    count_dict = dict(count_sort)

###    OUTPUT TO THE USER. Code to remove unicode formatting adapted from: bit.ly/1Py5OYT
    print "The following is a dictionary of the form {word: frequency} for individual words in the corpus:\n\n", ast.literal_eval(json.dumps(count_dict))
###    SOME COMPUTERS MAY STRAIN TO PRINT THE ENTIRE DICTIONARY. FOR CONVENIENCE
###    THE BELOW LINES OF CODE MAY BE UN-COMMENTED AND USED TO WRITE THE
###    DICTIONARY TO A FILE INSTEAD.
#    path_out = 'cA_baseFreq.json'
#    strout_bf = ast.literal_eval(json.dumps(count_dict))
#
#    with open(path_out, 'w') as outfile:
#        json.dump(strout_bf, outfile)
#    outfile.close()
###    // // // // // // // // // // // // // // //



###    THE FUNCTION relFreq COMPUTES THE RELATIVE FREQUENCY OF ALL WORDS PRESENT
###    IN THE CORPUS AND PRINTS A DICTIONARY OF THE FORM {word: ratio} WHERE
###    RATIO IS THE NUMBER OF TIMES A GIVEN WORD IS PRESENT IN THE CORPUS DIVIDED
###    BY THE TOTAL NUMBER OF WORDS IN THE CORPUS.
def relFreq():
    
    freq_dict = dict()

    for key, value in count_dict.items():
        freq_dict[key] = round(float(value) / len(count_dict), 5)
        freq_list = sorted(freq_dict.iteritems(), key=operator.itemgetter(1), reverse=True)

###    OUTPUT TO THE USER.
    print freq_dict
###    SOME COMPUTERS MAY STRAIN TO PRINT THE ENTIRE DICTIONARY. FOR CONVENIENCE
###    THE BELOW LINES OF CODE MAY BE UN-COMMENTED AND USED TO WRITE THE
###    DICTIONARY TO A FILE INSTEAD.
#    path_out = 'cA_relFreq.json'
#    strout_rf = ast.literal_eval(json.dumps(freq_dict))
#    
#    with open(path_out, 'w') as outfile:
#        json.dump(strout_rf, outfile)
#    outfile.close()
###    // // // // // // // // // // // // // // //



###    THE FUNCTION lexDiver COMPUTES A RATIO OF THE UNIQUE WORDS IN THE CORPUS
###    DIVIDED BY THE TOTAL NUMBER OF WORDS IN THE CORPUS.
def lexDiver():
    
    lex_diver = float(len(unique_lex)) / float(len(l_lex))
    
###    OUTPUT TO THE USER.    
    print "The lexical diversity of the corpus is:", round(lex_diver, 3)
###    // // // // // // // // // // // // // // //




###    THE FUNCTION topFreq(n) COMPUTES AND PRINTS THE n MOST FREQUENT WORDS
###    IN THE CORPUS. n MUST BE SPECIFIED BY THE USER.
def topFreq(n):
    
    freq_dict = dict()

###    freq_list LISTS WORDS IN ORDER OF DECREASING FREQUENCY.
    for key, value in count_dict.items():
        freq_dict[key] = round(float(value) / len(count_dict), 3)
        freq_list = sorted(freq_dict.iteritems(), key=operator.itemgetter(1), reverse=True)

###    top_ratio CALLS count_sort AND FINDS THE SUM OF THE FREQUENCIES OF THE
###    TOP n WORDS AND DIVIDES IT BY THE TOTAL NUMBER OF WORDS IN THE CORPUS.
    top_ratio = float(sum(n for _, n in count_sort[:n])) / float(len(l_lex))

###    OUTPUT TO THE USER.
    if n == 0:
        print "Please enter a value greater that zero."
    elif n == 1:
        print "The most frequent word in the corpus is:\n\n", ast.literal_eval(json.dumps([x for x,_ in freq_list[:n]]))
        print "\nIt accounts for " + str(round(top_ratio * 100, 1)) + "% of words in the corpus."
    elif n > 1:
        print "The following are the top", n, "words in the corpus:", "\n\n", ast.literal_eval(json.dumps([x for x,_ in freq_list[:n]]))
        print "\nThey account for " + str(round(top_ratio * 100, 1)) + "% of words in the corpus."
###    // // // // // // // // // // // // // // //




###    FUNCTION TO INTRODUCE THE USER TO THE SCRIPT AND ITS FUNCTIONS.
def welcomeUser():
    print "This script calculates a variety of metrics for a given corpus.\n"
    print "Functions available include:\n   - baseFreq() | Prints a dictionary of all individual words in the corpus and their respective frequencies.\n"
    print "   - relFreq() | Prints a dictionary of individual words and their frequency relative to the total number of words in the corpus.\n"
    print "   - lexDiver() | Returns the lexical diversity of the corpus, a ratio of unique words to total words.\n"
    print "   - topFreq(n) | Returns the n most frequent words in the corpus and what proportion of the text they account for. n must be specified by the user.\n"
###    // // // // // // // // // // // // // // //

welcomeUser();

