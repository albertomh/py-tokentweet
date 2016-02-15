###  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  ###
###    SCRIPT TO SCRUB DATA OBTAINED FROM A TWITTER SCRAPER
###
###    THIS SCRIPT READS DATA FROM A JSON FILE AND:
###        - REMOVES RT MARKERS, @USERNAMES, #HASHTAGS, URLS
###            AND SPECIAL SYMBOLS.
###
###        - SELECTS THE FIELDS AND DATA CONSIDERED RELEVANT.
###
###        - STORES THE CURATED, CONCISE DATA AS A LIST OF
###            DICTIONARIES. EACH DICTIONARY HOLDS THE DATA
###            OF AN INDIVIDUAL TWEET, INCLUDING A TOKENIZED
###            FORM OF THE TEXT IN A LIST.
###
###        - SAVES THE DATA IN THIS FORMAT TO A JSON FILE.
###
###    WRITTEN BY Alberto M.H. FOR LINGUIST492A, FEBRUARY 2016
###  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  ###
import ast
import json
import re

###    LOAD CORPUS FROM JSON FILE.
corpus_json = open('corpus50k.json', 'r')
corpus = corpus_json.read()

###    POPULATE THE LIST l_corpus BY EVALUATING THE STRING corpus.
l_corpus = ast.literal_eval(corpus)


n = range(len(l_corpus)) ### n IS THE NUMBER OF TWEETS IN THE CORPUS.


###    CREATE THE DICTIONARY d_tw AND POPULATE IT USING THE CONTENTS OF THE LIST l_corpus.
d_tw = {}
for twt in n:
    d_tw[twt] = json.loads(l_corpus[twt])


###    SCRUB THE CONTENTS OF THE 'text' FIELD IN TWEET DICTIONARY.
for twt in n:
    d_tw[twt]['text'] = d_tw[twt]['text'].replace("RT ", "") # REMOVE RT MARKERS
    d_tw[twt]['text'] = re.sub(ur"#\S+", "", d_tw[twt]['text']) # REMOVE HASHTAGS
    d_tw[twt]['text'] = re.sub(ur"@\S+", "", d_tw[twt]['text']) # REMOVE USERNAMES
    d_tw[twt]['text'] = re.sub(ur"http\S+", "", d_tw[twt]['text']) # REMOVE URLs
    d_tw[twt]['text'] = re.sub(ur"\n", "", d_tw[twt]['text']) # REMOVE NEWLINES
    d_tw[twt]['text'] = re.sub(ur"[^A-Za-z ]", "", d_tw[twt]['text']) # REMOVE DIGITS AND PUNCTUATION
    d_tw[twt]['text'] = re.sub(ur"^( +)|( +)$", "", d_tw[twt]['text']) # REMOVE SPACES AT START OR END OF STRING
    d_tw[twt]['text'] = re.sub(ur" . |^. | .$", "", d_tw[twt]['text']) # REMOVE SINGLE LETTERS THAT ARE NOT WORDS


    d_tw[twt]['text'] = d_tw[twt]['text'].lower() # MAKE ALL TEXT LOWERCASE.

###    REMOVE STOPWORDS:
    d_tw[twt]['text'] = re.sub(ur" the | i | im | am | of | at | is | in | to | a | for | on | about | that | this | there | be | it | its | with | by | and | you | youre | your | yours | mine | he | hes | his | him | she | shes | her | hers | they | their | theirs | theyre | pm | est | cet ", " ", d_tw[twt]['text'])
    d_tw[twt]['text'] = re.sub(ur" +", " ", d_tw[twt]['text']) #ENSURE THERE IS ONLY A SINGLE SPACE BETWEEN WORDS.

for twt in n:
    d_tw[twt]['parsed_tweet'] = str(d_tw[twt]['text'].split(" ")) #TOKENIZE TWEETS BY SPLITTING AT WHITESPACE.


###    CREATE THE LIST l_out AND POPULATE IT USING THE CONTENTS OF THE DICTIONARY d_tw.
l_out = []
for twt in n:
    l_out.append(d_tw[twt])


###    DEFINE PATH OF OUTPUT FILE AND WRITE TO FILE.
path_out = 'output50k.json'

with open(path_out, 'w') as outfile:
    json.dump(l_out, outfile)
outfile.close()

print "Successfully scrubbed and parsed", len(l_corpus), "tweets."
print "\nStored in:", path_out


