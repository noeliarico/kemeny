rep <- 10
cn <- c("id",
        "n",
        "omega",
        "index",
        "method",
        "time",
        "nsolutions",
        "ntentative",
        paste0("t",(1:rep)))
res8 <- read_csv("experiments/results/cwsinyconrec8prueba_azzini.csv",
                  col_names = cn, skip = 1) %>%
  mutate(method = as.factor(method),
         id = as.factor(id%/%2))
rep <- 3
cn <- c("id",
        "n",
        "omega",
        "index",
        "method",
        "time",
        "nsolutions",
        "ntentative",
        paste0("t",(1:rep)))
res9 <- read_csv("experiments/results/cwsinyconrec9prueba_azzini.csv",
                  col_names = cn, skip = 1) %>%
  mutate(method = as.factor(method),
         id = as.factor(id%/%2))
res10 <- read_csv("experiments/results/cwsinyconrec10prueba_azzini.csv",
                  col_names = cn, skip = 1) %>%
  mutate(method = as.factor(method),
         id = as.factor(id%/%2))
res11 <- read_csv("experiments/results/cwsinyconrec11prueba_azzini.csv",
                  col_names = cn, skip = 1) %>%
  mutate(method = as.factor(method),
         id = as.factor(id%/%2))

res12 <- read_csv("experiments/results/cwsinyconrec11prueba_azzini.csv",
                  col_names = cn, skip = 1) %>%
  mutate(method = as.factor(method),
         id = as.factor(id%/%2))

res <- res8[,1:11] %>%
  bind_rows(res9) %>%
  bind_rows(res10) %>%
  bind_rows(res11) %>%
  bind_rows(res12) %>%
  mutate(id2 = paste0(n+as.numeric(id)))

# RES09 -------------------------------------------------------------------

# Crecimiento del tiempo de ejecución cuando aumenta la n. No se ve la
# comparación entre los métodos
ggplot(res9, aes(id, time, color = method, group = id)) +
  geom_line(aes(size = ntentative), color = "black") +
  scale_size(range = c(.1, 3)) +
  geom_point(size = 2.5) +
  facet_wrap(~omega,  ncol = 9, scales = "free_x")

# Liberar los ejes de la escala para ver la comparación entre los métodos
ggplot(res9, aes(id, time, color = method, group = id)) +
  geom_line(aes(size = ntentative), color = "black") +
  scale_size(range = c(.1, 3)) +
  geom_point(size = 2.5) +
  facet_wrap(~omega, scales = "free", ncol = 9)

# RES10 -------------------------------------------------------------------

# Crecimiento del tiempo de ejecución cuando aumenta la n. No se ve la
# comparación entre los métodos
ggplot(res10, aes(id, time, color = method, group = id)) +
  geom_line(aes(size = ntentative), color = "black") +
  scale_size(range = c(.1, 3)) +
  geom_point(size = 2.5) +
  facet_wrap(~omega,  ncol = 10, scales = "free_x")

# Liberar los ejes de la escala para ver la comparación entre los métodos
ggplot(res10, aes(id, time, color = method, group = id)) +
  geom_line(aes(size = ntentative), color = "black") +
  scale_size(range = c(.1, 2)) +
  geom_point(size = 2.5) +
  facet_wrap(~omega, scales = "free", ncol = 10)

# RES11 -------------------------------------------------------------------

# Crecimiento del tiempo de ejecución cuando aumenta la n. No se ve la
# comparación entre los métodos
ggplot(res11, aes(id, time, color = method, group = id)) +
  geom_line(aes(size = ntentative), color = "black") +
  scale_size(range = c(.1, 3)) +
  geom_point(size = 2.5) +
  facet_wrap(~omega,  ncol = 10, scales = "free_x")

# Liberar los ejes de la escala para ver la comparación entre los métodos
ggplot(res11, aes(id, time, color = method, group = id)) +
  geom_line(aes(size = ntentative), color = "black") +
  scale_size(range = c(.1, 2)) +
  geom_point(size = 2.5) +
  facet_wrap(~omega, scales = "free", ncol = 10)

# RES12 -------------------------------------------------------------------

# Crecimiento del tiempo de ejecución cuando aumenta la n. No se ve la
# comparación entre los métodos
ggplot(res12, aes(id, time, color = method, group = id)) +
  geom_line(aes(size = ntentative), color = "black") +
  scale_size(range = c(.1, 3)) +
  geom_point(size = 2.5) +
  facet_wrap(~omega,  ncol = 10, scales = "free_x")

# Liberar los ejes de la escala para ver la comparación entre los métodos
ggplot(res12, aes(id, time, color = method, group = id)) +
  geom_line(aes(size = ntentative), color = "black") +
  scale_size(range = c(.1, 2)) +
  geom_point(size = 2.5) +
  facet_wrap(~omega, scales = "free", ncol = 10)


# Average by omega ----------------------------------------------------------

res_by_omega <- res %>%
  group_by(n, omega, method) %>%
  summarise(maxsol = max(nsolutions),
            minsol = min(nsolutions),
            maxten = max(ntentative),
            minten = min(ntentative),
            avgtime = mean(time))

# Increase of the average time when omega increases
ggplot(res_by_omega, aes(omega, avgtime, color = method)) +
  geom_line() +
  geom_point() +
  facet_wrap(~n, ncol = 4)
# Zoom
ggplot(res_by_omega, aes(omega, avgtime, color = method)) +
  geom_line() +
  geom_point() +
  facet_wrap(~n, ncol = 4, scales = "free")


# Average by n ----------------------------------------------------------

res_by_n <- res %>%
  group_by(n, method) %>%
  summarise(maxsol = max(nsolutions),
            minsol = min(nsolutions),
            maxten = max(ntentative),
            minten = min(ntentative),
            avgtime = mean(time))

# Increase of the average time when omega increases
ggplot(res_by_n, aes(n, avgtime, color = method)) +
  geom_line() +
  geom_point()
# Zoom
ggplot(res_by_omega, aes(omega, avgtime, color = method)) +
  geom_line() +
  geom_point() +
  facet_wrap(~n, ncol = 4, scales = "free")

ggplot(res_by_omega, aes(omega, avgtime, color = method)) +
  geom_line() +
  geom_point() +
  transition_reveal(method)

# Difference time ---------------------------------------------------------

res_time_dif <- res %>%
  select(n, omega, method, time) %>%
  group_by(n, omega, method) %>%
  mutate(avgtime = mean(time)) %>%
  ungroup() %>%
  group_by(n, omega) %>%
  summarise(max = max(avgtime),
            min = min(avgtime),
            diff = max(avgtime) - min(avgtime))

ggplot(res_time_dif %>% mutate(n=as.factor(n)), aes(omega, diff, col = n)) +
  geom_point() +
  geom_line()
# Zoom
ggplot(res_time_dif %>% mutate(n=as.factor(n)), aes(omega, diff, col = n)) +
  geom_point() +
  geom_line() +
  stat_mean_line(color="grey", linetype="dashed") +
  facet_wrap(~n, scales = "free")

# Comportamiento raro en 8
res %>% filter(n==8, omega==7) # es por el cuarto