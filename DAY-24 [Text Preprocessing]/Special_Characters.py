#In this step, special characters such as punctuation marks,
#symbols, or any non-alphanumeric characters are removed from
#the text. The goal is often to simplify the text and focus on
#the essential information without unnecessary noise. Special 
#characters may not carry significant meaning in many NLP tasks,
#and their removal can improve the efficiency of subsequent analyses.

import nltk

def transform_text(text):

    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    return y


print(transform_text("The @ symbol is commonly used in email addresses"))
# o/p -> ['The', 'symbol', 'is', 'commonly', 'used', 'in', 'email', 'addresses']
