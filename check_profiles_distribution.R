get_dists <- function(m, nrankings = 5000) {
  
max_iter <- nrankings/m

r4 <- create_profiles_count(4,25,max_iter = max_iter)
r5 <- create_profiles_count(5,25,max_iter = max_iter)
r6 <- create_profiles_count(6,25,max_iter = max_iter)
r7 <- create_profiles_count(7,25,max_iter = max_iter)
r8 <- create_profiles_count(8,25,max_iter = max_iter)
r9 <- create_profiles_count(9,25,max_iter = max_iter)
r10 <- create_profiles_count(10,25,max_iter = max_iter)
r11 <- create_profiles_count(11,25,max_iter = max_iter)
r12 <- create_profiles_count(12,25,max_iter = max_iter)
r13 <- create_profiles_count(13,25,max_iter = max_iter)
r14 <- create_profiles_count(14,25,max_iter = max_iter)
r15 <- create_profiles_count(15,25,max_iter = max_iter)
# r16 <- create_profiles_count(16,15,max_iter = 100)
# r17 <- create_profiles_count(17,15,max_iter = 100)
# r18 <- create_profiles_count(18,15,max_iter = 100)

res4 <- r4 %>% 
  as_tibble(rownames = "type") %>% 
  pivot_longer(-type, names_to = "omega", values_to = "times") %>% 
  mutate(omega = as.factor(str_remove(omega, "w")),
         n = 4)
res5 <- r5 %>% 
  as_tibble(rownames = "type") %>% 
  pivot_longer(-type, names_to = "omega", values_to = "times") %>% 
  mutate(omega = as.factor(str_remove(omega, "w")),
         n = 5)
res6 <- r6 %>% 
  as_tibble(rownames = "type") %>% 
  pivot_longer(-type, names_to = "omega", values_to = "times") %>% 
  mutate(omega = as.factor(str_remove(omega, "w")),
         n = 6)
res7 <- r7 %>% 
  as_tibble(rownames = "type") %>% 
  pivot_longer(-type, names_to = "omega", values_to = "times") %>% 
  mutate(omega = as.factor(str_remove(omega, "w")),
         n = 7)
res8 <- r8 %>% 
  as_tibble(rownames = "type") %>% 
  pivot_longer(-type, names_to = "omega", values_to = "times") %>% 
  mutate(omega = as.factor(str_remove(omega, "w")),
         n = 8)
res9 <- r9 %>% 
  as_tibble(rownames = "type") %>% 
  pivot_longer(-type, names_to = "omega", values_to = "times") %>% 
  mutate(omega = as.factor(str_remove(omega, "w")),
         n = 9)
res10 <- r10 %>% 
  as_tibble(rownames = "type") %>% 
  pivot_longer(-type, names_to = "omega", values_to = "times") %>% 
  mutate(omega = as.factor(str_remove(omega, "w")),
         n = 10)
res11 <- r11 %>% 
  as_tibble(rownames = "type") %>% 
  pivot_longer(-type, names_to = "omega", values_to = "times") %>% 
  mutate(omega = as.factor(str_remove(omega, "w")),
         n = 11)
res12 <- r12 %>% 
  as_tibble(rownames = "type") %>% 
  pivot_longer(-type, names_to = "omega", values_to = "times") %>% 
  mutate(omega = as.factor(str_remove(omega, "w")),
         n = 12)
res13 <- r13 %>% 
  as_tibble(rownames = "type") %>% 
  pivot_longer(-type, names_to = "omega", values_to = "times") %>% 
  mutate(omega = as.factor(str_remove(omega, "w")),
         n = 13)
res14 <- r14 %>% 
  as_tibble(rownames = "type") %>% 
  pivot_longer(-type, names_to = "omega", values_to = "times") %>% 
  mutate(omega = as.factor(str_remove(omega, "w")),
         n = 14)
res15 <- r15 %>% 
  as_tibble(rownames = "type") %>% 
  pivot_longer(-type, names_to = "omega", values_to = "times") %>% 
  mutate(omega = as.factor(str_remove(omega, "w")),
         n = 15)
# res16 <- r16 %>% 
#   as_tibble(rownames = "type") %>% 
#   pivot_longer(-type, names_to = "omega", values_to = "times") %>% 
#   mutate(omega = as.factor(str_remove(omega, "w")),
#          n = 16)
# res17 <- r17 %>% 
#   as_tibble(rownames = "type") %>% 
#   pivot_longer(-type, names_to = "omega", values_to = "times") %>% 
#   mutate(omega = as.factor(str_remove(omega, "w")),
#          n = 17)
# res18 <- r18 %>% 
#   as_tibble(rownames = "type") %>% 
#   pivot_longer(-type, names_to = "omega", values_to = "times") %>% 
#   mutate(omega = as.factor(str_remove(omega, "w")),
#          n = 18)

results <- bind_rows(
  res4 ,
  res5 ,
  res6 ,
  res7 ,
  res8 ,
  res9 ,
  res10,
  res11,
  res12,
  res13,
  res14,
  res15#,
  # res16,
  # res17,
  # res18
) %>% 
  mutate(n = as.factor(n),
         type = as.factor(type))


prop <- results %>%
  mutate(type = ifelse(as.character(type) == "cr", "cw", as.character(type))) %>%
  group_by(type, n) %>% 
  summarise(times = sum(times)) %>%
  mutate(type = as.factor(type))
# plot
ggplot(results %>% filter(n %in% 1:15), aes(omega, times, fill = type)) +
  geom_bar(stat="identity", color = "black") +
  facet_wrap(~n, scales = "free_x") +
  theme_linedraw() +
  scale_fill_manual(values = c("#383D3B","#EEE5E9","#7C7C7C"))

ggplot(prop %>% filter(n %in% 1:15), aes(n, times, fill = type)) +
  geom_bar(stat="identity", color = "black") +
  geom_hline(yintercept = sum(r15)*3/4, color = "gray", linetype = "dashed") +
  geom_hline(yintercept = sum(r15)/2, color = "gray", linetype = "dashed") +
  geom_hline(yintercept = sum(r15)/4, color = "gray", linetype = "dashed") +
  theme_linedraw() +
  scale_fill_manual(values = c("#EEE5E9","#7C7C7C")) + 
  scale_y_continuous(n.breaks = 10)
  #scale_y_continuous(labels = scales::percent_format(scale=1/90))

return(list(results, prop))
}
save(results, prop, file ="distribution15_random_pors.RData")
