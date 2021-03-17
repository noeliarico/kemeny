
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
[0,2,6,4,4,4,4,5,8,5,8,6],
[8,0,6,3,3,3,4,6,6,4,8,4],
[4,4,0,6,6,6,3,2,5,5,10,4],
[6,7,4,0,6,5,4,5,4,5,10,6],
[6,7,4,4,0,5,4,5,6,5,10,6],
[6,7,4,5,5,0,4,6,4,6,10,6],
[6,6,7,6,6,6,0,7,7,7,9,7],
[5,4,8,5,5,4,3,0,6,3,10,6],
[2,4,5,6,4,6,3,4,0,5,10,7],
[5,6,5,5,5,4,3,7,5,0,10,3],
[2,2,0,0,0,0,1,0,0,0,0,0],
[4,6,6,4,4,4,3,4,3,7,10,0]])


        
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
result = np.append(np.array([12, 11, 1, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 1, 2, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
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
result = np.append(np.array([12, 11, 1, 3, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,7,4,3,5,5,4,6,4,4,5,9],
[3,0,4,6,3,7,4,5,6,4,5,9],
[6,6,0,8,6,6,7,6,6,7,6,9],
[7,4,2,0,4,7,4,7,3,5,4,8],
[5,7,4,6,0,5,5,3,4,5,4,8],
[5,3,4,3,5,0,5,6,5,5,7,7],
[6,6,3,6,5,5,0,4,4,4,5,8],
[4,5,4,3,7,4,6,0,5,7,6,6],
[6,4,4,7,6,5,6,5,0,6,5,8],
[6,6,3,5,5,5,6,3,4,0,5,8],
[5,5,4,6,6,3,5,4,5,5,0,8],
[1,1,1,2,2,3,2,4,2,2,2,0]])


        
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
result = np.append(np.array([12, 11, 2, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 2, 2, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
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
result = np.append(np.array([12, 11, 2, 3, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,6,5,10,4,7,4,4,3,3,4,5],
[4,0,6,10,4,4,7,3,7,7,4,4],
[5,4,0,10,8,7,4,4,7,1,8,5],
[0,0,0,0,0,0,0,0,0,0,0,0],
[6,6,2,10,0,4,4,4,7,3,5,4],
[3,6,3,10,6,0,6,4,3,3,6,7],
[6,3,6,10,6,4,0,3,4,3,6,6],
[6,7,6,10,6,6,7,0,6,7,6,6],
[7,3,3,10,3,7,6,4,0,3,3,7],
[7,3,9,10,7,7,7,3,7,0,7,4],
[6,6,2,10,5,4,4,4,7,3,0,4],
[5,6,5,10,6,3,4,4,3,6,6,0]])


        
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
result = np.append(np.array([12, 11, 3, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 3, 2, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
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
result = np.append(np.array([12, 11, 3, 3, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,5,4,6,6,7,9,4,6,7,6,6],
[5,0,4,5,5,5,10,5,3,5,5,4],
[6,6,0,6,6,10,9,6,9,8,7,8],
[4,5,4,0,3,5,10,4,3,5,8,4],
[4,5,4,7,0,5,10,3,5,5,5,4],
[3,5,0,5,5,0,9,6,8,6,4,6],
[1,0,1,0,0,1,0,1,0,1,0,3],
[6,5,4,6,7,4,9,0,5,4,4,4],
[4,7,1,7,5,2,10,5,0,5,5,4],
[3,5,2,5,5,4,9,6,5,0,6,5],
[4,5,3,2,5,6,10,6,5,4,0,5],
[4,6,2,6,6,4,7,6,6,5,5,0]])


        
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
result = np.append(np.array([12, 11, 4, 1, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

times = np.zeros(rep)
for i in range(rep):
    # Algorithm without Condorcet
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 4, 2, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
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
result = np.append(np.array([12, 11, 4, 3, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results12 = np.vstack((results12, result))

##############################################################
om = np.array([
[0,5,5,10,5,5,3,5,5,5,3,5],
[5,0,3,10,2,7,3,5,5,5,5,7],
[5,7,0,7,7,7,0,5,5,7,5,7],
[0,0,3,0,0,0,0,0,0,0,0,0],
[5,8,3,10,0,5,3,5,5,5,5,5],
[5,3,3,10,5,0,3,8,5,5,8,5],
[7,7,10,10,7,7,0,7,7,7,7,7],
[5,5,5,10,5,2,3,0,5,5,5,7],
[5,5,5,10,5,5,3,5,0,5,3,5],
[5,5,3,10,5,5,3,5,5,0,5,5],
[7,5,5,10,5,2,3,5,7,5,0,2],
[5,3,3,10,5,5,3,3,5,5,8,0]])


        
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
    # Algorithm without Condorcet
    algorithm = am2.AzziniMunda2(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 5, 2, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
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

 
pd.DataFrame(results12).to_csv("resultsNC12cw_123_2.csv")
