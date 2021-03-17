cn <- c("n",
        "omega",
        "index",
        "method",
        "time",
        "nsolutions",
        "ntentative")

agreements <- unlist(check_data_experiments_margin(pors12nc))
#nrp <- unlist(check_data_experiments_nrp(pors12nc))
resultsNC12 <- read_delim("resultsNC12nc_123.csv",
                          col_names = cn, delim = " ") %>%
  mutate(
    id = rep(1:55, each = 3),
    agreement = rep(agreements, each = 3),
    method = as.factor(method),
    omega = as.factor(omega),
    #nrp = as.factor(rep(nrp, each = 3))
  )

agreements <- unlist(check_data_experiments_margin(pors13nc))[1:31]
#nrp <- unlist(check_data_experiments_nrp(pors12nc))
resultsNC13 <- read_delim("resultsNC13.csv",
                          col_names = cn, delim = " ") %>%
  mutate(
    id = 1:31,
    #agreement = agreements,
    method = as.factor(method),
    omega = as.factor(omega),
    #nrp = as.factor(rep(nrp, each = 3))
  )

agreements <- unlist(check_data_experiments_margin(pors14nc))[1:25]
#nrp <- unlist(check_data_experiments_nrp(pors12nc))
resultsNC14 <- read_delim("resultsNC14.csv",
                          col_names = cn, delim = " ") %>%
  mutate(
   # id = 1:25,
   # agreement = agreements,
    method = as.factor(method),
    omega = as.factor(omega),
    #nrp = as.factor(rep(nrp, each = 3))
  )

resultsNC <- bind_rows(
  resultsNC12 %>% filter(method==3),
  resultsNC13,
  resultsNC14
)

library(scales)
hex_codes1 <- hue_pal()(11)                             # Identify hex codes
hex_codes1 

# zoom in log transformation of n=12
zoomNC12 <- ggplot(resultsNC12 %>%
         filter(method!=2) %>%
         filter(as.numeric(omega) < 8) %>%
         group_by(id) %>%
         mutate(ntentative = max(ntentative)) %>%
         ungroup(), aes(ntentative, time, color = omega)) +
  geom_point(aes(shape=method), alpha = 0.9, size = 2) +
  geom_line(aes(group=id), alpha = 0.3) +
  scale_x_continuous(trans = 'log10') + 
  scale_colour_manual(values = hex_codes1[1:7]) +
  #facet_wrap(~omega, scales = "free") +
  theme_bw() +
  xlab(c(expression("zoom for " ~ omega ~ " < 8"))) +
  ylab("") +
  theme(text = element_text(family="Times New Roman", size = 10),
        legend.position = "none") 

allNC12 <- ggplot(resultsNC12 %>%
                    filter(method!=2) %>%
                    group_by(id) %>%
                    mutate(ntentative = max(ntentative)) %>%
                    ungroup(), aes(ntentative, time, color = omega)) +
  geom_point(aes(shape=method), alpha = 0.9, size = 2) +
  geom_line(aes(group=id), alpha = 0.3) +
  scale_x_continuous(trans = 'log10') + 
  scale_colour_manual(values = hex_codes1) +
  #facet_wrap(~omega, scales = "free") +
  xlab(expression(Log[10] ~" of number of tentative solutions")) +
  ylab("Execution time in seconds") +
  scale_shape_discrete(name = "Algorithm", labels = c("ME", "ME-RCW")) +
  theme_bw() +
  theme(text = element_text(family="Times New Roman", size = 10),
        axis.title.y = element_text(margin = margin(t = 0, r = 20, b = 0, l = 0))) + 
  labs(color = expression(omega))
         
allNC12 + zoomNC12 + plot_layout(guides = "collect")

ggplot(resultsNC %>% filter(time < 1000) , aes(ntentative, time, color = omega)) +
  #geom_line(aes(group = id)) +
  geom_point(alpha = 0.9, size = 2) +
  scale_x_continuous(trans = 'log2') + 
  facet_wrap(~n, scales = "free") +
  #scale_shape_manual(values = c(22,21,18)) +
  theme_light() +
  theme(text = element_text(family="Times New Roman", size = 14)) +
  xlab("") + ylab("") + labs(color = c(expression(omega)))


as.numeric(resultsNC13 %>% summarise(min = min(time),
                          mean = mean(time),
                          median = median(time),
                          max = max(time)))
as.numeric(resultsNC14 %>% summarise(min = min(time),
                          mean = mean(time),
                          median = median(time),
                          max = max(time)))
