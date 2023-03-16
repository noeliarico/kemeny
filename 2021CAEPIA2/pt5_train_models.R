library(arules)
library(caret)
library(vip)

fitControl <- trainControl(## 10-fold CV
  method = "repeatedcv",
  number = 10,
  repeats = 2)

# PROBLEM 1 ----------------------------------------------

## rpart para n = 8 ---------

totrain <- data %>% select(starts_with("mu"), n, time, odd) %>% filter(n==8) %>% select(-mu5,-n)
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


###### problem 1 classification 50-50


fitControl <- trainControl(#method = "cv", 
                     method = "repeatedcv",
                     number = 10,
                     repeats = 2,
                     classProbs = TRUE,
                     summaryFunction = prSummary)

totrain <- data %>% filter(n==8) %>% 
  mutate(quartile = fct_collapse(quartile, fast = c("q1","q2"), slow = c("q3","q4"))) %>%
  select(starts_with("mu"), quartile) %>% 
  select(-mu5)

set.seed(3456)
trainIndex <- createDataPartition(totrain$quartile, p = .8, 
                                  list = FALSE, 
                                  times = 1)
head(trainIndex)
dataTrain <- totrain[ trainIndex,]
dataTest  <- totrain[-trainIndex,]
model3_8 <- train(
  quartile ~., data = dataTrain, method = "rpart",
  #tuneLength = 3,
  tuneGrid = expand.grid(cp = seq(0.00001, 0.0001, 0.00001)),
  trControl = fitControl,
  metric = "Precision"
)
model3_8
confusionMatrix(model3_8)
vip(model3_8)


totrain <- data %>% filter(n==9) %>% 
  mutate(quartile = fct_collapse(quartile, fast = c("q1","q2"), slow = c("q3","q4"))) %>%
  select(starts_with("mu"), quartile) %>% 
  select(-mu5)

set.seed(3456)
trainIndex <- createDataPartition(totrain$quartile, p = .8, 
                                  list = FALSE, 
                                  times = 1)
head(trainIndex)
dataTrain <- totrain[ trainIndex,]
dataTest  <- totrain[-trainIndex,]
model3_9 <- train(
  quartile ~., data = dataTrain, method = "rpart",
  #tuneLength = 3,
  tuneGrid = expand.grid(cp = seq(0.00001, 0.0001, 0.00001)),
  trControl = fitControl,
  metric = "Precision"
)
model3_9
confusionMatrix(model3_9)
vip(model3_9)




totrain <- data %>% filter(n==10) %>% 
  mutate(quartile = fct_collapse(quartile, fast = c("q1","q2"), slow = c("q3","q4"))) %>%
  select(starts_with("mu"), quartile) %>% 
  select(-mu5)

set.seed(3456)
trainIndex <- createDataPartition(totrain$quartile, p = .8, 
                                  list = FALSE, 
                                  times = 1)
head(trainIndex)
dataTrain <- totrain[ trainIndex,]
dataTest  <- totrain[-trainIndex,]
model3_10 <- train(
  quartile ~., data = dataTrain, method = "rpart",
  #tuneLength = 3,
  tuneGrid = expand.grid(cp = seq(0.00001, 0.0001, 0.00001)),
  trControl = fitControl,
  metric = "Precision"
)
model3_10
confusionMatrix(model3_10)
vip(model3_10)

totrain <- data %>%
  mutate(quartile = fct_collapse(quartile, fast = c("q1","q2"), slow = c("q3","q4"))) %>%
  select(starts_with("mu"), quartile) %>% 
  select(-mu5)

set.seed(3456)
trainIndex <- createDataPartition(totrain$quartile, p = .8, 
                                  list = FALSE, 
                                  times = 1)
