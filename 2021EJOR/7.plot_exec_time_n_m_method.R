#colors <- c("#E7F046", "#2018BA", "#F2358A")
colors <- c("#EE4266", "#FFD23F", "#3BCEAC", "#1D7BC3")

theme_paper <- 
  theme_bw() +
  theme(text=element_text(size=10,  family="Times New Roman"),
        strip.background =element_rect(fill="white")) 

results_ejor_complete <- results_ejor
results_ejor <- results_ejor %>% filter(method %in% c("ME", "ME-RCW", "ME-BB", "ME-BBRCW"))

# General global means by n and method -----------------------------------------

p1 <- ggplot(results_ejor %>%
         group_by(n, method) %>%
         summarise(mean_time = mean(exec_time)),
       aes(n, mean_time, fill = method)) +
  geom_bar(stat = "identity", position = "dodge") +
  geom_text(aes(label = paste0(round(mean_time, 3), "s")), position = position_dodge(width = 1),
            vjust = -0.5, size = 3) +
  scale_fill_manual(values = colors) +
  labs(fill = "Algorithm",
       x = "Number of alternatives",
       y = "Average execution time in seconds") +
  theme_paper +
  theme(legend.position = "bottom") 
  

# Percentages of time reduction divided by n -----------------------------------

percentages <- results_ejor %>% 
  group_by(method, n) %>%
  summarise(average = mean(exec_time)) %>%
  ungroup() %>%
  group_by(n) %>%
  mutate(max = max(average)) %>%
  ungroup() %>%
  mutate(percentage = average/max,
         max = NULL)

p2 <- ggplot(percentages, aes(n, percentage, fill = method)) +
  geom_bar(stat = "identity", position = "identity") +
  geom_text(aes(label = paste0(str_pad(round(average, 3), 5, pad = "0", side = "right"), "s (", round(percentage*100, 2), "%)")), nudge_y = -.03,
            size = 3) +
  scale_y_continuous(labels = scales::percent) +
  labs(fill = "Algorithm",
        x = "Number of alternatives",
        y = "Percentage of time required") +
  scale_fill_manual(values = colors) +
  theme_paper +
  theme(legend.position = "bottom") 


### Exportar ### "time_improvement" a 11.94 x 4.98
p1 + p2 + plot_layout(guides = "collect", widths = c(2, 1)) & theme(legend.position = "bottom")


# Percentages of time reduction divided by n and m -----------------------------

percentages <- results_ejor %>% 
  group_by(method, n, m) %>%
  summarise(average = mean(exec_time)) %>%
  ungroup() %>%
  group_by(n, m) %>%
  mutate(max = max(average)) %>%
  ungroup() %>%
  mutate(percentage = average/max,
         max = NULL)

# total reduction in percentage
ggplot(percentages, aes(m, percentage, fill = method)) +
  geom_bar(stat = "identity", position = "identity", #color = "black",
           aes(alpha = as.factor(as.numeric(as.character(m))%%2))) +
 # geom_text(aes(label = paste0(round(average, 4), "s (", round(percentage*100, 2), "%)")), nudge_y = -.03) +
  facet_grid(~n) +
  geom_hline(yintercept = 0.1, linetype = "dashed") +
  scale_y_continuous(labels = scales::percent) +
  labs(fill = "Algorithm",
       x = "Number of alternatives",
       y = "Percentage of the execution time") +
  scale_fill_manual(values = colors) +
  scale_alpha_manual(values = c(0.5,0.9)) +
  guides(alpha = FALSE) +
  theme_paper +
  theme(legend.position = "bottom",
        panel.grid.major.x = element_blank(),
        panel.grid.minor.x = element_blank()) 


# Mean by method and n and m ---------------------------------------------------

ggplot (results_ejor %>%
  group_by(n, m, method) %>%
  summarise(mean_time = mean(exec_time)),
  aes(m, mean_time, fill = method)) +
  geom_bar(stat = "identity", position = "dodge", 
           aes(alpha = as.factor(as.numeric(as.character(m))%%2))) +
  facet_wrap(~n, scales = "free_y") +
  scale_alpha_manual(values = c(0.6,1)) +
  geom_hline(data = results_ejor %>%
               group_by(n, method) %>%
               summarise(mean_time = mean(exec_time)), 
             aes(yintercept = mean_time, color = method),
             alpha = 0.9, linetype = "dashed") +
  guides(alpha = FALSE, color = FALSE) +
  labs(fill = "Algorithm",
       x = "Number of voters",
       y = "Mean execution time") +
  scale_fill_manual(values = colors) +
  scale_color_manual(values = colors) +
  theme_paper +
  theme(axis.text.x = element_text(angle = 90),
        legend.position = "bottom") 


