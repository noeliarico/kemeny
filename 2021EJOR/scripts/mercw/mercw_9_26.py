
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,16,14,9,16,20,16,14,14],
[10,0,11,10,11,16,8,15,7],
[12,15,0,15,15,18,10,18,17],
[17,16,11,0,16,23,14,16,15],
[10,15,11,10,0,18,13,13,12],
[6,10,8,3,8,0,10,8,3],
[10,18,16,12,13,16,0,15,11],
[12,11,8,10,13,18,11,0,6],
[12,19,9,11,14,23,15,20,0]])



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
result = np.append(np.array([9, 26, 1, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,13,15,12,10,12,14,12],
[12,0,11,12,12,11,13,17,12],
[13,15,0,17,15,13,17,16,15],
[11,14,9,0,15,13,14,14,15],
[14,14,11,11,0,9,12,14,12],
[16,15,13,13,17,0,13,16,16],
[14,13,9,12,14,13,0,16,17],
[12,9,10,12,12,10,10,0,13],
[14,14,11,11,14,10,9,13,0]])



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
result = np.append(np.array([9, 26, 2, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,19,14,14,16,20,8,12],
[12,0,16,16,18,16,17,16,13],
[7,10,0,9,17,15,11,9,4],
[12,10,17,0,19,17,11,12,8],
[12,8,9,7,0,17,9,12,7],
[10,10,11,9,9,0,11,8,5],
[6,9,15,15,17,15,0,11,6],
[18,10,17,14,14,18,15,0,12],
[14,13,22,18,19,21,20,14,0]])



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
result = np.append(np.array([9, 26, 3, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,12,9,10,16,15,16,14],
[8,0,10,11,7,11,11,14,10],
[14,16,0,19,11,16,16,15,15],
[17,15,7,0,10,16,12,13,10],
[16,19,15,16,0,19,15,12,8],
[10,15,10,10,7,0,11,12,9],
[11,15,10,14,11,15,0,11,10],
[10,12,11,13,14,14,15,0,10],
[12,16,11,16,18,17,16,16,0]])



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
result = np.append(np.array([9, 26, 4, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,10,9,12,13,10,12,10],
[14,0,13,9,11,14,14,14,10],
[16,13,0,13,13,17,19,19,12],
[17,17,13,0,14,15,16,17,12],
[14,15,13,12,0,14,15,14,13],
[13,12,9,11,12,0,17,15,9],
[16,12,7,10,11,9,0,13,8],
[14,12,7,9,12,11,13,0,9],
[16,16,14,14,13,17,18,17,0]])



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
result = np.append(np.array([9, 26, 5, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,14,11,20,19,15,17,16],
[13,0,10,11,20,19,15,17,16],
[12,16,0,19,23,23,23,20,23],
[15,15,7,0,17,22,17,15,14],
[6,6,3,9,0,14,9,15,5],
[7,7,3,4,12,0,14,11,11],
[11,11,3,9,17,12,0,19,16],
[9,9,6,11,11,15,7,0,7],
[10,10,3,12,21,15,10,19,0]])



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
result = np.append(np.array([9, 26, 6, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,14,11,12,9,13,9,15],
[13,0,14,14,12,11,11,9,14],
[12,12,0,10,10,6,12,10,12],
[15,12,16,0,9,13,13,12,15],
[14,14,16,17,0,12,13,15,18],
[17,15,20,13,14,0,12,13,18],
[13,15,14,13,13,14,0,13,19],
[17,17,16,14,11,13,13,0,18],
[11,12,14,11,8,8,7,8,0]])



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
result = np.append(np.array([9, 26, 7, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,14,7,0,13,7,7,7],
[20,0,20,20,7,7,7,13,13],
[12,6,0,13,0,13,7,6,13],
[19,6,13,0,0,13,7,0,7],
[26,19,26,26,0,13,13,19,13],
[13,19,13,13,13,0,13,6,13],
[19,19,19,19,13,13,0,6,13],
[19,13,20,26,7,20,20,0,13],
[19,13,13,19,13,13,13,13,0]])



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
result = np.append(np.array([9, 26, 8, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,16,16,14,16,15,12,11],
[13,0,14,18,11,15,12,11,5],
[10,12,0,15,9,12,8,9,10],
[10,8,11,0,7,11,11,10,7],
[12,15,17,19,0,13,18,8,16],
[10,11,14,15,13,0,13,7,8],
[11,14,18,15,8,13,0,9,12],
[14,15,17,16,18,19,17,0,12],
[15,21,16,19,10,18,14,14,0]])



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
result = np.append(np.array([9, 26, 9, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,20,6,15,9,18,19,12],
[17,0,21,12,19,10,19,12,16],
[6,5,0,0,0,5,18,6,5],
[20,14,26,0,13,15,21,20,18],
[11,7,26,13,0,10,19,11,12],
[17,16,21,11,16,0,18,11,21],
[8,7,8,5,7,8,0,8,5],
[7,14,20,6,15,15,18,0,17],
[14,10,21,8,14,5,21,9,0]])



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
result = np.append(np.array([9, 26, 10, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,14,13,11,11,14,13,14],
[11,0,11,11,10,11,11,7,10],
[12,15,0,14,13,12,13,12,15],
[13,15,12,0,13,14,14,14,12],
[15,16,13,13,0,13,14,9,15],
[15,15,14,12,13,0,15,14,16],
[12,15,13,12,12,11,0,12,12],
[13,19,14,12,17,12,14,0,14],
[12,16,11,14,11,10,14,12,0]])



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
result = np.append(np.array([9, 26, 11, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,14,19,11,14,19,15,13],
[12,0,14,20,13,13,17,16,15],
[12,12,0,23,17,13,19,16,16],
[7,6,3,0,8,5,9,10,12],
[15,13,9,18,0,13,14,15,16],
[12,13,13,21,13,0,17,14,15],
[7,9,7,17,12,9,0,7,11],
[11,10,10,16,11,12,19,0,14],
[13,11,10,14,10,11,15,12,0]])



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
result = np.append(np.array([9, 26, 12, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,15,13,15,15,17,15,12],
[7,0,10,14,14,15,12,11,10],
[11,16,0,12,16,14,16,13,11],
[13,12,14,0,15,14,14,7,11],
[11,12,10,11,0,10,13,10,9],
[11,11,12,12,16,0,16,8,12],
[9,14,10,12,13,10,0,8,10],
[11,15,13,19,16,18,18,0,13],
[14,16,15,15,17,14,16,13,0]])



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
result = np.append(np.array([9, 26, 13, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,11,13,9,13,11,15,15],
[14,0,11,15,13,19,17,22,15],
[15,15,0,16,12,21,18,18,15],
[13,11,10,0,11,17,17,12,13],
[17,13,14,15,0,18,19,17,15],
[13,7,5,9,8,0,11,9,11],
[15,9,8,9,7,15,0,11,11],
[11,4,8,14,9,17,15,0,14],
[11,11,11,13,11,15,15,12,0]])



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
result = np.append(np.array([9, 26, 14, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,17,18,17,10,15,18,11],
[8,0,14,16,12,9,10,12,9],
[9,12,0,19,12,10,10,13,13],
[8,10,7,0,11,10,11,10,11],
[9,14,14,15,0,13,12,13,9],
[16,17,16,16,13,0,14,15,11],
[11,16,16,15,14,12,0,11,10],
[8,14,13,16,13,11,15,0,9],
[15,17,13,15,17,15,16,17,0]])



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
result = np.append(np.array([9, 26, 15, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,11,10,10,10,10,12,7],
[13,0,9,10,6,6,10,12,12],
[15,17,0,16,13,13,15,16,11],
[16,16,10,0,7,9,8,12,12],
[16,20,13,19,0,13,14,16,12],
[16,20,13,17,13,0,16,18,14],
[16,16,11,18,12,10,0,14,14],
[14,14,10,14,10,8,12,0,14],
[19,14,15,14,14,12,12,12,0]])



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
result = np.append(np.array([9, 26, 16, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,13,13,24,24,13,13],
[13,0,24,24,24,24,24,24,24],
[13,2,0,26,0,24,24,2,13],
[13,2,0,0,0,11,24,0,13],
[13,2,26,26,0,26,26,15,26],
[2,2,2,15,0,0,13,2,15],
[2,2,2,2,0,13,0,2,2],
[13,2,24,26,11,24,24,0,24],
[13,2,13,13,0,11,24,2,0]])



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
result = np.append(np.array([9, 26, 17, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,14,18,12,10,13,12,15],
[8,0,12,12,11,9,10,10,13],
[12,14,0,13,8,10,9,11,10],
[8,14,13,0,11,11,11,12,15],
[14,15,18,15,0,13,12,13,16],
[16,17,16,15,13,0,13,17,14],
[13,16,17,15,14,13,0,12,17],
[14,16,15,14,13,9,14,0,12],
[11,13,16,11,10,12,9,14,0]])



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
result = np.append(np.array([9, 26, 18, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,14,15,6,13,7,7,12],
[19,0,19,21,13,16,15,10,19],
[12,7,0,9,13,7,9,11,10],
[11,5,17,0,9,19,14,10,15],
[20,13,13,17,0,13,14,10,16],
[13,10,19,7,13,0,15,12,13],
[19,11,17,12,12,11,0,18,15],
[19,16,15,16,16,14,8,0,14],
[14,7,16,11,10,13,11,12,0]])



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
result = np.append(np.array([9, 26, 19, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,11,18,11,13,18,12,12],
[11,0,13,8,13,11,15,15,12],
[15,13,0,15,16,13,18,16,11],
[8,18,11,0,16,17,16,16,17],
[15,13,10,10,0,13,15,13,15],
[13,15,13,9,13,0,18,18,12],
[8,11,8,10,11,8,0,15,12],
[14,11,10,10,13,8,11,0,10],
[14,14,15,9,11,14,14,16,0]])



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
result = np.append(np.array([9, 26, 20, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,7,13,15,12,15,11,16],
[12,0,12,13,15,9,10,13,16],
[19,14,0,13,17,11,12,10,15],
[13,13,13,0,16,13,10,12,14],
[11,11,9,10,0,13,10,10,13],
[14,17,15,13,13,0,10,14,17],
[11,16,14,16,16,16,0,12,17],
[15,13,16,14,16,12,14,0,17],
[10,10,11,12,13,9,9,9,0]])



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
result = np.append(np.array([9, 26, 21, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,7,6,12,13,9,6,7],
[17,0,14,14,12,10,10,13,10],
[19,12,0,10,12,14,13,14,14],
[20,12,16,0,14,16,12,12,12],
[14,14,14,12,0,17,15,11,12],
[13,16,12,10,9,0,12,8,8],
[17,16,13,14,11,14,0,9,11],
[20,13,12,14,15,18,17,0,13],
[19,16,12,14,14,18,15,13,0]])



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
result = np.append(np.array([9, 26, 22, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,7,18,25,14,17,10,7],
[11,0,17,12,20,3,17,20,16],
[19,9,0,15,19,9,14,20,20],
[8,14,11,0,15,8,11,15,14],
[1,6,7,11,0,4,7,1,7],
[12,23,17,18,22,0,18,18,17],
[9,9,12,15,19,8,0,10,9],
[16,6,6,11,25,8,16,0,16],
[19,10,6,12,19,9,17,10,0]])



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
result = np.append(np.array([9, 26, 23, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,12,14,13,12,12,12,11],
[15,0,11,13,14,14,13,17,12],
[14,15,0,14,14,14,13,13,12],
[12,13,12,0,11,13,14,14,13],
[13,12,12,15,0,11,12,17,11],
[14,12,12,13,15,0,11,18,9],
[14,13,13,12,14,15,0,15,16],
[14,9,13,12,9,8,11,0,8],
[15,14,14,13,15,17,10,18,0]])



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
result = np.append(np.array([9, 26, 24, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,8,10,19,6,15,19,13],
[10,0,10,17,12,9,9,17,9],
[18,16,0,23,17,13,14,17,16],
[16,9,3,0,18,4,14,18,8],
[7,14,9,8,0,9,12,17,13],
[20,17,13,22,17,0,17,18,15],
[11,17,12,12,14,9,0,13,19],
[7,9,9,8,9,8,13,0,7],
[13,17,10,18,13,11,7,19,0]])



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
result = np.append(np.array([9, 26, 25, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,15,13,14,9,14,12,9],
[11,0,12,7,16,9,12,12,12],
[11,14,0,9,14,11,12,12,10],
[13,19,17,0,20,14,15,18,14],
[12,10,12,6,0,9,11,9,8],
[17,17,15,12,17,0,16,12,12],
[12,14,14,11,15,10,0,13,11],
[14,14,14,8,17,14,13,0,10],
[17,14,16,12,18,14,15,16,0]])



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
result = np.append(np.array([9, 26, 26, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,13,14,10,11,12,15,16],
[12,0,11,10,9,14,10,14,15],
[13,15,0,10,10,14,14,16,16],
[12,16,16,0,13,18,14,16,18],
[16,17,16,13,0,12,18,17,14],
[15,12,12,8,14,0,14,17,13],
[14,16,12,12,8,12,0,14,17],
[11,12,10,10,9,9,12,0,14],
[10,11,10,8,12,13,9,12,0]])



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
result = np.append(np.array([9, 26, 27, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,11,10,17,12,15,16,10],
[16,0,17,16,15,13,17,17,13],
[15,9,0,14,16,16,15,14,12],
[16,10,12,0,14,16,15,14,12],
[9,11,10,12,0,14,14,14,14],
[14,13,10,10,12,0,14,17,10],
[11,9,11,11,12,12,0,14,5],
[10,9,12,12,12,9,12,0,9],
[16,13,14,14,12,16,21,17,0]])



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
result = np.append(np.array([9, 26, 28, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,11,9,8,8,7,7,16],
[20,0,11,13,11,11,11,16,20],
[15,15,0,15,15,13,22,17,15],
[17,13,11,0,17,8,17,17,18],
[18,15,11,9,0,9,8,18,19],
[18,15,13,18,17,0,18,18,18],
[19,15,4,9,18,8,0,18,18],
[19,10,9,9,8,8,8,0,22],
[10,6,11,8,7,8,8,4,0]])



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
result = np.append(np.array([9, 26, 29, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,11,13,14,16,15,15,16],
[10,0,11,14,13,15,18,16,17],
[15,15,0,12,13,13,14,13,15],
[13,12,14,0,17,16,18,14,15],
[12,13,13,9,0,20,13,14,12],
[10,11,13,10,6,0,10,12,11],
[11,8,12,8,13,16,0,9,11],
[11,10,13,12,12,14,17,0,14],
[10,9,11,11,14,15,15,12,0]])



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
result = np.append(np.array([9, 26, 30, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,19,15,13,15,13,11,12],
[13,0,19,14,11,16,10,11,15],
[7,7,0,10,10,11,8,10,8],
[11,12,16,0,14,17,13,11,13],
[13,15,16,12,0,16,11,11,15],
[11,10,15,9,10,0,10,8,11],
[13,16,18,13,15,16,0,13,13],
[15,15,16,15,15,18,13,0,13],
[14,11,18,13,11,15,13,13,0]])



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
result = np.append(np.array([9, 26, 31, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,11,10,11,11,11,12,12],
[13,0,8,12,8,11,10,14,11],
[15,18,0,16,11,12,12,12,11],
[16,14,10,0,12,11,15,12,11],
[15,18,15,14,0,15,17,16,12],
[15,15,14,15,11,0,14,17,10],
[15,16,14,11,9,12,0,11,9],
[14,12,14,14,10,9,15,0,13],
[14,15,15,15,14,16,17,13,0]])



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
result = np.append(np.array([9, 26, 32, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,12,18,12,15,13,12,14],
[17,0,12,17,11,12,14,14,14],
[14,14,0,18,13,13,14,11,12],
[8,9,8,0,6,9,11,9,9],
[14,15,13,20,0,14,16,10,14],
[11,14,13,17,12,0,13,11,14],
[13,12,12,15,10,13,0,11,13],
[14,12,15,17,16,15,15,0,14],
[12,12,14,17,12,12,13,12,0]])



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
result = np.append(np.array([9, 26, 33, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,19,9,12,13,9,13,14],
[16,0,17,7,10,14,8,13,13],
[7,9,0,7,12,10,8,14,15],
[17,19,19,0,15,18,13,17,17],
[14,16,14,11,0,18,10,15,14],
[13,12,16,8,8,0,9,14,12],
[17,18,18,13,16,17,0,22,17],
[13,13,12,9,11,12,4,0,13],
[12,13,11,9,12,14,9,13,0]])



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
result = np.append(np.array([9, 26, 34, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,16,13,17,14,15,12,12],
[14,0,13,13,11,15,17,16,12],
[10,13,0,9,7,15,13,16,10],
[13,13,17,0,15,13,18,20,19],
[9,15,19,11,0,9,13,15,13],
[12,11,11,13,17,0,13,10,12],
[11,9,13,8,13,13,0,8,13],
[14,10,10,6,11,16,18,0,15],
[14,14,16,7,13,14,13,11,0]])



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
result = np.append(np.array([9, 26, 35, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,7,12,16,10,9,10,9],
[16,0,20,21,20,13,15,16,18],
[19,6,0,17,11,8,15,14,13],
[14,5,9,0,15,6,8,8,7],
[10,6,15,11,0,6,8,10,9],
[16,13,18,20,20,0,12,23,9],
[17,11,11,18,18,14,0,13,11],
[16,10,12,18,16,3,13,0,9],
[17,8,13,19,17,17,15,17,0]])



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
result = np.append(np.array([9, 26, 36, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,12,10,16,12,14,9,15],
[17,0,13,18,18,19,16,15,18],
[14,13,0,14,15,16,17,14,18],
[16,8,12,0,13,13,17,10,13],
[10,8,11,13,0,14,15,13,12],
[14,7,10,13,12,0,13,13,14],
[12,10,9,9,11,13,0,9,12],
[17,11,12,16,13,13,17,0,15],
[11,8,8,13,14,12,14,11,0]])



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
result = np.append(np.array([9, 26, 37, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,10,16,26,14,6,6,6],
[7,0,4,16,17,13,6,0,2],
[16,22,0,16,22,22,22,16,11],
[10,10,10,0,17,21,14,10,10],
[0,9,4,9,0,13,6,0,2],
[12,13,4,5,13,0,4,12,3],
[20,20,4,12,20,22,0,13,14],
[20,26,10,16,26,14,13,0,2],
[20,24,15,16,24,23,12,24,0]])



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
result = np.append(np.array([9, 26, 38, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,20,20,5,20,7,20,18],
[6,0,24,24,11,20,13,26,18],
[6,2,0,21,11,20,13,21,13],
[6,2,5,0,11,20,7,7,0],
[21,15,15,15,0,20,7,15,15],
[6,6,6,6,6,0,6,6,6],
[19,13,13,19,19,20,0,15,13],
[6,0,5,19,11,20,11,0,0],
[8,8,13,26,11,20,13,26,0]])



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
result = np.append(np.array([9, 26, 39, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,16,14,16,14,8,17,13],
[11,0,11,13,12,16,9,16,15],
[10,15,0,18,18,16,9,15,17],
[12,13,8,0,14,16,14,15,15],
[10,14,8,12,0,16,6,15,12],
[12,10,10,10,10,0,9,12,11],
[18,17,17,12,20,17,0,18,14],
[9,10,11,11,11,14,8,0,13],
[13,11,9,11,14,15,12,13,0]])



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
result = np.append(np.array([9, 26, 40, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,8,15,9,9,12,12,10],
[7,0,12,13,8,6,8,13,5],
[18,14,0,12,15,13,18,11,10],
[11,13,14,0,13,11,14,15,7],
[17,18,11,13,0,7,14,13,9],
[17,20,13,15,19,0,14,15,13],
[14,18,8,12,12,12,0,11,7],
[14,13,15,11,13,11,15,0,8],
[16,21,16,19,17,13,19,18,0]])



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
result = np.append(np.array([9, 26, 41, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,16,9,16,15,16,19,15],
[5,0,13,11,9,8,14,14,14],
[10,13,0,14,14,9,12,10,9],
[17,15,12,0,17,12,15,16,18],
[10,17,12,9,0,6,19,13,16],
[11,18,17,14,20,0,19,14,17],
[10,12,14,11,7,7,0,12,16],
[7,12,16,10,13,12,14,0,14],
[11,12,17,8,10,9,10,12,0]])



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
result = np.append(np.array([9, 26, 42, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,16,11,13,12,10,9,10],
[11,0,10,13,11,13,11,11,10],
[10,16,0,13,13,14,9,11,13],
[15,13,13,0,16,14,14,12,12],
[13,15,13,10,0,12,10,7,9],
[14,13,12,12,14,0,14,11,15],
[16,15,17,12,16,12,0,11,14],
[17,15,15,14,19,15,15,0,11],
[16,16,13,14,17,11,12,15,0]])



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
result = np.append(np.array([9, 26, 43, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,9,12,11,16,17,14,11],
[16,0,11,10,15,17,16,15,10],
[17,15,0,17,13,19,21,14,15],
[14,16,9,0,9,13,13,15,12],
[15,11,13,17,0,21,19,14,15],
[10,9,7,13,5,0,11,10,8],
[9,10,5,13,7,15,0,13,7],
[12,11,12,11,12,16,13,0,11],
[15,16,11,14,11,18,19,15,0]])



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
result = np.append(np.array([9, 26, 44, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,15,14,16,13,12,14,9],
[9,0,7,10,15,9,12,10,10],
[11,19,0,16,18,15,12,14,12],
[12,16,10,0,14,10,14,14,5],
[10,11,8,12,0,14,7,10,13],
[13,17,11,16,12,0,14,15,15],
[14,14,14,12,19,12,0,11,12],
[12,16,12,12,16,11,15,0,9],
[17,16,14,21,13,11,14,17,0]])



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
result = np.append(np.array([9, 26, 45, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,15,15,12,9,13,13,9],
[11,0,12,9,8,6,10,12,8],
[11,14,0,10,13,11,12,13,12],
[11,17,16,0,13,12,18,16,8],
[14,18,13,13,0,15,18,17,11],
[17,20,15,14,11,0,18,20,14],
[13,16,14,8,8,8,0,17,10],
[13,14,13,10,9,6,9,0,10],
[17,18,14,18,15,12,16,16,0]])



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
result = np.append(np.array([9, 26, 46, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,8,10,8,13,13,12,15],
[16,0,9,12,12,13,15,16,16],
[18,17,0,18,12,15,13,16,14],
[16,14,8,0,12,14,16,16,15],
[18,14,14,14,0,13,13,11,11],
[13,13,11,12,13,0,16,13,21],
[13,11,13,10,13,10,0,14,12],
[14,10,10,10,15,13,12,0,18],
[11,10,12,11,15,5,14,8,0]])



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
result = np.append(np.array([9, 26, 47, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,14,15,17,12,15,18,14],
[13,0,12,16,10,11,10,20,8],
[12,14,0,16,18,11,15,17,14],
[11,10,10,0,14,11,9,16,7],
[9,16,8,12,0,14,12,18,11],
[14,15,15,15,12,0,14,18,14],
[11,16,11,17,14,12,0,15,11],
[8,6,9,10,8,8,11,0,10],
[12,18,12,19,15,12,15,16,0]])



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
result = np.append(np.array([9, 26, 48, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,20,12,9,20,14,15,26],
[6,0,15,18,13,20,15,8,18],
[6,11,0,18,6,20,7,6,11],
[14,8,8,0,2,15,2,14,14],
[17,13,20,24,0,26,13,14,24],
[6,6,6,11,0,0,6,6,12],
[12,11,19,24,13,20,0,12,24],
[11,18,20,12,12,20,14,0,24],
[0,8,15,12,2,14,2,2,0]])



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
result = np.append(np.array([9, 26, 49, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,14,13,13,0,0,13,0],
[26,0,14,14,14,0,0,14,0],
[12,12,0,25,12,12,0,25,0],
[13,12,1,0,12,12,0,13,0],
[13,12,14,14,0,0,0,26,0],
[26,26,14,14,26,0,13,26,0],
[26,26,26,26,26,13,0,26,13],
[13,12,1,13,0,0,0,0,0],
[26,26,26,26,26,26,13,26,0]])



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
result = np.append(np.array([9, 26, 50, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,12,17,12,18,8,10,12],
[9,0,12,12,11,12,9,9,10],
[14,14,0,14,11,13,11,13,12],
[9,14,12,0,15,10,7,8,13],
[14,15,15,11,0,14,12,9,14],
[8,14,13,16,12,0,9,9,15],
[18,17,15,19,14,17,0,10,14],
[16,17,13,18,17,17,16,0,16],
[14,16,14,13,12,11,12,10,0]])



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
result = np.append(np.array([9, 26, 51, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,13,16,12,11,18,8,8],
[15,0,12,16,16,7,15,9,11],
[13,14,0,18,18,16,17,16,11],
[10,10,8,0,12,6,7,2,5],
[14,10,8,14,0,10,10,7,10],
[15,19,10,20,16,0,23,15,13],
[8,11,9,19,16,3,0,10,8],
[18,17,10,24,19,11,16,0,14],
[18,15,15,21,16,13,18,12,0]])



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
result = np.append(np.array([9, 26, 52, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,22,12,16,14,15,16,18],
[12,0,17,16,12,13,16,14,15],
[4,9,0,5,11,7,10,11,16],
[14,10,21,0,15,12,16,17,20],
[10,14,15,11,0,11,13,15,12],
[12,13,19,14,15,0,15,20,18],
[11,10,16,10,13,11,0,12,19],
[10,12,15,9,11,6,14,0,19],
[8,11,10,6,14,8,7,7,0]])



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
result = np.append(np.array([9, 26, 53, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,11,17,10,16,17,21,24],
[11,0,18,11,14,20,15,19,20],
[15,8,0,15,18,18,15,23,24],
[9,15,11,0,9,16,16,21,21],
[16,12,8,17,0,12,13,21,20],
[10,6,8,10,14,0,9,9,13],
[9,11,11,10,13,17,0,13,18],
[5,7,3,5,5,17,13,0,17],
[2,6,2,5,6,13,8,9,0]])



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
result = np.append(np.array([9, 26, 54, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,13,19,13,15,14,15,15],
[10,0,12,9,13,9,12,8,11],
[13,14,0,14,13,16,15,13,14],
[7,17,12,0,9,13,13,11,11],
[13,13,13,17,0,15,16,11,13],
[11,17,10,13,11,0,13,14,13],
[12,14,11,13,10,13,0,12,16],
[11,18,13,15,15,12,14,0,13],
[11,15,12,15,13,13,10,13,0]])



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
result = np.append(np.array([9, 26, 55, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,17,11,11,12,15,15,17],
[12,0,11,9,8,9,9,9,8],
[9,15,0,15,12,8,15,16,10],
[15,17,11,0,17,11,17,13,13],
[15,18,14,9,0,10,14,16,13],
[14,17,18,15,16,0,15,12,16],
[11,17,11,9,12,11,0,14,13],
[11,17,10,13,10,14,12,0,13],
[9,18,16,13,13,10,13,13,0]])



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
result = np.append(np.array([9, 26, 56, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,7,11,9,11,14,5,11],
[11,0,8,8,9,9,9,9,16],
[19,18,0,15,11,14,17,13,15],
[15,18,11,0,14,8,18,14,10],
[17,17,15,12,0,11,16,12,16],
[15,17,12,18,15,0,19,12,14],
[12,17,9,8,10,7,0,12,14],
[21,17,13,12,14,14,14,0,14],
[15,10,11,16,10,12,12,12,0]])



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
result = np.append(np.array([9, 26, 57, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,15,8,12,14,21,13,11],
[13,0,16,11,13,19,23,19,20],
[11,10,0,8,11,17,17,12,14],
[18,15,18,0,13,21,20,15,19],
[14,13,15,13,0,19,19,19,15],
[12,7,9,5,7,0,14,12,10],
[5,3,9,6,7,12,0,8,8],
[13,7,14,11,7,14,18,0,17],
[15,6,12,7,11,16,18,9,0]])



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
result = np.append(np.array([9, 26, 58, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,13,14,11,16,10,11,10],
[15,0,17,16,13,14,12,13,15],
[13,9,0,15,11,13,11,11,12],
[12,10,11,0,8,15,12,11,15],
[15,13,15,18,0,18,16,17,15],
[10,12,13,11,8,0,11,8,13],
[16,14,15,14,10,15,0,13,15],
[15,13,15,15,9,18,13,0,14],
[16,11,14,11,11,13,11,12,0]])



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
result = np.append(np.array([9, 26, 59, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,10,13,16,13,20,13],
[13,0,3,10,6,16,6,13,3],
[13,23,0,23,26,23,19,16,19],
[16,16,3,0,10,19,6,16,10],
[13,20,0,16,0,16,3,13,10],
[10,10,3,7,10,0,6,10,10],
[13,20,7,20,23,20,0,13,7],
[6,13,10,10,13,16,13,0,13],
[13,23,7,16,16,16,19,13,0]])



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
result = np.append(np.array([9, 26, 60, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,20,24,2,4,20,12,6],
[24,0,26,24,15,9,26,17,20],
[6,0,0,18,5,7,18,17,9],
[2,2,8,0,2,2,8,2,6],
[24,11,21,24,0,16,21,18,18],
[22,17,19,24,10,0,19,11,17],
[6,0,8,18,5,7,0,7,9],
[14,9,9,24,8,15,19,0,13],
[20,6,17,20,8,9,17,13,0]])



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
result = np.append(np.array([9, 26, 61, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,9,9,8,0,19,12,15],
[18,0,8,15,15,17,14,22,19],
[17,18,0,15,11,17,20,22,21],
[17,11,11,0,15,10,14,15,15],
[18,11,15,11,0,18,14,17,14],
[26,9,9,16,8,0,19,13,15],
[7,12,6,12,12,7,0,19,13],
[14,4,4,11,9,13,7,0,10],
[11,7,5,11,12,11,13,16,0]])



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
result = np.append(np.array([9, 26, 62, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,15,22,15,12,14,16,15],
[14,0,16,19,12,13,11,13,18],
[11,10,0,13,9,12,11,11,16],
[4,7,13,0,8,6,7,11,13],
[11,14,17,18,0,11,13,14,16],
[14,13,14,20,15,0,14,15,15],
[12,15,15,19,13,12,0,16,17],
[10,13,15,15,12,11,10,0,13],
[11,8,10,13,10,11,9,13,0]])



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
result = np.append(np.array([9, 26, 63, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,11,10,12,6,10,11,12],
[17,0,17,15,16,16,11,19,20],
[15,9,0,17,18,9,9,18,17],
[16,11,9,0,15,12,12,16,11],
[14,10,8,11,0,11,10,14,14],
[20,10,17,14,15,0,13,20,14],
[16,15,17,14,16,13,0,20,17],
[15,7,8,10,12,6,6,0,13],
[14,6,9,15,12,12,9,13,0]])



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
result = np.append(np.array([9, 26, 64, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,11,18,13,19,20,11,13],
[13,0,9,5,3,14,11,15,2],
[15,17,0,15,10,16,11,16,4],
[8,21,11,0,8,19,12,16,8],
[13,23,16,18,0,17,14,21,9],
[7,12,10,7,9,0,7,13,2],
[6,15,15,14,12,19,0,13,9],
[15,11,10,10,5,13,13,0,5],
[13,24,22,18,17,24,17,21,0]])



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
result = np.append(np.array([9, 26, 65, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,10,12,11,13,8,7,9],
[18,0,13,14,14,16,14,7,6],
[16,13,0,13,7,9,9,7,11],
[14,12,13,0,8,15,8,6,5],
[15,12,19,18,0,14,13,13,17],
[13,10,17,11,12,0,16,6,11],
[18,12,17,18,13,10,0,8,15],
[19,19,19,20,13,20,18,0,18],
[17,20,15,21,9,15,11,8,0]])



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
result = np.append(np.array([9, 26, 66, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,14,8,12,13,8,8,11],
[18,0,13,13,13,16,12,13,12],
[12,13,0,10,14,9,10,12,11],
[18,13,16,0,12,13,13,11,13],
[14,13,12,14,0,11,13,13,15],
[13,10,17,13,15,0,10,13,12],
[18,14,16,13,13,16,0,12,12],
[18,13,14,15,13,13,14,0,15],
[15,14,15,13,11,14,14,11,0]])



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
result = np.append(np.array([9, 26, 67, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,16,12,14,23,16,12,14],
[9,0,7,7,8,12,13,6,9],
[10,19,0,12,8,17,19,14,13],
[14,19,14,0,10,19,16,13,11],
[12,18,18,16,0,22,18,15,19],
[3,14,9,7,4,0,13,5,6],
[10,13,7,10,8,13,0,9,7],
[14,20,12,13,11,21,17,0,8],
[12,17,13,15,7,20,19,18,0]])



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
result = np.append(np.array([9, 26, 68, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,9,10,13,13,4,10,9],
[15,0,12,12,10,15,13,11,21],
[17,14,0,15,17,12,9,14,15],
[16,14,11,0,12,15,14,13,16],
[13,16,9,14,0,12,14,11,17],
[13,11,14,11,14,0,9,12,14],
[22,13,17,12,12,17,0,10,18],
[16,15,12,13,15,14,16,0,16],
[17,5,11,10,9,12,8,10,0]])



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
result = np.append(np.array([9, 26, 69, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,14,14,17,13,16,10,16],
[17,0,13,15,20,20,19,15,20],
[12,13,0,12,15,17,17,14,18],
[12,11,14,0,17,12,14,15,15],
[9,6,11,9,0,13,14,13,15],
[13,6,9,14,13,0,13,11,14],
[10,7,9,12,12,13,0,11,17],
[16,11,12,11,13,15,15,0,19],
[10,6,8,11,11,12,9,7,0]])



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
result = np.append(np.array([9, 26, 70, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,12,11,10,9,9,15,11],
[12,0,13,9,16,9,8,15,11],
[14,13,0,8,11,7,8,13,8],
[15,17,18,0,16,11,12,15,12],
[16,10,15,10,0,10,7,16,11],
[17,17,19,15,16,0,9,21,13],
[17,18,18,14,19,17,0,17,13],
[11,11,13,11,10,5,9,0,7],
[15,15,18,14,15,13,13,19,0]])



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
result = np.append(np.array([9, 26, 71, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,16,14,11,11,11,13,10],
[12,0,13,15,8,9,10,13,6],
[10,13,0,15,10,10,8,12,7],
[12,11,11,0,9,10,9,11,6],
[15,18,16,17,0,14,10,13,8],
[15,17,16,16,12,0,12,16,7],
[15,16,18,17,16,14,0,16,13],
[13,13,14,15,13,10,10,0,8],
[16,20,19,20,18,19,13,18,0]])



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
result = np.append(np.array([9, 26, 72, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,15,12,10,7,13,14,12],
[10,0,19,12,9,13,10,11,7],
[11,7,0,9,8,14,11,10,8],
[14,14,17,0,6,18,17,16,15],
[16,17,18,20,0,16,15,12,16],
[19,13,12,8,10,0,15,14,12],
[13,16,15,9,11,11,0,15,12],
[12,15,16,10,14,12,11,0,10],
[14,19,18,11,10,14,14,16,0]])



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
result = np.append(np.array([9, 26, 73, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,11,11,6,8,20,7,14],
[12,0,10,8,7,10,11,7,12],
[15,16,0,16,14,16,20,10,17],
[15,18,10,0,10,13,17,12,18],
[20,19,12,16,0,13,19,17,13],
[18,16,10,13,13,0,21,12,13],
[6,15,6,9,7,5,0,5,9],
[19,19,16,14,9,14,21,0,15],
[12,14,9,8,13,13,17,11,0]])



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
result = np.append(np.array([9, 26, 74, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,13,16,13,11,9,13,14],
[12,0,10,12,16,8,11,6,9],
[13,16,0,15,12,10,11,13,12],
[10,14,11,0,12,9,11,9,10],
[13,10,14,14,0,11,9,11,10],
[15,18,16,17,15,0,9,16,17],
[17,15,15,15,17,17,0,13,15],
[13,20,13,17,15,10,13,0,11],
[12,17,14,16,16,9,11,15,0]])



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
result = np.append(np.array([9, 26, 75, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,11,8,10,11,10,12,11],
[12,0,7,9,14,9,8,7,12],
[15,19,0,16,16,17,15,13,14],
[18,17,10,0,12,15,12,12,19],
[16,12,10,14,0,14,9,13,18],
[15,17,9,11,12,0,11,12,11],
[16,18,11,14,17,15,0,11,15],
[14,19,13,14,13,14,15,0,14],
[15,14,12,7,8,15,11,12,0]])



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
result = np.append(np.array([9, 26, 76, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,11,15,11,13,15,12,13],
[11,0,13,14,14,13,15,9,15],
[15,13,0,13,18,12,17,15,16],
[11,12,13,0,14,10,13,12,12],
[15,12,8,12,0,14,15,12,11],
[13,13,14,16,12,0,16,15,19],
[11,11,9,13,11,10,0,11,16],
[14,17,11,14,14,11,15,0,17],
[13,11,10,14,15,7,10,9,0]])



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
result = np.append(np.array([9, 26, 77, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,11,10,10,9,9,14,9],
[19,0,17,18,15,11,14,20,13],
[15,9,0,11,14,12,12,16,10],
[16,8,15,0,16,10,11,15,9],
[16,11,12,10,0,11,9,16,13],
[17,15,14,16,15,0,13,16,12],
[17,12,14,15,17,13,0,16,11],
[12,6,10,11,10,10,10,0,11],
[17,13,16,17,13,14,15,15,0]])



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
result = np.append(np.array([9, 26, 78, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,10,18,7,14,17,11,11],
[11,0,14,11,7,12,10,12,13],
[16,12,0,18,13,16,12,12,8],
[8,15,8,0,8,13,12,12,8],
[19,19,13,18,0,19,13,21,14],
[12,14,10,13,7,0,8,12,7],
[9,16,14,14,13,18,0,15,9],
[15,14,14,14,5,14,11,0,7],
[15,13,18,18,12,19,17,19,0]])



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
result = np.append(np.array([9, 26, 79, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,15,16,14,12,17,12,11],
[12,0,12,14,14,10,14,13,12],
[11,14,0,17,11,11,16,10,12],
[10,12,9,0,12,8,14,8,9],
[12,12,15,14,0,12,14,12,12],
[14,16,15,18,14,0,17,10,12],
[9,12,10,12,12,9,0,9,11],
[14,13,16,18,14,16,17,0,15],
[15,14,14,17,14,14,15,11,0]])



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
result = np.append(np.array([9, 26, 80, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,10,15,15,17,12,15,13],
[12,0,12,13,16,17,16,16,16],
[16,14,0,13,19,16,12,16,14],
[11,13,13,0,15,20,14,14,13],
[11,10,7,11,0,8,11,10,9],
[9,9,10,6,18,0,11,13,13],
[14,10,14,12,15,15,0,14,11],
[11,10,10,12,16,13,12,0,15],
[13,10,12,13,17,13,15,11,0]])



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
result = np.append(np.array([9, 26, 81, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,17,20,21,13,20,20,14],
[11,0,16,23,19,16,17,21,14],
[9,10,0,14,18,12,15,20,12],
[6,3,12,0,13,4,10,14,4],
[5,7,8,13,0,7,6,15,7],
[13,10,14,22,19,0,17,20,10],
[6,9,11,16,20,9,0,18,12],
[6,5,6,12,11,6,8,0,4],
[12,12,14,22,19,16,14,22,0]])



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
result = np.append(np.array([9, 26, 82, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,17,15,15,15,16,15,18],
[16,0,15,13,14,10,15,10,18],
[9,11,0,9,11,8,11,8,10],
[11,13,17,0,18,12,16,14,13],
[11,12,15,8,0,10,19,11,11],
[11,16,18,14,16,0,16,19,14],
[10,11,15,10,7,10,0,11,13],
[11,16,18,12,15,7,15,0,14],
[8,8,16,13,15,12,13,12,0]])



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
result = np.append(np.array([9, 26, 83, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,16,13,13,19,15,17,12],
[7,0,13,10,12,12,12,13,10],
[10,13,0,8,11,14,14,16,10],
[13,16,18,0,14,17,16,21,17],
[13,14,15,12,0,17,12,17,13],
[7,14,12,9,9,0,11,16,13],
[11,14,12,10,14,15,0,19,12],
[9,13,10,5,9,10,7,0,12],
[14,16,16,9,13,13,14,14,0]])



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
result = np.append(np.array([9, 26, 84, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,8,3,1,4,9,12,8],
[22,0,16,11,9,16,16,11,8],
[18,10,0,9,10,21,18,21,12],
[23,15,17,0,10,17,23,21,18],
[25,17,16,16,0,16,25,11,8],
[22,10,5,9,10,0,23,18,14],
[17,10,8,3,1,3,0,11,8],
[14,15,5,5,15,8,15,0,5],
[18,18,14,8,18,12,18,21,0]])



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
result = np.append(np.array([9, 26, 85, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,14,18,16,15,9,13,14],
[13,0,10,11,16,12,12,11,12],
[12,16,0,13,18,15,15,16,16],
[8,15,13,0,16,12,12,13,12],
[10,10,8,10,0,12,7,10,8],
[11,14,11,14,14,0,11,12,11],
[17,14,11,14,19,15,0,16,17],
[13,15,10,13,16,14,10,0,12],
[12,14,10,14,18,15,9,14,0]])



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
result = np.append(np.array([9, 26, 86, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,13,17,15,17,19,12,10],
[12,0,10,10,15,12,13,10,9],
[13,16,0,16,17,17,16,14,16],
[9,16,10,0,13,10,13,8,11],
[11,11,9,13,0,15,13,6,11],
[9,14,9,16,11,0,13,7,11],
[7,13,10,13,13,13,0,10,13],
[14,16,12,18,20,19,16,0,19],
[16,17,10,15,15,15,13,7,0]])



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
result = np.append(np.array([9, 26, 87, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,19,18,14,10,22,15,14],
[9,0,8,7,6,10,14,11,11],
[7,18,0,17,10,9,14,14,11],
[8,19,9,0,9,10,14,11,15],
[12,20,16,17,0,10,18,12,13],
[16,16,17,16,16,0,19,13,18],
[4,12,12,12,8,7,0,10,9],
[11,15,12,15,14,13,16,0,13],
[12,15,15,11,13,8,17,13,0]])



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
result = np.append(np.array([9, 26, 88, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,21,13,14,19,21,18,19],
[18,0,18,11,18,19,18,18,11],
[5,8,0,5,8,13,14,5,13],
[13,15,21,0,21,21,21,18,26],
[12,8,18,5,0,13,21,18,19],
[7,7,13,5,13,0,13,18,11],
[5,8,12,5,5,13,0,12,5],
[8,8,21,8,8,8,14,0,13],
[7,15,13,0,7,15,21,13,0]])



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
result = np.append(np.array([9, 26, 89, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,17,16,22,14,22,13,17],
[16,0,19,19,22,13,22,10,13],
[9,7,0,18,12,9,18,3,6],
[10,7,8,0,13,5,19,4,11],
[4,4,14,13,0,8,23,11,7],
[12,13,17,21,18,0,16,4,9],
[4,4,8,7,3,10,0,4,7],
[13,16,23,22,15,22,22,0,16],
[9,13,20,15,19,17,19,10,0]])



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
result = np.append(np.array([9, 26, 90, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,23,10,24,18,23,14,10],
[12,0,14,5,16,11,20,12,6],
[3,12,0,6,6,7,13,6,10],
[16,21,20,0,22,22,21,12,14],
[2,10,20,4,0,17,20,13,5],
[8,15,19,4,9,0,11,5,6],
[3,6,13,5,6,15,0,5,7],
[12,14,20,14,13,21,21,0,13],
[16,20,16,12,21,20,19,13,0]])



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
result = np.append(np.array([9, 26, 91, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,7,6,13,21,18,11,14],
[16,0,15,13,12,13,14,16,16],
[19,11,0,4,15,22,18,14,16],
[20,13,22,0,14,24,23,20,19],
[13,14,11,12,0,13,14,14,16],
[5,13,4,2,13,0,18,9,14],
[8,12,8,3,12,8,0,5,9],
[15,10,12,6,12,17,21,0,9],
[12,10,10,7,10,12,17,17,0]])



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
result = np.append(np.array([9, 26, 92, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,18,20,16,14,13,15,15],
[16,0,18,17,17,13,14,17,15],
[8,8,0,10,11,12,15,13,12],
[6,9,16,0,12,13,11,11,11],
[10,9,15,14,0,15,14,12,13],
[12,13,14,13,11,0,10,13,15],
[13,12,11,15,12,16,0,15,16],
[11,9,13,15,14,13,11,0,14],
[11,11,14,15,13,11,10,12,0]])



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
result = np.append(np.array([9, 26, 93, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,8,19,8,3,11,3,8],
[21,0,21,21,11,11,11,19,13],
[18,5,0,16,8,11,11,0,8],
[7,5,10,0,8,8,11,3,8],
[18,15,18,18,0,8,8,16,10],
[23,15,15,18,18,0,10,8,7],
[15,15,15,15,18,16,0,8,7],
[23,7,26,23,10,18,18,0,18],
[18,13,18,18,16,19,19,8,0]])



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
result = np.append(np.array([9, 26, 94, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,9,12,7,10,14,10,10],
[16,0,11,15,8,16,14,14,14],
[17,15,0,20,13,11,7,7,14],
[14,11,6,0,7,11,11,7,7],
[19,18,13,19,0,18,18,14,14],
[16,10,15,15,8,0,13,9,12],
[12,12,19,15,8,13,0,11,16],
[16,12,19,19,12,17,15,0,18],
[16,12,12,19,12,14,10,8,0]])



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
result = np.append(np.array([9, 26, 95, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,11,11,14,11,9,11],
[16,0,13,11,17,16,13,14,17],
[16,13,0,14,17,19,16,16,18],
[15,15,12,0,17,19,11,16,18],
[15,9,9,9,0,14,11,7,14],
[12,10,7,7,12,0,9,10,11],
[15,13,10,15,15,17,0,13,17],
[17,12,10,10,19,16,13,0,15],
[15,9,8,8,12,15,9,11,0]])



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
result = np.append(np.array([9, 26, 96, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1,1,12,12,0,2,12,1],
[25,0,3,15,14,1,13,12,12],
[25,23,0,12,14,1,13,12,12],
[14,11,14,0,13,12,13,23,12],
[14,12,12,13,0,1,13,12,12],
[26,25,25,14,25,0,15,23,13],
[24,13,13,13,13,11,0,12,11],
[14,14,14,3,14,3,14,0,12],
[25,14,14,14,14,13,15,14,0]])



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
result = np.append(np.array([9, 26, 97, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,11,15,14,14,15,20,15],
[11,0,11,17,13,14,10,17,19],
[15,15,0,14,13,13,12,19,14],
[11,9,12,0,12,15,10,15,17],
[12,13,13,14,0,16,14,20,16],
[12,12,13,11,10,0,14,20,16],
[11,16,14,16,12,12,0,19,18],
[6,9,7,11,6,6,7,0,9],
[11,7,12,9,10,10,8,17,0]])



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
result = np.append(np.array([9, 26, 98, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,17,9,10,12,8,15,9],
[20,0,11,15,10,18,13,14,22],
[9,15,0,13,12,12,12,12,15],
[17,11,13,0,9,12,10,13,16],
[16,16,14,17,0,17,7,17,19],
[14,8,14,14,9,0,10,14,11],
[18,13,14,16,19,16,0,21,15],
[11,12,14,13,9,12,5,0,16],
[17,4,11,10,7,15,11,10,0]])



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
result = np.append(np.array([9, 26, 99, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,13,11,11,15,17,17,16],
[14,0,17,14,11,14,20,15,10],
[13,9,0,10,10,9,10,13,7],
[15,12,16,0,11,15,12,12,12],
[15,15,16,15,0,11,12,11,13],
[11,12,17,11,15,0,15,10,10],
[9,6,16,14,14,11,0,13,8],
[9,11,13,14,15,16,13,0,12],
[10,16,19,14,13,16,18,14,0]])



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
result = np.append(np.array([9, 26, 100, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,12,14,14,12,13,15,16],
[12,0,7,10,22,14,13,11,12],
[14,19,0,15,19,10,17,10,18],
[12,16,11,0,20,16,16,14,17],
[12,4,7,6,0,6,6,8,7],
[14,12,16,10,20,0,13,12,11],
[13,13,9,10,20,13,0,15,13],
[11,15,16,12,18,14,11,0,21],
[10,14,8,9,19,15,13,5,0]])



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
result = np.append(np.array([9, 26, 101, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,12,16,14,20,16,13,15],
[11,0,15,12,12,19,14,9,12],
[14,11,0,12,13,19,12,11,14],
[10,14,14,0,12,18,11,10,15],
[12,14,13,14,0,17,13,11,14],
[6,7,7,8,9,0,10,8,9],
[10,12,14,15,13,16,0,11,16],
[13,17,15,16,15,18,15,0,15],
[11,14,12,11,12,17,10,11,0]])



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
result = np.append(np.array([9, 26, 102, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,9,20,12,9,23,15,23],
[14,0,4,17,12,9,23,13,21],
[17,22,0,20,12,5,19,15,17],
[6,9,6,0,2,6,13,16,13],
[14,14,14,24,0,6,13,17,11],
[17,17,21,20,20,0,23,13,21],
[3,3,7,13,13,3,0,6,14],
[11,13,11,10,9,13,20,0,18],
[3,5,9,13,15,5,12,8,0]])



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
result = np.append(np.array([9, 26, 103, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,2,16,11,3,13,7,13],
[9,0,1,11,7,5,6,6,12],
[24,25,0,20,19,13,25,16,17],
[10,15,6,0,6,7,13,8,4],
[15,19,7,20,0,10,17,17,14],
[23,21,13,19,16,0,17,15,15],
[13,20,1,13,9,9,0,9,11],
[19,20,10,18,9,11,17,0,17],
[13,14,9,22,12,11,15,9,0]])



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
result = np.append(np.array([9, 26, 104, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,12,9,15,14,11,14,11],
[15,0,10,9,16,12,12,11,13],
[14,16,0,13,19,13,17,16,11],
[17,17,13,0,16,17,18,14,16],
[11,10,7,10,0,11,10,9,10],
[12,14,13,9,15,0,14,14,12],
[15,14,9,8,16,12,0,13,11],
[12,15,10,12,17,12,13,0,11],
[15,13,15,10,16,14,15,15,0]])



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
result = np.append(np.array([9, 26, 105, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,13,12,15,14,11,11,10],
[15,0,13,13,18,16,16,13,11],
[13,13,0,12,15,9,13,13,10],
[14,13,14,0,19,13,13,13,10],
[11,8,11,7,0,11,17,12,4],
[12,10,17,13,15,0,17,16,13],
[15,10,13,13,9,9,0,13,12],
[15,13,13,13,14,10,13,0,13],
[16,15,16,16,22,13,14,13,0]])



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
result = np.append(np.array([9, 26, 106, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,17,13,14,18,17,16,13],
[13,0,14,12,10,13,14,16,11],
[9,12,0,8,6,11,12,13,8],
[13,14,18,0,15,15,18,18,7],
[12,16,20,11,0,17,14,17,10],
[8,13,15,11,9,0,14,14,9],
[9,12,14,8,12,12,0,15,8],
[10,10,13,8,9,12,11,0,5],
[13,15,18,19,16,17,18,21,0]])



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
result = np.append(np.array([9, 26, 107, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,13,13,14,14,13,12,10],
[18,0,16,11,16,16,16,14,14],
[13,10,0,18,15,14,16,16,13],
[13,15,8,0,12,11,16,13,10],
[12,10,11,14,0,14,13,12,9],
[12,10,12,15,12,0,14,15,10],
[13,10,10,10,13,12,0,13,10],
[14,12,10,13,14,11,13,0,8],
[16,12,13,16,17,16,16,18,0]])



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
result = np.append(np.array([9, 26, 108, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,9,15,16,10,11,9,14],
[20,0,12,18,17,18,14,14,17],
[17,14,0,15,16,12,13,13,16],
[11,8,11,0,16,9,10,6,11],
[10,9,10,10,0,11,10,10,8],
[16,8,14,17,15,0,13,11,16],
[15,12,13,16,16,13,0,9,13],
[17,12,13,20,16,15,17,0,19],
[12,9,10,15,18,10,13,7,0]])



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
result = np.append(np.array([9, 26, 109, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,13,15,11,4,7,12,7],
[15,0,8,11,14,11,10,14,14],
[13,18,0,18,14,10,14,19,15],
[11,15,8,0,7,7,14,15,11],
[15,12,12,19,0,11,9,12,7],
[22,15,16,19,15,0,18,12,12],
[19,16,12,12,17,8,0,11,14],
[14,12,7,11,14,14,15,0,9],
[19,12,11,15,19,14,12,17,0]])



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
result = np.append(np.array([9, 26, 110, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,12,15,13,14,15,12,14],
[13,0,16,17,15,13,10,14,15],
[14,10,0,17,17,16,11,11,16],
[11,9,9,0,11,11,9,10,9],
[13,11,9,15,0,14,10,10,12],
[12,13,10,15,12,0,12,16,13],
[11,16,15,17,16,14,0,15,14],
[14,12,15,16,16,10,11,0,13],
[12,11,10,17,14,13,12,13,0]])



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
result = np.append(np.array([9, 26, 111, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,4,9,8,15,10,10,9],
[19,0,11,11,9,9,15,7,16],
[22,15,0,13,6,18,15,8,16],
[17,15,13,0,14,18,14,12,17],
[18,17,20,12,0,20,16,14,17],
[11,17,8,8,6,0,13,6,8],
[16,11,11,12,10,13,0,12,12],
[16,19,18,14,12,20,14,0,19],
[17,10,10,9,9,18,14,7,0]])



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
result = np.append(np.array([9, 26, 112, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,17,26,17,26,19,12,17],
[7,0,12,26,5,26,19,19,5],
[9,14,0,26,2,26,21,14,19],
[0,0,0,0,0,5,12,0,5],
[9,21,24,26,0,26,21,21,26],
[0,0,0,21,0,0,19,12,5],
[7,7,5,14,5,7,0,7,5],
[14,7,12,26,5,14,19,0,5],
[9,21,7,21,0,21,21,21,0]])



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
result = np.append(np.array([9, 26, 113, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,18,17,16,15,17,12,10],
[14,0,11,11,15,12,17,9,13],
[8,15,0,13,17,20,16,12,10],
[9,15,13,0,13,14,14,12,11],
[10,11,9,13,0,11,16,9,7],
[11,14,6,12,15,0,11,6,8],
[9,9,10,12,10,15,0,9,7],
[14,17,14,14,17,20,17,0,10],
[16,13,16,15,19,18,19,16,0]])



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
result = np.append(np.array([9, 26, 114, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,15,21,15,7,6,7],
[13,0,12,21,21,15,8,8,15],
[13,14,0,26,20,20,8,13,20],
[11,5,0,0,15,6,6,0,5],
[5,5,6,11,0,5,0,0,5],
[11,11,6,20,21,0,6,6,12],
[19,18,18,20,26,20,0,11,12],
[20,18,13,26,26,20,15,0,12],
[19,11,6,21,21,14,14,14,0]])



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
result = np.append(np.array([9, 26, 115, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,10,9,9,10,11,10,13],
[14,0,11,16,10,8,13,10,12],
[16,15,0,15,9,5,9,9,14],
[17,10,11,0,10,10,10,11,11],
[17,16,17,16,0,10,11,14,12],
[16,18,21,16,16,0,16,11,15],
[15,13,17,16,15,10,0,11,16],
[16,16,17,15,12,15,15,0,13],
[13,14,12,15,14,11,10,13,0]])



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
result = np.append(np.array([9, 26, 116, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,15,17,16,13,16,14,12],
[10,0,16,10,13,10,15,11,12],
[11,10,0,13,12,9,14,11,11],
[9,16,13,0,15,9,18,11,14],
[10,13,14,11,0,9,16,10,11],
[13,16,17,17,17,0,17,14,11],
[10,11,12,8,10,9,0,9,11],
[12,15,15,15,16,12,17,0,14],
[14,14,15,12,15,15,15,12,0]])



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
result = np.append(np.array([9, 26, 117, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,16,20,20,16,12,16,10],
[10,0,20,26,14,10,16,16,14],
[10,6,0,20,10,10,22,12,20],
[6,0,6,0,6,10,6,6,10],
[6,12,16,20,0,16,18,6,16],
[10,16,16,16,10,0,22,16,20],
[14,10,4,20,8,4,0,10,20],
[10,10,14,20,20,10,16,0,20],
[16,12,6,16,10,6,6,6,0]])



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
result = np.append(np.array([9, 26, 118, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,12,5,12,14,12,9,3],
[14,0,8,5,11,9,15,11,5],
[14,18,0,10,16,12,17,14,8],
[21,21,16,0,26,18,20,12,18],
[14,15,10,0,0,15,7,4,9],
[12,17,14,8,11,0,12,5,3],
[14,11,9,6,19,14,0,6,6],
[17,15,12,14,22,21,20,0,14],
[23,21,18,8,17,23,20,12,0]])



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
result = np.append(np.array([9, 26, 119, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,9,14,14,15,13,18,16],
[14,0,14,11,15,13,13,17,13],
[17,12,0,15,18,13,13,14,15],
[12,15,11,0,12,13,11,19,12],
[12,11,8,14,0,13,10,15,14],
[11,13,13,13,13,0,12,15,14],
[13,13,13,15,16,14,0,17,14],
[8,9,12,7,11,11,9,0,11],
[10,13,11,14,12,12,12,15,0]])



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
result = np.append(np.array([9, 26, 120, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,17,8,13,14,15,12,14],
[13,0,19,15,19,12,16,17,12],
[9,7,0,8,8,11,7,10,13],
[18,11,18,0,15,17,17,15,14],
[13,7,18,11,0,10,17,9,13],
[12,14,15,9,16,0,9,11,9],
[11,10,19,9,9,17,0,11,8],
[14,9,16,11,17,15,15,0,12],
[12,14,13,12,13,17,18,14,0]])



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
result = np.append(np.array([9, 26, 121, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,14,12,7,14,13,11,10],
[15,0,13,13,15,12,17,13,12],
[12,13,0,8,10,14,14,13,10],
[14,13,18,0,12,17,14,12,11],
[19,11,16,14,0,15,14,11,11],
[12,14,12,9,11,0,16,11,14],
[13,9,12,12,12,10,0,11,8],
[15,13,13,14,15,15,15,0,11],
[16,14,16,15,15,12,18,15,0]])



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
result = np.append(np.array([9, 26, 122, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,9,12,8,12,13,10,13],
[19,0,11,16,14,16,15,16,17],
[17,15,0,16,12,13,13,12,20],
[14,10,10,0,10,13,16,11,16],
[18,12,14,16,0,12,14,16,15],
[14,10,13,13,14,0,14,10,16],
[13,11,13,10,12,12,0,11,14],
[16,10,14,15,10,16,15,0,14],
[13,9,6,10,11,10,12,12,0]])



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
result = np.append(np.array([9, 26, 123, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,8,12,12,15,13,10,15],
[12,0,12,10,12,13,12,13,12],
[18,14,0,15,17,15,16,9,13],
[14,16,11,0,14,12,17,10,12],
[14,14,9,12,0,14,12,11,11],
[11,13,11,14,12,0,14,8,13],
[13,14,10,9,14,12,0,9,10],
[16,13,17,16,15,18,17,0,13],
[11,14,13,14,15,13,16,13,0]])



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
result = np.append(np.array([9, 26, 124, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,16,16,14,15,18,12,14],
[14,0,15,15,14,16,19,12,17],
[10,11,0,10,13,13,14,11,12],
[10,11,16,0,13,14,15,14,12],
[12,12,13,13,0,14,17,12,14],
[11,10,13,12,12,0,13,15,9],
[8,7,12,11,9,13,0,11,9],
[14,14,15,12,14,11,15,0,13],
[12,9,14,14,12,17,17,13,0]])



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
result = np.append(np.array([9, 26, 125, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,12,15,13,16,9,8,14],
[11,0,12,12,12,14,16,11,17],
[14,14,0,11,15,17,15,11,13],
[11,14,15,0,12,15,10,11,14],
[13,14,11,14,0,15,13,12,12],
[10,12,9,11,11,0,11,9,10],
[17,10,11,16,13,15,0,13,13],
[18,15,15,15,14,17,13,0,16],
[12,9,13,12,14,16,13,10,0]])



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
result = np.append(np.array([9, 26, 126, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,6,12,5,8,9,11,5],
[17,0,17,16,13,11,9,15,7],
[20,9,0,10,13,8,9,12,8],
[14,10,16,0,12,13,13,14,12],
[21,13,13,14,0,16,19,19,11],
[18,15,18,13,10,0,20,18,18],
[17,17,17,13,7,6,0,18,7],
[15,11,14,12,7,8,8,0,11],
[21,19,18,14,15,8,19,15,0]])



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
result = np.append(np.array([9, 26, 127, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,13,12,11,10,12,14,14],
[15,0,15,14,15,10,16,16,14],
[13,11,0,12,12,13,12,13,11],
[14,12,14,0,13,13,16,15,17],
[15,11,14,13,0,12,13,17,14],
[16,16,13,13,14,0,15,16,15],
[14,10,14,10,13,11,0,13,11],
[12,10,13,11,9,10,13,0,14],
[12,12,15,9,12,11,15,12,0]])



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
result = np.append(np.array([9, 26, 128, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,15,6,12,7,5,10,11],
[16,0,16,13,16,10,9,14,13],
[11,10,0,10,11,8,5,11,6],
[20,13,16,0,10,16,15,12,9],
[14,10,15,16,0,10,7,10,11],
[19,16,18,10,16,0,12,11,6],
[21,17,21,11,19,14,0,14,13],
[16,12,15,14,16,15,12,0,18],
[15,13,20,17,15,20,13,8,0]])



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
result = np.append(np.array([9, 26, 129, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,12,13,18,10,21,18],
[13,0,9,13,14,20,12,13,17],
[13,17,0,13,18,24,14,19,16],
[14,13,13,0,17,24,10,21,8],
[13,12,8,9,0,16,8,11,6],
[8,6,2,2,10,0,4,6,6],
[16,14,12,16,18,22,0,21,17],
[5,13,7,5,15,20,5,0,11],
[8,9,10,18,20,20,9,15,0]])



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
result = np.append(np.array([9, 26, 130, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,12,14,19,10,10,14,17],
[9,0,7,14,21,8,8,14,9],
[14,19,0,14,14,9,7,8,12],
[12,12,12,0,13,11,6,6,16],
[7,5,12,13,0,7,6,8,10],
[16,18,17,15,19,0,11,16,16],
[16,18,19,20,20,15,0,20,13],
[12,12,18,20,18,10,6,0,14],
[9,17,14,10,16,10,13,12,0]])



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
result = np.append(np.array([9, 26, 131, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,13,18,20,15,16,21,14],
[11,0,9,11,14,13,8,15,7],
[13,17,0,14,21,11,9,20,12],
[8,15,12,0,13,15,8,9,12],
[6,12,5,13,0,11,11,13,6],
[11,13,15,11,15,0,10,17,11],
[10,18,17,18,15,16,0,15,13],
[5,11,6,17,13,9,11,0,11],
[12,19,14,14,20,15,13,15,0]])



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
result = np.append(np.array([9, 26, 132, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,9,12,8,10,12,12,17],
[14,0,13,10,14,14,12,10,18],
[17,13,0,13,20,18,17,17,22],
[14,16,13,0,14,14,15,9,17],
[18,12,6,12,0,16,12,11,19],
[16,12,8,12,10,0,14,16,14],
[14,14,9,11,14,12,0,13,17],
[14,16,9,17,15,10,13,0,14],
[9,8,4,9,7,12,9,12,0]])



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
result = np.append(np.array([9, 26, 133, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,16,14,14,16,13,15,14],
[12,0,12,10,13,19,12,14,11],
[10,14,0,7,11,18,11,12,13],
[12,16,19,0,15,19,17,17,14],
[12,13,15,11,0,16,11,13,11],
[10,7,8,7,10,0,6,7,6],
[13,14,15,9,15,20,0,14,11],
[11,12,14,9,13,19,12,0,11],
[12,15,13,12,15,20,15,15,0]])



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
result = np.append(np.array([9, 26, 134, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,20,13,19,13,22,20,7],
[12,0,16,13,12,19,16,19,13],
[6,10,0,6,15,17,21,12,6],
[13,13,20,0,18,15,22,19,15],
[7,14,11,8,0,14,17,9,8],
[13,7,9,11,12,0,19,15,14],
[4,10,5,4,9,7,0,11,1],
[6,7,14,7,17,11,15,0,10],
[19,13,20,11,18,12,25,16,0]])



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
result = np.append(np.array([9, 26, 135, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,17,15,12,14,21,19,13],
[12,0,14,14,10,13,16,16,9],
[9,12,0,11,8,12,11,14,9],
[11,12,15,0,9,10,15,12,12],
[14,16,18,17,0,14,17,16,13],
[12,13,14,16,12,0,17,14,13],
[5,10,15,11,9,9,0,11,9],
[7,10,12,14,10,12,15,0,12],
[13,17,17,14,13,13,17,14,0]])



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
result = np.append(np.array([9, 26, 136, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,10,14,14,11,15,13,11],
[15,0,12,18,15,13,12,12,18],
[16,14,0,16,18,11,15,15,17],
[12,8,10,0,16,8,13,10,11],
[12,11,8,10,0,9,14,10,10],
[15,13,15,18,17,0,13,16,16],
[11,14,11,13,12,13,0,14,14],
[13,14,11,16,16,10,12,0,14],
[15,8,9,15,16,10,12,12,0]])



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
result = np.append(np.array([9, 26, 137, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,10,9,11,17,15,13],
[16,0,16,17,12,16,18,19,15],
[16,10,0,11,7,9,16,13,12],
[16,9,15,0,6,10,17,13,12],
[17,14,19,20,0,13,21,17,15],
[15,10,17,16,13,0,17,12,13],
[9,8,10,9,5,9,0,12,8],
[11,7,13,13,9,14,14,0,12],
[13,11,14,14,11,13,18,14,0]])



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
result = np.append(np.array([9, 26, 138, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,13,9,13,14,13,12,15],
[12,0,13,13,15,16,15,14,17],
[13,13,0,13,14,16,16,11,16],
[17,13,13,0,16,12,10,11,15],
[13,11,12,10,0,11,11,10,14],
[12,10,10,14,15,0,12,11,18],
[13,11,10,16,15,14,0,16,17],
[14,12,15,15,16,15,10,0,16],
[11,9,10,11,12,8,9,10,0]])



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
result = np.append(np.array([9, 26, 139, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,16,19,16,20,12,13,12],
[3,0,9,8,12,6,5,5,8],
[10,17,0,16,18,21,14,17,18],
[7,18,10,0,20,18,9,4,14],
[10,14,8,6,0,10,5,7,11],
[6,20,5,8,16,0,5,4,12],
[14,21,12,17,21,21,0,10,17],
[13,21,9,22,19,22,16,0,12],
[14,18,8,12,15,14,9,14,0]])



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
result = np.append(np.array([9, 26, 140, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,15,20,20,12,20,14,18],
[13,0,16,17,20,14,19,10,16],
[11,10,0,15,12,11,12,10,16],
[6,9,11,0,12,10,11,10,10],
[6,6,14,14,0,11,13,10,14],
[14,12,15,16,15,0,12,8,13],
[6,7,14,15,13,14,0,8,15],
[12,16,16,16,16,18,18,0,17],
[8,10,10,16,12,13,11,9,0]])



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
result = np.append(np.array([9, 26, 141, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,14,12,11,12,12,12,13],
[14,0,18,15,10,12,15,17,10],
[12,8,0,9,11,12,12,10,11],
[14,11,17,0,13,17,15,16,14],
[15,16,15,13,0,14,14,14,13],
[14,14,14,9,12,0,14,13,10],
[14,11,14,11,12,12,0,14,13],
[14,9,16,10,12,13,12,0,9],
[13,16,15,12,13,16,13,17,0]])



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
result = np.append(np.array([9, 26, 142, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,15,10,14,13,18,14,12],
[13,0,13,13,16,16,17,15,12],
[11,13,0,7,12,13,16,14,11],
[16,13,19,0,14,16,16,15,15],
[12,10,14,12,0,13,13,12,12],
[13,10,13,10,13,0,17,14,10],
[8,9,10,10,13,9,0,14,12],
[12,11,12,11,14,12,12,0,13],
[14,14,15,11,14,16,14,13,0]])



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
result = np.append(np.array([9, 26, 143, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,12,16,9,15,7,8,11],
[14,0,11,15,12,12,11,12,11],
[14,15,0,16,19,19,16,17,10],
[10,11,10,0,12,12,12,10,9],
[17,14,7,14,0,11,15,14,12],
[11,14,7,14,15,0,9,14,10],
[19,15,10,14,11,17,0,16,15],
[18,14,9,16,12,12,10,0,11],
[15,15,16,17,14,16,11,15,0]])



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
result = np.append(np.array([9, 26, 144, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,10,11,10,13,16,11,11],
[14,0,10,14,15,9,17,11,14],
[16,16,0,15,13,15,15,16,18],
[15,12,11,0,12,11,13,11,16],
[16,11,13,14,0,14,12,13,14],
[13,17,11,15,12,0,13,11,16],
[10,9,11,13,14,13,0,12,14],
[15,15,10,15,13,15,14,0,16],
[15,12,8,10,12,10,12,10,0]])



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
result = np.append(np.array([9, 26, 145, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,11,11,11,13,17,11,10],
[19,0,15,14,16,18,17,13,15],
[15,11,0,14,14,16,16,13,12],
[15,12,12,0,13,17,19,14,12],
[15,10,12,13,0,14,15,15,13],
[13,8,10,9,12,0,13,12,7],
[9,9,10,7,11,13,0,12,12],
[15,13,13,12,11,14,14,0,10],
[16,11,14,14,13,19,14,16,0]])



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
result = np.append(np.array([9, 26, 146, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,17,21,13,17,20,18,20],
[9,0,15,17,11,10,12,14,17],
[9,11,0,19,8,18,18,22,15],
[5,9,7,0,4,11,13,14,10],
[13,15,18,22,0,16,15,19,10],
[9,16,8,15,10,0,10,12,18],
[6,14,8,13,11,16,0,13,11],
[8,12,4,12,7,14,13,0,12],
[6,9,11,16,16,8,15,14,0]])



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
result = np.append(np.array([9, 26, 147, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,15,13,14,14,17,11,12],
[13,0,14,15,12,15,16,12,16],
[11,12,0,11,8,11,10,12,12],
[13,11,15,0,11,14,17,13,14],
[12,14,18,15,0,13,15,13,17],
[12,11,15,12,13,0,13,9,12],
[9,10,16,9,11,13,0,9,10],
[15,14,14,13,13,17,17,0,12],
[14,10,14,12,9,14,16,14,0]])



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
result = np.append(np.array([9, 26, 148, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,13,13,16,15,11,15,14],
[11,0,11,9,11,15,8,16,18],
[13,15,0,16,14,11,8,15,15],
[13,17,10,0,14,15,13,16,13],
[10,15,12,12,0,16,13,18,15],
[11,11,15,11,10,0,6,11,14],
[15,18,18,13,13,20,0,16,15],
[11,10,11,10,8,15,10,0,15],
[12,8,11,13,11,12,11,11,0]])



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
result = np.append(np.array([9, 26, 149, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,7,12,12,7,12,13,11],
[14,0,12,13,14,11,13,13,17],
[19,14,0,14,15,10,14,14,17],
[14,13,12,0,11,8,12,7,16],
[14,12,11,15,0,13,12,11,14],
[19,15,16,18,13,0,15,12,17],
[14,13,12,14,14,11,0,13,14],
[13,13,12,19,15,14,13,0,16],
[15,9,9,10,12,9,12,10,0]])



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
result = np.append(np.array([9, 26, 150, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,14,15,14,15,18,13,16],
[16,0,11,16,15,19,14,16,17],
[12,15,0,16,15,15,21,14,18],
[11,10,10,0,11,11,11,13,14],
[12,11,11,15,0,13,13,10,13],
[11,7,11,15,13,0,14,11,17],
[8,12,5,15,13,12,0,11,13],
[13,10,12,13,16,15,15,0,13],
[10,9,8,12,13,9,13,13,0]])



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
result = np.append(np.array([9, 26, 151, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,11,12,12,10,12,13,9],
[14,0,12,15,12,13,12,13,13],
[15,14,0,13,17,15,14,14,13],
[14,11,13,0,12,13,12,12,13],
[14,14,9,14,0,10,11,14,11],
[16,13,11,13,16,0,15,14,13],
[14,14,12,14,15,11,0,17,13],
[13,13,12,14,12,12,9,0,9],
[17,13,13,13,15,13,13,17,0]])



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
result = np.append(np.array([9, 26, 152, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,22,22,13,26,9,9,22],
[13,0,22,13,26,22,13,13,22],
[4,4,0,4,13,13,4,4,13],
[4,13,22,0,13,13,0,4,13],
[13,0,13,13,0,13,0,0,13],
[0,4,13,13,13,0,0,0,9],
[17,13,22,26,26,26,0,4,26],
[17,13,22,22,26,26,22,0,26],
[4,4,13,13,13,17,0,0,0]])



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
result = np.append(np.array([9, 26, 153, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,16,16,13,13,13,12,15],
[8,0,12,18,16,12,12,8,13],
[10,14,0,13,14,11,15,13,17],
[10,8,13,0,15,11,15,11,15],
[13,10,12,11,0,14,9,10,14],
[13,14,15,15,12,0,8,12,17],
[13,14,11,11,17,18,0,9,14],
[14,18,13,15,16,14,17,0,18],
[11,13,9,11,12,9,12,8,0]])



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
result = np.append(np.array([9, 26, 154, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,14,17,12,19,15,21,16],
[9,0,12,12,7,10,9,9,10],
[12,14,0,10,4,14,12,13,16],
[9,14,16,0,13,14,11,12,19],
[14,19,22,13,0,20,17,14,23],
[7,16,12,12,6,0,9,12,17],
[11,17,14,15,9,17,0,14,16],
[5,17,13,14,12,14,12,0,21],
[10,16,10,7,3,9,10,5,0]])



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
result = np.append(np.array([9, 26, 155, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,11,15,9,12,5,12,11],
[11,0,12,15,9,16,6,16,15],
[15,14,0,19,14,15,14,10,14],
[11,11,7,0,1,17,1,7,1],
[17,17,12,25,0,22,7,12,12],
[14,10,11,9,4,0,0,10,9],
[21,20,12,25,19,26,0,16,25],
[14,10,16,19,14,16,10,0,14],
[15,11,12,25,14,17,1,12,0]])



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
result = np.append(np.array([9, 26, 156, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,18,16,18,16,18,13,13],
[11,0,11,13,17,12,16,12,14],
[8,15,0,14,10,9,16,9,8],
[10,13,12,0,14,9,17,9,10],
[8,9,16,12,0,9,10,11,12],
[10,14,17,17,17,0,15,12,11],
[8,10,10,9,16,11,0,9,8],
[13,14,17,17,15,14,17,0,7],
[13,12,18,16,14,15,18,19,0]])



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
result = np.append(np.array([9, 26, 157, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,18,14,16,22,8,10,15],
[6,0,20,7,17,22,10,10,15],
[8,6,0,7,11,16,9,6,9],
[12,19,19,0,18,25,12,9,14],
[10,9,15,8,0,19,8,8,10],
[4,4,10,1,7,0,4,4,10],
[18,16,17,14,18,22,0,13,15],
[16,16,20,17,18,22,13,0,12],
[11,11,17,12,16,16,11,14,0]])



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
result = np.append(np.array([9, 26, 158, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,14,11,17,16,16,13,13],
[15,0,12,13,17,18,15,11,13],
[12,14,0,10,13,20,16,12,14],
[15,13,16,0,16,18,19,14,15],
[9,9,13,10,0,13,15,10,16],
[10,8,6,8,13,0,16,10,12],
[10,11,10,7,11,10,0,9,8],
[13,15,14,12,16,16,17,0,15],
[13,13,12,11,10,14,18,11,0]])



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
result = np.append(np.array([9, 26, 159, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,8,14,11,11,4,6,5],
[17,0,11,10,18,22,16,14,19],
[18,15,0,8,17,19,14,14,17],
[12,16,18,0,15,16,14,15,14],
[15,8,9,11,0,6,16,7,10],
[15,4,7,10,20,0,16,16,15],
[22,10,12,12,10,10,0,15,14],
[20,12,12,11,19,10,11,0,17],
[21,7,9,12,16,11,12,9,0]])



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
result = np.append(np.array([9, 26, 160, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,13,11,10,13,6,12,8],
[15,0,14,13,15,18,14,19,15],
[13,12,0,16,20,13,8,16,14],
[15,13,10,0,13,16,14,19,15],
[16,11,6,13,0,17,10,15,15],
[13,8,13,10,9,0,11,17,5],
[20,12,18,12,16,15,0,13,13],
[14,7,10,7,11,9,13,0,7],
[18,11,12,11,11,21,13,19,0]])



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
result = np.append(np.array([9, 26, 161, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,14,16,17,11,12,14,6],
[16,0,14,13,15,15,10,15,9],
[12,12,0,12,15,8,7,12,7],
[10,13,14,0,16,12,14,12,10],
[9,11,11,10,0,8,10,17,5],
[15,11,18,14,18,0,13,18,12],
[14,16,19,12,16,13,0,15,13],
[12,11,14,14,9,8,11,0,4],
[20,17,19,16,21,14,13,22,0]])



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
result = np.append(np.array([9, 26, 162, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,14,11,20,12,13,8,14],
[13,0,11,10,11,13,14,13,12],
[12,15,0,19,18,16,15,15,14],
[15,16,7,0,18,14,7,10,11],
[6,15,8,8,0,5,11,5,9],
[14,13,10,12,21,0,10,6,15],
[13,12,11,19,15,16,0,17,13],
[18,13,11,16,21,20,9,0,16],
[12,14,12,15,17,11,13,10,0]])



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
result = np.append(np.array([9, 26, 163, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,13,13,13,16,19,18,13],
[10,0,11,10,14,16,17,15,15],
[13,15,0,14,14,15,17,16,17],
[13,16,12,0,13,15,17,18,13],
[13,12,12,13,0,15,13,13,15],
[10,10,11,11,11,0,15,15,11],
[7,9,9,9,13,11,0,11,15],
[8,11,10,8,13,11,15,0,11],
[13,11,9,13,11,15,11,15,0]])



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
result = np.append(np.array([9, 26, 164, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,13,15,13,16,14,13,19],
[5,0,12,12,12,10,10,9,8],
[13,14,0,12,15,12,11,13,13],
[11,14,14,0,18,9,11,11,13],
[13,14,11,8,0,9,10,6,9],
[10,16,14,17,17,0,15,12,17],
[12,16,15,15,16,11,0,14,11],
[13,17,13,15,20,14,12,0,10],
[7,18,13,13,17,9,15,16,0]])



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
result = np.append(np.array([9, 26, 165, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,7,13,11,8,11,14,13],
[14,0,15,13,15,9,11,15,14],
[19,11,0,13,12,12,13,13,14],
[13,13,13,0,13,8,11,11,11],
[15,11,14,13,0,13,14,13,17],
[18,17,14,18,13,0,18,16,18],
[15,15,13,15,12,8,0,12,15],
[12,11,13,15,13,10,14,0,16],
[13,12,12,15,9,8,11,10,0]])



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
result = np.append(np.array([9, 26, 166, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,11,10,12,11,6,5,7],
[22,0,16,17,17,16,13,15,15],
[15,10,0,17,13,13,13,7,7],
[16,9,9,0,15,12,7,9,7],
[14,9,13,11,0,10,8,10,7],
[15,10,13,14,16,0,11,8,12],
[20,13,13,19,18,15,0,10,13],
[21,11,19,17,16,18,16,0,11],
[19,11,19,19,19,14,13,15,0]])



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
result = np.append(np.array([9, 26, 167, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,16,16,15,16,15,11,19],
[8,0,11,12,12,13,8,4,16],
[10,15,0,11,16,12,12,10,14],
[10,14,15,0,12,17,13,13,17],
[11,14,10,14,0,14,10,9,13],
[10,13,14,9,12,0,11,10,14],
[11,18,14,13,16,15,0,9,13],
[15,22,16,13,17,16,17,0,18],
[7,10,12,9,13,12,13,8,0]])



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
result = np.append(np.array([9, 26, 168, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,15,16,13,11,15,10,17],
[12,0,10,16,12,11,15,15,12],
[11,16,0,14,17,15,16,16,15],
[10,10,12,0,14,13,10,9,10],
[13,14,9,12,0,10,15,12,11],
[15,15,11,13,16,0,14,13,12],
[11,11,10,16,11,12,0,12,16],
[16,11,10,17,14,13,14,0,11],
[9,14,11,16,15,14,10,15,0]])



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
result = np.append(np.array([9, 26, 169, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,13,16,19,16,12,13,16],
[19,0,19,14,26,16,16,18,11],
[13,7,0,15,14,15,10,14,9],
[10,12,11,0,15,14,10,14,7],
[7,0,12,11,0,15,6,10,8],
[10,10,11,12,11,0,11,13,8],
[14,10,16,16,20,15,0,16,11],
[13,8,12,12,16,13,10,0,11],
[10,15,17,19,18,18,15,15,0]])



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
result = np.append(np.array([9, 26, 170, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,10,12,10,11,10,10,13],
[13,0,14,12,11,10,13,14,12],
[16,12,0,16,14,12,13,12,13],
[14,14,10,0,9,10,13,14,12],
[16,15,12,17,0,10,15,15,13],
[15,16,14,16,16,0,13,12,12],
[16,13,13,13,11,13,0,10,11],
[16,12,14,12,11,14,16,0,12],
[13,14,13,14,13,14,15,14,0]])



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
result = np.append(np.array([9, 26, 171, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,13,14,6,10,15,16,6],
[16,0,11,14,11,11,18,21,14],
[13,15,0,16,12,14,18,18,12],
[12,12,10,0,10,12,17,21,9],
[20,15,14,16,0,15,21,23,12],
[16,15,12,14,11,0,14,23,8],
[11,8,8,9,5,12,0,18,7],
[10,5,8,5,3,3,8,0,9],
[20,12,14,17,14,18,19,17,0]])



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
result = np.append(np.array([9, 26, 172, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,20,17,13,20,14,10,12],
[16,0,19,19,13,20,11,13,11],
[6,7,0,14,6,7,4,5,8],
[9,7,12,0,14,13,9,11,9],
[13,13,20,12,0,16,19,12,11],
[6,6,19,13,10,0,9,10,9],
[12,15,22,17,7,17,0,9,14],
[16,13,21,15,14,16,17,0,17],
[14,15,18,17,15,17,12,9,0]])



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
result = np.append(np.array([9, 26, 173, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,12,0,26,13,13,14,26],
[12,0,12,0,26,13,13,14,26],
[14,14,0,1,14,14,14,14,26],
[26,26,25,0,26,13,14,14,26],
[0,0,12,0,0,0,0,0,12],
[13,13,12,13,26,0,26,14,13],
[13,13,12,12,26,0,0,1,13],
[12,12,12,12,26,12,25,0,13],
[0,0,0,0,14,13,13,13,0]])



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
result = np.append(np.array([9, 26, 174, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,7,10,11,13,9,8,10],
[20,0,17,17,13,13,12,12,17],
[19,9,0,16,16,11,11,9,13],
[16,9,10,0,10,11,5,3,11],
[15,13,10,16,0,12,8,8,10],
[13,13,15,15,14,0,11,13,12],
[17,14,15,21,18,15,0,13,12],
[18,14,17,23,18,13,13,0,16],
[16,9,13,15,16,14,14,10,0]])



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
result = np.append(np.array([9, 26, 175, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,12,9,11,10,7,8,12],
[12,0,12,12,12,12,10,11,14],
[14,14,0,13,11,15,11,13,12],
[17,14,13,0,17,15,16,10,16],
[15,14,15,9,0,14,12,9,9],
[16,14,11,11,12,0,8,7,12],
[19,16,15,10,14,18,0,13,15],
[18,15,13,16,17,19,13,0,15],
[14,12,14,10,17,14,11,11,0]])



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
result = np.append(np.array([9, 26, 176, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,12,15,12,15,10,16,9],
[15,0,13,16,7,14,10,17,12],
[14,13,0,12,11,14,11,14,9],
[11,10,14,0,8,8,10,13,6],
[14,19,15,18,0,11,15,19,13],
[11,12,12,18,15,0,13,13,11],
[16,16,15,16,11,13,0,16,12],
[10,9,12,13,7,13,10,0,10],
[17,14,17,20,13,15,14,16,0]])



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
result = np.append(np.array([9, 26, 177, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,11,12,8,10,15,12,10],
[18,0,15,13,15,16,16,13,14],
[15,11,0,13,16,16,13,15,15],
[14,13,13,0,11,14,18,12,9],
[18,11,10,15,0,17,17,13,13],
[16,10,10,12,9,0,12,14,9],
[11,10,13,8,9,14,0,8,10],
[14,13,11,14,13,12,18,0,11],
[16,12,11,17,13,17,16,15,0]])



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
result = np.append(np.array([9, 26, 178, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,0,4,7,4,4,10,0],
[26,0,15,15,12,7,10,22,14],
[26,11,0,15,15,15,10,22,17],
[22,11,11,0,15,15,18,22,11],
[19,14,11,11,0,7,6,19,6],
[22,19,11,11,19,0,6,19,14],
[22,16,16,8,20,20,0,16,16],
[16,4,4,4,7,7,10,0,3],
[26,12,9,15,20,12,10,23,0]])



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
result = np.append(np.array([9, 26, 179, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,10,13,14,12,13,13],
[15,0,12,9,12,10,14,9,14],
[15,14,0,11,12,17,12,11,12],
[16,17,15,0,15,13,14,15,13],
[13,14,14,11,0,15,13,11,10],
[12,16,9,13,11,0,7,14,16],
[14,12,14,12,13,19,0,16,12],
[13,17,15,11,15,12,10,0,12],
[13,12,14,13,16,10,14,14,0]])



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
result = np.append(np.array([9, 26, 180, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,14,17,16,17,14,13,13],
[12,0,11,13,16,15,13,11,14],
[12,15,0,19,19,18,14,15,16],
[9,13,7,0,13,15,10,10,11],
[10,10,7,13,0,11,11,9,11],
[9,11,8,11,15,0,11,10,12],
[12,13,12,16,15,15,0,12,14],
[13,15,11,16,17,16,14,0,14],
[13,12,10,15,15,14,12,12,0]])



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
result = np.append(np.array([9, 26, 181, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,16,17,11,11,9,9,12],
[14,0,13,19,13,19,14,16,17],
[10,13,0,15,9,13,11,15,17],
[9,7,11,0,10,10,7,10,10],
[15,13,17,16,0,15,13,13,16],
[15,7,13,16,11,0,13,9,14],
[17,12,15,19,13,13,0,10,10],
[17,10,11,16,13,17,16,0,13],
[14,9,9,16,10,12,16,13,0]])



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
result = np.append(np.array([9, 26, 182, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,13,12,8,13,18,14,14],
[9,0,15,11,9,11,13,14,15],
[13,11,0,11,13,13,16,13,18],
[14,15,15,0,13,10,17,14,11],
[18,17,13,13,0,12,19,15,14],
[13,15,13,16,14,0,16,16,19],
[8,13,10,9,7,10,0,13,14],
[12,12,13,12,11,10,13,0,12],
[12,11,8,15,12,7,12,14,0]])



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
result = np.append(np.array([9, 26, 183, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,12,10,18,5,17,12,8],
[15,0,11,14,17,6,18,12,12],
[14,15,0,11,13,14,15,16,13],
[16,12,15,0,16,7,18,17,17],
[8,9,13,10,0,7,19,10,14],
[21,20,12,19,19,0,23,21,19],
[9,8,11,8,7,3,0,5,6],
[14,14,10,9,16,5,21,0,12],
[18,14,13,9,12,7,20,14,0]])



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
result = np.append(np.array([9, 26, 184, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,0,0,0,0,0,0,0],
[26,0,12,23,26,23,23,23,26],
[26,14,0,26,26,23,11,14,26],
[26,3,0,0,15,0,11,14,14],
[26,0,0,11,0,0,11,11,14],
[26,3,3,26,26,0,11,14,14],
[26,3,15,15,15,15,0,14,26],
[26,3,12,12,15,12,12,0,15],
[26,0,0,12,12,12,0,11,0]])



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
result = np.append(np.array([9, 26, 185, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,15,14,12,16,15,15,16],
[10,0,6,11,5,13,11,9,16],
[11,20,0,17,14,19,14,14,18],
[12,15,9,0,5,15,11,14,18],
[14,21,12,21,0,20,15,17,18],
[10,13,7,11,6,0,12,6,14],
[11,15,12,15,11,14,0,14,16],
[11,17,12,12,9,20,12,0,18],
[10,10,8,8,8,12,10,8,0]])



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
result = np.append(np.array([9, 26, 186, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,0,5,5,5,5,11,0],
[21,0,14,14,15,10,21,21,15],
[26,12,0,10,11,10,16,17,21],
[21,12,16,0,7,11,11,12,16],
[21,11,15,19,0,21,21,21,20],
[21,16,16,15,5,0,11,21,16],
[21,5,10,15,5,15,0,21,15],
[15,5,9,14,5,5,5,0,14],
[26,11,5,10,6,10,11,12,0]])



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
result = np.append(np.array([9, 26, 187, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,15,17,15,8,17,15,16],
[7,0,17,13,15,9,14,11,9],
[11,9,0,11,6,10,11,8,12],
[9,13,15,0,9,9,11,12,15],
[11,11,20,17,0,11,14,16,12],
[18,17,16,17,15,0,21,12,15],
[9,12,15,15,12,5,0,14,13],
[11,15,18,14,10,14,12,0,13],
[10,17,14,11,14,11,13,13,0]])



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
result = np.append(np.array([9, 26, 188, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,12,0,6,0,12,0,0],
[8,0,0,8,8,0,8,8,8],
[14,26,0,14,14,6,14,14,14],
[26,18,12,0,18,18,18,20,6],
[20,18,12,8,0,12,12,20,0],
[26,26,20,8,14,0,20,8,8],
[14,18,12,8,14,6,0,8,6],
[26,18,12,6,6,18,18,0,6],
[26,18,12,20,26,18,20,20,0]])



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
result = np.append(np.array([9, 26, 189, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,10,13,12,11,11,9,12],
[13,0,4,13,10,9,11,9,12],
[16,22,0,19,17,13,15,15,15],
[13,13,7,0,11,5,9,7,11],
[14,16,9,15,0,9,12,11,15],
[15,17,13,21,17,0,13,12,16],
[15,15,11,17,14,13,0,11,15],
[17,17,11,19,15,14,15,0,16],
[14,14,11,15,11,10,11,10,0]])



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
result = np.append(np.array([9, 26, 190, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,11,15,15,13,16,10,14],
[12,0,15,14,11,14,12,10,14],
[15,11,0,16,15,17,14,13,16],
[11,12,10,0,14,14,11,11,15],
[11,15,11,12,0,16,14,9,15],
[13,12,9,12,10,0,11,12,14],
[10,14,12,15,12,15,0,11,15],
[16,16,13,15,17,14,15,0,19],
[12,12,10,11,11,12,11,7,0]])



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
result = np.append(np.array([9, 26, 191, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,16,17,12,14,11,15],
[13,0,14,18,18,13,19,13,14],
[13,12,0,12,16,14,15,9,12],
[10,8,14,0,13,12,15,9,13],
[9,8,10,13,0,10,14,13,8],
[14,13,12,14,16,0,15,11,16],
[12,7,11,11,12,11,0,10,10],
[15,13,17,17,13,15,16,0,15],
[11,12,14,13,18,10,16,11,0]])



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
result = np.append(np.array([9, 26, 192, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,15,15,14,13,17,13,13],
[11,0,14,12,17,17,12,17,13],
[11,12,0,11,13,13,12,12,16],
[11,14,15,0,16,13,17,16,15],
[12,9,13,10,0,12,14,17,15],
[13,9,13,13,14,0,11,13,13],
[9,14,14,9,12,15,0,14,14],
[13,9,14,10,9,13,12,0,17],
[13,13,10,11,11,13,12,9,0]])



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
result = np.append(np.array([9, 26, 193, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,16,13,11,15,13,11,10],
[11,0,13,10,14,12,9,14,9],
[10,13,0,13,11,10,13,10,11],
[13,16,13,0,14,14,13,12,13],
[15,12,15,12,0,15,13,13,8],
[11,14,16,12,11,0,13,14,11],
[13,17,13,13,13,13,0,13,9],
[15,12,16,14,13,12,13,0,12],
[16,17,15,13,18,15,17,14,0]])



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
result = np.append(np.array([9, 26, 194, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,9,14,12,12,15,7,15],
[13,0,13,9,11,11,12,13,12],
[17,13,0,14,12,13,11,12,12],
[12,17,12,0,8,17,10,11,13],
[14,15,14,18,0,18,12,14,10],
[14,15,13,9,8,0,13,12,11],
[11,14,15,16,14,13,0,12,14],
[19,13,14,15,12,14,14,0,13],
[11,14,14,13,16,15,12,13,0]])



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
result = np.append(np.array([9, 26, 195, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,11,12,12,14,12,11],
[15,0,11,12,12,15,14,14,14],
[15,15,0,11,11,12,15,17,17],
[15,14,15,0,12,14,16,12,15],
[14,14,15,14,0,12,14,13,13],
[14,11,14,12,14,0,11,13,11],
[12,12,11,10,12,15,0,13,11],
[14,12,9,14,13,13,13,0,14],
[15,12,9,11,13,15,15,12,0]])



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
result = np.append(np.array([9, 26, 196, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,14,13,12,14,16,12,14],
[13,0,13,15,16,19,19,17,11],
[12,13,0,10,10,10,15,12,12],
[13,11,16,0,14,18,17,14,12],
[14,10,16,12,0,15,17,13,17],
[12,7,16,8,11,0,14,12,9],
[10,7,11,9,9,12,0,9,11],
[14,9,14,12,13,14,17,0,11],
[12,15,14,14,9,17,15,15,0]])



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
result = np.append(np.array([9, 26, 197, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,11,15,15,10,12,14,5],
[6,0,6,3,2,4,4,6,4],
[15,20,0,7,9,5,6,10,7],
[11,23,19,0,10,4,7,7,3],
[11,24,17,16,0,6,6,9,4],
[16,22,21,22,20,0,10,13,12],
[14,22,20,19,20,16,0,21,13],
[12,20,16,19,17,13,5,0,8],
[21,22,19,23,22,14,13,18,0]])



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
result = np.append(np.array([9, 26, 198, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,11,15,8,9,17,14,10],
[17,0,5,6,10,8,11,5,5],
[15,21,0,19,15,19,17,20,13],
[11,20,7,0,10,10,17,14,14],
[18,16,11,16,0,16,21,11,14],
[17,18,7,16,10,0,11,17,7],
[9,15,9,9,5,15,0,9,8],
[12,21,6,12,15,9,17,0,10],
[16,21,13,12,12,19,18,16,0]])



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
result = np.append(np.array([9, 26, 199, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,11,9,10,11,11,16,12],
[13,0,13,12,10,13,8,11,10],
[15,13,0,13,13,17,15,15,16],
[17,14,13,0,14,14,11,12,11],
[16,16,13,12,0,14,11,16,12],
[15,13,9,12,12,0,12,15,11],
[15,18,11,15,15,14,0,18,15],
[10,15,11,14,10,11,8,0,10],
[14,16,10,15,14,15,11,16,0]])



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
result = np.append(np.array([9, 26, 200, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mercw/mercw_9_26.csv", index=False, header=False)