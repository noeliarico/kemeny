# n = 8,9,10 --------------------------------------------------------------

col_names_reps <- c("n", "m", "id", "method", "exec_time", "nsol", "ntent", "t1", "t2", "t3")

########################### ME #################################################

res_me_8 <- list.files(path = "2021EJOR/results/me/", 
                           pattern = "me_8", 
                           full.names = T) %>%
  lapply(read_csv, col_name = col_names_reps) %>%
  bind_rows() %>%
  select(n, m, id, method, exec_time)

res_me_9 <- list.files(path = "2021EJOR/results/me/", 
                       pattern = "me_9", 
                       full.names = T) %>%
  lapply(read_csv, col_name = col_names_reps) %>%
  bind_rows() %>%
  select(n, m, id, method, exec_time)

res_me_10 <- list.files(path = "2021EJOR/results/me/", 
                       pattern = "me_10", 
                       full.names = T) %>%
  lapply(read_csv, col_name = col_names_reps) %>%
  bind_rows() %>%
  select(n, m, id, method, exec_time)

########################### MERCW ##############################################

res_mercw_8 <- list.files(path = "2021EJOR/results/mercw/", 
                          pattern = "mercw_8", 
                          full.names = T) %>%
  lapply(read_csv, col_name = col_names_reps) %>%
  bind_rows() %>%
  select(n, m, id, method, exec_time)

res_mercw_9 <- list.files(path = "2021EJOR/results/mercw/", 
                          pattern = "mercw_9", 
                          full.names = T) %>%
  lapply(read_csv, col_name = col_names_reps) %>%
  bind_rows() %>%
  select(n, m, id, method, exec_time)

res_mercw_10 <- list.files(path = "2021EJOR/results/mercw/", 
                           pattern = "mercw_10", 
                           full.names = T) %>%
  lapply(read_csv, col_name = col_names_reps) %>%
  bind_rows() %>%
  select(n, m, id, method, exec_time)

############################# MEBB #############################################

res_mebb_8 <- list.files(path = "2021EJOR/results/mebb/", 
                          pattern = "mebb_8", 
                          full.names = T) %>%
  lapply(read_csv, col_name = col_names_reps) %>%
  bind_rows() %>%
  select(n, m, id, method, exec_time)

res_mebb_9 <- list.files(path = "2021EJOR/results/mebb/", 
                         pattern = "mebb_9", 
                         full.names = T) %>%
  lapply(read_csv, col_name = col_names_reps) %>%
  bind_rows() %>%
  select(n, m, id, method, exec_time)

res_mebb_10 <- list.files(path = "2021EJOR/results/mebb/", 
                         pattern = "mebb_10", 
                         full.names = T) %>%
  lapply(read_csv, col_name = col_names_reps) %>%
  bind_rows() %>%
  select(n, m, id, method, exec_time)

############################# MEBB #############################################

res_mebbd_8 <- list.files(path = "2021EJOR/results/mebbd/", 
                         pattern = "mebbd_8", 
                         full.names = T) %>%
  lapply(read_csv, col_name = col_names_reps) %>%
  bind_rows() %>%
  select(n, m, id, method, exec_time)

res_mebbd_9 <- list.files(path = "2021EJOR/results/mebbd/", 
                         pattern = "mebbd_9", 
                         full.names = T) %>%
  lapply(read_csv, col_name = col_names_reps) %>%
  bind_rows() %>%
  select(n, m, id, method, exec_time)

res_mebbd_10 <- list.files(path = "2021EJOR/results/mebbd/", 
                          pattern = "mebbd_10", 
                          full.names = T) %>%
  lapply(read_csv, col_name = col_names_reps) %>%
  bind_rows() %>%
  select(n, m, id, method, exec_time)

########################### MEBBRCW ###########################################


res_mebbrcw_8 <- list.files(path = "2021EJOR/results/mebbrcw/", 
                         pattern = "mebbrcw_8", 
                         full.names = T) %>%
  lapply(read_csv, col_name = col_names_reps) %>%
  bind_rows() %>%
  select(n, m, id, method, exec_time)

res_mebbrcw_9 <- list.files(path = "2021EJOR/results/mebbrcw/", 
                            pattern = "mebbrcw_9", 
                            full.names = T) %>%
  lapply(read_csv, col_name = col_names_reps) %>%
  bind_rows() %>%
  select(n, m, id, method, exec_time)

res_mebbrcw_10 <- list.files(path = "2021EJOR/results/mebbrcw/", 
                            pattern = "mebbrcw_10", 
                            full.names = T) %>%
  lapply(read_csv, col_name = col_names_reps) %>%
  bind_rows() %>%
  select(n, m, id, method, exec_time)

########################### MEBBRCW ###########################################


res_mebbrcwd_8 <- list.files(path = "2021EJOR/results/mebbrcwd/", 
                            pattern = "mebbrcwd_8", 
                            full.names = T) %>%
  lapply(read_csv, col_name = col_names_reps) %>%
  bind_rows() %>%
  select(n, m, id, method, exec_time)

res_mebbrcwd_9 <- list.files(path = "2021EJOR/results/mebbrcwd/", 
                            pattern = "mebbrcwd_9", 
                            full.names = T) %>%
  lapply(read_csv, col_name = col_names_reps) %>%
  bind_rows() %>%
  select(n, m, id, method, exec_time)

res_mebbrcwd_10 <- list.files(path = "2021EJOR/results/mebbrcwd/", 
                             pattern = "mebbrcwd_10", 
                             full.names = T) %>%
  lapply(read_csv, col_name = col_names_reps) %>%
  bind_rows() %>%
  select(n, m, id, method, exec_time)

