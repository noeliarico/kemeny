

library(caret)
predict_times_regression <- predict_times %>% 
  mutate(id = NULL, 
         nrankings = NULL)
  
set.seed(3456)
trainIndex <- createDataPartition(totrain$time, p = .8, 
                                  list = FALSE, 
                                  times = 1)
dataTrain <- totrain[ trainIndex,]
dataTest  <- totrain[-trainIndex,]
model1_8_10 <- train(
  time ~., data = dataTrain, method = "rpart",
 # tuneGrid = expand.grid(cp = seq(0.00001, 0.0001, 0.00001)),
  trControl = fitControl
)
model1_8_10 <- train(
  time ~., data = dataTrain, method = "cubist",
  # tuneGrid = expand.grid(cp = seq(0.00001, 0.0001, 0.00001)),
  trControl = fitControl
)

model1_8_10
vip(model1_8_10)
pred <- predict(model1_8_10, dataTest)
postResample(pred = pred, obs = dataTest$time)



