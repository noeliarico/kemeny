cn <- c("n","omega","index","method","time","nsolutions","ntentative")

pors <- pors12nc[3:10]
d <- unlist(check_data_experiments_distinct(pors))
data <- read_delim("resultsU.csv",
                          col_names = cn, delim = " ") %>%
  filter(method == 1) %>%
  mutate(
    method = NULL,
    id = 1:40,
    omega = as.factor(omega),
    d = as.factor(d)
  )

u1 <- unlist(check_data_experiments_u(pors, d1))
u2 <- unlist(check_data_experiments_u(pors, d2))
u3 <- unlist(check_data_experiments_u(pors, d7))
u4 <- unlist(check_data_experiments_u(pors, d11))
u5 <- unlist(check_data_experiments_u(pors, d12))
u6 <- unlist(check_data_experiments_u(pors, d13))

data <- data %>%
  mutate(
    u1 = u1,
    u2 = u2,
    u3 = u3,
    u4 = u4,
    u5 = u5,
    u6 = u6
  )

ggplot(data, aes(id, time)) +
  geom_point() +
  facet_wrap(~omega, scale = "free")

p <- ggplot(data, aes(id, time, 
                      label1 = u1, 
                      label2 = u2,
                      label3 = u3,
                      label4 = u4,
                      label5 = u5,
                      label6 = u6)) +
  geom_point(aes(color = omega, size = d)) +
  geom_text(aes(label = index)) +
  theme_bw()
  #facet_wrap(~omega, scale = "free")
ggplotly(p)

p <- ggplot(data, aes(id, time, label = d8)) +
  geom_point(aes(color = omega, size = d)) +
  geom_text(aes(label = index)) +
  facet_wrap(~omega, scale = "free")+
  theme_bw()
#facet_wrap(~omega, scale = "free")
ggplotly(p)


save(data, pors12nc, file = "paraElHtml.RData")