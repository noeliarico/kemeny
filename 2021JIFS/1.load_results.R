library(tidyverse)

# The results are the same of the profiles for the EJOR paper

# n = 8,9,10 --------------------------------------------------------------

col_names <- c("n", "m", "id", "method", "exec_time", "nsol", "ntent", "t1", "t2", "t3")
folder <- "2021JIFS"

########################### ME #################################################

res_me_8 <- list.files(path = file.path(folder, "results"), 
                       pattern = "me_8", 
                       full.names = T) %>%
  lapply(read_csv, col_name = col_names) %>%
  bind_rows() %>%
  select(n, m, id, method, exec_time)

res_me_9 <- list.files(path = file.path(folder, "results"), 
                       pattern = "me_9", 
                       full.names = T) %>%
  lapply(read_csv, col_name = col_names) %>%
  bind_rows() %>%
  select(n, m, id, method, exec_time)

res_me_10 <- list.files(path = file.path(folder, "results"), 
                        pattern = "me_10", 
                        full.names = T) %>%
  lapply(read_csv, col_name = col_names) %>%
  bind_rows() %>%
  select(n, m, id, method, exec_time)

execution_times <- res_me_8 %>% 
  bind_rows(res_me_9) %>% 
  bind_rows(res_me_10) %>%
  mutate(n = as.factor(n),
         m = as.factor(m),
         id = as.factor(id),
         method = as.factor(method))

execution_times <- execution_times %>% mutate(method = NULL)
