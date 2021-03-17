import numpy as np
import pandas as pd
import time
import kemeny.azzinimunda.azzinimunda5 as am5

rep = 1

om = np.array([
[0,4,4,6,4,3,5,2,3,4,5,5,2,6,4,5],
[6,0,5,5,5,5,6,3,4,7,7,6,3,7,6,4],
[6,5,0,5,5,3,5,3,3,6,5,4,4,6,5,4],
[4,5,5,0,6,5,7,6,6,6,8,7,5,7,6,4],
[6,5,5,4,0,4,6,4,5,6,4,5,3,7,5,5],
[7,5,7,5,6,0,5,4,6,7,9,8,5,8,4,5],
[5,4,5,3,4,5,0,2,4,6,4,4,3,4,6,4],
[8,7,7,4,6,6,8,0,8,7,8,9,6,8,8,6],
[7,6,7,4,5,4,6,2,0,6,7,7,4,7,6,4],
[6,3,4,4,4,3,4,3,4,0,4,3,3,4,3,4],
[5,3,5,2,6,1,6,2,3,6,0,4,3,4,4,4],
[5,4,6,3,5,2,6,1,3,7,6,0,1,5,6,4],
[8,7,6,5,7,5,7,4,6,7,7,9,0,7,7,4],
[4,3,4,3,3,2,6,2,3,6,6,5,3,0,4,3],
[6,4,5,4,5,6,4,2,4,7,6,4,3,6,0,3],
[5,6,6,6,5,5,6,4,6,6,6,6,6,7,7,0]])

times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = am5.AzziniMunda5(om, np.Inf) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([',n,', ',i,', ',j,', 5, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
