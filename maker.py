#!/usr/bin/env python -tt
  
import pickle
import random
import pandas as pd

data = pd.read_csv('mama.txt', header = None,sep='\t')
#print data

chain = pickle.load(open("mamachain.p", "rb"))
  
new_review = []
sword1 = "BEGIN"
sword2 = "NOW"
  
while True:
    sword1, sword2 = sword2, random.choice(chain[(sword1, sword2)])
    if sword2 == "END":
        break
    new_review.append(sword2)
  
new_stuff = ' '.join(new_review)
token='new stuff'
for ind,text in data.iterrows():
	if new_stuff in text:
		token='old wine'
		break
print new_stuff,' :: ',token   #i think this will work