colors <- c("#0b3c49",
            "#885a89",
            "#59a5d8",
            "#dbcbd8",
            "#ef946c",
            "#eb4511",
            "#fabc2a",
            "#86836d",
            "#00a878",
            "#32161f")



# Execution time ----------------------------------------------------------

ggplot(data, aes(x = 0, y = time, color = as.factor(basem), shape = odd)) +
  geom_jitter(height = 0, alpha = 0.8) +
  facet_grid(n~m, scales = "free_y", labeller = labeller(n = n.labs)) +
  scale_x_continuous(breaks = NULL) + 
  scale_color_manual(values = colors) +
 # scale_color_manual(values = c("#535050", "#312F2F")) +
  guides(color=FALSE,shape=FALSE) +
  theme_bw() +
  theme(text=element_text(size=12,  family="Times New Roman"),
        axis.title.y = element_text(margin = margin(t = 0, r = 20, b = 0, l = 0)),
        axis.title.x = element_text(margin = margin(t = 20, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        legend.position = "none",
        strip.text.y = element_text(size = 8)) +
  xlab("Number of voters") +
  ylab("Execution time (in seconds)")

# Average Kendall distance ------------------------------------------------

# New facet label names for n variable
n.labs <- paste("Number of alternatives:", 8:10)
names(n.labs) <- 8:10

ggplot(data_normalized, aes(mu1, as.factor(basem), shape = odd, color = as.factor(basem))) +
  geom_jitter(alpha = 0.7, width = 0) +
  geom_vline(xintercept = 0.5, alpha = 0.8) +
  facet_grid(n~., labeller = labeller(n = n.labs)) +
  theme_bw() +
  theme(text=element_text(size=12,  family="Times New Roman"),
        axis.title.y = element_text(margin = margin(t = 0, r = 20, b = 0, l = 0)),
        axis.title.x = element_text(margin = margin(t = 20, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        legend.position = "none",
        strip.text.y = element_text(size = 8)) +
  xlab(~ mu [1]) +
  ylab("Number of voters") +
  #xlim(c(0,1)) +
  scale_color_manual(values = colors) 


# Range of positions ------------------------------------------------------

p_mu2 <- ggplot(data, aes(as.factor(mu2), y = m, color = as.factor(basem), shape = odd)) +
  geom_jitter(alpha = .9, width=0.3) +
  facet_grid(.~n, labeller = labeller(n = n.labs), scales = "free_x") +
  theme_bw() +
  theme(text=element_text(size=9,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 12),
        panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank(),
        axis.text.y = element_blank(),
        axis.ticks.y = element_blank(),
        legend.position = "bottom") +
  xlab(~ mu [2]) +
  ylab("") +
  labs(title="Maximum range", color = "Number of voters") +
  scale_color_manual(values = colors) +
  scale_shape(guide = 'none') +
  guides(col = guide_legend(nrow = 1)) 

p_mu3 <- ggplot(data, aes(as.factor(mu3), y = m, color = as.factor(basem), shape = odd)) +
  geom_jitter(alpha = .9, width=0.3) +
  facet_grid(.~n, labeller = labeller(n = n.labs), scales = "free_x") +
  theme_bw() +
  theme(text=element_text(size=9,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 12),
        panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank(),
        axis.text.y = element_blank(),
        axis.ticks.y = element_blank(),
        legend.position = "bottom") +
  xlab(~ mu [3]) +
  ylab("") +
  labs(title="Minimum range", color = "Number of voters") +
  scale_color_manual(values = colors) +
  scale_shape(guide = 'none') +
  guides(col = guide_legend(nrow = 1)) 

p_mu4 <- ggplot(data, aes(mu4, y = m, color = as.factor(basem), shape = odd)) +
  geom_jitter(alpha = .9, width=0) +
  facet_grid(.~n, labeller = labeller(n = n.labs), scales = "free_x") +
  theme_bw() +
  theme(text=element_text(size=9,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 12),
        panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank(),
        axis.text.y = element_blank(),
        axis.ticks.y = element_blank(),
        legend.position = "bottom"
        ) +
  xlab(~ mu [4]) +
  ylab("") +
  labs(title="Average range", color = "Number of voters") +
  scale_color_manual(values = colors) + 
  scale_x_continuous(breaks=2:9) + 
  scale_shape(guide = 'none') +
  guides(col = guide_legend(nrow = 1)) 

(p_mu2/p_mu3/p_mu4)+plot_layout(guides = "collect") & theme(legend.position = 'bottom')


# Bounds ------------------------------------------------------------------

p_mu5 <- ggplot(data_normalized, aes(mu5, fill = as.factor(basem))) +
  geom_histogram(binwidth = .025) +
  facet_grid(n~as.factor(basem), labeller = labeller(n = n.labs)) +
  theme_bw() +
  theme(text=element_text(size=9,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 12),
        panel.grid.minor.y = element_blank(),
        legend.position = "bottom"
  ) +
  xlab(~ mu [5]) +
  ylab("") +
  labs(title="Lower bound", fill = "Number of voters") +
  guides(fill = guide_legend(nrow = 1)) +
  scale_fill_manual(values = colors)

p_mu6 <- ggplot(data_normalized, aes(mu6, fill = as.factor(basem))) +
  geom_histogram(binwidth = .025) +
  facet_grid(n~as.factor(basem), labeller = labeller(n = n.labs)) +
  theme_bw() +
  theme(text=element_text(size=9,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 12),
        panel.grid.minor.y = element_blank(),
        legend.position = "bottom"
  ) +
  xlab(~ mu [6]) +
  ylab("") +
  labs(title="Upper bound", fill = "Number of voters") +
  guides(fill = guide_legend(nrow = 1)) +
  scale_fill_manual(values = colors)

p_mu7 <- ggplot(data_normalized, aes(mu7, fill = as.factor(basem))) +
  geom_histogram(binwidth = .025) +
  facet_grid(n~as.factor(basem), labeller = labeller(n = n.labs)) +
  theme_bw() +
  theme(text=element_text(size=9,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 12),
        panel.grid.minor.y = element_blank(),
        legend.position = "bottom"
  ) +
  xlab(~ mu [7]) +
  ylab("") +
  labs(title="Range of the bounds", fill = "Number of voters") +
  guides(fill = guide_legend(nrow = 1)) +
  scale_fill_manual(values = colors)

(p_mu5/p_mu6/p_mu7)+plot_layout(guides = "collect") & theme(legend.position = 'bottom')

ggplot(data, aes(mu5, mu7)) +
  geom_point() +
  facet_grid(n~as.factor(basem))
  
# Pairwise opinion of the voters ------------------------------------------

ggplot(data_normalized, aes(mu8, fill = as.factor(basem))) +
  geom_histogram(binwidth = .05) +
  facet_grid(n~as.factor(basem), labeller = labeller(n = n.labs)) +
  theme_bw() +
  theme(text=element_text(size=9,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 12),
        panel.grid.minor.y = element_blank(),
        legend.position = "bottom"
  ) +
  xlab(~ mu [8]) +
  ylab("") +
  labs(fill = "Number of voters") +
  scale_fill_manual(values = colors) + 
  scale_x_continuous(labels=function(x) sprintf("%.1f", x)) +
  guides(fill = guide_legend(nrow = 1)) 


# Most common margin ------------------------------------------------------

ggplot(data_normalized, aes(mu9, fill = as.factor(basem))) +
  geom_histogram(binwidth = .1) +
  facet_grid(n~as.factor(basem), labeller = labeller(n = n.labs)) +
  theme_bw() +
  theme(text=element_text(size=9,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 12),
        panel.grid.minor.y = element_blank(),
        legend.position = "bottom"
  ) +
  xlab(~ mu [9]) +
  ylab("") +
  labs(fill = "Number of voters") +
  scale_fill_manual(values = colors) + 
  scale_x_continuous(labels=function(x) sprintf("%.1f", x)) +
  guides(fill = guide_legend(nrow = 1)) 


# Number of unique pairs --------------------------------------------------


ggplot(data_normalized, aes(mu10, fill = as.factor(basem))) +
  geom_histogram(binwidth = .025) +
  facet_grid(n~as.factor(basem), labeller = labeller(n = n.labs)) +
  theme_bw() +
  theme(text=element_text(size=9,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 12),
        panel.grid.minor.y = element_blank(),
        legend.position = "bottom"
  ) +
  xlab(~ mu [10]) +
  ylab("") +
  labs(fill = "Number of voters") +
  scale_fill_manual(values = colors) + 
  scale_x_continuous(labels=function(x) sprintf("%.1f", x)) +
  guides(fill = guide_legend(nrow = 1)) 



# Frequency of the lowest margin ------------------------------------------

ggplot(data_normalized, aes(mu11, fill = as.factor(basem))) +
  geom_histogram(binwidth = .025) +
  facet_grid(n~as.factor(basem), labeller = labeller(n = n.labs), scales = "free_x") +
  theme_bw() +
  theme(text=element_text(size=9,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 12),
        panel.grid.minor.y = element_blank(),
        legend.position = "bottom"
  ) +
  xlab(~ mu [10]) +
  ylab("") +
  labs(fill = "Number of voters") +
  scale_fill_manual(values = colors) + 
  scale_x_continuous(labels=function(x) sprintf("%.1f", x)) +
  guides(fill = guide_legend(nrow = 1)) 


# Distance from the Borda ranking to the profile --------------------------

ggplot(data_normalized, aes(mu12, fill = as.factor(basem))) +
  geom_histogram(binwidth = .025) +
  facet_grid(n~as.factor(basem), labeller = labeller(n = n.labs), scales = "free_x") +
  theme_bw() +
  theme(text=element_text(size=9,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 12),
        panel.grid.minor.y = element_blank(),
        legend.position = "bottom"
  ) +
  xlab(~ mu [10]) +
  ylab("") +
  labs(fill = "Number of voters") +
  scale_fill_manual(values = colors) + 
  scale_x_continuous(labels=function(x) sprintf("%.1f", x)) +
  guides(fill = guide_legend(nrow = 1)) 


# Omega -------------------------------------------------------------------

ggplot(data_normalized, aes(mu13, fill = as.factor(basem))) +
  geom_histogram(binwidth = .05) +
  facet_grid(n~as.factor(basem), labeller = labeller(n = n.labs), scales = "free_x") +
  theme_bw() +
  theme(text=element_text(size=9,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 12),
        panel.grid.minor.y = element_blank(),
        legend.position = "bottom"
  ) +
  xlab(~ mu [13]) +
  ylab("") +
  labs(fill = "Number of voters") +
  scale_fill_manual(values = colors) + 
  scale_x_continuous(labels=function(x) sprintf("%.1f", x)) +
  guides(fill = guide_legend(nrow = 1)) 


# Sd deviation of the rowsum ----------------------------------------------

ggplot(data, aes(mu14, fill = as.factor(basem))) +
  geom_histogram() +
  facet_grid(n~as.factor(basem), labeller = labeller(n = n.labs), scales = "free_x") +
  theme_bw() +
  theme(text=element_text(size=9,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 12),
        panel.grid.minor.y = element_blank(),
        legend.position = "bottom"
  ) +
  xlab(~ mu [13]) +
  ylab("") +
  labs(fill = "Number of voters") +
  scale_fill_manual(values = colors) + 
  scale_x_continuous(labels=function(x) sprintf("%.1f", x)) +
  guides(fill = guide_legend(nrow = 1)) 


# Standard deviation of beta ----------------------------------------------

ggplot(data, aes(mu15, fill = as.factor(basem))) +
  geom_histogram() +
  facet_grid(n~as.factor(basem), labeller = labeller(n = n.labs), scales = "free_x") +
  theme_bw() +
  theme(text=element_text(size=9,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 12),
        panel.grid.minor.y = element_blank(),
        legend.position = "bottom"
  ) +
  xlab(~ mu [13]) +
  ylab("") +
  labs(fill = "Number of voters") +
  scale_fill_manual(values = colors) + 
  scale_x_continuous(labels=function(x) sprintf("%.1f", x)) +
  guides(fill = guide_legend(nrow = 1)) 

# Mean of beta ------------------------------------------------------------

ggplot(data_normalized %>% filter(odd=="yes"), aes(mu16, fill = as.factor(basem))) +
  geom_histogram() +
  facet_grid(n~as.factor(basem), labeller = labeller(n = n.labs), scales = "free_x") +
  theme_bw() +
  theme(text=element_text(size=9,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 12),
        panel.grid.minor.y = element_blank(),
        legend.position = "bottom"
  ) +
  xlab(~ mu [16]) +
  ylab("") +
  labs(fill = "Number of voters") +
  scale_fill_manual(values = colors) + 
  scale_x_continuous(labels=function(x) sprintf("%.1f", x)) +
  guides(fill = guide_legend(nrow = 1)) 


# Media of beta -----------------------------------------------------------

ggplot(data_normalized %>% filter(odd=="yes"), aes(mu17, fill = as.factor(basem))) +
  geom_histogram() +
  facet_grid(n~as.factor(basem), labeller = labeller(n = n.labs), scales = "free_x") +
  theme_bw() +
  theme(text=element_text(size=9,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 12),
        panel.grid.minor.y = element_blank(),
        legend.position = "bottom"
  ) +
  xlab(~ mu [17]) +
  ylab("") +
  labs(fill = "Number of voters") +
  scale_fill_manual(values = colors) + 
  scale_x_continuous(labels=function(x) sprintf("%.1f", x)) +
  guides(fill = guide_legend(nrow = 1)) 



# Mean-median of beta -----------------------------------------------------


# Sum of beta -------------------------------------------------------------



# Metrics over the vector of Condorcet ------------------------------------

# 15 y 19 son proporcionales pero cambian dependiendo del valor de n
ggpairs(data %>% select(paste0("mu", 15:19)))

ggplot(data, aes(mu17, fill = as.factor(basem))) +
  geom_histogram(binwidth = .025) +
  facet_grid(n~as.factor(basem), labeller = labeller(n = n.labs), scales = "free") 
data %>% group_by(n,m) %>% summarise(range_min = range(mu16)[1], range_max = range(mu16)[2])

ggplot(data, aes(mu16, mu7, color = m)) +
  geom_point() +
  facet_grid(~n)


ggplot(data, aes(mu18, fill = as.factor(basem))) +
  geom_histogram() +
  facet_grid(n~as.factor(basem), labeller = labeller(n = n.labs), scales = "free") 

# Intransitivity ----------------------------------------------------------

ggplot(data, aes(mu20, fill = m)) +
  geom_histogram() +
  facet_grid(n~m, labeller = labeller(n = n.labs), scales = "free") 



# AHIC -------------------

data_to_plot <- data_quartiles 
data_to_plot$n <- relevel(data_to_plot$n, "9")
data_to_plot$n <- relevel(data_to_plot$n, "8")

l <- sort(as.numeric(levels(data_to_plot$m)))
data_to_plot$m <- factor(as.numeric(as.character(data_to_plot$m)),
                          levels = l)

ggplot(data_to_plot, aes(m, fill = odd)) +
  geom_bar() +
  facet_grid(n~quartile) +
  theme_bw() +
  theme(text=element_text(size=9,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 12),
        panel.grid.minor.y = element_blank(),
        legend.position = "bottom",
        axis.text.x = element_text(angle = 90)
  )



# SD TETA -----------------------------
ggplot(data_quartiles_normalized %>% 
          mutate(quartile = fct_collapse(quartile, fast = c("q1"), slow = c("q2","q3","q4"))), 
       aes(mu12, fill = quartile)) +
  geom_density(alpha = 0.5) +
  facet_grid(~n, labeller = labeller(n = n.labs)) +
  theme_bw() +
  theme(text=element_text(size=9,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 12),
        panel.grid.minor.y = element_blank(),
        legend.position = "bottom"
  ) +
  xlab(~ mu [12]) +
  xlim(c(0, 0.05)) +
  ylab("") +
  labs(fill = "Profiles of rankings that are") +
  #scale_fill_manual(values = colors) + 
  # scale_x_continuous(labels=function(x) sprintf("%.1f", x)) +
  theme(axis.text.x = element_text(angle=90))

ggplot(data_outliers_normalized,
       aes(mu12, fill = outlier)) +
  geom_density(alpha = 0.5) +
  #geom_histogram(binwidth = .001) +
  facet_grid(.~n, labeller = labeller(n = n.labs)) +
  theme_bw() +
  theme(text=element_text(size=9,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 12),
        panel.grid.minor.y = element_blank(),
        legend.position = "bottom"
  ) +
  xlab(~ mu [12]) +
  ylab("") +
  labs(fill = "The profile of rankings is an outlier") +
  #scale_fill_manual(values = colors) + 
  # scale_x_continuous(labels=function(x) sprintf("%.1f", x)) +
  theme(axis.text.x = element_text(angle=90))


# DIST BORDA --------------------
ggplot(data_quartiles_normalized  %>%
         mutate(is_q1 = ifelse(quartile == "q1", "FAST", "SLOW")), aes(mu10, fill = n)) +
  #geom_histogram() +
  geom_density(alpha = 0.2) +
  facet_grid(n~is_q1, labeller = labeller(n = n.labs)) +
  theme_bw() +
  theme(text=element_text(size=9,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 12),
        panel.grid.minor.y = element_blank(),
        legend.position = "bottom"
  ) +
  xlab(~ mu [10]) +
  ylab("") +
  labs(fill = "Number of voters") +
  scale_fill_manual(values = colors) + 
  scale_x_continuous(labels=function(x) sprintf("%.1f", x)) +
  guides(fill = "none") 

ggplot(data_outliers_normalized, aes(mu10, fill = outlier)) +
  #geom_histogram() +
  geom_density(alpha = 0.2) +
  facet_grid(n~., labeller = labeller(n = n.labs)) +
  theme_bw() +
  theme(text=element_text(size=9,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 12),
        panel.grid.minor.y = element_blank(),
        legend.position = "bottom"
  ) +
  xlab(~ mu [10]) +
  ylab("") +
  labs(fill = "Number of voters") +
  scale_fill_manual(values = colors) + 
  scale_x_continuous(labels=function(x) sprintf("%.1f", x)) +
  guides(fill = "none") 


# sd de beta
ggplot(data_quartiles_normalized %>%
         #filter(odd == "no") %>%
         mutate(is_q1 = quartile == "q1"), aes(mu13, fill = is_q1)) +
  #geom_density(alpha = 0.3) +
  geom_histogram(bins = 50) +
  facet_grid(n~., labeller = labeller(n = n.labs), scales = "free_y") +
  theme_bw() +
  theme(text=element_text(size=9,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 12),
        panel.grid.minor.y = element_blank(),
        legend.position = "bottom"
  ) +
  xlab(~ mu [13]) +
  ylab("") +
  labs(fill = "Execution time") +
  scale_fill_manual(values = colors) + 
  scale_x_continuous(labels=function(x) sprintf("%.1f", x)) +
  # guides(fill = guide_legend(nrow = 1)) 
  guides(fill = "none")

# mean beta # filtrado solo para los impares
ggplot(data_quartiles_normalized %>%
         filter(odd == "yes"), aes(mu14, fill = n)) +
  geom_density(alpha = 0.3) +
  #geom_histogram(bins = 50) +
  facet_grid(n~quartile, labeller = labeller(n = n.labs), scales = "free_y") +
  theme_bw() +
  theme(text=element_text(size=9,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 12),
        panel.grid.minor.y = element_blank(),
        legend.position = "bottom"
  ) +
  xlab(~ mu [14]) +
  ylab("") +
  labs(fill = "Execution time") +
  scale_fill_manual(values = colors) + 
  scale_x_continuous(labels=function(x) sprintf("%.1f", x)) +
  # guides(fill = guide_legend(nrow = 1)) 
  guides(fill = "none")


# pairwise final_aihc_8
ggplot(data_quartiles_normalized, aes(mu8, fill = quartile,
                                      color = quartile)) +
  #geom_density(alpha = 0.5, size = 0.8, aes(linetype = quartile, y = ..count..)) +
  geom_density(alpha = 0.5, size = 0.8, aes(linetype = quartile)) +
  facet_grid(n~., labeller = labeller(n = n.labs)) +
  theme_bw() +
  theme(text=element_text(size=9,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 12),
        panel.grid.minor.y = element_blank(),
        legend.position = "bottom"
  ) +
  xlab(~ mu [8]) +
  ylab("") +
  labs(fill = "Execution time") +
  #scale_fill_manual(values = colors) + 
  scale_x_continuous(labels=function(x) sprintf("%.1f", x)) +
  guides(color = "none", linetype = "none")

# binary - final_aihc_8_fastest
ggplot(data_quartiles_normalized %>%
         mutate(is_q1 = quartile == "q1"), aes(mu8, fill = is_q1,
                                               color = is_q1)) +
  #geom_density(alpha = 0.5, size = 0.8, aes(linetype = quartile, y = ..count..)) +
  geom_density(alpha = 0.5, size = 0.8, aes(linetype = is_q1)) +
  facet_grid(n~., labeller = labeller(n = n.labs)) +
  theme_bw() +
  theme(text=element_text(size=9,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 12),
        panel.grid.minor.y = element_blank(),
        legend.position = "bottom"
  ) +
  xlab(~ mu [8]) +
  ylab("") +
  labs(fill = "Is the profile q1?") +
  #scale_fill_manual(values = colors) + 
  scale_x_continuous(labels=function(x) sprintf("%.1f", x)) +
  guides(color = "none", linetype = "none")

# binary - final_aihc_8_outliers
ggplot(data_outliers_normalized, aes(mu8, fill = outlier,
                                               color = outlier)) +
  #geom_density(alpha = 0.5, size = 0.8, aes(linetype = quartile, y = ..count..)) +
  geom_density(alpha = 0.5, size = 0.8, aes(linetype = outlier)) +
  facet_grid(n~., labeller = labeller(n = n.labs)) +
  theme_bw() +
  theme(text=element_text(size=9,  family="Times New Roman"),
        axis.title.x = element_text(margin = margin(t = 10, r = 0, b = 0, l = 0)),
        strip.background = element_rect(fill="white"),
        strip.text.x = element_text(size = 12),
        panel.grid.minor.y = element_blank(),
        legend.position = "bottom"
  ) +
  xlab(~ mu [8]) +
  ylab("") +
  labs(fill = "Is the profile an outlier?") +
  #scale_fill_manual(values = colors) + 
  scale_x_continuous(labels=function(x) sprintf("%.1f", x)) +
  guides(color = "none", linetype = "none")
