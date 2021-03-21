# Import library
from collections import Counter
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer
from nltk.tag import pos_tag
from nltk.tokenize import sent_tokenize, word_tokenize

import matplotlib.pyplot as plt
import pandas as pd
import string

# Function
def pos_tagging(tokenized_sent):
    return list(map(pos_tag, tokenized_sent))

def punct_removal(tokenized):
    punctuation_list = string_to_char(string.punctuation)

    return [word for word in tokenized if word not in punctuation_list]

def stopwords_removal(tokenized):
    stop_words = set(stopwords.words('english'))

    return [word for word in tokenized if word not in stop_words]

def string_to_char(string):
    return [char for char in string]

def to_lowercase(tokenized):
    return [word.lower() for word in tokenized]

def word_stemming(tokenized):
    ps = PorterStemmer()
    
    return [ps.stem(word) for word in tokenized]

def word_tokenization(tokenized_sent):
    return list(map(word_tokenize, tokenized_sent))

# Import data
df = pd.read_csv("quotes.csv")
df_quote = df['quote'].rename('text')

# Sentence tokenization
tokenized_text = df_quote.apply(lambda row: sent_tokenize(row)) \
    .rename('tokenized_text')
df_quote = pd.concat([df_quote, tokenized_text], axis = 1)

# Word tokenization
tokenized_sent = df_quote['tokenized_text'].apply(lambda row: word_tokenization(row)) \
    .rename('tokenized_sent')
df_quote = pd.concat([df_quote, tokenized_sent], axis = 1)

# POS tagging
pos_tagged = df_quote['tokenized_sent'].apply(lambda row: pos_tagging(row)) \
    .rename('pos_tagged')
df_quote = pd.concat([df_quote, pos_tagged], axis = 1)

## Punctuation removal
#removed_punct = df_quote['tokenized'].apply(lambda row: punct_removal(row)) \
#    .rename('removed_punct')
#df_quote = pd.concat([df_quote, removed_punct], axis = 1)
#
## Convert to lowercase
#lowered = df_quote['removed_punct'].apply(lambda row: to_lowercase(row)) \
#    .rename('lowered')
#df_quote = pd.concat([df_quote, lowered], axis = 1)
#
## Stopwords removal
#removed_stopwords = df_quote['lowered'].apply(lambda row: stopwords_removal(row)) \
#    .rename('removed_stopwords')
#df_quote = pd.concat([df_quote, removed_stopwords], axis = 1)
#
## Stemming
#stemmed = df_quote['removed_stopwords'].apply(lambda row: word_stemming(row)) \
#    .rename('stemmed')
#df_quote = pd.concat([df_quote, stemmed], axis = 1)
#
## Frequency distribution
#count = {}
#for idx in df_quote.index:
#    freq = FreqDist(df_quote['stemmed'][idx])
#    count = Counter(count) + Counter(freq)
#
#count_most = count.most_common(20)
#
#plt.bar(count.keys(), count.values())
