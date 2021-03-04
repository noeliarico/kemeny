
import numpy as np
import pandas as pd
import time
import kemeny.azzinimunda.azzinimunda1 as am1
import kemeny.azzinimunda.azzinimunda2 as am2
import kemeny.azzinimunda.azzinimunda3 as am3

rep = 1
results12 = np.zeros(0).reshape(0,7+rep)


##############################################################
om = np.array([
[0,6,4,1,4,7,4,10,4,4,5,9],
[4,0,7,5,4,5,4,7,7,4,7,8],
[6,3,0,5,6,5,6,7,4,6,4,6],
[9,5,5,0,5,7,4,10,3,5,5,8],
[6,6,4,5,0,4,5,6,4,5,4,6],
[3,5,5,3,6,0,5,10,4,6,6,5],
[6,6,4,6,5,5,0,7,4,5,5,6],
[0,3,3,0,4,0,3,0,3,4,4,4],
[6,3,6,7,6,6,6,7,0,6,6,10],
[6,6,4,5,5,4,5,6,4,0,5,6],
[5,3,6,5,6,4,5,6,4,5,0,6],
[1,2,4,2,4,5,4,6,0,4,4,0]])


        
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
result = np.append(np.array([12, 11, 5, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

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
result = np.append(np.array([12, 11, 5, 3, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

 
pd.DataFrame(results12).to_csv("resultsNC12nc_123parte2.csv")
