import pandas
import os
import sklearn.linear_model
import numpy
import random
from scipy import misc
import matplotlib.pyplot as plt

data = pandas.read_csv("data/hasy-data-labels.csv")
data = data[data.symbol_id <= 80]
data = data[data.symbol_id >= 70]

data.sample(frac=1)


imgs = list()

for img_path in data.path:
  image = misc.imread(os.path.join("data", img_path))
  imagebw = list()
  for x in range(0, len(image)):
    for y in range(0, len(image)):
      imagebw.append(0 if image[x, y, 1] == 0 else 1)
  imgs.append(imagebw)
  

result = pandas.DataFrame.from_records(imgs)
result["value"] = pandas.Series(data["latex"].astype(int)).values
result["path"] = pandas.Series(data["path"]).values

msk = numpy.random.rand(len(result)) < 0.8
train = result[msk].drop("path", axis=1)
testP = result[~msk]
test = testP.drop("path", axis=1)

logfit = sklearn.linear_model.LogisticRegression()
logfit.fit(train.drop("value", axis=1), train.value)

prediction = logfit.predict(test.drop("value", axis=1))
randoms = [random.randint(0, 9) for i in range(0, len(prediction))]

corrRand = 0
corrPred = 0

wrongGuesses = list()

i = 0
for index, row in testP.iterrows():
  correct = row["value"]
  if correct == prediction[i]:
    corrPred = corrPred + 1
  else:
    wrongGuesses.append(row["path"])
  if correct == randoms[i]:
    corrRand = corrRand + 1
  i = i + 1

print(corrPred / i)
print(corrRand / i)

#plt.imshow(numpy.uint8(misc.imread(os.path.join("data", wrongGuesses[0]))))
#plt.show()

#plt.imshow(numpy.uint8(misc.imread(os.path.join("data", wrongGuesses[2]))))
#plt.show()

