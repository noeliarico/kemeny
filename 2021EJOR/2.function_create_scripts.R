# Function to create the scripts -----------------------------------------------

# Algorithm principal
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




# Algorithm used as baseline
scripts_mercw <- function(pors,n,m,
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
    algorithm = alg.AzziniMunda3(om) 
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
pd.DataFrame(results).to_csv("',file.path(path_out_csv,file_name),'.csv", index=False, header=False)'))
  out <- paste(out, collapse = "\n")
  sink(paste0(file.path(path_out_py,file_name), ".py"))
  cat(out)
  sink()
}

 


# Algorithm proposed
scripts_mebb <- function(pors,n,m,
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
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([',n,', ',m,', ',i,', "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
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


# Algorithm proposed
scripts_mebbd <- function(pors,n,m,
                           file_name,
                           path_out_py,
                           path_out_csv,
                           rep=1) {
  out <- c(paste0('
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg
from kemeny import sc

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
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([',n,', ',m,', ',i,', "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
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




# Algorithm proposed
scripts_mebbrcw <- function(pors,n,m,
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
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([',n,', ',m,', ',i,', "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
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



scripts_mebbrcwd <- function(pors,n,m,
                          file_name,
                          path_out_py,
                          path_out_csv,
                          rep=1) {
  out <- c(paste0('
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg
from kemeny import sc

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
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([',n,', ',m,', ',i,', "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
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

scripts_mebbrcwdc <- function(pors,n,m,
                              file_name,
                              path_out_py,
                              path_out_csv,
                              rep=1) {
  out <- c(paste0('
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg
from kemeny import sc

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
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([',n,', ',m,', ',i,', "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
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