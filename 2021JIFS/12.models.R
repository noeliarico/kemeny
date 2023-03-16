
totrain <- predict_times_mebbrcw %>% select(starts_with("mu"), time)
set.seed(3456)
trainIndex <- createDataPartition(totrain$time, p = .8, 
                                  list = FALSE, 
                                  times = 1)
dataTrain <- totrain[ trainIndex,]
dataTest  <- totrain[-trainIndex,]
model1_8 <- train(
  time ~., data = dataTrain, method = "rpart",
  tuneGrid = expand.grid(cp = seq(0.00001, 0.0001, 0.00001)),
  trControl = fitControl
)
model1_8
vip(model1_8)
pred <- predict(model1_8, dataTest)
postResample(pred = pred, obs = dataTest$time)


totrain <- predict_times_mebbrcw %>% select(starts_with("mu"), time)
set.seed(3456)
trainIndex <- createDataPartition(totrain$time, p = .8, 
                                  list = FALSE, 
                                  times = 1)
dataTrain <- totrain[ trainIndex,]
dataTest  <- totrain[-trainIndex,]
model1_8 <- train(
  time ~., data = dataTrain, method = "rpart",
  tuneGrid = expand.grid(cp = seq(0.00001, 0.0001, 0.00001)),
  trControl = fitControl
)
model1_8
vip(model1_8)
pred <- predict(model1_8, dataTest)
postResample(pred = pred, obs = dataTest$time)

