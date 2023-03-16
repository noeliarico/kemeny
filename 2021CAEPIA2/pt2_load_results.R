# Column names for the results -------------------------------------------------
cn <- c("n","m",
        "profile",
        "method",
        "time",
        "nsolutions",
        "ntentative",
        "t1",
        "t2",
        "t3")

times8 <-   read_csv("predict_time/results/predictTime_8_10.csv",  col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))  %>%
  bind_rows(read_csv("predict_time/results/predictTime_8_11.csv",  col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_8_20.csv",  col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_8_21.csv",  col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_8_30.csv",  col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_8_31.csv",  col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_8_50.csv",  col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_8_51.csv",  col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_8_80.csv",  col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_8_81.csv",  col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_8_130.csv", col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_8_131.csv", col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_8_210.csv", col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_8_211.csv", col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_8_340.csv", col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_8_341.csv", col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_8_550.csv", col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_8_551.csv", col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_8_890.csv", col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_8_891.csv", col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) 

times9 <-   read_csv("predict_time/results/predictTime_9_10.csv",  col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))  %>%
  bind_rows(read_csv("predict_time/results/predictTime_9_11.csv",  col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_9_20.csv",  col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_9_21.csv",  col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_9_30.csv",  col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_9_31.csv",  col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_9_50.csv",  col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_9_51.csv",  col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_9_80.csv",  col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_9_81.csv",  col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_9_130.csv", col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_9_131.csv", col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_9_210.csv", col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_9_211.csv", col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_9_340.csv", col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_9_341.csv", col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_9_550.csv", col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_9_551.csv", col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_9_890.csv", col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_9_891.csv", col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) 


times10 <-  read_csv("predict_time/results/predictTime_10_10.csv",  col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))  %>%
  bind_rows(read_csv("predict_time/results/predictTime_10_11.csv",  col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_10_20.csv",  col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_10_21.csv",  col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_10_30.csv",  col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_10_31.csv",  col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_10_50.csv",  col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_10_51.csv",  col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_10_80.csv",  col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_10_81.csv",  col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_10_130.csv", col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_10_131.csv", col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_10_210.csv", col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_10_211.csv", col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_10_340.csv", col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_10_341.csv", col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_10_550.csv", col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_10_551.csv", col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_10_890.csv", col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) %>%
  bind_rows(read_csv("predict_time/results/predictTime_10_891.csv", col_names = cn) %>% mutate(dist = c(rep("unif", 1000), rep("norm", 1000)))) 

quartiles8 <- times8 %>% pull(time) %>% quantile()
quartiles9 <- times9 %>% pull(time) %>% quantile()
quartiles10 <- times10 %>% pull(time) %>% quantile()

qs <- tibble(quartiles8, quartiles9, quartiles10, value = c("min", "q2", "median", "q3", "max"))
#qs %>%
 # pivot_longer(everything())

quartiles8[1] <- 0
quartiles9[1] <- 0
quartiles10[1] <- 0

tibble()
times8 <- times8 %>% mutate(quartile = cut(time, quartiles8, labels = paste0("q", 1:4)))
times9 <- times9 %>% mutate(quartile = cut(time, quartiles9, labels = paste0("q", 1:4)))
times10 <- times10 %>% mutate(quartile = cut(time, quartiles10, labels = paste0("q", 1:4)))

times <- bind_rows(times8, times9, times10) %>% 
  mutate(basem = ifelse(m%%2==0, m, m-1),
         odd = as.factor(ifelse(m%%2==0, "yes", "no")),
         n = as.factor(n),
         m = as.factor(m),
         quartile = as.factor(quartile)
         )

times 
p <- ggplot(times %>% filter(n==10), aes(x=m,y=time,color=quartile,group=m)) + 
  geom_jitter(height = 0) +
  geom_hline(aes(yintercept = mean(time))) +
  geom_hline(aes(yintercept = median(time)), linetype = "dashed") +
  facet_wrap(~n, scales = "free_y") +
  coord_flip()
p


all_ms_for_n <- function(the_n) {
  #v <- times8 %>% mutate(quartile = cut(time, quartiles8))
  p <- ggplot(times %>% filter(n==the_n), aes(x=m,y=time,color=odd)) + 
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
  
