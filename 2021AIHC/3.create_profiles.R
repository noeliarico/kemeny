# Create the profiles of rankings ----------------------------------------------

n <- 11 # change here the number of alternatives
r <- 1 # number of repetitions
ms <- c(10, 25, 50, 100, 250, 500, 1000)
ms <- 2000
for(i in c(ms, ms+1)) {
  print(i)
  set.seed(123)
  #set.seed(1994)
  # # create profiles with uniform distribution of the votes
  # porsPredictTime1 <- create_profiles_nc(n,i,1000,distribution = "unif")
  # names(porsPredictTime1) <- paste0(names(porsPredictTime1), "_unif")
  # # create profiles with normal distribution of the votes
  # porsPredictTime2 <- create_profiles_nc(n,i,1000,distribution = "norm")
  # names(porsPredictTime2) <- paste0(names(porsPredictTime2), "_norm")
  # # add both lists into the same list
  # porsPredictTime <- append(porsPredictTime1, porsPredictTime2)
  porsPredictTime <- create_profiles_nc(n,i,200,distribution = "unif")
  # write the python scripts to execute in python
  
  # scripts_mercw(porsPredictTime, n, i, "mercw", 
  #                file.path(getwd(), folder, "scripts/mercw/"),
  #                file.path(getwd(), folder, "results/mercw"),
  #                rep=r)
  # 
  # scripts_meprcw(porsPredictTime, n, i, "meprcw", 
  #   file.path(getwd(), folder, "scripts/meprcw/"),
  #   file.path(getwd(), folder, "results/meprcw"),
  #   rep=r)
  
  # save the profiles of rankings into a RData object
  save(porsPredictTime, file = file.path(folder, paste0("profiles_of_rankings/porsEJOR",n,"_",i,".RData")))
}