###########################################################################
# BIND RESULTS BY METHOD --------------------------------------------------
###########################################################################

res_me <- res_me_8 %>% 
  bind_rows(res_me_9) %>% 
  bind_rows(res_me_10) %>%
  mutate(n = as.factor(n),
         m = as.factor(m),
         id = as.factor(id),
         method = as.factor(method))

res_mercw <- res_mercw_8 %>% 
  bind_rows(res_mercw_9) %>% 
  bind_rows(res_mercw_10) %>%
  mutate(n = as.factor(n),
         m = as.factor(m),
         id = as.factor(id),
         method = as.factor(method))

res_mebb <- res_mebb_8 %>% 
  bind_rows(res_mebb_9) %>% 
  bind_rows(res_mebb_10) %>%
  mutate(n = as.factor(n),
         m = as.factor(m),
         id = as.factor(id),
         method = as.factor(method))

res_mebbd <- res_mebbd_8 %>% 
  bind_rows(res_mebbd_9) %>% 
  bind_rows(res_mebbd_10) %>%
  mutate(n = as.factor(n),
         m = as.factor(m),
         id = as.factor(id),
         method = as.factor(method))

res_mebbrcw <- res_mebbrcw_8 %>% 
  bind_rows(res_mebbrcw_9) %>% 
  bind_rows(res_mebbrcw_10) %>%
  mutate(n = as.factor(n),
         m = as.factor(m),
         id = as.factor(id),
         method = as.factor(method))

res_mebbrcwd <- res_mebbrcwd_8 %>% 
  bind_rows(res_mebbrcwd_9) %>% 
  bind_rows(res_mebbrcwd_10) %>%
  mutate(n = as.factor(n),
         m = as.factor(m),
         id = as.factor(id),
         method = as.factor(method))


###########################################################################
# BIND RESULTS BY N -------------------------------------------------------
###########################################################################

results8 <- res_me_8 %>%
  bind_rows(res_mercw_8) %>%
  bind_rows(res_mebb_8) %>%
  bind_rows(res_mebbd_8) %>%
  bind_rows(res_mebbrcw_8) %>%
  bind_rows(res_mebbrcwd_8) 

results9 <- res_me_9 %>%
  bind_rows(res_mercw_9) %>%
  bind_rows(res_mebb_9) %>%
  bind_rows(res_mebbd_9) %>%
  bind_rows(res_mebbrcw_9) %>%
  bind_rows(res_mebbrcwd_9) 

results10 <- res_me_10 %>%
  bind_rows(res_mercw_10) %>%
  bind_rows(res_mebb_10) %>%
  bind_rows(res_mebbd_10) %>%
  bind_rows(res_mebbrcw_10) %>%
  bind_rows(res_mebbrcwd_10) 


# Results for the benchmarking of all the methods
results_ejor <- res_me %>%
  bind_rows(res_mercw) %>%
  bind_rows(res_mebb) %>%
  bind_rows(res_mebbd) %>%
  bind_rows(res_mebbrcw) %>%
  bind_rows(res_mebbrcwd) 
results_ejor %>% group_by(method) %>% count()

################################################################################
########## RESULTS FOR LARGE VALUES OF N #######################################
################################################################################

col_names_sin_reps <- c("n", "m", "id", "method", "exec_time", "nsol", "ntent", "t1")

res_mebbrcw_11 <- list.files(path = "2021EJOR/results/mebbrcw/", 
                             pattern = "mebbrcw_11", 
                             full.names = T) %>%
  lapply(read_csv, col_name = col_names_sin_reps) %>%
  bind_rows() %>%
  select(n, m, id, method, exec_time) 

res_mebbrcw_12 <- list.files(path = "2021EJOR/results/mebbrcw/", 
                             pattern = "mebbrcw_12", 
                             full.names = T) %>%
  lapply(read_csv, col_name = col_names_sin_reps) %>%
  bind_rows() %>%
  select(n, m, id, method, exec_time) 

res_mebbrcw_13 <- list.files(path = "2021EJOR/results/mebbrcw/", 
                             pattern = "mebbrcw_13", 
                             full.names = T) %>%
  lapply(read_csv, col_name = col_names_sin_reps) %>%
  bind_rows() %>%
  select(n, m, id, method, exec_time) 

res_mebbrcw_14 <- list.files(path = "2021EJOR/results/mebbrcw/", 
                             pattern = "mebbrcw_14_11.csv", 
                             full.names = T) %>%
  lapply(read_csv, col_name = col_names_sin_reps) %>%
  bind_rows() %>%
  select(n, m, id, method, exec_time) 

res_mebbrcw_15 <- list.files(path = "2021EJOR/results/mebbrcw/", 
                             pattern = "mebbrcw_15_11.csv", 
                             full.names = T) %>%
  lapply(read_csv, col_name = col_names_sin_reps) %>%
  bind_rows() %>%
  select(n, m, id, method, exec_time) 

res_large_n <- res_mebbrcw_8 %>% 
  bind_rows(res_mebbrcw_9) %>% 
  bind_rows(res_mebbrcw_10) %>%
  bind_rows(res_mebbrcw_11) %>%
  bind_rows(res_mebbrcw_12) %>%
  bind_rows(res_mebbrcw_13) %>%
  bind_rows(res_mebbrcw_14) %>%
  bind_rows(res_mebbrcw_15) %>%
  mutate(n = as.factor(n),
         m = as.factor(m),
         id = as.factor(id),
         method = as.factor(method))


