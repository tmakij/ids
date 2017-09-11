import json
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")

with open("reviews_Automotive_5.json") as data_file:    
    data = data_file.readlines()

with open("stop") as stops_file:    
    stops = stops_file.read().splitlines()

data = map(lambda x: x.rstrip(), data)

data_json_str = "[" + ','.join(data) + "]"
reviews = json.loads(data_json_str)

punct = [",", ".", "!", "?", ":", ";", "-", "'", "´"]

positives = list()

negatives = list()

for i in range(0, len(reviews)):
  review = reviews[i]
  text = review["reviewText"]
  text = text.lower()
  for rem in punct:
    text = text.replace(rem, " ")
    if (text.startswith(rem)):
      text = text[len(rem):]
    if (text.endswith(rem)):
      text = text[:len(rem)]
  for rem in stops:
    text = text.replace(" " + rem + " ", " ")
    if (text.startswith(rem)):
      text = text[len(rem):]
    if (text.endswith(rem)):
      text = text[:len(rem)]
  splitted = text.split()
  for i in range(0, len(splitted)):
    splitted[i] = stemmer.stem(splitted[i])
  text = " ".join(splitted)
  if (review["overall"] > 3):
    positives.append(text)
  elif (review["overall"] < 3):
    negatives.append(text)

with open("pos.txt", "w") as posf:
  for item in positives:
    if (len(item) > 0):
      posf.write("%s\n" % item)

with open("neg.txt", "w") as negf:
  for item in negatives:
    if (len(item) > 0):
      negf.write("%s\n" % item)
