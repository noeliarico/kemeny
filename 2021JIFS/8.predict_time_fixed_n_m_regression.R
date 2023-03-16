#For the reggresion problem
fitControl <- trainControl(
  method = "repeatedcv",
  number = 5,
  repeats = 2)

library(caret)
predict_times_regression <- predict_times %>% 
  mutate(id = NULL, 
         nrankings = NULL)

totrain <- predict_times_regression %>% filter(n == 8) %>% mutate(n=NULL,m=NULL)
totrain <- data_normalized %>% filter(n == 8) %>% select(starts_with("mu"), time)

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



