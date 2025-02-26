from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stop_words = set(stopwords.words('english'))

text = word_tokenize("This is a sample text. It contains some stopwords.")

filtered_words = [word for word in text if word.lower() not in stop_words]

print("Filtered Words :",filtered_words)
