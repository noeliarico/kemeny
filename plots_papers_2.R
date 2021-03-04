library(readr)
cn <- c("id",
        "n",
        "omega",
        "index",
        "method",
        "time",
        "nsolutions",
        "ntentative",
        "t1",
        "t2",
        "t3")

agreements <- unlist(check_data_experiments_margin(pors8cw))
nrp <- unlist(check_data_experiments_nrp(pors8cw))
resultsCW8<- read_csv("resultsNC8cw_123.csv", skip = 1,
                       col_names = cn) %>%
  mutate(
    id = index+(5*(omega-1)),
    agreement = rep(agreements, each = 3),
    method = as.factor(method),
    omega = as.factor(omega),
    nrp = as.factor(rep(nrp, each = 3)))

agreements <- unlist(check_data_experiments_margin(pors9cw))
nrp <- unlist(check_data_experiments_nrp(pors9cw))
resultsCW9 <- read_csv("resultsNC9cw_123.csv", skip = 1,
                        col_names = cn) %>%
  mutate(
    id = index+(5*(omega-1)),
    agreement = rep(agreements, each = 3),
    method = as.factor(method),
    omega = as.factor(omega),
    nrp = as.factor(rep(nrp, each = 3)))


agreements <- unlist(check_data_experiments_margin(pors10cw))
nrp <- unlist(check_data_experiments_nrp(pors10cw))
resultsCW10 <- read_csv("resultsNC10cw_123.csv", skip = 1,
                        col_names = cn) %>%
  mutate(
    id = index+(5*(omega-1)),
    agreement = rep(agreements, each = 3),
    method = as.factor(method),
    omega = as.factor(omega),
    nrp = as.factor(rep(nrp, each = 3)))

cn <- c("id",
        "n",
        "omega",
        "index",
        "method",
        "time",
        "nsolutions",
        "ntentative",
        "t1",
        "t2",
        "t3")
agreements <- unlist(check_data_experiments_margin(pors11cw))
nrp <- unlist(check_data_experiments_nrp(pors11cw))
resultsCW11 <- read_csv("resultsNC11cw_123.csv", skip = 1,
                        col_names = cn) %>%
  mutate(
    id = index+(5*(omega-1)),
    agreement = rep(agreements, each = 3),
    method = as.factor(method),
    omega = as.factor(omega),
    nrp = as.factor(rep(nrp, each = 3)))

cn <- c("id",
        "n",
        "omega",
        "index",
        "method",
        "time",
        "nsolutions",
        "ntentative",
        "t1")
agreements <- unlist(check_data_experiments_margin(pors12cw))
agreements <- agreements[!is.na(agreements)]
nrp <- unlist(check_data_experiments_nrp(pors12cw))
nrp <- nrp[!is.na(nrp)]
resultsCW12 <- read_csv("resultsNC12cw_123.csv", skip = 1,
                        col_names = cn) %>%
  mutate(
    id = index+(5*(omega-1)),
    agreement = rep(agreements, each = 3),
    method = as.factor(method),
    omega = as.factor(omega),
    nrp = as.factor(rep(nrp, each = 3)))


resultsCW <- bind_rows(
  resultsCW8,
  resultsCW9,
  resultsCW10,
  resultsCW11,
  resultsCW12
)

resultsCW %>%
  filter(method != 3) %>%
  group_by(id,n) %>%
  mutate(diff = max(time)-min(time))

p8 <- ggplot(resultsCW %>% filter(n==8,method!=3), aes(id, time, color = omega)) +
  geom_line(aes(group = id), alpha = 0.1) +
  geom_point(aes(shape = method), size = 2) +
  facet_wrap(~n, scales = "free") +
  #scale_shape_manual(values = c(22,21,18)) +
  theme_light() +
  theme(text = element_text(family="Times New Roman", size = 14),
        axis.text.x = element_blank(),
        legend.title = element_text(size = 11),
        legend.text = element_text(size = 11)) +
  guides(shape = guide_legend(override.aes = list(size = 1.6)),
         color = guide_legend(override.aes = list(size = 1.6))) +
  scale_y_continuous(labels = function(x) paste0(x, "s")) +
  xlab("") + ylab("") +
  scale_color_manual(values = c(#"lightcyan3",
    # "orange3",
    #"plum4",
    "olivedrab3",
    "thistle3",
    "steelblue3",
    "sienna3",
    "orchid3",
    "turquoise3",
    "violetred3")) +
  guides(shape = FALSE)

