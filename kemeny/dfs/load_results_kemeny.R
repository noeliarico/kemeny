library(tidyverse)

results_kemeny <- read_csv("kemeny/results_kemeny.csv",
col_names = c('n','seed','i1','i2','i3','i4','i5','tk','tb','dk','db','winners'))
results_kemeny2 <- results_kemeny %>% pivot_longer(cols = c(tk, tb), names_to = "method", values_to = "time") %>% mutate(method = as.factor(method))

winners <- results_kemeny2 %>% 
  pull(winners) %>% 
  str_remove_all("\\[") %>% 
  str_remove_all("\\]") %>% 
  str_split(" ")
winners <- lapply(winners, as.numeric)
nwr <- sapply(winners, length)
firstw <- sapply(winners, min)
results_kemeny2 <- results_kemeny2 %>% mutate(nwr = nwr,
                                              fw = as.factor(firstw))

results_kemeny2 <- results_kemeny2 %>% mutate(minagree = 5*((n*(n-1))/2),
                                              maxagree = 10*((n*(n-1))/2),
                                              i6 = (i3-minagree)/(maxagree-minagree))

results_kemeny2 <- results_kemeny2 %>% group_by(n) %>% 
  mutate(avgi6 = median(i6)) %>% ungroup() %>% 
  mutate(level = ifelse(i6 < avgi6, 0, 1))


colors <- c(
  "#a4a8c3",
  "#9095b5",
  "#7b81a8",
  "#676e9a",
  "#595f86",
  "#4b5172",
  "#3e425d",
  "#373b53",
  "#303449",
  "#2a2c3f",
  "#232534",
  "#1c1e2a")

ids <- sort(rep(1:(nrow(results_kemeny2)/2), 2))
results_kemeny2 <- results_kemeny2 %>% mutate(id = ids)

# Plot incertidumbre
ggplot(results_kemeny2 %>% 
         mutate(method = fct_recode(method, worst = "tk", borda = "tb")) %>%
         rename(`Best alternative` = "fw"), aes(i6, time, shape = method, color = `Best alternative`)) + 
  geom_point(size = 2, alpha = 0.9) +
  geom_line(aes(group = id)) +
  facet_wrap(n~., scales = "free_y", ncol = 5) +
  scale_shape_manual(values = c(1, 19)) +
  scale_color_manual(values = colors) +
  theme_light() +
  guides(color = guide_legend(title.position = "top")) +
  # theme(legend.direction = "horizontal", 
  #       legend.position = c(1,0),
  #       legend.justification = c(1,0),
  #       legend.box.just = "top") +
  theme(legend.position = "bottom") + 
  theme(text = element_text(family="Times New Roman", size = 20)) +
  xlab("") + ylab("")



# Plot barras completo

rtoplot <- results_kemeny2 %>% 
  group_by(n, method) %>%
  summarise(meantime = mean(time)) %>%
  ungroup() %>%
  group_by(n) %>%
  mutate(max = max(meantime)) %>%
  ungroup() %>%
  mutate(perc = ifelse(max == meantime, 1, meantime/max),
         method = fct_relevel(method, "tk"),
         method = fct_recode(method, worst = "tk", borda = "tb"))

ggplot(rtoplot, aes(n)) +
  geom_bar(aes(weight = perc, fill = method), position = "identity", color = "black") +
  geom_hline(yintercept=0.9, linetype="dashed", color = "black", alpha = 0.5) +
  geom_text(aes(x=n,y=perc,label=round(meantime,2)), vjust = -.5, size = 3.5) +
  #scale_fill_manual(values=c("#79a3b1","#d0e8f2")) +
  scale_fill_manual(values=c("#d0e8f2","#79a3b1")) +
  theme_light() +
  theme(text = element_text(family="Times New Roman", size = 14)) +
  xlab("") + ylab("") + 
  scale_y_continuous(breaks = seq(0,1,.25), labels =paste0(seq(0,100,25), "%"), limits = c(0,1.1))
  

# Exponential execution time

rtoplot <- results_kemeny2 %>% 
  group_by(n, method) %>%
  summarise(meantime = mean(time)) %>%
  ungroup() %>%
  group_by(n) %>%
  mutate(max = max(meantime)) %>%
  ungroup() %>%
  mutate(perc = ifelse(max == meantime, 1, meantime/max),
         method = fct_recode(method, worst = "tk", borda = "tb"))

ggplot(rtoplot, aes(n)) +
  geom_bar(aes(weight = meantime, fill = method), 
           position = "dodge", 
           color = "black") +
  geom_hline(yintercept = 60*1, linetype = "dashed", alpha = 0.3) +
  geom_hline(yintercept = 60*2, linetype = "dashed", alpha = 0.3) +
  geom_hline(yintercept = 60*3, linetype = "dashed", alpha = 0.3) +
  geom_hline(yintercept = 60*4, linetype = "dashed", alpha = 0.3) +
  geom_hline(yintercept = 60*5, linetype = "dashed", alpha = 0.3) +
  geom_hline(yintercept = 60*6, linetype = "dashed", alpha = 0.3) +
  geom_hline(yintercept = 60*7, linetype = "dashed", alpha = 0.3) +
  geom_hline(yintercept = 60*8, linetype = "dashed", alpha = 0.3) +
  geom_hline(yintercept = 60*9, linetype = "dashed", alpha = 0.3) +
  # scale_fill_manual(values=c("#E69F00","#999999")) + # orange
  scale_fill_manual(values=c("#79a3b1","#d0e8f2")) +
  # scale_fill_manual(values=c("#d0e8f2","#79a3b1")) +
  coord_flip() +
  theme_light() +
  theme(text = element_text(family="Times New Roman", size = 16)) +
  xlab("") + ylab("") + guides(fill = guide_legend(reverse=TRUE))


# Summary ----------------------------------------------------------------------

results_kemeny2 %>% group_by(n) %>% count()
results_kemeny2 %>% group_by(n,level) %>% count()

results_kemeny2 %>%
  group_by(n, method) %>%
  mutate(min = min(time),
        max = max(time)) %>%
  ungroup() %>%
  group_by(n, method, min, max) %>%
  summarise(time = mean(time)) %>%
  ungroup() %>%
  group_by(n) %>%
  mutate(diff = max(time) - min(time)) %>%
  ungroup() %>%
  xtable()

# Incertidumbre

i6 <- function(om) {
  nvoters <- om[1,2]+om[2,1]
  elem <- sum(pmax(nvoters-om[upper.tri(om, diag = FALSE)],om[upper.tri(om, diag = FALSE)]))
  n <- ncol(om)
  max <- nvoters*((n*(n-1))/2)
  min <- (nvoters/2)*((n*(n-1))/2)
  return((elem-min)/(max-min))
}


# Diferencia

results_kemeny2 %>%
  group_by(id) %>%
  mutate(maxtime = max(time))

ggplot(results_kemeny2 %>% 
         filter(n==12) %>% 
         group_by(id) %>%
         mutate(maxtime = max(time),
                mintime = min(time),
                diff = max(time) - min(time)) %>%
         ungroup() %>%
         mutate(discret1 =  cut_number(i6, n = 10),
                discret2 =  cut_number(maxtime, n = 5)), aes(i6, time)) +
  geom_line(aes(group = id), alpha = 0.5) +
  geom_point(aes(color = fw, shape = method)) +
  facet_wrap(.~discret1, scales = "free") +
  scale_color_manual(values = colors)
