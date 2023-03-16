quantiles <- enframe(quantile(res_me_8$exec_time), name = "perc") %>% mutate(n = 8) %>%
  bind_rows(enframe(quantile(res_me_9$exec_time), name = "perc") %>% mutate(n = 9)) %>%
  bind_rows(enframe(quantile(res_me_10$exec_time), name = "perc") %>% mutate(n = 10)) %>%
  mutate(perc = as.factor(perc),
         n = as.factor(n))

quartiles8 <- res_me_8 %>% pull(exec_time) %>% quantile()
quartiles9 <- res_me_9 %>% pull(exec_time) %>% quantile()
quartiles10 <- res_me_10 %>% pull(exec_time) %>% quantile()

quartiles8[1] <- 0
quartiles9[1] <- 0
quartiles10[1] <- 0

times8 <- res_me_8 %>% mutate(quartile = cut(exec_time, quartiles8, labels = paste0("q", 1:4)))
times9 <- res_me_9 %>% mutate(quartile = cut(exec_time, quartiles9, labels = paste0("q", 1:4)))
times10 <- res_me_10 %>% mutate(quartile = cut(exec_time, quartiles10, labels = paste0("q", 1:4)))

times <- bind_rows(times8, times9, times10) %>% 
  mutate(basem = ifelse(m%%2==0, m, m-1),
         odd = as.factor(ifelse(m%%2==0, "yes", "no")),
         n = as.factor(n),
         m = as.factor(m),
         quartile = as.factor(quartile),
         method = NULL
  )

times 
ggplot(times, aes(x=as.numeric(m),y=exec_time,color=quartile,group=m)) + 
  geom_jitter(height = 0) +
  geom_hline(aes(yintercept = mean(exec_time))) +
  geom_hline(aes(yintercept = median(exec_time)), linetype = "dashed") +
  facet_wrap(~n, scales = "free_x") +
  coord_flip() +
  xlab("") + ylab("") +
  theme_light()
p


all_ms_for_n <- function(the_n) {
  #v <- times8 %>% mutate(quartile = cut(time, quartiles8))
  p <- ggplot(times %>% filter(n==the_n), aes(x=m,y=exec_time,color=odd)) + 
    geom_jitter(height = 0, shape = 21) +
    #geom_hline(yintercept = v[2], linetype = "dashed", color = "darkgray") + # 25%
    #geom_hline(yintercept = v[3], linetype = "dashed") + # 50%
    #geom_hline(yintercept = v[4], linetype = "dashed", color = "darkgray") + # 75%
    #geom_hline(aes(yintercept = mean(time))) +
    facet_wrap(~basem, scales = "free_x", ncol = 11) +
    theme_bw() +
    theme(panel.grid.major.x = element_blank(),
          legend.position = "none")
}
p1 <- all_ms_for_n(8) + ggtitle('n = 8')
p2 <- all_ms_for_n(9) + ggtitle('n = 9')
p3 <- all_ms_for_n(10) + ggtitle('n = 10')
p1 / p2 / p3 


# porcentajes de cada cuartil que hay para cada valor de n y m

ggplot(times %>% count(n,m,quartile), aes(m,nn,fill=quartile)) +
  geom_bar(aes(alpha = as.numeric(as.character(m))%%2==0),stat="identity", position="fill") +
  geom_text(aes(label=nn),position = position_fill(vjust = 0.5), angle = 90) +
  facet_grid(.~n) +
  geom_hline(yintercept = .75) +
  geom_hline(yintercept = .5) +
  geom_hline(yintercept = .25) +
  scale_alpha_discrete(range = c(0.6,1)) +
  theme_bw() +
  theme(legend.position = "none")


