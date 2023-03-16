
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,28,27,23,28,25,35,28],
[22,0,24,23,27,19,33,26],
[23,26,0,25,30,24,31,23],
[27,27,25,0,35,25,33,27],
[22,23,20,15,0,22,30,24],
[25,31,26,25,28,0,40,26],
[15,17,19,17,20,10,0,16],
[22,24,27,23,26,24,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 1, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,27,25,26,38,33,34],
[24,0,24,30,23,30,26,22],
[23,26,0,25,28,33,40,25],
[25,20,25,0,21,27,31,22],
[24,27,22,29,0,38,30,27],
[12,20,17,23,12,0,25,22],
[17,24,10,19,20,25,0,22],
[16,28,25,28,23,28,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 2, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,21,17,27,19,23,19],
[26,0,31,22,22,27,20,25],
[29,19,0,21,19,18,16,21],
[33,28,29,0,26,26,20,26],
[23,28,31,24,0,22,28,18],
[31,23,32,24,28,0,26,19],
[27,30,34,30,22,24,0,24],
[31,25,29,24,32,31,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 3, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,27,25,35,39,23,25],
[23,0,24,22,30,41,20,21],
[23,26,0,18,28,25,16,28],
[25,28,32,0,32,32,20,27],
[15,20,22,18,0,31,27,31],
[11,9,25,18,19,0,16,11],
[27,30,34,30,23,34,0,23],
[25,29,22,23,19,39,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 4, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,26,21,30,24,23,26],
[29,0,19,26,29,27,24,29],
[24,31,0,25,35,24,26,24],
[29,24,25,0,37,26,33,25],
[20,21,15,13,0,23,12,26],
[26,23,26,24,27,0,26,19],
[27,26,24,17,38,24,0,26],
[24,21,26,25,24,31,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 5, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,18,19,27,26,25,22],
[25,0,25,25,26,22,26,26],
[32,25,0,24,27,30,24,27],
[31,25,26,0,24,29,26,32],
[23,24,23,26,0,25,27,24],
[24,28,20,21,25,0,26,25],
[25,24,26,24,23,24,0,27],
[28,24,23,18,26,25,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 6, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,39,34,26,24,37,37],
[20,0,24,30,19,21,30,33],
[11,26,0,21,20,20,23,32],
[16,20,29,0,22,17,24,33],
[24,31,30,28,0,28,34,34],
[26,29,30,33,22,0,28,36],
[13,20,27,26,16,22,0,29],
[13,17,18,17,16,14,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 7, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,29,28,22,27,25,24],
[19,0,19,20,20,22,23,23],
[21,31,0,24,27,30,31,31],
[22,30,26,0,23,26,26,26],
[28,30,23,27,0,25,28,27],
[23,28,20,24,25,0,28,29],
[25,27,19,24,22,22,0,29],
[26,27,19,24,23,21,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 8, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,23,19,26,27,16,22],
[34,0,22,21,32,24,22,31],
[27,28,0,23,32,29,24,29],
[31,29,27,0,33,27,22,35],
[24,18,18,17,0,23,18,22],
[23,26,21,23,27,0,25,29],
[34,28,26,28,32,25,0,31],
[28,19,21,15,28,21,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 9, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,28,25,24,24,22,22],
[26,0,18,22,27,26,18,18],
[22,32,0,26,35,26,32,31],
[25,28,24,0,30,29,26,33],
[26,23,15,20,0,25,22,17],
[26,24,24,21,25,0,19,27],
[28,32,18,24,28,31,0,19],
[28,32,19,17,33,23,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 10, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,23,20,20,25,24,25],
[28,0,17,26,23,23,28,24],
[27,33,0,32,23,23,26,28],
[30,24,18,0,21,23,29,25],
[30,27,27,29,0,25,28,29],
[25,27,27,27,25,0,27,28],
[26,22,24,21,22,23,0,26],
[25,26,22,25,21,22,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 11, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,27,21,27,29,25,26],
[26,0,33,26,24,29,24,25],
[23,17,0,17,18,23,18,18],
[29,24,33,0,25,27,31,26],
[23,26,32,25,0,27,26,26],
[21,21,27,23,23,0,25,24],
[25,26,32,19,24,25,0,26],
[24,25,32,24,24,26,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 12, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,17,16,25,23,23,20],
[31,0,35,28,31,21,33,29],
[33,15,0,16,21,25,18,29],
[34,22,34,0,34,25,24,35],
[25,19,29,16,0,13,27,30],
[27,29,25,25,37,0,25,29],
[27,17,32,26,23,25,0,28],
[30,21,21,15,20,21,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 13, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,18,23,20,21,18,15],
[27,0,18,27,28,31,24,23],
[32,32,0,29,27,26,25,20],
[27,23,21,0,21,23,23,18],
[30,22,23,29,0,25,25,26],
[29,19,24,27,25,0,22,15],
[32,26,25,27,25,28,0,21],
[35,27,30,32,24,35,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 14, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,24,35,30,19,21,20],
[37,0,24,22,19,31,19,18],
[26,26,0,41,31,38,25,33],
[15,28,9,0,32,28,11,22],
[20,31,19,18,0,30,8,14],
[31,19,12,22,20,0,19,11],
[29,31,25,39,42,31,0,25],
[30,32,17,28,36,39,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 15, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,21,27,21,26,20,21],
[25,0,24,27,20,22,18,24],
[29,26,0,28,23,25,28,22],
[23,23,22,0,18,19,21,21],
[29,30,27,32,0,24,24,20],
[24,28,25,31,26,0,26,26],
[30,32,22,29,26,24,0,24],
[29,26,28,29,30,24,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 16, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,26,24,24,23,34,24],
[25,0,32,27,26,37,42,25],
[24,18,0,22,26,23,33,25],
[26,23,28,0,30,20,38,31],
[26,24,24,20,0,23,35,31],
[27,13,27,30,27,0,30,35],
[16,8,17,12,15,20,0,12],
[26,25,25,19,19,15,38,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 17, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,26,28,25,31,20,23],
[28,0,27,28,24,32,22,33],
[24,23,0,29,24,28,20,31],
[22,22,21,0,22,25,26,27],
[25,26,26,28,0,32,29,32],
[19,18,22,25,18,0,17,22],
[30,28,30,24,21,33,0,31],
[27,17,19,23,18,28,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 18, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,26,27,31,28,28,21],
[18,0,20,23,21,20,18,21],
[24,30,0,26,37,29,28,22],
[23,27,24,0,32,29,22,25],
[19,29,13,18,0,29,19,19],
[22,30,21,21,21,0,23,25],
[22,32,22,28,31,27,0,25],
[29,29,28,25,31,25,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 19, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,26,16,22,26,30,27],
[28,0,24,25,31,30,34,32],
[24,26,0,19,21,24,31,30],
[34,25,31,0,27,30,31,35],
[28,19,29,23,0,39,32,32],
[24,20,26,20,11,0,23,28],
[20,16,19,19,18,27,0,20],
[23,18,20,15,18,22,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 20, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,31,32,32,33,22,13],
[20,0,16,21,24,21,11,23],
[19,34,0,23,23,23,19,28],
[18,29,27,0,18,30,13,26],
[18,26,27,32,0,29,26,25],
[17,29,27,20,21,0,19,27],
[28,39,31,37,24,31,0,28],
[37,27,22,24,25,23,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 21, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,26,24,25,21,24,18],
[26,0,27,31,25,28,19,25],
[24,23,0,25,24,24,29,29],
[26,19,25,0,27,24,26,23],
[25,25,26,23,0,26,21,22],
[29,22,26,26,24,0,22,23],
[26,31,21,24,29,28,0,29],
[32,25,21,27,28,27,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 22, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,28,23,23,24,21,27],
[29,0,23,27,32,25,28,29],
[22,27,0,20,22,20,24,28],
[27,23,30,0,29,24,22,24],
[27,18,28,21,0,24,22,24],
[26,25,30,26,26,0,25,23],
[29,22,26,28,28,25,0,26],
[23,21,22,26,26,27,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 23, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,19,21,21,21,20,14],
[36,0,28,28,34,29,18,33],
[31,22,0,30,33,35,29,24],
[29,22,20,0,20,25,14,21],
[29,16,17,30,0,22,10,20],
[29,21,15,25,28,0,16,21],
[30,32,21,36,40,34,0,32],
[36,17,26,29,30,29,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 24, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,19,18,21,25,21,17],
[29,0,29,26,25,28,30,23],
[31,21,0,24,23,29,29,23],
[32,24,26,0,26,25,29,25],
[29,25,27,24,0,27,32,24],
[25,22,21,25,23,0,28,19],
[29,20,21,21,18,22,0,21],
[33,27,27,25,26,31,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 25, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,19,24,28,25,30,39],
[17,0,17,20,24,22,25,23],
[31,33,0,25,34,28,27,38],
[26,30,25,0,35,31,28,41],
[22,26,16,15,0,16,22,28],
[25,28,22,19,34,0,26,33],
[20,25,23,22,28,24,0,29],
[11,27,12,9,22,17,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 26, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,25,31,27,24,35,24],
[26,0,22,30,31,23,28,20],
[25,28,0,29,26,25,34,24],
[19,20,21,0,20,22,28,23],
[23,19,24,30,0,22,32,24],
[26,27,25,28,28,0,29,26],
[15,22,16,22,18,21,0,15],
[26,30,26,27,26,24,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 27, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,27,14,12,12,16,28],
[36,0,14,34,25,34,27,27],
[23,36,0,34,25,34,16,14],
[36,16,16,0,0,0,29,16],
[38,25,25,50,0,23,39,28],
[38,16,16,50,27,0,29,27],
[34,23,34,21,11,21,0,28],
[22,23,36,34,22,23,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 28, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,18,24,20,30,28,10],
[27,0,19,35,27,30,27,21],
[32,31,0,32,21,32,35,21],
[26,15,18,0,24,13,26,20],
[30,23,29,26,0,28,29,32],
[20,20,18,37,22,0,30,21],
[22,23,15,24,21,20,0,20],
[40,29,29,30,18,29,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 29, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,26,25,23,23,24,24],
[25,0,23,23,20,22,17,24],
[24,27,0,22,24,24,22,25],
[25,27,28,0,20,22,21,25],
[27,30,26,30,0,25,30,26],
[27,28,26,28,25,0,25,26],
[26,33,28,29,20,25,0,27],
[26,26,25,25,24,24,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 30, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,32,23,22,18,31,18],
[27,0,32,29,34,23,36,25],
[18,18,0,24,24,16,21,16],
[27,21,26,0,33,23,32,25],
[28,16,26,17,0,16,19,8],
[32,27,34,27,34,0,33,13],
[19,14,29,18,31,17,0,13],
[32,25,34,25,42,37,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 31, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,23,22,24,18,26,20],
[27,0,23,22,28,24,33,18],
[27,27,0,23,34,31,30,29],
[28,28,27,0,29,26,31,21],
[26,22,16,21,0,20,30,22],
[32,26,19,24,30,0,30,25],
[24,17,20,19,20,20,0,13],
[30,32,21,29,28,25,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 32, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,30,22,23,28,26,21],
[17,0,29,21,20,25,26,20],
[20,21,0,19,24,21,21,19],
[28,29,31,0,27,22,27,27],
[27,30,26,23,0,31,20,23],
[22,25,29,28,19,0,27,20],
[24,24,29,23,30,23,0,22],
[29,30,31,23,27,30,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 33, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,25,18,34,21,22,23],
[23,0,16,18,26,20,14,22],
[25,34,0,22,26,28,27,28],
[32,32,28,0,31,22,33,27],
[16,24,24,19,0,22,23,22],
[29,30,22,28,28,0,33,28],
[28,36,23,17,27,17,0,25],
[27,28,22,23,28,22,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 34, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,24,21,24,23,24,25],
[27,0,21,24,29,23,25,29],
[26,29,0,28,33,25,25,29],
[29,26,22,0,23,22,20,25],
[26,21,17,27,0,23,23,26],
[27,27,25,28,27,0,28,27],
[26,25,25,30,27,22,0,27],
[25,21,21,25,24,23,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 35, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,27,26,25,25,29,25],
[24,0,23,24,19,20,22,24],
[23,27,0,22,19,17,23,16],
[24,26,28,0,22,26,26,29],
[25,31,31,28,0,28,23,24],
[25,30,33,24,22,0,21,25],
[21,28,27,24,27,29,0,27],
[25,26,34,21,26,25,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 36, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,31,21,24,23,19,27],
[26,0,26,28,29,23,25,28],
[19,24,0,22,23,18,22,25],
[29,22,28,0,26,19,22,24],
[26,21,27,24,0,26,26,25],
[27,27,32,31,24,0,26,31],
[31,25,28,28,24,24,0,31],
[23,22,25,26,25,19,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 37, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,16,18,27,26,20,26],
[25,0,15,16,21,16,14,16],
[34,35,0,24,31,28,29,29],
[32,34,26,0,29,30,25,27],
[23,29,19,21,0,24,14,25],
[24,34,22,20,26,0,25,29],
[30,36,21,25,36,25,0,26],
[24,34,21,23,25,21,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 38, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,28,30,24,32,26,25],
[21,0,27,26,22,27,20,23],
[22,23,0,23,21,27,19,24],
[20,24,27,0,17,25,17,27],
[26,28,29,33,0,32,21,29],
[18,23,23,25,18,0,16,22],
[24,30,31,33,29,34,0,35],
[25,27,26,23,21,28,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 39, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,31,23,26,23,23,28],
[23,0,22,24,24,19,22,24],
[19,28,0,21,31,25,26,21],
[27,26,29,0,26,20,25,27],
[24,26,19,24,0,24,25,23],
[27,31,25,30,26,0,24,29],
[27,28,24,25,25,26,0,24],
[22,26,29,23,27,21,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 40, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,27,21,26,24,15,21],
[19,0,21,14,15,15,10,12],
[23,29,0,21,21,19,15,26],
[29,36,29,0,29,33,25,23],
[24,35,29,21,0,21,16,24],
[26,35,31,17,29,0,22,22],
[35,40,35,25,34,28,0,26],
[29,38,24,27,26,28,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 41, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,33,27,22,32,32,26],
[19,0,27,21,16,25,23,22],
[17,23,0,25,22,27,21,22],
[23,29,25,0,28,27,24,23],
[28,34,28,22,0,32,31,26],
[18,25,23,23,18,0,20,19],
[18,27,29,26,19,30,0,27],
[24,28,28,27,24,31,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 42, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,18,23,21,34,24,22],
[22,0,28,20,16,31,19,32],
[32,22,0,30,29,40,22,34],
[27,30,20,0,25,25,26,21],
[29,34,21,25,0,33,22,31],
[16,19,10,25,17,0,18,15],
[26,31,28,24,28,32,0,29],
[28,18,16,29,19,35,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 43, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,24,33,26,25,16,26],
[25,0,24,33,27,20,18,27],
[26,26,0,31,28,25,27,31],
[17,17,19,0,25,25,12,22],
[24,23,22,25,0,19,16,20],
[25,30,25,25,31,0,23,26],
[34,32,23,38,34,27,0,24],
[24,23,19,28,30,24,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 44, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,29,25,24,23,21,19],
[21,0,23,23,26,23,27,16],
[21,27,0,24,21,22,21,14],
[25,27,26,0,29,30,25,19],
[26,24,29,21,0,28,24,25],
[27,27,28,20,22,0,24,23],
[29,23,29,25,26,26,0,20],
[31,34,36,31,25,27,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 45, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,25,24,29,26,23,27],
[27,0,21,28,25,29,22,25],
[25,29,0,24,28,28,29,24],
[26,22,26,0,27,31,21,31],
[21,25,22,23,0,28,21,25],
[24,21,22,19,22,0,19,25],
[27,28,21,29,29,31,0,30],
[23,25,26,19,25,25,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 46, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,27,26,27,39,30,34],
[25,0,26,20,26,33,8,27],
[23,24,0,33,28,33,13,22],
[24,30,17,0,19,23,17,15],
[23,24,22,31,0,34,19,24],
[11,17,17,27,16,0,16,27],
[20,42,37,33,31,34,0,28],
[16,23,28,35,26,23,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 47, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,26,25,22,23,28,26],
[23,0,24,21,18,19,25,23],
[24,26,0,20,20,19,22,21],
[25,29,30,0,28,26,30,33],
[28,32,30,22,0,24,31,31],
[27,31,31,24,26,0,27,30],
[22,25,28,20,19,23,0,28],
[24,27,29,17,19,20,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 48, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,11,23,13,18,24,26],
[38,0,33,26,28,17,22,26],
[39,17,0,29,22,20,24,27],
[27,24,21,0,17,21,26,15],
[37,22,28,33,0,19,26,26],
[32,33,30,29,31,0,33,24],
[26,28,26,24,24,17,0,27],
[24,24,23,35,24,26,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 49, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,27,16,25,28,20,37],
[20,0,20,25,19,25,11,22],
[23,30,0,27,20,26,27,24],
[34,25,23,0,33,33,14,25],
[25,31,30,17,0,24,27,28],
[22,25,24,17,26,0,21,21],
[30,39,23,36,23,29,0,34],
[13,28,26,25,22,29,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 50, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,23,22,18,25,19,29],
[32,0,30,27,27,24,30,35],
[27,20,0,31,27,26,28,33],
[28,23,19,0,22,23,23,30],
[32,23,23,28,0,22,27,30],
[25,26,24,27,28,0,20,26],
[31,20,22,27,23,30,0,32],
[21,15,17,20,20,24,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 51, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,32,32,42,32,24],
[39,0,0,21,39,39,21,39],
[39,50,0,21,39,39,39,39],
[18,29,29,0,50,29,29,29],
[18,11,11,0,0,18,0,0],
[8,11,11,21,32,0,8,8],
[18,29,11,21,50,42,0,42],
[26,11,11,21,50,42,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 52, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,25,24,26,24,25,22],
[22,0,20,27,26,25,26,24],
[25,30,0,27,29,30,28,31],
[26,23,23,0,23,22,24,21],
[24,24,21,27,0,25,26,20],
[26,25,20,28,25,0,24,23],
[25,24,22,26,24,26,0,25],
[28,26,19,29,30,27,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 53, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,24,26,22,27,28,29],
[27,0,25,27,29,29,25,31],
[26,25,0,25,26,26,23,30],
[24,23,25,0,26,30,26,29],
[28,21,24,24,0,26,26,29],
[23,21,24,20,24,0,25,30],
[22,25,27,24,24,25,0,33],
[21,19,20,21,21,20,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 54, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,32,24,30,28,23,35],
[15,0,19,10,23,20,19,24],
[18,31,0,19,27,22,25,24],
[26,40,31,0,36,22,28,27],
[20,27,23,14,0,25,17,21],
[22,30,28,28,25,0,26,22],
[27,31,25,22,33,24,0,23],
[15,26,26,23,29,28,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 55, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,31,27,28,27,28,22],
[28,0,23,29,35,29,37,25],
[19,27,0,22,31,26,29,24],
[23,21,28,0,32,20,24,24],
[22,15,19,18,0,18,22,19],
[23,21,24,30,32,0,30,24],
[22,13,21,26,28,20,0,19],
[28,25,26,26,31,26,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 56, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,28,27,23,26,20,28],
[28,0,26,28,23,27,25,32],
[22,24,0,24,24,22,17,24],
[23,22,26,0,25,29,23,26],
[27,27,26,25,0,28,21,23],
[24,23,28,21,22,0,17,22],
[30,25,33,27,29,33,0,30],
[22,18,26,24,27,28,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 57, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,23,26,28,25,25,33],
[25,0,24,24,25,25,30,25],
[27,26,0,26,24,26,26,29],
[24,26,24,0,23,26,21,29],
[22,25,26,27,0,25,27,29],
[25,25,24,24,25,0,27,29],
[25,20,24,29,23,23,0,30],
[17,25,21,21,21,21,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 58, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,41,22,24,27,24,24],
[23,0,32,26,19,17,23,27],
[9,18,0,13,14,15,12,13],
[28,24,37,0,22,18,17,28],
[26,31,36,28,0,17,24,29],
[23,33,35,32,33,0,28,24],
[26,27,38,33,26,22,0,29],
[26,23,37,22,21,26,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 59, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,27,21,31,24,25,30],
[23,0,29,21,30,24,23,24],
[23,21,0,20,30,20,25,21],
[29,29,30,0,34,25,28,32],
[19,20,20,16,0,20,21,21],
[26,26,30,25,30,0,27,27],
[25,27,25,22,29,23,0,28],
[20,26,29,18,29,23,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 60, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,22,26,26,37,23,31],
[19,0,24,24,25,32,21,27],
[28,26,0,27,28,35,24,26],
[24,26,23,0,28,31,25,26],
[24,25,22,22,0,30,28,24],
[13,18,15,19,20,0,16,19],
[27,29,26,25,22,34,0,30],
[19,23,24,24,26,31,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 61, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,16,16,23,21,21,15],
[28,0,21,21,28,27,19,23],
[34,29,0,24,31,31,28,25],
[34,29,26,0,38,30,26,23],
[27,22,19,12,0,20,17,17],
[29,23,19,20,30,0,23,19],
[29,31,22,24,33,27,0,25],
[35,27,25,27,33,31,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 62, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,24,17,22,22,27,23],
[30,0,25,29,21,30,28,21],
[26,25,0,24,18,30,28,25],
[33,21,26,0,26,33,28,27],
[28,29,32,24,0,33,27,22],
[28,20,20,17,17,0,22,18],
[23,22,22,22,23,28,0,23],
[27,29,25,23,28,32,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 63, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,28,26,33,30,23,26],
[24,0,26,27,30,20,23,35],
[22,24,0,32,29,23,28,30],
[24,23,18,0,23,19,19,23],
[17,20,21,27,0,20,24,29],
[20,30,27,31,30,0,29,29],
[27,27,22,31,26,21,0,27],
[24,15,20,27,21,21,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 64, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,27,28,30,21,23,23],
[29,0,28,29,25,33,27,28],
[23,22,0,27,25,34,31,25],
[22,21,23,0,29,24,30,23],
[20,25,25,21,0,25,25,21],
[29,17,16,26,25,0,26,17],
[27,23,19,20,25,24,0,21],
[27,22,25,27,29,33,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 65, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,25,28,21,34,28,29],
[19,0,26,26,25,25,27,29],
[25,24,0,27,26,32,32,23],
[22,24,23,0,23,27,30,33],
[29,25,24,27,0,30,33,24],
[16,25,18,23,20,0,25,26],
[22,23,18,20,17,25,0,19],
[21,21,27,17,26,24,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 66, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,25,29,26,38,35,39],
[23,0,21,26,22,32,26,27],
[25,29,0,23,23,29,31,27],
[21,24,27,0,20,24,29,32],
[24,28,27,30,0,29,29,34],
[12,18,21,26,21,0,26,22],
[15,24,19,21,21,24,0,27],
[11,23,23,18,16,28,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 67, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,28,25,25,27,28,24],
[27,0,21,16,23,24,23,24],
[22,29,0,18,26,26,24,23],
[25,34,32,0,27,28,27,24],
[25,27,24,23,0,24,22,29],
[23,26,24,22,26,0,23,25],
[22,27,26,23,28,27,0,27],
[26,26,27,26,21,25,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 68, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,18,28,18,25,19,16],
[38,0,26,32,28,40,29,21],
[32,24,0,34,23,32,31,28],
[22,18,16,0,23,28,14,13],
[32,22,27,27,0,29,28,23],
[25,10,18,22,21,0,15,10],
[31,21,19,36,22,35,0,19],
[34,29,22,37,27,40,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 69, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,34,18,32,23,26,19],
[26,0,27,15,25,19,15,18],
[16,23,0,17,20,19,15,21],
[32,35,33,0,31,26,24,23],
[18,25,30,19,0,19,22,28],
[27,31,31,24,31,0,17,27],
[24,35,35,26,28,33,0,27],
[31,32,29,27,22,23,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 70, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,30,28,40,39,23,26],
[27,0,23,27,32,39,28,24],
[20,27,0,21,33,35,23,21],
[22,23,29,0,29,36,21,28],
[10,18,17,21,0,29,12,21],
[11,11,15,14,21,0,13,17],
[27,22,27,29,38,37,0,27],
[24,26,29,22,29,33,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 71, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,24,24,26,26,24,24],
[32,0,25,24,33,34,25,29],
[26,25,0,22,27,26,23,29],
[26,26,28,0,28,31,20,29],
[24,17,23,22,0,23,21,28],
[24,16,24,19,27,0,24,26],
[26,25,27,30,29,26,0,28],
[26,21,21,21,22,24,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 72, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,34,10,30,27,24,21],
[17,0,27,15,22,31,21,24],
[16,23,0,21,35,22,29,21],
[40,35,29,0,39,27,29,21],
[20,28,15,11,0,19,20,13],
[23,19,28,23,31,0,37,26],
[26,29,21,21,30,13,0,16],
[29,26,29,29,37,24,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 73, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,36,24,32,32,30,29],
[15,0,28,23,16,29,16,24],
[14,22,0,26,23,27,15,31],
[26,27,24,0,20,32,24,23],
[18,34,27,30,0,32,17,22],
[18,21,23,18,18,0,16,24],
[20,34,35,26,33,34,0,32],
[21,26,19,27,28,26,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 74, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,22,27,35,24,29,24],
[18,0,22,20,31,19,27,25],
[28,28,0,18,32,27,26,30],
[23,30,32,0,29,25,29,30],
[15,19,18,21,0,21,21,21],
[26,31,23,25,29,0,31,30],
[21,23,24,21,29,19,0,25],
[26,25,20,20,29,20,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 75, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,26,24,27,30,29,31],
[25,0,25,24,27,25,25,29],
[24,25,0,30,29,23,28,31],
[26,26,20,0,24,18,23,29],
[23,23,21,26,0,28,22,28],
[20,25,27,32,22,0,22,32],
[21,25,22,27,28,28,0,27],
[19,21,19,21,22,18,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 76, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,26,41,25,30,24,30],
[11,0,28,30,17,24,5,22],
[24,22,0,24,24,13,18,13],
[9,20,26,0,21,26,20,26],
[25,33,26,29,0,33,33,33],
[20,26,37,24,17,0,11,22],
[26,45,32,30,17,39,0,23],
[20,28,37,24,17,28,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 77, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,25,26,26,27,22,21],
[26,0,29,23,28,28,24,24],
[25,21,0,20,27,28,22,25],
[24,27,30,0,29,30,24,22],
[24,22,23,21,0,25,19,19],
[23,22,22,20,25,0,18,19],
[28,26,28,26,31,32,0,24],
[29,26,25,28,31,31,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 78, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,20,31,22,30,20,24],
[22,0,21,27,25,23,17,25],
[30,29,0,34,30,30,33,24],
[19,23,16,0,27,27,25,23],
[28,25,20,23,0,21,15,18],
[20,27,20,23,29,0,19,27],
[30,33,17,25,35,31,0,29],
[26,25,26,27,32,23,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 79, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,25,32,25,28,26,23],
[28,0,27,27,21,25,28,28],
[25,23,0,24,21,24,25,27],
[18,23,26,0,20,25,22,29],
[25,29,29,30,0,23,31,29],
[22,25,26,25,27,0,29,29],
[24,22,25,28,19,21,0,22],
[27,22,23,21,21,21,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 80, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,15,14,15,23,17,23],
[25,0,23,18,21,22,25,24],
[35,27,0,20,25,27,28,29],
[36,32,30,0,27,33,29,25],
[35,29,25,23,0,27,28,24],
[27,28,23,17,23,0,26,26],
[33,25,22,21,22,24,0,29],
[27,26,21,25,26,24,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 81, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,40,31,12,27,32,21],
[25,0,36,23,29,23,22,24],
[10,14,0,21,6,23,25,17],
[19,27,29,0,21,26,22,20],
[38,21,44,29,0,32,28,30],
[23,27,27,24,18,0,16,20],
[18,28,25,28,22,34,0,29],
[29,26,33,30,20,30,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 82, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,26,30,19,24,28,29],
[20,0,12,18,24,22,14,22],
[24,38,0,20,22,20,33,28],
[20,32,30,0,26,25,17,29],
[31,26,28,24,0,18,28,21],
[26,28,30,25,32,0,35,35],
[22,36,17,33,22,15,0,25],
[21,28,22,21,29,15,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 83, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,30,23,28,39,33,35],
[20,0,25,22,27,30,29,34],
[20,25,0,21,14,14,21,32],
[27,28,29,0,22,33,24,35],
[22,23,36,28,0,34,29,35],
[11,20,36,17,16,0,14,25],
[17,21,29,26,21,36,0,28],
[15,16,18,15,15,25,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 84, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,23,21,23,21,21,21],
[23,0,26,20,24,23,15,19],
[27,24,0,21,23,22,19,22],
[29,30,29,0,26,33,22,23],
[27,26,27,24,0,27,31,24],
[29,27,28,17,23,0,24,23],
[29,35,31,28,19,26,0,27],
[29,31,28,27,26,27,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 85, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,23,20,26,20,21,24],
[23,0,21,17,21,22,24,26],
[27,29,0,20,24,21,25,23],
[30,33,30,0,28,27,28,25],
[24,29,26,22,0,26,27,25],
[30,28,29,23,24,0,28,25],
[29,26,25,22,23,22,0,23],
[26,24,27,25,25,25,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 86, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,22,20,21,17,16,20],
[29,0,28,25,22,23,24,23],
[28,22,0,26,29,23,20,27],
[30,25,24,0,24,24,25,23],
[29,28,21,26,0,25,24,25],
[33,27,27,26,25,0,26,27],
[34,26,30,25,26,24,0,26],
[30,27,23,27,25,23,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 87, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,23,23,28,26,31,25],
[24,0,26,25,22,30,31,25],
[27,24,0,23,24,27,28,24],
[27,25,27,0,28,26,32,26],
[22,28,26,22,0,27,28,26],
[24,20,23,24,23,0,25,25],
[19,19,22,18,22,25,0,18],
[25,25,26,24,24,25,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 88, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,24,28,25,33,31,32],
[15,0,10,11,14,27,23,26],
[26,40,0,24,22,30,28,27],
[22,39,26,0,21,38,30,30],
[25,36,28,29,0,36,31,24],
[17,23,20,12,14,0,26,27],
[19,27,22,20,19,24,0,30],
[18,24,23,20,26,23,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 89, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,24,30,31,37,22,31],
[18,0,12,26,34,35,22,25],
[26,38,0,27,41,35,24,34],
[20,24,23,0,32,31,19,26],
[19,16,9,18,0,26,17,19],
[13,15,15,19,24,0,21,13],
[28,28,26,31,33,29,0,22],
[19,25,16,24,31,37,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 90, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,40,21,28,21,10,25],
[21,0,45,25,32,30,14,26],
[10,5,0,9,22,18,11,21],
[29,25,41,0,35,27,29,44],
[22,18,28,15,0,15,21,30],
[29,20,32,23,35,0,29,25],
[40,36,39,21,29,21,0,28],
[25,24,29,6,20,25,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 91, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,27,26,30,27,25,30],
[15,0,7,12,13,18,22,24],
[23,43,0,32,26,36,38,31],
[24,38,18,0,12,21,28,32],
[20,37,24,38,0,35,35,38],
[23,32,14,29,15,0,27,30],
[25,28,12,22,15,23,0,28],
[20,26,19,18,12,20,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 92, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,28,25,20,22,37,25],
[26,0,28,28,24,20,29,24],
[22,22,0,15,19,21,17,23],
[25,22,35,0,29,24,27,27],
[30,26,31,21,0,27,36,29],
[28,30,29,26,23,0,27,28],
[13,21,33,23,14,23,0,16],
[25,26,27,23,21,22,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 93, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,27,30,25,22,22,23],
[24,0,23,34,24,22,21,25],
[23,27,0,32,21,21,22,18],
[20,16,18,0,16,20,19,21],
[25,26,29,34,0,24,23,20],
[28,28,29,30,26,0,24,26],
[28,29,28,31,27,26,0,24],
[27,25,32,29,30,24,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 94, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,29,41,28,21,45,23],
[32,0,25,36,34,29,41,23],
[21,25,0,36,32,28,29,28],
[9,14,14,0,17,18,33,18],
[22,16,18,33,0,22,33,16],
[29,21,22,32,28,0,39,20],
[5,9,21,17,17,11,0,16],
[27,27,22,32,34,30,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 95, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,22,31,24,27,28,16],
[15,0,21,26,19,30,23,20],
[28,29,0,32,27,27,26,21],
[19,24,18,0,14,22,23,20],
[26,31,23,36,0,36,26,26],
[23,20,23,28,14,0,30,24],
[22,27,24,27,24,20,0,28],
[34,30,29,30,24,26,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 96, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,22,20,21,18,25,23],
[28,0,23,24,21,22,30,28],
[28,27,0,25,25,23,30,31],
[30,26,25,0,21,21,28,30],
[29,29,25,29,0,25,28,27],
[32,28,27,29,25,0,31,34],
[25,20,20,22,22,19,0,26],
[27,22,19,20,23,16,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 97, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,24,24,26,25,28,22],
[31,0,27,20,25,23,31,29],
[26,23,0,23,21,19,25,24],
[26,30,27,0,19,22,27,26],
[24,25,29,31,0,24,24,27],
[25,27,31,28,26,0,32,31],
[22,19,25,23,26,18,0,22],
[28,21,26,24,23,19,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 98, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,28,27,26,23,27,30],
[23,0,18,25,23,17,22,21],
[22,32,0,28,27,29,27,27],
[23,25,22,0,21,22,21,26],
[24,27,23,29,0,21,23,26],
[27,33,21,28,29,0,28,31],
[23,28,23,29,27,22,0,27],
[20,29,23,24,24,19,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 99, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,24,28,39,28,43,39],
[35,0,27,25,35,46,37,42],
[26,23,0,26,20,31,28,22],
[22,25,24,0,35,26,41,22],
[11,15,30,15,0,13,41,26],
[22,4,19,24,37,0,37,32],
[7,13,22,9,9,13,0,9],
[11,8,28,28,24,18,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 100, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,30,20,28,27,18,26],
[21,0,23,23,29,27,22,24],
[20,27,0,22,29,23,22,22],
[30,27,28,0,37,29,23,26],
[22,21,21,13,0,22,18,18],
[23,23,27,21,28,0,20,21],
[32,28,28,27,32,30,0,23],
[24,26,28,24,32,29,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 101, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,22,23,18,23,22,24],
[30,0,22,32,21,25,25,28],
[28,28,0,31,25,28,25,31],
[27,18,19,0,22,17,21,25],
[32,29,25,28,0,28,22,27],
[27,25,22,33,22,0,16,31],
[28,25,25,29,28,34,0,33],
[26,22,19,25,23,19,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 102, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,27,24,27,27,28,23],
[29,0,20,32,15,25,24,20],
[23,30,0,29,15,14,19,20],
[26,18,21,0,15,19,20,18],
[23,35,35,35,0,34,23,20],
[23,25,36,31,16,0,19,20],
[22,26,31,30,27,31,0,25],
[27,30,30,32,30,30,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 103, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,27,26,30,32,21,29],
[18,0,21,25,28,22,17,19],
[23,29,0,33,26,30,25,29],
[24,25,17,0,24,27,22,23],
[20,22,24,26,0,26,22,16],
[18,28,20,23,24,0,15,14],
[29,33,25,28,28,35,0,28],
[21,31,21,27,34,36,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 104, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,22,26,25,26,30,26],
[18,0,19,23,19,22,23,15],
[28,31,0,30,23,21,25,27],
[24,27,20,0,21,24,23,23],
[25,31,27,29,0,23,30,20],
[24,28,29,26,27,0,31,22],
[20,27,25,27,20,19,0,21],
[24,35,23,27,30,28,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 105, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,23,29,32,26,29,36],
[8,0,18,32,31,7,18,33],
[27,32,0,34,22,16,25,33],
[21,18,16,0,21,18,21,33],
[18,19,28,29,0,8,24,35],
[24,43,34,32,42,0,23,49],
[21,32,25,29,26,27,0,41],
[14,17,17,17,15,1,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 106, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,25,25,24,20,27,29],
[23,0,26,19,24,25,29,27],
[25,24,0,22,25,24,30,28],
[25,31,28,0,28,27,30,30],
[26,26,25,22,0,24,24,32],
[30,25,26,23,26,0,23,27],
[23,21,20,20,26,27,0,24],
[21,23,22,20,18,23,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 107, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,45,21,39,22,20,17],
[18,0,34,24,38,25,27,20],
[5,16,0,17,21,13,11,12],
[29,26,33,0,32,21,24,27],
[11,12,29,18,0,14,15,17],
[28,25,37,29,36,0,17,25],
[30,23,39,26,35,33,0,26],
[33,30,38,23,33,25,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 108, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,20,26,25,24,23,20],
[23,0,23,31,19,28,22,24],
[30,27,0,21,31,26,27,20],
[24,19,29,0,24,29,25,20],
[25,31,19,26,0,23,18,20],
[26,22,24,21,27,0,19,24],
[27,28,23,25,32,31,0,29],
[30,26,30,30,30,26,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 109, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,18,25,24,19,25,25],
[25,0,21,24,25,21,28,26],
[32,29,0,28,26,25,27,30],
[25,26,22,0,29,20,24,23],
[26,25,24,21,0,24,23,24],
[31,29,25,30,26,0,33,28],
[25,22,23,26,27,17,0,23],
[25,24,20,27,26,22,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 110, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,20,17,24,24,29,24],
[26,0,24,24,22,18,28,26],
[30,26,0,21,24,22,28,27],
[33,26,29,0,25,24,32,28],
[26,28,26,25,0,17,29,21],
[26,32,28,26,33,0,38,24],
[21,22,22,18,21,12,0,23],
[26,24,23,22,29,26,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 111, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,16,15,17,28,29,16],
[29,0,30,25,34,21,28,30],
[34,20,0,16,29,18,26,23],
[35,25,34,0,38,40,35,30],
[33,16,21,12,0,22,22,18],
[22,29,32,10,28,0,32,17],
[21,22,24,15,28,18,0,28],
[34,20,27,20,32,33,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 112, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,25,29,32,27,27,27],
[29,0,24,31,32,25,28,29],
[25,26,0,28,30,29,28,28],
[21,19,22,0,27,21,24,22],
[18,18,20,23,0,17,22,27],
[23,25,21,29,33,0,26,26],
[23,22,22,26,28,24,0,20],
[23,21,22,28,23,24,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 113, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,28,28,30,29,23,25],
[21,0,19,23,25,24,19,19],
[22,31,0,26,26,29,25,25],
[22,27,24,0,25,31,23,25],
[20,25,24,25,0,26,23,19],
[21,26,21,19,24,0,20,21],
[27,31,25,27,27,30,0,26],
[25,31,25,25,31,29,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 114, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,12,28,20,24,16,20],
[24,0,22,20,26,24,36,34],
[38,28,0,30,26,26,26,22],
[22,30,20,0,26,36,22,22],
[30,24,24,24,0,18,24,30],
[26,26,24,14,32,0,16,32],
[34,14,24,28,26,34,0,20],
[30,16,28,28,20,18,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 115, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,36,23,33,21,39,46],
[18,0,25,24,13,11,41,34],
[14,25,0,26,20,26,33,39],
[27,26,24,0,20,20,35,33],
[17,37,30,30,0,22,40,34],
[29,39,24,30,28,0,47,46],
[11,9,17,15,10,3,0,29],
[4,16,11,17,16,4,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 116, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,25,26,24,22,27,24],
[31,0,26,21,26,21,27,24],
[25,24,0,19,23,14,22,21],
[24,29,31,0,30,14,24,26],
[26,24,27,20,0,18,21,23],
[28,29,36,36,32,0,21,32],
[23,23,28,26,29,29,0,21],
[26,26,29,24,27,18,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 117, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,31,26,27,22,27,27],
[29,0,31,24,33,27,33,28],
[19,19,0,23,29,21,23,25],
[24,26,27,0,25,27,24,25],
[23,17,21,25,0,21,21,23],
[28,23,29,23,29,0,25,26],
[23,17,27,26,29,25,0,28],
[23,22,25,25,27,24,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 118, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,25,27,19,22,22,22],
[26,0,28,24,30,22,29,26],
[25,22,0,27,25,25,26,27],
[23,26,23,0,24,24,27,21],
[31,20,25,26,0,24,28,29],
[28,28,25,26,26,0,29,30],
[28,21,24,23,22,21,0,29],
[28,24,23,29,21,20,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 119, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,29,28,16,20,27,29],
[23,0,26,32,22,25,26,26],
[21,24,0,24,19,18,27,30],
[22,18,26,0,22,14,15,25],
[34,28,31,28,0,28,24,33],
[30,25,32,36,22,0,34,31],
[23,24,23,35,26,16,0,33],
[21,24,20,25,17,19,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 120, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,28,20,32,28,28,35],
[25,0,20,27,33,28,24,23],
[22,30,0,32,28,35,25,28],
[30,23,18,0,28,20,24,24],
[18,17,22,22,0,25,21,15],
[22,22,15,30,25,0,23,23],
[22,26,25,26,29,27,0,26],
[15,27,22,26,35,27,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 121, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,26,30,20,32,29,27],
[25,0,19,26,28,27,26,26],
[24,31,0,32,35,31,33,32],
[20,24,18,0,21,23,25,26],
[30,22,15,29,0,26,24,27],
[18,23,19,27,24,0,28,21],
[21,24,17,25,26,22,0,22],
[23,24,18,24,23,29,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 122, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,31,26,29,21,25,24],
[30,0,38,28,29,21,20,17],
[19,12,0,16,25,14,14,17],
[24,22,34,0,36,24,26,30],
[21,21,25,14,0,18,19,24],
[29,29,36,26,32,0,25,30],
[25,30,36,24,31,25,0,39],
[26,33,33,20,26,20,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 123, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,28,25,22,18,20,21],
[32,0,27,22,28,27,22,28],
[22,23,0,27,26,20,24,24],
[25,28,23,0,27,30,27,28],
[28,22,24,23,0,22,27,17],
[32,23,30,20,28,0,25,22],
[30,28,26,23,23,25,0,23],
[29,22,26,22,33,28,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 124, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,19,26,18,16,24,21],
[24,0,23,30,27,32,39,28],
[31,27,0,24,27,31,34,35],
[24,20,26,0,24,26,30,21],
[32,23,23,26,0,28,30,31],
[34,18,19,24,22,0,36,24],
[26,11,16,20,20,14,0,21],
[29,22,15,29,19,26,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 125, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,22,25,31,29,30,32],
[22,0,26,25,24,28,25,31],
[28,24,0,27,28,29,30,35],
[25,25,23,0,31,29,24,28],
[19,26,22,19,0,29,28,30],
[21,22,21,21,21,0,24,26],
[20,25,20,26,22,26,0,31],
[18,19,15,22,20,24,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 126, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,18,26,35,34,30,24],
[27,0,22,24,25,32,24,24],
[32,28,0,23,33,37,33,30],
[24,26,27,0,26,36,32,21],
[15,25,17,24,0,32,27,25],
[16,18,13,14,18,0,18,15],
[20,26,17,18,23,32,0,29],
[26,26,20,29,25,35,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 127, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,19,25,24,24,26,32],
[24,0,28,27,23,25,22,36],
[31,22,0,28,24,29,31,30],
[25,23,22,0,22,24,23,24],
[26,27,26,28,0,21,29,34],
[26,25,21,26,29,0,25,30],
[24,28,19,27,21,25,0,34],
[18,14,20,26,16,20,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 128, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,27,25,23,17,29,29],
[24,0,25,19,14,15,19,20],
[23,25,0,20,15,19,21,17],
[25,31,30,0,23,30,31,30],
[27,36,35,27,0,19,23,34],
[33,35,31,20,31,0,31,31],
[21,31,29,19,27,19,0,33],
[21,30,33,20,16,19,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 129, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,24,35,27,34,25,32],
[17,0,21,29,23,30,16,23],
[26,29,0,33,31,33,22,33],
[15,21,17,0,23,30,19,19],
[23,27,19,27,0,29,18,29],
[16,20,17,20,21,0,18,27],
[25,34,28,31,32,32,0,31],
[18,27,17,31,21,23,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 130, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,29,32,26,29,23,37],
[23,0,23,22,29,31,15,36],
[21,27,0,27,30,29,27,38],
[18,28,23,0,28,29,26,28],
[24,21,20,22,0,35,23,32],
[21,19,21,21,15,0,19,27],
[27,35,23,24,27,31,0,33],
[13,14,12,22,18,23,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 131, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,29,32,31,16,21,35],
[25,0,27,28,31,25,23,22],
[21,23,0,27,31,22,18,28],
[18,22,23,0,27,16,18,31],
[19,19,19,23,0,17,19,25],
[34,25,28,34,33,0,27,35],
[29,27,32,32,31,23,0,36],
[15,28,22,19,25,15,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 132, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,25,35,32,22,29,29],
[22,0,20,37,26,22,26,24],
[25,30,0,29,30,24,23,26],
[15,13,21,0,26,16,14,23],
[18,24,20,24,0,25,19,23],
[28,28,26,34,25,0,27,27],
[21,24,27,36,31,23,0,30],
[21,26,24,27,27,23,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 133, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,27,25,26,35,26,28],
[19,0,22,27,23,29,20,26],
[23,28,0,24,29,34,25,26],
[25,23,26,0,27,26,23,25],
[24,27,21,23,0,28,23,27],
[15,21,16,24,22,0,18,19],
[24,30,25,27,27,32,0,32],
[22,24,24,25,23,31,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 134, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,15,19,18,25,25,30],
[28,0,15,15,22,27,30,24],
[35,35,0,33,22,31,29,30],
[31,35,17,0,25,25,28,25],
[32,28,28,25,0,31,34,25],
[25,23,19,25,19,0,29,22],
[25,20,21,22,16,21,0,25],
[20,26,20,25,25,28,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 135, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,25,33,23,28,24,27],
[20,0,25,32,27,18,19,27],
[25,25,0,39,28,23,19,24],
[17,18,11,0,15,18,12,16],
[27,23,22,35,0,22,24,17],
[22,32,27,32,28,0,25,26],
[26,31,31,38,26,25,0,21],
[23,23,26,34,33,24,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 136, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,30,30,26,21,35,20],
[18,0,19,18,17,23,19,21],
[20,31,0,20,23,24,28,23],
[20,32,30,0,25,30,27,30],
[24,33,27,25,0,23,28,23],
[29,27,26,20,27,0,29,15],
[15,31,22,23,22,21,0,11],
[30,29,27,20,27,35,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 137, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,21,17,13,16,23,28],
[31,0,39,36,33,32,21,37],
[29,11,0,33,35,13,20,23],
[33,14,17,0,15,6,28,25],
[37,17,15,35,0,13,31,25],
[34,18,37,44,37,0,29,33],
[27,29,30,22,19,21,0,31],
[22,13,27,25,25,17,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 138, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,25,26,26,30,28,20],
[17,0,18,14,22,21,24,18],
[25,32,0,24,19,26,28,24],
[24,36,26,0,23,31,29,24],
[24,28,31,27,0,25,32,25],
[20,29,24,19,25,0,26,22],
[22,26,22,21,18,24,0,22],
[30,32,26,26,25,28,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 139, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,30,29,28,26,21,24],
[29,0,23,25,31,28,21,28],
[20,27,0,20,26,27,22,24],
[21,25,30,0,27,23,24,29],
[22,19,24,23,0,20,20,22],
[24,22,23,27,30,0,18,27],
[29,29,28,26,30,32,0,24],
[26,22,26,21,28,23,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 140, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,24,32,22,29,26,28],
[29,0,23,33,23,28,25,26],
[26,27,0,30,23,24,33,15],
[18,17,20,0,17,19,22,21],
[28,27,27,33,0,25,34,25],
[21,22,26,31,25,0,30,29],
[24,25,17,28,16,20,0,20],
[22,24,35,29,25,21,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 141, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,24,27,23,30,25,25],
[31,0,25,29,29,29,25,23],
[26,25,0,33,24,35,31,27],
[23,21,17,0,27,20,19,21],
[27,21,26,23,0,26,24,18],
[20,21,15,30,24,0,23,22],
[25,25,19,31,26,27,0,27],
[25,27,23,29,32,28,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 142, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,20,26,21,27,26,32],
[25,0,22,22,24,24,25,27],
[30,28,0,19,21,30,24,30],
[24,28,31,0,24,33,26,29],
[29,26,29,26,0,24,26,31],
[23,26,20,17,26,0,23,29],
[24,25,26,24,24,27,0,33],
[18,23,20,21,19,21,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 143, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,23,26,28,29,31,28],
[19,0,26,21,27,30,26,28],
[27,24,0,22,29,33,26,28],
[24,29,28,0,28,30,33,30],
[22,23,21,22,0,24,27,22],
[21,20,17,20,26,0,20,23],
[19,24,24,17,23,30,0,23],
[22,22,22,20,28,27,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 144, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,27,22,29,21,24,22],
[25,0,24,24,23,25,23,26],
[23,26,0,30,30,23,25,27],
[28,26,20,0,27,27,25,33],
[21,27,20,23,0,22,21,29],
[29,25,27,23,28,0,28,30],
[26,27,25,25,29,22,0,32],
[28,24,23,17,21,20,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 145, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,22,18,18,15,23,25],
[21,0,23,19,26,26,25,19],
[28,27,0,24,28,24,26,25],
[32,31,26,0,27,23,23,22],
[32,24,22,23,0,25,27,22],
[35,24,26,27,25,0,23,23],
[27,25,24,27,23,27,0,24],
[25,31,25,28,28,27,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 146, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,30,29,25,25,31,28],
[22,0,22,21,22,25,29,24],
[20,28,0,20,20,21,38,23],
[21,29,30,0,35,30,32,23],
[25,28,30,15,0,26,35,22],
[25,25,29,20,24,0,26,21],
[19,21,12,18,15,24,0,21],
[22,26,27,27,28,29,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 147, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,20,20,27,24,23,27],
[30,0,26,20,36,26,26,22],
[30,24,0,20,33,18,21,29],
[30,30,30,0,40,23,32,34],
[23,14,17,10,0,10,17,13],
[26,24,32,27,40,0,27,29],
[27,24,29,18,33,23,0,21],
[23,28,21,16,37,21,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 148, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,15,17,16,31,27,17],
[29,0,20,32,28,29,22,25],
[35,30,0,41,29,31,24,27],
[33,18,9,0,23,28,25,22],
[34,22,21,27,0,31,29,27],
[19,21,19,22,19,0,22,26],
[23,28,26,25,21,28,0,22],
[33,25,23,28,23,24,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 149, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,24,26,23,26,19,20],
[26,0,29,29,28,24,30,28],
[26,21,0,12,25,29,23,25],
[24,21,38,0,27,17,29,28],
[27,22,25,23,0,28,24,25],
[24,26,21,33,22,0,24,21],
[31,20,27,21,26,26,0,30],
[30,22,25,22,25,29,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 150, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,23,20,23,21,27,29],
[25,0,24,26,27,23,36,34],
[27,26,0,22,26,21,27,30],
[30,24,28,0,27,26,29,31],
[27,23,24,23,0,21,27,28],
[29,27,29,24,29,0,31,30],
[23,14,23,21,23,19,0,25],
[21,16,20,19,22,20,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 151, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,38,33,5,27,14,25],
[34,0,50,34,27,39,33,21],
[12,0,0,9,17,0,9,0],
[17,16,41,0,17,17,5,28],
[45,23,33,33,0,33,21,32],
[23,11,50,33,17,0,21,32],
[36,17,41,45,29,29,0,28],
[25,29,50,22,18,18,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 152, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,23,30,22,18,20,25],
[28,0,28,18,23,24,17,26],
[27,22,0,24,24,20,17,23],
[20,32,26,0,20,22,28,28],
[28,27,26,30,0,30,21,30],
[32,26,30,28,20,0,19,25],
[30,33,33,22,29,31,0,28],
[25,24,27,22,20,25,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 153, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,27,27,25,25,25,20],
[24,0,26,22,31,30,27,25],
[23,24,0,24,31,23,22,23],
[23,28,26,0,26,26,25,22],
[25,19,19,24,0,22,24,19],
[25,20,27,24,28,0,23,22],
[25,23,28,25,26,27,0,24],
[30,25,27,28,31,28,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 154, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,8,18,15,30,20,23],
[44,0,44,27,9,24,44,32],
[42,6,0,18,15,30,50,38],
[32,23,32,0,15,30,32,32],
[35,41,35,35,0,50,35,23],
[20,26,20,20,0,0,20,8],
[30,6,0,18,15,30,0,30],
[27,18,12,18,27,42,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 155, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,20,17,22,26,28,21],
[27,0,22,19,25,27,30,31],
[30,28,0,25,29,32,30,21],
[33,31,25,0,25,31,40,28],
[28,25,21,25,0,24,34,28],
[24,23,18,19,26,0,30,26],
[22,20,20,10,16,20,0,19],
[29,19,29,22,22,24,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 156, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,23,29,23,29,24,26],
[21,0,24,31,18,30,25,19],
[27,26,0,29,28,34,24,31],
[21,19,21,0,16,26,21,22],
[27,32,22,34,0,27,28,28],
[21,20,16,24,23,0,16,24],
[26,25,26,29,22,34,0,30],
[24,31,19,28,22,26,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 157, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,23,14,17,10,16,9],
[12,0,8,10,21,10,10,9],
[27,42,0,17,28,27,27,27],
[36,40,33,0,25,34,18,34],
[33,29,22,25,0,24,16,21],
[40,40,23,16,26,0,18,34],
[34,40,23,32,34,32,0,26],
[41,41,23,16,29,16,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 158, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,30,28,25,30,33,30],
[30,0,24,28,28,31,37,28],
[20,26,0,19,24,27,24,27],
[22,22,31,0,24,34,30,35],
[25,22,26,26,0,24,31,29],
[20,19,23,16,26,0,21,17],
[17,13,26,20,19,29,0,25],
[20,22,23,15,21,33,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 159, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,19,24,27,27,25,25],
[26,0,23,22,27,32,28,23],
[31,27,0,30,24,27,31,20],
[26,28,20,0,25,25,24,25],
[23,23,26,25,0,24,29,24],
[23,18,23,25,26,0,24,21],
[25,22,19,26,21,26,0,20],
[25,27,30,25,26,29,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 160, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,31,25,23,24,24,29],
[16,0,20,18,18,20,18,21],
[19,30,0,28,24,25,25,27],
[25,32,22,0,24,25,21,30],
[27,32,26,26,0,24,26,31],
[26,30,25,25,26,0,29,31],
[26,32,25,29,24,21,0,27],
[21,29,23,20,19,19,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 161, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,25,21,25,18,12,5],
[29,0,29,18,29,25,24,21],
[25,21,0,10,22,28,17,21],
[29,32,40,0,34,24,19,31],
[25,21,28,16,0,15,7,12],
[32,25,22,26,35,0,11,22],
[38,26,33,31,43,39,0,23],
[45,29,29,19,38,28,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 162, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,30,29,29,27,32,24],
[21,0,24,24,25,22,28,23],
[20,26,0,24,28,22,27,26],
[21,26,26,0,25,20,26,23],
[21,25,22,25,0,22,25,28],
[23,28,28,30,28,0,24,23],
[18,22,23,24,25,26,0,23],
[26,27,24,27,22,27,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 163, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,27,21,29,28,30,31],
[22,0,30,25,31,27,32,30],
[23,20,0,24,30,29,22,25],
[29,25,26,0,36,27,26,28],
[21,19,20,14,0,21,21,26],
[22,23,21,23,29,0,25,24],
[20,18,28,24,29,25,0,25],
[19,20,25,22,24,26,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 164, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,29,20,30,19,23,32],
[23,0,30,28,32,21,26,29],
[21,20,0,21,24,14,19,22],
[30,22,29,0,31,9,18,20],
[20,18,26,19,0,16,20,24],
[31,29,36,41,34,0,24,28],
[27,24,31,32,30,26,0,27],
[18,21,28,30,26,22,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 165, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,27,23,19,24,21,20],
[25,0,28,24,22,27,23,26],
[23,22,0,25,25,23,22,23],
[27,26,25,0,20,30,25,21],
[31,28,25,30,0,32,24,25],
[26,23,27,20,18,0,16,19],
[29,27,28,25,26,34,0,25],
[30,24,27,29,25,31,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 166, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,12,31,30,22,24,11],
[28,0,15,24,38,25,27,27],
[38,35,0,36,43,24,33,29],
[19,26,14,0,29,22,27,15],
[20,12,7,21,0,16,12,12],
[28,25,26,28,34,0,28,15],
[26,23,17,23,38,22,0,22],
[39,23,21,35,38,35,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 167, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,25,22,33,25,27,28],
[19,0,23,22,26,22,22,28],
[25,27,0,23,35,28,25,22],
[28,28,27,0,35,30,25,26],
[17,24,15,15,0,22,25,19],
[25,28,22,20,28,0,20,28],
[23,28,25,25,25,30,0,24],
[22,22,28,24,31,22,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 168, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,30,29,27,27,28,25],
[22,0,22,29,23,26,30,21],
[20,28,0,26,23,27,25,20],
[21,21,24,0,22,21,25,23],
[23,27,27,28,0,28,25,26],
[23,24,23,29,22,0,27,21],
[22,20,25,25,25,23,0,22],
[25,29,30,27,24,29,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 169, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,20,23,24,22,24,28],
[29,0,23,19,23,19,25,29],
[30,27,0,28,23,23,21,29],
[27,31,22,0,28,26,28,28],
[26,27,27,22,0,23,26,28],
[28,31,27,24,27,0,24,32],
[26,25,29,22,24,26,0,24],
[22,21,21,22,22,18,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 170, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,20,27,21,22,28,27],
[24,0,27,30,25,24,19,29],
[30,23,0,35,16,13,21,18],
[23,20,15,0,14,12,12,17],
[29,25,34,36,0,24,24,22],
[28,26,37,38,26,0,31,25],
[22,31,29,38,26,19,0,27],
[23,21,32,33,28,25,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 171, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,23,20,25,19,22,25],
[30,0,28,27,31,26,23,34],
[27,22,0,28,31,23,27,25],
[30,23,22,0,33,24,27,28],
[25,19,19,17,0,21,20,21],
[31,24,27,26,29,0,29,31],
[28,27,23,23,30,21,0,28],
[25,16,25,22,29,19,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 172, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,30,32,30,31,29,25],
[24,0,27,33,21,25,28,23],
[20,23,0,28,18,26,22,21],
[18,17,22,0,17,20,22,15],
[20,29,32,33,0,30,30,27],
[19,25,24,30,20,0,29,26],
[21,22,28,28,20,21,0,24],
[25,27,29,35,23,24,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 173, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,21,26,25,22,26,23],
[18,0,19,26,23,20,23,20],
[29,31,0,27,25,25,26,28],
[24,24,23,0,29,21,19,18],
[25,27,25,21,0,21,18,25],
[28,30,25,29,29,0,28,25],
[24,27,24,31,32,22,0,24],
[27,30,22,32,25,25,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 174, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,35,27,18,30,24,25],
[21,0,26,19,19,27,17,19],
[15,24,0,18,17,21,21,15],
[23,31,32,0,22,27,30,23],
[32,31,33,28,0,31,20,26],
[20,23,29,23,19,0,17,21],
[26,33,29,20,30,33,0,30],
[25,31,35,27,24,29,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 175, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,33,32,20,26,27,28],
[15,0,27,22,21,31,27,22],
[17,23,0,24,21,23,20,18],
[18,28,26,0,21,21,24,18],
[30,29,29,29,0,23,27,17],
[24,19,27,29,27,0,30,23],
[23,23,30,26,23,20,0,21],
[22,28,32,32,33,27,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 176, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,17,25,16,23,20,26],
[33,0,19,22,20,28,25,27],
[33,31,0,30,29,32,25,24],
[25,28,20,0,23,26,24,28],
[34,30,21,27,0,28,28,29],
[27,22,18,24,22,0,21,22],
[30,25,25,26,22,29,0,27],
[24,23,26,22,21,28,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 177, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,27,25,25,28,25,28],
[20,0,17,22,24,20,16,25],
[23,33,0,22,24,20,27,30],
[25,28,28,0,25,24,22,27],
[25,26,26,25,0,25,21,26],
[22,30,30,26,25,0,25,34],
[25,34,23,28,29,25,0,32],
[22,25,20,23,24,16,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 178, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,29,29,23,22,20,20],
[30,0,15,24,16,22,13,15],
[21,35,0,18,21,28,14,14],
[21,26,32,0,33,26,24,26],
[27,34,29,17,0,31,22,29],
[28,28,22,24,19,0,13,19],
[30,37,36,26,28,37,0,21],
[30,35,36,24,21,31,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 179, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,23,21,28,20,21,29],
[26,0,20,22,23,23,18,30],
[27,30,0,32,30,33,25,35],
[29,28,18,0,26,27,20,31],
[22,27,20,24,0,24,24,36],
[30,27,17,23,26,0,18,28],
[29,32,25,30,26,32,0,33],
[21,20,15,19,14,22,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 180, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,19,23,23,27,25,21],
[24,0,25,27,28,24,25,28],
[31,25,0,24,23,23,29,27],
[27,23,26,0,24,29,27,28],
[27,22,27,26,0,25,21,20],
[23,26,27,21,25,0,27,23],
[25,25,21,23,29,23,0,22],
[29,22,23,22,30,27,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 181, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,29,27,31,21,27,23],
[24,0,24,27,30,24,27,27],
[21,26,0,27,33,25,19,26],
[23,23,23,0,28,17,23,23],
[19,20,17,22,0,24,23,18],
[29,26,25,33,26,0,24,25],
[23,23,31,27,27,26,0,25],
[27,23,24,27,32,25,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 182, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,25,34,17,28,30,24],
[26,0,25,32,33,38,35,30],
[25,25,0,28,25,30,32,36],
[16,18,22,0,27,27,27,38],
[33,17,25,23,0,25,24,32],
[22,12,20,23,25,0,25,24],
[20,15,18,23,26,25,0,21],
[26,20,14,12,18,26,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 183, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,22,26,25,28,28,20],
[19,0,21,11,22,23,19,25],
[28,29,0,19,32,25,29,25],
[24,39,31,0,32,32,30,28],
[25,28,18,18,0,26,27,21],
[22,27,25,18,24,0,25,20],
[22,31,21,20,23,25,0,22],
[30,25,25,22,29,30,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 184, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,22,28,32,24,24,27],
[21,0,24,25,25,26,24,22],
[28,26,0,22,24,25,27,22],
[22,25,28,0,28,32,28,28],
[18,25,26,22,0,20,27,24],
[26,24,25,18,30,0,27,24],
[26,26,23,22,23,23,0,26],
[23,28,28,22,26,26,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 185, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,20,21,21,20,20,30],
[25,0,23,30,19,25,16,30],
[30,27,0,29,22,30,22,32],
[29,20,21,0,21,28,17,27],
[29,31,28,29,0,26,25,29],
[30,25,20,22,24,0,21,31],
[30,34,28,33,25,29,0,38],
[20,20,18,23,21,19,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 186, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,26,22,26,29,26,36],
[23,0,21,21,25,20,20,29],
[24,29,0,22,24,30,24,31],
[28,29,28,0,28,29,25,31],
[24,25,26,22,0,26,25,33],
[21,30,20,21,24,0,21,29],
[24,30,26,25,25,29,0,37],
[14,21,19,19,17,21,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 187, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,28,20,28,28,24,26],
[28,0,30,30,30,27,27,21],
[22,20,0,23,24,24,24,28],
[30,20,27,0,28,32,26,23],
[22,20,26,22,0,19,23,20],
[22,23,26,18,31,0,26,19],
[26,23,26,24,27,24,0,24],
[24,29,22,27,30,31,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 188, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,25,21,23,24,21,27],
[20,0,23,17,20,23,22,30],
[25,27,0,27,25,27,22,27],
[29,33,23,0,23,25,24,34],
[27,30,25,27,0,24,26,31],
[26,27,23,25,26,0,31,31],
[29,28,28,26,24,19,0,31],
[23,20,23,16,19,19,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 189, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,20,21,27,20,25,24],
[26,0,30,24,25,25,29,29],
[30,20,0,26,27,22,26,23],
[29,26,24,0,28,28,25,23],
[23,25,23,22,0,20,19,23],
[30,25,28,22,30,0,28,21],
[25,21,24,25,31,22,0,25],
[26,21,27,27,27,29,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 190, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,21,29,20,28,23,29],
[28,0,32,36,31,29,30,24],
[29,18,0,28,25,23,30,24],
[21,14,22,0,28,20,22,17],
[30,19,25,22,0,24,28,22],
[22,21,27,30,26,0,30,21],
[27,20,20,28,22,20,0,21],
[21,26,26,33,28,29,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 191, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,13,31,40,25,31,49],
[7,0,10,23,7,1,7,21],
[37,40,0,31,32,32,22,45],
[19,27,19,0,20,19,18,18],
[10,43,18,30,0,25,34,43],
[25,49,18,31,25,0,15,33],
[19,43,28,32,16,35,0,44],
[1,29,5,32,7,17,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 192, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,25,29,30,26,49,29],
[14,0,25,17,26,9,32,33],
[25,25,0,12,20,20,39,23],
[21,33,38,0,35,25,48,47],
[20,24,30,15,0,15,22,30],
[24,41,30,25,35,0,39,39],
[1,18,11,2,28,11,0,21],
[21,17,27,3,20,11,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 193, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,0,12,22,17,12,20],
[31,0,25,27,28,27,25,30],
[50,25,0,37,38,27,34,20],
[38,23,13,0,35,20,18,23],
[28,22,12,15,0,7,12,15],
[33,23,23,30,43,0,33,23],
[38,25,16,32,38,17,0,10],
[30,20,30,27,35,27,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 194, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,26,28,25,25,31,30],
[23,0,25,30,28,26,25,27],
[24,25,0,28,23,29,26,29],
[22,20,22,0,23,24,19,22],
[25,22,27,27,0,21,23,27],
[25,24,21,26,29,0,26,31],
[19,25,24,31,27,24,0,28],
[20,23,21,28,23,19,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 195, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,25,28,28,31,29,29],
[14,0,16,20,20,20,19,19],
[25,34,0,28,32,34,28,31],
[22,30,22,0,18,21,22,23],
[22,30,18,32,0,27,29,24],
[19,30,16,29,23,0,23,23],
[21,31,22,28,21,27,0,25],
[21,31,19,27,26,27,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 196, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,21,26,29,29,29,25],
[21,0,23,30,29,24,27,23],
[29,27,0,24,31,24,30,24],
[24,20,26,0,26,20,26,18],
[21,21,19,24,0,22,26,23],
[21,26,26,30,28,0,26,28],
[21,23,20,24,24,24,0,20],
[25,27,26,32,27,22,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 197, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,21,23,29,31,27,36],
[24,0,29,27,19,27,17,31],
[29,21,0,27,30,23,33,42],
[27,23,23,0,26,26,27,35],
[21,31,20,24,0,14,20,34],
[19,23,27,24,36,0,26,32],
[23,33,17,23,30,24,0,29],
[14,19,8,15,16,18,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 198, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,20,24,24,27,21,22],
[29,0,25,26,25,25,24,29],
[30,25,0,30,26,31,26,30],
[26,24,20,0,20,23,21,21],
[26,25,24,30,0,30,29,30],
[23,25,19,27,20,0,25,28],
[29,26,24,29,21,25,0,28],
[28,21,20,29,20,22,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 199, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,33,15,20,15,18,19],
[30,0,27,19,21,27,22,20],
[17,23,0,18,17,19,15,14],
[35,31,32,0,25,35,32,29],
[30,29,33,25,0,28,27,29],
[35,23,31,15,22,0,26,22],
[32,28,35,18,23,24,0,22],
[31,30,36,21,21,28,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda3(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 50, 200, "ME-RCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mercw/mercw_8_50.csv", index=False, header=False)