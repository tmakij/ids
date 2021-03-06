titanic = read.csv(file = "train_modified.csv", stringsAsFactors = FALSE)

mode = function(x) {
  ux = unique(x)
  ux[which.max(tabulate(match(x, ux)))]
}

avgperson = function(subdata) {
  list(
    survived = mode(subdata$Survived),
    pclass = mode(subdata$Pclass),
    sex = mode(subdata$Sex),
    age = mean(subdata$Age),
    sib = round(mean(subdata$SibSp)),
    parch = round(mean(subdata$Parch)),
    fare = mean(subdata$Fare),
    cabin = mode(subdata$Cabin),
    embarked = mode(subdata$Embarked),
    deck = mode(subdata$Deck)
  )
}

avg.passenger = avgperson(titanic)

survivors = titanic[titanic$Survived == 1, ]
avg.survivor = avgperson(survivors)

dead = titanic[titanic$Survived == 0, ]
avg.dead = avgperson(dead)

persd = function(subdata, person) {
  print(paste0("Data age avg ", person$age, " with dev ", sd(subdata$Age)))
  print(paste0("Data fare avg ", person$fare, " with dev ", sd(subdata$Fare)))
  cat(paste0("Data sex mode ", person$sex, " with table "))
  print(table(subdata$Sex))
  cat(paste0("Data siblings/spouses mode ", person$sib, " with table "))
  print(table(subdata$SibSp))
  cat(paste0("Data parents/children mode ", person$parch, " with table "))
  print(table(subdata$Parch))
  cat(paste0("Data class mode ", person$pclass, " with table "))
  print(table(subdata$Pclass))
  #cat(paste0("Data deck mode ", person$deck, " with table "))
  #print(table(subdata$Deck))
  cat(paste0("Data embarked mode ", person$embarked, " with table "))
  print(table(subdata$Embarked))
}

"all"
persd(titanic, avg.passenger)

"survivors"
persd(survivors, avg.survivor)

"dead"
persd(dead, avg.dead)

table(titanic$Pclass)
#table(survivors$Pclass)
table(dead$Pclass)

#Dead
#1st class
80 / 216

#2nd class
97 / 184

#3rd class
372 / 491

table(titanic$Embarked)
#table(survivors$Pclass)
table(dead$Embarked)

#Cherbourg
75 / 168
# ^less likely to die

#Queenstown
47 / 77

#Southampton
427 / 646

#hist(survivors$Age)

#age.ts = ts(survivors$Age, start = 0, end = 100)
#plot(age.ts, main = "Toy example", ylab = "age", xlab = "count")

#hist(survivors$Age, prob = TRUE, ylim = c(0, 0.10))
#plot.new()
plot(
  0,
  type = "n",
  xlab = "Age",
  ylab = "Density",
  xlim = c(0, 100),
  ylim = c(0, 0.1),
  yaxs = "i",
  xaxs = "i"
)
lines(density(survivors$Age), col = "blue")
lines(density(dead$Age), col = "red")

#hist(survivors$Ticket, prob = TRUE, ylab = "Ticket price")
#plot.new()
plot(
  0,
  type = "n",
  xlab = "Fare",
  ylab = "Density",
  xlim = c(0, 550),
  ylim = c(0, 0.07),
  yaxs = "i"
)
lines(density(survivors$Fare), col = "blue")
lines(density(dead$Fare), col = "red")

ds = prop.table(table(dead$Sex))
ss = prop.table(table(survivors$Sex))

frd = matrix(c(ds[1], ss[1], ds[2] , ss[2]), nrow = 2, dimnames = list(c("Women", "Men"), c("Dead", "Alive")))
#names(frd) = c("Women", "Men","Women", "Men")
barplot(frd, col = c("red", "blue"), beside = TRUE, xlab = "Red women, blue men")

# Inputation of most common  is really bad