head(trainIndex)
dataTrain <- totrain[ trainIndex,]
dataTest  <- totrain[-trainIndex,]
model3_all <- train(
  quartile ~., data = dataTrain, method = "rpart",
  #tuneLength = 3,
  tuneGrid = expand.grid(cp = seq(0.00001, 0.0001, 0.00001)),
  trControl = fitControl,
  metric = "Precision"
)
model3_all
confusionMatrix(model3_all)
vip(model3_all)
pred <- predict(model3_all, dataTest)
postResample(pred = pred, obs = dataTest$quartile)
confusionMatrix(data = pred, reference = dataTest$quartile, mode = "prec_recall")



v3_8 <- vip(model3_8) + labs(title = "n=8")
v3_9 <- vip(model3_9) + labs(title = "n=9")
v3_10 <- vip(model3_10) + labs(title = "n=10")
v3_all <- vip(model3_all) + labs(title = "All n")
v3_8+v3_9+v3_10+v3_all+plot_layout(ncol = 4)



##### regression q1 vs q2,q3,q4

totrain <- data %>%
  mutate(quartile = fct_collapse(quartile, fast = c("q1"), slow = c("q2","q3","q4"))) %>%
  select(starts_with("mu"), quartile) %>% 
  select(-mu5)

set.seed(3456)
trainIndex <- createDataPartition(totrain$quartile, p = .8, 
                                  list = FALSE, 
                                  times = 1)
head(trainIndex)
dataTrain <- totrain[ trainIndex,]
dataTest  <- totrain[-trainIndex,]
model4_all <- train(
  quartile ~., data = dataTrain, method = "rpart",
  #tuneLength = 3,
  tuneGrid = expand.grid(cp = seq(0.00001, 0.0001, 0.00001)),
  trControl = fitControl,
  metric = "Precision"
)
model4_all
confusionMatrix(model4_all)
vip(model4_all)
pred <- predict(model4_all, dataTest)
postResample(pred = pred, obs = dataTest$quartile)
confusionMatrix(data = pred, reference = dataTest$quartile, mode = "prec_recall")




totrain <- data %>% filter(n==8) %>%
  mutate(quartile = fct_collapse(quartile, fast = c("q1"), slow = c("q2","q3","q4"))) %>%
  select(starts_with("mu"), quartile) %>% 
  select(-mu5)

set.seed(3456)
trainIndex <- createDataPartition(totrain$quartile, p = .8, 
                                  list = FALSE, 
                                  times = 1)
head(trainIndex)
dataTrain <- totrain[ trainIndex,]
dataTest  <- totrain[-trainIndex,]
model4_8 <- train(
  quartile ~., data = dataTrain, method = "rpart",
  #tuneLength = 3,
  tuneGrid = expand.grid(cp = seq(0.00001, 0.0001, 0.00001)),
  trControl = fitControl,
  metric = "Precision"
)
model4_8
confusionMatrix(model4_8)
vip(model4_8)
pred <- predict(model4_8, dataTest)
postResample(pred = pred, obs = dataTest$quartile)



totrain <- data %>% filter(n==9) %>%
  mutate(quartile = fct_collapse(quartile, fast = c("q1"), slow = c("q2","q3","q4"))) %>%
  select(starts_with("mu"), quartile) %>% 
  select(-mu5)

set.seed(3456)
trainIndex <- createDataPartition(totrain$quartile, p = .8, 
                                  list = FALSE, 
                                  times = 1)
head(trainIndex)
dataTrain <- totrain[ trainIndex,]
dataTest  <- totrain[-trainIndex,]
model4_9 <- train(
  quartile ~., data = dataTrain, method = "rpart",
  #tuneLength = 3,
  tuneGrid = expand.grid(cp = seq(0.00001, 0.0001, 0.00001)),
  trControl = fitControl,
  metric = "Precision"
)
model4_9
confusionMatrix(model4_9)
vip(model4_9)
pred <- predict(model4_9, dataTest)
postResample(pred = pred, obs = dataTest$quartile)


totrain <- data %>% filter(n==10) %>%
  mutate(quartile = fct_collapse(quartile, fast = c("q1"), slow = c("q2","q3","q4"))) %>%
  select(starts_with("mu"), quartile) %>% 
  select(-mu5)