p9 <- ggplot(resultsCW %>% filter(n==9,method!=3), aes(id, time, color = omega)) +
  geom_line(aes(group = id), alpha = 0.1) +
  geom_point(aes(shape = method), size = 2) +
  facet_wrap(~n, scales = "free") +
  #scale_shape_manual(values = c(22,21,18)) +
  theme_light() +
  theme(text = element_text(family="Times New Roman", size = 14),
        axis.text.x = element_blank(),
        legend.title = element_text(size = 11),
        legend.text = element_text(size = 11)) +
  guides(shape = guide_legend(override.aes = list(size = 1.6)),
         color = guide_legend(override.aes = list(size = 1.6))) +
  scale_y_continuous(labels = function(x) paste0(x, "s")) +
  xlab("") + ylab("") +
  scale_color_manual(values = c(#"lightcyan3",
                                # "orange3",
                                "plum4",
                                "olivedrab3",
                                "thistle3",
                                "steelblue3",
                                "sienna3",
                                "orchid3",
                                "turquoise3",
                                "violetred3"))  +
  guides(shape = FALSE)

p10 <- ggplot(resultsCW %>% filter(n==10,method!=3), aes(id, time, color = omega)) +
  geom_line(aes(group = id), alpha = 0.1) +
  geom_point(aes(shape = method), size = 2) +
  facet_wrap(~n, scales = "free") +
  #scale_shape_manual(values = c(22,21,18)) +
  theme_light() +
  theme(text = element_text(family="Times New Roman", size = 14),
        axis.text.x = element_blank(),
        legend.title = element_text(size = 11),
        legend.text = element_text(size = 11)) +
  guides(shape = guide_legend(override.aes = list(size = 1.6)),
         color = guide_legend(override.aes = list(size = 1.6))) +
  scale_y_continuous(labels = function(x) paste0(x, "s")) +
  xlab("") + ylab("") +
  scale_color_manual(values = c(#"lightcyan3",
    "orange3",
    "plum4",
    "olivedrab3",
    "thistle3",
    "steelblue3",
    "sienna3",
    "orchid3",
    "turquoise3",
    "violetred3")) +
  guides(shape = FALSE)



p11 <- ggplot(resultsCW %>% filter(n==11,method!=3), aes(id, time, color = omega)) +
  geom_line(aes(group = id), alpha = 0.1) +
  geom_point(aes(shape = method), size = 2) +
  facet_wrap(~n, scales = "free") +
  #scale_shape_manual(values = c(22,21,18)) +
  theme_light() +
  theme(text = element_text(family="Times New Roman", size = 14),
        axis.text.x = element_blank(),
        legend.title = element_text(size = 11),
        legend.text = element_text(size = 11)) +
  guides(shape = guide_legend(override.aes = list(size = 1.6)),
         color = guide_legend(override.aes = list(size = 1.6))) +
  scale_y_continuous(labels = function(x) paste0(x, "s")) +
  xlab("") + ylab("") +
  scale_color_manual(values = c(
    "lightcyan3",
    "orange3",
    "plum4",
    "olivedrab3",
    "thistle3",
    "steelblue3",
    "sienna3",
    "orchid3",
    "turquoise3",
    "violetred3")) +
  guides(shape = FALSE)

p12 <- ggplot(resultsCW %>% filter(n==12,method!=3), aes(id, time, color = omega)) +
  geom_line(aes(group = id), alpha = 0.1) +
  geom_point(aes(shape = method), size = 2) +
  facet_wrap(~n, scales = "free") +
  #scale_shape_manual(values = c(22,21,18)) +
  theme_light() +
  theme(text = element_text(family="Times New Roman", size = 14),
        axis.text.x = element_blank(),
        legend.title = element_text(size = 11),
        legend.text = element_text(size = 11)) +
  guides(shape = guide_legend(override.aes = list(size = 1.6)),
         color = guide_legend(override.aes = list(size = 1.6))) +
  scale_y_continuous(labels = function(x) paste0(x, "s")) +
  xlab("") + ylab("") +
  scale_color_manual(values = c(
    "lightcyan3",
    "orange3",
    "plum4",
    "olivedrab3",
    "thistle3",
    "steelblue3",
    "sienna3",
    "orchid3",
    "turquoise3",
    "violetred3")) +
  guides(shape = FALSE)

((p8+p9)/(p10+p11))

# Plot average alg2 -------------------------------------------------------

results_avg <- resultsCW %>% 
  mutate(n = as.factor(n)) %>%
  group_by(n, method, omega) %>%
  summarise(meantime = mean(time), 
            #agreement = mean(agreement),
            #nsolutions = mean(nsolutions),
            # ntentative = mean(ntentative), ests no porque cambian dependiendo dle método
            .groups = "drop") %>%
  pivot_wider(names_from = method, values_from = meantime, names_prefix = "alg") %>%
  mutate(perc2 = alg2/alg1,
         perc3 = alg3/alg1,
         perc1 = 1) %>%
  select(n, omega, starts_with("perc")) %>%
  pivot_longer(-c(n,omega), names_to = "method", values_to = "perc") %>%
  mutate(method = recode(method, perc3 = "MorkExact3", perc2 = "MorkExact2", perc1 = "MorkExact1"))
