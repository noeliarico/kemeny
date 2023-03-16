pt_get_indexes_for_profiles <- function(the_n, absolute = TRUE) {
  indexes <- tribble(~profile, ~n, ~m, 
                     ~mu1, 
                     ~mu2, ~mu3, ~mu4,
                     ~mu5, ~mu6, ~mu7,
                     ~mu8, ~mu9, ~mu10,
                     ~mu11, ~mu12,
                     ~mu13, ~mu14, ~mu15, ~mu16, ~mu17,
                     ~mu18, ~mu19,
                     ~mu20
                     )
  for(i in c(10,11,20,21,30,31,50,51,80,81,130,131,210,211,340,341,550,551,890,891)) {
    print(i)
    load(paste0("predict_time/profiles/pt_pors_",the_n,"_",i,".RData"))
    # average kendall distance between the rankings of the profile
    mu1 <- sapply(porsPredictTime, d1)
    # range of the position of the alternatives
    mu2 <- sapply(porsPredictTime, d2) # maximum
    mu3 <- sapply(porsPredictTime, d3) # minimum
    mu4 <- sapply(porsPredictTime, d4) # average
    # # bounds to the optimal cost
    mu5 <- sapply(porsPredictTime, d5) # minimum
    mu6 <- sapply(porsPredictTime, d6) # maximum
    mu7 <- sapply(porsPredictTime, d7) # range
    # # margins
    mu8 <- sapply(porsPredictTime, d8) # average
    mu9 <- sapply(porsPredictTime, d9) # most common
    mu10 <- sapply(porsPredictTime, d10) # different
    # # rowsums
    mu11 <- sapply(porsPredictTime, d11) # distance borda
    mu12 <- sapply(porsPredictTime, d12) # omega
    # # beta
    mu13 <- sapply(porsPredictTime, d13) # omega
    mu14 <- sapply(porsPredictTime, d14) # omega
    mu15 <- sapply(porsPredictTime, d15) # omega
    mu16 <- sapply(porsPredictTime, d16) # omega
    mu17 <- sapply(porsPredictTime, d17) # omega
    mu18 <- sapply(porsPredictTime, d18)
    # # intransitive cycles
    mu18 <- sapply(porsPredictTime, d18)
    mu19 <- sapply(porsPredictTime, d19)
    # 
    mu20 <- sapply(porsPredictTime, d20)
    to_add <- tibble(profile = 1:length(porsPredictTime),
                     n = the_n,
                     m = i,
                     mu1 = mu1,
                     mu2 = mu2, mu3 = mu3, mu4 = mu4,
                     mu5 = mu5, mu6 = mu6, mu7 = mu7,
                     mu8 = mu8, mu9 = mu9, mu10 = mu10,
                     mu11 = mu11, mu12 = mu12,
                     mu13 = mu13, mu14 = mu14, mu15 = mu15, mu16 = mu16, mu17 = mu17,
                     mu18 = mu18, mu19 = mu19,
                     mu20 = mu20
                     )
    
    indexes <- indexes %>% bind_rows(to_add)
  }
  return(indexes)
}

indexes8 <- pt_get_indexes_for_profiles(8)
indexes9 <- pt_get_indexes_for_profiles(9)
indexes10 <- pt_get_indexes_for_profiles(10)
