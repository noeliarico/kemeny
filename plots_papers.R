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

agreements <- unlist(check_data_experiments_margin(pors8nc))
resultsNC8 <- read_csv("resultsNC8nc_123.csv", skip = 1,
                          col_names = cn) %>%
  mutate(
    id = index+(5*(omega-1)),
    agreement = rep(agreements, each = 3),
    method = as.factor(method),
    omega = as.factor(omega))
agreements <- unlist(check_data_experiments_margin(pors9nc))
resultsNC9 <- read_csv("resultsNC9nc_123.csv", skip = 1,
                       col_names = cn) %>%
  mutate(
    id = index+(5*(omega-1)),
    agreement = rep(agreements, each = 3),
    method = as.factor(method),
    omega = as.factor(omega))

resultsNC <- bind_rows(
  resultsNC8,
  resultsNC9
)

ggplot(resultsNC, aes(agreement, time)) +
  geom_line(aes(color = omega, group = id)) +
  geom_point(size = 2, aes(color = omega, shape = method), stroke = .5) +
  facet_wrap(~n, scales = "free") +
  scale_shape_manual(values = c(22,21,18))
