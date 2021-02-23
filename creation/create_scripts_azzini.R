scripts_azzini <- function(pors, n, file_name, rep = 0, type = "") {
  
  imports <- c("
import pandas as pd
import numpy as np
from kemeny.scf.borda import *
from kemeny.scf.condorcet import *
import kemeny.scf.distance as dist
import kemeny.scf.initialization as init
import kemeny.azzinimunda.azzinimunda0 as am0
import kemeny.azzinimunda.azzinimunda1 as am1
import kemeny.azzinimunda.azzinimunda2 as am2
import kemeny.azzinimunda.azzinimunda3 as am3
import time

")
  if(rep == 0) {
    out <- c(imports, paste0('
results',n,' = np.zeros(0).reshape(0,8)
'))
    for(i in 1:length(pors)) {
      for(j in 1:length(pors[[i]])) {
        if(!is.null(pors[[i]][[j]])) {
          out0 <- "##############################################################"
          out1 <- to_python_om(votrix(pors[[i]][[j]]))
          out2 <- paste0(' 
# Algorithm without Condorcet
exec_time = 0
algorithm = am0.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
result = np.array([',n,', ',i,', ',j,', 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object))
print(result[:7])
results',n,' = np.vstack((results',n,', result))
') 
          out3 <- paste0(' 
# Algorithm with Condorcet winner
exec_time = 0        
algorithm = am1.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
result = np.array([',n,', ',i,', ',j,', 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object))
print(result[:7])
results',n,' = np.vstack((results',n,', result))
')
          
          out4 <- paste0(' 
# Algorithm with Condorcet winner
exec_time = 0        
algorithm = am2.AzziniMunda2(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
result = np.array([',n,', ',i,', ',j,', 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object))
print(result[:7])
results',n,' = np.vstack((results',n,', result))
')
          out5 <- paste0(' 
# Algorithm with Condorcet winner
exec_time = 0        
algorithm = am3.AzziniMunda3(om, np.float("inf")) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
result = np.array([',n,', ',i,', ',j,', 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object))
print(result[:7])
results',n,' = np.vstack((results',n,', result))
')
          out <- c(out, out0, out1, out2, out3, out4, out5)
        }
      }
    }
  }
  else {
    out <- c(paste0(imports, '
rep = ',rep,'
results',n,' = np.zeros(0).reshape(0,8+rep)
' 
))
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
result = np.append(np.array([',n,', ',i,', ',j,', 0, exec_time, sol.shape[0], algorithm.ntentative, "NULL"], dtype=np.dtype(object)), times)
print(result[:7])
results',n,' = np.vstack((results',n,', result))
') 
          out3 <- paste0('
times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am1.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([',n,', ',i,', ',j,', 1, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results',n,' = np.vstack((results',n,', result))
')
          out4 <- paste0('
times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([',n,', ',i,', ',j,', 2, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results',n,' = np.vstack((results',n,', result))
')
          out5 <- paste0('
times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am3.AzziniMunda3(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([',n,', ',i,', ',j,', 3, exec_time, sol.shape[0], algorithm.ntentative, algorithm.cwinner], dtype=np.dtype(object)), times)
print(result[:7])
results',n,' = np.vstack((results',n,', result))
')
          out <- c(out, out0, out1, out2, out3, out4, out5)
        }
      }
    }
  }
  
  out <- c(out, paste0(' 
pd.DataFrame(results',n,').to_csv("results',n,type,'_azzini.csv")'))
  out <- paste(out, collapse = "\n")
  sink(file_name)
  cat(out)
  sink()
}
