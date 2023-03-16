colors <- c("#0b3c49",
            #"#885a89",
            "#59a5d8",
          #  "#dbcbd8",
            "#ef946c",
            #"#eb4511",
            "#fabc2a"
            #"#86836d",
            #"#00a878",
            #"#32161f")
)

ms_keep <- c(10, 50, 340, 890)
data_plot <- data %>% filter(n==10, m %in% c(ms_keep, ms_keep+1))


# FINALES

theme_border <- theme(panel.border = element_rect(colour = "black", fill=NA, size=5))

# Figure 1 ---------------------------------------------------------------------


# Average Kendall distance
s4_a <- ggplot(data_plot, aes(mu1, time)) +
  geom_point(aes(color = as.factor(basem), shape = odd), alpha = 0.5, size = 2) +
  facet_grid(~as.factor(basem)) +
  theme_bw() +
  theme(text=element_text(size=12,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 5, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 10),
        panel.grid.minor.y = element_blank(),
        #legend.position = "bottom",
        legend.position = "none"
  ) +
  scale_color_manual(values = colors) + 
  xlab(~ mu [1]) +
  ylab("") + 
  labs(title = "Average Kendall distance")

s4_a <- s4_a + plot_annotation(theme = theme_border)
  
# Range of positions

s4_b1 <- ggplot(data_plot, aes(factor(mu2, levels = 0:9), time)) +
  geom_jitter(height = 0, width = .2, aes(color = as.factor(basem), shape = odd), alpha = 0.5, size = 2) +
  facet_grid(~as.factor(basem)) +
  theme_bw() +
  theme(text=element_text(size=12,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 5, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 10),
        panel.grid.minor.y = element_blank(),
        #legend.position = "bottom",
        legend.position = "none"
  ) +
  scale_x_discrete(drop=FALSE) +
  scale_color_manual(values = colors) + 
  xlab(~ mu [2]) +
  ylab("") +
  labs(title = "Range of positions")

s4_b2 <- ggplot(data_plot, aes(factor(mu3, levels = 0:9), time)) +
  geom_jitter(height = 0, width = .1, aes(color = as.factor(basem), shape = odd), alpha = 0.5, size = 2) +
  facet_grid(~as.factor(basem)) +
  theme_bw() +
  theme(text=element_text(size=12,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 5, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 10),
        panel.grid.minor.y = element_blank(),
        #legend.position = "bottom",
        legend.position = "none"
  ) +
  scale_color_manual(values = colors) + 
  xlab(~ mu [3]) +
  ylab("") 

s4_b3 <- ggplot(data_plot, aes(mu4, time)) +
  geom_jitter(height = 0, width = .1, aes(color = as.factor(basem), shape = odd), alpha = 0.5, size = 2) +
  facet_grid(~as.factor(basem)) +
  theme_bw() +
  theme(text=element_text(size=12,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 5, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 10),
        panel.grid.minor.y = element_blank(),
        #legend.position = "bottom",
        legend.position = "none"
  ) +
  scale_color_manual(values = colors) + 
  xlab(~ mu [4]) +
  ylab("") 


s4_c <- ggplot(data_plot, aes(mu7, time)) +
  geom_jitter(height = 0, width = .1, aes(color = as.factor(basem), shape = odd), alpha = 0.5, size = 2) +
  facet_grid(~as.factor(basem), scales="free_x") +
  theme_bw() +
  theme(text=element_text(size=12,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 5, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 10),
        panel.grid.minor.y = element_blank(),
        #legend.position = "bottom",
        legend.position = "none",
        axis.text.x = element_text(angle = 90)
  ) +
  scale_color_manual(values = colors) + 
  xlab(~ mu [5]) +
  ylab("") +
  labs(title = "Bound to the optimal cost")
  

s4_d <- ggplot(data_plot, aes(mu20, time)) +
  geom_jitter(height = 0, width = .1, aes(color = as.factor(basem), shape = odd), alpha = 0.5, size = 2) +
  facet_grid(~as.factor(basem)) +
  theme_bw() +
  theme(text=element_text(size=12,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 5, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 10),
        panel.grid.minor.y = element_blank(),
        #legend.position = "bottom",
        legend.position = "none"
  ) +
  scale_color_manual(values = colors) + 
  xlab(~ mu [6]) +
  ylab("") +
  labs(title = "Intransitivity")

