import string

import nltk

text = '''
Joe waited for the 3,122.5 train. "We have to be honest. The train was late. 
Mary and Samantha took the bus. 
I looked for Mary and Samantha at the bus station.
'''
print("\nOriginal string:")
print(text)
token_text = nltk.sent_tokenize(text)
punctuations=set()
punctuations.update(string.punctuation)
punctuations.add('``')
punctuations.add('\'\'')
for sent in token_text:
    words = nltk.word_tokenize(sent)
    for word in words:
        if word not in punctuations:
            print(word)

