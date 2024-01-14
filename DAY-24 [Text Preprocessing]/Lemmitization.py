# For example, the lemma of "running" is "run," and the lemma of "better"
# is "good."

# Lemmatization takes into account the part of speech (POS) of a word
# and provides more accurate results compared to stemming. 
# It involves the use of a lexical database or linguistic rules to 
# determine the correct base form.

import nltk
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('wordnet')

text = "The quick brown foxes are jumping over the lazy dogs"

tokens = word_tokenize(text)

lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]

print("Original Tokens:", tokens)
print("Lemmatized Tokens:", lemmatized_tokens)


# o/p -> Original Tokens: ['The', 'quick', 'brown', 'foxes', 'are', 'jumping', 'over', 'the', 'lazy', 'dogs']
# Lemmatized Tokens: ['The', 'quick', 'brown', 'fox', 'are', 'jumping', 'over', 'the', 'lazy', 'dog']
