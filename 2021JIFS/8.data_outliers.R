quantiles <- enframe(quantile(res_me_8$exec_time), name = "perc") %>% mutate(n = 8) %>%
  bind_rows(enframe(quantile(res_me_9$exec_time), name = "perc") %>% mutate(n = 9)) %>%
  bind_rows(enframe(quantile(res_me_10$exec_time), name = "perc") %>% mutate(n = 10)) %>%
  mutate(perc = as.factor(perc),
         n = as.factor(n))

quartiles8 <- res_me_8 %>% pull(exec_time) %>% quantile()
quartiles9 <- res_me_9 %>% pull(exec_time) %>% quantile()
quartiles10 <- res_me_10 %>% pull(exec_time) %>% quantile()

boxplot.stats(res_me_8$exec_time)$stats[5]

outliers_8 <- res_me_8 %>% mutate(outlier = exec_time > boxplot.stats(res_me_8$exec_time)$stats[5])
outliers_9 <- res_me_9 %>% mutate(outlier = exec_time > boxplot.stats(res_me_9$exec_time)$stats[5])
outliers_10 <- res_me_10 %>% mutate(outlier = exec_time > boxplot.stats(res_me_10$exec_time)$stats[5])

outliers <- bind_rows(outliers_8, outliers_9, outliers_10) %>% 
  mutate(n = as.factor(n),
         m = as.factor(m),
         outlier = factor(outlier, labels = c("no", "yes")),
         method = NULL,
         outlier = fct_relevel(outlier, "no", after = Inf)
  ) 

outliers %>% filter(outlier == "yes") %>% group_by(n) %>% count() %>% mutate(perc = nn/2800)
