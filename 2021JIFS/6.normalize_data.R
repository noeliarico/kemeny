
data_normalized <- normalize(predict_times)
# apply(data_normalized %>% filter(n==10) %>% select(starts_with("mu")), 2, range)
apply(data_normalized %>% select(starts_with("mu")), 2, range)

# # check ranges for normalizing variables
# data %>% group_by(n,m) %>% summarise(range_min = range(mu15)[1], range_max = range(mu15)[2])
# # mean the beta is as maximum (n-1)/2
# 
# data %>% group_by(n,m) %>% 
#   summarise(range_min = range(mu16)[1], range_max = range(mu16)[2]) %>%
#   group_by(n) %>%
#   count(range_max)
# 
# # median. por algún motivo salen de max ((n/2)+.5) o .1, 1.5
# data %>% group_by(n,m, odd) %>% 
#   summarise(range_min = range(mu17)[1], range_max = range(mu17)[2]) %>%
#   group_by(n, odd) %>%
#   count(range_max)
# 
# data %>% group_by(n,m) %>% 
#   summarise(range_min = range(mu17)[1], range_max = range(mu17)[2]) %>%
#   group_by(n) %>%
#   count(range_max)
# 
# # mean-median
# data_normalized %>% 
#   #mutate(mu18 = abs(mu18)) %>%
#   group_by(n,m) %>% 
#   summarise(range_min = range(mu18)[1], range_max = range(mu18)[2]) 
# 
# ggpairs(data = data_normalized %>% select(paste0("mu", 5:7), odd), 
#         mapping=ggplot2::aes(colour = odd))
# 
