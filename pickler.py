#!/usr/bin/env python -tt
  
import pickle
  
fh = open("yo-mama.txt", "r")
  
chain = {}
  
def generate_trigram(words):
    if len(words) < 3:
        return
    for i in xrange(len(words) - 2):
        yield (words[i], words[i+1], words[i+2])
  
for line in fh.readlines():
    words = line.split()
    for word1, word2, word3 in generate_trigram(words):
        key = (word1, word2)
        if key in chain:
            chain[key].append(word3)
        else:
            chain[key] = [word3]
  
pickle.dump(chain, open("mamachain.p", "wb" ))