#brown corpus in nltk

import nltk
from nltk.corpus import brown

# Loading brown corpus

# nltk.download('brown')

brown_corpus = brown.words()

print("Length of Brown Corpus:", len(brown_corpus))

print("First 10 words in Brown Corpus:", brown_corpus[:10])

print("Last 10 words in Brown Corpus:", brown_corpus[-10:])

print("Average word length in Brown Corpus:", sum(len(word) for word in brown_corpus) / len(brown_corpus))