# ntentative = ntentative/factorial(n))

ggplot(results_avg, aes(omega)) +
  #geom_text(aes(x=n,y=perc,label=paste0(round(perc1,2)*100,"%")), vjust = -.5, size = 3.5) +
  geom_bar(aes(weight = perc, fill = method), 
           position = "identity",
           alpha = 0.5, color = "black") +
  scale_fill_manual(values=c("#d0e8f2","#79a3b1","black")) +
  facet_wrap(~n, scales = "free_x") +
  theme_light() +
  theme(text = element_text(family="Times New Roman", size = 14),
        legend.position = "bottom") +
  xlab("") + ylab("") + 
  scale_y_continuous(breaks = seq(0,1,.25), labels =paste0(seq(0,100,25), "%"), limits = c(0,1.1))

# Percentage of reduction: average results by method and n (alg2) --------------

results_avg <- resultsCW %>% 
  group_by(n, method, omega) %>%
  summarise(meantime = mean(time), .groups = "drop") %>%
  group_by(n, method) %>%
  summarise(meantime = mean(meantime), .groups = "drop") %>%
  pivot_wider(names_from = method, values_from = meantime, names_prefix = "alg") %>%
  mutate(perc = alg2/alg1,
         perc_full = 1) %>%
  pivot_longer(-c(n, starts_with("alg")), names_to = "method", values_to = "perc") %>%
  mutate(method = recode(method, perc = "MorkExact2", perc_full = "MorkExact1")) %>%
  mutate(time = ifelse(method == "MorkExact2", alg2, alg1)) %>%
  select(!starts_with("alg"))

ggplot(results_avg %>% filter(n!=12), aes(n)) +
  #geom_text(aes(x=n,y=perc,label=paste0(round(perc,2)*100,"%")), vjust = -.5, size = 3.5) +
  geom_text(aes(x=n,y=perc,label=paste(round(time, 3), "s")), 
            vjust = -.5, size = 4.5, family = "Times New Roman") +
  geom_bar(aes(weight = perc, fill = method), 
           position = "identity",
           alpha = 0.5, color = "black") +
  scale_fill_manual(values=c("#d0e8f2","#79a3b1")) +
  theme_light() +
  theme(text = element_text(family="Times New Roman", size = 14),
        legend.position = "bottom") +
  xlab("") + ylab("") + 
  scale_y_continuous(breaks = seq(0,1,.25), labels =paste0(seq(0,100,25), "%"), limits = c(0,1.1))


# Percentage of reduction: average results by method and n (alg2 and alg3) -----

results_avg <- resultsCW %>% 
  group_by(n, method, omega) %>%
  summarise(meantime = mean(time), .groups = "drop") %>%
  group_by(n, method) %>%
  summarise(meantime = mean(meantime), .groups = "drop") %>%
  pivot_wider(names_from = method, values_from = meantime, names_prefix = "alg") %>%
  mutate(perc2 = alg2/alg1,
         perc3 = alg3/alg1,
         perc_full = 1) %>%
  pivot_longer(-c(n, starts_with("alg")), names_to = "method", values_to = "perc") %>%
  mutate(method = recode(method, perc3 = "MorkExact3", perc2 = "MorkExact2", perc_full = "MorkExact1")) %>%
  mutate(time = ifelse(method == "MorkExact2", alg2, ifelse(method == "MorkExact3", alg3, alg1))) %>%
  select(!starts_with("alg"))

ggplot(results_avg %>% filter(n!=12), aes(n)) +
  #geom_text(aes(x=n,y=perc,label=paste0(round(perc,2)*100,"%")), vjust = -.5, size = 3.5) +
  geom_text(aes(x=n,y=perc,label=paste(round(time, 3), "s")), 
            vjust = -.5, size = 4.5, family = "Times New Roman") +
  geom_bar(aes(weight = perc, fill = method), 
           position = "identity",
           alpha = 0.5, color = "black") +
  scale_fill_manual(values=c("#d0e8f2","#79a3b1","black")) +
  theme_light() +
  theme(text = element_text(family="Times New Roman", size = 14),
        legend.position = "bottom") +
  xlab("") + ylab("") + 
  scale_y_continuous(breaks = seq(0,1,.25), labels =paste0(seq(0,100,25), "%"), limits = c(0,1.1))

