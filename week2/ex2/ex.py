import math
import operator
#import pandas as pd
#from ggplot import *
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def words(filename):
    with open(filename) as data_file:    
      data = data_file.readlines()

    words = list()
    for s in data:
      words.extend(s.split())
    return words

def counts(words):
    counts = dict()
    for w in words:
      counts[w] = counts.get(w, 0) + 1
    return counts

def maxvals(dvals):
    return sorted(dvals.items(), key = operator.itemgetter(1), reverse = True)

pwords = words("pos.txt")
nwords = words("neg.txt")

allWords = set(pwords + nwords)


pcounts = counts(pwords)
ncounts = counts(nwords)

pmax = maxvals(pcounts)
print("positive")
for w in range(1, 10):
  print(pmax[w])

nmax = maxvals(ncounts)
print("negative")
for w in range(1, 10):
  print(nmax[w])

def idf(words, ncounts, pcounts):
    idfs = dict()
    for w in words:
      idfs[w] = math.log(max(ncounts.get(w, 0), 1) + max(pcounts.get(w, 0), 1))
    return idfs

gidf = idf(allWords, ncounts, pcounts)

def tfidf(idfs, words, counts):
    tfidfs = dict()
    for w in words:
      tfidfs[w] = math.log(0.01 + (counts.get(w, 0) / len(counts)) * idfs[w])
    return tfidfs

ptfidf = tfidf(gidf, allWords, pcounts)

ntfidf = tfidf(gidf, allWords, ncounts)

#print(max(ptfidf, key = ptfidf.get))
#print(max(ntfidf, key = ntfidf.get))

#print(ptfidf[max(ptfidf, key = ptfidf.get)])


sorted_ptfidf = sorted(ptfidf.items(), key = operator.itemgetter(1), reverse = True)
sorted_ntfidf = sorted(ntfidf.items(), key = operator.itemgetter(1), reverse = True)

pptfidf = list()
nptfidf = list()

nufre = dict()
pufre = dict()

for swt in sorted_ptfidf:
  sw = swt[0]
  if sw in ncounts:
    if sw not in pcounts:
      nptfidf.append(swt)
      nufre[sw] = swt[1]
  elif sw in pcounts:
    pptfidf.append(swt)
    pufre[sw] = swt[1]

for swt in sorted_ntfidf:
  sw = swt[0]
  if sw in ncounts:
    if sw not in pcounts:
      nptfidf.append(swt)
      nufre[sw] = swt[1]
  elif sw in pcounts:
    pptfidf.append(swt)
    pufre[sw] = swt[1]

pptfidf.sort(key = lambda tup: tup[1], reverse = True)
nptfidf.sort(key = lambda tup: tup[1], reverse = True)

print("positive")
for s in range(1, 10):
  print(pptfidf[s])

print("negative")
for s in range(1, 10):
  print(nptfidf[s])


frequencies = sorted(ptfidf.items(), key=operator.itemgetter(1), reverse=True)
#print(frequencies)
for s in list(pufre):
  if pufre[s] == 0:
    del pufre[s]
    #print(s)
#max_frequency = float(frequencies[0][1])

#print(max_frequency)
#for word, freq in frequencies:
  #print(freq)
  #print(freq / max_frequency)
#frequencies = [(word, freq / max_frequency)
#for word, freq in frequencies]

wordcloud = WordCloud().generate_from_frequencies(pufre)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

wordcloud = WordCloud().generate_from_frequencies(nufre)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


#df = pd.DataFrame(pptfidf)
#print("test")
#print(df[0,0])
#df.pivot(index = 0, columns = 1, values = 2)
#df.pivot(index=0, columns=1, values=2)

#p = ggplot(aes(x='a'), data=df)
#p = ggplot(aes(x='date', y='beef'), data=meat)
#print(p)
#p + geom_histogram(binwidth=1)

#print("\n".join(sorted_ptfidf[1:10]))
#print("\n".join(sorted_ntfidf[1:10]))

