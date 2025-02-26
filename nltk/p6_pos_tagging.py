import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

text = "Saurabh is learning NLTK for NLP."
words = word_tokenize(text)
pos_tags = pos_tag(words)

print(pos_tags)
