ggcorr(predict_times %>% filter(method == "ME", n == 8),  label = TRUE)

ggplot(predict_times %>% filter(method == "ME", n == 8), aes(mu5, mu11)) + 
  geom_point() +
  facet_grid(n~m, scales = "free")

predict_times <- predict_times %>% 
  mutate(m = as.numeric(as.character(m)),
         odd = as.factor(m%%2==0),
         m = factor(m, levels = c(10,11,50,51,100,101,250,251,500,501,1000,1001,2000,2001)))

# time against all others
predict_times %>% filter(method == "ME", n == 8) %>%
  select(-method, -n) %>%
  gather(-time, key = "var", value = "value") %>%
  ggplot(aes(x = value, y = time)) +
  geom_point() +
  facet_wrap(~ var, scales = "free") +
  theme_bw()

ggplot(predict_times, aes(time, mu1)) + 
  geom_point() +
  facet_grid(n~m)

ggplot(predict_times, aes(time, mu5)) + 
  geom_point() +
  facet_grid(n~m, scales = "free")

ggplot(predict_times, aes(time, mu16)) + 
  geom_point() +
  facet_grid(n~m)

# Distribution of frequency of the minimum margin
ggplot(predict_times %>% 
         filter(n==13) %>% 
         mutate(basenum = ifelse(as.numeric(as.character(m))%%2==0, 
                                 as.numeric(as.character(m)), 
                                 as.numeric(as.character(m))-1)), 
       aes(mu9, alpha = odd)) + 
  geom_density(fill ="#1D7BC3") +
  facet_wrap(m~., nrow = 2, dir = "v") +
  scale_alpha_manual(values = c(1,.5)) +
  guides(alpha = FALSE) +
  xlab("Frequency of the minimum margin") +
  ylab("Density") +
  theme_paper


# Distribution of frequency of the minimum margin
ggplot(predict_times %>% 
         filter(n==13) %>% 
         mutate(basenum = ifelse(as.numeric(as.character(m))%%2==0, 
                                 as.numeric(as.character(m)), 
                                 as.numeric(as.character(m))-1)), 
       aes(mu1, time)) + 
  geom_point(color ="#1D7BC3", alpha = .2) +
  facet_wrap(m~., nrow = 2, dir = "v") +
  scale_alpha_manual(values = c(1,.5)) +
  guides(alpha = FALSE) +
  xlab("Average Kendall distance between the rankings of the profile") +
  ylab("Density") +
  theme_paper

