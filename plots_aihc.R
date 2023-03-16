colors_fast <- c("#88CDF6", "#00254D")
colors_outliers <- c("#BDE724", "#003200")

# OMEGA -----------------------------
p1 <- ggplot(data_quartiles_normalized %>%
         mutate(is_q1 = ifelse(quartile == "q1", "fast", "slow")), aes(mu11, fill = is_q1)) +
  geom_density(alpha = 0.6) +
  facet_grid(.~n, labeller = labeller(n = n.labs), scales = "free_y") +
  theme_bw() +
  theme(text=element_text(size=14,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 14),
        panel.grid.minor.y = element_blank(),
        legend.position = "right",
        axis.text.x = element_text(angle = 90)
  ) +
  xlab(~ mu [11]) +
  ylab("") +
  scale_fill_manual(values = colors_fast) +
  labs(fill = "Execution time")
  #guides(fill = "none") 

p2 <- ggplot(data_outliers_normalized, aes(mu11, fill = outlier)) +
  geom_density(alpha = 0.6) +
  facet_grid(.~n, labeller = labeller(n = n.labs)) +
  theme_bw() +
  theme(text=element_text(size=14,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 14),
        panel.grid.minor.y = element_blank(),
        legend.position = "right",
        axis.text.x = element_text(angle = 90)
  ) +
  xlab(~ mu [11]) +
  ylab("") +
  scale_fill_manual(values = colors_outliers)   +
  labs(fill = "Outlier")
  #guides(fill = "none") 
p <- p1/p2
ggsave("mu_11_formatoNuevo.png", plot=p, height=12, width=23, units=c("cm"), dpi=1000)

# SD TETA ----------------------------
p1 <- ggplot(data_quartiles_normalized %>%
               mutate(is_q1 = ifelse(quartile == "q1", "fast", "slow")), 
             aes(mu12, fill = is_q1)) +
  #geom_density(alpha = 0.6) +
  geom_histogram() +
  facet_grid(.~n, labeller = labeller(n = n.labs)) +
  theme_bw() +
  theme(text=element_text(size=14,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 14),
        panel.grid.minor.y = element_blank(),
        legend.position = "right",
        axis.text.x = element_text(angle = 90)
  ) +
  xlab(~ mu [12]) +
  ylab("") +
  labs(fill = "Execution time") +
  scale_fill_manual(values = colors_fast) 

p2 <- ggplot(data_outliers_normalized, aes(mu12, fill = outlier)) +
  #geom_density(alpha = 0.6)+
  geom_histogram() +
  facet_grid(.~n, labeller = labeller(n = n.labs)) +
  theme_bw() +
  theme(text=element_text(size=14,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 14),
        panel.grid.minor.y = element_blank(),
        legend.position = "right",
        axis.text.x = element_text(angle = 90)
  ) +
  xlab(~ mu [12]) +
  ylab("") +
  labs(fill = "Outliers") +
  scale_fill_manual(values = colors_outliers)  
p <- p1/p2
p
ggsave("mu12.png", plot=p, height=12, width=23, units=c("cm"), dpi=1000)


# DIST BORDA ----------------------------
p1 <- ggplot(data_quartiles_normalized %>%
               mutate(is_q1 = ifelse(quartile == "q1", "fast", "slow")), 
             aes(mu10, fill = is_q1)) +
  geom_density(alpha = 0.6) +
  geom_histogram() +
  facet_grid(.~n, labeller = labeller(n = n.labs), scales = "free_y") +
  theme_bw() +
  theme(text=element_text(size=14,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 14),
        panel.grid.minor.y = element_blank(),
        legend.position = "right"
  ) +
  xlab(~ mu [10]) +
  ylab("") +
  labs(fill = "Execution time") +
  scale_fill_manual(values = colors_fast) 

p2 <- ggplot(data_outliers_normalized, aes(mu10, fill = outlier)) +
  #geom_density(alpha = 0.6) +
  geom_histogram() +
  facet_grid(.~n, labeller = labeller(n = n.labs)) +
  theme_bw() +
  theme(text=element_text(size=14,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 14),
        panel.grid.minor.y = element_blank(),
        legend.position = "right"
  ) +
  xlab(~ mu [10]) +
  ylab("") +
  labs(fill = "Outliers") +
  scale_fill_manual(values = colors_outliers)  
p <- p1/p2
(p|p3) + plot_layout(guides = "collect") + theme(legend.position = "none")
ggsave("mu10.png", plot=p, height=12, width=23, units=c("cm"), dpi=1000)


# MEAN BETA ----------------------------
p1 <- ggplot(data_quartiles_normalized %>%
               filter(odd == "yes") %>%
               mutate(is_q1 = ifelse(quartile == "q1", "fast", "slow")), 
             aes(mu14, fill = is_q1)) +
  geom_density(alpha = 0.6) +
  facet_grid(.~n, labeller = labeller(n = n.labs), scales = "free_y") +
  theme_bw() +
  theme(text=element_text(size=14,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 14),
        panel.grid.minor.y = element_blank(),
        legend.position = "bottom"
  ) +
  xlab(~ mu [10]) +
  #xlim(c(0.3,0.5)) +
  ylab("") +
  scale_fill_manual(values = colors_fast) 

p2 <- ggplot(data_outliers_normalized %>%
               mutate(odd = as.numeric(as.character(m))%%2) %>%
               filter(odd == FALSE), 
             aes(mu14, fill = outlier)) +
  geom_density(alpha = 0.6) +
  # geom_histogram() +
  facet_grid(.~n, labeller = labeller(n = n.labs)) +
  theme_bw() +
  theme(text=element_text(size=14,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 14),
        panel.grid.minor.y = element_blank(),
        legend.position = "bottom"
  ) +
  xlab(~ mu [10]) +
  #xlim(c(0.3,0.5)) +
  ylab("") +
  scale_fill_manual(values = colors_outliers)  
p <- p1/p2
p


#  Number of different margins ----------------------------
p1 <- ggplot(data_quartiles_normalized %>%
               filter(odd == "yes") %>%
               mutate(is_q1 = ifelse(quartile == "q1", "fast", "slow")), 
             aes(mu8, fill = is_q1)) +
  geom_density(alpha = 0.6) +
  facet_grid(.~n, labeller = labeller(n = n.labs), scales = "free_y") +
  theme_bw() +
  theme(text=element_text(size=14,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 14),
        panel.grid.minor.y = element_blank(),
        axis.text.x = element_text(angle = 90)
        #legend.position = "bottom"
  ) +
  xlab(~ mu [8]) +
  ylab("") +
  labs(fill = "Execution time") +
  scale_fill_manual(values = colors_fast) 

p2 <- ggplot(data_outliers_normalized %>%
               mutate(odd = as.numeric(as.character(m))%%2) %>%
               filter(odd == FALSE), 
             aes(mu8, fill = outlier)) +
  geom_density(alpha = 0.6) +
  # geom_histogram() +
  facet_grid(.~n, labeller = labeller(n = n.labs)) +
  theme_bw() +
  theme(text=element_text(size=14,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 14),
        panel.grid.minor.y = element_blank(),
        axis.text.x = element_text(angle = 90)
  ) +
  xlab(~ mu [8]) +
  labs(fill = "Outlier") +
  #xlim(c(0.3,0.5)) +
  ylab("") +
  scale_fill_manual(values = colors_outliers)  
p <- p1/p2
p
ggsave("mu8.png", plot=p1, height=6, width=23, units=c("cm"), dpi=1000)

