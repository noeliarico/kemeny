
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,33,29,33,25,31,32,28,29],
[18,0,25,25,25,28,30,29,24],
[22,26,0,25,25,23,20,28,25],
[18,26,26,0,27,25,25,28,23],
[26,26,26,24,0,27,26,31,29],
[20,23,28,26,24,0,23,27,23],
[19,21,31,26,25,28,0,30,25],
[23,22,23,23,20,24,21,0,23],
[22,27,26,28,22,28,26,28,0]])



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
result = np.append(np.array([9, 51, 1, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,27,29,29,21,33,29,27],
[20,0,23,23,30,24,29,24,20],
[24,28,0,31,29,26,29,32,26],
[22,28,20,0,23,21,29,24,20],
[22,21,22,28,0,18,31,28,23],
[30,27,25,30,33,0,33,33,24],
[18,22,22,22,20,18,0,24,18],
[22,27,19,27,23,18,27,0,20],
[24,31,25,31,28,27,33,31,0]])



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
result = np.append(np.array([9, 51, 2, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,11,40,41,50,19,50,34],
[18,0,27,18,17,17,18,17,11],
[40,24,0,40,40,40,17,41,34],
[11,33,11,0,1,33,2,10,34],
[10,34,11,50,0,49,27,50,34],
[1,34,11,18,2,0,18,2,34],
[32,33,34,49,24,33,0,33,34],
[1,34,10,41,1,49,18,0,34],
[17,40,17,17,17,17,17,17,0]])



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
result = np.append(np.array([9, 51, 3, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,29,33,28,35,25,28,33],
[17,0,25,21,23,30,27,23,29],
[22,26,0,24,25,32,31,32,29],
[18,30,27,0,22,27,24,23,26],
[23,28,26,29,0,27,25,24,23],
[16,21,19,24,24,0,25,24,21],
[26,24,20,27,26,26,0,27,34],
[23,28,19,28,27,27,24,0,34],
[18,22,22,25,28,30,17,17,0]])



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
result = np.append(np.array([9, 51, 4, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,33,34,31,20,27,36,23],
[17,0,27,32,24,19,17,26,20],
[18,24,0,37,24,20,19,27,29],
[17,19,14,0,23,22,22,23,26],
[20,27,27,28,0,27,22,25,20],
[31,32,31,29,24,0,27,30,23],
[24,34,32,29,29,24,0,22,22],
[15,25,24,28,26,21,29,0,19],
[28,31,22,25,31,28,29,32,0]])



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
result = np.append(np.array([9, 51, 5, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,32,28,26,19,30,31,24],
[18,0,27,18,23,11,27,36,20],
[19,24,0,22,28,10,27,32,22],
[23,33,29,0,34,26,34,42,31],
[25,28,23,17,0,13,23,27,28],
[32,40,41,25,38,0,33,45,37],
[21,24,24,17,28,18,0,27,29],
[20,15,19,9,24,6,24,0,19],
[27,31,29,20,23,14,22,32,0]])



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
result = np.append(np.array([9, 51, 6, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,12,17,15,21,31,17,28],
[27,0,19,27,19,23,22,21,29],
[39,32,0,27,34,31,29,16,34],
[34,24,24,0,32,37,28,27,30],
[36,32,17,19,0,31,25,24,33],
[30,28,20,14,20,0,19,22,25],
[20,29,22,23,26,32,0,14,28],
[34,30,35,24,27,29,37,0,31],
[23,22,17,21,18,26,23,20,0]])



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
result = np.append(np.array([9, 51, 7, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,35,18,18,34,35,34,18],
[0,0,18,18,0,34,0,16,18],
[16,33,0,34,16,16,0,16,16],
[33,33,17,0,33,33,17,16,17],
[33,51,35,18,0,34,35,34,18],
[17,17,35,18,17,0,17,16,17],
[16,51,51,34,16,34,0,16,34],
[17,35,35,35,17,35,35,0,35],
[33,33,35,34,33,34,17,16,0]])



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
result = np.append(np.array([9, 51, 8, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,30,24,22,23,24,29,24],
[25,0,30,26,22,28,26,28,27],
[21,21,0,24,20,19,24,26,19],
[27,25,27,0,21,20,22,29,25],
[29,29,31,30,0,23,25,28,31],
[28,23,32,31,28,0,28,29,29],
[27,25,27,29,26,23,0,28,28],
[22,23,25,22,23,22,23,0,24],
[27,24,32,26,20,22,23,27,0]])



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
result = np.append(np.array([9, 51, 9, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,15,15,8,15,25,34,21],
[31,0,14,2,20,21,21,28,21],
[36,37,0,24,30,22,36,28,28],
[36,49,27,0,25,38,32,41,32],
[43,31,21,26,0,43,30,35,26],
[36,30,29,13,8,0,14,37,12],
[26,30,15,19,21,37,0,23,22],
[17,23,23,10,16,14,28,0,8],
[30,30,23,19,25,39,29,43,0]])



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
result = np.append(np.array([9, 51, 10, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,31,30,40,23,33,28,27],
[20,0,36,31,31,33,23,29,28],
[20,15,0,25,24,15,18,14,18],
[21,20,26,0,24,22,17,26,26],
[11,20,27,27,0,22,26,18,22],
[28,18,36,29,29,0,27,23,27],
[18,28,33,34,25,24,0,25,30],
[23,22,37,25,33,28,26,0,25],
[24,23,33,25,29,24,21,26,0]])



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
result = np.append(np.array([9, 51, 11, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,25,34,26,25,24,30,28],
[25,0,19,23,23,21,23,26,25],
[26,32,0,28,25,26,26,31,29],
[17,28,23,0,23,21,18,22,24],
[25,28,26,28,0,22,23,23,20],
[26,30,25,30,29,0,20,30,28],
[27,28,25,33,28,31,0,28,33],
[21,25,20,29,28,21,23,0,30],
[23,26,22,27,31,23,18,21,0]])



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
result = np.append(np.array([9, 51, 12, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,28,26,28,25,26,24,28],
[19,0,21,19,12,17,17,16,34],
[23,30,0,30,25,24,21,26,29],
[25,32,21,0,19,29,25,28,29],
[23,39,26,32,0,28,24,25,32],
[26,34,27,22,23,0,27,25,35],
[25,34,30,26,27,24,0,23,28],
[27,35,25,23,26,26,28,0,33],
[23,17,22,22,19,16,23,18,0]])



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
result = np.append(np.array([9, 51, 13, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,29,17,27,18,26,32,22],
[30,0,31,28,24,18,28,30,23],
[22,20,0,25,28,27,29,24,22],
[34,23,26,0,26,24,31,32,29],
[24,27,23,25,0,24,26,32,30],
[33,33,24,27,27,0,32,33,28],
[25,23,22,20,25,19,0,27,19],
[19,21,27,19,19,18,24,0,25],
[29,28,29,22,21,23,32,26,0]])



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
result = np.append(np.array([9, 51, 14, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,33,19,25,21,29,18,27],
[26,0,30,26,28,30,28,22,29],
[18,21,0,24,23,24,27,23,23],
[32,25,27,0,33,27,33,27,22],
[26,23,28,18,0,21,33,21,30],
[30,21,27,24,30,0,27,22,30],
[22,23,24,18,18,24,0,17,23],
[33,29,28,24,30,29,34,0,24],
[24,22,28,29,21,21,28,27,0]])



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
result = np.append(np.array([9, 51, 15, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,22,26,33,32,27,24,31],
[24,0,38,25,32,25,32,28,31],
[29,13,0,34,37,26,26,21,34],
[25,26,17,0,34,31,28,22,34],
[18,19,14,17,0,18,29,19,28],
[19,26,25,20,33,0,34,29,36],
[24,19,25,23,22,17,0,21,38],
[27,23,30,29,32,22,30,0,31],
[20,20,17,17,23,15,13,20,0]])



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
result = np.append(np.array([9, 51, 16, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,28,29,23,23,29,25,27],
[21,0,19,19,20,23,23,23,21],
[23,32,0,27,25,26,25,26,29],
[22,32,24,0,24,26,21,25,23],
[28,31,26,27,0,23,27,21,27],
[28,28,25,25,28,0,29,27,31],
[22,28,26,30,24,22,0,24,22],
[26,28,25,26,30,24,27,0,21],
[24,30,22,28,24,20,29,30,0]])



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
result = np.append(np.array([9, 51, 17, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,27,29,21,18,23,30,18],
[29,0,29,20,27,20,27,30,24],
[24,22,0,16,25,23,23,31,22],
[22,31,35,0,32,30,31,35,15],
[30,24,26,19,0,27,29,33,17],
[33,31,28,21,24,0,31,37,25],
[28,24,28,20,22,20,0,38,26],
[21,21,20,16,18,14,13,0,15],
[33,27,29,36,34,26,25,36,0]])



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
result = np.append(np.array([9, 51, 18, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,31,34,26,33,36,31,30],
[34,0,25,27,34,34,37,30,30],
[20,26,0,26,16,39,36,31,36],
[17,24,25,0,11,34,20,9,21],
[25,17,35,40,0,35,50,31,35],
[18,17,12,17,16,0,15,13,8],
[15,14,15,31,1,36,0,14,23],
[20,21,20,42,20,38,37,0,29],
[21,21,15,30,16,43,28,22,0]])



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
result = np.append(np.array([9, 51, 19, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,21,20,23,21,18,21,23],
[24,0,24,11,23,24,42,26,34],
[30,27,0,20,23,21,31,15,23],
[31,40,31,0,23,29,31,23,23],
[28,28,28,28,0,32,29,21,42],
[30,27,30,22,19,0,29,30,21],
[33,9,20,20,22,22,0,35,34],
[30,25,36,28,30,21,16,0,23],
[28,17,28,28,9,30,17,28,0]])



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
result = np.append(np.array([9, 51, 20, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,22,27,29,29,22,21,29],
[29,0,21,23,23,27,21,21,19],
[29,30,0,30,25,26,19,26,26],
[24,28,21,0,23,25,18,20,22],
[22,28,26,28,0,24,23,25,27],
[22,24,25,26,27,0,21,23,21],
[29,30,32,33,28,30,0,24,28],
[30,30,25,31,26,28,27,0,30],
[22,32,25,29,24,30,23,21,0]])



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
result = np.append(np.array([9, 51, 21, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,23,25,27,29,36,23,28],
[29,0,22,26,28,30,34,26,26],
[28,29,0,28,26,26,33,32,25],
[26,25,23,0,26,29,29,29,24],
[24,23,25,25,0,21,32,24,23],
[22,21,25,22,30,0,25,19,24],
[15,17,18,22,19,26,0,17,27],
[28,25,19,22,27,32,34,0,25],
[23,25,26,27,28,27,24,26,0]])



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
result = np.append(np.array([9, 51, 22, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,31,30,32,30,34,26,35],
[26,0,27,28,23,28,30,21,29],
[20,24,0,28,22,29,27,19,27],
[21,23,23,0,24,24,30,21,29],
[19,28,29,27,0,26,29,23,32],
[21,23,22,27,25,0,32,21,30],
[17,21,24,21,22,19,0,19,25],
[25,30,32,30,28,30,32,0,32],
[16,22,24,22,19,21,26,19,0]])



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
result = np.append(np.array([9, 51, 23, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,24,22,32,28,26,34,30],
[22,0,25,27,27,31,24,28,32],
[27,26,0,29,35,27,22,36,35],
[29,24,22,0,27,28,27,28,32],
[19,24,16,24,0,23,24,28,32],
[23,20,24,23,28,0,23,29,26],
[25,27,29,24,27,28,0,28,32],
[17,23,15,23,23,22,23,0,23],
[21,19,16,19,19,25,19,28,0]])



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
result = np.append(np.array([9, 51, 24, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,21,23,25,21,20,24,26],
[27,0,15,21,28,14,18,13,22],
[30,36,0,31,27,25,24,26,27],
[28,30,20,0,23,21,23,24,27],
[26,23,24,28,0,23,20,23,25],
[30,37,26,30,28,0,25,28,29],
[31,33,27,28,31,26,0,24,25],
[27,38,25,27,28,23,27,0,26],
[25,29,24,24,26,22,26,25,0]])



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
result = np.append(np.array([9, 51, 25, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,24,31,30,25,26,35,26],
[22,0,26,25,24,18,24,24,20],
[27,25,0,28,28,26,27,33,24],
[20,26,23,0,24,20,16,23,20],
[21,27,23,27,0,18,19,27,22],
[26,33,25,31,33,0,24,32,30],
[25,27,24,35,32,27,0,34,29],
[16,27,18,28,24,19,17,0,28],
[25,31,27,31,29,21,22,23,0]])



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
result = np.append(np.array([9, 51, 26, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,29,36,27,31,34,23,28],
[32,0,18,35,17,31,19,38,23],
[22,33,0,35,32,42,44,37,19],
[15,16,16,0,17,24,24,16,22],
[24,34,19,34,0,23,22,31,21],
[20,20,9,27,28,0,32,24,15],
[17,32,7,27,29,19,0,29,12],
[28,13,14,35,20,27,22,0,18],
[23,28,32,29,30,36,39,33,0]])



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
result = np.append(np.array([9, 51, 27, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,13,24,18,34,34,23,24],
[20,0,15,4,12,28,8,31,24],
[38,36,0,40,38,36,24,40,24],
[27,47,11,0,21,29,17,39,30],
[33,39,13,30,0,31,16,41,22],
[17,23,15,22,20,0,14,27,14],
[17,43,27,34,35,37,0,39,20],
[28,20,11,12,10,24,12,0,10],
[27,27,27,21,29,37,31,41,0]])



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
result = np.append(np.array([9, 51, 28, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,22,23,30,33,29,28,29],
[18,0,23,25,23,28,26,23,26],
[29,28,0,24,32,31,27,31,28],
[28,26,27,0,30,37,30,31,24],
[21,28,19,21,0,19,26,25,25],
[18,23,20,14,32,0,27,27,28],
[22,25,24,21,25,24,0,25,25],
[23,28,20,20,26,24,26,0,21],
[22,25,23,27,26,23,26,30,0]])



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
result = np.append(np.array([9, 51, 29, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,33,34,29,24,37,30,30],
[21,0,27,23,30,25,26,27,31],
[18,24,0,26,27,17,26,33,24],
[17,28,25,0,25,15,23,20,18],
[22,21,24,26,0,28,28,10,24],
[27,26,34,36,23,0,31,20,27],
[14,25,25,28,23,20,0,26,26],
[21,24,18,31,41,31,25,0,28],
[21,20,27,33,27,24,25,23,0]])



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
result = np.append(np.array([9, 51, 30, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,38,31,25,30,41,23,37],
[24,0,30,27,32,31,31,26,31],
[13,21,0,25,19,21,28,19,25],
[20,24,26,0,18,28,27,22,33],
[26,19,32,33,0,27,33,23,29],
[21,20,30,23,24,0,31,25,28],
[10,20,23,24,18,20,0,17,25],
[28,25,32,29,28,26,34,0,31],
[14,20,26,18,22,23,26,20,0]])



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
result = np.append(np.array([9, 51, 31, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,27,25,28,33,29,34,29],
[22,0,25,21,27,22,22,32,24],
[24,26,0,20,24,35,30,31,22],
[26,30,31,0,26,28,30,31,20],
[23,24,27,25,0,30,28,26,21],
[18,29,16,23,21,0,26,26,23],
[22,29,21,21,23,25,0,26,22],
[17,19,20,20,25,25,25,0,17],
[22,27,29,31,30,28,29,34,0]])



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
result = np.append(np.array([9, 51, 32, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,25,22,23,27,24,21,22],
[24,0,26,28,25,26,26,27,25],
[26,25,0,27,20,24,23,26,24],
[29,23,24,0,27,27,24,24,22],
[28,26,31,24,0,19,27,25,22],
[24,25,27,24,32,0,23,24,22],
[27,25,28,27,24,28,0,24,26],
[30,24,25,27,26,27,27,0,28],
[29,26,27,29,29,29,25,23,0]])



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
result = np.append(np.array([9, 51, 33, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,30,24,32,31,22,33,18],
[20,0,16,24,23,17,19,27,19],
[21,35,0,27,34,13,28,24,24],
[27,27,24,0,26,19,33,32,27],
[19,28,17,25,0,16,23,26,25],
[20,34,38,32,35,0,27,29,22],
[29,32,23,18,28,24,0,27,22],
[18,24,27,19,25,22,24,0,15],
[33,32,27,24,26,29,29,36,0]])



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
result = np.append(np.array([9, 51, 34, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,24,31,26,33,28,27,32],
[24,0,27,26,27,34,27,22,30],
[27,24,0,24,24,31,25,21,29],
[20,25,27,0,24,31,27,20,29],
[25,24,27,27,0,29,26,23,28],
[18,17,20,20,22,0,18,17,20],
[23,24,26,24,25,33,0,23,27],
[24,29,30,31,28,34,28,0,34],
[19,21,22,22,23,31,24,17,0]])



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
result = np.append(np.array([9, 51, 35, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,22,28,25,24,27,26,28],
[22,0,16,14,19,19,11,18,12],
[29,35,0,32,27,30,24,26,20],
[23,37,19,0,18,19,14,20,6],
[26,32,24,33,0,26,25,32,19],
[27,32,21,32,25,0,20,21,26],
[24,40,27,37,26,31,0,32,30],
[25,33,25,31,19,30,19,0,18],
[23,39,31,45,32,25,21,33,0]])



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
result = np.append(np.array([9, 51, 36, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,21,22,21,22,20,28,21],
[37,0,25,26,34,30,34,31,27],
[30,26,0,27,28,26,30,30,22],
[29,25,24,0,25,27,33,26,25],
[30,17,23,26,0,29,28,28,20],
[29,21,25,24,22,0,30,28,20],
[31,17,21,18,23,21,0,24,20],
[23,20,21,25,23,23,27,0,21],
[30,24,29,26,31,31,31,30,0]])



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
result = np.append(np.array([9, 51, 37, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,21,22,28,25,29,21,27],
[29,0,24,16,31,24,19,22,19],
[30,27,0,26,28,35,29,27,23],
[29,35,25,0,26,27,30,26,22],
[23,20,23,25,0,27,25,27,19],
[26,27,16,24,24,0,26,26,22],
[22,32,22,21,26,25,0,20,19],
[30,29,24,25,24,25,31,0,21],
[24,32,28,29,32,29,32,30,0]])



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
result = np.append(np.array([9, 51, 38, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,25,38,23,28,24,26,22],
[23,0,25,30,30,27,28,26,19],
[26,26,0,35,30,27,27,24,20],
[13,21,16,0,26,18,16,17,12],
[28,21,21,25,0,23,18,19,15],
[23,24,24,33,28,0,26,19,22],
[27,23,24,35,33,25,0,26,26],
[25,25,27,34,32,32,25,0,15],
[29,32,31,39,36,29,25,36,0]])



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
result = np.append(np.array([9, 51, 39, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,30,32,27,27,34,24,32],
[24,0,27,33,23,23,23,26,31],
[21,24,0,34,28,26,25,24,32],
[19,18,17,0,23,21,19,23,23],
[24,28,23,28,0,23,24,18,27],
[24,28,25,30,28,0,26,30,31],
[17,28,26,32,27,25,0,25,27],
[27,25,27,28,33,21,26,0,29],
[19,20,19,28,24,20,24,22,0]])



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
result = np.append(np.array([9, 51, 40, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,24,33,27,36,32,31,34],
[17,0,29,17,28,23,22,29,26],
[27,22,0,27,32,29,28,29,33],
[18,34,24,0,30,31,27,38,30],
[24,23,19,21,0,27,26,26,27],
[15,28,22,20,24,0,21,28,28],
[19,29,23,24,25,30,0,31,22],
[20,22,22,13,25,23,20,0,25],
[17,25,18,21,24,23,29,26,0]])



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
result = np.append(np.array([9, 51, 41, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,22,22,23,21,18,19,20],
[28,0,20,23,26,23,29,22,20],
[29,31,0,23,27,29,23,29,28],
[29,28,28,0,27,31,24,25,27],
[28,25,24,24,0,25,22,20,25],
[30,28,22,20,26,0,22,30,22],
[33,22,28,27,29,29,0,30,23],
[32,29,22,26,31,21,21,0,21],
[31,31,23,24,26,29,28,30,0]])



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
result = np.append(np.array([9, 51, 42, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,25,25,22,25,23,24,23],
[23,0,25,21,22,23,22,26,25],
[26,26,0,21,29,26,26,28,24],
[26,30,30,0,25,27,29,30,29],
[29,29,22,26,0,26,28,33,22],
[26,28,25,24,25,0,27,29,26],
[28,29,25,22,23,24,0,29,21],
[27,25,23,21,18,22,22,0,27],
[28,26,27,22,29,25,30,24,0]])



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
result = np.append(np.array([9, 51, 43, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,18,17,17,0,17,25,25],
[34,0,11,10,25,11,25,18,25],
[33,40,0,10,25,0,25,18,25],
[34,41,41,0,34,26,51,19,26],
[34,26,26,17,0,11,36,26,36],
[51,40,51,25,40,0,40,25,25],
[34,26,26,0,15,11,0,8,15],
[26,33,33,32,25,26,43,0,43],
[26,26,26,25,15,26,36,8,0]])



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
result = np.append(np.array([9, 51, 44, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,23,27,27,28,31,30,30],
[24,0,23,21,25,30,25,21,27],
[28,28,0,24,25,32,25,27,24],
[24,30,27,0,28,33,27,27,31],
[24,26,26,23,0,33,22,22,28],
[23,21,19,18,18,0,26,18,22],
[20,26,26,24,29,25,0,28,22],
[21,30,24,24,29,33,23,0,33],
[21,24,27,20,23,29,29,18,0]])



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
result = np.append(np.array([9, 51, 45, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,23,22,22,26,22,25,23],
[28,0,27,25,25,25,21,26,28],
[28,24,0,27,31,26,26,21,26],
[29,26,24,0,24,27,19,24,28],
[29,26,20,27,0,16,28,24,23],
[25,26,25,24,35,0,25,24,27],
[29,30,25,32,23,26,0,27,28],
[26,25,30,27,27,27,24,0,18],
[28,23,25,23,28,24,23,33,0]])



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
result = np.append(np.array([9, 51, 46, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,34,29,29,21,25,27,26],
[21,0,22,26,23,25,16,28,17],
[17,29,0,27,27,23,20,25,17],
[22,25,24,0,21,21,17,18,15],
[22,28,24,30,0,27,19,25,23],
[30,26,28,30,24,0,22,27,23],
[26,35,31,34,32,29,0,27,22],
[24,23,26,33,26,24,24,0,15],
[25,34,34,36,28,28,29,36,0]])



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
result = np.append(np.array([9, 51, 47, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,25,6,20,15,12,26,20],
[37,0,25,30,32,43,38,24,23],
[26,26,0,25,26,38,27,32,20],
[45,21,26,0,26,35,24,26,26],
[31,19,25,25,0,32,24,31,31],
[36,8,13,16,19,0,17,19,24],
[39,13,24,27,27,34,0,25,26],
[25,27,19,25,20,32,26,0,20],
[31,28,31,25,20,27,25,31,0]])



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
result = np.append(np.array([9, 51, 48, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,43,26,25,34,34,26,17],
[17,0,35,35,17,34,18,35,18],
[8,16,0,17,17,25,26,17,8],
[25,16,34,0,33,16,34,25,17],
[26,34,34,18,0,34,17,26,17],
[17,17,26,35,17,0,34,18,26],
[17,33,25,17,34,17,0,17,17],
[25,16,34,26,25,33,34,0,9],
[34,33,43,34,34,25,34,42,0]])



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
result = np.append(np.array([9, 51, 49, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,20,30,21,30,32,35,26],
[33,0,26,37,23,33,34,38,23],
[31,25,0,27,19,17,32,36,19],
[21,14,24,0,12,20,28,35,16],
[30,28,32,39,0,24,39,36,21],
[21,18,34,31,27,0,34,26,22],
[19,17,19,23,12,17,0,25,12],
[16,13,15,16,15,25,26,0,14],
[25,28,32,35,30,29,39,37,0]])



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
result = np.append(np.array([9, 51, 50, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,26,22,30,26,25,30,21],
[21,0,19,30,23,28,29,23,24],
[25,32,0,31,28,34,36,29,26],
[29,21,20,0,27,19,25,25,23],
[21,28,23,24,0,28,31,25,24],
[25,23,17,32,23,0,28,25,34],
[26,22,15,26,20,23,0,38,26],
[21,28,22,26,26,26,13,0,19],
[30,27,25,28,27,17,25,32,0]])



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
result = np.append(np.array([9, 51, 51, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,31,22,24,22,27,29,27],
[25,0,33,27,22,25,30,32,20],
[20,18,0,15,21,21,22,23,22],
[29,24,36,0,26,31,29,35,29],
[27,29,30,25,0,28,28,30,27],
[29,26,30,20,23,0,30,28,23],
[24,21,29,22,23,21,0,29,24],
[22,19,28,16,21,23,22,0,17],
[24,31,29,22,24,28,27,34,0]])



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
result = np.append(np.array([9, 51, 52, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,20,23,25,23,27,20,25],
[33,0,24,25,29,29,28,26,26],
[31,27,0,29,28,32,24,27,30],
[28,26,22,0,26,30,28,27,25],
[26,22,23,25,0,28,22,25,25],
[28,22,19,21,23,0,25,22,25],
[24,23,27,23,29,26,0,26,28],
[31,25,24,24,26,29,25,0,24],
[26,25,21,26,26,26,23,27,0]])



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
result = np.append(np.array([9, 51, 53, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,26,28,26,24,31,24,29],
[27,0,27,24,25,26,30,25,30],
[25,24,0,27,28,25,32,31,27],
[23,27,24,0,25,29,32,28,23],
[25,26,23,26,0,24,28,27,26],
[27,25,26,22,27,0,30,25,29],
[20,21,19,19,23,21,0,23,21],
[27,26,20,23,24,26,28,0,25],
[22,21,24,28,25,22,30,26,0]])



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
result = np.append(np.array([9, 51, 54, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,32,24,30,29,33,31,23],
[20,0,20,21,25,20,24,26,23],
[19,31,0,21,22,19,28,25,27],
[27,30,30,0,34,22,29,24,24],
[21,26,29,17,0,18,28,26,25],
[22,31,32,29,33,0,27,24,26],
[18,27,23,22,23,24,0,21,22],
[20,25,26,27,25,27,30,0,25],
[28,28,24,27,26,25,29,26,0]])



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
result = np.append(np.array([9, 51, 55, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,20,31,27,12,14,24,14],
[37,0,24,30,23,17,9,27,13],
[31,27,0,33,26,16,13,27,16],
[20,21,18,0,26,20,26,26,23],
[24,28,25,25,0,12,28,46,6],
[39,34,35,31,39,0,21,43,30],
[37,42,38,25,23,30,0,37,27],
[27,24,24,25,5,8,14,0,5],
[37,38,35,28,45,21,24,46,0]])



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
result = np.append(np.array([9, 51, 56, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,25,19,27,24,25,21,26],
[25,0,27,23,24,29,23,25,27],
[26,24,0,29,27,26,21,29,28],
[32,28,22,0,29,24,25,31,27],
[24,27,24,22,0,29,28,25,29],
[27,22,25,27,22,0,16,22,26],
[26,28,30,26,23,35,0,26,30],
[30,26,22,20,26,29,25,0,25],
[25,24,23,24,22,25,21,26,0]])



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
result = np.append(np.array([9, 51, 57, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,30,35,26,27,25,28,27],
[27,0,28,32,30,27,26,22,28],
[21,23,0,26,20,24,23,17,24],
[16,19,25,0,20,17,17,13,17],
[25,21,31,31,0,31,26,24,27],
[24,24,27,34,20,0,26,20,26],
[26,25,28,34,25,25,0,24,29],
[23,29,34,38,27,31,27,0,30],
[24,23,27,34,24,25,22,21,0]])



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
result = np.append(np.array([9, 51, 58, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,16,17,25,33,31,37,29],
[18,0,22,18,18,30,34,36,9],
[35,29,0,33,33,45,33,51,24],
[34,33,18,0,27,33,38,40,31],
[26,33,18,24,0,33,40,33,40],
[18,21,6,18,18,0,18,49,22],
[20,17,18,13,11,33,0,36,15],
[14,15,0,11,18,2,15,0,9],
[22,42,27,20,11,29,36,42,0]])



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
result = np.append(np.array([9, 51, 59, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,24,17,27,25,11,17,21],
[23,0,21,24,28,29,27,34,28],
[27,30,0,35,35,25,37,24,21],
[34,27,16,0,25,17,16,23,23],
[24,23,16,26,0,21,23,29,12],
[26,22,26,34,30,0,31,36,29],
[40,24,14,35,28,20,0,22,11],
[34,17,27,28,22,15,29,0,19],
[30,23,30,28,39,22,40,32,0]])



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
result = np.append(np.array([9, 51, 60, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,24,27,29,22,27,27,21],
[28,0,23,26,30,25,25,24,22],
[27,28,0,27,33,28,26,31,24],
[24,25,24,0,30,27,22,28,17],
[22,21,18,21,0,23,18,23,17],
[29,26,23,24,28,0,23,28,27],
[24,26,25,29,33,28,0,32,23],
[24,27,20,23,28,23,19,0,18],
[30,29,27,34,34,24,28,33,0]])



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
result = np.append(np.array([9, 51, 61, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,24,29,18,14,26,23,17],
[36,0,27,30,29,24,37,31,30],
[27,24,0,33,23,23,24,23,26],
[22,21,18,0,22,20,31,22,24],
[33,22,28,29,0,19,36,27,27],
[37,27,28,31,32,0,35,30,25],
[25,14,27,20,15,16,0,18,20],
[28,20,28,29,24,21,33,0,30],
[34,21,25,27,24,26,31,21,0]])



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
result = np.append(np.array([9, 51, 62, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,35,20,27,21,30,20,21],
[20,0,29,24,29,19,23,24,24],
[16,22,0,25,20,21,18,18,23],
[31,27,26,0,21,25,25,18,26],
[24,22,31,30,0,18,27,20,28],
[30,32,30,26,33,0,31,27,23],
[21,28,33,26,24,20,0,26,24],
[31,27,33,33,31,24,25,0,28],
[30,27,28,25,23,28,27,23,0]])



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
result = np.append(np.array([9, 51, 63, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,23,23,21,25,21,18,21],
[26,0,34,28,24,29,28,25,27],
[28,17,0,24,23,23,24,23,18],
[28,23,27,0,26,32,29,23,26],
[30,27,28,25,0,27,24,21,16],
[26,22,28,19,24,0,23,27,21],
[30,23,27,22,27,28,0,20,20],
[33,26,28,28,30,24,31,0,26],
[30,24,33,25,35,30,31,25,0]])



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
result = np.append(np.array([9, 51, 64, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,20,21,22,21,27,28,20],
[31,0,26,24,32,27,27,28,28],
[31,25,0,26,31,32,25,31,29],
[30,27,25,0,26,28,28,27,25],
[29,19,20,25,0,24,27,21,24],
[30,24,19,23,27,0,21,25,23],
[24,24,26,23,24,30,0,24,25],
[23,23,20,24,30,26,27,0,26],
[31,23,22,26,27,28,26,25,0]])



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
result = np.append(np.array([9, 51, 65, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,25,14,25,32,23,34,31],
[16,0,31,14,15,33,22,29,37],
[26,20,0,16,15,32,19,16,25],
[37,37,35,0,23,31,33,42,34],
[26,36,36,28,0,38,21,32,31],
[19,18,19,20,13,0,11,23,24],
[28,29,32,18,30,40,0,25,37],
[17,22,35,9,19,28,26,0,31],
[20,14,26,17,20,27,14,20,0]])



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
result = np.append(np.array([9, 51, 66, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,28,28,33,29,26,29,23],
[19,0,27,37,31,19,24,29,18],
[23,24,0,29,27,32,30,32,31],
[23,14,22,0,26,16,23,21,21],
[18,20,24,25,0,19,26,22,15],
[22,32,19,35,32,0,30,38,31],
[25,27,21,28,25,21,0,26,21],
[22,22,19,30,29,13,25,0,26],
[28,33,20,30,36,20,30,25,0]])



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
result = np.append(np.array([9, 51, 67, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,23,25,29,21,21,26,21],
[24,0,26,26,28,21,24,24,21],
[28,25,0,31,30,23,22,30,19],
[26,25,20,0,32,24,22,31,22],
[22,23,21,19,0,20,17,20,14],
[30,30,28,27,31,0,26,32,19],
[30,27,29,29,34,25,0,32,28],
[25,27,21,20,31,19,19,0,17],
[30,30,32,29,37,32,23,34,0]])



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
result = np.append(np.array([9, 51, 68, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,28,23,26,31,32,22,25],
[29,0,27,26,27,38,25,35,29],
[23,24,0,24,27,34,30,27,30],
[28,25,27,0,25,31,30,31,28],
[25,24,24,26,0,31,33,31,30],
[20,13,17,20,20,0,21,24,22],
[19,26,21,21,18,30,0,22,25],
[29,16,24,20,20,27,29,0,31],
[26,22,21,23,21,29,26,20,0]])



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
result = np.append(np.array([9, 51, 69, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,34,28,32,34,34,23,28],
[21,0,25,24,28,31,25,28,25],
[17,26,0,24,25,25,26,25,25],
[23,27,27,0,30,32,27,26,27],
[19,23,26,21,0,26,30,16,22],
[17,20,26,19,25,0,24,22,18],
[17,26,25,24,21,27,0,22,26],
[28,23,26,25,35,29,29,0,26],
[23,26,26,24,29,33,25,25,0]])



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
result = np.append(np.array([9, 51, 70, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,42,50,51,19,51,50,43],
[0,0,39,39,24,15,33,32,40],
[9,12,0,12,9,19,36,36,4],
[1,12,39,0,1,19,33,33,16],
[0,27,42,50,0,18,51,35,19],
[32,36,32,32,33,0,33,32,25],
[0,18,15,18,0,18,0,32,15],
[1,19,15,18,16,19,19,0,19],
[8,11,47,35,32,26,36,32,0]])



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
result = np.append(np.array([9, 51, 71, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,28,32,26,28,25,27,29],
[19,0,22,21,21,23,21,28,21],
[23,29,0,31,28,33,29,27,30],
[19,30,20,0,24,23,19,23,21],
[25,30,23,27,0,24,25,33,29],
[23,28,18,28,27,0,22,26,28],
[26,30,22,32,26,29,0,31,24],
[24,23,24,28,18,25,20,0,27],
[22,30,21,30,22,23,27,24,0]])



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
result = np.append(np.array([9, 51, 72, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,20,29,26,23,23,33,26],
[24,0,26,27,28,25,26,26,26],
[31,25,0,26,29,31,25,26,29],
[22,24,25,0,27,24,23,25,27],
[25,23,22,24,0,25,20,30,28],
[28,26,20,27,26,0,22,27,28],
[28,25,26,28,31,29,0,31,29],
[18,25,25,26,21,24,20,0,23],
[25,25,22,24,23,23,22,28,0]])



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
result = np.append(np.array([9, 51, 73, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,29,26,35,24,36,24,25],
[30,0,24,22,32,29,40,26,36],
[22,27,0,32,27,23,30,28,20],
[25,29,19,0,26,32,33,23,28],
[16,19,24,25,0,7,37,18,13],
[27,22,28,19,44,0,31,29,17],
[15,11,21,18,14,20,0,14,16],
[27,25,23,28,33,22,37,0,20],
[26,15,31,23,38,34,35,31,0]])



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
result = np.append(np.array([9, 51, 74, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,17,7,18,22,22,11,4],
[41,0,36,36,24,41,45,28,40],
[34,15,0,34,24,39,45,23,22],
[44,15,17,0,24,51,45,28,21],
[33,27,27,27,0,32,38,16,27],
[29,10,12,0,19,0,28,11,21],
[29,6,6,6,13,23,0,29,21],
[40,23,28,23,35,40,22,0,23],
[47,11,29,30,24,30,30,28,0]])



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
result = np.append(np.array([9, 51, 75, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,22,27,27,22,22,24,24],
[30,0,24,24,27,17,24,26,21],
[29,27,0,30,26,20,23,32,20],
[24,27,21,0,28,21,25,24,20],
[24,24,25,23,0,24,23,23,26],
[29,34,31,30,27,0,26,28,25],
[29,27,28,26,28,25,0,25,28],
[27,25,19,27,28,23,26,0,26],
[27,30,31,31,25,26,23,25,0]])



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
result = np.append(np.array([9, 51, 76, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,29,26,28,31,30,28,19],
[25,0,31,30,21,22,31,33,23],
[22,20,0,25,25,24,27,25,27],
[25,21,26,0,31,31,33,36,25],
[23,30,26,20,0,30,28,27,26],
[20,29,27,20,21,0,22,31,24],
[21,20,24,18,23,29,0,32,24],
[23,18,26,15,24,20,19,0,24],
[32,28,24,26,25,27,27,27,0]])



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
result = np.append(np.array([9, 51, 77, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,22,20,25,17,24,20,25],
[27,0,30,22,29,26,26,21,30],
[29,21,0,19,26,24,28,22,25],
[31,29,32,0,30,24,35,27,28],
[26,22,25,21,0,17,22,22,26],
[34,25,27,27,34,0,34,27,30],
[27,25,23,16,29,17,0,16,27],
[31,30,29,24,29,24,35,0,28],
[26,21,26,23,25,21,24,23,0]])



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
result = np.append(np.array([9, 51, 78, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,21,29,22,24,24,28,27],
[28,0,25,28,25,24,26,25,31],
[30,26,0,29,31,30,22,29,34],
[22,23,22,0,25,22,17,25,20],
[29,26,20,26,0,27,25,22,26],
[27,27,21,29,24,0,23,27,25],
[27,25,29,34,26,28,0,27,29],
[23,26,22,26,29,24,24,0,26],
[24,20,17,31,25,26,22,25,0]])



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
result = np.append(np.array([9, 51, 79, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,32,28,27,17,23,29,34],
[34,0,38,28,28,20,33,31,34],
[19,13,0,26,28,28,25,22,14],
[23,23,25,0,25,34,26,28,22],
[24,23,23,26,0,26,30,27,17],
[34,31,23,17,25,0,32,32,23],
[28,18,26,25,21,19,0,22,21],
[22,20,29,23,24,19,29,0,23],
[17,17,37,29,34,28,30,28,0]])



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
result = np.append(np.array([9, 51, 80, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,25,25,23,29,27,26,25],
[21,0,22,25,22,23,26,25,27],
[26,29,0,27,24,27,26,28,29],
[26,26,24,0,26,28,30,27,24],
[28,29,27,25,0,28,27,25,28],
[22,28,24,23,23,0,29,27,26],
[24,25,25,21,24,22,0,24,25],
[25,26,23,24,26,24,27,0,23],
[26,24,22,27,23,25,26,28,0]])



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
result = np.append(np.array([9, 51, 81, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,27,26,32,27,39,35,21],
[31,0,40,34,32,29,42,40,24],
[24,11,0,25,19,25,28,35,25],
[25,17,26,0,26,24,24,34,13],
[19,19,32,25,0,27,37,36,28],
[24,22,26,27,24,0,39,27,27],
[12,9,23,27,14,12,0,21,20],
[16,11,16,17,15,24,30,0,14],
[30,27,26,38,23,24,31,37,0]])



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
result = np.append(np.array([9, 51, 82, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,11,15,12,13,3,27,22],
[24,0,23,26,7,19,19,18,22],
[40,28,0,17,15,21,22,16,21],
[36,25,34,0,17,24,27,24,19],
[39,44,36,34,0,32,29,38,20],
[38,32,30,27,19,0,15,21,26],
[48,32,29,24,22,36,0,29,24],
[24,33,35,27,13,30,22,0,27],
[29,29,30,32,31,25,27,24,0]])



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
result = np.append(np.array([9, 51, 83, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,24,25,29,27,30,28,29],
[21,0,16,18,22,21,27,25,24],
[27,35,0,25,28,26,28,28,26],
[26,33,26,0,30,29,30,31,25],
[22,29,23,21,0,21,25,26,23],
[24,30,25,22,30,0,26,22,28],
[21,24,23,21,26,25,0,26,22],
[23,26,23,20,25,29,25,0,23],
[22,27,25,26,28,23,29,28,0]])



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
result = np.append(np.array([9, 51, 84, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,21,24,23,22,22,20,19],
[25,0,31,22,23,24,24,26,21],
[30,20,0,25,26,23,28,29,26],
[27,29,26,0,26,24,21,23,24],
[28,28,25,25,0,26,22,25,25],
[29,27,28,27,25,0,27,27,24],
[29,27,23,30,29,24,0,25,30],
[31,25,22,28,26,24,26,0,28],
[32,30,25,27,26,27,21,23,0]])



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
result = np.append(np.array([9, 51, 85, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,23,32,22,23,31,19,29],
[23,0,23,25,18,24,27,24,16],
[28,28,0,33,23,29,30,25,32],
[19,26,18,0,20,23,29,14,22],
[29,33,28,31,0,25,33,29,34],
[28,27,22,28,26,0,37,25,27],
[20,24,21,22,18,14,0,22,23],
[32,27,26,37,22,26,29,0,32],
[22,35,19,29,17,24,28,19,0]])



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
result = np.append(np.array([9, 51, 86, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,23,28,26,26,29,26,29],
[27,0,21,24,24,31,31,30,25],
[28,30,0,35,24,30,27,34,31],
[23,27,16,0,19,21,29,27,26],
[25,27,27,32,0,30,29,34,36],
[25,20,21,30,21,0,33,29,25],
[22,20,24,22,22,18,0,25,25],
[25,21,17,24,17,22,26,0,26],
[22,26,20,25,15,26,26,25,0]])



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
result = np.append(np.array([9, 51, 87, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,29,36,32,26,23,30,31],
[29,0,20,36,33,32,28,33,33],
[22,31,0,25,23,24,22,22,27],
[15,15,26,0,14,16,23,18,16],
[19,18,28,37,0,24,27,21,31],
[25,19,27,35,27,0,22,27,28],
[28,23,29,28,24,29,0,27,27],
[21,18,29,33,30,24,24,0,26],
[20,18,24,35,20,23,24,25,0]])



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
result = np.append(np.array([9, 51, 88, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,27,22,28,24,23,25,23],
[27,0,31,33,26,24,28,28,27],
[24,20,0,24,18,21,21,26,19],
[29,18,27,0,29,21,29,26,29],
[23,25,33,22,0,23,24,26,26],
[27,27,30,30,28,0,27,26,24],
[28,23,30,22,27,24,0,25,25],
[26,23,25,25,25,25,26,0,23],
[28,24,32,22,25,27,26,28,0]])



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
result = np.append(np.array([9, 51, 89, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,26,23,26,29,26,26,29],
[29,0,27,29,35,23,30,35,32],
[25,24,0,32,27,29,31,27,32],
[28,22,19,0,24,24,28,25,33],
[25,16,24,27,0,24,28,28,32],
[22,28,22,27,27,0,30,27,32],
[25,21,20,23,23,21,0,25,32],
[25,16,24,26,23,24,26,0,30],
[22,19,19,18,19,19,19,21,0]])



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
result = np.append(np.array([9, 51, 90, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,29,30,21,33,31,21,26],
[23,0,22,36,17,25,31,26,28],
[22,29,0,31,30,30,26,17,27],
[21,15,20,0,13,21,19,13,23],
[30,34,21,38,0,32,31,16,28],
[18,26,21,30,19,0,27,20,27],
[20,20,25,32,20,24,0,12,26],
[30,25,34,38,35,31,39,0,30],
[25,23,24,28,23,24,25,21,0]])



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
result = np.append(np.array([9, 51, 91, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,34,34,34,23,44,23,23],
[17,0,30,30,18,19,29,30,30],
[17,21,0,32,16,28,16,27,38],
[17,21,19,0,27,28,27,16,17],
[17,33,35,24,0,25,46,25,25],
[28,32,23,23,26,0,29,28,26],
[7,22,35,24,5,22,0,22,22],
[28,21,24,35,26,23,29,0,33],
[28,21,13,34,26,25,29,18,0]])



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
result = np.append(np.array([9, 51, 92, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,22,40,26,24,31,19,18],
[32,0,22,26,33,30,23,19,22],
[29,29,0,37,24,18,22,12,22],
[11,25,14,0,22,17,23,12,15],
[25,18,27,29,0,35,22,20,23],
[27,21,33,34,16,0,27,30,27],
[20,28,29,28,29,24,0,20,19],
[32,32,39,39,31,21,31,0,28],
[33,29,29,36,28,24,32,23,0]])



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
result = np.append(np.array([9, 51, 93, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,28,33,24,26,32,22,32],
[22,0,30,30,28,25,28,30,33],
[23,21,0,28,25,27,24,23,23],
[18,21,23,0,20,19,22,23,30],
[27,23,26,31,0,36,27,31,30],
[25,26,24,32,15,0,29,25,25],
[19,23,27,29,24,22,0,22,30],
[29,21,28,28,20,26,29,0,31],
[19,18,28,21,21,26,21,20,0]])



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
result = np.append(np.array([9, 51, 94, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,29,17,17,22,22,14,24],
[33,0,28,22,30,29,32,25,29],
[22,23,0,26,14,24,27,24,23],
[34,29,25,0,26,35,30,31,27],
[34,21,37,25,0,35,29,26,24],
[29,22,27,16,16,0,22,24,21],
[29,19,24,21,22,29,0,27,25],
[37,26,27,20,25,27,24,0,26],
[27,22,28,24,27,30,26,25,0]])



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
result = np.append(np.array([9, 51, 95, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,25,16,20,32,17,21,25],
[35,0,32,30,28,35,32,31,24],
[26,19,0,20,23,22,21,24,22],
[35,21,31,0,30,34,29,21,28],
[31,23,28,21,0,25,21,27,25],
[19,16,29,17,26,0,18,23,23],
[34,19,30,22,30,33,0,24,21],
[30,20,27,30,24,28,27,0,20],
[26,27,29,23,26,28,30,31,0]])



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
result = np.append(np.array([9, 51, 96, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,26,36,13,13,26,34,35],
[8,0,7,19,11,15,15,21,17],
[25,44,0,35,34,30,27,31,25],
[15,32,16,0,21,17,19,28,17],
[38,40,17,30,0,36,19,42,40],
[38,36,21,34,15,0,19,42,32],
[25,36,24,32,32,32,0,27,27],
[17,30,20,23,9,9,24,0,20],
[16,34,26,34,11,19,24,31,0]])



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
result = np.append(np.array([9, 51, 97, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,17,11,13,15,7,7,9],
[35,0,29,26,17,33,20,33,35],
[34,22,0,17,19,21,22,17,22],
[40,25,34,0,25,27,28,23,27],
[38,34,32,26,0,25,34,32,27],
[36,18,30,24,26,0,15,26,19],
[44,31,29,23,17,36,0,26,28],
[44,18,34,28,19,25,25,0,26],
[42,16,29,24,24,32,23,25,0]])



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
result = np.append(np.array([9, 51, 98, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,10,19,20,30,25,29,13],
[38,0,26,23,31,30,27,35,22],
[41,25,0,33,29,35,38,36,34],
[32,28,18,0,17,35,27,30,19],
[31,20,22,34,0,40,34,34,31],
[21,21,16,16,11,0,19,21,21],
[26,24,13,24,17,32,0,29,17],
[22,16,15,21,17,30,22,0,21],
[38,29,17,32,20,30,34,30,0]])



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
result = np.append(np.array([9, 51, 99, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,27,22,25,36,23,27,29],
[33,0,25,34,26,40,25,28,30],
[24,26,0,20,30,34,28,35,26],
[29,17,31,0,29,34,21,32,31],
[26,25,21,22,0,33,28,28,26],
[15,11,17,17,18,0,22,13,15],
[28,26,23,30,23,29,0,25,19],
[24,23,16,19,23,38,26,0,33],
[22,21,25,20,25,36,32,18,0]])



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
result = np.append(np.array([9, 51, 100, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,28,19,17,21,18,24,23],
[28,0,31,22,21,19,23,22,29],
[23,20,0,23,17,21,20,23,25],
[32,29,28,0,26,25,26,25,29],
[34,30,34,25,0,27,28,28,26],
[30,32,30,26,24,0,26,25,33],
[33,28,31,25,23,25,0,26,26],
[27,29,28,26,23,26,25,0,25],
[28,22,26,22,25,18,25,26,0]])



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
result = np.append(np.array([9, 51, 101, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,27,14,17,23,11,20,15],
[33,0,23,26,21,31,27,25,31],
[24,28,0,22,29,20,28,21,23],
[37,25,29,0,26,25,25,30,25],
[34,30,22,25,0,24,29,26,21],
[28,20,31,26,27,0,21,28,22],
[40,24,23,26,22,30,0,23,24],
[31,26,30,21,25,23,28,0,28],
[36,20,28,26,30,29,27,23,0]])



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
result = np.append(np.array([9, 51, 102, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,16,34,31,21,22,30,27],
[29,0,32,34,23,34,33,32,33],
[35,19,0,31,29,25,26,30,28],
[17,17,20,0,14,26,17,25,21],
[20,28,22,37,0,33,27,32,32],
[30,17,26,25,18,0,23,28,25],
[29,18,25,34,24,28,0,30,29],
[21,19,21,26,19,23,21,0,20],
[24,18,23,30,19,26,22,31,0]])



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
result = np.append(np.array([9, 51, 103, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,31,29,25,28,31,25,26],
[30,0,26,26,18,20,28,27,28],
[20,25,0,28,19,24,29,27,28],
[22,25,23,0,18,21,29,24,27],
[26,33,32,33,0,25,36,35,38],
[23,31,27,30,26,0,31,28,32],
[20,23,22,22,15,20,0,27,20],
[26,24,24,27,16,23,24,0,28],
[25,23,23,24,13,19,31,23,0]])



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
result = np.append(np.array([9, 51, 104, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,9,11,16,22,31,9,21],
[41,0,15,17,24,27,27,30,36],
[42,36,0,35,37,35,34,28,24],
[40,34,16,0,31,33,38,22,29],
[35,27,14,20,0,27,34,16,27],
[29,24,16,18,24,0,32,18,22],
[20,24,17,13,17,19,0,14,18],
[42,21,23,29,35,33,37,0,33],
[30,15,27,22,24,29,33,18,0]])



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
result = np.append(np.array([9, 51, 105, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,37,27,19,41,37,19,27],
[17,0,17,19,26,26,26,26,15],
[14,34,0,24,26,23,34,33,41],
[24,32,27,0,24,23,27,27,32],
[32,25,25,27,0,41,34,25,22],
[10,25,28,28,10,0,28,20,18],
[14,25,17,24,17,23,0,7,22],
[32,25,18,24,26,31,44,0,22],
[24,36,10,19,29,33,29,29,0]])



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
result = np.append(np.array([9, 51, 106, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,24,30,26,18,20,27,25],
[23,0,32,29,33,27,23,25,31],
[27,19,0,29,12,23,22,28,25],
[21,22,22,0,23,26,15,24,23],
[25,18,39,28,0,31,29,29,32],
[33,24,28,25,20,0,24,29,37],
[31,28,29,36,22,27,0,29,30],
[24,26,23,27,22,22,22,0,30],
[26,20,26,28,19,14,21,21,0]])



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
result = np.append(np.array([9, 51, 107, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,23,30,21,30,19,18,21],
[25,0,22,31,24,38,24,8,32],
[28,29,0,20,23,39,19,16,27],
[21,20,31,0,31,23,20,24,19],
[30,27,28,20,0,31,26,27,29],
[21,13,12,28,20,0,11,13,15],
[32,27,32,31,25,40,0,33,24],
[33,43,35,27,24,38,18,0,32],
[30,19,24,32,22,36,27,19,0]])



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
result = np.append(np.array([9, 51, 108, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,30,21,25,24,28,26,24],
[23,0,37,23,22,25,25,26,24],
[21,14,0,19,15,18,17,19,20],
[30,28,32,0,30,26,29,30,25],
[26,29,36,21,0,24,23,27,23],
[27,26,33,25,27,0,28,24,21],
[23,26,34,22,28,23,0,21,21],
[25,25,32,21,24,27,30,0,27],
[27,27,31,26,28,30,30,24,0]])



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
result = np.append(np.array([9, 51, 109, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,25,29,27,31,27,27,27],
[22,0,23,24,25,30,28,26,25],
[26,28,0,25,28,33,32,31,31],
[22,27,26,0,27,32,29,27,32],
[24,26,23,24,0,26,30,22,30],
[20,21,18,19,25,0,22,30,23],
[24,23,19,22,21,29,0,27,25],
[24,25,20,24,29,21,24,0,28],
[24,26,20,19,21,28,26,23,0]])



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
result = np.append(np.array([9, 51, 110, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,21,39,29,21,28,28,32],
[23,0,21,31,27,26,26,34,22],
[30,30,0,35,26,18,31,23,25],
[12,20,16,0,29,8,24,23,28],
[22,24,25,22,0,25,33,29,28],
[30,25,33,43,26,0,28,23,43],
[23,25,20,27,18,23,0,28,33],
[23,17,28,28,22,28,23,0,24],
[19,29,26,23,23,8,18,27,0]])



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
result = np.append(np.array([9, 51, 111, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,31,29,25,31,27,26,21],
[20,0,33,23,21,28,22,22,21],
[20,18,0,24,21,26,24,22,19],
[22,28,27,0,22,24,21,27,16],
[26,30,30,29,0,27,24,26,26],
[20,23,25,27,24,0,29,23,19],
[24,29,27,30,27,22,0,29,24],
[25,29,29,24,25,28,22,0,19],
[30,30,32,35,25,32,27,32,0]])



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
result = np.append(np.array([9, 51, 112, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,51,35,51,35,51,41,41],
[26,0,26,10,51,10,51,26,26],
[0,25,0,0,41,0,51,0,16],
[16,41,51,0,41,16,51,16,16],
[0,0,10,10,0,0,51,0,16],
[16,41,51,35,51,0,51,16,16],
[0,0,0,0,0,0,0,0,0],
[10,25,51,35,51,35,51,0,41],
[10,25,35,35,35,35,51,10,0]])



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
result = np.append(np.array([9, 51, 113, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,20,20,13,22,24,24,8],
[20,0,15,22,20,18,32,27,16],
[31,36,0,26,20,18,20,27,27],
[31,29,25,0,15,35,34,22,17],
[38,31,31,36,0,30,33,21,34],
[29,33,33,16,21,0,19,30,20],
[27,19,31,17,18,32,0,27,21],
[27,24,24,29,30,21,24,0,25],
[43,35,24,34,17,31,30,26,0]])



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
result = np.append(np.array([9, 51, 114, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,27,30,24,30,31,26,29],
[27,0,20,24,27,25,26,26,25],
[24,31,0,31,25,31,30,25,29],
[21,27,20,0,23,24,25,23,28],
[27,24,26,28,0,31,28,23,30],
[21,26,20,27,20,0,28,28,24],
[20,25,21,26,23,23,0,22,30],
[25,25,26,28,28,23,29,0,31],
[22,26,22,23,21,27,21,20,0]])



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
result = np.append(np.array([9, 51, 115, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,28,29,28,34,25,29,30],
[25,0,30,32,29,31,23,32,25],
[23,21,0,23,27,29,22,29,22],
[22,19,28,0,27,25,22,28,24],
[23,22,24,24,0,25,24,31,23],
[17,20,22,26,26,0,19,26,21],
[26,28,29,29,27,32,0,32,25],
[22,19,22,23,20,25,19,0,19],
[21,26,29,27,28,30,26,32,0]])



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
result = np.append(np.array([9, 51, 116, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,23,28,22,21,21,25,27],
[29,0,34,27,25,25,23,28,22],
[28,17,0,25,21,25,26,21,23],
[23,24,26,0,24,24,26,24,24],
[29,26,30,27,0,33,28,24,27],
[30,26,26,27,18,0,22,23,28],
[30,28,25,25,23,29,0,23,29],
[26,23,30,27,27,28,28,0,27],
[24,29,28,27,24,23,22,24,0]])



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
result = np.append(np.array([9, 51, 117, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,11,0,17,0,17,41,28],
[33,0,11,23,28,11,29,51,28],
[40,40,0,12,29,12,30,40,30],
[51,28,39,0,18,28,40,51,39],
[34,23,22,33,0,22,40,51,51],
[51,40,39,23,29,0,30,51,41],
[34,22,21,11,11,21,0,51,12],
[10,0,11,0,0,0,0,0,0],
[23,23,21,12,0,10,39,51,0]])



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
result = np.append(np.array([9, 51, 118, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,24,31,32,24,30,25,32],
[22,0,18,29,23,20,24,28,23],
[27,33,0,34,27,22,29,29,28],
[20,22,17,0,19,14,18,21,25],
[19,28,24,32,0,26,26,27,30],
[27,31,29,37,25,0,35,33,28],
[21,27,22,33,25,16,0,25,23],
[26,23,22,30,24,18,26,0,21],
[19,28,23,26,21,23,28,30,0]])



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
result = np.append(np.array([9, 51, 119, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,41,33,33,41,41,51,35],
[36,0,51,30,33,41,39,38,22],
[10,0,0,20,20,20,20,36,22],
[18,21,31,0,39,21,21,31,21],
[18,18,31,12,0,18,8,18,18],
[10,10,31,30,33,0,6,16,32],
[10,12,31,30,43,45,0,18,32],
[0,13,15,20,33,35,33,0,22],
[16,29,29,30,33,19,19,29,0]])



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
result = np.append(np.array([9, 51, 120, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,43,48,28,43,28,51,28],
[26,0,31,23,28,31,16,39,28],
[8,20,0,23,33,21,8,36,25],
[3,28,28,0,28,16,16,31,28],
[23,23,18,23,0,28,15,39,31],
[8,20,30,35,23,0,20,38,28],
[23,35,43,35,36,31,0,39,28],
[0,12,15,20,12,13,12,0,28],
[23,23,26,23,20,23,23,23,0]])



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
result = np.append(np.array([9, 51, 121, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,25,23,25,23,29,20,25],
[34,0,26,29,27,32,32,25,27],
[26,25,0,19,21,28,29,27,24],
[28,22,32,0,25,31,30,31,32],
[26,24,30,26,0,25,29,24,24],
[28,19,23,20,26,0,30,24,30],
[22,19,22,21,22,21,0,17,23],
[31,26,24,20,27,27,34,0,31],
[26,24,27,19,27,21,28,20,0]])



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
result = np.append(np.array([9, 51, 122, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,28,23,26,29,28,25,28],
[25,0,31,23,25,25,29,25,24],
[23,20,0,20,28,24,24,22,25],
[28,28,31,0,30,29,30,31,25],
[25,26,23,21,0,22,24,23,22],
[22,26,27,22,29,0,24,29,22],
[23,22,27,21,27,27,0,25,22],
[26,26,29,20,28,22,26,0,25],
[23,27,26,26,29,29,29,26,0]])



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
result = np.append(np.array([9, 51, 123, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,31,34,23,26,28,30,27],
[22,0,22,28,20,22,22,24,20],
[20,29,0,27,19,26,22,23,18],
[17,23,24,0,17,18,16,21,19],
[28,31,32,34,0,26,26,31,23],
[25,29,25,33,25,0,29,28,26],
[23,29,29,35,25,22,0,28,28],
[21,27,28,30,20,23,23,0,23],
[24,31,33,32,28,25,23,28,0]])



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
result = np.append(np.array([9, 51, 124, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,38,26,33,26,31,30,26],
[26,0,34,25,33,25,26,25,29],
[13,17,0,18,22,19,19,19,20],
[25,26,33,0,28,23,28,27,23],
[18,18,29,23,0,30,23,27,25],
[25,26,32,28,21,0,24,25,20],
[20,25,32,23,28,27,0,26,25],
[21,26,32,24,24,26,25,0,24],
[25,22,31,28,26,31,26,27,0]])



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
result = np.append(np.array([9, 51, 125, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,22,27,25,23,35,21,33],
[16,0,15,18,18,17,21,7,25],
[29,36,0,24,25,28,33,25,34],
[24,33,27,0,28,24,33,20,29],
[26,33,26,23,0,24,37,26,34],
[28,34,23,27,27,0,34,29,33],
[16,30,18,18,14,17,0,15,26],
[30,44,26,31,25,22,36,0,38],
[18,26,17,22,17,18,25,13,0]])



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
result = np.append(np.array([9, 51, 126, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,21,23,22,30,25,23,23],
[23,0,27,22,23,28,27,29,21],
[30,24,0,25,25,29,28,26,25],
[28,29,26,0,19,30,27,31,26],
[29,28,26,32,0,29,24,27,28],
[21,23,22,21,22,0,21,27,18],
[26,24,23,24,27,30,0,28,23],
[28,22,25,20,24,24,23,0,17],
[28,30,26,25,23,33,28,34,0]])



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
result = np.append(np.array([9, 51, 127, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,23,17,5,29,27,27,28],
[24,0,10,24,26,24,26,17,28],
[28,41,0,30,30,18,41,41,41],
[34,27,21,0,30,30,36,24,24],
[46,25,21,21,0,27,25,25,25],
[22,27,33,21,24,0,23,23,23],
[24,25,10,15,26,28,0,8,19],
[24,34,10,27,26,28,43,0,29],
[23,23,10,27,26,28,32,22,0]])



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
result = np.append(np.array([9, 51, 128, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,27,18,31,22,24,24,20],
[21,0,29,16,22,16,16,19,21],
[24,22,0,20,20,22,15,26,20],
[33,35,31,0,22,22,27,28,29],
[20,29,31,29,0,26,26,27,23],
[29,35,29,29,25,0,26,33,23],
[27,35,36,24,25,25,0,34,25],
[27,32,25,23,24,18,17,0,19],
[31,30,31,22,28,28,26,32,0]])



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
result = np.append(np.array([9, 51, 129, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,21,22,18,22,24,20,25],
[26,0,22,22,23,18,25,21,16],
[30,29,0,24,26,25,27,22,26],
[29,29,27,0,26,25,27,26,26],
[33,28,25,25,0,25,28,23,20],
[29,33,26,26,26,0,27,22,25],
[27,26,24,24,23,24,0,14,20],
[31,30,29,25,28,29,37,0,24],
[26,35,25,25,31,26,31,27,0]])



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
result = np.append(np.array([9, 51, 130, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,30,24,23,26,21,23,25],
[31,0,29,27,26,28,23,27,26],
[21,22,0,25,23,24,18,20,19],
[27,24,26,0,23,26,24,20,23],
[28,25,28,28,0,27,27,26,23],
[25,23,27,25,24,0,21,22,19],
[30,28,33,27,24,30,0,24,22],
[28,24,31,31,25,29,27,0,20],
[26,25,32,28,28,32,29,31,0]])



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
result = np.append(np.array([9, 51, 131, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,11,11,23,9,16,13,17],
[31,0,14,16,24,19,21,22,29],
[40,37,0,22,27,26,26,25,29],
[40,35,29,0,30,27,31,25,32],
[28,27,24,21,0,18,26,21,23],
[42,32,25,24,33,0,30,26,32],
[35,30,25,20,25,21,0,22,27],
[38,29,26,26,30,25,29,0,27],
[34,22,22,19,28,19,24,24,0]])



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
result = np.append(np.array([9, 51, 132, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,20,17,20,24,19,17,24],
[30,0,24,25,21,29,25,21,25],
[31,27,0,22,24,28,22,31,26],
[34,26,29,0,26,30,28,26,25],
[31,30,27,25,0,31,27,26,29],
[27,22,23,21,20,0,21,16,20],
[32,26,29,23,24,30,0,27,24],
[34,30,20,25,25,35,24,0,25],
[27,26,25,26,22,31,27,26,0]])



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
result = np.append(np.array([9, 51, 133, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,27,28,27,20,25,23,24],
[27,0,24,27,27,26,30,26,26],
[24,27,0,20,22,21,22,21,26],
[23,24,31,0,20,20,22,22,25],
[24,24,29,31,0,26,30,28,27],
[31,25,30,31,25,0,28,29,30],
[26,21,29,29,21,23,0,26,24],
[28,25,30,29,23,22,25,0,25],
[27,25,25,26,24,21,27,26,0]])



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
result = np.append(np.array([9, 51, 134, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,26,26,26,29,23,26,28],
[29,0,28,29,25,32,24,21,27],
[25,23,0,29,22,28,26,23,32],
[25,22,22,0,27,29,26,20,26],
[25,26,29,24,0,27,23,23,30],
[22,19,23,22,24,0,25,17,26],
[28,27,25,25,28,26,0,23,28],
[25,30,28,31,28,34,28,0,30],
[23,24,19,25,21,25,23,21,0]])



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
result = np.append(np.array([9, 51, 135, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,25,24,26,22,23,23,28],
[25,0,24,27,26,20,27,23,28],
[26,27,0,21,28,18,25,26,23],
[27,24,30,0,32,26,25,22,28],
[25,25,23,19,0,23,27,27,24],
[29,31,33,25,28,0,26,27,31],
[28,24,26,26,24,25,0,27,20],
[28,28,25,29,24,24,24,0,25],
[23,23,28,23,27,20,31,26,0]])



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
result = np.append(np.array([9, 51, 136, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,27,24,31,29,41,24,32],
[23,0,23,25,31,29,34,24,28],
[24,28,0,26,34,31,40,21,25],
[27,26,25,0,38,36,32,25,25],
[20,20,17,13,0,25,30,21,24],
[22,22,20,15,26,0,26,16,27],
[10,17,11,19,21,25,0,15,16],
[27,27,30,26,30,35,36,0,23],
[19,23,26,26,27,24,35,28,0]])



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
result = np.append(np.array([9, 51, 137, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,19,26,25,20,20,19,23],
[32,0,30,35,30,24,30,30,33],
[32,21,0,30,27,25,26,23,24],
[25,16,21,0,23,21,25,18,28],
[26,21,24,28,0,25,23,23,22],
[31,27,26,30,26,0,24,25,29],
[31,21,25,26,28,27,0,23,24],
[32,21,28,33,28,26,28,0,27],
[28,18,27,23,29,22,27,24,0]])



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
result = np.append(np.array([9, 51, 138, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,19,16,17,15,17,15,14],
[34,0,22,19,20,28,33,24,25],
[32,29,0,28,29,24,36,32,34],
[35,32,23,0,21,23,30,28,28],
[34,31,22,30,0,23,33,29,30],
[36,23,27,28,28,0,34,24,23],
[34,18,15,21,18,17,0,22,16],
[36,27,19,23,22,27,29,0,27],
[37,26,17,23,21,28,35,24,0]])



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
result = np.append(np.array([9, 51, 139, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,21,28,27,22,37,21,32],
[23,0,32,30,34,29,32,32,28],
[30,19,0,28,23,18,32,16,32],
[23,21,23,0,23,18,33,16,23],
[24,17,28,28,0,21,33,21,24],
[29,22,33,33,30,0,33,33,24],
[14,19,19,18,18,18,0,24,23],
[30,19,35,35,30,18,27,0,30],
[19,23,19,28,27,27,28,21,0]])



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
result = np.append(np.array([9, 51, 140, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,33,25,22,24,26,26,31],
[26,0,28,28,22,28,30,25,27],
[18,23,0,28,27,23,24,26,25],
[26,23,23,0,25,26,28,25,28],
[29,29,24,26,0,30,27,26,28],
[27,23,28,25,21,0,26,25,25],
[25,21,27,23,24,25,0,23,24],
[25,26,25,26,25,26,28,0,28],
[20,24,26,23,23,26,27,23,0]])



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
result = np.append(np.array([9, 51, 141, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,20,21,20,24,30,25,24],
[32,0,22,26,21,23,27,25,24],
[31,29,0,26,26,25,30,27,26],
[30,25,25,0,22,27,23,31,26],
[31,30,25,29,0,24,33,31,25],
[27,28,26,24,27,0,26,26,31],
[21,24,21,28,18,25,0,28,19],
[26,26,24,20,20,25,23,0,23],
[27,27,25,25,26,20,32,28,0]])



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
result = np.append(np.array([9, 51, 142, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,21,22,19,22,21,25,19],
[31,0,32,23,23,19,31,39,39],
[30,19,0,18,22,12,24,29,26],
[29,28,33,0,15,27,20,32,28],
[32,28,29,36,0,28,22,40,30],
[29,32,39,24,23,0,24,34,38],
[30,20,27,31,29,27,0,39,29],
[26,12,22,19,11,17,12,0,22],
[32,12,25,23,21,13,22,29,0]])



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
result = np.append(np.array([9, 51, 143, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,25,28,28,32,28,29,33],
[22,0,18,23,23,29,26,27,28],
[26,33,0,24,25,23,26,23,27],
[23,28,27,0,30,21,24,19,28],
[23,28,26,21,0,25,23,18,30],
[19,22,28,30,26,0,29,16,27],
[23,25,25,27,28,22,0,16,27],
[22,24,28,32,33,35,35,0,30],
[18,23,24,23,21,24,24,21,0]])



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
result = np.append(np.array([9, 51, 144, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,28,26,22,26,28,26,30],
[29,0,23,26,30,23,24,31,34],
[23,28,0,25,27,25,26,25,24],
[25,25,26,0,28,28,25,24,28],
[29,21,24,23,0,28,25,19,27],
[25,28,26,23,23,0,31,22,25],
[23,27,25,26,26,20,0,25,33],
[25,20,26,27,32,29,26,0,26],
[21,17,27,23,24,26,18,25,0]])



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
result = np.append(np.array([9, 51, 145, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,32,26,24,20,23,22,23],
[28,0,26,25,21,26,32,34,22],
[19,25,0,27,26,24,26,28,23],
[25,26,24,0,26,26,31,29,31],
[27,30,25,25,0,22,28,26,29],
[31,25,27,25,29,0,33,29,29],
[28,19,25,20,23,18,0,24,24],
[29,17,23,22,25,22,27,0,25],
[28,29,28,20,22,22,27,26,0]])



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
result = np.append(np.array([9, 51, 146, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,26,38,31,28,27,23,40],
[12,0,25,31,19,24,26,31,31],
[25,26,0,32,30,26,27,32,40],
[13,20,19,0,16,22,24,15,18],
[20,32,21,35,0,26,16,24,32],
[23,27,25,29,25,0,25,20,22],
[24,25,24,27,35,26,0,26,33],
[28,20,19,36,27,31,25,0,22],
[11,20,11,33,19,29,18,29,0]])



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
result = np.append(np.array([9, 51, 147, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,22,20,20,25,24,22,19],
[33,0,30,25,24,29,26,24,23],
[29,21,0,23,21,25,28,23,22],
[31,26,28,0,30,34,24,24,26],
[31,27,30,21,0,30,21,21,27],
[26,22,26,17,21,0,20,22,26],
[27,25,23,27,30,31,0,26,27],
[29,27,28,27,30,29,25,0,29],
[32,28,29,25,24,25,24,22,0]])



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
result = np.append(np.array([9, 51, 148, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,32,26,20,27,28,29,26],
[28,0,29,22,21,23,26,23,24],
[19,22,0,21,22,23,26,25,24],
[25,29,30,0,20,26,30,29,35],
[31,30,29,31,0,25,31,30,35],
[24,28,28,25,26,0,29,28,33],
[23,25,25,21,20,22,0,23,29],
[22,28,26,22,21,23,28,0,31],
[25,27,27,16,16,18,22,20,0]])



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
result = np.append(np.array([9, 51, 149, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,19,20,32,15,29,25,22],
[30,0,31,22,38,28,22,25,17],
[32,20,0,28,33,18,32,27,31],
[31,29,23,0,29,23,34,36,36],
[19,13,18,22,0,18,12,24,14],
[36,23,33,28,33,0,38,28,28],
[22,29,19,17,39,13,0,28,23],
[26,26,24,15,27,23,23,0,25],
[29,34,20,15,37,23,28,26,0]])



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
result = np.append(np.array([9, 51, 150, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,37,25,33,31,33,23,31,40],
[14,0,16,20,24,20,6,16,16],
[26,35,0,36,38,31,29,25,43],
[18,31,15,0,31,21,24,15,25],
[20,27,13,20,0,26,14,8,25],
[18,31,20,30,25,0,19,11,29],
[28,45,22,27,37,32,0,22,31],
[20,35,26,36,43,40,29,0,42],
[11,35,8,26,26,22,20,9,0]])



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
result = np.append(np.array([9, 51, 151, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,22,20,28,30,20,20,27],
[25,0,23,26,24,27,24,26,24],
[29,28,0,22,27,25,23,21,21],
[31,25,29,0,29,29,29,27,27],
[23,27,24,22,0,26,25,20,19],
[21,24,26,22,25,0,21,21,22],
[31,27,28,22,26,30,0,27,24],
[31,25,30,24,31,30,24,0,22],
[24,27,30,24,32,29,27,29,0]])



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
result = np.append(np.array([9, 51, 152, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,28,23,27,27,28,22,24],
[20,0,22,23,26,25,27,20,20],
[23,29,0,26,29,23,29,23,31],
[28,28,25,0,28,30,28,24,28],
[24,25,22,23,0,23,26,25,24],
[24,26,28,21,28,0,24,20,25],
[23,24,22,23,25,27,0,22,21],
[29,31,28,27,26,31,29,0,25],
[27,31,20,23,27,26,30,26,0]])



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
result = np.append(np.array([9, 51, 153, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,21,20,20,26,29,18,16],
[19,0,24,22,25,22,23,21,15],
[30,27,0,27,21,28,30,29,27],
[31,29,24,0,24,25,29,26,25],
[31,26,30,27,0,29,30,25,26],
[25,29,23,26,22,0,25,25,25],
[22,28,21,22,21,26,0,24,21],
[33,30,22,25,26,26,27,0,23],
[35,36,24,26,25,26,30,28,0]])



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
result = np.append(np.array([9, 51, 154, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,25,40,22,32,30,33,26],
[16,0,10,19,16,18,23,13,2],
[26,41,0,30,36,27,30,32,21],
[11,32,21,0,23,17,23,25,14],
[29,35,15,28,0,28,30,32,13],
[19,33,24,34,23,0,24,27,23],
[21,28,21,28,21,27,0,26,17],
[18,38,19,26,19,24,25,0,7],
[25,49,30,37,38,28,34,44,0]])



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
result = np.append(np.array([9, 51, 155, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,31,24,27,27,24,25,23],
[27,0,30,28,29,25,26,28,29],
[20,21,0,25,27,25,23,27,17],
[27,23,26,0,25,25,30,29,20],
[24,22,24,26,0,28,31,27,19],
[24,26,26,26,23,0,24,20,19],
[27,25,28,21,20,27,0,26,20],
[26,23,24,22,24,31,25,0,21],
[28,22,34,31,32,32,31,30,0]])



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
result = np.append(np.array([9, 51, 156, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,26,28,23,29,32,27,23],
[28,0,21,33,30,28,33,27,26],
[25,30,0,36,30,27,30,32,34],
[23,18,15,0,19,24,26,21,15],
[28,21,21,32,0,28,30,27,25],
[22,23,24,27,23,0,27,23,19],
[19,18,21,25,21,24,0,19,23],
[24,24,19,30,24,28,32,0,28],
[28,25,17,36,26,32,28,23,0]])



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
result = np.append(np.array([9, 51, 157, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,22,27,26,21,24,25,25],
[25,0,22,34,30,20,30,27,28],
[29,29,0,32,33,30,31,24,30],
[24,17,19,0,19,19,20,20,21],
[25,21,18,32,0,17,25,27,26],
[30,31,21,32,34,0,22,26,26],
[27,21,20,31,26,29,0,20,24],
[26,24,27,31,24,25,31,0,26],
[26,23,21,30,25,25,27,25,0]])



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
result = np.append(np.array([9, 51, 158, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,27,25,34,30,35,38,33],
[19,0,23,18,20,26,26,24,31],
[24,28,0,22,23,26,25,25,35],
[26,33,29,0,23,30,35,24,28],
[17,31,28,28,0,23,30,20,31],
[21,25,25,21,28,0,23,20,22],
[16,25,26,16,21,28,0,15,22],
[13,27,26,27,31,31,36,0,29],
[18,20,16,23,20,29,29,22,0]])



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
result = np.append(np.array([9, 51, 159, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,26,24,32,26,23,22,28],
[24,0,25,22,32,27,26,27,24],
[25,26,0,29,36,27,28,27,26],
[27,29,22,0,29,20,29,25,28],
[19,19,15,22,0,18,22,25,21],
[25,24,24,31,33,0,28,29,24],
[28,25,23,22,29,23,0,27,26],
[29,24,24,26,26,22,24,0,25],
[23,27,25,23,30,27,25,26,0]])



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
result = np.append(np.array([9, 51, 160, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,23,30,27,25,27,25,30],
[23,0,26,30,29,24,24,19,28],
[28,25,0,31,29,25,25,26,30],
[21,21,20,0,22,22,20,22,25],
[24,22,22,29,0,24,22,24,27],
[26,27,26,29,27,0,21,27,22],
[24,27,26,31,29,30,0,29,32],
[26,32,25,29,27,24,22,0,25],
[21,23,21,26,24,29,19,26,0]])



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
result = np.append(np.array([9, 51, 161, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,19,16,22,12,10,29,19],
[29,0,19,17,20,23,18,27,22],
[32,32,0,22,22,28,24,36,24],
[35,34,29,0,19,26,26,36,30],
[29,31,29,32,0,25,21,33,23],
[39,28,23,25,26,0,21,33,25],
[41,33,27,25,30,30,0,36,25],
[22,24,15,15,18,18,15,0,20],
[32,29,27,21,28,26,26,31,0]])



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
result = np.append(np.array([9, 51, 162, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,20,16,20,17,25,22,23],
[29,0,23,24,20,17,33,28,28],
[31,28,0,22,26,27,29,30,30],
[35,27,29,0,26,24,33,31,29],
[31,31,25,25,0,26,32,28,34],
[34,34,24,27,25,0,37,31,29],
[26,18,22,18,19,14,0,15,24],
[29,23,21,20,23,20,36,0,26],
[28,23,21,22,17,22,27,25,0]])



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
result = np.append(np.array([9, 51, 163, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,19,21,21,23,16,23,19],
[32,0,25,24,26,30,23,32,23],
[32,26,0,27,27,28,23,22,29],
[30,27,24,0,24,29,24,20,18],
[30,25,24,27,0,32,18,22,27],
[28,21,23,22,19,0,23,21,23],
[35,28,28,27,33,28,0,26,23],
[28,19,29,31,29,30,25,0,22],
[32,28,22,33,24,28,28,29,0]])



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
result = np.append(np.array([9, 51, 164, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,30,29,25,33,31,29,22],
[23,0,22,21,24,29,25,23,18],
[21,29,0,22,30,30,26,20,16],
[22,30,29,0,26,27,28,28,26],
[26,27,21,25,0,30,29,25,23],
[18,22,21,24,21,0,28,19,21],
[20,26,25,23,22,23,0,27,18],
[22,28,31,23,26,32,24,0,18],
[29,33,35,25,28,30,33,33,0]])



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
result = np.append(np.array([9, 51, 165, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,21,16,26,12,19,26,29],
[20,0,15,22,27,25,26,28,30],
[30,36,0,19,29,27,23,21,24],
[35,29,32,0,24,30,38,37,25],
[25,24,22,27,0,27,29,38,33],
[39,26,24,21,24,0,23,32,20],
[32,25,28,13,22,28,0,28,30],
[25,23,30,14,13,19,23,0,23],
[22,21,27,26,18,31,21,28,0]])



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
result = np.append(np.array([9, 51, 166, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,25,30,24,23,25,29,25],
[26,0,28,25,29,24,37,31,25],
[26,23,0,27,23,24,26,24,23],
[21,26,24,0,26,23,27,28,19],
[27,22,28,25,0,26,28,28,26],
[28,27,27,28,25,0,30,31,24],
[26,14,25,24,23,21,0,28,22],
[22,20,27,23,23,20,23,0,23],
[26,26,28,32,25,27,29,28,0]])



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
result = np.append(np.array([9, 51, 167, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,21,26,22,24,28,33,26],
[28,0,25,31,25,17,25,36,36],
[30,26,0,16,33,23,24,30,24],
[25,20,35,0,36,25,24,35,30],
[29,26,18,15,0,18,18,32,22],
[27,34,28,26,33,0,20,34,26],
[23,26,27,27,33,31,0,31,29],
[18,15,21,16,19,17,20,0,15],
[25,15,27,21,29,25,22,36,0]])



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
result = np.append(np.array([9, 51, 168, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,28,24,27,30,24,28,29],
[26,0,31,27,32,29,29,26,20],
[23,20,0,17,22,26,15,20,21],
[27,24,34,0,37,27,24,29,24],
[24,19,29,14,0,28,17,28,22],
[21,22,25,24,23,0,20,23,25],
[27,22,36,27,34,31,0,30,28],
[23,25,31,22,23,28,21,0,25],
[22,31,30,27,29,26,23,26,0]])



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
result = np.append(np.array([9, 51, 169, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,24,36,20,31,31,21,31],
[30,0,26,33,23,33,34,27,24],
[27,25,0,24,16,19,27,20,26],
[15,18,27,0,28,27,22,17,25],
[31,28,35,23,0,28,27,23,30],
[20,18,32,24,23,0,19,23,34],
[20,17,24,29,24,32,0,28,35],
[30,24,31,34,28,28,23,0,30],
[20,27,25,26,21,17,16,21,0]])



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
result = np.append(np.array([9, 51, 170, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,28,22,32,32,31,27,21],
[23,0,29,29,28,27,43,25,24],
[23,22,0,36,20,27,42,27,26],
[29,22,15,0,23,22,35,25,23],
[19,23,31,28,0,32,37,30,25],
[19,24,24,29,19,0,35,23,25],
[20,8,9,16,14,16,0,11,12],
[24,26,24,26,21,28,40,0,21],
[30,27,25,28,26,26,39,30,0]])



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
result = np.append(np.array([9, 51, 171, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,25,28,20,20,25,16,24],
[41,0,37,28,36,22,35,23,33],
[26,14,0,17,15,17,20,22,21],
[23,23,34,0,32,29,31,19,33],
[31,15,36,19,0,23,23,25,36],
[31,29,34,22,28,0,28,24,31],
[26,16,31,20,28,23,0,24,31],
[35,28,29,32,26,27,27,0,25],
[27,18,30,18,15,20,20,26,0]])



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
result = np.append(np.array([9, 51, 172, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,28,21,24,24,23,29,29],
[27,0,31,29,22,22,27,21,26],
[23,20,0,28,22,22,21,24,23],
[30,22,23,0,21,24,19,24,23],
[27,29,29,30,0,27,23,24,25],
[27,29,29,27,24,0,21,28,20],
[28,24,30,32,28,30,0,24,26],
[22,30,27,27,27,23,27,0,22],
[22,25,28,28,26,31,25,29,0]])



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
result = np.append(np.array([9, 51, 173, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,25,26,18,21,25,27,25],
[21,0,22,30,20,21,23,21,23],
[26,29,0,17,23,12,11,21,23],
[25,21,34,0,17,24,20,24,24],
[33,31,28,34,0,25,25,32,26],
[30,30,39,27,26,0,26,23,23],
[26,28,40,31,26,25,0,30,23],
[24,30,30,27,19,28,21,0,22],
[26,28,28,27,25,28,28,29,0]])



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
result = np.append(np.array([9, 51, 174, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,20,33,20,29,30,23,25],
[26,0,26,27,23,26,33,29,25],
[31,25,0,33,26,23,32,30,30],
[18,24,18,0,17,18,24,26,26],
[31,28,25,34,0,30,27,27,28],
[22,25,28,33,21,0,29,23,26],
[21,18,19,27,24,22,0,24,24],
[28,22,21,25,24,28,27,0,26],
[26,26,21,25,23,25,27,25,0]])



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
result = np.append(np.array([9, 51, 175, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,23,25,18,24,28,24,25],
[32,0,27,24,21,24,25,38,27],
[28,24,0,29,28,18,30,26,33],
[26,27,22,0,19,31,18,30,32],
[33,30,23,32,0,17,23,34,29],
[27,27,33,20,34,0,25,24,26],
[23,26,21,33,28,26,0,28,37],
[27,13,25,21,17,27,23,0,23],
[26,24,18,19,22,25,14,28,0]])



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
result = np.append(np.array([9, 51, 176, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,32,27,19,32,28,25,30],
[23,0,21,21,18,31,21,27,17],
[19,30,0,24,18,26,23,27,30],
[24,30,27,0,21,27,20,23,27],
[32,33,33,30,0,37,33,25,33],
[19,20,25,24,14,0,20,23,22],
[23,30,28,31,18,31,0,21,29],
[26,24,24,28,26,28,30,0,29],
[21,34,21,24,18,29,22,22,0]])



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
result = np.append(np.array([9, 51, 177, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,26,32,25,25,29,26,31],
[32,0,29,29,22,24,24,26,26],
[25,22,0,31,23,29,20,23,22],
[19,22,20,0,22,24,23,26,22],
[26,29,28,29,0,26,23,29,28],
[26,27,22,27,25,0,25,22,26],
[22,27,31,28,28,26,0,27,26],
[25,25,28,25,22,29,24,0,30],
[20,25,29,29,23,25,25,21,0]])



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
result = np.append(np.array([9, 51, 178, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,16,24,19,24,22,24,15],
[28,0,19,23,23,19,25,24,14],
[35,32,0,15,25,31,28,36,25],
[27,28,36,0,18,23,28,29,23],
[32,28,26,33,0,23,30,32,24],
[27,32,20,28,28,0,34,30,29],
[29,26,23,23,21,17,0,29,18],
[27,27,15,22,19,21,22,0,13],
[36,37,26,28,27,22,33,38,0]])



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
result = np.append(np.array([9, 51, 179, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,30,21,29,33,25,33,28],
[21,0,19,19,19,33,13,28,14],
[21,32,0,22,30,35,32,23,30],
[30,32,29,0,35,40,20,41,24],
[22,32,21,16,0,26,30,31,26],
[18,18,16,11,25,0,19,20,18],
[26,38,19,31,21,32,0,27,19],
[18,23,28,10,20,31,24,0,19],
[23,37,21,27,25,33,32,32,0]])



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
result = np.append(np.array([9, 51, 180, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,23,25,23,29,25,24,28],
[23,0,23,19,23,23,21,25,27],
[28,28,0,30,29,37,32,25,25],
[26,32,21,0,23,27,27,24,26],
[28,28,22,28,0,31,30,26,30],
[22,28,14,24,20,0,28,26,22],
[26,30,19,24,21,23,0,24,28],
[27,26,26,27,25,25,27,0,29],
[23,24,26,25,21,29,23,22,0]])



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
result = np.append(np.array([9, 51, 181, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,23,20,24,20,21,19,26],
[28,0,34,28,35,24,28,24,30],
[28,17,0,19,21,26,20,21,24],
[31,23,32,0,31,27,23,28,27],
[27,16,30,20,0,25,20,15,22],
[31,27,25,24,26,0,19,23,23],
[30,23,31,28,31,32,0,25,26],
[32,27,30,23,36,28,26,0,27],
[25,21,27,24,29,28,25,24,0]])



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
result = np.append(np.array([9, 51, 182, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,25,36,25,21,33,37,26],
[22,0,28,30,31,25,39,34,32],
[26,23,0,21,27,27,24,25,22],
[15,21,30,0,16,17,37,33,30],
[26,20,24,35,0,26,39,31,23],
[30,26,24,34,25,0,36,30,32],
[18,12,27,14,12,15,0,20,15],
[14,17,26,18,20,21,31,0,27],
[25,19,29,21,28,19,36,24,0]])



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
result = np.append(np.array([9, 51, 183, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,24,15,26,9,12,26,11],
[30,0,24,11,26,11,17,11,23],
[27,27,0,27,32,15,18,26,23],
[36,40,24,0,33,28,36,39,23],
[25,25,19,18,0,13,6,18,18],
[42,40,36,23,38,0,35,20,29],
[39,34,33,15,45,16,0,27,26],
[25,40,25,12,33,31,24,0,23],
[40,28,28,28,33,22,25,28,0]])



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
result = np.append(np.array([9, 51, 184, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,27,29,27,19,32,29,16],
[25,0,30,27,33,25,40,35,24],
[24,21,0,21,33,29,37,25,17],
[22,24,30,0,31,19,31,17,27],
[24,18,18,20,0,19,32,27,18],
[32,26,22,32,32,0,31,22,29],
[19,11,14,20,19,20,0,19,13],
[22,16,26,34,24,29,32,0,26],
[35,27,34,24,33,22,38,25,0]])



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
result = np.append(np.array([9, 51, 185, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,25,27,25,28,25,28,23],
[20,0,18,27,27,20,21,21,20],
[26,33,0,29,32,25,22,24,26],
[24,24,22,0,29,23,21,19,21],
[26,24,19,22,0,26,21,22,22],
[23,31,26,28,25,0,22,22,28],
[26,30,29,30,30,29,0,25,24],
[23,30,27,32,29,29,26,0,25],
[28,31,25,30,29,23,27,26,0]])



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
result = np.append(np.array([9, 51, 186, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,22,24,28,22,22,29,32],
[24,0,23,25,26,22,23,28,32],
[29,28,0,28,28,18,24,27,33],
[27,26,23,0,29,20,26,29,31],
[23,25,23,22,0,23,19,28,27],
[29,29,33,31,28,0,25,27,33],
[29,28,27,25,32,26,0,29,32],
[22,23,24,22,23,24,22,0,37],
[19,19,18,20,24,18,19,14,0]])



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
result = np.append(np.array([9, 51, 187, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,26,31,30,20,21,20,18],
[32,0,26,22,27,29,32,27,22],
[25,25,0,25,22,21,24,18,19],
[20,29,26,0,23,24,26,24,18],
[21,24,29,28,0,24,26,23,20],
[31,22,30,27,27,0,25,27,27],
[30,19,27,25,25,26,0,23,22],
[31,24,33,27,28,24,28,0,26],
[33,29,32,33,31,24,29,25,0]])



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
result = np.append(np.array([9, 51, 188, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,33,27,32,24,26,30,33],
[23,0,20,7,22,27,23,33,22],
[18,31,0,23,14,34,29,27,26],
[24,44,28,0,34,34,29,38,27],
[19,29,37,17,0,29,29,28,30],
[27,24,17,17,22,0,29,22,24],
[25,28,22,22,22,22,0,33,23],
[21,18,24,13,23,29,18,0,21],
[18,29,25,24,21,27,28,30,0]])



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
result = np.append(np.array([9, 51, 189, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,21,18,27,25,32,22,23],
[31,0,22,25,29,24,29,26,26],
[30,29,0,21,28,24,35,25,23],
[33,26,30,0,28,24,30,22,24],
[24,22,23,23,0,18,33,23,22],
[26,27,27,27,33,0,29,22,25],
[19,22,16,21,18,22,0,9,13],
[29,25,26,29,28,29,42,0,30],
[28,25,28,27,29,26,38,21,0]])



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
result = np.append(np.array([9, 51, 190, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,28,24,32,30,29,30,34],
[24,0,32,25,31,30,23,24,31],
[23,19,0,17,25,21,22,24,22],
[27,26,34,0,29,29,24,31,29],
[19,20,26,22,0,22,22,27,29],
[21,21,30,22,29,0,27,31,29],
[22,28,29,27,29,24,0,29,29],
[21,27,27,20,24,20,22,0,29],
[17,20,29,22,22,22,22,22,0]])



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
result = np.append(np.array([9, 51, 191, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,37,20,27,23,17,25,27,28],
[14,0,12,17,15,19,13,16,16],
[31,39,0,29,33,24,27,34,29],
[24,34,22,0,20,29,14,38,35],
[28,36,18,31,0,17,23,26,29],
[34,32,27,22,34,0,32,30,24],
[26,38,24,37,28,19,0,37,31],
[24,35,17,13,25,21,14,0,27],
[23,35,22,16,22,27,20,24,0]])



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
result = np.append(np.array([9, 51, 192, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,30,30,28,25,27,28,25],
[22,0,31,27,28,25,28,29,27],
[21,20,0,25,26,26,28,25,26],
[21,24,26,0,22,24,25,30,23],
[23,23,25,29,0,26,26,28,27],
[26,26,25,27,25,0,26,28,27],
[24,23,23,26,25,25,0,28,23],
[23,22,26,21,23,23,23,0,23],
[26,24,25,28,24,24,28,28,0]])



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
result = np.append(np.array([9, 51, 193, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,25,23,33,27,33,30,25],
[21,0,29,27,32,19,27,32,29],
[26,22,0,27,27,21,26,27,23],
[28,24,24,0,29,24,30,27,22],
[18,19,24,22,0,21,24,25,24],
[24,32,30,27,30,0,29,32,26],
[18,24,25,21,27,22,0,28,26],
[21,19,24,24,26,19,23,0,22],
[26,22,28,29,27,25,25,29,0]])



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
result = np.append(np.array([9, 51, 194, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,26,25,17,39,23,20,26],
[33,0,33,27,23,32,36,25,25],
[25,18,0,32,15,28,27,22,15],
[26,24,19,0,19,26,22,22,16],
[34,28,36,32,0,36,26,22,27],
[12,19,23,25,15,0,18,17,14],
[28,15,24,29,25,33,0,24,22],
[31,26,29,29,29,34,27,0,25],
[25,26,36,35,24,37,29,26,0]])



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
result = np.append(np.array([9, 51, 195, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,28,24,23,20,25,15,20],
[37,0,32,32,25,36,24,23,25],
[23,19,0,22,23,26,23,21,11],
[27,19,29,0,25,28,30,18,18],
[28,26,28,26,0,36,28,33,14],
[31,15,25,23,15,0,18,20,12],
[26,27,28,21,23,33,0,23,17],
[36,28,30,33,18,31,28,0,27],
[31,26,40,33,37,39,34,24,0]])



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
result = np.append(np.array([9, 51, 196, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,21,22,26,27,16,27,16],
[30,0,22,26,22,36,27,24,15],
[30,29,0,35,31,38,30,24,26],
[29,25,16,0,33,23,24,29,14],
[25,29,20,18,0,25,27,26,26],
[24,15,13,28,26,0,17,18,12],
[35,24,21,27,24,34,0,25,23],
[24,27,27,22,25,33,26,0,26],
[35,36,25,37,25,39,28,25,0]])



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
result = np.append(np.array([9, 51, 197, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,20,26,23,23,22,27,18],
[22,0,14,19,23,24,20,23,19],
[31,37,0,31,22,29,28,32,26],
[25,32,20,0,24,18,14,25,17],
[28,28,29,27,0,28,22,31,24],
[28,27,22,33,23,0,22,29,27],
[29,31,23,37,29,29,0,30,27],
[24,28,19,26,20,22,21,0,23],
[33,32,25,34,27,24,24,28,0]])



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
result = np.append(np.array([9, 51, 198, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,30,24,23,24,29,29,26],
[21,0,30,23,20,24,27,29,29],
[21,21,0,18,17,20,19,20,19],
[27,28,33,0,29,27,23,28,32],
[28,31,34,22,0,21,29,33,29],
[27,27,31,24,30,0,30,27,26],
[22,24,32,28,22,21,0,25,23],
[22,22,31,23,18,24,26,0,20],
[25,22,32,19,22,25,28,31,0]])



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
result = np.append(np.array([9, 51, 199, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,26,30,27,26,27,22,31],
[25,0,25,22,23,26,25,20,28],
[25,26,0,22,24,18,25,22,25],
[21,29,29,0,32,24,27,26,28],
[24,28,27,19,0,19,23,19,26],
[25,25,33,27,32,0,29,25,27],
[24,26,26,24,28,22,0,26,26],
[29,31,29,25,32,26,25,0,25],
[20,23,26,23,25,24,25,26,0]])



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
result = np.append(np.array([9, 51, 200, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbrcw/mebbrcw_9_51.csv", index=False, header=False)