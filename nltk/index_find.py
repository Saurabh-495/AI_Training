from nltk.tokenize import RegexpTokenizer

text = "Saurabh is learning NLTK in Python."

# Create a tokenizer that captures words
tokenizer = RegexpTokenizer(r'\w+')

# Get the tokenized words
tokens = tokenizer.tokenize(text)
print("Tokens:", tokens)

# Get the indexes (start, end) of each token
token_spans = list(tokenizer.span_tokenize(text))
print("Token Spans:", token_spans)
