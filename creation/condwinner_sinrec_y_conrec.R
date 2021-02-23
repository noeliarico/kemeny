comparar_fuzzieee <- function(pors,n,file_name,rep=0,type) {
  out <- c(paste0('
import numpy as np
import pandas as pd
import time
import kemeny.azzinimunda.azzinimunda0 as am0
import kemeny.azzinimunda.azzinimunda1 as am1
import kemeny.azzinimunda.azzinimunda1rec as am1rec

rep = ',rep,'
results',n,' = np.zeros(0).reshape(0,7+rep)
'))
  
  for(i in 1:length(pors)) {
    for(j in 1:length(pors[[i]])) {
      if(!is.null(pors[[i]][[j]])) {
        out0 <- "##############################################################"
        out1 <- to_python_om(votrix(pors[[i]][[j]]))
        out2 <- paste0('
        
times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am0.AzziniMunda0(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([',n,', ',i,', ',j,', 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results',n,' = np.vstack((results',n,', result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([',n,', ',i,', ',j,', 2, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results',n,' = np.vstack((results',n,', result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1rec.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([',n,', ',i,', ',j,', 3, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results',n,' = np.vstack((results',n,', result))
')
        
        out <- c(out, out0, out1, out2)
      } # end if
    } # end for
  } # end for
  
  out <- c(out, paste0(' 
pd.DataFrame(results',n,').to_csv("cwsinyconrec',n,type,'_azzini.csv")'))
  out <- paste(out, collapse = "\n")
  sink(file_name)
  cat(out)
  sink()
}
