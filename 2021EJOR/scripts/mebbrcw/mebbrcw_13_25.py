
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 1
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,16,11,13,12,14,14,18,13,17,15,11,16],
[9,0,6,11,9,12,13,13,9,13,13,13,13],
[14,19,0,17,11,15,15,18,12,19,16,16,14],
[12,14,8,0,11,11,10,16,10,16,12,11,12],
[13,16,14,14,0,14,15,15,12,17,16,16,13],
[11,13,10,14,11,0,13,13,10,13,15,13,13],
[11,12,10,15,10,12,0,15,10,16,12,14,13],
[7,12,7,9,10,12,10,0,11,14,12,13,14],
[12,16,13,15,13,15,15,14,0,17,14,17,14],
[8,12,6,9,8,12,9,11,8,0,11,10,12],
[10,12,9,13,9,10,13,13,11,14,0,11,13],
[14,12,9,14,9,12,11,12,8,15,14,0,11],
[9,12,11,13,12,12,12,11,11,13,12,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 1, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,9,9,13,10,16,15,9,18,15,19,8],
[15,0,13,12,15,14,14,17,10,17,16,20,13],
[16,12,0,10,14,13,15,20,13,20,19,19,11],
[16,13,15,0,14,11,17,15,12,15,16,17,11],
[12,10,11,11,0,11,7,17,15,14,14,15,13],
[15,11,12,14,14,0,13,21,12,15,18,17,13],
[9,11,10,8,18,12,0,17,15,18,17,16,13],
[10,8,5,10,8,4,8,0,9,11,11,11,11],
[16,15,12,13,10,13,10,16,0,18,19,14,15],
[7,8,5,10,11,10,7,14,7,0,8,14,4],
[10,9,6,9,11,7,8,14,6,17,0,14,4],
[6,5,6,8,10,8,9,14,11,11,11,0,6],
[17,12,14,14,12,12,12,14,10,21,21,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 2, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,6,12,7,10,13,12,11,9,10,9,10],
[10,0,9,11,14,11,10,12,15,13,11,14,10],
[19,16,0,13,14,15,15,14,14,14,10,12,14],
[13,14,12,0,19,14,18,17,14,17,17,15,14],
[18,11,11,6,0,13,13,14,9,10,10,9,10],
[15,14,10,11,12,0,12,19,10,14,9,12,11],
[12,15,10,7,12,13,0,11,10,9,7,12,9],
[13,13,11,8,11,6,14,0,11,11,7,11,11],
[14,10,11,11,16,15,15,14,0,14,11,11,11],
[16,12,11,8,15,11,16,14,11,0,11,13,14],
[15,14,15,8,15,16,18,18,14,14,0,13,13],
[16,11,13,10,16,13,13,14,14,12,12,0,12],
[15,15,11,11,15,14,16,14,14,11,12,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 3, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,13,13,10,15,13,14,14,17,18,12,12],
[13,0,10,12,11,14,13,14,13,13,17,12,11],
[12,15,0,11,13,15,13,15,14,15,17,12,12],
[12,13,14,0,14,17,14,16,12,17,14,14,13],
[15,14,12,11,0,15,11,15,13,16,17,11,12],
[10,11,10,8,10,0,9,14,11,11,14,11,10],
[12,12,12,11,14,16,0,9,13,13,15,11,12],
[11,11,10,9,10,11,16,0,11,13,13,8,14],
[11,12,11,13,12,14,12,14,0,14,13,10,12],
[8,12,10,8,9,14,12,12,11,0,11,11,10],
[7,8,8,11,8,11,10,12,12,14,0,9,8],
[13,13,13,11,14,14,14,17,15,14,16,0,13],
[13,14,13,12,13,15,13,11,13,15,17,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 4, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,7,4,6,8,9,7,8,12,10,9,3],
[13,0,9,6,5,8,7,10,7,9,11,5,8],
[18,16,0,11,10,10,14,14,18,19,21,12,7],
[21,19,14,0,11,9,16,17,15,17,16,14,9],
[19,20,15,14,0,11,15,9,12,13,14,5,12],
[17,17,15,16,14,0,14,19,18,18,18,15,10],
[16,18,11,9,10,11,0,14,11,12,14,7,7],
[18,15,11,8,16,6,11,0,15,16,16,16,14],
[17,18,7,10,13,7,14,10,0,12,13,12,9],
[13,16,6,8,12,7,13,9,13,0,13,12,2],
[15,14,4,9,11,7,11,9,12,12,0,11,9],
[16,20,13,11,20,10,18,9,13,13,14,0,12],
[22,17,18,16,13,15,18,11,16,23,16,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 5, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,13,12,11,11,14,9,9,12,15,15,13],
[10,0,9,13,12,10,12,10,9,12,13,14,15],
[12,16,0,11,14,10,14,9,8,10,14,9,14],
[13,12,14,0,10,8,14,11,10,9,17,14,15],
[14,13,11,15,0,11,15,8,9,11,15,18,11],
[14,15,15,17,14,0,14,13,13,12,17,14,16],
[11,13,11,11,10,11,0,14,5,13,9,13,15],
[16,15,16,14,17,12,11,0,11,9,16,17,13],
[16,16,17,15,16,12,20,14,0,11,20,13,19],
[13,13,15,16,14,13,12,16,14,0,14,13,16],
[10,12,11,8,10,8,16,9,5,11,0,10,16],
[10,11,16,11,7,11,12,8,12,12,15,0,13],
[12,10,11,10,14,9,10,12,6,9,9,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 6, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,17,9,14,17,13,11,13,12,8,13,15],
[12,0,11,8,14,13,11,11,13,13,10,10,11],
[8,14,0,10,13,16,10,11,12,14,12,8,10],
[16,17,15,0,16,18,19,17,14,15,18,11,17],
[11,11,12,9,0,11,16,13,11,7,11,9,11],
[8,12,9,7,14,0,14,11,13,14,8,12,9],
[12,14,15,6,9,11,0,12,10,12,8,11,11],
[14,14,14,8,12,14,13,0,15,10,14,11,14],
[12,12,13,11,14,12,15,10,0,8,12,8,10],
[13,12,11,10,18,11,13,15,17,0,12,10,11],
[17,15,13,7,14,17,17,11,13,13,0,12,13],
[12,15,17,14,16,13,14,14,17,15,13,0,12],
[10,14,15,8,14,16,14,11,15,14,12,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 7, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,12,10,15,14,18,20,17,17,21,13,15],
[6,0,13,12,14,10,13,14,12,16,17,7,11],
[13,12,0,14,15,13,12,17,15,17,17,12,15],
[15,13,11,0,16,15,16,19,17,17,18,8,17],
[10,11,10,9,0,16,12,15,15,12,17,11,14],
[11,15,12,10,9,0,12,16,14,11,17,11,16],
[7,12,13,9,13,13,0,9,12,8,20,7,9],
[5,11,8,6,10,9,16,0,10,8,16,5,10],
[8,13,10,8,10,11,13,15,0,13,19,9,9],
[8,9,8,8,13,14,17,17,12,0,17,8,9],
[4,8,8,7,8,8,5,9,6,8,0,2,5],
[12,18,13,17,14,14,18,20,16,17,23,0,17],
[10,14,10,8,11,9,16,15,16,16,20,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 8, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,12,13,14,12,10,10,7,13,11,13,11],
[14,0,9,12,16,16,13,14,9,16,11,14,11],
[13,16,0,11,15,13,6,15,12,12,14,13,11],
[12,13,14,0,16,9,13,14,11,12,16,11,9],
[11,9,10,9,0,10,10,10,9,10,11,9,12],
[13,9,12,16,15,0,14,14,15,15,15,17,14],
[15,12,19,12,15,11,0,13,11,16,16,9,18],
[15,11,10,11,15,11,12,0,12,8,10,12,12],
[18,16,13,14,16,10,14,13,0,11,16,14,12],
[12,9,13,13,15,10,9,17,14,0,15,9,15],
[14,14,11,9,14,10,9,15,9,10,0,10,10],
[12,11,12,14,16,8,16,13,11,16,15,0,13],
[14,14,14,16,13,11,7,13,13,10,15,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 9, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,5,15,14,17,15,10,19,11,12,7,12],
[13,0,7,15,12,13,11,12,19,8,11,7,8],
[20,18,0,18,16,14,17,12,23,13,12,17,15],
[10,10,7,0,9,14,13,12,13,7,12,7,13],
[11,13,9,16,0,20,15,12,19,9,18,7,14],
[8,12,11,11,5,0,11,6,15,1,10,12,10],
[10,14,8,12,10,14,0,9,16,8,8,11,8],
[15,13,13,13,13,19,16,0,15,15,16,10,15],
[6,6,2,12,6,10,9,10,0,5,6,7,11],
[14,17,12,18,16,24,17,10,20,0,22,14,17],
[13,14,13,13,7,15,17,9,19,3,0,13,16],
[18,18,8,18,18,13,14,15,18,11,12,0,16],
[13,17,10,12,11,15,17,10,14,8,9,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 10, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,10,15,13,19,15,13,15,14,15,14,13],
[11,0,8,10,13,12,17,11,11,12,16,12,11],
[15,17,0,14,16,16,19,14,11,17,18,17,14],
[10,15,11,0,14,15,9,9,9,11,16,12,10],
[12,12,9,11,0,13,13,12,10,11,15,11,8],
[6,13,9,10,12,0,10,9,8,12,13,12,10],
[10,8,6,16,12,15,0,8,7,10,13,10,5],
[12,14,11,16,13,16,17,0,17,13,16,17,12],
[10,14,14,16,15,17,18,8,0,12,17,13,10],
[11,13,8,14,14,13,15,12,13,0,14,14,10],
[10,9,7,9,10,12,12,9,8,11,0,11,7],
[11,13,8,13,14,13,15,8,12,11,14,0,14],
[12,14,11,15,17,15,20,13,15,15,18,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 11, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,16,12,14,15,15,13,13,20,8,14,13],
[11,0,8,5,5,10,12,7,9,12,7,9,8],
[9,17,0,12,11,11,13,14,15,18,13,16,11],
[13,20,13,0,13,12,15,16,18,13,6,15,11],
[11,20,14,12,0,19,16,17,15,19,9,16,14],
[10,15,14,13,6,0,13,9,11,19,10,13,9],
[10,13,12,10,9,12,0,11,16,15,8,10,9],
[12,18,11,9,8,16,14,0,11,17,12,16,8],
[12,16,10,7,10,14,9,14,0,16,9,14,12],
[5,13,7,12,6,6,10,8,9,0,9,10,7],
[17,18,12,19,16,15,17,13,16,16,0,16,14],
[11,16,9,10,9,12,15,9,11,15,9,0,7],
[12,17,14,14,11,16,16,17,13,18,11,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 12, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,13,13,9,14,12,11,10,13,12,14,12],
[10,0,10,9,9,13,11,9,11,9,8,10,10],
[12,15,0,13,11,13,13,11,12,9,13,11,13],
[12,16,12,0,11,12,16,9,10,13,10,12,11],
[16,16,14,14,0,13,13,11,14,10,12,15,16],
[11,12,12,13,12,0,13,11,10,12,11,15,11],
[13,14,12,9,12,12,0,11,11,11,8,9,13],
[14,16,14,16,14,14,14,0,15,12,13,16,16],
[15,14,13,15,11,15,14,10,0,11,11,11,14],
[12,16,16,12,15,13,14,13,14,0,12,12,14],
[13,17,12,15,13,14,17,12,14,13,0,13,13],
[11,15,14,13,10,10,16,9,14,13,12,0,12],
[13,15,12,14,9,14,12,9,11,11,12,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 13, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,12,14,14,13,17,10,12,10,18,12,16],
[9,0,12,10,9,6,11,7,7,7,16,8,10],
[13,13,0,14,11,13,13,14,7,13,16,14,10],
[11,15,11,0,10,8,16,12,10,9,18,7,13],
[11,16,14,15,0,12,16,12,7,15,20,11,18],
[12,19,12,17,13,0,16,13,12,13,15,12,12],
[8,14,12,9,9,9,0,8,10,11,19,10,12],
[15,18,11,13,13,12,17,0,12,8,17,11,14],
[13,18,18,15,18,13,15,13,0,17,20,10,19],
[15,18,12,16,10,12,14,17,8,0,18,14,10],
[7,9,9,7,5,10,6,8,5,7,0,9,9],
[13,17,11,18,14,13,15,14,15,11,16,0,14],
[9,15,15,12,7,13,13,11,6,15,16,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 14, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,19,17,15,0,10,4,4,10,10,15,0],
[21,0,25,21,21,10,17,21,21,10,17,21,21],
[6,0,0,6,0,6,6,0,6,6,6,13,6],
[8,4,19,0,15,0,10,8,12,0,6,19,4],
[10,4,25,10,0,10,10,8,14,6,10,17,10],
[25,15,19,25,15,0,25,19,19,21,21,19,11],
[15,8,19,15,15,0,0,15,19,0,7,19,11],
[21,4,25,17,17,6,10,0,21,10,13,17,17],
[21,4,19,13,11,6,6,4,0,6,6,11,10],
[15,15,19,25,19,4,25,15,19,0,17,19,15],
[15,8,19,19,15,4,18,12,19,8,0,19,11],
[10,4,12,6,8,6,6,8,14,6,6,0,6],
[25,4,19,21,15,14,14,8,15,10,14,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 15, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,12,15,13,16,15,12,14,17,15,14,13],
[8,0,11,12,13,15,15,11,7,16,13,11,9],
[13,14,0,15,14,18,15,11,11,19,12,13,10],
[10,13,10,0,10,12,13,12,11,16,16,16,11],
[12,12,11,15,0,16,14,12,14,16,14,16,12],
[9,10,7,13,9,0,12,12,9,14,12,15,9],
[10,10,10,12,11,13,0,11,10,13,16,17,10],
[13,14,14,13,13,13,14,0,13,14,16,15,12],
[11,18,14,14,11,16,15,12,0,19,16,14,11],
[8,9,6,9,9,11,12,11,6,0,12,9,7],
[10,12,13,9,11,13,9,9,9,13,0,14,9],
[11,14,12,9,9,10,8,10,11,16,11,0,9],
[12,16,15,14,13,16,15,13,14,18,16,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 16, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,16,15,16,12,12,16,14,14,13,11,10],
[13,0,11,13,17,6,10,16,17,13,9,11,14],
[9,14,0,13,17,13,8,14,20,17,16,13,13],
[10,12,12,0,12,7,3,9,18,5,10,7,5],
[9,8,8,13,0,5,6,12,11,9,9,8,0],
[13,19,12,18,20,0,15,20,20,16,18,14,10],
[13,15,17,22,19,10,0,15,17,15,18,14,14],
[9,9,11,16,13,5,10,0,11,9,13,12,8],
[11,8,5,7,14,5,8,14,0,7,2,8,8],
[11,12,8,20,16,9,10,16,18,0,15,12,8],
[12,16,9,15,16,7,7,12,23,10,0,11,9],
[14,14,12,18,17,11,11,13,17,13,14,0,10],
[15,11,12,20,25,15,11,17,17,17,16,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 17, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,12,10,10,12,7,9,13,11,14,11,15],
[13,0,11,10,10,12,10,10,13,9,11,10,12],
[13,14,0,11,13,16,13,12,13,12,16,10,13],
[15,15,14,0,10,16,7,7,13,12,13,10,15],
[15,15,12,15,0,17,9,10,16,13,13,11,16],
[13,13,9,9,8,0,8,8,12,8,12,9,12],
[18,15,12,18,16,17,0,13,16,17,18,14,18],
[16,15,13,18,15,17,12,0,19,16,15,16,18],
[12,12,12,12,9,13,9,6,0,11,9,9,14],
[14,16,13,13,12,17,8,9,14,0,16,11,14],
[11,14,9,12,12,13,7,10,16,9,0,11,17],
[14,15,15,15,14,16,11,9,16,14,14,0,15],
[10,13,12,10,9,13,7,7,11,11,8,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 18, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,12,12,10,12,9,13,17,14,13,14,15],
[14,0,14,11,10,11,11,12,16,17,17,16,17],
[13,11,0,13,9,15,11,15,14,16,11,12,15],
[13,14,12,0,16,15,15,14,17,13,13,16,15],
[15,15,16,9,0,20,16,18,17,16,17,16,14],
[13,14,10,10,5,0,12,14,13,15,12,14,16],
[16,14,14,10,9,13,0,13,18,16,16,14,17],
[12,13,10,11,7,11,12,0,13,17,10,11,13],
[8,9,11,8,8,12,7,12,0,18,11,9,16],
[11,8,9,12,9,10,9,8,7,0,10,11,13],
[12,8,14,12,8,13,9,15,14,15,0,14,16],
[11,9,13,9,9,11,11,14,16,14,11,0,14],
[10,8,10,10,11,9,8,12,9,12,9,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 19, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,14,18,16,13,13,11,11,10,14,14,16],
[8,0,9,10,8,8,10,10,6,6,10,9,9],
[11,16,0,14,13,10,15,10,8,9,13,11,14],
[7,15,11,0,12,11,13,10,9,7,10,12,14],
[9,17,12,13,0,12,10,13,13,11,11,13,16],
[12,17,15,14,13,0,15,12,12,14,13,12,16],
[12,15,10,12,15,10,0,12,11,10,8,13,13],
[14,15,15,15,12,13,13,0,11,9,17,13,14],
[14,19,17,16,12,13,14,14,0,9,13,12,15],
[15,19,16,18,14,11,15,16,16,0,18,15,18],
[11,15,12,15,14,12,17,8,12,7,0,13,15],
[11,16,14,13,12,13,12,12,13,10,12,0,14],
[9,16,11,11,9,9,12,11,10,7,10,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 20, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,6,13,13,2,18,12,6,25,17,3,25],
[3,0,0,3,3,3,5,8,5,11,5,3,19],
[19,25,0,19,11,5,21,11,13,19,21,11,21],
[12,22,6,0,8,2,10,12,14,12,17,11,25],
[12,22,14,17,0,14,10,20,14,15,17,15,25],
[23,22,20,23,11,0,21,12,22,23,25,23,23],
[7,20,4,15,15,4,0,12,6,15,9,7,23],
[13,17,14,13,5,13,13,0,17,17,17,11,25],
[19,20,12,11,11,3,19,8,0,19,17,3,23],
[0,14,6,13,10,2,10,8,6,0,9,3,25],
[8,20,4,8,8,0,16,8,8,16,0,0,20],
[22,22,14,14,10,2,18,14,22,22,25,0,22],
[0,6,4,0,0,2,2,0,2,0,5,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 21, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,15,20,14,20,18,9,4,20,8,14,4],
[15,0,15,15,13,22,13,15,8,22,8,6,6],
[10,10,0,13,14,9,7,3,4,21,8,7,4],
[5,10,12,0,3,17,7,10,0,21,5,10,0],
[11,12,11,22,0,18,9,9,4,22,8,14,2],
[5,3,16,8,7,0,2,10,6,16,11,9,6],
[7,12,18,18,16,23,0,12,11,25,11,18,7],
[16,10,22,15,16,15,13,0,13,20,15,16,13],
[21,17,21,25,21,19,14,12,0,23,18,14,7],
[5,3,4,4,3,9,0,5,2,0,4,5,0],
[17,17,17,20,17,14,14,10,7,21,0,10,7],
[11,19,18,15,11,16,7,9,11,20,15,0,4],
[21,19,21,25,23,19,18,12,18,25,18,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 22, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,13,12,11,13,10,13,12,8,14,15,12],
[14,0,11,19,18,16,6,10,9,9,9,10,16],
[12,14,0,12,17,17,16,22,19,14,19,11,15],
[13,6,13,0,11,13,8,13,12,4,13,10,8],
[14,7,8,14,0,11,12,11,10,7,11,10,20],
[12,9,8,12,14,0,8,16,8,11,6,12,12],
[15,19,9,17,13,17,0,17,16,14,18,13,15],
[12,15,3,12,14,9,8,0,12,7,13,7,11],
[13,16,6,13,15,17,9,13,0,12,15,13,14],
[17,16,11,21,18,14,11,18,13,0,15,14,18],
[11,16,6,12,14,19,7,12,10,10,0,11,14],
[10,15,14,15,15,13,12,18,12,11,14,0,16],
[13,9,10,17,5,13,10,14,11,7,11,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 23, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,17,17,13,14,10,16,12,16,16,16,15],
[13,0,19,19,17,15,18,15,12,16,15,11,20],
[8,6,0,11,11,16,12,12,10,15,15,8,17],
[8,6,14,0,7,13,9,15,14,12,13,12,16],
[12,8,14,18,0,18,10,16,12,18,14,14,20],
[11,10,9,12,7,0,10,11,9,11,16,9,16],
[15,7,13,16,15,15,0,19,15,17,15,15,21],
[9,10,13,10,9,14,6,0,13,12,11,12,8],
[13,13,15,11,13,16,10,12,0,10,13,11,11],
[9,9,10,13,7,14,8,13,15,0,16,7,15],
[9,10,10,12,11,9,10,14,12,9,0,11,9],
[9,14,17,13,11,16,10,13,14,18,14,0,15],
[10,5,8,9,5,9,4,17,14,10,16,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 24, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,18,19,14,15,18,20,12,14,13,18,11],
[20,0,19,20,19,12,20,20,16,20,19,18,19],
[7,6,0,9,6,4,6,5,5,2,6,6,9],
[6,5,16,0,7,4,10,8,4,7,12,13,16],
[11,6,19,18,0,9,15,13,9,14,10,13,12],
[10,13,21,21,16,0,16,20,9,16,19,15,20],
[7,5,19,15,10,9,0,17,6,9,10,12,12],
[5,5,20,17,12,5,8,0,5,9,15,11,15],
[13,9,20,21,16,16,19,20,0,20,15,13,15],
[11,5,23,18,11,9,16,16,5,0,10,14,13],
[12,6,19,13,15,6,15,10,10,15,0,14,13],
[7,7,19,12,12,10,13,14,12,11,11,0,13],
[14,6,16,9,13,5,13,10,10,12,12,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 25, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,17,11,12,11,15,12,16,11,10,14,16],
[13,0,13,10,14,11,15,12,17,11,11,11,13],
[8,12,0,6,11,9,11,11,14,5,6,11,11],
[14,15,19,0,17,12,18,13,19,13,16,15,22],
[13,11,14,8,0,13,12,13,13,12,8,13,14],
[14,14,16,13,12,0,16,14,16,11,10,13,18],
[10,10,14,7,13,9,0,11,15,11,6,13,16],
[13,13,14,12,12,11,14,0,17,10,10,14,14],
[9,8,11,6,12,9,10,8,0,9,7,9,12],
[14,14,20,12,13,14,14,15,16,0,14,16,14],
[15,14,19,9,17,15,19,15,18,11,0,16,16],
[11,14,14,10,12,12,12,11,16,9,9,0,14],
[9,12,14,3,11,7,9,11,13,11,9,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 26, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,16,16,9,19,16,9,10,9,10,16,6],
[15,0,16,13,24,22,25,21,16,21,16,7,21],
[9,9,0,6,15,16,12,9,15,15,15,9,15],
[9,12,19,0,12,13,13,12,12,18,18,12,15],
[16,1,10,13,0,16,10,7,10,6,7,7,15],
[6,3,9,12,9,0,9,0,0,6,9,6,6],
[9,0,13,12,15,16,0,0,15,6,15,0,15],
[16,4,16,13,18,25,25,0,19,18,19,10,15],
[15,9,10,13,15,25,10,6,0,12,9,7,12],
[16,4,10,7,19,19,19,7,13,0,13,7,21],
[15,9,10,7,18,16,10,6,16,12,0,7,21],
[9,18,16,13,18,19,25,15,18,18,18,0,15],
[19,4,10,10,10,19,10,10,13,4,4,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 27, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,12,15,12,15,15,15,15,22,25,12,22],
[0,0,12,12,12,12,15,15,12,12,12,12,22],
[13,13,0,3,13,3,3,15,3,10,13,12,13],
[10,13,22,0,22,10,25,25,13,22,10,22,10],
[13,13,12,3,0,3,3,15,3,22,13,12,13],
[10,13,22,15,22,0,25,25,3,22,10,22,10],
[10,10,22,0,22,0,0,22,0,22,10,22,10],
[10,10,10,0,10,0,3,0,0,10,10,10,10],
[10,13,22,12,22,22,25,25,0,22,22,22,22],
[3,13,15,3,3,3,3,15,3,0,13,15,13],
[0,13,12,15,12,15,15,15,3,12,0,12,10],
[13,13,13,3,13,3,3,15,3,10,13,0,13],
[3,3,12,15,12,15,15,15,3,12,15,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 28, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,17,12,18,15,20,17,15,18,18,15,14],
[4,0,11,11,7,8,9,8,11,6,9,8,8],
[8,14,0,11,9,12,13,12,14,13,11,10,13],
[13,14,14,0,13,10,15,15,16,12,17,11,14],
[7,18,16,12,0,10,17,17,13,10,12,11,13],
[10,17,13,15,15,0,18,11,17,13,15,9,15],
[5,16,12,10,8,7,0,10,13,8,10,10,12],
[8,17,13,10,8,14,15,0,15,12,13,12,12],
[10,14,11,9,12,8,12,10,0,10,14,11,15],
[7,19,12,13,15,12,17,13,15,0,16,10,14],
[7,16,14,8,13,10,15,12,11,9,0,10,11],
[10,17,15,14,14,16,15,13,14,15,15,0,15],
[11,17,12,11,12,10,13,13,10,11,14,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 29, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,12,13,9,10,10,9,11,11,15,8],
[15,0,15,19,22,15,14,16,11,13,14,18,15],
[15,10,0,12,14,8,9,14,12,12,13,15,5],
[13,6,13,0,13,7,7,9,9,12,12,13,9],
[12,3,11,12,0,12,13,14,10,13,10,12,9],
[16,10,17,18,13,0,9,15,12,16,16,17,14],
[15,11,16,18,12,16,0,17,16,16,17,18,14],
[15,9,11,16,11,10,8,0,14,10,11,8,11],
[16,14,13,16,15,13,9,11,0,12,11,12,13],
[14,12,13,13,12,9,9,15,13,0,13,13,8],
[14,11,12,13,15,9,8,14,14,12,0,16,16],
[10,7,10,12,13,8,7,17,13,12,9,0,10],
[17,10,20,16,16,11,11,14,12,17,9,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 30, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,14,9,14,20,10,11,15,12,10,13,15],
[13,0,10,8,9,13,7,14,14,12,10,11,11],
[11,15,0,12,15,19,10,16,16,15,9,16,20],
[16,17,13,0,16,17,11,13,15,13,12,11,16],
[11,16,10,9,0,16,15,14,16,14,13,14,17],
[5,12,6,8,9,0,6,10,11,8,6,8,11],
[15,18,15,14,10,19,0,16,16,15,13,13,18],
[14,11,9,12,11,15,9,0,12,12,11,11,14],
[10,11,9,10,9,14,9,13,0,11,7,11,13],
[13,13,10,12,11,17,10,13,14,0,9,10,18],
[15,15,16,13,12,19,12,14,18,16,0,16,17],
[12,14,9,14,11,17,12,14,14,15,9,0,17],
[10,14,5,9,8,14,7,11,12,7,8,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 31, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,17,17,18,17,9,13,14,13,11,14,12],
[10,0,16,10,17,11,12,10,8,15,10,7,12],
[8,9,0,9,16,11,8,7,8,7,10,7,9],
[8,15,16,0,16,12,9,10,13,13,11,9,9],
[7,8,9,9,0,11,6,7,11,8,12,11,10],
[8,14,14,13,14,0,11,10,17,12,12,11,14],
[16,13,17,16,19,14,0,11,12,12,6,10,11],
[12,15,18,15,18,15,14,0,17,13,8,11,12],
[11,17,17,12,14,8,13,8,0,14,8,9,12],
[12,10,18,12,17,13,13,12,11,0,11,13,8],
[14,15,15,14,13,13,19,17,17,14,0,12,17],
[11,18,18,16,14,14,15,14,16,12,13,0,15],
[13,13,16,16,15,11,14,13,13,17,8,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 32, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,16,9,24,9,19,9,18,9,19,18,10],
[7,0,13,9,13,8,10,3,9,7,3,0,1],
[9,12,0,10,18,9,10,3,18,2,12,12,3],
[16,16,15,0,16,16,23,9,16,15,18,16,16],
[1,12,7,9,0,3,10,3,12,7,12,9,3],
[16,17,16,9,22,0,17,3,18,7,12,9,8],
[6,15,15,2,15,8,0,8,18,0,11,9,6],
[16,22,22,16,22,22,17,0,16,16,17,9,23],
[7,16,7,9,13,7,7,9,0,7,9,7,7],
[16,18,23,10,18,18,25,9,18,0,12,12,9],
[6,22,13,7,13,13,14,8,16,13,0,6,13],
[7,25,13,9,16,16,16,16,18,13,19,0,16],
[15,24,22,9,22,17,19,2,18,16,12,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 33, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,9,11,11,13,18,13,16,8,13,13,12],
[18,0,18,15,22,12,24,17,22,19,17,20,19],
[16,7,0,11,17,12,17,10,23,22,17,11,12],
[14,10,14,0,20,9,16,14,12,13,9,14,15],
[14,3,8,5,0,13,20,17,16,13,8,9,14],
[12,13,13,16,12,0,17,10,23,11,12,12,8],
[7,1,8,9,5,8,0,8,12,8,2,9,7],
[12,8,15,11,8,15,17,0,18,20,12,7,8],
[9,3,2,13,9,2,13,7,0,6,9,2,8],
[17,6,3,12,12,14,17,5,19,0,12,11,11],
[12,8,8,16,17,13,23,13,16,13,0,12,17],
[12,5,14,11,16,13,16,18,23,14,13,0,10],
[13,6,13,10,11,17,18,17,17,14,8,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 34, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,15,13,12,11,15,15,9,17,14,12,14],
[6,0,3,8,11,3,14,17,10,12,10,13,14],
[10,22,0,10,17,14,14,17,8,12,20,13,13],
[12,17,15,0,19,11,16,23,15,23,17,15,17],
[13,14,8,6,0,13,13,17,2,11,12,9,16],
[14,22,11,14,12,0,16,18,11,16,16,10,14],
[10,11,11,9,12,9,0,12,9,12,15,14,10],
[10,8,8,2,8,7,13,0,8,6,16,11,7],
[16,15,17,10,23,14,16,17,0,10,15,13,14],
[8,13,13,2,14,9,13,19,15,0,15,15,13],
[11,15,5,8,13,9,10,9,10,10,0,6,9],
[13,12,12,10,16,15,11,14,12,10,19,0,9],
[11,11,12,8,9,11,15,18,11,12,16,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 35, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,19,12,18,19,12,19,16,22,17,15,17],
[2,0,12,10,9,4,5,10,10,7,10,5,6],
[6,13,0,10,12,10,4,13,13,10,12,8,7],
[13,15,15,0,15,15,4,17,18,10,14,10,11],
[7,16,13,10,0,14,8,16,16,11,14,11,7],
[6,21,15,10,11,0,10,13,8,16,13,13,12],
[13,20,21,21,17,15,0,13,16,16,14,11,11],
[6,15,12,8,9,12,12,0,8,16,10,11,10],
[9,15,12,7,9,17,9,17,0,10,17,13,12],
[3,18,15,15,14,9,9,9,15,0,13,18,14],
[8,15,13,11,11,12,11,15,8,12,0,17,11],
[10,20,17,15,14,12,14,14,12,7,8,0,8],
[8,19,18,14,18,13,14,15,13,11,14,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 36, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,13,7,13,8,8,8,8,8,8,5,8],
[15,0,14,15,22,12,15,13,16,10,13,6,16],
[12,11,0,12,12,12,12,13,11,5,13,15,13],
[18,10,13,0,10,10,8,15,10,3,16,12,10],
[12,3,13,15,0,5,6,9,6,9,6,3,11],
[17,13,13,15,20,0,11,14,14,14,11,6,16],
[17,10,13,17,19,14,0,13,13,11,16,13,13],
[17,12,12,10,16,11,12,0,11,10,15,7,15],
[17,9,14,15,19,11,12,14,0,12,15,12,20],
[17,15,20,22,16,11,14,15,13,0,13,10,15],
[17,12,12,9,19,14,9,10,10,12,0,5,10],
[20,19,10,13,22,19,12,18,13,15,20,0,16],
[17,9,12,15,14,9,12,10,5,10,15,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 37, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,11,17,12,14,13,12,12,13,15,14,16],
[10,0,15,14,10,13,13,11,13,7,16,12,17],
[14,10,0,15,11,15,15,13,14,11,14,11,10],
[8,11,10,0,9,10,13,9,13,7,12,8,13],
[13,15,14,16,0,15,18,15,18,9,16,14,16],
[11,12,10,15,10,0,12,12,12,7,15,13,13],
[12,12,10,12,7,13,0,11,13,8,11,12,12],
[13,14,12,16,10,13,14,0,13,11,18,12,15],
[13,12,11,12,7,13,12,12,0,8,13,14,9],
[12,18,14,18,16,18,17,14,17,0,17,12,16],
[10,9,11,13,9,10,14,7,12,8,0,10,7],
[11,13,14,17,11,12,13,13,11,13,15,0,10],
[9,8,15,12,9,12,13,10,16,9,18,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 38, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,11,12,10,12,11,15,14,13,10,14,10],
[12,0,14,11,9,8,9,18,7,8,13,16,9],
[14,11,0,13,8,11,11,16,12,9,12,17,9],
[13,14,12,0,11,11,12,16,10,11,12,10,13],
[15,16,17,14,0,11,16,18,15,10,19,16,12],
[13,17,14,14,14,0,14,16,18,11,17,13,11],
[14,16,14,13,9,11,0,18,9,9,13,10,7],
[10,7,9,9,7,9,7,0,5,10,8,14,9],
[11,18,13,15,10,7,16,20,0,10,12,14,9],
[12,17,16,14,15,14,16,15,15,0,13,17,10],
[15,12,13,13,6,8,12,17,13,12,0,16,13],
[11,9,8,15,9,12,15,11,11,8,9,0,7],
[15,16,16,12,13,14,18,16,16,15,12,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 39, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,6,0,5,5,6,11,10,5,0,11,5],
[15,0,11,11,5,5,11,11,11,9,5,11,5],
[19,14,0,5,15,15,11,15,19,9,4,15,15],
[25,14,20,0,19,19,11,25,25,9,14,21,15],
[20,20,10,6,0,0,6,10,20,4,4,6,0],
[20,20,10,6,25,0,6,20,20,10,10,21,16],
[19,14,14,14,19,19,0,19,14,9,14,15,19],
[14,14,10,0,15,5,6,0,14,4,4,15,5],
[15,14,6,0,5,5,11,11,0,9,4,11,5],
[20,16,16,16,21,15,16,21,16,0,10,21,15],
[25,20,21,11,21,15,11,21,21,15,0,21,21],
[14,14,10,4,19,4,10,10,14,4,4,0,4],
[20,20,10,10,25,9,6,20,20,10,4,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 40, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,11,11,12,13,11,12,14,13,15,14,16],
[11,0,11,12,16,11,7,10,14,13,14,16,14],
[14,14,0,17,18,15,14,12,15,16,15,14,17],
[14,13,8,0,11,10,12,12,12,11,10,11,16],
[13,9,7,14,0,12,8,11,11,15,11,13,12],
[12,14,10,15,13,0,10,15,14,14,16,15,17],
[14,18,11,13,17,15,0,11,15,14,16,16,17],
[13,15,13,13,14,10,14,0,17,15,18,16,16],
[11,11,10,13,14,11,10,8,0,15,12,14,15],
[12,12,9,14,10,11,11,10,10,0,10,14,13],
[10,11,10,15,14,9,9,7,13,15,0,14,13],
[11,9,11,14,12,10,9,9,11,11,11,0,14],
[9,11,8,9,13,8,8,9,10,12,12,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 41, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,3,13,14,11,14,12,7,14,18,6,11],
[17,0,11,17,17,11,20,16,14,14,18,15,14],
[22,14,0,19,20,12,21,12,14,20,17,11,20],
[12,8,6,0,14,5,13,12,9,15,16,6,14],
[11,8,5,11,0,9,15,10,7,14,12,6,12],
[14,14,13,20,16,0,15,12,12,18,17,13,17],
[11,5,4,12,10,10,0,11,14,11,15,6,10],
[13,9,13,13,15,13,14,0,13,14,16,7,12],
[18,11,11,16,18,13,11,12,0,18,19,10,15],
[11,11,5,10,11,7,14,11,7,0,13,9,6],
[7,7,8,9,13,8,10,9,6,12,0,8,9],
[19,10,14,19,19,12,19,18,15,16,17,0,17],
[14,11,5,11,13,8,15,13,10,19,16,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 42, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,7,0,17,13,0,7,3,8,3,20,8],
[12,0,7,0,17,3,12,12,0,12,15,22,8],
[18,18,0,13,20,13,8,8,13,8,8,18,8],
[25,25,12,0,22,20,12,15,3,15,15,25,15],
[8,8,5,3,0,3,8,8,3,8,8,8,8],
[12,22,12,5,22,0,12,12,0,12,12,22,12],
[25,13,17,13,17,13,0,25,13,25,8,25,18],
[18,13,17,10,17,13,0,0,13,8,3,20,18],
[22,25,12,22,22,25,12,12,0,15,15,22,15],
[17,13,17,10,17,13,0,17,10,0,3,17,18],
[22,10,17,10,17,13,17,22,10,22,0,17,18],
[5,3,7,0,17,3,0,5,3,8,8,0,8],
[17,17,17,10,17,13,7,7,10,7,7,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 43, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,14,13,10,14,14,9,21,8,11,9,14],
[17,0,15,13,14,14,17,12,15,16,12,14,14],
[11,10,0,14,14,16,14,13,16,12,14,12,14],
[12,12,11,0,12,13,15,10,10,11,12,9,11],
[15,11,11,13,0,15,13,14,18,13,11,12,17],
[11,11,9,12,10,0,11,10,15,7,13,7,7],
[11,8,11,10,12,14,0,10,10,10,14,12,13],
[16,13,12,15,11,15,15,0,15,13,12,12,10],
[4,10,9,15,7,10,15,10,0,10,7,8,8],
[17,9,13,14,12,18,15,12,15,0,13,12,12],
[14,13,11,13,14,12,11,13,18,12,0,9,12],
[16,11,13,16,13,18,13,13,17,13,16,0,12],
[11,11,11,14,8,18,12,15,17,13,13,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 44, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,9,12,6,6,9,5,10,9,9,3,5],
[13,0,13,14,12,12,16,9,12,7,15,9,11],
[16,12,0,10,7,6,9,8,11,11,9,6,6],
[13,11,15,0,9,11,14,9,14,12,11,10,9],
[19,13,18,16,0,14,14,9,11,12,16,9,12],
[19,13,19,14,11,0,19,13,16,11,16,10,12],
[16,9,16,11,11,6,0,11,12,10,13,10,10],
[20,16,17,16,16,12,14,0,17,14,15,15,14],
[15,13,14,11,14,9,13,8,0,8,13,9,12],
[16,18,14,13,13,14,15,11,17,0,14,6,11],
[16,10,16,14,9,9,12,10,12,11,0,10,8],
[22,16,19,15,16,15,15,10,16,19,15,0,13],
[20,14,19,16,13,13,15,11,13,14,17,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 45, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,18,13,10,6,9,9,3,12,15,9,14],
[11,0,15,9,10,12,14,15,10,3,5,12,12],
[7,10,0,8,10,12,14,14,7,0,3,9,10],
[12,16,17,0,11,5,7,15,11,8,12,17,21],
[15,15,15,14,0,9,11,15,13,11,13,21,23],
[19,13,13,20,16,0,9,14,19,11,14,17,19],
[16,11,11,18,14,16,0,15,17,8,9,14,19],
[16,10,11,10,10,11,10,0,16,8,11,16,15],
[22,15,18,14,12,6,8,9,0,14,16,12,17],
[13,22,25,17,14,14,17,17,11,0,11,12,18],
[10,20,22,13,12,11,16,14,9,14,0,16,20],
[16,13,16,8,4,8,11,9,13,13,9,0,9],
[11,13,15,4,2,6,6,10,8,7,5,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 46, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,14,17,14,9,13,13,11,13,14,13,13],
[6,0,10,14,9,12,8,7,8,9,7,11,9],
[11,15,0,15,9,11,13,9,3,12,13,18,15],
[8,11,10,0,9,5,9,10,6,5,13,10,9],
[11,16,16,16,0,12,13,14,13,11,13,17,14],
[16,13,14,20,13,0,12,11,10,13,14,15,13],
[12,17,12,16,12,13,0,10,6,9,13,9,12],
[12,18,16,15,11,14,15,0,11,15,8,17,14],
[14,17,22,19,12,15,19,14,0,18,15,21,20],
[12,16,13,20,14,12,16,10,7,0,10,24,15],
[11,18,12,12,12,11,12,17,10,15,0,16,11],
[12,14,7,15,8,10,16,8,4,1,9,0,8],
[12,16,10,16,11,12,13,11,5,10,14,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 47, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,9,15,11,15,12,9,10,7,11,12,11],
[15,0,14,12,11,19,12,16,20,15,7,15,17],
[16,11,0,10,9,15,14,9,14,12,7,10,8],
[10,13,15,0,11,18,14,7,17,9,11,14,11],
[14,14,16,14,0,22,12,11,21,10,12,13,16],
[10,6,10,7,3,0,7,2,10,2,4,6,8],
[13,13,11,11,13,18,0,15,16,8,16,16,10],
[16,9,16,18,14,23,10,0,22,16,13,13,14],
[15,5,11,8,4,15,9,3,0,7,3,6,9],
[18,10,13,16,15,23,17,9,18,0,13,13,9],
[14,18,18,14,13,21,9,12,22,12,0,22,17],
[13,10,15,11,12,19,9,12,19,12,3,0,17],
[14,8,17,14,9,17,15,11,16,16,8,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 48, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,12,13,11,10,13,7,10,12,7,13,8],
[14,0,15,14,11,14,17,14,14,14,11,14,9],
[13,10,0,10,5,15,13,7,6,19,7,8,8],
[12,11,15,0,13,13,13,2,10,13,7,12,4],
[14,14,20,12,0,15,18,14,11,19,9,11,9],
[15,11,10,12,10,0,10,10,10,12,8,13,5],
[12,8,12,12,7,15,0,12,12,11,7,11,6],
[18,11,18,23,11,15,13,0,18,19,13,14,10],
[15,11,19,15,14,15,13,7,0,15,8,11,8],
[13,11,6,12,6,13,14,6,10,0,3,11,8],
[18,14,18,18,16,17,18,12,17,22,0,21,13],
[12,11,17,13,14,12,14,11,14,14,4,0,11],
[17,16,17,21,16,20,19,15,17,17,12,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 49, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,8,6,8,11,20,11,13,17,8,8,17],
[11,0,12,12,14,15,17,17,19,20,17,11,12],
[17,13,0,15,19,17,19,19,22,20,13,11,14],
[19,13,10,0,19,16,16,10,22,14,16,13,14],
[17,11,6,6,0,17,19,8,16,17,17,14,14],
[14,10,8,9,8,0,22,13,13,20,16,8,15],
[5,8,6,9,6,3,0,8,13,11,8,8,15],
[14,8,6,15,17,12,17,0,17,15,19,9,12],
[12,6,3,3,9,12,12,8,0,17,14,11,9],
[8,5,5,11,8,5,14,10,8,0,7,10,11],
[17,8,12,9,8,9,17,6,11,18,0,12,12],
[17,14,14,12,11,17,17,16,14,15,13,0,12],
[8,13,11,11,11,10,10,13,16,14,13,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 50, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,15,12,13,11,12,13,14,11,13,12,11],
[12,0,10,10,9,17,14,12,12,12,13,10,11],
[10,15,0,12,13,15,16,14,13,10,16,12,13],
[13,15,13,0,13,19,15,12,14,13,16,13,11],
[12,16,12,12,0,15,15,10,11,13,13,9,11],
[14,8,10,6,10,0,10,8,13,11,11,8,10],
[13,11,9,10,10,15,0,10,12,8,15,12,10],
[12,13,11,13,15,17,15,0,12,13,11,10,13],
[11,13,12,11,14,12,13,13,0,11,14,11,9],
[14,13,15,12,12,14,17,12,14,0,17,12,10],
[12,12,9,9,12,14,10,14,11,8,0,10,11],
[13,15,13,12,16,17,13,15,14,13,15,0,14],
[14,14,12,14,14,15,15,12,16,15,14,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 51, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,8,14,16,16,9,8,7,11,8,8,8],
[17,0,3,9,11,11,11,0,3,3,3,9,11],
[17,22,0,18,18,15,18,8,24,10,17,18,22],
[11,16,7,0,18,15,11,7,10,10,10,18,15],
[9,14,7,7,0,22,9,7,16,10,16,16,13],
[9,14,10,10,3,0,9,7,10,10,16,16,16],
[16,14,7,14,16,16,0,8,7,10,14,14,8],
[17,25,17,18,18,18,17,0,24,10,10,18,18],
[18,22,1,15,9,15,18,1,0,11,7,18,15],
[14,22,15,15,15,15,15,15,14,0,7,15,15],
[17,22,8,15,9,9,11,15,18,18,0,18,8],
[17,16,7,7,9,9,11,7,7,10,7,0,15],
[17,14,3,10,12,9,17,7,10,10,17,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 52, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,15,10,11,13,9,12,13,16,8,18,8],
[11,0,14,14,11,14,10,13,15,14,12,17,10],
[10,11,0,12,9,12,11,11,13,13,10,16,9],
[15,11,13,0,10,15,10,7,12,13,10,15,8],
[14,14,16,15,0,15,16,17,16,15,8,18,13],
[12,11,13,10,10,0,13,12,13,14,11,10,9],
[16,15,14,15,9,12,0,9,12,16,11,19,15],
[13,12,14,18,8,13,16,0,12,16,15,15,11],
[12,10,12,13,9,12,13,13,0,18,11,9,5],
[9,11,12,12,10,11,9,9,7,0,8,16,10],
[17,13,15,15,17,14,14,10,14,17,0,15,9],
[7,8,9,10,7,15,6,10,16,9,10,0,6],
[17,15,16,17,12,16,10,14,20,15,16,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 53, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,12,13,9,12,12,14,14,10,14,13,14],
[13,0,14,15,9,11,10,15,11,9,10,13,13],
[13,11,0,16,8,10,8,15,11,9,10,14,11],
[12,10,9,0,6,7,5,13,9,8,8,10,10],
[16,16,17,19,0,15,13,18,17,11,14,16,15],
[13,14,15,18,10,0,13,15,14,13,10,12,14],
[13,15,17,20,12,12,0,16,12,11,9,17,15],
[11,10,10,12,7,10,9,0,13,8,7,7,13],
[11,14,14,16,8,11,13,12,0,10,10,13,16],
[15,16,16,17,14,12,14,17,15,0,9,13,15],
[11,15,15,17,11,15,16,18,15,16,0,17,17],
[12,12,11,15,9,13,8,18,12,12,8,0,11],
[11,12,14,15,10,11,10,12,9,10,8,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 54, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,13,16,12,11,17,14,14,12,13,16,9],
[10,0,14,14,15,11,16,13,15,10,11,15,8],
[12,11,0,15,12,11,16,14,18,12,10,17,13],
[9,11,10,0,11,8,11,12,15,9,9,9,5],
[13,10,13,14,0,13,17,11,14,12,13,13,8],
[14,14,14,17,12,0,14,14,16,11,14,14,12],
[8,9,9,14,8,11,0,11,14,12,9,10,8],
[11,12,11,13,14,11,14,0,11,9,10,14,8],
[11,10,7,10,11,9,11,14,0,5,9,12,5],
[13,15,13,16,13,14,13,16,20,0,16,12,13],
[12,14,15,16,12,11,16,15,16,9,0,12,12],
[9,10,8,16,12,11,15,11,13,13,13,0,8],
[16,17,12,20,17,13,17,17,20,12,13,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 55, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,15,17,16,14,14,11,18,11,14,15,9],
[10,0,16,12,15,10,14,15,17,11,11,13,14],
[10,9,0,9,8,9,10,9,13,10,6,9,11],
[8,13,16,0,11,12,9,13,14,11,11,9,12],
[9,10,17,14,0,12,12,11,13,10,10,9,13],
[11,15,16,13,13,0,12,14,19,12,15,14,9],
[11,11,15,16,13,13,0,11,16,12,12,8,13],
[14,10,16,12,14,11,14,0,14,14,10,12,13],
[7,8,12,11,12,6,9,11,0,11,10,10,5],
[14,14,15,14,15,13,13,11,14,0,15,12,12],
[11,14,19,14,15,10,13,15,15,10,0,13,13],
[10,12,16,16,16,11,17,13,15,13,12,0,10],
[16,11,14,13,12,16,12,12,20,13,12,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 56, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,1,7,6,1,13,3,9,13,7,19,7],
[22,0,11,6,10,4,12,3,14,18,17,19,16],
[24,14,0,18,18,18,12,9,20,24,22,18,18],
[18,19,7,0,18,6,16,13,18,18,19,21,12],
[19,15,7,7,0,7,13,3,9,19,19,19,13],
[24,21,7,19,18,0,12,15,20,24,19,19,18],
[12,13,13,9,12,13,0,9,12,13,13,15,13],
[22,22,16,12,22,10,16,0,24,22,16,18,16],
[16,11,5,7,16,5,13,1,0,17,17,19,17],
[12,7,1,7,6,1,12,3,8,0,13,19,13],
[18,8,3,6,6,6,12,9,8,12,0,19,6],
[6,6,7,4,6,6,10,7,6,6,6,0,6],
[18,9,7,13,12,7,12,9,8,12,19,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 57, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,15,13,14,15,15,15,13,12,14,15,16],
[6,0,12,11,10,13,12,11,11,12,10,16,10],
[10,13,0,14,12,14,14,12,14,13,11,15,12],
[12,14,11,0,11,11,14,15,11,12,11,14,13],
[11,15,13,14,0,18,12,15,11,12,13,16,14],
[10,12,11,14,7,0,12,14,10,9,10,15,12],
[10,13,11,11,13,13,0,15,9,10,9,15,13],
[10,14,13,10,10,11,10,0,10,10,8,14,13],
[12,14,11,14,14,15,16,15,0,15,14,19,13],
[13,13,12,13,13,16,15,15,10,0,11,15,12],
[11,15,14,14,12,15,16,17,11,14,0,19,16],
[10,9,10,11,9,10,10,11,6,10,6,0,12],
[9,15,13,12,11,13,12,12,12,13,9,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 58, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,15,12,11,11,10,9,13,14,10,13,11],
[12,0,15,13,12,12,11,12,12,13,9,11,11],
[10,10,0,10,9,11,10,9,10,10,10,10,10],
[13,12,15,0,10,11,8,11,10,12,12,10,14],
[14,13,16,15,0,14,11,16,13,13,13,12,12],
[14,13,14,14,11,0,15,10,11,14,13,13,11],
[15,14,15,17,14,10,0,12,14,13,11,9,13],
[16,13,16,14,9,15,13,0,9,13,12,12,13],
[12,13,15,15,12,14,11,16,0,14,12,10,11],
[11,12,15,13,12,11,12,12,11,0,15,12,11],
[15,16,15,13,12,12,14,13,13,10,0,12,14],
[12,14,15,15,13,12,16,13,15,13,13,0,11],
[14,14,15,11,13,14,12,12,14,14,11,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 59, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,13,10,10,9,10,11,13,12,13,12,12],
[15,0,14,11,10,11,10,12,13,14,16,14,19],
[12,11,0,8,6,11,5,10,9,11,9,11,13],
[15,14,17,0,12,15,10,18,10,13,15,16,16],
[15,15,19,13,0,16,12,16,14,13,16,16,19],
[16,14,14,10,9,0,9,11,11,12,17,13,15],
[15,15,20,15,13,16,0,14,12,13,16,19,21],
[14,13,15,7,9,14,11,0,15,10,11,14,18],
[12,12,16,15,11,14,13,10,0,14,13,17,16],
[13,11,14,12,12,13,12,15,11,0,16,14,17],
[12,9,16,10,9,8,9,14,12,9,0,14,17],
[13,11,14,9,9,12,6,11,8,11,11,0,16],
[13,6,12,9,6,10,4,7,9,8,8,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 60, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,11,14,14,14,9,14,17,12,13,17,19],
[9,0,8,14,11,13,8,13,13,9,12,12,15],
[14,17,0,14,14,15,14,14,15,12,14,17,16],
[11,11,11,0,16,10,13,13,12,12,9,16,10],
[11,14,11,9,0,12,11,11,14,10,10,14,15],
[11,12,10,15,13,0,14,17,14,13,15,13,18],
[16,17,11,12,14,11,0,11,12,14,10,16,16],
[11,12,11,12,14,8,14,0,13,8,12,12,14],
[8,12,10,13,11,11,13,12,0,17,9,18,13],
[13,16,13,13,15,12,11,17,8,0,12,20,14],
[12,13,11,16,15,10,15,13,16,13,0,18,13],
[8,13,8,9,11,12,9,13,7,5,7,0,11],
[6,10,9,15,10,7,9,11,12,11,12,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 61, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,11,9,11,9,9,11,10,13,12,8,10],
[13,0,9,6,12,10,10,11,10,9,11,14,12],
[14,16,0,8,11,13,13,9,12,15,17,11,9],
[16,19,17,0,14,12,17,15,14,16,16,17,15],
[14,13,14,11,0,14,15,8,12,17,15,12,13],
[16,15,12,13,11,0,16,11,10,17,13,12,13],
[16,15,12,8,10,9,0,10,10,13,15,14,10],
[14,14,16,10,17,14,15,0,16,15,15,12,15],
[15,15,13,11,13,15,15,9,0,15,11,13,10],
[12,16,10,9,8,8,12,10,10,0,7,10,7],
[13,14,8,9,10,12,10,10,14,18,0,7,12],
[17,11,14,8,13,13,11,13,12,15,18,0,16],
[15,13,16,10,12,12,15,10,15,18,13,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 62, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,9,6,8,4,13,11,12,14,14,10,11],
[16,0,8,10,13,8,11,11,11,13,15,14,11],
[16,17,0,14,8,13,9,15,13,18,13,6,12],
[19,15,11,0,9,11,10,14,17,16,15,12,11],
[17,12,17,16,0,15,17,17,18,18,18,13,13],
[21,17,12,14,10,0,13,14,12,17,14,13,12],
[12,14,16,15,8,12,0,9,10,13,12,13,11],
[14,14,10,11,8,11,16,0,14,18,17,14,10],
[13,14,12,8,7,13,15,11,0,21,11,12,10],
[11,12,7,9,7,8,12,7,4,0,11,11,8],
[11,10,12,10,7,11,13,8,14,14,0,10,3],
[15,11,19,13,12,12,12,11,13,14,15,0,11],
[14,14,13,14,12,13,14,15,15,17,22,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 63, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,11,10,10,17,22,13,13,19,12,5,12],
[16,0,12,8,11,16,19,12,13,14,11,10,11],
[14,13,0,16,18,12,20,15,12,15,16,14,18],
[15,17,9,0,15,17,13,10,15,13,13,14,13],
[15,14,7,10,0,14,12,12,13,12,11,14,9],
[8,9,13,8,11,0,13,11,7,12,10,8,13],
[3,6,5,12,13,12,0,4,10,11,13,7,8],
[12,13,10,15,13,14,21,0,14,15,17,17,14],
[12,12,13,10,12,18,15,11,0,14,12,9,14],
[6,11,10,12,13,13,14,10,11,0,11,10,15],
[13,14,9,12,14,15,12,8,13,14,0,15,9],
[20,15,11,11,11,17,18,8,16,15,10,0,12],
[13,14,7,12,16,12,17,11,11,10,16,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 64, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,13,16,20,9,13,11,21,12,20,9,17],
[8,0,14,10,10,5,12,9,12,4,10,5,11],
[12,11,0,14,9,11,8,11,16,6,11,13,6],
[9,15,11,0,18,13,13,11,22,10,18,7,15],
[5,15,16,7,0,7,16,11,11,15,20,7,15],
[16,20,14,12,18,0,12,17,23,13,18,19,15],
[12,13,17,12,9,13,0,14,16,13,16,9,11],
[14,16,14,14,14,8,11,0,16,15,14,16,15],
[4,13,9,3,14,2,9,9,0,4,14,7,8],
[13,21,19,15,10,12,12,10,21,0,19,17,23],
[5,15,14,7,5,7,9,11,11,6,0,9,13],
[16,20,12,18,18,6,16,9,18,8,16,0,13],
[8,14,19,10,10,10,14,10,17,2,12,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 65, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,16,14,14,17,12,17,19,14,21,15,17],
[12,0,15,14,17,15,15,17,15,12,12,12,16],
[9,10,0,12,12,15,9,15,14,13,15,10,14],
[11,11,13,0,15,9,11,13,14,9,14,14,17],
[11,8,13,10,0,15,15,15,14,13,16,11,13],
[8,10,10,16,10,0,11,13,12,11,15,10,13],
[13,10,16,14,10,14,0,18,16,13,17,14,19],
[8,8,10,12,10,12,7,0,14,7,16,10,14],
[6,10,11,11,11,13,9,11,0,7,11,13,11],
[11,13,12,16,12,14,12,18,18,0,15,13,14],
[4,13,10,11,9,10,8,9,14,10,0,7,8],
[10,13,15,11,14,15,11,15,12,12,18,0,18],
[8,9,11,8,12,12,6,11,14,11,17,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 66, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,15,19,17,15,10,15,19,17,14,14,15],
[15,0,18,19,15,17,16,17,17,18,16,18,12],
[10,7,0,13,15,15,7,14,16,16,11,13,16],
[6,6,12,0,10,12,10,14,17,15,9,16,12],
[8,10,10,15,0,15,11,14,14,14,14,13,14],
[10,8,10,13,10,0,5,12,18,14,12,10,13],
[15,9,18,15,14,20,0,16,17,18,15,12,16],
[10,8,11,11,11,13,9,0,10,14,12,8,8],
[6,8,9,8,11,7,8,15,0,13,10,9,13],
[8,7,9,10,11,11,7,11,12,0,8,8,9],
[11,9,14,16,11,13,10,13,15,17,0,15,14],
[11,7,12,9,12,15,13,17,16,17,10,0,14],
[10,13,9,13,11,12,9,17,12,16,11,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 67, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,11,7,10,13,10,15,14,14,15,11,15],
[15,0,12,5,10,14,11,15,13,16,9,9,15],
[14,13,0,14,14,16,12,14,14,13,14,13,17],
[18,20,11,0,16,14,12,19,19,15,17,18,17],
[15,15,11,9,0,15,12,14,16,18,15,15,19],
[12,11,9,11,10,0,13,14,14,12,12,12,16],
[15,14,13,13,13,12,0,14,10,13,14,11,14],
[10,10,11,6,11,11,11,0,7,11,12,9,11],
[11,12,11,6,9,11,15,18,0,13,14,9,14],
[11,9,12,10,7,13,12,14,12,0,13,11,12],
[10,16,11,8,10,13,11,13,11,12,0,11,17],
[14,16,12,7,10,13,14,16,16,14,14,0,16],
[10,10,8,8,6,9,11,14,11,13,8,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 68, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,19,8,19,19,11,19,23,11,13,19,11],
[14,0,19,8,19,19,11,19,12,11,21,19,11],
[6,6,0,6,14,11,15,17,14,17,17,11,17],
[17,17,19,0,19,11,15,15,23,11,17,11,17],
[6,6,11,6,0,11,15,17,6,13,17,11,17],
[6,6,14,14,14,0,4,14,14,17,6,10,6],
[14,14,10,10,10,21,0,14,14,13,25,10,21],
[6,6,8,10,8,11,11,0,14,13,17,8,13],
[2,13,11,2,19,11,11,11,0,13,13,11,13],
[14,14,8,14,12,8,12,12,12,0,14,8,14],
[12,4,8,8,8,19,0,8,12,11,0,8,0],
[6,6,14,14,14,15,15,17,14,17,17,0,17],
[14,14,8,8,8,19,4,12,12,11,25,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 69, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,12,14,13,13,12,9,11,15,14,12],
[14,0,14,10,15,12,17,12,11,10,17,13,13],
[14,11,0,10,11,12,15,13,9,12,14,12,14],
[13,15,15,0,15,12,17,13,10,10,16,15,15],
[11,10,14,10,0,8,15,14,10,11,13,14,14],
[12,13,13,13,17,0,17,15,9,12,17,16,14],
[12,8,10,8,10,8,0,12,8,10,8,10,14],
[13,13,12,12,11,10,13,0,8,11,15,11,15],
[16,14,16,15,15,16,17,17,0,12,16,13,16],
[14,15,13,15,14,13,15,14,13,0,16,14,11],
[10,8,11,9,12,8,17,10,9,9,0,9,13],
[11,12,13,10,11,9,15,14,12,11,16,0,16],
[13,12,11,10,11,11,11,10,9,14,12,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 70, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,13,15,11,10,11,12,12,14,13,11,13],
[13,0,14,17,12,13,14,17,13,14,10,16,14],
[12,11,0,14,10,14,13,15,11,13,10,13,13],
[10,8,11,0,8,11,9,16,7,9,9,12,11],
[14,13,15,17,0,13,10,18,13,9,11,17,12],
[15,12,11,14,12,0,12,16,14,11,10,17,8],
[14,11,12,16,15,13,0,16,13,15,12,16,14],
[13,8,10,9,7,9,9,0,9,10,8,14,11],
[13,12,14,18,12,11,12,16,0,16,15,15,14],
[11,11,12,16,16,14,10,15,9,0,14,17,11],
[12,15,15,16,14,15,13,17,10,11,0,18,12],
[14,9,12,13,8,8,9,11,10,8,7,0,9],
[12,11,12,14,13,17,11,14,11,14,13,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 71, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,12,17,13,14,16,13,12,14,17,14,15],
[8,0,15,7,10,13,15,13,9,12,7,10,8],
[13,10,0,11,11,13,11,13,11,8,7,12,6],
[8,18,14,0,11,11,17,10,12,13,8,10,8],
[12,15,14,14,0,10,17,9,11,14,13,13,16],
[11,12,12,14,15,0,15,9,10,10,12,14,12],
[9,10,14,8,8,10,0,9,10,8,6,9,8],
[12,12,12,15,16,16,16,0,13,15,15,15,12],
[13,16,14,13,14,15,15,12,0,13,15,13,12],
[11,13,17,12,11,15,17,10,12,0,7,13,12],
[8,18,18,17,12,13,19,10,10,18,0,12,13],
[11,15,13,15,12,11,16,10,12,12,13,0,11],
[10,17,19,17,9,13,17,13,13,13,12,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 72, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,14,17,16,16,12,16,11,15,15,12,15],
[13,0,16,17,15,15,13,16,15,16,15,10,16],
[11,9,0,12,14,12,8,13,9,13,10,7,14],
[8,8,13,0,10,10,9,11,8,13,11,6,13],
[9,10,11,15,0,12,11,10,12,13,9,9,14],
[9,10,13,15,13,0,11,12,12,14,13,12,16],
[13,12,17,16,14,14,0,17,15,16,16,14,16],
[9,9,12,14,15,13,8,0,11,17,11,10,15],
[14,10,16,17,13,13,10,14,0,16,13,12,13],
[10,9,12,12,12,11,9,8,9,0,7,10,13],
[10,10,15,14,16,12,9,14,12,18,0,9,14],
[13,15,18,19,16,13,11,15,13,15,16,0,17],
[10,9,11,12,11,9,9,10,12,12,11,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 73, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,18,15,16,18,11,15,19,15,14,19,18],
[16,0,15,16,13,19,14,10,18,15,15,17,12],
[7,10,0,16,10,10,8,7,13,12,14,13,10],
[10,9,9,0,14,10,14,15,18,12,12,13,13],
[9,12,15,11,0,16,8,9,18,9,12,18,9],
[7,6,15,15,9,0,14,13,12,12,12,15,14],
[14,11,17,11,17,11,0,16,16,18,12,14,14],
[10,15,18,10,16,12,9,0,16,12,15,13,12],
[6,7,12,7,7,13,9,9,0,13,9,14,9],
[10,10,13,13,16,13,7,13,12,0,7,13,13],
[11,10,11,13,13,13,13,10,16,18,0,16,10],
[6,8,12,12,7,10,11,12,11,12,9,0,9],
[7,13,15,12,16,11,11,13,16,12,15,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 74, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,25,23,23,7,17,17,17,15,9,23,15],
[10,0,25,25,25,9,17,17,17,17,17,18,17],
[0,0,0,16,16,0,10,2,0,7,0,8,8],
[2,0,9,0,17,7,17,2,9,9,2,0,15],
[2,0,9,8,0,7,10,2,9,9,2,8,0],
[18,16,25,18,18,0,10,10,17,17,10,18,18],
[8,8,15,8,15,15,0,8,15,7,8,8,8],
[8,8,23,23,23,15,17,0,15,7,0,8,23],
[8,8,25,16,16,8,10,10,0,7,8,8,16],
[10,8,18,16,16,8,18,18,18,0,10,8,16],
[16,8,25,23,23,15,17,25,17,15,0,16,23],
[2,7,17,25,17,7,17,17,17,17,9,0,15],
[10,8,17,10,25,7,17,2,9,9,2,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 75, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,13,14,10,10,11,15,9,11,13,13,12],
[15,0,18,13,13,17,10,16,17,14,18,18,18],
[12,7,0,17,12,15,15,16,12,12,19,19,14],
[11,12,8,0,9,12,11,9,7,3,11,8,11],
[15,12,13,16,0,15,14,16,14,12,17,13,15],
[15,8,10,13,10,0,15,13,12,7,15,9,13],
[14,15,10,14,11,10,0,16,12,9,15,10,18],
[10,9,9,16,9,12,9,0,9,5,12,8,14],
[16,8,13,18,11,13,13,16,0,12,17,14,17],
[14,11,13,22,13,18,16,20,13,0,19,17,21],
[12,7,6,14,8,10,10,13,8,6,0,11,14],
[12,7,6,17,12,16,15,17,11,8,14,0,17],
[13,7,11,14,10,12,7,11,8,4,11,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 76, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,12,18,16,14,16,20,15,14,11,13,12],
[9,0,17,18,17,21,16,17,17,14,16,16,12],
[13,8,0,12,12,16,19,21,16,10,14,6,10],
[7,7,13,0,19,14,11,19,16,12,8,10,6],
[9,8,13,6,0,13,11,11,13,10,10,12,4],
[11,4,9,11,12,0,12,16,15,11,11,9,7],
[9,9,6,14,14,13,0,17,16,12,11,10,7],
[5,8,4,6,14,9,8,0,15,11,7,8,3],
[10,8,9,9,12,10,9,10,0,12,11,8,6],
[11,11,15,13,15,14,13,14,13,0,13,16,6],
[14,9,11,17,15,14,14,18,14,12,0,6,13],
[12,9,19,15,13,16,15,17,17,9,19,0,11],
[13,13,15,19,21,18,18,22,19,19,12,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 77, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,18,12,19,15,17,14,14,15,14,14,13],
[14,0,12,13,10,10,15,12,9,13,12,9,8],
[7,13,0,9,14,10,16,13,11,10,11,6,11],
[13,12,16,0,14,16,16,11,12,15,12,12,13],
[6,15,11,11,0,13,12,7,9,11,10,11,8],
[10,15,15,9,12,0,14,12,10,10,11,9,8],
[8,10,9,9,13,11,0,3,5,8,7,11,5],
[11,13,12,14,18,13,22,0,14,16,14,13,13],
[11,16,14,13,16,15,20,11,0,18,12,13,12],
[10,12,15,10,14,15,17,9,7,0,12,12,7],
[11,13,14,13,15,14,18,11,13,13,0,14,16],
[11,16,19,13,14,16,14,12,12,13,11,0,13],
[12,17,14,12,17,17,20,12,13,18,9,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 78, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,7,9,14,9,7,8,8,6,8,8,10],
[11,0,15,13,14,14,11,10,11,11,8,7,9],
[18,10,0,14,17,12,13,13,11,13,12,14,17],
[16,12,11,0,13,10,12,14,12,14,13,14,17],
[11,11,8,12,0,4,8,6,8,7,10,6,11],
[16,11,13,15,21,0,13,12,10,13,9,9,16],
[18,14,12,13,17,12,0,16,12,12,12,9,14],
[17,15,12,11,19,13,9,0,13,14,16,9,18],
[17,14,14,13,17,15,13,12,0,16,9,16,12],
[19,14,12,11,18,12,13,11,9,0,12,14,12],
[17,17,13,12,15,16,13,9,16,13,0,11,13],
[17,18,11,11,19,16,16,16,9,11,14,0,16],
[15,16,8,8,14,9,11,7,13,13,12,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 79, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,12,12,11,11,11,14,11,16,11,8,12],
[13,0,13,8,12,14,11,13,16,18,13,8,11],
[13,12,0,10,11,11,9,13,16,12,12,11,12],
[13,17,15,0,12,14,11,11,15,12,14,7,14],
[14,13,14,13,0,16,10,14,14,15,13,15,14],
[14,11,14,11,9,0,12,11,13,12,10,11,12],
[14,14,16,14,15,13,0,13,13,18,12,14,14],
[11,12,12,14,11,14,12,0,14,13,11,12,10],
[14,9,9,10,11,12,12,11,0,12,11,10,12],
[9,7,13,13,10,13,7,12,13,0,10,9,12],
[14,12,13,11,12,15,13,14,14,15,0,15,12],
[17,17,14,18,10,14,11,13,15,16,10,0,10],
[13,14,13,11,11,13,11,15,13,13,13,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 80, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,16,13,18,14,19,16,12,17,19,19,18],
[7,0,14,11,16,9,18,13,13,15,11,7,15],
[9,11,0,9,11,7,13,16,9,10,9,8,15],
[12,14,16,0,16,14,16,15,13,19,16,11,14],
[7,9,14,9,0,7,13,12,10,15,15,10,21],
[11,16,18,11,18,0,16,18,11,14,21,14,16],
[6,7,12,9,12,9,0,15,13,12,8,5,10],
[9,12,9,10,13,7,10,0,9,9,11,13,14],
[13,12,16,12,15,14,12,16,0,10,13,12,18],
[8,10,15,6,10,11,13,16,15,0,9,8,12],
[6,14,16,9,10,4,17,14,12,16,0,9,15],
[6,18,17,14,15,11,20,12,13,17,16,0,12],
[7,10,10,11,4,9,15,11,7,13,10,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 81, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,9,16,13,6,15,12,8,14,9,15,12],
[12,0,5,20,18,13,19,11,14,10,11,18,19],
[16,20,0,22,20,15,21,19,10,16,11,20,18],
[9,5,3,0,7,8,13,4,4,8,2,12,3],
[12,7,5,18,0,13,16,11,12,12,11,16,9],
[19,12,10,17,12,0,23,12,11,16,6,16,14],
[10,6,4,12,9,2,0,3,6,8,5,10,12],
[13,14,6,21,14,13,22,0,11,14,7,22,12],
[17,11,15,21,13,14,19,14,0,18,12,21,14],
[11,15,9,17,13,9,17,11,7,0,8,14,12],
[16,14,14,23,14,19,20,18,13,17,0,20,12],
[10,7,5,13,9,9,15,3,4,11,5,0,6],
[13,6,7,22,16,11,13,13,11,13,13,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 82, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,10,8,7,12,12,16,10,10,15,16,11],
[16,0,11,13,10,17,11,13,10,13,20,19,13],
[15,14,0,11,10,21,11,17,14,18,22,22,17],
[17,12,14,0,12,18,8,16,14,12,18,19,15],
[18,15,15,13,0,18,9,14,15,14,20,18,12],
[13,8,4,7,7,0,11,12,6,8,19,17,8],
[13,14,14,17,16,14,0,16,14,13,19,18,12],
[9,12,8,9,11,13,9,0,7,10,17,17,8],
[15,15,11,11,10,19,11,18,0,19,21,18,17],
[15,12,7,13,11,17,12,15,6,0,19,18,11],
[10,5,3,7,5,6,6,8,4,6,0,12,8],
[9,6,3,6,7,8,7,8,7,7,13,0,7],
[14,12,8,10,13,17,13,17,8,14,17,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 83, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,14,4,22,14,18,11,14,18,4,14],
[14,0,18,14,4,22,7,14,18,14,14,14,21],
[14,7,0,14,11,15,14,21,10,7,14,7,17],
[11,11,11,0,15,22,11,15,11,18,11,11,18],
[21,21,14,10,0,18,10,17,21,14,21,14,21],
[3,3,10,3,7,0,3,10,3,7,3,3,17],
[11,18,11,14,15,22,0,18,18,18,18,11,18],
[7,11,4,10,8,15,7,0,14,11,14,7,14],
[14,7,15,14,4,22,7,11,0,14,18,11,17],
[11,11,18,7,11,18,7,14,11,0,11,11,25],
[7,11,11,14,4,22,7,11,7,14,0,7,17],
[21,11,18,14,11,22,14,18,14,14,18,0,17],
[11,4,8,7,4,8,7,11,8,0,8,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 84, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,13,15,18,14,17,17,16,12,14,12,15],
[11,0,17,13,14,14,13,15,13,15,11,13,13],
[12,8,0,13,8,13,16,15,14,11,10,16,15],
[10,12,12,0,13,14,16,16,14,11,12,11,13],
[7,11,17,12,0,8,13,10,12,14,7,10,14],
[11,11,12,11,17,0,15,13,15,16,14,11,18],
[8,12,9,9,12,10,0,14,15,13,12,8,13],
[8,10,10,9,15,12,11,0,16,13,11,8,16],
[9,12,11,11,13,10,10,9,0,14,10,7,7],
[13,10,14,14,11,9,12,12,11,0,13,10,14],
[11,14,15,13,18,11,13,14,15,12,0,13,19],
[13,12,9,14,15,14,17,17,18,15,12,0,16],
[10,12,10,12,11,7,12,9,18,11,6,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 85, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,13,7,11,5,10,13,7,12,7,9,9],
[19,0,14,16,13,15,12,14,11,9,9,11,12],
[12,11,0,12,10,10,13,19,11,18,12,14,15],
[18,9,13,0,18,11,15,18,15,15,10,18,15],
[14,12,15,7,0,10,11,16,13,16,8,15,10],
[20,10,15,14,15,0,15,17,15,15,13,18,14],
[15,13,12,10,14,10,0,15,14,15,6,6,12],
[12,11,6,7,9,8,10,0,8,14,4,9,9],
[18,14,14,10,12,10,11,17,0,13,6,12,15],
[13,16,7,10,9,10,10,11,12,0,5,9,10],
[18,16,13,15,17,12,19,21,19,20,0,16,16],
[16,14,11,7,10,7,19,16,13,16,9,0,15],
[16,13,10,10,15,11,13,16,10,15,9,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 86, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,11,14,0,0,2,7,2,11,2,12,0],
[13,0,13,13,13,13,11,4,13,13,4,13,13],
[14,12,0,23,14,9,14,12,2,16,5,21,14],
[11,12,2,0,9,9,9,0,2,11,2,0,9],
[25,12,11,16,0,0,2,7,9,18,14,14,7],
[25,12,16,16,25,0,16,14,11,23,14,16,16],
[23,14,11,16,23,9,0,9,9,20,14,14,16],
[18,21,13,25,18,11,16,0,13,11,18,18,16],
[23,12,23,23,16,14,16,12,0,16,12,21,14],
[14,12,9,14,7,2,5,14,9,0,14,14,7],
[23,21,20,23,11,11,11,7,13,11,0,23,9],
[13,12,4,25,11,9,11,7,4,11,2,0,11],
[25,12,11,16,18,9,9,9,11,18,16,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 87, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,7,7,7,4,2,10,1,9,7,7,10],
[15,0,9,10,12,7,7,15,8,8,13,11,13],
[18,16,0,16,17,14,14,17,12,13,12,13,15],
[18,15,9,0,10,11,11,9,16,12,14,11,13],
[18,13,8,15,0,5,8,8,14,14,10,6,10],
[21,18,11,14,20,0,11,18,11,16,18,16,17],
[23,18,11,14,17,14,0,16,15,13,13,9,13],
[15,10,8,16,17,7,9,0,11,11,10,10,11],
[24,17,13,9,11,14,10,14,0,17,17,13,15],
[16,17,12,13,11,9,12,14,8,0,13,11,12],
[18,12,13,11,15,7,12,15,8,12,0,12,14],
[18,14,12,14,19,9,16,15,12,14,13,0,15],
[15,12,10,12,15,8,12,14,10,13,11,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 88, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,16,13,14,12,16,15,15,14,17,14],
[14,0,10,10,15,16,14,19,20,11,14,15,15],
[14,15,0,10,8,12,11,18,15,11,16,17,10],
[9,15,15,0,13,12,12,17,14,14,10,10,12],
[12,10,17,12,0,16,15,18,14,14,15,20,14],
[11,9,13,13,9,0,15,15,12,11,13,16,10],
[13,11,14,13,10,10,0,15,13,12,17,12,11],
[9,6,7,8,7,10,10,0,12,8,11,9,7],
[10,5,10,11,11,13,12,13,0,13,10,10,12],
[10,14,14,11,11,14,13,17,12,0,18,11,11],
[11,11,9,15,10,12,8,14,15,7,0,8,8],
[8,10,8,15,5,9,13,16,15,14,17,0,12],
[11,10,15,13,11,15,14,18,13,14,17,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 89, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,12,8,11,13,12,13,11,13,12,10,11],
[12,0,9,9,13,11,12,10,14,12,15,10,18],
[13,16,0,10,14,8,14,8,9,9,16,13,16],
[17,16,15,0,15,13,18,13,11,15,17,16,17],
[14,12,11,10,0,11,15,9,14,12,16,9,19],
[12,14,17,12,14,0,16,10,14,10,11,13,19],
[13,13,11,7,10,9,0,6,12,11,11,12,13],
[12,15,17,12,16,15,19,0,14,12,11,16,17],
[14,11,16,14,11,11,13,11,0,7,9,14,15],
[12,13,16,10,13,15,14,13,18,0,19,12,15],
[13,10,9,8,9,14,14,14,16,6,0,12,15],
[15,15,12,9,16,12,13,9,11,13,13,0,16],
[14,7,9,8,6,6,12,8,10,10,10,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 90, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,19,15,19,17,18,16,16,13,16,15,15],
[13,0,19,14,17,18,16,15,14,14,12,19,18],
[6,6,0,8,6,14,5,9,12,7,6,7,12],
[10,11,17,0,17,20,15,13,10,18,11,15,17],
[6,8,19,8,0,18,9,12,9,12,10,10,15],
[8,7,11,5,7,0,10,4,9,7,6,8,11],
[7,9,20,10,16,15,0,12,11,16,7,9,10],
[9,10,16,12,13,21,13,0,9,9,13,13,16],
[9,11,13,15,16,16,14,16,0,14,10,11,15],
[12,11,18,7,13,18,9,16,11,0,12,10,12],
[9,13,19,14,15,19,18,12,15,13,0,13,15],
[10,6,18,10,15,17,16,12,14,15,12,0,13],
[10,7,13,8,10,14,15,9,10,13,10,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 91, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,13,10,16,14,9,10,13,16,10,13,14],
[16,0,15,13,16,19,13,15,15,19,13,10,16],
[12,10,0,11,11,16,11,10,13,16,10,13,12],
[15,12,14,0,12,17,11,18,13,18,11,10,17],
[9,9,14,13,0,18,9,11,11,17,11,11,13],
[11,6,9,8,7,0,13,10,10,13,7,8,5],
[16,12,14,14,16,12,0,11,15,19,14,11,10],
[15,10,15,7,14,15,14,0,12,16,13,7,10],
[12,10,12,12,14,15,10,13,0,16,10,11,11],
[9,6,9,7,8,12,6,9,9,0,8,9,4],
[15,12,15,14,14,18,11,12,15,17,0,10,14],
[12,15,12,15,14,17,14,18,14,16,15,0,15],
[11,9,13,8,12,20,15,15,14,21,11,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 92, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,10,12,7,14,14,13,11,15,11,12,14],
[13,0,14,13,16,15,13,19,10,13,18,12,16],
[15,11,0,13,8,14,17,11,14,14,14,14,15],
[13,12,12,0,10,15,14,14,10,14,14,7,12],
[18,9,17,15,0,16,15,19,15,14,15,15,20],
[11,10,11,10,9,0,11,13,11,8,10,10,15],
[11,12,8,11,10,14,0,15,8,15,12,11,13],
[12,6,14,11,6,12,10,0,9,9,6,11,13],
[14,15,11,15,10,14,17,16,0,16,16,14,17],
[10,12,11,11,11,17,10,16,9,0,13,17,16],
[14,7,11,11,10,15,13,19,9,12,0,11,19],
[13,13,11,18,10,15,14,14,11,8,14,0,14],
[11,9,10,13,5,10,12,12,8,9,6,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 93, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,16,15,13,18,14,18,14,17,18,12,13],
[8,0,9,5,7,10,14,10,10,10,11,12,6],
[9,16,0,15,10,10,14,12,14,12,21,11,12],
[10,20,10,0,15,13,11,14,6,11,15,13,9],
[12,18,15,10,0,17,17,14,12,18,18,20,9],
[7,15,15,12,8,0,10,14,12,11,20,13,15],
[11,11,11,14,8,15,0,17,13,17,17,8,11],
[7,15,13,11,11,11,8,0,8,13,15,9,12],
[11,15,11,19,13,13,12,17,0,12,16,11,13],
[8,15,13,14,7,14,8,12,13,0,15,11,8],
[7,14,4,10,7,5,8,10,9,10,0,6,6],
[13,13,14,12,5,12,17,16,14,14,19,0,11],
[12,19,13,16,16,10,14,13,12,17,19,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 94, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,19,8,13,7,10,15,13,10,13,19,13],
[15,0,17,17,21,17,16,20,17,19,12,22,19],
[6,8,0,3,7,5,5,10,7,3,5,10,8],
[17,8,22,0,22,13,18,13,24,16,8,24,13],
[12,4,18,3,0,6,10,11,17,11,9,20,14],
[18,8,20,12,19,0,19,16,19,17,14,25,19],
[15,9,20,7,15,6,0,15,12,9,10,20,15],
[10,5,15,12,14,9,10,0,17,8,9,15,12],
[12,8,18,1,8,6,13,8,0,11,6,18,6],
[15,6,22,9,14,8,16,17,14,0,12,22,20],
[12,13,20,17,16,11,15,16,19,13,0,19,18],
[6,3,15,1,5,0,5,10,7,3,6,0,11],
[12,6,17,12,11,6,10,13,19,5,7,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 95, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,7,16,5,7,4,19,14,7,14,8,3],
[15,0,7,15,9,2,2,17,6,11,8,5,2],
[18,18,0,18,9,8,13,19,11,18,8,11,11],
[9,10,7,0,13,10,7,22,9,7,12,9,9],
[20,16,16,12,0,11,9,19,12,15,20,5,12],
[18,23,17,15,14,0,11,18,16,16,20,16,16],
[21,23,12,18,16,14,0,23,16,10,12,8,8],
[6,8,6,3,6,7,2,0,12,4,10,7,4],
[11,19,14,16,13,9,9,13,0,15,16,11,10],
[18,14,7,18,10,9,15,21,10,0,12,11,8],
[11,17,17,13,5,5,13,15,9,13,0,9,4],
[17,20,14,16,20,9,17,18,14,14,16,0,14],
[22,23,14,16,13,9,17,21,15,17,21,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 96, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,11,14,12,11,15,18,13,14,18,12,15],
[17,0,15,12,14,12,14,17,14,10,14,15,16],
[14,10,0,13,16,11,16,18,15,11,16,11,18],
[11,13,12,0,12,10,17,17,14,11,13,12,17],
[13,11,9,13,0,10,18,16,13,10,15,10,16],
[14,13,14,15,15,0,15,16,10,12,15,9,13],
[10,11,9,8,7,10,0,11,10,7,10,8,15],
[7,8,7,8,9,9,14,0,11,7,12,7,12],
[12,11,10,11,12,15,15,14,0,11,11,8,13],
[11,15,14,14,15,13,18,18,14,0,14,15,20],
[7,11,9,12,10,10,15,13,14,11,0,10,12],
[13,10,14,13,15,16,17,18,17,10,15,0,16],
[10,9,7,8,9,12,10,13,12,5,13,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 97, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,9,15,15,13,8,10,10,11,10,13,14],
[17,0,11,20,16,17,14,17,17,15,13,19,18],
[16,14,0,17,14,16,11,12,15,15,12,15,14],
[10,5,8,0,13,10,7,12,14,12,8,13,10],
[10,9,11,12,0,13,6,10,11,13,9,11,13],
[12,8,9,15,12,0,10,8,9,11,11,13,11],
[17,11,14,18,19,15,0,12,14,15,10,17,12],
[15,8,13,13,15,17,13,0,17,11,9,13,15],
[15,8,10,11,14,16,11,8,0,10,9,12,14],
[14,10,10,13,12,14,10,14,15,0,10,11,15],
[15,12,13,17,16,14,15,16,16,15,0,15,17],
[12,6,10,12,14,12,8,12,13,14,10,0,13],
[11,7,11,15,12,14,13,10,11,10,8,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 98, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,12,9,15,14,8,2,11,10,11,12,13],
[18,0,14,11,17,19,11,9,15,9,16,10,12],
[13,11,0,9,16,10,8,9,13,6,11,14,8],
[16,14,16,0,15,14,11,8,11,11,14,13,12],
[10,8,9,10,0,10,3,10,10,8,12,6,8],
[11,6,15,11,15,0,9,8,10,6,12,11,8],
[17,14,17,14,22,16,0,17,16,16,15,13,11],
[23,16,16,17,15,17,8,0,10,13,15,13,13],
[14,10,12,14,15,15,9,15,0,7,13,10,9],
[15,16,19,14,17,19,9,12,18,0,17,13,10],
[14,9,14,11,13,13,10,10,12,8,0,12,9],
[13,15,11,12,19,14,12,12,15,12,13,0,11],
[12,13,17,13,17,17,14,12,16,15,16,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 99, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,20,11,15,14,14,15,19,17,16,15,15],
[11,0,13,9,13,9,15,13,12,12,12,14,15],
[5,12,0,6,13,7,14,7,11,13,12,10,11],
[14,16,19,0,13,15,17,12,14,17,18,15,18],
[10,12,12,12,0,12,14,11,13,13,15,14,14],
[11,16,18,10,13,0,19,12,12,14,18,14,15],
[11,10,11,8,11,6,0,9,11,12,13,10,12],
[10,12,18,13,14,13,16,0,13,11,14,16,14],
[6,13,14,11,12,13,14,12,0,16,14,14,15],
[8,13,12,8,12,11,13,14,9,0,18,11,15],
[9,13,13,7,10,7,12,11,11,7,0,9,12],
[10,11,15,10,11,11,15,9,11,14,16,0,17],
[10,10,14,7,11,10,13,11,10,10,13,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 100, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,16,16,18,16,13,19,16,14,12,16,18],
[8,0,12,8,12,9,12,14,14,8,10,10,12],
[9,13,0,13,14,17,10,13,14,11,16,14,13],
[9,17,12,0,19,15,13,14,16,15,13,14,14],
[7,13,11,6,0,11,10,12,8,12,12,11,12],
[9,16,8,10,14,0,10,13,13,14,14,14,15],
[12,13,15,12,15,15,0,15,18,13,13,13,14],
[6,11,12,11,13,12,10,0,15,13,13,10,13],
[9,11,11,9,17,12,7,10,0,11,11,10,18],
[11,17,14,10,13,11,12,12,14,0,13,14,17],
[13,15,9,12,13,11,12,12,14,12,0,14,12],
[9,15,11,11,14,11,12,15,15,11,11,0,11],
[7,13,12,11,13,10,11,12,7,8,13,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 101, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,11,15,7,10,12,10,13,13,12,9,7],
[16,0,13,15,11,16,12,9,12,16,13,9,8],
[14,12,0,17,12,14,15,16,13,15,13,8,13],
[10,10,8,0,12,9,9,5,10,12,8,9,9],
[18,14,13,13,0,16,16,15,15,16,13,14,10],
[15,9,11,16,9,0,9,13,11,15,7,6,6],
[13,13,10,16,9,16,0,8,12,11,12,8,7],
[15,16,9,20,10,12,17,0,17,14,14,12,7],
[12,13,12,15,10,14,13,8,0,13,16,11,13],
[12,9,10,13,9,10,14,11,12,0,10,11,4],
[13,12,12,17,12,18,13,11,9,15,0,13,12],
[16,16,17,16,11,19,17,13,14,14,12,0,10],
[18,17,12,16,15,19,18,18,12,21,13,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 102, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,9,11,8,12,12,11,11,9,12,8,10],
[18,0,12,12,10,16,12,13,12,13,15,12,12],
[16,13,0,16,14,14,14,14,14,14,13,10,12],
[14,13,9,0,15,11,12,14,9,12,14,12,10],
[17,15,11,10,0,15,13,14,12,15,15,13,14],
[13,9,11,14,10,0,16,13,13,11,11,11,10],
[13,13,11,13,12,9,0,14,13,11,11,11,11],
[14,12,11,11,11,12,11,0,8,10,13,10,12],
[14,13,11,16,13,12,12,17,0,13,10,13,15],
[16,12,11,13,10,14,14,15,12,0,16,11,15],
[13,10,12,11,10,14,14,12,15,9,0,11,11],
[17,13,15,13,12,14,14,15,12,14,14,0,14],
[15,13,13,15,11,15,14,13,10,10,14,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 103, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,10,10,9,13,8,12,9,6,12,9,11],
[11,0,14,9,8,10,11,10,8,10,11,10,12],
[15,11,0,11,12,14,17,13,12,10,14,11,14],
[15,16,14,0,13,17,15,17,12,11,16,10,12],
[16,17,13,12,0,19,13,16,13,10,17,14,13],
[12,15,11,8,6,0,13,11,10,10,12,11,12],
[17,14,8,10,12,12,0,11,11,12,12,7,10],
[13,15,12,8,9,14,14,0,10,12,13,13,12],
[16,17,13,13,12,15,14,15,0,9,14,11,15],
[19,15,15,14,15,15,13,13,16,0,14,12,13],
[13,14,11,9,8,13,13,12,11,11,0,14,11],
[16,15,14,15,11,14,18,12,14,13,11,0,13],
[14,13,11,13,12,13,15,13,10,12,14,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 104, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,7,22,13,9,18,7,14,12,12,7,10],
[4,0,9,16,11,11,12,6,11,12,8,8,11],
[18,16,0,19,16,13,15,13,15,21,11,17,10],
[3,9,6,0,8,7,15,5,10,12,7,4,10],
[12,14,9,17,0,13,13,4,19,11,8,14,13],
[16,14,12,18,12,0,16,10,18,12,14,8,7],
[7,13,10,10,12,9,0,10,11,8,13,7,10],
[18,19,12,20,21,15,15,0,16,15,9,15,14],
[11,14,10,15,6,7,14,9,0,12,10,7,2],
[13,13,4,13,14,13,17,10,13,0,12,11,10],
[13,17,14,18,17,11,12,16,15,13,0,14,13],
[18,17,8,21,11,17,18,10,18,14,11,0,10],
[15,14,15,15,12,18,15,11,23,15,12,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 105, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,11,7,17,13,7,11,13,14,7,17,4],
[11,0,12,15,15,15,10,11,10,14,5,16,11],
[14,13,0,11,16,14,15,15,9,14,7,16,8],
[18,10,14,0,12,13,15,13,12,15,15,19,8],
[8,10,9,13,0,15,13,15,10,14,5,13,8],
[12,10,11,12,10,0,13,7,15,9,9,13,11],
[18,15,10,10,12,12,0,11,16,11,10,13,14],
[14,14,10,12,10,18,14,0,18,10,13,15,14],
[12,15,16,13,15,10,9,7,0,16,9,14,11],
[11,11,11,10,11,16,14,15,9,0,11,17,10],
[18,20,18,10,20,16,15,12,16,14,0,20,18],
[8,9,9,6,12,12,12,10,11,8,5,0,4],
[21,14,17,17,17,14,11,11,14,15,7,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 106, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,10,13,10,13,11,15,17,14,13,12,14],
[18,0,16,14,15,15,12,16,17,16,13,12,12],
[15,9,0,11,12,12,13,15,17,13,14,13,14],
[12,11,14,0,13,14,11,15,15,13,9,11,12],
[15,10,13,12,0,13,11,15,18,12,15,11,9],
[12,10,13,11,12,0,13,13,15,9,9,10,13],
[14,13,12,14,14,12,0,18,21,17,13,11,15],
[10,9,10,10,10,12,7,0,13,10,11,9,14],
[8,8,8,10,7,10,4,12,0,10,11,9,10],
[11,9,12,12,13,16,8,15,15,0,13,12,14],
[12,12,11,16,10,16,12,14,14,12,0,12,12],
[13,13,12,14,14,15,14,16,16,13,13,0,19],
[11,13,11,13,16,12,10,11,15,11,13,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 107, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,11,14,13,12,13,14,15,11,15,12,16],
[11,0,11,16,12,12,12,10,14,13,14,12,14],
[14,14,0,17,13,14,13,12,17,15,15,12,18],
[11,9,8,0,10,13,9,5,9,9,9,9,14],
[12,13,12,15,0,15,12,13,15,12,14,15,19],
[13,13,11,12,10,0,11,10,14,11,14,12,14],
[12,13,12,16,13,14,0,11,15,15,15,12,16],
[11,15,13,20,12,15,14,0,15,12,15,11,18],
[10,11,8,16,10,11,10,10,0,12,13,9,12],
[14,12,10,16,13,14,10,13,13,0,16,12,14],
[10,11,10,16,11,11,10,10,12,9,0,7,13],
[13,13,13,16,10,13,13,14,16,13,18,0,15],
[9,11,7,11,6,11,9,7,13,11,12,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 108, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,12,16,9,14,10,14,13,9,10,17,7],
[18,0,15,15,12,19,11,14,16,10,14,19,12],
[13,10,0,9,9,17,15,14,13,9,12,13,11],
[9,10,16,0,8,18,15,14,13,8,10,16,10],
[16,13,16,17,0,23,15,17,19,11,15,20,15],
[11,6,8,7,2,0,9,9,10,5,10,12,9],
[15,14,10,10,10,16,0,14,14,12,10,17,13],
[11,11,11,11,8,16,11,0,11,7,7,12,5],
[12,9,12,12,6,15,11,14,0,7,13,11,14],
[16,15,16,17,14,20,13,18,18,0,16,16,12],
[15,11,13,15,10,15,15,18,12,9,0,16,14],
[8,6,12,9,5,13,8,13,14,9,9,0,6],
[18,13,14,15,10,16,12,20,11,13,11,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 109, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,14,17,8,10,11,12,11,14,11,16,15],
[7,0,11,16,9,9,8,10,9,10,9,13,13],
[11,14,0,17,12,14,15,9,12,14,11,17,10],
[8,9,8,0,9,11,8,4,12,7,13,12,14],
[17,16,13,16,0,8,14,10,9,16,13,16,16],
[15,16,11,14,17,0,13,7,15,13,16,10,15],
[14,17,10,17,11,12,0,10,15,9,13,14,19],
[13,15,16,21,15,18,15,0,15,12,16,19,15],
[14,16,13,13,16,10,10,10,0,13,16,15,14],
[11,15,11,18,9,12,16,13,12,0,11,13,16],
[14,16,14,12,12,9,12,9,9,14,0,15,14],
[9,12,8,13,9,15,11,6,10,12,10,0,13],
[10,12,15,11,9,10,6,10,11,9,11,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 110, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,22,21,13,7,19,21,18,17,8,18,21],
[8,0,12,8,7,7,22,21,14,18,8,21,4],
[3,13,0,7,13,7,22,14,11,13,4,18,14],
[4,17,18,0,13,7,18,21,14,18,4,21,14],
[12,18,12,12,0,11,22,21,18,18,15,21,21],
[18,18,18,18,14,0,18,18,18,18,4,18,18],
[6,3,3,7,3,7,0,17,13,16,7,21,7],
[4,4,11,4,4,7,8,0,14,7,4,18,7],
[7,11,14,11,7,7,12,11,0,11,8,22,8],
[8,7,12,7,7,7,9,18,14,0,8,22,4],
[17,17,21,21,10,21,18,21,17,17,0,20,17],
[7,4,7,4,4,7,4,7,3,3,5,0,4],
[4,21,11,11,4,7,18,18,17,21,8,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 111, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,13,11,12,13,13,10,14,13,10,13,11],
[11,0,15,16,13,13,11,13,16,14,12,18,13],
[12,10,0,15,14,13,11,11,16,11,11,15,16],
[14,9,10,0,13,12,14,7,13,13,12,16,13],
[13,12,11,12,0,16,18,9,18,17,14,16,9],
[12,12,12,13,9,0,13,9,16,14,13,14,14],
[12,14,14,11,7,12,0,12,18,8,15,14,12],
[15,12,14,18,16,16,13,0,16,12,13,17,14],
[11,9,9,12,7,9,7,9,0,6,11,9,11],
[12,11,14,12,8,11,17,13,19,0,15,19,11],
[15,13,14,13,11,12,10,12,14,10,0,15,17],
[12,7,10,9,9,11,11,8,16,6,10,0,14],
[14,12,9,12,16,11,13,11,14,14,8,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 112, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,8,14,12,13,10,10,11,10,10,15,16],
[10,0,14,15,10,13,9,12,8,9,16,14,18],
[17,11,0,14,14,13,14,15,11,12,12,11,18],
[11,10,11,0,11,16,15,16,12,7,17,18,22],
[13,15,11,14,0,11,13,10,12,5,13,14,19],
[12,12,12,9,14,0,17,13,13,8,14,15,19],
[15,16,11,10,12,8,0,12,11,6,13,13,18],
[15,13,10,9,15,12,13,0,10,10,11,13,17],
[14,17,14,13,13,12,14,15,0,13,14,14,15],
[15,16,13,18,20,17,19,15,12,0,18,16,22],
[15,9,13,8,12,11,12,14,11,7,0,13,15],
[10,11,14,7,11,10,12,12,11,9,12,0,15],
[9,7,7,3,6,6,7,8,10,3,10,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 113, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,14,15,10,17,13,13,12,18,13,13,13],
[15,0,10,11,3,10,7,8,8,8,15,9,10],
[11,15,0,8,5,12,6,7,4,11,11,5,6],
[10,14,17,0,14,12,10,10,10,10,7,17,12],
[15,22,20,11,0,18,12,11,10,13,15,17,13],
[8,15,13,13,7,0,13,13,8,17,15,10,7],
[12,18,19,15,13,12,0,14,9,10,12,19,9],
[12,17,18,15,14,12,11,0,9,15,11,15,10],
[13,17,21,15,15,17,16,16,0,13,13,12,19],
[7,17,14,15,12,8,15,10,12,0,14,14,7],
[12,10,14,18,10,10,13,14,12,11,0,15,10],
[12,16,20,8,8,15,6,10,13,11,10,0,13],
[12,15,19,13,12,18,16,15,6,18,15,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 114, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,15,11,14,13,8,10,18,12,10,12,13],
[17,0,16,12,19,17,19,15,24,20,18,17,20],
[10,9,0,9,11,12,5,12,14,11,11,9,14],
[14,13,16,0,19,12,13,11,18,17,17,16,18],
[11,6,14,6,0,12,16,10,16,15,16,13,16],
[12,8,13,13,13,0,10,13,20,13,14,12,16],
[17,6,20,12,9,15,0,10,22,15,20,19,17],
[15,10,13,14,15,12,15,0,19,14,18,17,13],
[7,1,11,7,9,5,3,6,0,10,8,10,10],
[13,5,14,8,10,12,10,11,15,0,16,15,17],
[15,7,14,8,9,11,5,7,17,9,0,13,10],
[13,8,16,9,12,13,6,8,15,10,12,0,15],
[12,5,11,7,9,9,8,12,15,8,15,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 115, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,19,19,22,18,22,20,16,16,12,14,18],
[10,0,14,19,20,19,19,14,15,10,15,8,13],
[6,11,0,10,16,13,19,16,6,9,11,14,10],
[6,6,15,0,18,14,11,14,10,10,7,5,13],
[3,5,9,7,0,7,17,9,10,4,8,5,3],
[7,6,12,11,18,0,13,14,12,5,9,8,8],
[3,6,6,14,8,12,0,14,11,3,9,10,3],
[5,11,9,11,16,11,11,0,12,6,7,8,5],
[9,10,19,15,15,13,14,13,0,12,7,11,16],
[9,15,16,15,21,20,22,19,13,0,9,17,13],
[13,10,14,18,17,16,16,18,18,16,0,14,16],
[11,17,11,20,20,17,15,17,14,8,11,0,11],
[7,12,15,12,22,17,22,20,9,12,9,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 116, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,19,13,9,10,12,9,13,13,13,11],
[12,0,13,19,16,13,13,16,11,15,15,15,14],
[12,12,0,16,12,10,9,15,13,12,17,13,15],
[6,6,9,0,11,8,7,7,10,8,8,11,8],
[12,9,13,14,0,7,11,13,13,9,12,12,13],
[16,12,15,17,18,0,13,16,9,15,16,13,16],
[15,12,16,18,14,12,0,15,13,14,16,14,17],
[13,9,10,18,12,9,10,0,10,13,13,11,13],
[16,14,12,15,12,16,12,15,0,13,14,16,12],
[12,10,13,17,16,10,11,12,12,0,15,13,16],
[12,10,8,17,13,9,9,12,11,10,0,9,8],
[12,10,12,14,13,12,11,14,9,12,16,0,13],
[14,11,10,17,12,9,8,12,13,9,17,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 117, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,5,6,13,17,11,5,11,12,8,8,9],
[15,0,12,13,18,20,16,12,9,15,13,18,16],
[20,13,0,13,12,20,19,10,14,19,16,14,17],
[19,12,12,0,15,19,18,11,13,18,15,9,15],
[12,7,13,10,0,11,19,13,8,14,10,12,16],
[8,5,5,6,14,0,13,8,11,14,6,11,16],
[14,9,6,7,6,12,0,6,11,9,10,9,8],
[20,13,15,14,12,17,19,0,8,16,12,18,19],
[14,16,11,12,17,14,14,17,0,11,11,13,17],
[13,10,6,7,11,11,16,9,14,0,10,12,13],
[17,12,9,10,15,19,15,13,14,15,0,13,13],
[17,7,11,16,13,14,16,7,12,13,12,0,13],
[16,9,8,10,9,9,17,6,8,12,12,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 118, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,6,13,13,6,14,14,14,11,10,13,11],
[11,0,11,15,13,8,16,14,6,11,11,12,13],
[19,14,0,13,15,8,13,11,11,11,11,13,16],
[12,10,12,0,10,9,11,11,11,11,6,14,10],
[12,12,10,15,0,12,12,10,10,10,9,14,11],
[19,17,17,16,13,0,16,14,12,12,11,14,12],
[11,9,12,14,13,9,0,15,6,9,9,12,11],
[11,11,14,14,15,11,10,0,9,12,6,14,11],
[11,19,14,14,15,13,19,16,0,12,10,15,11],
[14,14,14,14,15,13,16,13,13,0,10,11,11],
[15,14,14,19,16,14,16,19,15,15,0,14,12],
[12,13,12,11,11,11,13,11,10,14,11,0,18],
[14,12,9,15,14,13,14,14,14,14,13,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 119, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,11,10,10,17,11,14,8,8,5,16,13],
[12,0,10,7,3,14,8,11,2,9,1,10,11],
[14,15,0,16,9,14,9,17,9,12,1,16,15],
[15,18,9,0,6,18,15,15,9,11,7,12,11],
[15,22,16,19,0,16,13,16,16,15,13,14,12],
[8,11,11,7,9,0,5,13,6,10,3,12,8],
[14,17,16,10,12,20,0,14,12,13,9,10,13],
[11,14,8,10,9,12,11,0,12,13,4,17,11],
[17,23,16,16,9,19,13,13,0,14,8,15,11],
[17,16,13,14,10,15,12,12,11,0,8,15,9],
[20,24,24,18,12,22,16,21,17,17,0,18,16],
[9,15,9,13,11,13,15,8,10,10,7,0,8],
[12,14,10,14,13,17,12,14,14,16,9,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 120, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,7,12,16,13,11,9,12,8,9,11,6],
[11,0,8,7,19,9,6,11,10,6,4,3,9],
[18,17,0,14,20,19,15,11,13,9,11,13,10],
[13,18,11,0,22,11,10,12,6,11,12,15,9],
[9,6,5,3,0,8,4,3,4,7,7,6,3],
[12,16,6,14,17,0,16,12,14,9,11,11,14],
[14,19,10,15,21,9,0,13,15,10,10,12,12],
[16,14,14,13,22,13,12,0,13,10,16,12,14],
[13,15,12,19,21,11,10,12,0,12,9,13,12],
[17,19,16,14,18,16,15,15,13,0,11,13,13],
[16,21,14,13,18,14,15,9,16,14,0,17,15],
[14,22,12,10,19,14,13,13,12,12,8,0,13],
[19,16,15,16,22,11,13,11,13,12,10,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 121, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,14,11,12,13,16,15,10,13,15,14,13],
[12,0,10,13,12,8,9,11,11,10,9,9,7],
[11,15,0,11,15,10,16,11,14,11,11,16,12],
[14,12,14,0,11,11,13,13,13,11,13,18,16],
[13,13,10,14,0,7,13,12,11,8,10,16,9],
[12,17,15,14,18,0,16,12,15,15,15,17,13],
[9,16,9,12,12,9,0,9,11,9,9,14,9],
[10,14,14,12,13,13,16,0,13,9,17,17,13],
[15,14,11,12,14,10,14,12,0,12,13,13,11],
[12,15,14,14,17,10,16,16,13,0,13,16,15],
[10,16,14,12,15,10,16,8,12,12,0,13,10],
[11,16,9,7,9,8,11,8,12,9,12,0,11],
[12,18,13,9,16,12,16,12,14,10,15,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 122, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,11,11,12,11,6,8,11,11,6,10,11],
[21,0,11,8,9,12,6,14,14,11,13,22,11],
[14,14,0,9,16,10,13,14,19,16,9,14,16],
[14,17,16,0,15,20,17,14,19,19,12,14,18],
[13,16,9,10,0,11,17,12,19,18,11,15,23],
[14,13,15,5,14,0,13,11,18,21,10,13,18],
[19,19,12,8,8,12,0,20,15,12,14,22,11],
[17,11,11,11,13,14,5,0,18,13,6,14,11],
[14,11,6,6,6,7,10,7,0,6,6,8,6],
[14,14,9,6,7,4,13,12,19,0,11,15,12],
[19,12,16,13,14,15,11,19,19,14,0,21,14],
[15,3,11,11,10,12,3,11,17,10,4,0,10],
[14,14,9,7,2,7,14,14,19,13,11,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 123, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,19,12,9,10,11,14,4,22,11,18,12],
[17,0,24,14,18,14,13,16,12,22,8,22,21],
[6,1,0,12,9,10,3,1,6,19,5,15,15],
[13,11,13,0,13,6,11,7,11,15,15,14,19],
[16,7,16,12,0,13,7,17,9,15,11,21,16],
[15,11,15,19,12,0,11,14,14,15,15,17,16],
[14,12,22,14,18,14,0,18,10,18,7,22,21],
[11,9,24,18,8,11,7,0,12,18,12,22,14],
[21,13,19,14,16,11,15,13,0,18,15,19,21],
[3,3,6,10,10,10,7,7,7,0,6,20,10],
[14,17,20,10,14,10,18,13,10,19,0,20,17],
[7,3,10,11,4,8,3,3,6,5,5,0,14],
[13,4,10,6,9,9,4,11,4,15,8,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 124, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,12,12,15,20,18,11,16,12,11,12,16],
[11,0,9,10,16,16,19,11,8,13,13,10,16],
[13,16,0,13,20,21,19,13,15,12,10,14,18],
[13,15,12,0,12,16,16,15,16,9,10,15,14],
[10,9,5,13,0,13,16,10,10,10,7,8,11],
[5,9,4,9,12,0,16,8,10,7,8,6,12],
[7,6,6,9,9,9,0,9,5,9,7,5,13],
[14,14,12,10,15,17,16,0,14,14,16,10,21],
[9,17,10,9,15,15,20,11,0,13,11,11,15],
[13,12,13,16,15,18,16,11,12,0,10,10,16],
[14,12,15,15,18,17,18,9,14,15,0,10,19],
[13,15,11,10,17,19,20,15,14,15,15,0,17],
[9,9,7,11,14,13,12,4,10,9,6,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 125, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,13,9,12,12,19,12,8,13,14,13,8],
[17,0,15,11,12,15,17,14,14,17,11,17,17],
[12,10,0,10,17,15,18,15,11,12,15,16,16],
[16,14,15,0,12,15,13,12,12,14,13,18,15],
[13,13,8,13,0,15,20,13,13,18,16,18,13],
[13,10,10,10,10,0,16,8,12,15,10,14,12],
[6,8,7,12,5,9,0,7,10,11,9,14,7],
[13,11,10,13,12,17,18,0,10,16,7,15,16],
[17,11,14,13,12,13,15,15,0,12,14,13,12],
[12,8,13,11,7,10,14,9,13,0,9,18,13],
[11,14,10,12,9,15,16,18,11,16,0,14,13],
[12,8,9,7,7,11,11,10,12,7,11,0,7],
[17,8,9,10,12,13,18,9,13,12,12,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 126, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,11,16,10,16,15,18,18,16,13,16,16],
[9,0,9,16,9,14,19,21,10,14,8,6,15],
[14,16,0,20,17,17,19,23,19,15,14,11,18],
[9,9,5,0,12,15,9,18,8,17,3,7,11],
[15,16,8,13,0,14,16,16,17,17,12,16,14],
[9,11,8,10,11,0,9,15,12,14,5,7,15],
[10,6,6,16,9,16,0,21,9,14,6,8,14],
[7,4,2,7,9,10,4,0,7,12,3,8,4],
[7,15,6,17,8,13,16,18,0,11,12,13,16],
[9,11,10,8,8,11,11,13,14,0,7,12,8],
[12,17,11,22,13,20,19,22,13,18,0,20,22],
[9,19,14,18,9,18,17,17,12,13,5,0,19],
[9,10,7,14,11,10,11,21,9,17,3,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 127, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,16,17,9,16,16,17,25,8,17,17,8],
[8,0,16,0,0,8,8,9,17,8,0,25,0],
[9,9,0,9,9,8,17,9,17,8,9,9,9],
[8,25,16,0,8,8,8,25,17,8,17,25,16],
[16,25,16,17,0,16,16,25,25,8,17,25,16],
[9,17,17,17,9,0,17,17,17,17,17,17,17],
[9,17,8,17,9,8,0,17,25,8,9,17,17],
[8,16,16,0,0,8,8,0,17,8,0,25,16],
[0,8,8,8,0,8,0,8,0,8,0,8,8],
[17,17,17,17,17,8,17,17,17,0,17,17,17],
[8,25,16,8,8,8,16,25,25,8,0,25,16],
[8,0,16,0,0,8,8,0,17,8,0,0,0],
[17,25,16,9,9,8,8,9,17,8,9,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 128, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,11,16,12,16,15,12,16,15,11,10,14],
[11,0,6,14,5,12,10,9,10,6,6,7,6],
[14,19,0,17,9,15,13,17,16,17,11,13,12],
[9,11,8,0,10,17,13,11,17,14,13,12,9],
[13,20,16,15,0,14,18,14,12,19,15,7,15],
[9,13,10,8,11,0,15,10,8,14,7,11,11],
[10,15,12,12,7,10,0,16,10,14,5,11,9],
[13,16,8,14,11,15,9,0,13,13,8,10,8],
[9,15,9,8,13,17,15,12,0,18,10,8,7],
[10,19,8,11,6,11,11,12,7,0,4,7,9],
[14,19,14,12,10,18,20,17,15,21,0,10,17],
[15,18,12,13,18,14,14,15,17,18,15,0,13],
[11,19,13,16,10,14,16,17,18,16,8,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 129, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,15,15,15,15,12,16,13,14,13,13,13],
[12,0,14,15,12,8,8,20,10,14,12,11,10],
[10,11,0,16,12,12,9,15,7,10,11,8,12],
[10,10,9,0,14,12,9,13,7,9,9,10,8],
[10,13,13,11,0,13,10,18,9,10,12,10,10],
[10,17,13,13,12,0,12,18,13,16,14,13,15],
[13,17,16,16,15,13,0,19,13,14,17,15,11],
[9,5,10,12,7,7,6,0,6,8,8,7,6],
[12,15,18,18,16,12,12,19,0,16,13,13,15],
[11,11,15,16,15,9,11,17,9,0,17,12,11],
[12,13,14,16,13,11,8,17,12,8,0,10,10],
[12,14,17,15,15,12,10,18,12,13,15,0,14],
[12,15,13,17,15,10,14,19,10,14,15,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 130, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,13,11,11,9,9,10,9,17,13,14,10],
[11,0,11,11,9,10,10,10,10,11,9,13,9],
[12,14,0,10,10,7,12,13,9,12,12,14,10],
[14,14,15,0,11,9,12,9,13,19,12,17,11],
[14,16,15,14,0,11,15,12,14,17,15,19,13],
[16,15,18,16,14,0,14,9,14,18,12,16,13],
[16,15,13,13,10,11,0,13,14,15,13,17,12],
[15,15,12,16,13,16,12,0,17,18,15,17,14],
[16,15,16,12,11,11,11,8,0,20,12,14,13],
[8,14,13,6,8,7,10,7,5,0,7,11,7],
[12,16,13,13,10,13,12,10,13,18,0,13,12],
[11,12,11,8,6,9,8,8,11,14,12,0,8],
[15,16,15,14,12,12,13,11,12,18,13,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 131, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,15,17,12,19,14,16,17,19,12,17,12],
[10,0,14,11,11,9,11,9,17,13,13,13,8],
[10,11,0,8,10,12,10,8,14,13,14,9,11],
[8,14,17,0,14,14,17,12,15,17,14,16,14],
[13,14,15,11,0,16,14,11,18,12,16,14,12],
[6,16,13,11,9,0,15,11,12,14,13,16,10],
[11,14,15,8,11,10,0,11,14,11,9,11,13],
[9,16,17,13,14,14,14,0,18,15,16,14,11],
[8,8,11,10,7,13,11,7,0,11,11,9,6],
[6,12,12,8,13,11,14,10,14,0,14,12,8],
[13,12,11,11,9,12,16,9,14,11,0,11,10],
[8,12,16,9,11,9,14,11,16,13,14,0,11],
[13,17,14,11,13,15,12,14,19,17,15,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 132, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,18,18,18,18,10,18,17,18,9,18,10],
[7,0,10,17,9,0,9,17,0,24,9,17,9],
[7,15,0,17,17,8,9,17,8,24,9,17,9],
[7,8,8,0,9,0,0,18,0,15,9,7,9],
[7,16,8,16,0,9,0,18,0,15,0,16,0],
[7,25,17,25,16,0,16,18,7,24,9,24,9],
[15,16,16,25,25,9,0,18,15,24,17,16,18],
[7,8,8,7,7,7,7,0,7,7,0,7,7],
[8,25,17,25,25,18,10,18,0,25,9,25,10],
[7,1,1,10,10,1,1,18,0,0,9,1,10],
[16,16,16,16,25,16,8,25,16,16,0,16,17],
[7,8,8,18,9,1,9,18,0,24,9,0,9],
[15,16,16,16,25,16,7,18,15,15,8,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 133, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,8,24,21,22,16,24,15,25,12,18,17],
[9,0,11,17,14,17,8,24,8,17,8,17,17],
[17,14,0,16,14,20,8,17,8,17,9,13,15],
[1,8,9,0,22,17,8,14,8,16,9,7,12],
[4,11,11,3,0,14,11,11,4,4,9,7,11],
[3,8,5,8,11,0,0,10,5,8,9,12,8],
[9,17,17,17,14,25,0,24,8,17,18,18,17],
[1,1,8,11,14,15,1,0,5,9,9,9,11],
[10,17,17,17,21,20,17,20,0,18,18,13,17],
[0,8,8,9,21,17,8,16,7,0,9,4,8],
[13,17,16,16,16,16,7,16,7,16,0,16,14],
[7,8,12,18,18,13,7,16,12,21,9,0,8],
[8,8,10,13,14,17,8,14,8,17,11,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 134, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,23,17,9,21,15,17,16,18,17,12,17],
[5,0,13,15,11,18,17,19,16,14,15,13,15],
[2,12,0,9,3,11,15,14,10,6,8,12,11],
[8,10,16,0,12,19,20,18,19,13,17,14,17],
[16,14,22,13,0,16,17,19,13,18,10,21,19],
[4,7,14,6,9,0,17,14,14,14,12,9,11],
[10,8,10,5,8,8,0,10,8,12,10,13,15],
[8,6,11,7,6,11,15,0,9,12,10,11,11],
[9,9,15,6,12,11,17,16,0,13,13,14,10],
[7,11,19,12,7,11,13,13,12,0,8,12,15],
[8,10,17,8,15,13,15,15,12,17,0,16,18],
[13,12,13,11,4,16,12,14,11,13,9,0,14],
[8,10,14,8,6,14,10,14,15,10,7,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 135, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,11,13,14,13,13,10,12,11,11,17,5],
[7,0,14,15,10,8,12,14,9,9,8,7,8],
[14,11,0,12,14,8,10,8,11,12,14,10,10],
[12,10,13,0,13,13,13,12,12,9,11,14,8],
[11,15,11,12,0,9,11,9,10,8,14,13,7],
[12,17,17,12,16,0,14,17,17,10,15,22,12],
[12,13,15,12,14,11,0,9,12,13,15,12,9],
[15,11,17,13,16,8,16,0,17,8,17,12,13],
[13,16,14,13,15,8,13,8,0,11,19,13,11],
[14,16,13,16,17,15,12,17,14,0,14,14,16],
[14,17,11,14,11,10,10,8,6,11,0,12,7],
[8,18,15,11,12,3,13,13,12,11,13,0,11],
[20,17,15,17,18,13,16,12,14,9,18,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 136, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,8,16,9,7,14,7,14,10,10,13,14],
[12,0,14,10,14,7,11,9,7,10,12,15,14],
[17,11,0,14,14,15,13,11,12,14,16,16,15],
[9,15,11,0,12,10,10,11,7,9,14,15,16],
[16,11,11,13,0,12,13,10,8,11,19,16,17],
[18,18,10,15,13,0,16,14,13,15,18,15,17],
[11,14,12,15,12,9,0,10,9,12,10,11,14],
[18,16,14,14,15,11,15,0,15,14,16,19,22],
[11,18,13,18,17,12,16,10,0,12,15,20,17],
[15,15,11,16,14,10,13,11,13,0,15,18,13],
[15,13,9,11,6,7,15,9,10,10,0,13,11],
[12,10,9,10,9,10,14,6,5,7,12,0,15],
[11,11,10,9,8,8,11,3,8,12,14,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 137, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,9,9,10,13,14,13,11,18,5,5,9],
[14,0,12,14,11,12,13,13,15,14,14,12,17],
[16,13,0,14,10,12,12,11,11,13,16,13,13],
[16,11,11,0,8,11,12,11,14,15,12,9,14],
[15,14,15,17,0,16,11,12,13,16,16,14,16],
[12,13,13,14,9,0,15,13,12,12,14,12,10],
[11,12,13,13,14,10,0,13,8,16,9,10,9],
[12,12,14,14,13,12,12,0,14,12,13,10,17],
[14,10,14,11,12,13,17,11,0,13,14,10,14],
[7,11,12,10,9,13,9,13,12,0,7,7,11],
[20,11,9,13,9,11,16,12,11,18,0,10,9],
[20,13,12,16,11,13,15,15,15,18,15,0,14],
[16,8,12,11,9,15,16,8,11,14,16,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 138, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,11,9,13,18,8,14,12,12,8,11,11],
[11,0,13,11,15,12,11,14,14,12,11,12,12],
[14,12,0,8,14,14,10,15,14,12,10,11,14],
[16,14,17,0,17,13,12,13,12,10,13,12,14],
[12,10,11,8,0,11,9,13,9,10,9,12,12],
[7,13,11,12,14,0,9,16,10,13,12,10,12],
[17,14,15,13,16,16,0,16,10,13,10,10,14],
[11,11,10,12,12,9,9,0,11,12,11,8,13],
[13,11,11,13,16,15,15,14,0,12,9,10,12],
[13,13,13,15,15,12,12,13,13,0,11,11,12],
[17,14,15,12,16,13,15,14,16,14,0,13,15],
[14,13,14,13,13,15,15,17,15,14,12,0,15],
[14,13,11,11,13,13,11,12,13,13,10,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 139, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,16,13,13,13,13,10,15,13,10,13],
[12,0,6,10,10,1,14,17,14,22,1,10,14],
[12,19,0,16,16,7,20,23,20,18,7,16,16],
[9,15,9,0,13,4,17,17,14,15,4,10,13],
[12,15,9,12,0,5,13,18,16,24,10,7,7],
[12,24,18,21,20,0,22,24,21,24,20,18,22],
[12,11,5,8,12,3,0,18,13,20,3,11,3],
[12,8,2,8,7,1,7,0,10,18,1,7,0],
[15,11,5,11,9,4,12,15,0,11,3,9,9],
[10,3,7,10,1,1,5,7,14,0,4,1,4],
[12,24,18,21,15,5,22,24,22,21,0,22,19],
[15,15,9,15,18,7,14,18,16,24,3,0,7],
[12,11,9,12,18,3,22,25,16,21,6,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 140, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,5,13,18,9,6,6,8,8,15,15,18],
[8,0,9,9,6,5,2,7,1,3,13,11,11],
[20,16,0,17,19,19,13,18,11,11,13,15,25],
[12,16,8,0,12,11,4,11,5,7,9,12,21],
[7,19,6,13,0,9,6,9,8,7,15,15,14],
[16,20,6,14,16,0,5,8,11,7,16,16,15],
[19,23,12,21,19,20,0,15,15,7,18,18,18],
[19,18,7,14,16,17,10,0,15,6,20,19,18],
[17,24,14,20,17,14,10,10,0,13,19,17,20],
[17,22,14,18,18,18,18,19,12,0,20,17,23],
[10,12,12,16,10,9,7,5,6,5,0,16,16],
[10,14,10,13,10,9,7,6,8,8,9,0,13],
[7,14,0,4,11,10,7,7,5,2,9,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 141, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,12,15,17,17,14,16,13,14,16,15,15],
[7,0,12,13,9,14,14,12,13,10,15,15,12],
[13,13,0,15,12,15,15,14,16,14,17,17,16],
[10,12,10,0,13,14,15,11,15,10,13,18,11],
[8,16,13,12,0,14,15,11,14,13,16,15,11],
[8,11,10,11,11,0,14,6,13,13,14,12,13],
[11,11,10,10,10,11,0,8,11,12,14,12,14],
[9,13,11,14,14,19,17,0,16,12,12,17,14],
[12,12,9,10,11,12,14,9,0,15,13,12,9],
[11,15,11,15,12,12,13,13,10,0,18,14,12],
[9,10,8,12,9,11,11,13,12,7,0,17,14],
[10,10,8,7,10,13,13,8,13,11,8,0,8],
[10,13,9,14,14,12,11,11,16,13,11,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 142, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,11,11,10,11,7,8,8,12,13,10,12],
[13,0,11,10,8,11,8,9,11,10,11,14,13],
[14,14,0,12,12,10,8,8,8,11,11,9,14],
[14,15,13,0,11,15,12,9,12,15,17,14,14],
[15,17,13,14,0,16,13,14,12,16,17,13,15],
[14,14,15,10,9,0,11,13,12,15,15,15,14],
[18,17,17,13,12,14,0,17,11,17,18,17,14],
[17,16,17,16,11,12,8,0,13,17,17,16,17],
[17,14,17,13,13,13,14,12,0,15,16,15,12],
[13,15,14,10,9,10,8,8,10,0,11,12,12],
[12,14,14,8,8,10,7,8,9,14,0,11,13],
[15,11,16,11,12,10,8,9,10,13,14,0,12],
[13,12,11,11,10,11,11,8,13,13,12,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 143, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,9,11,9,8,13,11,11,8,11,10,11],
[13,0,11,14,12,8,13,14,12,9,13,10,11],
[16,14,0,13,13,11,11,13,9,10,13,13,13],
[14,11,12,0,12,5,11,11,10,10,9,11,12],
[16,13,12,13,0,13,15,13,14,14,14,12,12],
[17,17,14,20,12,0,16,15,15,13,18,14,17],
[12,12,14,14,10,9,0,11,13,9,14,11,12],
[14,11,12,14,12,10,14,0,11,9,12,12,9],
[14,13,16,15,11,10,12,14,0,11,13,12,11],
[17,16,15,15,11,12,16,16,14,0,15,11,14],
[14,12,12,16,11,7,11,13,12,10,0,10,12],
[15,15,12,14,13,11,14,13,13,14,15,0,15],
[14,14,12,13,13,8,13,16,14,11,13,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 144, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,14,13,19,14,17,11,12,15,18,8,15],
[12,0,10,15,15,12,11,12,13,13,13,13,15],
[11,15,0,19,13,13,10,15,11,11,21,14,19],
[12,10,6,0,15,11,9,11,12,14,13,9,14],
[6,10,12,10,0,11,9,11,9,11,17,10,17],
[11,13,12,14,14,0,12,12,9,13,14,13,14],
[8,14,15,16,16,13,0,13,11,14,21,8,18],
[14,13,10,14,14,13,12,0,13,15,14,12,16],
[13,12,14,13,16,16,14,12,0,15,18,13,18],
[10,12,14,11,14,12,11,10,10,0,19,10,18],
[7,12,4,12,8,11,4,11,7,6,0,7,9],
[17,12,11,16,15,12,17,13,12,15,18,0,17],
[10,10,6,11,8,11,7,9,7,7,16,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 145, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,9,10,10,6,20,14,10,16,14,10,12],
[12,0,13,12,6,11,14,13,10,24,11,6,5],
[16,12,0,13,9,14,15,6,13,13,6,6,8],
[15,13,12,0,10,15,10,14,6,23,10,6,8],
[15,19,16,15,0,14,18,17,17,24,10,10,8],
[19,14,11,10,11,0,14,12,16,18,9,9,8],
[5,11,10,15,7,11,0,7,10,17,7,2,5],
[11,12,19,11,8,13,18,0,13,15,8,13,8],
[15,15,12,19,8,9,15,12,0,23,10,5,12],
[9,1,12,2,1,7,8,10,2,0,1,2,1],
[11,14,19,15,15,16,18,17,15,24,0,12,15],
[15,19,19,19,15,16,23,12,20,23,13,0,15],
[13,20,17,17,17,17,20,17,13,24,10,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 146, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,15,22,11,12,19,12,9,12,5,15,4],
[15,0,13,20,8,12,22,24,15,12,3,13,5],
[10,12,0,13,5,5,14,19,3,19,12,6,10],
[3,5,12,0,3,5,14,14,5,14,7,8,4],
[14,17,20,22,0,21,20,18,16,19,11,13,13],
[13,13,20,20,4,0,24,22,20,19,12,10,14],
[6,3,11,11,5,1,0,13,3,8,2,4,4],
[13,1,6,11,7,3,12,0,5,8,1,4,4],
[16,10,22,20,9,5,22,20,0,17,10,13,11],
[13,13,6,11,6,6,17,17,8,0,10,4,13],
[20,22,13,18,14,13,23,24,15,15,0,11,14],
[10,12,19,17,12,15,21,21,12,21,14,0,13],
[21,20,15,21,12,11,21,21,14,12,11,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 147, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,12,13,11,15,13,16,10,11,13,13,10],
[14,0,10,21,13,16,11,16,15,17,8,14,15],
[13,15,0,20,10,17,13,12,18,17,16,15,11],
[12,4,5,0,9,9,9,11,11,11,7,8,7],
[14,12,15,16,0,12,10,13,16,19,9,13,7],
[10,9,8,16,13,0,8,12,14,9,10,16,13],
[12,14,12,16,15,17,0,15,19,15,10,14,14],
[9,9,13,14,12,13,10,0,14,14,11,12,12],
[15,10,7,14,9,11,6,11,0,13,6,11,5],
[14,8,8,14,6,16,10,11,12,0,9,12,8],
[12,17,9,18,16,15,15,14,19,16,0,16,16],
[12,11,10,17,12,9,11,13,14,13,9,0,15],
[15,10,14,18,18,12,11,13,20,17,9,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 148, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,6,12,12,12,8,7,10,8,12,8,12],
[11,0,11,8,7,11,13,9,10,11,6,11,10],
[19,14,0,13,15,15,11,10,15,12,13,10,11],
[13,17,12,0,13,10,13,10,10,15,9,10,15],
[13,18,10,12,0,13,12,8,12,16,10,10,14],
[13,14,10,15,12,0,10,7,6,14,9,12,10],
[17,12,14,12,13,15,0,13,15,13,11,15,19],
[18,16,15,15,17,18,12,0,18,19,15,15,18],
[15,15,10,15,13,19,10,7,0,16,15,14,11],
[17,14,13,10,9,11,12,6,9,0,10,7,13],
[13,19,12,16,15,16,14,10,10,15,0,12,16],
[17,14,15,15,15,13,10,10,11,18,13,0,14],
[13,15,14,10,11,15,6,7,14,12,9,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 149, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,11,11,12,16,11,12,9,15,14,9,11],
[11,0,6,8,10,13,8,13,10,15,9,13,10],
[14,19,0,13,16,17,12,11,14,15,11,16,11],
[14,17,12,0,12,15,13,15,15,15,12,12,11],
[13,15,9,13,0,15,8,13,13,13,11,13,12],
[9,12,8,10,10,0,9,13,10,15,11,13,11],
[14,17,13,12,17,16,0,14,11,19,17,16,15],
[13,12,14,10,12,12,11,0,11,12,11,13,11],
[16,15,11,10,12,15,14,14,0,13,12,12,12],
[10,10,10,10,12,10,6,13,12,0,9,11,12],
[11,16,14,13,14,14,8,14,13,16,0,16,12],
[16,12,9,13,12,12,9,12,13,14,9,0,11],
[14,15,14,14,13,14,10,14,13,13,13,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 150, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,17,17,17,19,23,11,17,13,19,17,19],
[14,0,20,20,6,14,18,20,14,8,14,12,14],
[8,5,0,8,11,8,18,6,14,8,14,12,19],
[8,5,17,0,11,7,23,6,11,8,19,17,19],
[8,19,14,14,0,14,14,14,8,8,20,14,25],
[6,11,17,18,11,0,23,12,17,6,17,17,17],
[2,7,7,2,11,2,0,2,7,2,8,6,13],
[14,5,19,19,11,13,23,0,13,8,13,17,19],
[8,11,11,14,17,8,18,12,0,8,20,12,25],
[12,17,17,17,17,19,23,17,17,0,19,11,19],
[6,11,11,6,5,8,17,12,5,6,0,12,13],
[8,13,13,8,11,8,19,8,13,14,13,0,13],
[6,11,6,6,0,8,12,6,0,6,12,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 151, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,9,6,7,9,22,10,0,0,4,4,11],
[14,0,11,14,12,11,22,6,11,11,6,6,14],
[16,14,0,16,7,14,25,13,16,9,16,6,14],
[19,11,9,0,16,9,16,17,4,9,11,4,15],
[18,13,18,9,0,18,25,10,13,13,13,13,18],
[16,14,11,16,7,0,20,17,10,10,14,17,16],
[3,3,0,9,0,5,0,6,0,3,3,0,14],
[15,19,12,8,15,8,19,0,8,8,8,8,8],
[25,14,9,21,12,15,25,17,0,8,20,10,14],
[25,14,16,16,12,15,22,17,17,0,20,17,14],
[21,19,9,14,12,11,22,17,5,5,0,11,14],
[21,19,19,21,12,8,25,17,15,8,14,0,14],
[14,11,11,10,7,9,11,17,11,11,11,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 152, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,12,12,14,11,12,14,10,14,14,14,16],
[12,0,11,11,14,11,14,10,15,14,10,17,12],
[13,14,0,13,15,7,15,14,9,9,10,14,14],
[13,14,12,0,12,8,14,13,7,10,12,16,11],
[11,11,10,13,0,7,11,13,8,11,13,10,12],
[14,14,18,17,18,0,19,15,12,10,15,19,19],
[13,11,10,11,14,6,0,15,8,10,9,13,13],
[11,15,11,12,12,10,10,0,9,13,13,16,12],
[15,10,16,18,17,13,17,16,0,12,12,18,17],
[11,11,16,15,14,15,15,12,13,0,15,15,15],
[11,15,15,13,12,10,16,12,13,10,0,18,15],
[11,8,11,9,15,6,12,9,7,10,7,0,9],
[9,13,11,14,13,6,12,13,8,10,10,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 153, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,8,9,15,15,13,9,10,8,6,7,7],
[19,0,20,17,11,16,17,14,11,20,16,19,13],
[17,5,0,12,15,16,9,6,11,8,6,11,8],
[16,8,13,0,15,16,13,8,15,8,10,9,8],
[10,14,10,10,0,14,7,5,9,13,12,11,9],
[10,9,9,9,11,0,7,7,6,8,12,15,8],
[12,8,16,12,18,18,0,14,14,8,10,16,15],
[16,11,19,17,20,18,11,0,8,19,11,20,17],
[15,14,14,10,16,19,11,17,0,13,16,15,14],
[17,5,17,17,12,17,17,6,12,0,12,12,9],
[19,9,19,15,13,13,15,14,9,13,0,18,15],
[18,6,14,16,14,10,9,5,10,13,7,0,2],
[18,12,17,17,16,17,10,8,11,16,10,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 154, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,9,10,11,9,11,7,8,9,8,9,11],
[15,0,11,10,10,15,15,11,12,8,15,11,14],
[16,14,0,13,16,11,11,8,10,15,14,14,15],
[15,15,12,0,13,12,13,10,14,14,13,11,15],
[14,15,9,12,0,9,12,8,11,13,14,9,14],
[16,10,14,13,16,0,10,9,15,9,11,12,14],
[14,10,14,12,13,15,0,12,14,12,13,14,17],
[18,14,17,15,17,16,13,0,10,16,15,20,17],
[17,13,15,11,14,10,11,15,0,15,13,15,18],
[16,17,10,11,12,16,13,9,10,0,15,14,18],
[17,10,11,12,11,14,12,10,12,10,0,11,16],
[16,14,11,14,16,13,11,5,10,11,14,0,16],
[14,11,10,10,11,11,8,8,7,7,9,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 155, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,13,12,14,11,14,12,13,10,16,12,9],
[15,0,12,15,15,16,13,12,12,14,13,15,9],
[12,13,0,13,17,18,15,16,12,16,16,15,13],
[13,10,12,0,14,12,12,10,12,14,13,14,10],
[11,10,8,11,0,11,11,11,10,12,12,10,10],
[14,9,7,13,14,0,10,11,9,10,13,10,9],
[11,12,10,13,14,15,0,13,12,10,14,12,9],
[13,13,9,15,14,14,12,0,13,12,16,14,9],
[12,13,13,13,15,16,13,12,0,12,14,18,10],
[15,11,9,11,13,15,15,13,13,0,15,16,10],
[9,12,9,12,13,12,11,9,11,10,0,11,9],
[13,10,10,11,15,15,13,11,7,9,14,0,7],
[16,16,12,15,15,16,16,16,15,15,16,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 156, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,17,18,13,16,15,19,15,14,10,14,14],
[11,0,12,11,10,15,10,11,19,9,9,11,8],
[8,13,0,13,11,14,9,14,14,10,9,10,10],
[7,14,12,0,9,16,8,17,13,12,9,14,11],
[12,15,14,16,0,12,12,13,16,10,8,12,11],
[9,10,11,9,13,0,9,13,11,11,6,9,9],
[10,15,16,17,13,16,0,18,16,13,15,15,14],
[6,14,11,8,12,12,7,0,12,9,11,11,8],
[10,6,11,12,9,14,9,13,0,10,9,12,14],
[11,16,15,13,15,14,12,16,15,0,9,10,12],
[15,16,16,16,17,19,10,14,16,16,0,17,13],
[11,14,15,11,13,16,10,14,13,15,8,0,10],
[11,17,15,14,14,16,11,17,11,13,12,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 157, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,16,9,16,16,13,16,15,12,13,16,17],
[16,0,16,11,15,20,19,14,14,13,13,16,14],
[9,9,0,11,13,15,9,14,15,10,11,13,15],
[16,14,14,0,20,19,13,16,17,15,12,19,16],
[9,10,12,5,0,19,14,15,11,11,4,16,12],
[9,5,10,6,6,0,13,10,9,12,7,11,15],
[12,6,16,12,11,12,0,11,12,8,9,10,9],
[9,11,11,9,10,15,14,0,9,11,7,11,15],
[10,11,10,8,14,16,13,16,0,14,9,12,14],
[13,12,15,10,14,13,17,14,11,0,10,14,17],
[12,12,14,13,21,18,16,18,16,15,0,19,19],
[9,9,12,6,9,14,15,14,13,11,6,0,13],
[8,11,10,9,13,10,16,10,11,8,6,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 158, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,11,12,9,12,18,8,16,15,9,9,7],
[17,0,14,13,12,10,11,10,18,13,11,8,9],
[14,11,0,14,11,10,13,9,16,16,14,13,9],
[13,12,11,0,10,12,17,8,18,14,14,13,10],
[16,13,14,15,0,13,17,12,20,14,11,13,12],
[13,15,15,13,12,0,16,9,19,14,15,8,9],
[7,14,12,8,8,9,0,8,17,12,8,8,6],
[17,15,16,17,13,16,17,0,18,22,16,13,12],
[9,7,9,7,5,6,8,7,0,7,8,8,9],
[10,12,9,11,11,11,13,3,18,0,10,7,5],
[16,14,11,11,14,10,17,9,17,15,0,10,9],
[16,17,12,12,12,17,17,12,17,18,15,0,13],
[18,16,16,15,13,16,19,13,16,20,16,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 159, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,15,11,14,17,17,14,16,14,7,14,11],
[9,0,10,14,16,13,15,11,14,11,11,14,9],
[10,15,0,7,13,15,16,18,15,13,8,12,12],
[14,11,18,0,16,16,16,13,17,18,11,16,14],
[11,9,12,9,0,8,17,10,18,11,7,10,7],
[8,12,10,9,17,0,12,7,17,15,8,10,11],
[8,10,9,9,8,13,0,12,13,11,10,6,9],
[11,14,7,12,15,18,13,0,16,12,7,9,9],
[9,11,10,8,7,8,12,9,0,12,7,12,10],
[11,14,12,7,14,10,14,13,13,0,15,14,14],
[18,14,17,14,18,17,15,18,18,10,0,12,15],
[11,11,13,9,15,15,19,16,13,11,13,0,12],
[14,16,13,11,18,14,16,16,15,11,10,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 160, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,11,10,9,17,13,6,11,14,8,14,12],
[13,0,11,11,11,12,9,6,13,12,13,13,12],
[14,14,0,14,11,10,15,9,13,14,13,12,18],
[15,14,11,0,13,17,10,7,9,10,9,14,19],
[16,14,14,12,0,19,13,13,18,16,12,14,16],
[8,13,15,8,6,0,11,8,14,12,14,14,15],
[12,16,10,15,12,14,0,6,10,11,10,13,23],
[19,19,16,18,12,17,19,0,22,16,17,18,23],
[14,12,12,16,7,11,15,3,0,17,9,15,16],
[11,13,11,15,9,13,14,9,8,0,11,14,15],
[17,12,12,16,13,11,15,8,16,14,0,15,17],
[11,12,13,11,11,11,12,7,10,11,10,0,16],
[13,13,7,6,9,10,2,2,9,10,8,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 161, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,9,6,14,12,9,10,6,12,17,9,5],
[16,0,13,12,14,17,10,12,11,15,15,9,12],
[16,12,0,7,12,16,12,9,6,10,15,6,7],
[19,13,18,0,15,16,13,14,10,16,19,11,14],
[11,11,13,10,0,9,7,10,10,14,16,11,11],
[13,8,9,9,16,0,10,12,10,12,14,11,11],
[16,15,13,12,18,15,0,14,14,15,15,16,11],
[15,13,16,11,15,13,11,0,9,12,16,11,11],
[19,14,19,15,15,15,11,16,0,16,17,13,12],
[13,10,15,9,11,13,10,13,9,0,11,6,7],
[8,10,10,6,9,11,10,9,8,14,0,5,8],
[16,16,19,14,14,14,9,14,12,19,20,0,12],
[20,13,18,11,14,14,14,14,13,18,17,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 162, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,12,15,11,12,11,7,9,12,12,12,12],
[12,0,14,19,10,12,9,10,10,13,11,13,14],
[13,11,0,17,8,11,15,11,7,8,12,14,14],
[10,6,8,0,6,7,6,6,6,6,5,10,6],
[14,15,17,19,0,17,18,15,15,19,12,11,21],
[13,13,14,18,8,0,13,10,8,11,12,11,13],
[14,16,10,19,7,12,0,11,9,16,12,12,18],
[18,15,14,19,10,15,14,0,12,15,13,15,19],
[16,15,18,19,10,17,16,13,0,14,10,11,15],
[13,12,17,19,6,14,9,10,11,0,10,12,15],
[13,14,13,20,13,13,13,12,15,15,0,14,15],
[13,12,11,15,14,14,13,10,14,13,11,0,16],
[13,11,11,19,4,12,7,6,10,10,10,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 163, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,7,8,12,6,10,10,21,15,12,10,7],
[13,0,10,11,12,10,14,10,19,13,17,12,15],
[18,15,0,18,16,14,13,13,20,15,12,14,13],
[17,14,7,0,18,15,13,9,18,18,16,9,15],
[13,13,9,7,0,9,11,11,17,9,14,11,10],
[19,15,11,10,16,0,12,8,19,19,18,11,18],
[15,11,12,12,14,13,0,8,17,14,16,13,16],
[15,15,12,16,14,17,17,0,17,15,18,17,20],
[4,6,5,7,8,6,8,8,0,9,10,6,9],
[10,12,10,7,16,6,11,10,16,0,16,10,11],
[13,8,13,9,11,7,9,7,15,9,0,11,14],
[15,13,11,16,14,14,12,8,19,15,14,0,14],
[18,10,12,10,15,7,9,5,16,14,11,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 164, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,11,12,8,6,11,6,7,6,11,13,10],
[16,0,16,12,12,16,17,12,13,10,16,16,14],
[14,9,0,16,10,16,14,12,14,10,13,14,11],
[13,13,9,0,6,9,12,8,9,9,13,13,9],
[17,13,15,19,0,15,16,15,9,10,17,15,15],
[19,9,9,16,10,0,13,15,7,8,17,14,11],
[14,8,11,13,9,12,0,12,13,9,13,9,10],
[19,13,13,17,10,10,13,0,12,13,16,14,14],
[18,12,11,16,16,18,12,13,0,12,16,12,13],
[19,15,15,16,15,17,16,12,13,0,21,16,15],
[14,9,12,12,8,8,12,9,9,4,0,14,8],
[12,9,11,12,10,11,16,11,13,9,11,0,11],
[15,11,14,16,10,14,15,11,12,10,17,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 165, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,8,13,9,12,10,8,8,10,12,10,9],
[16,0,11,13,15,10,13,14,13,14,16,12,12],
[17,14,0,12,12,15,11,14,13,13,14,13,13],
[12,12,13,0,12,13,11,13,9,17,12,14,13],
[16,10,13,13,0,13,11,13,13,17,15,15,13],
[13,15,10,12,12,0,12,10,7,13,14,15,12],
[15,12,14,14,14,13,0,15,12,16,12,14,17],
[17,11,11,12,12,15,10,0,11,16,12,12,13],
[17,12,12,16,12,18,13,14,0,14,13,13,13],
[15,11,12,8,8,12,9,9,11,0,12,13,12],
[13,9,11,13,10,11,13,13,12,13,0,13,10],
[15,13,12,11,10,10,11,13,12,12,12,0,13],
[16,13,12,12,12,13,8,12,12,13,15,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 166, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,9,13,15,12,12,18,11,14,14,8,10],
[12,0,11,9,16,9,15,13,14,15,14,12,12],
[16,14,0,13,19,14,16,16,15,18,16,12,14],
[12,16,12,0,15,9,13,14,12,16,14,15,15],
[10,9,6,10,0,11,10,12,13,15,11,7,9],
[13,16,11,16,14,0,16,17,17,18,12,10,12],
[13,10,9,12,15,9,0,12,13,14,8,9,12],
[7,12,9,11,13,8,13,0,12,14,8,12,14],
[14,11,10,13,12,8,12,13,0,14,14,10,12],
[11,10,7,9,10,7,11,11,11,0,8,4,10],
[11,11,9,11,14,13,17,17,11,17,0,10,11],
[17,13,13,10,18,15,16,13,15,21,15,0,12],
[15,13,11,10,16,13,13,11,13,15,14,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 167, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,5,5,12,8,10,8,8,12,10,7,10],
[18,0,13,11,12,14,17,14,12,14,13,12,10],
[20,12,0,16,14,13,12,16,14,15,16,15,13],
[20,14,9,0,16,13,13,17,11,14,17,14,15],
[13,13,11,9,0,14,15,13,14,12,13,13,10],
[17,11,12,12,11,0,14,16,17,13,14,14,15],
[15,8,13,12,10,11,0,14,15,14,15,12,12],
[17,11,9,8,12,9,11,0,12,11,13,14,13],
[17,13,11,14,11,8,10,13,0,14,13,16,13],
[13,11,10,11,13,12,11,14,11,0,11,14,14],
[15,12,9,8,12,11,10,12,12,14,0,11,12],
[18,13,10,11,12,11,13,11,9,11,14,0,12],
[15,15,12,10,15,10,13,12,12,11,13,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 168, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,17,13,11,7,13,17,12,17,10,8,11],
[15,0,19,15,9,11,11,17,17,15,19,17,19],
[8,6,0,9,7,3,9,13,18,10,6,4,7],
[12,10,16,0,9,8,12,20,20,10,22,14,16],
[14,16,18,16,0,12,16,20,20,18,18,18,16],
[18,14,22,17,13,0,6,18,20,18,16,18,19],
[12,14,16,13,9,19,0,17,14,12,16,14,19],
[8,8,12,5,5,7,8,0,14,12,10,2,19],
[13,8,7,5,5,5,11,11,0,11,8,2,5],
[8,10,15,15,7,7,13,13,14,0,12,12,19],
[15,6,19,3,7,9,9,15,17,13,0,15,19],
[17,8,21,11,7,7,11,23,23,13,10,0,19],
[14,6,18,9,9,6,6,6,20,6,6,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 169, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,17,25,17,17,25,25,10,25,9,17,17],
[8,0,9,17,17,8,25,17,18,25,15,17,7],
[8,16,0,18,10,8,18,18,18,16,8,8,16],
[0,8,7,0,17,0,17,23,8,16,7,7,0],
[8,8,15,8,0,0,8,16,8,16,8,15,8],
[8,17,17,25,25,0,25,25,10,25,15,17,15],
[0,0,7,8,17,0,0,15,0,16,7,7,0],
[0,8,7,2,9,0,10,0,8,16,0,7,0],
[15,7,7,17,17,15,25,17,0,23,7,15,7],
[0,0,9,9,9,0,9,9,2,0,7,7,7],
[16,10,17,18,17,10,18,25,18,18,0,25,10],
[8,8,17,18,10,8,18,18,10,18,0,0,8],
[8,18,9,25,17,10,25,25,18,18,15,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 170, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,9,11,14,12,23,11,24,25,9,22,20],
[3,0,9,7,3,7,7,14,8,9,3,19,20],
[16,16,0,11,18,12,23,16,24,22,7,22,25],
[14,18,14,0,14,25,25,13,24,25,3,19,20],
[11,22,7,11,0,12,23,11,13,12,13,22,25],
[13,18,13,0,13,0,19,13,19,19,2,19,19],
[2,18,2,0,2,6,0,13,8,8,2,13,20],
[14,11,9,12,14,12,12,0,13,14,14,11,25],
[1,17,1,1,12,6,17,12,0,7,1,12,20],
[0,16,3,0,13,6,17,11,18,0,2,11,20],
[16,22,18,22,12,23,23,11,24,23,0,22,20],
[3,6,3,6,3,6,12,14,13,14,3,0,20],
[5,5,0,5,0,6,5,0,5,5,5,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 171, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,12,8,10,4,13,8,6,3,4,8,14],
[15,0,8,11,13,8,17,14,11,11,6,18,13],
[13,17,0,17,17,7,20,13,13,10,9,15,15],
[17,14,8,0,13,10,18,11,13,12,6,15,13],
[15,12,8,12,0,8,15,18,16,13,13,15,13],
[21,17,18,15,17,0,17,15,13,15,17,10,15],
[12,8,5,7,10,8,0,9,8,10,3,12,10],
[17,11,12,14,7,10,16,0,12,12,8,14,17],
[19,14,12,12,9,12,17,13,0,9,5,10,19],
[22,14,15,13,12,10,15,13,16,0,8,14,20],
[21,19,16,19,12,8,22,17,20,17,0,17,18],
[17,7,10,10,10,15,13,11,15,11,8,0,17],
[11,12,10,12,12,10,15,8,6,5,7,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 172, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,12,10,14,12,11,12,11,12,14,10,8],
[10,0,11,10,11,15,12,10,7,13,10,7,8],
[13,14,0,14,15,15,14,14,12,11,16,13,7],
[15,15,11,0,12,12,13,17,11,11,16,12,10],
[11,14,10,13,0,12,12,14,13,9,12,10,13],
[13,10,10,13,13,0,11,13,9,10,15,9,10],
[14,13,11,12,13,14,0,12,10,13,10,6,8],
[13,15,11,8,11,12,13,0,11,10,12,7,12],
[14,18,13,14,12,16,15,14,0,13,15,14,15],
[13,12,14,14,16,15,12,15,12,0,17,12,9],
[11,15,9,9,13,10,15,13,10,8,0,11,9],
[15,18,12,13,15,16,19,18,11,13,14,0,13],
[17,17,18,15,12,15,17,13,10,16,16,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 173, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,20,17,16,15,19,15,14,15,15,16,17],
[14,0,21,13,11,20,20,16,16,14,13,16,16],
[5,4,0,10,9,10,17,14,11,13,7,14,13],
[8,12,15,0,11,11,21,13,8,8,11,11,6],
[9,14,16,14,0,15,19,18,10,12,16,10,9],
[10,5,15,14,10,0,23,11,14,6,11,14,12],
[6,5,8,4,6,2,0,9,7,5,7,3,3],
[10,9,11,12,7,14,16,0,12,10,11,11,9],
[11,9,14,17,15,11,18,13,0,13,10,15,13],
[10,11,12,17,13,19,20,15,12,0,12,17,15],
[10,12,18,14,9,14,18,14,15,13,0,15,13],
[9,9,11,14,15,11,22,14,10,8,10,0,15],
[8,9,12,19,16,13,22,16,12,10,12,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 174, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,12,14,13,14,13,12,10,13,15,9,12],
[12,0,10,16,17,17,15,14,13,17,15,11,15],
[13,15,0,16,15,14,16,10,10,16,14,12,14],
[11,9,9,0,10,11,9,11,8,10,10,6,9],
[12,8,10,15,0,10,15,10,11,13,15,10,14],
[11,8,11,14,15,0,14,14,13,15,11,11,13],
[12,10,9,16,10,11,0,14,9,11,13,12,11],
[13,11,15,14,15,11,11,0,14,15,14,13,11],
[15,12,15,17,14,12,16,11,0,14,12,16,14],
[12,8,9,15,12,10,14,10,11,0,10,8,10],
[10,10,11,15,10,14,12,11,13,15,0,12,12],
[16,14,13,19,15,14,13,12,9,17,13,0,14],
[13,10,11,16,11,12,14,14,11,15,13,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 175, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,7,10,7,11,13,10,9,8,7,14,8],
[12,0,7,9,7,11,12,8,8,11,12,12,9],
[18,18,0,13,12,11,20,12,12,12,14,14,9],
[15,16,12,0,9,12,13,4,10,12,8,15,12],
[18,18,13,16,0,13,17,12,9,14,17,15,11],
[14,14,14,13,12,0,13,12,10,14,10,13,12],
[12,13,5,12,8,12,0,9,9,13,12,11,8],
[15,17,13,21,13,13,16,0,14,17,11,18,12],
[16,17,13,15,16,15,16,11,0,13,15,12,9],
[17,14,13,13,11,11,12,8,12,0,12,13,8],
[18,13,11,17,8,15,13,14,10,13,0,13,13],
[11,13,11,10,10,12,14,7,13,12,12,0,10],
[17,16,16,13,14,13,17,13,16,17,12,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 176, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,14,7,14,9,9,15,15,11,15,19,11],
[9,0,11,9,12,7,6,10,13,8,11,10,12],
[11,14,0,10,13,10,6,9,13,11,18,13,11],
[18,16,15,0,14,15,14,19,17,10,16,16,13],
[11,13,12,11,0,9,8,12,12,10,14,12,9],
[16,18,15,10,16,0,15,12,18,18,18,16,14],
[16,19,19,11,17,10,0,15,17,13,20,13,17],
[10,15,16,6,13,13,10,0,13,11,17,14,10],
[10,12,12,8,13,7,8,12,0,10,13,10,8],
[14,17,14,15,15,7,12,14,15,0,14,16,16],
[10,14,7,9,11,7,5,8,12,11,0,10,9],
[6,15,12,9,13,9,12,11,15,9,15,0,11],
[14,13,14,12,16,11,8,15,17,9,16,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 177, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,18,18,18,19,8,18,10,10,14,18,14],
[7,0,14,14,16,17,10,14,7,13,20,19,19],
[7,11,0,13,11,15,11,12,9,13,20,13,15],
[7,11,12,0,10,11,6,14,13,13,20,13,15],
[7,9,14,15,0,11,5,14,7,13,20,19,13],
[6,8,10,14,14,0,10,14,2,12,20,12,14],
[17,15,14,19,20,15,0,18,11,17,20,19,15],
[7,11,13,11,11,11,7,0,9,13,21,15,15],
[15,18,16,12,18,23,14,16,0,20,20,16,15],
[15,12,12,12,12,13,8,12,5,0,14,12,9],
[11,5,5,5,5,5,5,4,5,11,0,5,5],
[7,6,12,12,6,13,6,10,9,13,20,0,11],
[11,6,10,10,12,11,10,10,10,16,20,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 178, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,15,11,12,15,18,10,11,13,16,10,13],
[10,0,15,4,13,14,11,7,7,13,12,8,12],
[10,10,0,6,10,15,11,11,8,9,10,8,9],
[14,21,19,0,14,16,18,11,14,13,14,13,14],
[13,12,15,11,0,15,15,13,9,11,16,10,18],
[10,11,10,9,10,0,14,6,9,12,12,8,15],
[7,14,14,7,10,11,0,8,8,10,15,10,11],
[15,18,14,14,12,19,17,0,17,10,14,13,16],
[14,18,17,11,16,16,17,8,0,13,18,13,17],
[12,12,16,12,14,13,15,15,12,0,19,10,17],
[9,13,15,11,9,13,10,11,7,6,0,9,5],
[15,17,17,12,15,17,15,12,12,15,16,0,16],
[12,13,16,11,7,10,14,9,8,8,20,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 179, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,14,16,14,13,11,14,10,8,12,10,11],
[13,0,14,16,15,12,13,17,11,14,17,12,9],
[11,11,0,12,11,11,15,15,9,10,18,12,12],
[9,9,13,0,9,11,14,12,11,7,14,10,10],
[11,10,14,16,0,12,11,11,11,9,15,14,7],
[12,13,14,14,13,0,14,13,10,10,17,9,12],
[14,12,10,11,14,11,0,14,8,5,12,8,10],
[11,8,10,13,14,12,11,0,7,11,11,8,6],
[15,14,16,14,14,15,17,18,0,12,17,12,13],
[17,11,15,18,16,15,20,14,13,0,13,16,12],
[13,8,7,11,10,8,13,14,8,12,0,9,8],
[15,13,13,15,11,16,17,17,13,9,16,0,9],
[14,16,13,15,18,13,15,19,12,13,17,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 180, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,10,17,16,18,11,18,10,13,17,20,9],
[4,0,9,10,13,13,7,13,10,9,14,17,6],
[15,16,0,19,23,14,11,18,17,19,17,19,17],
[8,15,6,0,15,12,12,16,8,10,14,18,12],
[9,12,2,10,0,9,10,13,5,6,14,16,8],
[7,12,11,13,16,0,14,13,13,10,12,11,10],
[14,18,14,13,15,11,0,8,13,12,14,13,14],
[7,12,7,9,12,12,17,0,9,8,10,16,9],
[15,15,8,17,20,12,12,16,0,5,13,19,9],
[12,16,6,15,19,15,13,17,20,0,15,21,14],
[8,11,8,11,11,13,11,15,12,10,0,18,8],
[5,8,6,7,9,14,12,9,6,4,7,0,8],
[16,19,8,13,17,15,11,16,16,11,17,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 181, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,10,11,15,15,14,10,8,12,13,11,16],
[20,0,18,18,21,15,11,13,19,19,17,16,17],
[15,7,0,15,15,15,15,15,11,15,9,13,19],
[14,7,10,0,14,13,8,9,9,13,8,11,18],
[10,4,10,11,0,11,8,9,4,9,9,8,7],
[10,10,10,12,14,0,10,11,11,12,7,10,9],
[11,14,10,17,17,15,0,11,9,19,10,13,18],
[15,12,10,16,16,14,14,0,13,16,13,11,16],
[17,6,14,16,21,14,16,12,0,18,17,15,16],
[13,6,10,12,16,13,6,9,7,0,9,10,14],
[12,8,16,17,16,18,15,12,8,16,0,13,14],
[14,9,12,14,17,15,12,14,10,15,12,0,17],
[9,8,6,7,18,16,7,9,9,11,11,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 182, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,10,13,9,14,10,12,8,9,10,7,12],
[18,0,17,17,12,20,15,12,11,15,15,10,13],
[15,8,0,14,10,12,9,13,11,11,10,9,12],
[12,8,11,0,8,12,10,10,13,8,9,8,10],
[16,13,15,17,0,15,10,11,15,14,16,12,14],
[11,5,13,13,10,0,10,8,9,10,11,9,13],
[15,10,16,15,15,15,0,13,13,15,11,11,15],
[13,13,12,15,14,17,12,0,14,13,15,13,14],
[17,14,14,12,10,16,12,11,0,12,12,9,11],
[16,10,14,17,11,15,10,12,13,0,10,11,14],
[15,10,15,16,9,14,14,10,13,15,0,9,13],
[18,15,16,17,13,16,14,12,16,14,16,0,15],
[13,12,13,15,11,12,10,11,14,11,12,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 183, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,5,7,6,12,11,14,10,9,10,7,8],
[16,0,8,14,18,15,14,16,16,10,13,11,9],
[20,17,0,14,13,15,16,20,18,11,13,18,13],
[18,11,11,0,16,16,19,18,18,15,15,13,12],
[19,7,12,9,0,15,13,15,15,11,14,9,11],
[13,10,10,9,10,0,15,19,9,10,11,11,9],
[14,11,9,6,12,10,0,12,8,9,13,8,10],
[11,9,5,7,10,6,13,0,7,9,10,12,7],
[15,9,7,7,10,16,17,18,0,12,11,12,9],
[16,15,14,10,14,15,16,16,13,0,11,15,8],
[15,12,12,10,11,14,12,15,14,14,0,12,9],
[18,14,7,12,16,14,17,13,13,10,13,0,8],
[17,16,12,13,14,16,15,18,16,17,16,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 184, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,10,12,12,6,4,7,9,13,17,11,13],
[4,0,6,4,6,2,4,7,5,5,8,5,9],
[15,19,0,12,9,5,8,11,6,14,10,5,17],
[13,21,13,0,11,11,9,14,10,12,13,14,18],
[13,19,16,14,0,16,11,11,11,12,21,9,21],
[19,23,20,14,9,0,11,17,8,17,14,14,21],
[21,21,17,16,14,14,0,15,10,18,23,11,19],
[18,18,14,11,14,8,10,0,15,17,18,17,16],
[16,20,19,15,14,17,15,10,0,18,20,17,20],
[12,20,11,13,13,8,7,8,7,0,13,9,14],
[8,17,15,12,4,11,2,7,5,12,0,3,15],
[14,20,20,11,16,11,14,8,8,16,22,0,14],
[12,16,8,7,4,4,6,9,5,11,10,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 185, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,13,6,18,15,13,13,13,9,17,11,17],
[14,0,13,11,21,16,13,13,9,14,16,14,15],
[12,12,0,10,18,17,12,6,13,15,12,8,17],
[19,14,15,0,21,20,17,12,16,17,17,11,20],
[7,4,7,4,0,7,6,5,6,12,4,6,9],
[10,9,8,5,18,0,12,13,11,9,13,9,16],
[12,12,13,8,19,13,0,11,12,10,16,6,18],
[12,12,19,13,20,12,14,0,17,15,18,11,15],
[12,16,12,9,19,14,13,8,0,17,14,13,20],
[16,11,10,8,13,16,15,10,8,0,9,6,12],
[8,9,13,8,21,12,9,7,11,16,0,8,15],
[14,11,17,14,19,16,19,14,12,19,17,0,20],
[8,10,8,5,16,9,7,10,5,13,10,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 186, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,15,12,10,11,15,11,12,10,10,13,14],
[12,0,16,18,8,12,9,9,15,13,19,17,14],
[10,9,0,14,13,10,14,9,10,10,17,18,17],
[13,7,11,0,12,7,7,11,8,9,14,15,16],
[15,17,12,13,0,10,7,14,10,12,13,17,14],
[14,13,15,18,15,0,12,9,18,14,17,18,21],
[10,16,11,18,18,13,0,11,16,15,15,17,17],
[14,16,16,14,11,16,14,0,14,12,16,18,16],
[13,10,15,17,15,7,9,11,0,9,12,17,16],
[15,12,15,16,13,11,10,13,16,0,12,13,17],
[15,6,8,11,12,8,10,9,13,13,0,17,16],
[12,8,7,10,8,7,8,7,8,12,8,0,14],
[11,11,8,9,11,4,8,9,9,8,9,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 187, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,8,11,9,13,11,11,5,11,11,10,7],
[15,0,9,10,11,14,16,10,10,13,10,11,9],
[17,16,0,15,14,15,16,12,8,14,14,17,14],
[14,15,10,0,11,12,13,15,11,12,14,14,9],
[16,14,11,14,0,14,19,12,15,15,14,16,11],
[12,11,10,13,11,0,13,12,9,14,13,11,7],
[14,9,9,12,6,12,0,10,8,12,10,10,9],
[14,15,13,10,13,13,15,0,12,14,15,13,11],
[20,15,17,14,10,16,17,13,0,16,17,20,14],
[14,12,11,13,10,11,13,11,9,0,13,14,14],
[14,15,11,11,11,12,15,10,8,12,0,16,13],
[15,14,8,11,9,14,15,12,5,11,9,0,9],
[18,16,11,16,14,18,16,14,11,11,12,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 188, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,6,7,7,8,8,5,8,6,6,5,5],
[18,0,11,17,11,16,12,10,13,11,13,10,10],
[19,14,0,16,15,15,16,14,13,11,14,15,13],
[18,8,9,0,9,15,10,7,12,9,11,10,8],
[18,14,10,16,0,14,14,12,14,13,15,14,15],
[17,9,10,10,11,0,11,10,14,10,8,8,11],
[17,13,9,15,11,14,0,6,16,11,11,9,13],
[20,15,11,18,13,15,19,0,15,12,13,11,17],
[17,12,12,13,11,11,9,10,0,12,7,12,11],
[19,14,14,16,12,15,14,13,13,0,14,15,14],
[19,12,11,14,10,17,14,12,18,11,0,9,14],
[20,15,10,15,11,17,16,14,13,10,16,0,16],
[20,15,12,17,10,14,12,8,14,11,11,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 189, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,21,9,19,8,15,11,18,12,16,16,8],
[14,0,22,13,22,8,13,10,13,17,11,11,16],
[4,3,0,5,20,6,6,5,7,12,8,8,8],
[16,12,20,0,15,17,12,15,17,12,16,13,15],
[6,3,5,10,0,6,6,7,8,6,8,10,12],
[17,17,19,8,19,0,18,13,19,15,23,18,12],
[10,12,19,13,19,7,0,6,10,14,11,12,7],
[14,15,20,10,18,12,19,0,18,11,21,11,10],
[7,12,18,8,17,6,15,7,0,15,19,10,8],
[13,8,13,13,19,10,11,14,10,0,15,13,9],
[9,14,17,9,17,2,14,4,6,10,0,11,10],
[9,14,17,12,15,7,13,14,15,12,14,0,10],
[17,9,17,10,13,13,18,15,17,16,15,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 190, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,9,10,11,18,16,9,8,16,18,9,16],
[15,0,10,7,12,11,16,6,5,17,11,6,17],
[16,15,0,10,14,14,15,3,11,17,13,11,16],
[15,18,15,0,15,15,14,15,14,19,15,10,11],
[14,13,11,10,0,15,14,10,13,19,14,10,19],
[7,14,11,10,10,0,16,7,2,17,16,11,15],
[9,9,10,11,11,9,0,6,4,14,15,9,14],
[16,19,22,10,15,18,19,0,19,20,18,15,16],
[17,20,14,11,12,23,21,6,0,17,19,16,21],
[9,8,8,6,6,8,11,5,8,0,13,8,9],
[7,14,12,10,11,9,10,7,6,12,0,11,16],
[16,19,14,15,15,14,16,10,9,17,14,0,19],
[9,8,9,14,6,10,11,9,4,16,9,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 191, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,8,8,1,8,9,4,6,4,6,11,14],
[19,0,14,14,10,11,15,10,7,17,10,11,14],
[17,11,0,14,12,16,12,9,14,13,13,8,17],
[17,11,11,0,4,7,13,7,9,7,11,11,12],
[24,15,13,21,0,14,13,15,9,13,15,16,17],
[17,14,9,18,11,0,16,12,6,17,17,11,14],
[16,10,13,12,12,9,0,9,5,11,11,8,14],
[21,15,16,18,10,13,16,0,11,17,13,10,16],
[19,18,11,16,16,19,20,14,0,12,17,11,17],
[21,8,12,18,12,8,14,8,13,0,8,12,18],
[19,15,12,14,10,8,14,12,8,17,0,9,15],
[14,14,17,14,9,14,17,15,14,13,16,0,10],
[11,11,8,13,8,11,11,9,8,7,10,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 192, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,12,13,13,13,11,16,14,10,15,13],
[15,0,10,17,15,17,16,10,12,17,12,17,13],
[15,15,0,15,15,16,16,13,12,18,12,18,17],
[13,8,10,0,16,12,10,7,12,13,12,15,14],
[12,10,10,9,0,8,7,8,11,12,9,17,10],
[12,8,9,13,17,0,10,12,17,15,11,16,17],
[12,9,9,15,18,15,0,12,12,14,12,16,11],
[14,15,12,18,17,13,13,0,14,19,13,15,12],
[9,13,13,13,14,8,13,11,0,17,11,15,14],
[11,8,7,12,13,10,11,6,8,0,9,13,11],
[15,13,13,13,16,14,13,12,14,16,0,16,15],
[10,8,7,10,8,9,9,10,10,12,9,0,10],
[12,12,8,11,15,8,14,13,11,14,10,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 193, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,15,13,11,20,15,14,13,10,11,11,19],
[10,0,15,13,8,13,14,11,12,11,12,14,11],
[10,10,0,13,8,17,12,11,14,10,8,10,17],
[12,12,12,0,8,15,12,11,13,6,10,12,15],
[14,17,17,17,0,16,14,12,17,11,16,14,16],
[5,12,8,10,9,0,6,10,8,6,11,7,8],
[10,11,13,13,11,19,0,8,10,9,9,10,17],
[11,14,14,14,13,15,17,0,11,13,12,11,17],
[12,13,11,12,8,17,15,14,0,11,8,10,18],
[15,14,15,19,14,19,16,12,14,0,17,15,18],
[14,13,17,15,9,14,16,13,17,8,0,14,14],
[14,11,15,13,11,18,15,14,15,10,11,0,19],
[6,14,8,10,9,17,8,8,7,7,11,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 194, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,9,5,12,9,9,5,13,8,6,9,9],
[14,0,14,10,17,12,13,9,14,14,12,15,13],
[16,11,0,7,12,7,12,8,12,11,11,13,13],
[20,15,18,0,16,13,12,15,15,14,17,16,16],
[13,8,13,9,0,9,10,7,10,12,11,12,10],
[16,13,18,12,16,0,15,13,14,11,16,17,15],
[16,12,13,13,15,10,0,11,15,12,12,16,15],
[20,16,17,10,18,12,14,0,18,16,11,15,12],
[12,11,13,10,15,11,10,7,0,11,10,15,11],
[17,11,14,11,13,14,13,9,14,0,12,15,14],
[19,13,14,8,14,9,13,14,15,13,0,13,11],
[16,10,12,9,13,8,9,10,10,10,12,0,13],
[16,12,12,9,15,10,10,13,14,11,14,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 195, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,13,12,12,10,11,12,9,11,12,10],
[12,0,14,16,14,11,9,8,16,9,10,11,11],
[12,11,0,10,14,10,11,11,15,10,9,10,8],
[12,9,15,0,14,13,11,8,9,11,10,7,12],
[13,11,11,11,0,12,11,8,10,8,11,11,7],
[13,14,15,12,13,0,13,12,12,14,11,16,17],
[15,16,14,14,14,12,0,14,15,14,9,14,12],
[14,17,14,17,17,13,11,0,14,12,10,15,12],
[13,9,10,16,15,13,10,11,0,11,10,13,9],
[16,16,15,14,17,11,11,13,14,0,10,15,13],
[14,15,16,15,14,14,16,15,15,15,0,16,12],
[13,14,15,18,14,9,11,10,12,10,9,0,13],
[15,14,17,13,18,8,13,13,16,12,13,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 196, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,10,10,23,11,16,12,11,14,9,10,12],
[16,0,15,13,20,13,18,13,13,15,11,14,15],
[15,10,0,16,19,9,20,21,12,15,7,16,13],
[15,12,9,0,21,17,17,11,13,11,9,12,16],
[2,5,6,4,0,7,7,6,6,9,6,6,1],
[14,12,16,8,18,0,14,13,9,12,12,13,12],
[9,7,5,8,18,11,0,7,7,9,9,6,5],
[13,12,4,14,19,12,18,0,9,10,10,12,14],
[14,12,13,12,19,16,18,16,0,19,13,15,13],
[11,10,10,14,16,13,16,15,6,0,7,16,8],
[16,14,18,16,19,13,16,15,12,18,0,15,15],
[15,11,9,13,19,12,19,13,10,9,10,0,9],
[13,10,12,9,24,13,20,11,12,17,10,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 197, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,16,18,18,9,9,13,14,9,14,12,11],
[10,0,16,13,15,16,6,10,12,9,10,10,9],
[9,9,0,6,12,8,6,12,11,9,11,11,12],
[7,12,19,0,16,10,13,7,18,16,11,9,12],
[7,10,13,9,0,6,8,3,5,2,3,3,15],
[16,9,17,15,19,0,6,9,19,16,11,9,13],
[16,19,19,12,17,19,0,10,21,18,12,12,12],
[12,15,13,18,22,16,15,0,18,15,24,19,15],
[11,13,14,7,20,6,4,7,0,1,9,9,14],
[16,16,16,9,23,9,7,10,24,0,9,15,16],
[11,15,14,14,22,14,13,1,16,16,0,19,16],
[13,15,14,16,22,16,13,6,16,10,6,0,16],
[14,16,13,13,10,12,13,10,11,9,9,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 198, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,13,11,7,10,11,15,15,15,11,11,15],
[9,0,14,10,12,14,16,14,16,11,11,11,9],
[12,11,0,10,10,12,8,12,13,14,11,10,12],
[14,15,15,0,14,16,14,16,16,18,13,12,15],
[18,13,15,11,0,17,11,15,14,15,12,12,15],
[15,11,13,9,8,0,11,14,12,11,9,9,13],
[14,9,17,11,14,14,0,12,12,11,12,12,14],
[10,11,13,9,10,11,13,0,13,11,9,12,12],
[10,9,12,9,11,13,13,12,0,11,10,9,8],
[10,14,11,7,10,14,14,14,14,0,11,12,11],
[14,14,14,12,13,16,13,16,15,14,0,14,16],
[14,14,15,13,13,16,13,13,16,13,11,0,12],
[10,16,13,10,10,12,11,13,17,14,9,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 199, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,4,13,4,9,13,13,4,4,4,13,4],
[12,0,16,25,12,21,21,25,12,12,16,25,16],
[21,9,0,21,21,9,9,9,0,0,0,9,4],
[12,0,4,0,12,0,0,4,0,0,4,0,4],
[21,13,4,13,0,9,9,13,0,0,4,13,4],
[16,4,16,25,16,0,13,16,16,4,16,13,16],
[12,4,16,25,16,12,0,16,12,16,16,16,16],
[12,0,16,21,12,9,9,0,12,0,0,9,4],
[21,13,25,25,25,9,13,13,0,13,13,13,13],
[21,13,25,25,25,21,9,25,12,0,16,25,16],
[21,9,25,21,21,9,9,25,12,9,0,9,13],
[12,0,16,25,12,12,9,16,12,0,16,0,16],
[21,9,21,21,21,9,9,21,12,9,12,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 25, 200, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbrcw/mebbrcw_13_25.csv", index=False, header=False)