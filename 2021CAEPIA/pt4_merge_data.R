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

save(data, data8, data9, data10, file ="predict_time_results.RData")

tr <- function(n) {(n*(n-1))/2}

normalize <- function(data) {
  data <- data %>%
    mutate(n = (as.numeric(as.character(n))),
           m = (as.numeric(as.character(m))),
      
           mu1 = mu1/tr(n), # average kendall distance
           
           # Related to the range of positions that the candidates can have
           mu2 = mu2/(n-1), # maximum range of positions of the alternatives
           mu3 = mu3/(n-1), # minimum range of positions of the alternatives
           mu4 = mu4/(n-1), # average range of positions of the alternatives
            
           # Related to the distance
           # lower bound to the optimal distance
           mu5 = mu5/(tr(n)*trunc(m/2)),
           # upper bound to the optimal distance
           mu6 = (mu6-(tr(n)*ceiling(m/2)))/((m*tr(n))-(tr(n)*ceiling(m/2))),
           # range of values that the distance can take
           mu7 = mu7/(tr(n)*m),
          
           # Related to the pairwise comparison of the alternatives
           mu8 = mu8/m, # average margin or pairwise comparisons
           mu9 = (mu9-(m%%2))/(m-(m%%2)), # most common margin
           mu10 = (mu10-1)/(tr(n)-1), # number of unique pairs
           mu11 = mu11/tr(n), # frequency of the lowest margin
           
           mu12 = mu12/(tr(n)*m), # distance from the borda ranking to the profile
           
           # Related to the rowsum of the outranking matrix
           mu13 = (mu13-1)/(n-1), # omega
           mu14 = mu14/(m*tr(n)), # standard deviation of the rowsum
           
           # Related to the condorcet vector
           mu15 = mu15/mu16, # standard deviation
           mu16 = mu16/((n-1)/2), # mean
           mu17 = mu17/(n-1), # media
           mu18 = (mu18+(tr(n)*m))/((tr(n)*m)+(tr(n)*m)),
          # mu19 ? # sum the beta
         
            # Number of intransitive cycles
           mu20 = mu20/(factorial(n)/(factorial(3)*factorial(n-3))),
          
           
           n = as.factor(n),
           m = as.factor(m)
           )
  data
}
data_normalized <- normalize(data)

# check ranges for normalizing variables
data %>% group_by(n,m) %>% summarise(range_min = range(mu15)[1], range_max = range(mu15)[2])
# mean the beta is as maximum (n-1)/2

data %>% group_by(n,m) %>% 
  summarise(range_min = range(mu16)[1], range_max = range(mu16)[2]) %>%
  group_by(n) %>%
  count(range_max)

# median. por algún motivo salen de max ((n/2)+.5) o .1, 1.5
data %>% group_by(n,m, odd) %>% 
  summarise(range_min = range(mu17)[1], range_max = range(mu17)[2]) %>%
  group_by(n, odd) %>%
  count(range_max)

data %>% group_by(n,m) %>% 
  summarise(range_min = range(mu17)[1], range_max = range(mu17)[2]) %>%
  group_by(n) %>%
  count(range_max)

# mean-median
data_normalized %>% 
  #mutate(mu18 = abs(mu18)) %>%
  group_by(n,m) %>% 
  summarise(range_min = range(mu18)[1], range_max = range(mu18)[2]) 

ggpairs(data = data_normalized %>% select(paste0("mu", 5:7), odd), 
        mapping=ggplot2::aes(colour = odd))

        