anim <- ggplot(iris, aes(Sepal.Length, Sepal.Width)) +
  geom_point() +
  labs(title = "{closest_state}") +
  transition_states(Species, transition_length = 4, state_length = 1) +
  view_follow()

# Fixing a dimension can be done in general
anim1 <- ggplot(iris, aes(Sepal.Length, Sepal.Width)) +
  geom_point() +
  labs(title = "{closest_state}") +
  transition_states(Species, transition_length = 4, state_length = 1) +
  view_follow(fixed_x = TRUE)

# ...or just for one side of the range
anim1 <- ggplot(iris, aes(Sepal.Length, Sepal.Width)) +
  geom_point() +
  labs(title = "{closest_state}") +
  transition_states(Species, transition_length = 4, state_length = 1) +
  view_follow(fixed_x = c(4, NA), fixed_y = c(2, NA)) +
  


ggplot(results10nc %>% filter(id %in%c(0,5,10,20,60)), aes(omega, time, color = method, group = method)) +
  geom_point() +
  geom_line() +
  transition_states(method, transition_length = 4, state_length = 1) +
  view_follow(fixed_x = TRUE)
