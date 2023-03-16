col_names_reps <- c("n", "m", "id", "method", "exec_time", "nsol", "ntent", "t1", "t2", "t3")

quantiles <- enframe(quantile(res_me_8$exec_time), name = "perc") %>% mutate(n = 8, method = "me") %>%
  bind_rows(enframe(quantile(res_meprcw_8$exec_time), name = "perc") %>% mutate(n = 8, method = "meprcw")) %>%
  bind_rows(enframe(quantile(res_me_9$exec_time), name = "perc") %>% mutate(n = 9, method = "me")) %>%
  bind_rows(enframe(quantile(res_meprcw_9$exec_time), name = "perc") %>% mutate(n = 9, method = "meprcw")) %>%
  bind_rows(enframe(quantile(res_me_10$exec_time), name = "perc") %>% mutate(n = 10, method = "me")) %>%
  bind_rows(enframe(quantile(res_meprcw_10$exec_time), name = "perc") %>% mutate(n = 10, method = "meprcw")) %>%
  mutate(perc = as.factor(perc),
         n = as.factor(n), 
         method = as.factor(method))


ggplot(quantiles, aes(value, method, color = method)) +
  geom_point() +
  geom_line() +
  facet_grid(n~.)

res_meprcw_8 
