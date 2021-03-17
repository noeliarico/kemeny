data <- resultsNC12
profiles <- pors12nc

data <- data %>% 
  filter(method == 1) %>%
  select(id, time, nsolutions, ntentative) %>%
  
