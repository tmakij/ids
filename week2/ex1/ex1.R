train = read.csv(file = "train.csv", stringsAsFactors = TRUE)
#test = read.csv(file = "test.csv", stringsAsFactors = FALSE)
#gender = read.csv(file = "gender_submission.csv", stringsAsFactors = FALSE)

train = train[, -4]
train$Deck = substring(text = train$Cabin,
                       first = 1,
                       last = 1)

encodeSex = function(sex) {
  if (sex == "male") {
    return(0)
  }
  return(1)
}

train$Sex = sapply(X = train$Sex, FUN = encodeSex)

encodeEmbarked = function(embarked) {
  if (embarked == "C") {
    return(0)
  }
  if (embarked == "Q") {
    return(1)
  }
  return(2)
}

train$Embarked = sapply(X = train$Embarked, FUN = encodeEmbarked)

train$Age[is.na(train$Age)] = mean(train$Age, na.rm = TRUE)

mode = function(x) {
  ux = unique(x)
  ux[which.max(tabulate(match(x, ux)))]
}

train$Deck[train$Deck == ""] = mode(train$Deck[train$Deck != ""])

stringMap = list()
ticketLevels = levels(train$Ticket)

for (i in 1:length(ticketLevels)) {
  stringMap[[ticketLevels[i]]] = i
}

train$Ticket = sapply(X = train$Ticket, FUN = function(ticket) stringMap[[ticket]])

stringMap = list()
cabinLevels = levels(train$Cabin)

for (i in 1:length(cabinLevels)) {
  stringMap[[cabinLevels[i]]] = i
}

train$Cabin = sapply(X = train$Cabin, FUN = function(cabin) stringMap[[cabin]])

stringMap = list()
deckLevels = unique(train$Deck)

for (i in 1:length(deckLevels)) {
  stringMap[[deckLevels[i]]] = i
}

train$Deck = sapply(X = train$Deck, FUN = function(deck) stringMap[[deck]])

write.csv(x = train, file = "train_modified.csv", row.names = FALSE, quote = FALSE)
#write.table(x = train, file = "train_modified.csv", col.names = TRUE, row.names = FALSE, sep = ",")
#write.table(trees, file="/tmp/trees.csv", row.names=FALSE, col.names=FALSE, sep=",")
library(jsonlite)

json = toJSON(train)
write(x = json, file = "train_modified.json")



