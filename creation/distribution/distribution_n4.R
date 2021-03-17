set.seed(123)
r4_norm10 <- create_profiles_distribution(4,10,max_iter=round(1000/10),"norm")
r4_norm35 <- create_profiles_distribution(4,35,max_iter=round(1000/35),"norm")
r4_norm60 <- create_profiles_distribution(4,60,max_iter=round(1000/60),"norm")
r4_norm85 <- create_profiles_distribution(4,85,max_iter=round(1000/85),"norm")

results_norm4 <- bind_rows(
  r4_norm10$details %>% mutate(m = 10),
  r4_norm35$details %>% mutate(m = 35),
  r4_norm60$details %>% mutate(m = 60),
  r4_norm85$details %>% mutate(m = 85),
) %>% mutate(distribution = "norm")

set.seed(123)
r4_unif10 <- create_profiles_distribution(4,10,max_iter=round(1000/10),"unif")
r4_unif35 <- create_profiles_distribution(4,35,max_iter=round(1000/35),"unif")
r4_unif60 <- create_profiles_distribution(4,60,max_iter=round(1000/60),"unif")
r4_unif85 <- create_profiles_distribution(4,85,max_iter=round(1000/85),"unif")

results_unif4 <- bind_rows(
  r4_unif10$details %>% mutate(m = 10), 
  r4_unif35$details %>% mutate(m = 35),
  r4_unif60$details %>% mutate(m = 60),
  r4_unif85$details %>% mutate(m = 85)
) %>% mutate(distribution = "unif")

results_n4 <- bind_rows(
  results_norm4,
  results_unif4
) %>% mutate(distribution = as.factor(distribution),
             type = as.factor(type),
             n = as.factor(as.numeric(n)),
             m = as.factor(as.numeric(m)),
             w = as.factor(as.numeric(w)),
             d = as.factor(as.numeric(d)))

results_n4_total <- results_n4 %>%
  group_by(n, w, d, m, type, distribution) %>%
  tally(name = "times")

# Comparación general. No cambia mucho la distribución
ggplot(results_n4_total %>% group_by(m, distribution, w, type) %>% count(), aes(w, n, fill = type)) +
  geom_bar(stat="identity", color = "black") +
  facet_grid(m~distribution, scales = "free_x") +
  theme_linedraw() +
  #scale_fill_manual(values = c("#383D3B","#EEE5E9","#7C7C7C", "white"))
  scale_fill_manual(values= blues)


ggplot(results_n4_total, aes(w, times, fill = distribution)) +
  geom_bar(stat="identity", color = "black", position = "dodge") +
  facet_grid(m~d, scales = "free_y") +
  theme_linedraw() +
  #scale_fill_manual(values = c("#383D3B","#EEE5E9","#7C7C7C", "white"))
  scale_fill_manual(values= blues)

ggplot(results_n4_total, aes(d, times, fill = type)) +
  geom_bar(stat="identity", color = "black") +
  facet_grid(m~distribution, scales = "free_y") +
  theme_linedraw() +
  scale_fill_manual(values = c("#383D3B","#EEE5E9","#7C7C7C", "white"))
  #scale_fill_manual(values= blues)
