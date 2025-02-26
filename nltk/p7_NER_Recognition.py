import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk

# Sample text
text = "Virat Kohli is a cricketer who played for Royal Challengers Bangalore and India."

# Tokenization and POS tagging
words = word_tokenize(text)
pos_tags = pos_tag(words)

# Named Entity Recognition (NER)
ner_tree = ne_chunk(pos_tags)

# Print the NER tree
print(ner_tree)

"""
PERSON → Recognizes "Virat Kohli" as a person.
ORGANIZATION → Recognizes "Royal Challengers Bangalore" as an organization.
GPE (Geopolitical Entity) → Recognizes "India" as a country.
🔹 NER helps in extracting useful information from text automatically.
"""