set.seed(3456)
trainIndex <- createDataPartition(totrain$quartile, p = .8, 
                                  list = FALSE, 
                                  times = 1)
head(trainIndex)
dataTrain <- totrain[ trainIndex,]
dataTest  <- totrain[-trainIndex,]
model4_10 <- train(
  quartile ~., data = dataTrain, method = "rpart",
  #tuneLength = 3,
  tuneGrid = expand.grid(cp = seq(0.00001, 0.0001, 0.00001)),
  trControl = fitControl,
  metric = "Precision"
)
model4_10
confusionMatrix(model4_10)
vip(model4_10)
pred <- predict(model4_10, dataTest)
postResample(pred = pred, obs = dataTest$quartile)


v4_8 <- vip(model4_8) + labs(title = "n=8")
v4_9 <- vip(model4_9) + labs(title = "n=9")
v4_10 <- vip(model4_10) + labs(title = "n=10")
v4_all <- vip(model4_all) + labs(title = "All n")
v4_8+v4_9+v4_10+v4_all+plot_layout(ncol = 4)



################################################################################
################ PROBLEM 2 #####################################################



totrain <- data_normalized %>% filter(n!=10) %>%
  mutate(quartile = fct_collapse(quartile, fast = c("q1"), slow = c("q2","q3","q4"))) %>%
  select(starts_with("mu"), quartile) %>% 
  select(-mu5)
tovalidate <- data_normalized %>% filter(n==10) %>%
  mutate(quartile = fct_collapse(quartile, fast = c("q1"), slow = c("q2","q3","q4"))) %>%
  select(starts_with("mu"), quartile) %>% 
  select(-mu5)
set.seed(3456)
trainIndex <- createDataPartition(totrain$quartile, p = .8, 
                                  list = FALSE, 
                                  times = 1)
head(trainIndex)
dataTrain <- totrain[ trainIndex,]
dataTest  <- totrain[-trainIndex,]
model5 <- train(
  quartile ~., data = dataTrain, method = "rpart",
  #tuneLength = 3,
  tuneGrid = expand.grid(cp = seq(0.00001, 0.0001, 0.00001)),
  trControl = fitControl,
  metric = "Precision"
)
model5
confusionMatrix(model5)
vip(model5)
pred <- predict(model5, dataTest)
postResample(pred = pred, obs = dataTest$quartile)
pred <- predict(model5, tovalidate)
postResample(pred = pred, obs = tovalidate$quartile)
confusionMatrix(data = pred, reference = tovalidate$quartile, mode = "prec_recall")




a <- tribble(~n, ~time,
2^4, 0.022770404815673828,
2^5, 0.1213388442993164,
2^6, 0.6537337303161621,
2^7, 8.118041276931763,
2^8, 93.69074010848999,
2^9, 855.8209142684937)
ggplot(a, aes(n, time)) + 
  geom_line(alpha = 0.3) + 
  geom_point() + 
  geom_text(aes(label = paste0(round(time, 2),"s")), vjust = -.8, hjust = -.2, family = "Times New Roman") + 
 # geom_hline(yintercept = 60, linetype = "dashed", alpha = 0.2) +
  scale_y_continuous(breaks = 60*(seq(1,20,2)), labels = seq(1,20,2), limits = c(0,900)) +
  theme_bw() + 
  theme(text=element_text(family="Times New Roman", size=14),
        panel.grid.minor.x = element_blank(),
        panel.grid.minor.y = element_blank()) +
  #scale_x_continuous(trans='log2', breaks = 2^(4:9), labels=scales::math_format(2^log2(.x)))
  scale_x_continuous(expand = expansion(mult = c(0.05, .3)),
                      trans = scales::log2_trans(),
                     breaks = scales::trans_breaks("log2", function(x) 2^x),
                     labels = scales::trans_format("log2", scales::math_format(2^.x))) +
  xlab("Number of focal elements of each set") +
  ylab("Execution time (in minutes)")
  