s4_a / s4_b1 / s4_b2 / s4_b3 / s4_c / s4_d

# Figura 2 ---------------------------------------------------------------------
# pairwise compasison of the voters 

# most common margin
p9 <- ggplot(data_plot, aes(mu9, time)) +
  geom_jitter(height = 0, width = .1, aes(color = as.factor(basem), shape = odd), alpha = 0.5, size = 2) +
  facet_grid(~as.factor(basem), scales = "free_x") +
  theme_bw() +
  theme(text=element_text(size=12,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 5, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 10),
        panel.grid.minor.y = element_blank(),
        #legend.position = "bottom",
        legend.position = "none",
        axis.text.x = element_text(angle = 90)
  ) +
  scale_color_manual(values = colors) + 
  xlab(~ mu [7]) +
  ylab("") 

# number of different margins
p10 <- ggplot(data_plot, aes(mu10, time)) +
  geom_jitter(height = 0, width = .1, aes(color = as.factor(basem), shape = odd), alpha = 0.5, size = 2) +
  facet_grid(~as.factor(basem), scales = "free_x") +
  theme_bw() +
  theme(text=element_text(size=12,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 5, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 10),
        panel.grid.minor.y = element_blank(),
        #legend.position = "bottom",
        legend.position = "none",
        axis.text.x = element_text(angle = 90)
  ) +
  scale_color_manual(values = colors) + 
  xlab(~ mu [8]) +
  ylab("") 

# frequency of the min margin
p11 <- ggplot(data_plot, aes(mu11, time)) +
  geom_jitter(height = 0, width = .1, aes(color = as.factor(basem), shape = odd), alpha = 0.5, size = 2) +
  facet_grid(~as.factor(basem), scales = "free_x") +
  theme_bw() +
  theme(text=element_text(size=12,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 5, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 10),
        panel.grid.minor.y = element_blank(),
        #legend.position = "bottom",
        legend.position = "none",
        axis.text.x = element_text(angle = 90)
  ) +
  scale_color_manual(values = colors) + 
  xlab(~ mu [9]) +
  ylab("") 

p9/p10/p11

# Figura 3 ---------------------------------------------------------------------
# Based on row sums

# borda
p12 <- ggplot(data_plot, aes(mu12, time)) +
  geom_jitter(height = 0, width = .1, aes(color = as.factor(basem), shape = odd), alpha = 0.5, size = 2) +
  facet_grid(~as.factor(basem), scales = "free_x") +
  theme_bw() +
  theme(text=element_text(size=12,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 5, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 10),
        panel.grid.minor.y = element_blank(),
        #legend.position = "bottom",
        legend.position = "none",
        axis.text.x = element_text(angle = 90)
  ) +
  scale_color_manual(values = colors) + 
  xlab(~ mu [10]) +
  ylab("") 

# omega
p13 <- ggplot(data_plot, aes(as.factor(mu13), time)) +
  geom_jitter(height = 0, width = .1, aes(color = as.factor(basem), shape = odd), alpha = 0.5, size = 2) +
  facet_grid(~as.factor(basem)) +
  theme_bw() +
  theme(text=element_text(size=12,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 5, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 10),
        panel.grid.minor.y = element_blank(),
        #legend.position = "bottom",
        legend.position = "none"
  ) +
  scale_color_manual(values = colors) + 
  xlab(~ mu [11]) +
  ylab("") 

# sd rowsum
p14 <- ggplot(data_plot, aes(mu14, time)) +
  geom_jitter(height = 0, width = .1, aes(color = as.factor(basem), shape = odd), alpha = 0.5, size = 2) +
  facet_grid(~as.factor(basem), scales = "free_x") +
  theme_bw() +
  theme(text=element_text(size=12,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 5, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 10),
        panel.grid.minor.y = element_blank(),
        #legend.position = "bottom",
        legend.position = "none",
        axis.text.x = element_text(angle = 90)
  ) +
  scale_color_manual(values = colors) + 
  xlab(~ mu [12]) +
  ylab("") 

p12/p13/p14

# Figura 5 ---------------------------------------------------------------------
# distribution of the condorcet ranking

