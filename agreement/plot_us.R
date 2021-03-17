results_to_plot <- resultsNC12
u8res <- rep(unlist(check_data_experiments_u(pors12nc, u8)), each = 3)
results_to_plot <- results_to_plot %>% mutate(u8 = u8res)
p <- ggplot(results_to_plot %>% filter(method == 1), aes(u8, time, color = omega)) +
  geom_point(aes(size = agreement), alpha = 0.7) +
  theme_bw()
p


results_to_plot <- resultsCW11
u8res <- rep(unlist(check_data_experiments_u(pors11cw, u11)), each = 3)
results_to_plot <- results_to_plot %>% mutate(u8 = u8res)
ggplot(results_to_plot %>% filter(method == 1), aes(u8, time, color = omega)) +
  geom_point(aes(size = agreement), alpha = 0.7) +
  theme_bw()


results_to_plot <- resultsNC12
u8res <- rep(unlist(check_data_experiments_u(pors12nc, u11)), each = 3)
results_to_plot <- results_to_plot %>% mutate(u8 = u8res)
ggplot(results_to_plot %>% filter(method == 1, as.numeric(omega) < 9), aes(u8, time, color = omega)) +
  geom_point(aes(size = agreement), alpha = 0.7) +
  theme_bw()

results_to_plot <- resultsCW11
u8res <- rep(unlist(check_data_experiments_u8(pors11cw)), each = 3)
results_to_plot <- results_to_plot %>% mutate(u8 = u8res)
ggplot(results_to_plot %>% filter(method == 1), aes(u8, time, color = omega)) +
  geom_point(aes(size = agreement), alpha = 0.7) +
  theme_bw()


ggplot(results_to_plot %>% filter(method == 1), aes(time, u8)) +
  geom_point() +
  facet_wrap(~omega, scales = "free")

