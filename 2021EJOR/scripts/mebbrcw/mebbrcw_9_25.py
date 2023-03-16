
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,17,13,18,12,15,15,12,13],
[8,0,12,10,10,10,14,9,10],
[12,13,0,13,10,9,11,12,12],
[7,15,12,0,12,10,13,10,9],
[13,15,15,13,0,11,14,14,13],
[10,15,16,15,14,0,12,12,11],
[10,11,14,12,11,13,0,12,14],
[13,16,13,15,11,13,13,0,13],
[12,15,13,16,12,14,11,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 1, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,18,13,19,14,11,10,17],
[7,0,10,14,14,9,9,11,14],
[7,15,0,12,17,13,16,10,12],
[12,11,13,0,19,13,10,13,11],
[6,11,8,6,0,8,10,10,12],
[11,16,12,12,17,0,13,16,11],
[14,16,9,15,15,12,0,13,15],
[15,14,15,12,15,9,12,0,7],
[8,11,13,14,13,14,10,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 2, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,16,13,11,18,19,9,13],
[9,0,12,17,7,12,15,11,6],
[9,13,0,16,8,9,12,10,10],
[12,8,9,0,7,12,15,5,10],
[14,18,17,18,0,14,23,6,14],
[7,13,16,13,11,0,22,9,10],
[6,10,13,10,2,3,0,3,11],
[16,14,15,20,19,16,22,0,11],
[12,19,15,15,11,15,14,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 3, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,14,14,11,15,17,8,12],
[13,0,13,14,13,17,16,7,8],
[11,12,0,13,9,18,12,8,8],
[11,11,12,0,14,17,16,12,8],
[14,12,16,11,0,18,17,10,13],
[10,8,7,8,7,0,11,11,11],
[8,9,13,9,8,14,0,9,9],
[17,18,17,13,15,14,16,0,11],
[13,17,17,17,12,14,16,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 4, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,17,8,8,12,11,7],
[15,0,10,23,7,16,14,17,14],
[15,15,0,22,13,14,8,15,14],
[8,2,3,0,4,3,6,8,7],
[17,18,12,21,0,12,16,19,14],
[17,9,11,22,13,0,9,10,16],
[13,11,17,19,9,16,0,15,11],
[14,8,10,17,6,15,10,0,10],
[18,11,11,18,11,9,14,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 5, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,15,15,11,7,14,12,15],
[16,0,20,14,16,15,16,13,9],
[10,5,0,7,10,12,13,12,6],
[10,11,18,0,9,12,13,15,19],
[14,9,15,16,0,14,19,19,16],
[18,10,13,13,11,0,14,10,13],
[11,9,12,12,6,11,0,16,15],
[13,12,13,10,6,15,9,0,14],
[10,16,19,6,9,12,10,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 6, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,18,12,15,14,20,14,14],
[6,0,13,12,12,12,13,8,12],
[7,12,0,11,14,9,13,12,13],
[13,13,14,0,16,10,18,9,11],
[10,13,11,9,0,11,16,12,11],
[11,13,16,15,14,0,21,10,14],
[5,12,12,7,9,4,0,7,9],
[11,17,13,16,13,15,18,0,13],
[11,13,12,14,14,11,16,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 7, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,16,15,16,17,17,14,10],
[7,0,10,7,13,15,12,9,10],
[9,15,0,10,13,15,12,12,10],
[10,18,15,0,16,18,15,10,13],
[9,12,12,9,0,9,14,15,12],
[8,10,10,7,16,0,9,6,14],
[8,13,13,10,11,16,0,4,11],
[11,16,13,15,10,19,21,0,14],
[15,15,15,12,13,11,14,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 8, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,19,11,6,14,17,6,17],
[0,0,8,0,6,8,0,0,0],
[6,17,0,17,6,14,6,6,17],
[14,25,8,0,14,14,6,14,6],
[19,19,19,11,0,19,11,11,11],
[11,17,11,11,6,0,11,11,11],
[8,25,19,19,14,14,0,8,17],
[19,25,19,11,14,14,17,0,17],
[8,25,8,19,14,14,8,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 9, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,8,15,14,14,17,16,16],
[12,0,5,12,16,14,16,13,15],
[17,20,0,21,12,15,15,16,18],
[10,13,4,0,13,14,14,12,17],
[11,9,13,12,0,18,17,21,19],
[11,11,10,11,7,0,13,10,20],
[8,9,10,11,8,12,0,13,16],
[9,12,9,13,4,15,12,0,18],
[9,10,7,8,6,5,9,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 10, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,12,9,14,9,14,13,8],
[9,0,8,9,16,13,12,5,12],
[13,17,0,17,16,16,9,16,13],
[16,16,8,0,12,12,15,8,11],
[11,9,9,13,0,12,12,8,12],
[16,12,9,13,13,0,10,8,5],
[11,13,16,10,13,15,0,8,15],
[12,20,9,17,17,17,17,0,13],
[17,13,12,14,13,20,10,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 11, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,9,6,6,7,9,10,9],
[19,0,13,15,11,15,16,14,20],
[16,12,0,11,9,14,13,11,14],
[19,10,14,0,6,9,14,12,14],
[19,14,16,19,0,16,17,12,19],
[18,10,11,16,9,0,15,14,13],
[16,9,12,11,8,10,0,11,16],
[15,11,14,13,13,11,14,0,19],
[16,5,11,11,6,12,9,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 12, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,14,15,14,11,11,12,12],
[9,0,13,15,12,7,10,12,8],
[11,12,0,13,12,11,13,13,14],
[10,10,12,0,13,12,11,11,9],
[11,13,13,12,0,11,12,12,14],
[14,18,14,13,14,0,13,8,11],
[14,15,12,14,13,12,0,12,11],
[13,13,12,14,13,17,13,0,9],
[13,17,11,16,11,14,14,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 13, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,15,19,10,12,19,16,17],
[6,0,10,8,8,9,14,17,12],
[10,15,0,16,13,9,17,20,13],
[6,17,9,0,12,14,13,17,16],
[15,17,12,13,0,11,15,15,16],
[13,16,16,11,14,0,17,21,13],
[6,11,8,12,10,8,0,14,10],
[9,8,5,8,10,4,11,0,9],
[8,13,12,9,9,12,15,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 14, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,10,15,13,12,14,9],
[12,0,11,13,13,7,7,13,13],
[12,14,0,14,14,11,13,15,13],
[15,12,11,0,16,12,10,11,12],
[10,12,11,9,0,8,10,8,10],
[12,18,14,13,17,0,11,9,12],
[13,18,12,15,15,14,0,13,17],
[11,12,10,14,17,16,12,0,11],
[16,12,12,13,15,13,8,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 15, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,17,12,15,15,15,14,15],
[10,0,12,13,12,13,12,8,11],
[8,13,0,15,11,11,12,7,14],
[13,12,10,0,10,15,13,11,11],
[10,13,14,15,0,15,13,13,10],
[10,12,14,10,10,0,12,10,14],
[10,13,13,12,12,13,0,10,12],
[11,17,18,14,12,15,15,0,13],
[10,14,11,14,15,11,13,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 16, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,12,13,9,12,14,10,12],
[15,0,14,14,12,15,17,12,15],
[13,11,0,13,10,10,14,10,9],
[12,11,12,0,9,11,13,10,10],
[16,13,15,16,0,12,15,12,12],
[13,10,15,14,13,0,17,13,13],
[11,8,11,12,10,8,0,9,10],
[15,13,15,15,13,12,16,0,13],
[13,10,16,15,13,12,15,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 17, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,14,13,17,14,16,11,14],
[12,0,11,15,15,13,15,12,11],
[11,14,0,13,16,11,16,11,12],
[12,10,12,0,15,13,13,10,11],
[8,10,9,10,0,11,12,10,11],
[11,12,14,12,14,0,13,11,14],
[9,10,9,12,13,12,0,8,12],
[14,13,14,15,15,14,17,0,10],
[11,14,13,14,14,11,13,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 18, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,15,14,21,8,13,10,9],
[12,0,21,20,17,16,9,12,16],
[10,4,0,15,9,6,8,3,10],
[11,5,10,0,9,5,4,7,12],
[4,8,16,16,0,11,8,7,7],
[17,9,19,20,14,0,10,12,16],
[12,16,17,21,17,15,0,15,16],
[15,13,22,18,18,13,10,0,14],
[16,9,15,13,18,9,9,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 19, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,11,9,19,12,15,17,12],
[7,0,8,9,11,9,15,15,6],
[14,17,0,13,14,11,17,16,14],
[16,16,12,0,16,13,21,22,14],
[6,14,11,9,0,11,10,16,10],
[13,16,14,12,14,0,17,15,8],
[10,10,8,4,15,8,0,11,10],
[8,10,9,3,9,10,14,0,7],
[13,19,11,11,15,17,15,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 20, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,14,5,10,4,13,12,8],
[11,0,12,9,10,6,10,14,8],
[11,13,0,11,15,11,19,12,11],
[20,16,14,0,15,12,15,17,16],
[15,15,10,10,0,10,10,14,12],
[21,19,14,13,15,0,18,19,10],
[12,15,6,10,15,7,0,11,5],
[13,11,13,8,11,6,14,0,10],
[17,17,14,9,13,15,20,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 21, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,15,12,12,10,9,18,13],
[15,0,16,15,15,9,11,16,14],
[10,9,0,14,10,11,13,13,14],
[13,10,11,0,12,8,14,16,13],
[13,10,15,13,0,16,14,16,19],
[15,16,14,17,9,0,16,19,13],
[16,14,12,11,11,9,0,20,13],
[7,9,12,9,9,6,5,0,12],
[12,11,11,12,6,12,12,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 22, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,15,14,12,9,13,14,8],
[16,0,14,12,12,13,17,13,13],
[10,11,0,10,11,7,12,11,8],
[11,13,15,0,7,14,13,11,11],
[13,13,14,18,0,15,15,13,11],
[16,12,18,11,10,0,14,15,11],
[12,8,13,12,10,11,0,15,12],
[11,12,14,14,12,10,10,0,7],
[17,12,17,14,14,14,13,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 23, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,16,19,15,19,12,8,9],
[10,0,15,13,16,19,11,9,13],
[9,10,0,14,20,13,8,9,6],
[6,12,11,0,16,14,11,10,5],
[10,9,5,9,0,13,8,6,6],
[6,6,12,11,12,0,11,3,3],
[13,14,17,14,17,14,0,12,11],
[17,16,16,15,19,22,13,0,7],
[16,12,19,20,19,22,14,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 24, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,10,9,9,14,10,13,11],
[11,0,9,9,11,14,9,10,9],
[15,16,0,12,13,13,11,10,10],
[16,16,13,0,13,15,11,13,11],
[16,14,12,12,0,15,12,13,13],
[11,11,12,10,10,0,11,13,10],
[15,16,14,14,13,14,0,11,13],
[12,15,15,12,12,12,14,0,13],
[14,16,15,14,12,15,12,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 25, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,12,10,6,16,16,10,16],
[15,0,21,13,9,19,19,19,21],
[13,4,0,13,4,4,19,19,19],
[15,12,12,0,0,6,15,21,21],
[19,16,21,25,0,10,25,25,25],
[9,6,21,19,15,0,21,15,21],
[9,6,6,10,0,4,0,10,6],
[15,6,6,4,0,10,15,0,21],
[9,4,6,4,0,4,19,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 26, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,11,14,10,20,11,10,17],
[6,0,9,9,11,11,6,6,10],
[14,16,0,7,8,11,14,11,12],
[11,16,18,0,13,16,13,16,16],
[15,14,17,12,0,17,11,15,14],
[5,14,14,9,8,0,9,6,16],
[14,19,11,12,14,16,0,12,14],
[15,19,14,9,10,19,13,0,11],
[8,15,13,9,11,9,11,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 27, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,16,14,15,9,13,9,12],
[13,0,15,15,12,13,15,10,17],
[9,10,0,12,11,7,17,9,10],
[11,10,13,0,12,11,12,8,9],
[10,13,14,13,0,10,14,9,11],
[16,12,18,14,15,0,12,14,16],
[12,10,8,13,11,13,0,9,10],
[16,15,16,17,16,11,16,0,15],
[13,8,15,16,14,9,15,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 28, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,19,18,15,7,12,19,18],
[10,0,11,18,19,17,12,15,12],
[6,14,0,14,19,8,8,15,8],
[7,7,11,0,7,5,15,11,5],
[10,6,6,18,0,12,12,17,12],
[18,8,17,20,13,0,12,17,16],
[13,13,17,10,13,13,0,17,8],
[6,10,10,14,8,8,8,0,8],
[7,13,17,20,13,9,17,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 29, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,9,9,13,10,9,13,9],
[6,0,9,7,8,12,7,11,9],
[16,16,0,13,15,13,8,13,14],
[16,18,12,0,14,14,11,16,11],
[12,17,10,11,0,12,6,14,10],
[15,13,12,11,13,0,11,17,11],
[16,18,17,14,19,14,0,15,12],
[12,14,12,9,11,8,10,0,11],
[16,16,11,14,15,14,13,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 30, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,8,15,12,12,11,7,8],
[11,0,10,15,11,10,13,3,9],
[17,15,0,18,12,9,14,9,12],
[10,10,7,0,8,7,12,7,9],
[13,14,13,17,0,11,18,13,10],
[13,15,16,18,14,0,18,12,13],
[14,12,11,13,7,7,0,7,6],
[18,22,16,18,12,13,18,0,18],
[17,16,13,16,15,12,19,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 31, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,10,3,5,5,12,13,12],
[2,0,12,5,7,0,7,10,7],
[15,13,0,13,13,3,15,8,15],
[22,20,12,0,15,10,22,18,12],
[20,18,12,10,0,5,22,15,12],
[20,25,22,15,20,0,25,15,12],
[13,18,10,3,3,0,0,13,2],
[12,15,17,7,10,10,12,0,12],
[13,18,10,13,13,13,23,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 32, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,15,14,13,15,20,15,10],
[15,0,18,14,10,11,14,14,10],
[10,7,0,15,10,14,16,15,7],
[11,11,10,0,7,11,9,16,6],
[12,15,15,18,0,16,14,20,14],
[10,14,11,14,9,0,14,14,14],
[5,11,9,16,11,11,0,20,11],
[10,11,10,9,5,11,5,0,7],
[15,15,18,19,11,11,14,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 33, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,12,9,15,12,12,12,11],
[20,0,18,11,19,14,16,13,16],
[13,7,0,10,11,12,10,10,10],
[16,14,15,0,16,12,17,11,9],
[10,6,14,9,0,11,10,9,11],
[13,11,13,13,14,0,14,11,10],
[13,9,15,8,15,11,0,12,10],
[13,12,15,14,16,14,13,0,15],
[14,9,15,16,14,15,15,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 34, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,14,14,14,12,16,17,14],
[12,0,11,14,13,12,13,17,15],
[11,14,0,13,13,13,11,14,13],
[11,11,12,0,13,12,12,15,11],
[11,12,12,12,0,14,13,16,9],
[13,13,12,13,11,0,15,19,13],
[9,12,14,13,12,10,0,15,14],
[8,8,11,10,9,6,10,0,10],
[11,10,12,14,16,12,11,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 35, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,11,15,10,15,12,12,18],
[12,0,12,17,8,17,12,14,11],
[14,13,0,17,13,18,16,10,15],
[10,8,8,0,11,15,8,14,11],
[15,17,12,14,0,16,17,12,13],
[10,8,7,10,9,0,10,9,7],
[13,13,9,17,8,15,0,9,13],
[13,11,15,11,13,16,16,0,12],
[7,14,10,14,12,18,12,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 36, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,7,13,12,13,14,10,7],
[17,0,9,12,13,11,13,8,8],
[18,16,0,13,12,17,20,12,15],
[12,13,12,0,14,12,17,13,7],
[13,12,13,11,0,14,13,11,9],
[12,14,8,13,11,0,14,16,12],
[11,12,5,8,12,11,0,9,11],
[15,17,13,12,14,9,16,0,11],
[18,17,10,18,16,13,14,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 37, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,16,16,20,9,17,16,17],
[10,0,9,12,10,11,13,8,15],
[9,16,0,12,16,14,16,14,15],
[9,13,13,0,12,6,14,11,17],
[5,15,9,13,0,5,12,9,17],
[16,14,11,19,20,0,23,18,19],
[8,12,9,11,13,2,0,7,18],
[9,17,11,14,16,7,18,0,21],
[8,10,10,8,8,6,7,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 38, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,16,12,11,14,14,19,18],
[10,0,13,14,12,12,13,18,15],
[9,12,0,11,8,12,14,21,10],
[13,11,14,0,17,13,17,14,18],
[14,13,17,8,0,17,15,20,12],
[11,13,13,12,8,0,13,13,14],
[11,12,11,8,10,12,0,15,15],
[6,7,4,11,5,12,10,0,12],
[7,10,15,7,13,11,10,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 39, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,9,0,11,5,16,16,25],
[9,0,9,0,11,5,16,11,25],
[16,16,0,0,16,5,16,16,16],
[25,25,25,0,16,5,16,16,25],
[14,14,9,9,0,5,5,14,14],
[20,20,20,20,20,0,11,20,20],
[9,9,9,9,20,14,0,20,9],
[9,14,9,9,11,5,5,0,14],
[0,0,9,0,11,5,16,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 40, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,19,9,19,19,19,14,4],
[17,0,21,11,21,21,25,19,11],
[6,4,0,7,4,19,14,6,8],
[16,14,18,0,14,18,16,12,20],
[6,4,21,11,0,21,21,16,6],
[6,4,6,7,4,0,12,6,6],
[6,0,11,9,4,13,0,2,6],
[11,6,19,13,9,19,23,0,15],
[21,14,17,5,19,19,19,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 41, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,16,13,12,14,15,16,14],
[11,0,11,11,11,13,15,12,12],
[9,14,0,16,15,16,18,15,14],
[12,14,9,0,13,17,15,13,12],
[13,14,10,12,0,18,15,14,16],
[11,12,9,8,7,0,11,9,15],
[10,10,7,10,10,14,0,10,10],
[9,13,10,12,11,16,15,0,16],
[11,13,11,13,9,10,15,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 42, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,13,13,15,12,16,15,16],
[17,0,9,15,17,18,17,11,16],
[12,16,0,12,16,17,18,13,15],
[12,10,13,0,13,16,14,16,16],
[10,8,9,12,0,10,13,9,15],
[13,7,8,9,15,0,14,14,16],
[9,8,7,11,12,11,0,14,13],
[10,14,12,9,16,11,11,0,12],
[9,9,10,9,10,9,12,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 43, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,15,16,16,11,14,16,15],
[9,0,13,11,12,10,11,11,12],
[10,12,0,9,13,13,12,13,14],
[9,14,16,0,15,12,14,17,11],
[9,13,12,10,0,8,10,12,10],
[14,15,12,13,17,0,14,12,13],
[11,14,13,11,15,11,0,13,14],
[9,14,12,8,13,13,12,0,12],
[10,13,11,14,15,12,11,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 44, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,12,9,11,10,8,10,10],
[11,0,7,10,16,11,9,10,10],
[13,18,0,14,14,15,13,14,10],
[16,15,11,0,12,14,7,7,12],
[14,9,11,13,0,11,11,11,11],
[15,14,10,11,14,0,9,9,11],
[17,16,12,18,14,16,0,15,14],
[15,15,11,18,14,16,10,0,14],
[15,15,15,13,14,14,11,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 45, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,19,14,12,14,13,18,12],
[13,0,19,15,11,16,15,13,15],
[6,6,0,3,6,8,4,6,8],
[11,10,22,0,13,11,12,13,15],
[13,14,19,12,0,13,15,11,10],
[11,9,17,14,12,0,10,13,15],
[12,10,21,13,10,15,0,12,15],
[7,12,19,12,14,12,13,0,19],
[13,10,17,10,15,10,10,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 46, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,11,13,15,17,11,9,7],
[13,0,12,13,10,13,13,13,9],
[14,13,0,11,12,16,15,15,8],
[12,12,14,0,12,15,12,18,10],
[10,15,13,13,0,11,10,12,13],
[8,12,9,10,14,0,14,9,8],
[14,12,10,13,15,11,0,9,6],
[16,12,10,7,13,16,16,0,7],
[18,16,17,15,12,17,19,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 47, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,10,5,14,13,19,10,15],
[13,0,13,14,14,16,16,9,13],
[15,12,0,13,18,12,14,15,18],
[20,11,12,0,16,21,20,14,17],
[11,11,7,9,0,11,13,7,16],
[12,9,13,4,14,0,13,12,15],
[6,9,11,5,12,12,0,10,14],
[15,16,10,11,18,13,15,0,15],
[10,12,7,8,9,10,11,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 48, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,6,15,14,15,15,14,11],
[10,0,10,8,11,16,13,8,8],
[19,15,0,17,15,15,9,12,12],
[10,17,8,0,19,19,16,16,13],
[11,14,10,6,0,17,9,13,8],
[10,9,10,6,8,0,1,16,8],
[10,12,16,9,16,24,0,16,11],
[11,17,13,9,12,9,9,0,9],
[14,17,13,12,17,17,14,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 49, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,12,12,19,14,17,14,15],
[15,0,15,12,16,16,14,8,15],
[13,10,0,12,16,13,16,17,11],
[13,13,13,0,14,16,19,17,9],
[6,9,9,11,0,6,9,11,10],
[11,9,12,9,19,0,13,9,14],
[8,11,9,6,16,12,0,11,10],
[11,17,8,8,14,16,14,0,13],
[10,10,14,16,15,11,15,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 50, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,16,13,17,8,17,14,14],
[9,0,16,14,9,7,8,15,16],
[9,9,0,15,12,12,13,13,14],
[12,11,10,0,10,11,10,12,13],
[8,16,13,15,0,10,14,16,14],
[17,18,13,14,15,0,14,11,14],
[8,17,12,15,11,11,0,15,13],
[11,10,12,13,9,14,10,0,10],
[11,9,11,12,11,11,12,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 51, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,10,10,13,13,11,18,12],
[9,0,10,11,11,13,10,15,11],
[15,15,0,13,11,13,14,17,14],
[15,14,12,0,15,15,11,17,14],
[12,14,14,10,0,15,9,17,9],
[12,12,12,10,10,0,12,14,8],
[14,15,11,14,16,13,0,17,16],
[7,10,8,8,8,11,8,0,8],
[13,14,11,11,16,17,9,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 52, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,8,11,12,6,10,9],
[14,0,7,7,14,9,5,7,10],
[14,18,0,14,18,15,13,15,11],
[17,18,11,0,10,14,11,13,17],
[14,11,7,15,0,12,6,13,13],
[13,16,10,11,13,0,8,11,9],
[19,20,12,14,19,17,0,12,14],
[15,18,10,12,12,14,13,0,10],
[16,15,14,8,12,16,11,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 53, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,21,9,15,25,25,19,19],
[4,0,4,4,4,4,10,4,4],
[4,21,0,9,0,25,10,4,4],
[16,21,16,0,10,25,16,10,10],
[10,21,25,15,0,25,16,19,16],
[0,21,0,0,0,0,10,4,4],
[0,15,15,9,9,15,0,9,9],
[6,21,21,15,6,21,16,0,16],
[6,21,21,15,9,21,16,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 54, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,14,20,13,14,19,9,9],
[14,0,14,13,10,13,13,13,15],
[11,11,0,16,12,14,16,13,8],
[5,12,9,0,13,10,14,11,9],
[12,15,13,12,0,11,12,14,10],
[11,12,11,15,14,0,13,12,7],
[6,12,9,11,13,12,0,10,8],
[16,12,12,14,11,13,15,0,7],
[16,10,17,16,15,18,17,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 55, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,18,16,14,11,11,15,9],
[11,0,15,11,14,9,9,12,8],
[7,10,0,9,9,9,5,8,4],
[9,14,16,0,13,12,9,14,9],
[11,11,16,12,0,12,10,15,10],
[14,16,16,13,13,0,13,15,11],
[14,16,20,16,15,12,0,18,13],
[10,13,17,11,10,10,7,0,10],
[16,17,21,16,15,14,12,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 56, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,20,18,16,16,12,16,18],
[9,0,23,18,13,14,12,13,18],
[5,2,0,7,11,11,7,11,10],
[7,7,18,0,11,9,14,11,14],
[9,12,14,14,0,5,16,12,9],
[9,11,14,16,20,0,21,16,11],
[13,13,18,11,9,4,0,12,9],
[9,12,14,14,13,9,13,0,11],
[7,7,15,11,16,14,16,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 57, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,14,10,11,13,13,13,12],
[9,0,11,8,8,9,10,7,12],
[11,14,0,11,8,10,11,12,12],
[15,17,14,0,16,8,13,13,13],
[14,17,17,9,0,13,15,11,13],
[12,16,15,17,12,0,10,18,11],
[12,15,14,12,10,15,0,12,13],
[12,18,13,12,14,7,13,0,13],
[13,13,13,12,12,14,12,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 58, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,13,10,14,15,13,11,11],
[14,0,18,14,16,12,10,13,9],
[12,7,0,9,15,16,8,9,11],
[15,11,16,0,18,10,10,9,8],
[11,9,10,7,0,12,10,8,10],
[10,13,9,15,13,0,12,12,16],
[12,15,17,15,15,13,0,16,15],
[14,12,16,16,17,13,9,0,14],
[14,16,14,17,15,9,10,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 59, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,10,10,12,13,10,9,6],
[16,0,12,17,16,16,14,14,11],
[15,13,0,13,16,13,15,12,13],
[15,8,12,0,13,12,13,10,11],
[13,9,9,12,0,12,11,11,12],
[12,9,12,13,13,0,13,11,10],
[15,11,10,12,14,12,0,9,9],
[16,11,13,15,14,14,16,0,11],
[19,14,12,14,13,15,16,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 60, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,13,14,12,12,11,14,10],
[14,0,12,13,14,15,13,11,12],
[12,13,0,14,19,13,15,14,14],
[11,12,11,0,17,13,12,10,15],
[13,11,6,8,0,7,9,9,12],
[13,10,12,12,18,0,8,11,12],
[14,12,10,13,16,17,0,12,14],
[11,14,11,15,16,14,13,0,14],
[15,13,11,10,13,13,11,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 61, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,16,16,11,16,16,12,8],
[11,0,15,13,14,16,17,18,13],
[9,10,0,11,8,13,14,12,9],
[9,12,14,0,9,14,15,13,8],
[14,11,17,16,0,18,16,18,13],
[9,9,12,11,7,0,11,11,10],
[9,8,11,10,9,14,0,12,8],
[13,7,13,12,7,14,13,0,8],
[17,12,16,17,12,15,17,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 62, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,13,9,14,16,15,14,13],
[13,0,11,12,14,13,10,17,16],
[12,14,0,9,16,20,14,17,13],
[16,13,16,0,12,17,17,15,12],
[11,11,9,13,0,13,9,11,10],
[9,12,5,8,12,0,15,12,11],
[10,15,11,8,16,10,0,11,11],
[11,8,8,10,14,13,14,0,7],
[12,9,12,13,15,14,14,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 63, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,17,14,10,15,8,7,11],
[16,0,14,14,11,16,9,15,11],
[8,11,0,15,8,11,9,8,7],
[11,11,10,0,9,13,9,11,10],
[15,14,17,16,0,16,13,11,10],
[10,9,14,12,9,0,3,12,6],
[17,16,16,16,12,22,0,15,13],
[18,10,17,14,14,13,10,0,13],
[14,14,18,15,15,19,12,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 64, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,10,7,7,18,13,9,11],
[10,0,10,11,10,12,11,14,11],
[15,15,0,11,8,13,9,13,10],
[18,14,14,0,14,14,11,15,11],
[18,15,17,11,0,15,15,13,14],
[7,13,12,11,10,0,13,8,10],
[12,14,16,14,10,12,0,13,13],
[16,11,12,10,12,17,12,0,14],
[14,14,15,14,11,15,12,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 65, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,16,13,12,13,11,13,14],
[19,0,16,13,14,12,10,15,13],
[9,9,0,15,12,13,10,9,13],
[12,12,10,0,13,16,9,12,17],
[13,11,13,12,0,5,6,8,11],
[12,13,12,9,20,0,6,9,12],
[14,15,15,16,19,19,0,10,13],
[12,10,16,13,17,16,15,0,22],
[11,12,12,8,14,13,12,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 66, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,10,12,13,13,13,12,11],
[13,0,11,14,9,20,16,17,12],
[15,14,0,18,12,14,13,16,20],
[13,11,7,0,8,10,11,10,12],
[12,16,13,17,0,17,17,19,18],
[12,5,11,15,8,0,12,11,15],
[12,9,12,14,8,13,0,10,18],
[13,8,9,15,6,14,15,0,15],
[14,13,5,13,7,10,7,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 67, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,14,13,9,13,11,13,11],
[14,0,15,13,11,15,16,17,16],
[11,10,0,10,13,11,13,17,12],
[12,12,15,0,11,10,10,15,10],
[16,14,12,14,0,11,12,17,8],
[12,10,14,15,14,0,10,11,11],
[14,9,12,15,13,15,0,16,13],
[12,8,8,10,8,14,9,0,10],
[14,9,13,15,17,14,12,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 68, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,13,12,15,7,12,12,8],
[15,0,18,13,16,12,13,16,14],
[12,7,0,11,11,10,11,10,7],
[13,12,14,0,14,15,12,16,10],
[10,9,14,11,0,9,11,11,8],
[18,13,15,10,16,0,11,16,8],
[13,12,14,13,14,14,0,14,12],
[13,9,15,9,14,9,11,0,11],
[17,11,18,15,17,17,13,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 69, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,11,15,14,14,15,20,15],
[10,0,10,16,13,13,10,16,18],
[14,15,0,14,13,13,12,19,14],
[10,9,11,0,12,14,10,14,16],
[11,12,12,13,0,15,13,19,15],
[11,12,12,11,10,0,14,19,16],
[10,15,13,15,12,11,0,18,17],
[5,9,6,11,6,6,7,0,9],
[10,7,11,9,10,9,8,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 70, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,16,11,14,15,17,12,17],
[9,0,14,16,19,14,17,9,17],
[9,11,0,13,15,20,10,6,11],
[14,9,12,0,18,18,11,13,15],
[11,6,10,7,0,18,15,5,7],
[10,11,5,7,7,0,7,5,10],
[8,8,15,14,10,18,0,11,10],
[13,16,19,12,20,20,14,0,15],
[8,8,14,10,18,15,15,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 71, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,10,19,11,11,13,12,16],
[7,0,9,11,10,7,10,14,5],
[15,16,0,19,15,11,19,17,15],
[6,14,6,0,8,12,8,7,4],
[14,15,10,17,0,16,15,15,8],
[14,18,14,13,9,0,12,12,8],
[12,15,6,17,10,13,0,15,8],
[13,11,8,18,10,13,10,0,4],
[9,20,10,21,17,17,17,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 72, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,12,15,15,17,15,13,17],
[12,0,14,11,14,20,15,11,15],
[13,11,0,7,11,15,11,13,13],
[10,14,18,0,14,15,14,10,15],
[10,11,14,11,0,15,11,10,11],
[8,5,10,10,10,0,6,5,9],
[10,10,14,11,14,19,0,9,16],
[12,14,12,15,15,20,16,0,17],
[8,10,12,10,14,16,9,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 73, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,17,10,12,19,14,16],
[12,0,9,12,12,11,17,11,13],
[12,16,0,18,11,12,17,13,20],
[8,13,7,0,9,12,14,10,13],
[15,13,14,16,0,11,12,12,11],
[13,14,13,13,14,0,16,11,13],
[6,8,8,11,13,9,0,6,15],
[11,14,12,15,13,14,19,0,19],
[9,12,5,12,14,12,10,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 74, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,13,13,15,14,15,13,10],
[14,0,11,15,15,14,16,15,12],
[12,14,0,12,14,12,14,16,13],
[12,10,13,0,14,13,15,12,15],
[10,10,11,11,0,14,16,11,10],
[11,11,13,12,11,0,14,12,10],
[10,9,11,10,9,11,0,12,9],
[12,10,9,13,14,13,13,0,10],
[15,13,12,10,15,15,16,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 75, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,13,11,16,14,14,12,14],
[11,0,11,10,13,10,10,10,8],
[12,14,0,11,9,14,12,12,11],
[14,15,14,0,14,15,13,13,11],
[9,12,16,11,0,12,13,14,9],
[11,15,11,10,13,0,13,14,11],
[11,15,13,12,12,12,0,11,12],
[13,15,13,12,11,11,14,0,10],
[11,17,14,14,16,14,13,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 76, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,11,16,16,14,15,11,12],
[16,0,13,10,20,15,16,13,13],
[14,12,0,21,16,15,16,15,15],
[9,15,4,0,14,10,15,8,8],
[9,5,9,11,0,10,12,8,6],
[11,10,10,15,15,0,13,12,10],
[10,9,9,10,13,12,0,10,8],
[14,12,10,17,17,13,15,0,12],
[13,12,10,17,19,15,17,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 77, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,12,17,18,8,13,13,12],
[10,0,8,13,16,9,13,12,13],
[13,17,0,15,17,11,15,14,16],
[8,12,10,0,12,10,12,13,10],
[7,9,8,13,0,8,9,9,9],
[17,16,14,15,17,0,14,12,12],
[12,12,10,13,16,11,0,12,11],
[12,13,11,12,16,13,13,0,11],
[13,12,9,15,16,13,14,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 78, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,10,16,11,7,13,13,17],
[14,0,14,20,10,13,7,13,16],
[15,11,0,8,11,8,11,11,18],
[9,5,17,0,7,9,10,15,21],
[14,15,14,18,0,9,12,13,19],
[18,12,17,16,16,0,11,20,20],
[12,18,14,15,13,14,0,14,17],
[12,12,14,10,12,5,11,0,18],
[8,9,7,4,6,5,8,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 79, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,16,15,12,12,14,11,14],
[13,0,16,14,11,11,10,14,13],
[9,9,0,14,14,12,9,10,13],
[10,11,11,0,12,12,10,12,11],
[13,14,11,13,0,12,10,11,12],
[13,14,13,13,13,0,10,15,13],
[11,15,16,15,15,15,0,15,15],
[14,11,15,13,14,10,10,0,12],
[11,12,12,14,13,12,10,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 80, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,18,15,11,11,14,12],
[12,0,11,17,14,10,10,10,11],
[12,14,0,18,14,12,9,14,13],
[7,8,7,0,12,7,7,7,6],
[10,11,11,13,0,12,9,12,8],
[14,15,13,18,13,0,9,12,12],
[14,15,16,18,16,16,0,16,12],
[11,15,11,18,13,13,9,0,10],
[13,14,12,19,17,13,13,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 81, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,5,4,9,4,9,14,5],
[15,0,11,10,18,10,9,19,15],
[20,14,0,10,12,10,9,13,5],
[21,15,15,0,15,15,10,10,6],
[16,7,13,10,0,12,9,14,6],
[21,15,15,10,13,0,10,14,5],
[16,16,16,15,16,15,0,20,12],
[11,6,12,15,11,11,5,0,8],
[20,10,20,19,19,20,13,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 82, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,10,17,11,18,15,17,16],
[10,0,13,11,14,13,13,16,13],
[15,12,0,15,15,14,14,15,17],
[8,14,10,0,11,14,12,19,14],
[14,11,10,14,0,14,14,14,15],
[7,12,11,11,11,0,11,15,13],
[10,12,11,13,11,14,0,15,11],
[8,9,10,6,11,10,10,0,10],
[9,12,8,11,10,12,14,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 83, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,8,11,10,11,10,10,9],
[15,0,7,13,11,9,13,11,12],
[17,18,0,11,14,21,14,16,17],
[14,12,14,0,8,17,11,13,14],
[15,14,11,17,0,15,14,11,13],
[14,16,4,8,10,0,13,12,12],
[15,12,11,14,11,12,0,14,12],
[15,14,9,12,14,13,11,0,12],
[16,13,8,11,12,13,13,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 84, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,13,14,15,15,12,14,15],
[7,0,9,10,10,13,12,10,10],
[12,16,0,12,13,15,14,16,16],
[11,15,13,0,16,16,15,15,15],
[10,15,12,9,0,14,10,13,9],
[10,12,10,9,11,0,9,13,10],
[13,13,11,10,15,16,0,14,13],
[11,15,9,10,12,12,11,0,10],
[10,15,9,10,16,15,12,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 85, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,11,10,11,14,8,11,10],
[13,0,11,6,14,12,16,18,11],
[14,14,0,17,11,12,12,13,15],
[15,19,8,0,14,16,14,13,15],
[14,11,14,11,0,7,16,6,8],
[11,13,13,9,18,0,15,9,17],
[17,9,13,11,9,10,0,10,8],
[14,7,12,12,19,16,15,0,16],
[15,14,10,10,17,8,17,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 86, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,11,15,7,11,11,11,15],
[10,0,12,12,13,9,3,10,17],
[14,13,0,8,12,9,11,7,12],
[10,13,17,0,8,5,11,10,12],
[18,12,13,17,0,6,12,12,12],
[14,16,16,20,19,0,11,15,15],
[14,22,14,14,13,14,0,12,21],
[14,15,18,15,13,10,13,0,17],
[10,8,13,13,13,10,4,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 87, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,12,19,14,15,18,16,11],
[10,0,12,17,13,15,13,11,9],
[13,13,0,17,13,16,15,11,10],
[6,8,8,0,10,9,7,5,4],
[11,12,12,15,0,8,12,8,9],
[10,10,9,16,17,0,17,9,11],
[7,12,10,18,13,8,0,9,7],
[9,14,14,20,17,16,16,0,13],
[14,16,15,21,16,14,18,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 88, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,8,10,6,13,9,11,8],
[16,0,13,12,11,16,11,17,12],
[17,12,0,11,14,15,13,14,13],
[15,13,14,0,12,16,13,15,14],
[19,14,11,13,0,16,14,17,12],
[12,9,10,9,9,0,11,15,11],
[16,14,12,12,11,14,0,15,13],
[14,8,11,10,8,10,10,0,10],
[17,13,12,11,13,14,12,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 89, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,9,12,13,10,9,17,13],
[17,0,17,15,20,16,12,19,19],
[16,8,0,16,10,11,14,18,16],
[13,10,9,0,14,14,7,16,17],
[12,5,15,11,0,10,5,17,18],
[15,9,14,11,15,0,12,15,11],
[16,13,11,18,20,13,0,18,19],
[8,6,7,9,8,10,7,0,8],
[12,6,9,8,7,14,6,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 90, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,23,9,18,17,10,15,15],
[7,0,7,12,13,8,11,7,7],
[2,18,0,6,6,10,4,5,2],
[16,13,19,0,13,17,7,11,9],
[7,12,19,12,0,15,7,13,11],
[8,17,15,8,10,0,6,13,9],
[15,14,21,18,18,19,0,12,14],
[10,18,20,14,12,12,13,0,14],
[10,18,23,16,14,16,11,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 91, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,16,16,13,16,10,16,17],
[9,0,16,11,7,7,11,8,12],
[9,9,0,4,5,3,6,8,6],
[9,14,21,0,14,13,13,13,16],
[12,18,20,11,0,17,12,13,17],
[9,18,22,12,8,0,12,12,11],
[15,14,19,12,13,13,0,13,13],
[9,17,17,12,12,13,12,0,13],
[8,13,19,9,8,14,12,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 92, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,16,13,13,17,20,16,15],
[13,0,19,14,9,15,17,19,11],
[9,6,0,8,7,12,14,14,10],
[12,11,17,0,7,13,16,16,16],
[12,16,18,18,0,18,17,18,17],
[8,10,13,12,7,0,14,13,12],
[5,8,11,9,8,11,0,13,8],
[9,6,11,9,7,12,12,0,8],
[10,14,15,9,8,13,17,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 93, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,14,13,17,13,16,17,10],
[14,0,13,13,18,11,15,12,17],
[11,12,0,11,13,10,15,14,13],
[12,12,14,0,15,10,17,12,16],
[8,7,12,10,0,10,15,11,11],
[12,14,15,15,15,0,15,15,15],
[9,10,10,8,10,10,0,9,10],
[8,13,11,13,14,10,16,0,13],
[15,8,12,9,14,10,15,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 94, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,15,14,12,16,12,16,13],
[6,0,4,2,10,2,9,2,6],
[10,21,0,6,14,8,13,7,10],
[11,23,19,0,15,16,15,16,8],
[13,15,11,10,0,11,9,14,8],
[9,23,17,9,14,0,8,20,10],
[13,16,12,10,16,17,0,18,12],
[9,23,18,9,11,5,7,0,11],
[12,19,15,17,17,15,13,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 95, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,13,15,13,14,15,16,11],
[13,0,11,19,10,15,18,17,15],
[12,14,0,15,10,12,18,16,12],
[10,6,10,0,12,8,15,14,9],
[12,15,15,13,0,12,18,13,12],
[11,10,13,17,13,0,14,14,16],
[10,7,7,10,7,11,0,15,10],
[9,8,9,11,12,11,10,0,8],
[14,10,13,16,13,9,15,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 96, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,8,10,15,12,10,12,14],
[12,0,13,12,12,13,15,12,14],
[17,12,0,16,17,17,16,16,16],
[15,13,9,0,10,14,14,9,14],
[10,13,8,15,0,12,14,11,11],
[13,12,8,11,13,0,14,14,13],
[15,10,9,11,11,11,0,12,15],
[13,13,9,16,14,11,13,0,13],
[11,11,9,11,14,12,10,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 97, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,15,9,8,9,12,13,11],
[12,0,18,14,9,7,13,21,9],
[10,7,0,3,9,4,10,8,6],
[16,11,22,0,14,15,14,13,15],
[17,16,16,11,0,8,13,18,13],
[16,18,21,10,17,0,20,19,15],
[13,12,15,11,12,5,0,16,11],
[12,4,17,12,7,6,9,0,6],
[14,16,19,10,12,10,14,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 98, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,16,14,17,12,14,17,15],
[12,0,13,12,16,12,13,15,10],
[9,12,0,10,16,12,12,18,13],
[11,13,15,0,15,16,14,19,16],
[8,9,9,10,0,12,10,11,9],
[13,13,13,9,13,0,11,15,13],
[11,12,13,11,15,14,0,15,15],
[8,10,7,6,14,10,10,0,8],
[10,15,12,9,16,12,10,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 99, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,16,23,15,15,18,9,15],
[4,0,16,19,12,15,20,10,15],
[9,9,0,17,13,12,19,17,17],
[2,6,8,0,14,5,12,4,9],
[10,13,12,11,0,5,14,13,10],
[10,10,13,20,20,0,16,15,20],
[7,5,6,13,11,9,0,1,14],
[16,15,8,21,12,10,24,0,20],
[10,10,8,16,15,5,11,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 100, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,10,10,9,12,11,8,8],
[19,0,12,15,17,19,20,12,16],
[15,13,0,13,11,17,17,9,13],
[15,10,12,0,12,16,16,12,12],
[16,8,14,13,0,15,13,13,11],
[13,6,8,9,10,0,9,9,6],
[14,5,8,9,12,16,0,10,9],
[17,13,16,13,12,16,15,0,9],
[17,9,12,13,14,19,16,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 101, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,13,15,18,16,16,11,13],
[9,0,12,10,12,12,11,9,8],
[12,13,0,12,11,14,10,11,11],
[10,15,13,0,12,14,14,12,12],
[7,13,14,13,0,12,13,12,7],
[9,13,11,11,13,0,10,10,12],
[9,14,15,11,12,15,0,13,10],
[14,16,14,13,13,15,12,0,13],
[12,17,14,13,18,13,15,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 102, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,15,10,8,15,12,16,15],
[11,0,10,10,11,17,9,11,13],
[10,15,0,12,12,14,9,19,14],
[15,15,13,0,15,11,16,19,15],
[17,14,13,10,0,18,15,15,14],
[10,8,11,14,7,0,9,12,11],
[13,16,16,9,10,16,0,19,14],
[9,14,6,6,10,13,6,0,10],
[10,12,11,10,11,14,11,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 103, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,10,19,19,19,10,10,10],
[6,0,10,10,16,16,16,16,10],
[15,15,0,9,15,16,15,15,15],
[6,15,16,0,24,25,16,16,15],
[6,9,10,1,0,1,10,10,10],
[6,9,9,0,24,0,15,15,9],
[15,9,10,9,15,10,0,18,9],
[15,9,10,9,15,10,7,0,9],
[15,15,10,10,15,16,16,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 104, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,12,10,13,12,17,13,17],
[12,0,10,6,13,18,17,15,12],
[13,15,0,11,11,16,18,16,16],
[15,19,14,0,10,15,17,17,14],
[12,12,14,15,0,13,18,15,15],
[13,7,9,10,12,0,17,13,15],
[8,8,7,8,7,8,0,7,10],
[12,10,9,8,10,12,18,0,11],
[8,13,9,11,10,10,15,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 105, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,11,10,14,11,10,7,13],
[15,0,13,18,13,17,18,10,15],
[14,12,0,14,13,15,16,11,13],
[15,7,11,0,11,11,14,11,8],
[11,12,12,14,0,10,10,9,14],
[14,8,10,14,15,0,16,13,11],
[15,7,9,11,15,9,0,12,13],
[18,15,14,14,16,12,13,0,13],
[12,10,12,17,11,14,12,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 106, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,11,14,13,12,13,12,15],
[10,0,7,11,16,7,10,10,12],
[14,18,0,12,15,11,15,14,16],
[11,14,13,0,15,12,13,14,16],
[12,9,10,10,0,7,11,11,11],
[13,18,14,13,18,0,9,13,15],
[12,15,10,12,14,16,0,12,14],
[13,15,11,11,14,12,13,0,16],
[10,13,9,9,14,10,11,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 107, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,14,15,12,15,13,15,12],
[9,0,13,15,11,10,11,9,12],
[11,12,0,13,8,12,14,11,15],
[10,10,12,0,11,8,12,9,12],
[13,14,17,14,0,16,15,10,16],
[10,15,13,17,9,0,13,12,14],
[12,14,11,13,10,12,0,8,12],
[10,16,14,16,15,13,17,0,17],
[13,13,10,13,9,11,13,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 108, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,6,9,5,11,10,10,13],
[17,0,7,9,13,8,14,9,17],
[19,18,0,15,16,9,16,16,20],
[16,16,10,0,16,10,13,11,15],
[20,12,9,9,0,10,16,9,14],
[14,17,16,15,15,0,11,16,16],
[15,11,9,12,9,14,0,9,12],
[15,16,9,14,16,9,16,0,23],
[12,8,5,10,11,9,13,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 109, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,12,13,14,14,15,11,10],
[13,0,12,12,17,16,15,10,13],
[13,13,0,11,13,18,15,13,14],
[12,13,14,0,15,14,15,12,11],
[11,8,12,10,0,12,15,12,13],
[11,9,7,11,13,0,16,11,12],
[10,10,10,10,10,9,0,10,9],
[14,15,12,13,13,14,15,0,14],
[15,12,11,14,12,13,16,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 110, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,10,12,14,13,10,11,9],
[14,0,5,12,12,11,5,18,11],
[15,20,0,19,14,22,12,19,21],
[13,13,6,0,9,18,9,20,11],
[11,13,11,16,0,18,14,16,15],
[12,14,3,7,7,0,3,17,4],
[15,20,13,16,11,22,0,17,19],
[14,7,6,5,9,8,8,0,7],
[16,14,4,14,10,21,6,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 111, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,14,10,11,11,8,10,7],
[14,0,18,7,11,13,13,11,10],
[11,7,0,5,10,4,3,5,5],
[15,18,20,0,16,14,12,12,13],
[14,14,15,9,0,13,12,10,11],
[14,12,21,11,12,0,9,13,11],
[17,12,22,13,13,16,0,13,14],
[15,14,20,13,15,12,12,0,16],
[18,15,20,12,14,14,11,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 112, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,17,25,17,25,16,8,8],
[16,0,17,16,8,25,16,8,16],
[8,8,0,8,8,8,8,16,8],
[0,9,17,0,17,9,0,8,8],
[8,17,17,8,0,17,8,16,8],
[0,0,17,16,8,0,8,8,8],
[9,9,17,25,17,17,0,8,17],
[17,17,9,17,9,17,17,0,17],
[17,9,17,17,17,17,8,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 113, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,14,9,17,9,14,10,13],
[10,0,11,7,12,11,13,8,9],
[11,14,0,14,12,10,9,11,12],
[16,18,11,0,14,11,13,13,12],
[8,13,13,11,0,9,14,10,11],
[16,14,15,14,16,0,14,12,19],
[11,12,16,12,11,11,0,11,15],
[15,17,14,12,15,13,14,0,15],
[12,16,13,13,14,6,10,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 114, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,15,8,15,11,11,8,12],
[7,0,15,13,7,7,10,9,7],
[10,10,0,9,10,6,6,6,8],
[17,12,16,0,12,15,16,13,16],
[10,18,15,13,0,13,16,18,13],
[14,18,19,10,12,0,19,16,22],
[14,15,19,9,9,6,0,12,16],
[17,16,19,12,7,9,13,0,16],
[13,18,17,9,12,3,9,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 115, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,17,11,11,17,15,15,19],
[6,0,14,8,10,6,12,13,13],
[8,11,0,7,8,9,13,12,13],
[14,17,18,0,9,16,23,13,16],
[14,15,17,16,0,12,18,14,19],
[8,19,16,9,13,0,14,13,15],
[10,13,12,2,7,11,0,9,12],
[10,12,13,12,11,12,16,0,14],
[6,12,12,9,6,10,13,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 116, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,12,10,10,13,14,11,18],
[7,0,12,14,10,11,13,4,12],
[13,13,0,10,8,13,10,7,20],
[15,11,15,0,15,11,8,9,14],
[15,15,17,10,0,13,10,6,13],
[12,14,12,14,12,0,18,14,15],
[11,12,15,17,15,7,0,13,18],
[14,21,18,16,19,11,12,0,15],
[7,13,5,11,12,10,7,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 117, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,24,18,9,18,18,9,25],
[1,0,6,0,9,0,0,10,25],
[1,19,0,19,10,18,19,10,25],
[7,25,6,0,9,0,1,10,25],
[16,16,15,16,0,15,16,7,16],
[7,25,7,25,10,0,19,16,25],
[7,25,6,24,9,6,0,16,25],
[16,15,15,15,18,9,9,0,16],
[0,0,0,0,9,0,0,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 118, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,9,10,12,13,8,11,11],
[17,0,15,14,15,16,12,16,12],
[16,10,0,13,15,12,12,12,10],
[15,11,12,0,14,11,11,12,11],
[13,10,10,11,0,12,12,11,11],
[12,9,13,14,13,0,12,14,14],
[17,13,13,14,13,13,0,13,11],
[14,9,13,13,14,11,12,0,11],
[14,13,15,14,14,11,14,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 119, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,14,21,10,11,18,18,25],
[21,0,10,17,13,17,14,18,21],
[11,15,0,15,11,11,12,12,21],
[4,8,10,0,4,4,8,8,14],
[15,12,14,21,0,15,12,12,21],
[14,8,14,21,10,0,18,18,21],
[7,11,13,17,13,7,0,11,17],
[7,7,13,17,13,7,14,0,17],
[0,4,4,11,4,4,8,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 120, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,13,11,15,8,13,13,10],
[11,0,11,10,14,8,11,13,10],
[12,14,0,10,15,11,11,14,13],
[14,15,15,0,17,10,11,17,9],
[10,11,10,8,0,7,7,11,8],
[17,17,14,15,18,0,12,17,16],
[12,14,14,14,18,13,0,17,15],
[12,12,11,8,14,8,8,0,8],
[15,15,12,16,17,9,10,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 121, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,11,15,16,11,14,15,15],
[12,0,16,15,14,13,16,20,20],
[14,9,0,11,13,10,16,15,12],
[10,10,14,0,12,10,16,15,18],
[9,11,12,13,0,9,16,17,18],
[14,12,15,15,16,0,14,22,20],
[11,9,9,9,9,11,0,16,14],
[10,5,10,10,8,3,9,0,12],
[10,5,13,7,7,5,11,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 122, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,11,10,13,12,14,11,15],
[12,0,12,10,10,10,14,12,11],
[14,13,0,15,14,12,15,14,14],
[15,15,10,0,10,8,14,14,10],
[12,15,11,15,0,10,16,13,11],
[13,15,13,17,15,0,14,11,13],
[11,11,10,11,9,11,0,10,13],
[14,13,11,11,12,14,15,0,15],
[10,14,11,15,14,12,12,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 123, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,6,7,7,10,8,5,10],
[16,0,15,15,11,12,13,12,18],
[19,10,0,11,14,11,14,7,12],
[18,10,14,0,12,12,10,6,13],
[18,14,11,13,0,10,8,8,10],
[15,13,14,13,15,0,13,15,12],
[17,12,11,15,17,12,0,8,10],
[20,13,18,19,17,10,17,0,17],
[15,7,13,12,15,13,15,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 124, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,13,14,17,15,10,14,11],
[13,0,13,13,11,13,14,17,13],
[12,12,0,12,12,14,8,14,10],
[11,12,13,0,15,14,16,14,11],
[8,14,13,10,0,14,13,15,10],
[10,12,11,11,11,0,10,14,10],
[15,11,17,9,12,15,0,16,11],
[11,8,11,11,10,11,9,0,10],
[14,12,15,14,15,15,14,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 125, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,9,14,11,7,10,12,9],
[17,0,13,15,16,14,14,9,16],
[16,12,0,13,15,12,9,11,15],
[11,10,12,0,11,6,14,8,10],
[14,9,10,14,0,13,11,13,12],
[18,11,13,19,12,0,15,15,12],
[15,11,16,11,14,10,0,9,13],
[13,16,14,17,12,10,16,0,15],
[16,9,10,15,13,13,12,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 126, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,13,14,6,12,14,13,11],
[8,0,5,9,11,10,9,8,7],
[12,20,0,15,14,14,16,16,14],
[11,16,10,0,10,13,18,12,10],
[19,14,11,15,0,18,16,12,14],
[13,15,11,12,7,0,16,12,10],
[11,16,9,7,9,9,0,8,10],
[12,17,9,13,13,13,17,0,10],
[14,18,11,15,11,15,15,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 127, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,15,13,15,11,9,15,15],
[14,0,11,6,6,4,6,8,11],
[10,14,0,14,2,14,6,8,2],
[12,19,11,0,12,18,12,14,12],
[10,19,23,13,0,17,17,11,11],
[14,21,11,7,8,0,9,15,9],
[16,19,19,13,8,16,0,17,11],
[10,17,17,11,14,10,8,0,17],
[10,14,23,13,14,16,14,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 128, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,7,0,10,8,16,2,12],
[17,0,9,2,12,7,18,6,13],
[18,16,0,0,12,11,13,6,12],
[25,23,25,0,24,11,25,18,23],
[15,13,13,1,0,7,16,10,2],
[17,18,14,14,18,0,17,12,20],
[9,7,12,0,9,8,0,10,3],
[23,19,19,7,15,13,15,0,11],
[13,12,13,2,23,5,22,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 129, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,13,10,11,12,13,6,6],
[16,0,12,11,10,13,11,10,11],
[12,13,0,12,13,15,12,10,9],
[15,14,13,0,9,21,13,13,15],
[14,15,12,16,0,14,11,12,12],
[13,12,10,4,11,0,14,5,10],
[12,14,13,12,14,11,0,10,8],
[19,15,15,12,13,20,15,0,14],
[19,14,16,10,13,15,17,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 130, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,10,12,12,8,12,12,4],
[12,0,16,20,14,11,14,16,12],
[15,9,0,13,4,12,11,15,8],
[13,5,12,0,12,7,10,16,13],
[13,11,21,13,0,13,12,17,17],
[17,14,13,18,12,0,16,17,10],
[13,11,14,15,13,9,0,13,9],
[13,9,10,9,8,8,12,0,8],
[21,13,17,12,8,15,16,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 131, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,10,2,2,2,8,8,8],
[23,0,25,25,7,7,15,23,23],
[15,0,0,7,7,7,8,8,15],
[23,0,18,0,7,0,8,8,16],
[23,18,18,18,0,8,8,16,16],
[23,18,18,25,17,0,8,16,16],
[17,10,17,17,17,17,0,10,17],
[17,2,17,17,9,9,15,0,17],
[17,2,10,9,9,9,8,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 132, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,12,11,11,13,11,19],
[12,0,12,10,15,15,14,17,16],
[12,13,0,12,9,15,12,15,15],
[13,15,13,0,16,11,16,15,16],
[14,10,16,9,0,17,15,17,19],
[14,10,10,14,8,0,11,11,14],
[12,11,13,9,10,14,0,10,13],
[14,8,10,10,8,14,15,0,16],
[6,9,10,9,6,11,12,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 133, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,10,15,8,13,7,7,12],
[10,0,8,13,8,9,6,8,7],
[15,17,0,17,12,16,12,12,15],
[10,12,8,0,10,10,8,9,8],
[17,17,13,15,0,16,13,12,14],
[12,16,9,15,9,0,12,13,14],
[18,19,13,17,12,13,0,15,18],
[18,17,13,16,13,12,10,0,17],
[13,18,10,17,11,11,7,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 134, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,12,7,9,12,9,13,5],
[16,0,22,14,16,16,13,14,12],
[13,3,0,13,10,9,12,14,12],
[18,11,12,0,8,9,8,16,12],
[16,9,15,17,0,12,12,23,15],
[13,9,16,16,13,0,7,20,12],
[16,12,13,17,13,18,0,20,18],
[12,11,11,9,2,5,5,0,9],
[20,13,13,13,10,13,7,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 135, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,20,19,15,15,12,15,15],
[12,0,13,11,11,9,13,11,11],
[5,12,0,9,5,12,7,10,12],
[6,14,16,0,7,14,9,13,12],
[10,14,20,18,0,11,14,15,14],
[10,16,13,11,14,0,16,17,15],
[13,12,18,16,11,9,0,10,14],
[10,14,15,12,10,8,15,0,9],
[10,14,13,13,11,10,11,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 136, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,13,13,12,16,12,13],
[12,0,14,15,14,12,14,11,14],
[12,11,0,15,10,14,12,12,14],
[12,10,10,0,10,9,12,9,15],
[12,11,15,15,0,13,16,13,13],
[13,13,11,16,12,0,13,9,12],
[9,11,13,13,9,12,0,11,13],
[13,14,13,16,12,16,14,0,14],
[12,11,11,10,12,13,12,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 137, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,21,12,22,17,23,21,21],
[11,0,10,12,11,18,11,18,17],
[4,15,0,6,5,9,6,15,12],
[13,13,19,0,14,20,11,24,23],
[3,14,20,11,0,19,8,23,14],
[8,7,16,5,6,0,6,24,7],
[2,14,19,14,17,19,0,22,14],
[4,7,10,1,2,1,3,0,1],
[4,8,13,2,11,18,11,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 138, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,12,9,13,12,12,15],
[12,0,13,16,17,15,14,7,10],
[12,12,0,19,14,18,17,12,15],
[13,9,6,0,18,9,10,13,16],
[16,8,11,7,0,6,15,7,11],
[12,10,7,16,19,0,18,11,14],
[13,11,8,15,10,7,0,15,15],
[13,18,13,12,18,14,10,0,18],
[10,15,10,9,14,11,10,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 139, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,14,23,15,12,19,6,25],
[16,0,15,16,12,12,10,12,16],
[11,10,0,11,12,7,14,3,11],
[2,9,14,0,12,6,13,1,11],
[10,13,13,13,0,15,17,9,15],
[13,13,18,19,10,0,17,14,19],
[6,15,11,12,8,8,0,7,12],
[19,13,22,24,16,11,18,0,24],
[0,9,14,14,10,6,13,1,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 140, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,12,12,7,10,10,10,13],
[12,0,3,8,5,5,6,11,9],
[13,22,0,20,12,13,10,16,15],
[13,17,5,0,6,8,7,13,9],
[18,20,13,19,0,11,15,16,19],
[15,20,12,17,14,0,13,17,13],
[15,19,15,18,10,12,0,14,16],
[15,14,9,12,9,8,11,0,13],
[12,16,10,16,6,12,9,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 141, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,12,16,11,11,13,13,12],
[10,0,12,12,2,8,8,11,12],
[13,13,0,16,7,10,9,13,11],
[9,13,9,0,8,10,12,10,10],
[14,23,18,17,0,17,12,15,19],
[14,17,15,15,8,0,11,14,11],
[12,17,16,13,13,14,0,9,18],
[12,14,12,15,10,11,16,0,13],
[13,13,14,15,6,14,7,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 142, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1,18,9,16,9,24,1,10],
[24,0,18,9,15,15,24,16,25],
[7,7,0,9,15,15,24,8,8],
[16,16,16,0,16,7,24,8,17],
[9,10,10,9,0,0,17,1,10],
[16,10,10,18,25,0,24,10,17],
[1,1,1,1,8,1,0,1,1],
[24,9,17,17,24,15,24,0,24],
[15,0,17,8,15,8,24,1,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 143, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,12,12,7,11,10,12,11],
[12,0,12,14,11,10,12,14,11],
[13,13,0,15,10,12,14,10,9],
[13,11,10,0,8,10,11,11,12],
[18,14,15,17,0,18,15,12,14],
[14,15,13,15,7,0,9,10,16],
[15,13,11,14,10,16,0,11,10],
[13,11,15,14,13,15,14,0,10],
[14,14,16,13,11,9,15,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 144, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,13,8,8,10,15,9],
[14,0,16,18,16,17,11,15,18],
[14,9,0,13,5,12,10,11,13],
[12,7,12,0,8,9,9,11,9],
[17,9,20,17,0,11,10,15,9],
[17,8,13,16,14,0,9,12,12],
[15,14,15,16,15,16,0,14,8],
[10,10,14,14,10,13,11,0,14],
[16,7,12,16,16,13,17,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 145, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,7,11,0,16,7,7,10],
[18,0,13,11,18,11,17,23,11],
[18,12,0,16,18,23,12,23,23],
[14,14,9,0,7,20,14,19,12],
[25,7,7,18,0,18,14,25,12],
[9,14,2,5,7,0,14,14,0],
[18,8,13,11,11,11,0,25,11],
[18,2,2,6,0,11,0,0,5],
[15,14,2,13,13,25,14,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 146, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,9,13,13,17,18,19,9],
[14,0,11,10,10,16,19,19,11],
[16,14,0,11,14,19,19,17,13],
[12,15,14,0,13,20,23,18,6],
[12,15,11,12,0,16,18,14,15],
[8,9,6,5,9,0,17,10,6],
[7,6,6,2,7,8,0,4,4],
[6,6,8,7,11,15,21,0,4],
[16,14,12,19,10,19,21,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 147, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,18,19,19,9,17,16,14],
[11,0,14,12,15,13,10,16,12],
[7,11,0,12,13,6,11,13,8],
[6,13,13,0,19,10,11,14,15],
[6,10,12,6,0,7,10,7,15],
[16,12,19,15,18,0,8,19,15],
[8,15,14,14,15,17,0,19,15],
[9,9,12,11,18,6,6,0,15],
[11,13,17,10,10,10,10,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 148, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,13,10,15,12,11,11,12],
[14,0,11,10,11,13,11,10,12],
[12,14,0,15,17,13,12,14,13],
[15,15,10,0,9,11,12,11,16],
[10,14,8,16,0,12,13,12,13],
[13,12,12,14,13,0,11,10,14],
[14,14,13,13,12,14,0,14,14],
[14,15,11,14,13,15,11,0,14],
[13,13,12,9,12,11,11,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 149, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,10,16,13,9,16,13,13],
[11,0,13,16,11,12,18,15,9],
[15,12,0,15,9,9,18,16,13],
[9,9,10,0,10,10,13,13,10],
[12,14,16,15,0,11,16,11,10],
[16,13,16,15,14,0,15,15,12],
[9,7,7,12,9,10,0,13,6],
[12,10,9,12,14,10,12,0,10],
[12,16,12,15,15,13,19,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 150, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,13,6,11,12,8,5,14],
[17,0,17,15,19,14,17,10,17],
[12,8,0,10,9,8,13,4,12],
[19,10,15,0,12,12,13,15,19],
[14,6,16,13,0,6,19,9,15],
[13,11,17,13,19,0,15,9,15],
[17,8,12,12,6,10,0,11,19],
[20,15,21,10,16,16,14,0,20],
[11,8,13,6,10,10,6,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 151, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,20,19,19,20,25,13,8],
[1,0,1,1,9,1,6,1,1],
[5,24,0,5,8,1,6,5,0],
[6,24,20,0,8,9,6,5,8],
[6,16,17,17,0,6,17,5,5],
[5,24,24,16,19,0,16,5,8],
[0,19,19,19,8,9,0,8,8],
[12,24,20,20,20,20,17,0,19],
[17,24,25,17,20,17,17,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 152, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,5,12,12,10,11,6,11],
[19,0,15,12,10,9,11,9,18],
[20,10,0,14,13,13,15,14,19],
[13,13,11,0,10,5,6,9,18],
[13,15,12,15,0,14,19,10,24],
[15,16,12,20,11,0,15,13,21],
[14,14,10,19,6,10,0,11,25],
[19,16,11,16,15,12,14,0,20],
[14,7,6,7,1,4,0,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 153, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,9,13,14,16,11,15,10],
[16,0,12,15,14,17,15,16,13],
[16,13,0,17,16,12,14,14,9],
[12,10,8,0,9,12,10,9,9],
[11,11,9,16,0,13,10,13,11],
[9,8,13,13,12,0,12,12,7],
[14,10,11,15,15,13,0,13,13],
[10,9,11,16,12,13,12,0,8],
[15,12,16,16,14,18,12,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 154, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,11,14,7,6,7,9,10],
[20,0,15,16,16,11,14,12,14],
[14,10,0,15,10,9,11,14,9],
[11,9,10,0,10,9,8,9,9],
[18,9,15,15,0,16,14,12,15],
[19,14,16,16,9,0,12,10,15],
[18,11,14,17,11,13,0,14,15],
[16,13,11,16,13,15,11,0,14],
[15,11,16,16,10,10,10,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 155, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,21,16,25,10,15,15,14],
[6,0,19,3,12,6,3,3,9],
[4,6,0,7,18,4,2,3,1],
[9,22,18,0,12,9,18,8,10],
[0,13,7,13,0,7,7,0,8],
[15,19,21,16,18,0,15,8,20],
[10,22,23,7,18,10,0,1,16],
[10,22,22,17,25,17,24,0,23],
[11,16,24,15,17,5,9,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 156, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,16,8,12,10,15,10,11],
[12,0,16,9,14,14,14,14,14],
[9,9,0,4,10,11,11,7,8],
[17,16,21,0,17,14,16,14,10],
[13,11,15,8,0,10,16,14,11],
[15,11,14,11,15,0,16,10,13],
[10,11,14,9,9,9,0,9,11],
[15,11,18,11,11,15,16,0,10],
[14,11,17,15,14,12,14,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 157, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,13,14,10,16,9,14,15],
[15,0,10,12,14,15,9,11,12],
[12,15,0,13,11,14,16,12,12],
[11,13,12,0,11,15,12,12,10],
[15,11,14,14,0,19,14,13,14],
[9,10,11,10,6,0,11,9,12],
[16,16,9,13,11,14,0,11,9],
[11,14,13,13,12,16,14,0,12],
[10,13,13,15,11,13,16,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 158, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,8,10,15,8,13,11],
[15,0,7,17,10,12,13,15,16],
[15,18,0,18,13,16,14,17,12],
[17,8,7,0,13,10,13,15,11],
[15,15,12,12,0,10,13,17,15],
[10,13,9,15,15,0,13,15,11],
[17,12,11,12,12,12,0,17,11],
[12,10,8,10,8,10,8,0,15],
[14,9,13,14,10,14,14,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 159, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,22,15,10,25,25,19,25],
[8,0,14,7,0,15,17,11,17],
[3,11,0,15,11,19,19,11,11],
[10,18,10,0,18,19,18,11,19],
[15,25,14,7,0,15,17,11,17],
[0,10,6,6,10,0,16,3,11],
[0,8,6,7,8,9,0,1,9],
[6,14,14,14,14,22,24,0,17],
[0,8,14,6,8,14,16,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 160, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,5,11,7,3,9,9,7],
[18,0,18,14,18,7,18,14,18],
[20,7,0,6,16,7,13,12,16],
[14,11,19,0,10,14,14,10,10],
[18,7,9,15,0,7,15,9,17],
[22,18,18,11,18,0,18,17,21],
[16,7,12,11,10,7,0,12,10],
[16,11,13,15,16,8,13,0,11],
[18,7,9,15,8,4,15,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 161, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,15,18,14,13,13,11,12],
[15,0,15,15,15,18,12,12,15],
[10,10,0,13,18,18,15,9,17],
[7,10,12,0,11,12,9,10,15],
[11,10,7,14,0,18,13,8,11],
[12,7,7,13,7,0,11,8,11],
[12,13,10,16,12,14,0,8,12],
[14,13,16,15,17,17,17,0,11],
[13,10,8,10,14,14,13,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 162, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,7,11,7,8,11,8,8],
[18,0,15,16,14,12,15,11,14],
[18,10,0,14,13,13,16,10,14],
[14,9,11,0,11,11,16,9,10],
[18,11,12,14,0,10,17,13,13],
[17,13,12,14,15,0,16,9,13],
[14,10,9,9,8,9,0,5,12],
[17,14,15,16,12,16,20,0,16],
[17,11,11,15,12,12,13,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 163, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,15,21,12,20,16,17,18],
[6,0,12,14,8,13,9,13,12],
[10,13,0,14,15,17,13,15,15],
[4,11,11,0,11,13,10,12,10],
[13,17,10,14,0,12,18,13,12],
[5,12,8,12,13,0,12,18,9],
[9,16,12,15,7,13,0,10,14],
[8,12,10,13,12,7,15,0,8],
[7,13,10,15,13,16,11,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 164, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,10,13,11,10,12,15,10],
[10,0,12,12,11,11,13,12,11],
[15,13,0,10,11,14,15,13,9],
[12,13,15,0,16,13,13,16,11],
[14,14,14,9,0,8,14,15,14],
[15,14,11,12,17,0,15,17,13],
[13,12,10,12,11,10,0,13,14],
[10,13,12,9,10,8,12,0,10],
[15,14,16,14,11,12,11,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 165, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,13,17,17,11,14,11,13],
[8,0,10,16,12,11,9,14,14],
[12,15,0,20,19,15,12,18,13],
[8,9,5,0,11,9,7,14,4],
[8,13,6,14,0,10,6,11,9],
[14,14,10,16,15,0,15,11,14],
[11,16,13,18,19,10,0,16,13],
[14,11,7,11,14,14,9,0,9],
[12,11,12,21,16,11,12,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 166, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,10,8,13,10,11,10,8],
[12,0,8,8,11,11,10,10,11],
[15,17,0,12,15,14,14,13,13],
[17,17,13,0,17,18,19,17,12],
[12,14,10,8,0,11,13,10,10],
[15,14,11,7,14,0,17,15,11],
[14,15,11,6,12,8,0,12,10],
[15,15,12,8,15,10,13,0,8],
[17,14,12,13,15,14,15,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 167, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,21,23,10,3,23,2,23],
[1,0,12,10,1,1,24,1,22],
[4,13,0,13,1,3,13,2,13],
[2,15,12,0,2,3,15,1,15],
[15,24,24,23,0,3,25,13,23],
[22,24,22,22,22,0,24,12,22],
[2,1,12,10,0,1,0,0,0],
[23,24,23,24,12,13,25,0,24],
[2,3,12,10,2,3,25,1,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 168, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,9,9,15,10,13,13,12],
[13,0,16,11,16,13,15,14,11],
[16,9,0,11,15,15,11,17,15],
[16,14,14,0,14,12,14,15,10],
[10,9,10,11,0,9,13,12,12],
[15,12,10,13,16,0,14,11,13],
[12,10,14,11,12,11,0,13,12],
[12,11,8,10,13,14,12,0,8],
[13,14,10,15,13,12,13,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 169, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,8,13,9,11,7,13,12],
[18,0,14,16,15,17,10,13,14],
[17,11,0,15,15,15,13,11,8],
[12,9,10,0,13,9,12,8,11],
[16,10,10,12,0,12,9,13,6],
[14,8,10,16,13,0,6,12,11],
[18,15,12,13,16,19,0,15,11],
[12,12,14,17,12,13,10,0,16],
[13,11,17,14,19,14,14,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 170, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,12,13,12,18,13,13,13],
[11,0,11,10,11,14,12,14,11],
[13,14,0,11,14,16,12,13,11],
[12,15,14,0,15,18,16,15,14],
[13,14,11,10,0,13,13,13,13],
[7,11,9,7,12,0,10,8,9],
[12,13,13,9,12,15,0,13,8],
[12,11,12,10,12,17,12,0,11],
[12,14,14,11,12,16,17,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 171, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,12,17,11,12,13,11,15],
[13,0,12,13,13,17,11,15,14],
[13,13,0,17,13,18,9,16,16],
[8,12,8,0,8,15,11,12,11],
[14,12,12,17,0,14,13,14,16],
[13,8,7,10,11,0,5,9,8],
[12,14,16,14,12,20,0,15,15],
[14,10,9,13,11,16,10,0,14],
[10,11,9,14,9,17,10,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 172, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,13,18,13,10,8,11,8],
[16,0,10,20,16,10,8,12,12],
[12,15,0,16,12,12,10,12,12],
[7,5,9,0,8,8,6,2,8],
[12,9,13,17,0,13,14,9,11],
[15,15,13,17,12,0,14,13,14],
[17,17,15,19,11,11,0,16,11],
[14,13,13,23,16,12,9,0,11],
[17,13,13,17,14,11,14,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 173, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,11,15,16,10,16,2,10],
[7,0,10,4,8,10,12,5,4],
[14,15,0,13,11,13,14,14,10],
[10,21,12,0,12,12,13,9,12],
[9,17,14,13,0,13,16,9,11],
[15,15,12,13,12,0,23,15,17],
[9,13,11,12,9,2,0,8,9],
[23,20,11,16,16,10,17,0,12],
[15,21,15,13,14,8,16,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 174, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,12,9,14,17,14,11,15],
[14,0,14,17,13,19,17,13,11],
[13,11,0,16,17,20,19,17,15],
[16,8,9,0,14,14,17,12,16],
[11,12,8,11,0,12,11,3,6],
[8,6,5,11,13,0,6,9,12],
[11,8,6,8,14,19,0,12,11],
[14,12,8,13,22,16,13,0,16],
[10,14,10,9,19,13,14,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 175, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,13,17,13,11,16,16,15],
[10,0,11,15,9,9,13,14,13],
[12,14,0,19,15,16,17,12,20],
[8,10,6,0,12,14,14,12,12],
[12,16,10,13,0,17,14,17,12],
[14,16,9,11,8,0,14,12,15],
[9,12,8,11,11,11,0,10,11],
[9,11,13,13,8,13,15,0,15],
[10,12,5,13,13,10,14,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 176, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,11,14,16,9,16,14,10],
[16,0,12,17,15,14,14,12,12],
[14,13,0,11,13,14,18,9,11],
[11,8,14,0,17,15,17,12,13],
[9,10,12,8,0,12,18,7,11],
[16,11,11,10,13,0,14,11,9],
[9,11,7,8,7,11,0,5,7],
[11,13,16,13,18,14,20,0,15],
[15,13,14,12,14,16,18,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 177, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,15,16,17,15,20,15,16],
[13,0,19,12,10,12,25,17,7],
[10,6,0,13,11,10,18,13,8],
[9,13,12,0,13,7,14,7,8],
[8,15,14,12,0,12,16,12,11],
[10,13,15,18,13,0,21,18,14],
[5,0,7,11,9,4,0,3,3],
[10,8,12,18,13,7,22,0,10],
[9,18,17,17,14,11,22,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 178, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,14,20,13,18,19,15],
[15,0,13,15,14,10,14,14,20],
[15,12,0,10,20,13,19,15,12],
[11,10,15,0,15,11,11,16,11],
[5,11,5,10,0,4,11,8,10],
[12,15,12,14,21,0,20,15,15],
[7,11,6,14,14,5,0,8,10],
[6,11,10,9,17,10,17,0,8],
[10,5,13,14,15,10,15,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 179, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,8,12,12,7,12,14,17],
[21,0,7,20,16,19,22,22,19],
[17,18,0,17,14,12,21,21,18],
[13,5,8,0,7,8,14,14,14],
[13,9,11,18,0,12,17,16,22],
[18,6,13,17,13,0,16,17,15],
[13,3,4,11,8,9,0,14,16],
[11,3,4,11,9,8,11,0,10],
[8,6,7,11,3,10,9,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 180, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,7,9,9,11,12,12,10],
[11,0,7,9,4,5,6,6,8],
[18,18,0,14,10,13,15,14,13],
[16,16,11,0,13,13,16,14,13],
[16,21,15,12,0,14,14,14,10],
[14,20,12,12,11,0,20,12,14],
[13,19,10,9,11,5,0,6,6],
[13,19,11,11,11,13,19,0,16],
[15,17,12,12,15,11,19,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 181, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,6,6,6,6,15,6,6],
[10,0,16,16,16,10,25,16,16],
[19,9,0,19,19,19,25,19,19],
[19,9,6,0,0,0,15,10,25],
[19,9,6,25,0,19,15,19,25],
[19,15,6,25,6,0,15,16,25],
[10,0,0,10,10,10,0,10,10],
[19,9,6,15,6,9,15,0,15],
[19,9,6,0,0,0,15,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 182, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,18,19,14,18,23,14,18],
[14,0,14,14,14,16,23,19,7],
[7,11,0,9,7,16,23,14,5],
[6,11,16,0,5,18,16,5,11],
[11,11,18,20,0,18,16,13,18],
[7,9,9,7,7,0,14,12,9],
[2,2,2,9,9,11,0,2,7],
[11,6,11,20,12,13,23,0,11],
[7,18,20,14,7,16,18,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 183, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,12,7,9,16,14,14,14],
[17,0,10,10,13,18,15,13,14],
[13,15,0,10,14,18,17,15,14],
[18,15,15,0,13,19,14,12,13],
[16,12,11,12,0,15,20,12,16],
[9,7,7,6,10,0,13,13,11],
[11,10,8,11,5,12,0,9,10],
[11,12,10,13,13,12,16,0,9],
[11,11,11,12,9,14,15,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 184, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,15,8,10,13,9,10,8],
[14,0,14,13,8,13,13,12,12],
[10,11,0,14,9,11,9,8,8],
[17,12,11,0,12,13,12,11,10],
[15,17,16,13,0,17,12,13,11],
[12,12,14,12,8,0,12,11,12],
[16,12,16,13,13,13,0,13,13],
[15,13,17,14,12,14,12,0,10],
[17,13,17,15,14,13,12,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 185, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,12,15,15,15,17,12,13],
[6,0,9,16,11,9,11,10,9],
[13,16,0,13,12,15,20,13,7],
[10,9,12,0,9,9,11,7,8],
[10,14,13,16,0,17,18,16,12],
[10,16,10,16,8,0,14,14,9],
[8,14,5,14,7,11,0,11,9],
[13,15,12,18,9,11,14,0,10],
[12,16,18,17,13,16,16,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 186, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,12,15,11,9,10,15,8],
[12,0,7,14,10,6,11,14,7],
[13,18,0,16,15,11,11,18,11],
[10,11,9,0,15,10,12,13,5],
[14,15,10,10,0,9,14,16,6],
[16,19,14,15,16,0,17,20,9],
[15,14,14,13,11,8,0,15,13],
[10,11,7,12,9,5,10,0,7],
[17,18,14,20,19,16,12,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 187, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,10,17,12,11,14,9,9],
[13,0,10,13,12,11,12,10,10],
[15,15,0,15,13,12,15,8,11],
[8,12,10,0,12,10,13,11,10],
[13,13,12,13,0,13,13,10,13],
[14,14,13,15,12,0,16,13,14],
[11,13,10,12,12,9,0,10,10],
[16,15,17,14,15,12,15,0,14],
[16,15,14,15,12,11,15,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 188, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,14,12,11,9,8,14],
[14,0,11,16,15,15,13,11,15],
[14,14,0,16,14,14,9,14,15],
[11,9,9,0,7,8,8,9,13],
[13,10,11,18,0,13,12,12,11],
[14,10,11,17,12,0,12,11,16],
[16,12,16,17,13,13,0,12,15],
[17,14,11,16,13,14,13,0,16],
[11,10,10,12,14,9,10,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 189, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,11,10,9,10,13,9,12],
[16,0,13,9,10,11,14,9,12],
[14,12,0,13,4,11,12,13,12],
[15,16,12,0,12,14,14,16,14],
[16,15,21,13,0,15,18,11,15],
[15,14,14,11,10,0,16,13,11],
[12,11,13,11,7,9,0,9,9],
[16,16,12,9,14,12,16,0,12],
[13,13,13,11,10,14,16,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 190, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,3,8,3,11,6,2,10],
[22,0,9,6,10,15,14,16,8],
[22,16,0,6,10,14,14,22,22],
[17,19,19,0,11,9,9,16,18],
[22,15,15,14,0,15,6,14,22],
[14,10,11,16,10,0,14,10,18],
[19,11,11,16,19,11,0,18,18],
[23,9,3,9,11,15,7,0,17],
[15,17,3,7,3,7,7,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 191, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,12,13,12,11,10,14,16],
[16,0,10,15,14,16,10,17,12],
[13,15,0,12,15,17,14,17,15],
[12,10,13,0,11,13,10,12,13],
[13,11,10,14,0,13,8,15,14],
[14,9,8,12,12,0,10,17,13],
[15,15,11,15,17,15,0,13,13],
[11,8,8,13,10,8,12,0,7],
[9,13,10,12,11,12,12,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 192, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,14,5,18,12,13,20,7],
[14,0,15,10,16,10,14,21,14],
[11,10,0,6,15,10,13,9,6],
[20,15,19,0,16,13,13,16,5],
[7,9,10,9,0,11,10,7,6],
[13,15,15,12,14,0,13,20,12],
[12,11,12,12,15,12,0,12,5],
[5,4,16,9,18,5,13,0,11],
[18,11,19,20,19,13,20,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 193, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,18,17,13,7,11,12,18],
[1,0,14,4,14,0,7,12,5],
[7,11,0,11,13,7,14,19,12],
[8,21,14,0,14,8,14,12,5],
[12,11,12,11,0,7,12,12,12],
[18,25,18,17,18,0,18,12,11],
[14,18,11,11,13,7,0,18,11],
[13,13,6,13,13,13,7,0,17],
[7,20,13,20,13,14,14,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 194, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,6,10,9,7,15,8,11],
[13,0,7,12,13,9,13,9,7],
[19,18,0,18,15,16,13,12,11],
[15,13,7,0,11,15,11,11,8],
[16,12,10,14,0,11,11,12,12],
[18,16,9,10,14,0,14,13,13],
[10,12,12,14,14,11,0,8,8],
[17,16,13,14,13,12,17,0,10],
[14,18,14,17,13,12,17,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 195, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,17,17,17,8,8,17,17],
[17,0,14,17,14,22,13,9,17],
[8,11,0,11,3,16,13,0,11],
[8,8,14,0,17,5,13,5,17],
[8,11,22,8,0,13,13,0,16],
[17,3,9,20,12,0,13,9,12],
[17,12,12,12,12,12,0,9,12],
[8,16,25,20,25,16,16,0,25],
[8,8,14,8,9,13,13,0,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 196, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,19,8,19,19,19,12,12],
[16,0,17,10,17,17,17,16,16],
[6,8,0,8,14,15,20,8,8],
[17,15,17,0,11,17,17,11,16],
[6,8,11,14,0,23,20,6,12],
[6,8,10,8,2,0,14,6,12],
[6,8,5,8,5,11,0,4,10],
[13,9,17,14,19,19,21,0,18],
[13,9,17,9,13,13,15,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 197, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,9,15,10,10,12,13,13],
[11,0,4,8,6,14,11,10,13],
[16,21,0,16,12,17,14,17,14],
[10,17,9,0,7,13,7,10,12],
[15,19,13,18,0,11,15,17,8],
[15,11,8,12,14,0,11,13,17],
[13,14,11,18,10,14,0,16,16],
[12,15,8,15,8,12,9,0,13],
[12,12,11,13,17,8,9,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 198, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,12,11,18,7,4,8,12],
[17,0,17,13,13,12,17,19,10],
[13,8,0,11,12,7,5,11,10],
[14,12,14,0,15,14,5,15,16],
[7,12,13,10,0,11,6,11,6],
[18,13,18,11,14,0,11,15,13],
[21,8,20,20,19,14,0,14,17],
[17,6,14,10,14,10,11,0,11],
[13,15,15,9,19,12,8,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 199, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,13,17,6,6,13,16,18],
[4,0,4,9,5,8,7,9,8],
[12,21,0,16,16,15,12,14,12],
[8,16,9,0,10,9,9,13,9],
[19,20,9,15,0,18,9,20,20],
[19,17,10,16,7,0,9,20,16],
[12,18,13,16,16,16,0,12,13],
[9,16,11,12,5,5,13,0,11],
[7,17,13,16,5,9,12,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 25, 200, "ME-BBRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbrcw/mebbrcw_9_25.csv", index=False, header=False)