# sd beta
p15 <- ggplot(data_plot, aes(mu15, time)) +
  geom_jitter(height = 0, width = .1, aes(color = as.factor(basem), shape = odd), alpha = 0.5, size = 2) +
  facet_grid(~as.factor(basem), scales = "free_x") +
  theme_bw() +
  theme(text=element_text(size=12,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 5, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 10),
        panel.grid.minor.y = element_blank(),
        #legend.position = "bottom",
        legend.position = "none",
        axis.text.x = element_text(angle = 90)
  ) +
  scale_color_manual(values = colors) + 
  xlab(~ mu [13]) +
  ylab("") 

# mean beta
p16 <- ggplot(data_plot, aes(mu16, time)) +
  geom_jitter(height = 0, width = .1, aes(color = as.factor(basem), shape = odd), alpha = 0.5, size = 2) +
  facet_grid(~as.factor(basem), scales = "free_x") +
  theme_bw() +
  theme(text=element_text(size=12,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 5, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 10),
        panel.grid.minor.y = element_blank(),
        #legend.position = "bottom",
        legend.position = "none"
  ) +
  scale_color_manual(values = colors) + 
  xlab(~ mu [14]) +
  ylab("") 


# median
p17 <- ggplot(data_plot, aes(mu17, time)) +
  geom_jitter(height = 0, width = .1, aes(color = as.factor(basem), shape = odd), alpha = 0.5, size = 2) +
  facet_grid(~as.factor(basem)) +
  theme_bw() +
  theme(text=element_text(size=12,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 5, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 10),
        panel.grid.minor.y = element_blank(),
        #legend.position = "bottom",
        legend.position = "none"
  ) +
  scale_color_manual(values = colors) + 
  xlab(~ mu [15]) +
  ylab("") 

# mean - median


p18 <- ggplot(data_plot, aes(mu18, time)) +
  geom_jitter(height = 0, width = .1, aes(color = as.factor(basem), shape = odd), alpha = 0.5, size = 2) +
  facet_grid(~as.factor(basem), scales = "free_x") +
  theme_bw() +
  theme(text=element_text(size=12,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 5, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 10),
        panel.grid.minor.y = element_blank(),
        #legend.position = "bottom",
        legend.position = "none",
        axis.text.x = element_text(angle = 90)
        
  ) +
  scale_color_manual(values = colors) + 
  xlab(~ mu [16]) +
  ylab("") 


p15/p16/p17/p18

p19 <- ggplot(data_plot, aes(mu19, time)) +
  geom_jitter(height = 0, width = .1, aes(color = as.factor(basem), shape = odd), alpha = 0.5, size = 2) +
  facet_grid(~as.factor(basem), scales = "free_x") +
  theme_bw() +
  theme(text=element_text(size=12,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 5, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 10),
        panel.grid.minor.y = element_blank(),
        #legend.position = "bottom",
        legend.position = "none",
        axis.text.x = element_text(angle = 90)
        
  ) +
  scale_color_manual(values = colors) + 
  xlab(~ mu [17]) +
  ylab("") 


# antiguas

# mu4
ggplot(data %>% filter(n==10), aes(as.factor(mu3), time)) +
  geom_point(aes(color = as.factor(basem), shape = odd), alpha = 0.3, size = 2) +
  #scale_x_log10() +
  #scale_y_log10() +
  #geom_smooth(color = "black") +
  #facet_grid(n~as.factor(basem), labeller = labeller(n = n.labs), scales = "free") +
  facet_grid(~as.factor(basem)) +
  theme_bw() +
  theme(text=element_text(size=12,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 5, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 10),
        panel.grid.minor.y = element_blank(),
        #legend.position = "bottom",
        legend.position = "none",
     #   axis.text.x = element_text(angle = 90)
  ) +
  labs(color = "Number of voters", shape = "Odd number of voters") +
  scale_color_manual(values = colors) + 
  #scale_x_continuous(labels=function(x) sprintf("%.1f", x)) +
  guides(color = guide_legend(nrow = 2))  +
  xlab(~ mu [4]) +
  ylab("") 





