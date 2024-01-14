# For example, the stem of "running" is "run," and the stem of "better"
# is "better." Stemming may result in the stem not being a valid word,
# as it focuses on linguistic reduction rather than maintaining grammatical 
# correctness or meaning.

import nltk
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.tokenize import word_tokenize

text = "The quick brown foxes are jumping over the lazy dogs"

tokens = word_tokenize(text)

stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in tokens]


print("Stemmed Tokens:", stemmed_tokens)
# o/p -> Stemmed Tokens: ['the', 'quick', 'brown', 'fox', 'are', 'jump', 'over', 'the', 'lazi', 'dog']