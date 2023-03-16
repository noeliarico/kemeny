results_ds <- read.csv("~/Desktop/resultsLuigi.csv")
results_ds <- results_ds %>% pivot_longer(-c(nitems, nfocals), names_to = "method", values_to = "time")

print(results_ds %>% 
  filter(method == "cpu") %>% select(-method) %>%
  pivot_wider(names_from = nfocals, values_from = time, names_prefix = "nfocals=") %>%
  xtable(label = "tab:AlgIPy", 
         align = "r|c|rrrrr",
         digits = 4), include.rownames = FALSE)

print(results_ds %>% 
        filter(method == "jit") %>% select(-method) %>%
        pivot_wider(names_from = nfocals, values_from = time, names_prefix = "nfocals=") %>%
        xtable(label = "tab:AlgCPy", 
               align = "r|c|rrrrr",
               digits = 4), include.rownames = FALSE)

print(results_ds %>% 
        filter(method == "gpu") %>% select(-method) %>%
        pivot_wider(names_from = nfocals, values_from = time, names_prefix = "nfocals=") %>%
        xtable(label = "tab:AlgGPU", 
               align = "r|c|rrrrr",
               digits = 4), include.rownames = FALSE)
  
# baselines fixing the number of items

baselines <- results_ds %>% 
  filter(method == "cpu", nfocals == 2) %>% 
  select(-method) %>%
  mutate(baseline = time, 
         time = NULL, nfocals = NULL,)
print(results_ds %>% 
  filter(method == "cpu") %>% select(-method) %>%
  left_join(baselines) %>%
  mutate(speed_up = round(time/baseline, 2), 
         speed_up = paste0("x", speed_up), 
         time = NULL) %>%
  filter(nfocals != 2) %>%
  mutate(baseline = NULL) %>%
  pivot_wider(names_from = nfocals, values_from = speed_up) %>%
    xtable(label = "tab:AlgIPy", 
           align = "r|c|rrrr|",
           digits = 4), include.rownames = FALSE)



baselines <- results_ds %>% 
  filter(method == "jit", nfocals == 2) %>% 
  select(-method) %>%
  mutate(baseline = time, 
         time = NULL, nfocals = NULL,)
print(results_ds %>% 
        filter(method == "jit") %>% select(-method) %>%
        left_join(baselines) %>%
        mutate(speed_up = round(time/baseline, 2), 
               speed_up = paste0("x", speed_up), 
               time = NULL) %>%
        filter(nfocals != 2) %>%
        mutate(baseline = NULL) %>%
        pivot_wider(names_from = nfocals, values_from = speed_up) %>%
        xtable(label = "tab:AlgCPy", 
               align = "r|c|rrrr|",
               digits = 4), include.rownames = FALSE)



baselines <- results_ds %>% 
  filter(method == "gpu", nfocals == 2) %>% 
  select(-method) %>%
  mutate(baseline = time, 
         time = NULL, nfocals = NULL)
print(results_ds %>% 
        filter(method == "gpu") %>% select(-method) %>%
        left_join(baselines) %>%
        mutate(speed_up = round(time/baseline, 2), 
               speed_up = paste0("x", speed_up), 
               time = NULL) %>%
        filter(nfocals != 2) %>%
        mutate(baseline = NULL) %>%
        pivot_wider(names_from = nfocals, values_from = speed_up) %>%
        xtable(label = "tab:AlgGPU", 
               align = "r|c|rrrr|",
               digits = 4), include.rownames = FALSE)

# baselines fixing the number of focal elements

baselines <- results_ds %>% 
  filter(method == "cpu", nfocals == 2) %>% 
  select(-method) %>%
  mutate(baseline = time, 
         time = NULL, nfocals = NULL)
print(results_ds %>% 
        filter(method == "cpu") %>% select(-method) %>%
        left_join(baselines) %>%
        mutate(speed_up = round(time/baseline, 2), 
               speed_up = paste0("x", speed_up), 
               time = NULL) %>%
        filter(nfocals != 2) %>%
        mutate(baseline = NULL) %>%
        pivot_wider(names_from = nfocals, values_from = speed_up) %>%
        xtable(label = "tab:AlgIPy", 
               align = "r|c|rrrr|",
               digits = 4), include.rownames = FALSE)



#their_times <- 
print(tribble(~nfocals, ~nitems, ~time,
log2(4    ), 5 , 0.0005080699920654297,
log2(4    ), 10, 0.0013265609741210938,
log2(4    ), 15, 0.1571800708770752,
log2(4    ), 20, 2.141662120819092,
log2(16   ), 5 , 0.0007841587066650391,
log2(16   ), 10, 0.00966191291809082,
log2(16   ), 15, 0.43939924240112305,
log2(16   ), 20, 16.84366011619568,
log2(512  ), 10, 0.2107541561126709,
log2(512  ), 15, 8.116032838821411,
log2(512  ), 20, 325.07727122306824,
log2(16384), 15, 268.4908757209778) %>%
  pivot_wider(names_from = nfocals, values_from = time) %>%
  xtable(label = "tab:theirResults", 
         align = "r|c|llll",
         digits = 4), include.rownames = FALSE)



