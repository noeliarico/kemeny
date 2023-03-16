
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 1
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,6,7,6,8,4,6,5,5,5,6,6,8,4],
[5,0,7,5,7,6,6,8,7,6,5,7,8,5],
[4,4,0,3,7,5,4,3,3,5,6,2,6,4],
[5,6,8,0,7,6,4,7,5,5,7,6,7,5],
[3,4,4,4,0,6,3,6,4,2,5,3,5,2],
[7,5,6,5,5,0,5,5,4,4,5,4,7,6],
[5,5,7,7,8,6,0,6,7,6,7,6,7,6],
[6,3,8,4,5,6,5,0,5,4,5,5,7,5],
[6,4,8,6,7,7,4,6,0,5,4,6,8,7],
[6,5,6,6,9,7,5,7,6,0,6,6,8,6],
[5,6,5,4,6,6,4,6,7,5,0,5,7,4],
[5,4,9,5,8,7,5,6,5,5,6,0,6,5],
[3,3,5,4,6,4,4,4,3,3,4,5,0,3],
[7,6,7,6,9,5,5,6,4,5,7,6,8,0]])



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
result = np.append(np.array([16, 11, 1, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,2,5,4,2,2,5,0,3,3,6,3,7],
[9,0,5,8,6,7,7,8,5,9,6,6,8,7],
[9,6,0,8,7,6,7,7,6,9,9,5,8,7],
[6,3,3,0,6,3,4,9,2,3,5,5,5,6],
[7,5,4,5,0,5,5,10,4,4,7,6,6,8],
[9,4,5,8,6,0,7,8,3,5,6,6,3,7],
[9,4,4,7,6,4,0,7,4,9,6,6,7,7],
[6,3,4,2,1,3,4,0,3,3,3,5,5,7],
[11,6,5,9,7,8,7,8,0,6,7,7,9,8],
[8,2,2,8,7,6,2,8,5,0,7,6,4,8],
[8,5,2,6,4,5,5,8,4,4,0,6,6,8],
[5,5,6,6,5,5,5,6,4,5,5,0,8,5],
[8,3,3,6,5,8,4,6,2,7,5,3,0,5],
[4,4,4,5,3,4,4,4,3,3,3,6,6,0]])



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
result = np.append(np.array([16, 11, 2, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbrcw/mebbrcw2_16_11.csv", index=False, header=False)