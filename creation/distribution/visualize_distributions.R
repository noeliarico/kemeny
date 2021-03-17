# Color palettes ----------------------------------------------------------

blues <- c(
  "#054a91",
  "#3e7cb1",
  "#81a4cd",
  "#dbe4ee")

reds <- c(
  "#4f000b",
  "#720026",
  "#ce4257")

fina <- c(
  "#eff9f0",
  "#ddc8c4",
  "#896a67",
  "#6b4d57",
  "#13070c")


# Plot for individual -----------------------------------------------------

individual_profiles <- rpors25unif

ggplot(individual_profiles$results, aes(omega, times, fill = type)) +
  geom_bar(stat="identity", color = "black") +
  facet_wrap(~n, scales = "free_x") +
  theme_linedraw() +
  scale_fill_manual(values = c("#383D3B","#EEE5E9","#7C7C7C", "white"))

ggplot(individual_profiles$prop, aes(n, times, fill = type)) +
  geom_bar(stat="identity", color = "black") +
  geom_hline(aes(yintercept = 5000*3/4), color = "white", linetype = "dashed") +
  geom_hline(aes(yintercept = 5000/2), color = "white", linetype = "dashed") +
  geom_hline(aes(yintercept = 5000/4), color = "white", linetype = "dashed") +
  theme_classic() +
  #facet_wrap(~m, ncol = 2) +
  #scale_fill_manual(values = blues) + 
  scale_y_continuous(n.breaks = 10)


# Plot for all the values of m --------------------------------------------

propsNorm <- bind_rows(
  rpors10norm$prop %>% mutate(total = rpors10norm$total, m = 10),
  rpors25norm$prop %>% mutate(total = rpors25norm$total, m = 25), 
  rpors40norm$prop %>% mutate(total = rpors40norm$total, m = 40), 
  rpors55norm$prop %>% mutate(total = rpors55norm$total, m = 55), 
  rpors70norm$prop %>% mutate(total = rpors70norm$total, m = 70), 
  rpors85norm$prop %>% mutate(total = rpors85norm$total, m = 85), 
  rpors100norm$prop %>% mutate(total = rpors100norm$total, m = 100),
  rpors125norm$prop %>% mutate(total = rpors125norm$total, m = 125),
  rpors200norm$prop %>% mutate(total = rpors200norm$total, m = 200),
  rpors225norm$prop %>% mutate(total = rpors225norm$total, m = 225)
) %>% ungroup() %>% mutate(m=as.factor(m))

propsUnif <- bind_rows(
  rpors10unif$prop %>% mutate(total = rpors10unif$total, m = 10),
  rpors25unif$prop %>% mutate(total = rpors25unif$total, m = 25), 
  rpors40unif$prop %>% mutate(total = rpors40unif$total, m = 40), 
  rpors55unif$prop %>% mutate(total = rpors55unif$total, m = 55),
  rpors70unif$prop %>% mutate(total = rpors70unif$total, m = 70), 
  rpors85unif$prop %>% mutate(total = rpors85unif$total, m = 85), 
  rpors100unif$prop %>% mutate(total = rpors100unif$total, m = 100),
  rpors125unif$prop %>% mutate(total = rpors125unif$total, m = 125),
  rpors200unif$prop %>% mutate(total = rpors200unif$total, m = 200),
  rpors225unif$prop %>% mutate(total = rpors225unif$total, m = 225)
) %>% ungroup() %>% mutate(m=as.factor(m))

props <- bind_rows(
  propsNorm %>% mutate(distribution = "norm"),
  propsUnif %>% mutate(distribution = "unif")
) %>% mutate(distribution=as.factor(distribution))

ggplot(props, aes(n, times, fill = type)) +
  geom_bar(stat="identity", color = "black") +
  geom_hline(aes(yintercept = 5000*3/4), color = "white", linetype = "dashed") +
  geom_hline(aes(yintercept = 5000/2), color = "white", linetype = "dashed") +
  geom_hline(aes(yintercept = 5000/4), color = "white", linetype = "dashed") +
  theme_classic() +
  facet_grid(m~distribution) +
  scale_fill_manual(values = blues) + 
  scale_y_continuous(n.breaks = 10)


# Solo para ds concretas

detailsNorm <- bind_rows(
  rpors10norm$details ,
  rpors25norm$details ,
  rpors40norm$details ,
  rpors55norm$details ,
  rpors70norm$details ,
  rpors85norm$details ,
  rpors100norm$details,
  rpors125norm$details,
  rpors200norm$details,
  rpors225norm$details
) 

detailsUnif <- bind_rows(
  rpors10unif$details ,
  rpors25unif$details ,
  rpors40unif$details ,
  rpors55unif$details ,
  rpors70unif$details ,
  rpors85unif$details ,
  rpors100unif$details,
  rpors125unif$details,
  rpors200unif$details,
  rpors225unif$details
) 

details <- bind_rows(
  detailsNorm %>% mutate(distribution = "norm"),
  detailsUnif %>% mutate(distribution = "unif")
) %>% mutate(distribution=as.factor(distribution))

ggplot(details %>%
          group_by(n,w,d,type,m,distribution) %>%
          summarise(times = n(), .groups = "drop") %>%
          filter(d==2), 
        aes(n, times, fill = type)) + 
  #geom_bar() + 
  geom_bar(stat="identity") +
  facet_grid(m~distribution, scales = "free_y") +
  theme_classic() +
  scale_fill_manual(values = blues)

ggplot(props %>% filter(type == "cw") %>%
         filter(!(n==5&m==125))  %>% 
         filter(!(n==5&m==200))  %>% 
         filter(!(n==5&m==225)) %>% 
         mutate(votes = as.factor(ifelse(as.numeric(m)%%2==0, 0, 1))), 
       aes(n, times, 
           group=m)) +
  geom_point(aes(shape=votes, color = m)) +
  geom_line(aes(color = m), alpha = 0.7) +
  geom_hline(aes(yintercept = 5000*3/4, ), color = "black", linetype = "dashed") +
  geom_hline(aes(yintercept = 5000/2), color = "black", linetype = "dashed") +
  geom_hline(aes(yintercept = 5000/4), color = "black", linetype = "dashed") +
  theme_minimal() +
  scale_shape(guide = FALSE) +
  scale_y_continuous(limits = c(0,5000)) +
  scale_color_brewer(palette="PRGn") 


