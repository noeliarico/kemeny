results_to_plot <- resultsNC10
u8res <- rep(unlist(check_data_experiments_u8(pors10nc)), each = 3)
results_to_plot <- results_to_plot %>% mutate(u8 = u8res)
p <- ggplot(results_to_plot %>% filter(method == 1), aes(u8, time, color = omega)) +
  geom_point(aes(size = agreement), alpha = 0.7) +
  theme_bw()

results_to_plot <- resultsNC11
u8res <- rep(unlist(check_data_experiments_u8(pors11nc)), each = 3)
results_to_plot <- results_to_plot %>% mutate(u8 = u8res)
ggplot(results_to_plot %>% filter(method == 1), aes(u8, time, color = omega)) +
  geom_point(aes(size = agreement), alpha = 0.7) +
  theme_bw()


results_to_plot <- resultsCW10
u8res <- rep(unlist(check_data_experiments_u8(pors10cw)), each = 3)
results_to_plot <- results_to_plot %>% mutate(u8 = u8res)
ggplot(results_to_plot %>% filter(method == 1), aes(u8, time, color = omega)) +
  geom_point(aes(size = agreement), alpha = 0.7) +
  theme_bw()

results_to_plot <- resultsCW11
u8res <- rep(unlist(check_data_experiments_u8(pors11cw)), each = 3)
results_to_plot <- results_to_plot %>% mutate(u8 = u8res)
ggplot(results_to_plot %>% filter(method == 1), aes(u8, time, color = omega)) +
  geom_point(aes(size = agreement), alpha = 0.7) +
  theme_bw()
