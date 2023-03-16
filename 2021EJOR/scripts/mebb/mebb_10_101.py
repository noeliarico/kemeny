
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,49,65,46,45,60,48,42,70,51],
[52,0,70,65,55,66,53,59,75,46],
[36,31,0,46,33,52,47,41,55,37],
[55,36,55,0,46,58,54,55,59,53],
[56,46,68,55,0,60,52,54,70,56],
[41,35,49,43,41,0,38,34,73,49],
[53,48,54,47,49,63,0,46,58,51],
[59,42,60,46,47,67,55,0,76,54],
[31,26,46,42,31,28,43,25,0,30],
[50,55,64,48,45,52,50,47,71,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 1, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,47,51,44,43,54,48,49,46],
[51,0,49,49,41,42,45,46,44,44],
[54,52,0,47,38,44,50,44,47,52],
[50,52,54,0,49,46,48,48,55,39],
[57,60,63,52,0,43,51,51,55,50],
[58,59,57,55,58,0,49,53,55,57],
[47,56,51,53,50,52,0,42,56,57],
[53,55,57,53,50,48,59,0,57,56],
[52,57,54,46,46,46,45,44,0,51],
[55,57,49,62,51,44,44,45,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 2, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,55,51,46,51,53,46,54,52],
[48,0,47,51,54,41,50,45,51,49],
[46,54,0,44,40,48,38,41,55,44],
[50,50,57,0,43,57,47,45,51,47],
[55,47,61,58,0,57,54,57,59,58],
[50,60,53,44,44,0,47,46,55,51],
[48,51,63,54,47,54,0,45,58,58],
[55,56,60,56,44,55,56,0,55,59],
[47,50,46,50,42,46,43,46,0,45],
[49,52,57,54,43,50,43,42,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 3, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,56,57,49,47,42,48,46,58],
[57,0,61,56,50,54,47,52,47,62],
[45,40,0,44,50,53,39,44,41,54],
[44,45,57,0,47,44,49,41,52,55],
[52,51,51,54,0,60,59,54,45,46],
[54,47,48,57,41,0,55,44,49,48],
[59,54,62,52,42,46,0,52,50,50],
[53,49,57,60,47,57,49,0,55,60],
[55,54,60,49,56,52,51,46,0,60],
[43,39,47,46,55,53,51,41,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 4, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,28,73,63,47,52,47,47,31],
[47,0,38,50,69,58,53,53,46,50],
[73,63,0,69,62,64,62,46,52,55],
[28,51,32,0,47,46,44,36,49,33],
[38,32,39,54,0,54,72,40,47,31],
[54,43,37,55,47,0,61,31,33,21],
[49,48,39,57,29,40,0,30,29,25],
[54,48,55,65,61,70,71,0,50,39],
[54,55,49,52,54,68,72,51,0,44],
[70,51,46,68,70,80,76,62,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 5, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,64,50,50,46,57,44,58,48,57],
[37,0,39,55,45,59,49,44,33,48],
[51,62,0,50,50,66,49,62,56,67],
[51,46,51,0,51,59,53,59,47,54],
[55,56,51,50,0,47,44,54,44,53],
[44,42,35,42,54,0,34,54,39,51],
[57,52,52,48,57,67,0,53,47,60],
[43,57,39,42,47,47,48,0,48,62],
[53,68,45,54,57,62,54,53,0,56],
[44,53,34,47,48,50,41,39,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 6, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,65,58,79,68,49,69,79,83,49],
[36,0,49,43,50,41,40,42,61,41],
[43,52,0,53,60,41,51,51,60,58],
[22,58,48,0,57,49,56,40,69,43],
[33,51,41,44,0,59,75,33,62,30],
[52,60,60,52,42,0,50,52,77,44],
[32,61,50,45,26,51,0,38,61,29],
[22,59,50,61,68,49,63,0,50,40],
[18,40,41,32,39,24,40,51,0,34],
[52,60,43,58,71,57,72,61,67,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 7, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,49,60,61,50,62,47,52,54],
[50,0,46,56,56,58,54,48,54,57],
[52,55,0,65,63,44,58,55,51,46],
[41,45,36,0,58,48,52,42,37,41],
[40,45,38,43,0,42,46,42,37,40],
[51,43,57,53,59,0,63,41,46,46],
[39,47,43,49,55,38,0,46,47,44],
[54,53,46,59,59,60,55,0,54,55],
[49,47,50,64,64,55,54,47,0,45],
[47,44,55,60,61,55,57,46,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 8, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,38,54,56,52,57,51,52,55],
[52,0,42,52,49,44,38,42,54,53],
[63,59,0,56,62,51,43,45,49,55],
[47,49,45,0,50,47,45,49,58,52],
[45,52,39,51,0,51,37,36,54,47],
[49,57,50,54,50,0,48,43,56,57],
[44,63,58,56,64,53,0,47,55,59],
[50,59,56,52,65,58,54,0,68,54],
[49,47,52,43,47,45,46,33,0,56],
[46,48,46,49,54,44,42,47,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 9, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,50,49,41,38,38,49,47,41],
[63,0,59,58,56,44,53,49,58,52],
[51,42,0,44,42,40,39,45,51,39],
[52,43,57,0,50,42,40,50,56,50],
[60,45,59,51,0,48,53,62,58,51],
[63,57,61,59,53,0,53,63,58,49],
[63,48,62,61,48,48,0,56,68,53],
[52,52,56,51,39,38,45,0,61,45],
[54,43,50,45,43,43,33,40,0,43],
[60,49,62,51,50,52,48,56,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 10, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,51,47,51,47,36,50,50,47],
[56,0,56,50,54,49,55,58,54,57],
[50,45,0,46,48,50,46,55,49,49],
[54,51,55,0,50,54,46,57,53,44],
[50,47,53,51,0,52,46,50,57,45],
[54,52,51,47,49,0,45,55,50,49],
[65,46,55,55,55,56,0,56,56,60],
[51,43,46,44,51,46,45,0,48,47],
[51,47,52,48,44,51,45,53,0,50],
[54,44,52,57,56,52,41,54,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 11, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,48,53,40,44,41,43,41,47],
[58,0,55,56,48,50,54,43,46,50],
[53,46,0,55,40,41,42,46,38,47],
[48,45,46,0,40,45,40,41,43,49],
[61,53,61,61,0,52,52,48,52,44],
[57,51,60,56,49,0,50,50,48,50],
[60,47,59,61,49,51,0,47,52,54],
[58,58,55,60,53,51,54,0,53,48],
[60,55,63,58,49,53,49,48,0,55],
[54,51,54,52,57,51,47,53,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 12, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,68,52,51,48,56,58,46,48,57],
[33,0,47,45,31,46,45,50,47,37],
[49,54,0,63,48,53,56,39,53,42],
[50,56,38,0,55,58,54,51,57,45],
[53,70,53,46,0,62,52,52,42,56],
[45,55,48,43,39,0,54,43,57,44],
[43,56,45,47,49,47,0,44,50,51],
[55,51,62,50,49,58,57,0,55,52],
[53,54,48,44,59,44,51,46,0,45],
[44,64,59,56,45,57,50,49,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 13, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,24,39,43,52,41,46,42,44],
[70,0,53,42,60,54,49,48,56,61],
[77,48,0,41,56,77,48,69,55,70],
[62,59,60,0,66,52,52,50,50,68],
[58,41,45,35,0,61,43,47,52,61],
[49,47,24,49,40,0,40,44,35,57],
[60,52,53,49,58,61,0,43,62,71],
[55,53,32,51,54,57,58,0,49,77],
[59,45,46,51,49,66,39,52,0,57],
[57,40,31,33,40,44,30,24,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 14, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,49,50,49,50,36,40,43,39],
[55,0,49,59,51,47,48,48,43,54],
[52,52,0,49,45,54,39,47,50,47],
[51,42,52,0,42,56,41,49,40,43],
[52,50,56,59,0,59,39,53,45,43],
[51,54,47,45,42,0,39,46,43,46],
[65,53,62,60,62,62,0,56,53,50],
[61,53,54,52,48,55,45,0,55,47],
[58,58,51,61,56,58,48,46,0,52],
[62,47,54,58,58,55,51,54,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 15, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,43,36,41,59,64,54,54,43],
[46,0,37,33,35,35,46,43,42,35],
[58,64,0,50,50,65,47,50,52,44],
[65,68,51,0,35,64,62,62,64,59],
[60,66,51,66,0,66,51,60,45,60],
[42,66,36,37,35,0,43,39,51,38],
[37,55,54,39,50,58,0,49,42,42],
[47,58,51,39,41,62,52,0,53,60],
[47,59,49,37,56,50,59,48,0,40],
[58,66,57,42,41,63,59,41,61,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 16, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,48,43,47,56,43,54,45,51],
[55,0,52,61,56,55,48,60,57,57],
[53,49,0,55,50,50,46,56,49,55],
[58,40,46,0,50,53,53,58,52,53],
[54,45,51,51,0,49,49,53,52,51],
[45,46,51,48,52,0,47,47,49,54],
[58,53,55,48,52,54,0,59,53,60],
[47,41,45,43,48,54,42,0,49,47],
[56,44,52,49,49,52,48,52,0,53],
[50,44,46,48,50,47,41,54,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 17, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,50,48,51,44,45,57,54,48],
[47,0,52,44,44,56,50,58,51,41],
[51,49,0,47,44,55,46,55,55,45],
[53,57,54,0,49,56,44,58,54,56],
[50,57,57,52,0,56,55,64,64,50],
[57,45,46,45,45,0,46,54,51,51],
[56,51,55,57,46,55,0,61,54,50],
[44,43,46,43,37,47,40,0,49,44],
[47,50,46,47,37,50,47,52,0,48],
[53,60,56,45,51,50,51,57,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 18, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,58,78,62,54,49,65,68,60],
[44,0,38,53,46,37,23,47,43,43],
[43,63,0,71,56,53,30,46,57,46],
[23,48,30,0,50,34,34,42,42,29],
[39,55,45,51,0,43,34,56,35,44],
[47,64,48,67,58,0,27,46,53,50],
[52,78,71,67,67,74,0,50,62,44],
[36,54,55,59,45,55,51,0,54,44],
[33,58,44,59,66,48,39,47,0,53],
[41,58,55,72,57,51,57,57,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 19, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,41,48,43,59,46,45,47,46],
[52,0,52,51,54,55,43,56,52,50],
[60,49,0,52,56,51,47,56,57,45],
[53,50,49,0,54,45,48,58,51,45],
[58,47,45,47,0,50,45,58,52,54],
[42,46,50,56,51,0,48,45,44,46],
[55,58,54,53,56,53,0,63,55,50],
[56,45,45,43,43,56,38,0,51,40],
[54,49,44,50,49,57,46,50,0,52],
[55,51,56,56,47,55,51,61,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 20, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,54,59,60,50,68,60,67,56],
[42,0,45,50,48,51,48,45,52,48],
[47,56,0,50,53,56,52,59,59,54],
[42,51,51,0,58,50,62,58,63,48],
[41,53,48,43,0,53,58,55,60,49],
[51,50,45,51,48,0,62,56,57,50],
[33,53,49,39,43,39,0,48,56,41],
[41,56,42,43,46,45,53,0,58,47],
[34,49,42,38,41,44,45,43,0,47],
[45,53,47,53,52,51,60,54,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 21, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,14,62,48,9,48,48,57,57],
[53,0,23,71,48,23,57,14,57,9],
[87,78,0,62,78,87,78,48,57,57],
[39,30,39,0,78,39,39,0,87,9],
[53,53,23,23,0,23,53,23,71,23],
[92,78,14,62,78,0,78,48,48,48],
[53,44,23,62,48,23,0,14,71,23],
[53,87,53,101,78,53,87,0,87,39],
[44,44,44,14,30,53,30,14,0,14],
[44,92,44,92,78,53,78,62,87,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 22, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,69,55,54,28,57,41,42,34],
[39,0,37,57,26,37,25,39,59,21],
[32,64,0,44,37,27,34,26,32,48],
[46,44,57,0,25,45,36,34,37,54],
[47,75,64,76,0,33,50,47,54,45],
[73,64,74,56,68,0,47,61,60,69],
[44,76,67,65,51,54,0,52,50,44],
[60,62,75,67,54,40,49,0,47,57],
[59,42,69,64,47,41,51,54,0,51],
[67,80,53,47,56,32,57,44,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 23, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,54,42,48,58,57,67,54,35],
[63,0,61,70,49,53,64,59,58,44],
[47,40,0,47,52,60,67,50,57,53],
[59,31,54,0,44,54,50,52,46,31],
[53,52,49,57,0,67,59,63,52,44],
[43,48,41,47,34,0,37,30,37,41],
[44,37,34,51,42,64,0,51,54,36],
[34,42,51,49,38,71,50,0,41,44],
[47,43,44,55,49,64,47,60,0,41],
[66,57,48,70,57,60,65,57,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 24, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,59,50,57,48,51,57,64,51],
[40,0,45,44,56,37,51,39,56,55],
[42,56,0,39,60,42,55,45,54,47],
[51,57,62,0,66,36,59,40,63,50],
[44,45,41,35,0,29,38,37,42,37],
[53,64,59,65,72,0,59,47,58,63],
[50,50,46,42,63,42,0,40,51,52],
[44,62,56,61,64,54,61,0,47,45],
[37,45,47,38,59,43,50,54,0,45],
[50,46,54,51,64,38,49,56,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 25, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,54,52,61,51,55,42,51,48],
[45,0,51,61,50,46,56,64,59,49],
[47,50,0,50,57,47,56,49,49,40],
[49,40,51,0,55,44,44,43,53,40],
[40,51,44,46,0,35,41,45,41,40],
[50,55,54,57,66,0,62,53,63,55],
[46,45,45,57,60,39,0,47,46,45],
[59,37,52,58,56,48,54,0,54,46],
[50,42,52,48,60,38,55,47,0,39],
[53,52,61,61,61,46,56,55,62,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 26, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,57,71,48,29,30,48,71,29],
[55,0,84,53,30,53,30,84,82,59],
[44,17,0,42,19,42,2,19,71,29],
[30,48,59,0,59,28,30,31,56,59],
[53,71,82,42,0,53,53,71,71,57],
[72,48,59,73,48,0,30,48,73,59],
[71,71,99,71,48,71,0,71,71,29],
[53,17,82,70,30,53,30,0,71,57],
[30,19,30,45,30,28,30,30,0,30],
[72,42,72,42,44,42,72,44,71,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 27, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,47,56,54,46,45,44,44,48],
[47,0,39,63,38,50,50,58,43,52],
[54,62,0,61,44,53,51,50,51,46],
[45,38,40,0,36,45,51,38,36,43],
[47,63,57,65,0,46,50,56,55,42],
[55,51,48,56,55,0,54,48,45,47],
[56,51,50,50,51,47,0,50,48,49],
[57,43,51,63,45,53,51,0,45,47],
[57,58,50,65,46,56,53,56,0,50],
[53,49,55,58,59,54,52,54,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 28, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,67,48,51,67,67,53,70,67,52],
[34,0,24,9,52,21,37,35,64,22],
[53,77,0,41,92,57,58,63,92,53],
[50,92,60,0,83,88,65,66,79,78],
[34,49,9,18,0,49,49,44,39,41],
[34,80,44,13,52,0,37,50,64,50],
[48,64,43,36,52,64,0,48,64,52],
[31,66,38,35,57,51,53,0,53,66],
[34,37,9,22,62,37,37,48,0,41],
[49,79,48,23,60,51,49,35,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 29, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,49,56,59,52,38,55,55,46],
[57,0,42,56,59,52,45,49,54,54],
[52,59,0,61,57,56,46,64,59,49],
[45,45,40,0,43,40,38,46,47,54],
[42,42,44,58,0,46,48,47,42,45],
[49,49,45,61,55,0,47,44,56,50],
[63,56,55,63,53,54,0,59,52,48],
[46,52,37,55,54,57,42,0,52,46],
[46,47,42,54,59,45,49,49,0,55],
[55,47,52,47,56,51,53,55,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 30, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,66,53,70,59,54,47,59,47],
[52,0,68,51,76,73,46,66,67,56],
[35,33,0,42,61,49,47,52,50,36],
[48,50,59,0,54,59,45,49,41,40],
[31,25,40,47,0,53,49,41,47,31],
[42,28,52,42,48,0,38,46,44,32],
[47,55,54,56,52,63,0,56,60,46],
[54,35,49,52,60,55,45,0,45,30],
[42,34,51,60,54,57,41,56,0,42],
[54,45,65,61,70,69,55,71,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 31, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,65,55,54,48,53,56,44,52,57],
[36,0,48,44,44,53,48,48,58,49],
[46,53,0,40,41,52,44,44,42,54],
[47,57,61,0,56,66,57,52,60,67],
[53,57,60,45,0,59,53,50,51,57],
[48,48,49,35,42,0,48,42,49,53],
[45,53,57,44,48,53,0,50,54,59],
[57,53,57,49,51,59,51,0,49,53],
[49,43,59,41,50,52,47,52,0,53],
[44,52,47,34,44,48,42,48,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 32, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,79,79,79,35,79,101,101,57,44],
[22,0,0,57,22,101,57,22,22,44],
[22,101,0,101,57,101,101,57,57,66],
[22,44,0,0,0,66,101,22,22,44],
[66,79,44,101,0,101,101,101,66,44],
[22,0,0,35,0,0,57,22,22,44],
[0,44,0,0,0,44,0,22,22,44],
[0,79,44,79,0,79,79,0,0,44],
[44,79,44,79,35,79,79,101,0,44],
[57,57,35,57,57,57,57,57,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 33, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,52,51,46,58,49,56,48,57],
[57,0,50,55,51,59,54,62,50,51],
[49,51,0,47,51,49,44,49,51,51],
[50,46,54,0,46,57,50,49,47,45],
[55,50,50,55,0,55,50,55,55,48],
[43,42,52,44,46,0,45,49,38,44],
[52,47,57,51,51,56,0,58,59,57],
[45,39,52,52,46,52,43,0,48,45],
[53,51,50,54,46,63,42,53,0,56],
[44,50,50,56,53,57,44,56,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 34, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,68,69,54,49,50,51,47,59],
[49,0,45,56,60,41,47,53,51,73],
[33,56,0,76,35,46,73,51,48,62],
[32,45,25,0,30,24,44,39,22,48],
[47,41,66,71,0,52,51,48,47,71],
[52,60,55,77,49,0,46,61,30,67],
[51,54,28,57,50,55,0,63,57,56],
[50,48,50,62,53,40,38,0,50,54],
[54,50,53,79,54,71,44,51,0,57],
[42,28,39,53,30,34,45,47,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 35, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,54,50,47,50,50,49,52,56],
[48,0,56,53,50,51,56,54,54,56],
[47,45,0,44,43,43,48,42,49,50],
[51,48,57,0,48,53,54,50,53,56],
[54,51,58,53,0,59,49,48,52,57],
[51,50,58,48,42,0,45,50,52,49],
[51,45,53,47,52,56,0,49,43,51],
[52,47,59,51,53,51,52,0,56,57],
[49,47,52,48,49,49,58,45,0,54],
[45,45,51,45,44,52,50,44,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 36, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,37,52,54,54,39,44,44,52],
[56,0,45,51,51,53,42,39,43,49],
[64,56,0,57,59,56,55,42,47,63],
[49,50,44,0,52,45,33,40,46,54],
[47,50,42,49,0,53,42,44,41,51],
[47,48,45,56,48,0,41,43,42,54],
[62,59,46,68,59,60,0,56,54,55],
[57,62,59,61,57,58,45,0,52,66],
[57,58,54,55,60,59,47,49,0,60],
[49,52,38,47,50,47,46,35,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 37, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,47,48,43,47,57,48,50,55],
[52,0,48,45,47,48,52,53,48,53],
[54,53,0,44,51,49,61,50,51,57],
[53,56,57,0,46,60,62,57,53,54],
[58,54,50,55,0,52,60,63,54,54],
[54,53,52,41,49,0,58,46,53,50],
[44,49,40,39,41,43,0,52,50,54],
[53,48,51,44,38,55,49,0,46,57],
[51,53,50,48,47,48,51,55,0,52],
[46,48,44,47,47,51,47,44,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 38, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,50,53,51,49,58,55,51,46],
[49,0,43,45,43,46,45,61,49,47],
[51,58,0,44,44,49,45,66,59,44],
[48,56,57,0,49,53,60,59,46,57],
[50,58,57,52,0,53,46,60,51,56],
[52,55,52,48,48,0,39,68,64,49],
[43,56,56,41,55,62,0,46,58,53],
[46,40,35,42,41,33,55,0,45,43],
[50,52,42,55,50,37,43,56,0,49],
[55,54,57,44,45,52,48,58,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 39, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,59,66,55,48,49,48,47,51],
[44,0,52,49,54,45,36,50,39,37],
[42,49,0,54,50,47,45,49,41,50],
[35,52,47,0,53,54,54,52,49,60],
[46,47,51,48,0,49,46,52,45,48],
[53,56,54,47,52,0,46,59,55,53],
[52,65,56,47,55,55,0,55,45,52],
[53,51,52,49,49,42,46,0,36,38],
[54,62,60,52,56,46,56,65,0,51],
[50,64,51,41,53,48,49,63,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 40, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,61,66,57,62,63,52,49,55],
[41,0,54,45,54,42,48,48,40,41],
[40,47,0,50,57,50,50,40,45,41],
[35,56,51,0,52,52,52,48,46,48],
[44,47,44,49,0,55,49,49,46,46],
[39,59,51,49,46,0,57,48,49,39],
[38,53,51,49,52,44,0,43,44,43],
[49,53,61,53,52,53,58,0,52,55],
[52,61,56,55,55,52,57,49,0,48],
[46,60,60,53,55,62,58,46,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 41, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,47,46,63,58,49,67,50,26],
[44,0,41,62,55,56,52,52,52,52],
[54,60,0,51,69,47,44,51,61,40],
[55,39,50,0,54,57,52,61,55,36],
[38,46,32,47,0,34,25,45,41,31],
[43,45,54,44,67,0,39,24,40,25],
[52,49,57,49,76,62,0,46,45,36],
[34,49,50,40,56,77,55,0,58,28],
[51,49,40,46,60,61,56,43,0,32],
[75,49,61,65,70,76,65,73,69,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 42, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,47,52,54,54,48,49,59,56],
[50,0,46,46,52,53,44,48,56,56],
[54,55,0,55,54,54,49,58,63,61],
[49,55,46,0,55,48,48,49,53,60],
[47,49,47,46,0,51,45,52,56,58],
[47,48,47,53,50,0,47,42,52,58],
[53,57,52,53,56,54,0,53,50,60],
[52,53,43,52,49,59,48,0,62,59],
[42,45,38,48,45,49,51,39,0,51],
[45,45,40,41,43,43,41,42,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 43, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,41,40,43,39,37,40,48,43],
[68,0,59,49,57,51,49,51,56,63],
[60,42,0,47,56,48,47,50,66,57],
[61,52,54,0,58,57,54,46,60,59],
[58,44,45,43,0,52,46,44,60,52],
[62,50,53,44,49,0,59,55,52,60],
[64,52,54,47,55,42,0,46,58,52],
[61,50,51,55,57,46,55,0,57,63],
[53,45,35,41,41,49,43,44,0,50],
[58,38,44,42,49,41,49,38,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 44, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,45,50,53,47,54,62,51,55],
[49,0,48,49,47,45,49,44,55,49],
[56,53,0,57,56,52,53,50,55,53],
[51,52,44,0,54,57,53,49,49,52],
[48,54,45,47,0,41,47,53,49,44],
[54,56,49,44,60,0,46,59,54,54],
[47,52,48,48,54,55,0,51,48,50],
[39,57,51,52,48,42,50,0,52,54],
[50,46,46,52,52,47,53,49,0,51],
[46,52,48,49,57,47,51,47,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 45, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,43,48,48,53,44,58,47,53],
[54,0,55,50,52,50,46,55,53,52],
[58,46,0,52,57,53,50,56,60,53],
[53,51,49,0,59,56,59,59,57,62],
[53,49,44,42,0,42,45,51,51,49],
[48,51,48,45,59,0,45,54,52,50],
[57,55,51,42,56,56,0,58,53,53],
[43,46,45,42,50,47,43,0,51,48],
[54,48,41,44,50,49,48,50,0,51],
[48,49,48,39,52,51,48,53,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 46, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,51,48,42,46,47,50,58,53],
[45,0,59,38,42,39,50,40,45,57],
[50,42,0,53,51,48,43,54,51,46],
[53,63,48,0,55,43,58,63,58,48],
[59,59,50,46,0,53,54,53,53,48],
[55,62,53,58,48,0,53,45,53,48],
[54,51,58,43,47,48,0,53,54,48],
[51,61,47,38,48,56,48,0,39,50],
[43,56,50,43,48,48,47,62,0,58],
[48,44,55,53,53,53,53,51,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 47, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,52,50,48,48,53,56,46,56],
[47,0,61,56,54,47,50,57,45,50],
[49,40,0,44,55,47,50,51,51,54],
[51,45,57,0,52,49,44,52,46,60],
[53,47,46,49,0,54,52,61,45,57],
[53,54,54,52,47,0,51,56,45,54],
[48,51,51,57,49,50,0,58,44,53],
[45,44,50,49,40,45,43,0,41,62],
[55,56,50,55,56,56,57,60,0,55],
[45,51,47,41,44,47,48,39,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 48, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,49,59,50,49,52,53,52,50],
[47,0,50,60,48,45,43,57,57,53],
[52,51,0,53,47,51,45,52,51,53],
[42,41,48,0,48,38,41,48,47,50],
[51,53,54,53,0,51,51,56,53,49],
[52,56,50,63,50,0,44,60,55,52],
[49,58,56,60,50,57,0,60,56,49],
[48,44,49,53,45,41,41,0,50,46],
[49,44,50,54,48,46,45,51,0,45],
[51,48,48,51,52,49,52,55,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 49, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,42,54,50,40,46,52,45,51],
[56,0,41,42,53,41,47,52,50,52],
[59,60,0,53,49,51,51,64,57,47],
[47,59,48,0,48,43,46,53,51,57],
[51,48,52,53,0,37,45,52,46,56],
[61,60,50,58,64,0,53,60,61,53],
[55,54,50,55,56,48,0,53,58,52],
[49,49,37,48,49,41,48,0,51,49],
[56,51,44,50,55,40,43,50,0,49],
[50,49,54,44,45,48,49,52,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 50, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,49,74,65,73,58,79,54,70],
[47,0,51,57,47,66,42,59,46,54],
[52,50,0,52,55,59,43,69,29,66],
[27,44,49,0,34,56,25,46,24,46],
[36,54,46,67,0,73,60,73,55,70],
[28,35,42,45,28,0,39,53,13,39],
[43,59,58,76,41,62,0,49,38,46],
[22,42,32,55,28,48,52,0,27,52],
[47,55,72,77,46,88,63,74,0,81],
[31,47,35,55,31,62,55,49,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 51, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,53,46,53,56,51,53,52,52],
[46,0,48,48,41,56,43,53,51,50],
[48,53,0,52,51,59,54,58,56,48],
[55,53,49,0,45,55,46,59,49,47],
[48,60,50,56,0,50,50,59,56,52],
[45,45,42,46,51,0,45,52,53,42],
[50,58,47,55,51,56,0,55,52,58],
[48,48,43,42,42,49,46,0,51,44],
[49,50,45,52,45,48,49,50,0,46],
[49,51,53,54,49,59,43,57,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 52, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,51,53,56,47,44,48,50,46],
[51,0,61,64,54,52,59,54,58,46],
[50,40,0,59,62,49,58,50,55,54],
[48,37,42,0,36,44,43,47,43,55],
[45,47,39,65,0,50,52,48,52,51],
[54,49,52,57,51,0,48,58,57,58],
[57,42,43,58,49,53,0,59,44,47],
[53,47,51,54,53,43,42,0,57,50],
[51,43,46,58,49,44,57,44,0,45],
[55,55,47,46,50,43,54,51,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 53, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,47,46,45,44,47,48,53,54],
[57,0,50,53,50,48,51,51,48,58],
[54,51,0,51,51,48,51,44,49,56],
[55,48,50,0,48,48,51,52,54,50],
[56,51,50,53,0,44,55,50,60,57],
[57,53,53,53,57,0,50,48,57,61],
[54,50,50,50,46,51,0,48,58,52],
[53,50,57,49,51,53,53,0,55,56],
[48,53,52,47,41,44,43,46,0,49],
[47,43,45,51,44,40,49,45,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 54, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,50,56,58,49,51,51,44,51],
[58,0,43,52,54,46,47,55,52,53],
[51,58,0,59,59,52,48,61,53,60],
[45,49,42,0,54,47,61,44,50,57],
[43,47,42,47,0,49,46,41,56,48],
[52,55,49,54,52,0,43,58,50,59],
[50,54,53,40,55,58,0,46,52,42],
[50,46,40,57,60,43,55,0,55,52],
[57,49,48,51,45,51,49,46,0,51],
[50,48,41,44,53,42,59,49,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 55, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,39,41,41,34,40,52,45,43],
[61,0,67,81,75,48,63,73,52,53],
[62,34,0,44,39,33,34,59,41,37],
[60,20,57,0,59,28,50,59,47,34],
[60,26,62,42,0,43,50,50,36,50],
[67,53,68,73,58,0,76,63,50,52],
[61,38,67,51,51,25,0,54,35,18],
[49,28,42,42,51,38,47,0,43,36],
[56,49,60,54,65,51,66,58,0,43],
[58,48,64,67,51,49,83,65,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 56, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,33,53,33,64,67,33,24,57],
[52,0,46,64,43,61,89,53,34,53],
[68,55,0,74,69,82,71,45,68,91],
[48,37,27,0,34,44,53,14,34,51],
[68,58,32,67,0,55,60,48,73,70],
[37,40,19,57,46,0,58,39,39,29],
[34,12,30,48,41,43,0,37,32,59],
[68,48,56,87,53,62,64,0,53,61],
[77,67,33,67,28,62,69,48,0,61],
[44,48,10,50,31,72,42,40,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 57, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,46,55,51,53,55,50,56,49],
[56,0,42,58,54,58,60,56,63,48],
[55,59,0,55,49,51,48,63,59,55],
[46,43,46,0,41,48,42,48,43,46],
[50,47,52,60,0,51,47,61,60,48],
[48,43,50,53,50,0,43,46,55,52],
[46,41,53,59,54,58,0,58,61,51],
[51,45,38,53,40,55,43,0,57,41],
[45,38,42,58,41,46,40,44,0,39],
[52,53,46,55,53,49,50,60,62,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 58, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,53,48,45,49,45,53,45,48],
[56,0,54,58,47,54,51,55,57,56],
[48,47,0,51,43,47,49,45,51,50],
[53,43,50,0,48,54,47,50,53,59],
[56,54,58,53,0,51,49,53,60,58],
[52,47,54,47,50,0,49,54,56,57],
[56,50,52,54,52,52,0,49,53,52],
[48,46,56,51,48,47,52,0,59,42],
[56,44,50,48,41,45,48,42,0,48],
[53,45,51,42,43,44,49,59,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 59, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,47,49,41,53,35,50,39,44],
[53,0,51,64,51,55,53,57,45,48],
[54,50,0,55,46,59,54,66,46,55],
[52,37,46,0,43,52,52,48,42,42],
[60,50,55,58,0,60,53,63,58,61],
[48,46,42,49,41,0,45,42,39,46],
[66,48,47,49,48,56,0,55,55,53],
[51,44,35,53,38,59,46,0,41,42],
[62,56,55,59,43,62,46,60,0,45],
[57,53,46,59,40,55,48,59,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 60, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,54,41,29,30,53,30,34,46],
[62,0,47,47,55,48,69,23,24,47],
[47,54,0,43,21,32,44,43,44,54],
[60,54,58,0,30,32,45,54,23,47],
[72,46,80,71,0,48,65,47,57,68],
[71,53,69,69,53,0,65,53,45,57],
[48,32,57,56,36,36,0,22,33,35],
[71,78,58,47,54,48,79,0,58,60],
[67,77,57,78,44,56,68,43,0,49],
[55,54,47,54,33,44,66,41,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 61, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,55,52,40,48,45,49,52,65],
[54,0,68,62,62,49,49,62,62,60],
[46,33,0,42,33,28,30,14,51,36],
[49,39,59,0,48,39,42,39,61,50],
[61,39,68,53,0,62,55,49,61,57],
[53,52,73,62,39,0,51,70,53,56],
[56,52,71,59,46,50,0,55,72,63],
[52,39,87,62,52,31,46,0,61,83],
[49,39,50,40,40,48,29,40,0,43],
[36,41,65,51,44,45,38,18,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 62, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,47,56,57,53,55,53,54,52],
[44,0,49,58,60,55,57,52,64,44],
[54,52,0,57,54,50,54,52,56,52],
[45,43,44,0,47,46,53,44,52,43],
[44,41,47,54,0,48,57,47,47,38],
[48,46,51,55,53,0,47,48,50,43],
[46,44,47,48,44,54,0,44,50,45],
[48,49,49,57,54,53,57,0,59,49],
[47,37,45,49,54,51,51,42,0,47],
[49,57,49,58,63,58,56,52,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 63, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,46,53,51,45,56,48,49,52],
[56,0,47,54,54,49,52,46,50,50],
[55,54,0,54,56,53,52,51,55,50],
[48,47,47,0,40,41,52,54,44,53],
[50,47,45,61,0,53,58,58,53,52],
[56,52,48,60,48,0,51,51,53,55],
[45,49,49,49,43,50,0,45,52,41],
[53,55,50,47,43,50,56,0,50,55],
[52,51,46,57,48,48,49,51,0,53],
[49,51,51,48,49,46,60,46,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 64, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,47,58,51,51,57,50,41,46],
[48,0,43,53,48,49,50,52,47,44],
[54,58,0,53,53,52,54,45,51,53],
[43,48,48,0,37,41,48,50,44,43],
[50,53,48,64,0,56,59,52,48,54],
[50,52,49,60,45,0,50,55,57,45],
[44,51,47,53,42,51,0,55,46,47],
[51,49,56,51,49,46,46,0,57,44],
[60,54,50,57,53,44,55,44,0,43],
[55,57,48,58,47,56,54,57,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 65, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,62,59,48,58,55,57,56,53],
[49,0,55,57,51,59,48,45,49,54],
[39,46,0,51,46,55,43,47,45,55],
[42,44,50,0,38,54,44,43,48,56],
[53,50,55,63,0,57,45,55,53,57],
[43,42,46,47,44,0,33,44,44,47],
[46,53,58,57,56,68,0,49,47,57],
[44,56,54,58,46,57,52,0,49,56],
[45,52,56,53,48,57,54,52,0,52],
[48,47,46,45,44,54,44,45,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 66, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,52,49,53,50,46,58,48,51],
[49,0,45,48,56,46,44,57,52,53],
[49,56,0,54,57,50,49,59,57,53],
[52,53,47,0,53,53,50,53,59,52],
[48,45,44,48,0,52,42,48,44,44],
[51,55,51,48,49,0,49,57,53,48],
[55,57,52,51,59,52,0,63,50,57],
[43,44,42,48,53,44,38,0,44,47],
[53,49,44,42,57,48,51,57,0,53],
[50,48,48,49,57,53,44,54,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 67, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,75,75,64,75,57,52,70,83,45],
[26,0,58,35,77,51,34,33,67,30],
[26,43,0,47,70,55,39,62,51,43],
[37,66,54,0,64,66,34,47,61,56],
[26,24,31,37,0,17,4,31,50,28],
[44,50,46,35,84,0,0,47,52,44],
[49,67,62,67,97,101,0,53,67,66],
[31,68,39,54,70,54,48,0,39,52],
[18,34,50,40,51,49,34,62,0,37],
[56,71,58,45,73,57,35,49,64,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 68, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,65,48,65,63,52,44,44,62],
[44,0,55,52,44,52,47,51,42,50],
[36,46,0,34,53,62,40,37,51,45],
[53,49,67,0,61,61,54,49,61,59],
[36,57,48,40,0,50,41,37,47,43],
[38,49,39,40,51,0,44,41,45,53],
[49,54,61,47,60,57,0,53,51,53],
[57,50,64,52,64,60,48,0,60,58],
[57,59,50,40,54,56,50,41,0,57],
[39,51,56,42,58,48,48,43,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 69, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,68,61,30,73,54,38,50,49,37],
[33,0,33,37,50,33,21,38,45,23],
[40,68,0,56,69,33,21,50,45,49],
[71,64,45,0,71,64,64,64,64,61],
[28,51,32,30,0,33,19,33,57,30],
[47,68,68,37,68,0,40,64,51,58],
[63,80,80,37,82,61,0,80,63,65],
[51,63,51,37,68,37,21,0,49,34],
[52,56,56,37,44,50,38,52,0,54],
[64,78,52,40,71,43,36,67,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 70, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,57,51,54,52,50,55,57,54],
[51,0,46,57,44,44,54,49,48,51],
[44,55,0,50,49,49,52,50,59,50],
[50,44,51,0,53,42,48,49,51,51],
[47,57,52,48,0,52,52,52,50,49],
[49,57,52,59,49,0,53,53,57,56],
[51,47,49,53,49,48,0,48,48,44],
[46,52,51,52,49,48,53,0,55,53],
[44,53,42,50,51,44,53,46,0,45],
[47,50,51,50,52,45,57,48,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 71, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,48,63,59,74,49,51,42,60],
[44,0,53,39,59,61,38,45,37,58],
[53,48,0,50,52,79,47,55,57,57],
[38,62,51,0,59,61,47,40,37,51],
[42,42,49,42,0,72,42,50,33,47],
[27,40,22,40,29,0,27,35,20,36],
[52,63,54,54,59,74,0,44,33,58],
[50,56,46,61,51,66,57,0,45,53],
[59,64,44,64,68,81,68,56,0,60],
[41,43,44,50,54,65,43,48,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 72, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,46,35,43,43,39,44,40,37],
[53,0,45,45,42,48,42,52,49,48],
[55,56,0,48,55,47,47,53,48,51],
[66,56,53,0,57,52,56,47,48,48],
[58,59,46,44,0,48,41,49,45,47],
[58,53,54,49,53,0,46,52,43,50],
[62,59,54,45,60,55,0,50,53,52],
[57,49,48,54,52,49,51,0,50,49],
[61,52,53,53,56,58,48,51,0,48],
[64,53,50,53,54,51,49,52,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 73, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,52,32,65,68,28,52,31,30],
[73,0,36,55,65,60,44,60,61,65],
[49,65,0,56,57,48,56,62,57,58],
[69,46,45,0,55,56,39,42,51,59],
[36,36,44,46,0,59,32,56,42,27],
[33,41,53,45,42,0,40,42,29,34],
[73,57,45,62,69,61,0,54,58,54],
[49,41,39,59,45,59,47,0,38,41],
[70,40,44,50,59,72,43,63,0,50],
[71,36,43,42,74,67,47,60,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 74, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,61,59,57,53,74,43,51,38],
[56,0,46,36,65,45,54,55,58,36],
[40,55,0,28,57,35,58,66,42,22],
[42,65,73,0,56,49,56,72,53,54],
[44,36,44,45,0,34,58,40,32,36],
[48,56,66,52,67,0,53,71,56,53],
[27,47,43,45,43,48,0,47,33,43],
[58,46,35,29,61,30,54,0,41,47],
[50,43,59,48,69,45,68,60,0,38],
[63,65,79,47,65,48,58,54,63,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 75, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,51,50,50,54,47,45,50,52],
[55,0,55,54,44,56,50,47,54,51],
[50,46,0,45,48,55,39,44,51,44],
[51,47,56,0,48,57,46,51,51,54],
[51,57,53,53,0,58,55,47,55,55],
[47,45,46,44,43,0,35,46,41,41],
[54,51,62,55,46,66,0,45,53,58],
[56,54,57,50,54,55,56,0,51,52],
[51,47,50,50,46,60,48,50,0,45],
[49,50,57,47,46,60,43,49,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 76, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,46,51,50,50,45,52,48,51],
[47,0,53,50,48,62,43,56,44,50],
[55,48,0,52,52,61,51,56,50,49],
[50,51,49,0,54,60,47,57,51,50],
[51,53,49,47,0,55,46,53,44,43],
[51,39,40,41,46,0,37,46,41,48],
[56,58,50,54,55,64,0,59,54,53],
[49,45,45,44,48,55,42,0,48,52],
[53,57,51,50,57,60,47,53,0,51],
[50,51,52,51,58,53,48,49,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 77, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,52,65,52,49,56,57,50,55],
[40,0,41,53,48,48,43,50,39,50],
[49,60,0,62,57,51,43,61,50,58],
[36,48,39,0,44,38,41,52,38,49],
[49,53,44,57,0,46,53,56,45,60],
[52,53,50,63,55,0,40,55,46,60],
[45,58,58,60,48,61,0,60,51,58],
[44,51,40,49,45,46,41,0,34,49],
[51,62,51,63,56,55,50,67,0,62],
[46,51,43,52,41,41,43,52,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 78, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,68,70,49,53,86,52,56,74,74],
[33,0,40,38,15,68,41,71,63,89],
[31,61,0,42,15,43,50,64,64,67],
[52,63,59,0,34,52,34,60,52,63],
[48,86,86,67,0,86,68,74,74,74],
[15,33,58,49,15,0,29,55,40,74],
[49,60,51,67,33,72,0,89,74,67],
[45,30,37,41,27,46,12,0,18,46],
[27,38,37,49,27,61,27,83,0,79],
[27,12,34,38,27,27,34,55,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 79, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,87,52,66,63,62,39,50,53,46],
[14,0,7,55,34,50,34,31,23,28],
[49,94,0,73,67,75,64,44,57,81],
[35,46,28,0,43,44,30,27,31,42],
[38,67,34,58,0,60,34,36,45,53],
[39,51,26,57,41,0,31,40,40,42],
[62,67,37,71,67,70,0,55,67,68],
[51,70,57,74,65,61,46,0,65,67],
[48,78,44,70,56,61,34,36,0,58],
[55,73,20,59,48,59,33,34,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 80, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,50,49,55,45,49,47,56,52],
[42,0,53,51,58,56,49,49,49,64],
[51,48,0,51,51,43,40,53,48,54],
[52,50,50,0,58,51,50,48,48,52],
[46,43,50,43,0,45,42,36,48,51],
[56,45,58,50,56,0,56,50,53,47],
[52,52,61,51,59,45,0,54,49,57],
[54,52,48,53,65,51,47,0,50,47],
[45,52,53,53,53,48,52,51,0,55],
[49,37,47,49,50,54,44,54,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 81, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,81,46,44,50,60,54,40,57],
[63,0,79,37,75,67,63,63,57,63],
[20,22,0,30,22,22,22,28,44,49],
[55,64,71,0,64,50,55,44,64,79],
[57,26,79,37,0,48,69,52,52,51],
[51,34,79,51,53,0,43,34,54,59],
[41,38,79,46,32,58,0,32,44,57],
[47,38,73,57,49,67,69,0,63,41],
[61,44,57,37,49,47,57,38,0,55],
[44,38,52,22,50,42,44,60,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 82, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,69,72,60,49,54,37,52,57,51],
[32,0,75,50,33,49,41,44,68,48],
[29,26,0,40,32,41,44,38,55,38],
[41,51,61,0,54,57,61,46,49,46],
[52,68,69,47,0,66,59,56,63,64],
[47,52,60,44,35,0,51,61,58,56],
[64,60,57,40,42,50,0,38,55,35],
[49,57,63,55,45,40,63,0,70,50],
[44,33,46,52,38,43,46,31,0,38],
[50,53,63,55,37,45,66,51,63,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 83, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,64,50,48,59,54,62,46,45],
[50,0,69,58,46,54,57,62,59,52],
[37,32,0,32,39,44,46,50,45,38],
[51,43,69,0,54,63,60,55,47,49],
[53,55,62,47,0,54,55,54,48,48],
[42,47,57,38,47,0,49,51,55,39],
[47,44,55,41,46,52,0,58,51,47],
[39,39,51,46,47,50,43,0,45,39],
[55,42,56,54,53,46,50,56,0,40],
[56,49,63,52,53,62,54,62,61,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 84, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,53,47,36,28,58,28,48,41],
[66,0,64,80,57,49,68,52,56,69],
[48,37,0,50,35,35,39,35,45,28],
[54,21,51,0,48,33,41,36,57,54],
[65,44,66,53,0,50,39,51,58,69],
[73,52,66,68,51,0,41,43,58,75],
[43,33,62,60,62,60,0,44,46,56],
[73,49,66,65,50,58,57,0,57,83],
[53,45,56,44,43,43,55,44,0,50],
[60,32,73,47,32,26,45,18,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 85, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,56,57,52,54,60,60,59,45],
[47,0,59,57,60,56,54,60,52,49],
[45,42,0,52,56,52,57,52,52,41],
[44,44,49,0,47,41,50,52,49,47],
[49,41,45,54,0,49,61,57,47,48],
[47,45,49,60,52,0,54,51,55,45],
[41,47,44,51,40,47,0,57,39,42],
[41,41,49,49,44,50,44,0,48,41],
[42,49,49,52,54,46,62,53,0,53],
[56,52,60,54,53,56,59,60,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 86, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,63,42,46,47,50,54,48,59,52],
[38,0,51,37,40,48,51,45,50,46],
[59,50,0,41,46,56,48,45,62,55],
[55,64,60,0,44,53,51,64,68,53],
[54,61,55,57,0,52,64,49,74,52],
[51,53,45,48,49,0,48,43,56,50],
[47,50,53,50,37,53,0,39,63,48],
[53,56,56,37,52,58,62,0,57,58],
[42,51,39,33,27,45,38,44,0,51],
[49,55,46,48,49,51,53,43,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 87, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,54,57,44,60,40,55,62,41],
[65,0,57,74,52,58,46,55,58,44],
[47,44,0,56,54,60,50,44,59,37],
[44,27,45,0,50,58,29,40,45,41],
[57,49,47,51,0,54,40,42,54,38],
[41,43,41,43,47,0,42,54,53,42],
[61,55,51,72,61,59,0,50,61,57],
[46,46,57,61,59,47,51,0,68,55],
[39,43,42,56,47,48,40,33,0,39],
[60,57,64,60,63,59,44,46,62,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 88, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,47,49,49,48,59,46,50,48],
[53,0,48,56,52,50,59,49,53,50],
[54,53,0,50,54,52,58,51,53,57],
[52,45,51,0,50,49,55,49,46,46],
[52,49,47,51,0,43,52,45,46,53],
[53,51,49,52,58,0,64,51,52,47],
[42,42,43,46,49,37,0,41,49,45],
[55,52,50,52,56,50,60,0,55,52],
[51,48,48,55,55,49,52,46,0,56],
[53,51,44,55,48,54,56,49,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 89, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,53,36,49,42,44,31,50,45],
[59,0,59,46,55,47,51,59,48,56],
[48,42,0,31,61,51,40,36,52,34],
[65,55,70,0,75,54,62,40,58,44],
[52,46,40,26,0,46,44,44,50,49],
[59,54,50,47,55,0,46,44,48,48],
[57,50,61,39,57,55,0,49,46,50],
[70,42,65,61,57,57,52,0,56,50],
[51,53,49,43,51,53,55,45,0,49],
[56,45,67,57,52,53,51,51,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 90, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,61,48,59,52,59,48,60,59],
[46,0,55,46,57,49,54,58,48,55],
[40,46,0,44,54,45,53,53,47,51],
[53,55,57,0,58,47,57,52,55,61],
[42,44,47,43,0,45,50,49,52,51],
[49,52,56,54,56,0,58,49,60,51],
[42,47,48,44,51,43,0,47,46,50],
[53,43,48,49,52,52,54,0,49,55],
[41,53,54,46,49,41,55,52,0,53],
[42,46,50,40,50,50,51,46,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 91, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,52,51,57,50,50,46,45,45],
[48,0,65,51,57,52,51,51,51,48],
[49,36,0,47,55,54,45,47,48,51],
[50,50,54,0,62,59,57,55,46,49],
[44,44,46,39,0,51,49,50,45,44],
[51,49,47,42,50,0,50,51,44,45],
[51,50,56,44,52,51,0,43,50,56],
[55,50,54,46,51,50,58,0,49,44],
[56,50,53,55,56,57,51,52,0,55],
[56,53,50,52,57,56,45,57,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 92, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,45,49,61,42,38,49,28,41],
[58,0,60,48,63,33,27,42,35,33],
[56,41,0,41,39,42,28,27,28,50],
[52,53,60,0,62,40,53,49,50,57],
[40,38,62,39,0,47,31,27,31,38],
[59,68,59,61,54,0,45,80,51,53],
[63,74,73,48,70,56,0,71,48,78],
[52,59,74,52,74,21,30,0,53,56],
[73,66,73,51,70,50,53,48,0,62],
[60,68,51,44,63,48,23,45,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 93, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,61,57,49,46,71,73,50,50],
[44,0,46,38,37,32,41,52,43,36],
[40,55,0,66,53,50,60,66,64,57],
[44,63,35,0,32,35,46,39,51,40],
[52,64,48,69,0,60,61,56,51,56],
[55,69,51,66,41,0,48,61,58,62],
[30,60,41,55,40,53,0,59,54,61],
[28,49,35,62,45,40,42,0,26,36],
[51,58,37,50,50,43,47,75,0,54],
[51,65,44,61,45,39,40,65,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 94, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,64,54,55,57,56,39,56,51,43],
[37,0,40,42,43,53,43,52,38,33],
[47,61,0,59,61,61,47,51,36,50],
[46,59,42,0,46,51,47,59,44,43],
[44,58,40,55,0,52,40,63,44,38],
[45,48,40,50,49,0,46,44,38,34],
[62,58,54,54,61,55,0,66,49,53],
[45,49,50,42,38,57,35,0,53,44],
[50,63,65,57,57,63,52,48,0,57],
[58,68,51,58,63,67,48,57,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 95, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,52,49,65,50,39,49,45,63],
[65,0,46,72,57,52,41,52,47,79],
[49,55,0,67,62,41,42,57,59,82],
[52,29,34,0,46,33,46,44,47,52],
[36,44,39,55,0,43,45,61,44,51],
[51,49,60,68,58,0,42,55,47,78],
[62,60,59,55,56,59,0,60,47,72],
[52,49,44,57,40,46,41,0,39,50],
[56,54,42,54,57,54,54,62,0,70],
[38,22,19,49,50,23,29,51,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 96, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,48,67,45,43,43,53,56,48],
[53,0,41,58,42,58,36,42,58,48],
[53,60,0,53,54,48,47,34,60,47],
[34,43,48,0,38,39,36,42,48,28],
[56,59,47,63,0,46,52,46,65,52],
[58,43,53,62,55,0,47,49,61,61],
[58,65,54,65,49,54,0,53,71,60],
[48,59,67,59,55,52,48,0,64,59],
[45,43,41,53,36,40,30,37,0,42],
[53,53,54,73,49,40,41,42,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 97, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,52,57,50,54,50,45,51,62],
[48,0,48,56,48,46,45,49,47,54],
[49,53,0,54,41,58,48,44,43,53],
[44,45,47,0,39,49,40,42,44,44],
[51,53,60,62,0,57,56,50,51,55],
[47,55,43,52,44,0,41,49,48,50],
[51,56,53,61,45,60,0,46,54,60],
[56,52,57,59,51,52,55,0,46,52],
[50,54,58,57,50,53,47,55,0,51],
[39,47,48,57,46,51,41,49,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 98, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,49,52,42,54,57,48,58,41],
[50,0,48,51,47,49,53,55,47,47],
[52,53,0,56,49,59,58,52,53,54],
[49,50,45,0,55,42,54,45,52,45],
[59,54,52,46,0,51,49,53,59,49],
[47,52,42,59,50,0,52,52,54,44],
[44,48,43,47,52,49,0,48,50,44],
[53,46,49,56,48,49,53,0,60,55],
[43,54,48,49,42,47,51,41,0,40],
[60,54,47,56,52,57,57,46,61,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 99, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,53,77,21,77,77,84,80,73],
[45,0,53,46,14,42,42,49,42,42],
[48,48,0,42,55,66,45,45,45,45],
[24,55,59,0,38,80,80,73,97,97],
[80,87,46,63,0,70,77,77,80,73],
[24,59,35,21,31,0,25,62,69,69],
[24,59,56,21,24,76,0,62,55,48],
[17,52,56,28,24,39,39,0,83,52],
[21,59,56,4,21,32,46,18,0,31],
[28,59,56,4,28,32,53,49,70,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 100, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,59,50,59,57,48,49,46,49],
[49,0,58,51,60,47,52,54,51,53],
[42,43,0,46,45,37,42,42,44,41],
[51,50,55,0,53,49,43,51,41,46],
[42,41,56,48,0,45,38,47,45,48],
[44,54,64,52,56,0,48,57,53,56],
[53,49,59,58,63,53,0,52,55,55],
[52,47,59,50,54,44,49,0,51,48],
[55,50,57,60,56,48,46,50,0,52],
[52,48,60,55,53,45,46,53,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 101, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,52,57,47,49,66,44,49,60],
[48,0,50,54,45,52,53,40,49,45],
[49,51,0,55,49,49,59,41,48,58],
[44,47,46,0,55,44,53,46,44,51],
[54,56,52,46,0,55,55,48,56,56],
[52,49,52,57,46,0,62,53,54,56],
[35,48,42,48,46,39,0,38,47,50],
[57,61,60,55,53,48,63,0,59,59],
[52,52,53,57,45,47,54,42,0,50],
[41,56,43,50,45,45,51,42,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 102, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,53,51,49,49,56,43,51,65],
[48,0,52,47,46,48,40,49,54,55],
[48,49,0,45,42,39,47,44,48,54],
[50,54,56,0,49,43,51,54,49,55],
[52,55,59,52,0,61,52,49,54,54],
[52,53,62,58,40,0,52,53,54,52],
[45,61,54,50,49,49,0,50,58,53],
[58,52,57,47,52,48,51,0,54,59],
[50,47,53,52,47,47,43,47,0,62],
[36,46,47,46,47,49,48,42,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 103, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,39,32,36,45,34,38,31,40],
[60,0,53,43,38,45,50,55,64,58],
[62,48,0,48,50,55,37,37,38,54],
[69,58,53,0,61,69,44,49,47,57],
[65,63,51,40,0,54,44,49,52,57],
[56,56,46,32,47,0,47,45,49,51],
[67,51,64,57,57,54,0,47,53,61],
[63,46,64,52,52,56,54,0,49,50],
[70,37,63,54,49,52,48,52,0,47],
[61,43,47,44,44,50,40,51,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 104, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,53,47,64,52,61,48,46,61],
[44,0,58,42,53,41,68,48,57,53],
[48,43,0,39,45,41,46,61,41,48],
[54,59,62,0,55,44,56,60,67,61],
[37,48,56,46,0,45,46,57,43,47],
[49,60,60,57,56,0,61,70,51,58],
[40,33,55,45,55,40,0,52,52,50],
[53,53,40,41,44,31,49,0,46,52],
[55,44,60,34,58,50,49,55,0,55],
[40,48,53,40,54,43,51,49,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 105, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,49,54,50,50,46,49,56,51],
[54,0,47,43,51,48,38,50,53,56],
[52,54,0,40,54,52,47,41,52,42],
[47,58,61,0,50,50,49,39,55,46],
[51,50,47,51,0,59,53,42,51,55],
[51,53,49,51,42,0,58,54,53,53],
[55,63,54,52,48,43,0,44,56,44],
[52,51,60,62,59,47,57,0,54,51],
[45,48,49,46,50,48,45,47,0,43],
[50,45,59,55,46,48,57,50,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 106, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,52,54,46,51,51,54,46,51],
[57,0,56,48,48,49,54,56,49,52],
[49,45,0,44,39,45,45,49,32,41],
[47,53,57,0,42,48,46,45,50,46],
[55,53,62,59,0,51,56,51,54,49],
[50,52,56,53,50,0,52,47,49,48],
[50,47,56,55,45,49,0,46,45,48],
[47,45,52,56,50,54,55,0,48,54],
[55,52,69,51,47,52,56,53,0,50],
[50,49,60,55,52,53,53,47,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 107, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,56,53,54,47,57,59,49,53],
[49,0,55,63,60,46,51,53,41,55],
[45,46,0,43,49,47,47,51,42,46],
[48,38,58,0,52,50,47,50,51,53],
[47,41,52,49,0,41,48,46,40,46],
[54,55,54,51,60,0,52,50,40,51],
[44,50,54,54,53,49,0,54,48,51],
[42,48,50,51,55,51,47,0,46,51],
[52,60,59,50,61,61,53,55,0,54],
[48,46,55,48,55,50,50,50,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 108, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,57,55,52,51,59,54,42,54],
[43,0,48,45,43,45,47,42,43,47],
[44,53,0,51,52,51,56,50,52,56],
[46,56,50,0,50,56,53,54,53,49],
[49,58,49,51,0,52,57,48,50,54],
[50,56,50,45,49,0,46,49,45,47],
[42,54,45,48,44,55,0,48,49,53],
[47,59,51,47,53,52,53,0,53,51],
[59,58,49,48,51,56,52,48,0,53],
[47,54,45,52,47,54,48,50,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 109, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,70,47,59,57,55,51,51,49],
[55,0,67,82,72,75,50,66,70,63],
[31,34,0,57,53,32,65,33,23,49],
[54,19,44,0,62,60,36,39,39,36],
[42,29,48,39,0,22,32,34,31,22],
[44,26,69,41,79,0,52,63,49,46],
[46,51,36,65,69,49,0,50,52,68],
[50,35,68,62,67,38,51,0,66,46],
[50,31,78,62,70,52,49,35,0,40],
[52,38,52,65,79,55,33,55,61,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 110, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,58,26,34,43,38,40,32,17],
[72,0,74,57,70,42,49,48,74,43],
[43,27,0,45,30,31,31,44,33,41],
[75,44,56,0,55,60,51,45,60,49],
[67,31,71,46,0,30,43,51,49,38],
[58,59,70,41,71,0,44,44,51,47],
[63,52,70,50,58,57,0,63,64,56],
[61,53,57,56,50,57,38,0,54,57],
[69,27,68,41,52,50,37,47,0,48],
[84,58,60,52,63,54,45,44,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 111, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,47,49,52,37,48,46,48,49],
[45,0,40,43,43,30,45,41,46,37],
[54,61,0,54,55,51,57,50,50,49],
[52,58,47,0,51,44,48,40,47,41],
[49,58,46,50,0,39,54,45,49,44],
[64,71,50,57,62,0,62,55,53,54],
[53,56,44,53,47,39,0,49,52,48],
[55,60,51,61,56,46,52,0,52,53],
[53,55,51,54,52,48,49,49,0,47],
[52,64,52,60,57,47,53,48,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 112, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,50,54,51,37,48,39,47,52],
[44,0,51,49,47,40,37,41,43,46],
[51,50,0,55,54,45,42,50,51,55],
[47,52,46,0,54,35,49,40,46,51],
[50,54,47,47,0,39,36,39,54,57],
[64,61,56,66,62,0,55,49,64,62],
[53,64,59,52,65,46,0,51,59,50],
[62,60,51,61,62,52,50,0,57,58],
[54,58,50,55,47,37,42,44,0,57],
[49,55,46,50,44,39,51,43,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 113, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,65,50,64,55,57,59,50,63],
[52,0,60,46,57,47,58,57,44,55],
[36,41,0,59,60,42,52,52,50,42],
[51,55,42,0,57,34,52,46,49,48],
[37,44,41,44,0,43,51,46,42,39],
[46,54,59,67,58,0,50,54,62,54],
[44,43,49,49,50,51,0,62,58,53],
[42,44,49,55,55,47,39,0,39,47],
[51,57,51,52,59,39,43,62,0,46],
[38,46,59,53,62,47,48,54,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 114, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,50,59,47,45,54,42,48,43],
[51,0,53,57,63,54,64,50,55,53],
[51,48,0,47,48,46,57,58,52,44],
[42,44,54,0,45,42,47,53,49,40],
[54,38,53,56,0,47,55,55,47,44],
[56,47,55,59,54,0,55,55,50,49],
[47,37,44,54,46,46,0,47,40,41],
[59,51,43,48,46,46,54,0,49,47],
[53,46,49,52,54,51,61,52,0,46],
[58,48,57,61,57,52,60,54,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 115, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,61,59,60,48,56,61,59,55],
[42,0,54,61,54,55,60,61,54,47],
[40,47,0,52,54,55,54,54,49,49],
[42,40,49,0,60,46,58,63,41,41],
[41,47,47,41,0,45,57,53,33,36],
[53,46,46,55,56,0,54,52,44,47],
[45,41,47,43,44,47,0,47,45,43],
[40,40,47,38,48,49,54,0,38,38],
[42,47,52,60,68,57,56,63,0,54],
[46,54,52,60,65,54,58,63,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 116, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,73,57,59,48,69,56,53,53,69],
[28,0,54,60,34,48,47,30,46,57],
[44,47,0,37,47,53,33,52,43,54],
[42,41,64,0,48,59,41,50,45,61],
[53,67,54,53,0,63,46,60,55,62],
[32,53,48,42,38,0,26,37,31,36],
[45,54,68,60,55,75,0,59,58,62],
[48,71,49,51,41,64,42,0,42,59],
[48,55,58,56,46,70,43,59,0,57],
[32,44,47,40,39,65,39,42,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 117, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,64,62,54,54,46,55,53,57,53],
[37,0,46,39,47,49,43,33,37,37],
[39,55,0,42,47,40,56,41,42,43],
[47,62,59,0,55,54,61,49,56,53],
[47,54,54,46,0,41,51,44,46,47],
[55,52,61,47,60,0,56,44,59,55],
[46,58,45,40,50,45,0,50,55,41],
[48,68,60,52,57,57,51,0,55,52],
[44,64,59,45,55,42,46,46,0,50],
[48,64,58,48,54,46,60,49,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 118, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,60,56,52,58,61,39,41,55],
[43,0,37,47,35,45,45,39,43,59],
[41,64,0,53,52,34,42,37,44,49],
[45,54,48,0,41,59,61,49,45,47],
[49,66,49,60,0,42,55,52,58,64],
[43,56,67,42,59,0,64,60,43,60],
[40,56,59,40,46,37,0,52,39,57],
[62,62,64,52,49,41,49,0,56,65],
[60,58,57,56,43,58,62,45,0,50],
[46,42,52,54,37,41,44,36,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 119, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,55,55,55,55,47,46,51,51],
[51,0,52,44,41,39,41,45,47,49],
[46,49,0,49,41,39,43,42,50,51],
[46,57,52,0,37,39,46,56,51,57],
[46,60,60,64,0,61,47,51,60,60],
[46,62,62,62,40,0,51,57,55,57],
[54,60,58,55,54,50,0,58,54,55],
[55,56,59,45,50,44,43,0,49,54],
[50,54,51,50,41,46,47,52,0,49],
[50,52,50,44,41,44,46,47,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 120, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,53,38,47,53,86,38,62,29],
[57,0,67,24,52,67,42,52,58,67],
[48,34,0,0,43,43,57,38,33,18],
[63,77,101,0,58,86,67,71,73,43],
[54,49,58,43,0,58,39,43,45,43],
[48,34,58,15,43,0,57,43,63,18],
[15,59,44,34,62,44,0,44,43,44],
[63,49,63,30,58,58,57,0,63,48],
[39,43,68,28,56,38,58,38,0,38],
[72,34,83,58,58,83,57,53,63,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 121, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,70,63,63,101,31,82,31,51,101],
[31,0,31,31,31,31,31,31,0,31],
[38,70,0,70,51,69,82,38,51,51],
[38,70,31,0,38,69,69,38,38,51],
[0,70,50,63,0,31,31,31,38,82],
[70,70,32,32,70,0,51,51,51,70],
[19,70,19,32,70,50,0,0,57,70],
[70,70,63,63,70,50,101,0,70,101],
[50,101,50,63,63,50,44,31,0,63],
[0,70,50,50,19,31,31,0,38,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 122, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,53,56,51,55,50,51,50,57],
[49,0,55,49,47,50,51,50,54,50],
[48,46,0,54,47,49,50,48,52,54],
[45,52,47,0,40,49,42,51,48,46],
[50,54,54,61,0,54,48,58,53,49],
[46,51,52,52,47,0,53,51,50,45],
[51,50,51,59,53,48,0,51,54,51],
[50,51,53,50,43,50,50,0,51,49],
[51,47,49,53,48,51,47,50,0,47],
[44,51,47,55,52,56,50,52,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 123, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,55,55,51,60,57,56,53,61],
[53,0,54,45,52,49,49,48,50,61],
[46,47,0,50,48,55,59,42,47,54],
[46,56,51,0,62,47,54,52,45,59],
[50,49,53,39,0,55,49,44,50,54],
[41,52,46,54,46,0,48,43,53,56],
[44,52,42,47,52,53,0,39,47,49],
[45,53,59,49,57,58,62,0,48,64],
[48,51,54,56,51,48,54,53,0,59],
[40,40,47,42,47,45,52,37,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 124, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,67,57,63,58,63,62,36,64,50],
[34,0,29,39,46,50,51,34,55,30],
[44,72,0,59,57,45,60,61,57,53],
[38,62,42,0,48,46,51,39,62,44],
[43,55,44,53,0,60,66,35,54,39],
[38,51,56,55,41,0,61,51,46,68],
[39,50,41,50,35,40,0,38,45,53],
[65,67,40,62,66,50,63,0,62,42],
[37,46,44,39,47,55,56,39,0,45],
[51,71,48,57,62,33,48,59,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 125, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,55,60,44,57,43,52,52,45],
[48,0,45,56,45,46,40,49,46,29],
[46,56,0,57,43,49,44,59,48,46],
[41,45,44,0,42,35,39,44,45,45],
[57,56,58,59,0,52,48,52,57,52],
[44,55,52,66,49,0,48,52,48,49],
[58,61,57,62,53,53,0,61,54,50],
[49,52,42,57,49,49,40,0,49,41],
[49,55,53,56,44,53,47,52,0,48],
[56,72,55,56,49,52,51,60,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 126, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,55,46,56,60,55,55,62,62],
[45,0,53,45,49,48,53,46,56,50],
[46,48,0,43,53,58,57,52,61,57],
[55,56,58,0,49,57,59,52,59,56],
[45,52,48,52,0,57,60,48,64,59],
[41,53,43,44,44,0,54,50,55,52],
[46,48,44,42,41,47,0,53,56,54],
[46,55,49,49,53,51,48,0,56,60],
[39,45,40,42,37,46,45,45,0,49],
[39,51,44,45,42,49,47,41,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 127, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,53,50,52,48,51,56,52,52],
[53,0,52,55,51,48,52,56,49,51],
[48,49,0,44,49,49,45,52,51,47],
[51,46,57,0,53,52,50,59,52,54],
[49,50,52,48,0,52,49,57,46,55],
[53,53,52,49,49,0,52,57,52,57],
[50,49,56,51,52,49,0,54,49,50],
[45,45,49,42,44,44,47,0,49,48],
[49,52,50,49,55,49,52,52,0,51],
[49,50,54,47,46,44,51,53,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 128, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,53,57,54,46,51,53,58,43],
[50,0,63,60,51,40,51,50,60,45],
[48,38,0,57,46,35,28,45,45,34],
[44,41,44,0,47,42,37,46,49,37],
[47,50,55,54,0,49,50,49,55,48],
[55,61,66,59,52,0,53,48,61,61],
[50,50,73,64,51,48,0,46,56,53],
[48,51,56,55,52,53,55,0,53,57],
[43,41,56,52,46,40,45,48,0,33],
[58,56,67,64,53,40,48,44,68,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 129, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,50,52,37,49,66,66,48,60],
[75,0,60,75,37,71,80,66,50,54],
[51,41,0,74,41,41,63,56,53,76],
[49,26,27,0,38,38,40,51,43,47],
[64,64,60,63,0,39,67,75,53,79],
[52,30,60,63,62,0,70,77,62,73],
[35,21,38,61,34,31,0,51,59,41],
[35,35,45,50,26,24,50,0,58,35],
[53,51,48,58,48,39,42,43,0,48],
[41,47,25,54,22,28,60,66,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 130, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,37,49,55,53,48,51,58,41,46],
[64,0,59,59,56,52,56,61,45,55],
[52,42,0,54,54,47,51,51,44,52],
[46,42,47,0,51,47,48,54,38,42],
[48,45,47,50,0,45,52,57,40,54],
[53,49,54,54,56,0,58,62,54,55],
[50,45,50,53,49,43,0,56,43,45],
[43,40,50,47,44,39,45,0,41,46],
[60,56,57,63,61,47,58,60,0,60],
[55,46,49,59,47,46,56,55,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 131, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,46,47,55,41,50,58,52,44],
[49,0,45,46,55,46,49,55,52,43],
[55,56,0,50,57,53,57,65,60,51],
[54,55,51,0,59,49,57,65,55,50],
[46,46,44,42,0,39,47,55,53,39],
[60,55,48,52,62,0,61,65,58,54],
[51,52,44,44,54,40,0,53,48,44],
[43,46,36,36,46,36,48,0,45,36],
[49,49,41,46,48,43,53,56,0,45],
[57,58,50,51,62,47,57,65,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 132, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,48,46,50,59,32,46,34,48],
[60,0,55,50,55,47,42,51,41,60],
[53,46,0,47,50,47,36,43,39,54],
[55,51,54,0,56,49,47,53,50,52],
[51,46,51,45,0,48,34,47,44,56],
[42,54,54,52,53,0,51,43,45,60],
[69,59,65,54,67,50,0,61,57,59],
[55,50,58,48,54,58,40,0,43,54],
[67,60,62,51,57,56,44,58,0,60],
[53,41,47,49,45,41,42,47,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 133, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,33,45,40,41,40,41,34,39],
[50,0,40,53,39,44,42,40,43,41],
[68,61,0,59,49,48,51,52,52,54],
[56,48,42,0,44,41,50,44,44,40],
[61,62,52,57,0,49,49,39,47,45],
[60,57,53,60,52,0,52,44,50,54],
[61,59,50,51,52,49,0,46,41,50],
[60,61,49,57,62,57,55,0,51,43],
[67,58,49,57,54,51,60,50,0,55],
[62,60,47,61,56,47,51,58,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 134, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,46,47,40,48,45,66,45,41],
[50,0,66,61,35,59,47,56,45,47],
[55,35,0,52,53,56,38,75,53,50],
[54,40,49,0,50,38,36,60,34,41],
[61,66,48,51,0,62,58,74,73,56],
[53,42,45,63,39,0,47,57,62,43],
[56,54,63,65,43,54,0,70,62,43],
[35,45,26,41,27,44,31,0,47,30],
[56,56,48,67,28,39,39,54,0,41],
[60,54,51,60,45,58,58,71,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 135, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,42,38,45,50,50,44,36,50],
[55,0,59,53,47,62,52,58,54,52],
[59,42,0,52,49,50,48,44,49,55],
[63,48,49,0,46,65,51,60,49,54],
[56,54,52,55,0,62,47,52,53,58],
[51,39,51,36,39,0,41,41,43,51],
[51,49,53,50,54,60,0,51,52,51],
[57,43,57,41,49,60,50,0,56,46],
[65,47,52,52,48,58,49,45,0,53],
[51,49,46,47,43,50,50,55,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 136, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,47,38,37,44,50,36,37,51],
[65,0,76,62,48,68,69,41,67,71],
[54,25,0,43,40,56,59,40,52,76],
[63,39,58,0,32,59,57,43,57,60],
[64,53,61,69,0,68,71,49,53,76],
[57,33,45,42,33,0,52,39,42,51],
[51,32,42,44,30,49,0,32,43,68],
[65,60,61,58,52,62,69,0,49,71],
[64,34,49,44,48,59,58,52,0,61],
[50,30,25,41,25,50,33,30,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 137, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,56,49,51,40,55,49,45,51],
[50,0,61,54,51,54,74,56,52,56],
[45,40,0,44,53,49,54,46,46,52],
[52,47,57,0,53,47,76,49,57,51],
[50,50,48,48,0,53,62,42,43,47],
[61,47,52,54,48,0,65,54,57,51],
[46,27,47,25,39,36,0,37,39,42],
[52,45,55,52,59,47,64,0,58,44],
[56,49,55,44,58,44,62,43,0,57],
[50,45,49,50,54,50,59,57,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 138, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,55,51,48,51,47,47,52,55],
[56,0,54,55,51,56,53,49,60,53],
[46,47,0,45,44,52,45,42,50,49],
[50,46,56,0,48,45,55,48,54,60],
[53,50,57,53,0,50,55,48,53,59],
[50,45,49,56,51,0,53,51,52,55],
[54,48,56,46,46,48,0,48,54,53],
[54,52,59,53,53,50,53,0,60,62],
[49,41,51,47,48,49,47,41,0,49],
[46,48,52,41,42,46,48,39,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 139, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,34,43,26,45,39,35,56,43],
[71,0,47,51,47,43,60,59,60,61],
[67,54,0,59,39,55,47,59,72,58],
[58,50,42,0,52,54,54,59,48,53],
[75,54,62,49,0,47,67,46,67,58],
[56,58,46,47,54,0,50,58,54,66],
[62,41,54,47,34,51,0,45,53,58],
[66,42,42,42,55,43,56,0,69,59],
[45,41,29,53,34,47,48,32,0,35],
[58,40,43,48,43,35,43,42,66,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 140, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,66,34,40,38,60,45,50,46],
[62,0,64,50,72,31,67,57,65,55],
[35,37,0,50,39,24,30,38,51,47],
[67,51,51,0,59,42,59,59,54,45],
[61,29,62,42,0,29,55,49,54,37],
[63,70,77,59,72,0,57,50,66,63],
[41,34,71,42,46,44,0,46,50,42],
[56,44,63,42,52,51,55,0,53,51],
[51,36,50,47,47,35,51,48,0,32],
[55,46,54,56,64,38,59,50,69,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 141, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,63,61,70,72,63,71,51,49,62],
[38,0,43,44,50,30,49,48,34,39],
[40,58,0,69,58,64,65,63,48,52],
[31,57,32,0,46,30,69,57,51,41],
[29,51,43,55,0,37,54,42,36,48],
[38,71,37,71,64,0,63,60,37,58],
[30,52,36,32,47,38,0,49,32,34],
[50,53,38,44,59,41,52,0,38,52],
[52,67,53,50,65,64,69,63,0,64],
[39,62,49,60,53,43,67,49,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 142, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,30,30,61,57,42,38,37,35],
[54,0,46,58,50,60,55,45,51,48],
[71,55,0,41,55,50,51,54,55,43],
[71,43,60,0,47,49,43,43,53,51],
[40,51,46,54,0,63,60,56,58,53],
[44,41,51,52,38,0,24,32,58,25],
[59,46,50,58,41,77,0,46,61,51],
[63,56,47,58,45,69,55,0,64,54],
[64,50,46,48,43,43,40,37,0,57],
[66,53,58,50,48,76,50,47,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 143, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,71,69,62,61,65,35,60,51],
[52,0,56,59,49,49,52,22,42,34],
[30,45,0,53,39,37,32,21,29,32],
[32,42,48,0,50,52,57,32,37,36],
[39,52,62,51,0,66,49,29,38,35],
[40,52,64,49,35,0,24,18,38,19],
[36,49,69,44,52,77,0,38,47,27],
[66,79,80,69,72,83,63,0,57,28],
[41,59,72,64,63,63,54,44,0,43],
[50,67,69,65,66,82,74,73,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 144, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,61,55,57,38,62,65,56,78],
[48,0,58,59,56,55,64,64,46,79],
[40,43,0,40,68,34,46,35,40,58],
[46,42,61,0,73,57,55,49,38,73],
[44,45,33,28,0,44,47,45,35,61],
[63,46,67,44,57,0,64,62,45,63],
[39,37,55,46,54,37,0,41,39,59],
[36,37,66,52,56,39,60,0,34,71],
[45,55,61,63,66,56,62,67,0,84],
[23,22,43,28,40,38,42,30,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 145, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,41,51,49,57,51,55,50,42],
[48,0,54,45,55,46,48,57,56,52],
[60,47,0,52,50,55,45,54,52,58],
[50,56,49,0,48,57,51,54,59,52],
[52,46,51,53,0,56,51,52,55,56],
[44,55,46,44,45,0,42,47,49,42],
[50,53,56,50,50,59,0,56,49,49],
[46,44,47,47,49,54,45,0,57,51],
[51,45,49,42,46,52,52,44,0,48],
[59,49,43,49,45,59,52,50,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 146, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,54,54,57,59,55,49,48,58],
[53,0,53,56,52,58,53,53,50,58],
[47,48,0,52,47,45,48,41,46,46],
[47,45,49,0,48,51,54,50,43,50],
[44,49,54,53,0,49,56,49,53,52],
[42,43,56,50,52,0,54,43,50,48],
[46,48,53,47,45,47,0,47,48,42],
[52,48,60,51,52,58,54,0,50,60],
[53,51,55,58,48,51,53,51,0,56],
[43,43,55,51,49,53,59,41,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 147, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,50,52,52,56,60,54,58,53],
[47,0,47,49,42,47,55,55,51,58],
[51,54,0,43,36,34,53,42,52,50],
[49,52,58,0,47,48,49,49,54,53],
[49,59,65,54,0,58,62,58,61,54],
[45,54,67,53,43,0,55,52,60,58],
[41,46,48,52,39,46,0,47,46,54],
[47,46,59,52,43,49,54,0,56,53],
[43,50,49,47,40,41,55,45,0,47],
[48,43,51,48,47,43,47,48,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 148, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,48,53,52,50,54,50,55,56],
[51,0,44,34,55,50,51,38,49,57],
[53,57,0,45,52,57,69,58,58,59],
[48,67,56,0,56,58,65,51,51,60],
[49,46,49,45,0,52,53,44,52,51],
[51,51,44,43,49,0,57,44,55,60],
[47,50,32,36,48,44,0,39,52,49],
[51,63,43,50,57,57,62,0,57,63],
[46,52,43,50,49,46,49,44,0,56],
[45,44,42,41,50,41,52,38,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 149, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,47,45,50,49,43,48,41,51],
[60,0,57,53,63,63,50,51,57,57],
[54,44,0,51,56,58,48,50,52,46],
[56,48,50,0,50,61,47,47,53,47],
[51,38,45,51,0,52,45,50,45,45],
[52,38,43,40,49,0,41,53,43,50],
[58,51,53,54,56,60,0,49,52,52],
[53,50,51,54,51,48,52,0,50,52],
[60,44,49,48,56,58,49,51,0,55],
[50,44,55,54,56,51,49,49,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 150, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,55,61,60,54,52,60,52,49],
[51,0,57,56,61,55,59,59,56,48],
[46,44,0,56,50,49,47,48,47,43],
[40,45,45,0,53,47,50,49,44,41],
[41,40,51,48,0,49,49,49,38,38],
[47,46,52,54,52,0,58,55,48,45],
[49,42,54,51,52,43,0,57,45,43],
[41,42,53,52,52,46,44,0,49,46],
[49,45,54,57,63,53,56,52,0,57],
[52,53,58,60,63,56,58,55,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 151, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,59,61,52,55,62,69,68,53],
[52,0,68,67,44,44,63,71,60,48],
[42,33,0,59,48,39,52,34,48,44],
[40,34,42,0,36,34,53,48,50,29],
[49,57,53,65,0,53,62,59,60,43],
[46,57,62,67,48,0,58,57,61,41],
[39,38,49,48,39,43,0,45,45,57],
[32,30,67,53,42,44,56,0,58,45],
[33,41,53,51,41,40,56,43,0,52],
[48,53,57,72,58,60,44,56,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 152, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,60,58,52,50,55,54,37,50],
[45,0,50,57,49,45,44,46,43,49],
[41,51,0,47,55,48,51,50,40,39],
[43,44,54,0,44,46,44,46,39,48],
[49,52,46,57,0,42,53,44,40,50],
[51,56,53,55,59,0,50,42,47,49],
[46,57,50,57,48,51,0,51,35,39],
[47,55,51,55,57,59,50,0,46,53],
[64,58,61,62,61,54,66,55,0,47],
[51,52,62,53,51,52,62,48,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 153, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,59,54,60,53,53,54,49,57],
[46,0,49,52,53,56,38,45,41,37],
[42,52,0,55,57,49,42,45,42,44],
[47,49,46,0,63,44,42,44,36,48],
[41,48,44,38,0,35,35,31,47,41],
[48,45,52,57,66,0,52,42,52,46],
[48,63,59,59,66,49,0,43,50,60],
[47,56,56,57,70,59,58,0,45,53],
[52,60,59,65,54,49,51,56,0,48],
[44,64,57,53,60,55,41,48,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 154, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,63,59,53,46,51,48,56,51,55],
[38,0,53,57,55,47,48,53,48,54],
[42,48,0,50,48,40,42,50,47,54],
[48,44,51,0,48,53,49,55,47,54],
[55,46,53,53,0,58,46,56,51,46],
[50,54,61,48,43,0,45,55,48,53],
[53,53,59,52,55,56,0,56,45,58],
[45,48,51,46,45,46,45,0,39,47],
[50,53,54,54,50,53,56,62,0,58],
[46,47,47,47,55,48,43,54,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 155, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,27,34,48,46,37,48,37,16],
[68,0,40,54,54,48,35,59,41,36],
[74,61,0,66,59,67,52,69,61,50],
[67,47,35,0,57,47,29,67,53,51],
[53,47,42,44,0,36,39,66,36,37],
[55,53,34,54,65,0,30,52,57,32],
[64,66,49,72,62,71,0,72,69,63],
[53,42,32,34,35,49,29,0,39,40],
[64,60,40,48,65,44,32,62,0,40],
[85,65,51,50,64,69,38,61,61,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 156, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,58,51,40,45,41,48,51,51],
[42,0,55,40,43,39,48,52,61,51],
[43,46,0,40,43,46,43,37,47,45],
[50,61,61,0,50,58,49,45,57,53],
[61,58,58,51,0,55,59,50,69,59],
[56,62,55,43,46,0,53,42,58,58],
[60,53,58,52,42,48,0,46,68,58],
[53,49,64,56,51,59,55,0,72,65],
[50,40,54,44,32,43,33,29,0,47],
[50,50,56,48,42,43,43,36,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 157, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,56,67,44,48,61,60,54,54],
[52,0,45,57,55,54,47,59,49,52],
[45,56,0,65,51,58,52,53,47,55],
[34,44,36,0,44,41,54,47,45,45],
[57,46,50,57,0,49,46,53,45,46],
[53,47,43,60,52,0,51,60,58,57],
[40,54,49,47,55,50,0,59,44,62],
[41,42,48,54,48,41,42,0,50,40],
[47,52,54,56,56,43,57,51,0,52],
[47,49,46,56,55,44,39,61,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 158, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,44,42,50,45,36,37,57,41],
[63,0,48,56,61,66,58,50,63,49],
[57,53,0,47,55,51,49,47,52,40],
[59,45,54,0,61,57,51,60,58,51],
[51,40,46,40,0,52,48,44,64,41],
[56,35,50,44,49,0,56,46,50,35],
[65,43,52,50,53,45,0,64,57,50],
[64,51,54,41,57,55,37,0,56,38],
[44,38,49,43,37,51,44,45,0,42],
[60,52,61,50,60,66,51,63,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 159, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,58,43,46,47,47,50,58,46],
[51,0,52,42,58,53,49,54,54,46],
[43,49,0,48,41,43,41,45,40,37],
[58,59,53,0,51,47,49,57,54,53],
[55,43,60,50,0,54,51,51,55,48],
[54,48,58,54,47,0,47,60,54,48],
[54,52,60,52,50,54,0,63,52,54],
[51,47,56,44,50,41,38,0,52,45],
[43,47,61,47,46,47,49,49,0,42],
[55,55,64,48,53,53,47,56,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 160, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,45,39,34,49,43,50,48,50],
[57,0,37,51,38,51,47,49,43,51],
[56,64,0,51,49,59,47,61,57,51],
[62,50,50,0,41,49,49,61,55,52],
[67,63,52,60,0,60,55,57,60,50],
[52,50,42,52,41,0,48,49,60,45],
[58,54,54,52,46,53,0,58,52,49],
[51,52,40,40,44,52,43,0,52,47],
[53,58,44,46,41,41,49,49,0,48],
[51,50,50,49,51,56,52,54,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 161, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,61,46,47,50,51,56,59,46],
[52,0,57,51,60,54,55,59,50,51],
[40,44,0,53,46,46,53,49,42,46],
[55,50,48,0,51,49,55,53,47,54],
[54,41,55,50,0,51,55,55,49,44],
[51,47,55,52,50,0,51,55,45,48],
[50,46,48,46,46,50,0,47,43,42],
[45,42,52,48,46,46,54,0,48,46],
[42,51,59,54,52,56,58,53,0,50],
[55,50,55,47,57,53,59,55,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 162, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,63,43,47,51,46,47,48,54],
[61,0,73,52,51,61,56,57,49,64],
[38,28,0,46,43,47,56,40,41,46],
[58,49,55,0,53,62,54,50,54,55],
[54,50,58,48,0,51,49,52,49,46],
[50,40,54,39,50,0,44,36,52,54],
[55,45,45,47,52,57,0,45,51,64],
[54,44,61,51,49,65,56,0,57,60],
[53,52,60,47,52,49,50,44,0,63],
[47,37,55,46,55,47,37,41,38,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 163, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,51,53,36,57,64,43,38,38],
[42,0,59,61,41,54,54,56,50,60],
[50,42,0,59,54,59,51,58,57,49],
[48,40,42,0,36,49,41,51,46,48],
[65,60,47,65,0,66,49,43,48,47],
[44,47,42,52,35,0,52,47,44,41],
[37,47,50,60,52,49,0,68,59,43],
[58,45,43,50,58,54,33,0,54,39],
[63,51,44,55,53,57,42,47,0,41],
[63,41,52,53,54,60,58,62,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 164, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,54,54,48,46,34,51,42,46],
[52,0,53,57,57,50,50,54,46,35],
[47,48,0,51,46,39,37,51,48,47],
[47,44,50,0,43,37,45,69,39,46],
[53,44,55,58,0,34,43,56,43,38],
[55,51,62,64,67,0,39,67,48,51],
[67,51,64,56,58,62,0,63,44,42],
[50,47,50,32,45,34,38,0,31,38],
[59,55,53,62,58,53,57,70,0,47],
[55,66,54,55,63,50,59,63,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 165, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,101,42,35,35,26,73,26,31,20],
[0,0,0,31,15,0,31,7,15,16],
[59,101,0,31,90,42,73,64,69,58],
[66,70,70,0,63,49,58,49,45,65],
[66,86,11,38,0,49,58,49,7,65],
[75,101,59,52,52,0,73,26,31,16],
[28,70,28,43,43,28,0,28,43,44],
[75,94,37,52,52,75,73,0,52,37],
[70,86,32,56,94,70,58,49,0,58],
[81,85,43,36,36,85,57,64,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 166, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,36,48,55,54,47,50,40,42],
[47,0,38,52,48,59,38,35,43,48],
[65,63,0,59,54,61,57,49,47,55],
[53,49,42,0,41,60,55,44,31,46],
[46,53,47,60,0,53,51,38,31,41],
[47,42,40,41,48,0,33,35,37,38],
[54,63,44,46,50,68,0,44,43,53],
[51,66,52,57,63,66,57,0,49,56],
[61,58,54,70,70,64,58,52,0,48],
[59,53,46,55,60,63,48,45,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 167, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,51,62,56,50,63,59,59,57],
[55,0,47,64,54,52,59,58,61,62],
[50,54,0,54,49,43,57,48,61,49],
[39,37,47,0,53,35,45,48,53,48],
[45,47,52,48,0,38,43,53,49,48],
[51,49,58,66,63,0,55,54,59,54],
[38,42,44,56,58,46,0,55,44,46],
[42,43,53,53,48,47,46,0,43,50],
[42,40,40,48,52,42,57,58,0,48],
[44,39,52,53,53,47,55,51,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 168, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,54,56,52,48,50,54,48,48],
[48,0,47,54,47,48,45,53,54,45],
[47,54,0,52,46,51,47,59,54,43],
[45,47,49,0,45,48,46,55,47,46],
[49,54,55,56,0,53,53,60,55,48],
[53,53,50,53,48,0,53,59,55,49],
[51,56,54,55,48,48,0,57,56,51],
[47,48,42,46,41,42,44,0,43,48],
[53,47,47,54,46,46,45,58,0,42],
[53,56,58,55,53,52,50,53,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 169, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,56,50,56,55,60,55,55,54],
[54,0,47,50,54,58,46,61,56,63],
[45,54,0,52,54,57,49,52,52,52],
[51,51,49,0,54,58,53,56,59,58],
[45,47,47,47,0,50,49,45,50,48],
[46,43,44,43,51,0,41,52,52,51],
[41,55,52,48,52,60,0,48,54,55],
[46,40,49,45,56,49,53,0,54,53],
[46,45,49,42,51,49,47,47,0,47],
[47,38,49,43,53,50,46,48,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 170, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,52,52,56,51,52,49,49,50],
[50,0,55,47,54,54,54,52,53,50],
[49,46,0,42,51,49,47,50,45,41],
[49,54,59,0,62,56,56,55,56,48],
[45,47,50,39,0,53,49,51,50,52],
[50,47,52,45,48,0,49,49,46,48],
[49,47,54,45,52,52,0,52,49,49],
[52,49,51,46,50,52,49,0,52,53],
[52,48,56,45,51,55,52,49,0,48],
[51,51,60,53,49,53,52,48,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 171, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,47,59,47,48,52,50,48,53],
[41,0,44,41,44,39,49,47,35,52],
[54,57,0,55,48,48,54,59,50,57],
[42,60,46,0,48,36,49,46,46,52],
[54,57,53,53,0,51,49,51,51,58],
[53,62,53,65,50,0,56,51,50,53],
[49,52,47,52,52,45,0,48,42,48],
[51,54,42,55,50,50,53,0,46,51],
[53,66,51,55,50,51,59,55,0,52],
[48,49,44,49,43,48,53,50,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 172, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,75,53,53,67,66,60,60,50],
[49,0,54,46,58,50,56,58,56,60],
[26,47,0,40,37,52,34,52,49,43],
[48,55,61,0,67,66,64,69,69,60],
[48,43,64,34,0,51,59,51,53,46],
[34,51,49,35,50,0,47,50,46,42],
[35,45,67,37,42,54,0,52,47,56],
[41,43,49,32,50,51,49,0,54,38],
[41,45,52,32,48,55,54,47,0,39],
[51,41,58,41,55,59,45,63,62,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 173, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,50,56,53,53,49,50,49,50],
[45,0,44,50,50,46,47,48,46,45],
[51,57,0,50,54,52,48,47,52,43],
[45,51,51,0,49,48,52,50,47,48],
[48,51,47,52,0,50,45,48,46,45],
[48,55,49,53,51,0,50,50,46,54],
[52,54,53,49,56,51,0,53,48,52],
[51,53,54,51,53,51,48,0,51,53],
[52,55,49,54,55,55,53,50,0,51],
[51,56,58,53,56,47,49,48,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 174, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,57,43,43,49,46,49,44,58],
[48,0,62,48,49,48,46,53,52,55],
[44,39,0,46,50,43,42,49,50,51],
[58,53,55,0,53,52,46,49,51,46],
[58,52,51,48,0,51,53,57,55,52],
[52,53,58,49,50,0,52,57,58,61],
[55,55,59,55,48,49,0,51,51,60],
[52,48,52,52,44,44,50,0,45,55],
[57,49,51,50,46,43,50,56,0,58],
[43,46,50,55,49,40,41,46,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 175, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,42,45,48,41,43,53,40,36],
[49,0,39,39,39,24,30,22,34,30],
[59,62,0,55,42,66,37,46,36,39],
[56,62,46,0,37,50,51,40,32,16],
[53,62,59,64,0,50,71,71,49,29],
[60,77,35,51,51,0,59,54,57,38],
[58,71,64,50,30,42,0,47,46,38],
[48,79,55,61,30,47,54,0,47,34],
[61,67,65,69,52,44,55,54,0,61],
[65,71,62,85,72,63,63,67,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 176, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,80,48,57,68,58,58,51,73,57],
[21,0,31,46,46,38,56,38,34,48],
[53,70,0,68,57,53,50,56,65,64],
[44,55,33,0,65,49,56,37,60,62],
[33,55,44,36,0,36,44,42,47,28],
[43,63,48,52,65,0,49,44,54,61],
[43,45,51,45,57,52,0,42,62,58],
[50,63,45,64,59,57,59,0,67,57],
[28,67,36,41,54,47,39,34,0,41],
[44,53,37,39,73,40,43,44,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 177, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,53,63,55,63,59,53,72,51],
[51,0,46,65,58,51,69,51,62,54],
[48,55,0,67,57,54,53,52,60,58],
[38,36,34,0,43,39,53,42,51,47],
[46,43,44,58,0,49,47,42,58,56],
[38,50,47,62,52,0,51,47,56,61],
[42,32,48,48,54,50,0,48,66,58],
[48,50,49,59,59,54,53,0,65,56],
[29,39,41,50,43,45,35,36,0,51],
[50,47,43,54,45,40,43,45,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 178, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,50,44,49,50,50,53,57,55],
[54,0,47,50,55,46,52,52,55,50],
[51,54,0,53,53,52,58,50,58,56],
[57,51,48,0,61,47,45,51,51,50],
[52,46,48,40,0,45,49,51,49,49],
[51,55,49,54,56,0,65,51,57,60],
[51,49,43,56,52,36,0,50,53,45],
[48,49,51,50,50,50,51,0,50,51],
[44,46,43,50,52,44,48,51,0,52],
[46,51,45,51,52,41,56,50,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 179, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,47,51,55,50,58,47,51,45],
[48,0,51,50,60,51,54,39,52,46],
[54,50,0,45,50,49,45,41,44,44],
[50,51,56,0,55,48,54,51,53,45],
[46,41,51,46,0,44,43,40,47,44],
[51,50,52,53,57,0,51,42,52,53],
[43,47,56,47,58,50,0,45,51,47],
[54,62,60,50,61,59,56,0,56,49],
[50,49,57,48,54,49,50,45,0,46],
[56,55,57,56,57,48,54,52,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 180, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,48,45,53,32,47,46,69,30],
[49,0,51,40,66,36,56,55,64,59],
[53,50,0,49,69,39,54,44,65,49],
[56,61,52,0,50,33,43,43,62,38],
[48,35,32,51,0,25,37,45,57,32],
[69,65,62,68,76,0,39,64,78,70],
[54,45,47,58,64,62,0,28,60,37],
[55,46,57,58,56,37,73,0,57,42],
[32,37,36,39,44,23,41,44,0,21],
[71,42,52,63,69,31,64,59,80,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 181, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,47,62,55,57,52,58,67,47],
[56,0,55,69,56,62,60,54,69,50],
[54,46,0,75,51,73,57,58,76,60],
[39,32,26,0,40,45,45,46,44,45],
[46,45,50,61,0,52,56,53,64,44],
[44,39,28,56,49,0,49,39,51,39],
[49,41,44,56,45,52,0,53,62,43],
[43,47,43,55,48,62,48,0,56,51],
[34,32,25,57,37,50,39,45,0,37],
[54,51,41,56,57,62,58,50,64,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 182, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,33,33,37,54,28,30,34,30],
[79,0,35,58,61,60,60,43,56,58],
[68,66,0,60,62,74,62,47,58,60],
[68,43,41,0,47,61,47,51,49,67],
[64,40,39,54,0,59,44,50,45,42],
[47,41,27,40,42,0,46,22,36,48],
[73,41,39,54,57,55,0,54,45,42],
[71,58,54,50,51,79,47,0,47,64],
[67,45,43,52,56,65,56,54,0,53],
[71,43,41,34,59,53,59,37,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 183, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,56,48,38,46,37,35,47,45],
[57,0,59,48,41,52,39,45,53,54],
[45,42,0,34,33,39,30,38,45,39],
[53,53,67,0,37,50,39,46,58,52],
[63,60,68,64,0,62,55,50,62,53],
[55,49,62,51,39,0,43,48,56,53],
[64,62,71,62,46,58,0,53,57,60],
[66,56,63,55,51,53,48,0,53,58],
[54,48,56,43,39,45,44,48,0,51],
[56,47,62,49,48,48,41,43,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 184, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,55,49,42,42,46,43,40,49],
[56,0,55,52,45,42,41,45,39,43],
[46,46,0,53,43,45,48,44,38,42],
[52,49,48,0,54,40,54,41,43,40],
[59,56,58,47,0,48,47,62,47,45],
[59,59,56,61,53,0,53,54,55,47],
[55,60,53,47,54,48,0,60,44,54],
[58,56,57,60,39,47,41,0,48,44],
[61,62,63,58,54,46,57,53,0,54],
[52,58,59,61,56,54,47,57,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 185, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,49,50,53,51,49,47,52,52],
[54,0,59,49,48,57,58,54,55,47],
[52,42,0,46,52,51,46,53,47,54],
[51,52,55,0,54,56,55,58,44,56],
[48,53,49,47,0,56,51,49,57,58],
[50,44,50,45,45,0,57,46,51,44],
[52,43,55,46,50,44,0,51,54,48],
[54,47,48,43,52,55,50,0,46,52],
[49,46,54,57,44,50,47,55,0,53],
[49,54,47,45,43,57,53,49,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 186, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,62,52,57,60,47,49,59,51],
[52,0,53,55,50,54,54,56,59,53],
[39,48,0,51,39,50,42,52,47,46],
[49,46,50,0,52,52,44,52,52,49],
[44,51,62,49,0,46,39,51,55,51],
[41,47,51,49,55,0,49,48,40,50],
[54,47,59,57,62,52,0,51,54,51],
[52,45,49,49,50,53,50,0,55,48],
[42,42,54,49,46,61,47,46,0,49],
[50,48,55,52,50,51,50,53,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 187, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,51,53,44,46,57,50,41,56],
[39,0,44,54,50,57,53,67,41,31],
[50,57,0,51,44,49,52,55,42,33],
[48,47,50,0,43,41,70,51,37,46],
[57,51,57,58,0,55,62,69,51,33],
[55,44,52,60,46,0,61,45,40,40],
[44,48,49,31,39,40,0,46,39,29],
[51,34,46,50,32,56,55,0,41,34],
[60,60,59,64,50,61,62,60,0,44],
[45,70,68,55,68,61,72,67,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 188, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,55,56,49,44,50,52,47,55],
[45,0,47,65,41,42,59,49,60,50],
[46,54,0,59,49,44,63,50,59,53],
[45,36,42,0,40,38,46,43,43,42],
[52,60,52,61,0,51,53,52,54,50],
[57,59,57,63,50,0,74,62,63,55],
[51,42,38,55,48,27,0,47,43,52],
[49,52,51,58,49,39,54,0,50,52],
[54,41,42,58,47,38,58,51,0,47],
[46,51,48,59,51,46,49,49,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 189, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,60,49,50,50,52,50,50,54],
[52,0,49,33,38,44,39,47,41,46],
[41,52,0,46,43,45,49,52,46,45],
[52,68,55,0,50,54,56,61,61,54],
[51,63,58,51,0,47,50,63,54,47],
[51,57,56,47,54,0,51,52,54,51],
[49,62,52,45,51,50,0,56,51,51],
[51,54,49,40,38,49,45,0,47,48],
[51,60,55,40,47,47,50,54,0,48],
[47,55,56,47,54,50,50,53,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 190, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,59,54,47,58,59,51,49,57],
[42,0,62,43,42,55,54,41,43,54],
[42,39,0,45,42,46,48,39,44,43],
[47,58,56,0,47,58,55,50,49,52],
[54,59,59,54,0,53,57,45,51,56],
[43,46,55,43,48,0,55,41,40,52],
[42,47,53,46,44,46,0,39,36,56],
[50,60,62,51,56,60,62,0,53,58],
[52,58,57,52,50,61,65,48,0,58],
[44,47,58,49,45,49,45,43,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 191, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,101,51,73,73,60,73,88,67,32],
[0,0,6,50,6,13,60,60,50,28],
[50,95,0,95,91,82,95,82,63,50],
[28,51,6,0,6,47,47,88,9,56],
[28,95,10,95,0,41,95,88,63,50],
[41,88,19,54,60,0,92,88,54,19],
[28,41,6,54,6,9,0,84,63,13],
[13,41,19,13,13,13,17,0,13,13],
[34,51,38,92,38,47,38,88,0,47],
[69,73,51,45,51,82,88,88,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 192, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,45,56,77,56,45,35,61,53],
[48,0,48,41,77,59,38,54,49,32],
[56,53,0,62,79,87,36,43,49,61],
[45,60,39,0,79,60,54,43,38,61],
[24,24,22,22,0,39,23,30,38,28],
[45,42,14,41,62,0,7,57,52,52],
[56,63,65,47,78,94,0,68,63,52],
[66,47,58,58,71,44,33,0,58,79],
[40,52,52,63,63,49,38,43,0,53],
[48,69,40,40,73,49,49,22,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 193, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,42,42,49,23,30,23,72,42],
[94,0,65,65,72,94,23,23,94,65],
[59,36,0,7,30,52,30,23,59,23],
[59,36,94,0,101,52,59,52,101,94],
[52,29,71,0,0,52,52,23,94,52],
[78,7,49,49,49,0,30,23,78,49],
[71,78,71,42,49,71,0,65,78,71],
[78,78,78,49,78,78,36,0,78,78],
[29,7,42,0,7,23,23,23,0,0],
[59,36,78,7,49,52,30,23,101,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 194, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,44,48,48,55,52,44,53,56],
[51,0,52,48,51,57,41,46,50,51],
[57,49,0,46,48,54,49,50,58,60],
[53,53,55,0,46,52,46,48,53,54],
[53,50,53,55,0,51,51,51,50,56],
[46,44,47,49,50,0,44,43,50,48],
[49,60,52,55,50,57,0,49,53,52],
[57,55,51,53,50,58,52,0,54,57],
[48,51,43,48,51,51,48,47,0,54],
[45,50,41,47,45,53,49,44,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 195, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,67,58,53,57,49,54,57,55,58],
[34,0,51,42,44,43,49,51,45,47],
[43,50,0,43,50,41,49,62,42,50],
[48,59,58,0,53,46,48,52,52,52],
[44,57,51,48,0,51,48,53,48,50],
[52,58,60,55,50,0,55,54,50,49],
[47,52,52,53,53,46,0,49,45,54],
[44,50,39,49,48,47,52,0,47,50],
[46,56,59,49,53,51,56,54,0,51],
[43,54,51,49,51,52,47,51,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 196, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,56,49,51,48,58,58,56,52],
[49,0,52,52,52,47,54,62,49,51],
[45,49,0,42,48,41,54,54,53,51],
[52,49,59,0,50,54,61,58,55,49],
[50,49,53,51,0,53,52,57,51,54],
[53,54,60,47,48,0,55,57,52,53],
[43,47,47,40,49,46,0,58,54,46],
[43,39,47,43,44,44,43,0,43,46],
[45,52,48,46,50,49,47,58,0,45],
[49,50,50,52,47,48,55,55,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 197, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,71,65,53,51,46,61,57,64],
[43,0,62,61,69,51,73,69,78,61],
[30,39,0,38,62,46,41,44,41,56],
[36,40,63,0,42,60,49,67,55,40],
[48,32,39,59,0,46,47,69,55,57],
[50,50,55,41,55,0,60,55,58,45],
[55,28,60,52,54,41,0,57,54,59],
[40,32,57,34,32,46,44,0,43,48],
[44,23,60,46,46,43,47,58,0,43],
[37,40,45,61,44,56,42,53,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 198, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,68,57,49,49,52,49,59,37,51],
[33,0,44,37,39,52,44,46,32,46],
[44,57,0,51,44,50,45,41,35,58],
[52,64,50,0,51,46,46,54,40,56],
[52,62,57,50,0,47,51,60,44,62],
[49,49,51,55,54,0,53,71,53,42],
[52,57,56,55,50,48,0,73,53,46],
[42,55,60,47,41,30,28,0,44,48],
[64,69,66,61,57,48,48,57,0,59],
[50,55,43,45,39,59,55,53,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 199, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,54,56,50,51,54,48,48,49],
[58,0,64,62,56,53,60,57,44,54],
[47,37,0,52,40,34,47,42,37,44],
[45,39,49,0,49,44,46,42,43,46],
[51,45,61,52,0,50,59,50,40,53],
[50,48,67,57,51,0,55,48,46,58],
[47,41,54,55,42,46,0,48,41,47],
[53,44,59,59,51,53,53,0,54,56],
[53,57,64,58,61,55,60,47,0,57],
[52,47,57,55,48,43,54,45,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 101, 200, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebb/mebb_10_101.csv", index=False, header=False)