
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 1
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,13,6,9,10,8,15,14,9,11,8],
[13,0,8,10,7,7,11,14,11,10,11],
[20,18,0,15,13,13,15,13,9,17,11],
[17,16,11,0,15,9,13,15,14,11,11],
[16,19,13,11,0,13,15,17,14,15,12],
[18,19,13,17,13,0,18,18,17,17,10],
[11,15,11,13,11,8,0,11,13,14,14],
[12,12,13,11,9,8,15,0,11,10,11],
[17,15,17,12,12,9,13,15,0,15,8],
[15,16,9,15,11,9,12,16,11,0,10],
[18,15,15,15,14,16,12,15,18,16,0]])



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
result = np.append(np.array([11, 26, 1, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,11,12,9,11,10,14,11,13,10],
[13,0,15,13,9,13,14,16,10,14,14],
[15,11,0,11,8,15,8,12,10,10,9],
[14,13,15,0,10,13,10,18,14,11,11],
[17,17,18,16,0,15,19,19,11,17,14],
[15,13,11,13,11,0,8,16,15,13,11],
[16,12,18,16,7,18,0,17,14,15,12],
[12,10,14,8,7,10,9,0,7,10,9],
[15,16,16,12,15,11,12,19,0,14,10],
[13,12,16,15,9,13,11,16,12,0,12],
[16,12,17,15,12,15,14,17,16,14,0]])



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
result = np.append(np.array([11, 26, 2, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,18,21,16,12,11,9,14,14,14],
[15,0,14,21,16,17,14,18,10,21,20],
[8,12,0,22,11,7,10,10,10,15,6],
[5,5,4,0,9,11,8,8,8,14,8],
[10,10,15,17,0,10,8,14,10,14,10],
[14,9,19,15,16,0,10,14,7,13,12],
[15,12,16,18,18,16,0,15,10,15,14],
[17,8,16,18,12,12,11,0,9,19,14],
[12,16,16,18,16,19,16,17,0,23,15],
[12,5,11,12,12,13,11,7,3,0,11],
[12,6,20,18,16,14,12,12,11,15,0]])



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
result = np.append(np.array([11, 26, 3, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,14,22,18,20,14,17,18,17,12],
[11,0,14,23,13,17,19,14,16,19,15],
[12,12,0,17,10,16,13,13,12,10,9],
[4,3,9,0,9,12,2,5,11,11,9],
[8,13,16,17,0,10,11,14,13,16,10],
[6,9,10,14,16,0,8,12,9,10,5],
[12,7,13,24,15,18,0,16,14,15,13],
[9,12,13,21,12,14,10,0,11,15,13],
[8,10,14,15,13,17,12,15,0,14,13],
[9,7,16,15,10,16,11,11,12,0,14],
[14,11,17,17,16,21,13,13,13,12,0]])



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
result = np.append(np.array([11, 26, 4, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,2,20,19,13,14,14,14,14,20],
[6,0,8,25,18,13,14,20,13,7,13],
[24,18,0,18,24,13,19,12,18,19,18],
[6,1,8,0,19,7,7,13,12,8,7],
[7,8,2,7,0,1,2,14,7,2,7],
[13,13,13,19,25,0,14,19,7,13,19],
[12,12,7,19,24,12,0,18,13,13,19],
[12,6,14,13,12,7,8,0,13,7,7],
[12,13,8,14,19,19,13,13,0,14,13],
[12,19,7,18,24,13,13,19,12,0,18],
[6,13,8,19,19,7,7,19,13,8,0]])



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
result = np.append(np.array([11, 26, 5, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,10,10,13,7,13,10,6,13,16],
[17,0,7,11,13,13,10,16,12,12,14],
[16,19,0,16,21,19,17,13,12,14,18],
[16,15,10,0,16,12,12,16,9,15,18],
[13,13,5,10,0,9,5,9,3,12,14],
[19,13,7,14,17,0,12,16,12,16,19],
[13,16,9,14,21,14,0,12,12,10,18],
[16,10,13,10,17,10,14,0,13,15,18],
[20,14,14,17,23,14,14,13,0,20,16],
[13,14,12,11,14,10,16,11,6,0,17],
[10,12,8,8,12,7,8,8,10,9,0]])



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
result = np.append(np.array([11, 26, 6, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,15,15,12,12,14,13,13,14,15],
[7,0,8,13,6,5,11,7,11,9,5],
[11,18,0,15,8,11,13,8,11,14,11],
[11,13,11,0,8,9,16,10,15,15,10],
[14,20,18,18,0,14,16,12,20,19,12],
[14,21,15,17,12,0,17,14,14,22,12],
[12,15,13,10,10,9,0,10,15,13,12],
[13,19,18,16,14,12,16,0,18,20,13],
[13,15,15,11,6,12,11,8,0,15,10],
[12,17,12,11,7,4,13,6,11,0,11],
[11,21,15,16,14,14,14,13,16,15,0]])



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
result = np.append(np.array([11, 26, 7, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,11,11,13,14,7,10,17,14,7],
[9,0,10,13,8,10,9,10,15,8,6],
[15,16,0,11,12,13,11,7,16,13,6],
[15,13,15,0,17,14,10,13,20,14,8],
[13,18,14,9,0,13,12,12,19,16,9],
[12,16,13,12,13,0,9,10,16,10,5],
[19,17,15,16,14,17,0,12,18,16,11],
[16,16,19,13,14,16,14,0,18,15,13],
[9,11,10,6,7,10,8,8,0,10,5],
[12,18,13,12,10,16,10,11,16,0,10],
[19,20,20,18,17,21,15,13,21,16,0]])



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
result = np.append(np.array([11, 26, 8, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,9,11,7,7,10,11,12,12],
[13,0,15,10,12,13,12,14,12,13,12],
[13,11,0,7,12,10,8,13,13,11,11],
[17,16,19,0,13,14,15,17,17,18,15],
[15,14,14,13,0,11,11,14,10,14,10],
[19,13,16,12,15,0,10,16,15,16,13],
[19,14,18,11,15,16,0,18,14,17,12],
[16,12,13,9,12,10,8,0,13,13,8],
[15,14,13,9,16,11,12,13,0,13,9],
[14,13,15,8,12,10,9,13,13,0,12],
[14,14,15,11,16,13,14,18,17,14,0]])



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
result = np.append(np.array([11, 26, 9, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,18,17,16,16,15,16,15,13,16],
[9,0,12,12,13,13,11,12,14,7,10],
[8,14,0,14,15,16,10,12,14,9,12],
[9,14,12,0,15,13,14,14,14,8,13],
[10,13,11,11,0,12,9,14,10,8,11],
[10,13,10,13,14,0,12,13,17,9,11],
[11,15,16,12,17,14,0,15,13,13,11],
[10,14,14,12,12,13,11,0,15,11,15],
[11,12,12,12,16,9,13,11,0,9,10],
[13,19,17,18,18,17,13,15,17,0,16],
[10,16,14,13,15,15,15,11,16,10,0]])



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
result = np.append(np.array([11, 26, 10, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,13,10,13,11,9,14,14,12,8],
[16,0,15,11,13,16,14,15,13,12,13],
[13,11,0,13,11,9,10,10,10,9,8],
[16,15,13,0,15,15,11,15,13,14,10],
[13,13,15,11,0,12,11,14,10,18,9],
[15,10,17,11,14,0,12,13,15,16,11],
[17,12,16,15,15,14,0,14,18,18,12],
[12,11,16,11,12,13,12,0,11,11,6],
[12,13,16,13,16,11,8,15,0,13,8],
[14,14,17,12,8,10,8,15,13,0,7],
[18,13,18,16,17,15,14,20,18,19,0]])



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
result = np.append(np.array([11, 26, 11, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,21,21,17,13,15,21,15,18,19],
[9,0,18,14,12,13,14,20,14,18,13],
[5,8,0,8,7,12,5,13,9,11,6],
[5,12,18,0,9,9,14,12,9,14,13],
[9,14,19,17,0,7,10,19,8,17,12],
[13,13,14,17,19,0,15,16,15,15,15],
[11,12,21,12,16,11,0,15,11,18,15],
[5,6,13,14,7,10,11,0,9,7,7],
[11,12,17,17,18,11,15,17,0,13,11],
[8,8,15,12,9,11,8,19,13,0,14],
[7,13,20,13,14,11,11,19,15,12,0]])



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
result = np.append(np.array([11, 26, 12, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,15,17,15,17,12,17,10,12],
[15,0,16,17,19,18,16,14,18,16,11],
[15,10,0,13,16,15,15,15,15,14,14],
[11,9,13,0,12,10,12,13,17,12,7],
[9,7,10,14,0,13,16,13,13,14,7],
[11,8,11,16,13,0,17,11,17,16,13],
[9,10,11,14,10,9,0,14,15,14,12],
[14,12,11,13,13,15,12,0,18,17,14],
[9,8,11,9,13,9,11,8,0,11,10],
[16,10,12,14,12,10,12,9,15,0,11],
[14,15,12,19,19,13,14,12,16,15,0]])



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
result = np.append(np.array([11, 26, 13, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,13,13,15,10,8,11,10,11,12],
[16,0,11,8,9,4,9,11,16,16,15],
[13,15,0,13,20,15,20,15,13,17,17],
[13,18,13,0,15,13,13,14,15,20,19],
[11,17,6,11,0,4,12,10,14,18,16],
[16,22,11,13,22,0,15,13,19,22,18],
[18,17,6,13,14,11,0,12,12,14,15],
[15,15,11,12,16,13,14,0,15,16,20],
[16,10,13,11,12,7,14,11,0,21,13],
[15,10,9,6,8,4,12,10,5,0,11],
[14,11,9,7,10,8,11,6,13,15,0]])



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
result = np.append(np.array([11, 26, 14, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,14,13,13,26,12,13,14,26,16],
[0,0,14,0,4,13,3,13,1,6,4],
[12,12,0,9,12,22,9,12,4,15,13],
[13,26,17,0,16,26,25,16,17,26,26],
[13,22,14,10,0,25,22,15,14,25,26],
[0,13,4,0,1,0,12,13,1,7,7],
[14,23,17,1,4,14,0,16,14,17,7],
[13,13,14,10,11,13,10,0,14,16,14],
[12,25,22,9,12,25,12,12,0,15,15],
[0,20,11,0,1,19,9,10,11,0,1],
[10,22,13,0,0,19,19,12,11,25,0]])



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
result = np.append(np.array([11, 26, 15, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,12,14,16,16,11,15,14,14,11],
[11,0,11,9,12,12,9,11,10,9,9],
[14,15,0,10,15,14,16,12,13,13,12],
[12,17,16,0,18,19,15,13,12,10,14],
[10,14,11,8,0,13,10,12,9,10,9],
[10,14,12,7,13,0,13,12,10,12,7],
[15,17,10,11,16,13,0,13,7,10,7],
[11,15,14,13,14,14,13,0,13,10,10],
[12,16,13,14,17,16,19,13,0,12,11],
[12,17,13,16,16,14,16,16,14,0,11],
[15,17,14,12,17,19,19,16,15,15,0]])



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
result = np.append(np.array([11, 26, 16, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,17,9,13,7,13,13,13,17,17],
[13,0,17,13,4,14,13,20,13,20,21],
[9,9,0,11,8,12,12,14,9,23,14],
[17,13,15,0,13,17,18,18,13,18,18],
[13,22,18,13,0,11,13,16,16,21,21],
[19,12,14,9,15,0,7,15,11,15,11],
[13,13,14,8,13,19,0,17,17,17,22],
[13,6,12,8,10,11,9,0,13,17,13],
[13,13,17,13,10,15,9,13,0,17,22],
[9,6,3,8,5,11,9,9,9,0,13],
[9,5,12,8,5,15,4,13,4,13,0]])



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
result = np.append(np.array([11, 26, 17, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,19,12,15,10,14,13,12,8],
[15,0,16,20,14,18,14,16,14,13,10],
[15,10,0,19,12,16,13,14,15,15,13],
[7,6,7,0,9,14,6,11,10,12,6],
[14,12,14,17,0,13,13,16,13,14,11],
[11,8,10,12,13,0,14,14,11,14,8],
[16,12,13,20,13,12,0,15,9,17,9],
[12,10,12,15,10,12,11,0,8,13,7],
[13,12,11,16,13,15,17,18,0,11,9],
[14,13,11,14,12,12,9,13,15,0,10],
[18,16,13,20,15,18,17,19,17,16,0]])



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
result = np.append(np.array([11, 26, 18, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,12,7,15,10,9,11,9,15,7],
[15,0,11,12,11,11,14,8,15,14,13],
[14,15,0,9,13,11,15,10,14,21,10],
[19,14,17,0,16,10,17,15,12,15,15],
[11,15,13,10,0,9,10,9,10,17,10],
[16,15,15,16,17,0,14,12,13,18,15],
[17,12,11,9,16,12,0,7,8,16,13],
[15,18,16,11,17,14,19,0,16,18,14],
[17,11,12,14,16,13,18,10,0,16,16],
[11,12,5,11,9,8,10,8,10,0,11],
[19,13,16,11,16,11,13,12,10,15,0]])



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
result = np.append(np.array([11, 26, 19, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,12,11,15,8,10,2,7,6,10],
[19,0,24,18,21,20,14,18,21,21,11],
[14,2,0,6,15,12,13,7,6,9,2],
[15,8,20,0,11,13,9,13,10,13,6],
[11,5,11,15,0,9,4,6,10,6,2],
[18,6,14,13,17,0,10,13,18,14,9],
[16,12,13,17,22,16,0,8,13,16,13],
[24,8,19,13,20,13,18,0,15,15,16],
[19,5,20,16,16,8,13,11,0,15,11],
[20,5,17,13,20,12,10,11,11,0,12],
[16,15,24,20,24,17,13,10,15,14,0]])



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
result = np.append(np.array([11, 26, 20, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,12,16,13,9,9,15,12,14,14],
[11,0,12,17,12,10,7,14,8,11,10],
[14,14,0,15,16,8,8,12,14,15,14],
[10,9,11,0,12,9,7,15,11,8,11],
[13,14,10,14,0,11,8,15,13,10,14],
[17,16,18,17,15,0,13,15,16,13,15],
[17,19,18,19,18,13,0,18,16,15,16],
[11,12,14,11,11,11,8,0,12,11,13],
[14,18,12,15,13,10,10,14,0,13,15],
[12,15,11,18,16,13,11,15,13,0,15],
[12,16,12,15,12,11,10,13,11,11,0]])



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
result = np.append(np.array([11, 26, 21, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,17,15,13,16,16,17,14,18,15],
[7,0,13,11,9,11,10,10,8,11,9],
[9,13,0,11,10,12,12,10,9,13,10],
[11,15,15,0,11,13,10,13,14,14,11],
[13,17,16,15,0,16,15,14,11,15,11],
[10,15,14,13,10,0,14,14,13,15,13],
[10,16,14,16,11,12,0,12,10,12,14],
[9,16,16,13,12,12,14,0,11,13,11],
[12,18,17,12,15,13,16,15,0,15,13],
[8,15,13,12,11,11,14,13,11,0,8],
[11,17,16,15,15,13,12,15,13,18,0]])



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
result = np.append(np.array([11, 26, 22, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,16,19,14,11,14,14,17,22,18],
[8,0,13,9,9,10,11,10,11,12,11],
[10,13,0,14,9,14,16,12,13,18,19],
[7,17,12,0,10,15,13,10,14,12,14],
[12,17,17,16,0,16,21,17,18,19,14],
[15,16,12,11,10,0,12,11,11,17,18],
[12,15,10,13,5,14,0,17,13,17,10],
[12,16,14,16,9,15,9,0,18,14,14],
[9,15,13,12,8,15,13,8,0,16,17],
[4,14,8,14,7,9,9,12,10,0,11],
[8,15,7,12,12,8,16,12,9,15,0]])



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
result = np.append(np.array([11, 26, 23, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,14,19,15,15,18,15,13,14,13],
[13,0,15,22,8,18,17,11,14,18,10],
[12,11,0,17,10,17,21,14,10,16,14],
[7,4,9,0,5,17,20,7,10,15,8],
[11,18,16,21,0,18,20,17,13,11,4],
[11,8,9,9,8,0,5,5,9,18,9],
[8,9,5,6,6,21,0,6,4,15,8],
[11,15,12,19,9,21,20,0,9,15,8],
[13,12,16,16,13,17,22,17,0,17,10],
[12,8,10,11,15,8,11,11,9,0,9],
[13,16,12,18,22,17,18,18,16,17,0]])



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
result = np.append(np.array([11, 26, 24, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,17,17,14,17,17,15,13,19,12],
[14,0,13,11,8,14,14,14,13,14,14],
[9,13,0,10,7,15,17,8,6,13,13],
[9,15,16,0,17,13,16,13,15,15,11],
[12,18,19,9,0,13,21,14,8,18,14],
[9,12,11,13,13,0,18,10,12,15,11],
[9,12,9,10,5,8,0,8,3,12,10],
[11,12,18,13,12,16,18,0,9,22,15],
[13,13,20,11,18,14,23,17,0,19,15],
[7,12,13,11,8,11,14,4,7,0,7],
[14,12,13,15,12,15,16,11,11,19,0]])



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
result = np.append(np.array([11, 26, 25, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,17,10,14,10,9,10,14,11,13],
[12,0,13,4,10,9,13,9,10,10,10],
[9,13,0,7,8,11,13,8,6,9,10],
[16,22,19,0,18,17,12,15,16,13,14],
[12,16,18,8,0,9,13,7,11,11,14],
[16,17,15,9,17,0,16,14,14,13,19],
[17,13,13,14,13,10,0,11,12,10,14],
[16,17,18,11,19,12,15,0,19,13,13],
[12,16,20,10,15,12,14,7,0,9,11],
[15,16,17,13,15,13,16,13,17,0,13],
[13,16,16,12,12,7,12,13,15,13,0]])



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
result = np.append(np.array([11, 26, 26, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,16,6,8,9,14,6,17,4,9],
[21,0,20,12,10,9,9,11,12,9,14],
[10,6,0,5,9,14,10,11,18,9,14],
[20,14,21,0,9,14,19,17,17,14,15],
[18,16,17,17,0,10,15,16,18,10,19],
[17,17,12,12,16,0,17,17,13,14,15],
[12,17,16,7,11,9,0,7,13,5,10],
[20,15,15,9,10,9,19,0,15,9,14],
[9,14,8,9,8,13,13,11,0,13,14],
[22,17,17,12,16,12,21,17,13,0,17],
[17,12,12,11,7,11,16,12,12,9,0]])



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
result = np.append(np.array([11, 26, 27, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,7,22,15,22,15,14,13,14,17],
[11,0,15,7,17,16,9,7,9,16,9],
[19,11,0,18,15,23,20,17,19,10,18],
[4,19,8,0,17,18,7,5,11,16,5],
[11,9,11,9,0,16,9,7,9,12,11],
[4,10,3,8,10,0,3,2,11,12,10],
[11,17,6,19,17,23,0,16,11,16,17],
[12,19,9,21,19,24,10,0,9,18,12],
[13,17,7,15,17,15,15,17,0,16,13],
[12,10,16,10,14,14,10,8,10,0,10],
[9,17,8,21,15,16,9,14,13,16,0]])



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
result = np.append(np.array([11, 26, 28, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,13,19,17,19,16,20,23,18,20],
[7,0,7,14,13,14,2,11,19,14,11],
[13,19,0,16,14,11,14,12,16,13,19],
[7,12,10,0,17,11,10,10,21,6,17],
[9,13,12,9,0,10,8,11,13,9,16],
[7,12,15,15,16,0,6,17,18,9,22],
[10,24,12,16,18,20,0,14,21,13,17],
[6,15,14,16,15,9,12,0,21,10,18],
[3,7,10,5,13,8,5,5,0,9,17],
[8,12,13,20,17,17,13,16,17,0,17],
[6,15,7,9,10,4,9,8,9,9,0]])



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
result = np.append(np.array([11, 26, 29, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,10,17,10,22,17,17,11,13],
[15,0,13,19,19,12,22,15,19,6,15],
[15,13,0,17,20,19,22,13,24,13,15],
[16,7,9,0,9,13,22,9,19,13,9],
[9,7,6,17,0,13,22,7,19,13,9],
[16,14,7,13,13,0,22,14,13,9,14],
[4,4,4,4,4,4,0,4,10,4,4],
[9,11,13,17,19,12,22,0,19,6,15],
[9,7,2,7,7,13,16,7,0,6,9],
[15,20,13,13,13,17,22,20,20,0,20],
[13,11,11,17,17,12,22,11,17,6,0]])



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
result = np.append(np.array([11, 26, 30, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,13,14,15,13,12,10,13,15,13],
[12,0,12,12,7,13,14,8,7,9,6],
[13,14,0,11,12,11,15,11,10,9,11],
[12,14,15,0,14,13,13,12,11,14,14],
[11,19,14,12,0,15,16,13,11,13,12],
[13,13,15,13,11,0,12,7,12,12,12],
[14,12,11,13,10,14,0,10,11,11,11],
[16,18,15,14,13,19,16,0,15,14,15],
[13,19,16,15,15,14,15,11,0,16,15],
[11,17,17,12,13,14,15,12,10,0,16],
[13,20,15,12,14,14,15,11,11,10,0]])



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
result = np.append(np.array([11, 26, 31, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,7,8,10,13,11,16,12,11,11],
[15,0,13,13,11,14,13,17,13,14,14],
[19,13,0,14,14,15,17,16,13,18,12],
[18,13,12,0,12,11,16,15,13,18,15],
[16,15,12,14,0,15,16,17,17,19,15],
[13,12,11,15,11,0,13,19,15,17,16],
[15,13,9,10,10,13,0,15,14,16,12],
[10,9,10,11,9,7,11,0,9,11,10],
[14,13,13,13,9,11,12,17,0,14,13],
[15,12,8,8,7,9,10,15,12,0,12],
[15,12,14,11,11,10,14,16,13,14,0]])



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
result = np.append(np.array([11, 26, 32, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,16,12,17,13,14,15,15,16,15],
[13,0,14,12,17,15,17,18,14,16,15],
[10,12,0,11,11,13,15,16,16,15,11],
[14,14,15,0,17,13,18,16,15,18,17],
[9,9,15,9,0,10,16,14,12,15,10],
[13,11,13,13,16,0,17,14,14,18,14],
[12,9,11,8,10,9,0,15,11,13,9],
[11,8,10,10,12,12,11,0,10,14,13],
[11,12,10,11,14,12,15,16,0,14,11],
[10,10,11,8,11,8,13,12,12,0,11],
[11,11,15,9,16,12,17,13,15,15,0]])



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
result = np.append(np.array([11, 26, 33, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,13,9,8,11,11,16,11,11,10],
[20,0,17,12,7,15,13,20,14,13,15],
[13,9,0,8,8,9,16,22,11,11,13],
[17,14,18,0,15,14,16,20,16,13,16],
[18,19,18,11,0,13,18,21,16,13,18],
[15,11,17,12,13,0,19,20,12,11,14],
[15,13,10,10,8,7,0,13,11,9,10],
[10,6,4,6,5,6,13,0,4,5,8],
[15,12,15,10,10,14,15,22,0,14,15],
[15,13,15,13,13,15,17,21,12,0,13],
[16,11,13,10,8,12,16,18,11,13,0]])



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
result = np.append(np.array([11, 26, 34, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,17,16,19,14,14,16,13,13,15],
[6,0,12,6,16,9,9,14,9,9,9],
[9,14,0,11,17,17,18,18,10,14,12],
[10,20,15,0,17,12,13,16,11,13,10],
[7,10,9,9,0,11,12,15,7,8,8],
[12,17,9,14,15,0,12,14,10,12,9],
[12,17,8,13,14,14,0,12,7,8,8],
[10,12,8,10,11,12,14,0,10,6,10],
[13,17,16,15,19,16,19,16,0,15,18],
[13,17,12,13,18,14,18,20,11,0,9],
[11,17,14,16,18,17,18,16,8,17,0]])



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
result = np.append(np.array([11, 26, 35, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,13,12,11,8,12,11,6,12,9],
[15,0,14,11,12,15,11,15,10,11,9],
[13,12,0,10,9,8,12,12,7,9,12],
[14,15,16,0,11,10,14,18,13,12,13],
[15,14,17,15,0,13,14,14,10,11,10],
[18,11,18,16,13,0,15,18,13,10,14],
[14,15,14,12,12,11,0,15,13,13,11],
[15,11,14,8,12,8,11,0,8,11,11],
[20,16,19,13,16,13,13,18,0,15,12],
[14,15,17,14,15,16,13,15,11,0,12],
[17,17,14,13,16,12,15,15,14,14,0]])



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
result = np.append(np.array([11, 26, 36, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,13,13,19,11,13,9,12,12,11],
[16,0,11,16,18,11,16,11,12,11,10],
[13,15,0,19,11,12,11,18,11,15,15],
[13,10,7,0,11,13,10,8,5,10,10],
[7,8,15,15,0,11,13,10,11,9,9],
[15,15,14,13,15,0,14,11,12,14,9],
[13,10,15,16,13,12,0,10,14,12,9],
[17,15,8,18,16,15,16,0,8,12,12],
[14,14,15,21,15,14,12,18,0,12,12],
[14,15,11,16,17,12,14,14,14,0,16],
[15,16,11,16,17,17,17,14,14,10,0]])



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
result = np.append(np.array([11, 26, 37, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,12,15,16,10,11,18,13,12],
[15,0,16,12,16,12,14,14,18,13,17],
[15,10,0,11,14,9,13,7,17,10,14],
[14,14,15,0,15,10,12,10,14,13,15],
[11,10,12,11,0,11,7,7,15,9,10],
[10,14,17,16,15,0,9,11,15,13,16],
[16,12,13,14,19,17,0,12,19,12,11],
[15,12,19,16,19,15,14,0,14,16,17],
[8,8,9,12,11,11,7,12,0,7,14],
[13,13,16,13,17,13,14,10,19,0,17],
[14,9,12,11,16,10,15,9,12,9,0]])



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
result = np.append(np.array([11, 26, 38, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,17,22,22,22,17,14,13,9,13],
[8,0,8,26,17,15,17,13,13,8,17],
[9,18,0,18,22,16,14,18,13,9,13],
[4,0,8,0,8,8,4,0,4,4,4],
[4,9,4,18,0,15,9,13,13,0,13],
[4,11,10,18,11,0,6,18,13,5,13],
[9,9,12,22,17,20,0,16,11,9,11],
[12,13,8,26,13,8,10,0,8,13,10],
[13,13,13,22,13,13,15,18,0,9,6],
[17,18,17,22,26,21,17,13,17,0,17],
[13,9,13,22,13,13,15,16,20,9,0]])



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
result = np.append(np.array([11, 26, 39, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,15,20,12,11,18,18,11,10,16],
[13,0,15,19,13,12,13,19,12,19,18],
[11,11,0,12,9,13,12,14,5,5,8],
[6,7,14,0,11,8,13,15,11,9,12],
[14,13,17,15,0,13,20,20,10,13,10],
[15,14,13,18,13,0,18,19,10,12,14],
[8,13,14,13,6,8,0,20,5,12,13],
[8,7,12,11,6,7,6,0,11,11,10],
[15,14,21,15,16,16,21,15,0,9,14],
[16,7,21,17,13,14,14,15,17,0,17],
[10,8,18,14,16,12,13,16,12,9,0]])



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
result = np.append(np.array([11, 26, 40, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,4,12,18,13,7,13,9,14,3],
[9,0,0,8,21,9,4,11,1,13,3],
[22,26,0,26,22,16,16,14,17,26,12],
[14,18,0,0,22,13,16,11,14,22,9],
[8,5,4,4,0,8,5,10,1,17,4],
[13,17,10,13,18,0,7,13,9,13,0],
[19,22,10,10,21,19,0,10,11,13,13],
[13,15,12,15,16,13,16,0,12,17,12],
[17,25,9,12,25,17,15,14,0,17,12],
[12,13,0,4,9,13,13,9,9,0,4],
[23,23,14,17,22,26,13,14,14,22,0]])



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
result = np.append(np.array([11, 26, 41, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,17,12,14,10,11,14,16,14,13],
[11,0,15,13,11,12,11,15,12,12,14],
[9,11,0,8,11,9,8,12,11,8,12],
[14,13,18,0,16,17,13,13,14,12,14],
[12,15,15,10,0,15,9,13,13,9,10],
[16,14,17,9,11,0,10,13,13,13,15],
[15,15,18,13,17,16,0,15,16,15,15],
[12,11,14,13,13,13,11,0,15,12,13],
[10,14,15,12,13,13,10,11,0,13,16],
[12,14,18,14,17,13,11,14,13,0,12],
[13,12,14,12,16,11,11,13,10,14,0]])



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
result = np.append(np.array([11, 26, 42, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,13,8,13,8,18,13,13,13,13],
[16,0,16,8,21,16,13,16,16,21,21],
[13,10,0,5,5,13,5,13,5,21,13],
[18,18,21,0,21,18,18,26,26,21,13],
[13,5,21,5,0,13,10,13,5,21,18],
[18,10,13,8,13,0,18,18,18,13,13],
[8,13,21,8,16,8,0,8,16,21,13],
[13,10,13,0,13,8,18,0,13,13,13],
[13,10,21,0,21,8,10,13,0,21,13],
[13,5,5,5,5,13,5,13,5,0,18],
[13,5,13,13,8,13,13,13,13,8,0]])



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
result = np.append(np.array([11, 26, 43, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,12,12,15,8,12,12,11,15,12],
[12,0,10,13,15,12,10,13,8,10,10],
[14,16,0,14,15,12,14,15,11,13,11],
[14,13,12,0,13,12,11,12,11,13,12],
[11,11,11,13,0,10,10,12,9,12,10],
[18,14,14,14,16,0,13,13,15,14,9],
[14,16,12,15,16,13,0,18,15,14,10],
[14,13,11,14,14,13,8,0,11,14,10],
[15,18,15,15,17,11,11,15,0,14,14],
[11,16,13,13,14,12,12,12,12,0,11],
[14,16,15,14,16,17,16,16,12,15,0]])



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
result = np.append(np.array([11, 26, 44, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,12,19,15,13,11,12,14,15,13],
[8,0,13,22,11,8,10,11,12,16,11],
[14,13,0,19,12,17,11,15,15,18,14],
[7,4,7,0,6,7,6,10,10,10,8],
[11,15,14,20,0,13,14,14,15,18,20],
[13,18,9,19,13,0,12,15,14,16,12],
[15,16,15,20,12,14,0,20,14,19,15],
[14,15,11,16,12,11,6,0,15,18,14],
[12,14,11,16,11,12,12,11,0,18,17],
[11,10,8,16,8,10,7,8,8,0,10],
[13,15,12,18,6,14,11,12,9,16,0]])



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
result = np.append(np.array([11, 26, 45, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,20,13,16,11,13,18,11,11,16],
[11,0,19,17,22,16,18,16,15,12,19],
[6,7,0,11,13,7,13,8,3,8,10],
[13,9,15,0,18,15,16,12,9,15,15],
[10,4,13,8,0,11,8,13,5,8,5],
[15,10,19,11,15,0,15,13,9,13,9],
[13,8,13,10,18,11,0,15,11,6,13],
[8,10,18,14,13,13,11,0,7,9,14],
[15,11,23,17,21,17,15,19,0,13,15],
[15,14,18,11,18,13,20,17,13,0,14],
[10,7,16,11,21,17,13,12,11,12,0]])



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
result = np.append(np.array([11, 26, 46, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,15,12,15,14,13,10,13,14],
[13,0,10,14,10,14,11,10,9,14,11],
[13,16,0,18,16,18,12,13,11,16,18],
[11,12,8,0,10,12,12,12,9,12,11],
[14,16,10,16,0,19,11,15,9,14,14],
[11,12,8,14,7,0,10,11,7,12,12],
[12,15,14,14,15,16,0,12,13,15,14],
[13,16,13,14,11,15,14,0,15,15,15],
[16,17,15,17,17,19,13,11,0,19,15],
[13,12,10,14,12,14,11,11,7,0,11],
[12,15,8,15,12,14,12,11,11,15,0]])



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
result = np.append(np.array([11, 26, 47, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,9,14,12,8,13,10,10,10,7],
[16,0,13,14,12,17,17,14,14,10,10],
[17,13,0,15,12,12,12,12,13,11,8],
[12,12,11,0,9,8,14,9,10,6,7],
[14,14,14,17,0,17,18,20,18,15,12],
[18,9,14,18,9,0,13,15,14,12,11],
[13,9,14,12,8,13,0,9,14,13,6],
[16,12,14,17,6,11,17,0,14,11,13],
[16,12,13,16,8,12,12,12,0,9,10],
[16,16,15,20,11,14,13,15,17,0,11],
[19,16,18,19,14,15,20,13,16,15,0]])



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
result = np.append(np.array([11, 26, 48, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,18,10,14,15,16,16,8,14,18],
[12,0,18,12,14,13,14,11,10,13,12],
[8,8,0,11,11,11,11,14,7,8,11],
[16,14,15,0,13,17,15,17,13,13,14],
[12,12,15,13,0,11,10,17,9,15,16],
[11,13,15,9,15,0,11,13,9,12,12],
[10,12,15,11,16,15,0,17,11,13,17],
[10,15,12,9,9,13,9,0,9,11,10],
[18,16,19,13,17,17,15,17,0,18,16],
[12,13,18,13,11,14,13,15,8,0,13],
[8,14,15,12,10,14,9,16,10,13,0]])



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
result = np.append(np.array([11, 26, 49, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,11,11,11,18,10,14,18,11,14],
[13,0,14,12,7,14,11,13,16,14,10],
[15,12,0,12,10,14,9,11,16,12,9],
[15,14,14,0,11,13,12,14,15,13,17],
[15,19,16,15,0,15,13,14,16,10,13],
[8,12,12,13,11,0,9,10,13,7,9],
[16,15,17,14,13,17,0,14,19,13,15],
[12,13,15,12,12,16,12,0,14,10,13],
[8,10,10,11,10,13,7,12,0,10,10],
[15,12,14,13,16,19,13,16,16,0,11],
[12,16,17,9,13,17,11,13,16,15,0]])



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
result = np.append(np.array([11, 26, 50, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,20,17,15,19,15,19,21,18,21],
[13,0,18,14,17,14,14,21,18,17,16],
[6,8,0,8,10,8,10,15,14,11,10],
[9,12,18,0,14,16,10,15,18,19,17],
[11,9,16,12,0,9,7,14,10,10,13],
[7,12,18,10,17,0,9,15,15,10,18],
[11,12,16,16,19,17,0,14,17,21,21],
[7,5,11,11,12,11,12,0,10,14,11],
[5,8,12,8,16,11,9,16,0,11,16],
[8,9,15,7,16,16,5,12,15,0,16],
[5,10,16,9,13,8,5,15,10,10,0]])



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
result = np.append(np.array([11, 26, 51, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,7,11,16,9,7,8,16,15,11],
[14,0,9,6,16,8,10,10,10,19,13],
[19,17,0,19,16,10,10,10,11,18,12],
[15,20,7,0,14,8,12,7,11,15,16],
[10,10,10,12,0,7,7,12,13,16,13],
[17,18,16,18,19,0,15,12,16,23,21],
[19,16,16,14,19,11,0,13,16,24,16],
[18,16,16,19,14,14,13,0,17,22,18],
[10,16,15,15,13,10,10,9,0,16,12],
[11,7,8,11,10,3,2,4,10,0,4],
[15,13,14,10,13,5,10,8,14,22,0]])



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
result = np.append(np.array([11, 26, 52, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,16,0,6,10,4,10,3,22,6],
[17,0,20,14,16,14,17,14,7,20,20],
[10,6,0,10,3,10,0,10,0,19,3],
[26,12,16,0,12,13,7,13,3,26,12],
[20,10,23,14,0,14,4,14,4,23,13],
[16,12,16,13,12,0,7,17,7,26,16],
[22,9,26,19,22,19,0,13,9,22,12],
[16,12,16,13,12,9,13,0,13,26,12],
[23,19,26,23,22,19,17,13,0,26,22],
[4,6,7,0,3,0,4,0,0,0,3],
[20,6,23,14,13,10,14,14,4,23,0]])



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
result = np.append(np.array([11, 26, 53, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,15,11,10,11,13,16,10,12],
[13,0,11,12,12,11,10,15,14,12,11],
[13,15,0,10,11,10,8,14,13,13,10],
[11,14,16,0,16,13,10,14,12,11,11],
[15,14,15,10,0,12,12,17,15,12,10],
[16,15,16,13,14,0,12,15,17,16,10],
[15,16,18,16,14,14,0,18,14,12,15],
[13,11,12,12,9,11,8,0,17,13,5],
[10,12,13,14,11,9,12,9,0,8,9],
[16,14,13,15,14,10,14,13,18,0,11],
[14,15,16,15,16,16,11,21,17,15,0]])



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
result = np.append(np.array([11, 26, 54, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,13,13,17,12,10,14,14,11,12],
[14,0,13,10,15,13,13,13,14,7,14],
[13,13,0,12,16,16,9,13,15,9,14],
[13,16,14,0,16,13,15,14,17,13,14],
[9,11,10,10,0,11,10,9,14,8,7],
[14,13,10,13,15,0,10,14,15,12,13],
[16,13,17,11,16,16,0,14,14,11,13],
[12,13,13,12,17,12,12,0,13,10,13],
[12,12,11,9,12,11,12,13,0,8,13],
[15,19,17,13,18,14,15,16,18,0,13],
[14,12,12,12,19,13,13,13,13,13,0]])



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
result = np.append(np.array([11, 26, 55, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,16,10,11,11,12,13,12,10,10],
[18,0,20,14,17,15,19,14,17,16,13],
[10,6,0,11,11,10,11,9,11,9,10],
[16,12,15,0,16,12,16,15,15,14,14],
[15,9,15,10,0,13,12,17,10,9,11],
[15,11,16,14,13,0,19,13,15,14,9],
[14,7,15,10,14,7,0,11,17,13,9],
[13,12,17,11,9,13,15,0,12,9,12],
[14,9,15,11,16,11,9,14,0,13,10],
[16,10,17,12,17,12,13,17,13,0,12],
[16,13,16,12,15,17,17,14,16,14,0]])



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
result = np.append(np.array([11, 26, 56, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,9,10,13,9,9,12,9,7,9],
[13,0,12,9,12,14,11,16,10,12,11],
[17,14,0,11,11,14,9,16,9,13,11],
[16,17,15,0,14,13,16,16,14,15,13],
[13,14,15,12,0,12,10,14,11,10,11],
[17,12,12,13,14,0,13,15,9,13,9],
[17,15,17,10,16,13,0,16,10,13,12],
[14,10,10,10,12,11,10,0,8,8,9],
[17,16,17,12,15,17,16,18,0,15,13],
[19,14,13,11,16,13,13,18,11,0,9],
[17,15,15,13,15,17,14,17,13,17,0]])



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
result = np.append(np.array([11, 26, 57, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,23,25,21,17,14,21,17,25,9],
[16,0,25,16,21,21,21,21,16,21,9],
[3,1,0,3,3,9,1,8,3,3,4],
[1,10,23,0,5,6,6,10,14,10,6],
[5,5,23,21,0,9,14,13,13,23,9],
[9,5,17,20,17,0,17,5,12,17,13],
[12,5,25,20,12,9,0,8,12,25,13],
[5,5,18,16,13,21,18,0,8,18,8],
[9,10,23,12,13,14,14,18,0,17,1],
[1,5,23,16,3,9,1,8,9,0,9],
[17,17,22,20,17,13,13,18,25,17,0]])



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
result = np.append(np.array([11, 26, 58, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,13,11,11,9,12,12,9,14,15],
[14,0,12,8,10,10,12,10,10,14,13],
[13,14,0,11,15,15,14,11,10,19,12],
[15,18,15,0,13,13,13,14,14,17,14],
[15,16,11,13,0,14,16,14,12,15,12],
[17,16,11,13,12,0,12,11,11,15,13],
[14,14,12,13,10,14,0,11,11,13,15],
[14,16,15,12,12,15,15,0,11,17,15],
[17,16,16,12,14,15,15,15,0,18,13],
[12,12,7,9,11,11,13,9,8,0,12],
[11,13,14,12,14,13,11,11,13,14,0]])



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
result = np.append(np.array([11, 26, 59, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,14,11,10,13,8,10,9,9,12],
[16,0,14,16,15,16,13,15,11,13,14],
[12,12,0,16,13,16,13,13,13,12,12],
[15,10,10,0,17,15,12,11,9,12,14],
[16,11,13,9,0,15,13,11,13,15,16],
[13,10,10,11,11,0,11,10,7,8,11],
[18,13,13,14,13,15,0,14,13,13,14],
[16,11,13,15,15,16,12,0,12,14,14],
[17,15,13,17,13,19,13,14,0,19,16],
[17,13,14,14,11,18,13,12,7,0,14],
[14,12,14,12,10,15,12,12,10,12,0]])



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
result = np.append(np.array([11, 26, 60, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,9,5,13,18,13,11,10,12,10],
[15,0,11,12,15,20,13,14,11,17,13],
[17,15,0,12,15,17,16,11,13,14,14],
[21,14,14,0,14,18,13,17,13,14,12],
[13,11,11,12,0,16,9,13,11,11,11],
[8,6,9,8,10,0,11,11,8,9,6],
[13,13,10,13,17,15,0,12,10,17,13],
[15,12,15,9,13,15,14,0,11,12,12],
[16,15,13,13,15,18,16,15,0,13,17],
[14,9,12,12,15,17,9,14,13,0,13],
[16,13,12,14,15,20,13,14,9,13,0]])



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
result = np.append(np.array([11, 26, 61, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,13,15,16,9,10,15,13,13,12],
[12,0,11,12,12,12,9,14,9,12,14],
[13,15,0,15,13,11,12,17,8,15,13],
[11,14,11,0,13,8,13,16,11,13,14],
[10,14,13,13,0,11,11,13,11,13,10],
[17,14,15,18,15,0,11,17,13,12,14],
[16,17,14,13,15,15,0,17,15,16,12],
[11,12,9,10,13,9,9,0,8,12,12],
[13,17,18,15,15,13,11,18,0,14,15],
[13,14,11,13,13,14,10,14,12,0,12],
[14,12,13,12,16,12,14,14,11,14,0]])



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
result = np.append(np.array([11, 26, 62, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,10,6,16,17,11,10,11,11,13],
[10,0,11,11,11,17,11,13,8,14,7],
[16,15,0,7,14,18,7,12,10,12,13],
[20,15,19,0,12,16,16,13,13,17,15],
[10,15,12,14,0,14,8,10,11,15,14],
[9,9,8,10,12,0,0,13,3,7,8],
[15,15,19,10,18,26,0,13,14,14,11],
[16,13,14,13,16,13,13,0,14,17,10],
[15,18,16,13,15,23,12,12,0,16,14],
[15,12,14,9,11,19,12,9,10,0,10],
[13,19,13,11,12,18,15,16,12,16,0]])



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
result = np.append(np.array([11, 26, 63, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,11,8,17,9,8,13,14,12,11],
[11,0,15,6,13,14,9,15,18,9,9],
[15,11,0,12,15,18,11,14,13,10,11],
[18,20,14,0,20,15,11,12,15,14,16],
[9,13,11,6,0,12,6,10,13,9,11],
[17,12,8,11,14,0,11,13,11,10,14],
[18,17,15,15,20,15,0,14,20,14,12],
[13,11,12,14,16,13,12,0,16,8,13],
[12,8,13,11,13,15,6,10,0,13,8],
[14,17,16,12,17,16,12,18,13,0,8],
[15,17,15,10,15,12,14,13,18,18,0]])



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
result = np.append(np.array([11, 26, 64, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,12,13,17,6,13,11,18,12,6],
[11,0,7,15,17,9,8,12,7,7,6],
[14,19,0,10,15,2,6,11,9,18,6],
[13,11,16,0,9,2,6,10,9,12,6],
[9,9,11,17,0,13,9,13,13,7,9],
[20,17,24,24,13,0,9,20,16,16,12],
[13,18,20,20,17,17,0,22,13,20,13],
[15,14,15,16,13,6,4,0,11,7,14],
[8,19,17,17,13,10,13,15,0,16,10],
[14,19,8,14,19,10,6,19,10,0,10],
[20,20,20,20,17,14,13,12,16,16,0]])



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
result = np.append(np.array([11, 26, 65, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,8,8,14,14,10,9,13,10,12],
[17,0,14,10,13,15,9,14,11,12,13],
[18,12,0,11,15,16,11,14,14,10,14],
[18,16,15,0,16,12,9,15,15,17,17],
[12,13,11,10,0,12,8,12,10,10,12],
[12,11,10,14,14,0,13,15,11,13,17],
[16,17,15,17,18,13,0,17,17,17,18],
[17,12,12,11,14,11,9,0,13,9,13],
[13,15,12,11,16,15,9,13,0,11,15],
[16,14,16,9,16,13,9,17,15,0,17],
[14,13,12,9,14,9,8,13,11,9,0]])



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
result = np.append(np.array([11, 26, 66, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,10,5,5,15,5,0,10,10,15],
[21,0,15,10,0,15,5,0,15,10,10],
[16,11,0,5,0,10,5,0,15,10,21],
[21,16,21,0,5,10,16,16,15,15,21],
[21,26,26,21,0,15,21,16,15,10,26],
[11,11,16,16,11,0,16,11,10,10,21],
[21,21,21,10,5,10,0,16,10,10,21],
[26,26,26,10,10,15,10,0,15,10,26],
[16,11,11,11,11,16,16,11,0,21,16],
[16,16,16,11,16,16,16,16,5,0,21],
[11,16,5,5,0,5,5,0,10,5,0]])



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
result = np.append(np.array([11, 26, 67, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,18,0,9,18,9,9,0,26,8],
[17,0,26,8,17,26,17,17,17,26,17],
[8,0,0,8,17,17,17,17,0,17,8],
[26,18,18,0,17,18,17,9,18,26,26],
[17,9,9,9,0,9,8,0,9,17,17],
[8,0,9,8,17,0,8,17,0,8,8],
[17,9,9,9,18,18,0,9,9,17,17],
[17,9,9,17,26,9,17,0,9,17,17],
[26,9,26,8,17,26,17,17,0,26,8],
[0,0,9,0,9,18,9,9,0,0,0],
[18,9,18,0,9,18,9,9,18,26,0]])



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
result = np.append(np.array([11, 26, 68, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,6,6,9,10,6,12,8,6,9],
[18,0,11,12,11,15,11,16,14,10,12],
[20,15,0,14,17,14,14,16,17,15,12],
[20,14,12,0,15,13,15,15,15,14,15],
[17,15,9,11,0,16,12,15,14,9,8],
[16,11,12,13,10,0,12,14,13,11,12],
[20,15,12,11,14,14,0,12,13,10,15],
[14,10,10,11,11,12,14,0,11,9,11],
[18,12,9,11,12,13,13,15,0,9,11],
[20,16,11,12,17,15,16,17,17,0,14],
[17,14,14,11,18,14,11,15,15,12,0]])



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
result = np.append(np.array([11, 26, 69, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,9,4,16,16,13,10,10,13,9],
[10,0,9,10,15,15,7,19,19,15,18],
[17,17,0,10,17,17,17,10,10,14,9],
[22,16,16,0,22,13,13,17,17,13,16],
[10,11,9,4,0,17,8,10,4,7,9],
[10,11,9,13,9,0,1,19,13,9,18],
[13,19,9,13,18,25,0,19,13,15,18],
[16,7,16,9,16,7,7,0,19,16,16],
[16,7,16,9,22,13,13,7,0,13,13],
[13,11,12,13,19,17,11,10,13,0,9],
[17,8,17,10,17,8,8,10,13,17,0]])



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
result = np.append(np.array([11, 26, 70, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,13,15,15,14,7,9,18,14,13],
[12,0,16,14,14,16,6,13,16,13,14],
[13,10,0,11,14,16,10,15,15,9,11],
[11,12,15,0,14,12,10,11,21,10,15],
[11,12,12,12,0,16,6,10,14,17,14],
[12,10,10,14,10,0,10,14,11,9,14],
[19,20,16,16,20,16,0,13,22,20,13],
[17,13,11,15,16,12,13,0,18,13,12],
[8,10,11,5,12,15,4,8,0,7,8],
[12,13,17,16,9,17,6,13,19,0,14],
[13,12,15,11,12,12,13,14,18,12,0]])



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
result = np.append(np.array([11, 26, 71, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,11,12,11,9,14,7,13,11,13],
[12,0,12,13,8,9,14,10,14,11,9],
[15,14,0,15,12,12,17,9,17,11,12],
[14,13,11,0,8,12,16,10,13,9,12],
[15,18,14,18,0,16,17,13,15,16,16],
[17,17,14,14,10,0,16,12,14,13,13],
[12,12,9,10,9,10,0,9,9,9,12],
[19,16,17,16,13,14,17,0,15,15,15],
[13,12,9,13,11,12,17,11,0,12,14],
[15,15,15,17,10,13,17,11,14,0,14],
[13,17,14,14,10,13,14,11,12,12,0]])



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
result = np.append(np.array([11, 26, 72, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,14,16,13,16,15,17,11,15,15],
[9,0,16,14,11,13,13,15,8,14,14],
[12,10,0,13,13,16,17,14,12,18,18],
[10,12,13,0,15,12,16,11,14,15,16],
[13,15,13,11,0,16,13,11,12,17,13],
[10,13,10,14,10,0,12,12,14,14,13],
[11,13,9,10,13,14,0,14,10,11,14],
[9,11,12,15,15,14,12,0,10,14,16],
[15,18,14,12,14,12,16,16,0,13,14],
[11,12,8,11,9,12,15,12,13,0,14],
[11,12,8,10,13,13,12,10,12,12,0]])



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
result = np.append(np.array([11, 26, 73, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,18,19,24,13,19,14,26,18,15],
[10,0,15,19,24,11,18,6,18,11,9],
[8,11,0,15,16,7,13,0,20,5,3],
[7,7,11,0,17,11,15,7,14,7,9],
[2,2,10,9,0,5,12,4,12,6,2],
[13,15,19,15,21,0,13,17,24,14,15],
[7,8,13,11,14,13,0,6,16,8,4],
[12,20,26,19,22,9,20,0,22,11,9],
[0,8,6,12,14,2,10,4,0,8,2],
[8,15,21,19,20,12,18,15,18,0,12],
[11,17,23,17,24,11,22,17,24,14,0]])



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
result = np.append(np.array([11, 26, 74, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,14,26,17,20,18,13,14,19,21],
[7,0,15,22,15,21,18,14,8,16,19],
[12,11,0,20,8,14,12,3,19,14,12],
[0,4,6,0,1,3,11,3,3,7,0],
[9,11,18,25,0,18,16,14,12,19,17],
[6,5,12,23,8,0,13,0,9,19,16],
[8,8,14,15,10,13,0,13,8,8,14],
[13,12,23,23,12,26,13,0,19,19,22],
[12,18,7,23,14,17,18,7,0,21,14],
[7,10,12,19,7,7,18,7,5,0,11],
[5,7,14,26,9,10,12,4,12,15,0]])



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
result = np.append(np.array([11, 26, 75, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,15,15,11,16,13,12,13,10,15],
[12,0,14,14,12,12,13,13,10,11,10],
[11,12,0,13,11,10,13,12,11,8,11],
[11,12,13,0,11,15,14,13,9,10,12],
[15,14,15,15,0,15,17,14,12,15,15],
[10,14,16,11,11,0,14,14,10,14,12],
[13,13,13,12,9,12,0,14,11,8,12],
[14,13,14,13,12,12,12,0,10,11,11],
[13,16,15,17,14,16,15,16,0,11,12],
[16,15,18,16,11,12,18,15,15,0,13],
[11,16,15,14,11,14,14,15,14,13,0]])



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
result = np.append(np.array([11, 26, 76, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,10,12,15,14,11,19,11,14,14],
[12,0,9,7,13,9,12,7,3,7,12],
[16,17,0,3,15,8,7,12,12,12,14],
[14,19,23,0,12,16,13,15,11,15,14],
[11,13,11,14,0,12,12,15,8,9,12],
[12,17,18,10,14,0,15,14,10,14,13],
[15,14,19,13,14,11,0,19,15,17,14],
[7,19,14,11,11,12,7,0,8,7,13],
[15,23,14,15,18,16,11,18,0,12,17],
[12,19,14,11,17,12,9,19,14,0,18],
[12,14,12,12,14,13,12,13,9,8,0]])



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
result = np.append(np.array([11, 26, 77, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,16,12,17,12,16,11,13,10,10],
[11,0,16,12,14,14,11,11,11,7,17],
[10,10,0,10,11,17,8,8,11,9,15],
[14,14,16,0,16,15,16,11,11,11,12],
[9,12,15,10,0,15,15,15,11,13,14],
[14,12,9,11,11,0,13,8,13,7,12],
[10,15,18,10,11,13,0,12,11,6,15],
[15,15,18,15,11,18,14,0,14,10,18],
[13,15,15,15,15,13,15,12,0,13,17],
[16,19,17,15,13,19,20,16,13,0,16],
[16,9,11,14,12,14,11,8,9,10,0]])



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
result = np.append(np.array([11, 26, 78, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,13,11,12,15,15,13,12,18,16],
[14,0,15,9,11,16,13,11,12,14,14],
[13,11,0,11,11,13,13,11,11,17,16],
[15,17,15,0,14,17,15,10,11,11,16],
[14,15,15,12,0,19,14,16,16,14,18],
[11,10,13,9,7,0,17,11,12,13,14],
[11,13,13,11,12,9,0,9,10,14,16],
[13,15,15,16,10,15,17,0,9,16,15],
[14,14,15,15,10,14,16,17,0,14,19],
[8,12,9,15,12,13,12,10,12,0,16],
[10,12,10,10,8,12,10,11,7,10,0]])



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
result = np.append(np.array([11, 26, 79, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,10,15,9,13,8,13,13,10,11],
[10,0,11,13,9,14,11,12,12,12,10],
[16,15,0,18,10,19,13,13,15,14,15],
[11,13,8,0,10,9,8,7,11,13,9],
[17,17,16,16,0,17,13,15,17,16,15],
[13,12,7,17,9,0,8,11,12,13,10],
[18,15,13,18,13,18,0,15,17,13,14],
[13,14,13,19,11,15,11,0,14,13,14],
[13,14,11,15,9,14,9,12,0,15,13],
[16,14,12,13,10,13,13,13,11,0,12],
[15,16,11,17,11,16,12,12,13,14,0]])



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
result = np.append(np.array([11, 26, 80, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,18,13,15,12,12,12,13,11,14],
[9,0,18,17,10,10,13,10,7,9,7],
[8,8,0,12,10,9,8,10,8,6,11],
[13,9,14,0,11,14,10,8,9,10,10],
[11,16,16,15,0,10,11,10,9,8,16],
[14,16,17,12,16,0,14,9,12,9,13],
[14,13,18,16,15,12,0,13,12,13,14],
[14,16,16,18,16,17,13,0,16,15,15],
[13,19,18,17,17,14,14,10,0,13,16],
[15,17,20,16,18,17,13,11,13,0,17],
[12,19,15,16,10,13,12,11,10,9,0]])



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
result = np.append(np.array([11, 26, 81, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,19,12,8,15,13,18,13,15,15],
[15,0,18,8,12,15,8,11,12,6,11],
[7,8,0,15,4,14,7,15,9,10,14],
[14,18,11,0,14,11,10,14,15,14,11],
[18,14,22,12,0,19,18,21,18,18,19],
[11,11,12,15,7,0,7,15,12,7,13],
[13,18,19,16,8,19,0,18,13,18,19],
[8,15,11,12,5,11,8,0,13,11,15],
[13,14,17,11,8,14,13,13,0,13,18],
[11,20,16,12,8,19,8,15,13,0,21],
[11,15,12,15,7,13,7,11,8,5,0]])



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
result = np.append(np.array([11, 26, 82, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,12,17,14,14,6,12,20,12,17],
[24,0,17,17,19,13,16,16,19,16,16],
[14,9,0,19,9,14,12,6,9,15,15],
[9,9,7,0,10,10,9,5,7,15,13],
[12,7,17,16,0,19,10,17,13,17,17],
[12,13,12,16,7,0,12,10,7,13,13],
[20,10,14,17,16,14,0,12,14,20,14],
[14,10,20,21,9,16,14,0,14,15,19],
[6,7,17,19,13,19,12,12,0,12,16],
[14,10,11,11,9,13,6,11,14,0,12],
[9,10,11,13,9,13,12,7,10,14,0]])



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
result = np.append(np.array([11, 26, 83, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,17,19,13,14,13,12,12,14,14],
[14,0,17,18,13,15,13,12,14,16,14],
[9,9,0,18,12,18,12,14,11,15,11],
[7,8,8,0,11,8,8,11,10,9,6],
[13,13,14,15,0,14,12,18,12,16,11],
[12,11,8,18,12,0,9,14,10,13,11],
[13,13,14,18,14,17,0,13,17,17,14],
[14,14,12,15,8,12,13,0,13,15,12],
[14,12,15,16,14,16,9,13,0,16,12],
[12,10,11,17,10,13,9,11,10,0,12],
[12,12,15,20,15,15,12,14,14,14,0]])



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
result = np.append(np.array([11, 26, 84, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,17,13,21,20,17,17,21,17,17],
[5,0,13,7,17,9,8,13,10,15,7],
[9,13,0,13,18,22,6,14,14,15,17],
[13,19,13,0,25,18,6,11,15,16,11],
[5,9,8,1,0,9,6,11,5,6,4],
[6,17,4,8,17,0,5,13,9,18,5],
[9,18,20,20,20,21,0,16,15,21,16],
[9,13,12,15,15,13,10,0,14,17,16],
[5,16,12,11,21,17,11,12,0,18,12],
[9,11,11,10,20,8,5,9,8,0,7],
[9,19,9,15,22,21,10,10,14,19,0]])



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
result = np.append(np.array([11, 26, 85, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,11,7,11,10,16,18,14,12,12],
[13,0,11,9,9,14,19,16,13,16,13],
[15,15,0,13,11,14,15,19,16,17,14],
[19,17,13,0,16,13,21,15,15,17,21],
[15,17,15,10,0,13,19,19,14,17,16],
[16,12,12,13,13,0,16,15,14,14,12],
[10,7,11,5,7,10,0,13,5,10,7],
[8,10,7,11,7,11,13,0,13,11,10],
[12,13,10,11,12,12,21,13,0,10,11],
[14,10,9,9,9,12,16,15,16,0,13],
[14,13,12,5,10,14,19,16,15,13,0]])



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
result = np.append(np.array([11, 26, 86, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,15,15,12,17,15,14,13,10,15],
[7,0,14,14,12,15,12,11,13,9,11],
[11,12,0,13,15,15,13,16,16,14,10],
[11,12,13,0,11,12,12,13,12,10,9],
[14,14,11,15,0,14,14,15,14,10,12],
[9,11,11,14,12,0,8,11,12,11,10],
[11,14,13,14,12,18,0,14,13,11,11],
[12,15,10,13,11,15,12,0,16,11,15],
[13,13,10,14,12,14,13,10,0,10,11],
[16,17,12,16,16,15,15,15,16,0,10],
[11,15,16,17,14,16,15,11,15,16,0]])



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
result = np.append(np.array([11, 26, 87, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,15,15,17,17,7,15,13,13,15],
[15,0,11,13,16,19,16,19,20,17,13],
[11,15,0,17,15,18,15,19,18,19,15],
[11,13,9,0,16,13,11,12,14,19,13],
[9,10,11,10,0,11,12,8,20,15,15],
[9,7,8,13,15,0,13,10,17,16,11],
[19,10,11,15,14,13,0,14,12,13,14],
[11,7,7,14,18,16,12,0,16,14,10],
[13,6,8,12,6,9,14,10,0,11,10],
[13,9,7,7,11,10,13,12,15,0,11],
[11,13,11,13,11,15,12,16,16,15,0]])



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
result = np.append(np.array([11, 26, 88, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,3,26,26,12,16,16,16,22,16],
[13,0,9,16,26,12,16,16,13,22,13],
[23,17,0,26,26,12,16,16,16,22,16],
[0,10,0,0,26,3,3,12,13,22,9],
[0,0,0,0,0,0,0,0,0,3,0],
[14,14,14,23,26,0,13,13,13,26,13],
[10,10,10,23,26,13,0,13,23,22,13],
[10,10,10,14,26,13,13,0,23,13,9],
[10,13,10,13,26,13,3,3,0,13,9],
[4,4,4,4,23,0,4,13,13,0,13],
[10,13,10,17,26,13,13,17,17,13,0]])



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
result = np.append(np.array([11, 26, 89, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,22,21,24,25,20,22,20,13,24],
[6,0,19,22,8,21,11,22,9,13,18],
[4,7,0,21,4,10,7,9,11,3,7],
[5,4,5,0,7,7,10,9,8,3,7],
[2,18,22,19,0,21,10,14,13,14,18],
[1,5,16,19,5,0,8,5,12,10,18],
[6,15,19,16,16,18,0,18,9,14,18],
[4,4,17,17,12,21,8,0,8,12,18],
[6,17,15,18,13,14,17,18,0,10,18],
[13,13,23,23,12,16,12,14,16,0,22],
[2,8,19,19,8,8,8,8,8,4,0]])



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
result = np.append(np.array([11, 26, 90, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,7,7,5,10,7,7,12,9,9],
[17,0,11,11,8,13,12,10,13,7,11],
[19,15,0,13,14,14,13,13,20,16,10],
[19,15,13,0,7,16,9,14,15,9,15],
[21,18,12,19,0,18,14,12,18,20,15],
[16,13,12,10,8,0,9,10,11,10,12],
[19,14,13,17,12,17,0,16,13,17,17],
[19,16,13,12,14,16,10,0,17,14,16],
[14,13,6,11,8,15,13,9,0,12,10],
[17,19,10,17,6,16,9,12,14,0,15],
[17,15,16,11,11,14,9,10,16,11,0]])



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
result = np.append(np.array([11, 26, 91, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,15,10,14,14,19,14,10,11,12],
[12,0,13,14,12,13,18,16,10,10,14],
[11,13,0,10,11,11,17,11,7,12,9],
[16,12,16,0,14,15,19,16,15,17,14],
[12,14,15,12,0,14,18,16,14,13,13],
[12,13,15,11,12,0,17,12,13,18,12],
[7,8,9,7,8,9,0,12,8,9,9],
[12,10,15,10,10,14,14,0,10,11,13],
[16,16,19,11,12,13,18,16,0,12,11],
[15,16,14,9,13,8,17,15,14,0,15],
[14,12,17,12,13,14,17,13,15,11,0]])



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
result = np.append(np.array([11, 26, 92, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,17,26,14,11,13,20,19,22,15],
[6,0,9,16,8,6,11,9,16,14,11],
[9,17,0,21,7,11,7,12,16,16,8],
[0,10,5,0,4,4,6,5,13,6,7],
[12,18,19,22,0,11,12,16,15,15,19],
[15,20,15,22,15,0,8,20,17,17,17],
[13,15,19,20,14,18,0,12,13,9,21],
[6,17,14,21,10,6,14,0,19,20,11],
[7,10,10,13,11,9,13,7,0,14,10],
[4,12,10,20,11,9,17,6,12,0,13],
[11,15,18,19,7,9,5,15,16,13,0]])



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
result = np.append(np.array([11, 26, 93, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,12,13,13,10,10,13,10,14,9],
[18,0,17,17,15,14,11,14,15,17,13],
[14,9,0,12,13,12,13,14,16,17,9],
[13,9,14,0,12,12,13,12,12,16,12],
[13,11,13,14,0,15,11,15,13,14,11],
[16,12,14,14,11,0,15,15,15,16,14],
[16,15,13,13,15,11,0,13,17,21,15],
[13,12,12,14,11,11,13,0,13,17,10],
[16,11,10,14,13,11,9,13,0,12,11],
[12,9,9,10,12,10,5,9,14,0,6],
[17,13,17,14,15,12,11,16,15,20,0]])



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
result = np.append(np.array([11, 26, 94, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,11,16,15,10,12,13,14,14,10],
[11,0,12,10,8,10,12,14,13,11,12],
[15,14,0,14,11,12,10,11,13,14,15],
[10,16,12,0,13,10,13,15,16,12,11],
[11,18,15,13,0,13,10,15,13,14,13],
[16,16,14,16,13,0,12,11,16,15,16],
[14,14,16,13,16,14,0,13,16,12,14],
[13,12,15,11,11,15,13,0,15,14,14],
[12,13,13,10,13,10,10,11,0,12,13],
[12,15,12,14,12,11,14,12,14,0,11],
[16,14,11,15,13,10,12,12,13,15,0]])



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
result = np.append(np.array([11, 26, 95, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,16,10,14,12,12,11,9,15,10],
[14,0,18,14,15,13,15,11,14,15,18],
[10,8,0,11,10,9,9,12,7,10,9],
[16,12,15,0,15,15,12,12,12,11,12],
[12,11,16,11,0,14,14,12,11,15,8],
[14,13,17,11,12,0,14,14,16,16,13],
[14,11,17,14,12,12,0,13,12,13,8],
[15,15,14,14,14,12,13,0,13,12,13],
[17,12,19,14,15,10,14,13,0,13,14],
[11,11,16,15,11,10,13,14,13,0,10],
[16,8,17,14,18,13,18,13,12,16,0]])



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
result = np.append(np.array([11, 26, 96, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,10,14,13,12,14,16,13,16,16],
[15,0,15,17,13,13,17,18,15,17,19],
[16,11,0,13,14,11,14,17,14,18,19],
[12,9,13,0,12,12,14,12,12,13,17],
[13,13,12,14,0,14,14,15,12,16,12],
[14,13,15,14,12,0,17,17,15,15,18],
[12,9,12,12,12,9,0,12,14,14,13],
[10,8,9,14,11,9,14,0,13,14,11],
[13,11,12,14,14,11,12,13,0,15,17],
[10,9,8,13,10,11,12,12,11,0,13],
[10,7,7,9,14,8,13,15,9,13,0]])



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
result = np.append(np.array([11, 26, 97, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,8,12,14,15,13,14,12,13,10],
[16,0,14,14,19,14,17,12,12,14,14],
[18,12,0,15,16,18,18,15,14,16,11],
[14,12,11,0,13,12,13,11,9,8,7],
[12,7,10,13,0,13,10,13,10,8,8],
[11,12,8,14,13,0,13,15,11,13,9],
[13,9,8,13,16,13,0,13,11,13,11],
[12,14,11,15,13,11,13,0,11,8,6],
[14,14,12,17,16,15,15,15,0,13,13],
[13,12,10,18,18,13,13,18,13,0,12],
[16,12,15,19,18,17,15,20,13,14,0]])



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
result = np.append(np.array([11, 26, 98, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,18,15,17,10,19,11,18,11,17],
[9,0,7,12,7,6,11,9,11,9,11],
[8,19,0,15,8,10,16,8,13,12,11],
[11,14,11,0,12,8,16,12,16,12,12],
[9,19,18,14,0,12,13,11,20,13,15],
[16,20,16,18,14,0,13,12,15,12,17],
[7,15,10,10,13,13,0,8,13,10,13],
[15,17,18,14,15,14,18,0,18,15,13],
[8,15,13,10,6,11,13,8,0,12,8],
[15,17,14,14,13,14,16,11,14,0,14],
[9,15,15,14,11,9,13,13,18,12,0]])



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
result = np.append(np.array([11, 26, 99, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,10,15,16,15,18,22,18,15,18],
[10,0,4,18,22,18,17,17,13,14,11],
[16,22,0,19,23,19,24,17,13,18,18],
[11,8,7,0,14,8,17,14,16,7,16],
[10,4,3,12,0,12,15,12,8,8,7],
[11,8,7,18,14,0,12,9,13,7,16],
[8,9,2,9,11,14,0,9,4,7,11],
[4,9,9,12,14,17,17,0,11,9,14],
[8,13,13,10,18,13,22,15,0,13,24],
[11,12,8,19,18,19,19,17,13,0,18],
[8,15,8,10,19,10,15,12,2,8,0]])



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
result = np.append(np.array([11, 26, 100, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,15,11,14,12,9,12,8,9,9],
[16,0,14,12,11,7,7,13,13,15,13],
[11,12,0,10,8,11,8,5,13,12,12],
[15,14,16,0,17,13,16,17,17,15,13],
[12,15,18,9,0,12,5,14,11,14,13],
[14,19,15,13,14,0,15,16,12,16,12],
[17,19,18,10,21,11,0,15,16,19,13],
[14,13,21,9,12,10,11,0,15,16,10],
[18,13,13,9,15,14,10,11,0,16,13],
[17,11,14,11,12,10,7,10,10,0,9],
[17,13,14,13,13,14,13,16,13,17,0]])



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
result = np.append(np.array([11, 26, 101, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,5,11,6,15,8,12,9,10,11],
[20,0,11,22,14,17,15,16,16,16,16],
[21,15,0,20,12,15,14,16,18,19,16],
[15,4,6,0,8,9,12,10,8,12,14],
[20,12,14,18,0,17,13,15,13,17,19],
[11,9,11,17,9,0,13,15,15,13,17],
[18,11,12,14,13,13,0,13,15,15,13],
[14,10,10,16,11,11,13,0,10,12,11],
[17,10,8,18,13,11,11,16,0,15,14],
[16,10,7,14,9,13,11,14,11,0,15],
[15,10,10,12,7,9,13,15,12,11,0]])



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
result = np.append(np.array([11, 26, 102, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,9,9,13,13,13,9,9,13,15],
[17,0,13,11,14,17,10,15,12,15,21],
[17,13,0,14,16,17,14,13,18,17,17],
[17,15,12,0,12,18,16,14,13,20,19],
[13,12,10,14,0,16,9,10,11,14,12],
[13,9,9,8,10,0,10,10,10,12,11],
[13,16,12,10,17,16,0,14,13,13,16],
[17,11,13,12,16,16,12,0,17,13,20],
[17,14,8,13,15,16,13,9,0,16,15],
[13,11,9,6,12,14,13,13,10,0,16],
[11,5,9,7,14,15,10,6,11,10,0]])



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
result = np.append(np.array([11, 26, 103, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,17,7,9,19,2,12,7,17,17],
[16,0,19,9,9,19,2,12,9,9,19],
[9,7,0,9,9,19,9,9,7,9,17],
[19,17,17,0,16,19,19,19,17,17,10],
[17,17,17,10,0,12,10,12,17,10,10],
[7,7,7,7,14,0,7,9,14,7,7],
[24,24,17,7,16,19,0,19,24,17,17],
[14,14,17,7,14,17,7,0,14,7,17],
[19,17,19,9,9,12,2,12,0,12,12],
[9,17,17,9,16,19,9,19,14,0,17],
[9,7,9,16,16,19,9,9,14,9,0]])



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
result = np.append(np.array([11, 26, 104, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,12,11,12,15,11,12,14,12,13],
[15,0,13,13,10,17,12,14,14,16,16],
[14,13,0,12,16,18,14,10,13,12,15],
[15,13,14,0,13,19,14,13,14,15,16],
[14,16,10,13,0,17,14,14,17,14,17],
[11,9,8,7,9,0,11,12,9,13,10],
[15,14,12,12,12,15,0,16,14,11,14],
[14,12,16,13,12,14,10,0,13,12,12],
[12,12,13,12,9,17,12,13,0,14,14],
[14,10,14,11,12,13,15,14,12,0,12],
[13,10,11,10,9,16,12,14,12,14,0]])



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
result = np.append(np.array([11, 26, 105, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,6,17,18,11,23,20,12,16,16],
[6,0,9,16,16,15,17,16,11,8,12],
[20,17,0,25,25,12,25,21,21,15,16],
[9,10,1,0,13,8,20,10,8,9,15],
[8,10,1,13,0,10,18,13,11,10,11],
[15,11,14,18,16,0,19,20,15,14,17],
[3,9,1,6,8,7,0,9,10,7,9],
[6,10,5,16,13,6,17,0,11,10,11],
[14,15,5,18,15,11,16,15,0,9,15],
[10,18,11,17,16,12,19,16,17,0,16],
[10,14,10,11,15,9,17,15,11,10,0]])



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
result = np.append(np.array([11, 26, 106, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,14,8,15,17,13,8,13,12,14],
[14,0,20,18,17,22,14,17,17,12,15],
[12,6,0,10,15,11,12,2,16,13,16],
[18,8,16,0,15,18,12,13,17,8,18],
[11,9,11,11,0,16,10,5,14,9,14],
[9,4,15,8,10,0,7,6,13,10,13],
[13,12,14,14,16,19,0,8,17,12,17],
[18,9,24,13,21,20,18,0,18,18,17],
[13,9,10,9,12,13,9,8,0,10,16],
[14,14,13,18,17,16,14,8,16,0,13],
[12,11,10,8,12,13,9,9,10,13,0]])



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
result = np.append(np.array([11, 26, 107, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,15,19,12,13,12,13,18,11,15],
[8,0,7,11,10,10,12,12,13,6,5],
[11,19,0,16,12,12,17,11,17,9,14],
[7,15,10,0,11,12,8,11,12,4,8],
[14,16,14,15,0,13,11,15,19,14,10],
[13,16,14,14,13,0,14,8,20,12,14],
[14,14,9,18,15,12,0,15,16,7,13],
[13,14,15,15,11,18,11,0,15,10,10],
[8,13,9,14,7,6,10,11,0,7,6],
[15,20,17,22,12,14,19,16,19,0,16],
[11,21,12,18,16,12,13,16,20,10,0]])



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
result = np.append(np.array([11, 26, 108, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,17,17,16,17,18,16,17,18],
[13,0,15,13,16,14,16,15,13,12,18],
[13,11,0,14,16,15,16,15,15,17,16],
[9,13,12,0,15,15,17,17,17,14,15],
[9,10,10,11,0,11,13,14,10,10,13],
[10,12,11,11,15,0,13,15,16,15,11],
[9,10,10,9,13,13,0,13,12,10,15],
[8,11,11,9,12,11,13,0,10,8,13],
[10,13,11,9,16,10,14,16,0,12,14],
[9,14,9,12,16,11,16,18,14,0,12],
[8,8,10,11,13,15,11,13,12,14,0]])



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
result = np.append(np.array([11, 26, 109, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,15,7,3,6,12,9,14,7,10],
[18,0,19,17,9,16,18,14,17,9,13],
[11,7,0,9,9,10,12,7,20,6,4],
[19,9,17,0,2,9,8,18,17,6,8],
[23,17,17,24,0,17,17,19,19,11,13],
[20,10,16,17,9,0,20,16,20,12,9],
[14,8,14,18,9,6,0,15,15,10,10],
[17,12,19,8,7,10,11,0,20,12,14],
[12,9,6,9,7,6,11,6,0,8,5],
[19,17,20,20,15,14,16,14,18,0,9],
[16,13,22,18,13,17,16,12,21,17,0]])



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
result = np.append(np.array([11, 26, 110, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,14,13,10,11,8,11,15,12,4],
[19,0,19,15,15,15,9,15,15,13,13],
[12,7,0,10,18,12,9,14,15,17,9],
[13,11,16,0,15,15,11,13,17,21,15],
[16,11,8,11,0,12,11,13,9,11,11],
[15,11,14,11,14,0,9,14,17,17,11],
[18,17,17,15,15,17,0,13,18,13,11],
[15,11,12,13,13,12,13,0,11,15,13],
[11,11,11,9,17,9,8,15,0,12,4],
[14,13,9,5,15,9,13,11,14,0,7],
[22,13,17,11,15,15,15,13,22,19,0]])



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
result = np.append(np.array([11, 26, 111, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,12,10,10,14,13,9,10,12,12],
[12,0,12,15,11,14,12,6,11,8,14],
[14,14,0,12,9,14,16,9,9,11,14],
[16,11,14,0,8,13,15,8,10,7,10],
[16,15,17,18,0,12,18,12,7,16,17],
[12,12,12,13,14,0,15,13,11,9,17],
[13,14,10,11,8,11,0,8,7,9,15],
[17,20,17,18,14,13,18,0,18,13,16],
[16,15,17,16,19,15,19,8,0,14,17],
[14,18,15,19,10,17,17,13,12,0,17],
[14,12,12,16,9,9,11,10,9,9,0]])



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
result = np.append(np.array([11, 26, 112, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,13,18,14,15,12,11,10,17,17],
[12,0,10,19,13,17,11,15,13,18,18],
[13,16,0,16,14,15,15,16,11,19,18],
[8,7,10,0,9,11,9,6,9,11,12],
[12,13,12,17,0,14,12,14,12,16,18],
[11,9,11,15,12,0,13,11,11,16,16],
[14,15,11,17,14,13,0,17,11,17,20],
[15,11,10,20,12,15,9,0,13,13,15],
[16,13,15,17,14,15,15,13,0,18,20],
[9,8,7,15,10,10,9,13,8,0,12],
[9,8,8,14,8,10,6,11,6,14,0]])



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
result = np.append(np.array([11, 26, 113, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,11,13,13,16,16,17,10,11,12],
[8,0,11,8,12,12,15,16,13,8,15],
[15,15,0,13,14,14,18,17,12,14,12],
[13,18,13,0,11,16,17,15,16,13,14],
[13,14,12,15,0,14,13,14,13,13,15],
[10,14,12,10,12,0,11,16,16,13,16],
[10,11,8,9,13,15,0,16,10,13,10],
[9,10,9,11,12,10,10,0,11,8,13],
[16,13,14,10,13,10,16,15,0,12,12],
[15,18,12,13,13,13,13,18,14,0,15],
[14,11,14,12,11,10,16,13,14,11,0]])



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
result = np.append(np.array([11, 26, 114, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,16,13,10,10,15,13,10,15,14],
[9,0,15,13,12,9,9,12,12,9,13],
[10,11,0,11,6,13,10,10,8,10,13],
[13,13,15,0,12,14,14,12,12,17,9],
[16,14,20,14,0,12,12,13,14,17,14],
[16,17,13,12,14,0,17,13,9,16,19],
[11,17,16,12,14,9,0,10,10,12,11],
[13,14,16,14,13,13,16,0,12,15,19],
[16,14,18,14,12,17,16,14,0,18,19],
[11,17,16,9,9,10,14,11,8,0,15],
[12,13,13,17,12,7,15,7,7,11,0]])



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
result = np.append(np.array([11, 26, 115, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,15,11,11,12,11,16,16,25,18],
[10,0,7,7,17,10,5,5,10,10,13],
[11,19,0,19,19,21,19,19,19,26,21],
[15,19,7,0,20,10,5,8,13,15,18],
[15,9,7,6,0,10,4,8,16,15,21],
[14,16,5,16,16,0,16,19,6,16,18],
[15,21,7,21,22,10,0,10,15,15,21],
[10,21,7,18,18,7,16,0,8,10,18],
[10,16,7,13,10,20,11,18,0,10,18],
[1,16,0,11,11,10,11,16,16,0,11],
[8,13,5,8,5,8,5,8,8,15,0]])



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
result = np.append(np.array([11, 26, 116, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,17,11,15,17,7,8,17,14,17],
[10,0,10,11,10,13,16,12,14,12,12],
[9,16,0,13,14,15,11,16,21,12,21],
[15,15,13,0,19,20,17,20,26,22,20],
[11,16,12,7,0,21,13,16,15,14,18],
[9,13,11,6,5,0,16,8,9,9,11],
[19,10,15,9,13,10,0,5,15,8,11],
[18,14,10,6,10,18,21,0,14,17,16],
[9,12,5,0,11,17,11,12,0,12,14],
[12,14,14,4,12,17,18,9,14,0,16],
[9,14,5,6,8,15,15,10,12,10,0]])



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
result = np.append(np.array([11, 26, 117, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,6,6,6,17,9,11,9,9,23],
[15,0,6,6,6,17,15,20,15,15,23],
[20,20,0,23,17,17,20,20,20,9,17],
[20,20,3,0,6,20,9,20,9,9,17],
[20,20,9,20,0,20,9,14,9,9,23],
[9,9,9,6,6,0,15,9,15,15,12],
[17,11,6,17,17,11,0,17,0,9,17],
[15,6,6,6,12,17,9,0,9,9,12],
[17,11,6,17,17,11,26,17,0,9,17],
[17,11,17,17,17,11,17,17,17,0,23],
[3,3,9,9,3,14,9,14,9,3,0]])



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
result = np.append(np.array([11, 26, 118, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,9,10,7,10,12,16,13,9,14],
[7,0,12,9,9,10,9,14,11,13,11],
[17,14,0,8,7,14,13,14,14,18,16],
[16,17,18,0,10,14,11,20,17,16,15],
[19,17,19,16,0,19,20,23,13,17,15],
[16,16,12,12,7,0,12,13,13,11,17],
[14,17,13,15,6,14,0,19,10,18,14],
[10,12,12,6,3,13,7,0,4,13,6],
[13,15,12,9,13,13,16,22,0,13,18],
[17,13,8,10,9,15,8,13,13,0,12],
[12,15,10,11,11,9,12,20,8,14,0]])



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
result = np.append(np.array([11, 26, 119, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,13,10,12,15,14,16,8,8,9],
[15,0,11,13,14,13,9,13,8,13,12],
[13,15,0,17,14,15,15,16,13,16,12],
[16,13,9,0,12,13,14,11,6,11,10],
[14,12,12,14,0,17,11,11,9,12,11],
[11,13,11,13,9,0,10,8,8,9,4],
[12,17,11,12,15,16,0,13,9,11,13],
[10,13,10,15,15,18,13,0,11,16,12],
[18,18,13,20,17,18,17,15,0,15,12],
[18,13,10,15,14,17,15,10,11,0,13],
[17,14,14,16,15,22,13,14,14,13,0]])



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
result = np.append(np.array([11, 26, 120, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,11,12,8,10,8,5,12,9,10],
[16,0,14,12,11,14,15,8,12,11,15],
[15,12,0,12,10,14,15,12,13,14,15],
[14,14,14,0,6,16,11,10,12,12,16],
[18,15,16,20,0,22,14,14,14,13,18],
[16,12,12,10,4,0,10,10,11,13,15],
[18,11,11,15,12,16,0,10,12,13,16],
[21,18,14,16,12,16,16,0,17,13,19],
[14,14,13,14,12,15,14,9,0,14,19],
[17,15,12,14,13,13,13,13,12,0,16],
[16,11,11,10,8,11,10,7,7,10,0]])



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
result = np.append(np.array([11, 26, 121, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,13,13,16,16,13,15,14,16,16],
[12,0,13,15,15,13,8,14,14,13,15],
[13,13,0,12,14,14,11,13,10,15,15],
[13,11,14,0,15,15,12,12,11,10,15],
[10,11,12,11,0,11,12,13,10,15,16],
[10,13,12,11,15,0,9,9,12,11,10],
[13,18,15,14,14,17,0,14,13,13,14],
[11,12,13,14,13,17,12,0,8,15,17],
[12,12,16,15,16,14,13,18,0,21,17],
[10,13,11,16,11,15,13,11,5,0,15],
[10,11,11,11,10,16,12,9,9,11,0]])



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
result = np.append(np.array([11, 26, 122, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,14,13,17,17,10,14,14,10,22],
[9,0,11,13,9,10,10,11,19,6,18],
[12,15,0,8,17,16,8,18,13,4,8],
[13,13,18,0,13,18,5,10,15,14,17],
[9,17,9,13,0,10,5,15,18,5,13],
[9,16,10,8,16,0,0,5,13,1,8],
[16,16,18,21,21,26,0,15,21,9,20],
[12,15,8,16,11,21,11,0,21,8,11],
[12,7,13,11,8,13,5,5,0,8,16],
[16,20,22,12,21,25,17,18,18,0,17],
[4,8,18,9,13,18,6,15,10,9,0]])



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
result = np.append(np.array([11, 26, 123, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,9,12,12,16,10,12,11,16,10],
[16,0,14,13,12,14,13,11,12,15,10],
[17,12,0,14,18,17,16,12,13,20,14],
[14,13,12,0,10,19,16,12,11,14,10],
[14,14,8,16,0,15,17,13,12,20,14],
[10,12,9,7,11,0,10,11,11,15,11],
[16,13,10,10,9,16,0,14,14,14,11],
[14,15,14,14,13,15,12,0,7,14,12],
[15,14,13,15,14,15,12,19,0,15,15],
[10,11,6,12,6,11,12,12,11,0,8],
[16,16,12,16,12,15,15,14,11,18,0]])



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
result = np.append(np.array([11, 26, 124, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,10,14,17,13,15,19,10,12,13],
[7,0,6,10,10,10,8,9,10,19,12],
[16,20,0,20,19,21,17,21,13,23,17],
[12,16,6,0,14,20,12,11,13,13,17],
[9,16,7,12,0,17,15,14,14,14,10],
[13,16,5,6,9,0,5,7,12,13,12],
[11,18,9,14,11,21,0,7,16,16,17],
[7,17,5,15,12,19,19,0,12,17,12],
[16,16,13,13,12,14,10,14,0,18,17],
[14,7,3,13,12,13,10,9,8,0,6],
[13,14,9,9,16,14,9,14,9,20,0]])



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
result = np.append(np.array([11, 26, 125, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,10,9,7,5,12,7,8,7,10],
[15,0,13,16,8,8,12,13,13,10,15],
[16,13,0,13,9,10,13,12,15,13,16],
[17,10,13,0,11,6,16,11,11,9,13],
[19,18,17,15,0,10,15,14,17,9,17],
[21,18,16,20,16,0,16,17,16,10,18],
[14,14,13,10,11,10,0,9,13,9,15],
[19,13,14,15,12,9,17,0,15,8,17],
[18,13,11,15,9,10,13,11,0,12,13],
[19,16,13,17,17,16,17,18,14,0,16],
[16,11,10,13,9,8,11,9,13,10,0]])



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
result = np.append(np.array([11, 26, 126, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,15,14,3,12,17,10,10,16,7],
[16,0,16,15,6,13,16,5,12,10,13],
[11,10,0,13,6,14,11,3,15,7,7],
[12,11,13,0,6,10,12,8,13,10,13],
[23,20,20,20,0,17,14,13,21,16,17],
[14,13,12,16,9,0,15,7,20,12,11],
[9,10,15,14,12,11,0,6,9,13,10],
[16,21,23,18,13,19,20,0,20,20,20],
[16,14,11,13,5,6,17,6,0,9,16],
[10,16,19,16,10,14,13,6,17,0,17],
[19,13,19,13,9,15,16,6,10,9,0]])



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
result = np.append(np.array([11, 26, 127, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,13,12,9,8,14,14,11,11,9],
[16,0,13,13,7,9,11,13,10,14,12],
[13,13,0,14,11,8,13,13,13,9,10],
[14,13,12,0,8,9,9,10,9,12,12],
[17,19,15,18,0,11,13,19,16,14,14],
[18,17,18,17,15,0,16,13,14,19,14],
[12,15,13,17,13,10,0,13,11,13,14],
[12,13,13,16,7,13,13,0,12,14,11],
[15,16,13,17,10,12,15,14,0,14,9],
[15,12,17,14,12,7,13,12,12,0,13],
[17,14,16,14,12,12,12,15,17,13,0]])



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
result = np.append(np.array([11, 26, 128, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,11,16,12,14,11,10,16,9,13],
[16,0,12,13,12,15,10,16,13,15,14],
[15,14,0,12,11,13,8,9,14,10,10],
[10,13,14,0,12,16,14,13,16,13,14],
[14,14,15,14,0,13,10,14,14,12,13],
[12,11,13,10,13,0,11,12,13,9,10],
[15,16,18,12,16,15,0,12,14,14,14],
[16,10,17,13,12,14,14,0,13,11,14],
[10,13,12,10,12,13,12,13,0,13,14],
[17,11,16,13,14,17,12,15,13,0,17],
[13,12,16,12,13,16,12,12,12,9,0]])



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
result = np.append(np.array([11, 26, 129, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,9,13,7,8,11,10,12,15,7],
[15,0,13,15,13,12,18,16,14,15,8],
[17,13,0,11,10,17,12,17,14,15,14],
[13,11,15,0,11,13,13,12,15,15,7],
[19,13,16,15,0,15,10,13,22,19,11],
[18,14,9,13,11,0,11,15,13,10,11],
[15,8,14,13,16,15,0,16,17,18,10],
[16,10,9,14,13,11,10,0,14,14,9],
[14,12,12,11,4,13,9,12,0,13,9],
[11,11,11,11,7,16,8,12,13,0,10],
[19,18,12,19,15,15,16,17,17,16,0]])



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
result = np.append(np.array([11, 26, 130, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,13,13,15,17,16,18,12,14],
[15,0,13,16,18,17,16,15,19,15,15],
[15,13,0,13,15,16,12,15,18,12,16],
[13,10,13,0,12,14,11,15,18,13,8],
[13,8,11,14,0,14,9,14,15,13,11],
[11,9,10,12,12,0,13,15,14,8,10],
[9,10,14,15,17,13,0,15,14,12,13],
[10,11,11,11,12,11,11,0,11,11,9],
[8,7,8,8,11,12,12,15,0,9,11],
[14,11,14,13,13,18,14,15,17,0,12],
[12,11,10,18,15,16,13,17,15,14,0]])



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
result = np.append(np.array([11, 26, 131, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,12,16,13,12,15,14,11,14,17],
[14,0,12,14,13,15,17,16,15,13,17],
[14,14,0,13,10,13,11,13,11,12,16],
[10,12,13,0,9,14,11,15,13,13,17],
[13,13,16,17,0,13,16,18,16,15,18],
[14,11,13,12,13,0,12,15,11,12,16],
[11,9,15,15,10,14,0,11,10,12,15],
[12,10,13,11,8,11,15,0,10,12,17],
[15,11,15,13,10,15,16,16,0,15,21],
[12,13,14,13,11,14,14,14,11,0,17],
[9,9,10,9,8,10,11,9,5,9,0]])



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
result = np.append(np.array([11, 26, 132, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,14,12,14,8,15,12,10,14,10],
[10,0,8,13,15,8,15,14,9,13,9],
[12,18,0,14,17,14,15,15,14,13,13],
[14,13,12,0,15,9,12,14,12,12,11],
[12,11,9,11,0,5,10,12,8,11,10],
[18,18,12,17,21,0,14,16,12,16,14],
[11,11,11,14,16,12,0,14,12,16,12],
[14,12,11,12,14,10,12,0,10,11,10],
[16,17,12,14,18,14,14,16,0,14,14],
[12,13,13,14,15,10,10,15,12,0,13],
[16,17,13,15,16,12,14,16,12,13,0]])



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
result = np.append(np.array([11, 26, 133, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,10,14,11,14,12,15,12,13,15],
[15,0,15,17,15,15,12,17,16,14,14],
[16,11,0,12,13,16,11,15,17,12,11],
[12,9,14,0,12,12,17,14,13,11,14],
[15,11,13,14,0,12,14,12,14,16,13],
[12,11,10,14,14,0,12,16,16,14,12],
[14,14,15,9,12,14,0,16,16,12,14],
[11,9,11,12,14,10,10,0,12,12,15],
[14,10,9,13,12,10,10,14,0,10,10],
[13,12,14,15,10,12,14,14,16,0,11],
[11,12,15,12,13,14,12,11,16,15,0]])



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
result = np.append(np.array([11, 26, 134, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,14,13,21,17,15,12,12,21,20],
[8,0,9,5,11,8,10,11,9,14,10],
[12,17,0,12,16,16,12,16,12,16,17],
[13,21,14,0,21,19,9,12,14,23,14],
[5,15,10,5,0,9,2,8,5,10,11],
[9,18,10,7,17,0,5,7,2,17,11],
[11,16,14,17,24,21,0,14,11,16,19],
[14,15,10,14,18,19,12,0,11,19,17],
[14,17,14,12,21,24,15,15,0,18,16],
[5,12,10,3,16,9,10,7,8,0,10],
[6,16,9,12,15,15,7,9,10,16,0]])



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
result = np.append(np.array([11, 26, 135, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,11,19,12,15,14,16,14,13,11],
[5,0,10,16,12,7,11,11,9,9,11],
[15,16,0,15,11,12,10,13,10,11,8],
[7,10,11,0,11,7,8,12,12,11,2],
[14,14,15,15,0,15,16,19,14,16,10],
[11,19,14,19,11,0,10,13,14,10,11],
[12,15,16,18,10,16,0,15,7,18,10],
[10,15,13,14,7,13,11,0,9,12,10],
[12,17,16,14,12,12,19,17,0,17,13],
[13,17,15,15,10,16,8,14,9,0,11],
[15,15,18,24,16,15,16,16,13,15,0]])



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
result = np.append(np.array([11, 26, 136, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,13,18,17,12,14,13,15,10,16],
[12,0,14,16,13,11,13,16,14,13,17],
[13,12,0,17,15,11,11,16,13,13,19],
[8,10,9,0,13,13,9,12,10,10,11],
[9,13,11,13,0,8,13,12,13,11,12],
[14,15,15,13,18,0,12,14,15,13,14],
[12,13,15,17,13,14,0,14,13,12,15],
[13,10,10,14,14,12,12,0,13,11,14],
[11,12,13,16,13,11,13,13,0,10,15],
[16,13,13,16,15,13,14,15,16,0,16],
[10,9,7,15,14,12,11,12,11,10,0]])



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
result = np.append(np.array([11, 26, 137, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,10,17,12,15,18,14,14,11,15],
[8,0,8,9,13,14,14,11,11,10,12],
[16,18,0,17,10,13,18,20,14,15,15],
[9,17,9,0,10,14,18,13,10,11,16],
[14,13,16,16,0,17,17,14,11,14,13],
[11,12,13,12,9,0,16,11,12,9,7],
[8,12,8,8,9,10,0,8,12,10,11],
[12,15,6,13,12,15,18,0,12,13,12],
[12,15,12,16,15,14,14,14,0,16,12],
[15,16,11,15,12,17,16,13,10,0,12],
[11,14,11,10,13,19,15,14,14,14,0]])



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
result = np.append(np.array([11, 26, 138, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,18,7,7,7,16,12,12,12,12],
[8,0,4,0,0,8,16,4,8,4,9],
[8,22,0,11,11,4,16,16,11,15,9],
[19,26,15,0,16,8,16,15,26,20,9],
[19,26,15,10,0,14,26,15,26,19,19],
[19,18,22,18,12,0,22,22,22,16,9],
[10,10,10,10,0,4,0,10,10,4,0],
[14,22,10,11,11,4,16,0,17,15,9],
[14,18,15,0,0,4,16,9,0,9,9],
[14,22,11,6,7,10,22,11,17,0,15],
[14,17,17,17,7,17,26,17,17,11,0]])



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
result = np.append(np.array([11, 26, 139, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,13,13,0,13,13,0,13,13],
[13,0,26,26,26,13,26,26,13,26,13],
[13,0,0,26,26,0,13,26,13,13,13],
[13,0,0,0,13,0,13,13,13,13,13],
[13,0,0,13,0,0,13,26,13,13,13],
[26,13,26,26,26,0,13,26,13,13,13],
[13,0,13,13,13,13,0,13,13,0,0],
[13,0,0,13,0,0,13,0,13,13,13],
[26,13,13,13,13,13,13,13,0,13,13],
[13,0,13,13,13,13,26,13,13,0,13],
[13,13,13,13,13,13,26,13,13,13,0]])



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
result = np.append(np.array([11, 26, 140, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,15,6,7,14,12,12,15,13,14],
[20,0,15,16,10,19,16,15,19,18,20],
[11,11,0,11,5,15,5,11,15,14,14],
[20,10,15,0,14,14,15,14,14,8,10],
[19,16,21,12,0,15,17,11,20,18,21],
[12,7,11,12,11,0,12,10,17,6,12],
[14,10,21,11,9,14,0,16,20,9,10],
[14,11,15,12,15,16,10,0,20,9,11],
[11,7,11,12,6,9,6,6,0,9,14],
[13,8,12,18,8,20,17,17,17,0,20],
[12,6,12,16,5,14,16,15,12,6,0]])



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
result = np.append(np.array([11, 26, 141, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,10,12,14,13,10,10,11,15,10],
[15,0,9,12,14,14,14,12,13,13,12],
[16,17,0,14,16,14,16,16,16,17,13],
[14,14,12,0,13,13,15,15,16,15,11],
[12,12,10,13,0,10,11,12,11,11,12],
[13,12,12,13,16,0,11,9,12,14,11],
[16,12,10,11,15,15,0,13,16,16,15],
[16,14,10,11,14,17,13,0,14,13,14],
[15,13,10,10,15,14,10,12,0,11,9],
[11,13,9,11,15,12,10,13,15,0,10],
[16,14,13,15,14,15,11,12,17,16,0]])



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
result = np.append(np.array([11, 26, 142, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,17,19,14,15,18,17,8,19,16],
[18,0,20,20,15,13,22,16,16,22,19],
[9,6,0,13,11,13,14,9,11,14,9],
[7,6,13,0,10,9,14,8,5,8,2],
[12,11,15,16,0,12,18,5,7,15,13],
[11,13,13,17,14,0,19,7,9,13,14],
[8,4,12,12,8,7,0,5,7,7,6],
[9,10,17,18,21,19,21,0,10,20,18],
[18,10,15,21,19,17,19,16,0,16,11],
[7,4,12,18,11,13,19,6,10,0,11],
[10,7,17,24,13,12,20,8,15,15,0]])



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
result = np.append(np.array([11, 26, 143, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,17,12,12,19,17,13,13,14,12],
[14,0,12,14,9,13,14,13,13,11,13],
[9,14,0,13,12,15,14,13,11,10,12],
[14,12,13,0,13,17,13,14,13,13,12],
[14,17,14,13,0,14,17,15,15,15,13],
[7,13,11,9,12,0,15,11,12,10,7],
[9,12,12,13,9,11,0,10,10,11,5],
[13,13,13,12,11,15,16,0,13,10,12],
[13,13,15,13,11,14,16,13,0,10,11],
[12,15,16,13,11,16,15,16,16,0,11],
[14,13,14,14,13,19,21,14,15,15,0]])



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
result = np.append(np.array([11, 26, 144, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,9,16,12,15,15,14,12,8,14],
[19,0,17,19,15,18,20,25,13,10,17],
[17,9,0,11,14,16,9,18,10,8,9],
[10,7,15,0,11,10,7,10,4,2,6],
[14,11,12,15,0,15,14,14,14,13,13],
[11,8,10,16,11,0,8,11,3,8,3],
[11,6,17,19,12,18,0,13,5,9,9],
[12,1,8,16,12,15,13,0,11,8,13],
[14,13,16,22,12,23,21,15,0,16,21],
[18,16,18,24,13,18,17,18,10,0,13],
[12,9,17,20,13,23,17,13,5,13,0]])



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
result = np.append(np.array([11, 26, 145, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,18,12,12,15,14,12,19,15,14],
[7,0,15,10,12,15,12,14,15,14,14],
[8,11,0,11,9,16,11,12,15,9,12],
[14,16,15,0,9,16,16,18,18,15,12],
[14,14,17,17,0,17,14,16,16,14,10],
[11,11,10,10,9,0,16,11,11,7,5],
[12,14,15,10,12,10,0,14,10,8,12],
[14,12,14,8,10,15,12,0,12,12,15],
[7,11,11,8,10,15,16,14,0,12,12],
[11,12,17,11,12,19,18,14,14,0,15],
[12,12,14,14,16,21,14,11,14,11,0]])



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
result = np.append(np.array([11, 26, 146, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,12,19,20,15,20,19,20,14,17],
[12,0,9,17,20,18,18,18,19,11,15],
[14,17,0,20,21,21,19,21,13,13,23],
[7,9,6,0,14,15,11,10,9,6,8],
[6,6,5,12,0,10,10,6,7,5,7],
[11,8,5,11,16,0,16,14,12,4,7],
[6,8,7,15,16,10,0,11,15,6,9],
[7,8,5,16,20,12,15,0,7,6,9],
[6,7,13,17,19,14,11,19,0,12,18],
[12,15,13,20,21,22,20,20,14,0,18],
[9,11,3,18,19,19,17,17,8,8,0]])



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
result = np.append(np.array([11, 26, 147, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,10,16,18,14,18,7,12,9,8],
[10,0,8,6,10,6,11,6,6,8,5],
[16,18,0,12,23,12,17,14,13,11,12],
[10,20,14,0,22,18,19,9,11,13,8],
[8,16,3,4,0,6,13,3,3,8,3],
[12,20,14,8,20,0,16,10,7,9,10],
[8,15,9,7,13,10,0,6,8,7,1],
[19,20,12,17,23,16,20,0,14,18,13],
[14,20,13,15,23,19,18,12,0,15,8],
[17,18,15,13,18,17,19,8,11,0,7],
[18,21,14,18,23,16,25,13,18,19,0]])



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
result = np.append(np.array([11, 26, 148, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,16,10,12,13,13,13,13,8,12],
[14,0,15,13,14,17,19,16,13,11,15],
[10,11,0,10,11,15,20,17,13,12,15],
[16,13,16,0,13,14,17,17,14,10,16],
[14,12,15,13,0,18,15,16,14,9,16],
[13,9,11,12,8,0,16,14,12,8,13],
[13,7,6,9,11,10,0,12,11,7,11],
[13,10,9,9,10,12,14,0,15,9,13],
[13,13,13,12,12,14,15,11,0,13,11],
[18,15,14,16,17,18,19,17,13,0,16],
[14,11,11,10,10,13,15,13,15,10,0]])



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
result = np.append(np.array([11, 26, 149, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,9,11,15,9,11,16,10,13,5],
[10,0,10,8,11,7,11,14,9,12,13],
[17,16,0,8,18,15,16,17,19,16,15],
[15,18,18,0,16,11,16,16,16,19,14],
[11,15,8,10,0,8,16,14,12,11,11],
[17,19,11,15,18,0,17,19,17,17,18],
[15,15,10,10,10,9,0,15,10,16,9],
[10,12,9,10,12,7,11,0,6,10,7],
[16,17,7,10,14,9,16,20,0,14,12],
[13,14,10,7,15,9,10,16,12,0,8],
[21,13,11,12,15,8,17,19,14,18,0]])



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
result = np.append(np.array([11, 26, 150, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,13,16,14,12,12,16,16,15,14],
[11,0,12,14,15,13,13,16,16,15,17],
[13,14,0,12,11,9,14,16,13,16,13],
[10,12,14,0,12,10,13,12,15,13,14],
[12,11,15,14,0,13,10,13,13,13,16],
[14,13,17,16,13,0,14,13,18,13,18],
[14,13,12,13,16,12,0,14,14,15,16],
[10,10,10,14,13,13,12,0,19,14,15],
[10,10,13,11,13,8,12,7,0,12,12],
[11,11,10,13,13,13,11,12,14,0,13],
[12,9,13,12,10,8,10,11,14,13,0]])



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
result = np.append(np.array([11, 26, 151, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,16,16,15,15,14,19,12,18,14],
[10,0,12,13,15,13,12,10,10,14,10],
[10,14,0,15,14,14,11,18,10,14,12],
[10,13,11,0,13,13,8,16,9,14,9],
[11,11,12,13,0,12,11,18,10,14,11],
[11,13,12,13,14,0,10,13,10,9,14],
[12,14,15,18,15,16,0,15,13,18,16],
[7,16,8,10,8,13,11,0,10,15,14],
[14,16,16,17,16,16,13,16,0,20,20],
[8,12,12,12,12,17,8,11,6,0,14],
[12,16,14,17,15,12,10,12,6,12,0]])



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
result = np.append(np.array([11, 26, 152, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,10,16,13,13,12,14,9,8,12],
[14,0,7,13,15,12,13,11,12,10,12],
[16,19,0,17,15,17,17,17,14,13,17],
[10,13,9,0,14,11,9,14,12,9,11],
[13,11,11,12,0,13,10,16,9,10,12],
[13,14,9,15,13,0,15,16,16,12,16],
[14,13,9,17,16,11,0,15,15,12,17],
[12,15,9,12,10,10,11,0,10,9,12],
[17,14,12,14,17,10,11,16,0,11,13],
[18,16,13,17,16,14,14,17,15,0,17],
[14,14,9,15,14,10,9,14,13,9,0]])



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
result = np.append(np.array([11, 26, 153, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,1,4,14,12,13,12,12,17,14],
[17,0,14,12,23,20,17,25,21,26,14],
[25,12,0,20,26,11,25,25,21,17,17],
[22,14,6,0,23,8,14,14,18,14,14],
[12,3,0,3,0,3,12,3,12,3,0],
[14,6,15,18,23,0,17,26,13,18,14],
[13,9,1,12,14,9,0,9,12,14,14],
[14,1,1,12,23,0,17,0,13,9,14],
[14,5,5,8,14,13,14,13,0,6,14],
[9,0,9,12,23,8,12,17,20,0,8],
[12,12,9,12,26,12,12,12,12,18,0]])



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
result = np.append(np.array([11, 26, 154, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,15,15,13,15,15,15,15,24,15],
[2,0,13,2,2,6,2,13,2,13,2],
[11,13,0,15,15,15,13,6,11,13,15],
[11,24,11,0,9,15,13,11,11,24,15],
[13,24,11,17,0,15,15,17,11,24,15],
[11,20,11,11,11,0,9,13,13,20,2],
[11,24,13,13,11,17,0,13,13,20,17],
[11,13,20,15,9,13,13,0,9,24,13],
[11,24,15,15,15,13,13,17,0,24,6],
[2,13,13,2,2,6,6,2,2,0,6],
[11,24,11,11,11,24,9,13,20,20,0]])



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
result = np.append(np.array([11, 26, 155, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,8,11,8,7,5,12,8,8,8],
[12,0,12,13,12,11,11,11,8,11,12],
[18,14,0,16,15,10,8,10,11,11,14],
[15,13,10,0,8,9,8,9,10,10,8],
[18,14,11,18,0,12,10,15,11,10,13],
[19,15,16,17,14,0,15,13,12,13,12],
[21,15,18,18,16,11,0,16,13,14,13],
[14,15,16,17,11,13,10,0,10,12,10],
[18,18,15,16,15,14,13,16,0,11,15],
[18,15,15,16,16,13,12,14,15,0,17],
[18,14,12,18,13,14,13,16,11,9,0]])



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
result = np.append(np.array([11, 26, 156, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,14,12,13,13,8,9,12,10],
[13,0,13,11,16,9,15,11,10,10,15],
[13,13,0,13,14,12,11,10,8,12,14],
[12,15,13,0,11,12,10,8,11,13,12],
[14,10,12,15,0,9,12,4,5,13,14],
[13,17,14,14,17,0,13,14,13,13,12],
[13,11,15,16,14,13,0,13,11,10,11],
[18,15,16,18,22,12,13,0,12,16,17],
[17,16,18,15,21,13,15,14,0,15,14],
[14,16,14,13,13,13,16,10,11,0,13],
[16,11,12,14,12,14,15,9,12,13,0]])



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
result = np.append(np.array([11, 26, 157, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,14,11,9,7,17,6,7,4,13],
[9,0,5,12,5,11,13,10,9,8,9],
[12,21,0,15,6,11,15,12,9,7,13],
[15,14,11,0,6,7,13,14,7,5,13],
[17,21,20,20,0,17,21,16,18,9,21],
[19,15,15,19,9,0,16,14,15,9,12],
[9,13,11,13,5,10,0,3,5,7,15],
[20,16,14,12,10,12,23,0,12,11,17],
[19,17,17,19,8,11,21,14,0,13,15],
[22,18,19,21,17,17,19,15,13,0,20],
[13,17,13,13,5,14,11,9,11,6,0]])



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
result = np.append(np.array([11, 26, 158, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,14,13,12,9,20,26,15,11,16],
[12,0,8,4,9,9,11,15,20,6,13],
[12,18,0,7,10,9,14,15,12,9,11],
[13,22,19,0,19,14,13,17,22,16,16],
[14,17,16,7,0,9,14,18,15,11,10],
[17,17,17,12,17,0,20,23,25,9,16],
[6,15,12,13,12,6,0,17,15,12,17],
[0,11,11,9,8,3,9,0,11,6,13],
[11,6,14,4,11,1,11,15,0,9,16],
[15,20,17,10,15,17,14,20,17,0,17],
[10,13,15,10,16,10,9,13,10,9,0]])



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
result = np.append(np.array([11, 26, 159, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,12,12,14,21,19,22,12,13,10],
[17,0,10,8,21,17,15,22,14,16,13],
[14,16,0,9,18,22,15,18,18,16,14],
[14,18,17,0,22,18,22,26,14,16,10],
[12,5,8,4,0,16,9,12,8,5,1],
[5,9,4,8,10,0,9,13,9,5,5],
[7,11,11,4,17,17,0,11,8,12,3],
[4,4,8,0,14,13,15,0,8,9,6],
[14,12,8,12,18,17,18,18,0,16,10],
[13,10,10,10,21,21,14,17,10,0,6],
[16,13,12,16,25,21,23,20,16,20,0]])



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
result = np.append(np.array([11, 26, 160, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,19,13,11,13,14,16,19,19,18],
[11,0,14,8,8,10,12,12,12,17,13],
[7,12,0,9,10,9,10,13,14,15,12],
[13,18,17,0,13,12,13,11,18,22,14],
[15,18,16,13,0,12,15,16,15,16,17],
[13,16,17,14,14,0,13,16,18,19,13],
[12,14,16,13,11,13,0,13,17,19,18],
[10,14,13,15,10,10,13,0,13,19,11],
[7,14,12,8,11,8,9,13,0,13,14],
[7,9,11,4,10,7,7,7,13,0,10],
[8,13,14,12,9,13,8,15,12,16,0]])



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
result = np.append(np.array([11, 26, 161, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,2,4,8,5,9,6,3,5,16],
[20,0,12,8,11,6,15,11,11,11,21],
[24,14,0,8,21,15,18,18,12,16,26],
[22,18,18,0,18,19,13,14,14,9,25],
[18,15,5,8,0,14,8,5,6,9,16],
[21,20,11,7,12,0,11,7,12,15,21],
[17,11,8,13,18,15,0,9,12,11,22],
[20,15,8,12,21,19,17,0,12,16,21],
[23,15,14,12,20,14,14,14,0,14,21],
[21,15,10,17,17,11,15,10,12,0,17],
[10,5,0,1,10,5,4,5,5,9,0]])



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
result = np.append(np.array([11, 26, 162, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,16,19,14,14,17,15,14,14,14],
[14,0,16,14,15,16,18,13,15,14,12],
[10,10,0,16,14,12,12,7,14,15,9],
[7,12,10,0,15,7,10,8,10,12,9],
[12,11,12,11,0,11,11,8,15,13,10],
[12,10,14,19,15,0,11,16,15,15,12],
[9,8,14,16,15,15,0,13,14,13,10],
[11,13,19,18,18,10,13,0,16,16,14],
[12,11,12,16,11,11,12,10,0,14,9],
[12,12,11,14,13,11,13,10,12,0,9],
[12,14,17,17,16,14,16,12,17,17,0]])



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
result = np.append(np.array([11, 26, 163, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,9,12,18,12,12,14,11,19,16],
[14,0,12,11,16,15,13,8,12,19,15],
[17,14,0,15,15,17,13,12,13,18,13],
[14,15,11,0,17,19,11,14,10,15,15],
[8,10,11,9,0,10,4,4,6,11,14],
[14,11,9,7,16,0,13,8,10,15,14],
[14,13,13,15,22,13,0,14,14,15,15],
[12,18,14,12,22,18,12,0,14,19,19],
[15,14,13,16,20,16,12,12,0,13,14],
[7,7,8,11,15,11,11,7,13,0,10],
[10,11,13,11,12,12,11,7,12,16,0]])



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
result = np.append(np.array([11, 26, 164, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,12,9,9,12,9,11,13,16,17],
[13,0,18,7,12,13,15,12,16,16,18],
[14,8,0,3,12,13,11,11,7,9,18],
[17,19,23,0,15,14,19,20,15,13,21],
[17,14,14,11,0,16,17,20,12,16,21],
[14,13,13,12,10,0,16,15,11,13,17],
[17,11,15,7,9,10,0,13,13,13,17],
[15,14,15,6,6,11,13,0,13,13,16],
[13,10,19,11,14,15,13,13,0,9,21],
[10,10,17,13,10,13,13,13,17,0,17],
[9,8,8,5,5,9,9,10,5,9,0]])



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
result = np.append(np.array([11, 26, 165, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,10,17,16,16,13,16,15,17,13],
[8,0,11,17,14,18,16,14,14,17,14],
[16,15,0,15,18,13,13,14,14,18,15],
[9,9,11,0,15,16,16,12,14,13,13],
[10,12,8,11,0,16,15,17,13,15,11],
[10,8,13,10,10,0,6,10,12,16,13],
[13,10,13,10,11,20,0,13,11,17,13],
[10,12,12,14,9,16,13,0,12,14,8],
[11,12,12,12,13,14,15,14,0,9,12],
[9,9,8,13,11,10,9,12,17,0,12],
[13,12,11,13,15,13,13,18,14,14,0]])



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
result = np.append(np.array([11, 26, 166, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,5,11,12,9,9,8,15,12,16],
[19,0,15,16,12,11,13,16,14,13,13],
[21,11,0,15,16,14,8,14,17,14,15],
[15,10,11,0,13,7,9,9,8,11,12],
[14,14,10,13,0,7,5,15,11,6,13],
[17,15,12,19,19,0,9,16,14,12,16],
[17,13,18,17,21,17,0,17,16,16,17],
[18,10,12,17,11,10,9,0,13,15,16],
[11,12,9,18,15,12,10,13,0,17,17],
[14,13,12,15,20,14,10,11,9,0,16],
[10,13,11,14,13,10,9,10,9,10,0]])



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
result = np.append(np.array([11, 26, 167, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,12,13,14,16,10,12,15,16,8],
[11,0,8,16,12,11,17,10,12,14,12],
[14,18,0,16,10,14,15,11,19,15,13],
[13,10,10,0,8,12,10,7,13,14,9],
[12,14,16,18,0,15,14,14,18,16,8],
[10,15,12,14,11,0,12,9,14,16,10],
[16,9,11,16,12,14,0,10,15,15,9],
[14,16,15,19,12,17,16,0,19,21,13],
[11,14,7,13,8,12,11,7,0,14,14],
[10,12,11,12,10,10,11,5,12,0,10],
[18,14,13,17,18,16,17,13,12,16,0]])



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
result = np.append(np.array([11, 26, 168, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,10,5,13,12,11,9,13,11,13],
[15,0,13,14,21,13,14,12,12,17,17],
[16,13,0,7,18,14,11,10,13,14,14],
[21,12,19,0,20,17,15,17,17,20,22],
[13,5,8,6,0,12,9,7,9,11,15],
[14,13,12,9,14,0,7,8,14,10,19],
[15,12,15,11,17,19,0,11,17,13,18],
[17,14,16,9,19,18,15,0,18,13,17],
[13,14,13,9,17,12,9,8,0,10,16],
[15,9,12,6,15,16,13,13,16,0,20],
[13,9,12,4,11,7,8,9,10,6,0]])



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
result = np.append(np.array([11, 26, 169, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,9,10,9,10,14,12,9,4,8],
[11,0,9,5,7,11,11,11,9,5,3],
[17,17,0,15,12,13,14,16,8,5,9],
[16,21,11,0,12,15,19,21,14,11,19],
[17,19,14,14,0,19,18,19,17,11,17],
[16,15,13,11,7,0,12,15,11,8,9],
[12,15,12,7,8,14,0,14,8,11,10],
[14,15,10,5,7,11,12,0,10,5,6],
[17,17,18,12,9,15,18,16,0,7,12],
[22,21,21,15,15,18,15,21,19,0,13],
[18,23,17,7,9,17,16,20,14,13,0]])



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
result = np.append(np.array([11, 26, 170, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,14,7,9,10,10,12,14,9],
[15,0,16,16,11,17,11,19,15,21,12],
[15,10,0,12,8,14,13,12,13,16,9],
[12,10,14,0,13,14,12,12,15,17,14],
[19,15,18,13,0,17,17,17,19,18,14],
[17,9,12,12,9,0,12,13,9,17,9],
[16,15,13,14,9,14,0,17,15,19,11],
[16,7,14,14,9,13,9,0,13,15,11],
[14,11,13,11,7,17,11,13,0,14,13],
[12,5,10,9,8,9,7,11,12,0,9],
[17,14,17,12,12,17,15,15,13,17,0]])



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
result = np.append(np.array([11, 26, 171, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,6,6,5,6,9,8,24,15,4],
[2,0,7,3,6,2,2,2,10,2,5],
[20,19,0,11,14,10,13,17,20,19,12],
[20,23,15,0,9,20,13,20,25,16,11],
[21,20,12,17,0,21,14,21,21,12,13],
[20,24,16,6,5,0,9,20,25,15,11],
[17,24,13,13,12,17,0,16,23,15,11],
[18,24,9,6,5,6,10,0,25,16,4],
[2,16,6,1,5,1,3,1,0,15,4],
[11,24,7,10,14,11,11,10,11,0,14],
[22,21,14,15,13,15,15,22,22,12,0]])



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
result = np.append(np.array([11, 26, 172, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,15,17,10,10,12,12,10,12,12],
[12,0,14,11,10,11,9,13,6,12,13],
[11,12,0,12,10,11,8,14,10,11,16],
[9,15,14,0,8,8,8,11,7,13,11],
[16,16,16,18,0,12,11,14,14,14,19],
[16,15,15,18,14,0,10,11,10,16,17],
[14,17,18,18,15,16,0,15,12,15,18],
[14,13,12,15,12,15,11,0,11,16,17],
[16,20,16,19,12,16,14,15,0,17,16],
[14,14,15,13,12,10,11,10,9,0,12],
[14,13,10,15,7,9,8,9,10,14,0]])



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
result = np.append(np.array([11, 26, 173, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,10,21,13,10,12,20,11,10,10],
[12,0,12,18,12,7,17,14,14,11,5],
[16,14,0,16,18,14,12,19,11,16,13],
[5,8,10,0,10,10,12,13,12,4,9],
[13,14,8,16,0,7,20,18,10,14,13],
[16,19,12,16,19,0,19,17,15,16,16],
[14,9,14,14,6,7,0,19,4,14,11],
[6,12,7,13,8,9,7,0,6,4,8],
[15,12,15,14,16,11,22,20,0,14,15],
[16,15,10,22,12,10,12,22,12,0,17],
[16,21,13,17,13,10,15,18,11,9,0]])



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
result = np.append(np.array([11, 26, 174, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,7,19,11,13,14,11,15,13,10],
[12,0,12,15,16,13,19,19,15,14,15],
[19,14,0,18,18,12,18,11,18,15,16],
[7,11,8,0,12,12,16,10,15,12,8],
[15,10,8,14,0,8,9,11,20,7,6],
[13,13,14,14,18,0,18,18,14,14,14],
[12,7,8,10,17,8,0,10,15,10,7],
[15,7,15,16,15,8,16,0,14,9,13],
[11,11,8,11,6,12,11,12,0,9,8],
[13,12,11,14,19,12,16,17,17,0,9],
[16,11,10,18,20,12,19,13,18,17,0]])



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
result = np.append(np.array([11, 26, 175, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,18,13,10,10,7,10,11,10,8],
[17,0,17,14,14,16,13,8,13,12,11],
[8,9,0,13,13,12,10,12,12,11,11],
[13,12,13,0,9,10,8,10,8,9,11],
[16,12,13,17,0,17,14,8,11,9,13],
[16,10,14,16,9,0,11,11,11,12,11],
[19,13,16,18,12,15,0,12,12,14,15],
[16,18,14,16,18,15,14,0,11,13,13],
[15,13,14,18,15,15,14,15,0,11,16],
[16,14,15,17,17,14,12,13,15,0,14],
[18,15,15,15,13,15,11,13,10,12,0]])



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
result = np.append(np.array([11, 26, 176, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,13,14,12,12,12,15,12,8,12],
[15,0,15,14,13,13,11,13,15,15,16],
[13,11,0,13,14,10,12,9,12,9,14],
[12,12,13,0,11,8,7,13,7,8,12],
[14,13,12,15,0,13,9,14,13,10,15],
[14,13,16,18,13,0,15,15,15,11,17],
[14,15,14,19,17,11,0,15,12,11,15],
[11,13,17,13,12,11,11,0,13,14,14],
[14,11,14,19,13,11,14,13,0,8,15],
[18,11,17,18,16,15,15,12,18,0,17],
[14,10,12,14,11,9,11,12,11,9,0]])



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
result = np.append(np.array([11, 26, 177, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,15,15,13,11,12,13,13,12,22],
[13,0,13,25,17,14,18,14,11,19,24],
[11,13,0,18,14,17,17,17,16,15,21],
[11,1,8,0,11,11,8,9,3,8,13],
[13,9,12,15,0,14,15,14,8,15,18],
[15,12,9,15,12,0,13,13,7,12,19],
[14,8,9,18,11,13,0,12,12,11,17],
[13,12,9,17,12,13,14,0,9,14,19],
[13,15,10,23,18,19,14,17,0,18,22],
[14,7,11,18,11,14,15,12,8,0,21],
[4,2,5,13,8,7,9,7,4,5,0]])



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
result = np.append(np.array([11, 26, 178, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,14,14,13,16,18,16,14,20,11],
[14,0,15,13,14,13,19,14,16,18,12],
[12,11,0,14,14,13,20,15,15,19,15],
[12,13,12,0,14,16,14,17,16,18,10],
[13,12,12,12,0,15,16,16,17,17,12],
[10,13,13,10,11,0,13,14,17,16,9],
[8,7,6,12,10,13,0,13,12,15,10],
[10,12,11,9,10,12,13,0,12,13,10],
[12,10,11,10,9,9,14,14,0,12,9],
[6,8,7,8,9,10,11,13,14,0,7],
[15,14,11,16,14,17,16,16,17,19,0]])



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
result = np.append(np.array([11, 26, 179, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,10,15,18,16,17,14,13,14,16],
[11,0,11,8,7,8,10,16,12,8,8],
[16,15,0,14,16,13,15,14,10,13,16],
[11,18,12,0,15,10,8,14,13,9,16],
[8,19,10,11,0,7,7,14,13,4,9],
[10,18,13,16,19,0,10,12,15,11,20],
[9,16,11,18,19,16,0,13,16,11,18],
[12,10,12,12,12,14,13,0,11,12,14],
[13,14,16,13,13,11,10,15,0,13,18],
[12,18,13,17,22,15,15,14,13,0,18],
[10,18,10,10,17,6,8,12,8,8,0]])



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
result = np.append(np.array([11, 26, 180, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,16,7,6,10,9,9,7,5,11],
[11,0,17,12,4,14,12,8,6,11,14],
[10,9,0,4,9,4,8,12,7,8,11],
[19,14,22,0,10,11,12,15,15,12,15],
[20,22,17,16,0,12,17,18,18,19,18],
[16,12,22,15,14,0,11,15,14,19,18],
[17,14,18,14,9,15,0,13,9,20,14],
[17,18,14,11,8,11,13,0,4,14,15],
[19,20,19,11,8,12,17,22,0,16,18],
[21,15,18,14,7,7,6,12,10,0,13],
[15,12,15,11,8,8,12,11,8,13,0]])



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
result = np.append(np.array([11, 26, 181, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,12,4,8,6,9,4,5,5,5],
[19,0,16,16,18,14,19,12,17,14,10],
[14,10,0,9,9,9,14,6,7,11,5],
[22,10,17,0,15,14,15,14,10,13,14],
[18,8,17,11,0,8,17,5,10,10,11],
[20,12,17,12,18,0,17,17,13,15,7],
[17,7,12,11,9,9,0,7,4,11,10],
[22,14,20,12,21,9,19,0,12,13,12],
[21,9,19,16,16,13,22,14,0,18,17],
[21,12,15,13,16,11,15,13,8,0,5],
[21,16,21,12,15,19,16,14,9,21,0]])



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
result = np.append(np.array([11, 26, 182, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,12,14,20,14,8,15,8,15,13],
[15,0,14,16,17,8,13,12,10,15,7],
[14,12,0,17,15,12,10,13,9,14,13],
[12,10,9,0,11,7,7,10,5,12,8],
[6,9,11,15,0,7,3,9,6,9,8],
[12,18,14,19,19,0,9,12,10,14,7],
[18,13,16,19,23,17,0,23,16,19,14],
[11,14,13,16,17,14,3,0,11,14,13],
[18,16,17,21,20,16,10,15,0,19,11],
[11,11,12,14,17,12,7,12,7,0,12],
[13,19,13,18,18,19,12,13,15,14,0]])



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
result = np.append(np.array([11, 26, 183, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,9,16,10,8,14,14,13,14,14],
[9,0,12,14,14,12,23,12,11,23,11],
[17,14,0,17,6,6,15,15,17,17,17],
[10,12,9,0,11,13,17,24,8,20,10],
[16,12,20,15,0,8,15,19,14,15,16],
[18,14,20,13,18,0,11,15,14,17,22],
[12,3,11,9,11,15,0,14,7,10,11],
[12,14,11,2,7,11,12,0,3,17,12],
[13,15,9,18,12,12,19,23,0,23,12],
[12,3,9,6,11,9,16,9,3,0,11],
[12,15,9,16,10,4,15,14,14,15,0]])



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
result = np.append(np.array([11, 26, 184, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,9,4,10,4,6,15,13,13,6],
[19,0,15,13,21,9,10,19,13,19,19],
[17,11,0,12,14,8,14,21,17,21,8],
[22,13,14,0,18,12,11,18,18,18,18],
[16,5,12,8,0,5,11,19,16,22,9],
[22,17,18,14,21,0,17,21,22,22,12],
[20,16,12,15,15,9,0,15,18,18,13],
[11,7,5,8,7,5,11,0,14,14,7],
[13,13,9,8,10,4,8,12,0,6,6],
[13,7,5,8,4,4,8,12,20,0,4],
[20,7,18,8,17,14,13,19,20,22,0]])



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
result = np.append(np.array([11, 26, 185, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,11,17,16,8,15,14,11,13,12],
[8,0,4,12,12,2,11,14,6,3,11],
[15,22,0,18,17,15,12,17,16,10,18],
[9,14,8,0,10,4,9,13,9,9,6],
[10,14,9,16,0,9,10,12,10,13,15],
[18,24,11,22,17,0,18,17,13,16,14],
[11,15,14,17,16,8,0,15,13,10,14],
[12,12,9,13,14,9,11,0,11,10,8],
[15,20,10,17,16,13,13,15,0,19,15],
[13,23,16,17,13,10,16,16,7,0,17],
[14,15,8,20,11,12,12,18,11,9,0]])



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
result = np.append(np.array([11, 26, 186, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,11,10,11,13,14,12,14,14,14],
[11,0,10,11,9,12,15,10,12,16,13],
[15,16,0,15,15,14,14,12,14,17,17],
[16,15,11,0,14,14,12,11,13,16,18],
[15,17,11,12,0,12,16,12,15,17,18],
[13,14,12,12,14,0,15,11,15,17,15],
[12,11,12,14,10,11,0,12,13,16,12],
[14,16,14,15,14,15,14,0,13,17,17],
[12,14,12,13,11,11,13,13,0,17,14],
[12,10,9,10,9,9,10,9,9,0,15],
[12,13,9,8,8,11,14,9,12,11,0]])



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
result = np.append(np.array([11, 26, 187, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,15,15,12,9,11,16,18,20,18],
[9,0,11,10,11,11,6,14,12,13,12],
[11,15,0,13,11,9,8,15,12,17,17],
[11,16,13,0,13,9,7,14,15,16,15],
[14,15,15,13,0,15,9,13,14,15,14],
[17,15,17,17,11,0,14,17,19,20,18],
[15,20,18,19,17,12,0,21,19,19,18],
[10,12,11,12,13,9,5,0,10,13,13],
[8,14,14,11,12,7,7,16,0,16,18],
[6,13,9,10,11,6,7,13,10,0,13],
[8,14,9,11,12,8,8,13,8,13,0]])



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
result = np.append(np.array([11, 26, 188, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,12,10,8,8,7,8,6,7,10],
[15,0,13,15,10,13,10,11,10,9,14],
[14,13,0,12,11,10,7,10,7,9,12],
[16,11,14,0,8,14,6,12,10,7,14],
[18,16,15,18,0,15,7,17,8,8,14],
[18,13,16,12,11,0,6,8,10,6,14],
[19,16,19,20,19,20,0,21,13,13,20],
[18,15,16,14,9,18,5,0,11,8,15],
[20,16,19,16,18,16,13,15,0,11,13],
[19,17,17,19,18,20,13,18,15,0,16],
[16,12,14,12,12,12,6,11,13,10,0]])



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
result = np.append(np.array([11, 26, 189, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,12,14,13,15,10,10,14,11,10],
[9,0,11,10,7,11,5,6,10,8,5],
[14,15,0,12,10,15,10,12,13,9,9],
[12,16,14,0,11,14,12,6,7,14,7],
[13,19,16,15,0,17,11,9,10,16,8],
[11,15,11,12,9,0,8,9,10,9,7],
[16,21,16,14,15,18,0,11,13,17,13],
[16,20,14,20,17,17,15,0,15,18,10],
[12,16,13,19,16,16,13,11,0,15,9],
[15,18,17,12,10,17,9,8,11,0,11],
[16,21,17,19,18,19,13,16,17,15,0]])



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
result = np.append(np.array([11, 26, 190, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,15,20,20,14,12,12,19,23,24],
[6,0,11,9,12,3,8,9,8,13,13],
[11,15,0,15,17,9,13,8,7,24,20],
[6,17,11,0,14,11,15,16,10,26,26],
[6,14,9,12,0,9,16,14,11,16,16],
[12,23,17,15,17,0,10,11,19,19,24],
[14,18,13,11,10,16,0,7,15,26,20],
[14,17,18,10,12,15,19,0,9,19,18],
[7,18,19,16,15,7,11,17,0,19,24],
[3,13,2,0,10,7,0,7,7,0,17],
[2,13,6,0,10,2,6,8,2,9,0]])



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
result = np.append(np.array([11, 26, 191, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,14,11,8,12,13,12,13,15,14],
[11,0,16,11,11,12,13,12,13,14,17],
[12,10,0,9,10,9,9,12,12,9,10],
[15,15,17,0,15,15,15,16,13,10,17],
[18,15,16,11,0,16,15,16,15,16,17],
[14,14,17,11,10,0,15,13,12,14,15],
[13,13,17,11,11,11,0,15,13,13,15],
[14,14,14,10,10,13,11,0,17,13,16],
[13,13,14,13,11,14,13,9,0,13,15],
[11,12,17,16,10,12,13,13,13,0,13],
[12,9,16,9,9,11,11,10,11,13,0]])



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
result = np.append(np.array([11, 26, 192, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,13,15,11,14,14,14,12,13,17],
[18,0,16,15,13,16,12,13,11,13,15],
[13,10,0,12,14,17,13,16,11,13,14],
[11,11,14,0,13,12,11,13,10,8,12],
[15,13,12,13,0,15,11,15,11,11,15],
[12,10,9,14,11,0,11,13,11,10,13],
[12,14,13,15,15,15,0,19,15,12,13],
[12,13,10,13,11,13,7,0,11,11,11],
[14,15,15,16,15,15,11,15,0,14,16],
[13,13,13,18,15,16,14,15,12,0,18],
[9,11,12,14,11,13,13,15,10,8,0]])



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
result = np.append(np.array([11, 26, 193, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,13,12,9,13,15,17,9,4,12],
[7,0,11,5,7,9,13,19,12,8,7],
[13,15,0,6,7,16,12,11,14,15,13],
[14,21,20,0,16,24,25,24,19,12,20],
[17,19,19,10,0,20,20,22,19,17,17],
[13,17,10,2,6,0,10,12,9,7,7],
[11,13,14,1,6,16,0,15,8,10,9],
[9,7,15,2,4,14,11,0,6,11,6],
[17,14,12,7,7,17,18,20,0,10,12],
[22,18,11,14,9,19,16,15,16,0,16],
[14,19,13,6,9,19,17,20,14,10,0]])



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
result = np.append(np.array([11, 26, 194, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,13,10,8,7,11,12,10,8,15],
[17,0,15,12,18,17,18,17,14,18,22],
[13,11,0,7,11,8,8,11,9,10,16],
[16,14,19,0,13,9,11,16,18,11,22],
[18,8,15,13,0,11,11,19,16,11,20],
[19,9,18,17,15,0,17,19,16,18,22],
[15,8,18,15,15,9,0,16,15,10,17],
[14,9,15,10,7,7,10,0,12,7,18],
[16,12,17,8,10,10,11,14,0,8,18],
[18,8,16,15,15,8,16,19,18,0,25],
[11,4,10,4,6,4,9,8,8,1,0]])



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
result = np.append(np.array([11, 26, 195, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,14,13,12,13,10,9,8,13,7],
[19,0,13,12,14,14,13,12,12,12,12],
[12,13,0,16,10,16,11,14,9,12,9],
[13,14,10,0,15,12,12,12,12,16,13],
[14,12,16,11,0,19,18,16,11,17,13],
[13,12,10,14,7,0,12,14,14,8,10],
[16,13,15,14,8,14,0,17,13,14,11],
[17,14,12,14,10,12,9,0,14,10,10],
[18,14,17,14,15,12,13,12,0,16,12],
[13,14,14,10,9,18,12,16,10,0,10],
[19,14,17,13,13,16,15,16,14,16,0]])



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
result = np.append(np.array([11, 26, 196, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,20,18,13,21,18,20,22,22,14],
[5,0,7,7,8,11,7,8,11,13,9],
[6,19,0,19,11,17,19,19,16,12,15],
[8,19,7,0,8,10,12,13,7,17,4],
[13,18,15,18,0,19,21,20,19,19,15],
[5,15,9,16,7,0,5,10,11,11,7],
[8,19,7,14,5,21,0,14,13,13,13],
[6,18,7,13,6,16,12,0,9,11,10],
[4,15,10,19,7,15,13,17,0,13,9],
[4,13,14,9,7,15,13,15,13,0,7],
[12,17,11,22,11,19,13,16,17,19,0]])



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
result = np.append(np.array([11, 26, 197, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,15,11,11,11,15,9,9,6,11],
[20,0,19,20,14,14,17,13,16,14,17],
[11,7,0,9,8,10,8,8,9,5,6],
[15,6,17,0,12,12,13,7,11,7,9],
[15,12,18,14,0,15,15,14,15,11,13],
[15,12,16,14,11,0,14,11,14,12,11],
[11,9,18,13,11,12,0,9,11,7,12],
[17,13,18,19,12,15,17,0,16,11,15],
[17,10,17,15,11,12,15,10,0,11,11],
[20,12,21,19,15,14,19,15,15,0,17],
[15,9,20,17,13,15,14,11,15,9,0]])



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
result = np.append(np.array([11, 26, 198, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,18,14,12,13,13,17,16,18,13],
[14,0,18,11,15,14,11,15,15,11,16],
[8,8,0,9,14,10,7,13,13,11,13],
[12,15,17,0,16,17,11,19,14,14,17],
[14,11,12,10,0,11,11,14,14,13,10],
[13,12,16,9,15,0,9,16,13,9,15],
[13,15,19,15,15,17,0,14,16,13,16],
[9,11,13,7,12,10,12,0,9,10,8],
[10,11,13,12,12,13,10,17,0,13,14],
[8,15,15,12,13,17,13,16,13,0,17],
[13,10,13,9,16,11,10,18,12,9,0]])



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
result = np.append(np.array([11, 26, 199, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,14,11,16,7,13,12,15,12],
[13,0,16,14,17,11,13,13,14,12,9],
[13,10,0,9,12,8,15,14,17,16,13],
[12,12,17,0,10,15,15,9,14,13,13],
[15,9,14,16,0,14,13,11,14,13,12],
[10,15,18,11,12,0,15,13,16,15,12],
[19,13,11,11,13,11,0,12,17,17,14],
[13,13,12,17,15,13,14,0,13,11,8],
[14,12,9,12,12,10,9,13,0,14,11],
[11,14,10,13,13,11,9,15,12,0,11],
[14,17,13,13,14,14,12,18,15,15,0]])



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
result = np.append(np.array([11, 26, 200, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbrcw/mebbrcw_11_26.csv", index=False, header=False)