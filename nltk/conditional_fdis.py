from nltk.corpus import gutenberg


# print(gutenberg.fileids())

raw_text = gutenberg.raw('austen-persuasion.txt')

print(raw_text[:200])