from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Step 1: Read the text file
ps = PorterStemmer()
words = ["running", "flies", "happily", "better", "studies"]

stemmed_words = [ps.stem(word) for word in words]
print(stemmed_words)
