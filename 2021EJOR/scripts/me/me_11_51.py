
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,32,14,21,25,27,30,23,22,16,21],
[19,0,15,18,16,21,21,18,18,17,17],
[37,36,0,32,28,30,31,22,19,25,23],
[30,33,19,0,33,25,27,29,27,19,23],
[26,35,23,18,0,24,24,21,26,24,20],
[24,30,21,26,27,0,27,20,29,26,20],
[21,30,20,24,27,24,0,22,22,24,22],
[28,33,29,22,30,31,29,0,26,28,24],
[29,33,32,24,25,22,29,25,0,22,21],
[35,34,26,32,27,25,27,23,29,0,28],
[30,34,28,28,31,31,29,27,30,23,0]])



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
result = np.append(np.array([11, 51, 1, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,31,29,29,24,22,25,26,28,22],
[22,0,27,25,22,23,23,26,19,23,22],
[20,24,0,25,22,21,22,22,21,27,21],
[22,26,26,0,25,25,26,27,24,27,23],
[22,29,29,26,0,27,26,29,20,31,26],
[27,28,30,26,24,0,22,28,23,33,23],
[29,28,29,25,25,29,0,26,22,30,25],
[26,25,29,24,22,23,25,0,20,27,25],
[25,32,30,27,31,28,29,31,0,32,20],
[23,28,24,24,20,18,21,24,19,0,24],
[29,29,30,28,25,28,26,26,31,27,0]])



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
result = np.append(np.array([11, 51, 2, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,19,23,21,18,15,26,26,30,23],
[37,0,24,24,23,31,29,29,29,32,32],
[32,27,0,29,23,31,24,22,26,26,27],
[28,27,22,0,25,31,22,26,25,33,30],
[30,28,28,26,0,30,22,28,24,37,27],
[33,20,20,20,21,0,19,28,23,31,29],
[36,22,27,29,29,32,0,32,34,33,31],
[25,22,29,25,23,23,19,0,24,29,23],
[25,22,25,26,27,28,17,27,0,27,22],
[21,19,25,18,14,20,18,22,24,0,22],
[28,19,24,21,24,22,20,28,29,29,0]])



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
result = np.append(np.array([11, 51, 3, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,51,30,20,30,20,30,30,20,30],
[21,0,31,51,41,31,21,51,31,21,41],
[0,20,0,30,20,0,0,30,0,0,20],
[21,0,21,0,21,21,21,31,21,21,41],
[31,10,31,30,0,31,31,51,31,31,51],
[21,20,51,30,20,0,41,51,21,41,41],
[31,30,51,30,20,10,0,51,31,21,51],
[21,0,21,20,0,0,0,0,0,0,41],
[21,20,51,30,20,30,20,51,0,20,41],
[31,30,51,30,20,10,30,51,31,0,51],
[21,10,31,10,0,10,0,10,10,0,0]])



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
result = np.append(np.array([11, 51, 4, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,32,29,33,31,21,19,28,24,24],
[20,0,22,22,20,25,25,16,21,24,17],
[19,29,0,20,31,28,27,20,24,25,21],
[22,29,31,0,32,32,25,25,27,25,28],
[18,31,20,19,0,25,24,16,25,20,24],
[20,26,23,19,26,0,26,17,21,27,17],
[30,26,24,26,27,25,0,24,21,16,20],
[32,35,31,26,35,34,27,0,34,22,30],
[23,30,27,24,26,30,30,17,0,23,18],
[27,27,26,26,31,24,35,29,28,0,22],
[27,34,30,23,27,34,31,21,33,29,0]])



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
result = np.append(np.array([11, 51, 5, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,31,25,33,25,28,30,25,29,33],
[23,0,20,19,36,26,29,34,25,36,24],
[20,31,0,22,28,24,31,27,20,23,37],
[26,32,29,0,29,25,24,27,27,31,36],
[18,15,23,22,0,28,26,22,23,21,20],
[26,25,27,26,23,0,28,20,22,22,26],
[23,22,20,27,25,23,0,22,29,21,18],
[21,17,24,24,29,31,29,0,29,29,22],
[26,26,31,24,28,29,22,22,0,24,28],
[22,15,28,20,30,29,30,22,27,0,22],
[18,27,14,15,31,25,33,29,23,29,0]])



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
result = np.append(np.array([11, 51, 6, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,28,29,27,22,24,26,27,28,23],
[22,0,26,29,25,24,18,22,16,23,16],
[23,25,0,26,24,20,21,22,22,25,25],
[22,22,25,0,26,23,19,24,19,21,20],
[24,26,27,25,0,26,22,25,22,22,21],
[29,27,31,28,25,0,23,25,25,25,27],
[27,33,30,32,29,28,0,29,24,27,28],
[25,29,29,27,26,26,22,0,20,24,22],
[24,35,29,32,29,26,27,31,0,27,26],
[23,28,26,30,29,26,24,27,24,0,25],
[28,35,26,31,30,24,23,29,25,26,0]])



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
result = np.append(np.array([11, 51, 7, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,27,34,27,26,28,24,30,31,29],
[22,0,24,22,24,20,22,19,25,22,18],
[24,27,0,28,25,27,29,22,25,30,29],
[17,29,23,0,25,30,27,23,27,24,16],
[24,27,26,26,0,25,34,25,29,25,17],
[25,31,24,21,26,0,22,20,26,28,23],
[23,29,22,24,17,29,0,24,23,32,19],
[27,32,29,28,26,31,27,0,28,28,24],
[21,26,26,24,22,25,28,23,0,26,21],
[20,29,21,27,26,23,19,23,25,0,16],
[22,33,22,35,34,28,32,27,30,35,0]])



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
result = np.append(np.array([11, 51, 8, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,28,28,34,28,25,25,28,27,28],
[22,0,22,14,26,22,21,18,23,26,17],
[23,29,0,23,27,24,27,22,27,26,22],
[23,37,28,0,37,34,25,26,32,29,25],
[17,25,24,14,0,21,19,14,21,22,20],
[23,29,27,17,30,0,22,24,26,26,25],
[26,30,24,26,32,29,0,28,30,24,27],
[26,33,29,25,37,27,23,0,29,26,26],
[23,28,24,19,30,25,21,22,0,24,22],
[24,25,25,22,29,25,27,25,27,0,23],
[23,34,29,26,31,26,24,25,29,28,0]])



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
result = np.append(np.array([11, 51, 9, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,24,47,47,47,47,34,51,34,47],
[27,0,40,36,36,47,51,23,40,27,51],
[27,11,0,23,36,47,47,34,27,23,34],
[4,15,28,0,51,51,28,11,15,27,15],
[4,15,15,0,0,28,15,11,4,27,15],
[4,4,4,0,23,0,15,0,4,27,4],
[4,0,4,23,36,36,0,23,4,27,23],
[17,28,17,40,40,51,28,0,17,27,51],
[0,11,24,36,47,47,47,34,0,23,47],
[17,24,28,24,24,24,24,24,28,0,24],
[4,0,17,36,36,47,28,0,4,27,0]])



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
result = np.append(np.array([11, 51, 10, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,26,26,31,25,20,28,19,23,32],
[35,0,32,23,32,27,26,31,23,28,28],
[25,19,0,28,38,30,24,29,38,25,27],
[25,28,23,0,38,32,21,25,30,24,27],
[20,19,13,13,0,15,20,15,22,18,21],
[26,24,21,19,36,0,21,23,26,20,27],
[31,25,27,30,31,30,0,27,26,25,28],
[23,20,22,26,36,28,24,0,23,25,38],
[32,28,13,21,29,25,25,28,0,30,30],
[28,23,26,27,33,31,26,26,21,0,28],
[19,23,24,24,30,24,23,13,21,23,0]])



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
result = np.append(np.array([11, 51, 11, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,39,44,44,45,33,38,34,23,20],
[21,0,28,30,39,28,23,34,28,22,18],
[12,23,0,22,44,39,27,26,22,17,18],
[7,21,29,0,34,25,24,27,21,17,12],
[7,12,7,17,0,28,7,11,21,12,19],
[6,23,12,26,23,0,17,17,11,16,11],
[18,28,24,27,44,34,0,29,22,16,12],
[13,17,25,24,40,34,22,0,22,18,19],
[17,23,29,30,30,40,29,29,0,22,30],
[28,29,34,34,39,35,35,33,29,0,19],
[31,33,33,39,32,40,39,32,21,32,0]])



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
result = np.append(np.array([11, 51, 12, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,23,36,31,27,20,33,27,29,17],
[24,0,20,34,29,28,25,28,23,29,19],
[28,31,0,38,30,29,17,25,29,30,22],
[15,17,13,0,15,21,7,7,12,20,15],
[20,22,21,36,0,23,19,22,7,29,18],
[24,23,22,30,28,0,21,26,22,29,26],
[31,26,34,44,32,30,0,36,25,40,31],
[18,23,26,44,29,25,15,0,15,25,17],
[24,28,22,39,44,29,26,36,0,33,24],
[22,22,21,31,22,22,11,26,18,0,17],
[34,32,29,36,33,25,20,34,27,34,0]])



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
result = np.append(np.array([11, 51, 13, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,21,25,27,25,25,21,23,18,23],
[28,0,21,29,31,23,26,26,32,28,32],
[30,30,0,32,37,27,28,30,29,24,28],
[26,22,19,0,29,22,24,24,26,19,20],
[24,20,14,22,0,23,25,23,25,17,16],
[26,28,24,29,28,0,26,28,25,19,24],
[26,25,23,27,26,25,0,23,25,22,17],
[30,25,21,27,28,23,28,0,27,27,28],
[28,19,22,25,26,26,26,24,0,18,22],
[33,23,27,32,34,32,29,24,33,0,27],
[28,19,23,31,35,27,34,23,29,24,0]])



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
result = np.append(np.array([11, 51, 14, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,30,24,25,24,26,29,28,20,28],
[20,0,23,23,20,26,20,22,22,21,28],
[21,28,0,22,18,29,21,21,26,15,30],
[27,28,29,0,26,30,17,18,26,21,29],
[26,31,33,25,0,32,25,22,28,24,26],
[27,25,22,21,19,0,17,21,24,21,27],
[25,31,30,34,26,34,0,27,28,30,33],
[22,29,30,33,29,30,24,0,28,23,31],
[23,29,25,25,23,27,23,23,0,21,33],
[31,30,36,30,27,30,21,28,30,0,29],
[23,23,21,22,25,24,18,20,18,22,0]])



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
result = np.append(np.array([11, 51, 15, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,20,19,25,13,18,18,22,23,21],
[28,0,17,26,27,19,17,26,19,22,21],
[31,34,0,32,29,22,26,27,23,29,27],
[32,25,19,0,24,21,22,24,26,26,24],
[26,24,22,27,0,22,22,26,22,24,24],
[38,32,29,30,29,0,29,31,33,30,24],
[33,34,25,29,29,22,0,37,32,30,25],
[33,25,24,27,25,20,14,0,23,26,21],
[29,32,28,25,29,18,19,28,0,26,31],
[28,29,22,25,27,21,21,25,25,0,25],
[30,30,24,27,27,27,26,30,20,26,0]])



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
result = np.append(np.array([11, 51, 16, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,27,24,29,22,34,34,24,33,30],
[21,0,23,25,29,24,32,25,23,26,26],
[24,28,0,27,34,25,31,25,17,31,29],
[27,26,24,0,30,30,33,26,24,30,29],
[22,22,17,21,0,22,22,26,18,20,22],
[29,27,26,21,29,0,29,30,28,31,27],
[17,19,20,18,29,22,0,24,23,20,22],
[17,26,26,25,25,21,27,0,21,25,33],
[27,28,34,27,33,23,28,30,0,29,27],
[18,25,20,21,31,20,31,26,22,0,26],
[21,25,22,22,29,24,29,18,24,25,0]])



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
result = np.append(np.array([11, 51, 17, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,25,27,19,20,27,22,19,18,29],
[31,0,31,30,26,26,30,25,22,28,28],
[26,20,0,26,23,19,25,21,19,23,25],
[24,21,25,0,20,22,27,18,17,23,27],
[32,25,28,31,0,30,29,31,28,29,30],
[31,25,32,29,21,0,28,28,23,23,28],
[24,21,26,24,22,23,0,19,21,23,22],
[29,26,30,33,20,23,32,0,24,26,29],
[32,29,32,34,23,28,30,27,0,27,33],
[33,23,28,28,22,28,28,25,24,0,30],
[22,23,26,24,21,23,29,22,18,21,0]])



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
result = np.append(np.array([11, 51, 18, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,21,29,26,31,20,27,31,27,21],
[23,0,19,26,21,33,21,28,27,29,20],
[30,32,0,25,32,28,26,23,29,31,20],
[22,25,26,0,23,24,20,20,27,21,24],
[25,30,19,28,0,27,21,25,24,25,19],
[20,18,23,27,24,0,20,19,26,21,17],
[31,30,25,31,30,31,0,30,32,33,29],
[24,23,28,31,26,32,21,0,28,25,23],
[20,24,22,24,27,25,19,23,0,23,22],
[24,22,20,30,26,30,18,26,28,0,18],
[30,31,31,27,32,34,22,28,29,33,0]])



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
result = np.append(np.array([11, 51, 19, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,28,25,32,17,23,31,28,25,26],
[23,0,21,26,32,19,26,22,26,27,23],
[23,30,0,25,41,26,24,22,28,26,23],
[26,25,26,0,31,22,33,32,29,22,26],
[19,19,10,20,0,11,23,23,19,19,23],
[34,32,25,29,40,0,28,32,30,32,27],
[28,25,27,18,28,23,0,27,24,25,23],
[20,29,29,19,28,19,24,0,24,19,26],
[23,25,23,22,32,21,27,27,0,27,30],
[26,24,25,29,32,19,26,32,24,0,19],
[25,28,28,25,28,24,28,25,21,32,0]])



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
result = np.append(np.array([11, 51, 20, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,33,34,25,36,31,35,27,21,32],
[31,0,25,37,33,34,30,43,33,34,34],
[18,26,0,27,29,23,22,34,18,22,18],
[17,14,24,0,21,25,31,32,10,21,22],
[26,18,22,30,0,26,24,35,32,27,25],
[15,17,28,26,25,0,30,31,15,30,20],
[20,21,29,20,27,21,0,34,23,21,21],
[16,8,17,19,16,20,17,0,25,22,11],
[24,18,33,41,19,36,28,26,0,19,28],
[30,17,29,30,24,21,30,29,32,0,27],
[19,17,33,29,26,31,30,40,23,24,0]])



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
result = np.append(np.array([11, 51, 21, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,20,31,19,21,16,25,33,26,16],
[30,0,24,27,31,25,26,26,31,23,31],
[31,27,0,25,25,28,17,34,30,27,30],
[20,24,26,0,21,21,16,34,32,21,22],
[32,20,26,30,0,30,19,27,29,28,23],
[30,26,23,30,21,0,16,32,36,28,21],
[35,25,34,35,32,35,0,31,35,28,30],
[26,25,17,17,24,19,20,0,29,26,20],
[18,20,21,19,22,15,16,22,0,19,24],
[25,28,24,30,23,23,23,25,32,0,22],
[35,20,21,29,28,30,21,31,27,29,0]])



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
result = np.append(np.array([11, 51, 22, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,16,18,25,19,17,18,20,20,21],
[32,0,24,20,25,28,20,24,24,26,22],
[35,27,0,26,32,27,25,31,26,28,28],
[33,31,25,0,32,25,21,24,29,29,27],
[26,26,19,19,0,24,18,23,22,22,26],
[32,23,24,26,27,0,27,33,22,25,31],
[34,31,26,30,33,24,0,25,34,28,28],
[33,27,20,27,28,18,26,0,25,20,25],
[31,27,25,22,29,29,17,26,0,27,27],
[31,25,23,22,29,26,23,31,24,0,24],
[30,29,23,24,25,20,23,26,24,27,0]])



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
result = np.append(np.array([11, 51, 23, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,22,18,24,20,18,18,21,24,22],
[28,0,26,28,28,29,27,29,33,22,31],
[29,25,0,25,31,26,27,25,26,28,25],
[33,23,26,0,33,26,27,23,27,31,28],
[27,23,20,18,0,24,19,20,25,22,20],
[31,22,25,25,27,0,20,25,26,24,26],
[33,24,24,24,32,31,0,27,24,25,29],
[33,22,26,28,31,26,24,0,29,25,22],
[30,18,25,24,26,25,27,22,0,22,24],
[27,29,23,20,29,27,26,26,29,0,25],
[29,20,26,23,31,25,22,29,27,26,0]])



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
result = np.append(np.array([11, 51, 24, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,31,30,36,40,30,24,51,32,30],
[11,0,32,29,36,20,20,19,34,22,17],
[20,19,0,19,13,21,14,0,35,6,14],
[21,22,32,0,34,32,30,13,34,10,29],
[15,15,38,17,0,17,15,10,30,16,19],
[11,31,30,19,34,0,14,26,35,21,18],
[21,31,37,21,36,37,0,16,42,20,20],
[27,32,51,38,41,25,35,0,39,34,29],
[0,17,16,17,21,16,9,12,0,20,4],
[19,29,45,41,35,30,31,17,31,0,30],
[21,34,37,22,32,33,31,22,47,21,0]])



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
result = np.append(np.array([11, 51, 25, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,32,24,21,24,19,30,25,20,27],
[24,0,28,27,21,25,24,28,27,18,31],
[19,23,0,21,20,24,17,27,23,19,28],
[27,24,30,0,28,28,24,24,25,22,31],
[30,30,31,23,0,31,23,34,32,27,39],
[27,26,27,23,20,0,23,28,29,18,29],
[32,27,34,27,28,28,0,31,31,24,29],
[21,23,24,27,17,23,20,0,23,27,27],
[26,24,28,26,19,22,20,28,0,17,26],
[31,33,32,29,24,33,27,24,34,0,35],
[24,20,23,20,12,22,22,24,25,16,0]])



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
result = np.append(np.array([11, 51, 26, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,26,28,29,23,29,29,28,26,26],
[26,0,25,25,24,24,21,26,24,25,24],
[25,26,0,31,28,31,26,32,28,32,30],
[23,26,20,0,29,23,22,24,26,27,26],
[22,27,23,22,0,25,19,28,23,24,23],
[28,27,20,28,26,0,21,29,23,29,24],
[22,30,25,29,32,30,0,24,30,30,27],
[22,25,19,27,23,22,27,0,29,24,30],
[23,27,23,25,28,28,21,22,0,29,23],
[25,26,19,24,27,22,21,27,22,0,25],
[25,27,21,25,28,27,24,21,28,26,0]])



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
result = np.append(np.array([11, 51, 27, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,26,26,23,33,30,27,31,24,28],
[21,0,23,20,26,32,26,24,34,19,27],
[25,28,0,22,28,32,26,24,33,28,29],
[25,31,29,0,24,31,29,28,33,28,28],
[28,25,23,27,0,31,25,29,33,25,25],
[18,19,19,20,20,0,15,23,27,19,24],
[21,25,25,22,26,36,0,28,33,24,25],
[24,27,27,23,22,28,23,0,32,25,33],
[20,17,18,18,18,24,18,19,0,17,17],
[27,32,23,23,26,32,27,26,34,0,26],
[23,24,22,23,26,27,26,18,34,25,0]])



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
result = np.append(np.array([11, 51, 28, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,27,24,35,29,28,31,36,25,30],
[26,0,22,28,29,22,28,24,32,25,25],
[24,29,0,28,30,30,24,26,29,24,30],
[27,23,23,0,30,25,26,27,34,22,24],
[16,22,21,21,0,23,17,15,25,19,21],
[22,29,21,26,28,0,28,26,30,28,29],
[23,23,27,25,34,23,0,25,28,24,28],
[20,27,25,24,36,25,26,0,29,22,24],
[15,19,22,17,26,21,23,22,0,16,19],
[26,26,27,29,32,23,27,29,35,0,27],
[21,26,21,27,30,22,23,27,32,24,0]])



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
result = np.append(np.array([11, 51, 29, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,31,23,27,27,30,25,24,24,23],
[21,0,21,25,21,20,22,27,20,16,22],
[20,30,0,27,23,25,22,29,22,25,24],
[28,26,24,0,25,28,24,30,29,24,29],
[24,30,28,26,0,32,27,30,30,29,29],
[24,31,26,23,19,0,27,28,24,27,24],
[21,29,29,27,24,24,0,28,27,26,30],
[26,24,22,21,21,23,23,0,25,19,26],
[27,31,29,22,21,27,24,26,0,24,24],
[27,35,26,27,22,24,25,32,27,0,29],
[28,29,27,22,22,27,21,25,27,22,0]])



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
result = np.append(np.array([11, 51, 30, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,23,21,28,24,29,25,22,24,21],
[30,0,24,25,28,27,26,28,24,24,22],
[28,27,0,26,28,29,30,26,26,31,25],
[30,26,25,0,28,27,33,27,25,29,29],
[23,23,23,23,0,24,29,24,22,27,25],
[27,24,22,24,27,0,30,26,26,29,27],
[22,25,21,18,22,21,0,17,23,26,20],
[26,23,25,24,27,25,34,0,20,29,22],
[29,27,25,26,29,25,28,31,0,29,25],
[27,27,20,22,24,22,25,22,22,0,21],
[30,29,26,22,26,24,31,29,26,30,0]])



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
result = np.append(np.array([11, 51, 31, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,27,25,27,34,25,17,23,26,25],
[25,0,37,26,33,42,42,28,33,43,29],
[24,14,0,39,35,34,37,23,15,26,28],
[26,25,12,0,27,33,25,22,23,27,33],
[24,18,16,24,0,24,48,15,19,32,31],
[17,9,17,18,27,0,36,18,9,24,29],
[26,9,14,26,3,15,0,9,2,23,22],
[34,23,28,29,36,33,42,0,13,34,25],
[28,18,36,28,32,42,49,38,0,41,40],
[25,8,25,24,19,27,28,17,10,0,22],
[26,22,23,18,20,22,29,26,11,29,0]])



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
result = np.append(np.array([11, 51, 32, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,31,29,27,27,28,29,21,21,23],
[19,0,24,27,24,18,21,28,27,20,23],
[20,27,0,27,22,25,31,22,26,23,22],
[22,24,24,0,25,18,26,29,26,20,20],
[24,27,29,26,0,27,28,27,22,23,21],
[24,33,26,33,24,0,26,27,25,23,24],
[23,30,20,25,23,25,0,25,19,21,21],
[22,23,29,22,24,24,26,0,24,24,19],
[30,24,25,25,29,26,32,27,0,28,23],
[30,31,28,31,28,28,30,27,23,0,27],
[28,28,29,31,30,27,30,32,28,24,0]])



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
result = np.append(np.array([11, 51, 33, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,28,14,19,34,23,21,20,19,26],
[28,0,28,22,18,33,18,28,27,27,30],
[23,23,0,20,27,30,25,17,26,23,28],
[37,29,31,0,25,38,31,30,32,32,37],
[32,33,24,26,0,33,21,27,37,24,32],
[17,18,21,13,18,0,16,21,15,19,25],
[28,33,26,20,30,35,0,37,31,20,32],
[30,23,34,21,24,30,14,0,24,20,25],
[31,24,25,19,14,36,20,27,0,27,28],
[32,24,28,19,27,32,31,31,24,0,27],
[25,21,23,14,19,26,19,26,23,24,0]])



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
result = np.append(np.array([11, 51, 34, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,18,12,18,21,18,21,12,30,33],
[39,0,18,39,18,39,18,39,18,18,51],
[33,33,0,33,30,33,12,33,12,12,33],
[39,12,18,0,18,39,18,21,18,18,51],
[33,33,21,33,0,33,21,33,12,33,33],
[30,12,18,12,18,0,18,33,12,30,12],
[33,33,39,33,30,33,0,33,12,12,33],
[30,12,18,30,18,18,18,0,30,30,30],
[39,33,39,33,39,39,39,21,0,51,51],
[21,33,39,33,18,21,39,21,0,0,33],
[18,0,18,0,18,39,18,21,0,18,0]])



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
result = np.append(np.array([11, 51, 35, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,26,25,32,27,31,30,31,26,27],
[25,0,27,21,25,25,22,21,22,20,24],
[25,24,0,27,26,27,28,23,26,19,28],
[26,30,24,0,31,23,23,19,26,24,34],
[19,26,25,20,0,24,19,22,23,17,24],
[24,26,24,28,27,0,27,21,24,23,23],
[20,29,23,28,32,24,0,25,26,22,27],
[21,30,28,32,29,30,26,0,28,31,30],
[20,29,25,25,28,27,25,23,0,25,26],
[25,31,32,27,34,28,29,20,26,0,30],
[24,27,23,17,27,28,24,21,25,21,0]])



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
result = np.append(np.array([11, 51, 36, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,24,32,27,20,23,25,29,22,31],
[27,0,17,26,21,20,27,27,21,24,21],
[27,34,0,33,32,23,31,26,36,26,29],
[19,25,18,0,27,23,22,24,27,16,19],
[24,30,19,24,0,24,23,27,31,22,23],
[31,31,28,28,27,0,27,26,30,25,28],
[28,24,20,29,28,24,0,27,31,22,29],
[26,24,25,27,24,25,24,0,33,27,25],
[22,30,15,24,20,21,20,18,0,18,23],
[29,27,25,35,29,26,29,24,33,0,29],
[20,30,22,32,28,23,22,26,28,22,0]])



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
result = np.append(np.array([11, 51, 37, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,17,24,24,19,15,22,8,14,17],
[26,0,21,30,25,22,21,22,18,25,28],
[34,30,0,34,24,20,28,25,13,27,22],
[27,21,17,0,17,18,22,29,7,20,16],
[27,26,27,34,0,31,30,28,15,30,28],
[32,29,31,33,20,0,36,23,27,32,29],
[36,30,23,29,21,15,0,24,11,22,33],
[29,29,26,22,23,28,27,0,17,26,25],
[43,33,38,44,36,24,40,34,0,42,45],
[37,26,24,31,21,19,29,25,9,0,22],
[34,23,29,35,23,22,18,26,6,29,0]])



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
result = np.append(np.array([11, 51, 38, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,25,27,29,26,20,27,26,32,24],
[34,0,23,32,39,32,28,40,33,33,33],
[26,28,0,26,27,25,34,32,22,36,29],
[24,19,25,0,30,22,31,29,31,32,30],
[22,12,24,21,0,16,16,23,18,26,16],
[25,19,26,29,35,0,28,27,32,29,29],
[31,23,17,20,35,23,0,25,30,23,25],
[24,11,19,22,28,24,26,0,29,28,30],
[25,18,29,20,33,19,21,22,0,27,15],
[19,18,15,19,25,22,28,23,24,0,18],
[27,18,22,21,35,22,26,21,36,33,0]])



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
result = np.append(np.array([11, 51, 39, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,17,30,36,17,30,17,17,26,38],
[34,0,21,40,45,15,28,34,32,15,38],
[34,30,0,51,30,30,24,45,24,39,45],
[21,11,0,0,17,0,11,26,11,15,32],
[15,6,21,34,0,15,34,21,6,15,38],
[34,36,21,51,36,0,45,45,30,28,51],
[21,23,27,40,17,6,0,38,17,21,38],
[34,17,6,25,30,6,13,0,11,15,32],
[34,19,27,40,45,21,34,40,0,21,32],
[25,36,12,36,36,23,30,36,30,0,36],
[13,13,6,19,13,0,13,19,19,15,0]])



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
result = np.append(np.array([11, 51, 40, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,14,11,18,20,17,17,23,20,30],
[25,0,23,11,13,23,33,39,30,33,27],
[37,28,0,19,22,27,39,36,31,13,25],
[40,40,32,0,25,42,39,42,39,31,34],
[33,38,29,26,0,32,29,35,26,23,42],
[31,28,24,9,19,0,28,33,25,25,25],
[34,18,12,12,22,23,0,24,9,16,19],
[34,12,15,9,16,18,27,0,21,18,19],
[28,21,20,12,25,26,42,30,0,16,25],
[31,18,38,20,28,26,35,33,35,0,36],
[21,24,26,17,9,26,32,32,26,15,0]])



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
result = np.append(np.array([11, 51, 41, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,32,30,29,24,30,35,33,21,31],
[16,0,24,23,15,26,18,29,15,14,14],
[19,27,0,19,17,20,19,21,18,17,19],
[21,28,32,0,25,23,21,23,28,26,28],
[22,36,34,26,0,28,29,35,31,24,22],
[27,25,31,28,23,0,32,34,25,24,25],
[21,33,32,30,22,19,0,32,30,23,26],
[16,22,30,28,16,17,19,0,28,17,13],
[18,36,33,23,20,26,21,23,0,13,26],
[30,37,34,25,27,27,28,34,38,0,23],
[20,37,32,23,29,26,25,38,25,28,0]])



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
result = np.append(np.array([11, 51, 42, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,26,17,32,34,38,39,24,17,32],
[25,0,18,20,39,29,19,33,13,28,35],
[25,33,0,26,26,35,35,32,30,32,33],
[34,31,25,0,29,31,42,25,18,25,19],
[19,12,25,22,0,37,14,10,10,26,19],
[17,22,16,20,14,0,23,7,12,23,9],
[13,32,16,9,37,28,0,33,18,17,26],
[12,18,19,26,41,44,18,0,13,28,35],
[27,38,21,33,41,39,33,38,0,32,26],
[34,23,19,26,25,28,34,23,19,0,26],
[19,16,18,32,32,42,25,16,25,25,0]])



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
result = np.append(np.array([11, 51, 43, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,17,17,16,20,14,10,20,15,12],
[33,0,31,28,29,35,32,23,30,32,26],
[34,20,0,26,32,31,32,31,26,34,28],
[34,23,25,0,24,37,21,21,23,26,27],
[35,22,19,27,0,36,21,24,25,28,29],
[31,16,20,14,15,0,14,20,17,26,18],
[37,19,19,30,30,37,0,28,25,31,25],
[41,28,20,30,27,31,23,0,29,30,26],
[31,21,25,28,26,34,26,22,0,37,32],
[36,19,17,25,23,25,20,21,14,0,22],
[39,25,23,24,22,33,26,25,19,29,0]])



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
result = np.append(np.array([11, 51, 44, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,17,24,35,9,27,23,13,29,39],
[23,0,17,12,20,21,26,20,22,25,34],
[34,34,0,30,49,31,24,31,31,29,39],
[27,39,21,0,47,30,29,25,17,32,30],
[16,31,2,4,0,14,10,10,7,27,24],
[42,30,20,21,37,0,35,35,20,29,44],
[24,25,27,22,41,16,0,30,19,30,31],
[28,31,20,26,41,16,21,0,18,29,22],
[38,29,20,34,44,31,32,33,0,21,34],
[22,26,22,19,24,22,21,22,30,0,28],
[12,17,12,21,27,7,20,29,17,23,0]])



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
result = np.append(np.array([11, 51, 45, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,13,50,27,24,39,38,36,15,51],
[12,0,12,36,26,24,38,12,24,14,36],
[38,39,0,50,27,24,39,38,36,27,51],
[1,15,1,0,15,12,27,26,12,15,39],
[24,25,24,36,0,24,24,12,36,27,36],
[27,27,27,39,27,0,27,26,25,15,39],
[12,13,12,24,27,24,0,12,24,15,25],
[13,39,13,25,39,25,39,0,25,15,25],
[15,27,15,39,15,26,27,26,0,15,39],
[36,37,24,36,24,36,36,36,36,0,36],
[0,15,0,12,15,12,26,26,12,15,0]])



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
result = np.append(np.array([11, 51, 46, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,25,30,32,30,31,26,31,33,24],
[25,0,24,33,23,28,23,20,19,25,24],
[26,27,0,25,26,25,23,22,20,31,26],
[21,18,26,0,28,22,23,19,19,23,24],
[19,28,25,23,0,22,26,28,22,29,28],
[21,23,26,29,29,0,21,24,16,27,17],
[20,28,28,28,25,30,0,25,22,31,22],
[25,31,29,32,23,27,26,0,17,32,28],
[20,32,31,32,29,35,29,34,0,36,30],
[18,26,20,28,22,24,20,19,15,0,22],
[27,27,25,27,23,34,29,23,21,29,0]])



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
result = np.append(np.array([11, 51, 47, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,23,28,20,21,26,24,26,24,23],
[28,0,26,25,19,26,26,29,31,26,30],
[28,25,0,27,22,22,27,24,29,26,27],
[23,26,24,0,19,21,30,23,25,23,23],
[31,32,29,32,0,23,30,29,28,25,33],
[30,25,29,30,28,0,27,27,31,26,30],
[25,25,24,21,21,24,0,19,29,20,23],
[27,22,27,28,22,24,32,0,27,24,26],
[25,20,22,26,23,20,22,24,0,21,23],
[27,25,25,28,26,25,31,27,30,0,26],
[28,21,24,28,18,21,28,25,28,25,0]])



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
result = np.append(np.array([11, 51, 48, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,32,19,17,18,18,22,15,16,23],
[24,0,35,30,26,21,24,23,18,26,29],
[19,16,0,26,16,13,15,21,14,16,19],
[32,21,25,0,23,27,25,27,27,24,25],
[34,25,35,28,0,26,29,29,24,23,27],
[33,30,38,24,25,0,29,24,24,23,17],
[33,27,36,26,22,22,0,23,26,29,33],
[29,28,30,24,22,27,28,0,19,24,26],
[36,33,37,24,27,27,25,32,0,31,28],
[35,25,35,27,28,28,22,27,20,0,22],
[28,22,32,26,24,34,18,25,23,29,0]])



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
result = np.append(np.array([11, 51, 49, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,18,31,14,23,23,20,23,29,14],
[20,0,15,15,17,22,33,21,18,18,6],
[33,36,0,25,25,35,32,32,31,36,27],
[20,36,26,0,16,26,28,19,25,25,18],
[37,34,26,35,0,34,26,22,36,30,20],
[28,29,16,25,17,0,23,19,20,16,17],
[28,18,19,23,25,28,0,20,24,27,12],
[31,30,19,32,29,32,31,0,34,26,13],
[28,33,20,26,15,31,27,17,0,24,15],
[22,33,15,26,21,35,24,25,27,0,18],
[37,45,24,33,31,34,39,38,36,33,0]])



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
result = np.append(np.array([11, 51, 50, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,23,31,23,20,27,23,30,19,26],
[31,0,21,32,30,26,24,22,40,28,33],
[28,30,0,27,26,29,23,23,35,27,29],
[20,19,24,0,18,15,19,22,34,25,17],
[28,21,25,33,0,20,20,21,31,25,22],
[31,25,22,36,31,0,27,29,40,23,27],
[24,27,28,32,31,24,0,25,34,28,25],
[28,29,28,29,30,22,26,0,28,26,25],
[21,11,16,17,20,11,17,23,0,14,19],
[32,23,24,26,26,28,23,25,37,0,26],
[25,18,22,34,29,24,26,26,32,25,0]])



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
result = np.append(np.array([11, 51, 51, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,23,25,22,23,24,24,20,21,22],
[25,0,23,24,22,25,26,21,22,21,24],
[28,28,0,24,22,20,23,25,22,16,26],
[26,27,27,0,17,27,29,31,24,27,28],
[29,29,29,34,0,23,28,26,25,26,33],
[28,26,31,24,28,0,29,28,28,25,32],
[27,25,28,22,23,22,0,22,18,23,29],
[27,30,26,20,25,23,29,0,20,26,33],
[31,29,29,27,26,23,33,31,0,24,32],
[30,30,35,24,25,26,28,25,27,0,32],
[29,27,25,23,18,19,22,18,19,19,0]])



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
result = np.append(np.array([11, 51, 52, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,24,26,30,23,26,27,22,22,18],
[21,0,16,16,17,13,18,19,18,17,20],
[27,35,0,24,32,21,28,26,29,19,26],
[25,35,27,0,35,20,22,25,23,22,27],
[21,34,19,16,0,22,22,23,22,16,21],
[28,38,30,31,29,0,26,27,24,22,26],
[25,33,23,29,29,25,0,21,20,24,19],
[24,32,25,26,28,24,30,0,20,24,17],
[29,33,22,28,29,27,31,31,0,18,23],
[29,34,32,29,35,29,27,27,33,0,18],
[33,31,25,24,30,25,32,34,28,33,0]])



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
result = np.append(np.array([11, 51, 53, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,31,24,42,11,32,29,32,41,25],
[15,0,13,32,23,9,28,25,22,36,29],
[20,38,0,28,36,30,29,35,31,41,33],
[27,19,23,0,25,17,26,31,27,37,24],
[9,28,15,26,0,3,15,18,11,30,24],
[40,42,21,34,48,0,27,33,37,44,31],
[19,23,22,25,36,24,0,33,32,39,26],
[22,26,16,20,33,18,18,0,20,33,16],
[19,29,20,24,40,14,19,31,0,34,18],
[10,15,10,14,21,7,12,18,17,0,14],
[26,22,18,27,27,20,25,35,33,37,0]])



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
result = np.append(np.array([11, 51, 54, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,24,30,24,26,23,28,26,27,27],
[24,0,26,31,29,23,26,32,24,27,29],
[27,25,0,29,29,29,25,34,24,22,27],
[21,20,22,0,24,24,16,24,21,24,21],
[27,22,22,27,0,24,22,26,25,28,23],
[25,28,22,27,27,0,20,30,25,25,28],
[28,25,26,35,29,31,0,29,27,29,27],
[23,19,17,27,25,21,22,0,23,24,29],
[25,27,27,30,26,26,24,28,0,29,27],
[24,24,29,27,23,26,22,27,22,0,23],
[24,22,24,30,28,23,24,22,24,28,0]])



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
result = np.append(np.array([11, 51, 55, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,22,27,24,22,36,26,28,25,29],
[19,0,15,25,26,22,32,22,31,23,26],
[29,36,0,34,24,21,37,38,34,33,31],
[24,26,17,0,23,23,30,24,25,23,31],
[27,25,27,28,0,28,29,25,31,27,27],
[29,29,30,28,23,0,39,29,31,26,25],
[15,19,14,21,22,12,0,16,24,22,20],
[25,29,13,27,26,22,35,0,26,24,29],
[23,20,17,26,20,20,27,25,0,24,24],
[26,28,18,28,24,25,29,27,27,0,24],
[22,25,20,20,24,26,31,22,27,27,0]])



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
result = np.append(np.array([11, 51, 56, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,22,21,32,25,31,26,25,29,27],
[24,0,27,24,30,25,31,27,27,26,24],
[29,24,0,25,38,31,32,22,25,25,27],
[30,27,26,0,33,24,25,28,26,22,22],
[19,21,13,18,0,22,25,16,15,23,14],
[26,26,20,27,29,0,23,20,24,22,20],
[20,20,19,26,26,28,0,21,25,26,19],
[25,24,29,23,35,31,30,0,30,28,24],
[26,24,26,25,36,27,26,21,0,26,20],
[22,25,26,29,28,29,25,23,25,0,25],
[24,27,24,29,37,31,32,27,31,26,0]])



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
result = np.append(np.array([11, 51, 57, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,24,41,41,41,24,31,24,24,27],
[27,0,34,24,27,24,24,7,31,51,3],
[27,17,0,24,27,24,17,7,31,51,3],
[10,27,27,0,44,41,27,34,27,27,27],
[10,24,24,7,0,41,24,31,24,27,3],
[10,27,27,10,10,0,3,34,27,34,3],
[27,27,34,24,27,48,0,34,31,34,3],
[20,44,44,17,20,17,17,0,41,44,20],
[27,20,20,24,27,24,20,10,0,27,3],
[27,0,0,24,24,17,17,7,24,0,3],
[24,48,48,24,48,48,48,31,48,48,0]])



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
result = np.append(np.array([11, 51, 58, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,22,9,13,25,10,23,14,20,33],
[34,0,34,16,22,26,29,34,29,35,28],
[29,17,0,11,12,18,10,42,19,18,29],
[42,35,40,0,30,30,22,31,27,31,42],
[38,29,39,21,0,29,21,32,26,24,32],
[26,25,33,21,22,0,20,31,25,26,31],
[41,22,41,29,30,31,0,41,24,36,43],
[28,17,9,20,19,20,10,0,13,17,29],
[37,22,32,24,25,26,27,38,0,26,31],
[31,16,33,20,27,25,15,34,25,0,31],
[18,23,22,9,19,20,8,22,20,20,0]])



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
result = np.append(np.array([11, 51, 59, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,31,30,34,28,16,23,28,21,23],
[20,0,29,27,18,27,25,35,26,20,25],
[20,22,0,28,30,28,22,32,23,22,19],
[21,24,23,0,25,22,20,26,26,23,25],
[17,33,21,26,0,23,16,27,23,14,21],
[23,24,23,29,28,0,31,28,26,25,29],
[35,26,29,31,35,20,0,29,24,15,31],
[28,16,19,25,24,23,22,0,28,22,30],
[23,25,28,25,28,25,27,23,0,27,29],
[30,31,29,28,37,26,36,29,24,0,36],
[28,26,32,26,30,22,20,21,22,15,0]])



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
result = np.append(np.array([11, 51, 60, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,20,14,40,36,25,20,28,22,17],
[34,0,23,30,40,32,26,39,26,22,33],
[31,28,0,33,37,35,29,32,29,25,30],
[37,21,18,0,39,27,24,32,22,23,23],
[11,11,14,12,0,23,5,15,14,8,10],
[15,19,16,24,28,0,20,19,13,3,14],
[26,25,22,27,46,31,0,32,26,12,17],
[31,12,19,19,36,32,19,0,26,27,21],
[23,25,22,29,37,38,25,25,0,15,25],
[29,29,26,28,43,48,39,24,36,0,31],
[34,18,21,28,41,37,34,30,26,20,0]])



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
result = np.append(np.array([11, 51, 61, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,27,22,26,17,26,27,22,21,16],
[26,0,27,25,26,24,32,34,24,30,25],
[24,24,0,25,29,27,32,33,28,28,28],
[29,26,26,0,27,22,26,28,24,23,28],
[25,25,22,24,0,24,27,31,21,19,26],
[34,27,24,29,27,0,26,32,28,25,30],
[25,19,19,25,24,25,0,30,27,23,23],
[24,17,18,23,20,19,21,0,24,19,23],
[29,27,23,27,30,23,24,27,0,28,19],
[30,21,23,28,32,26,28,32,23,0,24],
[35,26,23,23,25,21,28,28,32,27,0]])



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
result = np.append(np.array([11, 51, 62, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,48,22,41,33,25,51,48,51,48],
[15,0,26,15,26,26,40,18,37,29,41],
[3,25,0,15,15,29,25,18,37,44,26],
[29,36,36,0,41,14,36,29,48,36,41],
[10,25,36,10,0,21,25,25,40,36,51],
[18,25,22,37,30,0,40,40,37,51,41],
[26,11,26,15,26,11,0,26,48,29,41],
[0,33,33,22,26,11,25,0,37,51,41],
[3,14,14,3,11,14,3,14,0,14,14],
[0,22,7,15,15,0,22,0,37,0,15],
[3,10,25,10,0,10,10,10,37,36,0]])



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
result = np.append(np.array([11, 51, 63, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,23,29,24,22,22,29,30,26,24],
[25,0,21,29,30,27,24,31,31,31,31],
[28,30,0,26,20,17,28,34,26,30,25],
[22,22,25,0,19,19,24,25,25,24,24],
[27,21,31,32,0,29,23,28,26,28,31],
[29,24,34,32,22,0,27,30,30,30,32],
[29,27,23,27,28,24,0,30,28,29,28],
[22,20,17,26,23,21,21,0,35,31,27],
[21,20,25,26,25,21,23,16,0,25,25],
[25,20,21,27,23,21,22,20,26,0,22],
[27,20,26,27,20,19,23,24,26,29,0]])



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
result = np.append(np.array([11, 51, 64, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,37,28,32,33,25,34,28,35,27],
[18,0,36,30,27,32,15,21,17,27,22],
[14,15,0,19,29,24,14,24,21,24,17],
[23,21,32,0,24,28,17,30,20,33,22],
[19,24,22,27,0,26,25,28,28,25,20],
[18,19,27,23,25,0,14,22,13,29,12],
[26,36,37,34,26,37,0,28,24,27,23],
[17,30,27,21,23,29,23,0,19,26,19],
[23,34,30,31,23,38,27,32,0,34,24],
[16,24,27,18,26,22,24,25,17,0,26],
[24,29,34,29,31,39,28,32,27,25,0]])



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
result = np.append(np.array([11, 51, 65, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,11,23,19,10,21,21,21,23,22],
[32,0,28,29,25,23,23,19,22,24,27],
[40,23,0,32,31,26,27,29,23,25,28],
[28,22,19,0,18,18,20,23,16,24,23],
[32,26,20,33,0,17,21,25,21,22,27],
[41,28,25,33,34,0,38,35,23,26,29],
[30,28,24,31,30,13,0,24,23,20,25],
[30,32,22,28,26,16,27,0,23,23,23],
[30,29,28,35,30,28,28,28,0,25,27],
[28,27,26,27,29,25,31,28,26,0,25],
[29,24,23,28,24,22,26,28,24,26,0]])



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
result = np.append(np.array([11, 51, 66, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,31,29,18,28,33,25,19,15,32],
[23,0,23,25,14,25,30,20,8,18,27],
[20,28,0,27,20,28,29,24,17,17,25],
[22,26,24,0,14,23,25,25,15,14,31],
[33,37,31,37,0,40,38,31,31,24,39],
[23,26,23,28,11,0,21,20,22,19,18],
[18,21,22,26,13,30,0,13,13,20,31],
[26,31,27,26,20,31,38,0,19,19,33],
[32,43,34,36,20,29,38,32,0,30,38],
[36,33,34,37,27,32,31,32,21,0,40],
[19,24,26,20,12,33,20,18,13,11,0]])



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
result = np.append(np.array([11, 51, 67, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,0,0,0,31,21,39,10,10,21],
[41,0,29,33,29,39,21,39,31,31,29],
[51,22,0,12,20,39,31,51,22,22,33],
[51,18,39,0,8,39,39,39,10,10,29],
[51,22,31,43,0,39,31,51,31,43,21],
[20,12,12,12,12,0,21,30,22,22,33],
[30,30,20,12,20,30,0,30,22,22,41],
[12,12,0,12,0,21,21,0,10,10,21],
[41,20,29,41,20,29,29,41,0,51,29],
[41,20,29,41,8,29,29,41,0,0,29],
[30,22,18,22,30,18,10,30,22,22,0]])



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
result = np.append(np.array([11, 51, 68, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,24,16,21,26,21,21,25,17,18],
[25,0,23,20,24,25,24,20,24,16,20],
[27,28,0,22,25,28,21,23,27,18,20],
[35,31,29,0,27,32,28,29,31,25,30],
[30,27,26,24,0,30,22,25,26,20,25],
[25,26,23,19,21,0,18,18,26,17,21],
[30,27,30,23,29,33,0,25,29,26,23],
[30,31,28,22,26,33,26,0,31,19,23],
[26,27,24,20,25,25,22,20,0,15,23],
[34,35,33,26,31,34,25,32,36,0,29],
[33,31,31,21,26,30,28,28,28,22,0]])



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
result = np.append(np.array([11, 51, 69, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,28,31,25,28,23,21,27,35,32],
[16,0,26,27,29,29,21,28,24,36,32],
[23,25,0,24,28,27,26,22,22,30,30],
[20,24,27,0,28,22,22,22,19,30,33],
[26,22,23,23,0,23,25,27,26,31,31],
[23,22,24,29,28,0,24,32,23,33,30],
[28,30,25,29,26,27,0,35,30,33,31],
[30,23,29,29,24,19,16,0,24,29,34],
[24,27,29,32,25,28,21,27,0,28,35],
[16,15,21,21,20,18,18,22,23,0,28],
[19,19,21,18,20,21,20,17,16,23,0]])



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
result = np.append(np.array([11, 51, 70, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,21,26,31,20,24,29,18,34,30],
[15,0,21,16,19,9,17,24,13,24,23],
[30,30,0,24,33,17,30,29,29,28,33],
[25,35,27,0,32,29,23,31,26,27,35],
[20,32,18,19,0,22,15,19,14,22,31],
[31,42,34,22,29,0,31,23,24,26,40],
[27,34,21,28,36,20,0,37,27,27,27],
[22,27,22,20,32,28,14,0,20,21,27],
[33,38,22,25,37,27,24,31,0,31,38],
[17,27,23,24,29,25,24,30,20,0,29],
[21,28,18,16,20,11,24,24,13,22,0]])



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
result = np.append(np.array([11, 51, 71, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,27,19,26,22,20,21,25,17,28],
[32,0,35,33,41,23,34,26,34,30,37],
[24,16,0,23,23,8,23,13,17,14,24],
[32,18,28,0,31,19,32,21,24,18,28],
[25,10,28,20,0,17,21,21,23,22,32],
[29,28,43,32,34,0,28,32,24,30,38],
[31,17,28,19,30,23,0,22,20,18,30],
[30,25,38,30,30,19,29,0,23,17,36],
[26,17,34,27,28,27,31,28,0,23,32],
[34,21,37,33,29,21,33,34,28,0,32],
[23,14,27,23,19,13,21,15,19,19,0]])



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
result = np.append(np.array([11, 51, 72, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,33,38,26,23,29,33,27,23,30],
[24,0,29,31,24,22,22,27,24,25,34],
[18,22,0,29,22,21,26,26,23,18,28],
[13,20,22,0,22,13,14,24,12,15,18],
[25,27,29,29,0,22,24,27,22,26,32],
[28,29,30,38,29,0,31,30,24,22,32],
[22,29,25,37,27,20,0,27,24,19,28],
[18,24,25,27,24,21,24,0,23,27,28],
[24,27,28,39,29,27,27,28,0,24,28],
[28,26,33,36,25,29,32,24,27,0,33],
[21,17,23,33,19,19,23,23,23,18,0]])



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
result = np.append(np.array([11, 51, 73, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,25,26,22,27,29,27,24,31,26],
[28,0,32,25,31,28,33,29,29,31,31],
[26,19,0,25,25,23,31,29,24,31,27],
[25,26,26,0,26,24,25,29,25,33,24],
[29,20,26,25,0,30,28,30,28,33,28],
[24,23,28,27,21,0,23,26,25,31,24],
[22,18,20,26,23,28,0,25,26,31,28],
[24,22,22,22,21,25,26,0,20,23,25],
[27,22,27,26,23,26,25,31,0,28,24],
[20,20,20,18,18,20,20,28,23,0,23],
[25,20,24,27,23,27,23,26,27,28,0]])



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
result = np.append(np.array([11, 51, 74, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,26,37,34,27,26,32,32,30,26],
[26,0,26,25,29,31,25,36,34,24,34],
[25,25,0,34,40,24,24,33,32,30,28],
[14,26,17,0,34,31,24,37,40,29,31],
[17,22,11,17,0,17,22,20,24,25,7],
[24,20,27,20,34,0,17,31,23,22,28],
[25,26,27,27,29,34,0,35,28,20,28],
[19,15,18,14,31,20,16,0,23,22,15],
[19,17,19,11,27,28,23,28,0,18,27],
[21,27,21,22,26,29,31,29,33,0,27],
[25,17,23,20,44,23,23,36,24,24,0]])



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
result = np.append(np.array([11, 51, 75, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,26,23,31,17,18,24,19,19,17],
[28,0,27,24,29,15,24,24,23,29,13],
[25,24,0,18,25,14,20,20,17,25,14],
[28,27,33,0,27,17,21,23,18,32,22],
[20,22,26,24,0,18,18,18,17,19,14],
[34,36,37,34,33,0,23,29,25,30,21],
[33,27,31,30,33,28,0,32,25,33,30],
[27,27,31,28,33,22,19,0,24,26,23],
[32,28,34,33,34,26,26,27,0,34,23],
[32,22,26,19,32,21,18,25,17,0,18],
[34,38,37,29,37,30,21,28,28,33,0]])



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
result = np.append(np.array([11, 51, 76, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,30,25,23,20,22,23,30,30,23],
[32,0,24,35,25,33,22,17,25,31,31],
[21,27,0,26,21,21,31,31,26,35,18],
[26,16,25,0,19,13,13,17,24,31,25],
[28,26,30,32,0,19,24,21,26,34,18],
[31,18,30,38,32,0,21,22,26,31,26],
[29,29,20,38,27,30,0,15,30,28,24],
[28,34,20,34,30,29,36,0,34,31,30],
[21,26,25,27,25,25,21,17,0,20,20],
[21,20,16,20,17,20,23,20,31,0,17],
[28,20,33,26,33,25,27,21,31,34,0]])



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
result = np.append(np.array([11, 51, 77, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,19,34,29,20,30,28,26,28,13],
[24,0,23,33,27,27,28,34,18,28,20],
[32,28,0,29,26,25,24,38,20,24,29],
[17,18,22,0,28,19,23,22,22,34,22],
[22,24,25,23,0,20,28,31,21,30,14],
[31,24,26,32,31,0,26,28,21,32,29],
[21,23,27,28,23,25,0,23,22,27,22],
[23,17,13,29,20,23,28,0,21,28,20],
[25,33,31,29,30,30,29,30,0,31,25],
[23,23,27,17,21,19,24,23,20,0,21],
[38,31,22,29,37,22,29,31,26,30,0]])



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
result = np.append(np.array([11, 51, 78, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,16,12,15,10,27,24,25,26,22],
[22,0,20,20,19,15,30,21,17,32,28],
[35,31,0,29,27,30,30,25,30,32,38],
[39,31,22,0,28,28,26,23,28,30,39],
[36,32,24,23,0,25,32,24,23,37,35],
[41,36,21,23,26,0,33,29,31,36,33],
[24,21,21,25,19,18,0,27,25,29,30],
[27,30,26,28,27,22,24,0,25,26,30],
[26,34,21,23,28,20,26,26,0,32,27],
[25,19,19,21,14,15,22,25,19,0,31],
[29,23,13,12,16,18,21,21,24,20,0]])



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
result = np.append(np.array([11, 51, 79, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,17,24,26,27,20,22,28,30,23],
[23,0,17,24,28,26,27,17,31,24,17],
[34,34,0,35,32,30,26,25,37,37,29],
[27,27,16,0,30,26,23,21,28,30,17],
[25,23,19,21,0,28,21,20,25,31,16],
[24,25,21,25,23,0,21,23,30,32,23],
[31,24,25,28,30,30,0,26,32,31,22],
[29,34,26,30,31,28,25,0,34,34,27],
[23,20,14,23,26,21,19,17,0,24,19],
[21,27,14,21,20,19,20,17,27,0,19],
[28,34,22,34,35,28,29,24,32,32,0]])



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
result = np.append(np.array([11, 51, 80, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,30,21,30,33,24,23,30,18,25],
[24,0,18,21,32,23,36,21,20,14,32],
[21,33,0,22,37,25,35,32,26,26,32],
[30,30,29,0,36,32,34,29,27,18,33],
[21,19,14,15,0,23,20,15,19,13,23],
[18,28,26,19,28,0,22,18,28,15,27],
[27,15,16,17,31,29,0,14,22,14,26],
[28,30,19,22,36,33,37,0,34,24,25],
[21,31,25,24,32,23,29,17,0,23,27],
[33,37,25,33,38,36,37,27,28,0,34],
[26,19,19,18,28,24,25,26,24,17,0]])



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
result = np.append(np.array([11, 51, 81, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,28,40,23,37,21,29,34,30,42],
[11,0,13,25,12,32,6,14,25,26,31],
[23,38,0,36,30,40,26,36,35,30,34],
[11,26,15,0,16,29,10,23,27,17,38],
[28,39,21,35,0,36,15,28,30,37,32],
[14,19,11,22,15,0,7,21,27,21,28],
[30,45,25,41,36,44,0,42,45,41,44],
[22,37,15,28,23,30,9,0,23,30,39],
[17,26,16,24,21,24,6,28,0,21,39],
[21,25,21,34,14,30,10,21,30,0,32],
[9,20,17,13,19,23,7,12,12,19,0]])



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
result = np.append(np.array([11, 51, 82, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,37,29,28,31,29,35,34,37,31],
[26,0,35,23,28,30,20,30,30,19,34],
[14,16,0,20,27,18,12,28,23,17,29],
[22,28,31,0,33,32,21,36,25,25,35],
[23,23,24,18,0,20,19,27,23,25,21],
[20,21,33,19,31,0,15,27,23,13,32],
[22,31,39,30,32,36,0,27,31,25,35],
[16,21,23,15,24,24,24,0,17,17,18],
[17,21,28,26,28,28,20,34,0,24,33],
[14,32,34,26,26,38,26,34,27,0,39],
[20,17,22,16,30,19,16,33,18,12,0]])



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
result = np.append(np.array([11, 51, 83, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,30,30,27,20,14,32,19,20,27],
[27,0,20,20,28,26,19,23,22,27,21],
[21,31,0,22,27,26,16,30,16,28,23],
[21,31,29,0,25,20,27,39,28,31,19],
[24,23,24,26,0,23,20,38,20,23,15],
[31,25,25,31,28,0,20,36,20,26,21],
[37,32,35,24,31,31,0,33,33,25,26],
[19,28,21,12,13,15,18,0,13,18,19],
[32,29,35,23,31,31,18,38,0,19,20],
[31,24,23,20,28,25,26,33,32,0,22],
[24,30,28,32,36,30,25,32,31,29,0]])



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
result = np.append(np.array([11, 51, 84, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,28,18,25,16,16,16,28,18,18],
[29,0,22,14,23,16,35,19,28,30,21],
[23,29,0,13,28,32,22,16,34,27,9],
[33,37,38,0,32,32,32,26,45,32,7],
[26,28,23,19,0,19,22,31,17,39,14],
[35,35,19,19,32,0,19,28,19,31,25],
[35,16,29,19,29,32,0,25,19,32,7],
[35,32,35,25,20,23,26,0,25,31,32],
[23,23,17,6,34,32,32,26,0,27,9],
[33,21,24,19,12,20,19,20,24,0,25],
[33,30,42,44,37,26,44,19,42,26,0]])



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
result = np.append(np.array([11, 51, 85, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,37,33,42,22,32,29,30,35,24],
[21,0,27,26,31,14,30,21,29,26,19],
[14,24,0,33,36,27,29,19,33,32,27],
[18,25,18,0,37,19,25,26,29,19,21],
[9,20,15,14,0,17,23,22,23,10,19],
[29,37,24,32,34,0,36,24,26,22,24],
[19,21,22,26,28,15,0,17,26,23,18],
[22,30,32,25,29,27,34,0,36,30,28],
[21,22,18,22,28,25,25,15,0,17,13],
[16,25,19,32,41,29,28,21,34,0,28],
[27,32,24,30,32,27,33,23,38,23,0]])



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
result = np.append(np.array([11, 51, 86, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,30,21,20,15,8,18,18,21,16],
[39,0,33,29,19,26,17,19,18,31,21],
[21,18,0,26,20,18,20,12,18,19,15],
[30,22,25,0,27,23,17,8,27,32,19],
[31,32,31,24,0,27,27,27,25,31,18],
[36,25,33,28,24,0,27,24,18,27,29],
[43,34,31,34,24,24,0,23,29,41,20],
[33,32,39,43,24,27,28,0,35,33,28],
[33,33,33,24,26,33,22,16,0,37,22],
[30,20,32,19,20,24,10,18,14,0,21],
[35,30,36,32,33,22,31,23,29,30,0]])



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
result = np.append(np.array([11, 51, 87, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,29,22,23,26,31,30,27,29,31],
[24,0,23,20,24,31,22,30,27,26,31],
[22,28,0,21,26,31,23,32,28,32,30],
[29,31,30,0,28,35,23,33,33,36,32],
[28,27,25,23,0,32,24,34,27,35,27],
[25,20,20,16,19,0,17,31,20,28,25],
[20,29,28,28,27,34,0,34,32,26,32],
[21,21,19,18,17,20,17,0,27,26,32],
[24,24,23,18,24,31,19,24,0,28,28],
[22,25,19,15,16,23,25,25,23,0,24],
[20,20,21,19,24,26,19,19,23,27,0]])



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
result = np.append(np.array([11, 51, 88, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,29,27,21,25,16,19,21,27,45],
[29,0,32,19,16,22,23,29,30,27,27],
[22,19,0,14,16,15,30,8,26,17,21],
[24,32,37,0,18,27,30,16,22,26,45],
[30,35,35,33,0,26,22,30,35,25,34],
[26,29,36,24,25,0,30,21,38,30,36],
[35,28,21,21,29,21,0,19,21,25,34],
[32,22,43,35,21,30,32,0,25,29,43],
[30,21,25,29,16,13,30,26,0,26,36],
[24,24,34,25,26,21,26,22,25,0,28],
[6,24,30,6,17,15,17,8,15,23,0]])



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
result = np.append(np.array([11, 51, 89, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,25,25,27,31,30,31,27,24,34],
[25,0,32,29,32,30,31,31,27,28,34],
[26,19,0,27,24,24,22,21,25,23,24],
[26,22,24,0,25,25,24,18,25,21,25],
[24,19,27,26,0,28,27,25,23,24,27],
[20,21,27,26,23,0,27,23,20,20,26],
[21,20,29,27,24,24,0,26,30,23,26],
[20,20,30,33,26,28,25,0,22,24,29],
[24,24,26,26,28,31,21,29,0,24,29],
[27,23,28,30,27,31,28,27,27,0,31],
[17,17,27,26,24,25,25,22,22,20,0]])



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
result = np.append(np.array([11, 51, 90, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,27,28,30,29,29,23,34,38,27],
[25,0,25,24,24,29,24,27,32,29,25],
[24,26,0,29,36,31,29,25,33,31,32],
[23,27,22,0,33,31,30,33,35,27,25],
[21,27,15,18,0,25,24,20,35,32,28],
[22,22,20,20,26,0,27,30,29,25,25],
[22,27,22,21,27,24,0,22,29,31,30],
[28,24,26,18,31,21,29,0,31,32,28],
[17,19,18,16,16,22,22,20,0,19,15],
[13,22,20,24,19,26,20,19,32,0,23],
[24,26,19,26,23,26,21,23,36,28,0]])



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
result = np.append(np.array([11, 51, 91, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,16,20,27,28,24,24,21,17,17],
[25,0,13,23,22,21,22,24,18,21,18],
[35,38,0,28,27,32,30,28,28,23,20],
[31,28,23,0,24,27,29,27,22,15,25],
[24,29,24,27,0,25,27,22,22,11,18],
[23,30,19,24,26,0,23,22,17,15,21],
[27,29,21,22,24,28,0,25,21,20,24],
[27,27,23,24,29,29,26,0,26,22,27],
[30,33,23,29,29,34,30,25,0,27,27],
[34,30,28,36,40,36,31,29,24,0,23],
[34,33,31,26,33,30,27,24,24,28,0]])



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
result = np.append(np.array([11, 51, 92, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,29,27,10,36,20,12,19,5,22],
[37,0,41,39,12,36,15,19,22,25,22],
[22,10,0,39,12,34,20,19,10,10,27],
[24,12,12,0,12,26,10,22,3,15,17],
[41,39,39,39,0,38,32,25,39,32,30],
[15,15,17,25,13,0,20,20,20,13,30],
[31,36,31,41,19,31,0,33,24,29,24],
[39,32,32,29,26,31,18,0,30,32,29],
[32,29,41,48,12,31,27,21,0,20,24],
[46,26,41,36,19,38,22,19,31,0,22],
[29,29,24,34,21,21,27,22,27,29,0]])



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
result = np.append(np.array([11, 51, 93, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,25,35,19,35,29,32,36,25,26],
[27,0,22,27,19,26,28,22,27,28,33],
[26,29,0,37,20,39,21,31,35,25,27],
[16,24,14,0,15,34,13,25,26,19,15],
[32,32,31,36,0,36,20,31,38,21,33],
[16,25,12,17,15,0,14,19,27,19,20],
[22,23,30,38,31,37,0,35,41,22,26],
[19,29,20,26,20,32,16,0,33,27,28],
[15,24,16,25,13,24,10,18,0,16,21],
[26,23,26,32,30,32,29,24,35,0,37],
[25,18,24,36,18,31,25,23,30,14,0]])



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
result = np.append(np.array([11, 51, 94, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,18,12,19,19,18,22,18,16,22],
[38,0,32,23,30,32,28,35,33,31,31],
[33,19,0,24,23,27,27,24,25,26,30],
[39,28,27,0,29,30,20,25,31,25,31],
[32,21,28,22,0,25,26,20,22,25,25],
[32,19,24,21,26,0,27,25,22,24,26],
[33,23,24,31,25,24,0,23,27,27,30],
[29,16,27,26,31,26,28,0,29,29,29],
[33,18,26,20,29,29,24,22,0,29,27],
[35,20,25,26,26,27,24,22,22,0,27],
[29,20,21,20,26,25,21,22,24,24,0]])



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
result = np.append(np.array([11, 51, 95, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,32,35,32,29,29,30,34,24,27],
[25,0,28,28,33,32,26,25,34,25,23],
[19,23,0,28,28,22,19,18,26,26,27],
[16,23,23,0,25,25,20,21,25,20,18],
[19,18,23,26,0,23,21,26,26,24,29],
[22,19,29,26,28,0,21,24,25,22,25],
[22,25,32,31,30,30,0,23,29,25,25],
[21,26,33,30,25,27,28,0,31,25,28],
[17,17,25,26,25,26,22,20,0,23,25],
[27,26,25,31,27,29,26,26,28,0,28],
[24,28,24,33,22,26,26,23,26,23,0]])



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
result = np.append(np.array([11, 51, 96, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,28,23,25,32,20,27,18,18,34],
[32,0,31,24,30,28,33,23,27,24,30],
[23,20,0,25,23,24,27,22,19,16,40],
[28,27,26,0,26,25,30,23,21,22,27],
[26,21,28,25,0,24,28,27,30,26,22],
[19,23,27,26,27,0,25,33,25,19,36],
[31,18,24,21,23,26,0,27,24,18,28],
[24,28,29,28,24,18,24,0,22,20,25],
[33,24,32,30,21,26,27,29,0,20,32],
[33,27,35,29,25,32,33,31,31,0,38],
[17,21,11,24,29,15,23,26,19,13,0]])



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
result = np.append(np.array([11, 51, 97, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,26,19,21,25,23,23,20,23,20],
[25,0,25,25,27,18,20,22,19,22,17],
[25,26,0,25,29,20,25,25,25,24,23],
[32,26,26,0,31,25,31,25,24,26,26],
[30,24,22,20,0,25,25,25,19,24,20],
[26,33,31,26,26,0,28,28,26,27,25],
[28,31,26,20,26,23,0,22,22,26,20],
[28,29,26,26,26,23,29,0,25,25,21],
[31,32,26,27,32,25,29,26,0,30,22],
[28,29,27,25,27,24,25,26,21,0,20],
[31,34,28,25,31,26,31,30,29,31,0]])



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
result = np.append(np.array([11, 51, 98, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,26,31,30,28,31,25,24,25,20],
[19,0,22,27,27,22,27,23,17,26,18],
[25,29,0,30,32,25,29,27,24,25,21],
[20,24,21,0,23,21,25,23,18,23,15],
[21,24,19,28,0,22,27,23,22,23,22],
[23,29,26,30,29,0,27,30,23,29,26],
[20,24,22,26,24,24,0,27,21,22,21],
[26,28,24,28,28,21,24,0,21,30,23],
[27,34,27,33,29,28,30,30,0,29,25],
[26,25,26,28,28,22,29,21,22,0,18],
[31,33,30,36,29,25,30,28,26,33,0]])



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
result = np.append(np.array([11, 51, 99, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,18,12,17,8,19,13,9,8,13],
[37,0,36,30,30,19,26,29,33,22,22],
[33,15,0,19,24,15,12,20,26,25,10],
[39,21,32,0,32,27,17,28,28,11,16],
[34,21,27,19,0,21,27,25,25,23,15],
[43,32,36,24,30,0,25,37,34,28,27],
[32,25,39,34,24,26,0,24,25,22,24],
[38,22,31,23,26,14,27,0,29,17,22],
[42,18,25,23,26,17,26,22,0,17,23],
[43,29,26,40,28,23,29,34,34,0,24],
[38,29,41,35,36,24,27,29,28,27,0]])



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
result = np.append(np.array([11, 51, 100, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,26,25,19,23,26,25,25,22,20],
[30,0,35,26,29,25,31,33,30,30,28],
[25,16,0,20,22,19,26,27,27,23,20],
[26,25,31,0,27,27,30,27,33,28,27],
[32,22,29,24,0,25,29,29,24,22,28],
[28,26,32,24,26,0,32,26,26,23,24],
[25,20,25,21,22,19,0,26,22,22,21],
[26,18,24,24,22,25,25,0,23,23,25],
[26,21,24,18,27,25,29,28,0,24,24],
[29,21,28,23,29,28,29,28,27,0,28],
[31,23,31,24,23,27,30,26,27,23,0]])



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
result = np.append(np.array([11, 51, 101, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,27,28,23,29,19,32,26,27,25],
[26,0,27,27,25,30,27,30,27,31,28],
[24,24,0,22,24,28,22,28,24,29,24],
[23,24,29,0,20,28,26,32,22,30,29],
[28,26,27,31,0,27,28,31,25,34,29],
[22,21,23,23,24,0,21,26,25,28,21],
[32,24,29,25,23,30,0,31,27,32,30],
[19,21,23,19,20,25,20,0,22,22,17],
[25,24,27,29,26,26,24,29,0,31,24],
[24,20,22,21,17,23,19,29,20,0,19],
[26,23,27,22,22,30,21,34,27,32,0]])



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
result = np.append(np.array([11, 51, 102, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,22,31,19,32,28,28,38,18,37],
[27,0,32,32,28,29,23,16,26,18,30],
[29,19,0,20,32,38,34,14,45,32,23],
[20,19,31,0,35,32,34,16,39,24,24],
[32,23,19,16,0,33,33,18,39,17,22],
[19,22,13,19,18,0,24,19,38,18,21],
[23,28,17,17,18,27,0,16,35,19,23],
[23,35,37,35,33,32,35,0,39,36,23],
[13,25,6,12,12,13,16,12,0,12,23],
[33,33,19,27,34,33,32,15,39,0,21],
[14,21,28,27,29,30,28,28,28,30,0]])



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
result = np.append(np.array([11, 51, 103, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,3,12,28,14,16,20,23,24,12],
[27,0,25,28,23,13,18,32,34,20,23],
[48,26,0,25,25,32,26,32,38,30,14],
[39,23,26,0,39,25,23,29,39,28,24],
[23,28,26,12,0,20,23,26,24,23,22],
[37,38,19,26,31,0,21,38,40,16,27],
[35,33,25,28,28,30,0,29,45,34,27],
[31,19,19,22,25,13,22,0,16,16,9],
[28,17,13,12,27,11,6,35,0,17,14],
[27,31,21,23,28,35,17,35,34,0,26],
[39,28,37,27,29,24,24,42,37,25,0]])



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
result = np.append(np.array([11, 51, 104, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,26,29,28,21,25,21,23,28,23],
[22,0,22,20,21,21,19,23,22,25,25],
[25,29,0,27,27,20,26,18,21,32,23],
[22,31,24,0,20,17,21,22,19,26,23],
[23,30,24,31,0,21,24,22,24,36,29],
[30,30,31,34,30,0,31,26,22,35,29],
[26,32,25,30,27,20,0,25,29,29,29],
[30,28,33,29,29,25,26,0,28,31,24],
[28,29,30,32,27,29,22,23,0,34,26],
[23,26,19,25,15,16,22,20,17,0,27],
[28,26,28,28,22,22,22,27,25,24,0]])



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
result = np.append(np.array([11, 51, 105, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,29,30,28,29,21,34,29,17,26],
[28,0,26,25,28,30,26,30,28,26,23],
[22,25,0,25,28,24,20,32,31,20,26],
[21,26,26,0,23,22,27,32,29,28,24],
[23,23,23,28,0,27,20,32,27,24,26],
[22,21,27,29,24,0,28,32,32,21,22],
[30,25,31,24,31,23,0,33,33,25,28],
[17,21,19,19,19,19,18,0,26,19,21],
[22,23,20,22,24,19,18,25,0,17,25],
[34,25,31,23,27,30,26,32,34,0,27],
[25,28,25,27,25,29,23,30,26,24,0]])



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
result = np.append(np.array([11, 51, 106, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,27,22,29,31,29,24,24,21,20],
[20,0,25,22,28,26,22,23,20,23,18],
[24,26,0,23,33,28,25,27,23,22,24],
[29,29,28,0,27,24,27,28,26,26,29],
[22,23,18,24,0,23,21,22,22,18,14],
[20,25,23,27,28,0,24,21,24,25,17],
[22,29,26,24,30,27,0,25,25,24,24],
[27,28,24,23,29,30,26,0,25,25,21],
[27,31,28,25,29,27,26,26,0,24,26],
[30,28,29,25,33,26,27,26,27,0,31],
[31,33,27,22,37,34,27,30,25,20,0]])



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
result = np.append(np.array([11, 51, 107, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,25,23,31,25,27,30,20,29,20],
[23,0,22,25,31,21,20,22,28,34,25],
[26,29,0,21,23,21,30,27,21,29,20],
[28,26,30,0,25,17,22,21,19,25,28],
[20,20,28,26,0,14,21,28,24,23,19],
[26,30,30,34,37,0,25,33,27,34,33],
[24,31,21,29,30,26,0,30,30,28,29],
[21,29,24,30,23,18,21,0,27,32,29],
[31,23,30,32,27,24,21,24,0,22,26],
[22,17,22,26,28,17,23,19,29,0,22],
[31,26,31,23,32,18,22,22,25,29,0]])



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
result = np.append(np.array([11, 51, 108, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,27,21,23,22,20,26,21,25,21],
[24,0,30,22,23,26,22,28,27,26,24],
[24,21,0,22,18,24,16,23,25,26,24],
[30,29,29,0,30,26,23,30,32,29,23],
[28,28,33,21,0,26,25,37,30,27,27],
[29,25,27,25,25,0,28,29,33,32,23],
[31,29,35,28,26,23,0,30,28,28,24],
[25,23,28,21,14,22,21,0,22,27,17],
[30,24,26,19,21,18,23,29,0,27,22],
[26,25,25,22,24,19,23,24,24,0,25],
[30,27,27,28,24,28,27,34,29,26,0]])



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
result = np.append(np.array([11, 51, 109, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,23,21,24,13,31,26,21,32,16],
[36,0,35,30,35,26,36,30,31,40,23],
[28,16,0,31,30,16,31,24,29,37,28],
[30,21,20,0,23,23,37,30,29,38,21],
[27,16,21,28,0,13,26,23,22,30,18],
[38,25,35,28,38,0,37,30,29,37,21],
[20,15,20,14,25,14,0,20,18,32,11],
[25,21,27,21,28,21,31,0,24,36,24],
[30,20,22,22,29,22,33,27,0,36,22],
[19,11,14,13,21,14,19,15,15,0,5],
[35,28,23,30,33,30,40,27,29,46,0]])



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
result = np.append(np.array([11, 51, 110, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,33,31,24,26,30,28,28,29,26],
[26,0,28,30,26,28,25,29,23,28,22],
[18,23,0,24,21,25,23,23,21,24,22],
[20,21,27,0,25,28,23,24,25,22,20],
[27,25,30,26,0,29,26,25,24,27,23],
[25,23,26,23,22,0,22,30,24,25,19],
[21,26,28,28,25,29,0,30,27,29,26],
[23,22,28,27,26,21,21,0,21,25,21],
[23,28,30,26,27,27,24,30,0,26,25],
[22,23,27,29,24,26,22,26,25,0,21],
[25,29,29,31,28,32,25,30,26,30,0]])



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
result = np.append(np.array([11, 51, 111, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,32,25,33,22,23,42,27,37,34],
[23,0,24,26,28,15,25,32,25,27,27],
[19,27,0,17,24,13,20,34,21,27,27],
[26,25,34,0,27,26,27,36,19,32,34],
[18,23,27,24,0,14,20,30,19,26,31],
[29,36,38,25,37,0,34,45,31,34,32],
[28,26,31,24,31,17,0,41,24,36,37],
[9,19,17,15,21,6,10,0,13,19,28],
[24,26,30,32,32,20,27,38,0,41,40],
[14,24,24,19,25,17,15,32,10,0,31],
[17,24,24,17,20,19,14,23,11,20,0]])



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
result = np.append(np.array([11, 51, 112, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,26,23,31,36,35,33,36,33,36],
[26,0,32,31,22,34,34,24,28,26,30],
[25,19,0,25,21,35,37,29,21,25,37],
[28,20,26,0,28,36,22,12,28,20,36],
[20,29,30,23,0,24,26,22,24,32,24],
[15,17,16,15,27,0,37,19,24,25,28],
[16,17,14,29,25,14,0,12,20,16,26],
[18,27,22,39,29,32,39,0,32,37,30],
[15,23,30,23,27,27,31,19,0,27,28],
[18,25,26,31,19,26,35,14,24,0,20],
[15,21,14,15,27,23,25,21,23,31,0]])



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
result = np.append(np.array([11, 51, 113, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,21,30,22,22,31,25,26,26,34],
[24,0,25,26,23,19,28,27,22,23,26],
[30,26,0,25,26,22,28,21,25,27,29],
[21,25,26,0,26,28,33,27,23,28,34],
[29,28,25,25,0,24,28,20,26,29,30],
[29,32,29,23,27,0,34,30,20,27,32],
[20,23,23,18,23,17,0,24,20,25,23],
[26,24,30,24,31,21,27,0,24,32,29],
[25,29,26,28,25,31,31,27,0,26,31],
[25,28,24,23,22,24,26,19,25,0,26],
[17,25,22,17,21,19,28,22,20,25,0]])



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
result = np.append(np.array([11, 51, 114, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,23,27,20,24,22,25,22,26,28],
[22,0,22,24,26,23,23,17,23,24,22],
[28,29,0,29,27,27,28,28,24,30,33],
[24,27,22,0,29,24,25,23,21,29,30],
[31,25,24,22,0,23,19,24,25,24,24],
[27,28,24,27,28,0,26,18,20,23,30],
[29,28,23,26,32,25,0,22,31,28,32],
[26,34,23,28,27,33,29,0,31,28,31],
[29,28,27,30,26,31,20,20,0,25,32],
[25,27,21,22,27,28,23,23,26,0,32],
[23,29,18,21,27,21,19,20,19,19,0]])



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
result = np.append(np.array([11, 51, 115, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,16,27,23,27,17,25,23,26,29],
[23,0,25,30,37,29,24,28,26,25,28],
[35,26,0,27,26,28,26,23,25,32,25],
[24,21,24,0,32,29,19,27,19,27,24],
[28,14,25,19,0,22,9,24,18,19,22],
[24,22,23,22,29,0,17,21,22,24,21],
[34,27,25,32,42,34,0,29,28,37,32],
[26,23,28,24,27,30,22,0,20,27,19],
[28,25,26,32,33,29,23,31,0,27,23],
[25,26,19,24,32,27,14,24,24,0,19],
[22,23,26,27,29,30,19,32,28,32,0]])



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
result = np.append(np.array([11, 51, 116, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,21,19,21,21,29,28,26,24,22],
[25,0,20,19,20,19,25,21,21,17,17],
[30,31,0,27,22,21,29,32,30,26,24],
[32,32,24,0,30,26,30,28,34,29,28],
[30,31,29,21,0,23,29,24,25,29,27],
[30,32,30,25,28,0,31,33,29,30,25],
[22,26,22,21,22,20,0,26,26,27,25],
[23,30,19,23,27,18,25,0,25,24,22],
[25,30,21,17,26,22,25,26,0,25,26],
[27,34,25,22,22,21,24,27,26,0,21],
[29,34,27,23,24,26,26,29,25,30,0]])



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
result = np.append(np.array([11, 51, 117, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,30,18,26,25,7,21,16,47,12],
[33,0,34,22,30,33,29,15,24,29,22],
[21,17,0,16,30,27,17,32,27,41,26],
[33,29,35,0,30,39,29,25,35,35,22],
[25,21,21,21,0,25,21,16,21,21,22],
[26,18,24,12,26,0,21,21,42,47,12],
[44,22,34,22,30,30,0,25,39,51,21],
[30,36,19,26,35,30,26,0,42,42,31],
[35,27,24,16,30,9,12,9,0,31,12],
[4,22,10,16,30,4,0,9,20,0,16],
[39,29,25,29,29,39,30,20,39,35,0]])



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
result = np.append(np.array([11, 51, 118, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,38,47,21,29,41,38,41,41,46],
[38,0,42,47,39,21,45,43,34,46,50],
[13,9,0,47,1,25,25,31,42,30,41],
[4,4,4,0,4,20,12,26,20,12,37],
[30,12,50,47,0,33,45,34,46,29,45],
[22,30,26,31,18,0,29,27,42,30,45],
[10,6,26,39,6,22,0,27,34,22,38],
[13,8,20,25,17,24,24,0,25,13,41],
[10,17,9,31,5,9,17,26,0,17,50],
[10,5,21,39,22,21,29,38,34,0,38],
[5,1,10,14,6,6,13,10,1,13,0]])



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
result = np.append(np.array([11, 51, 119, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,19,22,24,25,26,25,23,25,30],
[27,0,20,21,17,25,23,21,21,26,21],
[32,31,0,26,28,26,29,23,26,28,29],
[29,30,25,0,24,27,30,25,25,26,30],
[27,34,23,27,0,25,23,23,21,29,29],
[26,26,25,24,26,0,24,22,20,27,31],
[25,28,22,21,28,27,0,28,25,26,27],
[26,30,28,26,28,29,23,0,24,27,30],
[28,30,25,26,30,31,26,27,0,26,28],
[26,25,23,25,22,24,25,24,25,0,23],
[21,30,22,21,22,20,24,21,23,28,0]])



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
result = np.append(np.array([11, 51, 120, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,25,38,28,37,27,31,34,40,30],
[20,0,28,29,25,17,24,22,25,31,30],
[26,23,0,27,17,25,20,26,17,30,28],
[13,22,24,0,14,19,22,30,31,32,24],
[23,26,34,37,0,26,24,30,36,31,22],
[14,34,26,32,25,0,27,18,28,33,25],
[24,27,31,29,27,24,0,28,23,34,33],
[20,29,25,21,21,33,23,0,23,29,21],
[17,26,34,20,15,23,28,28,0,27,32],
[11,20,21,19,20,18,17,22,24,0,32],
[21,21,23,27,29,26,18,30,19,19,0]])



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
result = np.append(np.array([11, 51, 121, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,18,8,8,12,16,17,10,8,26],
[27,0,21,18,18,28,18,14,25,19,28],
[33,30,0,19,21,23,21,25,22,21,34],
[43,33,32,0,19,25,25,24,16,27,30],
[43,33,30,32,0,31,21,28,22,32,27],
[39,23,28,26,20,0,22,27,26,14,29],
[35,33,30,26,30,29,0,24,27,26,27],
[34,37,26,27,23,24,27,0,22,23,32],
[41,26,29,35,29,25,24,29,0,18,36],
[43,32,30,24,19,37,25,28,33,0,33],
[25,23,17,21,24,22,24,19,15,18,0]])



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
result = np.append(np.array([11, 51, 122, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,24,20,29,23,32,33,8,27,22],
[15,0,22,14,29,19,12,29,17,19,19],
[27,29,0,13,24,37,29,29,22,32,26],
[31,37,38,0,30,29,30,29,38,37,19],
[22,22,27,21,0,32,24,29,22,32,27],
[28,32,14,22,19,0,25,20,22,26,27],
[19,39,22,21,27,26,0,27,22,30,27],
[18,22,22,22,22,31,24,0,17,16,17],
[43,34,29,13,29,29,29,34,0,37,31],
[24,32,19,14,19,25,21,35,14,0,19],
[29,32,25,32,24,24,24,34,20,32,0]])



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
result = np.append(np.array([11, 51, 123, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,23,35,25,30,39,32,26,25,28],
[24,0,29,37,30,36,37,25,28,30,33],
[28,22,0,34,32,32,34,36,33,33,33],
[16,14,17,0,17,19,30,20,23,24,19],
[26,21,19,34,0,28,32,25,26,24,26],
[21,15,19,32,23,0,29,23,27,25,25],
[12,14,17,21,19,22,0,21,26,18,17],
[19,26,15,31,26,28,30,0,28,21,24],
[25,23,18,28,25,24,25,23,0,25,27],
[26,21,18,27,27,26,33,30,26,0,27],
[23,18,18,32,25,26,34,27,24,24,0]])



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
result = np.append(np.array([11, 51, 124, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,22,32,27,18,21,26,35,32,32],
[32,0,27,40,26,20,27,29,32,29,31],
[29,24,0,38,26,29,25,28,35,27,33],
[19,11,13,0,26,14,18,16,27,25,17],
[24,25,25,25,0,16,23,25,29,30,22],
[33,31,22,37,35,0,29,32,29,33,27],
[30,24,26,33,28,22,0,25,35,28,31],
[25,22,23,35,26,19,26,0,26,31,23],
[16,19,16,24,22,22,16,25,0,23,19],
[19,22,24,26,21,18,23,20,28,0,22],
[19,20,18,34,29,24,20,28,32,29,0]])



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
result = np.append(np.array([11, 51, 125, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,23,27,29,25,26,21,21,30,26],
[28,0,28,29,30,25,31,25,29,34,28],
[28,23,0,26,27,23,26,20,21,30,22],
[24,22,25,0,29,28,23,26,27,26,25],
[22,21,24,22,0,27,31,24,24,28,24],
[26,26,28,23,24,0,30,30,23,32,29],
[25,20,25,28,20,21,0,24,26,28,23],
[30,26,31,25,27,21,27,0,23,28,24],
[30,22,30,24,27,28,25,28,0,27,30],
[21,17,21,25,23,19,23,23,24,0,22],
[25,23,29,26,27,22,28,27,21,29,0]])



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
result = np.append(np.array([11, 51, 126, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,27,24,27,31,30,28,27,30,28],
[28,0,24,27,28,35,34,31,26,31,30],
[24,27,0,23,27,28,29,30,26,31,23],
[27,24,28,0,26,29,40,33,28,31,31],
[24,23,24,25,0,28,31,27,24,28,24],
[20,16,23,22,23,0,29,26,21,28,25],
[21,17,22,11,20,22,0,23,21,26,22],
[23,20,21,18,24,25,28,0,21,26,24],
[24,25,25,23,27,30,30,30,0,30,31],
[21,20,20,20,23,23,25,25,21,0,22],
[23,21,28,20,27,26,29,27,20,29,0]])



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
result = np.append(np.array([11, 51, 127, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,27,27,27,31,27,20,29,23,21],
[19,0,14,18,21,22,16,16,19,14,24],
[24,37,0,22,27,32,31,27,29,32,16],
[24,33,29,0,26,29,27,29,28,33,29],
[24,30,24,25,0,26,23,20,24,23,25],
[20,29,19,22,25,0,25,13,17,16,21],
[24,35,20,24,28,26,0,24,27,27,22],
[31,35,24,22,31,38,27,0,30,28,23],
[22,32,22,23,27,34,24,21,0,24,21],
[28,37,19,18,28,35,24,23,27,0,23],
[30,27,35,22,26,30,29,28,30,28,0]])



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
result = np.append(np.array([11, 51, 128, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,16,22,23,12,35,16,22,16,32],
[20,0,10,20,11,4,33,16,22,27,27],
[35,41,0,35,21,11,40,21,14,35,49],
[29,31,16,0,23,13,24,5,17,16,29],
[28,40,30,28,0,11,33,14,20,35,35],
[39,47,40,38,40,0,30,24,28,27,40],
[16,18,11,27,18,21,0,14,11,17,18],
[35,35,30,46,37,27,37,0,41,21,35],
[29,29,37,34,31,23,40,10,0,23,37],
[35,24,16,35,16,24,34,30,28,0,34],
[19,24,2,22,16,11,33,16,14,17,0]])



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
result = np.append(np.array([11, 51, 129, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,30,18,22,31,19,23,29,28,25],
[25,0,30,22,20,30,24,26,28,28,23],
[21,21,0,14,21,27,18,19,17,22,23],
[33,29,37,0,26,35,20,25,30,35,31],
[29,31,30,25,0,36,25,25,28,32,29],
[20,21,24,16,15,0,17,15,17,26,19],
[32,27,33,31,26,34,0,26,25,27,32],
[28,25,32,26,26,36,25,0,24,29,31],
[22,23,34,21,23,34,26,27,0,31,26],
[23,23,29,16,19,25,24,22,20,0,23],
[26,28,28,20,22,32,19,20,25,28,0]])



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
result = np.append(np.array([11, 51, 130, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,23,22,25,29,28,27,32,31,27],
[29,0,28,26,21,34,25,23,30,31,25],
[28,23,0,23,20,29,29,25,23,30,27],
[29,25,28,0,27,29,27,28,30,29,27],
[26,30,31,24,0,34,31,27,26,36,28],
[22,17,22,22,17,0,20,18,26,26,24],
[23,26,22,24,20,31,0,20,30,23,28],
[24,28,26,23,24,33,31,0,29,31,25],
[19,21,28,21,25,25,21,22,0,30,18],
[20,20,21,22,15,25,28,20,21,0,22],
[24,26,24,24,23,27,23,26,33,29,0]])



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
result = np.append(np.array([11, 51, 131, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,18,22,20,31,13,15,24,24,24],
[30,0,18,21,28,34,19,27,19,28,30],
[33,33,0,24,31,39,29,33,34,36,34],
[29,30,27,0,28,30,12,26,26,33,28],
[31,23,20,23,0,24,21,17,25,23,26],
[20,17,12,21,27,0,17,19,27,25,24],
[38,32,22,39,30,34,0,31,35,36,26],
[36,24,18,25,34,32,20,0,27,34,22],
[27,32,17,25,26,24,16,24,0,30,28],
[27,23,15,18,28,26,15,17,21,0,24],
[27,21,17,23,25,27,25,29,23,27,0]])



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
result = np.append(np.array([11, 51, 132, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,28,22,27,21,23,30,19,21,18],
[20,0,27,17,25,15,19,40,17,26,25],
[23,24,0,17,35,16,18,31,21,29,17],
[29,34,34,0,34,19,25,35,19,35,26],
[24,26,16,17,0,20,24,25,22,26,22],
[30,36,35,32,31,0,25,34,25,33,26],
[28,32,33,26,27,26,0,33,30,36,24],
[21,11,20,16,26,17,18,0,17,21,11],
[32,34,30,32,29,26,21,34,0,29,23],
[30,25,22,16,25,18,15,30,22,0,17],
[33,26,34,25,29,25,27,40,28,34,0]])



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
result = np.append(np.array([11, 51, 133, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,40,26,42,31,20,29,24,26,30],
[9,0,25,5,18,9,16,27,18,20,18],
[11,26,0,13,33,27,31,21,22,24,18],
[25,46,38,0,30,32,22,38,31,29,34],
[9,33,18,21,0,10,9,25,24,18,21],
[20,42,24,19,41,0,21,24,35,23,31],
[31,35,20,29,42,30,0,29,32,23,38],
[22,24,30,13,26,27,22,0,29,24,29],
[27,33,29,20,27,16,19,22,0,19,21],
[25,31,27,22,33,28,28,27,32,0,25],
[21,33,33,17,30,20,13,22,30,26,0]])



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
result = np.append(np.array([11, 51, 134, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,25,29,33,37,35,40,23,40,24],
[17,0,19,25,24,30,34,36,12,33,27],
[26,32,0,25,34,36,31,42,26,35,24],
[22,26,26,0,22,36,31,37,25,30,21],
[18,27,17,29,0,33,38,33,20,31,18],
[14,21,15,15,18,0,20,28,19,25,17],
[16,17,20,20,13,31,0,21,15,29,15],
[11,15,9,14,18,23,30,0,9,23,10],
[28,39,25,26,31,32,36,42,0,42,32],
[11,18,16,21,20,26,22,28,9,0,16],
[27,24,27,30,33,34,36,41,19,35,0]])



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
result = np.append(np.array([11, 51, 135, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,23,27,23,27,24,28,20,22,20],
[26,0,17,24,24,24,23,28,17,20,15],
[28,34,0,29,24,29,28,32,26,25,23],
[24,27,22,0,21,30,28,31,23,25,26],
[28,27,27,30,0,30,29,30,25,29,26],
[24,27,22,21,21,0,26,27,24,21,21],
[27,28,23,23,22,25,0,27,23,22,20],
[23,23,19,20,21,24,24,0,19,16,14],
[31,34,25,28,26,27,28,32,0,29,25],
[29,31,26,26,22,30,29,35,22,0,21],
[31,36,28,25,25,30,31,37,26,30,0]])



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
result = np.append(np.array([11, 51, 136, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,29,29,41,28,33,28,20,32,32],
[29,0,19,29,29,24,29,24,29,37,27],
[22,32,0,47,51,24,28,38,28,22,18],
[22,22,4,0,12,18,22,18,28,22,12],
[10,22,0,39,0,18,10,18,16,18,12],
[23,27,27,33,33,0,33,41,33,21,19],
[18,22,23,29,41,18,0,28,28,8,12],
[23,27,13,33,33,10,23,0,19,21,13],
[31,22,23,23,35,18,23,32,0,12,12],
[19,14,29,29,33,30,43,30,39,0,33],
[19,24,33,39,39,32,39,38,39,18,0]])



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
result = np.append(np.array([11, 51, 137, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,10,11,26,25,19,16,21,21,26],
[35,0,25,36,36,25,26,16,36,36,18],
[41,26,0,33,40,25,23,16,15,30,26],
[40,15,18,0,19,26,23,16,18,26,23],
[25,15,11,32,0,19,21,12,22,22,16],
[26,26,26,25,32,0,26,15,15,15,16],
[32,25,28,28,30,25,0,26,18,18,33],
[35,35,35,35,39,36,25,0,36,35,26],
[30,15,36,33,29,36,33,15,0,39,33],
[30,15,21,25,29,36,33,16,12,0,26],
[25,33,25,28,35,35,18,25,18,25,0]])



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
result = np.append(np.array([11, 51, 138, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,25,21,23,21,25,21,22,24,22],
[30,0,32,27,28,26,31,28,24,29,29],
[26,19,0,28,25,23,25,19,20,22,24],
[30,24,23,0,27,25,26,24,27,22,25],
[28,23,26,24,0,25,28,30,22,22,25],
[30,25,28,26,26,0,29,18,27,28,21],
[26,20,26,25,23,22,0,24,22,25,26],
[30,23,32,27,21,33,27,0,22,31,29],
[29,27,31,24,29,24,29,29,0,24,28],
[27,22,29,29,29,23,26,20,27,0,25],
[29,22,27,26,26,30,25,22,23,26,0]])



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
result = np.append(np.array([11, 51, 139, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,24,25,16,29,22,22,25,19,30],
[25,0,31,26,22,33,26,28,28,18,24],
[27,20,0,30,19,34,31,28,35,28,36],
[26,25,21,0,17,26,16,17,28,12,18],
[35,29,32,34,0,36,27,27,39,19,36],
[22,18,17,25,15,0,11,24,26,14,24],
[29,25,20,35,24,40,0,23,34,24,33],
[29,23,23,34,24,27,28,0,33,23,34],
[26,23,16,23,12,25,17,18,0,17,24],
[32,33,23,39,32,37,27,28,34,0,29],
[21,27,15,33,15,27,18,17,27,22,0]])



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
result = np.append(np.array([11, 51, 140, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,26,20,30,27,22,23,24,29,33],
[32,0,32,23,34,30,22,26,28,28,30],
[25,19,0,17,29,30,21,22,18,24,32],
[31,28,34,0,32,29,33,27,21,30,33],
[21,17,22,19,0,30,19,19,16,26,30],
[24,21,21,22,21,0,25,18,26,23,27],
[29,29,30,18,32,26,0,28,26,27,31],
[28,25,29,24,32,33,23,0,23,27,31],
[27,23,33,30,35,25,25,28,0,34,29],
[22,23,27,21,25,28,24,24,17,0,34],
[18,21,19,18,21,24,20,20,22,17,0]])



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
result = np.append(np.array([11, 51, 141, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,26,20,30,23,26,25,17,24,24],
[20,0,26,18,25,25,27,29,22,28,22],
[25,25,0,25,22,21,23,29,24,27,27],
[31,33,26,0,32,25,32,30,26,31,26],
[21,26,29,19,0,23,30,26,17,29,26],
[28,26,30,26,28,0,23,28,23,23,19],
[25,24,28,19,21,28,0,27,22,25,24],
[26,22,22,21,25,23,24,0,17,20,27],
[34,29,27,25,34,28,29,34,0,29,24],
[27,23,24,20,22,28,26,31,22,0,22],
[27,29,24,25,25,32,27,24,27,29,0]])



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
result = np.append(np.array([11, 51, 142, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,32,25,19,25,25,22,24,28,26],
[24,0,22,24,22,26,23,24,25,30,26],
[19,29,0,23,24,25,33,27,23,28,26],
[26,27,28,0,20,28,26,23,28,25,29],
[32,29,27,31,0,26,29,24,23,32,32],
[26,25,26,23,25,0,26,31,22,26,27],
[26,28,18,25,22,25,0,24,25,29,29],
[29,27,24,28,27,20,27,0,26,26,27],
[27,26,28,23,28,29,26,25,0,27,29],
[23,21,23,26,19,25,22,25,24,0,23],
[25,25,25,22,19,24,22,24,22,28,0]])



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
result = np.append(np.array([11, 51, 143, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,30,25,32,27,26,33,32,26,25],
[25,0,25,21,27,25,22,31,37,22,22],
[21,26,0,24,33,28,25,28,31,24,27],
[26,30,27,0,33,27,27,37,35,25,29],
[19,24,18,18,0,15,15,30,26,21,16],
[24,26,23,24,36,0,24,28,33,25,28],
[25,29,26,24,36,27,0,28,32,25,28],
[18,20,23,14,21,23,23,0,29,20,17],
[19,14,20,16,25,18,19,22,0,19,20],
[25,29,27,26,30,26,26,31,32,0,27],
[26,29,24,22,35,23,23,34,31,24,0]])



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
result = np.append(np.array([11, 51, 144, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,19,30,32,21,23,38,30,23,25],
[15,0,21,23,25,24,20,33,29,22,23],
[32,30,0,27,29,31,29,39,25,30,22],
[21,28,24,0,37,28,27,42,30,25,28],
[19,26,22,14,0,30,31,36,31,18,28],
[30,27,20,23,21,0,26,33,28,23,21],
[28,31,22,24,20,25,0,27,27,23,35],
[13,18,12,9,15,18,24,0,15,11,20],
[21,22,26,21,20,23,24,36,0,13,25],
[28,29,21,26,33,28,28,40,38,0,31],
[26,28,29,23,23,30,16,31,26,20,0]])



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
result = np.append(np.array([11, 51, 145, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,30,32,29,29,31,27,21,22,31],
[13,0,15,29,22,25,23,25,19,13,14],
[21,36,0,33,29,21,21,28,30,25,14],
[19,22,18,0,23,17,18,13,26,20,11],
[22,29,22,28,0,19,20,24,31,18,22],
[22,26,30,34,32,0,30,31,35,23,28],
[20,28,30,33,31,21,0,24,30,26,13],
[24,26,23,38,27,20,27,0,25,22,19],
[30,32,21,25,20,16,21,26,0,19,17],
[29,38,26,31,33,28,25,29,32,0,26],
[20,37,37,40,29,23,38,32,34,25,0]])



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
result = np.append(np.array([11, 51, 146, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,20,26,27,20,24,18,31,29,30],
[19,0,20,29,25,18,29,26,31,25,41],
[31,31,0,35,23,18,33,24,36,31,36],
[25,22,16,0,21,21,14,23,25,21,29],
[24,26,28,30,0,28,22,30,29,31,37],
[31,33,33,30,23,0,23,26,24,25,31],
[27,22,18,37,29,28,0,21,22,32,37],
[33,25,27,28,21,25,30,0,33,28,29],
[20,20,15,26,22,27,29,18,0,18,30],
[22,26,20,30,20,26,19,23,33,0,33],
[21,10,15,22,14,20,14,22,21,18,0]])



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
result = np.append(np.array([11, 51, 147, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,25,30,27,26,31,26,29,27,30],
[30,0,33,31,30,29,35,34,23,31,34],
[26,18,0,27,31,28,35,30,26,26,30],
[21,20,24,0,22,23,28,22,16,20,22],
[24,21,20,29,0,27,29,28,26,22,27],
[25,22,23,28,24,0,33,26,28,23,25],
[20,16,16,23,22,18,0,22,24,22,21],
[25,17,21,29,23,25,29,0,22,26,24],
[22,28,25,35,25,23,27,29,0,27,26],
[24,20,25,31,29,28,29,25,24,0,25],
[21,17,21,29,24,26,30,27,25,26,0]])



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
result = np.append(np.array([11, 51, 148, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,31,24,34,30,24,22,25,27,27],
[20,0,25,22,24,25,22,18,24,21,25],
[20,26,0,27,27,24,26,23,23,21,20],
[27,29,24,0,31,28,29,20,30,30,24],
[17,27,24,20,0,23,20,20,23,18,21],
[21,26,27,23,28,0,27,22,23,23,22],
[27,29,25,22,31,24,0,23,21,24,25],
[29,33,28,31,31,29,28,0,29,27,24],
[26,27,28,21,28,28,30,22,0,24,23],
[24,30,30,21,33,28,27,24,27,0,23],
[24,26,31,27,30,29,26,27,28,28,0]])



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
result = np.append(np.array([11, 51, 149, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,22,26,20,31,25,19,24,25,24],
[25,0,20,23,21,27,19,21,28,21,27],
[29,31,0,29,23,32,31,23,28,28,32],
[25,28,22,0,22,28,22,28,26,26,31],
[31,30,28,29,0,29,31,25,32,26,33],
[20,24,19,23,22,0,19,21,25,20,24],
[26,32,20,29,20,32,0,24,30,25,31],
[32,30,28,23,26,30,27,0,31,28,33],
[27,23,23,25,19,26,21,20,0,23,25],
[26,30,23,25,25,31,26,23,28,0,26],
[27,24,19,20,18,27,20,18,26,25,0]])



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
result = np.append(np.array([11, 51, 150, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,20,23,17,14,8,22,15,29,20],
[25,0,25,20,23,25,10,16,14,28,22],
[31,26,0,35,16,31,8,22,15,29,17],
[28,31,16,0,27,17,14,14,10,23,15],
[34,28,35,24,0,31,28,22,24,30,28],
[37,26,20,34,20,0,19,28,28,37,25],
[43,41,43,37,23,32,0,24,19,36,26],
[29,35,29,37,29,23,27,0,32,42,27],
[36,37,36,41,27,23,32,19,0,24,22],
[22,23,22,28,21,14,15,9,27,0,14],
[31,29,34,36,23,26,25,24,29,37,0]])



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
result = np.append(np.array([11, 51, 151, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,25,28,23,26,25,30,25,29,21],
[29,0,25,31,25,26,19,29,24,29,22],
[26,26,0,22,28,31,24,28,26,30,22],
[23,20,29,0,25,26,20,31,28,25,26],
[28,26,23,26,0,23,23,29,27,25,18],
[25,25,20,25,28,0,24,27,22,23,16],
[26,32,27,31,28,27,0,26,25,35,23],
[21,22,23,20,22,24,25,0,27,24,24],
[26,27,25,23,24,29,26,24,0,28,18],
[22,22,21,26,26,28,16,27,23,0,19],
[30,29,29,25,33,35,28,27,33,32,0]])



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
result = np.append(np.array([11, 51, 152, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,22,26,28,20,31,24,31,29,34],
[30,0,26,23,33,31,31,31,30,34,35],
[29,25,0,23,32,27,29,25,25,31,32],
[25,28,28,0,27,29,31,28,30,35,31],
[23,18,19,24,0,21,31,27,26,29,29],
[31,20,24,22,30,0,31,27,28,34,33],
[20,20,22,20,20,20,0,28,28,25,26],
[27,20,26,23,24,24,23,0,32,26,29],
[20,21,26,21,25,23,23,19,0,23,27],
[22,17,20,16,22,17,26,25,28,0,29],
[17,16,19,20,22,18,25,22,24,22,0]])



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
result = np.append(np.array([11, 51, 153, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,30,32,28,29,28,20,29,24,26],
[26,0,28,31,31,27,23,29,27,25,24],
[21,23,0,28,26,30,24,23,29,29,29],
[19,20,23,0,24,28,24,21,28,21,27],
[23,20,25,27,0,21,21,22,26,29,20],
[22,24,21,23,30,0,25,27,27,25,25],
[23,28,27,27,30,26,0,22,27,24,25],
[31,22,28,30,29,24,29,0,32,21,22],
[22,24,22,23,25,24,24,19,0,21,20],
[27,26,22,30,22,26,27,30,30,0,27],
[25,27,22,24,31,26,26,29,31,24,0]])



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
result = np.append(np.array([11, 51, 154, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,20,18,20,16,23,23,20,23,21],
[34,0,27,24,24,25,29,32,27,28,26],
[31,24,0,22,23,21,21,25,23,25,28],
[33,27,29,0,27,23,26,29,28,31,26],
[31,27,28,24,0,20,30,31,25,30,27],
[35,26,30,28,31,0,30,28,25,29,29],
[28,22,30,25,21,21,0,33,26,22,30],
[28,19,26,22,20,23,18,0,23,23,28],
[31,24,28,23,26,26,25,28,0,27,28],
[28,23,26,20,21,22,29,28,24,0,28],
[30,25,23,25,24,22,21,23,23,23,0]])



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
result = np.append(np.array([11, 51, 155, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,35,33,27,25,33,28,34,34,26],
[15,0,20,18,21,18,19,15,27,21,20],
[16,31,0,23,27,26,23,17,29,25,18],
[18,33,28,0,24,22,22,27,28,29,18],
[24,30,24,27,0,26,27,30,34,32,25],
[26,33,25,29,25,0,28,34,35,32,28],
[18,32,28,29,24,23,0,26,29,35,24],
[23,36,34,24,21,17,25,0,32,30,19],
[17,24,22,23,17,16,22,19,0,24,17],
[17,30,26,22,19,19,16,21,27,0,22],
[25,31,33,33,26,23,27,32,34,29,0]])



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
result = np.append(np.array([11, 51, 156, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,32,26,26,29,33,28,24,20,21],
[24,0,25,25,28,20,25,26,25,23,23],
[19,26,0,25,23,18,28,24,20,20,21],
[25,26,26,0,25,20,35,30,30,24,25],
[25,23,28,26,0,22,26,28,20,25,17],
[22,31,33,31,29,0,33,35,28,26,26],
[18,26,23,16,25,18,0,25,21,15,20],
[23,25,27,21,23,16,26,0,19,20,17],
[27,26,31,21,31,23,30,32,0,22,26],
[31,28,31,27,26,25,36,31,29,0,24],
[30,28,30,26,34,25,31,34,25,27,0]])



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
result = np.append(np.array([11, 51, 157, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,30,28,24,24,22,25,19,21,25],
[21,0,24,21,21,19,18,24,16,21,23],
[21,27,0,22,19,18,25,25,17,27,22],
[23,30,29,0,18,27,25,24,22,26,26],
[27,30,32,33,0,29,28,23,28,26,23],
[27,32,33,24,22,0,27,25,20,25,27],
[29,33,26,26,23,24,0,29,24,30,24],
[26,27,26,27,28,26,22,0,17,24,24],
[32,35,34,29,23,31,27,34,0,35,35],
[30,30,24,25,25,26,21,27,16,0,27],
[26,28,29,25,28,24,27,27,16,24,0]])



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
result = np.append(np.array([11, 51, 158, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,21,28,28,24,25,32,22,22,30],
[31,0,31,30,36,29,38,38,23,25,23],
[30,20,0,28,29,18,27,36,21,32,21],
[23,21,23,0,30,25,29,31,20,24,22],
[23,15,22,21,0,15,19,30,14,20,18],
[27,22,33,26,36,0,28,38,24,26,22],
[26,13,24,22,32,23,0,26,18,30,24],
[19,13,15,20,21,13,25,0,9,17,13],
[29,28,30,31,37,27,33,42,0,31,23],
[29,26,19,27,31,25,21,34,20,0,23],
[21,28,30,29,33,29,27,38,28,28,0]])



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
result = np.append(np.array([11, 51, 159, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,24,22,37,35,28,26,32,25,27],
[33,0,26,28,39,26,21,28,36,31,33],
[27,25,0,20,22,33,22,30,32,27,25],
[29,23,31,0,27,30,19,27,34,28,34],
[14,12,29,24,0,25,10,19,30,20,27],
[16,25,18,21,26,0,17,24,30,25,24],
[23,30,29,32,41,34,0,29,33,34,35],
[25,23,21,24,32,27,22,0,29,24,33],
[19,15,19,17,21,21,18,22,0,24,22],
[26,20,24,23,31,26,17,27,27,0,34],
[24,18,26,17,24,27,16,18,29,17,0]])



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
result = np.append(np.array([11, 51, 160, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,30,30,26,26,24,30,28,28,23],
[27,0,32,28,25,28,25,26,26,32,23],
[21,19,0,24,23,20,15,23,18,24,18],
[21,23,27,0,26,24,23,26,22,29,22],
[25,26,28,25,0,24,26,25,25,32,24],
[25,23,31,27,27,0,23,29,25,29,22],
[27,26,36,28,25,28,0,29,26,35,20],
[21,25,28,25,26,22,22,0,23,29,27],
[23,25,33,29,26,26,25,28,0,31,24],
[23,19,27,22,19,22,16,22,20,0,19],
[28,28,33,29,27,29,31,24,27,32,0]])



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
result = np.append(np.array([11, 51, 161, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,37,27,28,23,33,28,22,29,33],
[22,0,22,12,22,16,27,26,24,25,23],
[14,29,0,23,28,24,23,31,19,24,21],
[24,39,28,0,34,29,29,41,25,30,26],
[23,29,23,17,0,21,22,30,25,21,32],
[28,35,27,22,30,0,33,34,26,26,34],
[18,24,28,22,29,18,0,29,26,24,24],
[23,25,20,10,21,17,22,0,27,25,20],
[29,27,32,26,26,25,25,24,0,28,26],
[22,26,27,21,30,25,27,26,23,0,26],
[18,28,30,25,19,17,27,31,25,25,0]])



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
result = np.append(np.array([11, 51, 162, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,23,20,26,27,18,27,8,16,17],
[43,0,43,21,43,27,37,34,18,35,18],
[28,8,0,28,25,19,26,27,18,23,10],
[31,30,23,0,38,32,32,32,30,38,33],
[25,8,26,13,0,27,19,27,11,10,10],
[24,24,32,19,24,0,34,25,9,17,33],
[33,14,25,19,32,17,0,34,16,15,8],
[24,17,24,19,24,26,17,0,17,24,17],
[43,33,33,21,40,42,35,34,0,25,25],
[35,16,28,13,41,34,36,27,26,0,25],
[34,33,41,18,41,18,43,34,26,26,0]])



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
result = np.append(np.array([11, 51, 163, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,14,20,17,8,20,21,25,18,29],
[30,0,30,31,20,22,20,29,33,29,40],
[37,21,0,34,22,19,31,10,30,23,34],
[31,20,17,0,23,14,23,10,25,18,16],
[34,31,29,28,0,34,23,29,25,34,37],
[43,29,32,37,17,0,23,29,25,29,37],
[31,31,20,28,28,28,0,27,17,18,21],
[30,22,41,41,22,22,24,0,38,25,41],
[26,18,21,26,26,26,34,13,0,20,18],
[33,22,28,33,17,22,33,26,31,0,33],
[22,11,17,35,14,14,30,10,33,18,0]])



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
result = np.append(np.array([11, 51, 164, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,17,34,25,26,10,23,31,8,9],
[23,0,20,41,22,27,13,35,34,24,11],
[34,31,0,41,18,31,28,45,32,36,40],
[17,10,10,0,1,13,8,30,20,10,9],
[26,29,33,50,0,28,13,34,34,33,32],
[25,24,20,38,23,0,10,33,30,21,24],
[41,38,23,43,38,41,0,43,30,37,47],
[28,16,6,21,17,18,8,0,32,6,22],
[20,17,19,31,17,21,21,19,0,19,18],
[43,27,15,41,18,30,14,45,32,0,32],
[42,40,11,42,19,27,4,29,33,19,0]])



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
result = np.append(np.array([11, 51, 165, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,20,16,25,21,22,24,26,23,26],
[32,0,24,27,28,26,25,31,25,28,23],
[31,27,0,25,26,20,24,26,23,27,26],
[35,24,26,0,22,22,26,30,26,29,30],
[26,23,25,29,0,24,27,24,25,26,26],
[30,25,31,29,27,0,26,28,27,32,25],
[29,26,27,25,24,25,0,27,24,24,29],
[27,20,25,21,27,23,24,0,25,24,21],
[25,26,28,25,26,24,27,26,0,23,26],
[28,23,24,22,25,19,27,27,28,0,26],
[25,28,25,21,25,26,22,30,25,25,0]])



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
result = np.append(np.array([11, 51, 166, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,20,20,21,19,18,27,19,26,16],
[29,0,21,19,23,22,25,24,21,27,21],
[31,30,0,27,29,27,19,27,20,34,27],
[31,32,24,0,23,28,24,28,24,31,25],
[30,28,22,28,0,23,19,27,19,34,22],
[32,29,24,23,28,0,28,29,30,32,27],
[33,26,32,27,32,23,0,32,23,32,25],
[24,27,24,23,24,22,19,0,23,27,18],
[32,30,31,27,32,21,28,28,0,33,27],
[25,24,17,20,17,19,19,24,18,0,18],
[35,30,24,26,29,24,26,33,24,33,0]])



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
result = np.append(np.array([11, 51, 167, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,21,17,26,22,19,35,21,24,26],
[30,0,23,25,24,28,28,37,27,28,29],
[30,28,0,26,22,22,28,26,28,24,22],
[34,26,25,0,26,21,31,33,30,32,28],
[25,27,29,25,0,15,22,30,22,22,18],
[29,23,29,30,36,0,28,40,25,27,32],
[32,23,23,20,29,23,0,27,29,24,20],
[16,14,25,18,21,11,24,0,17,27,17],
[30,24,23,21,29,26,22,34,0,27,24],
[27,23,27,19,29,24,27,24,24,0,24],
[25,22,29,23,33,19,31,34,27,27,0]])



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
result = np.append(np.array([11, 51, 168, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,33,21,27,25,30,36,34,51,32],
[32,0,33,24,47,30,30,41,30,47,28],
[18,18,0,21,27,10,19,27,10,31,19],
[30,27,30,0,40,32,27,32,23,36,40],
[24,4,24,11,0,34,17,20,25,30,23],
[26,21,41,19,17,0,23,26,17,30,32],
[21,21,32,24,34,28,0,30,17,21,23],
[15,10,24,19,31,25,21,0,25,38,14],
[17,21,41,28,26,34,34,26,0,27,36],
[0,4,20,15,21,21,30,13,24,0,19],
[19,23,32,11,28,19,28,37,15,32,0]])



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
result = np.append(np.array([11, 51, 169, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,19,30,27,30,26,30,25,27,30],
[24,0,25,28,24,27,26,31,26,33,28],
[32,26,0,24,23,32,30,34,28,25,31],
[21,23,27,0,23,27,26,31,25,26,29],
[24,27,28,28,0,29,25,32,26,30,35],
[21,24,19,24,22,0,24,28,23,28,28],
[25,25,21,25,26,27,0,26,27,28,27],
[21,20,17,20,19,23,25,0,22,26,25],
[26,25,23,26,25,28,24,29,0,25,33],
[24,18,26,25,21,23,23,25,26,0,28],
[21,23,20,22,16,23,24,26,18,23,0]])



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
result = np.append(np.array([11, 51, 170, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,24,27,28,34,32,34,31,29,22],
[22,0,24,26,28,28,29,27,30,28,23],
[27,27,0,28,27,32,24,28,37,28,28],
[24,25,23,0,23,31,24,32,27,26,25],
[23,23,24,28,0,26,27,31,27,20,17],
[17,23,19,20,25,0,21,30,27,22,20],
[19,22,27,27,24,30,0,34,30,25,23],
[17,24,23,19,20,21,17,0,24,17,15],
[20,21,14,24,24,24,21,27,0,22,19],
[22,23,23,25,31,29,26,34,29,0,25],
[29,28,23,26,34,31,28,36,32,26,0]])



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
result = np.append(np.array([11, 51, 171, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,38,28,22,29,30,30,31,26,30],
[28,0,29,29,23,31,24,29,31,27,34],
[13,22,0,19,11,19,26,15,14,11,24],
[23,22,32,0,23,25,28,23,24,19,26],
[29,28,40,28,0,25,28,33,25,24,32],
[22,20,32,26,26,0,30,31,25,19,31],
[21,27,25,23,23,21,0,22,24,21,22],
[21,22,36,28,18,20,29,0,24,22,23],
[20,20,37,27,26,26,27,27,0,24,28],
[25,24,40,32,27,32,30,29,27,0,36],
[21,17,27,25,19,20,29,28,23,15,0]])



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
result = np.append(np.array([11, 51, 172, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,35,24,35,35,27,27,51,27,35],
[28,0,51,24,51,23,27,35,39,35,23],
[16,0,0,0,11,0,12,11,24,12,11],
[27,27,51,0,39,31,23,39,39,39,31],
[16,0,40,12,0,4,12,11,28,12,15],
[16,28,51,20,47,0,12,39,51,39,27],
[24,24,39,28,39,39,0,39,39,51,39],
[24,16,40,12,40,12,12,0,28,28,23],
[0,12,27,12,23,0,12,23,0,12,11],
[24,16,39,12,39,12,0,23,39,0,23],
[16,28,40,20,36,24,12,28,40,28,0]])



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
result = np.append(np.array([11, 51, 173, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,17,24,20,22,14,20,26,23,17],
[36,0,20,29,28,23,25,24,30,30,28],
[34,31,0,34,17,28,27,26,30,33,32],
[27,22,17,0,17,19,19,24,27,21,22],
[31,23,34,34,0,27,23,29,34,30,29],
[29,28,23,32,24,0,19,24,32,24,22],
[37,26,24,32,28,32,0,31,35,32,28],
[31,27,25,27,22,27,20,0,31,19,22],
[25,21,21,24,17,19,16,20,0,21,22],
[28,21,18,30,21,27,19,32,30,0,23],
[34,23,19,29,22,29,23,29,29,28,0]])



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
result = np.append(np.array([11, 51, 174, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,17,17,17,9,26,11,16,18,20],
[34,0,28,26,20,30,41,24,27,24,32],
[34,23,0,24,25,22,24,20,25,32,23],
[34,25,27,0,24,24,32,21,28,32,30],
[34,31,26,27,0,22,35,21,20,29,29],
[42,21,29,27,29,0,26,27,19,28,30],
[25,10,27,19,16,25,0,22,18,22,26],
[40,27,31,30,30,24,29,0,21,25,30],
[35,24,26,23,31,32,33,30,0,28,29],
[33,27,19,19,22,23,29,26,23,0,25],
[31,19,28,21,22,21,25,21,22,26,0]])



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
result = np.append(np.array([11, 51, 175, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,33,27,29,32,34,30,31,24,26],
[17,0,22,15,19,23,28,23,23,21,22],
[18,29,0,18,18,20,24,21,24,19,21],
[24,36,33,0,31,30,25,31,28,26,28],
[22,32,33,20,0,28,27,25,27,25,27],
[19,28,31,21,23,0,27,18,25,23,24],
[17,23,27,26,24,24,0,26,20,26,24],
[21,28,30,20,26,33,25,0,26,23,27],
[20,28,27,23,24,26,31,25,0,25,32],
[27,30,32,25,26,28,25,28,26,0,25],
[25,29,30,23,24,27,27,24,19,26,0]])



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
result = np.append(np.array([11, 51, 176, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,25,35,22,31,31,33,36,24,29],
[26,0,33,34,28,26,31,18,33,30,32],
[26,18,0,29,22,18,26,18,24,18,21],
[16,17,22,0,28,20,19,14,21,17,19],
[29,23,29,23,0,32,37,21,36,20,27],
[20,25,33,31,19,0,27,16,35,27,21],
[20,20,25,32,14,24,0,12,22,15,17],
[18,33,33,37,30,35,39,0,37,33,27],
[15,18,27,30,15,16,29,14,0,27,21],
[27,21,33,34,31,24,36,18,24,0,27],
[22,19,30,32,24,30,34,24,30,24,0]])



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
result = np.append(np.array([11, 51, 177, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,31,29,30,31,28,25,26,27,25],
[24,0,29,29,28,23,28,28,27,29,18],
[20,22,0,22,23,23,21,23,14,19,18],
[22,22,29,0,26,28,26,27,24,26,22],
[21,23,28,25,0,32,26,24,19,23,25],
[20,28,28,23,19,0,25,24,22,22,21],
[23,23,30,25,25,26,0,22,26,25,22],
[26,23,28,24,27,27,29,0,25,23,25],
[25,24,37,27,32,29,25,26,0,30,26],
[24,22,32,25,28,29,26,28,21,0,27],
[26,33,33,29,26,30,29,26,25,24,0]])



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
result = np.append(np.array([11, 51, 178, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,23,24,27,26,29,30,20,22,26],
[32,0,26,31,36,26,25,29,24,31,26],
[28,25,0,26,27,25,22,24,24,31,27],
[27,20,25,0,22,22,22,26,28,29,24],
[24,15,24,29,0,26,23,28,20,30,20],
[25,25,26,29,25,0,25,27,29,27,28],
[22,26,29,29,28,26,0,30,28,33,28],
[21,22,27,25,23,24,21,0,22,30,24],
[31,27,27,23,31,22,23,29,0,28,24],
[29,20,20,22,21,24,18,21,23,0,21],
[25,25,24,27,31,23,23,27,27,30,0]])



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
result = np.append(np.array([11, 51, 179, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,42,33,34,31,18,20,40,33,39],
[18,0,20,26,32,35,18,26,26,35,24],
[9,31,0,19,29,37,18,26,26,28,17],
[18,25,32,0,23,23,18,29,35,31,20],
[17,19,22,28,0,26,18,15,15,8,17],
[20,16,14,28,25,0,18,26,37,30,28],
[33,33,33,33,33,33,0,20,31,33,39],
[31,25,25,22,36,25,31,0,40,25,31],
[11,25,25,16,36,14,20,11,0,20,31],
[18,16,23,20,43,21,18,26,31,0,29],
[12,27,34,31,34,23,12,20,20,22,0]])



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
result = np.append(np.array([11, 51, 180, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,29,21,33,19,24,33,21,15,18],
[35,0,36,28,44,38,26,37,23,28,26],
[22,15,0,16,21,20,16,21,14,17,14],
[30,23,35,0,30,34,32,30,29,29,25],
[18,7,30,21,0,28,19,30,21,17,24],
[32,13,31,17,23,0,17,22,23,20,17],
[27,25,35,19,32,34,0,30,19,19,18],
[18,14,30,21,21,29,21,0,26,21,19],
[30,28,37,22,30,28,32,25,0,25,24],
[36,23,34,22,34,31,32,30,26,0,20],
[33,25,37,26,27,34,33,32,27,31,0]])



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
result = np.append(np.array([11, 51, 181, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,17,20,19,23,16,30,28,22,16],
[27,0,20,20,26,27,24,30,25,26,23],
[34,31,0,26,28,31,25,34,36,28,26],
[31,31,25,0,24,22,21,27,31,25,20],
[32,25,23,27,0,30,22,27,32,27,25],
[28,24,20,29,21,0,25,28,27,26,19],
[35,27,26,30,29,26,0,29,28,27,20],
[21,21,17,24,24,23,22,0,27,23,14],
[23,26,15,20,19,24,23,24,0,23,14],
[29,25,23,26,24,25,24,28,28,0,21],
[35,28,25,31,26,32,31,37,37,30,0]])



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
result = np.append(np.array([11, 51, 182, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,17,11,18,24,12,24,21,18,18],
[27,0,27,14,23,29,22,26,16,22,21],
[34,24,0,19,27,24,22,29,22,22,26],
[40,37,32,0,30,32,26,35,22,33,31],
[33,28,24,21,0,28,27,34,21,24,26],
[27,22,27,19,23,0,16,23,19,20,22],
[39,29,29,25,24,35,0,28,25,25,25],
[27,25,22,16,17,28,23,0,21,22,21],
[30,35,29,29,30,32,26,30,0,29,24],
[33,29,29,18,27,31,26,29,22,0,26],
[33,30,25,20,25,29,26,30,27,25,0]])



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
result = np.append(np.array([11, 51, 183, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,26,28,27,25,24,33,22,20,22],
[28,0,28,28,30,28,24,36,28,28,25],
[25,23,0,28,25,20,19,29,22,22,18],
[23,23,23,0,24,25,24,29,21,17,23],
[24,21,26,27,0,24,28,24,25,27,24],
[26,23,31,26,27,0,24,29,24,29,28],
[27,27,32,27,23,27,0,29,24,23,25],
[18,15,22,22,27,22,22,0,21,20,14],
[29,23,29,30,26,27,27,30,0,27,24],
[31,23,29,34,24,22,28,31,24,0,28],
[29,26,33,28,27,23,26,37,27,23,0]])



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
result = np.append(np.array([11, 51, 184, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,24,27,22,25,21,27,24,30,31],
[26,0,27,24,23,31,21,24,25,28,32],
[27,24,0,25,26,28,27,24,25,29,31],
[24,27,26,0,28,30,23,29,27,28,31],
[29,28,25,23,0,34,25,27,23,28,29],
[26,20,23,21,17,0,22,26,20,26,25],
[30,30,24,28,26,29,0,25,28,27,30],
[24,27,27,22,24,25,26,0,23,26,29],
[27,26,26,24,28,31,23,28,0,27,27],
[21,23,22,23,23,25,24,25,24,0,25],
[20,19,20,20,22,26,21,22,24,26,0]])



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
result = np.append(np.array([11, 51, 185, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,22,25,29,23,26,29,25,17,27],
[22,0,20,20,22,23,20,27,25,18,23],
[29,31,0,26,33,28,24,31,26,18,31],
[26,31,25,0,31,25,24,26,26,22,27],
[22,29,18,20,0,20,22,19,20,21,27],
[28,28,23,26,31,0,29,28,23,22,22],
[25,31,27,27,29,22,0,26,28,25,27],
[22,24,20,25,32,23,25,0,25,26,28],
[26,26,25,25,31,28,23,26,0,24,25],
[34,33,33,29,30,29,26,25,27,0,27],
[24,28,20,24,24,29,24,23,26,24,0]])



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
result = np.append(np.array([11, 51, 186, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,28,28,27,26,21,23,19,25,26],
[23,0,24,19,27,20,21,16,18,24,19],
[23,27,0,24,30,19,21,17,24,24,21],
[23,32,27,0,32,22,23,17,25,25,22],
[24,24,21,19,0,20,20,18,19,24,17],
[25,31,32,29,31,0,21,21,21,25,18],
[30,30,30,28,31,30,0,25,24,28,28],
[28,35,34,34,33,30,26,0,25,30,26],
[32,33,27,26,32,30,27,26,0,26,22],
[26,27,27,26,27,26,23,21,25,0,19],
[25,32,30,29,34,33,23,25,29,32,0]])



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
result = np.append(np.array([11, 51, 187, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,33,25,32,34,31,28,23,28,31],
[23,0,32,28,27,31,31,25,25,18,29],
[18,19,0,21,28,26,28,31,23,25,24],
[26,23,30,0,29,31,23,35,19,17,30],
[19,24,23,22,0,14,23,18,19,19,19],
[17,20,25,20,37,0,31,32,29,21,27],
[20,20,23,28,28,20,0,24,23,20,25],
[23,26,20,16,33,19,27,0,24,25,25],
[28,26,28,32,32,22,28,27,0,31,32],
[23,33,26,34,32,30,31,26,20,0,28],
[20,22,27,21,32,24,26,26,19,23,0]])



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
result = np.append(np.array([11, 51, 188, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,28,23,24,23,29,25,30,26,27],
[28,0,31,31,33,28,23,27,29,24,35],
[23,20,0,17,20,18,18,12,15,21,25],
[28,20,34,0,26,28,26,25,25,29,31],
[27,18,31,25,0,26,29,19,22,24,30],
[28,23,33,23,25,0,29,20,23,20,32],
[22,28,33,25,22,22,0,20,21,27,35],
[26,24,39,26,32,31,31,0,25,27,30],
[21,22,36,26,29,28,30,26,0,26,30],
[25,27,30,22,27,31,24,24,25,0,31],
[24,16,26,20,21,19,16,21,21,20,0]])



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
result = np.append(np.array([11, 51, 189, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,26,28,31,35,29,24,28,27,26],
[26,0,25,27,31,34,25,28,30,29,28],
[25,26,0,27,30,30,26,33,27,27,28],
[23,24,24,0,33,33,28,29,31,26,30],
[20,20,21,18,0,25,21,22,19,22,20],
[16,17,21,18,26,0,24,25,24,21,19],
[22,26,25,23,30,27,0,24,28,21,25],
[27,23,18,22,29,26,27,0,26,26,26],
[23,21,24,20,32,27,23,25,0,29,18],
[24,22,24,25,29,30,30,25,22,0,25],
[25,23,23,21,31,32,26,25,33,26,0]])



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
result = np.append(np.array([11, 51, 190, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,31,30,28,33,27,30,25,30,29],
[24,0,25,26,22,24,26,24,28,28,24],
[20,26,0,26,25,23,24,23,26,26,20],
[21,25,25,0,25,28,25,22,26,27,26],
[23,29,26,26,0,27,25,24,25,28,28],
[18,27,28,23,24,0,27,21,24,26,29],
[24,25,27,26,26,24,0,26,25,28,24],
[21,27,28,29,27,30,25,0,27,30,27],
[26,23,25,25,26,27,26,24,0,27,28],
[21,23,25,24,23,25,23,21,24,0,20],
[22,27,31,25,23,22,27,24,23,31,0]])



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
result = np.append(np.array([11, 51, 191, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,23,27,25,24,26,25,25,23,23],
[26,0,22,26,25,24,25,31,29,27,24],
[28,29,0,27,24,25,27,29,26,26,24],
[24,25,24,0,21,25,21,26,24,23,24],
[26,26,27,30,0,24,29,25,28,23,29],
[27,27,26,26,27,0,24,30,30,29,28],
[25,26,24,30,22,27,0,28,25,27,22],
[26,20,22,25,26,21,23,0,26,23,22],
[26,22,25,27,23,21,26,25,0,19,24],
[28,24,25,28,28,22,24,28,32,0,26],
[28,27,27,27,22,23,29,29,27,25,0]])



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
result = np.append(np.array([11, 51, 192, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,29,25,28,38,39,33,32,33,30],
[20,0,26,36,27,33,39,22,24,25,16],
[22,25,0,23,22,33,36,22,32,33,24],
[26,15,28,0,24,33,39,25,22,33,20],
[23,24,29,27,0,30,32,25,20,23,19],
[13,18,18,18,21,0,25,23,18,20,16],
[12,12,15,12,19,26,0,18,17,17,19],
[18,29,29,26,26,28,33,0,28,32,20],
[19,27,19,29,31,33,34,23,0,23,19],
[18,26,18,18,28,31,34,19,28,0,17],
[21,35,27,31,32,35,32,31,32,34,0]])



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
result = np.append(np.array([11, 51, 193, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,27,26,26,24,28,28,29,29,28],
[24,0,20,22,25,24,25,23,28,30,23],
[24,31,0,28,32,34,31,28,32,31,26],
[25,29,23,0,27,24,30,26,22,29,26],
[25,26,19,24,0,27,29,25,19,28,20],
[27,27,17,27,24,0,28,29,19,30,23],
[23,26,20,21,22,23,0,24,19,24,22],
[23,28,23,25,26,22,27,0,25,22,24],
[22,23,19,29,32,32,32,26,0,34,27],
[22,21,20,22,23,21,27,29,17,0,22],
[23,28,25,25,31,28,29,27,24,29,0]])



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
result = np.append(np.array([11, 51, 194, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,26,23,22,25,22,31,23,24,29],
[31,0,31,23,29,28,29,27,29,29,25],
[25,20,0,20,23,25,26,25,24,21,26],
[28,28,31,0,29,26,23,31,25,27,24],
[29,22,28,22,0,29,28,31,27,28,26],
[26,23,26,25,22,0,21,25,24,21,22],
[29,22,25,28,23,30,0,28,28,24,26],
[20,24,26,20,20,26,23,0,22,20,27],
[28,22,27,26,24,27,23,29,0,23,23],
[27,22,30,24,23,30,27,31,28,0,31],
[22,26,25,27,25,29,25,24,28,20,0]])



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
result = np.append(np.array([11, 51, 195, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,31,26,27,33,23,24,28,24,27],
[23,0,28,25,28,25,23,25,27,28,30],
[20,23,0,25,24,25,20,24,22,23,22],
[25,26,26,0,28,28,20,29,27,26,26],
[24,23,27,23,0,27,21,22,27,24,21],
[18,26,26,23,24,0,26,22,20,22,26],
[28,28,31,31,30,25,0,30,28,29,27],
[27,26,27,22,29,29,21,0,24,27,27],
[23,24,29,24,24,31,23,27,0,23,24],
[27,23,28,25,27,29,22,24,28,0,26],
[24,21,29,25,30,25,24,24,27,25,0]])



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
result = np.append(np.array([11, 51, 196, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,19,29,27,28,21,23,28,26,25],
[25,0,19,26,22,26,23,25,28,19,25],
[32,32,0,30,34,26,26,25,29,26,29],
[22,25,21,0,26,21,27,23,28,22,19],
[24,29,17,25,0,22,19,22,24,20,22],
[23,25,25,30,29,0,27,24,27,28,31],
[30,28,25,24,32,24,0,24,26,26,24],
[28,26,26,28,29,27,27,0,29,24,31],
[23,23,22,23,27,24,25,22,0,24,22],
[25,32,25,29,31,23,25,27,27,0,28],
[26,26,22,32,29,20,27,20,29,23,0]])



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
result = np.append(np.array([11, 51, 197, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,19,31,24,25,24,25,26,28,31],
[19,0,17,26,29,29,30,23,16,27,25],
[32,34,0,41,35,28,38,25,24,31,47],
[20,25,10,0,17,22,21,29,19,24,17],
[27,22,16,34,0,22,22,26,19,21,24],
[26,22,23,29,29,0,35,24,20,29,36],
[27,21,13,30,29,16,0,20,18,24,28],
[26,28,26,22,25,27,31,0,23,26,31],
[25,35,27,32,32,31,33,28,0,28,35],
[23,24,20,27,30,22,27,25,23,0,25],
[20,26,4,34,27,15,23,20,16,26,0]])



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
result = np.append(np.array([11, 51, 198, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,30,27,29,25,26,30,31,26,30],
[26,0,30,24,33,28,25,29,29,27,27],
[21,21,0,23,23,18,18,23,24,21,23],
[24,27,28,0,26,23,30,29,27,28,26],
[22,18,28,25,0,22,21,26,23,23,22],
[26,23,33,28,29,0,30,32,30,28,31],
[25,26,33,21,30,21,0,30,28,25,26],
[21,22,28,22,25,19,21,0,23,22,24],
[20,22,27,24,28,21,23,28,0,24,27],
[25,24,30,23,28,23,26,29,27,0,27],
[21,24,28,25,29,20,25,27,24,24,0]])



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
result = np.append(np.array([11, 51, 199, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,25,21,20,23,22,24,23,22,22],
[27,0,25,17,23,22,20,25,26,28,24],
[26,26,0,22,24,27,24,24,29,31,26],
[30,34,29,0,26,31,23,27,30,28,26],
[31,28,27,25,0,22,25,23,26,20,31],
[28,29,24,20,29,0,24,23,29,28,26],
[29,31,27,28,26,27,0,28,25,26,27],
[27,26,27,24,28,28,23,0,24,27,24],
[28,25,22,21,25,22,26,27,0,26,29],
[29,23,20,23,31,23,25,24,25,0,21],
[29,27,25,25,20,25,24,27,22,30,0]])



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
result = np.append(np.array([11, 51, 200, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/me/me_11_51.csv", index=False, header=False)