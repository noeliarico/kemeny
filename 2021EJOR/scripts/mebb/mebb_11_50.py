
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,31,14,20,24,26,29,22,21,16,20],
[19,0,15,18,16,21,21,18,18,17,17],
[36,35,0,31,27,29,30,21,18,25,22],
[30,32,19,0,32,25,27,28,26,19,22],
[26,34,23,18,0,24,24,21,26,24,20],
[24,29,21,25,26,0,27,19,28,26,19],
[21,29,20,23,26,23,0,21,21,24,21],
[28,32,29,22,29,31,29,0,26,28,24],
[29,32,32,24,24,22,29,24,0,22,21],
[34,33,25,31,26,24,26,22,28,0,27],
[30,33,28,28,30,31,29,26,29,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 1, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,50,50,25,50,50,50,25,50,50],
[0,0,0,25,0,0,25,25,25,25,25],
[0,50,0,50,25,25,25,50,25,50,50],
[0,25,0,0,0,0,25,0,0,25,25],
[25,50,25,50,0,25,50,50,25,50,50],
[0,50,25,50,25,0,25,50,25,50,50],
[0,25,25,25,0,25,0,25,0,50,25],
[0,25,0,50,0,0,25,0,0,50,25],
[25,25,25,50,25,25,50,50,0,50,25],
[0,25,0,25,0,0,0,0,0,0,25],
[0,25,0,25,0,0,25,25,25,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 2, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,30,28,28,23,22,24,25,27,22],
[22,0,27,25,22,22,23,25,19,22,22],
[20,23,0,24,22,20,22,21,20,26,21],
[22,25,26,0,25,24,26,26,24,26,23],
[22,28,28,25,0,26,26,28,19,30,26],
[27,28,30,26,24,0,22,27,23,33,23],
[28,27,28,24,24,28,0,25,21,29,24],
[26,25,29,24,22,23,25,0,20,27,25],
[25,31,30,26,31,27,29,30,0,31,20],
[23,28,24,24,20,17,21,23,19,0,24],
[28,28,29,27,24,27,26,25,30,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 3, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,24,26,23,24,25,23,30,26,32],
[23,0,24,31,27,25,28,25,30,24,30],
[26,26,0,24,31,27,27,23,31,27,23],
[24,19,26,0,28,22,19,24,24,25,31],
[27,23,19,22,0,20,26,27,28,21,30],
[26,25,23,28,30,0,28,30,29,23,32],
[25,22,23,31,24,22,0,23,31,26,28],
[27,25,27,26,23,20,27,0,29,27,31],
[20,20,19,26,22,21,19,21,0,20,21],
[24,26,23,25,29,27,24,23,30,0,31],
[18,20,27,19,20,18,22,19,29,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 4, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,26,23,24,13,12,15,20,23,23],
[23,0,28,15,19,22,18,20,25,25,25],
[24,22,0,16,26,22,16,26,26,24,27],
[27,35,34,0,34,24,28,31,27,33,27],
[26,31,24,16,0,20,17,21,19,24,19],
[37,28,28,26,30,0,19,26,25,30,20],
[38,32,34,22,33,31,0,34,32,33,28],
[35,30,24,19,29,24,16,0,29,24,21],
[30,25,24,23,31,25,18,21,0,21,21],
[27,25,26,17,26,20,17,26,29,0,25],
[27,25,23,23,31,30,22,29,29,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 5, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,27,24,21,23,23,26,24,24,27],
[24,0,23,19,21,25,23,25,27,21,23],
[23,27,0,20,19,24,18,21,26,19,26],
[26,31,30,0,25,29,25,31,29,27,30],
[29,29,31,25,0,30,25,30,22,30,30],
[27,25,26,21,20,0,21,31,27,24,27],
[27,27,32,25,25,29,0,30,30,28,29],
[24,25,29,19,20,19,20,0,26,22,24],
[26,23,24,21,28,23,20,24,0,25,26],
[26,29,31,23,20,26,22,28,25,0,27],
[23,27,24,20,20,23,21,26,24,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 6, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,36,28,34,28,29,31,30,25,28],
[19,0,26,19,25,24,30,27,30,22,26],
[14,24,0,21,25,21,21,25,30,23,23],
[22,31,29,0,23,23,31,20,29,24,24],
[16,25,25,27,0,18,31,31,22,23,24],
[22,26,29,27,32,0,31,24,29,23,34],
[21,20,29,19,19,19,0,20,24,26,26],
[19,23,25,30,19,26,30,0,24,17,27],
[20,20,20,21,28,21,26,26,0,16,23],
[25,28,27,26,27,27,24,33,34,0,31],
[22,24,27,26,26,16,24,23,27,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 7, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,31,27,29,29,24,25,26,26,23],
[24,0,26,24,19,22,22,20,24,23,19],
[19,24,0,20,26,26,23,24,24,27,20],
[23,26,30,0,27,27,27,32,27,31,24],
[21,31,24,23,0,26,30,26,29,30,24],
[21,28,24,23,24,0,28,26,25,30,23],
[26,28,27,23,20,22,0,27,23,24,23],
[25,30,26,18,24,24,23,0,25,23,25],
[24,26,26,23,21,25,27,25,0,29,24],
[24,27,23,19,20,20,26,27,21,0,19],
[27,31,30,26,26,27,27,25,26,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 8, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,21,25,31,21,22,27,21,22,25],
[21,0,21,23,27,22,23,25,22,22,23],
[29,29,0,25,29,23,31,23,20,24,24],
[25,27,25,0,32,27,24,26,25,27,30],
[19,23,21,18,0,17,24,24,19,19,18],
[29,28,27,23,33,0,30,28,23,27,25],
[28,27,19,26,26,20,0,22,19,19,16],
[23,25,27,24,26,22,28,0,25,21,23],
[29,28,30,25,31,27,31,25,0,27,27],
[28,28,26,23,31,23,31,29,23,0,27],
[25,27,26,20,32,25,34,27,23,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 9, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,22,23,22,22,21,28,22,25,20],
[32,0,24,27,24,28,25,23,24,28,20],
[28,26,0,27,23,25,30,24,24,32,27],
[27,23,23,0,18,25,21,24,24,23,23],
[28,26,27,32,0,24,22,25,27,29,25],
[28,22,25,25,26,0,24,26,22,30,22],
[29,25,20,29,28,26,0,23,24,30,25],
[22,27,26,26,25,24,27,0,21,29,18],
[28,26,26,26,23,28,26,29,0,26,27],
[25,22,18,27,21,20,20,21,24,0,22],
[30,30,23,27,25,28,25,32,23,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 10, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,44,40,12,12,28,45,45,28,28],
[17,0,29,14,22,14,19,19,24,14,19],
[6,21,0,8,16,2,18,21,23,18,18],
[10,36,42,0,15,17,17,42,32,25,17],
[38,28,34,35,0,17,23,35,40,40,23],
[38,36,48,33,33,0,23,33,50,38,23],
[22,31,32,33,27,27,0,48,37,27,37],
[5,31,29,8,15,17,2,0,27,17,2],
[5,26,27,18,10,0,13,23,0,6,7],
[22,36,32,25,10,12,23,33,44,0,17],
[22,31,32,33,27,27,13,48,43,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 11, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,16,23,20,23,22,21,28,22,26],
[27,0,22,23,26,20,26,22,27,24,25],
[34,28,0,22,25,25,27,21,27,31,31],
[27,27,28,0,29,31,28,28,26,28,24],
[30,24,25,21,0,18,29,20,21,23,15],
[27,30,25,19,32,0,30,24,33,29,29],
[28,24,23,22,21,20,0,21,19,26,23],
[29,28,29,22,30,26,29,0,27,26,25],
[22,23,23,24,29,17,31,23,0,24,20],
[28,26,19,22,27,21,24,24,26,0,22],
[24,25,19,26,35,21,27,25,30,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 12, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,32,29,32,34,25,27,31,31,27],
[22,0,24,23,26,23,22,19,25,30,15],
[18,26,0,25,23,23,22,21,26,26,20],
[21,27,25,0,31,26,23,22,29,29,23],
[18,24,27,19,0,26,18,20,20,24,17],
[16,27,27,24,24,0,18,23,27,24,22],
[25,28,28,27,32,32,0,29,31,30,24],
[23,31,29,28,30,27,21,0,25,29,25],
[19,25,24,21,30,23,19,25,0,31,26],
[19,20,24,21,26,26,20,21,19,0,14],
[23,35,30,27,33,28,26,25,24,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 13, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,22,23,23,23,27,22,21,25,20],
[28,0,25,26,20,25,33,23,23,23,21],
[28,25,0,24,26,23,33,21,21,26,22],
[27,24,26,0,26,22,31,23,23,26,28],
[27,30,24,24,0,27,36,23,22,30,23],
[27,25,27,28,23,0,30,25,26,26,24],
[23,17,17,19,14,20,0,17,19,20,17],
[28,27,29,27,27,25,33,0,26,29,27],
[29,27,29,27,28,24,31,24,0,27,26],
[25,27,24,24,20,24,30,21,23,0,25],
[30,29,28,22,27,26,33,23,24,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 14, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,28,20,26,23,26,28,26,25,26],
[22,0,25,22,26,25,29,30,23,31,26],
[22,25,0,22,22,22,25,31,27,29,23],
[30,28,28,0,29,22,27,34,28,30,30],
[24,24,28,21,0,27,30,26,29,26,24],
[27,25,28,28,23,0,31,29,31,33,27],
[24,21,25,23,20,19,0,29,23,26,21],
[22,20,19,16,24,21,21,0,22,25,20],
[24,27,23,22,21,19,27,28,0,26,21],
[25,19,21,20,24,17,24,25,24,0,18],
[24,24,27,20,26,23,29,30,29,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 15, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,18,29,30,27,33,36,34,45,24],
[21,0,26,24,34,29,21,29,24,28,27],
[32,24,0,25,27,21,34,33,32,34,33],
[21,26,25,0,31,35,27,23,17,25,25],
[20,16,23,19,0,25,23,27,17,27,22],
[23,21,29,15,25,0,30,26,26,33,28],
[17,29,16,23,27,20,0,37,24,28,25],
[14,21,17,27,23,24,13,0,23,37,27],
[16,26,18,33,33,24,26,27,0,31,29],
[5,22,16,25,23,17,22,13,19,0,17],
[26,23,17,25,28,22,25,23,21,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 16, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,28,28,32,27,24,31,27,24,28],
[21,0,25,21,28,21,23,27,23,23,20],
[22,25,0,22,35,29,25,28,32,22,28],
[22,29,28,0,36,30,23,25,27,19,22],
[18,22,15,14,0,18,18,19,25,18,25],
[23,29,21,20,32,0,22,23,23,22,23],
[26,27,25,27,32,28,0,27,25,21,22],
[19,23,22,25,31,27,23,0,22,24,28],
[23,27,18,23,25,27,25,28,0,26,29],
[26,27,28,31,32,28,29,26,24,0,24],
[22,30,22,28,25,27,28,22,21,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 17, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,25,46,46,29,46,25,23,50,25],
[4,0,23,23,44,27,25,25,25,27,25],
[25,27,0,23,46,50,46,46,27,27,50],
[4,27,27,0,27,27,29,25,25,50,29],
[4,6,4,23,0,29,6,2,27,27,6],
[21,23,0,23,21,0,23,23,23,27,2],
[4,25,4,21,44,27,0,0,25,25,4],
[25,25,4,25,48,27,50,0,25,25,27],
[27,25,23,25,23,27,25,25,0,29,25],
[0,23,23,0,23,23,25,25,21,0,25],
[25,25,0,21,44,48,46,23,25,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 18, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,25,29,27,25,25,25,27,24,23],
[26,0,26,34,28,30,30,26,26,25,25],
[25,24,0,32,28,29,25,29,32,22,25],
[21,16,18,0,21,20,16,18,19,16,18],
[23,22,22,29,0,27,21,21,25,27,22],
[25,20,21,30,23,0,24,24,24,21,17],
[25,20,25,34,29,26,0,26,27,26,24],
[25,24,21,32,29,26,24,0,28,23,20],
[23,24,18,31,25,26,23,22,0,22,20],
[26,25,28,34,23,29,24,27,28,0,28],
[27,25,25,32,28,33,26,30,30,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 19, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,21,26,20,19,20,29,19,16,21],
[24,0,25,26,17,16,27,23,21,20,11],
[29,25,0,27,25,24,23,28,18,20,26],
[24,24,23,0,19,22,28,20,16,24,16],
[30,33,25,31,0,28,34,28,27,24,24],
[31,34,26,28,22,0,31,32,26,30,29],
[30,23,27,22,16,19,0,27,26,19,19],
[21,27,22,30,22,18,23,0,15,28,15],
[31,29,32,34,23,24,24,35,0,30,22],
[34,30,30,26,26,20,31,22,20,0,15],
[29,39,24,34,26,21,31,35,28,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 20, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,29,24,23,22,28,28,27,24,24],
[18,0,18,20,16,19,19,19,17,21,18],
[21,32,0,17,16,24,19,19,26,19,28],
[26,30,33,0,26,30,19,21,26,27,28],
[27,34,34,24,0,32,28,26,27,28,25],
[28,31,26,20,18,0,19,22,24,25,27],
[22,31,31,31,22,31,0,25,30,29,33],
[22,31,31,29,24,28,25,0,27,23,31],
[23,33,24,24,23,26,20,23,0,25,29],
[26,29,31,23,22,25,21,27,25,0,23],
[26,32,22,22,25,23,17,19,21,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 21, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,22,27,23,22,28,23,24,24,31],
[28,0,27,28,24,26,26,27,20,26,23],
[28,23,0,31,27,26,28,30,25,30,23],
[23,22,19,0,20,22,24,18,16,23,26],
[27,26,23,30,0,29,25,30,26,28,30],
[28,24,24,28,21,0,25,27,23,19,23],
[22,24,22,26,25,25,0,23,24,28,26],
[27,23,20,32,20,23,27,0,20,22,23],
[26,30,25,34,24,27,26,30,0,20,38],
[26,24,20,27,22,31,22,28,30,0,33],
[19,27,27,24,20,27,24,27,12,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 22, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,20,32,38,15,16,25,32,32,25],
[44,0,24,36,46,23,31,36,42,29,36],
[30,26,0,34,30,24,27,23,39,40,20],
[18,14,16,0,36,7,8,9,25,17,11],
[12,4,20,14,0,7,1,23,15,21,15],
[35,27,26,43,43,0,25,19,43,37,36],
[34,19,23,42,49,25,0,23,49,35,35],
[25,14,27,41,27,31,27,0,30,31,37],
[18,8,11,25,35,7,1,20,0,11,11],
[18,21,10,33,29,13,15,19,39,0,19],
[25,14,30,39,35,14,15,13,39,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 23, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,26,19,25,20,18,26,19,21,26],
[29,0,24,24,34,25,20,27,24,23,26],
[24,26,0,22,32,22,22,24,22,24,21],
[31,26,28,0,33,25,31,33,21,25,30],
[25,16,18,17,0,15,20,22,20,20,21],
[30,25,28,25,35,0,25,28,20,30,29],
[32,30,28,19,30,25,0,28,19,25,25],
[24,23,26,17,28,22,22,0,22,21,25],
[31,26,28,29,30,30,31,28,0,25,33],
[29,27,26,25,30,20,25,29,25,0,21],
[24,24,29,20,29,21,25,25,17,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 24, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,23,23,27,19,15,20,19,18,20],
[34,0,23,19,29,29,22,26,24,14,25],
[27,27,0,25,32,31,22,23,25,17,27],
[27,31,25,0,34,28,32,31,31,26,31],
[23,21,18,16,0,21,14,18,25,17,15],
[31,21,19,22,29,0,21,28,21,18,20],
[35,28,28,18,36,29,0,29,26,22,25],
[30,24,27,19,32,22,21,0,21,18,23],
[31,26,25,19,25,29,24,29,0,16,24],
[32,36,33,24,33,32,28,32,34,0,28],
[30,25,23,19,35,30,25,27,26,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 25, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,26,24,29,25,35,23,27,25,27],
[21,0,24,30,22,23,28,26,32,29,25],
[24,26,0,32,27,22,28,27,26,23,22],
[26,20,18,0,23,23,25,22,23,19,15],
[21,28,23,27,0,20,24,22,27,25,30],
[25,27,28,27,30,0,37,33,33,28,26],
[15,22,22,25,26,13,0,22,29,20,19],
[27,24,23,28,28,17,28,0,34,28,28],
[23,18,24,27,23,17,21,16,0,25,19],
[25,21,27,31,25,22,30,22,25,0,24],
[23,25,28,35,20,24,31,22,31,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 26, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,22,23,27,20,21,19,22,21,26],
[32,0,24,27,28,25,29,25,22,25,29],
[28,26,0,26,25,26,27,20,26,26,22],
[27,23,24,0,24,22,23,20,23,25,20],
[23,22,25,26,0,25,21,20,22,21,24],
[30,25,24,28,25,0,27,22,26,24,23],
[29,21,23,27,29,23,0,24,25,28,27],
[31,25,30,30,30,28,26,0,25,26,24],
[28,28,24,27,28,24,25,25,0,27,22],
[29,25,24,25,29,26,22,24,23,0,26],
[24,21,28,30,26,27,23,26,28,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 27, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,9,0,20,31,14,30,20,31,15],
[25,0,19,19,31,37,11,25,19,40,9],
[41,31,0,6,35,31,36,32,34,31,20],
[50,31,44,0,36,32,36,42,43,32,23],
[30,19,15,14,0,32,6,30,19,30,20],
[19,13,19,18,18,0,19,30,18,24,9],
[36,39,14,14,44,31,0,40,25,39,15],
[20,25,18,8,20,20,10,0,19,25,18],
[30,31,16,7,31,32,25,31,0,32,29],
[19,10,19,18,20,26,11,25,18,0,9],
[35,41,30,27,30,41,35,32,21,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 28, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,19,19,19,24,19,16,19,9,19],
[27,0,17,11,26,28,11,17,27,12,22],
[31,33,0,33,33,39,22,27,22,30,33],
[31,39,17,0,30,32,15,17,31,25,26],
[31,24,17,20,0,36,11,17,17,20,41],
[26,22,11,18,14,0,15,27,15,19,23],
[31,39,28,35,39,35,0,28,28,25,40],
[34,33,23,33,33,23,22,0,33,9,33],
[31,23,28,19,33,35,22,17,0,20,29],
[41,38,20,25,30,31,25,41,30,0,25],
[31,28,17,24,9,27,10,17,21,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 29, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,17,18,26,17,18,23,24,22,25],
[25,0,19,18,24,22,18,16,19,21,23],
[33,31,0,28,33,25,26,28,29,26,28],
[32,32,22,0,33,24,23,24,30,30,31],
[24,26,17,17,0,17,17,19,23,18,24],
[33,28,25,26,33,0,27,33,26,29,34],
[32,32,24,27,33,23,0,24,35,27,30],
[27,34,22,26,31,17,26,0,25,20,30],
[26,31,21,20,27,24,15,25,0,22,28],
[28,29,24,20,32,21,23,30,28,0,30],
[25,27,22,19,26,16,20,20,22,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 30, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,32,24,28,23,30,25,28,26,22],
[21,0,32,20,26,32,27,25,22,19,34],
[18,18,0,17,22,24,17,17,23,20,26],
[26,30,33,0,30,30,28,28,23,29,29],
[22,24,28,20,0,31,27,28,27,26,22],
[27,18,26,20,19,0,27,20,26,21,20],
[20,23,33,22,23,23,0,21,23,17,25],
[25,25,33,22,22,30,29,0,27,26,28],
[22,28,27,27,23,24,27,23,0,29,31],
[24,31,30,21,24,29,33,24,21,0,29],
[28,16,24,21,28,30,25,22,19,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 31, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,20,25,16,27,19,27,25,24,21],
[29,0,22,26,23,27,26,22,29,25,30],
[30,28,0,31,24,37,27,26,32,32,31],
[25,24,19,0,20,23,20,17,22,25,21],
[34,27,26,30,0,35,25,28,31,28,33],
[23,23,13,27,15,0,18,20,25,26,19],
[31,24,23,30,25,32,0,24,31,30,27],
[23,28,24,33,22,30,26,0,27,28,27],
[25,21,18,28,19,25,19,23,0,26,29],
[26,25,18,25,22,24,20,22,24,0,25],
[29,20,19,29,17,31,23,23,21,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 32, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,44,31,36,16,15,7,21,29,31],
[14,0,44,32,21,14,15,19,1,28,1],
[6,6,0,16,22,1,15,5,6,28,1],
[19,18,34,0,34,18,19,19,19,28,5],
[14,29,28,16,0,28,15,18,15,28,15],
[34,36,49,32,22,0,15,19,7,28,16],
[35,35,35,31,35,35,0,35,34,29,22],
[43,31,45,31,32,31,15,0,31,43,30],
[29,49,44,31,35,43,16,19,0,29,30],
[21,22,22,22,22,22,21,7,21,0,21],
[19,49,49,45,35,34,28,20,20,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 33, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,25,21,20,22,28,26,19,25,27],
[24,0,22,19,19,25,22,24,23,23,25],
[25,28,0,24,24,28,30,30,25,28,31],
[29,31,26,0,29,27,35,24,25,28,35],
[30,31,26,21,0,30,23,27,25,27,29],
[28,25,22,23,20,0,25,28,21,22,25],
[22,28,20,15,27,25,0,22,20,24,23],
[24,26,20,26,23,22,28,0,23,25,31],
[31,27,25,25,25,29,30,27,0,30,30],
[25,27,22,22,23,28,26,25,20,0,29],
[23,25,19,15,21,25,27,19,20,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 34, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,25,23,24,26,29,25,29,25,27],
[21,0,22,21,21,28,28,21,30,23,22],
[25,28,0,22,30,29,27,22,32,30,28],
[27,29,28,0,25,26,31,25,32,30,28],
[26,29,20,25,0,27,27,26,27,25,27],
[24,22,21,24,23,0,21,22,25,21,24],
[21,22,23,19,23,29,0,25,27,25,26],
[25,29,28,25,24,28,25,0,33,27,30],
[21,20,18,18,23,25,23,17,0,21,21],
[25,27,20,20,25,29,25,23,29,0,23],
[23,28,22,22,23,26,24,20,29,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 35, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,23,27,25,26,29,26,27,21,26],
[26,0,28,30,25,24,29,25,24,26,26],
[27,22,0,31,30,25,28,25,26,28,27],
[23,20,19,0,20,22,24,21,22,19,18],
[25,25,20,30,0,27,29,23,26,23,20],
[24,26,25,28,23,0,29,23,23,22,25],
[21,21,22,26,21,21,0,18,23,22,22],
[24,25,25,29,27,27,32,0,24,26,20],
[23,26,24,28,24,27,27,26,0,20,22],
[29,24,22,31,27,28,28,24,30,0,25],
[24,24,23,32,30,25,28,30,28,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 36, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,22,18,24,31,29,25,27,25,21],
[26,0,18,26,19,27,26,24,20,21,21],
[28,32,0,30,25,29,29,25,25,32,24],
[32,24,20,0,23,33,27,30,29,30,28],
[26,31,25,27,0,37,29,28,32,34,30],
[19,23,21,17,13,0,23,19,19,26,20],
[21,24,21,23,21,27,0,24,20,29,25],
[25,26,25,20,22,31,26,0,29,26,31],
[23,30,25,21,18,31,30,21,0,27,20],
[25,29,18,20,16,24,21,24,23,0,24],
[29,29,26,22,20,30,25,19,30,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 37, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,24,22,27,26,29,25,22,24,21],
[28,0,22,23,25,27,25,26,21,22,19],
[26,28,0,26,25,30,30,26,24,29,25],
[28,27,24,0,25,27,33,26,24,28,28],
[23,25,25,25,0,27,31,26,24,28,26],
[24,23,20,23,23,0,28,24,24,26,25],
[21,25,20,17,19,22,0,16,22,24,19],
[25,24,24,24,24,26,34,0,20,28,23],
[28,29,26,26,26,26,28,30,0,29,25],
[26,28,21,22,22,24,26,22,21,0,20],
[29,31,25,22,24,25,31,27,25,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 38, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,19,18,22,23,32,17,27,22,19],
[29,0,26,24,17,18,32,21,30,24,24],
[31,24,0,28,23,20,35,29,31,29,24],
[32,26,22,0,20,20,34,24,25,21,25],
[28,33,27,30,0,21,33,24,29,28,27],
[27,32,30,30,29,0,31,22,33,23,24],
[18,18,15,16,17,19,0,12,19,17,18],
[33,29,21,26,26,28,38,0,31,24,29],
[23,20,19,25,21,17,31,19,0,23,21],
[28,26,21,29,22,27,33,26,27,0,34],
[31,26,26,25,23,26,32,21,29,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 39, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,34,22,30,22,31,30,28,28,29],
[17,0,32,24,27,19,25,22,21,28,27],
[16,18,0,15,17,15,16,22,15,23,18],
[28,26,35,0,26,25,29,28,28,26,30],
[20,23,33,24,0,19,27,27,32,27,25],
[28,31,35,25,31,0,30,31,35,31,32],
[19,25,34,21,23,20,0,26,27,19,21],
[20,28,28,22,23,19,24,0,26,25,20],
[22,29,35,22,18,15,23,24,0,24,26],
[22,22,27,24,23,19,31,25,26,0,26],
[21,23,32,20,25,18,29,30,24,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 40, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,43,37,30,33,17,33,33,43,27],
[17,0,34,32,25,22,12,28,13,38,32],
[7,16,0,22,25,18,12,16,10,26,22],
[13,18,28,0,18,14,26,18,14,24,18],
[20,25,25,32,0,16,17,21,6,26,31],
[17,28,32,36,34,0,27,25,17,30,31],
[33,38,38,24,33,23,0,28,23,33,38],
[17,22,34,32,29,25,22,0,13,26,41],
[17,37,40,36,44,33,27,37,0,47,41],
[7,12,24,26,24,20,17,24,3,0,34],
[23,18,28,32,19,19,12,9,9,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 41, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,25,27,31,29,29,27,29,31,28],
[26,0,26,27,22,26,29,28,22,26,34],
[25,24,0,24,26,23,26,30,22,31,32],
[23,23,26,0,25,26,29,27,24,27,30],
[19,28,24,25,0,30,28,27,24,30,23],
[21,24,27,24,20,0,29,26,25,27,25],
[21,21,24,21,22,21,0,21,23,22,25],
[23,22,20,23,23,24,29,0,24,29,23],
[21,28,28,26,26,25,27,26,0,29,31],
[19,24,19,23,20,23,28,21,21,0,25],
[22,16,18,20,27,25,25,27,19,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 42, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,24,24,24,23,29,26,20,31,28],
[22,0,19,21,23,20,27,26,17,26,16],
[26,31,0,25,28,23,31,28,19,33,20],
[26,29,25,0,26,13,19,29,16,26,19],
[26,27,22,24,0,29,34,32,16,34,17],
[27,30,27,37,21,0,18,21,21,30,20],
[21,23,19,31,16,32,0,20,18,21,15],
[24,24,22,21,18,29,30,0,30,28,25],
[30,33,31,34,34,29,32,20,0,35,38],
[19,24,17,24,16,20,29,22,15,0,24],
[22,34,30,31,33,30,35,25,12,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 43, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,12,15,7,7,21,7,15,25,26],
[35,0,27,3,16,16,27,27,17,39,35],
[38,23,0,16,17,17,27,24,17,44,22],
[35,47,34,0,23,16,31,34,31,39,42],
[43,34,33,27,0,22,28,28,29,47,26],
[43,34,33,34,28,0,28,28,21,47,36],
[29,23,23,19,22,22,0,18,26,29,19],
[43,23,26,16,22,22,32,0,19,36,27],
[35,33,33,19,21,29,24,31,0,39,23],
[25,11,6,11,3,3,21,14,11,0,22],
[24,15,28,8,24,14,31,23,27,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 44, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,24,27,27,30,24,24,24,26,28],
[21,0,22,22,20,29,17,17,22,28,21],
[26,28,0,22,26,31,25,21,24,26,27],
[23,28,28,0,27,30,27,21,22,26,26],
[23,30,24,23,0,26,23,24,23,26,24],
[20,21,19,20,24,0,23,21,17,23,21],
[26,33,25,23,27,27,0,29,25,25,25],
[26,33,29,29,26,29,21,0,20,29,23],
[26,28,26,28,27,33,25,30,0,27,27],
[24,22,24,24,24,27,25,21,23,0,26],
[22,29,23,24,26,29,25,27,23,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 45, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,26,31,28,24,31,25,31,33,24],
[27,0,23,31,27,30,29,24,27,30,22],
[24,27,0,30,30,24,35,26,34,31,26],
[19,19,20,0,25,23,27,17,30,25,20],
[22,23,20,25,0,22,22,19,26,23,23],
[26,20,26,27,28,0,26,23,30,30,25],
[19,21,15,23,28,24,0,20,26,25,20],
[25,26,24,33,31,27,30,0,33,32,28],
[19,23,16,20,24,20,24,17,0,24,16],
[17,20,19,25,27,20,25,18,26,0,19],
[26,28,24,30,27,25,30,22,34,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 46, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,20,26,31,28,27,25,28,23,26],
[24,0,12,20,21,20,22,23,23,19,20],
[30,38,0,26,29,25,28,36,26,28,27],
[24,30,24,0,31,29,29,33,23,27,21],
[19,29,21,19,0,30,25,20,28,19,24],
[22,30,25,21,20,0,25,22,30,27,25],
[23,28,22,21,25,25,0,27,21,21,27],
[25,27,14,17,30,28,23,0,27,29,28],
[22,27,24,27,22,20,29,23,0,17,26],
[27,31,22,23,31,23,29,21,33,0,30],
[24,30,23,29,26,25,23,22,24,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 47, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,29,29,28,31,21,23,23,28,33],
[19,0,24,34,20,30,22,29,29,30,32],
[21,26,0,29,23,29,26,31,26,33,33],
[21,16,21,0,19,26,21,19,25,21,27],
[22,30,27,31,0,30,25,28,27,30,34],
[19,20,21,24,20,0,22,22,23,27,28],
[29,28,24,29,25,28,0,27,26,29,36],
[27,21,19,31,22,28,23,0,28,21,28],
[27,21,24,25,23,27,24,22,0,25,34],
[22,20,17,29,20,23,21,29,25,0,27],
[17,18,17,23,16,22,14,22,16,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 48, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,23,25,23,26,24,25,25,20,18],
[22,0,21,24,27,29,23,26,26,17,20],
[27,29,0,33,29,28,27,29,25,21,24],
[25,26,17,0,19,28,21,23,22,15,16],
[27,23,21,31,0,25,21,23,21,19,20],
[24,21,22,22,25,0,18,27,22,21,20],
[26,27,23,29,29,32,0,28,27,22,26],
[25,24,21,27,27,23,22,0,27,17,21],
[25,24,25,28,29,28,23,23,0,21,19],
[30,33,29,35,31,29,28,33,29,0,25],
[32,30,26,34,30,30,24,29,31,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 49, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,29,26,23,27,20,29,28,18,20],
[25,0,33,31,33,33,25,33,30,20,27],
[21,17,0,27,18,37,18,32,33,19,28],
[24,19,23,0,11,23,22,20,21,20,22],
[27,17,32,39,0,35,23,30,36,25,26],
[23,17,13,27,15,0,17,29,13,20,20],
[30,25,32,28,27,33,0,40,30,26,25],
[21,17,18,30,20,21,10,0,22,20,19],
[22,20,17,29,14,37,20,28,0,23,26],
[32,30,31,30,25,30,24,30,27,0,28],
[30,23,22,28,24,30,25,31,24,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 50, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,21,15,19,21,21,22,23,29,22],
[27,0,23,24,22,23,25,30,21,32,19],
[29,27,0,24,27,27,30,27,25,26,23],
[35,26,26,0,25,29,28,27,28,34,23],
[31,28,23,25,0,28,25,28,26,30,27],
[29,27,23,21,22,0,22,29,23,29,19],
[29,25,20,22,25,28,0,23,20,26,23],
[28,20,23,23,22,21,27,0,23,30,17],
[27,29,25,22,24,27,30,27,0,25,26],
[21,18,24,16,20,21,24,20,25,0,21],
[28,31,27,27,23,31,27,33,24,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 51, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,15,12,9,20,22,17,16,14,11],
[26,0,26,16,16,18,21,18,18,15,21],
[35,24,0,22,20,25,24,23,27,22,26],
[38,34,28,0,11,36,19,28,28,27,35],
[41,34,30,39,0,41,25,29,33,34,36],
[30,32,25,14,9,0,24,17,18,32,26],
[28,29,26,31,25,26,0,22,28,29,29],
[33,32,27,22,21,33,28,0,28,30,31],
[34,32,23,22,17,32,22,22,0,21,26],
[36,35,28,23,16,18,21,20,29,0,33],
[39,29,24,15,14,24,21,19,24,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 52, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,25,24,33,19,31,31,25,27,27],
[26,0,25,26,25,27,31,29,24,32,25],
[25,25,0,25,26,21,24,32,22,30,26],
[26,24,25,0,26,24,28,26,19,24,23],
[17,25,24,24,0,18,27,28,19,27,24],
[31,23,29,26,32,0,28,34,24,34,24],
[19,19,26,22,23,22,0,29,18,27,18],
[19,21,18,24,22,16,21,0,14,25,16],
[25,26,28,31,31,26,32,36,0,29,26],
[23,18,20,26,23,16,23,25,21,0,16],
[23,25,24,27,26,26,32,34,24,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 53, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,23,25,21,24,24,21,21,24,19],
[31,0,26,28,22,28,29,27,26,26,34],
[27,24,0,32,18,25,27,19,31,29,31],
[25,22,18,0,19,25,22,20,22,23,24],
[29,28,32,31,0,24,30,29,21,19,31],
[26,22,25,25,26,0,18,20,28,22,23],
[26,21,23,28,20,32,0,25,29,24,26],
[29,23,31,30,21,30,25,0,25,24,36],
[29,24,19,28,29,22,21,25,0,23,25],
[26,24,21,27,31,28,26,26,27,0,31],
[31,16,19,26,19,27,24,14,25,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 54, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,28,25,18,21,26,26,21,23,22],
[25,0,27,27,21,24,23,24,23,25,24],
[22,23,0,27,19,21,22,24,24,21,19],
[25,23,23,0,17,21,22,26,25,20,19],
[32,29,31,33,0,25,28,36,31,24,25],
[29,26,29,29,25,0,29,31,29,27,23],
[24,27,28,28,22,21,0,23,22,27,27],
[24,26,26,24,14,19,27,0,21,23,22],
[29,27,26,25,19,21,28,29,0,20,24],
[27,25,29,30,26,23,23,27,30,0,27],
[28,26,31,31,25,27,23,28,26,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 55, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,29,25,27,28,24,26,25,33,22],
[18,0,24,15,21,25,22,20,19,18,19],
[21,26,0,19,19,27,21,22,24,28,18],
[25,35,31,0,20,29,24,25,27,22,26],
[23,29,31,30,0,28,23,21,29,26,26],
[22,25,23,21,22,0,19,21,20,22,25],
[26,28,29,26,27,31,0,23,24,30,22],
[24,30,28,25,29,29,27,0,30,25,22],
[25,31,26,23,21,30,26,20,0,24,19],
[17,32,22,28,24,28,20,25,26,0,21],
[28,31,32,24,24,25,28,28,31,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 56, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,26,27,23,24,28,28,25,21,23],
[24,0,25,27,29,24,26,25,28,23,24],
[24,25,0,22,25,26,21,24,23,20,21],
[23,23,28,0,15,19,23,29,25,23,18],
[27,21,25,35,0,23,20,24,25,23,19],
[26,26,24,31,27,0,28,30,27,20,27],
[22,24,29,27,30,22,0,25,29,25,25],
[22,25,26,21,26,20,25,0,22,25,21],
[25,22,27,25,25,23,21,28,0,20,25],
[29,27,30,27,27,30,25,25,30,0,24],
[27,26,29,32,31,23,25,29,25,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 57, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,28,20,30,23,27,29,25,29,19],
[17,0,11,18,30,17,25,28,20,19,15],
[22,39,0,29,36,28,33,32,30,28,26],
[30,32,21,0,34,22,19,27,25,22,16],
[20,20,14,16,0,9,9,24,10,17,14],
[27,33,22,28,41,0,25,34,22,31,20],
[23,25,17,31,41,25,0,29,25,34,23],
[21,22,18,23,26,16,21,0,16,21,11],
[25,30,20,25,40,28,25,34,0,27,25],
[21,31,22,28,33,19,16,29,23,0,16],
[31,35,24,34,36,30,27,39,25,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 58, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,25,32,22,25,24,32,28,26,23],
[29,0,30,34,25,26,28,40,30,27,27],
[25,20,0,30,21,30,26,31,29,22,26],
[18,16,20,0,21,21,20,28,19,19,22],
[28,25,29,29,0,20,25,29,29,33,25],
[25,24,20,29,30,0,26,35,29,27,32],
[26,22,24,30,25,24,0,30,30,24,28],
[18,10,19,22,21,15,20,0,22,19,25],
[22,20,21,31,21,21,20,28,0,25,21],
[24,23,28,31,17,23,26,31,25,0,25],
[27,23,24,28,25,18,22,25,29,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 59, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,22,32,31,32,24,26,34,34,30],
[16,0,22,27,36,24,22,17,37,26,28],
[28,28,0,31,37,25,30,35,33,27,33],
[18,23,19,0,31,32,14,20,27,37,14],
[19,14,13,19,0,29,16,18,26,24,12],
[18,26,25,18,21,0,11,11,21,24,19],
[26,28,20,36,34,39,0,19,25,36,22],
[24,33,15,30,32,39,31,0,38,32,31],
[16,13,17,23,24,29,25,12,0,26,23],
[16,24,23,13,26,26,14,18,24,0,20],
[20,22,17,36,38,31,28,19,27,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 60, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,23,33,26,23,27,24,22,20,26],
[24,0,29,32,27,21,28,27,24,19,27],
[27,21,0,28,25,17,24,28,23,21,24],
[17,18,22,0,21,17,20,21,21,18,17],
[24,23,25,29,0,22,25,25,23,22,23],
[27,29,33,33,28,0,28,29,28,21,26],
[23,22,26,30,25,22,0,24,20,20,24],
[26,23,22,29,25,21,26,0,22,20,24],
[28,26,27,29,27,22,30,28,0,26,28],
[30,31,29,32,28,29,30,30,24,0,28],
[24,23,26,33,27,24,26,26,22,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 61, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,20,20,29,32,26,30,24,19,23],
[28,0,21,27,26,23,31,30,34,24,25],
[30,29,0,25,32,31,26,30,31,24,21],
[30,23,25,0,34,31,34,31,34,24,27],
[21,24,18,16,0,24,21,31,27,20,22],
[18,27,19,19,26,0,31,28,28,23,17],
[24,19,24,16,29,19,0,28,25,13,23],
[20,20,20,19,19,22,22,0,21,20,16],
[26,16,19,16,23,22,25,29,0,26,25],
[31,26,26,26,30,27,37,30,24,0,25],
[27,25,29,23,28,33,27,34,25,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 62, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,31,22,23,19,31,27,27,35,27],
[24,0,24,19,13,24,28,20,24,28,16],
[19,26,0,26,31,20,27,22,27,28,30],
[28,31,24,0,31,16,27,35,35,39,20],
[27,37,19,19,0,20,20,30,33,35,15],
[31,26,30,34,30,0,20,30,26,27,27],
[19,22,23,23,30,30,0,30,34,39,23],
[23,30,28,15,20,20,20,0,35,36,17],
[23,26,23,15,17,24,16,15,0,24,8],
[15,22,22,11,15,23,11,14,26,0,18],
[23,34,20,30,35,23,27,33,42,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 63, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,29,22,23,13,23,20,22,25,27],
[32,0,27,33,25,19,36,28,27,25,30],
[21,23,0,14,19,13,20,14,13,15,21],
[28,17,36,0,33,23,35,24,31,27,34],
[27,25,31,17,0,19,26,16,15,19,17],
[37,31,37,27,31,0,28,24,27,21,30],
[27,14,30,15,24,22,0,15,24,18,21],
[30,22,36,26,34,26,35,0,30,24,35],
[28,23,37,19,35,23,26,20,0,18,24],
[25,25,35,23,31,29,32,26,32,0,32],
[23,20,29,16,33,20,29,15,26,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 64, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,29,23,31,34,36,27,33,36,31],
[18,0,18,23,22,26,22,26,28,29,18],
[21,32,0,19,25,30,25,30,30,29,25],
[27,27,31,0,32,31,37,30,29,23,25],
[19,28,25,18,0,30,26,30,26,22,20],
[16,24,20,19,20,0,26,23,19,20,23],
[14,28,25,13,24,24,0,26,30,22,10],
[23,24,20,20,20,27,24,0,26,29,27],
[17,22,20,21,24,31,20,24,0,17,13],
[14,21,21,27,28,30,28,21,33,0,17],
[19,32,25,25,30,27,40,23,37,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 65, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,23,21,16,29,24,23,21,25,24],
[30,0,30,28,26,30,24,25,22,28,24],
[27,20,0,27,26,31,25,26,28,27,25],
[29,22,23,0,23,28,27,26,22,22,21],
[34,24,24,27,0,30,23,23,25,25,23],
[21,20,19,22,20,0,18,18,19,24,16],
[26,26,25,23,27,32,0,29,30,26,21],
[27,25,24,24,27,32,21,0,29,24,23],
[29,28,22,28,25,31,20,21,0,24,17],
[25,22,23,28,25,26,24,26,26,0,25],
[26,26,25,29,27,34,29,27,33,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 66, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,27,29,27,27,17,27,29,31,22],
[21,0,27,24,27,25,24,34,31,26,26],
[23,23,0,29,27,20,19,29,23,27,20],
[21,26,21,0,26,24,23,26,26,27,19],
[23,23,23,24,0,26,20,28,28,23,20],
[23,25,30,26,24,0,26,30,26,29,21],
[33,26,31,27,30,24,0,34,27,25,24],
[23,16,21,24,22,20,16,0,25,27,28],
[21,19,27,24,22,24,23,25,0,26,22],
[19,24,23,23,27,21,25,23,24,0,24],
[28,24,30,31,30,29,26,22,28,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 67, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,25,22,25,21,27,26,24,20,19],
[24,0,25,26,24,24,30,32,23,26,27],
[25,25,0,22,26,28,32,32,30,25,28],
[28,24,28,0,26,24,28,28,25,24,25],
[25,26,24,24,0,24,31,30,26,22,26],
[29,26,22,26,26,0,29,31,27,24,29],
[23,20,18,22,19,21,0,25,23,22,20],
[24,18,18,22,20,19,25,0,23,19,22],
[26,27,20,25,24,23,27,27,0,25,22],
[30,24,25,26,28,26,28,31,25,0,26],
[31,23,22,25,24,21,30,28,28,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 68, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,28,19,23,25,21,29,27,28,21],
[29,0,26,29,31,26,28,24,32,30,23],
[22,24,0,19,15,22,20,31,18,27,16],
[31,21,31,0,21,26,29,29,28,37,24],
[27,19,35,29,0,30,26,37,21,35,22],
[25,24,28,24,20,0,23,30,26,25,20],
[29,22,30,21,24,27,0,26,23,30,24],
[21,26,19,21,13,20,24,0,21,26,24],
[23,18,32,22,29,24,27,29,0,35,26],
[22,20,23,13,15,25,20,24,15,0,21],
[29,27,34,26,28,30,26,26,24,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 69, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,27,35,18,33,25,28,29,20,21],
[25,0,22,28,26,30,29,23,25,24,25],
[23,28,0,31,17,36,32,28,30,30,28],
[15,22,19,0,21,33,27,30,26,18,29],
[32,24,33,29,0,37,33,32,32,27,36],
[17,20,14,17,13,0,25,20,24,18,27],
[25,21,18,23,17,25,0,24,23,19,24],
[22,27,22,20,18,30,26,0,21,20,20],
[21,25,20,24,18,26,27,29,0,22,27],
[30,26,20,32,23,32,31,30,28,0,28],
[29,25,22,21,14,23,26,30,23,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 70, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,26,26,25,25,26,21,23,21,21],
[28,0,28,25,33,26,29,22,28,24,23],
[24,22,0,22,24,28,18,19,19,21,23],
[24,25,28,0,25,25,24,21,26,21,21],
[25,17,26,25,0,26,25,12,23,22,24],
[25,24,22,25,24,0,22,20,23,25,25],
[24,21,32,26,25,28,0,27,27,22,18],
[29,28,31,29,38,30,23,0,29,25,29],
[27,22,31,24,27,27,23,21,0,27,22],
[29,26,29,29,28,25,28,25,23,0,19],
[29,27,27,29,26,25,32,21,28,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 71, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,29,17,16,11,27,9,32,28,24],
[28,0,25,18,18,18,24,24,28,30,32],
[21,25,0,13,20,14,25,19,32,31,15],
[33,32,37,0,19,27,34,29,38,35,39],
[34,32,30,31,0,17,27,24,31,34,38],
[39,32,36,23,33,0,36,24,33,34,38],
[23,26,25,16,23,14,0,15,23,35,23],
[41,26,31,21,26,26,35,0,32,30,29],
[18,22,18,12,19,17,27,18,0,29,18],
[22,20,19,15,16,16,15,20,21,0,23],
[26,18,35,11,12,12,27,21,32,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 72, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,31,14,12,19,18,20,13,26,15],
[37,0,37,28,21,24,29,25,35,34,32],
[19,13,0,11,20,24,19,18,18,21,17],
[36,22,39,0,24,19,19,24,12,40,17],
[38,29,30,26,0,19,18,20,32,29,16],
[31,26,26,31,31,0,17,31,33,35,23],
[32,21,31,31,32,33,0,20,27,35,25],
[30,25,32,26,30,19,30,0,27,35,21],
[37,15,32,38,18,17,23,23,0,33,21],
[24,16,29,10,21,15,15,15,17,0,18],
[35,18,33,33,34,27,25,29,29,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 73, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,31,35,36,40,27,44,31,25,28],
[15,0,26,15,20,16,15,11,11,16,16],
[19,24,0,23,23,28,7,19,23,8,28],
[15,35,27,0,23,15,10,19,4,15,11],
[14,30,27,27,0,23,23,17,20,13,20],
[10,34,22,35,27,0,23,17,20,12,19],
[23,35,43,40,27,27,0,30,33,21,30],
[6,39,31,31,33,33,20,0,24,25,32],
[19,39,27,46,30,30,17,26,0,19,30],
[25,34,42,35,37,38,29,25,31,0,34],
[22,34,22,39,30,31,20,18,20,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 74, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,22,25,21,27,26,20,37,28,20],
[24,0,29,21,23,22,23,19,30,20,21],
[28,21,0,24,26,28,28,23,30,26,25],
[25,29,26,0,26,28,30,27,38,22,23],
[29,27,24,24,0,28,28,26,35,21,28],
[23,28,22,22,22,0,30,27,38,21,23],
[24,27,22,20,22,20,0,20,36,21,21],
[30,31,27,23,24,23,30,0,37,29,24],
[13,20,20,12,15,12,14,13,0,21,17],
[22,30,24,28,29,29,29,21,29,0,23],
[30,29,25,27,22,27,29,26,33,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 75, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,21,33,24,26,26,28,27,31,30],
[24,0,25,26,21,22,28,35,25,33,30],
[29,25,0,22,25,17,33,25,24,28,28],
[17,24,28,0,25,24,31,24,30,26,27],
[26,29,25,25,0,25,27,25,31,25,25],
[24,28,33,26,25,0,34,28,24,25,32],
[24,22,17,19,23,16,0,29,24,26,27],
[22,15,25,26,25,22,21,0,23,21,26],
[23,25,26,20,19,26,26,27,0,28,30],
[19,17,22,24,25,25,24,29,22,0,24],
[20,20,22,23,25,18,23,24,20,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 76, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,29,20,12,14,22,20,12,13,12],
[43,0,44,28,42,34,36,50,36,21,49],
[21,6,0,13,21,13,21,29,6,6,6],
[30,22,37,0,42,28,36,43,21,27,27],
[38,8,29,8,0,8,23,29,1,8,14],
[36,16,37,22,42,0,36,28,36,22,27],
[28,14,29,14,27,14,0,20,6,7,19],
[30,0,21,7,21,22,30,0,21,21,15],
[38,14,44,29,49,14,44,29,0,14,13],
[37,29,44,23,42,28,43,29,36,0,43],
[38,1,44,23,36,23,31,35,37,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 77, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,30,35,29,26,26,34,28,24,32],
[22,0,25,35,28,24,19,23,20,26,37],
[20,25,0,32,25,25,27,28,27,21,31],
[15,15,18,0,21,17,12,24,9,14,21],
[21,22,25,29,0,22,21,22,21,25,29],
[24,26,25,33,28,0,26,29,20,18,32],
[24,31,23,38,29,24,0,32,22,22,36],
[16,27,22,26,28,21,18,0,21,23,32],
[22,30,23,41,29,30,28,29,0,24,35],
[26,24,29,36,25,32,28,27,26,0,31],
[18,13,19,29,21,18,14,18,15,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 78, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,24,26,21,26,28,26,23,30,26],
[28,0,32,25,30,27,33,29,28,31,31],
[26,18,0,25,24,22,30,28,23,30,27],
[24,25,25,0,25,23,24,28,24,32,24],
[29,20,26,25,0,29,28,30,27,33,28],
[24,23,28,27,21,0,23,26,25,31,24],
[22,17,20,26,22,27,0,25,25,31,28],
[24,21,22,22,20,24,25,0,19,23,25],
[27,22,27,26,23,25,25,31,0,28,24],
[20,19,20,18,17,19,19,27,22,0,23],
[24,19,23,26,22,26,22,25,26,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 79, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,24,32,28,30,26,28,25,25,22],
[30,0,21,23,23,29,26,25,26,21,23],
[26,29,0,30,35,30,32,39,26,22,26],
[18,27,20,0,24,27,24,32,28,27,25],
[22,27,15,26,0,24,24,24,28,21,17],
[20,21,20,23,26,0,24,28,23,24,22],
[24,24,18,26,26,26,0,28,22,20,26],
[22,25,11,18,26,22,22,0,17,15,19],
[25,24,24,22,22,27,28,33,0,20,21],
[25,29,28,23,29,26,30,35,30,0,26],
[28,27,24,25,33,28,24,31,29,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 80, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,27,27,27,25,25,22,23,26,22],
[22,0,19,21,22,26,22,20,19,23,25],
[23,31,0,28,29,31,26,24,25,30,28],
[23,29,22,0,27,23,24,17,27,25,23],
[23,28,21,23,0,24,21,20,25,26,21],
[25,24,19,27,26,0,26,20,22,24,21],
[25,28,24,26,29,24,0,16,30,23,20],
[28,30,26,33,30,30,34,0,29,25,26],
[27,31,25,23,25,28,20,21,0,24,23],
[24,27,20,25,24,26,27,25,26,0,20],
[28,25,22,27,29,29,30,24,27,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 81, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,19,28,27,23,26,23,28,30,23],
[19,0,18,19,22,20,21,16,20,22,16],
[31,32,0,29,21,23,20,19,25,29,22],
[22,31,21,0,30,17,24,20,24,24,17],
[23,28,29,20,0,26,26,22,22,25,19],
[27,30,27,33,24,0,24,26,27,32,24],
[24,29,30,26,24,26,0,24,29,29,23],
[27,34,31,30,28,24,26,0,29,32,31],
[22,30,25,26,28,23,21,21,0,26,22],
[20,28,21,26,25,18,21,18,24,0,20],
[27,34,28,33,31,26,27,19,28,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 82, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,8,23,13,24,29,17,26,20,26],
[29,0,25,22,29,25,31,21,32,30,25],
[42,25,0,30,37,29,28,39,38,30,42],
[27,28,20,0,28,32,33,33,38,24,38],
[37,21,13,22,0,24,28,32,31,23,24],
[26,25,21,18,26,0,31,22,33,18,21],
[21,19,22,17,22,19,0,27,35,17,32],
[33,29,11,17,18,28,23,0,34,28,24],
[24,18,12,12,19,17,15,16,0,17,21],
[30,20,20,26,27,32,33,22,33,0,29],
[24,25,8,12,26,29,18,26,29,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 83, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,18,12,33,21,21,12,23,22,18],
[32,0,20,18,34,26,26,22,23,28,20],
[32,30,0,27,34,38,28,33,36,21,25],
[38,32,23,0,40,29,32,25,32,22,27],
[17,16,16,10,0,22,11,16,17,13,15],
[29,24,12,21,28,0,20,19,24,16,21],
[29,24,22,18,39,30,0,30,29,15,25],
[38,28,17,25,34,31,20,0,26,26,23],
[27,27,14,18,33,26,21,24,0,14,27],
[28,22,29,28,37,34,35,24,36,0,26],
[32,30,25,23,35,29,25,27,23,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 84, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,27,23,29,28,25,20,27,28,28],
[26,0,20,28,22,25,32,23,23,25,28],
[23,30,0,24,29,30,31,26,25,22,35],
[27,22,26,0,21,30,29,23,26,19,32],
[21,28,21,29,0,30,27,20,24,19,30],
[22,25,20,20,20,0,20,14,20,22,26],
[25,18,19,21,23,30,0,27,25,19,30],
[30,27,24,27,30,36,23,0,29,29,31],
[23,27,25,24,26,30,25,21,0,23,25],
[22,25,28,31,31,28,31,21,27,0,26],
[22,22,15,18,20,24,20,19,25,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 85, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,21,16,9,21,21,28,16,17,18],
[27,0,35,22,24,25,25,40,17,18,36],
[29,15,0,17,17,10,20,29,9,8,9],
[34,28,33,0,30,24,32,39,14,12,29],
[41,26,33,20,0,24,24,38,27,19,28],
[29,25,40,26,26,0,29,39,26,26,29],
[29,25,30,18,26,21,0,38,16,9,26],
[22,10,21,11,12,11,12,0,16,9,24],
[34,33,41,36,23,24,34,34,0,21,26],
[33,32,42,38,31,24,41,41,29,0,36],
[32,14,41,21,22,21,24,26,24,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 86, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,39,29,17,36,36,30,37,25,26],
[22,0,21,29,15,29,17,26,17,24,24],
[11,29,0,25,23,18,29,37,40,25,26],
[21,21,25,0,21,24,28,30,32,16,27],
[33,35,27,29,0,32,31,43,43,25,29],
[14,21,32,26,18,0,35,24,35,23,22],
[14,33,21,22,19,15,0,27,34,16,14],
[20,24,13,20,7,26,23,0,29,12,15],
[13,33,10,18,7,15,16,21,0,13,11],
[25,26,25,34,25,27,34,38,37,0,24],
[24,26,24,23,21,28,36,35,39,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 87, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,29,25,29,33,25,27,27,29,29],
[26,0,26,34,30,36,27,24,33,36,30],
[21,24,0,23,20,28,20,23,25,34,33],
[25,16,27,0,23,33,25,24,19,27,29],
[21,20,30,27,0,30,22,24,28,34,39],
[17,14,22,17,20,0,22,23,20,24,16],
[25,23,30,25,28,28,0,18,22,22,28],
[23,26,27,26,26,27,32,0,29,31,22],
[23,17,25,31,22,30,28,21,0,23,26],
[21,14,16,23,16,26,28,19,27,0,19],
[21,20,17,21,11,34,22,28,24,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 88, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,19,19,20,36,14,30,9,1,11],
[22,0,18,8,19,36,18,30,18,8,19],
[31,32,0,18,24,46,20,40,15,15,16],
[31,42,32,0,34,46,26,40,25,11,22],
[30,31,26,16,0,35,26,46,21,11,10],
[14,14,4,4,15,0,4,34,4,4,4],
[36,32,30,24,24,46,0,30,13,11,12],
[20,20,10,10,4,16,20,0,4,10,0],
[41,32,35,25,29,46,37,46,0,28,11],
[49,42,35,39,39,46,39,40,22,0,25],
[39,31,34,28,40,46,38,50,39,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 89, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,30,26,20,31,22,24,32,28,27],
[18,0,25,22,15,24,18,23,25,22,25],
[20,25,0,22,23,25,20,22,24,23,28],
[24,28,28,0,25,26,21,25,28,22,30],
[30,35,27,25,0,32,22,25,26,30,29],
[19,26,25,24,18,0,24,24,29,23,19],
[28,32,30,29,28,26,0,31,31,23,29],
[26,27,28,25,25,26,19,0,24,16,30],
[18,25,26,22,24,21,19,26,0,19,30],
[22,28,27,28,20,27,27,34,31,0,29],
[23,25,22,20,21,31,21,20,20,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 90, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,26,24,21,27,25,24,26,30,30],
[25,0,28,23,30,31,29,28,27,31,32],
[24,22,0,18,24,26,22,19,19,23,27],
[26,27,32,0,27,27,25,27,28,31,31],
[29,20,26,23,0,28,24,26,22,29,29],
[23,19,24,23,22,0,24,23,20,31,27],
[25,21,28,25,26,26,0,29,25,31,28],
[26,22,31,23,24,27,21,0,26,28,26],
[24,23,31,22,28,30,25,24,0,26,30],
[20,19,27,19,21,19,19,22,24,0,27],
[20,18,23,19,21,23,22,24,20,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 91, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,20,11,8,19,8,18,17,7,11],
[50,0,20,23,20,35,32,42,31,24,23],
[30,30,0,18,12,37,12,29,24,30,29],
[39,27,32,0,27,39,16,38,33,27,30],
[42,30,38,23,0,37,30,41,30,37,34],
[31,15,13,11,13,0,13,42,32,8,22],
[42,18,38,34,20,37,0,36,36,37,22],
[32,8,21,12,9,8,14,0,13,8,23],
[33,19,26,17,20,18,14,37,0,18,17],
[43,26,20,23,13,42,13,42,32,0,22],
[39,27,21,20,16,28,28,27,33,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 92, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,30,33,27,21,28,30,32,28,29],
[19,0,23,25,28,21,27,17,29,27,24],
[20,27,0,28,28,30,32,28,29,23,14],
[17,25,22,0,24,19,31,36,32,31,34],
[23,22,22,26,0,19,26,24,27,22,25],
[29,29,20,31,31,0,33,32,33,27,30],
[22,23,18,19,24,17,0,27,25,21,20],
[20,33,22,14,26,18,23,0,26,23,27],
[18,21,21,18,23,17,25,24,0,32,21],
[22,23,27,19,28,23,29,27,18,0,20],
[21,26,36,16,25,20,30,23,29,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 93, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,31,0,0,0,11,0,20,20,20],
[19,0,50,19,0,0,11,0,20,20,20],
[19,0,0,19,0,0,11,0,20,20,20],
[50,31,31,0,31,31,31,11,31,31,31],
[50,50,50,19,0,31,31,11,31,20,31],
[50,50,50,19,19,0,30,30,50,39,50],
[39,39,39,19,19,20,0,0,20,20,20],
[50,50,50,39,39,20,50,0,50,39,50],
[30,30,30,19,19,0,30,0,0,39,30],
[30,30,30,19,30,11,30,11,11,0,30],
[30,30,30,19,19,0,30,0,20,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 94, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,28,24,24,24,28,22,27,28,28],
[29,0,26,22,21,27,28,24,20,32,27],
[22,24,0,19,18,23,19,16,17,21,22],
[26,28,31,0,29,33,23,21,22,31,30],
[26,29,32,21,0,30,26,25,24,30,29],
[26,23,27,17,20,0,22,20,21,22,21],
[22,22,31,27,24,28,0,18,18,32,24],
[28,26,34,29,25,30,32,0,28,35,34],
[23,30,33,28,26,29,32,22,0,33,33],
[22,18,29,19,20,28,18,15,17,0,23],
[22,23,28,20,21,29,26,16,17,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 95, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,31,30,24,26,18,25,23,20,28],
[21,0,19,22,18,15,13,16,16,18,17],
[19,31,0,27,24,21,12,20,25,19,10],
[20,28,23,0,16,15,20,24,26,19,13],
[26,32,26,34,0,19,20,29,25,22,15],
[24,35,29,35,31,0,19,25,26,25,23],
[32,37,38,30,30,31,0,28,34,24,30],
[25,34,30,26,21,25,22,0,19,17,25],
[27,34,25,24,25,24,16,31,0,13,16],
[30,32,31,31,28,25,26,33,37,0,26],
[22,33,40,37,35,27,20,25,34,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 96, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,30,36,33,18,19,22,33,28,31],
[24,0,28,30,32,15,23,21,25,22,25],
[20,22,0,32,28,28,28,19,32,21,23],
[14,20,18,0,30,22,16,20,33,14,25],
[17,18,22,20,0,18,14,21,30,14,25],
[32,35,22,28,32,0,24,26,36,26,26],
[31,27,22,34,36,26,0,25,40,25,27],
[28,29,31,30,29,24,25,0,39,30,25],
[17,25,18,17,20,14,10,11,0,10,21],
[22,28,29,36,36,24,25,20,40,0,27],
[19,25,27,25,25,24,23,25,29,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 97, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,23,10,17,23,14,21,33,50,21],
[29,0,29,29,46,23,33,19,29,33,40],
[27,21,0,10,27,21,31,17,14,31,21],
[40,21,40,0,17,40,21,21,23,40,40],
[33,4,23,33,0,23,33,23,33,33,23],
[27,27,29,10,27,0,10,27,10,50,17],
[36,17,19,29,17,40,0,36,29,50,40],
[29,31,33,29,27,23,14,0,33,33,40],
[17,21,36,27,17,40,21,17,0,40,21],
[0,17,19,10,17,0,0,17,10,0,17],
[29,10,29,10,27,33,10,10,29,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 98, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,23,21,20,20,27,22,29,30,34],
[26,0,28,20,28,23,21,24,32,29,36],
[27,22,0,18,27,21,18,23,26,33,30],
[29,30,32,0,26,29,20,30,26,33,35],
[30,22,23,24,0,23,22,26,30,31,33],
[30,27,29,21,27,0,21,31,29,32,36],
[23,29,32,30,28,29,0,30,36,25,37],
[28,26,27,20,24,19,20,0,33,32,38],
[21,18,24,24,20,21,14,17,0,23,25],
[20,21,17,17,19,18,25,18,27,0,29],
[16,14,20,15,17,14,13,12,25,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 99, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,31,30,29,27,35,21,31,30,24],
[21,0,26,30,25,28,19,20,28,20,24],
[19,24,0,33,26,28,28,23,31,22,26],
[20,20,17,0,23,28,24,20,32,23,25],
[21,25,24,27,0,30,28,25,27,25,25],
[23,22,22,22,20,0,27,22,22,22,21],
[15,31,22,26,22,23,0,18,30,24,23],
[29,30,27,30,25,28,32,0,35,35,25],
[19,22,19,18,23,28,20,15,0,18,26],
[20,30,28,27,25,28,26,15,32,0,23],
[26,26,24,25,25,29,27,25,24,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 100, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,21,31,21,28,29,32,29,27,34],
[24,0,24,24,27,31,32,29,27,31,36],
[29,26,0,34,22,28,37,25,25,26,24],
[19,26,16,0,19,25,23,20,28,23,29],
[29,23,28,31,0,27,35,27,19,29,32],
[22,19,22,25,23,0,35,27,17,28,32],
[21,18,13,27,15,15,0,16,17,19,26],
[18,21,25,30,23,23,34,0,22,25,33],
[21,23,25,22,31,33,33,28,0,20,26],
[23,19,24,27,21,22,31,25,30,0,38],
[16,14,26,21,18,18,24,17,24,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 101, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,40,31,40,41,49,31,41,27,41],
[36,0,27,27,37,27,39,36,28,13,27],
[10,23,0,24,24,25,49,24,24,1,15],
[19,23,26,0,24,37,49,37,41,11,27],
[10,13,26,26,0,37,40,30,27,26,26],
[9,23,25,13,13,0,39,27,13,13,13],
[1,11,1,1,10,11,0,1,1,1,1],
[19,14,26,13,20,23,49,0,27,13,13],
[9,22,26,9,23,37,49,23,0,0,3],
[23,37,49,39,24,37,49,37,50,0,39],
[9,23,35,23,24,37,49,37,47,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 102, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,27,31,32,23,26,22,27,30,23],
[25,0,24,30,30,26,25,28,30,29,22],
[23,26,0,32,33,25,27,24,30,25,26],
[19,20,18,0,25,20,24,25,25,22,18],
[18,20,17,25,0,18,22,20,29,26,22],
[27,24,25,30,32,0,27,29,25,23,24],
[24,25,23,26,28,23,0,22,24,29,23],
[28,22,26,25,30,21,28,0,28,27,24],
[23,20,20,25,21,25,26,22,0,20,19],
[20,21,25,28,24,27,21,23,30,0,22],
[27,28,24,32,28,26,27,26,31,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 103, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,18,19,25,26,20,21,18,17,17],
[25,0,17,21,22,24,25,24,26,21,18],
[32,33,0,26,29,34,32,26,29,24,25],
[31,29,24,0,27,31,28,27,23,22,25],
[25,28,21,23,0,28,32,24,26,26,23],
[24,26,16,19,22,0,24,19,19,17,14],
[30,25,18,22,18,26,0,24,22,19,21],
[29,26,24,23,26,31,26,0,29,24,26],
[32,24,21,27,24,31,28,21,0,18,24],
[33,29,26,28,24,33,31,26,32,0,25],
[33,32,25,25,27,36,29,24,26,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 104, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,30,23,32,23,39,28,23,34,29],
[25,0,28,16,21,22,29,32,31,25,30],
[20,22,0,6,19,27,21,27,24,36,15],
[27,34,44,0,39,34,25,26,36,39,25],
[18,29,31,11,0,36,22,24,32,37,21],
[27,28,23,16,14,0,23,18,24,26,16],
[11,21,29,25,28,27,0,23,21,19,17],
[22,18,23,24,26,32,27,0,31,31,32],
[27,19,26,14,18,26,29,19,0,27,15],
[16,25,14,11,13,24,31,19,23,0,20],
[21,20,35,25,29,34,33,18,35,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 105, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,18,12,18,18,18,21,17,16,21],
[38,0,32,23,29,31,28,34,32,31,30],
[32,18,0,23,22,26,27,23,24,26,29],
[38,27,27,0,28,29,20,24,30,25,30],
[32,21,28,22,0,24,26,19,22,25,24],
[32,19,24,21,26,0,27,24,22,24,26],
[32,22,23,30,24,23,0,22,26,26,29],
[29,16,27,26,31,26,28,0,29,29,29],
[33,18,26,20,28,28,24,21,0,29,26],
[34,19,24,25,25,26,24,21,21,0,26],
[29,20,21,20,26,24,21,21,24,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 106, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,32,35,32,28,28,30,33,23,27],
[24,0,28,28,32,31,25,25,33,24,23],
[18,22,0,27,27,21,18,17,25,25,26],
[15,22,23,0,24,24,19,21,24,19,18],
[18,18,23,26,0,22,20,26,25,23,29],
[22,19,29,26,28,0,20,24,25,21,25],
[22,25,32,31,30,30,0,23,29,25,25],
[20,25,33,29,24,26,27,0,30,24,27],
[17,17,25,26,25,25,21,20,0,22,25],
[27,26,25,31,27,29,25,26,28,0,28],
[23,27,24,32,21,25,25,23,25,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 107, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,27,15,27,20,14,27,19,19,24],
[30,0,32,21,28,26,28,27,24,28,31],
[23,18,0,22,17,17,23,17,22,13,33],
[35,29,28,0,28,24,29,26,23,27,29],
[23,22,33,22,0,25,24,30,24,30,26],
[30,24,33,26,25,0,24,28,27,23,29],
[36,22,27,21,26,26,0,29,26,23,24],
[23,23,33,24,20,22,21,0,21,22,26],
[31,26,28,27,26,23,24,29,0,25,24],
[31,22,37,23,20,27,27,28,25,0,35],
[26,19,17,21,24,21,26,24,26,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 108, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,31,29,31,27,23,33,26,19,17],
[29,0,31,35,33,22,23,30,31,21,26],
[19,19,0,17,32,21,11,27,25,13,14],
[21,15,33,0,27,22,25,33,29,19,19],
[19,17,18,23,0,21,20,26,30,13,11],
[23,28,29,28,29,0,19,30,34,25,18],
[27,27,39,25,30,31,0,32,35,21,22],
[17,20,23,17,24,20,18,0,28,17,15],
[24,19,25,21,20,16,15,22,0,14,6],
[31,29,37,31,37,25,29,33,36,0,23],
[33,24,36,31,39,32,28,35,44,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 109, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,22,22,25,23,20,18,18,31,34],
[23,0,26,23,22,21,23,19,17,26,32],
[28,24,0,20,28,30,32,27,23,34,34],
[28,27,30,0,18,22,20,21,19,35,34],
[25,28,22,32,0,25,27,26,22,36,36],
[27,29,20,28,25,0,24,29,26,40,38],
[30,27,18,30,23,26,0,28,18,36,35],
[32,31,23,29,24,21,22,0,18,31,34],
[32,33,27,31,28,24,32,32,0,38,40],
[19,24,16,15,14,10,14,19,12,0,28],
[16,18,16,16,14,12,15,16,10,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 110, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,15,13,15,6,26,25,38,28,15],
[22,0,35,26,21,26,47,15,35,39,22],
[35,15,0,25,26,13,37,25,50,40,15],
[37,24,25,0,24,6,28,38,35,39,24],
[35,29,24,26,0,5,48,28,39,50,14],
[44,24,37,44,45,0,43,34,46,46,25],
[24,3,13,22,2,7,0,13,24,37,3],
[25,35,25,12,22,16,37,0,44,36,21],
[12,15,0,15,11,4,26,6,0,40,11],
[22,11,10,11,0,4,13,14,10,0,0],
[35,28,35,26,36,25,47,29,39,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 111, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,22,28,33,33,28,23,25,23,15],
[20,0,23,30,31,26,27,19,15,26,17],
[28,27,0,33,34,30,27,27,27,22,21],
[22,20,17,0,27,25,27,20,23,19,16],
[17,19,16,23,0,23,27,21,22,26,19],
[17,24,20,25,27,0,28,24,22,28,20],
[22,23,23,23,23,22,0,26,20,23,22],
[27,31,23,30,29,26,24,0,28,31,28],
[25,35,23,27,28,28,30,22,0,23,21],
[27,24,28,31,24,22,27,19,27,0,18],
[35,33,29,34,31,30,28,22,29,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 112, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,13,8,24,17,8,23,20,20,9],
[38,0,35,22,30,25,16,23,20,14,34],
[37,15,0,14,19,22,15,19,24,15,15],
[42,28,36,0,33,22,28,34,38,34,31],
[26,20,31,17,0,19,21,29,33,20,25],
[33,25,28,28,31,0,17,36,30,32,23],
[42,34,35,22,29,33,0,31,28,21,27],
[27,27,31,16,21,14,19,0,18,12,29],
[30,30,26,12,17,20,22,32,0,16,27],
[30,36,35,16,30,18,29,38,34,0,35],
[41,16,35,19,25,27,23,21,23,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 113, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,22,26,21,22,26,24,24,26,19],
[26,0,26,28,23,27,20,27,25,26,20],
[28,24,0,23,24,22,21,22,19,22,21],
[24,22,27,0,16,16,23,22,20,17,14],
[29,27,26,34,0,24,25,28,16,29,15],
[28,23,28,34,26,0,25,28,23,30,22],
[24,30,29,27,25,25,0,28,21,24,23],
[26,23,28,28,22,22,22,0,19,21,19],
[26,25,31,30,34,27,29,31,0,30,25],
[24,24,28,33,21,20,26,29,20,0,19],
[31,30,29,36,35,28,27,31,25,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 114, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,27,20,15,12,18,14,12,15,16],
[36,0,35,32,24,22,25,24,21,19,21],
[23,15,0,20,17,11,12,13,18,17,12],
[30,18,30,0,21,18,21,16,15,10,19],
[35,26,33,29,0,18,32,20,23,27,27],
[38,28,39,32,32,0,28,28,25,27,25],
[32,25,38,29,18,22,0,22,18,26,17],
[36,26,37,34,30,22,28,0,27,19,26],
[38,29,32,35,27,25,32,23,0,28,30],
[35,31,33,40,23,23,24,31,22,0,23],
[34,29,38,31,23,25,33,24,20,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 115, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,26,25,22,26,18,27,19,27,21],
[24,0,25,28,23,26,16,24,26,26,20],
[24,25,0,25,25,29,22,29,22,24,24],
[25,22,25,0,25,26,25,28,22,27,24],
[28,27,25,25,0,25,20,27,22,26,19],
[24,24,21,24,25,0,19,25,24,24,24],
[32,34,28,25,30,31,0,26,24,26,25],
[23,26,21,22,23,25,24,0,23,27,24],
[31,24,28,28,28,26,26,27,0,24,22],
[23,24,26,23,24,26,24,23,26,0,24],
[29,30,26,26,31,26,25,26,28,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 116, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,29,28,23,26,30,25,25,30,34],
[25,0,25,27,30,24,28,23,29,30,34],
[21,25,0,24,25,23,23,20,25,29,33],
[22,23,26,0,24,27,25,24,26,25,34],
[27,20,25,26,0,24,24,20,20,24,34],
[24,26,27,23,26,0,24,22,23,26,33],
[20,22,27,25,26,26,0,24,25,24,31],
[25,27,30,26,30,28,26,0,30,31,34],
[25,21,25,24,30,27,25,20,0,27,30],
[20,20,21,25,26,24,26,19,23,0,33],
[16,16,17,16,16,17,19,16,20,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 117, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,20,17,22,24,24,24,25,27,25],
[32,0,27,24,28,29,29,26,25,29,26],
[30,23,0,21,33,25,26,23,28,30,23],
[33,26,29,0,31,27,29,23,28,32,26],
[28,22,17,19,0,27,20,24,26,28,21],
[26,21,25,23,23,0,18,26,25,28,26],
[26,21,24,21,30,32,0,29,27,30,28],
[26,24,27,27,26,24,21,0,32,29,27],
[25,25,22,22,24,25,23,18,0,31,23],
[23,21,20,18,22,22,20,21,19,0,26],
[25,24,27,24,29,24,22,23,27,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 118, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,30,24,20,30,29,28,41,17,21],
[20,0,28,20,18,27,25,22,23,19,24],
[20,22,0,25,21,25,33,25,26,21,25],
[26,30,25,0,29,17,30,30,29,20,24],
[30,32,29,21,0,20,30,29,33,13,20],
[20,23,25,33,30,0,34,31,30,29,23],
[21,25,17,20,20,16,0,22,22,12,21],
[22,28,25,20,21,19,28,0,29,18,22],
[9,27,24,21,17,20,28,21,0,18,17],
[33,31,29,30,37,21,38,32,32,0,31],
[29,26,25,26,30,27,29,28,33,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 119, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,28,24,19,22,11,15,20,23,30],
[36,0,32,29,30,31,25,27,23,36,42],
[22,18,0,21,21,28,15,18,24,24,33],
[26,21,29,0,27,28,19,19,25,31,32],
[31,20,29,23,0,28,17,19,23,23,33],
[28,19,22,22,22,0,24,25,25,26,30],
[39,25,35,31,33,26,0,34,26,32,32],
[35,23,32,31,31,25,16,0,27,29,36],
[30,27,26,25,27,25,24,23,0,32,35],
[27,14,26,19,27,24,18,21,18,0,32],
[20,8,17,18,17,20,18,14,15,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 120, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,23,21,22,23,21,25,21,19,19],
[34,0,31,28,33,30,30,24,22,26,27],
[27,19,0,27,31,32,28,28,24,28,25],
[29,22,23,0,25,26,23,23,26,22,21],
[28,17,19,25,0,25,27,25,25,20,20],
[27,20,18,24,25,0,24,23,24,27,20],
[29,20,22,27,23,26,0,21,25,27,21],
[25,26,22,27,25,27,29,0,24,26,21],
[29,28,26,24,25,26,25,26,0,25,22],
[31,24,22,28,30,23,23,24,25,0,21],
[31,23,25,29,30,30,29,29,28,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 121, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,21,36,30,30,32,27,18,29,30],
[19,0,27,36,24,30,36,18,24,30,24],
[29,23,0,30,26,34,39,33,27,26,26],
[14,14,20,0,16,20,26,18,20,20,21],
[20,26,24,34,0,28,39,33,27,31,31],
[20,20,16,30,22,0,25,24,18,15,32],
[18,14,11,24,11,25,0,21,16,22,19],
[23,32,17,32,17,26,29,0,19,21,24],
[32,26,23,30,23,32,34,31,0,30,31],
[21,20,24,30,19,35,28,29,20,0,38],
[20,26,24,29,19,18,31,26,19,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 122, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,28,34,28,24,27,24,29,23,26],
[24,0,25,27,19,23,23,28,26,24,24],
[22,25,0,24,25,22,23,23,23,23,23],
[16,23,26,0,18,20,22,23,21,18,22],
[22,31,25,32,0,22,27,30,25,25,29],
[26,27,28,30,28,0,29,28,25,27,27],
[23,27,27,28,23,21,0,25,25,24,25],
[26,22,27,27,20,22,25,0,25,22,23],
[21,24,27,29,25,25,25,25,0,27,24],
[27,26,27,32,25,23,26,28,23,0,26],
[24,26,27,28,21,23,25,27,26,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 123, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,29,35,27,24,32,26,30,28,30],
[20,0,23,26,20,22,24,21,25,23,21],
[21,27,0,24,23,21,28,24,25,27,25],
[15,24,26,0,21,20,28,26,26,21,25],
[23,30,27,29,0,26,34,29,32,25,29],
[26,28,29,30,24,0,26,31,30,30,27],
[18,26,22,22,16,24,0,22,28,21,25],
[24,29,26,24,21,19,28,0,25,26,27],
[20,25,25,24,18,20,22,25,0,25,22],
[22,27,23,29,25,20,29,24,25,0,22],
[20,29,25,25,21,23,25,23,28,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 124, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,15,18,12,18,12,12,18,18,12],
[29,0,23,34,25,21,32,30,38,34,25],
[35,27,0,27,25,18,18,26,18,31,26],
[32,16,23,0,34,13,24,28,4,31,15],
[38,25,25,16,0,27,21,18,18,32,16],
[32,29,32,37,23,0,33,33,41,37,20],
[38,18,32,26,29,17,0,28,25,35,28],
[38,20,24,22,32,17,22,0,24,34,25],
[32,12,32,46,32,9,25,26,0,35,20],
[32,16,19,19,18,13,15,16,15,0,2],
[38,25,24,35,34,30,22,25,30,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 125, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,21,18,22,20,23,26,24,21,23],
[29,0,30,25,24,20,35,24,27,27,31],
[29,20,0,17,18,18,25,17,18,18,25],
[32,25,33,0,29,24,29,26,29,26,32],
[28,26,32,21,0,24,26,27,23,30,31],
[30,30,32,26,26,0,31,31,27,28,25],
[27,15,25,21,24,19,0,26,29,25,26],
[24,26,33,24,23,19,24,0,25,25,23],
[26,23,32,21,27,23,21,25,0,23,25],
[29,23,32,24,20,22,25,25,27,0,25],
[27,19,25,18,19,25,24,27,25,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 126, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,25,24,27,27,23,25,24,23,20],
[24,0,24,22,26,25,21,22,23,24,20],
[25,26,0,25,25,27,22,29,21,25,22],
[26,28,25,0,23,24,25,25,22,27,24],
[23,24,25,27,0,25,20,27,22,23,18],
[23,25,23,26,25,0,23,26,22,23,20],
[27,29,28,25,30,27,0,25,24,28,25],
[25,28,21,25,23,24,25,0,22,24,24],
[26,27,29,28,28,28,26,28,0,30,24],
[27,26,25,23,27,27,22,26,20,0,27],
[30,30,28,26,32,30,25,26,26,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 127, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,8,22,19,22,8,10,31,22,12],
[37,0,25,33,29,41,28,24,38,30,32],
[42,25,0,30,27,35,27,28,41,36,23],
[28,17,20,0,26,34,22,23,37,32,25],
[31,21,23,24,0,29,34,21,32,20,18],
[28,9,15,16,21,0,26,17,38,22,23],
[42,22,23,28,16,24,0,17,39,25,12],
[40,26,22,27,29,33,33,0,39,32,23],
[19,12,9,13,18,12,11,11,0,18,11],
[28,20,14,18,30,28,25,18,32,0,19],
[38,18,27,25,32,27,38,27,39,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 128, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,12,17,20,20,20,13,16,23,19],
[36,0,21,26,19,28,25,24,23,25,26],
[38,29,0,28,25,24,29,23,25,31,24],
[33,24,22,0,23,26,33,29,24,26,23],
[30,31,25,27,0,24,32,22,22,27,22],
[30,22,26,24,26,0,28,19,23,26,22],
[30,25,21,17,18,22,0,15,17,20,22],
[37,26,27,21,28,31,35,0,23,27,31],
[34,27,25,26,28,27,33,27,0,29,23],
[27,25,19,24,23,24,30,23,21,0,26],
[31,24,26,27,28,28,28,19,27,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 129, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,20,19,26,25,22,17,15,24,19],
[32,0,28,15,29,27,18,19,19,27,25],
[30,22,0,22,32,27,15,22,24,24,21],
[31,35,28,0,29,30,18,23,27,24,29],
[24,21,18,21,0,24,12,18,16,22,19],
[25,23,23,20,26,0,23,24,15,19,19],
[28,32,35,32,38,27,0,32,19,25,23],
[33,31,28,27,32,26,18,0,22,29,27],
[35,31,26,23,34,35,31,28,0,26,33],
[26,23,26,26,28,31,25,21,24,0,24],
[31,25,29,21,31,31,27,23,17,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 130, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,14,24,11,23,12,33,22,18,21],
[33,0,26,32,24,27,26,42,27,29,24],
[36,24,0,32,19,25,16,31,30,27,30],
[26,18,18,0,16,26,13,23,25,23,20],
[39,26,31,34,0,30,25,33,25,34,24],
[27,23,25,24,20,0,14,29,21,25,21],
[38,24,34,37,25,36,0,42,36,34,28],
[17,8,19,27,17,21,8,0,22,20,14],
[28,23,20,25,25,29,14,28,0,25,29],
[32,21,23,27,16,25,16,30,25,0,26],
[29,26,20,30,26,29,22,36,21,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 131, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,23,22,30,24,24,30,27,29,23],
[22,0,16,17,23,24,20,24,19,24,25],
[27,34,0,23,34,30,26,33,29,32,27],
[28,33,27,0,39,30,24,32,34,35,28],
[20,27,16,11,0,17,15,19,23,18,21],
[26,26,20,20,33,0,23,30,24,27,34],
[26,30,24,26,35,27,0,36,30,32,33],
[20,26,17,18,31,20,14,0,29,20,23],
[23,31,21,16,27,26,20,21,0,24,25],
[21,26,18,15,32,23,18,30,26,0,25],
[27,25,23,22,29,16,17,27,25,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 132, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,27,31,26,32,24,34,33,30,36],
[20,0,24,33,31,38,28,27,35,34,39],
[23,26,0,31,39,30,31,30,34,32,38],
[19,17,19,0,19,22,20,24,32,18,27],
[24,19,11,31,0,28,29,30,25,25,26],
[18,12,20,28,22,0,24,20,33,38,29],
[26,22,19,30,21,26,0,25,28,25,31],
[16,23,20,26,20,30,25,0,24,26,30],
[17,15,16,18,25,17,22,26,0,21,26],
[20,16,18,32,25,12,25,24,29,0,28],
[14,11,12,23,24,21,19,20,24,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 133, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,27,26,23,26,24,20,25,23,26],
[25,0,26,17,24,18,22,26,24,23,25],
[23,24,0,24,22,23,27,25,24,27,30],
[24,33,26,0,30,25,27,24,31,25,28],
[27,26,28,20,0,26,26,23,25,25,29],
[24,32,27,25,24,0,30,27,32,28,30],
[26,28,23,23,24,20,0,22,25,20,26],
[30,24,25,26,27,23,28,0,24,31,30],
[25,26,26,19,25,18,25,26,0,25,27],
[27,27,23,25,25,22,30,19,25,0,26],
[24,25,20,22,21,20,24,20,23,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 134, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,27,19,31,21,23,29,28,28,23],
[20,0,29,19,21,23,24,34,29,21,25],
[23,21,0,24,31,25,25,37,33,24,29],
[31,31,26,0,30,27,22,32,37,33,29],
[19,29,19,20,0,23,22,28,31,19,24],
[29,27,25,23,27,0,31,30,35,32,24],
[27,26,25,28,28,19,0,33,32,28,22],
[21,16,13,18,22,20,17,0,18,25,11],
[22,21,17,13,19,15,18,32,0,29,27],
[22,29,26,17,31,18,22,25,21,0,22],
[27,25,21,21,26,26,28,39,23,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 135, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,27,21,21,28,34,20,22,25,24],
[24,0,27,20,25,29,28,30,24,32,24],
[23,23,0,23,23,8,18,23,20,24,29],
[29,30,27,0,24,24,30,36,27,33,20],
[29,25,27,26,0,21,31,19,26,26,25],
[22,21,42,26,29,0,30,29,28,27,31],
[16,22,32,20,19,20,0,19,17,29,19],
[30,20,27,14,31,21,31,0,22,30,22],
[28,26,30,23,24,22,33,28,0,25,21],
[25,18,26,17,24,23,21,20,25,0,17],
[26,26,21,30,25,19,31,28,29,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 136, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,33,39,26,37,38,17,29,25,30],
[28,0,24,27,29,28,22,17,17,25,32],
[17,26,0,24,27,29,24,14,15,22,27],
[11,23,26,0,30,33,24,17,21,8,18],
[24,21,23,20,0,33,31,17,13,17,27],
[13,22,21,17,17,0,21,23,15,14,16],
[12,28,26,26,19,29,0,25,22,23,19],
[33,33,36,33,33,27,25,0,19,33,28],
[21,33,35,29,37,35,28,31,0,17,24],
[25,25,28,42,33,36,27,17,33,0,14],
[20,18,23,32,23,34,31,22,26,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 137, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,29,27,25,25,29,29,31,25,29],
[22,0,28,24,27,25,24,25,22,24,18],
[21,22,0,23,21,24,23,25,22,28,22],
[23,26,27,0,24,21,19,25,26,22,20],
[25,23,29,26,0,25,24,25,28,26,23],
[25,25,26,29,25,0,21,30,29,27,26],
[21,26,27,31,26,29,0,30,28,30,26],
[21,25,25,25,25,20,20,0,23,20,24],
[19,28,28,24,22,21,22,27,0,25,26],
[25,26,22,28,24,23,20,30,25,0,26],
[21,32,28,30,27,24,24,26,24,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 138, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,19,8,16,2,33,12,24,16,13],
[32,0,25,15,16,17,42,24,32,20,29],
[31,25,0,28,26,30,46,29,28,22,29],
[42,35,22,0,23,37,33,34,36,29,44],
[34,34,24,27,0,29,46,35,33,31,38],
[48,33,20,13,21,0,33,21,32,18,45],
[17,8,4,17,4,17,0,17,14,16,16],
[38,26,21,16,15,29,33,0,26,21,37],
[26,18,22,14,17,18,36,24,0,12,25],
[34,30,28,21,19,32,34,29,38,0,39],
[37,21,21,6,12,5,34,13,25,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 139, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,37,28,26,28,30,35,36,22,25,27],
[13,0,29,15,13,15,21,16,18,11,19],
[22,21,0,14,25,18,26,26,21,12,15],
[24,35,36,0,28,26,38,37,25,19,30],
[22,37,25,22,0,17,36,20,29,14,19],
[20,35,32,24,33,0,31,24,28,25,25],
[15,29,24,12,14,19,0,24,21,12,20],
[14,34,24,13,30,26,26,0,19,11,15],
[28,32,29,25,21,22,29,31,0,24,24],
[25,39,38,31,36,25,38,39,26,0,36],
[23,31,35,20,31,25,30,35,26,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 140, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,35,26,36,28,31,35,33,39,25],
[18,0,11,19,29,27,17,30,25,18,19],
[15,39,0,28,30,28,25,33,24,20,19],
[24,31,22,0,28,24,32,28,30,31,19],
[14,21,20,22,0,31,21,21,24,22,19],
[22,23,22,26,19,0,29,21,31,25,11],
[19,33,25,18,29,21,0,27,24,29,23],
[15,20,17,22,29,29,23,0,26,25,20],
[17,25,26,20,26,19,26,24,0,31,18],
[11,32,30,19,28,25,21,25,19,0,20],
[25,31,31,31,31,39,27,30,32,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 141, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,38,30,23,35,21,33,25,12,25],
[8,0,15,22,16,18,14,21,11,12,21],
[12,35,0,27,28,30,22,34,20,13,23],
[20,28,23,0,24,25,30,30,27,19,30],
[27,34,22,26,0,34,36,33,33,25,36],
[15,32,20,25,16,0,21,32,30,17,29],
[29,36,28,20,14,29,0,25,22,19,35],
[17,29,16,20,17,18,25,0,27,19,30],
[25,39,30,23,17,20,28,23,0,21,15],
[38,38,37,31,25,33,31,31,29,0,37],
[25,29,27,20,14,21,15,20,35,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 142, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,23,24,27,26,29,25,27,21,26],
[26,0,24,24,24,33,37,25,29,26,28],
[27,26,0,26,24,30,34,28,29,21,31],
[26,26,24,0,27,30,29,25,27,25,30],
[23,26,26,23,0,30,28,28,26,24,27],
[24,17,20,20,20,0,28,21,25,25,24],
[21,13,16,21,22,22,0,19,22,16,18],
[25,25,22,25,22,29,31,0,28,25,26],
[23,21,21,23,24,25,28,22,0,25,24],
[29,24,29,25,26,25,34,25,25,0,25],
[24,22,19,20,23,26,32,24,26,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 143, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,25,27,18,23,27,26,31,29,32],
[22,0,21,21,20,20,29,27,23,27,24],
[25,29,0,24,19,24,34,26,28,30,29],
[23,29,26,0,25,31,35,32,24,34,30],
[32,30,31,25,0,26,29,24,30,31,29],
[27,30,26,19,24,0,30,32,22,32,27],
[23,21,16,15,21,20,0,25,22,28,21],
[24,23,24,18,26,18,25,0,25,34,25],
[19,27,22,26,20,28,28,25,0,27,25],
[21,23,20,16,19,18,22,16,23,0,19],
[18,26,21,20,21,23,29,25,25,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 144, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,21,23,26,25,34,30,25,22,30],
[18,0,22,25,20,22,32,28,24,24,24],
[29,28,0,32,19,13,36,37,29,32,24],
[27,25,18,0,24,16,28,24,25,28,25],
[24,30,31,26,0,28,32,25,28,30,30],
[25,28,37,34,22,0,35,42,25,34,26],
[16,18,14,22,18,15,0,18,19,19,22],
[20,22,13,26,25,8,32,0,18,24,25],
[25,26,21,25,22,25,31,32,0,24,26],
[28,26,18,22,20,16,31,26,26,0,22],
[20,26,26,25,20,24,28,25,24,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 145, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,10,10,29,12,17,20,18,18,20],
[32,0,20,20,30,28,29,18,22,20,24],
[40,30,0,27,34,20,21,23,18,26,28],
[40,30,23,0,26,24,28,23,24,33,25],
[21,20,16,24,0,17,19,18,11,21,22],
[38,22,30,26,33,0,24,23,17,27,28],
[33,21,29,22,31,26,0,28,31,24,28],
[30,32,27,27,32,27,22,0,20,22,21],
[32,28,32,26,39,33,19,30,0,26,30],
[32,30,24,17,29,23,26,28,24,0,19],
[30,26,22,25,28,22,22,29,20,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 146, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,16,20,33,14,18,20,11,13,28],
[25,0,13,17,32,18,13,32,8,15,25],
[34,37,0,25,40,35,32,32,25,26,29],
[30,33,25,0,32,23,26,33,13,15,25],
[17,18,10,18,0,13,15,27,3,12,15],
[36,32,15,27,37,0,27,35,11,21,31],
[32,37,18,24,35,23,0,37,15,15,30],
[30,18,18,17,23,15,13,0,3,15,18],
[39,42,25,37,47,39,35,47,0,31,34],
[37,35,24,35,38,29,35,35,19,0,45],
[22,25,21,25,35,19,20,32,16,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 147, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,29,35,30,26,29,25,33,18,34],
[23,0,25,34,30,22,30,24,24,23,22],
[21,25,0,35,23,17,26,18,26,25,29],
[15,16,15,0,21,17,23,11,17,11,22],
[20,20,27,29,0,21,25,27,19,24,32],
[24,28,33,33,29,0,23,25,30,28,32],
[21,20,24,27,25,27,0,23,19,21,24],
[25,26,32,39,23,25,27,0,35,20,37],
[17,26,24,33,31,20,31,15,0,26,35],
[32,27,25,39,26,22,29,30,24,0,41],
[16,28,21,28,18,18,26,13,15,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 148, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,11,22,16,24,25,36,10,14,23],
[30,0,25,34,17,25,36,26,24,18,17],
[39,25,0,29,31,21,27,30,29,20,28],
[28,16,21,0,11,28,38,31,9,9,18],
[34,33,19,39,0,29,42,28,24,29,40],
[26,25,29,22,21,0,29,30,8,17,28],
[25,14,23,12,8,21,0,27,17,8,21],
[14,24,20,19,22,20,23,0,7,13,21],
[40,26,21,41,26,42,33,43,0,24,25],
[36,32,30,41,21,33,42,37,26,0,24],
[27,33,22,32,10,22,29,29,25,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 149, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,24,12,28,22,23,28,22,25,28],
[23,0,21,19,15,21,19,31,30,21,23],
[26,29,0,17,32,30,26,21,22,27,26],
[38,31,33,0,34,24,28,31,31,28,35],
[22,35,18,16,0,19,10,21,20,18,29],
[28,29,20,26,31,0,19,21,20,26,27],
[27,31,24,22,40,31,0,29,31,30,30],
[22,19,29,19,29,29,21,0,24,21,27],
[28,20,28,19,30,30,19,26,0,25,29],
[25,29,23,22,32,24,20,29,25,0,23],
[22,27,24,15,21,23,20,23,21,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 150, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,43,31,33,29,30,29,23,25,25],
[11,0,38,24,33,27,24,19,20,16,27],
[7,12,0,11,15,14,14,2,11,14,19],
[19,26,39,0,30,33,22,25,28,22,31],
[17,17,35,20,0,24,18,8,14,20,25],
[21,23,36,17,26,0,18,17,27,22,32],
[20,26,36,28,32,32,0,30,32,29,30],
[21,31,48,25,42,33,20,0,26,25,33],
[27,30,39,22,36,23,18,24,0,25,38],
[25,34,36,28,30,28,21,25,25,0,29],
[25,23,31,19,25,18,20,17,12,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 151, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,25,30,27,30,26,28,28,28,27],
[21,0,22,27,25,26,22,23,25,26,28],
[25,28,0,29,23,26,24,24,22,22,24],
[20,23,21,0,17,23,22,20,18,24,22],
[23,25,27,33,0,28,23,23,26,22,22],
[20,24,24,27,22,0,23,18,25,21,23],
[24,28,26,28,27,27,0,22,27,26,29],
[22,27,26,30,27,32,28,0,26,29,27],
[22,25,28,32,24,25,23,24,0,25,29],
[22,24,28,26,28,29,24,21,25,0,26],
[23,22,26,28,28,27,21,23,21,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 152, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,14,14,20,18,20,26,0,11,19],
[27,0,28,20,25,20,16,25,13,17,31],
[36,22,0,15,16,30,31,27,9,22,29],
[36,30,35,0,20,28,24,20,28,28,26],
[30,25,34,30,0,29,29,32,22,29,34],
[32,30,20,22,21,0,25,26,14,17,30],
[30,34,19,26,21,25,0,30,16,27,30],
[24,25,23,30,18,24,20,0,13,8,21],
[50,37,41,22,28,36,34,37,0,36,40],
[39,33,28,22,21,33,23,42,14,0,30],
[31,19,21,24,16,20,20,29,10,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 153, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,22,30,25,31,31,34,27,36,25],
[19,0,23,22,26,33,24,30,26,26,21],
[28,27,0,28,25,36,29,39,26,34,37],
[20,28,22,0,23,28,28,30,19,26,21],
[25,24,25,27,0,25,31,35,29,24,28],
[19,17,14,22,25,0,16,18,18,23,16],
[19,26,21,22,19,34,0,29,21,26,16],
[16,20,11,20,15,32,21,0,15,13,17],
[23,24,24,31,21,32,29,35,0,26,29],
[14,24,16,24,26,27,24,37,24,0,25],
[25,29,13,29,22,34,34,33,21,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 154, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,20,22,29,25,19,32,26,28,30],
[25,0,20,24,26,16,26,23,23,21,27],
[30,30,0,27,29,25,23,25,25,25,28],
[28,26,23,0,32,23,30,35,22,26,32],
[21,24,21,18,0,20,19,25,20,21,31],
[25,34,25,27,30,0,22,29,31,26,26],
[31,24,27,20,31,28,0,31,29,21,34],
[18,27,25,15,25,21,19,0,23,23,29],
[24,27,25,28,30,19,21,27,0,22,29],
[22,29,25,24,29,24,29,27,28,0,30],
[20,23,22,18,19,24,16,21,21,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 155, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,23,26,22,20,18,30,27,24,34],
[29,0,28,30,33,21,29,30,28,32,36],
[27,22,0,26,27,27,25,30,25,33,31],
[24,20,24,0,29,26,20,25,25,29,29],
[28,17,23,21,0,22,21,30,27,33,31],
[30,29,23,24,28,0,23,26,21,30,33],
[32,21,25,30,29,27,0,33,25,33,40],
[20,20,20,25,20,24,17,0,21,22,27],
[23,22,25,25,23,29,25,29,0,34,29],
[26,18,17,21,17,20,17,28,16,0,27],
[16,14,19,21,19,17,10,23,21,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 156, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,33,41,21,29,39,35,39,37,28],
[15,0,21,15,10,27,15,16,26,7,15],
[17,29,0,23,17,30,30,17,30,19,30],
[9,35,27,0,15,20,20,20,28,15,20],
[29,40,33,35,0,27,26,25,26,27,33],
[21,23,20,30,23,0,28,23,28,23,8],
[11,35,20,30,24,22,0,22,29,19,14],
[15,34,33,30,25,27,28,0,26,18,20],
[11,24,20,22,24,22,21,24,0,17,17],
[13,43,31,35,23,27,31,32,33,0,18],
[22,35,20,30,17,42,36,30,33,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 157, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,32,22,27,34,27,30,39,32,33],
[21,0,24,22,21,23,22,27,34,21,24],
[18,26,0,21,17,21,26,24,32,21,22],
[28,28,29,0,32,15,18,25,35,20,27],
[23,29,33,18,0,20,23,28,34,22,30],
[16,27,29,35,30,0,30,31,39,30,32],
[23,28,24,32,27,20,0,26,24,20,32],
[20,23,26,25,22,19,24,0,25,30,23],
[11,16,18,15,16,11,26,25,0,21,29],
[18,29,29,30,28,20,30,20,29,0,30],
[17,26,28,23,20,18,18,27,21,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 158, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,13,13,21,22,25,30,18,23,29],
[32,0,31,27,42,33,28,25,36,37,31],
[37,19,0,31,31,33,25,29,30,39,36],
[37,23,19,0,29,32,20,28,25,22,35],
[29,8,19,21,0,34,30,30,37,32,32],
[28,17,17,18,16,0,23,30,28,24,30],
[25,22,25,30,20,27,0,30,33,28,26],
[20,25,21,22,20,20,20,0,19,29,23],
[32,14,20,25,13,22,17,31,0,21,20],
[27,13,11,28,18,26,22,21,29,0,40],
[21,19,14,15,18,20,24,27,30,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 159, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,25,30,34,27,26,25,23,28,27],
[23,0,30,28,27,28,27,22,28,28,29],
[25,20,0,29,27,23,21,19,22,22,24],
[20,22,21,0,24,29,24,18,20,26,23],
[16,23,23,26,0,26,25,20,20,24,20],
[23,22,27,21,24,0,25,22,24,28,30],
[24,23,29,26,25,25,0,24,23,27,21],
[25,28,31,32,30,28,26,0,26,29,33],
[27,22,28,30,30,26,27,24,0,28,30],
[22,22,28,24,26,22,23,21,22,0,22],
[23,21,26,27,30,20,29,17,20,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 160, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,27,23,23,24,25,24,24,23,24],
[27,0,22,26,22,28,25,29,23,27,23],
[23,28,0,22,23,29,29,26,25,28,27],
[27,24,28,0,23,26,35,32,29,26,27],
[27,28,27,27,0,30,31,26,22,29,21],
[26,22,21,24,20,0,28,27,20,28,21],
[25,25,21,15,19,22,0,23,23,26,22],
[26,21,24,18,24,23,27,0,21,27,21],
[26,27,25,21,28,30,27,29,0,28,28],
[27,23,22,24,21,22,24,23,22,0,23],
[26,27,23,23,29,29,28,29,22,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 161, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,34,32,27,27,22,27,23,37,31],
[32,0,40,27,31,32,25,26,24,42,38],
[16,10,0,22,23,10,18,27,23,27,27],
[18,23,28,0,32,23,13,21,26,31,25],
[23,19,27,18,0,23,26,27,23,29,30],
[23,18,40,27,27,0,28,28,32,35,26],
[28,25,32,37,24,22,0,25,35,33,33],
[23,24,23,29,23,22,25,0,32,32,24],
[27,26,27,24,27,18,15,18,0,38,32],
[13,8,23,19,21,15,17,18,12,0,20],
[19,12,23,25,20,24,17,26,18,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 162, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,23,24,23,22,22,21,25,23,19],
[23,0,15,23,21,20,15,22,24,14,26],
[27,35,0,26,27,27,26,30,34,30,22],
[26,27,24,0,26,24,26,25,25,25,27],
[27,29,23,24,0,25,24,27,27,25,27],
[28,30,23,26,25,0,26,22,25,23,21],
[28,35,24,24,26,24,0,27,29,27,21],
[29,28,20,25,23,28,23,0,24,25,22],
[25,26,16,25,23,25,21,26,0,21,22],
[27,36,20,25,25,27,23,25,29,0,25],
[31,24,28,23,23,29,29,28,28,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 163, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,26,25,31,25,29,20,31,24,26],
[30,0,29,29,30,23,28,25,27,20,26],
[24,21,0,21,21,19,23,17,15,20,23],
[25,21,29,0,24,23,24,17,26,22,28],
[19,20,29,26,0,19,21,9,18,19,27],
[25,27,31,27,31,0,30,28,29,25,27],
[21,22,27,26,29,20,0,18,18,24,27],
[30,25,33,33,41,22,32,0,29,20,30],
[19,23,35,24,32,21,32,21,0,23,29],
[26,30,30,28,31,25,26,30,27,0,28],
[24,24,27,22,23,23,23,20,21,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 164, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,27,31,26,24,25,22,24,25,16],
[28,0,34,28,26,19,24,23,24,31,23],
[23,16,0,25,23,26,21,20,20,24,20],
[19,22,25,0,23,22,18,20,23,28,20],
[24,24,27,27,0,20,24,21,23,31,17],
[26,31,24,28,30,0,25,24,22,29,22],
[25,26,29,32,26,25,0,29,28,29,23],
[28,27,30,30,29,26,21,0,22,30,25],
[26,26,30,27,27,28,22,28,0,39,30],
[25,19,26,22,19,21,21,20,11,0,20],
[34,27,30,30,33,28,27,25,20,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 165, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,32,21,24,26,23,25,26,22,31],
[21,0,25,20,20,20,21,28,22,27,27],
[18,25,0,23,25,22,25,29,24,24,24],
[29,30,27,0,23,25,18,30,30,27,26],
[26,30,25,27,0,27,23,27,30,23,27],
[24,30,28,25,23,0,22,26,28,27,21],
[27,29,25,32,27,28,0,32,36,29,26],
[25,22,21,20,23,24,18,0,24,23,29],
[24,28,26,20,20,22,14,26,0,23,26],
[28,23,26,23,27,23,21,27,27,0,26],
[19,23,26,24,23,29,24,21,24,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 166, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,23,21,26,25,22,24,18,22,22],
[22,0,27,16,27,24,19,33,19,28,27],
[27,23,0,18,30,24,23,29,24,29,21],
[29,34,32,0,31,26,24,29,23,35,26],
[24,23,20,19,0,22,18,21,20,24,22],
[25,26,26,24,28,0,22,29,21,28,25],
[28,31,27,26,32,28,0,33,30,34,25],
[26,17,21,21,29,21,17,0,24,26,15],
[32,31,26,27,30,29,20,26,0,29,24],
[28,22,21,15,26,22,16,24,21,0,22],
[28,23,29,24,28,25,25,35,26,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 167, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,31,25,30,24,30,28,32,27,20],
[20,0,25,17,19,22,16,28,23,19,16],
[19,25,0,19,21,21,21,26,25,26,17],
[25,33,31,0,23,25,20,28,29,25,21],
[20,31,29,27,0,27,22,27,31,20,13],
[26,28,29,25,23,0,21,32,27,23,22],
[20,34,29,30,28,29,0,34,33,29,25],
[22,22,24,22,23,18,16,0,28,14,17],
[18,27,25,21,19,23,17,22,0,18,16],
[23,31,24,25,30,27,21,36,32,0,25],
[30,34,33,29,37,28,25,33,34,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 168, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,26,29,25,31,31,29,23,29,24],
[25,0,25,30,26,31,29,33,25,31,31],
[24,25,0,27,26,28,27,32,25,29,27],
[21,20,23,0,20,28,24,29,22,22,25],
[25,24,24,30,0,34,34,29,23,28,27],
[19,19,22,22,16,0,20,26,21,25,24],
[19,21,23,26,16,30,0,22,16,27,22],
[21,17,18,21,21,24,28,0,21,23,17],
[27,25,25,28,27,29,34,29,0,29,28],
[21,19,21,28,22,25,23,27,21,0,22],
[26,19,23,25,23,26,28,33,22,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 169, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,19,20,27,31,22,24,18,24,17],
[20,0,25,22,26,20,22,32,19,18,19],
[31,25,0,21,25,22,21,30,20,21,17],
[30,28,29,0,20,25,28,23,26,23,26],
[23,24,25,30,0,22,28,21,29,24,22],
[19,30,28,25,28,0,25,29,21,26,22],
[28,28,29,22,22,25,0,28,17,26,20],
[26,18,20,27,29,21,22,0,19,19,19],
[32,31,30,24,21,29,33,31,0,29,27],
[26,32,29,27,26,24,24,31,21,0,27],
[33,31,33,24,28,28,30,31,23,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 170, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,24,27,22,23,27,25,28,26,23],
[26,0,21,26,24,26,28,22,22,26,27],
[26,29,0,29,22,24,25,23,18,22,22],
[23,24,21,0,20,22,20,20,19,20,27],
[28,26,28,30,0,22,25,25,28,26,30],
[27,24,26,28,28,0,32,24,24,24,29],
[23,22,25,30,25,18,0,19,23,26,28],
[25,28,27,30,25,26,31,0,28,24,29],
[22,28,32,31,22,26,27,22,0,26,30],
[24,24,28,30,24,26,24,26,24,0,28],
[27,23,28,23,20,21,22,21,20,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 171, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,28,22,27,31,25,30,24,36,21],
[12,0,11,11,19,12,3,25,13,12,19],
[22,39,0,28,32,34,17,38,28,27,18],
[28,39,22,0,34,21,23,37,19,20,29],
[23,31,18,16,0,18,23,24,21,20,29],
[19,38,16,29,32,0,17,43,20,26,22],
[25,47,33,27,27,33,0,40,28,29,26],
[20,25,12,13,26,7,10,0,20,22,18],
[26,37,22,31,29,30,22,30,0,35,28],
[14,38,23,30,30,24,21,28,15,0,20],
[29,31,32,21,21,28,24,32,22,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 172, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,22,24,22,22,30,28,26,25,28],
[21,0,22,19,22,22,28,26,22,23,23],
[28,28,0,24,25,27,25,21,25,26,27],
[26,31,26,0,26,28,29,28,29,23,31],
[28,28,25,24,0,27,31,32,28,21,28],
[28,28,23,22,23,0,30,24,26,24,24],
[20,22,25,21,19,20,0,22,22,20,28],
[22,24,29,22,18,26,28,0,28,28,29],
[24,28,25,21,22,24,28,22,0,22,32],
[25,27,24,27,29,26,30,22,28,0,28],
[22,27,23,19,22,26,22,21,18,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 173, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,43,29,25,3,25,46,3,25,32],
[7,0,21,25,21,3,28,10,3,21,10],
[7,29,0,29,32,7,32,28,3,25,11],
[21,25,21,0,21,3,7,21,3,21,3],
[25,29,18,29,0,18,32,28,21,21,29],
[47,47,43,47,32,0,32,50,25,43,32],
[25,22,18,43,18,18,0,25,18,18,25],
[4,40,22,29,22,0,25,0,7,25,11],
[47,47,47,47,29,25,32,43,0,47,47],
[25,29,25,29,29,7,32,25,3,0,29],
[18,40,39,47,21,18,25,39,3,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 174, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,27,21,30,22,26,26,19,26,26],
[27,0,27,24,33,26,30,32,25,29,25],
[23,23,0,22,24,23,26,24,21,26,27],
[29,26,28,0,29,26,32,25,23,30,30],
[20,17,26,21,0,26,25,24,18,24,25],
[28,24,27,24,24,0,26,26,24,24,22],
[24,20,24,18,25,24,0,24,22,23,22],
[24,18,26,25,26,24,26,0,18,24,26],
[31,25,29,27,32,26,28,32,0,28,25],
[24,21,24,20,26,26,27,26,22,0,23],
[24,25,23,20,25,28,28,24,25,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 175, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,5,16,16,27,28,28,28,5,11],
[22,0,16,16,27,27,39,45,16,11,22],
[45,34,0,39,45,22,45,45,50,34,45],
[34,34,11,0,45,22,34,34,39,34,45],
[34,23,5,5,0,27,28,34,39,0,11],
[23,23,28,28,23,0,28,23,28,23,34],
[22,11,5,16,22,22,0,45,16,0,11],
[22,5,5,16,16,27,5,0,16,0,11],
[22,34,0,11,11,22,34,34,0,0,11],
[45,39,16,16,50,27,50,50,50,0,22],
[39,28,5,5,39,16,39,39,39,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 176, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,24,22,21,17,24,20,23,27,23],
[27,0,21,29,17,15,27,18,26,19,23],
[26,29,0,27,17,21,31,20,20,24,22],
[28,21,23,0,14,19,27,18,21,19,29],
[29,33,33,36,0,28,34,22,31,35,32],
[33,35,29,31,22,0,32,27,32,28,24],
[26,23,19,23,16,18,0,19,21,17,16],
[30,32,30,32,28,23,31,0,30,29,34],
[27,24,30,29,19,18,29,20,0,21,25],
[23,31,26,31,15,22,33,21,29,0,22],
[27,27,28,21,18,26,34,16,25,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 177, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,24,29,23,23,18,24,22,24,28],
[25,0,18,24,28,26,18,17,13,20,25],
[26,32,0,23,28,18,21,25,23,19,28],
[21,26,27,0,24,19,24,20,24,19,26],
[27,22,22,26,0,22,22,15,19,21,27],
[27,24,32,31,28,0,24,27,21,19,24],
[32,32,29,26,28,26,0,27,25,26,29],
[26,33,25,30,35,23,23,0,26,24,25],
[28,37,27,26,31,29,25,24,0,25,26],
[26,30,31,31,29,31,24,26,25,0,25],
[22,25,22,24,23,26,21,25,24,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 178, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,15,22,35,30,24,29,34,16,19],
[27,0,13,20,31,24,16,28,34,15,13],
[35,37,0,23,30,29,22,35,28,16,21],
[28,30,27,0,42,35,34,42,21,28,20],
[15,19,20,8,0,19,14,16,19,14,13],
[20,26,21,15,31,0,23,23,28,21,26],
[26,34,28,16,36,27,0,24,18,13,21],
[21,22,15,8,34,27,26,0,21,22,20],
[16,16,22,29,31,22,32,29,0,14,15],
[34,35,34,22,36,29,37,28,36,0,27],
[31,37,29,30,37,24,29,30,35,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 179, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,23,25,35,26,21,35,18,32,29],
[28,0,25,27,35,24,27,43,30,24,33],
[27,25,0,23,36,21,29,38,16,34,26],
[25,23,27,0,34,27,21,33,26,32,19],
[15,15,14,16,0,17,20,26,14,30,13],
[24,26,29,23,33,0,34,30,37,42,26],
[29,23,21,29,30,16,0,36,20,29,18],
[15,7,12,17,24,20,14,0,11,20,19],
[32,20,34,24,36,13,30,39,0,28,20],
[18,26,16,18,20,8,21,30,22,0,24],
[21,17,24,31,37,24,32,31,30,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 180, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,11,13,2,28,17,0,13,0,2],
[19,0,28,19,19,28,19,19,30,17,19],
[39,22,0,24,11,28,28,11,11,28,39],
[37,31,26,0,17,37,17,26,11,26,28],
[48,31,39,33,0,37,37,20,11,37,50],
[22,22,22,13,13,0,13,13,13,11,13],
[33,31,22,33,13,37,0,20,13,20,22],
[50,31,39,24,30,37,30,0,13,37,41],
[37,20,39,39,39,37,37,37,0,37,39],
[50,33,22,24,13,39,30,13,13,0,30],
[48,31,11,22,0,37,28,9,11,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 181, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,25,36,25,22,32,21,31,33,27],
[16,0,9,19,16,10,27,13,16,23,15],
[25,41,0,33,22,24,33,27,23,30,22],
[14,31,17,0,17,17,24,14,25,18,12],
[25,34,28,33,0,22,43,31,22,31,27],
[28,40,26,33,28,0,34,22,22,29,21],
[18,23,17,26,7,16,0,15,14,15,16],
[29,37,23,36,19,28,35,0,26,28,24],
[19,34,27,25,28,28,36,24,0,35,24],
[17,27,20,32,19,21,35,22,15,0,16],
[23,35,28,38,23,29,34,26,26,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 182, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,23,23,16,12,23,8,26,21,17],
[39,0,31,35,29,21,30,39,35,36,31],
[27,19,0,31,25,25,33,33,23,31,31],
[27,15,19,0,12,12,25,18,14,25,15],
[34,21,25,38,0,24,33,33,32,33,30],
[38,29,25,38,26,0,31,31,31,41,38],
[27,20,17,25,17,19,0,27,21,12,17],
[42,11,17,32,17,19,23,0,29,23,20],
[24,15,27,36,18,19,29,21,0,25,30],
[29,14,19,25,17,9,38,27,25,0,25],
[33,19,19,35,20,12,33,30,20,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 183, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,19,22,22,14,23,29,29,23,25],
[38,0,36,29,25,39,26,37,34,38,30],
[31,14,0,26,26,23,23,24,24,28,25],
[28,21,24,0,26,28,20,23,29,28,29],
[28,25,24,24,0,26,31,29,28,29,27],
[36,11,27,22,24,0,27,24,28,25,27],
[27,24,27,30,19,23,0,25,31,32,20],
[21,13,26,27,21,26,25,0,30,27,23],
[21,16,26,21,22,22,19,20,0,25,15],
[27,12,22,22,21,25,18,23,25,0,20],
[25,20,25,21,23,23,30,27,35,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 184, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,41,23,23,18,36,42,31,31,33],
[14,0,31,28,19,27,29,34,28,26,24],
[9,19,0,9,19,6,28,28,17,19,18],
[27,22,41,0,13,15,30,42,19,35,33],
[27,31,31,37,0,18,35,37,33,32,33],
[32,23,44,35,32,0,36,44,20,44,40],
[14,21,22,20,15,14,0,25,26,16,16],
[8,16,22,8,13,6,25,0,13,12,23],
[19,22,33,31,17,30,24,37,0,32,27],
[19,24,31,15,18,6,34,38,18,0,17],
[17,26,32,17,17,10,34,27,23,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 185, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,17,21,12,25,12,22,17,19,21],
[18,0,11,24,13,21,11,19,11,22,19],
[33,39,0,27,18,30,20,25,27,26,25],
[29,26,23,0,20,31,21,18,29,27,26],
[38,37,32,30,0,38,21,31,35,34,28],
[25,29,20,19,12,0,15,14,24,15,20],
[38,39,30,29,29,35,0,21,28,30,31],
[28,31,25,32,19,36,29,0,32,34,27],
[33,39,23,21,15,26,22,18,0,17,21],
[31,28,24,23,16,35,20,16,33,0,20],
[29,31,25,24,22,30,19,23,29,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 186, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,22,26,30,19,28,22,19,29,27],
[25,0,24,28,29,28,29,23,23,28,28],
[28,26,0,29,33,29,31,24,23,31,31],
[24,22,21,0,27,28,29,21,20,33,27],
[20,21,17,23,0,23,21,15,15,23,21],
[31,22,21,22,27,0,29,27,16,28,23],
[22,21,19,21,29,21,0,18,21,29,18],
[28,27,26,29,35,23,32,0,25,28,28],
[31,27,27,30,35,34,29,25,0,34,28],
[21,22,19,17,27,22,21,22,16,0,25],
[23,22,19,23,29,27,32,22,22,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 187, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,36,45,45,31,31,31,31,31,45],
[26,0,26,50,21,7,31,7,45,45,45],
[14,24,0,45,45,7,31,31,45,38,45],
[5,0,5,0,21,0,24,0,0,0,0],
[5,29,5,29,0,5,29,5,29,29,29],
[19,43,43,50,45,0,36,36,50,38,50],
[19,19,19,26,21,14,0,0,19,14,19],
[19,43,19,50,45,14,50,0,43,38,43],
[19,5,5,50,21,0,31,7,0,14,45],
[19,5,12,50,21,12,36,12,36,0,50],
[5,5,5,50,21,0,31,7,5,0,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 188, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,26,29,26,23,29,26,26,28,27],
[28,0,32,31,26,26,32,33,25,32,32],
[24,18,0,25,28,24,30,30,26,28,28],
[21,19,25,0,22,22,23,24,16,23,19],
[24,24,22,28,0,23,27,32,29,27,27],
[27,24,26,28,27,0,31,28,30,25,24],
[21,18,20,27,23,19,0,26,27,27,23],
[24,17,20,26,18,22,24,0,24,27,23],
[24,25,24,34,21,20,23,26,0,27,23],
[22,18,22,27,23,25,23,23,23,0,22],
[23,18,22,31,23,26,27,27,27,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 189, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,31,19,25,32,27,33,31,25,29],
[19,0,21,18,19,29,23,23,24,21,25],
[19,29,0,21,19,24,25,31,23,23,23],
[31,32,29,0,24,26,27,34,28,27,26],
[25,31,31,26,0,33,28,32,29,28,30],
[18,21,26,24,17,0,20,26,23,18,23],
[23,27,25,23,22,30,0,29,23,23,26],
[17,27,19,16,18,24,21,0,22,22,25],
[19,26,27,22,21,27,27,28,0,27,24],
[25,29,27,23,22,32,27,28,23,0,24],
[21,25,27,24,20,27,24,25,26,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 190, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,20,27,24,35,28,17,25,26,28],
[22,0,28,21,26,32,16,20,26,26,30],
[30,22,0,27,17,38,27,25,21,37,39],
[23,29,23,0,28,41,34,30,24,37,38],
[26,24,33,22,0,41,23,30,23,31,34],
[15,18,12,9,9,0,13,16,13,19,21],
[22,34,23,16,27,37,0,21,21,23,37],
[33,30,25,20,20,34,29,0,14,30,35],
[25,24,29,26,27,37,29,36,0,33,29],
[24,24,13,13,19,31,27,20,17,0,29],
[22,20,11,12,16,29,13,15,21,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 191, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,14,26,31,26,25,23,25,31,24],
[32,0,21,22,28,24,20,23,30,31,21],
[36,29,0,34,30,33,27,24,32,35,27],
[24,28,16,0,26,26,17,23,24,28,24],
[19,22,20,24,0,26,20,25,27,30,23],
[24,26,17,24,24,0,18,25,29,26,18],
[25,30,23,33,30,32,0,24,30,30,27],
[27,27,26,27,25,25,26,0,31,27,26],
[25,20,18,26,23,21,20,19,0,25,24],
[19,19,15,22,20,24,20,23,25,0,21],
[26,29,23,26,27,32,23,24,26,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 192, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,28,24,25,31,20,31,26,36,17],
[26,0,27,27,23,29,15,28,27,36,20],
[22,23,0,15,26,32,21,21,29,26,14],
[26,23,35,0,26,28,18,29,34,29,26],
[25,27,24,24,0,26,18,32,29,26,12],
[19,21,18,22,24,0,19,23,24,24,17],
[30,35,29,32,32,31,0,29,29,40,23],
[19,22,29,21,18,27,21,0,33,28,22],
[24,23,21,16,21,26,21,17,0,27,15],
[14,14,24,21,24,26,10,22,23,0,15],
[33,30,36,24,38,33,27,28,35,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 193, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,20,28,25,19,25,32,23,23,26],
[24,0,20,33,21,16,18,26,25,26,32],
[30,30,0,32,24,29,32,36,25,31,31],
[22,17,18,0,20,18,23,29,26,25,27],
[25,29,26,30,0,23,27,27,26,30,34],
[31,34,21,32,27,0,29,32,25,33,30],
[25,32,18,27,23,21,0,36,30,33,33],
[18,24,14,21,23,18,14,0,15,22,23],
[27,25,25,24,24,25,20,35,0,20,20],
[27,24,19,25,20,17,17,28,30,0,25],
[24,18,19,23,16,20,17,27,30,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 194, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,22,24,18,16,20,15,27,20,23],
[31,0,28,24,19,20,19,22,31,22,25],
[28,22,0,22,21,18,15,16,29,22,25],
[26,26,28,0,16,21,25,22,30,28,26],
[32,31,29,34,0,23,30,29,30,26,29],
[34,30,32,29,27,0,24,24,33,24,30],
[30,31,35,25,20,26,0,27,29,23,31],
[35,28,34,28,21,26,23,0,38,31,33],
[23,19,21,20,20,17,21,12,0,17,20],
[30,28,28,22,24,26,27,19,33,0,26],
[27,25,25,24,21,20,19,17,30,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 195, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,27,17,20,21,25,33,19,16,21],
[26,0,30,14,23,16,22,25,31,19,27],
[23,20,0,11,23,16,18,31,27,17,17],
[33,36,39,0,34,23,37,41,37,29,31],
[30,27,27,16,0,19,23,32,29,20,22],
[29,34,34,27,31,0,29,40,31,23,32],
[25,28,32,13,27,21,0,34,32,25,29],
[17,25,19,9,18,10,16,0,26,17,17],
[31,19,23,13,21,19,18,24,0,24,19],
[34,31,33,21,30,27,25,33,26,0,32],
[29,23,33,19,28,18,21,33,31,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 196, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,34,19,10,35,32,36,32,19,29],
[20,0,35,14,16,14,11,36,10,21,17],
[16,15,0,19,6,10,16,16,11,16,14],
[31,36,31,0,31,41,32,36,23,31,38],
[40,34,44,19,0,31,38,41,31,38,25],
[15,36,40,9,19,0,20,44,11,20,39],
[18,39,34,18,12,30,0,40,30,28,24],
[14,14,34,14,9,6,10,0,6,5,16],
[18,40,39,27,19,39,20,44,0,19,33],
[31,29,34,19,12,30,22,45,31,0,28],
[21,33,36,12,25,11,26,34,17,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 197, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,30,27,26,23,26,24,25,29,28],
[26,0,26,25,24,21,26,26,22,27,27],
[20,24,0,19,21,20,22,23,24,28,25],
[23,25,31,0,21,23,25,26,23,26,30],
[24,26,29,29,0,29,27,22,27,25,27],
[27,29,30,27,21,0,28,25,23,27,26],
[24,24,28,25,23,22,0,25,28,27,27],
[26,24,27,24,28,25,25,0,24,29,28],
[25,28,26,27,23,27,22,26,0,27,30],
[21,23,22,24,25,23,23,21,23,0,26],
[22,23,25,20,23,24,23,22,20,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 198, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,19,24,23,22,19,23,14,20,21],
[30,0,25,26,23,29,23,30,18,23,24],
[31,25,0,29,26,23,24,28,25,31,29],
[26,24,21,0,30,27,23,22,19,25,19],
[27,27,24,20,0,24,17,23,23,30,25],
[28,21,27,23,26,0,27,23,16,28,24],
[31,27,26,27,33,23,0,30,31,28,24],
[27,20,22,28,27,27,20,0,13,25,18],
[36,32,25,31,27,34,19,37,0,31,25],
[30,27,19,25,20,22,22,25,19,0,23],
[29,26,21,31,25,26,26,32,25,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 199, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,26,31,21,15,16,25,24,17,13],
[32,0,29,33,31,32,20,19,21,25,15],
[24,21,0,27,19,14,16,22,15,23,15],
[19,17,23,0,20,20,16,18,19,24,11],
[29,19,31,30,0,19,19,20,22,30,16],
[35,18,36,30,31,0,22,21,20,29,21],
[34,30,34,34,31,28,0,23,29,29,17],
[25,31,28,32,30,29,27,0,26,27,25],
[26,29,35,31,28,30,21,24,0,33,25],
[33,25,27,26,20,21,21,23,17,0,18],
[37,35,35,39,34,29,33,25,25,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 50, 200, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebb/mebb_11_50.csv", index=False, header=False)