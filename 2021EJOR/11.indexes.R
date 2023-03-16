# For each of the profiles of rankings

# 4 must be executed before in order to load the profiles into the profiles_ejor environment
indexes <- tribble(~n, ~m, ~id, ~nrankings, 
                   ~mu1,
                   ~mu2, ~mu3, ~mu4,
                   ~mu5,
                   ~mu6, 
                   ~mu7, ~mu8, ~mu9, 
                   ~mu10, ~mu11, ~mu12, 
                   ~mu13, ~mu14, ~mu15, ~mu16)
names <- list.files(file.path(folder, "profiles_of_rankings")) %>% str_remove(".RData")
for(name in names) {
  info <- str_remove(name, "porsEJOR") %>% str_split("_", simplify = TRUE)
  n <- as.numeric(info[1,1])
  m <- as.numeric(info[1,2])
  porsPredictTime <- get(name, envir = profiles_ejor)
  
  nrankings <- sapply(porsPredictTime, function(x) nrow(x$profileOfRankings))
  mu1 <- sapply(porsPredictTime, d1)
  mu2 <- sapply(porsPredictTime, d2)
  mu3 <- sapply(porsPredictTime, d3)
  mu4 <- sapply(porsPredictTime, d4)
  mu5 <- sapply(porsPredictTime, d5)
  mu6 <- sapply(porsPredictTime, d6)
  mu7 <- sapply(porsPredictTime, d7)
  mu8 <- sapply(porsPredictTime, d8)
  mu9 <- sapply(porsPredictTime, d9)
  mu10 <- sapply(porsPredictTime, d10)
  mu11 <- sapply(porsPredictTime, d11)
  mu12 <- sapply(porsPredictTime, d12)
  mu13 <- sapply(porsPredictTime, d13)
  mu14 <- sapply(porsPredictTime, d14)
  mu15 <- sapply(porsPredictTime, d15)
  mu16 <- sapply(porsPredictTime, d16)
  
  info <- tibble(n = n,
                 m = m,
                 id = 1:length(porsPredictTime),
                 nrankings = nrankings,
                 mu1 = mu1, 
                 mu2 = mu2,
                 mu3 = mu3, 
                 mu4 = mu4,
                 mu5 = mu5,
                 mu6 = mu6, 
                 mu7 = mu7, 
                 mu8 = mu8, 
                 mu9 = mu9, 
                 mu10 = mu10, 
                 mu11 = mu11, 
                 mu12 = mu12, 
                 mu13 = mu13, 
                 mu14 = mu14, 
                 mu15 = mu15, 
                 mu16 = mu16)
  
  indexes <- indexes %>% bind_rows(info)
}

# Add the execution times

indexes_join <- indexes %>%
  mutate(n = as.character(n),
         m = as.character(m),
         id = as.character(id))
predict_times <- res_large_n %>%
  mutate(n = as.character(n),
         m = as.character(m),
         id = as.character(id)) %>%
  left_join(indexes_join, 
            by = c("n"="n", "m"="m", "id"="id")) %>%
  mutate(n = as.factor(n),
         m = as.factor(m),
         id = as.factor(id)) %>% 
  rename(time = "exec_time") 

predict_times_me <- predict_times %>% filter(method == "ME") 
predict_times_mebbrcw <- predict_times %>% filter(method == "ME-BBRCW") 

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

