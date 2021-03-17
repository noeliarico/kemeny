# Load data ---------------------------------------------------------------

library(readr)
cn <- c("id",
        "n",
        "omega",
        "index",
        "method",
        "time",
        "nsolutions",
        "ntentative",
        "t1",
        "t2",
        "t3")

# n8
agreements <- unlist(check_data_experiments_margin(pors8cw))
nrp <- unlist(check_data_experiments_nrp(pors8cw))
resultsCW8 <- read_csv("resultsNC8cw_123.csv", skip = 1,
                       col_names = cn) %>%
  mutate(
    id = index+(5*(omega-1)),
    agreement = rep(agreements, each = 3),
    method = as.factor(method),
    omega = as.factor(omega),
    nrp = as.factor(rep(nrp, each = 3))
    )

# n9
agreements <- unlist(check_data_experiments_margin(pors9nc))
nrp <- unlist(check_data_experiments_nrp(pors9nc))
resultsNC9 <- read_csv("resultsNC9nc_123.csv", skip = 1,
                       col_names = cn) %>%
  mutate(
    id = index+(5*(omega-1)),
    agreement = rep(agreements, each = 3),
    method = as.factor(method),
    omega = as.factor(omega),
    nrp = as.factor(rep(nrp, each = 3)))

# n10
agreements <- unlist(check_data_experiments_margin(pors10nc))
nrp <- unlist(check_data_experiments_nrp(pors10nc))
resultsNC10 <- read_csv("resultsNC10nc_123.csv", skip = 1,
                       col_names = cn) %>%
  mutate(
    id = index+(5*(omega-1)),
    agreement = rep(agreements, each = 3),
    method = as.factor(method),
    omega = as.factor(omega),
    nrp = as.factor(rep(nrp, each = 3)))

cn <- c("id",
        "n",
        "omega",
        "index",
        "method",
        "time",
        "nsolutions",
        "ntentative",
        "t1")

# n11
agreements <- unlist(check_data_experiments_margin(pors11nc))
nrp <- unlist(check_data_experiments_nrp(pors11nc))
resultsNC11 <- read_csv("resultsNC11nc_123.csv", skip = 1,
                        col_names = cn) %>%
  mutate(
    id = index+(5*(omega-1)),
    agreement = rep(agreements, each = 3),
    method = as.factor(method),
    omega = as.factor(omega),
    nrp = as.factor(rep(nrp, each = 3)))

# n12

cn <- c("n",
        "omega",
        "index",
        "method",
        "time",
        "nsolutions",
        "ntentative")

agreements <- unlist(check_data_experiments_margin(pors12nc))
nrp <- unlist(check_data_experiments_nrp(pors12nc))
resultsNC12 <- read_delim("resultsNC12nc_123.csv",
                        col_names = cn, delim = " ") %>%
  mutate(
    id = rep(1:55, each = 3),
    agreement = rep(agreements, each = 3),
    method = as.factor(method),
    omega = as.factor(omega),
    #nrp = as.factor(rep(nrp, each = 3))
    )

resultsNC <- bind_rows(
  resultsNC8,
  resultsNC9,
  resultsNC10,
  resultsNC11,
  resultsNC12
) 

# General view of the results by n ---------------------------------------------

ggplot(resultsNC %>% filter(as.numeric(omega) < 8), aes(agreement, time)) +
  geom_line(aes(color = omega, group = id)) +
  geom_point(size = 2, aes(color = omega, shape = method), stroke = .5) +
  facet_wrap(~n) +
  facet_wrap(~n, scales = "free") +
  scale_shape_manual(values = c(22,21,18))

ggplot(resultsNC, aes(agreement, time, color = omega)) +
  geom_line(aes(group = id)) +
  geom_point(aes(shape = method)) +
  facet_wrap(~n, scales = "free_y") +
  #scale_shape_manual(values = c(22,21,18)) +
  theme_light() +
  theme(text = element_text(family="Times New Roman", size = 14)) +
  xlab("") + ylab("") 



