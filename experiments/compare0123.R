# Condorcet ranking -------------------------------------------------------

library(readr)
cn <- c("id",
        "n",
        "omega",
        "index",
        "method",
        "time",
        "nsolutions",
        "ntentative",
        "cond_win",
        "t1",
        "t2",
        "t3")
results10 <- read_csv("experiments/results/results10cr_azzini.csv", skip = 1,
                    col_names = cn) %>%
  mutate(
    id = id%/%4,
    method = as.factor(method),
    omega = as.factor(omega))
results11 <- read_csv("experiments/results/results11cr_azzini.csv", skip = 1,
                      col_names = cn) %>%
  mutate(
    id = id%/%4,
    method = as.factor(method),
    omega = as.factor(omega))
results12 <- read_csv("experiments/results/results12cr_azzini.csv", skip = 1,
                      col_names = cn) %>%
  mutate(
    id = id%/%4,
    method = as.factor(method),
    omega = as.factor(omega))

results <- bind_rows(
  results10,
  results11,
  results12
)

resultss2 <- results %>% filter(method != 2)
resultss3 <- results %>% filter(method != 3)

# Comparación general
ggplot(resultss3 %>% filter(time < 60), aes(id, time, color = method, group = id)) +
  geom_line(color = "black") +
  scale_size(range = c(.1, 3)) +
  geom_point(size = 1.5) +
  facet_grid(n~omega, scales = "free")

# Condorcet winner -------------------------

results11cw <- read_csv("experiments/results/results11cw_azzini.csv", skip = 1,
                        col_names = cn) %>%
  mutate(
    id = id%/%4,
    method = as.factor(method),
    omega = as.factor(omega))


ggplot(results11cw %>% filter(method != 3), aes(id, time, color = method, group = id)) +
  geom_line(color = "black") +
  scale_size(range = c(.1, 3)) +
  geom_jitter(size = 2, alpha = 0.6, width = 0.2, height = 0) +
  facet_wrap(~omega, scales="free")


# No Condorcet ------------------------------------------------------------

results10nc <- read_csv("experiments/results/results10_azzini.csv", skip = 1,
                        col_names = cn) %>%
  mutate(
    id = id%/%4,
    method = as.factor(method),
    omega = as.factor(omega))

ggplot(results10nc %>% filter(method != 3), aes(id, time, color = method, group = id)) +
  geom_line(color = "black") +
  scale_size(range = c(.1, 3)) +
  geom_jitter(size = 2, alpha = 0.6, width = 0.2, height = 0) +
  facet_wrap(~omega, scales="free")

# Prune ----------------------

ggplot(results11cw %>% filter(method != 2), aes(id, time, color = method, group = id)) +
  geom_line(color = "black") +
  scale_size(range = c(.1, 3)) +
  geom_jitter(size = 2, alpha = 0.6, width = 0.2, height = 0) +
  facet_wrap(~omega, scales="free")

ggplot(results10nc %>% filter(method != 2), aes(id, time, color = method, group = id)) +
  geom_line(color = "black") +
  scale_size(range = c(.1, 3)) +
  geom_jitter(size = 2, alpha = 0.6, width = 0.2, height = 0) +
  facet_wrap(~omega, scales="free")
