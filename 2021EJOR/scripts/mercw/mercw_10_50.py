
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,24,21,21,21,18,18,22,19,20],
[26,0,23,31,24,19,23,27,34,28],
[29,27,0,28,24,24,23,23,21,23],
[29,19,22,0,21,22,20,25,22,21],
[29,26,26,29,0,19,17,22,27,27],
[32,31,26,28,31,0,33,29,26,24],
[32,27,27,30,33,17,0,27,24,27],
[28,23,27,25,28,21,23,0,19,21],
[31,16,29,28,23,24,26,31,0,19],
[30,22,27,29,23,26,23,29,31,0]])



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
result = np.append(np.array([10, 50, 1, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,25,31,25,23,23,28,25,25],
[25,0,24,25,21,22,21,27,19,27],
[25,26,0,27,24,24,21,24,21,29],
[19,25,23,0,19,16,21,22,21,25],
[25,29,26,31,0,27,29,27,19,25],
[27,28,26,34,23,0,27,26,28,27],
[27,29,29,29,21,23,0,25,21,27],
[22,23,26,28,23,24,25,0,23,29],
[25,31,29,29,31,22,29,27,0,28],
[25,23,21,25,25,23,23,21,22,0]])



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
result = np.append(np.array([10, 50, 2, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,28,34,30,21,26,24,24,22],
[23,0,26,27,26,23,23,25,24,23],
[22,24,0,28,27,24,22,21,22,21],
[16,23,22,0,29,22,22,19,24,22],
[20,24,23,21,0,21,24,22,20,21],
[29,27,26,28,29,0,29,23,23,24],
[24,27,28,28,26,21,0,19,21,21],
[26,25,29,31,28,27,31,0,21,30],
[26,26,28,26,30,27,29,29,0,24],
[28,27,29,28,29,26,29,20,26,0]])



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
result = np.append(np.array([10, 50, 3, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,21,20,23,22,26,17,20,21],
[31,0,23,24,23,20,31,21,24,23],
[29,27,0,26,33,24,31,16,31,27],
[30,26,24,0,27,32,32,22,33,29],
[27,27,17,23,0,23,21,16,25,20],
[28,30,26,18,27,0,24,27,29,24],
[24,19,19,18,29,26,0,13,21,20],
[33,29,34,28,34,23,37,0,30,28],
[30,26,19,17,25,21,29,20,0,21],
[29,27,23,21,30,26,30,22,29,0]])



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
result = np.append(np.array([10, 50, 4, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,23,26,30,33,23,34,26,34],
[25,0,30,27,23,36,30,35,30,28],
[27,20,0,29,23,35,29,36,31,29],
[24,23,21,0,25,30,35,35,26,31],
[20,27,27,25,0,30,23,32,29,27],
[17,14,15,20,20,0,24,16,20,18],
[27,20,21,15,27,26,0,25,28,31],
[16,15,14,15,18,34,25,0,16,19],
[24,20,19,24,21,30,22,34,0,23],
[16,22,21,19,23,32,19,31,27,0]])



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
result = np.append(np.array([10, 50, 5, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,30,14,18,28,21,22,23,24],
[34,0,33,28,23,30,28,30,35,34],
[20,17,0,19,24,23,15,23,26,25],
[36,22,31,0,28,33,24,27,24,29],
[32,27,26,22,0,28,24,30,23,30],
[22,20,27,17,22,0,22,25,24,27],
[29,22,35,26,26,28,0,30,26,25],
[28,20,27,23,20,25,20,0,30,27],
[27,15,24,26,27,26,24,20,0,24],
[26,16,25,21,20,23,25,23,26,0]])



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
result = np.append(np.array([10, 50, 6, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,25,31,26,25,23,19,28,30],
[26,0,27,27,24,24,26,21,26,29],
[25,23,0,32,27,23,23,23,21,25],
[19,23,18,0,27,32,19,28,20,20],
[24,26,23,23,0,21,26,19,28,22],
[25,26,27,18,29,0,18,13,21,26],
[27,24,27,31,24,32,0,27,29,30],
[31,29,27,22,31,37,23,0,24,36],
[22,24,29,30,22,29,21,26,0,28],
[20,21,25,30,28,24,20,14,22,0]])



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
result = np.append(np.array([10, 50, 7, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,0,0,19,7,7,7,32,19],
[43,0,43,43,43,13,25,25,25,25],
[50,7,0,32,37,20,19,20,32,32],
[50,7,18,0,37,20,19,20,32,32],
[31,7,13,13,0,20,7,20,20,20],
[43,37,30,30,30,0,37,37,25,19],
[43,25,31,31,43,13,0,20,25,25],
[43,25,30,30,30,13,30,0,25,12],
[18,25,18,18,30,25,25,25,0,25],
[31,25,18,18,30,31,25,38,25,0]])



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
result = np.append(np.array([10, 50, 8, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,14,21,19,18,26,20,14,10],
[32,0,17,27,22,17,27,21,22,17],
[36,33,0,22,31,21,28,28,27,27],
[29,23,28,0,27,27,30,25,25,25],
[31,28,19,23,0,23,34,21,22,20],
[32,33,29,23,27,0,27,27,22,24],
[24,23,22,20,16,23,0,19,26,21],
[30,29,22,25,29,23,31,0,18,20],
[36,28,23,25,28,28,24,32,0,25],
[40,33,23,25,30,26,29,30,25,0]])



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
result = np.append(np.array([10, 50, 9, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,22,27,25,31,29,21,25,30],
[21,0,25,20,26,28,26,27,27,29],
[28,25,0,24,19,20,24,26,24,23],
[23,30,26,0,24,24,27,24,28,31],
[25,24,31,26,0,29,25,28,29,30],
[19,22,30,26,21,0,23,20,27,25],
[21,24,26,23,25,27,0,22,26,28],
[29,23,24,26,22,30,28,0,24,32],
[25,23,26,22,21,23,24,26,0,30],
[20,21,27,19,20,25,22,18,20,0]])



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
result = np.append(np.array([10, 50, 10, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,25,21,18,22,32,17,22,14],
[12,0,26,13,6,20,11,15,15,12],
[25,24,0,23,18,23,16,19,18,13],
[29,37,27,0,20,30,25,33,30,22],
[32,44,32,30,0,28,30,40,32,25],
[28,30,27,20,22,0,30,24,21,11],
[18,39,34,25,20,20,0,29,26,21],
[33,35,31,17,10,26,21,0,25,15],
[28,35,32,20,18,29,24,25,0,13],
[36,38,37,28,25,39,29,35,37,0]])



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
result = np.append(np.array([10, 50, 11, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,25,19,29,21,21,24,19,25],
[34,0,30,27,30,25,29,29,27,28],
[25,20,0,20,26,23,25,27,21,30],
[31,23,30,0,33,29,30,33,23,31],
[21,20,24,17,0,23,22,21,23,27],
[29,25,27,21,27,0,30,28,25,34],
[29,21,25,20,28,20,0,28,25,27],
[26,21,23,17,29,22,22,0,25,25],
[31,23,29,27,27,25,25,25,0,33],
[25,22,20,19,23,16,23,25,17,0]])



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
result = np.append(np.array([10, 50, 12, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,23,28,27,24,28,27,29,25],
[20,0,14,24,20,22,15,21,27,18],
[27,36,0,31,32,32,23,29,31,27],
[22,26,19,0,19,27,21,20,30,21],
[23,30,18,31,0,29,22,25,31,26],
[26,28,18,23,21,0,17,21,32,24],
[22,35,27,29,28,33,0,26,31,21],
[23,29,21,30,25,29,24,0,30,21],
[21,23,19,20,19,18,19,20,0,19],
[25,32,23,29,24,26,29,29,31,0]])



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
result = np.append(np.array([10, 50, 13, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,2,5,7,7,7,48,7,23],
[30,0,25,30,32,32,32,30,32,30],
[48,25,0,5,7,7,7,48,7,23],
[45,20,45,0,50,25,32,43,45,48],
[43,18,43,0,0,18,30,43,43,43],
[43,18,43,25,32,0,30,43,27,43],
[43,18,43,18,20,20,0,43,45,43],
[2,20,2,7,7,7,7,0,2,5],
[43,18,43,5,7,23,5,48,0,48],
[27,20,27,2,7,7,7,45,2,0]])



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
result = np.append(np.array([10, 50, 14, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,25,30,32,30,27,35,27,30],
[18,0,16,22,22,26,22,33,24,25],
[25,34,0,27,24,27,23,36,30,32],
[20,28,23,0,21,27,26,33,18,24],
[18,28,26,29,0,31,28,33,31,28],
[20,24,23,23,19,0,24,32,21,23],
[23,28,27,24,22,26,0,38,25,27],
[15,17,14,17,17,18,12,0,18,18],
[23,26,20,32,19,29,25,32,0,29],
[20,25,18,26,22,27,23,32,21,0]])



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
result = np.append(np.array([10, 50, 15, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,18,28,24,21,22,30,16,16],
[28,0,19,23,21,21,22,25,19,18],
[32,31,0,28,29,26,31,28,29,22],
[22,27,22,0,25,19,18,23,20,16],
[26,29,21,25,0,27,32,34,19,26],
[29,29,24,31,23,0,32,33,22,26],
[28,28,19,32,18,18,0,31,20,14],
[20,25,22,27,16,17,19,0,22,19],
[34,31,21,30,31,28,30,28,0,27],
[34,32,28,34,24,24,36,31,23,0]])



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
result = np.append(np.array([10, 50, 16, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,5,37,13,11,29,29,35,23],
[21,0,21,36,21,18,22,25,28,31],
[45,29,0,44,30,41,36,42,42,25],
[13,14,6,0,14,13,18,13,20,13],
[37,29,20,36,0,25,36,27,49,24],
[39,32,9,37,25,0,31,29,39,33],
[21,28,14,32,14,19,0,18,28,21],
[21,25,8,37,23,21,32,0,44,25],
[15,22,8,30,1,11,22,6,0,11],
[27,19,25,37,26,17,29,25,39,0]])



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
result = np.append(np.array([10, 50, 17, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,19,27,32,24,18,20,27,24],
[24,0,28,30,30,28,21,27,28,26],
[31,22,0,30,33,29,32,25,26,29],
[23,20,20,0,31,33,22,24,29,28],
[18,20,17,19,0,24,17,20,19,20],
[26,22,21,17,26,0,19,23,19,22],
[32,29,18,28,33,31,0,30,26,26],
[30,23,25,26,30,27,20,0,24,23],
[23,22,24,21,31,31,24,26,0,25],
[26,24,21,22,30,28,24,27,25,0]])



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
result = np.append(np.array([10, 50, 18, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,25,26,21,23,19,29,24,24],
[32,0,31,28,28,26,28,25,29,28],
[25,19,0,23,22,25,21,26,27,21],
[24,22,27,0,26,24,24,25,28,26],
[29,22,28,24,0,26,28,33,28,28],
[27,24,25,26,24,0,25,28,23,22],
[31,22,29,26,22,25,0,29,30,25],
[21,25,24,25,17,22,21,0,28,22],
[26,21,23,22,22,27,20,22,0,25],
[26,22,29,24,22,28,25,28,25,0]])



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
result = np.append(np.array([10, 50, 19, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,28,27,28,25,21,33,33,29],
[17,0,22,23,17,11,20,25,26,15],
[22,28,0,24,26,23,23,27,28,23],
[23,27,26,0,23,20,23,29,26,24],
[22,33,24,27,0,23,23,27,26,16],
[25,39,27,30,27,0,27,32,30,26],
[29,30,27,27,27,23,0,34,30,21],
[17,25,23,21,23,18,16,0,24,16],
[17,24,22,24,24,20,20,26,0,21],
[21,35,27,26,34,24,29,34,29,0]])



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
result = np.append(np.array([10, 50, 20, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,25,22,28,22,29,22,24,26],
[26,0,17,25,26,24,26,26,24,25],
[25,33,0,30,29,30,28,36,30,28],
[28,25,20,0,28,26,29,26,24,22],
[22,24,21,22,0,23,23,22,22,20],
[28,26,20,24,27,0,25,24,25,27],
[21,24,22,21,27,25,0,26,26,28],
[28,24,14,24,28,26,24,0,27,24],
[26,26,20,26,28,25,24,23,0,25],
[24,25,22,28,30,23,22,26,25,0]])



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
result = np.append(np.array([10, 50, 21, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,25,28,24,25,26,29,23,26],
[22,0,18,22,22,15,18,30,19,10],
[25,32,0,35,26,24,32,35,28,22],
[22,28,15,0,27,21,25,34,26,20],
[26,28,24,23,0,23,25,34,20,26],
[25,35,26,29,27,0,29,37,31,25],
[24,32,18,25,25,21,0,28,23,22],
[21,20,15,16,16,13,22,0,17,18],
[27,31,22,24,30,19,27,33,0,23],
[24,40,28,30,24,25,28,32,27,0]])



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
result = np.append(np.array([10, 50, 22, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,21,26,23,25,21,21,24,22],
[31,0,30,31,30,25,30,28,29,30],
[29,20,0,22,24,20,26,22,22,24],
[24,19,28,0,24,24,26,24,28,28],
[27,20,26,26,0,21,25,25,25,22],
[25,25,30,26,29,0,25,26,25,25],
[29,20,24,24,25,25,0,22,23,22],
[29,22,28,26,25,24,28,0,29,29],
[26,21,28,22,25,25,27,21,0,25],
[28,20,26,22,28,25,28,21,25,0]])



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
result = np.append(np.array([10, 50, 23, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,38,24,23,23,29,25,29,29],
[19,0,33,18,23,18,19,19,28,21],
[12,17,0,17,15,15,21,20,25,19],
[26,32,33,0,24,22,31,25,37,25],
[27,27,35,26,0,26,25,20,34,27],
[27,32,35,28,24,0,27,21,28,29],
[21,31,29,19,25,23,0,22,27,26],
[25,31,30,25,30,29,28,0,27,32],
[21,22,25,13,16,22,23,23,0,24],
[21,29,31,25,23,21,24,18,26,0]])



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
result = np.append(np.array([10, 50, 24, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,16,18,34,29,12,18,22,24],
[40,0,23,32,32,32,42,25,30,34],
[34,27,0,24,29,38,33,33,39,30],
[32,18,26,0,35,38,19,29,34,19],
[16,18,21,15,0,28,24,17,18,10],
[21,18,12,12,22,0,17,25,16,20],
[38,8,17,31,26,33,0,22,27,30],
[32,25,17,21,33,25,28,0,30,32],
[28,20,11,16,32,34,23,20,0,26],
[26,16,20,31,40,30,20,18,24,0]])



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
result = np.append(np.array([10, 50, 25, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,29,24,20,22,24,20,18,22],
[26,0,35,27,31,18,30,32,26,26],
[21,15,0,26,20,20,26,17,14,14],
[26,23,24,0,14,14,21,21,19,10],
[30,19,30,36,0,32,28,32,31,20],
[28,32,30,36,18,0,27,27,36,27],
[26,20,24,29,22,23,0,21,19,18],
[30,18,33,29,18,23,29,0,30,21],
[32,24,36,31,19,14,31,20,0,21],
[28,24,36,40,30,23,32,29,29,0]])



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
result = np.append(np.array([10, 50, 26, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,27,25,26,23,23,26,24,25],
[26,0,31,25,29,24,27,30,30,29],
[23,19,0,21,23,21,26,28,22,26],
[25,25,29,0,26,27,27,32,28,25],
[24,21,27,24,0,22,24,25,27,23],
[27,26,29,23,28,0,30,29,26,24],
[27,23,24,23,26,20,0,28,27,29],
[24,20,22,18,25,21,22,0,21,19],
[26,20,28,22,23,24,23,29,0,26],
[25,21,24,25,27,26,21,31,24,0]])



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
result = np.append(np.array([10, 50, 27, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,32,23,25,26,19,20,18,24],
[24,0,39,24,25,31,30,23,23,22],
[18,11,0,8,15,13,12,22,10,13],
[27,26,42,0,24,30,31,32,24,22],
[25,25,35,26,0,36,29,22,23,15],
[24,19,37,20,14,0,24,22,24,19],
[31,20,38,19,21,26,0,17,21,26],
[30,27,28,18,28,28,33,0,26,18],
[32,27,40,26,27,26,29,24,0,25],
[26,28,37,28,35,31,24,32,25,0]])



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
result = np.append(np.array([10, 50, 28, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,18,20,29,18,28,22,28,24],
[27,0,10,12,23,11,21,28,22,28],
[32,40,0,18,41,30,29,40,40,30],
[30,38,32,0,30,14,30,31,29,32],
[21,27,9,20,0,7,18,17,29,9],
[32,39,20,36,43,0,30,32,37,21],
[22,29,21,20,32,20,0,30,30,32],
[28,22,10,19,33,18,20,0,30,22],
[22,28,10,21,21,13,20,20,0,21],
[26,22,20,18,41,29,18,28,29,0]])



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
result = np.append(np.array([10, 50, 29, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,26,22,30,21,19,23,27,21],
[19,0,14,19,20,15,14,13,19,18],
[24,36,0,26,28,22,22,25,26,21],
[28,31,24,0,33,21,21,26,29,31],
[20,30,22,17,0,20,17,25,21,23],
[29,35,28,29,30,0,24,30,30,30],
[31,36,28,29,33,26,0,28,25,29],
[27,37,25,24,25,20,22,0,29,25],
[23,31,24,21,29,20,25,21,0,23],
[29,32,29,19,27,20,21,25,27,0]])



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
result = np.append(np.array([10, 50, 30, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,34,28,34,31,30,37,40,27],
[26,0,27,28,29,30,33,21,28,26],
[16,23,0,12,17,8,29,15,25,12],
[22,22,38,0,33,26,30,34,36,30],
[16,21,33,17,0,17,38,22,33,26],
[19,20,42,24,33,0,29,28,36,26],
[20,17,21,20,12,21,0,20,33,14],
[13,29,35,16,28,22,30,0,29,35],
[10,22,25,14,17,14,17,21,0,17],
[23,24,38,20,24,24,36,15,33,0]])



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
result = np.append(np.array([10, 50, 31, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,24,26,22,27,24,33,25,33],
[18,0,22,18,19,20,18,23,18,22],
[26,28,0,24,30,28,17,29,24,27],
[24,32,26,0,23,27,20,30,28,35],
[28,31,20,27,0,27,22,32,26,32],
[23,30,22,23,23,0,25,26,29,28],
[26,32,33,30,28,25,0,35,32,35],
[17,27,21,20,18,24,15,0,24,30],
[25,32,26,22,24,21,18,26,0,25],
[17,28,23,15,18,22,15,20,25,0]])



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
result = np.append(np.array([10, 50, 32, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,31,24,35,28,16,24,35,24],
[22,0,46,46,46,31,38,46,33,46],
[19,4,0,8,15,12,0,0,22,8],
[26,4,42,0,35,4,4,11,14,4],
[15,4,35,15,0,4,15,15,26,15],
[22,19,38,46,46,0,28,22,37,36],
[34,12,50,46,35,22,0,37,37,12],
[26,4,50,39,35,28,13,0,22,25],
[15,17,28,36,24,13,13,28,0,21],
[26,4,42,46,35,14,38,25,29,0]])



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
result = np.append(np.array([10, 50, 33, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,30,27,34,31,33,32,21,34],
[17,0,29,25,28,22,23,27,22,27],
[20,21,0,33,30,23,27,25,23,31],
[23,25,17,0,27,25,32,20,23,32],
[16,22,20,23,0,20,20,26,16,29],
[19,28,27,25,30,0,27,24,25,30],
[17,27,23,18,30,23,0,24,24,29],
[18,23,25,30,24,26,26,0,24,27],
[29,28,27,27,34,25,26,26,0,29],
[16,23,19,18,21,20,21,23,21,0]])



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
result = np.append(np.array([10, 50, 34, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,26,28,24,25,28,18,29,21],
[19,0,25,21,20,24,26,17,21,18],
[24,25,0,25,20,26,27,18,24,16],
[22,29,25,0,24,27,30,21,26,27],
[26,30,30,26,0,31,30,22,24,23],
[25,26,24,23,19,0,34,18,17,19],
[22,24,23,20,20,16,0,16,18,20],
[32,33,32,29,28,32,34,0,29,25],
[21,29,26,24,26,33,32,21,0,26],
[29,32,34,23,27,31,30,25,24,0]])



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
result = np.append(np.array([10, 50, 35, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,27,25,24,21,23,19,25,25],
[25,0,24,26,20,23,18,16,21,24],
[23,26,0,23,23,23,21,21,23,27],
[25,24,27,0,17,19,18,20,23,25],
[26,30,27,33,0,29,26,22,25,27],
[29,27,27,31,21,0,26,19,27,30],
[27,32,29,32,24,24,0,22,29,30],
[31,34,29,30,28,31,28,0,34,25],
[25,29,27,27,25,23,21,16,0,22],
[25,26,23,25,23,20,20,25,28,0]])



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
result = np.append(np.array([10, 50, 36, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,15,20,16,26,17,27,19,20],
[33,0,25,19,25,34,27,32,24,26],
[35,25,0,21,30,34,25,36,28,34],
[30,31,29,0,27,30,27,32,27,25],
[34,25,20,23,0,34,20,25,23,31],
[24,16,16,20,16,0,15,20,16,22],
[33,23,25,23,30,35,0,30,26,34],
[23,18,14,18,25,30,20,0,18,29],
[31,26,22,23,27,34,24,32,0,26],
[30,24,16,25,19,28,16,21,24,0]])



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
result = np.append(np.array([10, 50, 37, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,28,27,26,22,26,33,26,21],
[24,0,23,23,22,20,14,31,33,22],
[22,27,0,21,27,16,21,29,32,33],
[23,27,29,0,35,28,22,33,37,25],
[24,28,23,15,0,26,16,27,24,23],
[28,30,34,22,24,0,26,36,35,26],
[24,36,29,28,34,24,0,32,34,29],
[17,19,21,17,23,14,18,0,20,17],
[24,17,18,13,26,15,16,30,0,17],
[29,28,17,25,27,24,21,33,33,0]])



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
result = np.append(np.array([10, 50, 38, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,17,21,22,32,32,38,30,34],
[17,0,18,21,19,32,23,41,24,18],
[33,32,0,19,19,32,28,36,30,31],
[29,29,31,0,22,31,31,42,30,29],
[28,31,31,28,0,29,23,37,27,26],
[18,18,18,19,21,0,22,39,22,26],
[18,27,22,19,27,28,0,41,30,33],
[12,9,14,8,13,11,9,0,20,11],
[20,26,20,20,23,28,20,30,0,26],
[16,32,19,21,24,24,17,39,24,0]])



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
result = np.append(np.array([10, 50, 39, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,32,34,30,32,25,28,28,23],
[22,0,25,28,28,26,24,25,27,28],
[18,25,0,22,23,26,16,26,26,24],
[16,22,28,0,23,24,16,24,20,23],
[20,22,27,27,0,29,19,31,24,19],
[18,24,24,26,21,0,18,25,20,22],
[25,26,34,34,31,32,0,29,25,23],
[22,25,24,26,19,25,21,0,23,20],
[22,23,24,30,26,30,25,27,0,26],
[27,22,26,27,31,28,27,30,24,0]])



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
result = np.append(np.array([10, 50, 40, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,28,35,29,18,36,23,25,21],
[36,0,36,35,31,30,45,27,21,26],
[22,14,0,20,27,22,36,25,14,29],
[15,15,30,0,34,16,25,29,18,27],
[21,19,23,16,0,24,19,29,22,21],
[32,20,28,34,26,0,35,17,22,36],
[14,5,14,25,31,15,0,14,20,18],
[27,23,25,21,21,33,36,0,20,28],
[25,29,36,32,28,28,30,30,0,27],
[29,24,21,23,29,14,32,22,23,0]])



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
result = np.append(np.array([10, 50, 41, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,25,27,30,35,23,33,23,32],
[22,0,24,30,26,23,20,25,27,28],
[25,26,0,30,26,28,21,33,23,30],
[23,20,20,0,19,25,25,27,29,25],
[20,24,24,31,0,24,23,28,29,28],
[15,27,22,25,26,0,22,24,22,27],
[27,30,29,25,27,28,0,34,27,31],
[17,25,17,23,22,26,16,0,22,22],
[27,23,27,21,21,28,23,28,0,29],
[18,22,20,25,22,23,19,28,21,0]])



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
result = np.append(np.array([10, 50, 42, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,34,37,34,29,24,38,32,33],
[18,0,26,29,23,25,26,26,21,21],
[16,24,0,26,23,23,25,28,26,25],
[13,21,24,0,16,20,20,22,20,16],
[16,27,27,34,0,25,23,27,26,26],
[21,25,27,30,25,0,22,25,27,25],
[26,24,25,30,27,28,0,28,20,21],
[12,24,22,28,23,25,22,0,19,23],
[18,29,24,30,24,23,30,31,0,28],
[17,29,25,34,24,25,29,27,22,0]])



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
result = np.append(np.array([10, 50, 43, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,18,23,25,19,26,26,32,23],
[27,0,25,24,30,26,22,30,32,23],
[32,25,0,20,28,28,23,23,35,27],
[27,26,30,0,35,28,25,33,33,33],
[25,20,22,15,0,24,23,25,28,19],
[31,24,22,22,26,0,20,27,26,23],
[24,28,27,25,27,30,0,31,33,27],
[24,20,27,17,25,23,19,0,27,21],
[18,18,15,17,22,24,17,23,0,25],
[27,27,23,17,31,27,23,29,25,0]])



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
result = np.append(np.array([10, 50, 44, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,26,29,29,35,25,30,37,32],
[17,0,26,16,28,28,26,35,25,26],
[24,24,0,18,32,26,23,20,24,33],
[21,34,32,0,30,33,24,32,26,24],
[21,22,18,20,0,28,19,22,23,27],
[15,22,24,17,22,0,30,26,22,25],
[25,24,27,26,31,20,0,30,22,25],
[20,15,30,18,28,24,20,0,28,26],
[13,25,26,24,27,28,28,22,0,25],
[18,24,17,26,23,25,25,24,25,0]])



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
result = np.append(np.array([10, 50, 45, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,27,32,31,28,28,15,27,28],
[23,0,19,27,25,20,21,19,20,19],
[23,31,0,30,32,31,33,14,28,26],
[18,23,20,0,31,29,20,18,29,23],
[19,25,18,19,0,21,26,13,22,17],
[22,30,19,21,29,0,27,17,27,18],
[22,29,17,30,24,23,0,24,24,13],
[35,31,36,32,37,33,26,0,40,25],
[23,30,22,21,28,23,26,10,0,22],
[22,31,24,27,33,32,37,25,28,0]])



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
result = np.append(np.array([10, 50, 46, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,34,32,30,30,30,31,25,31],
[20,0,25,17,23,25,27,21,20,21],
[16,25,0,25,18,29,30,24,16,27],
[18,33,25,0,26,24,33,30,20,23],
[20,27,32,24,0,25,28,29,25,27],
[20,25,21,26,25,0,26,27,22,21],
[20,23,20,17,22,24,0,19,18,18],
[19,29,26,20,21,23,31,0,16,26],
[25,30,34,30,25,28,32,34,0,31],
[19,29,23,27,23,29,32,24,19,0]])



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
result = np.append(np.array([10, 50, 47, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,15,28,16,30,15,23,16,14],
[35,0,23,32,22,34,25,34,21,26],
[35,27,0,37,26,30,28,34,27,25],
[22,18,13,0,19,19,17,21,17,18],
[34,28,24,31,0,30,26,29,28,30],
[20,16,20,31,20,0,22,23,19,22],
[35,25,22,33,24,28,0,35,24,27],
[27,16,16,29,21,27,15,0,18,19],
[34,29,23,33,22,31,26,32,0,28],
[36,24,25,32,20,28,23,31,22,0]])



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
result = np.append(np.array([10, 50, 48, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,19,24,23,15,30,28,30,21],
[27,0,18,21,23,18,25,25,27,19],
[31,32,0,32,26,21,26,27,35,25],
[26,29,18,0,28,21,32,34,36,21],
[27,27,24,22,0,21,28,27,30,21],
[35,32,29,29,29,0,35,32,37,25],
[20,25,24,18,22,15,0,23,29,15],
[22,25,23,16,23,18,27,0,31,13],
[20,23,15,14,20,13,21,19,0,17],
[29,31,25,29,29,25,35,37,33,0]])



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
result = np.append(np.array([10, 50, 49, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,32,26,28,24,26,25,18,26],
[24,0,28,28,30,26,21,24,26,19],
[18,22,0,22,28,25,17,19,19,19],
[24,22,28,0,35,34,24,22,25,23],
[22,20,22,15,0,24,14,17,17,21],
[26,24,25,16,26,0,22,22,22,19],
[24,29,33,26,36,28,0,27,24,25],
[25,26,31,28,33,28,23,0,26,24],
[32,24,31,25,33,28,26,24,0,24],
[24,31,31,27,29,31,25,26,26,0]])



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
result = np.append(np.array([10, 50, 50, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,23,22,35,33,33,41,12,29],
[10,0,2,12,31,23,21,20,12,31],
[27,48,0,20,43,48,21,29,27,29],
[28,38,30,0,40,30,40,19,38,26],
[15,19,7,10,0,40,21,18,17,18],
[17,27,2,20,10,0,21,18,27,18],
[17,29,29,10,29,29,0,10,17,10],
[9,30,21,31,32,32,40,0,19,38],
[38,38,23,12,33,23,33,31,0,19],
[21,19,21,24,32,32,40,12,31,0]])



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
result = np.append(np.array([10, 50, 51, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,37,24,26,32,26,37,22,31],
[33,0,36,32,36,35,41,43,25,32],
[13,14,0,23,17,15,16,25,19,20],
[26,18,27,0,22,28,31,36,26,32],
[24,14,33,28,0,26,27,41,21,18],
[18,15,35,22,24,0,29,30,17,11],
[24,9,34,19,23,21,0,33,16,25],
[13,7,25,14,9,20,17,0,10,7],
[28,25,31,24,29,33,34,40,0,37],
[19,18,30,18,32,39,25,43,13,0]])



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
result = np.append(np.array([10, 50, 52, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,26,32,27,29,31,13,29,19],
[31,0,27,32,26,32,34,21,28,26],
[24,23,0,22,19,17,21,20,19,19],
[18,18,28,0,19,19,24,19,26,16],
[23,24,31,31,0,35,34,23,37,24],
[21,18,33,31,15,0,20,11,26,18],
[19,16,29,26,16,30,0,17,30,26],
[37,29,30,31,27,39,33,0,23,29],
[21,22,31,24,13,24,20,27,0,22],
[31,24,31,34,26,32,24,21,28,0]])



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
result = np.append(np.array([10, 50, 53, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,26,23,21,17,24,18,19,26],
[31,0,26,25,27,21,22,27,26,22],
[24,24,0,27,24,12,19,27,21,22],
[27,25,23,0,26,25,23,18,24,20],
[29,23,26,24,0,19,20,30,29,25],
[33,29,38,25,31,0,22,26,26,36],
[26,28,31,27,30,28,0,34,35,24],
[32,23,23,32,20,24,16,0,28,19],
[31,24,29,26,21,24,15,22,0,24],
[24,28,28,30,25,14,26,31,26,0]])



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
result = np.append(np.array([10, 50, 54, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,26,27,27,23,24,23,24,19],
[31,0,27,29,26,24,27,24,31,23],
[24,23,0,23,25,24,23,20,23,26],
[23,21,27,0,23,25,25,23,27,19],
[23,24,25,27,0,20,27,23,21,20],
[27,26,26,25,30,0,31,26,29,27],
[26,23,27,25,23,19,0,21,25,17],
[27,26,30,27,27,24,29,0,30,23],
[26,19,27,23,29,21,25,20,0,22],
[31,27,24,31,30,23,33,27,28,0]])



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
result = np.append(np.array([10, 50, 55, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,32,31,40,25,31,29,31,23],
[19,0,28,28,27,23,26,20,25,26],
[18,22,0,30,32,22,29,21,31,21],
[19,22,20,0,28,15,23,13,22,15],
[10,23,18,22,0,13,19,19,19,15],
[25,27,28,35,37,0,32,20,28,30],
[19,24,21,27,31,18,0,13,26,23],
[21,30,29,37,31,30,37,0,21,24],
[19,25,19,28,31,22,24,29,0,18],
[27,24,29,35,35,20,27,26,32,0]])



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
result = np.append(np.array([10, 50, 56, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,23,25,29,22,21,22,22,23],
[25,0,26,30,27,23,27,32,29,30],
[27,24,0,29,27,25,26,26,25,22],
[25,20,21,0,29,22,24,21,25,23],
[21,23,23,21,0,22,23,22,24,21],
[28,27,25,28,28,0,27,25,31,29],
[29,23,24,26,27,23,0,23,23,24],
[28,18,24,29,28,25,27,0,22,26],
[28,21,25,25,26,19,27,28,0,19],
[27,20,28,27,29,21,26,24,31,0]])



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
result = np.append(np.array([10, 50, 57, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,28,26,19,25,20,17,24,31],
[26,0,26,25,25,23,28,25,27,28],
[22,24,0,25,21,22,24,23,18,28],
[24,25,25,0,14,23,18,24,22,23],
[31,25,29,36,0,20,23,23,26,33],
[25,27,28,27,30,0,26,19,25,30],
[30,22,26,32,27,24,0,22,26,35],
[33,25,27,26,27,31,28,0,21,26],
[26,23,32,28,24,25,24,29,0,24],
[19,22,22,27,17,20,15,24,26,0]])



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
result = np.append(np.array([10, 50, 58, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,27,20,32,14,25,20,25,12],
[29,0,38,24,32,19,30,35,26,41],
[23,12,0,29,17,17,26,29,26,17],
[30,26,21,0,26,26,30,31,32,23],
[18,18,33,24,0,18,32,30,32,18],
[36,31,33,24,32,0,30,35,32,36],
[25,20,24,20,18,20,0,20,19,25],
[30,15,21,19,20,15,30,0,21,23],
[25,24,24,18,18,18,31,29,0,23],
[38,9,33,27,32,14,25,27,27,0]])



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
result = np.append(np.array([10, 50, 59, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,24,18,29,22,13,20,25,33],
[24,0,23,25,29,23,27,20,33,35],
[26,27,0,26,24,24,24,24,26,37],
[32,25,24,0,29,32,28,18,33,32],
[21,21,26,21,0,23,17,18,25,23],
[28,27,26,18,27,0,22,25,23,28],
[37,23,26,22,33,28,0,26,38,32],
[30,30,26,32,32,25,24,0,29,38],
[25,17,24,17,25,27,12,21,0,25],
[17,15,13,18,27,22,18,12,25,0]])



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
result = np.append(np.array([10, 50, 60, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,22,23,30,22,29,16,31,32],
[30,0,19,25,22,23,26,27,25,31],
[28,31,0,24,33,26,28,26,24,27],
[27,25,26,0,29,28,25,20,30,26],
[20,28,17,21,0,22,28,22,32,34],
[28,27,24,22,28,0,37,18,37,33],
[21,24,22,25,22,13,0,17,29,24],
[34,23,24,30,28,32,33,0,36,33],
[19,25,26,20,18,13,21,14,0,26],
[18,19,23,24,16,17,26,17,24,0]])



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
result = np.append(np.array([10, 50, 61, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,18,21,33,21,19,23,19,27],
[29,0,25,29,28,24,23,23,25,27],
[32,25,0,24,31,27,28,27,19,26],
[29,21,26,0,29,27,28,24,24,28],
[17,22,19,21,0,24,19,20,16,23],
[29,26,23,23,26,0,24,22,19,27],
[31,27,22,22,31,26,0,21,19,27],
[27,27,23,26,30,28,29,0,22,30],
[31,25,31,26,34,31,31,28,0,29],
[23,23,24,22,27,23,23,20,21,0]])



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
result = np.append(np.array([10, 50, 62, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,21,29,23,22,26,21,21,26],
[29,0,26,26,16,19,28,27,27,26],
[29,24,0,26,17,11,24,22,23,22],
[21,24,24,0,18,19,25,18,19,19],
[27,34,33,32,0,25,31,33,22,26],
[28,31,39,31,25,0,33,28,24,37],
[24,22,26,25,19,17,0,29,23,23],
[29,23,28,32,17,22,21,0,22,25],
[29,23,27,31,28,26,27,28,0,32],
[24,24,28,31,24,13,27,25,18,0]])



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
result = np.append(np.array([10, 50, 63, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,22,25,23,28,28,25,28,23],
[24,0,23,30,27,28,31,23,25,24],
[28,27,0,30,28,31,23,29,30,30],
[25,20,20,0,22,24,25,23,24,22],
[27,23,22,28,0,27,27,26,28,24],
[22,22,19,26,23,0,25,24,24,22],
[22,19,27,25,23,25,0,26,25,26],
[25,27,21,27,24,26,24,0,30,22],
[22,25,20,26,22,26,25,20,0,22],
[27,26,20,28,26,28,24,28,28,0]])



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
result = np.append(np.array([10, 50, 64, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,26,26,27,27,15,26,27,25],
[21,0,15,19,21,16,18,20,22,20],
[24,35,0,25,30,32,25,34,30,26],
[24,31,25,0,27,25,23,22,23,32],
[23,29,20,23,0,26,23,26,22,22],
[23,34,18,25,24,0,18,16,22,26],
[35,32,25,27,27,32,0,26,29,30],
[24,30,16,28,24,34,24,0,24,29],
[23,28,20,27,28,28,21,26,0,31],
[25,30,24,18,28,24,20,21,19,0]])



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
result = np.append(np.array([10, 50, 65, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,24,31,35,20,32,30,33,27],
[27,0,27,23,34,16,21,18,22,21],
[26,23,0,31,32,21,27,32,25,19],
[19,27,19,0,28,20,27,27,29,24],
[15,16,18,22,0,13,26,22,19,25],
[30,34,29,30,37,0,33,23,33,25],
[18,29,23,23,24,17,0,29,22,20],
[20,32,18,23,28,27,21,0,28,14],
[17,28,25,21,31,17,28,22,0,30],
[23,29,31,26,25,25,30,36,20,0]])



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
result = np.append(np.array([10, 50, 66, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,17,19,26,23,24,22,20,22],
[27,0,28,18,36,17,27,30,26,21],
[33,22,0,21,30,24,29,23,27,18],
[31,32,29,0,38,25,34,31,31,25],
[24,14,20,12,0,16,26,13,18,15],
[27,33,26,25,34,0,31,33,32,27],
[26,23,21,16,24,19,0,16,23,21],
[28,20,27,19,37,17,34,0,21,16],
[30,24,23,19,32,18,27,29,0,20],
[28,29,32,25,35,23,29,34,30,0]])



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
result = np.append(np.array([10, 50, 67, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,38,25,33,27,31,23,27,31],
[22,0,32,29,32,34,22,27,26,29],
[12,18,0,21,22,21,19,14,17,21],
[25,21,29,0,25,25,23,21,16,20],
[17,18,28,25,0,22,27,17,20,21],
[23,16,29,25,28,0,20,23,22,19],
[19,28,31,27,23,30,0,28,23,23],
[27,23,36,29,33,27,22,0,17,22],
[23,24,33,34,30,28,27,33,0,24],
[19,21,29,30,29,31,27,28,26,0]])



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
result = np.append(np.array([10, 50, 68, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,31,27,37,23,31,31,24,27],
[19,0,22,20,34,20,27,30,22,16],
[19,28,0,21,27,26,22,21,26,20],
[23,30,29,0,33,30,31,33,33,26],
[13,16,23,17,0,18,26,23,15,20],
[27,30,24,20,32,0,32,26,29,23],
[19,23,28,19,24,18,0,23,26,15],
[19,20,29,17,27,24,27,0,17,18],
[26,28,24,17,35,21,24,33,0,26],
[23,34,30,24,30,27,35,32,24,0]])



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
result = np.append(np.array([10, 50, 69, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,29,27,20,20,28,29,35,30],
[22,0,34,24,19,26,24,24,26,33],
[21,16,0,23,20,15,16,16,18,17],
[23,26,27,0,16,28,27,26,29,22],
[30,31,30,34,0,22,42,30,34,33],
[30,24,35,22,28,0,32,32,26,39],
[22,26,34,23,8,18,0,21,27,22],
[21,26,34,24,20,18,29,0,30,27],
[15,24,32,21,16,24,23,20,0,21],
[20,17,33,28,17,11,28,23,29,0]])



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
result = np.append(np.array([10, 50, 70, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,21,22,25,21,23,27,30,23],
[26,0,20,24,29,20,26,30,25,21],
[29,30,0,23,25,28,27,29,29,21],
[28,26,27,0,23,20,22,28,26,25],
[25,21,25,27,0,17,22,29,27,21],
[29,30,22,30,33,0,26,31,35,30],
[27,24,23,28,28,24,0,30,27,25],
[23,20,21,22,21,19,20,0,28,26],
[20,25,21,24,23,15,23,22,0,25],
[27,29,29,25,29,20,25,24,25,0]])



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
result = np.append(np.array([10, 50, 71, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,50,25,50,50,50,25,25,25],
[25,0,25,25,25,25,50,25,25,25],
[0,25,0,25,25,50,50,25,25,25],
[25,25,25,0,25,25,25,25,50,0],
[0,25,25,25,0,25,25,25,25,0],
[0,25,0,25,25,0,25,25,25,0],
[0,0,0,25,25,25,0,25,25,0],
[25,25,25,25,25,25,25,0,25,0],
[25,25,25,0,25,25,25,25,0,0],
[25,25,25,50,50,50,50,50,50,0]])



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
result = np.append(np.array([10, 50, 72, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,22,20,14,19,25,24,18,25],
[31,0,21,25,22,25,30,34,26,31],
[28,29,0,30,22,24,28,30,25,28],
[30,25,20,0,23,19,30,29,22,28],
[36,28,28,27,0,18,24,31,24,32],
[31,25,26,31,32,0,31,27,26,33],
[25,20,22,20,26,19,0,26,24,29],
[26,16,20,21,19,23,24,0,17,24],
[32,24,25,28,26,24,26,33,0,33],
[25,19,22,22,18,17,21,26,17,0]])



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
result = np.append(np.array([10, 50, 73, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,22,29,21,33,29,23,30,30],
[18,0,23,22,20,33,24,20,31,26],
[28,27,0,29,22,34,24,26,29,32],
[21,28,21,0,21,34,25,23,29,32],
[29,30,28,29,0,38,33,23,33,33],
[17,17,16,16,12,0,18,16,19,25],
[21,26,26,25,17,32,0,21,30,31],
[27,30,24,27,27,34,29,0,31,31],
[20,19,21,21,17,31,20,19,0,23],
[20,24,18,18,17,25,19,19,27,0]])



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
result = np.append(np.array([10, 50, 74, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,37,23,28,30,25,27,29,35],
[14,0,22,14,14,14,12,22,18,18],
[13,28,0,16,16,16,14,16,19,18],
[27,36,34,0,22,27,26,18,26,41],
[22,36,34,28,0,28,26,29,25,38],
[20,36,34,23,22,0,25,26,23,27],
[25,38,36,24,24,25,0,24,29,35],
[23,28,34,32,21,24,26,0,29,31],
[21,32,31,24,25,27,21,21,0,25],
[15,32,32,9,12,23,15,19,25,0]])



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
result = np.append(np.array([10, 50, 75, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,23,23,24,25,22,23,21,19],
[25,0,23,25,26,28,27,27,26,18],
[27,27,0,25,27,23,24,24,22,25],
[27,25,25,0,30,29,26,22,23,19],
[26,24,23,20,0,23,28,26,26,20],
[25,22,27,21,27,0,26,25,24,16],
[28,23,26,24,22,24,0,26,24,21],
[27,23,26,28,24,25,24,0,27,17],
[29,24,28,27,24,26,26,23,0,18],
[31,32,25,31,30,34,29,33,32,0]])



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
result = np.append(np.array([10, 50, 76, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,28,27,9,26,17,32,21,30],
[30,0,25,31,26,24,28,40,26,31],
[22,25,0,20,16,15,14,29,17,21],
[23,19,30,0,18,23,19,32,15,25],
[41,24,34,32,0,32,17,36,33,30],
[24,26,35,27,18,0,11,27,17,23],
[33,22,36,31,33,39,0,41,30,30],
[18,10,21,18,14,23,9,0,18,25],
[29,24,33,35,17,33,20,32,0,30],
[20,19,29,25,20,27,20,25,20,0]])



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
result = np.append(np.array([10, 50, 77, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,24,15,27,25,31,27,24,28],
[27,0,34,26,28,21,33,31,27,30],
[26,16,0,21,27,21,27,26,25,24],
[35,24,29,0,27,25,35,31,30,32],
[23,22,23,23,0,20,28,29,24,27],
[25,29,29,25,30,0,37,29,31,30],
[19,17,23,15,22,13,0,23,22,18],
[23,19,24,19,21,21,27,0,22,26],
[26,23,25,20,26,19,28,28,0,28],
[22,20,26,18,23,20,32,24,22,0]])



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
result = np.append(np.array([10, 50, 78, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,17,18,31,16,20,36,20,25],
[34,0,22,21,27,27,27,35,25,34],
[33,28,0,25,29,29,31,34,30,29],
[32,29,25,0,25,29,33,43,29,39],
[19,23,21,25,0,23,22,32,14,28],
[34,23,21,21,27,0,22,38,27,35],
[30,23,19,17,28,28,0,26,19,30],
[14,15,16,7,18,12,24,0,15,13],
[30,25,20,21,36,23,31,35,0,30],
[25,16,21,11,22,15,20,37,20,0]])



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
result = np.append(np.array([10, 50, 79, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,24,25,26,27,31,29,31,22],
[25,0,27,26,25,29,36,35,29,30],
[26,23,0,19,20,21,27,26,21,21],
[25,24,31,0,23,31,32,30,36,26],
[24,25,30,27,0,28,33,28,30,27],
[23,21,29,19,22,0,24,26,28,15],
[19,14,23,18,17,26,0,25,22,16],
[21,15,24,20,22,24,25,0,27,18],
[19,21,29,14,20,22,28,23,0,18],
[28,20,29,24,23,35,34,32,32,0]])



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
result = np.append(np.array([10, 50, 80, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,22,35,21,24,23,23,29,18],
[21,0,15,22,18,11,21,17,9,16],
[28,35,0,25,16,20,22,14,30,21],
[15,28,25,0,33,28,29,22,23,22],
[29,32,34,17,0,19,26,23,29,27],
[26,39,30,22,31,0,31,25,26,25],
[27,29,28,21,24,19,0,21,28,25],
[27,33,36,28,27,25,29,0,28,26],
[21,41,20,27,21,24,22,22,0,17],
[32,34,29,28,23,25,25,24,33,0]])



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
result = np.append(np.array([10, 50, 81, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,22,25,19,26,23,29,25,24],
[30,0,25,27,33,31,26,32,31,29],
[28,25,0,29,25,28,25,30,31,28],
[25,23,21,0,22,26,28,29,29,22],
[31,17,25,28,0,27,28,29,23,23],
[24,19,22,24,23,0,26,29,24,19],
[27,24,25,22,22,24,0,32,29,22],
[21,18,20,21,21,21,18,0,21,20],
[25,19,19,21,27,26,21,29,0,19],
[26,21,22,28,27,31,28,30,31,0]])



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
result = np.append(np.array([10, 50, 82, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,28,23,25,23,26,24,23,25],
[23,0,30,24,23,29,28,24,24,27],
[22,20,0,22,21,22,23,27,22,26],
[27,26,28,0,25,27,24,30,23,29],
[25,27,29,25,0,24,26,28,25,25],
[27,21,28,23,26,0,28,31,24,31],
[24,22,27,26,24,22,0,31,21,27],
[26,26,23,20,22,19,19,0,27,25],
[27,26,28,27,25,26,29,23,0,25],
[25,23,24,21,25,19,23,25,25,0]])



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
result = np.append(np.array([10, 50, 83, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,25,18,20,19,19,21,23,20],
[31,0,28,27,25,28,26,26,28,22],
[25,22,0,20,24,26,24,23,22,19],
[32,23,30,0,25,29,24,28,31,23],
[30,25,26,25,0,21,24,21,23,21],
[31,22,24,21,29,0,27,25,25,19],
[31,24,26,26,26,23,0,27,27,26],
[29,24,27,22,29,25,23,0,26,18],
[27,22,28,19,27,25,23,24,0,19],
[30,28,31,27,29,31,24,32,31,0]])



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
result = np.append(np.array([10, 50, 84, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,23,21,18,16,19,20,27,29],
[26,0,26,28,22,21,23,26,30,32],
[27,24,0,26,25,21,25,28,27,29],
[29,22,24,0,21,20,20,29,27,34],
[32,28,25,29,0,23,23,28,28,35],
[34,29,29,30,27,0,25,29,32,34],
[31,27,25,30,27,25,0,29,31,34],
[30,24,22,21,22,21,21,0,23,29],
[23,20,23,23,22,18,19,27,0,28],
[21,18,21,16,15,16,16,21,22,0]])



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
result = np.append(np.array([10, 50, 85, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,20,33,26,34,17,29,24,24],
[24,0,23,27,19,32,16,29,19,29],
[30,27,0,34,30,32,29,23,20,36],
[17,23,16,0,28,19,10,29,24,25],
[24,31,20,22,0,25,17,24,22,26],
[16,18,18,31,25,0,18,25,17,25],
[33,34,21,40,33,32,0,26,27,30],
[21,21,27,21,26,25,24,0,15,32],
[26,31,30,26,28,33,23,35,0,35],
[26,21,14,25,24,25,20,18,15,0]])



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
result = np.append(np.array([10, 50, 86, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,25,34,24,39,32,31,30,32],
[14,0,18,25,21,27,20,27,25,26],
[25,32,0,25,26,33,30,26,28,25],
[16,25,25,0,18,38,20,28,25,22],
[26,29,24,32,0,35,33,30,26,28],
[11,23,17,12,15,0,15,17,20,16],
[18,30,20,30,17,35,0,27,24,22],
[19,23,24,22,20,33,23,0,20,28],
[20,25,22,25,24,30,26,30,0,21],
[18,24,25,28,22,34,28,22,29,0]])



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
result = np.append(np.array([10, 50, 87, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,28,25,23,26,31,20,24,32],
[23,0,28,21,22,26,28,21,25,30],
[22,22,0,29,23,27,29,20,22,31],
[25,29,21,0,26,27,29,24,26,31],
[27,28,27,24,0,26,29,25,24,30],
[24,24,23,23,24,0,29,21,24,27],
[19,22,21,21,21,21,0,18,22,25],
[30,29,30,26,25,29,32,0,26,31],
[26,25,28,24,26,26,28,24,0,26],
[18,20,19,19,20,23,25,19,24,0]])



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
result = np.append(np.array([10, 50, 88, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,25,31,20,24,32,19,27,26],
[27,0,23,27,29,26,24,24,26,24],
[25,27,0,32,23,26,28,29,29,25],
[19,23,18,0,14,25,22,21,17,27],
[30,21,27,36,0,23,27,22,25,23],
[26,24,24,25,27,0,26,20,32,32],
[18,26,22,28,23,24,0,19,27,27],
[31,26,21,29,28,30,31,0,25,21],
[23,24,21,33,25,18,23,25,0,24],
[24,26,25,23,27,18,23,29,26,0]])



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
result = np.append(np.array([10, 50, 89, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,27,33,31,30,25,30,29,24],
[20,0,26,28,27,30,25,29,23,21],
[23,24,0,31,28,29,23,24,22,24],
[17,22,19,0,25,28,26,23,21,25],
[19,23,22,25,0,28,26,29,24,22],
[20,20,21,22,22,0,24,26,25,21],
[25,25,27,24,24,26,0,27,25,25],
[20,21,26,27,21,24,23,0,21,17],
[21,27,28,29,26,25,25,29,0,23],
[26,29,26,25,28,29,25,33,27,0]])



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
result = np.append(np.array([10, 50, 90, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,28,33,36,27,31,23,32,32],
[11,0,21,21,28,16,21,18,24,27],
[22,29,0,20,31,19,21,18,31,24],
[17,29,30,0,31,22,32,29,32,28],
[14,22,19,19,0,15,19,10,22,27],
[23,34,31,28,35,0,26,30,36,34],
[19,29,29,18,31,24,0,22,28,29],
[27,32,32,21,40,20,28,0,30,30],
[18,26,19,18,28,14,22,20,0,24],
[18,23,26,22,23,16,21,20,26,0]])



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
result = np.append(np.array([10, 50, 91, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,29,33,21,25,31,22,24,21],
[22,0,26,20,22,20,25,13,21,17],
[21,24,0,21,17,22,29,18,29,22],
[17,30,29,0,21,21,32,26,26,28],
[29,28,33,29,0,25,27,22,28,22],
[25,30,28,29,25,0,30,21,27,22],
[19,25,21,18,23,20,0,22,18,17],
[28,37,32,24,28,29,28,0,30,29],
[26,29,21,24,22,23,32,20,0,25],
[29,33,28,22,28,28,33,21,25,0]])



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
result = np.append(np.array([10, 50, 92, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,20,23,14,21,28,24,15,12],
[22,0,31,23,22,16,36,23,25,17],
[30,19,0,31,35,24,33,29,28,21],
[27,27,19,0,17,18,29,15,16,17],
[36,28,15,33,0,22,38,26,19,20],
[29,34,26,32,28,0,44,28,26,16],
[22,14,17,21,12,6,0,11,22,14],
[26,27,21,35,24,22,39,0,23,29],
[35,25,22,34,31,24,28,27,0,19],
[38,33,29,33,30,34,36,21,31,0]])



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
result = np.append(np.array([10, 50, 93, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,18,23,27,28,15,19,18,28],
[32,0,27,25,30,20,13,28,27,27],
[32,23,0,24,30,25,26,31,19,27],
[27,25,26,0,28,26,19,29,23,33],
[23,20,20,22,0,21,18,22,16,20],
[22,30,25,24,29,0,21,27,26,33],
[35,37,24,31,32,29,0,30,29,28],
[31,22,19,21,28,23,20,0,21,23],
[32,23,31,27,34,24,21,29,0,30],
[22,23,23,17,30,17,22,27,20,0]])



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
result = np.append(np.array([10, 50, 94, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,25,26,25,24,18,14,22,20],
[28,0,22,28,22,18,13,22,23,18],
[25,28,0,25,32,23,19,23,23,17],
[24,22,25,0,23,20,25,18,29,25],
[25,28,18,27,0,22,16,18,21,20],
[26,32,27,30,28,0,21,25,27,28],
[32,37,31,25,34,29,0,26,24,24],
[36,28,27,32,32,25,24,0,20,25],
[28,27,27,21,29,23,26,30,0,18],
[30,32,33,25,30,22,26,25,32,0]])



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
result = np.append(np.array([10, 50, 95, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,33,26,25,26,25,25,41,49],
[25,0,33,50,21,21,49,34,36,37],
[17,17,0,42,17,13,42,26,29,29],
[24,0,8,0,8,1,8,21,28,36],
[25,29,33,42,0,13,41,34,28,49],
[24,29,37,49,37,0,49,33,36,49],
[25,1,8,42,9,1,0,34,28,37],
[25,16,24,29,16,17,16,0,28,36],
[9,14,21,22,22,14,22,22,0,38],
[1,13,21,14,1,1,13,14,12,0]])



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
result = np.append(np.array([10, 50, 96, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,25,16,26,22,30,16,20,25],
[25,0,30,17,26,24,32,31,25,36],
[25,20,0,22,18,24,27,11,24,23],
[34,33,28,0,29,23,32,26,30,33],
[24,24,32,21,0,26,28,25,25,26],
[28,26,26,27,24,0,32,27,27,33],
[20,18,23,18,22,18,0,18,25,24],
[34,19,39,24,25,23,32,0,30,25],
[30,25,26,20,25,23,25,20,0,28],
[25,14,27,17,24,17,26,25,22,0]])



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
result = np.append(np.array([10, 50, 97, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,19,41,16,23,24,32,36,30],
[31,0,28,50,21,27,24,29,29,30],
[31,22,0,50,33,32,21,34,33,31],
[9,0,0,0,4,18,17,16,20,18],
[34,29,17,46,0,18,20,28,20,26],
[27,23,18,32,32,0,13,34,13,27],
[26,26,29,33,30,37,0,25,33,22],
[18,21,16,34,22,16,25,0,25,34],
[14,21,17,30,30,37,17,25,0,28],
[20,20,19,32,24,23,28,16,22,0]])



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
result = np.append(np.array([10, 50, 98, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,0,32,15,33,9,6,37,21],
[32,0,23,32,36,32,20,25,48,32],
[50,27,0,38,15,48,11,6,37,21],
[18,18,12,0,18,28,9,18,37,12],
[35,14,35,32,0,44,20,13,48,32],
[17,18,2,22,6,0,11,6,37,0],
[41,30,39,41,30,39,0,18,39,23],
[44,25,44,32,37,44,32,0,48,44],
[13,2,13,13,2,13,11,2,0,11],
[29,18,29,38,18,50,27,6,39,0]])



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
result = np.append(np.array([10, 50, 99, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,14,21,23,26,18,15,25,26],
[28,0,17,26,26,18,21,20,27,27],
[36,33,0,29,21,30,30,26,35,37],
[29,24,21,0,21,19,19,24,30,24],
[27,24,29,29,0,23,26,23,32,31],
[24,32,20,31,27,0,22,16,29,26],
[32,29,20,31,24,28,0,23,33,24],
[35,30,24,26,27,34,27,0,33,35],
[25,23,15,20,18,21,17,17,0,27],
[24,23,13,26,19,24,26,15,23,0]])



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
result = np.append(np.array([10, 50, 100, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,23,24,30,24,29,20,17,23],
[25,0,25,29,23,28,31,22,22,23],
[27,25,0,31,25,27,30,27,28,28],
[26,21,19,0,25,27,26,22,19,30],
[20,27,25,25,0,26,26,24,15,26],
[26,22,23,23,24,0,29,16,21,23],
[21,19,20,24,24,21,0,21,13,22],
[30,28,23,28,26,34,29,0,26,23],
[33,28,22,31,35,29,37,24,0,33],
[27,27,22,20,24,27,28,27,17,0]])



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
result = np.append(np.array([10, 50, 101, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,31,37,32,25,33,36,35,31],
[16,0,30,19,16,11,27,32,33,23],
[19,20,0,31,29,18,27,38,36,34],
[13,31,19,0,22,19,23,35,36,25],
[18,34,21,28,0,25,23,37,34,31],
[25,39,32,31,25,0,31,37,33,32],
[17,23,23,27,27,19,0,33,24,28],
[14,18,12,15,13,13,17,0,26,17],
[15,17,14,14,16,17,26,24,0,17],
[19,27,16,25,19,18,22,33,33,0]])



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
result = np.append(np.array([10, 50, 102, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,24,40,29,29,25,24,28,32],
[21,0,22,28,23,27,27,20,29,24],
[26,28,0,30,25,32,26,18,32,23],
[10,22,20,0,26,23,24,17,26,18],
[21,27,25,24,0,26,27,11,24,24],
[21,23,18,27,24,0,19,21,22,20],
[25,23,24,26,23,31,0,19,28,24],
[26,30,32,33,39,29,31,0,34,22],
[22,21,18,24,26,28,22,16,0,26],
[18,26,27,32,26,30,26,28,24,0]])



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
result = np.append(np.array([10, 50, 103, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,29,40,34,29,19,28,30,24],
[21,0,25,31,20,29,25,20,31,34],
[21,25,0,35,26,25,19,15,31,19],
[10,19,15,0,15,28,19,29,31,16],
[16,30,24,35,0,39,24,29,35,33],
[21,21,25,22,11,0,15,20,31,20],
[31,25,31,31,26,35,0,34,30,30],
[22,30,35,21,21,30,16,0,32,25],
[20,19,19,19,15,19,20,18,0,20],
[26,16,31,34,17,30,20,25,30,0]])



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
result = np.append(np.array([10, 50, 104, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,22,26,22,22,11,12,22,17],
[26,0,22,19,14,23,15,15,19,22],
[28,28,0,23,21,22,18,21,19,17],
[24,31,27,0,23,24,20,19,21,27],
[28,36,29,27,0,34,24,28,26,30],
[28,27,28,26,16,0,22,10,21,23],
[39,35,32,30,26,28,0,18,25,28],
[38,35,29,31,22,40,32,0,29,29],
[28,31,31,29,24,29,25,21,0,25],
[33,28,33,23,20,27,22,21,25,0]])



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
result = np.append(np.array([10, 50, 105, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,21,31,17,18,15,17,31,25],
[39,0,37,35,24,33,25,29,41,27],
[29,13,0,34,21,19,17,24,29,30],
[19,15,16,0,14,18,20,16,20,24],
[33,26,29,36,0,32,24,27,34,35],
[32,17,31,32,18,0,24,21,27,29],
[35,25,33,30,26,26,0,29,34,30],
[33,21,26,34,23,29,21,0,29,30],
[19,9,21,30,16,23,16,21,0,23],
[25,23,20,26,15,21,20,20,27,0]])



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
result = np.append(np.array([10, 50, 106, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,23,28,26,29,25,17,26,28],
[24,0,28,32,27,30,26,27,26,27],
[27,22,0,34,30,34,30,28,35,30],
[22,18,16,0,31,30,25,18,23,25],
[24,23,20,19,0,29,20,23,28,28],
[21,20,16,20,21,0,26,17,21,23],
[25,24,20,25,30,24,0,15,25,18],
[33,23,22,32,27,33,35,0,26,27],
[24,24,15,27,22,29,25,24,0,28],
[22,23,20,25,22,27,32,23,22,0]])



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
result = np.append(np.array([10, 50, 107, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,23,21,26,20,23,25,20,24],
[17,0,15,15,16,16,20,11,20,22],
[27,35,0,32,25,22,26,23,25,25],
[29,35,18,0,26,25,25,28,29,25],
[24,34,25,24,0,25,26,26,24,29],
[30,34,28,25,25,0,21,25,27,29],
[27,30,24,25,24,29,0,19,28,20],
[25,39,27,22,24,25,31,0,29,31],
[30,30,25,21,26,23,22,21,0,24],
[26,28,25,25,21,21,30,19,26,0]])



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
result = np.append(np.array([10, 50, 108, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,25,26,25,31,25,25,23,29],
[30,0,26,28,29,33,26,28,28,25],
[25,24,0,24,32,29,26,23,28,21],
[24,22,26,0,30,32,29,25,26,30],
[25,21,18,20,0,26,25,21,25,25],
[19,17,21,18,24,0,25,21,22,22],
[25,24,24,21,25,25,0,23,25,22],
[25,22,27,25,29,29,27,0,29,24],
[27,22,22,24,25,28,25,21,0,30],
[21,25,29,20,25,28,28,26,20,0]])



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
result = np.append(np.array([10, 50, 109, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,15,21,20,17,17,26,23,18],
[23,0,23,18,21,18,19,21,25,22],
[35,27,0,27,27,24,22,25,31,26],
[29,32,23,0,27,24,29,30,33,26],
[30,29,23,23,0,21,21,23,27,20],
[33,32,26,26,29,0,21,27,27,27],
[33,31,28,21,29,29,0,27,28,26],
[24,29,25,20,27,23,23,0,29,24],
[27,25,19,17,23,23,22,21,0,18],
[32,28,24,24,30,23,24,26,32,0]])



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
result = np.append(np.array([10, 50, 110, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,18,20,16,24,25,21,16,15],
[25,0,28,16,21,22,31,17,17,18],
[32,22,0,28,21,26,30,25,22,22],
[30,34,22,0,26,31,33,32,26,18],
[34,29,29,24,0,24,30,22,22,18],
[26,28,24,19,26,0,25,24,19,13],
[25,19,20,17,20,25,0,22,21,17],
[29,33,25,18,28,26,28,0,19,23],
[34,33,28,24,28,31,29,31,0,25],
[35,32,28,32,32,37,33,27,25,0]])



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
result = np.append(np.array([10, 50, 111, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,25,31,25,22,30,28,26,28],
[30,0,23,29,28,20,29,27,29,15],
[25,27,0,33,29,26,29,23,31,26],
[19,21,17,0,17,11,22,21,20,15],
[25,22,21,33,0,14,30,21,24,28],
[28,30,24,39,36,0,36,22,30,22],
[20,21,21,28,20,14,0,23,13,24],
[22,23,27,29,29,28,27,0,29,26],
[24,21,19,30,26,20,37,21,0,25],
[22,35,24,35,22,28,26,24,25,0]])



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
result = np.append(np.array([10, 50, 112, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,25,24,23,31,25,27,25,29],
[23,0,27,30,29,26,22,28,28,29],
[25,23,0,22,28,28,24,28,24,30],
[26,20,28,0,29,27,21,27,24,32],
[27,21,22,21,0,30,24,31,28,31],
[19,24,22,23,20,0,21,27,17,24],
[25,28,26,29,26,29,0,30,26,27],
[23,22,22,23,19,23,20,0,20,28],
[25,22,26,26,22,33,24,30,0,27],
[21,21,20,18,19,26,23,22,23,0]])



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
result = np.append(np.array([10, 50, 113, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,31,27,22,32,21,23,39,28],
[23,0,24,18,10,26,22,17,29,17],
[19,26,0,27,23,32,22,22,31,27],
[23,32,23,0,20,31,26,26,37,25],
[28,40,27,30,0,35,29,25,34,34],
[18,24,18,19,15,0,18,23,30,29],
[29,28,28,24,21,32,0,27,37,33],
[27,33,28,24,25,27,23,0,34,32],
[11,21,19,13,16,20,13,16,0,27],
[22,33,23,25,16,21,17,18,23,0]])



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
result = np.append(np.array([10, 50, 114, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,24,30,21,24,25,28,27,26],
[27,0,28,31,19,27,23,32,29,28],
[26,22,0,28,20,26,21,19,31,23],
[20,19,22,0,24,22,22,24,27,27],
[29,31,30,26,0,32,25,29,32,28],
[26,23,24,28,18,0,21,26,23,23],
[25,27,29,28,25,29,0,31,32,32],
[22,18,31,26,21,24,19,0,26,25],
[23,21,19,23,18,27,18,24,0,23],
[24,22,27,23,22,27,18,25,27,0]])



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
result = np.append(np.array([10, 50, 115, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,25,14,24,21,21,18,22,25],
[31,0,32,24,35,24,30,28,29,25],
[25,18,0,12,31,18,27,22,24,18],
[36,26,38,0,23,28,27,32,23,27],
[26,15,19,27,0,17,19,23,25,17],
[29,26,32,22,33,0,28,25,33,28],
[29,20,23,23,31,22,0,27,28,19],
[32,22,28,18,27,25,23,0,27,23],
[28,21,26,27,25,17,22,23,0,27],
[25,25,32,23,33,22,31,27,23,0]])



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
result = np.append(np.array([10, 50, 116, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,22,29,26,24,29,26,26,30],
[27,0,27,28,20,30,26,27,28,25],
[28,23,0,28,23,29,27,25,26,28],
[21,22,22,0,23,21,21,20,22,23],
[24,30,27,27,0,29,27,27,23,29],
[26,20,21,29,21,0,25,20,23,20],
[21,24,23,29,23,25,0,23,27,26],
[24,23,25,30,23,30,27,0,30,24],
[24,22,24,28,27,27,23,20,0,28],
[20,25,22,27,21,30,24,26,22,0]])



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
result = np.append(np.array([10, 50, 117, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,14,14,22,26,15,15,19,8],
[33,0,32,27,43,40,29,26,31,23],
[36,18,0,17,28,29,12,28,26,22],
[36,23,33,0,34,29,30,30,32,17],
[28,7,22,16,0,26,8,22,20,16],
[24,10,21,21,24,0,17,22,21,19],
[35,21,38,20,42,33,0,40,36,27],
[35,24,22,20,28,28,10,0,23,18],
[31,19,24,18,30,29,14,27,0,9],
[42,27,28,33,34,31,23,32,41,0]])



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
result = np.append(np.array([10, 50, 118, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,26,23,28,24,23,22,26,26],
[19,0,26,22,22,22,19,25,21,16],
[24,24,0,25,27,25,23,27,28,22],
[27,28,25,0,22,21,26,19,20,22],
[22,28,23,28,0,26,28,21,26,19],
[26,28,25,29,24,0,31,23,30,28],
[27,31,27,24,22,19,0,23,22,20],
[28,25,23,31,29,27,27,0,31,20],
[24,29,22,30,24,20,28,19,0,24],
[24,34,28,28,31,22,30,30,26,0]])



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
result = np.append(np.array([10, 50, 119, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,22,22,19,16,25,21,26,29],
[27,0,17,19,24,16,23,18,20,25],
[28,33,0,24,25,36,36,27,27,37],
[28,31,26,0,26,25,28,32,37,34],
[31,26,25,24,0,33,29,23,31,38],
[34,34,14,25,17,0,28,21,21,35],
[25,27,14,22,21,22,0,24,32,30],
[29,32,23,18,27,29,26,0,26,32],
[24,30,23,13,19,29,18,24,0,35],
[21,25,13,16,12,15,20,18,15,0]])



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
result = np.append(np.array([10, 50, 120, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,21,27,26,24,27,29,19,26],
[32,0,20,27,26,31,33,30,26,32],
[29,30,0,33,27,24,29,33,24,30],
[23,23,17,0,24,25,25,25,25,24],
[24,24,23,26,0,21,26,34,23,28],
[26,19,26,25,29,0,29,31,23,31],
[23,17,21,25,24,21,0,23,17,22],
[21,20,17,25,16,19,27,0,22,23],
[31,24,26,25,27,27,33,28,0,25],
[24,18,20,26,22,19,28,27,25,0]])



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
result = np.append(np.array([10, 50, 121, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,16,28,29,23,22,18,24,28],
[22,0,15,21,33,15,15,21,26,24],
[34,35,0,32,40,28,23,35,39,19],
[22,29,18,0,28,19,17,21,24,29],
[21,17,10,22,0,14,15,13,17,21],
[27,35,22,31,36,0,26,26,35,27],
[28,35,27,33,35,24,0,27,33,24],
[32,29,15,29,37,24,23,0,29,26],
[26,24,11,26,33,15,17,21,0,22],
[22,26,31,21,29,23,26,24,28,0]])



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
result = np.append(np.array([10, 50, 122, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,22,27,29,31,25,26,29,23],
[26,0,25,22,27,29,21,29,27,25],
[28,25,0,29,29,33,23,29,23,29],
[23,28,21,0,27,26,25,23,23,21],
[21,23,21,23,0,28,27,27,24,28],
[19,21,17,24,22,0,22,23,20,25],
[25,29,27,25,23,28,0,24,26,24],
[24,21,21,27,23,27,26,0,25,24],
[21,23,27,27,26,30,24,25,0,27],
[27,25,21,29,22,25,26,26,23,0]])



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
result = np.append(np.array([10, 50, 123, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,23,24,25,26,22,23,23,19],
[32,0,34,30,29,25,25,23,30,26],
[27,16,0,26,27,24,19,22,22,24],
[26,20,24,0,30,21,22,16,30,16],
[25,21,23,20,0,21,21,21,23,21],
[24,25,26,29,29,0,27,26,33,23],
[28,25,31,28,29,23,0,24,24,23],
[27,27,28,34,29,24,26,0,35,25],
[27,20,28,20,27,17,26,15,0,17],
[31,24,26,34,29,27,27,25,33,0]])



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
result = np.append(np.array([10, 50, 124, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,24,23,28,31,27,30,30,27],
[20,0,21,26,23,29,18,29,27,22],
[26,29,0,25,28,36,25,30,34,27],
[27,24,25,0,24,28,20,30,30,25],
[22,27,22,26,0,27,24,30,28,27],
[19,21,14,22,23,0,16,26,26,19],
[23,32,25,30,26,34,0,27,31,29],
[20,21,20,20,20,24,23,0,30,19],
[20,23,16,20,22,24,19,20,0,20],
[23,28,23,25,23,31,21,31,30,0]])



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
result = np.append(np.array([10, 50, 125, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,16,31,32,29,15,25,16,33],
[28,0,21,25,40,25,14,27,19,24],
[34,29,0,31,37,27,21,39,22,36],
[19,25,19,0,31,26,10,22,14,23],
[18,10,13,19,0,22,11,16,17,18],
[21,25,23,24,28,0,25,29,22,28],
[35,36,29,40,39,25,0,36,30,36],
[25,23,11,28,34,21,14,0,17,28],
[34,31,28,36,33,28,20,33,0,35],
[17,26,14,27,32,22,14,22,15,0]])



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
result = np.append(np.array([10, 50, 126, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,25,34,33,27,30,22,15,29],
[30,0,31,37,35,33,32,20,17,24],
[25,19,0,29,35,35,37,35,16,26],
[16,13,21,0,23,26,18,14,9,21],
[17,15,15,27,0,27,24,20,16,19],
[23,17,15,24,23,0,31,23,25,22],
[20,18,13,32,26,19,0,23,8,18],
[28,30,15,36,30,27,27,0,25,24],
[35,33,34,41,34,25,42,25,0,27],
[21,26,24,29,31,28,32,26,23,0]])



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
result = np.append(np.array([10, 50, 127, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,25,27,23,26,31,26,31,22],
[24,0,30,27,19,26,32,20,28,21],
[25,20,0,24,24,24,25,23,27,21],
[23,23,26,0,18,23,29,26,29,22],
[27,31,26,32,0,27,31,24,31,24],
[24,24,26,27,23,0,24,26,27,26],
[19,18,25,21,19,26,0,24,20,20],
[24,30,27,24,26,24,26,0,27,20],
[19,22,23,21,19,23,30,23,0,17],
[28,29,29,28,26,24,30,30,33,0]])



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
result = np.append(np.array([10, 50, 128, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,25,26,26,24,22,28,25,19],
[25,0,17,16,21,22,26,23,24,16],
[25,33,0,24,35,28,29,31,26,29],
[24,34,26,0,27,23,23,30,21,24],
[24,29,15,23,0,22,13,29,18,20],
[26,28,22,27,28,0,21,32,21,19],
[28,24,21,27,37,29,0,31,26,26],
[22,27,19,20,21,18,19,0,19,16],
[25,26,24,29,32,29,24,31,0,22],
[31,34,21,26,30,31,24,34,28,0]])



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
result = np.append(np.array([10, 50, 129, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,23,27,20,21,21,17,23,25],
[28,0,23,32,30,22,23,18,22,23],
[27,27,0,26,20,21,23,17,18,25],
[23,18,24,0,17,14,17,20,20,18],
[30,20,30,33,0,18,20,17,21,27],
[29,28,29,36,32,0,27,24,25,31],
[29,27,27,33,30,23,0,28,25,31],
[33,32,33,30,33,26,22,0,26,33],
[27,28,32,30,29,25,25,24,0,26],
[25,27,25,32,23,19,19,17,24,0]])



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
result = np.append(np.array([10, 50, 130, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,19,24,22,26,28,26,27,21],
[27,0,28,25,21,35,27,31,25,28],
[31,22,0,20,26,28,28,21,22,22],
[26,25,30,0,20,27,35,31,31,25],
[28,29,24,30,0,33,34,28,34,27],
[24,15,22,23,17,0,26,16,24,22],
[22,23,22,15,16,24,0,23,23,19],
[24,19,29,19,22,34,27,0,24,21],
[23,25,28,19,16,26,27,26,0,20],
[29,22,28,25,23,28,31,29,30,0]])



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
result = np.append(np.array([10, 50, 131, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,31,31,33,25,26,24,32,32],
[28,0,33,31,31,30,25,26,24,32],
[19,17,0,25,28,23,20,16,24,30],
[19,19,25,0,28,23,23,23,22,25],
[17,19,22,22,0,21,26,17,27,21],
[25,20,27,27,29,0,20,26,28,28],
[24,25,30,27,24,30,0,26,26,28],
[26,24,34,27,33,24,24,0,27,32],
[18,26,26,28,23,22,24,23,0,28],
[18,18,20,25,29,22,22,18,22,0]])



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
result = np.append(np.array([10, 50, 132, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,22,24,27,21,23,29,18,32],
[23,0,24,24,28,19,23,23,21,26],
[28,26,0,24,30,23,26,27,22,27],
[26,26,26,0,27,25,22,27,19,30],
[23,22,20,23,0,23,27,29,17,23],
[29,31,27,25,27,0,26,31,26,28],
[27,27,24,28,23,24,0,28,22,29],
[21,27,23,23,21,19,22,0,19,23],
[32,29,28,31,33,24,28,31,0,34],
[18,24,23,20,27,22,21,27,16,0]])



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
result = np.append(np.array([10, 50, 133, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,20,20,20,24,15,19,17,32],
[28,0,14,23,25,20,22,19,29,24],
[30,36,0,31,34,29,23,29,29,41],
[30,27,19,0,27,24,21,26,25,31],
[30,25,16,23,0,19,18,18,28,21],
[26,30,21,26,31,0,23,26,25,29],
[35,28,27,29,32,27,0,21,29,32],
[31,31,21,24,32,24,29,0,26,35],
[33,21,21,25,22,25,21,24,0,31],
[18,26,9,19,29,21,18,15,19,0]])



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
result = np.append(np.array([10, 50, 134, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,16,29,21,23,22,22,24,13],
[22,0,12,26,22,19,24,22,22,18],
[34,38,0,36,32,24,32,31,34,23],
[21,24,14,0,24,21,22,23,26,16],
[29,28,18,26,0,27,26,24,29,26],
[27,31,26,29,23,0,27,27,27,21],
[28,26,18,28,24,23,0,21,22,19],
[28,28,19,27,26,23,29,0,31,23],
[26,28,16,24,21,23,28,19,0,23],
[37,32,27,34,24,29,31,27,27,0]])



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
result = np.append(np.array([10, 50, 135, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,26,36,21,23,36,20,26,32],
[26,0,17,28,25,16,25,16,25,17],
[24,33,0,33,29,23,37,28,34,31],
[14,22,17,0,15,8,25,20,18,19],
[29,25,21,35,0,20,40,26,31,29],
[27,34,27,42,30,0,38,22,29,33],
[14,25,13,25,10,12,0,7,17,21],
[30,34,22,30,24,28,43,0,31,29],
[24,25,16,32,19,21,33,19,0,29],
[18,33,19,31,21,17,29,21,21,0]])



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
result = np.append(np.array([10, 50, 136, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,14,23,16,22,24,20,12,19],
[27,0,23,21,19,21,30,25,18,29],
[36,27,0,27,29,31,34,27,23,32],
[27,29,23,0,23,21,28,24,21,30],
[34,31,21,27,0,33,35,33,32,33],
[28,29,19,29,17,0,29,24,18,22],
[26,20,16,22,15,21,0,20,15,27],
[30,25,23,26,17,26,30,0,24,19],
[38,32,27,29,18,32,35,26,0,25],
[31,21,18,20,17,28,23,31,25,0]])



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
result = np.append(np.array([10, 50, 137, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,17,18,19,28,15,12,18,20],
[41,0,27,22,33,22,31,29,21,30],
[33,23,0,12,14,20,14,17,22,23],
[32,28,38,0,26,31,29,17,24,31],
[31,17,36,24,0,24,22,27,22,21],
[22,28,30,19,26,0,21,18,13,31],
[35,19,36,21,28,29,0,22,20,17],
[38,21,33,33,23,32,28,0,27,34],
[32,29,28,26,28,37,30,23,0,33],
[30,20,27,19,29,19,33,16,17,0]])



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
result = np.append(np.array([10, 50, 138, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,20,31,32,32,31,19,24,34],
[21,0,19,21,24,19,22,19,20,24],
[30,31,0,25,34,29,32,23,23,31],
[19,29,25,0,26,28,28,22,17,29],
[18,26,16,24,0,24,24,13,17,31],
[18,31,21,22,26,0,27,17,19,25],
[19,28,18,22,26,23,0,17,13,26],
[31,31,27,28,37,33,33,0,25,33],
[26,30,27,33,33,31,37,25,0,24],
[16,26,19,21,19,25,24,17,26,0]])



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
result = np.append(np.array([10, 50, 139, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,19,20,21,21,21,24,20,18],
[30,0,21,22,27,31,29,25,21,20],
[31,29,0,25,28,28,26,32,26,24],
[30,28,25,0,23,32,23,29,21,24],
[29,23,22,27,0,28,22,34,30,23],
[29,19,22,18,22,0,18,21,21,23],
[29,21,24,27,28,32,0,26,26,25],
[26,25,18,21,16,29,24,0,21,15],
[30,29,24,29,20,29,24,29,0,21],
[32,30,26,26,27,27,25,35,29,0]])



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
result = np.append(np.array([10, 50, 140, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,19,23,23,21,22,19,14,21],
[27,0,20,21,28,22,24,20,16,19],
[31,30,0,28,32,25,28,25,19,25],
[27,29,22,0,32,26,26,20,24,26],
[27,22,18,18,0,20,18,19,20,22],
[29,28,25,24,30,0,25,23,23,18],
[28,26,22,24,32,25,0,25,21,26],
[31,30,25,30,31,27,25,0,25,29],
[36,34,31,26,30,27,29,25,0,29],
[29,31,25,24,28,32,24,21,21,0]])



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
result = np.append(np.array([10, 50, 141, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,35,35,35,28,33,39,30,31],
[28,0,32,33,23,36,30,36,24,34],
[15,18,0,20,29,29,25,27,22,22],
[15,17,30,0,24,35,25,35,19,29],
[15,27,21,26,0,30,21,32,17,21],
[22,14,21,15,20,0,15,26,13,25],
[17,20,25,25,29,35,0,32,19,30],
[11,14,23,15,18,24,18,0,12,17],
[20,26,28,31,33,37,31,38,0,29],
[19,16,28,21,29,25,20,33,21,0]])



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
result = np.append(np.array([10, 50, 142, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,28,21,22,20,24,22,26,25],
[29,0,21,22,17,20,23,19,24,20],
[22,29,0,19,17,21,28,23,26,26],
[29,28,31,0,24,23,25,28,29,27],
[28,33,33,26,0,26,27,21,27,30],
[30,30,29,27,24,0,28,23,32,25],
[26,27,22,25,23,22,0,21,25,21],
[28,31,27,22,29,27,29,0,27,27],
[24,26,24,21,23,18,25,23,0,22],
[25,30,24,23,20,25,29,23,28,0]])



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
result = np.append(np.array([10, 50, 143, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,25,22,23,26,19,29,20,30],
[21,0,18,23,19,19,20,22,21,22],
[25,32,0,26,24,28,21,31,23,29],
[28,27,24,0,28,23,23,23,19,29],
[27,31,26,22,0,29,27,29,28,34],
[24,31,22,27,21,0,26,36,23,33],
[31,30,29,27,23,24,0,31,23,29],
[21,28,19,27,21,14,19,0,19,23],
[30,29,27,31,22,27,27,31,0,34],
[20,28,21,21,16,17,21,27,16,0]])



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
result = np.append(np.array([10, 50, 144, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,33,26,31,24,24,26,22,25],
[30,0,33,23,26,25,24,28,29,29],
[17,17,0,21,20,20,21,19,23,25],
[24,27,29,0,25,28,28,25,30,31],
[19,24,30,25,0,22,25,20,30,24],
[26,25,30,22,28,0,25,27,30,27],
[26,26,29,22,25,25,0,20,28,26],
[24,22,31,25,30,23,30,0,30,24],
[28,21,27,20,20,20,22,20,0,26],
[25,21,25,19,26,23,24,26,24,0]])



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
result = np.append(np.array([10, 50, 145, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,28,26,22,16,19,20,21,22],
[32,0,28,30,23,25,21,24,25,25],
[22,22,0,26,25,20,19,21,21,23],
[24,20,24,0,27,17,23,21,21,27],
[28,27,25,23,0,23,21,24,26,26],
[34,25,30,33,27,0,27,29,26,28],
[31,29,31,27,29,23,0,22,23,27],
[30,26,29,29,26,21,28,0,29,29],
[29,25,29,29,24,24,27,21,0,25],
[28,25,27,23,24,22,23,21,25,0]])



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
result = np.append(np.array([10, 50, 146, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,23,24,20,23,28,27,28,25],
[28,0,29,27,20,26,30,31,28,29],
[27,21,0,26,21,24,24,29,33,29],
[26,23,24,0,27,24,29,29,30,23],
[30,30,29,23,0,27,29,29,33,31],
[27,24,26,26,23,0,29,31,30,28],
[22,20,26,21,21,21,0,25,25,19],
[23,19,21,21,21,19,25,0,22,21],
[22,22,17,20,17,20,25,28,0,21],
[25,21,21,27,19,22,31,29,29,0]])



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
result = np.append(np.array([10, 50, 147, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,21,28,28,23,28,27,25,31],
[28,0,21,25,22,24,24,29,25,30],
[29,29,0,28,25,22,24,28,26,29],
[22,25,22,0,19,20,19,23,19,25],
[22,28,25,31,0,25,30,29,31,26],
[27,26,28,30,25,0,27,27,32,28],
[22,26,26,31,20,23,0,28,28,28],
[23,21,22,27,21,23,22,0,22,25],
[25,25,24,31,19,18,22,28,0,28],
[19,20,21,25,24,22,22,25,22,0]])



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
result = np.append(np.array([10, 50, 148, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,20,24,22,16,18,18,27,19],
[24,0,24,21,21,17,8,11,15,16],
[30,26,0,25,22,23,27,24,34,31],
[26,29,25,0,24,20,15,21,23,26],
[28,29,28,26,0,26,25,18,26,22],
[34,33,27,30,24,0,25,28,26,29],
[32,42,23,35,25,25,0,27,27,24],
[32,39,26,29,32,22,23,0,24,28],
[23,35,16,27,24,24,23,26,0,23],
[31,34,19,24,28,21,26,22,27,0]])



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
result = np.append(np.array([10, 50, 149, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,28,30,30,28,29,31,19,23],
[17,0,21,29,25,19,21,24,17,21],
[22,29,0,26,27,24,22,30,28,26],
[20,21,24,0,30,27,18,28,17,24],
[20,25,23,20,0,26,22,21,21,25],
[22,31,26,23,24,0,20,24,16,25],
[21,29,28,32,28,30,0,23,23,28],
[19,26,20,22,29,26,27,0,19,29],
[31,33,22,33,29,34,27,31,0,32],
[27,29,24,26,25,25,22,21,18,0]])



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
result = np.append(np.array([10, 50, 150, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,13,24,32,19,12,17,18,22],
[28,0,16,15,20,27,15,23,26,20],
[37,34,0,25,32,32,27,29,29,27],
[26,35,25,0,23,24,17,26,19,27],
[18,30,18,27,0,21,17,18,20,22],
[31,23,18,26,29,0,21,24,16,27],
[38,35,23,33,33,29,0,36,31,34],
[33,27,21,24,32,26,14,0,20,29],
[32,24,21,31,30,34,19,30,0,26],
[28,30,23,23,28,23,16,21,24,0]])



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
result = np.append(np.array([10, 50, 151, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,26,25,23,25,31,15,21,15],
[33,0,33,27,24,24,35,25,26,23],
[24,17,0,23,24,25,34,24,26,20],
[25,23,27,0,19,13,31,17,26,24],
[27,26,26,31,0,23,36,23,31,29],
[25,26,25,37,27,0,35,25,27,23],
[19,15,16,19,14,15,0,18,18,13],
[35,25,26,33,27,25,32,0,26,30],
[29,24,24,24,19,23,32,24,0,24],
[35,27,30,26,21,27,37,20,26,0]])



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
result = np.append(np.array([10, 50, 152, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,25,22,18,19,20,25,28,19],
[28,0,28,21,26,22,19,28,27,24],
[25,22,0,21,24,25,22,22,24,25],
[28,29,29,0,32,24,25,30,34,27],
[32,24,26,18,0,23,19,22,29,25],
[31,28,25,26,27,0,25,21,29,27],
[30,31,28,25,31,25,0,28,29,23],
[25,22,28,20,28,29,22,0,27,22],
[22,23,26,16,21,21,21,23,0,23],
[31,26,25,23,25,23,27,28,27,0]])



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
result = np.append(np.array([10, 50, 153, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,30,29,32,28,27,33,23,28],
[14,0,20,23,25,18,20,26,14,20],
[20,30,0,21,29,28,23,25,25,24],
[21,27,29,0,23,23,29,24,22,18],
[18,25,21,27,0,21,22,31,20,22],
[22,32,22,27,29,0,24,25,23,26],
[23,30,27,21,28,26,0,22,24,21],
[17,24,25,26,19,25,28,0,21,25],
[27,36,25,28,30,27,26,29,0,26],
[22,30,26,32,28,24,29,25,24,0]])



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
result = np.append(np.array([10, 50, 154, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,22,22,25,33,27,28,30,29],
[26,0,29,24,26,28,29,25,31,25],
[28,21,0,24,26,27,30,24,26,25],
[28,26,26,0,26,29,25,27,31,24],
[25,24,24,24,0,32,31,27,29,25],
[17,22,23,21,18,0,22,28,21,17],
[23,21,20,25,19,28,0,29,25,25],
[22,25,26,23,23,22,21,0,29,25],
[20,19,24,19,21,29,25,21,0,22],
[21,25,25,26,25,33,25,25,28,0]])



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
result = np.append(np.array([10, 50, 155, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,25,29,27,17,23,26,26,20],
[30,0,30,29,26,25,27,29,28,23],
[25,20,0,31,25,22,19,22,22,19],
[21,21,19,0,20,16,21,23,21,18],
[23,24,25,30,0,17,24,28,23,19],
[33,25,28,34,33,0,32,27,28,25],
[27,23,31,29,26,18,0,26,27,24],
[24,21,28,27,22,23,24,0,26,23],
[24,22,28,29,27,22,23,24,0,22],
[30,27,31,32,31,25,26,27,28,0]])



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
result = np.append(np.array([10, 50, 156, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,22,24,30,32,33,28,24,26],
[30,0,23,33,36,46,36,27,37,31],
[28,27,0,31,27,48,24,27,31,27],
[26,17,19,0,36,33,39,33,27,26],
[20,14,23,14,0,27,24,16,24,16],
[18,4,2,17,23,0,14,14,8,21],
[17,14,26,11,26,36,0,22,20,13],
[22,23,23,17,34,36,28,0,16,29],
[26,13,19,23,26,42,30,34,0,25],
[24,19,23,24,34,29,37,21,25,0]])



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
result = np.append(np.array([10, 50, 157, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,33,31,23,15,25,25,31,20],
[11,0,33,21,13,5,10,5,31,10],
[17,17,0,11,16,5,11,5,32,10],
[19,29,39,0,13,29,25,15,31,25],
[27,37,34,37,0,16,31,20,37,26],
[35,45,45,21,34,0,21,15,42,21],
[25,40,39,25,19,29,0,13,50,24],
[25,45,45,35,30,35,37,0,42,35],
[19,19,18,19,13,8,0,8,0,18],
[30,40,40,25,24,29,26,15,32,0]])



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
result = np.append(np.array([10, 50, 158, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,22,23,21,22,30,20,24,23],
[26,0,23,27,27,29,31,26,32,23],
[28,27,0,25,25,25,27,27,24,27],
[27,23,25,0,18,23,30,23,21,23],
[29,23,25,32,0,26,30,28,28,26],
[28,21,25,27,24,0,25,24,27,27],
[20,19,23,20,20,25,0,24,21,19],
[30,24,23,27,22,26,26,0,22,28],
[26,18,26,29,22,23,29,28,0,25],
[27,27,23,27,24,23,31,22,25,0]])



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
result = np.append(np.array([10, 50, 159, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,22,24,26,18,24,21,21,24],
[23,0,18,27,25,22,25,24,25,27],
[28,32,0,28,27,26,33,24,31,33],
[26,23,22,0,20,18,26,23,17,25],
[24,25,23,30,0,23,30,27,26,30],
[32,28,24,32,27,0,33,28,31,29],
[26,25,17,24,20,17,0,24,20,31],
[29,26,26,27,23,22,26,0,28,25],
[29,25,19,33,24,19,30,22,0,22],
[26,23,17,25,20,21,19,25,28,0]])



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
result = np.append(np.array([10, 50, 160, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,26,25,17,14,18,22,20,20],
[24,0,21,25,12,13,14,14,24,20],
[24,29,0,20,14,12,15,21,16,23],
[25,25,30,0,20,15,20,19,21,29],
[33,38,36,30,0,33,33,24,32,24],
[36,37,38,35,17,0,32,29,33,30],
[32,36,35,30,17,18,0,24,26,29],
[28,36,29,31,26,21,26,0,26,17],
[30,26,34,29,18,17,24,24,0,25],
[30,30,27,21,26,20,21,33,25,0]])



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
result = np.append(np.array([10, 50, 161, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,28,31,23,31,30,29,29,28],
[25,0,27,27,25,32,24,23,26,27],
[22,23,0,25,20,31,23,24,27,30],
[19,23,25,0,18,29,23,20,27,29],
[27,25,30,32,0,30,25,30,30,29],
[19,18,19,21,20,0,15,20,21,23],
[20,26,27,27,25,35,0,26,23,28],
[21,27,26,30,20,30,24,0,25,30],
[21,24,23,23,20,29,27,25,0,27],
[22,23,20,21,21,27,22,20,23,0]])



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
result = np.append(np.array([10, 50, 162, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,34,50,36,39,36,23,39,39],
[16,0,18,23,29,21,5,29,19,10],
[16,32,0,21,34,37,13,39,27,21],
[0,27,29,0,13,21,5,18,19,21],
[14,21,16,37,0,24,18,18,21,21],
[11,29,13,29,26,0,24,29,24,18],
[14,45,37,45,32,26,0,37,32,28],
[27,21,11,32,32,21,13,0,16,21],
[11,31,23,31,29,26,18,34,0,23],
[11,40,29,29,29,32,22,29,27,0]])



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
result = np.append(np.array([10, 50, 163, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,32,25,28,25,28,30,33,29],
[18,0,20,23,26,22,18,20,22,25],
[18,30,0,22,28,23,21,26,26,27],
[25,27,28,0,22,23,23,23,27,32],
[22,24,22,28,0,23,21,22,23,27],
[25,28,27,27,27,0,23,24,27,31],
[22,32,29,27,29,27,0,20,28,29],
[20,30,24,27,28,26,30,0,23,27],
[17,28,24,23,27,23,22,27,0,23],
[21,25,23,18,23,19,21,23,27,0]])



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
result = np.append(np.array([10, 50, 164, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,25,24,39,21,25,23,26,24],
[34,0,28,34,29,24,29,25,36,26],
[25,22,0,34,39,21,27,22,34,29],
[26,16,16,0,25,15,14,9,31,20],
[11,21,11,25,0,16,21,27,27,22],
[29,26,29,35,34,0,30,27,34,25],
[25,21,23,36,29,20,0,28,34,29],
[27,25,28,41,23,23,22,0,33,27],
[24,14,16,19,23,16,16,17,0,15],
[26,24,21,30,28,25,21,23,35,0]])



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
result = np.append(np.array([10, 50, 165, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,20,27,23,23,20,22,25,16],
[30,0,21,26,31,27,23,28,26,27],
[30,29,0,31,26,32,28,24,30,20],
[23,24,19,0,19,18,18,20,24,16],
[27,19,24,31,0,27,22,29,22,15],
[27,23,18,32,23,0,22,20,31,19],
[30,27,22,32,28,28,0,30,29,21],
[28,22,26,30,21,30,20,0,24,19],
[25,24,20,26,28,19,21,26,0,21],
[34,23,30,34,35,31,29,31,29,0]])



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
result = np.append(np.array([10, 50, 166, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,23,24,23,22,26,31,22,27],
[25,0,28,22,30,21,24,29,24,26],
[27,22,0,27,28,19,25,29,31,29],
[26,28,23,0,23,24,28,26,26,27],
[27,20,22,27,0,26,24,28,25,21],
[28,29,31,26,24,0,32,31,26,29],
[24,26,25,22,26,18,0,31,16,26],
[19,21,21,24,22,19,19,0,20,25],
[28,26,19,24,25,24,34,30,0,31],
[23,24,21,23,29,21,24,25,19,0]])



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
result = np.append(np.array([10, 50, 167, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,12,15,14,19,22,14,12,28],
[30,0,21,12,17,24,22,32,20,25],
[38,29,0,19,25,31,22,24,18,32],
[35,38,31,0,25,34,22,39,33,39],
[36,33,25,25,0,37,30,28,26,26],
[31,26,19,16,13,0,14,23,26,26],
[28,28,28,28,20,36,0,29,23,35],
[36,18,26,11,22,27,21,0,12,30],
[38,30,32,17,24,24,27,38,0,35],
[22,25,18,11,24,24,15,20,15,0]])



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
result = np.append(np.array([10, 50, 168, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,27,24,33,28,30,28,34,26],
[22,0,26,29,32,24,30,36,35,26],
[23,24,0,22,29,31,30,34,30,21],
[26,21,28,0,27,25,28,29,27,26],
[17,18,21,23,0,20,28,20,22,21],
[22,26,19,25,30,0,22,26,29,23],
[20,20,20,22,22,28,0,31,24,17],
[22,14,16,21,30,24,19,0,22,23],
[16,15,20,23,28,21,26,28,0,13],
[24,24,29,24,29,27,33,27,37,0]])



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
result = np.append(np.array([10, 50, 169, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,28,21,28,20,25,28,28,30],
[26,0,22,25,22,24,23,28,25,26],
[22,28,0,24,24,23,25,27,26,25],
[29,25,26,0,24,23,25,26,25,27],
[22,28,26,26,0,19,25,24,24,24],
[30,26,27,27,31,0,25,30,33,32],
[25,27,25,25,25,25,0,25,26,28],
[22,22,23,24,26,20,25,0,27,23],
[22,25,24,25,26,17,24,23,0,23],
[20,24,25,23,26,18,22,27,27,0]])



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
result = np.append(np.array([10, 50, 170, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,24,14,19,20,11,21,9,17],
[24,0,23,24,20,26,10,25,16,27],
[26,27,0,29,27,35,26,9,16,19],
[36,26,21,0,21,35,19,29,29,35],
[31,30,23,29,0,29,30,24,17,31],
[30,24,15,15,21,0,27,23,15,25],
[39,40,24,31,20,23,0,26,17,28],
[29,25,41,21,26,27,24,0,28,28],
[41,34,34,21,33,35,33,22,0,33],
[33,23,31,15,19,25,22,22,17,0]])



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
result = np.append(np.array([10, 50, 171, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,32,23,33,34,30,21,24,30],
[25,0,28,30,26,29,30,24,23,25],
[18,22,0,17,27,29,19,20,27,23],
[27,20,33,0,30,28,26,21,26,28],
[17,24,23,20,0,24,19,15,23,19],
[16,21,21,22,26,0,22,21,25,25],
[20,20,31,24,31,28,0,25,23,21],
[29,26,30,29,35,29,25,0,24,32],
[26,27,23,24,27,25,27,26,0,29],
[20,25,27,22,31,25,29,18,21,0]])



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
result = np.append(np.array([10, 50, 172, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,28,30,30,21,25,19,27,30],
[18,0,23,43,3,31,27,32,43,32],
[22,27,0,25,17,36,29,16,42,42],
[20,7,25,0,8,25,29,25,45,20],
[20,47,33,42,0,41,40,36,42,42],
[29,19,14,25,9,0,12,17,27,16],
[25,23,21,21,10,38,0,10,27,38],
[31,18,34,25,14,33,40,0,37,36],
[23,7,8,5,8,23,23,13,0,25],
[20,18,8,30,8,34,12,14,25,0]])



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
result = np.append(np.array([10, 50, 173, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,35,24,32,23,26,37,29,31],
[19,0,35,21,31,21,30,31,29,27],
[15,15,0,17,16,13,28,26,29,22],
[26,29,33,0,34,23,24,38,37,34],
[18,19,34,16,0,28,22,31,24,27],
[27,29,37,27,22,0,27,26,27,21],
[24,20,22,26,28,23,0,37,29,31],
[13,19,24,12,19,24,13,0,17,16],
[21,21,21,13,26,23,21,33,0,25],
[19,23,28,16,23,29,19,34,25,0]])



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
result = np.append(np.array([10, 50, 174, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,33,29,26,27,23,36,20,33],
[18,0,29,25,28,20,26,41,20,22],
[17,21,0,22,30,23,16,33,19,32],
[21,25,28,0,20,24,15,21,12,27],
[24,22,20,30,0,25,16,24,27,24],
[23,30,27,26,25,0,30,29,17,28],
[27,24,34,35,34,20,0,26,25,36],
[14,9,17,29,26,21,24,0,14,14],
[30,30,31,38,23,33,25,36,0,37],
[17,28,18,23,26,22,14,36,13,0]])



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
result = np.append(np.array([10, 50, 175, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,28,25,14,16,19,22,17,29],
[33,0,34,31,27,24,34,27,28,35],
[22,16,0,28,23,17,21,25,25,26],
[25,19,22,0,20,12,19,27,20,25],
[36,23,27,30,0,24,24,30,29,30],
[34,26,33,38,26,0,32,33,23,29],
[31,16,29,31,26,18,0,21,20,27],
[28,23,25,23,20,17,29,0,20,32],
[33,22,25,30,21,27,30,30,0,32],
[21,15,24,25,20,21,23,18,18,0]])



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
result = np.append(np.array([10, 50, 176, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,35,23,22,28,21,22,24,35],
[28,0,29,20,23,29,21,22,24,24],
[15,21,0,15,15,22,12,18,18,23],
[27,30,35,0,21,23,17,18,27,30],
[28,27,35,29,0,25,24,21,25,30],
[22,21,28,27,25,0,19,22,24,25],
[29,29,38,33,26,31,0,30,22,26],
[28,28,32,32,29,28,20,0,28,28],
[26,26,32,23,25,26,28,22,0,27],
[15,26,27,20,20,25,24,22,23,0]])



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
result = np.append(np.array([10, 50, 177, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,28,32,27,20,26,20,27,25],
[31,0,25,29,23,14,21,15,19,28],
[22,25,0,30,28,24,29,20,28,24],
[18,21,20,0,24,19,24,20,22,20],
[23,27,22,26,0,23,30,24,29,27],
[30,36,26,31,27,0,30,25,28,31],
[24,29,21,26,20,20,0,18,17,25],
[30,35,30,30,26,25,32,0,27,28],
[23,31,22,28,21,22,33,23,0,27],
[25,22,26,30,23,19,25,22,23,0]])



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
result = np.append(np.array([10, 50, 178, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,13,4,22,31,18,40,21,21],
[41,0,18,37,37,26,41,41,33,37],
[37,32,0,25,43,25,35,40,44,42],
[46,13,25,0,37,31,41,46,44,48],
[28,13,7,13,0,13,6,28,24,28],
[19,24,25,19,37,0,35,35,33,36],
[32,9,15,9,44,15,0,40,38,38],
[10,9,10,4,22,15,10,0,9,9],
[29,17,6,6,26,17,12,41,0,17],
[29,13,8,2,22,14,12,41,33,0]])



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
result = np.append(np.array([10, 50, 179, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,20,32,21,23,24,24,28,20],
[26,0,27,37,24,24,21,28,25,21],
[30,23,0,30,24,24,26,24,28,25],
[18,13,20,0,15,18,17,22,25,13],
[29,26,26,35,0,25,27,27,25,24],
[27,26,26,32,25,0,24,27,29,23],
[26,29,24,33,23,26,0,22,26,20],
[26,22,26,28,23,23,28,0,28,19],
[22,25,22,25,25,21,24,22,0,22],
[30,29,25,37,26,27,30,31,28,0]])



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
result = np.append(np.array([10, 50, 180, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,23,35,30,22,25,23,28,24],
[12,0,20,29,17,18,19,22,21,14],
[27,30,0,28,23,30,25,21,29,27],
[15,21,22,0,14,18,19,13,20,16],
[20,33,27,36,0,22,20,18,27,23],
[28,32,20,32,28,0,24,31,31,23],
[25,31,25,31,30,26,0,26,27,23],
[27,28,29,37,32,19,24,0,36,24],
[22,29,21,30,23,19,23,14,0,21],
[26,36,23,34,27,27,27,26,29,0]])



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
result = np.append(np.array([10, 50, 181, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,25,0,7,25,7,7,25,11],
[43,0,38,20,31,34,27,49,39,21],
[25,12,0,0,22,25,8,11,26,16],
[50,30,50,0,50,35,35,39,35,25],
[43,19,28,0,0,34,8,26,19,12],
[25,16,25,15,16,0,19,23,34,16],
[43,23,42,15,42,31,0,22,43,25],
[43,1,39,11,24,27,28,0,39,21],
[25,11,24,15,31,16,7,11,0,24],
[39,29,34,25,38,34,25,29,26,0]])



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
result = np.append(np.array([10, 50, 182, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,11,15,25,19,24,15,26,16],
[22,0,22,19,32,27,22,18,32,23],
[39,28,0,31,40,28,29,25,33,27],
[35,31,19,0,27,28,24,16,33,32],
[25,18,10,23,0,15,21,14,28,19],
[31,23,22,22,35,0,22,17,33,28],
[26,28,21,26,29,28,0,17,27,26],
[35,32,25,34,36,33,33,0,33,31],
[24,18,17,17,22,17,23,17,0,12],
[34,27,23,18,31,22,24,19,38,0]])



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
result = np.append(np.array([10, 50, 183, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,29,19,28,26,25,28,22,27],
[18,0,23,21,23,23,21,19,22,21],
[21,27,0,20,20,21,21,25,21,20],
[31,29,30,0,29,27,23,30,28,28],
[22,27,30,21,0,19,21,19,18,16],
[24,27,29,23,31,0,23,25,26,24],
[25,29,29,27,29,27,0,27,24,19],
[22,31,25,20,31,25,23,0,23,19],
[28,28,29,22,32,24,26,27,0,24],
[23,29,30,22,34,26,31,31,26,0]])



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
result = np.append(np.array([10, 50, 184, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,26,27,28,32,27,29,31,30],
[25,0,21,27,30,34,24,26,30,24],
[24,29,0,26,33,33,27,25,25,29],
[23,23,24,0,24,31,26,23,25,28],
[22,20,17,26,0,26,20,20,21,23],
[18,16,17,19,24,0,19,18,25,19],
[23,26,23,24,30,31,0,23,25,27],
[21,24,25,27,30,32,27,0,27,31],
[19,20,25,25,29,25,25,23,0,24],
[20,26,21,22,27,31,23,19,26,0]])



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
result = np.append(np.array([10, 50, 185, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,34,27,25,30,23,29,25,30],
[27,0,27,28,22,21,25,27,23,26],
[16,23,0,20,18,24,21,24,27,25],
[23,22,30,0,24,27,23,27,25,27],
[25,28,32,26,0,31,24,27,23,21],
[20,29,26,23,19,0,21,24,24,23],
[27,25,29,27,26,29,0,24,26,25],
[21,23,26,23,23,26,26,0,24,29],
[25,27,23,25,27,26,24,26,0,24],
[20,24,25,23,29,27,25,21,26,0]])



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
result = np.append(np.array([10, 50, 186, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,26,27,28,29,31,23,26,26],
[24,0,20,25,29,21,26,22,20,21],
[24,30,0,25,28,21,31,24,25,22],
[23,25,25,0,28,23,31,19,22,23],
[22,21,22,22,0,20,27,18,19,20],
[21,29,29,27,30,0,34,25,26,26],
[19,24,19,19,23,16,0,15,16,16],
[27,28,26,31,32,25,35,0,28,21],
[24,30,25,28,31,24,34,22,0,25],
[24,29,28,27,30,24,34,29,25,0]])



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
result = np.append(np.array([10, 50, 187, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,21,17,18,26,24,20,19,33],
[40,0,30,29,24,32,39,31,32,35],
[29,20,0,27,18,20,37,19,31,39],
[33,21,23,0,21,24,27,26,25,32],
[32,26,32,29,0,27,29,25,24,36],
[24,18,30,26,23,0,32,21,29,32],
[26,11,13,23,21,18,0,20,14,27],
[30,19,31,24,25,29,30,0,31,36],
[31,18,19,25,26,21,36,19,0,32],
[17,15,11,18,14,18,23,14,18,0]])



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
result = np.append(np.array([10, 50, 188, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,20,14,19,16,16,26,24,27],
[37,0,25,26,30,22,21,32,43,39],
[30,25,0,20,34,20,26,35,40,33],
[36,24,30,0,35,18,29,28,42,27],
[31,20,16,15,0,15,6,30,31,29],
[34,28,30,32,35,0,21,39,41,38],
[34,29,24,21,44,29,0,32,42,35],
[24,18,15,22,20,11,18,0,29,23],
[26,7,10,8,19,9,8,21,0,19],
[23,11,17,23,21,12,15,27,31,0]])



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
result = np.append(np.array([10, 50, 189, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,26,17,19,28,22,24,27,17],
[22,0,23,24,15,34,13,30,27,20],
[24,27,0,25,24,30,18,24,27,22],
[33,26,25,0,26,34,26,22,27,23],
[31,35,26,24,0,32,27,28,28,24],
[22,16,20,16,18,0,15,20,18,16],
[28,37,32,24,23,35,0,28,36,28],
[26,20,26,28,22,30,22,0,30,24],
[23,23,23,23,22,32,14,20,0,19],
[33,30,28,27,26,34,22,26,31,0]])



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
result = np.append(np.array([10, 50, 190, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,14,7,40,10,13,25,24,18],
[40,0,25,7,30,22,20,25,24,18],
[36,25,0,15,26,18,33,19,12,16],
[43,43,35,0,38,28,20,26,33,16],
[10,20,24,12,0,15,20,21,7,25],
[40,28,32,22,35,0,30,30,19,18],
[37,30,17,30,30,20,0,15,27,10],
[25,25,31,24,29,20,35,0,12,7],
[26,26,38,17,43,31,23,38,0,18],
[32,32,34,34,25,32,40,43,32,0]])



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
result = np.append(np.array([10, 50, 191, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,26,25,27,26,16,24,22,25],
[22,0,19,23,18,21,21,21,20,23],
[24,31,0,29,26,24,22,27,27,31],
[25,27,21,0,24,23,21,26,23,33],
[23,32,24,26,0,26,21,28,25,27],
[24,29,26,27,24,0,25,24,21,28],
[34,29,28,29,29,25,0,28,24,30],
[26,29,23,24,22,26,22,0,20,25],
[28,30,23,27,25,29,26,30,0,29],
[25,27,19,17,23,22,20,25,21,0]])



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
result = np.append(np.array([10, 50, 192, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,30,31,23,25,26,29,26,27],
[24,0,28,31,27,26,29,25,29,24],
[20,22,0,22,26,28,24,24,25,24],
[19,19,28,0,29,24,30,22,27,23],
[27,23,24,21,0,28,30,24,26,25],
[25,24,22,26,22,0,25,29,24,26],
[24,21,26,20,20,25,0,24,20,25],
[21,25,26,28,26,21,26,0,24,23],
[24,21,25,23,24,26,30,26,0,25],
[23,26,26,27,25,24,25,27,25,0]])



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
result = np.append(np.array([10, 50, 193, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,27,29,12,14,27,23,31,16],
[25,0,20,20,10,17,10,23,20,17],
[23,30,0,22,18,23,8,23,20,31],
[21,30,28,0,11,11,3,32,20,31],
[38,40,32,39,0,27,16,34,36,33],
[36,33,27,39,23,0,17,35,30,25],
[23,40,42,47,34,33,0,35,24,35],
[27,27,27,18,16,15,15,0,34,31],
[19,30,30,30,14,20,26,16,0,30],
[34,33,19,19,17,25,15,19,20,0]])



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
result = np.append(np.array([10, 50, 194, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,18,19,26,29,21,27,30,27],
[30,0,28,24,22,30,27,27,31,28],
[32,22,0,25,26,27,31,24,31,24],
[31,26,25,0,25,29,32,25,29,30],
[24,28,24,25,0,24,33,23,31,28],
[21,20,23,21,26,0,27,23,30,28],
[29,23,19,18,17,23,0,12,25,25],
[23,23,26,25,27,27,38,0,39,29],
[20,19,19,21,19,20,25,11,0,24],
[23,22,26,20,22,22,25,21,26,0]])



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
result = np.append(np.array([10, 50, 195, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,28,31,29,22,23,29,28,20],
[25,0,21,26,26,21,24,26,21,22],
[22,29,0,28,29,24,22,25,21,19],
[19,24,22,0,23,27,24,20,24,21],
[21,24,21,27,0,17,18,21,27,18],
[28,29,26,23,33,0,22,23,25,21],
[27,26,28,26,32,28,0,25,26,25],
[21,24,25,30,29,27,25,0,25,22],
[22,29,29,26,23,25,24,25,0,27],
[30,28,31,29,32,29,25,28,23,0]])



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
result = np.append(np.array([10, 50, 196, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,25,28,27,24,29,40,29,29],
[16,0,25,18,21,22,28,33,19,23],
[25,25,0,23,28,25,22,33,28,27],
[22,32,27,0,28,26,28,34,25,22],
[23,29,22,22,0,17,28,35,24,22],
[26,28,25,24,33,0,26,34,24,23],
[21,22,28,22,22,24,0,26,30,31],
[10,17,17,16,15,16,24,0,17,19],
[21,31,22,25,26,26,20,33,0,21],
[21,27,23,28,28,27,19,31,29,0]])



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
result = np.append(np.array([10, 50, 197, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,27,23,19,19,26,23,20,19],
[23,0,23,22,19,23,17,27,22,25],
[23,27,0,21,14,20,21,26,21,21],
[27,28,29,0,23,24,24,31,21,26],
[31,31,36,27,0,23,27,34,26,24],
[31,27,30,26,27,0,28,31,21,30],
[24,33,29,26,23,22,0,30,23,21],
[27,23,24,19,16,19,20,0,21,16],
[30,28,29,29,24,29,27,29,0,25],
[31,25,29,24,26,20,29,34,25,0]])



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
result = np.append(np.array([10, 50, 198, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,34,30,21,34,34,33,29,30],
[16,0,20,13,22,31,23,24,13,12],
[16,30,0,23,24,40,30,26,26,24],
[20,37,27,0,24,44,32,34,23,29],
[29,28,26,26,0,34,30,30,24,27],
[16,19,10,6,16,0,19,12,17,15],
[16,27,20,18,20,31,0,18,25,15],
[17,26,24,16,20,38,32,0,26,22],
[21,37,24,27,26,33,25,24,0,26],
[20,38,26,21,23,35,35,28,24,0]])



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
result = np.append(np.array([10, 50, 199, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,24,20,30,25,29,25,25,26],
[24,0,19,20,27,20,27,24,22,21],
[26,31,0,26,34,28,30,26,29,25],
[30,30,24,0,36,32,29,29,21,29],
[20,23,16,14,0,25,22,18,20,18],
[25,30,22,18,25,0,24,20,22,21],
[21,23,20,21,28,26,0,22,22,23],
[25,26,24,21,32,30,28,0,22,29],
[25,28,21,29,30,28,28,28,0,26],
[24,29,25,21,32,29,27,21,24,0]])



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
result = np.append(np.array([10, 50, 200, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mercw/mercw_10_50.csv", index=False, header=False)