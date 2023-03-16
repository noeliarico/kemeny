indexes8 <- indexes8 %>% 
  mutate(dist = rep(c(rep("unif", 1000), rep("norm", 1000)), nrow(indexes8)/2000))
indexes9 <- indexes9 %>% 
  mutate(dist = rep(c(rep("unif", 1000), rep("norm", 1000)), nrow(indexes9)/2000))
indexes10 <- indexes10 %>% 
  mutate(dist = rep(c(rep("unif", 1000), rep("norm", 1000)), nrow(indexes10)/2000))
data8 <- inner_join(times8, indexes8, by = c("profile","n","m","dist"))
data9 <- inner_join(times9, indexes9, by = c("profile","n","m","dist"))
data10 <- inner_join(times10, indexes10, by = c("profile","n","m","dist"))
data <- bind_rows(data8, data9, data10)  %>% 
mutate(basem = ifelse(m%%2==0, m, m-1),
       odd = as.factor(ifelse(m%%2==0, "yes", "no")),
       n = as.factor(n),
       m = as.factor(m),
       quartile = as.factor(quartile)
)

save(data, data8, data9, data10, file =file.path(folder, "predict_time_results.RData"))