# mu14
ggplot(data %>% filter(n==10), aes(mu14, time)) +
  geom_point(aes(color = as.factor(basem), shape = odd), alpha = 0.3, size = 2) +
  scale_x_log10() +
  #scale_y_log10() +
  geom_smooth(color = "black") +
  #facet_grid(n~as.factor(basem), labeller = labeller(n = n.labs), scales = "free") +
  facet_grid(~as.factor(basem), scales = "free_x") +
  theme_bw() +
  theme(text=element_text(size=12,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 5, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 10),
        panel.grid.minor.y = element_blank(),
        #legend.position = "bottom",
        legend.position = "none",
        axis.text.x = element_text(angle = 90)
  ) +
  labs(color = "Number of voters", shape = "Odd number of voters") +
  scale_color_manual(values = colors) + 
  #scale_x_continuous(labels=function(x) sprintf("%.1f", x)) +
  guides(color = guide_legend(nrow = 2))  +
  xlab(~ mu [14]) +
  ylab("") 




# mu15 pero se ve peor
ggplot(data %>% filter(n==10), aes(mu15, time)) +
  geom_point(aes(color = as.factor(basem), shape = odd), alpha = 0.3, size = 2) +
  #scale_x_log10() +
  scale_y_log10() +
  #geom_smooth(color = "black") +
  #facet_grid(n~as.factor(basem), labeller = labeller(n = n.labs), scales = "free") +
  facet_grid(~as.factor(basem)) +
  theme_bw() +
  theme(text=element_text(size=12,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 5, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 10),
        panel.grid.minor.y = element_blank(),
        #legend.position = "bottom",
        #legend.position = "none",
        axis.text.x = element_text(angle = 90)
  ) +
  labs(color = "Number of voters", shape = "Odd number of voters") +
  scale_color_manual(values = colors) + 
  #scale_x_continuous(labels=function(x) sprintf("%.1f", x)) +
  guides(color = guide_legend(nrow = 2))  +
  xlab(~ mu [15]) +
  ylab("") 




# Figura 3 (5, 6, 7): bounds to the optimal cost. Eliminada por redundante

# p5 <- ggplot(data_plot, aes(mu5, time)) +
#   geom_jitter(height = 0, width = .1, aes(color = as.factor(basem), shape = odd), alpha = 0.5, size = 2) +
#   facet_grid(~as.factor(basem), scales = "free_x") +
#   theme_bw() +
#   theme(text=element_text(size=12,  family="Times New Roman"),
#         axis.title.x = element_text(margin = margin(t = 5, r = 0, b = 0, l = 0)),
#         strip.background = element_rect(fill="white"),
#         strip.text.x = element_text(size = 10),
#         panel.grid.minor.y = element_blank(),
#         #legend.position = "bottom",
#         legend.position = "none",
#         axis.text.x = element_text(angle = 90)
#   ) +
#   scale_color_manual(values = colors) + 
#   xlab(~ mu [5]) +
#   ylab("") 
# 
# p6 <- ggplot(data_plot, aes(mu6, time)) +
#   geom_jitter(height = 0, width = .1, aes(color = as.factor(basem), shape = odd), alpha = 0.5, size = 2) +
#   facet_grid(~as.factor(basem), scales = "free_x") +
#   theme_bw() +
#   theme(text=element_text(size=12,  family="Times New Roman"),
#         axis.title.x = element_text(margin = margin(t = 5, r = 0, b = 0, l = 0)),
#         strip.background = element_rect(fill="white"),
#         strip.text.x = element_text(size = 10),
#         panel.grid.minor.y = element_blank(),
#         #legend.position = "bottom",
#         legend.position = "none",
#         axis.text.x = element_text(angle = 90)
#   ) +
#   scale_color_manual(values = colors) + 
#   xlab(~ mu [6]) +
#   ylab("") 
# 
# p7 <- ggplot(data_plot, aes(mu7, time)) +
#   geom_jitter(height = 0, width = .1, aes(color = as.factor(basem), shape = odd), alpha = 0.5, size = 2) +
#   facet_grid(~as.factor(basem), scales = "free_x") +
#   theme_bw() +
#   theme(text=element_text(size=12,  family="Times New Roman"),
#         axis.title.x = element_text(margin = margin(t = 5, r = 0, b = 0, l = 0)),
#         strip.background = element_rect(fill="white"),
#         strip.text.x = element_text(size = 10),
#         panel.grid.minor.y = element_blank(),
#         #legend.position = "bottom",
#         legend.position = "none",
#         axis.text.x = element_text(angle = 90)
#   ) +
#   scale_color_manual(values = colors) + 
#   xlab(~ mu [5]) +
#   ylab("") 
# 
# p5+p6+p7
# 
# 
# 
