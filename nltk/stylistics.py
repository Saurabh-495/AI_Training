import nltk
from nltk.corpus import brown
from nltk import FreqDist

# Download the Brown corpus if you haven't already
# nltk.download('brown')

Models = ["may", "could", "will"]
genres = ["adventure", "news", "government", "romance"]

for g in genres:
    # use categories instead of categorises
    words = brown.words(categories=g)  
    fdist = FreqDist(w.lower() for w in words)
    # Iterate over Models, not previous w from FreqDist
    for w in Models:  
        if w.lower() in fdist:  
            print(g, fdist[w.lower()])
            
