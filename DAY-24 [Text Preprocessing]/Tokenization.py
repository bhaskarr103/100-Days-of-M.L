#Tokenization is the process of breaking down a text into smaller units,
#typically words or phrases, known as tokens.
#This step is crucial for various NLP tasks as it helps in analyzing and 
#understanding the structure of the text. Tokens are the building blocks
#for subsequent analyses such as sentiment analysis, part-of-speech tagging,
#and more.

import nltk

def transform_text(text):
    text = nltk.word_tokenize(text)
    return text

print(transform_text("Hello how Are YOU ?"))

# o/p -> ['Hello', 'how', 'Are', 'YOU', '?']