get_profiles_distribution <- function(m, nrankings = 5000, omit = FALSE, distribution = "norm") {
  
  max_iter <- nrankings/(m-1)
  
  if(!omit) {
    r5 <- create_profiles_distribution(5,m,max_iter = max_iter,distribution)
  }
  else {
    r5 <- matrix(rep(0, m*4), nrow = 4)
    colnames(r5) <- paste0("w", 1:m)
    rownames(r5) <- c("nc", "cw", "cr", "wcw")
    r5 <- list(res = r5, pors = NULL, details = NULL)
  }
  
  # r5 <- create_profiles_distribution(5,m,max_iter = max_iter)
  r6 <- create_profiles_distribution(6,m,max_iter = max_iter,distribution)
  r7 <- create_profiles_distribution(7,m,max_iter = max_iter,distribution)
  r8 <- create_profiles_distribution(8,m,max_iter = max_iter,distribution)
  r9 <- create_profiles_distribution(9,m,max_iter = max_iter,distribution)
  r10 <- create_profiles_distribution(10,m,max_iter = max_iter,distribution)
  r11 <- create_profiles_distribution(11,m,max_iter = max_iter,distribution)
  r12 <- create_profiles_distribution(12,m,max_iter = max_iter,distribution)
  r13 <- create_profiles_distribution(13,m,max_iter = max_iter,distribution)
  r14 <- create_profiles_distribution(14,m,max_iter = max_iter,distribution)
  r15 <- create_profiles_distribution(15,m,max_iter = max_iter,distribution)
  r16 <- create_profiles_distribution(16,m,max_iter = max_iter,distribution)
  
  # res4 <- r4$res %>% 
  #   as_tibble(rownames = "type") %>% 
  #   pivot_longer(-type, names_to = "omega", values_to = "times") %>% 
  #   mutate(omega = as.factor(str_remove(omega, "w")),
  #          n = 4)
  res5 <- r5$res %>% 
    as_tibble(rownames = "type") %>% 
    pivot_longer(-type, names_to = "omega", values_to = "times") %>% 
    mutate(omega = as.factor(str_remove(omega, "w")),
           n = 5)
  res6 <- r6$res %>% 
    as_tibble(rownames = "type") %>% 
    pivot_longer(-type, names_to = "omega", values_to = "times") %>% 
    mutate(omega = as.factor(str_remove(omega, "w")),
           n = 6)
  res7 <- r7$res %>% 
    as_tibble(rownames = "type") %>% 
    pivot_longer(-type, names_to = "omega", values_to = "times") %>% 
    mutate(omega = as.factor(str_remove(omega, "w")),
           n = 7)
  res8 <- r8$res %>% 
    as_tibble(rownames = "type") %>% 
    pivot_longer(-type, names_to = "omega", values_to = "times") %>% 
    mutate(omega = as.factor(str_remove(omega, "w")),
           n = 8)
  res9 <- r9$res %>% 
    as_tibble(rownames = "type") %>% 
    pivot_longer(-type, names_to = "omega", values_to = "times") %>% 
    mutate(omega = as.factor(str_remove(omega, "w")),
           n = 9)
  res10 <- r10$res %>% 
    as_tibble(rownames = "type") %>% 
    pivot_longer(-type, names_to = "omega", values_to = "times") %>% 
    mutate(omega = as.factor(str_remove(omega, "w")),
           n = 10)
  res11 <- r11$res %>% 
    as_tibble(rownames = "type") %>% 
    pivot_longer(-type, names_to = "omega", values_to = "times") %>% 
    mutate(omega = as.factor(str_remove(omega, "w")),
           n = 11)
  res12 <- r12$res %>% 
    as_tibble(rownames = "type") %>% 
    pivot_longer(-type, names_to = "omega", values_to = "times") %>% 
    mutate(omega = as.factor(str_remove(omega, "w")),
           n = 12)
  res13 <- r13$res %>% 
    as_tibble(rownames = "type") %>% 
    pivot_longer(-type, names_to = "omega", values_to = "times") %>% 
    mutate(omega = as.factor(str_remove(omega, "w")),
           n = 13)
  res14 <- r14$res %>% 
    as_tibble(rownames = "type") %>% 
    pivot_longer(-type, names_to = "omega", values_to = "times") %>% 
    mutate(omega = as.factor(str_remove(omega, "w")),
           n = 14)
  res15 <- r15$res %>% 
    as_tibble(rownames = "type") %>% 
    pivot_longer(-type, names_to = "omega", values_to = "times") %>% 
    mutate(omega = as.factor(str_remove(omega, "w")),
           n = 15)
  res16 <- r16$res %>%
    as_tibble(rownames = "type") %>%
    pivot_longer(-type, names_to = "omega", values_to = "times") %>%
    mutate(omega = as.factor(str_remove(omega, "w")),
           n = 16)
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
    #res4 ,
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
    res15,
    res16
    # res17,
    # res18
  ) %>% 
    mutate(n = as.factor(n),
           type = as.factor(type),
           m = m)
  
  prop <- results %>%
    mutate(type = ifelse(as.character(type) == "cr", "cw", as.character(type))) %>%
    group_by(type, n) %>% 
    summarise(times = sum(times)) %>%
    mutate(n = as.factor(n),
           type = factor(type, levels = c("nc", "wcw", "cw")))
  
  results %>%
    mutate(type = ifelse(as.character(type) == "cr", "cw", as.character(type))) %>%
    group_by(type, n) %>% 
    summarise(times = sum(times)) %>%
    mutate(n = as.factor(n),
           type = factor(type, levels = c("nc", "wcw", "cw")))
  
  pors <- list(
    #r4$pors,
    r5$pors,
    r6$pors,
    r7$pors,
    r8$pors,
    r9$pors,
    r10$pors,
    r11$pors,
    r12$pors,
    r13$pors,
    r14$pors,
    r15$pors,
    r16$pors
  ) 
  
  details <- bind_rows(
    #r4$details,
    r5$details,
    r6$details,
    r7$details,
    r8$details,
    r9$details,
    r10$details,
    r11$details,
    r12$details,
    r13$details,
    r14$details,
    r15$details,
    r16$details
  ) %>% mutate(n = as.factor(as.numeric(n)),
               m = as.factor(as.numeric(m)), 
               w = as.factor(as.numeric(w)),
               d = as.factor(as.numeric(d)), 
               type = factor(type, levels = c("nc", "wcw", "cw", "cr")))
  
  
  return(list(results = results, 
              prop = prop, pors = pors, details = details,
              total = sum(r7$res)))
}


