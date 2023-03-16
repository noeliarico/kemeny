library(arules)
library(caret)
library(vip)

fitControl <- trainControl(## 10-fold CV
  method = "repeatedcv",
  number = 10,
  repeats = 2)

# PROBLEM 1 ----------------------------------------------

## rpart para n = 8 ---------

totrain <- data_normalized %>% filter(n==10) %>% select(starts_with("mu"), time)
set.seed(3456)
trainIndex <- createDataPartition(totrain$time, p = .8, 
                                  list = FALSE, 
                                  times = 1)
dataTrain <- totrain[ trainIndex,]
dataTest  <- totrain[-trainIndex,]
model1_8 <- train(
  time ~., data = dataTrain, method = "rf",
  # tuneGrid = expand.grid(cp = seq(0.00001, 0.0001, 0.00001)),
  trControl = fitControl
)
model1_8
vip(model1_8)
pred <- predict(model1_8, dataTest)
postResample(pred = pred, obs = dataTest$time)

## rpart para n=9 -----------------
totrain <- data %>% select(starts_with("mu"), n, time, odd) %>% filter(n==9) %>% select(-mu5,-n)
set.seed(3456)
trainIndex <- createDataPartition(totrain$time, p = .8, 
                                  list = FALSE, 
                                  times = 1)
dataTrain <- totrain[ trainIndex,]
dataTest  <- totrain[-trainIndex,]
model1_9 <- train(
  time ~., data = dataTrain, method = "rpart",
  tuneGrid = expand.grid(cp = seq(0.00001, 0.0001, 0.00001)),
  trControl = fitControl
)
model1_9
vip(model1_9)
pred <- predict(model1_9, dataTest)
postResample(pred = pred, obs = dataTest$time)

## rpart para n=10 -------------
totrain <- data %>% select(starts_with("mu"), n, time, odd) %>% filter(n==10) %>% select(-mu5,-n)
set.seed(3456)
trainIndex <- createDataPartition(totrain$time, p = .8, 
                                  list = FALSE, 
                                  times = 1)
dataTrain <- totrain[ trainIndex,]
dataTest  <- totrain[-trainIndex,]
model1_10 <- train(
  time ~., data = dataTrain, method = "rpart",
  tuneGrid = expand.grid(cp = seq(0.00001, 0.0001, 0.00001)),
  trControl = fitControl
)
model1_10
vip(model1_10)
pred <- predict(model1_10, dataTest)
postResample(pred = pred, obs = dataTest$time)

## rpart para todos a la vez -----------------
totrain <- data %>% select(starts_with("mu"), time) %>% select(-mu5)
set.seed(3456)
trainIndex <- createDataPartition(totrain$time, p = .8, 
                                  list = FALSE, 
                                  times = 1)
dataTrain <- totrain[ trainIndex,]
dataTest  <- totrain[-trainIndex,]
model1_all <- train(
  time ~., data = dataTrain, method = "rpart",
  tuneGrid = expand.grid(cp = seq(0.00001, 0.0001, 0.00001)),
  trControl = fitControl
)
model1_all
vip(model1_all)
pred <- predict(model1_all, dataTest)
postResample(pred = pred, obs = dataTest$time)





## cubist para n=8 ----------

totrain <- data %>% select(starts_with("mu"), n, time, odd) %>% filter(n==8) %>% select(-mu5,-n)
set.seed(3456)
trainIndex <- createDataPartition(totrain$time, p = .8, 
                                  list = FALSE, 
                                  times = 1)
dataTrain <- totrain[ trainIndex,]
dataTest  <- totrain[-trainIndex,]

model2_8 <- train(
  time ~., data = dataTrain, method = "cubist",
  tuneLength = 3,
  #tuneGrid = expand.grid(cp = seq(0.00001, 0.0001, 0.00001)),
  trControl = fitControl
)
model2_8
vip(model2_8)
pred <- predict(model2_8, dataTest)
postResample(pred = pred, obs = dataTest$time)

## cubist para n=9 ----------

totrain <- data %>% select(starts_with("mu"), n, time, odd) %>% filter(n==9) %>% select(-mu5,-n)
set.seed(3456)
trainIndex <- createDataPartition(totrain$time, p = .8, 
                                  list = FALSE, 
                                  times = 1)
dataTrain <- totrain[ trainIndex,]
dataTest  <- totrain[-trainIndex,]

model2_9 <- train(
  time ~., data = dataTrain, method = "cubist",
  tuneLength = 3,
  #tuneGrid = expand.grid(cp = seq(0.00001, 0.0001, 0.00001)),
  trControl = fitControl
)
model2_9
vip(model2_9)
pred <- predict(model2_9, dataTest)
postResample(pred = pred, obs = dataTest$time)

## cubist para n=10 ----------

totrain <- data %>% select(starts_with("mu"), n, time, odd) %>% filter(n==10) %>% select(-mu5,-n)
set.seed(3456)
trainIndex <- createDataPartition(totrain$time, p = .8, 
                                  list = FALSE, 
                                  times = 1)
dataTrain <- totrain[ trainIndex,]
dataTest  <- totrain[-trainIndex,]

model2_10<- train(
  time ~., data = dataTrain, method = "cubist",
  tuneLength = 3,
  #tuneGrid = expand.grid(cp = seq(0.00001, 0.0001, 0.00001)),
  trControl = fitControl
)
model2_10
vip(model2_10)
pred <- predict(model2_10, dataTest)
postResample(pred = pred, obs = dataTest$time)

## cubist para todos ----------

totrain <- data %>% select(starts_with("mu"), time, odd) %>% select(-mu5,-n)
set.seed(3456)
trainIndex <- createDataPartition(totrain$time, p = .8, 
                                  list = FALSE, 
                                  times = 1)
dataTrain <- totrain[ trainIndex,]
dataTest  <- totrain[-trainIndex,]

model2_all<- train(
  time ~., data = dataTrain, method = "cubist",
  tuneLength = 3,
  #tuneGrid = expand.grid(cp = seq(0.00001, 0.0001, 0.00001)),
  trControl = fitControl
)

model2_all
vip(model2_all)
pred <- predict(model2_all, dataTest)
postResample(pred = pred, obs = dataTest$time)

# plots para problem 1 regression --------

v1_8 <- vip(model1_8) + labs(title = "n=8")
v1_9 <- vip(model1_9) + labs(title = "n=9")
v1_10 <- vip(model1_10) + labs(title = "n=10")
v1_all <- vip(model1_all) + labs(title = "All n")
v1_8+v1_9+v1_10+v1_all+plot_layout(ncol = 4)

v2_8 <- vip(model2_8) + labs(title = "n=8")
v2_9 <- vip(model2_9) + labs(title = "n=9")
v2_10 <- vip(model2_10) + labs(title = "n=10")
v2_all <- vip(model2_all) + labs(title = "All n")
v2_8+v2_9+v2_10+v2_all+plot_layout(ncol = 4)

