data_sim <- tibble(n = 8, 
               m = c(10, 25, 50, 100, 250, 500, 1000),
               time = sample(1:10,7))
ggplot(data_sim, aes(m, time)) +
  geom_point() +
  scale_x_log10()




ggplot(results10 %>%
         group_by(method) %>%
         summarise(mean_time = mean(exec_time)),
       aes(method, mean_time, fill = method)) +
  geom_bar(stat = "identity", position = "dodge", color = "black") +
  geom_text(aes(label = paste0(round(mean_time, 4), "s")), position = position_dodge(width = 1),
            vjust = -0.5, size = 3) +
  # scale_fill_manual(values = colors) +
  labs(fill = "Algorithm",
       x = "Algorithm",
       y = "Average execution time in seconds") +
  theme_paper +
  theme(legend.position = "bottom") 

ggplot(results10 %>%
         group_by(m, method) %>%
         summarise(mean_time = mean(exec_time)) %>%
         mutate(m=as.factor(m)),
       aes(m, mean_time, fill = method)) +
  geom_bar(stat = "identity", position = "dodge", color = "black") +
  # geom_text(aes(label = paste0(round(mean_time, 4), "s")), position = position_dodge(width = 1),
  #  vjust = -0.5, size = 3) +
  # scale_fill_manual(values = colors) +
  labs(fill = "Algorithm",
       x = "Algorithm",
       y = "Average execution time in seconds") +
  theme_paper +
  theme(legend.position = "bottom") 