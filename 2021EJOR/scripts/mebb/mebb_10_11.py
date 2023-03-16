
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,5,5,3,2,0,3,4,4,3],
[6,0,6,5,2,2,2,5,7,5],
[6,5,0,6,5,2,2,4,6,6],
[8,6,5,0,2,3,2,5,7,4],
[9,9,6,9,0,6,5,8,10,9],
[11,9,9,8,5,0,7,9,10,9],
[8,9,9,9,6,4,0,5,7,8],
[7,6,7,6,3,2,6,0,6,4],
[7,4,5,4,1,1,4,5,0,4],
[8,6,5,7,2,2,3,7,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 1, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,5,6,4,4,4,5,5,6],
[6,0,6,8,3,4,5,4,7,6],
[6,5,0,6,7,8,6,7,6,6],
[5,3,5,0,4,4,4,5,7,5],
[7,8,4,7,0,4,4,5,7,7],
[7,7,3,7,7,0,5,5,6,7],
[7,6,5,7,7,6,0,6,4,8],
[6,7,4,6,6,6,5,0,8,5],
[6,4,5,4,4,5,7,3,0,6],
[5,5,5,6,4,4,3,6,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 2, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,5,6,7,4,4,8,6,6],
[4,0,4,5,6,4,4,6,6,3],
[6,7,0,5,5,4,6,7,7,5],
[5,6,6,0,7,3,4,6,6,6],
[4,5,6,4,0,3,6,8,8,6],
[7,7,7,8,8,0,5,8,10,8],
[7,7,5,7,5,6,0,7,5,5],
[3,5,4,5,3,3,4,0,7,3],
[5,5,4,5,3,1,6,4,0,3],
[5,8,6,5,5,3,6,8,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 3, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,5,6,7,5,6,5,5,5],
[4,0,5,7,6,8,7,5,7,5],
[6,6,0,6,6,9,8,5,7,7],
[5,4,5,0,6,5,6,5,4,3],
[4,5,5,5,0,5,7,5,4,3],
[6,3,2,6,6,0,4,4,4,7],
[5,4,3,5,4,7,0,2,4,4],
[6,6,6,6,6,7,9,0,7,5],
[6,4,4,7,7,7,7,4,0,5],
[6,6,4,8,8,4,7,6,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 4, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,7,7,4,5,5,0,5,7],
[4,0,8,4,4,4,6,2,6,4],
[4,3,0,2,4,4,6,2,4,4],
[4,7,9,0,4,5,4,2,4,7],
[7,7,7,7,0,5,7,7,7,7],
[6,7,7,6,6,0,2,4,2,6],
[6,5,5,7,4,9,0,4,4,9],
[11,9,9,9,4,7,7,0,7,11],
[6,5,7,7,4,9,7,4,0,9],
[4,7,7,4,4,5,2,0,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 5, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,6,8,5,4,7,6,6,6],
[6,0,6,7,2,3,4,4,3,2],
[5,5,0,6,6,2,6,5,5,3],
[3,4,5,0,1,3,2,2,6,1],
[6,9,5,10,0,3,7,5,9,2],
[7,8,9,8,8,0,10,9,9,5],
[4,7,5,9,4,1,0,0,10,3],
[5,7,6,9,6,2,11,0,10,3],
[5,8,6,5,2,2,1,1,0,2],
[5,9,8,10,9,6,8,8,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 6, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,4,5,4,7,8,9,5,4],
[6,0,7,5,7,5,5,8,6,8],
[7,4,0,5,5,5,6,8,4,5],
[6,6,6,0,4,5,6,9,3,6],
[7,4,6,7,0,6,7,11,6,6],
[4,6,6,6,5,0,5,9,7,5],
[3,6,5,5,4,6,0,9,5,6],
[2,3,3,2,0,2,2,0,1,4],
[6,5,7,8,5,4,6,10,0,6],
[7,3,6,5,5,6,5,7,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 7, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,5,4,5,4,2,4,2,5],
[7,0,6,6,5,6,4,4,5,7],
[6,5,0,4,6,5,4,3,4,5],
[7,5,7,0,6,6,3,4,6,7],
[6,6,5,5,0,6,5,6,5,5],
[7,5,6,5,5,0,5,5,7,5],
[9,7,7,8,6,6,0,5,6,8],
[7,7,8,7,5,6,6,0,8,7],
[9,6,7,5,6,4,5,3,0,7],
[6,4,6,4,6,6,3,4,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 8, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,5,8,6,6,6,8,8,5],
[3,0,5,3,6,5,2,6,5,7],
[6,6,0,3,6,8,5,11,8,7],
[3,8,8,0,6,6,6,8,8,4],
[5,5,5,5,0,5,5,5,5,2],
[5,6,3,5,6,0,5,3,3,5],
[5,9,6,5,6,6,0,6,3,5],
[3,5,0,3,6,8,5,0,5,7],
[3,6,3,3,6,8,8,6,0,5],
[6,4,4,7,9,6,6,4,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 9, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,4,4,7,1,1,1,8,8],
[6,0,0,7,6,1,4,4,7,4],
[7,11,0,7,10,7,4,4,11,4],
[7,4,4,0,7,0,4,7,4,7],
[4,5,1,4,0,1,4,4,1,4],
[10,10,4,11,10,0,8,7,10,7],
[10,7,7,7,7,3,0,7,7,7],
[10,7,7,4,7,4,4,0,8,7],
[3,4,0,7,10,1,4,3,0,3],
[3,7,7,4,7,4,4,4,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 10, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,9,8,7,6,9,5,6,11],
[7,0,8,6,5,5,7,4,6,9],
[2,3,0,5,6,3,5,4,4,5],
[3,5,6,0,7,5,5,2,4,10],
[4,6,5,4,0,5,6,6,5,10],
[5,6,8,6,6,0,8,5,6,10],
[2,4,6,6,5,3,0,3,4,7],
[6,7,7,9,5,6,8,0,3,10],
[5,5,7,7,6,5,7,8,0,10],
[0,2,6,1,1,1,4,1,1,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 11, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,7,6,8,6,9,9,3,7],
[7,0,7,9,5,3,6,7,2,7],
[4,4,0,8,5,4,4,4,3,6],
[5,2,3,0,7,4,5,5,2,6],
[3,6,6,4,0,6,9,8,5,7],
[5,8,7,7,5,0,8,9,6,8],
[2,5,7,6,2,3,0,3,1,4],
[2,4,7,6,3,2,8,0,0,8],
[8,9,8,9,6,5,10,11,0,11],
[4,4,5,5,4,3,7,3,0,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 12, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,7,5,5,5,5,7,5,4],
[5,0,8,4,4,8,5,7,7,2],
[4,3,0,5,4,3,3,4,3,3],
[6,7,6,0,4,6,5,8,5,5],
[6,7,7,7,0,6,4,6,6,5],
[6,3,8,5,5,0,3,6,4,2],
[6,6,8,6,7,8,0,8,5,6],
[4,4,7,3,5,5,3,0,3,4],
[6,4,8,6,5,7,6,8,0,3],
[7,9,8,6,6,9,5,7,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 13, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,7,6,6,4,6,5,6,4],
[5,0,2,2,5,5,8,5,6,4],
[4,9,0,4,7,6,7,8,8,3],
[5,9,7,0,4,5,7,6,9,3],
[5,6,4,7,0,4,6,7,7,5],
[7,6,5,6,7,0,7,6,7,6],
[5,3,4,4,5,4,0,5,7,6],
[6,6,3,5,4,5,6,0,6,4],
[5,5,3,2,4,4,4,5,0,2],
[7,7,8,8,6,5,5,7,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 14, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,8,8,7,6,4,6,6,7],
[4,0,4,4,3,4,2,3,1,5],
[3,7,0,6,4,7,2,7,6,6],
[3,7,5,0,7,6,6,5,6,10],
[4,8,7,4,0,5,3,7,4,5],
[5,7,4,5,6,0,6,5,5,6],
[7,9,9,5,8,5,0,7,6,6],
[5,8,4,6,4,6,4,0,2,7],
[5,10,5,5,7,6,5,9,0,7],
[4,6,5,1,6,5,5,4,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 15, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,10,5,9,7,6,8,10,8],
[2,0,4,4,8,3,2,8,9,3],
[1,7,0,6,7,5,4,9,8,4],
[6,7,5,0,6,6,5,6,5,6],
[2,3,4,5,0,3,2,5,2,3],
[4,8,6,5,8,0,3,10,7,6],
[5,9,7,6,9,8,0,8,7,6],
[3,3,2,5,6,1,3,0,2,2],
[1,2,3,6,9,4,4,9,0,1],
[3,8,7,5,8,5,5,9,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 16, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,6,6,4,6,6,6,8,8],
[5,0,6,5,7,7,5,5,4,5],
[5,5,0,5,4,6,6,7,6,7],
[5,6,6,0,6,7,6,8,4,8],
[7,4,7,5,0,6,6,5,4,6],
[5,4,5,4,5,0,6,5,3,7],
[5,6,5,5,5,5,0,6,6,8],
[5,6,4,3,6,6,5,0,4,7],
[3,7,5,7,7,8,5,7,0,8],
[3,6,4,3,5,4,3,4,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 17, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,5,5,4,4,1,8,2,2],
[4,0,1,4,7,5,5,8,3,5],
[6,10,0,5,8,8,5,8,8,5],
[6,7,6,0,7,5,3,7,7,7],
[7,4,3,4,0,1,1,6,4,2],
[7,6,3,6,10,0,6,7,6,7],
[10,6,6,8,10,5,0,10,6,7],
[3,3,3,4,5,4,1,0,3,1],
[9,8,3,4,7,5,5,8,0,4],
[9,6,6,4,9,4,4,10,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 18, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,7,6,8,4,6,7,6,5],
[4,0,5,6,8,7,7,6,7,7],
[4,6,0,6,8,4,4,6,4,4],
[5,5,5,0,7,6,7,4,6,5],
[3,3,3,4,0,4,5,3,7,2],
[7,4,7,5,7,0,5,5,7,6],
[5,4,7,4,6,6,0,4,7,6],
[4,5,5,7,8,6,7,0,7,6],
[5,4,7,5,4,4,4,4,0,4],
[6,4,7,6,9,5,5,5,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 19, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,5,7,8,6,7,5,4,7],
[6,0,4,6,6,4,7,4,4,6],
[6,7,0,9,8,4,5,5,7,10],
[4,5,2,0,5,5,6,3,5,7],
[3,5,3,6,0,4,5,5,4,8],
[5,7,7,6,7,0,5,8,5,8],
[4,4,6,5,6,6,0,7,3,7],
[6,7,6,8,6,3,4,0,5,9],
[7,7,4,6,7,6,8,6,0,8],
[4,5,1,4,3,3,4,2,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 20, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,4,5,5,6,4,2,4,6],
[4,0,3,6,4,4,3,1,4,4],
[7,8,0,9,6,6,5,6,9,6],
[6,5,2,0,5,6,5,3,4,6],
[6,7,5,6,0,6,5,2,5,3],
[5,7,5,5,5,0,3,4,6,3],
[7,8,6,6,6,8,0,4,6,5],
[9,10,5,8,9,7,7,0,7,8],
[7,7,2,7,6,5,5,4,0,5],
[5,7,5,5,8,8,6,3,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 21, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,4,6,4,6,6,4,8,4],
[3,0,1,4,2,0,3,3,1,0],
[7,10,0,9,3,6,7,3,6,6],
[5,7,2,0,3,4,1,3,5,5],
[7,9,8,8,0,7,7,9,5,8],
[5,11,5,7,4,0,5,6,4,3],
[5,8,4,10,4,6,0,4,7,8],
[7,8,8,8,2,5,7,0,7,6],
[3,10,5,6,6,7,4,4,0,5],
[7,11,5,6,3,8,3,5,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 22, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,7,4,7,6,6,7,6,9],
[6,0,7,4,5,9,6,6,7,10],
[4,4,0,4,5,8,4,7,10,10],
[7,7,7,0,4,6,4,7,6,10],
[4,6,6,7,0,7,4,10,9,8],
[5,2,3,5,4,0,2,4,7,9],
[5,5,7,7,7,9,0,7,8,9],
[4,5,4,4,1,7,4,0,6,8],
[5,4,1,5,2,4,3,5,0,7],
[2,1,1,1,3,2,2,3,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 23, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,5,4,8,6,4,7,3,5],
[5,0,3,5,5,4,4,3,3,5],
[6,8,0,5,6,5,6,7,5,7],
[7,6,6,0,6,5,4,7,4,5],
[3,6,5,5,0,5,4,7,3,5],
[5,7,6,6,6,0,6,5,7,6],
[7,7,5,7,7,5,0,4,8,4],
[4,8,4,4,4,6,7,0,5,7],
[8,8,6,7,8,4,3,6,0,6],
[6,6,4,6,6,5,7,4,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 24, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,7,8,6,6,5,10,7,6],
[4,0,8,9,7,7,3,10,6,2],
[4,3,0,7,3,5,5,9,5,2],
[3,2,4,0,2,2,4,7,5,2],
[5,4,8,9,0,7,3,9,8,4],
[5,4,6,9,4,0,6,10,5,4],
[6,8,6,7,8,5,0,9,8,7],
[1,1,2,4,2,1,2,0,2,0],
[4,5,6,6,3,6,3,9,0,4],
[5,9,9,9,7,7,4,11,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 25, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,4,4,9,4,4,4,4,0],
[6,0,4,6,9,4,4,6,6,2],
[7,7,0,2,11,0,6,2,2,2],
[7,5,9,0,9,9,4,4,9,5],
[2,2,0,2,0,0,4,2,2,2],
[7,7,11,2,11,0,6,2,6,2],
[7,7,5,7,7,5,0,2,7,7],
[7,5,9,7,9,9,9,0,9,5],
[7,5,9,2,9,5,4,2,0,0],
[11,9,9,6,9,9,4,6,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 26, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,5,5,5,4,5,3,4,6],
[5,0,5,4,6,3,6,3,5,6],
[6,6,0,6,6,6,6,3,5,7],
[6,7,5,0,4,6,6,5,5,5],
[6,5,5,7,0,5,7,6,6,8],
[7,8,5,5,6,0,6,4,6,7],
[6,5,5,5,4,5,0,5,4,6],
[8,8,8,6,5,7,6,0,6,7],
[7,6,6,6,5,5,7,5,0,7],
[5,5,4,6,3,4,5,4,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 27, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,6,5,6,4,4,6,4,6],
[5,0,4,4,5,7,4,6,5,6],
[5,7,0,5,6,5,5,7,5,6],
[6,7,6,0,7,7,7,5,5,6],
[5,6,5,4,0,5,6,5,3,3],
[7,4,6,4,6,0,6,5,5,6],
[7,7,6,4,5,5,0,6,5,5],
[5,5,4,6,6,6,5,0,6,6],
[7,6,6,6,8,6,6,5,0,6],
[5,5,5,5,8,5,6,5,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 28, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,4,7,5,4,6,5,8,5],
[6,0,6,5,5,6,5,4,6,4],
[7,5,0,7,4,5,5,6,6,5],
[4,6,4,0,6,6,6,6,6,5],
[6,6,7,5,0,5,6,5,8,6],
[7,5,6,5,6,0,5,4,7,4],
[5,6,6,5,5,6,0,6,7,6],
[6,7,5,5,6,7,5,0,8,7],
[3,5,5,5,3,4,4,3,0,3],
[6,7,6,6,5,7,5,4,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 29, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,3,7,8,5,10,6,8,8],
[4,0,3,5,6,6,6,4,8,5],
[8,8,0,8,11,4,8,6,10,6],
[4,6,3,0,10,4,7,7,7,7],
[3,5,0,1,0,3,6,3,3,5],
[6,5,7,7,8,0,10,6,10,7],
[1,5,3,4,5,1,0,3,5,5],
[5,7,5,4,8,5,8,0,8,10],
[3,3,1,4,8,1,6,3,0,3],
[3,6,5,4,6,4,6,1,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 30, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,5,3,6,6,5,6,1,2],
[5,0,2,4,5,5,4,4,5,2],
[6,9,0,5,9,5,7,8,6,8],
[8,7,6,0,9,6,6,9,6,4],
[5,6,2,2,0,6,6,7,3,3],
[5,6,6,5,5,0,4,5,5,3],
[6,7,4,5,5,7,0,4,6,4],
[5,7,3,2,4,6,7,0,2,4],
[10,6,5,5,8,6,5,9,0,3],
[9,9,3,7,8,8,7,7,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 31, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,2,6,2,5,5,4,8,2],
[9,0,5,6,6,7,7,5,9,8],
[9,6,0,6,5,8,6,7,10,9],
[5,5,5,0,3,7,6,4,8,6],
[9,5,6,8,0,9,9,7,10,7],
[6,4,3,4,2,0,4,5,4,5],
[6,4,5,5,2,7,0,6,6,6],
[7,6,4,7,4,6,5,0,7,6],
[3,2,1,3,1,7,5,4,0,4],
[9,3,2,5,4,6,5,5,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 32, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,4,6,5,7,6,6,6,4],
[8,0,5,3,5,5,6,7,7,8],
[7,6,0,6,6,6,6,6,6,4],
[5,8,5,0,6,7,10,7,6,8],
[6,6,5,5,0,5,8,4,5,8],
[4,6,5,4,6,0,7,4,10,7],
[5,5,5,1,3,4,0,4,4,4],
[5,4,5,4,7,7,7,0,7,5],
[5,4,5,5,6,1,7,4,0,7],
[7,3,7,3,3,4,7,6,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 33, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,6,8,8,5,4,10,4,2],
[6,0,6,5,9,5,4,9,4,4],
[5,5,0,5,5,3,4,7,5,5],
[3,6,6,0,4,4,4,7,4,4],
[3,2,6,7,0,5,5,10,4,3],
[6,6,8,7,6,0,6,11,4,6],
[7,7,7,7,6,5,0,7,7,6],
[1,2,4,4,1,0,4,0,2,2],
[7,7,6,7,7,7,4,9,0,7],
[9,7,6,7,8,5,5,9,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 34, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,7,8,7,6,5,7,6,7],
[3,0,6,6,6,7,4,4,6,8],
[4,5,0,5,3,4,3,2,4,5],
[3,5,6,0,4,5,3,5,4,6],
[4,5,8,7,0,5,4,4,5,8],
[5,4,7,6,6,0,6,4,6,7],
[6,7,8,8,7,5,0,5,7,8],
[4,7,9,6,7,7,6,0,7,10],
[5,5,7,7,6,5,4,4,0,7],
[4,3,6,5,3,4,3,1,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 35, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,4,0,4,4,4,4,4,4],
[7,0,7,3,3,3,0,7,3,7],
[7,4,0,4,4,4,4,7,4,4],
[11,8,7,0,4,8,8,11,8,8],
[7,8,7,7,0,8,4,7,8,8],
[7,8,7,3,3,0,4,7,7,4],
[7,11,7,3,7,7,0,7,11,11],
[7,4,4,0,4,4,4,0,4,4],
[7,8,7,3,3,4,0,7,0,8],
[7,4,7,3,3,7,0,7,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 36, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,5,0,0,0,0,2,0,0],
[6,0,11,6,0,4,0,6,0,4],
[6,0,0,6,0,4,0,2,0,4],
[11,5,5,0,0,4,0,7,5,4],
[11,11,11,11,0,6,2,11,11,6],
[11,7,7,7,5,0,7,7,7,5],
[11,11,11,11,9,4,0,11,11,9],
[9,5,9,4,0,4,0,0,5,4],
[11,11,11,6,0,4,0,6,0,4],
[11,7,7,7,5,6,2,7,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 37, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,6,2,7,5,7,6,3,3],
[4,0,8,5,8,2,5,5,5,6],
[5,3,0,1,6,3,2,1,7,2],
[9,6,10,0,10,4,9,9,8,7],
[4,3,5,1,0,2,7,4,4,6],
[6,9,8,7,9,0,8,7,8,5],
[4,6,9,2,4,3,0,4,5,5],
[5,6,10,2,7,4,7,0,8,5],
[8,6,4,3,7,3,6,3,0,2],
[8,5,9,4,5,6,6,6,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 38, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,7,7,6,7,9,7,6,5],
[5,0,6,5,5,5,8,5,4,4],
[4,5,0,4,6,7,10,6,5,5],
[4,6,7,0,5,7,9,9,4,7],
[5,6,5,6,0,6,7,6,6,6],
[4,6,4,4,5,0,6,4,5,7],
[2,3,1,2,4,5,0,5,5,5],
[4,6,5,2,5,7,6,0,5,6],
[5,7,6,7,5,6,6,6,0,7],
[6,7,6,4,5,4,6,5,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 39, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,4,6,8,4,7,5,5,6],
[5,0,7,5,8,4,6,8,7,6],
[7,4,0,3,6,3,5,4,7,4],
[5,6,8,0,7,4,7,8,7,6],
[3,3,5,4,0,3,6,5,3,4],
[7,7,8,7,8,0,6,6,5,6],
[4,5,6,4,5,5,0,4,6,5],
[6,3,7,3,6,5,7,0,7,8],
[6,4,4,4,8,6,5,4,0,6],
[5,5,7,5,7,5,6,3,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 40, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,6,7,8,5,6,7,8,6],
[3,0,2,5,6,2,2,3,4,4],
[5,9,0,4,8,4,5,8,5,8],
[4,6,7,0,10,7,8,7,5,8],
[3,5,3,1,0,4,5,5,2,7],
[6,9,7,4,7,0,8,7,5,5],
[5,9,6,3,6,3,0,6,4,4],
[4,8,3,4,6,4,5,0,5,6],
[3,7,6,6,9,6,7,6,0,6],
[5,7,3,3,4,6,7,5,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 41, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,6,6,2,3,8,3,8,5],
[8,0,8,3,5,6,5,6,11,8],
[5,3,0,3,2,6,5,3,11,5],
[5,8,8,0,5,5,11,3,8,5],
[9,6,9,6,0,6,8,3,11,8],
[8,5,5,6,5,0,8,0,5,5],
[3,6,6,0,3,3,0,3,6,5],
[8,5,8,8,8,11,8,0,11,11],
[3,0,0,3,0,6,5,0,0,2],
[6,3,6,6,3,6,6,0,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 42, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,9,8,6,5,10,6,9,9],
[6,0,7,8,8,4,9,7,7,7],
[2,4,0,6,3,0,5,3,0,2],
[3,3,5,0,5,1,5,1,1,1],
[5,3,8,6,0,5,8,1,5,4],
[6,7,11,10,6,0,9,5,7,8],
[1,2,6,6,3,2,0,2,2,5],
[5,4,8,10,10,6,9,0,7,6],
[2,4,11,10,6,4,9,4,0,7],
[2,4,9,10,7,3,6,5,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 43, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,3,3,6,3,7,7,6,4],
[4,0,3,4,6,3,7,7,6,4],
[8,8,0,8,6,3,7,8,8,8],
[8,7,3,0,3,6,7,11,10,8],
[5,5,5,8,0,3,4,8,8,5],
[8,8,8,5,8,0,4,11,11,8],
[4,4,4,4,7,7,0,7,7,4],
[4,4,3,0,3,0,4,0,7,4],
[5,5,3,1,3,0,4,4,0,1],
[7,7,3,3,6,3,7,7,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 44, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,3,7,7,5,6,7,7,6],
[7,0,3,8,9,6,5,5,7,6],
[8,8,0,8,7,4,6,5,5,6],
[4,3,3,0,7,1,5,5,5,5],
[4,2,4,4,0,2,2,2,5,3],
[6,5,7,10,9,0,9,8,9,8],
[5,6,5,6,9,2,0,6,8,6],
[4,6,6,6,9,3,5,0,7,5],
[4,4,6,6,6,2,3,4,0,5],
[5,5,5,6,8,3,5,6,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 45, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,3,7,8,8,5,7,6,4],
[4,0,4,5,8,5,2,6,7,4],
[8,7,0,7,8,7,5,7,7,6],
[4,6,4,0,5,8,5,6,6,5],
[3,3,3,6,0,7,3,5,5,4],
[3,6,4,3,4,0,3,5,4,4],
[6,9,6,6,8,8,0,9,7,5],
[4,5,4,5,6,6,2,0,3,3],
[5,4,4,5,6,7,4,8,0,4],
[7,7,5,6,7,7,6,8,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 46, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,3,6,8,6,8,3,8,6],
[6,0,6,6,8,6,8,6,5,6],
[8,5,0,6,8,3,5,5,5,3],
[5,5,5,0,8,6,5,5,5,5],
[3,3,3,3,0,3,5,3,0,3],
[5,5,8,5,8,0,5,8,8,8],
[3,3,6,6,6,6,0,6,6,9],
[8,5,6,6,8,3,5,0,5,6],
[3,6,6,6,11,3,5,6,0,6],
[5,5,8,6,8,3,2,5,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 47, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,7,5,8,6,8,4,7,5],
[7,0,7,7,9,7,10,5,8,8],
[4,4,0,5,8,5,9,6,5,3],
[6,4,6,0,5,6,7,4,8,6],
[3,2,3,6,0,6,7,6,6,5],
[5,4,6,5,5,0,9,5,8,5],
[3,1,2,4,4,2,0,3,5,4],
[7,6,5,7,5,6,8,0,7,6],
[4,3,6,3,5,3,6,4,0,3],
[6,3,8,5,6,6,7,5,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 48, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,7,5,6,5,8,6,5,5],
[4,0,3,3,1,1,6,4,1,1],
[4,8,0,8,3,3,5,6,6,8],
[6,8,3,0,5,0,4,8,0,5],
[5,10,8,6,0,6,9,5,6,7],
[6,10,8,11,5,0,8,8,5,5],
[3,5,6,7,2,3,0,5,5,5],
[5,7,5,3,6,3,6,0,3,4],
[6,10,5,11,5,6,6,8,0,7],
[6,10,3,6,4,6,6,7,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 49, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,5,6,8,7,2,7,5,7],
[3,0,3,6,6,8,4,9,4,4],
[6,8,0,7,6,7,4,8,7,5],
[5,5,4,0,7,8,4,6,4,3],
[3,5,5,4,0,8,3,8,6,3],
[4,3,4,3,3,0,3,6,1,3],
[9,7,7,7,8,8,0,10,5,6],
[4,2,3,5,3,5,1,0,3,3],
[6,7,4,7,5,10,6,8,0,5],
[4,7,6,8,8,8,5,8,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 50, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,3,7,11,8,4,3,7,7],
[4,0,4,0,7,4,4,4,4,4],
[8,7,0,4,11,8,8,7,4,7],
[4,11,7,0,7,4,4,7,11,7],
[0,4,0,4,0,0,0,0,4,4],
[3,7,3,7,11,0,7,3,7,7],
[7,7,3,7,11,4,0,3,7,7],
[8,7,4,4,11,8,8,0,4,4],
[4,7,7,0,7,4,4,7,0,7],
[4,7,4,4,7,4,4,7,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 51, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,7,4,3,3,7,7,11,7],
[4,0,4,4,7,4,0,4,4,4],
[4,7,0,4,3,3,3,4,7,0],
[7,7,7,0,7,3,3,7,7,3],
[8,4,8,4,0,0,4,8,8,4],
[8,7,8,8,11,0,7,8,11,4],
[4,11,8,8,7,4,0,8,8,8],
[4,7,7,4,3,3,3,0,7,0],
[0,7,4,4,3,0,3,4,0,4],
[4,7,11,8,7,7,3,11,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 52, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,8,3,7,5,9,10,5,9],
[6,0,8,4,6,6,9,10,10,8],
[3,3,0,6,7,6,2,3,3,5],
[8,7,5,0,8,2,7,8,8,9],
[4,5,4,3,0,5,5,6,5,8],
[6,5,5,9,6,0,6,6,6,8],
[2,2,9,4,6,5,0,2,3,4],
[1,1,8,3,5,5,9,0,2,4],
[6,1,8,3,6,5,8,9,0,8],
[2,3,6,2,3,3,7,7,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 53, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,4,4,5,7,3,4,4,2],
[6,0,5,6,8,7,3,6,7,5],
[7,6,0,5,7,7,6,6,9,5],
[7,5,6,0,6,8,5,6,7,6],
[6,3,4,5,0,8,2,5,6,2],
[4,4,4,3,3,0,5,5,5,3],
[8,8,5,6,9,6,0,8,7,5],
[7,5,5,5,6,6,3,0,8,5],
[7,4,2,4,5,6,4,3,0,3],
[9,6,6,5,9,8,6,6,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 54, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,9,5,3,7,3,5,6,6],
[4,0,10,7,4,2,3,4,4,4],
[2,1,0,4,2,3,0,4,4,3],
[6,4,7,0,6,6,1,5,3,3],
[8,7,9,5,0,6,3,6,6,8],
[4,9,8,5,5,0,5,5,5,7],
[8,8,11,10,8,6,0,5,8,8],
[6,7,7,6,5,6,6,0,6,6],
[5,7,7,8,5,6,3,5,0,9],
[5,7,8,8,3,4,3,5,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 55, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,6,4,6,6,6,6,11,6],
[0,0,4,0,0,6,2,2,0,4],
[5,7,0,0,0,6,2,2,7,5],
[7,11,11,0,2,6,11,11,11,11],
[5,11,11,9,0,11,11,11,11,9],
[5,5,5,5,0,0,7,5,5,5],
[5,9,9,0,0,4,0,9,9,9],
[5,9,9,0,0,6,2,0,9,9],
[0,11,4,0,0,6,2,2,0,4],
[5,7,6,0,2,6,2,2,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 56, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,7,6,7,5,7,4,7,5],
[5,0,6,8,8,8,5,5,5,5],
[4,5,0,7,7,7,6,4,4,6],
[5,3,4,0,8,5,5,5,4,5],
[4,3,4,3,0,3,4,2,3,4],
[6,3,4,6,8,0,4,4,3,6],
[4,6,5,6,7,7,0,5,4,5],
[7,6,7,6,9,7,6,0,5,5],
[4,6,7,7,8,8,7,6,0,5],
[6,6,5,6,7,5,6,6,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 57, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,7,7,6,5,7,8,10,7],
[5,0,6,8,6,4,4,7,8,5],
[4,5,0,6,4,7,3,7,8,6],
[4,3,5,0,4,4,4,7,8,5],
[5,5,7,7,0,6,5,8,9,7],
[6,7,4,7,5,0,5,7,8,6],
[4,7,8,7,6,6,0,9,11,6],
[3,4,4,4,3,4,2,0,8,5],
[1,3,3,3,2,3,0,3,0,3],
[4,6,5,6,4,5,5,6,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 58, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,5,5,5,5,3,4,3,5],
[6,0,5,3,2,3,3,1,5,4],
[6,6,0,4,4,5,4,4,3,5],
[6,8,7,0,6,8,5,5,5,6],
[6,9,7,5,0,8,7,7,7,6],
[6,8,6,3,3,0,3,5,5,3],
[8,8,7,6,4,8,0,3,7,5],
[7,10,7,6,4,6,8,0,8,6],
[8,6,8,6,4,6,4,3,0,6],
[6,7,6,5,5,8,6,5,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 59, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,8,6,3,7,7,7,6,1],
[8,0,5,5,6,7,5,5,4,3],
[3,6,0,7,6,9,8,9,8,4],
[5,6,4,0,8,9,8,9,7,4],
[8,5,5,3,0,4,5,6,4,4],
[4,4,2,2,7,0,8,5,0,2],
[4,6,3,3,6,3,0,5,2,4],
[4,6,2,2,5,6,6,0,2,3],
[5,7,3,4,7,11,9,9,0,6],
[10,8,7,7,7,9,7,8,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 60, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,4,4,7,4,5,5,5,4],
[6,0,4,4,8,3,4,5,6,4],
[7,7,0,7,10,6,6,7,7,5],
[7,7,4,0,8,3,5,5,8,5],
[4,3,1,3,0,2,3,2,3,0],
[7,8,5,8,9,0,8,6,9,5],
[6,7,5,6,8,3,0,5,7,2],
[6,6,4,6,9,5,6,0,5,6],
[6,5,4,3,8,2,4,6,0,4],
[7,7,6,6,11,6,9,5,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 61, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,1,5,5,3,2,4,4,3],
[7,0,4,7,7,6,6,4,5,4],
[10,7,0,10,5,4,7,7,8,9],
[6,4,1,0,5,2,4,4,4,4],
[6,4,6,6,0,4,5,3,7,6],
[8,5,7,9,7,0,6,5,6,5],
[9,5,4,7,6,5,0,5,6,6],
[7,7,4,7,8,6,6,0,6,7],
[7,6,3,7,4,5,5,5,0,6],
[8,7,2,7,5,6,5,4,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 62, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,6,4,4,3,2,4,3,5],
[7,0,6,3,6,6,4,6,3,6],
[5,5,0,1,3,4,3,5,3,6],
[7,8,10,0,6,5,7,8,6,9],
[7,5,8,5,0,6,5,7,4,6],
[8,5,7,6,5,0,3,6,5,8],
[9,7,8,4,6,8,0,5,6,8],
[7,5,6,3,4,5,6,0,5,5],
[8,8,8,5,7,6,5,6,0,8],
[6,5,5,2,5,3,3,6,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 63, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,4,5,2,8,7,4,0,3],
[5,0,3,5,2,5,5,0,0,1],
[7,8,0,5,2,5,5,3,0,6],
[6,6,6,0,5,8,6,3,1,3],
[9,9,9,6,0,10,9,4,6,6],
[3,6,6,3,1,0,4,1,1,3],
[4,6,6,5,2,7,0,1,0,3],
[7,11,8,8,7,10,10,0,3,6],
[11,11,11,10,5,10,11,8,0,6],
[8,10,5,8,5,8,8,5,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 64, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,6,7,7,5,8,7,4,4],
[7,0,6,9,8,6,6,7,4,9],
[5,5,0,5,7,5,6,8,6,7],
[4,2,6,0,5,5,2,4,2,5],
[4,3,4,6,0,5,3,6,5,5],
[6,5,6,6,6,0,4,6,3,5],
[3,5,5,9,8,7,0,5,4,5],
[4,4,3,7,5,5,6,0,5,6],
[7,7,5,9,6,8,7,6,0,7],
[7,2,4,6,6,6,6,5,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 65, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,2,2,6,1,3,4,1,2],
[8,0,3,2,5,3,6,7,3,2],
[9,8,0,4,5,4,7,7,3,3],
[9,9,7,0,9,5,7,6,5,3],
[5,6,6,2,0,3,6,4,2,3],
[10,8,7,6,8,0,7,8,6,5],
[8,5,4,4,5,4,0,6,3,5],
[7,4,4,5,7,3,5,0,0,5],
[10,8,8,6,9,5,8,11,0,6],
[9,9,8,8,8,6,6,6,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 66, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,1,3,4,3,4,7,4,3],
[8,0,8,7,7,4,8,7,7,8],
[10,3,0,3,7,6,7,7,7,6],
[8,4,8,0,7,8,11,7,10,11],
[7,4,4,4,0,7,8,7,7,7],
[8,7,5,3,4,0,10,7,4,7],
[7,3,4,0,3,1,0,3,1,6],
[4,4,4,4,4,4,8,0,4,7],
[7,4,4,1,4,7,10,7,0,7],
[8,3,5,0,4,4,5,4,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 67, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,5,10,7,8,5,3,4,6],
[8,0,8,11,8,6,6,8,5,7],
[6,3,0,6,3,6,6,4,4,3],
[1,0,5,0,5,1,3,2,3,3],
[4,3,8,6,0,4,6,3,4,4],
[3,5,5,10,7,0,7,5,6,8],
[6,5,5,8,5,4,0,6,2,4],
[8,3,7,9,8,6,5,0,6,6],
[7,6,7,8,7,5,9,5,0,9],
[5,4,8,8,7,3,7,5,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 68, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,5,8,4,5,3,1,3,5],
[8,0,5,9,7,8,7,6,6,8],
[6,6,0,6,4,6,6,5,5,7],
[3,2,5,0,4,4,5,2,5,4],
[7,4,7,7,0,5,8,5,4,7],
[6,3,5,7,6,0,5,3,4,5],
[8,4,5,6,3,6,0,5,5,8],
[10,5,6,9,6,8,6,0,6,9],
[8,5,6,6,7,7,6,5,0,7],
[6,3,4,7,4,6,3,2,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 69, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,3,4,5,6,4,5,6,6],
[7,0,6,2,4,6,4,3,4,5],
[8,5,0,2,4,7,5,4,4,3],
[7,9,9,0,5,7,5,3,7,5],
[6,7,7,6,0,4,6,2,7,7],
[5,5,4,4,7,0,4,4,5,6],
[7,7,6,6,5,7,0,7,7,6],
[6,8,7,8,9,7,4,0,8,10],
[5,7,7,4,4,6,4,3,0,6],
[5,6,8,6,4,5,5,1,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 70, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,8,7,8,8,5,5,5,6],
[6,0,7,9,8,7,5,4,5,4],
[3,4,0,9,6,7,5,7,7,4],
[4,2,2,0,2,4,3,3,3,5],
[3,3,5,9,0,7,3,3,5,4],
[3,4,4,7,4,0,3,5,5,3],
[6,6,6,8,8,8,0,5,5,6],
[6,7,4,8,8,6,6,0,4,6],
[6,6,4,8,6,6,6,7,0,5],
[5,7,7,6,7,8,5,5,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 71, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,5,3,6,7,2,2,3,4],
[8,0,5,3,5,7,8,2,5,7],
[6,6,0,2,3,7,7,7,7,5],
[8,8,9,0,10,11,6,6,6,4],
[5,6,8,1,0,8,6,6,7,5],
[4,4,4,0,3,0,5,6,5,3],
[9,3,4,5,5,6,0,3,4,6],
[9,9,4,5,5,5,8,0,8,5],
[8,6,4,5,4,6,7,3,0,5],
[7,4,6,7,6,8,5,6,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 72, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,5,7,7,7,6,6,5,7],
[6,0,6,6,9,7,7,8,5,7],
[6,5,0,5,5,8,8,7,5,8],
[4,5,6,0,7,8,6,7,6,5],
[4,2,6,4,0,6,6,5,3,5],
[4,4,3,3,5,0,6,6,2,6],
[5,4,3,5,5,5,0,5,5,7],
[5,3,4,4,6,5,6,0,4,8],
[6,6,6,5,8,9,6,7,0,6],
[4,4,3,6,6,5,4,3,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 73, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,5,6,7,4,6,4,5,3],
[8,0,6,6,7,3,8,6,8,1],
[6,5,0,8,6,4,4,6,4,3],
[5,5,3,0,3,1,2,4,5,1],
[4,4,5,8,0,4,5,6,6,3],
[7,8,7,10,7,0,5,7,10,7],
[5,3,7,9,6,6,0,7,6,4],
[7,5,5,7,5,4,4,0,8,4],
[6,3,7,6,5,1,5,3,0,3],
[8,10,8,10,8,4,7,7,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 74, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,5,5,5,6,6,7,7,6],
[3,0,3,4,4,6,4,5,6,5],
[6,8,0,4,7,6,7,6,8,8],
[6,7,7,0,5,7,6,6,7,6],
[6,7,4,6,0,7,7,5,8,7],
[5,5,5,4,4,0,4,8,3,6],
[5,7,4,5,4,7,0,6,8,7],
[4,6,5,5,6,3,5,0,5,3],
[4,5,3,4,3,8,3,6,0,4],
[5,6,3,5,4,5,4,8,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 75, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,9,7,4,2,4,8,4,3],
[5,0,8,6,5,5,5,8,6,5],
[2,3,0,7,3,2,4,8,5,2],
[4,5,4,0,2,1,3,6,3,1],
[7,6,8,9,0,3,5,8,7,6],
[9,6,9,10,8,0,7,10,8,4],
[7,6,7,8,6,4,0,7,7,6],
[3,3,3,5,3,1,4,0,2,2],
[7,5,6,8,4,3,4,9,0,4],
[8,6,9,10,5,7,5,9,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 76, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,9,5,5,4,3,6,7,5],
[2,0,5,4,2,3,3,3,4,3],
[2,6,0,6,4,2,3,4,4,4],
[6,7,5,0,4,4,3,8,6,6],
[6,9,7,7,0,4,6,8,6,7],
[7,8,9,7,7,0,5,7,8,7],
[8,8,8,8,5,6,0,8,6,7],
[5,8,7,3,3,4,3,0,7,5],
[4,7,7,5,5,3,5,4,0,5],
[6,8,7,5,4,4,4,6,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 77, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,5,5,10,7,8,6,4,4],
[5,0,5,4,4,4,2,5,4,5],
[6,6,0,5,6,6,3,5,4,5],
[6,7,6,0,9,4,6,3,4,4],
[1,7,5,2,0,3,6,3,2,4],
[4,7,5,7,8,0,5,4,3,2],
[3,9,8,5,5,6,0,6,7,6],
[5,6,6,8,8,7,5,0,4,4],
[7,7,7,7,9,8,4,7,0,7],
[7,6,6,7,7,9,5,7,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 78, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,7,7,7,7,7,7,4,4],
[4,0,4,4,0,4,0,7,4,0],
[4,7,0,4,4,7,0,7,4,4],
[4,7,7,0,4,11,4,7,8,4],
[4,11,7,7,0,7,4,7,4,8],
[4,7,4,0,4,0,4,3,0,4],
[4,11,11,7,7,7,0,7,4,4],
[4,4,4,4,4,8,4,0,8,4],
[7,7,7,3,7,11,7,3,0,7],
[7,11,7,7,3,7,7,7,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 79, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1,4,6,3,3,2,3,1,3],
[10,0,5,6,5,6,5,3,4,6],
[7,6,0,8,7,5,6,5,5,5],
[5,5,3,0,4,3,1,2,0,2],
[8,6,4,7,0,5,5,1,4,4],
[8,5,6,8,6,0,6,5,4,6],
[9,6,5,10,6,5,0,6,6,5],
[8,8,6,9,10,6,5,0,7,6],
[10,7,6,11,7,7,5,4,0,6],
[8,5,6,9,7,5,6,5,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 80, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,8,8,8,7,9,4,8,7],
[5,0,6,7,5,6,7,4,5,5],
[3,5,0,6,4,4,6,4,5,6],
[3,4,5,0,3,2,4,2,5,5],
[3,6,7,8,0,4,7,5,8,5],
[4,5,7,9,7,0,7,7,6,6],
[2,4,5,7,4,4,0,5,5,5],
[7,7,7,9,6,4,6,0,8,9],
[3,6,6,6,3,5,6,3,0,6],
[4,6,5,6,6,5,6,2,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 81, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,7,6,11,11,11,7,7,3],
[4,0,8,6,10,8,10,4,4,7],
[4,3,0,6,10,9,10,7,4,3],
[5,5,5,0,5,5,9,5,5,7],
[0,1,1,6,0,5,10,5,1,3],
[0,3,2,6,6,0,6,7,2,3],
[0,1,1,2,1,5,0,1,1,3],
[4,7,4,6,6,4,10,0,4,7],
[4,7,7,6,10,9,10,7,0,7],
[8,4,8,4,8,8,8,4,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 82, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,2,11,2,7,7,2,7,6],
[9,0,2,11,7,11,7,6,11,6],
[9,9,0,9,5,11,5,6,11,6],
[0,0,2,0,0,2,0,2,2,2],
[9,4,6,11,0,11,11,6,11,6],
[4,0,0,9,0,0,5,6,4,4],
[4,4,6,11,0,6,0,6,6,6],
[9,5,5,9,5,5,5,0,5,4],
[4,0,0,9,0,7,5,6,0,4],
[5,5,5,9,5,7,5,7,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 83, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,4,4,4,2,4,4,4,4],
[5,0,5,5,6,4,4,3,5,6],
[7,6,0,9,5,3,4,3,6,3],
[7,6,2,0,3,3,3,3,2,4],
[7,5,6,8,0,4,3,3,6,4],
[9,7,8,8,7,0,9,3,7,5],
[7,7,7,8,8,2,0,2,7,4],
[7,8,8,8,8,8,9,0,8,5],
[7,6,5,9,5,4,4,3,0,5],
[7,5,8,7,7,6,7,6,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 84, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,6,7,5,4,9,6,8,8],
[6,0,6,6,7,4,9,4,8,8],
[5,5,0,2,8,4,6,8,5,6],
[4,5,9,0,8,4,9,7,8,6],
[6,4,3,3,0,4,4,1,3,3],
[7,7,7,7,7,0,8,7,4,7],
[2,2,5,2,7,3,0,3,4,8],
[5,7,3,4,10,4,8,0,7,8],
[3,3,6,3,8,7,7,4,0,4],
[3,3,5,5,8,4,3,3,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 85, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,7,2,5,4,2,6,4,4],
[4,0,4,2,3,4,3,2,3,3],
[4,7,0,6,6,3,4,5,4,2],
[9,9,5,0,5,5,3,6,4,6],
[6,8,5,6,0,6,6,7,3,6],
[7,7,8,6,5,0,6,6,6,8],
[9,8,7,8,5,5,0,7,3,6],
[5,9,6,5,4,5,4,0,4,4],
[7,8,7,7,8,5,8,7,0,7],
[7,8,9,5,5,3,5,7,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 86, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,7,3,7,7,4,3,3,0],
[7,0,3,3,3,7,3,3,3,3],
[4,8,0,4,4,8,4,7,4,4],
[8,8,7,0,4,8,8,3,0,4],
[4,8,7,7,0,4,4,7,7,4],
[4,4,3,3,7,0,0,3,3,0],
[7,8,7,3,7,11,0,3,3,7],
[8,8,4,8,4,8,8,0,4,4],
[8,8,7,11,4,8,8,7,0,4],
[11,8,7,7,7,11,4,7,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 87, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,11,11,2,11,9,11,11,11],
[4,0,11,9,6,9,9,9,11,6],
[0,0,0,0,0,4,4,4,0,0],
[0,2,11,0,2,9,9,9,7,2],
[9,5,11,9,0,9,9,9,11,11],
[0,2,7,2,2,0,0,4,2,2],
[2,2,7,2,2,11,0,11,7,2],
[0,2,7,2,2,7,0,0,2,2],
[0,0,11,4,0,9,4,9,0,6],
[0,5,11,9,0,9,9,9,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 88, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,7,6,6,5,4,8,7,6],
[6,0,5,7,7,6,5,5,6,6],
[4,6,0,4,5,2,5,5,5,3],
[5,4,7,0,6,5,4,7,6,6],
[5,4,6,5,0,4,7,4,6,7],
[6,5,9,6,7,0,6,6,8,7],
[7,6,6,7,4,5,0,7,9,4],
[3,6,6,4,7,5,4,0,7,8],
[4,5,6,5,5,3,2,4,0,5],
[5,5,8,5,4,4,7,3,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 89, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,5,5,9,6,7,7,5,6],
[5,0,7,4,8,7,7,5,6,7],
[6,4,0,5,10,7,6,5,6,6],
[6,7,6,0,7,5,4,6,7,7],
[2,3,1,4,0,5,3,4,4,6],
[5,4,4,6,6,0,5,4,5,6],
[4,4,5,7,8,6,0,6,6,7],
[4,6,6,5,7,7,5,0,6,6],
[6,5,5,4,7,6,5,5,0,8],
[5,4,5,4,5,5,4,5,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 90, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,4,5,2,5,3,6,5,6],
[6,0,5,7,2,4,4,6,4,7],
[7,6,0,6,6,5,3,6,7,6],
[6,4,5,0,3,4,2,4,5,5],
[9,9,5,8,0,5,6,7,6,8],
[6,7,6,7,6,0,4,5,7,8],
[8,7,8,9,5,7,0,7,8,7],
[5,5,5,7,4,6,4,0,6,8],
[6,7,4,6,5,4,3,5,0,6],
[5,4,5,6,3,3,4,3,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 91, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,7,6,8,7,4,6,8,6],
[4,0,10,10,10,7,8,10,7,10],
[4,1,0,2,4,3,0,0,5,2],
[5,1,9,0,8,1,1,2,3,1],
[3,1,7,3,0,1,3,3,5,3],
[4,4,8,10,10,0,6,4,8,8],
[7,3,11,10,8,5,0,8,8,3],
[5,1,11,9,8,7,3,0,5,6],
[3,4,6,8,6,3,3,6,0,5],
[5,1,9,10,8,3,8,5,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 92, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,6,5,7,6,7,5,8,4],
[6,0,8,9,7,5,7,5,9,6],
[5,3,0,5,6,2,6,3,5,3],
[6,2,6,0,8,5,7,4,5,4],
[4,4,5,3,0,4,7,3,5,3],
[5,6,9,6,7,0,8,5,8,4],
[4,4,5,4,4,3,0,3,6,2],
[6,6,8,7,8,6,8,0,8,5],
[3,2,6,6,6,3,5,3,0,4],
[7,5,8,7,8,7,9,6,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 93, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,3,7,4,8,6,5,7,3],
[8,0,3,7,5,9,6,5,7,5],
[8,8,0,10,7,8,7,5,9,8],
[4,4,1,0,5,6,2,3,3,1],
[7,6,4,6,0,7,5,3,7,3],
[3,2,3,5,4,0,2,3,5,1],
[5,5,4,9,6,9,0,6,7,5],
[6,6,6,8,8,8,5,0,6,3],
[4,4,2,8,4,6,4,5,0,5],
[8,6,3,10,8,10,6,8,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 94, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,6,8,11,5,5,0,5,3],
[6,0,6,6,6,6,3,6,3,6],
[5,5,0,5,8,5,5,0,5,0],
[3,5,6,0,11,8,8,3,5,3],
[0,5,3,0,0,0,0,0,0,0],
[6,5,6,3,11,0,0,6,0,6],
[6,8,6,3,11,11,0,6,8,6],
[11,5,11,8,11,5,5,0,5,11],
[6,8,6,6,11,11,3,6,0,6],
[8,5,11,8,11,5,5,0,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 95, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,5,5,5,4,5,5,5,5],
[5,0,7,4,5,6,4,7,6,7],
[6,4,0,7,5,5,4,6,8,8],
[6,7,4,0,6,5,6,5,5,6],
[6,6,6,5,0,4,5,5,5,7],
[7,5,6,6,7,0,5,5,9,6],
[6,7,7,5,6,6,0,6,7,7],
[6,4,5,6,6,6,5,0,8,5],
[6,5,3,6,6,2,4,3,0,5],
[6,4,3,5,4,5,4,6,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 96, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,2,6,6,8,4,4,8,4],
[5,0,4,7,6,8,8,4,8,6],
[9,7,0,9,7,9,5,7,8,2],
[5,4,2,0,6,6,4,8,8,4],
[5,5,4,5,0,6,4,7,8,4],
[3,3,2,5,5,0,4,3,4,0],
[7,3,6,7,7,7,0,7,6,2],
[7,7,4,3,4,8,4,0,10,4],
[3,3,3,3,3,7,5,1,0,2],
[7,5,9,7,7,11,9,7,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 97, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,8,8,3,8,8,2,3,8],
[8,0,6,7,9,7,9,5,3,7],
[3,5,0,3,3,5,3,4,6,4],
[3,4,8,0,2,7,8,1,3,7],
[8,2,8,9,0,8,10,2,5,8],
[3,4,6,4,3,0,9,1,4,7],
[3,2,8,3,1,2,0,1,3,8],
[9,6,7,10,9,10,10,0,5,10],
[8,8,5,8,6,7,8,6,0,6],
[3,4,7,4,3,4,3,1,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 98, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,7,4,7,6,7,8,6,4],
[5,0,6,4,7,5,8,8,5,5],
[4,5,0,5,4,8,8,5,2,4],
[7,7,6,0,7,5,6,7,6,5],
[4,4,7,4,0,7,9,6,3,4],
[5,6,3,6,4,0,7,5,3,6],
[4,3,3,5,2,4,0,2,1,5],
[3,3,6,4,5,6,9,0,5,6],
[5,6,9,5,8,8,10,6,0,4],
[7,6,7,6,7,5,6,5,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 99, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,7,7,6,6,6,7,5,7],
[7,0,8,6,7,4,4,6,1,6],
[4,3,0,6,5,2,2,4,1,3],
[4,5,5,0,5,5,5,4,3,6],
[5,4,6,6,0,5,5,4,1,4],
[5,7,9,6,6,0,6,2,7,9],
[5,7,9,6,6,5,0,4,7,7],
[4,5,7,7,7,9,7,0,5,7],
[6,10,10,8,10,4,4,6,0,8],
[4,5,8,5,7,2,4,4,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 100, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,4,5,6,4,6,4,0,5],
[6,0,5,8,8,7,7,4,3,8],
[7,6,0,3,6,4,6,2,0,3],
[6,3,8,0,3,4,10,7,5,5],
[5,3,5,8,0,5,9,4,5,6],
[7,4,7,7,6,0,9,4,4,7],
[5,4,5,1,2,2,0,2,1,4],
[7,7,9,4,7,7,9,0,6,9],
[11,8,11,6,6,7,10,5,0,5],
[6,3,8,6,5,4,7,2,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 101, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,6,5,5,6,4,7,3,7],
[4,0,6,5,4,4,3,3,4,6],
[5,5,0,8,6,3,4,5,4,6],
[6,6,3,0,8,5,5,6,4,7],
[6,7,5,3,0,6,6,6,4,5],
[5,7,8,6,5,0,6,6,5,6],
[7,8,7,6,5,5,0,6,7,9],
[4,8,6,5,5,5,5,0,4,8],
[8,7,7,7,7,6,4,7,0,10],
[4,5,5,4,6,5,2,3,1,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 102, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,8,5,7,5,7,8,8,9],
[8,0,7,8,8,6,7,9,5,8],
[3,4,0,4,6,6,7,7,7,5],
[6,3,7,0,7,5,7,10,8,5],
[4,3,5,4,0,3,6,7,5,3],
[6,5,5,6,8,0,5,7,6,8],
[4,4,4,4,5,6,0,4,8,4],
[3,2,4,1,4,4,7,0,4,5],
[3,6,4,3,6,5,3,7,0,5],
[2,3,6,6,8,3,7,6,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 103, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,7,4,7,6,8,6,5,7],
[6,0,7,6,8,5,8,7,7,7],
[4,4,0,3,7,3,3,4,3,5],
[7,5,8,0,5,3,5,6,4,6],
[4,3,4,6,0,5,7,5,6,6],
[5,6,8,8,6,0,7,6,6,7],
[3,3,8,6,4,4,0,6,6,6],
[5,4,7,5,6,5,5,0,5,7],
[6,4,8,7,5,5,5,6,0,6],
[4,4,6,5,5,4,5,4,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 104, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,7,7,7,6,4,7,4,9],
[4,0,6,5,4,5,4,5,4,5],
[4,5,0,6,6,5,6,3,4,6],
[4,6,5,0,6,5,4,1,6,5],
[4,7,5,5,0,4,4,4,6,6],
[5,6,6,6,7,0,4,2,7,7],
[7,7,5,7,7,7,0,3,7,7],
[4,6,8,10,7,9,8,0,6,9],
[7,7,7,5,5,4,4,5,0,5],
[2,6,5,6,5,4,4,2,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 105, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,1,8,9,6,9,3,3,6],
[6,0,5,6,7,6,6,5,1,3],
[10,6,0,10,11,6,9,5,4,7],
[3,5,1,0,7,5,4,2,2,5],
[2,4,0,4,0,6,3,2,3,3],
[5,5,5,6,5,0,5,5,2,3],
[2,5,2,7,8,6,0,2,4,2],
[8,6,6,9,9,6,9,0,3,7],
[8,10,7,9,8,9,7,8,0,4],
[5,8,4,6,8,8,9,4,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 106, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,6,8,5,6,2,5,2,4],
[7,0,7,6,7,5,4,7,8,5],
[5,4,0,6,6,4,3,5,4,5],
[3,5,5,0,3,4,4,4,4,5],
[6,4,5,8,0,6,6,7,6,6],
[5,6,7,7,5,0,1,8,6,8],
[9,7,8,7,5,10,0,10,9,9],
[6,4,6,7,4,3,1,0,7,4],
[9,3,7,7,5,5,2,4,0,5],
[7,6,6,6,5,3,2,7,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 107, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,4,3,5,4,5,4,7,8],
[6,0,7,4,7,7,8,7,6,8],
[7,4,0,6,8,6,4,4,7,7],
[8,7,5,0,5,7,6,5,6,8],
[6,4,3,6,0,5,4,5,5,8],
[7,4,5,4,6,0,4,7,4,7],
[6,3,7,5,7,7,0,7,4,8],
[7,4,7,6,6,4,4,0,4,7],
[4,5,4,5,6,7,7,7,0,10],
[3,3,4,3,3,4,3,4,1,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 108, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,7,6,5,4,7,6,4,7],
[8,0,7,5,7,6,8,6,4,6],
[4,4,0,7,5,5,6,6,4,7],
[5,6,4,0,7,7,6,6,6,5],
[6,4,6,4,0,4,7,8,6,7],
[7,5,6,4,7,0,8,7,4,4],
[4,3,5,5,4,3,0,5,4,5],
[5,5,5,5,3,4,6,0,4,7],
[7,7,7,5,5,7,7,7,0,5],
[4,5,4,6,4,7,6,4,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 109, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1,4,3,2,8,1,3,6,7],
[10,0,5,4,4,11,6,7,9,10],
[7,6,0,6,3,9,5,4,7,9],
[8,7,5,0,5,9,5,7,5,8],
[9,7,8,6,0,11,4,7,9,10],
[3,0,2,2,0,0,1,0,3,5],
[10,5,6,6,7,10,0,5,8,8],
[8,4,7,4,4,11,6,0,7,7],
[5,2,4,6,2,8,3,4,0,7],
[4,1,2,3,1,6,3,4,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 110, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,4,1,5,4,5,4,4,7],
[4,0,4,2,3,6,6,1,4,6],
[7,7,0,4,6,4,7,5,5,8],
[10,9,7,0,6,5,9,4,8,10],
[6,8,5,5,0,5,7,7,5,7],
[7,5,7,6,6,0,7,4,7,7],
[6,5,4,2,4,4,0,5,8,9],
[7,10,6,7,4,7,6,0,4,6],
[7,7,6,3,6,4,3,7,0,6],
[4,5,3,1,4,4,2,5,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 111, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,6,7,4,5,6,5,4,4],
[4,0,7,8,7,4,8,4,6,7],
[5,4,0,4,5,5,3,5,7,2],
[4,3,7,0,4,4,5,4,6,5],
[7,4,6,7,0,7,6,4,5,4],
[6,7,6,7,4,0,7,5,6,7],
[5,3,8,6,5,4,0,4,6,4],
[6,7,6,7,7,6,7,0,5,6],
[7,5,4,5,6,5,5,6,0,5],
[7,4,9,6,7,4,7,5,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 112, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,9,9,5,7,7,5,3,7],
[7,0,8,9,5,7,8,5,6,8],
[2,3,0,5,2,6,4,5,4,6],
[2,2,6,0,0,5,5,3,5,5],
[6,6,9,11,0,7,8,5,5,7],
[4,4,5,6,4,0,4,4,3,7],
[4,3,7,6,3,7,0,5,4,4],
[6,6,6,8,6,7,6,0,5,7],
[8,5,7,6,6,8,7,6,0,9],
[4,3,5,6,4,4,7,4,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 113, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,1,4,0,3,4,4,6,4],
[7,0,1,0,1,4,5,1,3,4],
[10,10,0,7,7,7,7,4,6,10],
[7,11,4,0,4,4,5,4,6,7],
[11,10,4,7,0,10,10,8,9,10],
[8,7,4,7,1,0,4,2,6,7],
[7,6,4,6,1,7,0,1,6,10],
[7,10,7,7,3,9,10,0,9,10],
[5,8,5,5,2,5,5,2,0,5],
[7,7,1,4,1,4,1,1,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 114, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,7,6,4,5,9,5,6,6],
[5,0,8,4,6,6,7,4,6,6],
[4,3,0,3,5,5,4,5,3,5],
[5,7,8,0,6,5,7,8,7,6],
[7,5,6,5,0,7,7,5,7,8],
[6,5,6,6,4,0,8,6,6,7],
[2,4,7,4,4,3,0,5,4,5],
[6,7,6,3,6,5,6,0,3,5],
[5,5,8,4,4,5,7,8,0,6],
[5,5,6,5,3,4,6,6,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 115, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,4,7,8,5,7,8,11,10],
[6,0,7,4,7,6,6,6,9,8],
[7,4,0,5,8,7,5,7,8,7],
[4,7,6,0,7,6,4,4,9,6],
[3,4,3,4,0,3,4,5,4,2],
[6,5,4,5,8,0,7,8,11,10],
[4,5,6,7,7,4,0,6,7,4],
[3,5,4,7,6,3,5,0,7,6],
[0,2,3,2,7,0,4,4,0,4],
[1,3,4,5,9,1,7,5,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 116, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,7,8,5,4,8,5,6,4],
[6,0,7,8,6,6,10,5,4,5],
[4,4,0,4,6,5,8,5,5,6],
[3,3,7,0,7,5,7,5,4,6],
[6,5,5,4,0,5,5,7,5,5],
[7,5,6,6,6,0,7,2,6,8],
[3,1,3,4,6,4,0,3,4,4],
[6,6,6,6,4,9,8,0,6,7],
[5,7,6,7,6,5,7,5,0,5],
[7,6,5,5,6,3,7,4,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 117, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,4,6,4,6,2,3,4,4],
[8,0,3,5,3,6,3,3,4,5],
[7,8,0,7,7,7,7,3,6,7],
[5,6,4,0,5,5,5,6,6,6],
[7,8,4,6,0,7,5,3,4,8],
[5,5,4,6,4,0,4,4,3,5],
[9,8,4,6,6,7,0,3,6,8],
[8,8,8,5,8,7,8,0,9,8],
[7,7,5,5,7,8,5,2,0,7],
[7,6,4,5,3,6,3,3,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 118, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,6,9,8,7,5,6,5,9],
[4,0,3,5,5,2,4,1,5,4],
[5,8,0,8,7,4,2,8,5,8],
[2,6,3,0,5,4,4,6,7,4],
[3,6,4,6,0,3,5,4,5,6],
[4,9,7,7,8,0,6,9,6,9],
[6,7,9,7,6,5,0,7,6,7],
[5,10,3,5,7,2,4,0,7,7],
[6,6,6,4,6,5,5,4,0,8],
[2,7,3,7,5,2,4,4,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 119, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,3,7,6,8,5,9,6,6],
[6,0,5,9,6,8,6,6,7,5],
[8,6,0,10,8,7,7,11,7,5],
[4,2,1,0,3,7,4,5,5,3],
[5,5,3,8,0,7,6,8,5,3],
[3,3,4,4,4,0,4,5,2,5],
[6,5,4,7,5,7,0,10,6,6],
[2,5,0,6,3,6,1,0,3,3],
[5,4,4,6,6,9,5,8,0,5],
[5,6,6,8,8,6,5,8,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 120, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,6,7,7,6,7,7,8,5],
[8,0,6,10,7,8,9,8,10,5],
[5,5,0,5,5,7,5,6,7,5],
[4,1,6,0,7,6,6,7,8,4],
[4,4,6,4,0,6,6,7,6,5],
[5,3,4,5,5,0,6,7,8,6],
[4,2,6,5,5,5,0,5,7,4],
[4,3,5,4,4,4,6,0,6,4],
[3,1,4,3,5,3,4,5,0,2],
[6,6,6,7,6,5,7,7,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 121, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,9,9,4,3,3,3,6,8],
[5,0,11,7,4,7,5,5,5,7],
[2,0,0,0,1,1,1,0,1,3],
[2,4,11,0,1,2,2,0,2,4],
[7,7,10,10,0,4,4,6,8,10],
[8,4,10,9,7,0,8,8,8,10],
[8,6,10,9,7,3,0,9,8,10],
[8,6,11,11,5,3,2,0,5,10],
[5,6,10,9,3,3,3,6,0,7],
[3,4,8,7,1,1,1,1,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 122, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,7,6,10,5,6,5,4,8],
[4,0,7,5,8,3,7,3,2,6],
[4,4,0,6,5,4,3,6,6,6],
[5,6,5,0,9,4,4,6,3,5],
[1,3,6,2,0,3,3,4,2,3],
[6,8,7,7,8,0,6,9,2,8],
[5,4,8,7,8,5,0,5,6,5],
[6,8,5,5,7,2,6,0,2,5],
[7,9,5,8,9,9,5,9,0,8],
[3,5,5,6,8,3,6,6,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 123, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,5,5,6,7,4,7,5,5],
[4,0,5,2,5,6,5,8,4,4],
[6,6,0,4,5,5,4,4,4,5],
[6,9,7,0,5,7,5,8,5,5],
[5,6,6,6,0,7,5,5,6,7],
[4,5,6,4,4,0,6,7,4,6],
[7,6,7,6,6,5,0,8,5,7],
[4,3,7,3,6,4,3,0,5,4],
[6,7,7,6,5,7,6,6,0,5],
[6,7,6,6,4,5,4,7,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 124, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,5,6,6,8,7,6,3,6],
[5,0,5,5,6,8,7,5,6,6],
[6,6,0,8,6,10,9,6,5,7],
[5,6,3,0,6,7,7,7,4,5],
[5,5,5,5,0,8,8,6,4,7],
[3,3,1,4,3,0,5,4,2,3],
[4,4,2,4,3,6,0,2,2,2],
[5,6,5,4,5,7,9,0,4,6],
[8,5,6,7,7,9,9,7,0,7],
[5,5,4,6,4,8,9,5,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 125, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,1,4,7,7,7,8,2,6],
[3,0,2,2,5,6,4,5,2,3],
[10,9,0,4,9,7,9,7,6,6],
[7,9,7,0,8,7,7,9,7,5],
[4,6,2,3,0,7,7,8,3,3],
[4,5,4,4,4,0,7,6,5,3],
[4,7,2,4,4,4,0,4,3,6],
[3,6,4,2,3,5,7,0,4,4],
[9,9,5,4,8,6,8,7,0,4],
[5,8,5,6,8,8,5,7,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 126, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,6,6,3,5,3,5,6,2],
[5,0,5,2,3,5,3,5,7,3],
[5,6,0,4,6,5,4,3,4,1],
[5,9,7,0,5,6,6,7,6,4],
[8,8,5,6,0,7,5,6,6,5],
[6,6,6,5,4,0,5,6,5,4],
[8,8,7,5,6,6,0,7,5,3],
[6,6,8,4,5,5,4,0,7,6],
[5,4,7,5,5,6,6,4,0,4],
[9,8,10,7,6,7,8,5,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 127, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,5,8,1,7,5,6,5,5],
[5,0,5,5,5,8,3,7,5,4],
[6,6,0,8,4,10,7,6,5,5],
[3,6,3,0,3,6,5,4,4,2],
[10,6,7,8,0,9,5,8,6,8],
[4,3,1,5,2,0,3,3,1,1],
[6,8,4,6,6,8,0,8,8,5],
[5,4,5,7,3,8,3,0,4,4],
[6,6,6,7,5,10,3,7,0,6],
[6,7,6,9,3,10,6,7,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 128, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,4,3,0,8,3,3,3,3],
[3,0,3,3,3,0,2,2,2,3],
[7,8,0,5,2,5,2,2,2,0],
[8,8,6,0,3,5,0,7,2,1],
[11,8,9,8,0,8,3,10,5,3],
[3,11,6,6,3,0,3,5,6,3],
[8,9,9,11,8,8,0,10,5,6],
[8,9,9,4,1,6,1,0,4,1],
[8,9,9,9,6,5,6,7,0,6],
[8,8,11,10,8,8,5,10,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 129, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,1,4,2,5,2,3,2,3],
[9,0,6,6,2,6,5,4,5,7],
[10,5,0,6,6,7,7,6,7,8],
[7,5,5,0,1,6,5,5,3,6],
[9,9,5,10,0,8,7,8,7,7],
[6,5,4,5,3,0,4,6,5,7],
[9,6,4,6,4,7,0,8,7,6],
[8,7,5,6,3,5,3,0,4,5],
[9,6,4,8,4,6,4,7,0,7],
[8,4,3,5,4,4,5,6,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 130, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,5,4,3,4,5,5,7,5],
[6,0,7,6,4,6,5,7,7,6],
[6,4,0,4,6,4,6,7,8,5],
[7,5,7,0,5,4,5,6,7,7],
[8,7,5,6,0,7,7,9,8,6],
[7,5,7,7,4,0,5,7,7,7],
[6,6,5,6,4,6,0,8,7,7],
[6,4,4,5,2,4,3,0,6,4],
[4,4,3,4,3,4,4,5,0,3],
[6,5,6,4,5,4,4,7,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 131, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,4,5,6,4,6,6,7,6],
[6,0,5,7,7,4,4,7,5,9],
[7,6,0,5,5,7,7,7,6,6],
[6,4,6,0,8,6,6,8,6,5],
[5,4,6,3,0,4,5,7,5,4],
[7,7,4,5,7,0,8,7,8,6],
[5,7,4,5,6,3,0,5,7,6],
[5,4,4,3,4,4,6,0,5,4],
[4,6,5,5,6,3,4,6,0,7],
[5,2,5,6,7,5,5,7,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 132, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,7,4,2,8,5,4,5,4],
[8,0,7,5,6,8,6,8,6,5],
[4,4,0,2,3,7,3,3,2,2],
[7,6,9,0,3,9,6,6,5,6],
[9,5,8,8,0,8,7,7,9,8],
[3,3,4,2,3,0,5,3,3,2],
[6,5,8,5,4,6,0,5,7,5],
[7,3,8,5,4,8,6,0,7,4],
[6,5,9,6,2,8,4,4,0,6],
[7,6,9,5,3,9,6,7,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 133, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,0,4,4,8,4,4,4,0],
[7,0,4,4,4,4,4,7,4,0],
[11,7,0,11,11,8,7,11,4,3],
[7,7,0,0,7,8,7,11,4,3],
[7,7,0,4,0,4,7,11,4,0],
[3,7,3,3,7,0,7,7,7,3],
[7,7,4,4,4,4,0,11,4,0],
[7,4,0,0,0,4,0,0,0,0],
[7,7,7,7,7,4,7,11,0,7],
[11,11,8,8,11,8,11,11,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 134, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,5,5,8,7,3,8,5,6],
[7,0,5,8,10,10,8,8,6,4],
[6,6,0,6,6,7,5,7,5,4],
[6,3,5,0,9,9,4,7,5,3],
[3,1,5,2,0,5,2,4,3,4],
[4,1,4,2,6,0,2,4,2,3],
[8,3,6,7,9,9,0,8,4,6],
[3,3,4,4,7,7,3,0,4,3],
[6,5,6,6,8,9,7,7,0,4],
[5,7,7,8,7,8,5,8,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 135, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,6,3,5,5,3,3,7,8],
[3,0,3,4,3,7,3,3,4,3],
[5,8,0,3,4,7,6,2,7,10],
[8,7,8,0,5,5,6,6,8,10],
[6,8,7,6,0,8,8,5,8,11],
[6,4,4,6,3,0,6,4,7,6],
[8,8,5,5,3,5,0,4,9,8],
[8,8,9,5,6,7,7,0,8,11],
[4,7,4,3,3,4,2,3,0,6],
[3,8,1,1,0,5,3,0,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 136, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,5,5,7,5,6,0,7,4],
[2,0,0,0,2,0,2,2,2,0],
[6,11,0,6,6,4,6,6,7,6],
[6,11,5,0,2,9,6,2,7,4],
[4,9,5,9,0,9,6,4,7,4],
[6,11,7,2,2,0,6,2,7,6],
[5,9,5,5,5,5,0,0,5,0],
[11,9,5,9,7,9,11,0,7,9],
[4,9,4,4,4,4,6,4,0,4],
[7,11,5,7,7,5,11,2,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 137, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,9,3,6,5,3,7,1,2],
[8,0,7,5,5,6,4,8,3,3],
[2,4,0,4,2,6,2,6,2,2],
[8,6,7,0,5,9,6,10,3,5],
[5,6,9,6,0,5,6,6,4,6],
[6,5,5,2,6,0,2,5,0,1],
[8,7,9,5,5,9,0,8,4,7],
[4,3,5,1,5,6,3,0,0,3],
[10,8,9,8,7,11,7,11,0,5],
[9,8,9,6,5,10,4,8,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 138, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,5,9,4,6,7,2,5,0],
[5,0,5,11,4,6,7,5,5,2],
[6,6,0,8,4,8,4,2,2,2],
[2,0,3,0,4,4,7,2,3,0],
[7,7,7,7,0,8,7,7,7,2],
[5,5,3,7,3,0,3,5,5,0],
[4,4,7,4,4,8,0,4,7,2],
[9,6,9,9,4,6,7,0,9,6],
[6,6,9,8,4,6,4,2,0,6],
[11,9,9,11,9,11,9,5,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 139, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,7,8,4,5,6,6,8,5],
[6,0,7,9,4,8,7,7,9,5],
[4,4,0,7,6,3,3,5,5,7],
[3,2,4,0,1,3,4,7,5,5],
[7,7,5,10,0,6,5,8,8,8],
[6,3,8,8,5,0,8,5,9,5],
[5,4,8,7,6,3,0,7,7,6],
[5,4,6,4,3,6,4,0,6,3],
[3,2,6,6,3,2,4,5,0,5],
[6,6,4,6,3,6,5,8,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 140, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,6,5,3,4,6,4,6,7],
[8,0,4,5,6,5,7,4,7,8],
[5,7,0,8,5,5,6,6,7,6],
[6,6,3,0,6,4,8,6,5,7],
[8,5,6,5,0,5,9,7,6,6],
[7,6,6,7,6,0,8,5,5,7],
[5,4,5,3,2,3,0,5,6,6],
[7,7,5,5,4,6,6,0,5,5],
[5,4,4,6,5,6,5,6,0,7],
[4,3,5,4,5,4,5,6,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 141, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,6,9,6,4,2,9,4,4],
[7,0,6,11,6,9,2,9,6,7],
[5,5,0,5,7,5,7,5,9,5],
[2,0,6,0,6,4,2,9,6,2],
[5,5,4,5,0,5,5,5,9,5],
[7,2,6,7,6,0,2,7,6,7],
[9,9,4,9,6,9,0,9,9,9],
[2,2,6,2,6,4,2,0,6,2],
[7,5,2,5,2,5,2,5,0,5],
[7,4,6,9,6,4,2,9,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 142, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,7,5,6,8,6,3,6,5],
[5,0,6,6,7,7,5,5,5,6],
[4,5,0,5,6,3,4,3,4,3],
[6,5,6,0,7,4,5,7,4,6],
[5,4,5,4,0,4,4,3,4,4],
[3,4,8,7,7,0,5,6,5,8],
[5,6,7,6,7,6,0,5,6,6],
[8,6,8,4,8,5,6,0,4,8],
[5,6,7,7,7,6,5,7,0,7],
[6,5,8,5,7,3,5,3,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 143, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,2,6,11,7,2,11,6,11],
[5,0,7,2,7,7,2,7,2,7],
[9,4,0,6,9,7,6,11,4,9],
[5,9,5,0,9,5,5,9,4,9],
[0,4,2,2,0,2,2,11,4,11],
[4,4,4,6,9,0,6,11,4,9],
[9,9,5,6,9,5,0,9,4,9],
[0,4,0,2,0,0,2,0,0,0],
[5,9,7,7,7,7,7,11,0,7],
[0,4,2,2,0,2,2,11,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 144, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,6,5,8,6,7,6,4,6],
[6,0,8,7,8,5,7,5,5,5],
[5,3,0,5,7,3,2,3,2,3],
[6,4,6,0,6,3,4,3,2,3],
[3,3,4,5,0,2,1,1,1,3],
[5,6,8,8,9,0,7,4,6,5],
[4,4,9,7,10,4,0,3,3,3],
[5,6,8,8,10,7,8,0,6,6],
[7,6,9,9,10,5,8,5,0,6],
[5,6,8,8,8,6,8,5,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 145, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,4,2,8,2,0,5,2,4],
[8,0,8,10,9,7,5,8,7,7],
[7,3,0,5,8,4,2,8,2,3],
[9,1,6,0,6,5,6,5,7,4],
[3,2,3,5,0,2,0,5,2,0],
[9,4,7,6,9,0,7,6,5,7],
[11,6,9,5,11,4,0,8,5,9],
[6,3,3,6,6,5,3,0,5,4],
[9,4,9,4,9,6,6,6,0,7],
[7,4,8,7,11,4,2,7,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 146, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,5,5,10,1,3,3,6,3],
[6,0,6,6,6,4,7,7,7,4],
[6,5,0,6,6,3,6,6,9,6],
[6,5,5,0,7,4,3,3,3,0],
[1,5,5,4,0,1,3,4,7,4],
[10,7,8,7,10,0,7,3,8,7],
[8,4,5,8,8,4,0,4,6,6],
[8,4,5,8,7,8,7,0,6,8],
[5,4,2,8,4,3,5,5,0,5],
[8,7,5,11,7,4,5,3,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 147, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,4,3,5,4,5,6,6,4],
[5,0,6,5,6,6,6,4,7,6],
[7,5,0,5,6,6,6,6,8,6],
[8,6,6,0,6,5,9,5,8,4],
[6,5,5,5,0,5,6,6,6,4],
[7,5,5,6,6,0,7,6,7,6],
[6,5,5,2,5,4,0,3,6,4],
[5,7,5,6,5,5,8,0,5,4],
[5,4,3,3,5,4,5,6,0,3],
[7,5,5,7,7,5,7,7,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 148, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,7,2,7,5,4,6,6,8],
[5,0,5,4,7,6,3,4,6,4],
[4,6,0,3,7,6,4,7,6,3],
[9,7,8,0,9,7,5,7,6,9],
[4,4,4,2,0,6,3,3,4,4],
[6,5,5,4,5,0,5,5,4,4],
[7,8,7,6,8,6,0,6,5,6],
[5,7,4,4,8,6,5,0,5,4],
[5,5,5,5,7,7,6,6,0,5],
[3,7,8,2,7,7,5,7,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 149, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,6,7,5,7,5,4,8,6],
[6,0,6,6,4,7,4,6,6,8],
[5,5,0,5,5,5,6,4,6,7],
[4,5,6,0,6,6,5,2,6,5],
[6,7,6,5,0,4,4,4,5,5],
[4,4,6,5,7,0,6,4,6,9],
[6,7,5,6,7,5,0,4,6,7],
[7,5,7,9,7,7,7,0,7,8],
[3,5,5,5,6,5,5,4,0,4],
[5,3,4,6,6,2,4,3,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 150, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,6,7,5,6,8,6,6,6],
[6,0,5,6,4,5,7,6,4,4],
[5,6,0,5,3,5,5,7,5,4],
[4,5,6,0,6,4,6,4,6,5],
[6,7,8,5,0,7,8,7,7,6],
[5,6,6,7,4,0,6,7,5,6],
[3,4,6,5,3,5,0,6,4,4],
[5,5,4,7,4,4,5,0,6,6],
[5,7,6,5,4,6,7,5,0,5],
[5,7,7,6,5,5,7,5,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 151, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,7,5,7,6,7,4,5,6],
[4,0,7,6,7,8,8,6,7,7],
[4,4,0,4,5,5,5,4,3,4],
[6,5,7,0,7,7,8,6,7,6],
[4,4,6,4,0,4,4,4,4,4],
[5,3,6,4,7,0,7,6,7,5],
[4,3,6,3,7,4,0,4,5,4],
[7,5,7,5,7,5,7,0,4,6],
[6,4,8,4,7,4,6,7,0,4],
[5,4,7,5,7,6,7,5,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 152, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,4,7,5,6,5,7,5,6],
[7,0,6,7,4,6,5,10,5,9],
[7,5,0,5,4,7,7,6,4,8],
[4,4,6,0,1,5,3,7,3,8],
[6,7,7,10,0,6,5,8,7,8],
[5,5,4,6,5,0,5,5,5,6],
[6,6,4,8,6,6,0,7,5,9],
[4,1,5,4,3,6,4,0,2,7],
[6,6,7,8,4,6,6,9,0,7],
[5,2,3,3,3,5,2,4,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 153, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,2,4,6,7,8,6,6,5],
[8,0,6,6,8,9,8,8,4,9],
[9,5,0,9,7,7,7,9,4,7],
[7,5,2,0,6,7,6,6,4,7],
[5,3,4,5,0,7,6,6,6,7],
[4,2,4,4,4,0,8,4,6,8],
[3,3,4,5,5,3,0,2,2,5],
[5,3,2,5,5,7,9,0,4,9],
[5,7,7,7,5,5,9,7,0,7],
[6,2,4,4,4,3,6,2,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 154, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,6,5,5,6,3,5,4,8],
[5,0,4,5,6,5,5,6,8,9],
[5,7,0,4,5,5,5,6,6,8],
[6,6,7,0,5,7,7,5,5,9],
[6,5,6,6,0,7,3,5,4,8],
[5,6,6,4,4,0,5,6,6,7],
[8,6,6,4,8,6,0,7,9,8],
[6,5,5,6,6,5,4,0,5,10],
[7,3,5,6,7,5,2,6,0,8],
[3,2,3,2,3,4,3,1,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 155, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,6,8,5,5,4,5,4,6],
[5,0,3,8,6,8,7,5,7,8],
[5,8,0,9,7,7,8,8,7,8],
[3,3,2,0,5,7,6,1,5,5],
[6,5,4,6,0,3,4,3,4,4],
[6,3,4,4,8,0,5,3,4,4],
[7,4,3,5,7,6,0,3,4,4],
[6,6,3,10,8,8,8,0,8,9],
[7,4,4,6,7,7,7,3,0,6],
[5,3,3,6,7,7,7,2,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 156, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,6,5,8,3,2,5,5,4],
[3,0,3,5,4,6,3,6,5,7],
[5,8,0,7,3,5,5,6,8,6],
[6,6,4,0,4,1,0,3,4,4],
[3,7,8,7,0,3,5,6,8,6],
[8,5,6,10,8,0,8,4,6,8],
[9,8,6,11,6,3,0,5,6,6],
[6,5,5,8,5,7,6,0,7,4],
[6,6,3,7,3,5,5,4,0,4],
[7,4,5,7,5,3,5,7,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 157, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,2,8,3,5,4,5,7,8],
[7,0,5,7,2,7,4,7,7,6],
[9,6,0,9,6,6,7,5,9,9],
[3,4,2,0,3,6,4,4,9,4],
[8,9,5,8,0,9,8,7,8,8],
[6,4,5,5,2,0,3,5,8,7],
[7,7,4,7,3,8,0,6,8,6],
[6,4,6,7,4,6,5,0,6,6],
[4,4,2,2,3,3,3,5,0,2],
[3,5,2,7,3,4,5,5,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 158, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,6,6,5,5,4,5,6,5],
[6,0,9,7,7,7,6,5,6,7],
[5,2,0,4,4,5,3,5,6,7],
[5,4,7,0,3,3,4,4,5,5],
[6,4,7,8,0,6,5,5,6,8],
[6,4,6,8,5,0,3,6,5,6],
[7,5,8,7,6,8,0,7,6,8],
[6,6,6,7,6,5,4,0,6,6],
[5,5,5,6,5,6,5,5,0,6],
[6,4,4,6,3,5,3,5,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 159, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,8,11,6,5,9,6,11,7],
[0,0,6,5,3,2,6,3,1,5],
[3,5,0,7,3,3,8,5,3,7],
[0,6,4,0,2,4,5,4,0,4],
[5,8,8,9,0,3,7,4,5,6],
[6,9,8,7,8,0,6,5,6,5],
[2,5,3,6,4,5,0,5,4,6],
[5,8,6,7,7,6,6,0,5,4],
[0,10,8,11,6,5,7,6,0,7],
[4,6,4,7,5,6,5,7,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 160, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,4,3,3,5,6,5,4,4],
[5,0,4,6,5,6,5,4,5,3],
[7,7,0,6,6,10,3,9,8,7],
[8,5,5,0,6,7,6,6,6,6],
[8,6,5,5,0,8,5,5,6,3],
[6,5,1,4,3,0,4,4,5,2],
[5,6,8,5,6,7,0,6,6,6],
[6,7,2,5,6,7,5,0,7,3],
[7,6,3,5,5,6,5,4,0,3],
[7,8,4,5,8,9,5,8,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 161, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,6,6,7,6,2,4,3,2],
[7,0,5,6,7,7,4,5,4,3],
[5,6,0,6,4,5,3,4,3,3],
[5,5,5,0,5,4,5,6,5,5],
[4,4,7,6,0,5,5,3,4,2],
[5,4,6,7,6,0,5,2,6,5],
[9,7,8,6,6,6,0,7,6,5],
[7,6,7,5,8,9,4,0,4,4],
[8,7,8,6,7,5,5,7,0,6],
[9,8,8,6,9,6,6,7,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 162, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,7,6,6,4,5,7,6,5],
[7,0,5,7,6,6,5,8,8,6],
[4,6,0,5,5,3,2,5,7,4],
[5,4,6,0,4,2,2,4,5,4],
[5,5,6,7,0,6,5,8,5,8],
[7,5,8,9,5,0,6,9,8,6],
[6,6,9,9,6,5,0,8,8,6],
[4,3,6,7,3,2,3,0,5,4],
[5,3,4,6,6,3,3,6,0,6],
[6,5,7,7,3,5,5,7,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 163, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,0,5,4,2,1,3,2,5],
[7,0,5,7,5,4,1,4,5,6],
[11,6,0,6,4,2,2,6,4,6],
[6,4,5,0,4,1,3,3,2,6],
[7,6,7,7,0,8,5,5,7,8],
[9,7,9,10,3,0,8,5,7,7],
[10,10,9,8,6,3,0,5,4,5],
[8,7,5,8,6,6,6,0,5,6],
[9,6,7,9,4,4,7,6,0,10],
[6,5,5,5,3,4,6,5,1,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 164, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,9,7,9,6,11,11,9,5],
[4,0,7,7,7,8,11,11,7,7],
[2,4,0,5,6,8,9,8,8,2],
[4,4,6,0,6,6,6,8,6,4],
[2,4,5,5,0,6,9,9,9,5],
[5,3,3,5,5,0,9,11,7,5],
[0,0,2,5,2,2,0,8,2,2],
[0,0,3,3,2,0,3,0,3,3],
[2,4,3,5,2,4,9,8,0,2],
[6,4,9,7,6,6,9,8,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 165, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,10,7,4,6,10,7,5,6],
[4,0,7,4,4,2,7,4,5,5],
[1,4,0,4,2,4,4,4,4,4],
[4,7,7,0,4,5,6,8,3,5],
[7,7,9,7,0,7,8,8,5,7],
[5,9,7,6,4,0,7,8,7,8],
[1,4,7,5,3,4,0,5,4,4],
[4,7,7,3,3,3,6,0,5,5],
[6,6,7,8,6,4,7,6,0,8],
[5,6,7,6,4,3,7,6,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 166, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1,5,1,6,5,4,8,3,4],
[10,0,9,3,8,7,6,10,7,6],
[6,2,0,2,5,4,1,5,5,3],
[10,8,9,0,8,7,8,10,5,8],
[5,3,6,3,0,5,4,5,5,3],
[6,4,7,4,6,0,4,9,6,3],
[7,5,10,3,7,7,0,7,7,5],
[3,1,6,1,6,2,4,0,3,1],
[8,4,6,6,6,5,4,8,0,5],
[7,5,8,3,8,8,6,10,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 167, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1,5,11,10,9,3,3,4,4],
[10,0,8,10,10,8,5,8,5,3],
[6,3,0,8,5,6,6,4,1,4],
[0,1,3,0,2,2,1,0,4,0],
[1,1,6,9,0,6,3,3,4,1],
[2,3,5,9,5,0,3,1,6,3],
[8,6,5,10,8,8,0,6,6,8],
[8,3,7,11,8,10,5,0,6,6],
[7,6,10,7,7,5,5,5,0,5],
[7,8,7,11,10,8,3,5,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 168, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,5,5,4,3,8,7,4,7],
[6,0,6,6,4,5,7,5,5,6],
[6,5,0,5,4,5,5,7,5,6],
[6,5,6,0,6,5,7,6,3,5],
[7,7,7,5,0,5,7,7,4,6],
[8,6,6,6,6,0,5,8,5,7],
[3,4,6,4,4,6,0,6,5,4],
[4,6,4,5,4,3,5,0,2,5],
[7,6,6,8,7,6,6,9,0,5],
[4,5,5,6,5,4,7,6,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 169, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,0,2,8,1,4,6,7,1],
[7,0,2,6,9,2,6,6,6,3],
[11,9,0,7,9,5,9,9,8,8],
[9,5,4,0,8,5,4,9,8,4],
[3,2,2,3,0,3,3,3,6,3],
[10,9,6,6,8,0,7,8,8,5],
[7,5,2,7,8,4,0,9,8,2],
[5,5,2,2,8,3,2,0,7,3],
[4,5,3,3,5,3,3,4,0,2],
[10,8,3,7,8,6,9,8,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 170, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,2,5,4,5,4,2,7,3],
[3,0,1,3,2,2,4,0,2,0],
[9,10,0,9,7,9,9,6,9,5],
[6,8,2,0,5,7,5,3,7,3],
[7,9,4,6,0,6,8,1,7,7],
[6,9,2,4,5,0,6,1,8,4],
[7,7,2,6,3,5,0,3,6,0],
[9,11,5,8,10,10,8,0,10,7],
[4,9,2,4,4,3,5,1,0,0],
[8,11,6,8,4,7,11,4,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 171, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,7,7,8,7,8,9,5,5],
[5,0,3,7,8,7,9,9,5,3],
[4,8,0,7,7,7,7,6,8,4],
[4,4,4,0,8,6,7,8,6,4],
[3,3,4,3,0,5,7,8,4,4],
[4,4,4,5,6,0,5,6,6,6],
[3,2,4,4,4,6,0,7,4,2],
[2,2,5,3,3,5,4,0,3,3],
[6,6,3,5,7,5,7,8,0,7],
[6,8,7,7,7,5,9,8,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 172, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,4,5,6,5,6,5,6,4],
[7,0,6,6,7,8,7,4,6,7],
[7,5,0,7,8,5,6,6,5,7],
[6,5,4,0,5,7,7,4,7,5],
[5,4,3,6,0,4,8,3,6,5],
[6,3,6,4,7,0,7,5,6,7],
[5,4,5,4,3,4,0,2,5,4],
[6,7,5,7,8,6,9,0,9,7],
[5,5,6,4,5,5,6,2,0,3],
[7,4,4,6,6,4,7,4,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 173, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,4,6,5,4,7,6,6,6],
[6,0,4,5,5,6,5,6,6,7],
[7,7,0,7,5,6,8,8,6,4],
[5,6,4,0,6,4,4,7,5,6],
[6,6,6,5,0,4,7,7,5,6],
[7,5,5,7,7,0,7,5,7,7],
[4,6,3,7,4,4,0,7,5,6],
[5,5,3,4,4,6,4,0,6,6],
[5,5,5,6,6,4,6,5,0,6],
[5,4,7,5,5,4,5,5,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 174, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,10,6,5,1,6,6,6,10],
[5,0,10,11,5,6,0,6,1,10],
[1,1,0,1,5,1,1,1,1,5],
[5,0,10,0,5,1,0,6,1,10],
[6,6,6,6,0,6,6,1,1,10],
[10,5,10,10,5,0,5,5,5,10],
[5,11,10,11,5,6,0,6,1,10],
[5,5,10,5,10,6,5,0,5,10],
[5,10,10,10,10,6,10,6,0,10],
[1,1,6,1,1,1,1,1,1,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 175, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,8,8,8,9,7,7,9,5],
[6,0,8,7,7,8,4,8,9,9],
[3,3,0,4,7,6,2,2,6,6],
[3,4,7,0,3,4,3,4,5,5],
[3,4,4,8,0,6,3,2,8,5],
[2,3,5,7,5,0,1,4,5,5],
[4,7,9,8,8,10,0,9,7,7],
[4,3,9,7,9,7,2,0,8,7],
[2,2,5,6,3,6,4,3,0,2],
[6,2,5,6,6,6,4,4,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 176, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,3,7,4,4,7,11,3,0],
[4,0,4,7,4,4,7,7,7,0],
[8,7,0,7,4,4,7,11,7,0],
[4,4,4,0,0,4,3,11,3,4],
[7,7,7,11,0,11,7,11,3,7],
[7,7,7,7,0,0,3,7,3,4],
[4,4,4,8,4,8,0,11,3,4],
[0,4,0,0,0,4,0,0,0,0],
[8,4,4,8,8,8,8,11,0,4],
[11,11,11,7,4,7,7,11,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 177, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,7,7,1,5,7,6,7,7],
[5,0,5,9,3,7,5,9,7,9],
[4,6,0,9,3,5,5,7,4,9],
[4,2,2,0,4,4,4,6,4,8],
[10,8,8,7,0,5,7,7,6,7],
[6,4,6,7,6,0,5,5,3,9],
[4,6,6,7,4,6,0,6,6,7],
[5,2,4,5,4,6,5,0,2,7],
[4,4,7,7,5,8,5,9,0,7],
[4,2,2,3,4,2,4,4,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 178, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,4,9,2,9,7,7,4,4],
[7,0,5,7,9,5,7,9,9,6],
[7,6,0,9,7,11,5,9,6,6],
[2,4,2,0,2,7,5,9,6,6],
[9,2,4,9,0,7,5,7,6,6],
[2,6,0,4,4,0,5,9,6,4],
[4,4,6,6,6,6,0,7,6,6],
[4,2,2,2,4,2,4,0,8,6],
[7,2,5,5,5,5,5,3,0,6],
[7,5,5,5,5,7,5,5,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 179, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,8,8,5,11,8,7,11,5],
[0,0,8,4,5,11,7,7,10,5],
[3,3,0,7,8,7,7,7,7,8],
[3,7,4,0,5,11,7,3,10,5],
[6,6,3,6,0,10,10,6,10,11],
[0,0,4,0,1,0,7,0,4,1],
[3,4,4,4,1,4,0,0,3,1],
[4,4,4,8,5,11,11,0,8,5],
[0,1,4,1,1,7,8,3,0,1],
[6,6,3,6,0,10,10,6,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 180, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,7,6,3,8,4,7,7,5],
[4,0,5,6,6,8,5,5,8,6],
[4,6,0,6,5,7,4,7,7,7],
[5,5,5,0,6,8,5,6,7,5],
[8,5,6,5,0,7,7,7,6,8],
[3,3,4,3,4,0,2,5,6,3],
[7,6,7,6,4,9,0,7,6,8],
[4,6,4,5,4,6,4,0,7,4],
[4,3,4,4,5,5,5,4,0,4],
[6,5,4,6,3,8,3,7,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 181, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,6,5,1,0,6,1,1,1],
[6,0,6,1,1,1,6,1,1,1],
[5,5,0,5,0,0,10,0,1,1],
[6,10,6,0,6,6,11,6,1,6],
[10,10,11,5,0,5,11,11,1,11],
[11,10,11,5,6,0,11,6,6,11],
[5,5,1,0,0,0,0,0,1,1],
[10,10,11,5,0,5,11,0,1,6],
[10,10,10,10,10,5,10,10,0,11],
[10,10,10,5,0,0,10,5,0,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 182, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,7,4,7,7,6,8,6,4],
[6,0,6,6,5,7,4,6,6,4],
[4,5,0,5,4,8,5,4,5,5],
[7,5,6,0,7,7,6,5,5,3],
[4,6,7,4,0,7,6,8,7,5],
[4,4,3,4,4,0,4,4,3,5],
[5,7,6,5,5,7,0,6,7,6],
[3,5,7,6,3,7,5,0,4,4],
[5,5,6,6,4,8,4,7,0,5],
[7,7,6,8,6,6,5,7,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 183, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,4,4,4,6,4,4,4,4],
[5,0,4,9,9,4,9,9,4,9],
[7,7,0,7,11,2,7,7,11,7],
[7,2,4,0,6,2,4,6,6,6],
[7,2,0,5,0,2,5,0,4,0],
[5,7,9,9,9,0,9,9,9,9],
[7,2,4,7,6,2,0,6,6,6],
[7,2,4,5,11,2,5,0,4,4],
[7,7,0,5,7,2,5,7,0,5],
[7,2,4,5,11,2,5,7,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 184, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,5,5,8,5,6,7,7,6],
[4,0,5,5,7,7,6,6,4,4],
[6,6,0,5,7,5,7,5,5,6],
[6,6,6,0,8,7,6,7,8,4],
[3,4,4,3,0,5,6,6,6,3],
[6,4,6,4,6,0,5,6,4,3],
[5,5,4,5,5,6,0,6,5,3],
[4,5,6,4,5,5,5,0,6,3],
[4,7,6,3,5,7,6,5,0,4],
[5,7,5,7,8,8,8,8,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 185, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,6,7,4,6,5,9,3,4],
[6,0,6,6,6,8,6,9,7,5],
[5,5,0,6,5,5,4,6,5,5],
[4,5,5,0,5,5,5,6,5,5],
[7,5,6,6,0,6,5,9,4,5],
[5,3,6,6,5,0,7,10,5,4],
[6,5,7,6,6,4,0,8,6,7],
[2,2,5,5,2,1,3,0,2,2],
[8,4,6,6,7,6,5,9,0,5],
[7,6,6,6,6,7,4,9,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 186, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,5,5,6,5,5,4,8,8],
[5,0,3,4,5,5,3,4,6,5],
[6,8,0,6,7,7,7,5,7,8],
[6,7,5,0,8,8,6,5,9,5],
[5,6,4,3,0,3,1,3,4,5],
[6,6,4,3,8,0,4,5,8,5],
[6,8,4,5,10,7,0,6,9,7],
[7,7,6,6,8,6,5,0,8,6],
[3,5,4,2,7,3,2,3,0,4],
[3,6,3,6,6,6,4,5,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 187, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,8,5,11,4,5,6,7,5],
[5,0,9,6,8,4,6,9,7,4],
[3,2,0,4,4,1,3,4,4,2],
[6,5,7,0,8,5,9,8,6,7],
[0,3,7,3,0,3,4,3,3,3],
[7,7,10,6,8,0,5,7,9,6],
[6,5,8,2,7,6,0,9,8,5],
[5,2,7,3,8,4,2,0,6,2],
[4,4,7,5,8,2,3,5,0,4],
[6,7,9,4,8,5,6,9,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 188, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,4,4,6,4,5,8,2,4],
[5,0,5,3,4,4,6,6,3,5],
[7,6,0,5,6,6,7,8,6,6],
[7,8,6,0,4,6,7,9,5,7],
[5,7,5,7,0,5,6,8,3,6],
[7,7,5,5,6,0,6,9,5,6],
[6,5,4,4,5,5,0,5,3,6],
[3,5,3,2,3,2,6,0,2,3],
[9,8,5,6,8,6,8,9,0,7],
[7,6,5,4,5,5,5,8,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 189, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,7,4,4,4,8,3,2,5],
[6,0,7,6,7,7,6,6,5,8],
[4,4,0,6,3,3,9,3,3,6],
[7,5,5,0,5,3,7,2,2,5],
[7,4,8,6,0,3,8,3,3,10],
[7,4,8,8,8,0,7,5,6,10],
[3,5,2,4,3,4,0,4,3,4],
[8,5,8,9,8,6,7,0,8,8],
[9,6,8,9,8,5,8,3,0,8],
[6,3,5,6,1,1,7,3,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 190, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,5,5,5,7,8,7,9,5],
[4,0,7,6,8,8,5,7,9,6],
[6,4,0,6,4,3,6,8,9,3],
[6,5,5,0,6,8,7,7,9,6],
[6,3,7,5,0,4,7,7,9,4],
[4,3,8,3,7,0,7,9,7,6],
[3,6,5,4,4,4,0,7,7,5],
[4,4,3,4,4,2,4,0,6,4],
[2,2,2,2,2,4,4,5,0,1],
[6,5,8,5,7,5,6,7,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 191, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,4,6,4,6,4,11,8,3],
[5,0,7,0,7,5,5,5,7,7],
[7,4,0,4,5,9,4,7,6,4],
[5,11,7,0,7,5,5,7,7,7],
[7,4,6,4,0,9,7,7,9,9],
[5,6,2,6,2,0,2,9,2,3],
[7,6,7,6,4,9,0,11,8,3],
[0,6,4,4,4,2,0,0,2,2],
[3,4,5,4,2,9,3,9,0,4],
[8,4,7,4,2,8,8,9,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 192, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,5,7,4,8,6,7,9,7],
[2,0,2,7,5,6,8,8,8,8],
[6,9,0,6,6,5,6,6,6,6],
[4,4,5,0,1,9,7,6,10,5],
[7,6,5,10,0,9,11,10,11,7],
[3,5,6,2,2,0,5,2,5,3],
[5,3,5,4,0,6,0,5,4,1],
[4,3,5,5,1,9,6,0,8,4],
[2,3,5,1,0,6,7,3,0,1],
[4,3,5,6,4,8,10,7,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 193, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,7,8,5,11,4,6,8,6],
[3,0,6,6,1,3,3,2,3,1],
[4,5,0,7,1,5,2,2,4,4],
[3,5,4,0,1,5,1,2,1,4],
[6,10,10,10,0,7,4,2,8,5],
[0,8,6,6,4,0,1,2,6,1],
[7,8,9,10,7,10,0,5,7,5],
[5,9,9,9,9,9,6,0,7,4],
[3,8,7,10,3,5,4,4,0,4],
[5,10,7,7,6,10,6,7,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 194, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,8,5,7,6,7,6,7,4],
[4,0,6,6,6,4,7,5,8,7],
[3,5,0,4,4,3,6,2,7,5],
[6,5,7,0,6,8,7,7,7,7],
[4,5,7,5,0,7,4,6,5,6],
[5,7,8,3,4,0,6,5,8,5],
[4,4,5,4,7,5,0,4,5,4],
[5,6,9,4,5,6,7,0,6,7],
[4,3,4,4,6,3,6,5,0,5],
[7,4,6,4,5,6,7,4,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 195, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,6,6,5,6,7,9,4,3],
[5,0,6,6,4,5,7,6,6,5],
[5,5,0,6,3,6,6,7,5,6],
[5,5,5,0,3,5,5,7,5,6],
[6,7,8,8,0,9,7,9,8,5],
[5,6,5,6,2,0,7,9,6,4],
[4,4,5,6,4,4,0,5,3,3],
[2,5,4,4,2,2,6,0,4,4],
[7,5,6,6,3,5,8,7,0,3],
[8,6,5,5,6,7,8,7,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 196, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,3,5,3,6,3,4,5,5],
[6,0,5,3,7,4,3,4,5,5],
[8,6,0,6,3,7,5,4,7,7],
[6,8,5,0,7,6,4,5,6,4],
[8,4,8,4,0,6,3,8,8,7],
[5,7,4,5,5,0,2,2,5,5],
[8,8,6,7,8,9,0,7,9,5],
[7,7,7,6,3,9,4,0,5,5],
[6,6,4,5,3,6,2,6,0,4],
[6,6,4,7,4,6,6,6,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 197, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,8,5,6,5,6,6,6,7],
[3,0,3,0,4,1,6,1,0,6],
[3,8,0,2,4,2,4,3,3,6],
[6,11,9,0,11,9,8,5,9,10],
[5,7,7,0,0,3,5,1,4,5],
[6,10,9,2,8,0,7,3,2,9],
[5,5,7,3,6,4,0,1,4,8],
[5,10,8,6,10,8,10,0,5,10],
[5,11,8,2,7,9,7,6,0,9],
[4,5,5,1,6,2,3,1,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 198, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,10,8,6,3,8,8,6,8],
[6,0,9,7,5,7,7,7,8,11],
[1,2,0,2,2,2,2,6,2,5],
[3,4,9,0,8,5,10,7,8,7],
[5,6,9,3,0,7,7,7,7,7],
[8,4,9,6,4,0,7,7,5,7],
[3,4,9,1,4,4,0,7,5,7],
[3,4,5,4,4,4,4,0,4,8],
[5,3,9,3,4,6,6,7,0,4],
[3,0,6,4,4,4,4,3,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 199, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,6,5,6,7,6,9,5,8],
[4,0,5,5,7,7,6,7,6,5],
[5,6,0,7,7,7,6,8,7,6],
[6,6,4,0,4,7,7,7,5,8],
[5,4,4,7,0,6,7,7,3,6],
[4,4,4,4,5,0,6,5,3,4],
[5,5,5,4,4,5,0,7,4,5],
[2,4,3,4,4,6,4,0,3,5],
[6,5,4,6,8,8,7,8,0,7],
[3,6,5,3,5,7,6,6,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 11, 200, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebb/mebb_10_11.csv", index=False, header=False)