resultsNCt <- resultsNC %>%
  select(id,n,omega,index,method,time,ntentative) %>%
  group_by(id) %>%
  mutate(ntentative = max(ntentative)) %>% 
  ungroup()

ggplot(resultsNCt %>% filter(as.numeric(omega)< 7), aes(ntentative, time, color = omega)) +
  geom_line(aes(group = id)) +
  geom_point(aes(shape = method)) +
  scale_x_continuous(trans = 'log2') + 
  facet_wrap(~n, scales = "free") +
  #scale_shape_manual(values = c(22,21,18)) +
  theme_light() +
  theme(text = element_text(family="Times New Roman", size = 14)) +
  
  xlab("") + ylab("")

# Average results by method, n and omega ---------------------------------------

results_avg <- resultsNC %>% 
  group_by(n, method, omega) %>%
  summarise(meantime = median(time), 
            agreement = median(agreement),
            nsolutions = mean(nsolutions),
            # ntentative = mean(ntentative), ests no porque cambian dependiendo dle método
            .groups = "drop") %>%
  pivot_wider(names_from = method, values_from = meantime, names_prefix = "alg") %>%
  mutate(perc = alg3/alg1,
         nsolutions = nsolutions/factorial(n))
        # ntentative = ntentative/factorial(n))


ggplot(results_avg %>% filter(n<12), aes(omega)) +
  geom_bar(aes(weight = perc), 
           position = "dodge", 
           fill = "#fabada",
           color = "gray",
           alpha = 0.5) +
  facet_wrap(~n) +
  geom_point(aes(y = agreement)) +
  geom_line(aes(y = agreement, group = n)) +
  ylab("relative execution time and agreement")

# Percentage of reduction: average results by method and n ---------------------

results_avg <- resultsNC %>% 
  group_by(n, method, omega) %>%
  summarise(meantime = mean(time), .groups = "drop") %>%
  group_by(n, method) %>%
  summarise(meantime = mean(meantime), .groups = "drop") %>%
  pivot_wider(names_from = method, values_from = meantime, names_prefix = "alg") %>%
  mutate(perc2 = alg2/alg1,
         perc3 = alg3/alg1,
         perc_full = 1) %>%
  pivot_longer(-c(n, starts_with("alg")), names_to = "method", values_to = "perc") %>%
  mutate(method = recode(method, perc3 = "ME-RCW", perc2 = "ME-CW", perc_full = "ME")) %>%
  mutate(time = ifelse(method == "ME-CW", alg2, ifelse(method == "ME-RCW", alg3, alg1))) %>%
  select(!starts_with("alg"))

ggplot(results_avg %>% filter(method!="ME-CW"), aes(n)) +
  geom_bar(aes(weight = perc, fill = method), 
           position = "identity",
           alpha = rep(c(.5,1), each=5), color = "black") +
  geom_text(aes(x=n,y=perc,label=paste(round(time, 3), "s")), 
            vjust = 1.5, size = 3.5, family = "Times New Roman",
            colour = c(rep(c("white","black"),5))) +
  scale_fill_manual(values=c("#d0e8f2","#5B6569")) +
  theme_light() +
  theme(text = element_text(family="Times New Roman", size = 12),
        legend.position = "right") +
  xlab("") + ylab("") +  labs(fill="Algorithm") +
  scale_y_continuous(breaks = seq(0,1,.25), labels =paste0(seq(0,100,25), "%"), limits = c(0,1))

# Exponential time: average results by method and n ----------------------------

results_avg <- resultsNC %>% 
  group_by(n, method, omega) %>%
  summarise(meantime = mean(time), .groups = "drop") %>%
  group_by(n, method) %>%
  summarise(meantime = mean(meantime), .groups = "drop") %>%
  mutate(#method = recode(method, `1` = "ME", `2` = "ME-CW", `3` = "ME-RCW"),
         method = fct_relevel(method, rev))

