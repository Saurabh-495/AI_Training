import nltk


# guetenberg corpus

nltk.download('gutenberg')
from nltk.corpus import gutenberg

print(gutenberg.fileids())

# get book text

emma = gutenberg.raw('austen-emma.txt')

print(emma[:100])

# tokenization

from nltk.tokenize import sent_tokenize, word_tokenize

sentences = sent_tokenize(emma)

print(sentences[:5])

words = word_tokenize(sentences[0])

print(words[:10])