# initialization
ggplot (results_ejor_complete %>%
            filter(method %in% c("ME-BB", "ME-BBd", "ME-BBRCW", "ME-BBRCWd")) %>%
            group_by(n, m, method) %>%
            summarise(mean_time = mean(exec_time)),
          aes(m, mean_time, fill = method, color = method)) +
  geom_bar(stat = "identity", position = "dodge", 
           aes(alpha = as.factor(as.numeric(as.character(m))%%2)),
           size = .1) +
  facet_wrap(~n, scales = "free_y") +
  scale_alpha_manual(values = c(0.6,1)) +
  scale_fill_manual(values = c("#3BCEAC", "white", "#1D7BC3", "white")) +
  scale_color_manual(values = c("white", "#3BCEAC", "white", "#1D7BC3")) +
  guides(alpha = FALSE) +
  labs(fill = "Algorithm",
       color = "Algorithm",
       x = "Number of voters",
       y = "Mean execution time") +
  theme_paper +
  theme(axis.text.x = element_text(angle = 90),
        legend.position = "bottom") 


# meprcw
ggplot(res_me, aes(m, exec_time)) +
  geom_jitter(height = 0, width = .2) +
  facet_wrap(.~n, scales = "free")

ggplot(res_mercw, aes(m, exec_time)) +
  geom_jitter(height = 0, width = .2) +
  facet_wrap(.~n, scales = "free")

ggplot(res_mercw, aes(m, exec_time)) +
  geom_jitter(height = 0, width = .2) +
  facet_wrap(.~n, scales = "free")

# No se ve tendencia cuando aumenta el num de votantes
ggplot(res_meprcw, aes(m, exec_time)) +
  geom_jitter(height = 0, width = .2) +
  facet_wrap(.~n, scales = "free")


# Large n average

# Exponential MEAN execution time in seconds by n
palg_mean <- ggplot(res_large_n %>% filter(as.numeric(as.character(n))<14) %>%
         group_by(n) %>%
         summarise(mean_time = mean(exec_time)),
       aes(n, mean_time)) +
  geom_bar(stat = "identity", position = "dodge", fill = "#1D7BC3") +
  geom_text(aes(label = paste0(round(mean_time, 3), "s")), position = position_dodge(width = 1),
            vjust = -0.5, size = 3) +
  scale_fill_manual(values = colors) +
  labs(fill = "Algorithm",
       x = "Number of alternatives",
       y = "Mean execution time in seconds") +
  theme_paper +
  theme(legend.position = "bottom")


# Exponential MEDIAN execution time in seconds by n
palg_median <- ggplot(res_large_n %>% filter(as.numeric(as.character(n))<14) %>%
         group_by(n) %>%
         summarise(median_time = median(exec_time)),
       aes(n, median_time)) +
  geom_bar(stat = "identity", position = "dodge", fill = "#1D7BC3") +
  geom_text(aes(label = paste0(round(median_time, 3), "s")), position = position_dodge(width = 1),
            vjust = -0.5, size = 3) +
  scale_fill_manual(values = colors) +
  labs(fill = "Algorithm",
       x = "Number of alternatives",
       y = "Median execution time in seconds") +
  theme_paper +
  theme(legend.position = "bottom")

palg_mean + palg_median

# Solo media dirección opuesta
ggplot(res_large_n %>% filter(as.numeric(as.character(n))<14) %>%
         group_by(n) %>%
         summarise(mean_time = mean(exec_time)),
       aes(n, mean_time)) +
  geom_bar(stat = "identity", position = "dodge", fill = "#1D7BC3") +
  geom_text(aes(label = paste0(round(mean_time, 3), "s")), position = position_dodge(width = 1),
            hjust = -.2, size = 3) +
  scale_fill_manual(values = colors) +
  labs(fill = "Algorithm",
       x = "Number of alternatives",
       y = "Mean execution time in seconds") +
  theme_paper +
  theme(legend.position = "bottom") +
  scale_y_continuous(breaks = 1:10, limits = c(0,12))  +
  coord_flip() 

# MEAN execution time by n and m
ggplot (res_large_n %>% filter(as.numeric(as.character(n))<14) %>%
          group_by(n, m) %>%
          summarise(mean_time = mean(exec_time)),
        aes(m, mean_time)) +
  geom_bar(stat = "identity", position = "dodge", fill ="#1D7BC3", 
           aes(alpha = as.factor(as.numeric(as.character(m))%%2)), width=.8) +
  geom_hline(data = res_large_n %>% filter(as.numeric(as.character(n))<14) %>%
               group_by(n) %>%
               summarise(mean_time = mean(exec_time)),
             aes(yintercept = mean_time)) +
  geom_text(aes(label = round(mean_time,4), y=mean_time), 
            size = 3, color = "black", angle = 90, position = position_stack(vjust = 0.6)) +
  facet_wrap(~n, scales = "free_y", ncol = 3) +
  scale_alpha_manual(values = c(0.3,0.6)) +
  guides(alpha = FALSE, color = FALSE) +
  labs(fill = "Algorithm",
       x = "Number of voters",
       y = "Mean execution time in seconds") +
  scale_fill_manual(values = colors) +
  scale_color_manual(values = colors) +
  theme_paper +
  theme(axis.text.x = element_text(angle = 90),
        panel.grid.major.x = element_blank(), 
        legend.position = "bottom")