ggplot(results_avg, aes(n)) +
  geom_bar(aes(weight = meantime, fill = method), 
           position = "dodge",
           alpha = 0.5, color = "black") +
  scale_fill_manual(values=c("#d0e8f2","#79a3b1", "#456268")) +
  theme_light() +
  theme(text = element_text(family="Times New Roman", size = 14)) +
  xlab("") + ylab("") +
  coord_flip() +
  # geom_hline(yintercept = 1, linetype = "dashed", alpha = 0.3) +
  guides(fill = guide_legend(reverse=TRUE))


# Exponential time: average results by method, omega and n ---------------------

results_avg <- resultsNC %>% 
  group_by(n, method, omega) %>%
  summarise(meantime = mean(time), .groups = "drop") %>%
  mutate(#method = recode(method, `1` = "ME", `2` = "ME-CW", `3` = "ME-RCW"),
    method = fct_relevel(method, rev))

# filter(as.numeric(omega) < 10
ggplot(results_avg, aes(omega)) +
  geom_bar(aes(weight = meantime, fill = method), 
           position = "dodge",
           alpha = 0.5, color = "black") +
  scale_fill_manual(values=c("#d0e8f2","#79a3b1", "#456268")) +
  facet_wrap(~n, scales = "free") +
  theme_light() +
  theme(text = element_text(family="Times New Roman", size = 14)) +
  xlab("") + ylab("") +
  coord_flip() +
  # geom_hline(yintercept = 1, linetype = "dashed", alpha = 0.3) +
  guides(fill = guide_legend(reverse=TRUE))


# Plots by n 

ggplot(resultsNC8, aes(agreement, time, color = nrp)) +
  geom_line(aes(group = id)) +
  geom_point(aes(shape = method)) +
  facet_wrap(~omega, scales = "free_y")

ggplot(resultsNC9, aes(agreement, time, color = nrp)) +
  geom_line(aes(group = id)) +
  geom_point(aes(shape = method)) +
  facet_wrap(~omega, scales = "free_y")

ggplot(resultsNC10, aes(agreement, time, color = nrp)) +
  geom_line(aes(group = id)) +
  geom_point(aes(shape = method)) +
  facet_wrap(~omega, scales = "free_y")


# Compare results with the ones in the paper ------------------------------
  
compare_results <- tribble(~method, ~n, ~min, ~mean, ~max,
                          "am", 8, 27, 331, 1475,
                          "am", 9, 242, 1496, 8310,
                          "am", 10, 1166, 7409, 30029,
                          "am", 11, 4386, 40877, 252563,
                          "am", 12, 33983, 246090, 1710682)

m1 <- resultsNC %>% 
  filter(method == 1) %>%
  select(n, ntentative) %>%
  group_by(n) %>%
  summarise(method = "m1",
            min = min(ntentative),
            mean = mean(ntentative),
            max = max(ntentative))

m3 <- resultsNC %>% 
  filter(method == 3) %>%
  select(n, ntentative) %>%
  group_by(n) %>%
  summarise(method = "m3",
            min = min(ntentative),
            mean = mean(ntentative),
            max = max(ntentative))

plcompare_results <- bind_rows(
  compare_results,
  m1,
  m3
) %>%
  pivot_longer(-c(method, n), names_to = "metric")

# usar filtros
ggplot(compare_results %>% filter(n==8), aes(n, value, fill = method)) +
  geom_bar(stat= "identity", position = "dodge", alpha = 0.7, color = "black") +
  facet_wrap(~metric) + #, scales = "free_y") +
  theme_light()


ggplot(resultsNC10, aes(agreement, time, shape = method, color = nrp)) +
  geom_line(aes(group = id)) +
  geom_point() +
  facet_wrap(~omega)#, scales = "free_y")

