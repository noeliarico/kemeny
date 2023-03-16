# Function to create the scripts -----------------------------------------------

# Algorithm ME that is not affected by any pruning process and therefore
# by where the solution is place on the search space or any other factor
scripts_me <- function(pors,n,m,
                          file_name,
                          path_out_py,
                          path_out_csv,
                          rep=1) {
  out <- c(paste0('
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

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
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([',n,', ',m,', ',i,', "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))
')
    
    out <- c(out, out0, out1, out2)
    
    
  } # end for
  
  file_name <- paste(file_name, n, m, sep="_")
  out <- c(out, paste0(' 
pd.DataFrame(results).to_csv("',file.path(path_out_csv,file_name),'.csv", index=False, header=False)'))
  out <- paste(out, collapse = "\n")
  sink(paste0(file.path(path_out_py,file_name), ".py"))
  cat(out)
  sink()
}
