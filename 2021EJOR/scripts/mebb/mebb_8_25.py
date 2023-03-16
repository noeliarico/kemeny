
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,15,10,7,5,5,19,13],
[10,0,4,4,7,5,20,4],
[15,21,0,13,11,11,24,9],
[18,21,12,0,16,16,25,15],
[20,18,14,9,0,19,18,14],
[20,20,14,9,6,0,24,8],
[6,5,1,0,7,1,0,3],
[12,21,16,10,11,17,22,0]])



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
result = np.append(np.array([8, 25, 1, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,14,14,17,15,11,14],
[11,0,13,14,12,8,9,9],
[11,12,0,13,12,11,11,15],
[11,11,12,0,12,8,11,13],
[8,13,13,13,0,12,13,14],
[10,17,14,17,13,0,11,14],
[14,16,14,14,12,14,0,19],
[11,16,10,12,11,11,6,0]])



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
result = np.append(np.array([8, 25, 2, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,8,15,14,15,10,20],
[12,0,16,19,12,14,15,18],
[17,9,0,17,17,21,16,21],
[10,6,8,0,6,10,7,8],
[11,13,8,19,0,13,17,18],
[10,11,4,15,12,0,14,17],
[15,10,9,18,8,11,0,20],
[5,7,4,17,7,8,5,0]])



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
result = np.append(np.array([8, 25, 3, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,6,12,12,13,12,13],
[19,0,1,19,19,7,19,19],
[19,24,0,25,25,7,18,19],
[13,6,0,0,13,7,12,7],
[13,6,0,12,0,7,12,13],
[12,18,18,18,18,0,18,19],
[13,6,7,13,13,7,0,13],
[12,6,6,18,12,6,12,0]])



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
result = np.append(np.array([8, 25, 4, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,10,10,15,8,14,8],
[13,0,10,10,14,11,11,13],
[15,15,0,13,17,13,11,15],
[15,15,12,0,15,13,13,16],
[10,11,8,10,0,12,11,8],
[17,14,12,12,13,0,13,11],
[11,14,14,12,14,12,0,13],
[17,12,10,9,17,14,12,0]])



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
result = np.append(np.array([8, 25, 5, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,10,6,11,9,13,15],
[14,0,7,10,13,10,9,13],
[15,18,0,12,17,13,13,14],
[19,15,13,0,19,9,16,17],
[14,12,8,6,0,8,8,16],
[16,15,12,16,17,0,13,15],
[12,16,12,9,17,12,0,15],
[10,12,11,8,9,10,10,0]])



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
result = np.append(np.array([8, 25, 6, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,10,15,14,7,12,17],
[16,0,14,17,16,10,17,16],
[15,11,0,17,16,13,17,18],
[10,8,8,0,9,6,9,12],
[11,9,9,16,0,7,12,17],
[18,15,12,19,18,0,14,18],
[13,8,8,16,13,11,0,12],
[8,9,7,13,8,7,13,0]])



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
result = np.append(np.array([8, 25, 7, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,10,14,16,15,7,14],
[7,0,8,10,11,17,4,11],
[15,17,0,10,13,18,13,15],
[11,15,15,0,17,20,11,12],
[9,14,12,8,0,18,9,13],
[10,8,7,5,7,0,5,8],
[18,21,12,14,16,20,0,17],
[11,14,10,13,12,17,8,0]])



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
result = np.append(np.array([8, 25, 8, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,13,17,20,6,7,11],
[11,0,13,9,20,5,6,8],
[12,12,0,17,23,14,15,14],
[8,16,8,0,11,3,5,5],
[5,5,2,14,0,0,2,2],
[19,20,11,22,25,0,12,16],
[18,19,10,20,23,13,0,14],
[14,17,11,20,23,9,11,0]])



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
result = np.append(np.array([8, 25, 9, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,6,10,12,16,9,9],
[14,0,12,17,13,17,14,17],
[19,13,0,14,16,18,12,14],
[15,8,11,0,8,19,14,14],
[13,12,9,17,0,17,14,16],
[9,8,7,6,8,0,9,9],
[16,11,13,11,11,16,0,14],
[16,8,11,11,9,16,11,0]])



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
result = np.append(np.array([8, 25, 10, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,18,12,20,17,18,19],
[10,0,8,9,14,10,13,15],
[7,17,0,13,14,12,15,16],
[13,16,12,0,15,13,14,15],
[5,11,11,10,0,11,9,13],
[8,15,13,12,14,0,14,16],
[7,12,10,11,16,11,0,15],
[6,10,9,10,12,9,10,0]])



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
result = np.append(np.array([8, 25, 11, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,20,15,18,13,12,13],
[14,0,17,19,10,7,18,20],
[5,8,0,4,6,3,6,10],
[10,6,21,0,10,7,13,13],
[7,15,19,15,0,10,16,19],
[12,18,22,18,15,0,17,23],
[13,7,19,12,9,8,0,11],
[12,5,15,12,6,2,14,0]])



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
result = np.append(np.array([8, 25, 12, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,9,15,13,10,13,9],
[11,0,8,13,10,9,12,7],
[16,17,0,12,17,13,18,14],
[10,12,13,0,14,11,11,12],
[12,15,8,11,0,11,9,12],
[15,16,12,14,14,0,13,14],
[12,13,7,14,16,12,0,12],
[16,18,11,13,13,11,13,0]])



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
result = np.append(np.array([8, 25, 13, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,13,16,14,8,11,18],
[11,0,6,11,11,6,11,17],
[12,19,0,15,12,15,12,16],
[9,14,10,0,9,8,11,14],
[11,14,13,16,0,11,12,15],
[17,19,10,17,14,0,13,19],
[14,14,13,14,13,12,0,22],
[7,8,9,11,10,6,3,0]])



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
result = np.append(np.array([8, 25, 14, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,9,8,16,12,13,12],
[9,0,6,10,17,9,12,8],
[16,19,0,15,19,20,12,10],
[17,15,10,0,19,14,11,12],
[9,8,6,6,0,6,4,6],
[13,16,5,11,19,0,10,10],
[12,13,13,14,21,15,0,14],
[13,17,15,13,19,15,11,0]])



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
result = np.append(np.array([8, 25, 15, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,13,0,0,9,0,0],
[25,0,25,12,21,25,4,9],
[12,0,0,12,12,9,0,0],
[25,13,13,0,9,13,13,13],
[25,4,13,16,0,13,4,4],
[16,0,16,12,12,0,4,0],
[25,21,25,12,21,21,0,9],
[25,16,25,12,21,25,16,0]])



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
result = np.append(np.array([8, 25, 16, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,12,11,16,13,10,10],
[12,0,14,13,11,15,11,10],
[13,11,0,12,12,15,10,11],
[14,12,13,0,12,13,14,11],
[9,14,13,13,0,15,13,13],
[12,10,10,12,10,0,11,9],
[15,14,15,11,12,14,0,16],
[15,15,14,14,12,16,9,0]])



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
result = np.append(np.array([8, 25, 17, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,9,9,15,12,13,12],
[17,0,15,12,16,14,16,11],
[16,10,0,10,12,10,15,14],
[16,13,15,0,17,11,11,14],
[10,9,13,8,0,8,13,15],
[13,11,15,14,17,0,13,12],
[12,9,10,14,12,12,0,11],
[13,14,11,11,10,13,14,0]])



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
result = np.append(np.array([8, 25, 18, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,11,14,12,7,15,11],
[16,0,13,14,11,15,14,13],
[14,12,0,14,13,9,14,6],
[11,11,11,0,9,8,11,11],
[13,14,12,16,0,17,15,15],
[18,10,16,17,8,0,18,12],
[10,11,11,14,10,7,0,9],
[14,12,19,14,10,13,16,0]])



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
result = np.append(np.array([8, 25, 19, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,14,11,13,14,13,9],
[13,0,12,12,13,13,10,12],
[11,13,0,15,13,14,13,13],
[14,13,10,0,15,15,11,12],
[12,12,12,10,0,14,12,12],
[11,12,11,10,11,0,13,14],
[12,15,12,14,13,12,0,9],
[16,13,12,13,13,11,16,0]])



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
result = np.append(np.array([8, 25, 20, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,19,14,16,10,16,15],
[11,0,21,17,9,9,12,10],
[6,4,0,13,9,7,8,9],
[11,8,12,0,11,5,10,11],
[9,16,16,14,0,11,11,11],
[15,16,18,20,14,0,12,14],
[9,13,17,15,14,13,0,12],
[10,15,16,14,14,11,13,0]])



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
result = np.append(np.array([8, 25, 21, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,13,17,12,9,11,11],
[13,0,11,14,7,7,9,14],
[12,14,0,14,12,11,10,13],
[8,11,11,0,11,6,9,8],
[13,18,13,14,0,8,15,14],
[16,18,14,19,17,0,11,15],
[14,16,15,16,10,14,0,16],
[14,11,12,17,11,10,9,0]])



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
result = np.append(np.array([8, 25, 22, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,9,15,11,10,14],
[15,0,13,16,17,13,12,16],
[15,12,0,14,20,13,13,15],
[16,9,11,0,17,7,9,14],
[10,8,5,8,0,8,6,6],
[14,12,12,18,17,0,13,19],
[15,13,12,16,19,12,0,17],
[11,9,10,11,19,6,8,0]])



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
result = np.append(np.array([8, 25, 23, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,11,10,10,16,14,12],
[15,0,10,9,11,18,12,15],
[14,15,0,11,14,17,14,16],
[15,16,14,0,12,19,17,19],
[15,14,11,13,0,18,15,16],
[9,7,8,6,7,0,9,8],
[11,13,11,8,10,16,0,13],
[13,10,9,6,9,17,12,0]])



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
result = np.append(np.array([8, 25, 24, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,7,13,10,16,12,12],
[7,0,5,11,6,12,8,8],
[18,20,0,17,13,19,15,12],
[12,14,8,0,10,14,13,13],
[15,19,12,15,0,18,15,13],
[9,13,6,11,7,0,7,8],
[13,17,10,12,10,18,0,8],
[13,17,13,12,12,17,17,0]])



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
result = np.append(np.array([8, 25, 25, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,12,9,12,12,18,15],
[12,0,14,16,16,16,20,20],
[13,11,0,12,16,16,17,20],
[16,9,13,0,11,17,15,16],
[13,9,9,14,0,14,10,12],
[13,9,9,8,11,0,10,13],
[7,5,8,10,15,15,0,16],
[10,5,5,9,13,12,9,0]])



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
result = np.append(np.array([8, 25, 26, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,10,20,18,16,18,13],
[4,0,6,7,12,16,16,9],
[15,19,0,12,17,19,14,10],
[5,18,13,0,16,14,11,9],
[7,13,8,9,0,9,6,7],
[9,9,6,11,16,0,8,5],
[7,9,11,14,19,17,0,14],
[12,16,15,16,18,20,11,0]])



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
result = np.append(np.array([8, 25, 27, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,13,16,12,13,15,15],
[8,0,12,10,10,11,13,11],
[12,13,0,10,14,10,11,12],
[9,15,15,0,12,8,12,13],
[13,15,11,13,0,12,16,12],
[12,14,15,17,13,0,13,13],
[10,12,14,13,9,12,0,12],
[10,14,13,12,13,12,13,0]])



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
result = np.append(np.array([8, 25, 28, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,10,11,17,12,10,13],
[8,0,10,7,15,10,9,9],
[15,15,0,9,13,11,14,11],
[14,18,16,0,16,12,13,12],
[8,10,12,9,0,10,9,8],
[13,15,14,13,15,0,11,12],
[15,16,11,12,16,14,0,8],
[12,16,14,13,17,13,17,0]])



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
result = np.append(np.array([8, 25, 29, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,11,14,16,13,15,14],
[11,0,12,14,10,12,10,14],
[14,13,0,9,11,14,13,15],
[11,11,16,0,10,11,10,16],
[9,15,14,15,0,12,15,17],
[12,13,11,14,13,0,12,15],
[10,15,12,15,10,13,0,15],
[11,11,10,9,8,10,10,0]])



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
result = np.append(np.array([8, 25, 30, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,16,13,11,11,5],
[15,0,9,13,15,11,13,9],
[15,16,0,16,16,12,12,11],
[9,12,9,0,8,13,11,11],
[12,10,9,17,0,10,10,9],
[14,14,13,12,15,0,13,14],
[14,12,13,14,15,12,0,8],
[20,16,14,14,16,11,17,0]])



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
result = np.append(np.array([8, 25, 31, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,16,11,15,15,12,11],
[13,0,13,15,11,14,9,13],
[9,12,0,12,9,11,13,13],
[14,10,13,0,14,13,12,13],
[10,14,16,11,0,14,11,14],
[10,11,14,12,11,0,11,11],
[13,16,12,13,14,14,0,15],
[14,12,12,12,11,14,10,0]])



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
result = np.append(np.array([8, 25, 32, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,13,17,11,8,14],
[14,0,10,15,16,15,13,13],
[14,15,0,13,17,13,10,17],
[12,10,12,0,14,9,10,14],
[8,9,8,11,0,8,8,11],
[14,10,12,16,17,0,13,15],
[17,12,15,15,17,12,0,18],
[11,12,8,11,14,10,7,0]])



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
result = np.append(np.array([8, 25, 33, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,14,16,13,14,12,14],
[11,0,12,15,14,14,9,12],
[11,13,0,17,12,14,10,13],
[9,10,8,0,10,13,8,12],
[12,11,13,15,0,12,13,14],
[11,11,11,12,13,0,10,13],
[13,16,15,17,12,15,0,16],
[11,13,12,13,11,12,9,0]])



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
result = np.append(np.array([8, 25, 34, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,10,12,11,13,7],
[14,0,12,5,12,15,17,13],
[14,13,0,12,13,17,17,11],
[15,20,13,0,14,14,18,11],
[13,13,12,11,0,11,15,9],
[14,10,8,11,14,0,16,11],
[12,8,8,7,10,9,0,8],
[18,12,14,14,16,14,17,0]])



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
result = np.append(np.array([8, 25, 35, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,9,8,12,13,18,16],
[8,0,11,10,9,11,6,11],
[16,14,0,10,15,10,14,20],
[17,15,15,0,12,16,18,19],
[13,16,10,13,0,14,13,17],
[12,14,15,9,11,0,13,16],
[7,19,11,7,12,12,0,14],
[9,14,5,6,8,9,11,0]])



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
result = np.append(np.array([8, 25, 36, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,13,12,15,10,16,8],
[16,0,12,14,13,11,15,10],
[12,13,0,15,18,13,16,12],
[13,11,10,0,15,10,12,8],
[10,12,7,10,0,8,12,6],
[15,14,12,15,17,0,15,13],
[9,10,9,13,13,10,0,8],
[17,15,13,17,19,12,17,0]])



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
result = np.append(np.array([8, 25, 37, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,12,16,11,21,16],
[12,0,5,9,7,10,13,12],
[12,20,0,14,13,9,16,14],
[13,16,11,0,16,14,21,16],
[9,18,12,9,0,8,21,14],
[14,15,16,11,17,0,24,14],
[4,12,9,4,4,1,0,14],
[9,13,11,9,11,11,11,0]])



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
result = np.append(np.array([8, 25, 38, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,12,15,13,13,13,15],
[10,0,14,14,9,10,9,12],
[13,11,0,14,11,10,10,13],
[10,11,11,0,6,14,11,15],
[12,16,14,19,0,15,15,19],
[12,15,15,11,10,0,12,16],
[12,16,15,14,10,13,0,13],
[10,13,12,10,6,9,12,0]])



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
result = np.append(np.array([8, 25, 39, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,14,13,15,17,11,11],
[13,0,14,9,13,11,15,10],
[11,11,0,11,11,9,12,13],
[12,16,14,0,11,12,13,11],
[10,12,14,14,0,12,13,6],
[8,14,16,13,13,0,7,18],
[14,10,13,12,12,18,0,12],
[14,15,12,14,19,7,13,0]])



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
result = np.append(np.array([8, 25, 40, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,18,17,9,13,17,16],
[10,0,14,11,12,9,15,13],
[7,11,0,10,10,9,15,12],
[8,14,15,0,13,8,17,13],
[16,13,15,12,0,9,14,13],
[12,16,16,17,16,0,18,17],
[8,10,10,8,11,7,0,8],
[9,12,13,12,12,8,17,0]])



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
result = np.append(np.array([8, 25, 41, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,6,12,11,10,16,9],
[17,0,9,15,13,12,12,13],
[19,16,0,17,16,13,16,11],
[13,10,8,0,8,17,14,8],
[14,12,9,17,0,16,18,12],
[15,13,12,8,9,0,12,9],
[9,13,9,11,7,13,0,7],
[16,12,14,17,13,16,18,0]])



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
result = np.append(np.array([8, 25, 42, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,11,10,13,15,14,13],
[15,0,14,12,13,16,10,12],
[14,11,0,13,14,14,10,12],
[15,13,12,0,12,13,14,12],
[12,12,11,13,0,14,14,10],
[10,9,11,12,11,0,12,9],
[11,15,15,11,11,13,0,11],
[12,13,13,13,15,16,14,0]])



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
result = np.append(np.array([8, 25, 43, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,16,10,18,15,11,12],
[7,0,7,7,11,12,7,10],
[9,18,0,7,11,12,7,12],
[15,18,18,0,16,12,14,12],
[7,14,14,9,0,8,16,12],
[10,13,13,13,17,0,14,11],
[14,18,18,11,9,11,0,13],
[13,15,13,13,13,14,12,0]])



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
result = np.append(np.array([8, 25, 44, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,13,14,15,13,11,16],
[9,0,12,14,10,7,13,11],
[12,13,0,10,12,11,10,12],
[11,11,15,0,12,10,14,13],
[10,15,13,13,0,9,15,15],
[12,18,14,15,16,0,16,17],
[14,12,15,11,10,9,0,13],
[9,14,13,12,10,8,12,0]])



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
result = np.append(np.array([8, 25, 45, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,14,10,14,13,8,11],
[15,0,17,15,19,16,14,12],
[11,8,0,5,14,14,7,13],
[15,10,20,0,18,15,11,13],
[11,6,11,7,0,12,8,12],
[12,9,11,10,13,0,7,12],
[17,11,18,14,17,18,0,14],
[14,13,12,12,13,13,11,0]])



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
result = np.append(np.array([8, 25, 46, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,14,15,14,16,14,15],
[15,0,13,12,10,13,15,14],
[11,12,0,16,14,16,17,14],
[10,13,9,0,10,17,13,15],
[11,15,11,15,0,16,11,16],
[9,12,9,8,9,0,13,13],
[11,10,8,12,14,12,0,11],
[10,11,11,10,9,12,14,0]])



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
result = np.append(np.array([8, 25, 47, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,10,7,10,8,13,12],
[14,0,10,11,8,14,15,15],
[15,15,0,8,11,17,16,14],
[18,14,17,0,15,10,12,14],
[15,17,14,10,0,15,20,16],
[17,11,8,15,10,0,16,12],
[12,10,9,13,5,9,0,10],
[13,10,11,11,9,13,15,0]])



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
result = np.append(np.array([8, 25, 48, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,14,11,16,14,14,20],
[14,0,9,11,17,11,13,15],
[11,16,0,14,15,15,19,15],
[14,14,11,0,15,12,10,14],
[9,8,10,10,0,9,8,11],
[11,14,10,13,16,0,16,15],
[11,12,6,15,17,9,0,13],
[5,10,10,11,14,10,12,0]])



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
result = np.append(np.array([8, 25, 49, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,15,10,13,11,11,21],
[15,0,8,14,12,10,13,20],
[10,17,0,11,13,15,10,19],
[15,11,14,0,11,14,12,18],
[12,13,12,14,0,17,12,20],
[14,15,10,11,8,0,13,17],
[14,12,15,13,13,12,0,15],
[4,5,6,7,5,8,10,0]])



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
result = np.append(np.array([8, 25, 50, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,13,12,11,12,17,10],
[10,0,9,15,10,15,15,9],
[12,16,0,15,13,13,15,14],
[13,10,10,0,6,11,14,12],
[14,15,12,19,0,14,17,18],
[13,10,12,14,11,0,16,12],
[8,10,10,11,8,9,0,10],
[15,16,11,13,7,13,15,0]])



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
result = np.append(np.array([8, 25, 51, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,16,9,25,16,16,16],
[0,0,7,9,25,16,9,9],
[9,18,0,18,18,18,18,18],
[16,16,7,0,16,7,7,7],
[0,0,7,9,0,0,0,0],
[9,9,7,18,25,0,9,9],
[9,16,7,18,25,16,0,16],
[9,16,7,18,25,16,9,0]])



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
result = np.append(np.array([8, 25, 52, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,10,10,19,10,0,19],
[9,0,19,10,19,10,9,19],
[15,6,0,0,9,0,9,9],
[15,15,25,0,19,19,9,19],
[6,6,16,6,0,0,6,16],
[15,15,25,6,25,0,15,25],
[25,16,16,16,19,10,0,19],
[6,6,16,6,9,0,6,0]])



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
result = np.append(np.array([8, 25, 53, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,15,13,10,12,12,15],
[15,0,15,9,10,12,13,16],
[10,10,0,11,14,13,14,16],
[12,16,14,0,10,15,11,17],
[15,15,11,15,0,9,11,14],
[13,13,12,10,16,0,13,19],
[13,12,11,14,14,12,0,16],
[10,9,9,8,11,6,9,0]])



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
result = np.append(np.array([8, 25, 54, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,13,9,12,13,9,11],
[13,0,13,8,12,10,10,13],
[12,12,0,9,11,9,12,15],
[16,17,16,0,15,12,13,12],
[13,13,14,10,0,13,14,15],
[12,15,16,13,12,0,15,17],
[16,15,13,12,11,10,0,16],
[14,12,10,13,10,8,9,0]])



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
result = np.append(np.array([8, 25, 55, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,16,2,11,9,5,9],
[9,0,7,7,7,7,5,13],
[9,18,0,8,16,17,6,12],
[23,18,17,0,15,9,6,10],
[14,18,9,10,0,14,13,16],
[16,18,8,16,11,0,5,17],
[20,20,19,19,12,20,0,14],
[16,12,13,15,9,8,11,0]])



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
result = np.append(np.array([8, 25, 56, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,12,15,18,18,16,16],
[11,0,16,10,20,19,18,14],
[13,9,0,12,16,15,9,9],
[10,15,13,0,17,14,12,7],
[7,5,9,8,0,10,3,7],
[7,6,10,11,15,0,8,3],
[9,7,16,13,22,17,0,10],
[9,11,16,18,18,22,15,0]])



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
result = np.append(np.array([8, 25, 57, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,16,11,15,16,14,11],
[13,0,15,14,15,13,10,9],
[9,10,0,6,12,11,8,8],
[14,11,19,0,17,14,14,16],
[10,10,13,8,0,13,9,13],
[9,12,14,11,12,0,13,13],
[11,15,17,11,16,12,0,11],
[14,16,17,9,12,12,14,0]])



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
result = np.append(np.array([8, 25, 58, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,12,10,12,10,10,9],
[14,0,9,11,13,12,12,8],
[13,16,0,11,19,15,15,10],
[15,14,14,0,14,13,12,13],
[13,12,6,11,0,12,13,8],
[15,13,10,12,13,0,11,9],
[15,13,10,13,12,14,0,9],
[16,17,15,12,17,16,16,0]])



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
result = np.append(np.array([8, 25, 59, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,14,18,15,12,14,14],
[13,0,11,13,11,12,13,10],
[11,14,0,15,14,11,13,15],
[7,12,10,0,12,10,12,11],
[10,14,11,13,0,10,10,10],
[13,13,14,15,15,0,13,12],
[11,12,12,13,15,12,0,13],
[11,15,10,14,15,13,12,0]])



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
result = np.append(np.array([8, 25, 60, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,19,14,12,16,11,13],
[6,0,11,5,3,10,9,3],
[6,14,0,7,7,10,12,9],
[11,20,18,0,13,18,15,14],
[13,22,18,12,0,14,15,14],
[9,15,15,7,11,0,8,9],
[14,16,13,10,10,17,0,10],
[12,22,16,11,11,16,15,0]])



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
result = np.append(np.array([8, 25, 61, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,7,10,11,9,9,9],
[17,0,15,13,15,19,16,12],
[18,10,0,11,18,11,13,13],
[15,12,14,0,13,13,6,14],
[14,10,7,12,0,11,5,11],
[16,6,14,12,14,0,11,9],
[16,9,12,19,20,14,0,16],
[16,13,12,11,14,16,9,0]])



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
result = np.append(np.array([8, 25, 62, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,14,11,8,14,15,13],
[14,0,17,13,12,15,13,13],
[11,8,0,10,10,10,9,12],
[14,12,15,0,13,10,15,14],
[17,13,15,12,0,13,15,17],
[11,10,15,15,12,0,13,13],
[10,12,16,10,10,12,0,12],
[12,12,13,11,8,12,13,0]])



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
result = np.append(np.array([8, 25, 63, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,12,5,7,7,1,2],
[14,0,19,9,11,14,6,10],
[13,6,0,13,17,6,6,11],
[20,16,12,0,11,12,14,7],
[18,14,8,14,0,10,10,9],
[18,11,19,13,15,0,10,13],
[24,19,19,11,15,15,0,12],
[23,15,14,18,16,12,13,0]])



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
result = np.append(np.array([8, 25, 64, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,13,15,13,19,10,12],
[4,0,10,11,10,15,10,7],
[12,15,0,12,13,19,14,11],
[10,14,13,0,12,15,11,10],
[12,15,12,13,0,14,11,13],
[6,10,6,10,11,0,10,7],
[15,15,11,14,14,15,0,7],
[13,18,14,15,12,18,18,0]])



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
result = np.append(np.array([8, 25, 65, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,11,15,13,11,12,13],
[12,0,10,18,15,8,8,13],
[14,15,0,17,13,12,14,15],
[10,7,8,0,11,9,5,10],
[12,10,12,14,0,10,9,11],
[14,17,13,16,15,0,9,15],
[13,17,11,20,16,16,0,13],
[12,12,10,15,14,10,12,0]])



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
result = np.append(np.array([8, 25, 66, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,4,8,14,10,10,10],
[15,0,15,4,15,21,16,5],
[21,10,0,8,14,12,16,11],
[17,21,17,0,17,17,12,17],
[11,10,11,8,0,6,10,5],
[15,4,13,8,19,0,20,5],
[15,9,9,13,15,5,0,5],
[15,20,14,8,20,20,20,0]])



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
result = np.append(np.array([8, 25, 67, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,11,13,16,15,14,10],
[11,0,14,9,15,16,12,9],
[14,11,0,9,12,13,11,15],
[12,16,16,0,15,15,16,13],
[9,10,13,10,0,11,10,10],
[10,9,12,10,14,0,13,9],
[11,13,14,9,15,12,0,11],
[15,16,10,12,15,16,14,0]])



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
result = np.append(np.array([8, 25, 68, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,14,15,12,14,14,19],
[10,0,7,5,7,4,6,7],
[11,18,0,18,20,17,22,16],
[10,20,7,0,12,9,9,9],
[13,18,5,13,0,11,17,11],
[11,21,8,16,14,0,21,10],
[11,19,3,16,8,4,0,12],
[6,18,9,16,14,15,13,0]])



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
result = np.append(np.array([8, 25, 69, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,14,11,11,7,12,12],
[17,0,13,13,11,11,13,15],
[11,12,0,14,15,12,13,12],
[14,12,11,0,13,13,16,15],
[14,14,10,12,0,11,11,14],
[18,14,13,12,14,0,12,18],
[13,12,12,9,14,13,0,12],
[13,10,13,10,11,7,13,0]])



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
result = np.append(np.array([8, 25, 70, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,23,15,13,15,23,15],
[17,0,25,15,5,15,17,17],
[2,0,0,7,5,15,7,7],
[10,10,18,0,15,20,15,12],
[12,20,20,10,0,10,20,20],
[10,10,10,5,15,0,15,12],
[2,8,18,10,5,10,0,2],
[10,8,18,13,5,13,23,0]])



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
result = np.append(np.array([8, 25, 71, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,15,18,2,17,0,5],
[25,0,23,20,18,23,16,11],
[10,2,0,10,7,7,7,10],
[7,5,15,0,0,5,5,5],
[23,7,18,25,0,22,12,13],
[8,2,18,20,3,0,3,8],
[25,9,18,20,13,22,0,11],
[20,14,15,20,12,17,14,0]])



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
result = np.append(np.array([8, 25, 72, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,9,14,10,17,16,10],
[10,0,9,14,9,13,13,12],
[16,16,0,17,14,19,16,11],
[11,11,8,0,13,16,11,15],
[15,16,11,12,0,18,15,9],
[8,12,6,9,7,0,12,8],
[9,12,9,14,10,13,0,14],
[15,13,14,10,16,17,11,0]])



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
result = np.append(np.array([8, 25, 73, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,18,11,23,14,15,14],
[12,0,17,15,17,14,15,19],
[7,8,0,11,15,11,10,8],
[14,10,14,0,13,16,11,8],
[2,8,10,12,0,10,10,13],
[11,11,14,9,15,0,8,9],
[10,10,15,14,15,17,0,12],
[11,6,17,17,12,16,13,0]])



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
result = np.append(np.array([8, 25, 74, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,11,6,10,19,13],
[14,0,12,13,9,11,18,10],
[14,13,0,14,15,11,19,11],
[14,12,11,0,10,9,19,13],
[19,16,10,15,0,14,18,19],
[15,14,14,16,11,0,19,15],
[6,7,6,6,7,6,0,8],
[12,15,14,12,6,10,17,0]])



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
result = np.append(np.array([8, 25, 75, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,10,5,9,13,9,12],
[17,0,14,10,13,17,15,14],
[15,11,0,10,11,17,14,14],
[20,15,15,0,12,15,16,17],
[16,12,14,13,0,14,14,16],
[12,8,8,10,11,0,12,9],
[16,10,11,9,11,13,0,18],
[13,11,11,8,9,16,7,0]])



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
result = np.append(np.array([8, 25, 76, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,11,13,13,12,17,23],
[13,0,14,16,10,12,18,18],
[14,11,0,15,14,14,11,15],
[12,9,10,0,12,16,16,16],
[12,15,11,13,0,15,14,16],
[13,13,11,9,10,0,17,19],
[8,7,14,9,11,8,0,12],
[2,7,10,9,9,6,13,0]])



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
result = np.append(np.array([8, 25, 77, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,13,18,11,16,13,19],
[10,0,11,12,13,14,12,14],
[12,14,0,14,14,16,14,14],
[7,13,11,0,10,15,11,14],
[14,12,11,15,0,13,12,15],
[9,11,9,10,12,0,7,15],
[12,13,11,14,13,18,0,17],
[6,11,11,11,10,10,8,0]])



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
result = np.append(np.array([8, 25, 78, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,11,19,16,17,11,15],
[10,0,11,20,17,18,14,15],
[14,14,0,18,17,17,9,12],
[6,5,7,0,12,10,10,10],
[9,8,8,13,0,14,8,13],
[8,7,8,15,11,0,14,13],
[14,11,16,15,17,11,0,13],
[10,10,13,15,12,12,12,0]])



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
result = np.append(np.array([8, 25, 79, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,11,12,14,11,18,19],
[13,0,16,17,12,14,16,16],
[14,9,0,12,10,10,13,17],
[13,8,13,0,15,7,12,13],
[11,13,15,10,0,12,12,16],
[14,11,15,18,13,0,17,20],
[7,9,12,13,13,8,0,17],
[6,9,8,12,9,5,8,0]])



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
result = np.append(np.array([8, 25, 80, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,11,12,15,14,12,13],
[15,0,13,9,16,15,12,13],
[14,12,0,13,15,12,9,11],
[13,16,12,0,16,15,13,14],
[10,9,10,9,0,11,11,8],
[11,10,13,10,14,0,11,13],
[13,13,16,12,14,14,0,15],
[12,12,14,11,17,12,10,0]])



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
result = np.append(np.array([8, 25, 81, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,12,12,14,15,14,10],
[14,0,12,16,13,14,10,11],
[13,13,0,16,12,17,11,14],
[13,9,9,0,9,14,16,8],
[11,12,13,16,0,15,13,10],
[10,11,8,11,10,0,8,9],
[11,15,14,9,12,17,0,11],
[15,14,11,17,15,16,14,0]])



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
result = np.append(np.array([8, 25, 82, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,13,13,10,17,14,12],
[15,0,11,13,11,17,16,14],
[12,14,0,15,12,15,15,7],
[12,12,10,0,10,15,16,7],
[15,14,13,15,0,15,16,12],
[8,8,10,10,10,0,12,4],
[11,9,10,9,9,13,0,8],
[13,11,18,18,13,21,17,0]])



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
result = np.append(np.array([8, 25, 83, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,12,13,11,15,8,8],
[15,0,14,16,12,17,13,15],
[13,11,0,12,6,12,11,11],
[12,9,13,0,13,14,14,3],
[14,13,19,12,0,13,16,10],
[10,8,13,11,12,0,16,8],
[17,12,14,11,9,9,0,11],
[17,10,14,22,15,17,14,0]])



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
result = np.append(np.array([8, 25, 84, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,16,13,12,11,16,13],
[16,0,18,15,9,8,17,13],
[9,7,0,8,12,8,9,12],
[12,10,17,0,14,13,9,15],
[13,16,13,11,0,15,17,11],
[14,17,17,12,10,0,14,14],
[9,8,16,16,8,11,0,12],
[12,12,13,10,14,11,13,0]])



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
result = np.append(np.array([8, 25, 85, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,16,18,13,13,12,14],
[9,0,19,9,14,13,10,13],
[9,6,0,10,15,9,8,15],
[7,16,15,0,17,10,11,12],
[12,11,10,8,0,10,6,11],
[12,12,16,15,15,0,8,12],
[13,15,17,14,19,17,0,12],
[11,12,10,13,14,13,13,0]])



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
result = np.append(np.array([8, 25, 86, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,14,11,13,10,13,9],
[12,0,17,13,13,13,15,11],
[11,8,0,13,12,7,12,7],
[14,12,12,0,13,12,13,9],
[12,12,13,12,0,10,10,11],
[15,12,18,13,15,0,14,15],
[12,10,13,12,15,11,0,10],
[16,14,18,16,14,10,15,0]])



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
result = np.append(np.array([8, 25, 87, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,21,6,23,17,15,23],
[4,0,13,6,12,6,4,12],
[4,12,0,4,12,4,4,12],
[19,19,21,0,19,11,11,23],
[2,13,13,6,0,6,2,6],
[8,19,21,14,19,0,19,12],
[10,21,21,14,23,6,0,14],
[2,13,13,2,19,13,11,0]])



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
result = np.append(np.array([8, 25, 88, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,9,17,10,9,14,12],
[14,0,14,15,14,13,19,12],
[16,11,0,12,12,12,16,10],
[8,10,13,0,11,10,16,15],
[15,11,13,14,0,14,16,13],
[16,12,13,15,11,0,15,14],
[11,6,9,9,9,10,0,9],
[13,13,15,10,12,11,16,0]])



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
result = np.append(np.array([8, 25, 89, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,13,8,15,9,11,8],
[15,0,13,10,14,11,11,10],
[12,12,0,10,14,12,12,9],
[17,15,15,0,17,11,13,13],
[10,11,11,8,0,8,10,7],
[16,14,13,14,17,0,12,13],
[14,14,13,12,15,13,0,12],
[17,15,16,12,18,12,13,0]])



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
result = np.append(np.array([8, 25, 90, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,9,9,17,12,20,12],
[11,0,9,8,8,11,11,3],
[16,16,0,11,11,16,16,16],
[16,17,14,0,8,8,16,17],
[8,17,14,17,0,17,17,17],
[13,14,9,17,8,0,11,14],
[5,14,9,9,8,14,0,14],
[13,22,9,8,8,11,11,0]])



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
result = np.append(np.array([8, 25, 91, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,15,23,7,16,0,15],
[5,0,12,15,12,4,4,4],
[10,13,0,9,12,5,9,5],
[2,10,16,0,9,1,0,1],
[18,13,13,16,0,13,16,12],
[9,21,20,24,12,0,9,11],
[25,21,16,25,9,16,0,16],
[10,21,20,24,13,14,9,0]])



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
result = np.append(np.array([8, 25, 92, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,11,13,13,9,13,12],
[15,0,10,14,14,14,17,13],
[14,15,0,11,15,12,19,18],
[12,11,14,0,11,8,17,16],
[12,11,10,14,0,6,17,12],
[16,11,13,17,19,0,17,13],
[12,8,6,8,8,8,0,10],
[13,12,7,9,13,12,15,0]])



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
result = np.append(np.array([8, 25, 93, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,9,6,11,9,14,12],
[11,0,8,8,8,10,11,10],
[16,17,0,11,10,13,13,11],
[19,17,14,0,12,13,16,14],
[14,17,15,13,0,11,13,15],
[16,15,12,12,14,0,19,13],
[11,14,12,9,12,6,0,11],
[13,15,14,11,10,12,14,0]])



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
result = np.append(np.array([8, 25, 94, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,15,10,8,19,19,18],
[11,0,20,15,11,22,21,19],
[10,5,0,10,11,10,16,9],
[15,10,15,0,10,16,13,14],
[17,14,14,15,0,17,15,12],
[6,3,15,9,8,0,21,14],
[6,4,9,12,10,4,0,2],
[7,6,16,11,13,11,23,0]])



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
result = np.append(np.array([8, 25, 95, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,16,14,10,8,12],
[12,0,15,10,18,15,8,16],
[12,10,0,12,18,15,7,15],
[9,15,13,0,14,12,13,15],
[11,7,7,11,0,9,7,13],
[15,10,10,13,16,0,7,15],
[17,17,18,12,18,18,0,15],
[13,9,10,10,12,10,10,0]])



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
result = np.append(np.array([8, 25, 96, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,8,12,22,14,16,12],
[3,0,9,9,17,16,11,15],
[17,16,0,9,17,16,19,9],
[13,16,16,0,17,10,18,14],
[3,8,8,8,0,2,8,8],
[11,9,9,15,23,0,17,13],
[9,14,6,7,17,8,0,12],
[13,10,16,11,17,12,13,0]])



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
result = np.append(np.array([8, 25, 97, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,14,19,19,14,7,19],
[11,0,13,19,12,12,18,18],
[11,12,0,19,12,19,18,12],
[6,6,6,0,18,7,13,18],
[6,13,13,7,0,7,13,18],
[11,13,6,18,18,0,18,18],
[18,7,7,12,12,7,0,19],
[6,7,13,7,7,7,6,0]])



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
result = np.append(np.array([8, 25, 98, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,16,15,15,12,15,14],
[13,0,13,11,13,14,11,14],
[9,12,0,15,14,16,14,12],
[10,14,10,0,15,11,13,12],
[10,12,11,10,0,12,12,13],
[13,11,9,14,13,0,13,10],
[10,14,11,12,13,12,0,11],
[11,11,13,13,12,15,14,0]])



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
result = np.append(np.array([8, 25, 99, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,12,17,14,18,18,15],
[3,0,12,7,10,8,3,6],
[13,13,0,10,13,18,13,6],
[8,18,15,0,15,8,8,11],
[11,15,12,10,0,11,11,11],
[7,17,7,17,14,0,10,10],
[7,22,12,17,14,15,0,15],
[10,19,19,14,14,15,10,0]])



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
result = np.append(np.array([8, 25, 100, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,9,9,7,2,2,4],
[16,0,9,9,16,9,9,16],
[16,16,0,9,16,16,16,16],
[16,16,16,0,21,16,11,16],
[18,9,9,4,0,18,11,18],
[23,16,9,9,7,0,9,23],
[23,16,9,14,14,16,0,16],
[21,9,9,9,7,2,9,0]])



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
result = np.append(np.array([8, 25, 101, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,14,13,15,10,14,10],
[9,0,10,12,13,12,14,8],
[11,15,0,12,13,14,13,14],
[12,13,13,0,13,13,16,14],
[10,12,12,12,0,8,15,11],
[15,13,11,12,17,0,15,10],
[11,11,12,9,10,10,0,13],
[15,17,11,11,14,15,12,0]])



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
result = np.append(np.array([8, 25, 102, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,19,12,19,14,15,13],
[11,0,12,14,17,14,10,13],
[6,13,0,9,12,8,6,13],
[13,11,16,0,16,11,14,18],
[6,8,13,9,0,9,8,15],
[11,11,17,14,16,0,8,14],
[10,15,19,11,17,17,0,19],
[12,12,12,7,10,11,6,0]])



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
result = np.append(np.array([8, 25, 103, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,12,15,15,13,14],
[12,0,9,11,10,17,13,13],
[12,16,0,11,13,15,11,14],
[13,14,14,0,13,16,12,17],
[10,15,12,12,0,16,11,14],
[10,8,10,9,9,0,9,11],
[12,12,14,13,14,16,0,15],
[11,12,11,8,11,14,10,0]])



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
result = np.append(np.array([8, 25, 104, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,16,19,15,18,18,13],
[13,0,18,19,16,17,13,12],
[9,7,0,16,14,16,10,9],
[6,6,9,0,9,14,8,8],
[10,9,11,16,0,12,7,9],
[7,8,9,11,13,0,11,5],
[7,12,15,17,18,14,0,13],
[12,13,16,17,16,20,12,0]])



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
result = np.append(np.array([8, 25, 105, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,12,15,13,15,11,13],
[14,0,10,11,9,9,5,11],
[13,15,0,12,12,13,15,13],
[10,14,13,0,12,11,10,12],
[12,16,13,13,0,9,12,13],
[10,16,12,14,16,0,12,16],
[14,20,10,15,13,13,0,16],
[12,14,12,13,12,9,9,0]])



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
result = np.append(np.array([8, 25, 106, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,14,9,13,14,15,13],
[10,0,14,12,12,16,15,15],
[11,11,0,14,16,15,16,15],
[16,13,11,0,13,12,17,13],
[12,13,9,12,0,13,14,10],
[11,9,10,13,12,0,15,14],
[10,10,9,8,11,10,0,7],
[12,10,10,12,15,11,18,0]])



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
result = np.append(np.array([8, 25, 107, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,15,14,13,13,10,14],
[10,0,10,14,11,13,11,14],
[10,15,0,14,8,13,10,12],
[11,11,11,0,9,9,7,12],
[12,14,17,16,0,14,14,12],
[12,12,12,16,11,0,10,13],
[15,14,15,18,11,15,0,13],
[11,11,13,13,13,12,12,0]])



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
result = np.append(np.array([8, 25, 108, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,12,11,13,6,17,13],
[15,0,10,16,21,13,16,15],
[13,15,0,14,14,7,12,12],
[14,9,11,0,11,5,20,15],
[12,4,11,14,0,10,14,13],
[19,12,18,20,15,0,23,19],
[8,9,13,5,11,2,0,9],
[12,10,13,10,12,6,16,0]])



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
result = np.append(np.array([8, 25, 109, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,5,9,12,15,9,13],
[13,0,10,12,19,9,9,17],
[20,15,0,12,20,15,18,17],
[16,13,13,0,17,8,7,14],
[13,6,5,8,0,11,1,11],
[10,16,10,17,14,0,9,11],
[16,16,7,18,24,16,0,18],
[12,8,8,11,14,14,7,0]])



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
result = np.append(np.array([8, 25, 110, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,9,25,25,13,9,13],
[0,0,9,13,9,9,9,9],
[16,16,0,16,25,13,13,4],
[0,12,9,0,21,9,9,0],
[0,16,0,4,0,0,0,0],
[12,16,12,16,25,0,9,16],
[16,16,12,16,25,16,0,16],
[12,16,21,25,25,9,9,0]])



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
result = np.append(np.array([8, 25, 111, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,11,16,11,13,12,9],
[12,0,9,11,12,9,11,12],
[14,16,0,12,18,17,17,13],
[9,14,13,0,15,8,17,9],
[14,13,7,10,0,9,11,11],
[12,16,8,17,16,0,16,12],
[13,14,8,8,14,9,0,7],
[16,13,12,16,14,13,18,0]])



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
result = np.append(np.array([8, 25, 112, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,12,15,11,10,17,14],
[14,0,14,12,12,14,19,14],
[13,11,0,8,10,11,14,15],
[10,13,17,0,11,12,14,13],
[14,13,15,14,0,12,18,18],
[15,11,14,13,13,0,19,15],
[8,6,11,11,7,6,0,6],
[11,11,10,12,7,10,19,0]])



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
result = np.append(np.array([8, 25, 113, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,11,9,15,8,11,4],
[20,0,21,18,20,17,20,10],
[14,4,0,11,13,9,14,13],
[16,7,14,0,13,12,9,10],
[10,5,12,12,0,9,13,10],
[17,8,16,13,16,0,20,10],
[14,5,11,16,12,5,0,4],
[21,15,12,15,15,15,21,0]])



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
result = np.append(np.array([8, 25, 114, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,7,13,7,19,19,19],
[6,0,6,6,13,18,6,13],
[18,19,0,18,19,12,12,19],
[12,19,7,0,7,12,12,19],
[18,12,6,18,0,18,18,18],
[6,7,13,13,7,0,13,13],
[6,19,13,13,7,12,0,7],
[6,12,6,6,7,12,18,0]])



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
result = np.append(np.array([8, 25, 115, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,19,11,21,17,18,14],
[14,0,19,17,17,17,19,11],
[6,6,0,1,11,11,14,7],
[14,8,24,0,19,18,16,10],
[4,8,14,6,0,15,12,7],
[8,8,14,7,10,0,15,12],
[7,6,11,9,13,10,0,9],
[11,14,18,15,18,13,16,0]])



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
result = np.append(np.array([8, 25, 116, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,6,7,9,10,12,10],
[15,0,14,11,16,13,13,16],
[19,11,0,11,13,14,12,14],
[18,14,14,0,13,13,13,11],
[16,9,12,12,0,11,12,10],
[15,12,11,12,14,0,15,13],
[13,12,13,12,13,10,0,14],
[15,9,11,14,15,12,11,0]])



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
result = np.append(np.array([8, 25, 117, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,17,14,9,15,16,12],
[11,0,17,15,13,18,14,16],
[8,8,0,9,7,16,11,11],
[11,10,16,0,13,20,13,13],
[16,12,18,12,0,22,16,14],
[10,7,9,5,3,0,8,7],
[9,11,14,12,9,17,0,14],
[13,9,14,12,11,18,11,0]])



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
result = np.append(np.array([8, 25, 118, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,15,14,12,13,16,14],
[14,0,14,13,13,11,16,13],
[10,11,0,12,10,11,12,15],
[11,12,13,0,13,12,14,14],
[13,12,15,12,0,11,13,13],
[12,14,14,13,14,0,14,12],
[9,9,13,11,12,11,0,14],
[11,12,10,11,12,13,11,0]])



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
result = np.append(np.array([8, 25, 119, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,12,15,10,13,14,15],
[11,0,7,10,14,13,9,13],
[13,18,0,10,12,10,17,15],
[10,15,15,0,13,13,9,14],
[15,11,13,12,0,9,15,9],
[12,12,15,12,16,0,18,17],
[11,16,8,16,10,7,0,12],
[10,12,10,11,16,8,13,0]])



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
result = np.append(np.array([8, 25, 120, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,11,14,10,12,14,10],
[10,0,11,11,9,12,9,9],
[14,14,0,17,15,10,10,16],
[11,14,8,0,8,15,7,10],
[15,16,10,17,0,17,15,14],
[13,13,15,10,8,0,7,13],
[11,16,15,18,10,18,0,14],
[15,16,9,15,11,12,11,0]])



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
result = np.append(np.array([8, 25, 121, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,10,13,7,11,13,8],
[20,0,17,18,11,16,15,11],
[15,8,0,11,11,9,12,11],
[12,7,14,0,13,12,12,12],
[18,14,14,12,0,19,13,16],
[14,9,16,13,6,0,15,12],
[12,10,13,13,12,10,0,7],
[17,14,14,13,9,13,18,0]])



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
result = np.append(np.array([8, 25, 122, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,16,9,9,13,8,8],
[25,0,16,9,20,21,16,8],
[9,9,0,6,17,6,9,5],
[16,16,19,0,20,13,8,0],
[16,5,8,5,0,13,8,5],
[12,4,19,12,12,0,8,0],
[17,9,16,17,17,17,0,13],
[17,17,20,25,20,25,12,0]])



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
result = np.append(np.array([8, 25, 123, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,16,18,14,10,18,15],
[16,0,17,16,14,12,14,14],
[9,8,0,17,10,8,6,14],
[7,9,8,0,11,8,12,14],
[11,11,15,14,0,13,17,16],
[15,13,17,17,12,0,16,20],
[7,11,19,13,8,9,0,13],
[10,11,11,11,9,5,12,0]])



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
result = np.append(np.array([8, 25, 124, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,8,11,8,12,11,12],
[15,0,15,12,12,18,14,15],
[17,10,0,14,14,19,16,15],
[14,13,11,0,9,14,15,14],
[17,13,11,16,0,17,15,13],
[13,7,6,11,8,0,9,9],
[14,11,9,10,10,16,0,12],
[13,10,10,11,12,16,13,0]])



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
result = np.append(np.array([8, 25, 125, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,13,14,9,19,15,14],
[7,0,8,11,10,16,10,10],
[12,17,0,12,12,15,12,17],
[11,14,13,0,11,18,15,14],
[16,15,13,14,0,16,11,11],
[6,9,10,7,9,0,16,6],
[10,15,13,10,14,9,0,12],
[11,15,8,11,14,19,13,0]])



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
result = np.append(np.array([8, 25, 126, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,12,16,13,14,17,17],
[9,0,8,10,10,13,14,15],
[13,17,0,17,12,13,17,13],
[9,15,8,0,10,13,10,13],
[12,15,13,15,0,14,15,13],
[11,12,12,12,11,0,17,15],
[8,11,8,15,10,8,0,14],
[8,10,12,12,12,10,11,0]])



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
result = np.append(np.array([8, 25, 127, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,12,8,6,6,8,5],
[16,0,15,13,11,13,8,13],
[13,10,0,7,4,7,6,6],
[17,12,18,0,7,12,9,9],
[19,14,21,18,0,14,9,14],
[19,12,18,13,11,0,11,12],
[17,17,19,16,16,14,0,11],
[20,12,19,16,11,13,14,0]])



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
result = np.append(np.array([8, 25, 128, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,14,7,15,11,15,13],
[11,0,10,8,12,13,14,17],
[11,15,0,13,12,13,17,16],
[18,17,12,0,13,15,16,15],
[10,13,13,12,0,15,15,15],
[14,12,12,10,10,0,11,14],
[10,11,8,9,10,14,0,14],
[12,8,9,10,10,11,11,0]])



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
result = np.append(np.array([8, 25, 129, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,12,12,11,13,14,11],
[12,0,13,13,11,16,12,15],
[13,12,0,14,13,12,12,14],
[13,12,11,0,9,13,14,12],
[14,14,12,16,0,17,13,18],
[12,9,13,12,8,0,15,15],
[11,13,13,11,12,10,0,16],
[14,10,11,13,7,10,9,0]])



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
result = np.append(np.array([8, 25, 130, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,18,18,13,13,18,11],
[13,0,19,17,11,8,14,11],
[7,6,0,15,8,6,4,8],
[7,8,10,0,9,8,8,3],
[12,14,17,16,0,11,14,14],
[12,17,19,17,14,0,17,14],
[7,11,21,17,11,8,0,12],
[14,14,17,22,11,11,13,0]])



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
result = np.append(np.array([8, 25, 131, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,8,6,13,8,10,9],
[15,0,13,12,11,14,13,14],
[17,12,0,13,14,16,16,15],
[19,13,12,0,13,15,13,16],
[12,14,11,12,0,13,12,13],
[17,11,9,10,12,0,11,11],
[15,12,9,12,13,14,0,15],
[16,11,10,9,12,14,10,0]])



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
result = np.append(np.array([8, 25, 132, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,12,12,12,7,11,10],
[12,0,10,10,15,10,13,8],
[13,15,0,12,12,11,13,11],
[13,15,13,0,18,13,15,11],
[13,10,13,7,0,10,11,8],
[18,15,14,12,15,0,12,13],
[14,12,12,10,14,13,0,13],
[15,17,14,14,17,12,12,0]])



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
result = np.append(np.array([8, 25, 133, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,13,9,14,12,13,15],
[11,0,9,11,13,12,9,14],
[12,16,0,12,13,14,14,16],
[16,14,13,0,16,17,12,16],
[11,12,12,9,0,10,11,13],
[13,13,11,8,15,0,13,13],
[12,16,11,13,14,12,0,16],
[10,11,9,9,12,12,9,0]])



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
result = np.append(np.array([8, 25, 134, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,15,10,22,8,15,15],
[14,0,12,14,21,12,15,22],
[10,13,0,20,20,17,14,24],
[15,11,5,0,22,14,9,22],
[3,4,5,3,0,1,3,14],
[17,13,8,11,24,0,10,21],
[10,10,11,16,22,15,0,23],
[10,3,1,3,11,4,2,0]])



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
result = np.append(np.array([8, 25, 135, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,5,9,9,0,6,14],
[16,0,5,12,11,3,11,17],
[20,20,0,12,20,14,15,18],
[16,13,13,0,19,16,11,11],
[16,14,5,6,0,5,6,17],
[25,22,11,9,20,0,11,20],
[19,14,10,14,19,14,0,17],
[11,8,7,14,8,5,8,0]])



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
result = np.append(np.array([8, 25, 136, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,10,14,9,12,13],
[15,0,11,13,17,13,14,12],
[15,14,0,15,14,11,12,11],
[15,12,10,0,16,11,13,13],
[11,8,11,9,0,7,11,10],
[16,12,14,14,18,0,14,14],
[13,11,13,12,14,11,0,12],
[12,13,14,12,15,11,13,0]])



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
result = np.append(np.array([8, 25, 137, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,15,13,10,15,13,10],
[15,0,16,21,15,16,12,13],
[10,9,0,14,11,11,7,10],
[12,4,11,0,13,12,11,10],
[15,10,14,12,0,17,14,11],
[10,9,14,13,8,0,9,13],
[12,13,18,14,11,16,0,13],
[15,12,15,15,14,12,12,0]])



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
result = np.append(np.array([8, 25, 138, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,11,13,16,11,9,13],
[11,0,10,12,14,8,8,9],
[14,15,0,16,16,9,11,12],
[12,13,9,0,14,11,6,16],
[9,11,9,11,0,9,8,9],
[14,17,16,14,16,0,13,10],
[16,17,14,19,17,12,0,14],
[12,16,13,9,16,15,11,0]])



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
result = np.append(np.array([8, 25, 139, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,15,15,12,19,13,15],
[10,0,12,12,13,11,14,14],
[10,13,0,14,10,12,12,15],
[10,13,11,0,13,11,14,18],
[13,12,15,12,0,14,16,17],
[6,14,13,14,11,0,13,13],
[12,11,13,11,9,12,0,12],
[10,11,10,7,8,12,13,0]])



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
result = np.append(np.array([8, 25, 140, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,17,13,17,14,14,12],
[13,0,11,12,12,10,10,8],
[8,14,0,7,8,6,8,9],
[12,13,18,0,19,12,15,13],
[8,13,17,6,0,11,12,10],
[11,15,19,13,14,0,14,11],
[11,15,17,10,13,11,0,12],
[13,17,16,12,15,14,13,0]])



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
result = np.append(np.array([8, 25, 141, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,16,14,10,7,10],
[15,0,7,6,13,0,0,5],
[15,18,0,10,16,12,10,12],
[9,19,15,0,16,17,7,10],
[11,12,9,9,0,12,9,9],
[15,25,13,8,13,0,13,13],
[18,25,15,18,16,12,0,10],
[15,20,13,15,16,12,15,0]])



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
result = np.append(np.array([8, 25, 142, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,12,11,13,12,8,14],
[7,0,12,12,12,12,6,11],
[13,13,0,12,13,15,12,15],
[14,13,13,0,13,11,13,12],
[12,13,12,12,0,9,11,14],
[13,13,10,14,16,0,12,11],
[17,19,13,12,14,13,0,14],
[11,14,10,13,11,14,11,0]])



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
result = np.append(np.array([8, 25, 143, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,9,14,13,15,14,12],
[12,0,15,9,16,15,15,15],
[16,10,0,12,12,16,12,11],
[11,16,13,0,11,14,18,15],
[12,9,13,14,0,12,15,15],
[10,10,9,11,13,0,18,12],
[11,10,13,7,10,7,0,14],
[13,10,14,10,10,13,11,0]])



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
result = np.append(np.array([8, 25, 144, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,13,12,12,11,13,12],
[13,0,12,16,14,12,12,10],
[12,13,0,11,10,12,10,12],
[13,9,14,0,15,14,10,15],
[13,11,15,10,0,14,11,12],
[14,13,13,11,11,0,13,12],
[12,13,15,15,14,12,0,16],
[13,15,13,10,13,13,9,0]])



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
result = np.append(np.array([8, 25, 145, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,11,14,16,13,9,16],
[6,0,6,10,9,5,6,6],
[14,19,0,16,16,13,6,17],
[11,15,9,0,12,18,14,19],
[9,16,9,13,0,8,9,14],
[12,20,12,7,17,0,7,17],
[16,19,19,11,16,18,0,19],
[9,19,8,6,11,8,6,0]])



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
result = np.append(np.array([8, 25, 146, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,12,10,13,12,8,11],
[15,0,11,8,10,19,11,12],
[13,14,0,19,15,17,15,11],
[15,17,6,0,11,17,10,13],
[12,15,10,14,0,17,4,13],
[13,6,8,8,8,0,7,10],
[17,14,10,15,21,18,0,16],
[14,13,14,12,12,15,9,0]])



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
result = np.append(np.array([8, 25, 147, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,16,10,12,11,11,14],
[18,0,18,13,12,16,18,15],
[9,7,0,10,12,9,5,12],
[15,12,15,0,13,13,9,12],
[13,13,13,12,0,16,10,10],
[14,9,16,12,9,0,17,11],
[14,7,20,16,15,8,0,12],
[11,10,13,13,15,14,13,0]])



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
result = np.append(np.array([8, 25, 148, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,9,13,12,16,11],
[14,0,14,10,16,12,18,10],
[14,11,0,11,16,13,15,13],
[16,15,14,0,15,17,18,12],
[12,9,9,10,0,7,11,9],
[13,13,12,8,18,0,16,8],
[9,7,10,7,14,9,0,8],
[14,15,12,13,16,17,17,0]])



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
result = np.append(np.array([8, 25, 149, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,12,16,13,13,11,13],
[16,0,13,18,15,11,14,12],
[13,12,0,14,13,11,14,12],
[9,7,11,0,14,8,13,7],
[12,10,12,11,0,4,12,8],
[12,14,14,17,21,0,16,12],
[14,11,11,12,13,9,0,9],
[12,13,13,18,17,13,16,0]])



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
result = np.append(np.array([8, 25, 150, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,13,10,13,15,13,17],
[9,0,14,11,11,14,12,15],
[12,11,0,15,13,12,13,15],
[15,14,10,0,11,16,11,16],
[12,14,12,14,0,10,16,16],
[10,11,13,9,15,0,15,19],
[12,13,12,14,9,10,0,11],
[8,10,10,9,9,6,14,0]])



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
result = np.append(np.array([8, 25, 151, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,7,20,14,18,17,15],
[16,0,15,20,18,22,19,12],
[18,10,0,15,13,19,17,15],
[5,5,10,0,7,11,10,4],
[11,7,12,18,0,21,20,14],
[7,3,6,14,4,0,11,8],
[8,6,8,15,5,14,0,11],
[10,13,10,21,11,17,14,0]])



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
result = np.append(np.array([8, 25, 152, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,16,11,12,13,13,12],
[14,0,16,12,13,16,16,16],
[9,9,0,12,8,14,13,13],
[14,13,13,0,11,14,18,12],
[13,12,17,14,0,15,17,14],
[12,9,11,11,10,0,13,10],
[12,9,12,7,8,12,0,6],
[13,9,12,13,11,15,19,0]])



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
result = np.append(np.array([8, 25, 153, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,18,12,15,17,13,15],
[6,0,12,6,11,11,8,13],
[7,13,0,12,11,13,6,12],
[13,19,13,0,14,18,9,13],
[10,14,14,11,0,13,9,12],
[8,14,12,7,12,0,8,15],
[12,17,19,16,16,17,0,15],
[10,12,13,12,13,10,10,0]])



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
result = np.append(np.array([8, 25, 154, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,18,11,12,12,13,7],
[8,0,14,9,16,10,15,11],
[7,11,0,14,10,13,11,9],
[14,16,11,0,14,12,17,14],
[13,9,15,11,0,13,17,12],
[13,15,12,13,12,0,9,10],
[12,10,14,8,8,16,0,11],
[18,14,16,11,13,15,14,0]])



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
result = np.append(np.array([8, 25, 155, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,17,13,15,13,16,11],
[11,0,10,12,18,15,13,10],
[8,15,0,12,12,12,10,13],
[12,13,13,0,15,15,14,12],
[10,7,13,10,0,11,12,10],
[12,10,13,10,14,0,14,9],
[9,12,15,11,13,11,0,8],
[14,15,12,13,15,16,17,0]])



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
result = np.append(np.array([8, 25, 156, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,8,11,11,15,11,8],
[10,0,8,7,13,11,10,8],
[17,17,0,11,15,17,18,14],
[14,18,14,0,15,19,12,9],
[14,12,10,10,0,12,10,12],
[10,14,8,6,13,0,10,11],
[14,15,7,13,15,15,0,9],
[17,17,11,16,13,14,16,0]])



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
result = np.append(np.array([8, 25, 157, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,14,15,11,16,17,15],
[20,0,14,14,12,16,19,15],
[11,11,0,11,14,12,14,10],
[10,11,14,0,12,13,16,14],
[14,13,11,13,0,10,13,15],
[9,9,13,12,15,0,15,13],
[8,6,11,9,12,10,0,10],
[10,10,15,11,10,12,15,0]])



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
result = np.append(np.array([8, 25, 158, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,10,10,12,12,9,4],
[18,0,14,15,14,13,12,7],
[15,11,0,11,11,13,10,11],
[15,10,14,0,12,15,12,9],
[13,11,14,13,0,14,15,10],
[13,12,12,10,11,0,8,13],
[16,13,15,13,10,17,0,12],
[21,18,14,16,15,12,13,0]])



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
result = np.append(np.array([8, 25, 159, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,8,9,5,9,5,5],
[17,0,14,18,10,8,10,12],
[17,11,0,18,11,9,15,9],
[16,7,7,0,6,4,13,11],
[20,15,14,19,0,14,10,18],
[16,17,16,21,11,0,14,13],
[20,15,10,12,15,11,0,8],
[20,13,16,14,7,12,17,0]])



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
result = np.append(np.array([8, 25, 160, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,12,12,16,16,15,14],
[11,0,14,11,14,10,14,14],
[13,11,0,13,11,13,13,15],
[13,14,12,0,12,11,11,13],
[9,11,14,13,0,11,15,16],
[9,15,12,14,14,0,11,14],
[10,11,12,14,10,14,0,13],
[11,11,10,12,9,11,12,0]])



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
result = np.append(np.array([8, 25, 161, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,15,15,11,14,8],
[15,0,11,16,15,10,15,10],
[15,14,0,18,17,12,17,13],
[10,9,7,0,11,9,8,7],
[10,10,8,14,0,9,11,9],
[14,15,13,16,16,0,14,12],
[11,10,8,17,14,11,0,10],
[17,15,12,18,16,13,15,0]])



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
result = np.append(np.array([8, 25, 162, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,22,9,22,10,15,15],
[10,0,14,15,18,12,10,9],
[3,11,0,9,18,5,4,4],
[16,10,16,0,18,3,10,17],
[3,7,7,7,0,9,3,2],
[15,13,20,22,16,0,9,16],
[10,15,21,15,22,16,0,15],
[10,16,21,8,23,9,10,0]])



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
result = np.append(np.array([8, 25, 163, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,15,16,8,13,15,12],
[12,0,13,16,14,15,14,11],
[10,12,0,17,14,15,17,12],
[9,9,8,0,9,10,11,11],
[17,11,11,16,0,12,15,13],
[12,10,10,15,13,0,13,11],
[10,11,8,14,10,12,0,12],
[13,14,13,14,12,14,13,0]])



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
result = np.append(np.array([8, 25, 164, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,10,5,12,6,8,11],
[18,0,11,13,18,11,7,19],
[15,14,0,14,11,11,14,17],
[20,12,11,0,16,11,15,14],
[13,7,14,9,0,7,9,14],
[19,14,14,14,18,0,12,18],
[17,18,11,10,16,13,0,15],
[14,6,8,11,11,7,10,0]])



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
result = np.append(np.array([8, 25, 165, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,14,10,9,12,7,16],
[13,0,16,14,14,10,7,7],
[11,9,0,10,5,12,10,12],
[15,11,15,0,18,10,13,18],
[16,11,20,7,0,10,14,18],
[13,15,13,15,15,0,11,15],
[18,18,15,12,11,14,0,22],
[9,18,13,7,7,10,3,0]])



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
result = np.append(np.array([8, 25, 166, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,13,10,14,10,17,13],
[13,0,15,17,13,16,8,11],
[12,10,0,15,11,10,9,7],
[15,8,10,0,11,12,9,10],
[11,12,14,14,0,13,10,16],
[15,9,15,13,12,0,12,13],
[8,17,16,16,15,13,0,17],
[12,14,18,15,9,12,8,0]])



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
result = np.append(np.array([8, 25, 167, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,6,10,16,18,12,9],
[14,0,15,11,17,20,11,12],
[19,10,0,15,21,17,17,14],
[15,14,10,0,17,16,14,13],
[9,8,4,8,0,18,5,7],
[7,5,8,9,7,0,9,9],
[13,14,8,11,20,16,0,10],
[16,13,11,12,18,16,15,0]])



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
result = np.append(np.array([8, 25, 168, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,13,15,5,9,18,5],
[20,0,9,21,21,20,14,14],
[12,16,0,21,17,20,10,10],
[10,4,4,0,11,14,10,4],
[20,4,8,14,0,20,18,18],
[16,5,5,11,5,0,10,4],
[7,11,15,15,7,15,0,11],
[20,11,15,21,7,21,14,0]])



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
result = np.append(np.array([8, 25, 169, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,14,0,0,5,0,5],
[17,0,14,17,11,10,6,22],
[11,11,0,11,11,16,11,16],
[25,8,14,0,8,5,11,11],
[25,14,14,17,0,11,11,22],
[20,15,9,20,14,0,15,20],
[25,19,14,14,14,10,0,16],
[20,3,9,14,3,5,9,0]])



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
result = np.append(np.array([8, 25, 170, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,11,11,19,13,16,17],
[10,0,10,9,13,12,11,15],
[14,15,0,13,17,10,18,18],
[14,16,12,0,18,15,16,16],
[6,12,8,7,0,12,10,14],
[12,13,15,10,13,0,14,15],
[9,14,7,9,15,11,0,13],
[8,10,7,9,11,10,12,0]])



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
result = np.append(np.array([8, 25, 171, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,14,14,14,9,15,14],
[11,0,14,18,13,14,15,18],
[11,11,0,14,10,20,15,18],
[11,7,11,0,11,11,16,11],
[11,12,15,14,0,10,15,14],
[16,11,5,14,15,0,15,5],
[10,10,10,9,10,10,0,9],
[11,7,7,14,11,20,16,0]])



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
result = np.append(np.array([8, 25, 172, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,11,12,14,12,10,10],
[15,0,15,14,17,12,11,11],
[14,10,0,10,13,10,8,11],
[13,11,15,0,16,16,13,12],
[11,8,12,9,0,13,11,8],
[13,13,15,9,12,0,11,12],
[15,14,17,12,14,14,0,15],
[15,14,14,13,17,13,10,0]])



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
result = np.append(np.array([8, 25, 173, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,13,11,11,12,11,10],
[13,0,14,10,12,13,13,12],
[12,11,0,13,14,17,17,17],
[14,15,12,0,10,13,13,9],
[14,13,11,15,0,15,13,14],
[13,12,8,12,10,0,13,11],
[14,12,8,12,12,12,0,10],
[15,13,8,16,11,14,15,0]])



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
result = np.append(np.array([8, 25, 174, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,11,14,14,12,13,12],
[13,0,11,11,13,13,14,16],
[14,14,0,15,12,16,14,12],
[11,14,10,0,13,12,11,13],
[11,12,13,12,0,14,12,12],
[13,12,9,13,11,0,14,12],
[12,11,11,14,13,11,0,13],
[13,9,13,12,13,13,12,0]])



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
result = np.append(np.array([8, 25, 175, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,13,13,16,12,16,12],
[11,0,14,13,12,13,13,12],
[12,11,0,14,16,14,14,13],
[12,12,11,0,13,10,13,7],
[9,13,9,12,0,11,12,10],
[13,12,11,15,14,0,16,8],
[9,12,11,12,13,9,0,12],
[13,13,12,18,15,17,13,0]])



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
result = np.append(np.array([8, 25, 176, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,18,10,11,18,12,14],
[11,0,15,10,15,17,14,12],
[7,10,0,14,15,13,13,13],
[15,15,11,0,13,16,13,13],
[14,10,10,12,0,11,11,12],
[7,8,12,9,14,0,13,8],
[13,11,12,12,14,12,0,12],
[11,13,12,12,13,17,13,0]])



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
result = np.append(np.array([8, 25, 177, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,9,8,12,5,7,6],
[20,0,9,14,13,5,17,10],
[16,16,0,17,20,12,17,17],
[17,11,8,0,13,11,16,14],
[13,12,5,12,0,15,12,17],
[20,20,13,14,10,0,13,18],
[18,8,8,9,13,12,0,17],
[19,15,8,11,8,7,8,0]])



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
result = np.append(np.array([8, 25, 178, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,14,15,10,14,17,14],
[14,0,12,13,14,14,18,17],
[11,13,0,15,11,12,12,16],
[10,12,10,0,13,12,13,12],
[15,11,14,12,0,16,18,15],
[11,11,13,13,9,0,14,14],
[8,7,13,12,7,11,0,13],
[11,8,9,13,10,11,12,0]])



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
result = np.append(np.array([8, 25, 179, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,14,15,16,11,13,16],
[11,0,17,11,16,13,11,12],
[11,8,0,11,15,16,11,11],
[10,14,14,0,18,13,17,16],
[9,9,10,7,0,11,10,9],
[14,12,9,12,14,0,9,13],
[12,14,14,8,15,16,0,16],
[9,13,14,9,16,12,9,0]])



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
result = np.append(np.array([8, 25, 180, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,8,11,9,10,14,4],
[16,0,12,20,16,12,6,18],
[17,13,0,23,19,19,13,9],
[14,5,2,0,14,10,10,5],
[16,9,6,11,0,5,6,4],
[15,13,6,15,20,0,12,8],
[11,19,12,15,19,13,0,15],
[21,7,16,20,21,17,10,0]])



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
result = np.append(np.array([8, 25, 181, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,15,16,12,13,9,14],
[14,0,12,19,11,14,11,12],
[10,13,0,17,12,17,12,15],
[9,6,8,0,13,10,11,8],
[13,14,13,12,0,13,13,13],
[12,11,8,15,12,0,8,9],
[16,14,13,14,12,17,0,13],
[11,13,10,17,12,16,12,0]])



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
result = np.append(np.array([8, 25, 182, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,20,20,18,11,18,21],
[7,0,15,11,15,17,14,18],
[5,10,0,6,8,8,7,14],
[5,14,19,0,21,14,21,21],
[7,10,17,4,0,7,7,14],
[14,8,17,11,18,0,17,23],
[7,11,18,4,18,8,0,23],
[4,7,11,4,11,2,2,0]])



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
result = np.append(np.array([8, 25, 183, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,10,10,11,10,9,6],
[17,0,17,10,13,17,13,17],
[15,8,0,13,8,13,6,11],
[15,15,12,0,14,15,10,13],
[14,12,17,11,0,14,15,18],
[15,8,12,10,11,0,8,12],
[16,12,19,15,10,17,0,14],
[19,8,14,12,7,13,11,0]])



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
result = np.append(np.array([8, 25, 184, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,19,17,13,14,22,16],
[13,0,12,13,10,14,13,13],
[6,13,0,10,7,7,12,11],
[8,12,15,0,13,10,18,13],
[12,15,18,12,0,14,17,13],
[11,11,18,15,11,0,18,11],
[3,12,13,7,8,7,0,11],
[9,12,14,12,12,14,14,0]])



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
result = np.append(np.array([8, 25, 185, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,17,19,9,17,15,17],
[7,0,17,17,9,7,17,17],
[8,8,0,20,16,15,16,25],
[6,8,5,0,5,6,14,14],
[16,16,9,20,0,11,14,18],
[8,18,10,19,14,0,15,17],
[10,8,9,11,11,10,0,18],
[8,8,0,11,7,8,7,0]])



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
result = np.append(np.array([8, 25, 186, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,6,10,11,15,6,12],
[13,0,16,16,9,15,19,16],
[19,9,0,14,17,14,14,9],
[15,9,11,0,8,15,9,5],
[14,16,8,17,0,16,11,16],
[10,10,11,10,9,0,4,8],
[19,6,11,16,14,21,0,11],
[13,9,16,20,9,17,14,0]])



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
result = np.append(np.array([8, 25, 187, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,5,9,11,2,0,5],
[23,0,10,14,12,7,10,9],
[20,15,0,15,14,16,16,11],
[16,11,10,0,14,14,7,14],
[14,13,11,11,0,4,14,10],
[23,18,9,11,21,0,14,18],
[25,15,9,18,11,11,0,9],
[20,16,14,11,15,7,16,0]])



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
result = np.append(np.array([8, 25, 188, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,9,8,7,8,10,10],
[17,0,14,14,14,12,17,15],
[16,11,0,11,11,9,11,12],
[17,11,14,0,14,13,14,13],
[18,11,14,11,0,12,14,14],
[17,13,16,12,13,0,14,15],
[15,8,14,11,11,11,0,13],
[15,10,13,12,11,10,12,0]])



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
result = np.append(np.array([8, 25, 189, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,25,21,6,15,22,14],
[4,0,14,11,4,11,14,14],
[0,11,0,11,3,7,18,8],
[4,14,14,0,4,13,11,14],
[19,21,22,21,0,10,21,21],
[10,14,18,12,15,0,22,24],
[3,11,7,14,4,3,0,12],
[11,11,17,11,4,1,13,0]])



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
result = np.append(np.array([8, 25, 190, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,14,12,17,14,13,13],
[10,0,12,12,14,12,14,10],
[11,13,0,12,12,10,14,9],
[13,13,13,0,15,13,10,8],
[8,11,13,10,0,12,13,9],
[11,13,15,12,13,0,16,12],
[12,11,11,15,12,9,0,11],
[12,15,16,17,16,13,14,0]])



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
result = np.append(np.array([8, 25, 191, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,16,13,13,13,10,9],
[15,0,16,14,11,10,10,9],
[9,9,0,5,9,11,8,8],
[12,11,20,0,11,13,12,10],
[12,14,16,14,0,8,11,11],
[12,15,14,12,17,0,13,15],
[15,15,17,13,14,12,0,12],
[16,16,17,15,14,10,13,0]])



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
result = np.append(np.array([8, 25, 192, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,11,11,10,11,7,9],
[17,0,15,9,13,13,10,9],
[14,10,0,8,9,13,10,11],
[14,16,17,0,12,14,8,9],
[15,12,16,13,0,12,8,14],
[14,12,12,11,13,0,13,12],
[18,15,15,17,17,12,0,16],
[16,16,14,16,11,13,9,0]])



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
result = np.append(np.array([8, 25, 193, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,5,10,7,9,12,8],
[21,0,16,15,16,11,18,21],
[20,9,0,15,12,14,25,11],
[15,10,10,0,8,9,15,13],
[18,9,13,17,0,14,19,21],
[16,14,11,16,11,0,16,16],
[13,7,0,10,6,9,0,6],
[17,4,14,12,4,9,19,0]])



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
result = np.append(np.array([8, 25, 194, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,24,20,11,24,21,20],
[12,0,17,14,11,20,14,18],
[1,8,0,5,9,14,9,15],
[5,11,20,0,14,16,15,21],
[14,14,16,11,0,13,18,21],
[1,5,11,9,12,0,5,11],
[4,11,16,10,7,20,0,14],
[5,7,10,4,4,14,11,0]])



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
result = np.append(np.array([8, 25, 195, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,12,17,7,12,13,11],
[13,0,15,14,10,15,11,9],
[13,10,0,13,10,16,14,9],
[8,11,12,0,7,11,11,11],
[18,15,15,18,0,13,12,14],
[13,10,9,14,12,0,10,6],
[12,14,11,14,13,15,0,9],
[14,16,16,14,11,19,16,0]])



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
result = np.append(np.array([8, 25, 196, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,16,7,1,7,1,14],
[18,0,16,22,18,16,9,14],
[9,9,0,12,9,1,6,6],
[18,3,13,0,16,11,6,14],
[24,7,16,9,0,9,15,20],
[18,9,24,14,16,0,6,13],
[24,16,19,19,10,19,0,17],
[11,11,19,11,5,12,8,0]])



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
result = np.append(np.array([8, 25, 197, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,8,12,10,10,14,11],
[12,0,14,14,14,16,16,12],
[17,11,0,16,17,16,15,15],
[13,11,9,0,10,9,10,11],
[15,11,8,15,0,14,17,13],
[15,9,9,16,11,0,14,10],
[11,9,10,15,8,11,0,8],
[14,13,10,14,12,15,17,0]])



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
result = np.append(np.array([8, 25, 198, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,10,12,14,12,13,10],
[11,0,10,8,9,8,16,12],
[15,15,0,14,12,14,18,14],
[13,17,11,0,19,17,16,14],
[11,16,13,6,0,15,17,13],
[13,17,11,8,10,0,13,11],
[12,9,7,9,8,12,0,8],
[15,13,11,11,12,14,17,0]])



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
result = np.append(np.array([8, 25, 199, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,12,11,13,12,11],
[14,0,16,14,13,11,12,13],
[14,9,0,14,9,9,9,10],
[13,11,11,0,13,12,13,12],
[14,12,16,12,0,13,13,15],
[12,14,16,13,12,0,14,16],
[13,13,16,12,12,11,0,13],
[14,12,15,13,10,9,12,0]])



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
result = np.append(np.array([8, 25, 200, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebb/mebb_8_25.csv", index=False, header=False)