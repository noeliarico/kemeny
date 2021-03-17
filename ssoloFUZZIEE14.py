
import numpy as np
import pandas as pd
import time
import kemeny.azzinimunda.azzinimunda3 as am3

rep = 1
results14 = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,2,6,3,3,5,6,3,7,2,6,2,4,4],
[8,0,8,6,6,5,6,5,7,5,8,2,2,4],
[4,2,0,2,5,7,5,5,4,4,5,4,4,4],
[7,4,8,0,8,7,8,7,7,7,10,4,4,4],
[7,4,5,2,0,7,5,7,7,4,7,4,4,4],
[5,5,3,3,3,0,3,2,5,5,3,2,4,4],
[4,4,5,2,5,7,0,7,4,4,7,4,4,4],
[7,5,5,3,3,8,3,0,7,7,3,5,7,7],
[3,3,6,3,3,5,6,3,0,3,6,5,5,2],
[8,5,6,3,6,5,6,3,7,0,6,5,5,4],
[4,2,5,0,3,7,3,7,4,4,0,4,4,4],
[8,8,6,6,6,8,6,5,5,5,6,0,10,7],
[6,8,6,6,6,6,6,3,5,5,6,0,0,7],
[6,6,6,6,6,6,6,3,8,6,6,3,3,0]])



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
result = np.append(np.array([14, 1, 1, 3, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results14 = np.vstack((results14, result))

##############################################################
om = np.array([
[0,2,4,3,5,5,4,3,5,2,6,2,3,3],
[8,0,8,6,6,6,6,8,7,6,8,5,5,6],
[6,2,0,4,6,7,5,6,3,4,6,5,3,5],
[7,4,6,0,9,7,7,9,5,5,10,6,4,5],
[5,4,4,1,0,5,3,6,4,4,7,3,3,3],
[5,4,3,3,5,0,2,3,3,4,5,4,4,6],
[6,4,5,3,7,8,0,9,4,5,8,6,4,6],
[7,2,4,1,4,7,1,0,5,4,4,5,5,6],
[5,3,7,5,6,7,6,5,0,3,7,6,6,4],
[8,4,6,5,6,6,5,6,7,0,6,7,7,6],
[4,2,4,0,3,5,2,6,3,4,0,3,3,3],
[8,5,5,4,7,6,4,5,4,3,7,0,7,5],
[7,5,7,6,7,6,6,5,4,3,7,3,0,7],
[7,4,5,5,7,4,4,4,6,4,7,5,3,0]])



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
result = np.append(np.array([14, 1, 2, 3, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results14 = np.vstack((results14, result))

##############################################################
om = np.array([
[0,10,10,10,5,5,5,10,10,5,5,10,10,10],
[0,0,10,10,5,5,5,10,10,5,5,10,10,10],
[0,0,0,5,5,0,0,10,0,5,5,5,5,0],
[0,0,5,0,5,5,0,10,5,5,5,10,10,0],
[5,5,5,5,0,5,5,5,5,10,10,5,5,5],
[5,5,10,5,5,0,5,10,5,5,5,10,10,5],
[5,5,10,10,5,5,0,10,5,5,5,10,10,5],
[0,0,0,0,5,0,0,0,0,5,5,5,5,0],
[0,0,10,5,5,5,5,10,0,5,5,10,10,5],
[5,5,5,5,0,5,5,5,5,0,10,5,5,5],
[5,5,5,5,0,5,5,5,5,0,0,5,5,5],
[0,0,5,0,5,0,0,5,0,5,5,0,5,0],
[0,0,5,0,5,0,0,5,0,5,5,5,0,0],
[0,0,10,10,5,5,5,10,5,5,5,10,10,0]])



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
result = np.append(np.array([14, 1, 3, 3, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results14 = np.vstack((results14, result))

##############################################################
om = np.array([
[0,6,5,5,6,2,2,6,8,5,3,7,6,6],
[4,0,3,4,7,5,2,8,7,3,3,9,5,6],
[5,7,0,9,9,4,3,8,5,5,6,9,5,6],
[5,6,1,0,6,4,0,8,6,2,4,10,6,4],
[4,3,1,4,0,4,1,4,5,3,5,4,3,5],
[8,5,6,6,6,0,5,9,8,5,5,7,5,7],
[8,8,7,10,9,5,0,8,6,7,6,10,8,8],
[4,2,2,2,6,1,2,0,6,3,3,5,3,2],
[2,3,5,4,5,2,4,4,0,4,4,5,5,4],
[5,7,5,8,7,5,3,7,6,0,7,8,5,8],
[7,7,4,6,5,5,4,7,6,3,0,7,7,7],
[3,1,1,0,6,3,0,5,5,2,3,0,4,4],
[4,5,5,4,7,5,2,7,5,5,3,6,0,7],
[4,4,4,6,5,3,2,8,6,2,3,6,3,0]])



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
result = np.append(np.array([14, 1, 4, 3, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results14 = np.vstack((results14, result))

##############################################################
om = np.array([
[0,6,5,4,6,2,3,7,8,5,4,7,7,6],
[4,0,4,5,7,5,3,8,7,4,5,9,5,6],
[5,6,0,8,7,3,3,8,6,5,6,8,5,6],
[6,5,2,0,6,4,1,8,6,4,5,9,7,5],
[4,3,3,4,0,3,2,5,6,4,5,4,3,6],
[8,5,7,6,7,0,6,9,8,5,6,7,6,7],
[7,7,7,9,8,4,0,8,7,6,6,9,8,8],
[3,2,2,2,5,1,2,0,5,3,3,4,3,2],
[2,3,4,4,4,2,3,5,0,4,4,5,5,4],
[5,6,5,6,6,5,4,7,6,0,7,7,5,7],
[6,5,4,5,5,4,4,7,6,3,0,6,6,6],
[3,1,2,1,6,3,1,6,5,3,4,0,4,4],
[3,5,5,3,7,4,2,7,5,5,4,6,0,6],
[4,4,4,5,4,3,2,8,6,3,4,6,4,0]])



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
result = np.append(np.array([14, 1, 5, 3, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results14 = np.vstack((results14, result))

##############################################################
om = np.array([
[0,2,4,2,3,5,4,2,5,4,4,1,3,2],
[8,0,8,4,4,5,5,6,6,6,8,5,4,6],
[6,2,0,3,4,6,3,4,3,5,6,5,3,5],
[8,6,7,0,8,6,5,7,5,7,10,7,4,6],
[7,6,6,2,0,5,3,5,4,6,8,5,3,5],
[5,5,4,4,5,0,3,4,4,5,5,4,4,5],
[6,5,7,5,7,7,0,8,6,6,8,6,6,6],
[8,4,6,3,5,6,2,0,5,5,6,5,7,6],
[5,4,7,5,6,6,4,5,0,4,7,5,5,4],
[6,4,5,3,4,5,4,5,6,0,5,4,5,4],
[6,2,4,0,2,5,2,4,3,5,0,2,3,2],
[9,5,5,3,5,6,4,5,5,6,8,0,6,6],
[7,6,7,6,7,6,4,3,5,5,7,4,0,7],
[8,4,5,4,5,5,4,4,6,6,8,4,3,0]])



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
result = np.append(np.array([14, 2, 1, 3, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results14 = np.vstack((results14, result))

##############################################################
om = np.array([
[0,3,5,2,4,4,5,3,5,3,4,2,4,3],
[7,0,7,4,4,4,5,6,6,5,7,4,4,5],
[5,3,0,3,4,5,3,5,3,4,5,4,3,4],
[8,6,7,0,8,6,6,8,5,6,9,7,5,6],
[6,6,6,2,0,4,4,6,4,5,7,4,3,5],
[6,6,5,4,6,0,4,5,4,5,5,5,5,6],
[5,5,7,4,6,6,0,8,5,5,7,5,5,6],
[7,4,5,2,4,5,2,0,5,4,5,4,6,5],
[5,4,7,5,6,6,5,5,0,4,7,5,5,4],
[7,5,6,4,5,5,5,6,6,0,5,5,6,5],
[6,3,5,1,3,5,3,5,3,5,0,3,4,3],
[8,6,6,3,6,5,5,6,5,5,7,0,6,6],
[6,6,7,5,7,5,5,4,5,4,6,4,0,7],
[7,5,6,4,5,4,4,5,6,5,7,4,3,0]])



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
result = np.append(np.array([14, 2, 2, 3, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results14 = np.vstack((results14, result))

##############################################################
om = np.array([
[0,6,6,6,3,3,3,6,10,3,3,6,6,6],
[4,0,6,10,7,7,3,10,10,3,7,10,6,6],
[4,4,0,7,7,4,4,10,4,3,7,7,3,4],
[4,0,3,0,3,3,0,10,7,3,7,10,6,0],
[7,3,3,7,0,7,3,7,7,6,10,7,3,3],
[7,3,6,7,3,0,3,10,7,3,7,10,6,3],
[7,7,6,10,7,7,0,10,7,3,7,10,6,3],
[4,0,0,0,3,0,0,0,4,3,7,3,3,0],
[0,0,6,3,3,3,3,6,0,3,3,6,6,3],
[7,7,7,7,4,7,7,7,7,0,10,7,3,7],
[7,3,3,3,0,3,3,3,7,0,0,3,3,3],
[4,0,3,0,3,0,0,7,4,3,7,0,3,0],
[4,4,7,4,7,4,4,7,4,7,7,7,0,4],
[4,4,6,10,7,7,7,10,7,3,7,10,6,0]])



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
result = np.append(np.array([14, 2, 3, 3, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results14 = np.vstack((results14, result))

##############################################################
om = np.array([
[0,10,8,5,9,4,7,8,4,5,4,4,5,4],
[0,0,5,2,5,3,5,4,4,2,3,2,3,2],
[2,5,0,3,4,4,4,4,3,4,2,4,1,4],
[5,8,7,0,7,6,7,7,4,4,5,5,3,4],
[1,5,6,3,0,4,5,3,2,2,4,2,3,3],
[6,7,6,4,6,0,5,5,4,4,6,3,6,6],
[3,5,6,3,5,5,0,6,3,4,6,6,3,3],
[2,6,6,3,7,5,4,0,4,4,3,6,2,3],
[6,6,7,6,8,6,7,6,0,4,6,7,6,4],
[5,8,6,6,8,6,6,6,6,0,4,3,6,4],
[6,7,8,5,6,4,4,7,4,6,0,4,4,6],
[6,8,6,5,8,7,4,4,3,7,6,0,3,6],
[5,7,9,7,7,4,7,8,4,4,6,7,0,6],
[6,8,6,6,7,4,7,7,6,6,4,4,4,0]])



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
result = np.append(np.array([14, 2, 4, 3, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results14 = np.vstack((results14, result))

##############################################################
om = np.array([
[0,9,8,6,8,4,6,8,4,4,4,4,5,5],
[1,0,4,3,4,3,5,6,4,2,2,3,4,4],
[2,6,0,3,4,3,5,5,4,4,2,4,3,5],
[4,7,7,0,6,4,6,6,4,3,5,5,5,4],
[2,6,6,4,0,4,5,5,3,2,3,3,4,5],
[6,7,7,6,6,0,5,7,4,3,7,5,7,6],
[4,5,5,4,5,5,0,7,3,4,5,5,3,4],
[2,4,5,4,5,3,3,0,4,3,3,5,3,3],
[6,6,6,6,7,6,7,6,0,4,6,7,8,5],
[6,8,6,7,8,7,6,7,6,0,5,4,6,6],
[6,8,8,5,7,3,5,7,4,5,0,4,5,6],
[6,7,6,5,7,5,5,5,3,6,6,0,4,6],
[5,6,7,5,6,3,7,7,2,4,5,6,0,6],
[5,6,5,6,5,4,6,7,5,4,4,4,4,0]])



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
result = np.append(np.array([14, 2, 5, 3, exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results14 = np.vstack((results14, result))

 
pd.DataFrame(results14).to_csv("fuzziee14nc_123.csv")