# MEDIAN execution time by n and m
ggplot (res_large_n %>% filter(as.numeric(as.character(n))<14) %>%
          group_by(n, m) %>%
          summarise(median_time = median(exec_time)),
        aes(m, median_time)) +
  geom_bar(stat = "identity", position = "dodge", fill ="#1D7BC3", 
           aes(alpha = as.factor(as.numeric(as.character(m))%%2))) +
  geom_text(aes(label = paste0(round(median_time,4), "s"), y=median_time), 
            size = 3, color = "white", angle = 90, position = position_stack(vjust = 0.5)) +
  facet_wrap(~n, scales = "free_y", ncol = 3) +
  scale_alpha_manual(values = c(0.6,1)) +
  guides(alpha = FALSE, color = FALSE) +
  labs(fill = "Algorithm",
       x = "Number of voters",
       y = "Median execution time") +
  scale_fill_manual(values = colors) +
  scale_color_manual(values = colors) +
  theme_paper +
  theme(axis.text.x = element_text(angle = 90),
        legend.position = "bottom")


# Boxplots de los executions time divided by n and m
ggplot(res_large_n %>% filter(as.numeric(as.character(n))<14), 
       aes(m, exec_time)) +
  geom_boxplot(color ="#1D7BC3", aes(alpha = as.factor(as.numeric(as.character(m))%%2))) +
  facet_wrap(~n, scales = "free_y", ncol = 6) +
  scale_alpha_manual(values = c(1,.5)) +
  guides(alpha = FALSE, color = FALSE) +
  labs(fill = "Algorithm",
       x = "Number of voters",
       y = "Distribution of the execution times ME-BBRCW") +
  scale_fill_manual(values = colors) +
  scale_color_manual(values = colors) +
  theme_paper +
  theme(axis.text.x = element_text(angle = 90),
        legend.position = "bottom")



n14 <- ggplot(res_large_n %>% filter(n == 14), aes(exec_time, y = 0)) +
  geom_boxplot(color ="#1D7BC3") +
  guides(alpha = FALSE, color = FALSE) +
  labs(fill = "Algorithm",
       x = "Execution time in seconds of profiles of 14 alternatives and 11 voters",
       y = "") +
  scale_fill_manual(values = colors) +
  scale_color_manual(values = colors) +
  scale_x_continuous(breaks = c(seq(0,max(res_large_n %>% filter(n == 14) %>% pull(exec_time) %>% max()), by = 100),60,120)) +
  geom_vline(xintercept = 60, linetype = "dashed") +
  geom_vline(xintercept = 120, linetype = "dashed") +
  theme_paper +
  theme(#axis.text.x = element_text(angle = 90),
        axis.ticks.y = element_blank(),
        axis.text.y = element_blank(),
        panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank(),
        panel.grid.minor.x = element_blank(),
        legend.position = "bottom")


n15 <- ggplot(res_large_n %>% filter(n == 15), aes(exec_time, y = 0)) +
  geom_boxplot(color ="#1D7BC3") +
  guides(alpha = FALSE, color = FALSE) +
  labs(fill = "Algorithm",
       x = "Execution time in seconds of profiles of 15 alternatives and 11 voters",
       y = "") +
  scale_fill_manual(values = colors) +
  scale_color_manual(values = colors) +
  scale_x_continuous(breaks = c(seq(0,max(res_large_n %>% filter(n == 15) %>% pull(exec_time) %>% max()), by = 100),60,120,180)) +
  geom_vline(xintercept = 60, linetype = "dashed") +
  geom_vline(xintercept = 120, linetype = "dashed") +
  geom_vline(xintercept = 180, linetype = "dashed") +
  theme_paper +
  theme(#axis.text.x = element_text(angle = 90),
    axis.ticks.y = element_blank(),
    axis.text.y = element_blank(),
    panel.grid.major.y = element_blank(),
    panel.grid.minor.y = element_blank(),
    panel.grid.minor.x = element_blank(),
    legend.position = "bottom")


mus1 <- sapply(profiles_ejor$porsEJOR14_1000, d1)
