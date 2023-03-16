# For each of the profiles of rankings
library(consensus)

indexes <- tribble(~n, ~m, ~id, ~nrankings, 
                   ~mu1,
                   ~mu2, ~mu3, ~mu4,
                   ~mu5,
                   ~mu6, 
                   ~mu7, ~mu8, ~mu9, 
                   ~mu10, ~mu11, ~mu12, 
                   ~mu13, ~mu14, ~mu15, ~mu16)

names <- list.files(file.path(folder, "profiles")) %>% str_remove(".RData")
for(name in names) {
  info <- str_remove(name, "porsJIFS") %>% str_split("_", simplify = TRUE)
  print(name)
  n <- as.numeric(info[1,1])
  m <- as.numeric(info[1,2])
  pors <- get(name, envir = profiles_jifs)
  
  nrankings <- sapply(pors, function(x) nrow(x$profileOfRankings))
  
  
  # Compute the indexes
  mu1 <-  sapply(pors, d1)
  mu2 <-  sapply(pors, d2)
  mu3 <-  sapply(pors, d3)
  mu4 <-  sapply(pors, d4)
  mu5 <-  sapply(pors, d5)
  mu6 <-  sapply(pors, d6)
  mu7 <-  sapply(pors, d7)
  mu8 <-  sapply(pors, d8)
  mu9 <-  sapply(pors, d9)
  mu10 <- sapply(pors, d10)
  mu11 <- sapply(pors, d11)
  mu12 <- sapply(pors, d12)
  mu13 <- sapply(pors, d13)
  mu14 <- sapply(pors, d14)
  mu15 <- sapply(pors, d15)
  mu16 <- sapply(pors, d16)
  
  # Create the row for the profile
  info <- tibble(n = n,
                 m = m,
                 id = 1:length(pors),
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

  # Append to the table
  indexes <- indexes %>% bind_rows(info)
}

# Add the execution times
indexes_join <- indexes %>%
  mutate(n = as.character(n),
         m = as.character(m),
         id = as.character(id))
predict_times <- execution_times %>%
  mutate(n = as.character(n),
         m = as.character(m),
         id = as.character(id)) %>%
  left_join(indexes_join, 
            by = c("n"="n", "m"="m", "id"="id")) %>%
  mutate(n = as.factor(n),
         m = as.factor(m),
         id = as.factor(id)) %>% 
  rename(time = "exec_time") 

################################################################################
####### CHECK ##################################################################
################################################################################

resumen <- predict_times %>% 
  mutate(n = as.numeric(as.character(n)),
         m = as.numeric(as.character(m))) %>%
  group_by(n, m) %>%
  summarise(min_mu1 = min(mu1),
            max_mu1 = max(mu1),
            min_mu2 = min(mu2),
            max_mu2 = max(mu2),
            min_mu3 = min(mu3),
            max_mu3 = max(mu3),
            min_mu4 = min(mu4),
            max_mu4 = max(mu4),
            min_mu5 = min(mu5),
            max_mu5 = max(mu5),
            min_mu6 = min(mu6),
            max_mu6 = max(mu6),
            min_mu7 = min(mu7),
            max_mu7 = max(mu7),
            min_mu8 = min(mu8),
            max_mu8 = max(mu8),
            min_mu9 = min(mu9),
            max_mu9 = max(mu9),
            min_mu10 = min(mu10),
            max_mu10 = max(mu10),
            min_mu11 = min(mu11),
            max_mu11 = max(mu11),
            min_mu12 = min(mu12),
            max_mu12 = max(mu12),
            min_mu13 = min(mu13),
            max_mu13 = max(mu13),
            min_mu14 = min(mu14),
            max_mu14 = max(mu14),
            min_mu15 = min(mu15),
            max_mu15 = max(mu15),
            min_mu16 = min(mu16),
            max_mu16 = max(mu16),
            .groups = "keep") %>% ungroup()

# mu1 must be in []
resumen

# mu2 must be in [0,n-1] (maximum range of positions)
resumen %>% pull(min_mu2)
resumen %>% pull(max_mu2) %>% table()

# mu3 must be in [0,n-1] (minimum range of positions)
resumen %>% pull(min_mu3)
resumen %>% pull(max_mu3) 

# mu4 must be in [0,n-1] (average range of positions)
resumen %>% mutate(check = min_mu4 < n) %>% group_by(check) %>% count()
resumen %>% mutate(check = max_mu4 < n) %>% group_by(check) %>% count()

# mu5 must be in the range [0,m*tau_n] if m even and [tau_n,m*tau_n] if odd
resumen %>% select(n, m, min_mu5)
resumen %>% filter(m%%2==0) %>% mutate(check = min_mu5 > 0) %>% group_by(check) %>% count()
resumen %>% filter(m%%2!=0) %>% mutate(check = min_mu5 > tr(n)) %>% group_by(check) %>% count()
resumen %>% mutate(check = max_mu5 < (tr(n)*m)) %>% group_by(check) %>% count()
resumen %>% mutate(upper_bound = (tr(n)*m),
                   check = max_mu5 < upper_bound) %>%
  select(n, m, max_mu5, upper_bound)
# experimental results shows that the maximum never exceed the upper_bound/2, check:
resumen %>% mutate(upper_bound = (tr(n)*m),
                   check = max_mu5 < (upper_bound/2)) %>% group_by(check) %>% count()

# mu6 number of dirty triples [0, n!/(3!(n-3)!)]
resumen %>% pull(min_mu6)
print(resumen %>% mutate(upper_bound = factorial(n)/(6*factorial(n-3)),
                   check = max_mu6 < upper_bound) %>%
  select(n, m, max_mu6, upper_bound), n = 100)
# very under the upper bound

# mu7 mode margin for odd [1, m] and even [0,m]
resumen %>% filter(m%%2==0) %>% pull(min_mu7)
resumen %>% filter(m%%2!=0) %>% pull(min_mu7)
resumen %>% mutate(check = max_mu7 <= m) %>% group_by(check) %>% count()
print(resumen %>% select(n, m, max_mu7), n = 100)

# mu8 number of unique margins [1,tau_n]
resumen %>% pull(min_mu8)
resumen %>% pull(max_mu8)
resumen %>% mutate(check = max_mu8 <= tr(n)) %>% group_by(check) %>% count()
print(resumen %>% 
        mutate(check = max_mu8 <= tr(n),
               upper_bound = tr(n)) %>%
        select(n, m, max_mu8, upper_bound), n = 100)

# mu9 frequency of the minimum margin [0,tau_n]
resumen %>% pull(min_mu9)
resumen %>% pull(max_mu9)
resumen %>% mutate(check = max_mu9 <= tr(n)) %>% group_by(check) %>% count()
print(resumen %>% 
        mutate(check = max_mu9 <= tr(n),
               upper_bound = tr(n)) %>%
        select(n, m, max_mu9, upper_bound), n = 100)

# mu10 distance to borda ranking [0,tau_n*m]
resumen %>% pull(min_mu10)
resumen %>% pull(max_mu10)
resumen %>% mutate(check = max_mu10 <= (tr(n)*m)) %>% group_by(check) %>% count()
print(resumen %>% 
        mutate(upper_bound = tr(n)*m,
               check = max_mu10 <= upper_bound,
               prop = max_mu10/upper_bound) %>%
        select(n, m, max_mu10, upper_bound, prop), n = 100) # all of them < 50%

# mu11 number of overall preferred alternatives [1,n]
resumen %>% pull(min_mu11)
resumen %>% pull(max_mu11)

# mu12 sd dev of rowsum [0,tau_n*m]
resumen %>% pull(min_mu12)
resumen %>% pull(max_mu12)
resumen %>% mutate(check = max_mu12 <= (tr(n)*m)) %>% group_by(check) %>% count()
print(resumen %>% 
        mutate(upper_bound = tr(n)*m,
               check = max_mu12 <= upper_bound,
               prop = max_mu12/upper_bound) %>%
        select(n, m, max_mu12, upper_bound, prop), n = 100) # all of them < 1%

# mu13 sd dev of beta [0,tau_n]
resumen %>% pull(min_mu13)
resumen %>% pull(max_mu13)
resumen %>% mutate(check = max_mu13 <= tr(n)) %>% group_by(check) %>% count()
print(resumen %>% 
        mutate(upper_bound = tr(n),
               check = max_mu13 <= upper_bound,
               prop = max_mu13/upper_bound) %>%
        select(n, m, max_mu13, upper_bound, prop), n = 100) # all of them < 1%

# mu14 mean of beta [0,n-1)
resumen %>% pull(min_mu14)
resumen %>% pull(max_mu14)

# mu15 mean of beta [0,n-1)
resumen %>% pull(min_mu15)
resumen %>% pull(max_mu15)

# mu16 mean of beta [0,n-1)
resumen %>% pull(min_mu16)
resumen %>% pull(max_mu16)


