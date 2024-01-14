#This step involves converting all the text to lowercase. 
#Making all characters lowercase is a common preprocessing
# step to ensure uniformity in the text data.
# It helps in treating words in a case-insensitive manner, 
#preventing duplication of words with different cases and 
#simplifying subsequent analyses.


def transform_text(text):
    text = text.lower()
    return text

print(transform_text("HI HOW ARE YOU ?"))

# o/p -> hi how are you ?