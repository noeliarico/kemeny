# Function to create the profiles of rankings ----------------------------------

create_profiles_nc <- function(n, nvotes, total = 100, 
                               seed = NULL, 
                               max_distinct = NULL,
                               distribution = "norm")  {
  
  profiles <- vector(mode = "list", length = total)
  names(profiles) <- paste0("pr",1:total)
  
  created <- 1
  if(!is.null(seed)) set.seed(seed)
  if(is.null(max_distinct)) max_distinct <- nvotes
  if(max_distinct > nvotes) stop("max_distinct must be < than nvotes")
  
  while(created <= total) {
    
    d <- sample(1:max_distinct, 1)
    r <- random_profile_of_rankings(n, nvotes, seed = seed, distinct = d, distribution = distribution)
    
    if(!condorcet(r) && !condorcet_winner(r)) { 
      profiles[[created]] <- r
      created <- created + 1
    }
    
  }
  return(profiles)
}

# Function to create the scripts -----------------------------------------------

scripts_mercw <- function(pors,n,m,file_name,rep=1) {
  out <- c(paste0('
import numpy as np
import pandas as pd
import time
import kemeny.azzinimunda.azzinimunda3 as am3

rep = ',rep,'
results = np.zeros(0).reshape(0,7+rep)
'))
  
  for(i in 1:length(pors)) {
    
    out0 <- "##############################################################"
    out1 <- to_python_om(votrix(pors[[i]]))
    out2 <- paste0('

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am3.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([',n,', ',m,', ',i,', "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))
')
    
    out <- c(out, out0, out1, out2)
    
    
  } # end for
  
  file_name <- paste(file_name, n, m, sep="_")
  out <- c(out, paste0(' 
pd.DataFrame(results).to_csv("',file_name,'.csv", index=False, header=False)'))
  out <- paste(out, collapse = "\n")
  sink(paste0(file_name, ".py"))
  cat(out)
  sink()
}


# Create the profiles of rankings ----------------------------------------------

n <- 8 # change here the number of alternatives
for(i in c(10,11,20,21,30,31,50,51,80,81,130,131,210,211,
           340,341,550,551,890,891)) {
  print(i)
  # seed(123)
  set.seed(1994)
  # create profiles with uniform distribution of the votes
  porsPredictTime1 <- create_profiles_nc(n,i,1000,distribution = "unif")
  names(porsPredictTime1) <- paste0(names(porsPredictTime1), "_unif")
  # create profiles with normal distribution of the votes
  porsPredictTime2 <- create_profiles_nc(n,i,1000,distribution = "norm")
  names(porsPredictTime2) <- paste0(names(porsPredictTime2), "_norm")
  # add both lists into the same list
  porsPredictTime <- append(porsPredictTime1, porsPredictTime2)
  # write the python scripts to execute in python
  scripts_mercw(porsPredictTime, n, i, "predictTime", rep=3)
  # save the profiles of rankings into a RData object
  save(porsPredictTime, file = paste0("pt_pors_seed1994",n,"_",i,".RData"))
}
