#Count words
from collections import Counter
import re
def word_frequencies(filename):
    with open(filename) as f:
       array = []
       for line in f:
        for word in line.split():
            array.append(word.strip("""!"#$%&'()*,-./:;?@[]_"""))
    c=dict(Counter(array))
    return c



filename = "Alice.txt"
c=word_frequencies(filename)
for key, val in c.items():
    print(key,':',val)
