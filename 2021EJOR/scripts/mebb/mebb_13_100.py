
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,58,49,43,41,51,32,36,49,46,48,45,49],
[42,0,33,29,41,43,32,36,44,30,48,35,43],
[51,67,0,46,52,46,34,35,53,44,54,46,57],
[57,71,54,0,60,49,47,33,54,52,61,63,57],
[59,59,48,40,0,45,32,33,47,35,49,33,57],
[49,57,54,51,55,0,28,40,59,44,57,44,49],
[68,68,66,53,68,72,0,50,54,53,71,68,67],
[64,64,65,67,67,60,50,0,58,55,65,70,66],
[51,56,47,46,53,41,46,42,0,45,58,45,53],
[54,70,56,48,65,56,47,45,55,0,58,63,72],
[52,52,46,39,51,43,29,35,42,42,0,36,47],
[55,65,54,37,67,56,32,30,55,37,64,0,69],
[51,57,43,43,43,51,33,34,47,28,53,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 1, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,51,49,44,45,50,55,38,52,57,46,43],
[58,0,58,59,45,58,53,59,47,53,59,60,51],
[49,42,0,51,46,54,51,55,41,49,53,52,50],
[51,41,49,0,47,48,53,56,46,50,55,53,46],
[56,55,54,53,0,57,53,61,50,54,62,54,51],
[55,42,46,52,43,0,51,55,42,51,55,53,50],
[50,47,49,47,47,49,0,57,40,55,52,53,50],
[45,41,45,44,39,45,43,0,42,46,50,46,49],
[62,53,59,54,50,58,60,58,0,60,68,60,54],
[48,47,51,50,46,49,45,54,40,0,47,48,43],
[43,41,47,45,38,45,48,50,32,53,0,46,41],
[54,40,48,47,46,47,47,54,40,52,54,0,47],
[57,49,50,54,49,50,50,51,46,57,59,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 2, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,60,52,60,49,51,47,49,49,54,50,55],
[42,0,44,44,51,42,45,51,52,50,40,43,45],
[40,56,0,50,50,50,42,48,44,47,45,39,52],
[48,56,50,0,56,50,52,49,49,45,54,43,47],
[40,49,50,44,0,34,45,51,46,35,43,42,49],
[51,58,50,50,66,0,55,62,57,52,47,45,52],
[49,55,58,48,55,45,0,57,47,53,48,47,50],
[53,49,52,51,49,38,43,0,51,43,54,42,50],
[51,48,56,51,54,43,53,49,0,44,43,49,52],
[51,50,53,55,65,48,47,57,56,0,54,49,50],
[46,60,55,46,57,53,52,46,57,46,0,45,48],
[50,57,61,57,58,55,53,58,51,51,55,0,53],
[45,55,48,53,51,48,50,50,48,50,52,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 3, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,53,45,54,54,55,56,52,52,54,52,46],
[51,0,53,50,58,47,59,50,45,49,60,47,52],
[47,47,0,40,51,47,51,48,48,47,42,44,41],
[55,50,60,0,65,60,69,60,60,52,53,56,56],
[46,42,49,35,0,46,55,48,45,45,50,47,42],
[46,53,53,40,54,0,47,49,52,43,54,50,41],
[45,41,49,31,45,53,0,43,47,39,53,42,41],
[44,50,52,40,52,51,57,0,50,46,54,49,45],
[48,55,52,40,55,48,53,50,0,47,59,52,48],
[48,51,53,48,55,57,61,54,53,0,54,52,59],
[46,40,58,47,50,46,47,46,41,46,0,40,43],
[48,53,56,44,53,50,58,51,48,48,60,0,48],
[54,48,59,44,58,59,59,55,52,41,57,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 4, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,54,51,50,59,58,54,58,58,48,45,49],
[46,0,40,40,39,48,50,47,45,47,42,43,43],
[46,60,0,47,44,58,52,55,52,55,55,53,52],
[49,60,53,0,53,51,47,55,56,59,45,50,45],
[50,61,56,47,0,55,54,54,54,54,51,50,48],
[41,52,42,49,45,0,46,47,41,50,44,47,50],
[42,50,48,53,46,54,0,47,47,50,46,46,44],
[46,53,45,45,46,53,53,0,54,50,43,45,47],
[42,55,48,44,46,59,53,46,0,49,50,46,46],
[42,53,45,41,46,50,50,50,51,0,49,51,48],
[52,58,45,55,49,56,54,57,50,51,0,42,52],
[55,57,47,50,50,53,54,55,54,49,58,0,53],
[51,57,48,55,52,50,56,53,54,52,48,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 5, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,46,55,55,45,60,44,48,55,60,51,59],
[52,0,53,49,54,39,43,51,42,44,56,48,52],
[54,47,0,56,47,47,49,54,47,56,60,56,56],
[45,51,44,0,46,47,52,47,45,53,54,51,46],
[45,46,53,54,0,52,56,53,41,52,58,50,57],
[55,61,53,53,48,0,60,50,50,56,58,53,46],
[40,57,51,48,44,40,0,45,54,46,46,51,50],
[56,49,46,53,47,50,55,0,49,51,54,56,52],
[52,58,53,55,59,50,46,51,0,70,58,54,56],
[45,56,44,47,48,44,54,49,30,0,63,51,47],
[40,44,40,46,42,42,54,46,42,37,0,51,40],
[49,52,44,49,50,47,49,44,46,49,49,0,44],
[41,48,44,54,43,54,50,48,44,53,60,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 6, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,54,48,47,54,52,51,60,56,56,56,61],
[49,0,44,45,45,45,57,48,56,52,53,51,53],
[46,56,0,49,45,62,56,56,55,62,53,45,57],
[52,55,51,0,51,58,50,46,55,54,47,51,58],
[53,55,55,49,0,58,53,55,56,58,54,52,47],
[46,55,38,42,42,0,54,50,48,58,56,50,51],
[48,43,44,50,47,46,0,52,55,59,57,50,56],
[49,52,44,54,45,50,48,0,59,60,50,49,52],
[40,44,45,45,44,52,45,41,0,59,49,50,59],
[44,48,38,46,42,42,41,40,41,0,50,41,49],
[44,47,47,53,46,44,43,50,51,50,0,53,61],
[44,49,55,49,48,50,50,51,50,59,47,0,57],
[39,47,43,42,53,49,44,48,41,51,39,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 7, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,53,54,52,51,46,44,38,43,45,49,54],
[48,0,52,43,42,51,45,50,40,44,42,47,48],
[47,48,0,43,49,47,48,35,44,38,44,45,51],
[46,57,57,0,45,52,55,48,44,48,43,53,53],
[48,58,51,55,0,57,54,50,48,54,49,55,56],
[49,49,53,48,43,0,48,40,45,46,44,43,50],
[54,55,52,45,46,52,0,46,46,48,43,49,52],
[56,50,65,52,50,60,54,0,50,44,51,56,58],
[62,60,56,56,52,55,54,50,0,44,53,48,57],
[57,56,62,52,46,54,52,56,56,0,54,55,55],
[55,58,56,57,51,56,57,49,47,46,0,51,60],
[51,53,55,47,45,57,51,44,52,45,49,0,55],
[46,52,49,47,44,50,48,42,43,45,40,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 8, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,37,46,45,43,49,50,52,49,40,43,50,46],
[63,0,54,52,55,49,59,59,57,54,51,50,51],
[54,46,0,39,50,49,52,54,50,45,44,47,50],
[55,48,61,0,49,45,56,53,61,50,56,54,63],
[57,45,50,51,0,54,53,54,52,48,44,52,51],
[51,51,51,55,46,0,51,54,47,44,43,53,60],
[50,41,48,44,47,49,0,57,58,43,41,47,50],
[48,41,46,47,46,46,43,0,44,39,44,44,41],
[51,43,50,39,48,53,42,56,0,42,39,41,42],
[60,46,55,50,52,56,57,61,58,0,50,54,55],
[57,49,56,44,56,57,59,56,61,50,0,55,54],
[50,50,53,46,48,47,53,56,59,46,45,0,52],
[54,49,50,37,49,40,50,59,58,45,46,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 9, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,64,47,57,53,47,61,49,52,55,60,61,53],
[36,0,43,51,42,35,44,41,44,37,40,38,35],
[53,57,0,55,50,52,51,46,49,59,53,44,58],
[43,49,45,0,51,48,56,42,43,41,52,43,43],
[47,58,50,49,0,42,50,52,39,49,50,45,50],
[53,65,48,52,58,0,50,42,55,56,56,46,53],
[39,56,49,44,50,50,0,42,50,46,48,49,51],
[51,59,54,58,48,58,58,0,58,54,58,52,55],
[48,56,51,57,61,45,50,42,0,53,55,53,59],
[45,63,41,59,51,44,54,46,47,0,52,50,42],
[40,60,47,48,50,44,52,42,45,48,0,47,45],
[39,62,56,57,55,54,51,48,47,50,53,0,52],
[47,65,42,57,50,47,49,45,41,58,55,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 10, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,52,46,49,55,42,50,47,47,42,57,50],
[53,0,47,45,44,58,42,57,47,43,37,58,40],
[48,53,0,50,54,51,51,66,56,50,50,61,46],
[54,55,50,0,53,59,47,52,57,60,45,63,47],
[51,56,46,47,0,59,51,57,58,58,51,56,54],
[45,42,49,41,41,0,36,57,41,48,34,42,43],
[58,58,49,53,49,64,0,58,54,55,49,61,57],
[50,43,34,48,43,43,42,0,43,45,44,47,39],
[53,53,44,43,42,59,46,57,0,42,40,49,43],
[53,57,50,40,42,52,45,55,58,0,46,49,47],
[58,63,50,55,49,66,51,56,60,54,0,66,59],
[43,42,39,37,44,58,39,53,51,51,34,0,48],
[50,60,54,53,46,57,43,61,57,53,41,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 11, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,49,62,47,45,57,53,60,67,44,50,60],
[58,0,58,57,58,44,67,58,66,66,48,62,53],
[51,42,0,57,61,50,57,45,48,59,40,49,62],
[38,43,43,0,54,36,53,37,39,49,27,39,35],
[53,42,39,46,0,50,53,49,41,52,36,41,46],
[55,56,50,64,50,0,68,59,62,67,53,62,63],
[43,33,43,47,47,32,0,45,37,48,29,41,30],
[47,42,55,63,51,41,55,0,46,59,41,51,51],
[40,34,52,61,59,38,63,54,0,59,43,45,45],
[33,34,41,51,48,33,52,41,41,0,29,39,48],
[56,52,60,73,64,47,71,59,57,71,0,60,61],
[50,38,51,61,59,38,59,49,55,61,40,0,65],
[40,47,38,65,54,37,70,49,55,52,39,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 12, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,47,55,52,55,52,56,55,51,58,56,49],
[39,0,43,45,45,46,39,48,44,39,52,46,41],
[53,57,0,54,47,52,52,50,48,48,56,49,48],
[45,55,46,0,53,46,46,50,53,48,61,47,48],
[48,55,53,47,0,46,52,52,47,41,58,51,43],
[45,54,48,54,54,0,47,49,52,44,60,51,49],
[48,61,48,54,48,53,0,54,51,51,51,48,47],
[44,52,50,50,48,51,46,0,45,43,61,43,51],
[45,56,52,47,53,48,49,55,0,45,53,54,43],
[49,61,52,52,59,56,49,57,55,0,58,59,49],
[42,48,44,39,42,40,49,39,47,42,0,46,41],
[44,54,51,53,49,49,52,57,46,41,54,0,41],
[51,59,52,52,57,51,53,49,57,51,59,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 13, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,37,40,41,43,46,36,44,50,52,46,50,51],
[63,0,50,48,50,49,43,54,52,52,48,55,53],
[60,50,0,54,52,60,57,58,52,50,54,56,57],
[59,52,46,0,46,43,48,59,47,54,49,48,49],
[57,50,48,54,0,47,49,59,55,57,53,47,52],
[54,51,40,57,53,0,46,59,54,57,48,61,58],
[64,57,43,52,51,54,0,54,54,57,55,60,56],
[56,46,42,41,41,41,46,0,48,49,52,54,48],
[50,48,48,53,45,46,46,52,0,49,48,50,52],
[48,48,50,46,43,43,43,51,51,0,51,48,45],
[54,52,46,51,47,52,45,48,52,49,0,56,50],
[50,45,44,52,53,39,40,46,50,52,44,0,52],
[49,47,43,51,48,42,44,52,48,55,50,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 14, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,48,48,49,52,56,55,49,53,59,51,57],
[50,0,50,50,54,56,59,63,48,59,61,50,56],
[52,50,0,57,52,55,55,55,49,50,62,44,59],
[52,50,43,0,49,45,50,56,47,51,56,44,54],
[51,46,48,51,0,54,53,50,43,49,63,49,55],
[48,44,45,55,46,0,45,46,44,57,56,38,50],
[44,41,45,50,47,55,0,47,49,47,53,47,55],
[45,37,45,44,50,54,53,0,44,42,51,42,47],
[51,52,51,53,57,56,51,56,0,57,59,50,60],
[47,41,50,49,51,43,53,58,43,0,54,41,48],
[41,39,38,44,37,44,47,49,41,46,0,37,37],
[49,50,56,56,51,62,53,58,50,59,63,0,60],
[43,44,41,46,45,50,45,53,40,52,63,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 15, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,48,45,42,44,50,45,50,55,52,37,43],
[44,0,52,52,49,56,54,58,57,56,57,51,49],
[52,48,0,50,42,42,52,44,49,54,54,41,33],
[55,48,50,0,43,53,51,49,55,45,49,50,41],
[58,51,58,57,0,53,56,52,50,56,55,45,45],
[56,44,58,47,47,0,54,56,52,48,52,43,45],
[50,46,48,49,44,46,0,45,44,55,52,44,41],
[55,42,56,51,48,44,55,0,56,54,47,40,52],
[50,43,51,45,50,48,56,44,0,48,55,45,35],
[45,44,46,55,44,52,45,46,52,0,49,40,36],
[48,43,46,51,45,48,48,53,45,51,0,47,46],
[63,49,59,50,55,57,56,60,55,60,53,0,46],
[57,51,67,59,55,55,59,48,65,64,54,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 16, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,52,56,50,45,57,56,55,56,48,55,39],
[42,0,43,47,38,41,43,46,38,32,32,47,41],
[48,57,0,53,41,45,45,54,49,42,42,37,35],
[44,53,47,0,50,40,39,52,45,50,47,50,42],
[50,62,59,50,0,51,53,47,53,50,54,57,40],
[55,59,55,60,49,0,53,52,45,47,39,52,52],
[43,57,55,61,47,47,0,47,47,43,39,62,48],
[44,54,46,48,53,48,53,0,43,52,38,50,36],
[45,62,51,55,47,55,53,57,0,50,37,57,43],
[44,68,58,50,50,53,57,48,50,0,46,56,43],
[52,68,58,53,46,61,61,62,63,54,0,60,47],
[45,53,63,50,43,48,38,50,43,44,40,0,39],
[61,59,65,58,60,48,52,64,57,57,53,61,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 17, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,55,46,41,46,39,42,49,50,55,53,47],
[57,0,66,60,45,59,47,58,57,53,63,56,54],
[45,34,0,47,41,44,39,44,47,44,56,54,43],
[54,40,53,0,48,52,40,42,49,49,54,50,48],
[59,55,59,52,0,52,50,58,55,50,55,53,55],
[54,41,56,48,48,0,54,52,57,52,57,59,56],
[61,53,61,60,50,46,0,51,52,63,58,58,60],
[58,42,56,58,42,48,49,0,53,47,60,50,54],
[51,43,53,51,45,43,48,47,0,48,56,50,54],
[50,47,56,51,50,48,37,53,52,0,55,51,53],
[45,37,44,46,45,43,42,40,44,45,0,45,47],
[47,44,46,50,47,41,42,50,50,49,55,0,44],
[53,46,57,52,45,44,40,46,46,47,53,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 18, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,44,49,50,54,53,51,57,55,49,44,54],
[50,0,43,49,49,52,50,55,58,46,49,45,56],
[56,57,0,54,56,55,56,59,60,56,48,57,57],
[51,51,46,0,52,56,54,56,51,56,51,50,56],
[50,51,44,48,0,59,48,56,50,54,47,58,56],
[46,48,45,44,41,0,44,50,56,50,43,46,47],
[47,50,44,46,52,56,0,49,55,53,49,56,53],
[49,45,41,44,44,50,51,0,52,44,46,50,52],
[43,42,40,49,50,44,45,48,0,44,44,48,47],
[45,54,44,44,46,50,47,56,56,0,46,54,48],
[51,51,52,49,53,57,51,54,56,54,0,58,50],
[56,55,43,50,42,54,44,50,52,46,42,0,49],
[46,44,43,44,44,53,47,48,53,52,50,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 19, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,47,54,41,55,39,57,50,56,50,54,48],
[47,0,48,52,44,55,46,46,45,52,48,48,48],
[53,52,0,55,51,55,44,54,45,58,49,48,56],
[46,48,45,0,43,43,46,47,40,44,43,51,39],
[59,56,49,57,0,62,59,58,45,53,56,57,41],
[45,45,45,57,38,0,39,44,32,50,45,46,40],
[61,54,56,54,41,61,0,62,51,56,49,58,49],
[43,54,46,53,42,56,38,0,38,47,51,51,43],
[50,55,55,60,55,68,49,62,0,48,54,55,51],
[44,48,42,56,47,50,44,53,52,0,52,52,37],
[50,52,51,57,44,55,51,49,46,48,0,47,39],
[46,52,52,49,43,54,42,49,45,48,53,0,48],
[52,52,44,61,59,60,51,57,49,63,61,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 20, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,51,56,50,43,45,48,46,50,46,51,51],
[54,0,51,52,50,48,55,56,51,52,48,62,48],
[49,49,0,47,44,44,55,49,45,51,47,57,46],
[44,48,53,0,46,40,53,49,42,44,50,53,51],
[50,50,56,54,0,46,51,50,51,45,48,59,53],
[57,52,56,60,54,0,54,53,51,48,53,62,48],
[55,45,45,47,49,46,0,50,44,51,40,51,53],
[52,44,51,51,50,47,50,0,42,46,49,55,56],
[54,49,55,58,49,49,56,58,0,56,52,54,58],
[50,48,49,56,55,52,49,54,44,0,55,66,48],
[54,52,53,50,52,47,60,51,48,45,0,56,52],
[49,38,43,47,41,38,49,45,46,34,44,0,45],
[49,52,54,49,47,52,47,44,42,52,48,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 21, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,56,59,58,49,50,60,54,49,54,51,60],
[50,0,54,56,55,54,58,54,58,51,54,55,55],
[44,46,0,55,54,48,48,51,54,47,52,50,53],
[41,44,45,0,48,36,50,47,50,45,49,44,47],
[42,45,46,52,0,46,45,48,52,42,43,49,56],
[51,46,52,64,54,0,59,55,60,51,58,60,65],
[50,42,52,50,55,41,0,53,54,49,50,46,51],
[40,46,49,53,52,45,47,0,56,49,50,49,56],
[46,42,46,50,48,40,46,44,0,46,45,45,48],
[51,49,53,55,58,49,51,51,54,0,42,58,57],
[46,46,48,51,57,42,50,50,55,58,0,45,52],
[49,45,50,56,51,40,54,51,55,42,55,0,53],
[40,45,47,53,44,35,49,44,52,43,48,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 22, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,41,44,44,55,48,46,44,43,50,45,50],
[60,0,52,45,59,74,48,52,55,59,54,54,60],
[59,48,0,49,52,57,61,51,48,51,54,49,46],
[56,55,51,0,64,56,52,50,47,46,52,58,47],
[56,41,48,36,0,60,49,52,51,46,45,49,42],
[45,26,43,44,40,0,50,44,47,43,51,36,39],
[52,52,39,48,51,50,0,46,46,46,52,49,52],
[54,48,49,50,48,56,54,0,55,52,52,50,45],
[56,45,52,53,49,53,54,45,0,42,52,53,47],
[57,41,49,54,54,57,54,48,58,0,54,54,49],
[50,46,46,48,55,49,48,48,48,46,0,39,47],
[55,46,51,42,51,64,51,50,47,46,61,0,47],
[50,40,54,53,58,61,48,55,53,51,53,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 23, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,64,54,51,62,66,41,58,64,62,55,68],
[48,0,60,53,67,63,61,34,60,59,51,41,58],
[36,40,0,49,49,57,52,37,55,50,43,46,58],
[46,47,51,0,50,58,62,50,60,53,53,47,52],
[49,33,51,50,0,54,45,26,48,44,54,36,56],
[38,37,43,42,46,0,53,44,47,49,45,43,53],
[34,39,48,38,55,47,0,38,60,57,47,41,57],
[59,66,63,50,74,56,62,0,61,56,51,53,65],
[42,40,45,40,52,53,40,39,0,42,40,37,41],
[36,41,50,47,56,51,43,44,58,0,41,47,47],
[38,49,57,47,46,55,53,49,60,59,0,56,66],
[45,59,54,53,64,57,59,47,63,53,44,0,59],
[32,42,42,48,44,47,43,35,59,53,34,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 24, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,36,35,48,39,55,38,47,51,45,53,53],
[51,0,49,53,57,56,58,58,53,56,50,63,63],
[64,51,0,52,69,61,60,49,49,53,52,61,62],
[65,47,48,0,52,59,59,59,60,58,45,61,66],
[52,43,31,48,0,45,54,51,53,50,42,56,58],
[61,44,39,41,55,0,50,50,47,49,51,60,58],
[45,42,40,41,46,50,0,46,61,51,49,57,59],
[62,42,51,41,49,50,54,0,49,47,44,56,68],
[53,47,51,40,47,53,39,51,0,47,42,50,56],
[49,44,47,42,50,51,49,53,53,0,43,62,53],
[55,50,48,55,58,49,51,56,58,57,0,57,67],
[47,37,39,39,44,40,43,44,50,38,43,0,57],
[47,37,38,34,42,42,41,32,44,47,33,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 25, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,38,43,50,41,43,48,47,44,46,47,42],
[51,0,48,45,47,53,49,46,50,53,51,57,48],
[62,52,0,53,54,55,49,58,52,57,54,61,52],
[57,55,47,0,56,54,45,50,53,51,58,60,50],
[50,53,46,44,0,42,39,38,48,49,48,47,50],
[59,47,45,46,58,0,51,47,46,48,54,49,47],
[57,51,51,55,61,49,0,49,53,54,51,52,52],
[52,54,42,50,62,53,51,0,49,53,54,55,48],
[53,50,48,47,52,54,47,51,0,54,48,51,53],
[56,47,43,49,51,52,46,47,46,0,52,55,52],
[54,49,46,42,52,46,49,46,52,48,0,51,50],
[53,43,39,40,53,51,48,45,49,45,49,0,51],
[58,52,48,50,50,53,48,52,47,48,50,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 26, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,55,53,51,50,52,47,50,53,54,53,51],
[52,0,56,52,41,53,62,42,44,45,48,49,49],
[45,44,0,53,49,52,47,44,47,50,38,45,48],
[47,48,47,0,45,52,49,53,43,44,46,44,48],
[49,59,51,55,0,66,60,53,51,44,51,51,53],
[50,47,48,48,34,0,57,51,39,40,46,34,50],
[48,38,53,51,40,43,0,49,44,37,38,38,43],
[53,58,56,47,47,49,51,0,48,44,42,41,51],
[50,56,53,57,49,61,56,52,0,55,50,51,54],
[47,55,50,56,56,60,63,56,45,0,43,45,55],
[46,52,62,54,49,54,62,58,50,57,0,47,55],
[47,51,55,56,49,66,62,59,49,55,53,0,54],
[49,51,52,52,47,50,57,49,46,45,45,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 27, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,42,48,47,47,36,45,39,42,38,41,44],
[55,0,54,52,65,54,49,58,64,53,60,48,56],
[58,46,0,58,55,52,50,55,50,55,53,51,51],
[52,48,42,0,52,46,42,47,49,45,38,37,42],
[53,35,45,48,0,33,41,40,50,49,41,39,42],
[53,46,48,54,67,0,43,48,53,55,52,45,47],
[64,51,50,58,59,57,0,55,65,57,50,44,51],
[55,42,45,53,60,52,45,0,55,49,36,42,45],
[61,36,50,51,50,47,35,45,0,55,43,38,43],
[58,47,45,55,51,45,43,51,45,0,52,38,46],
[62,40,47,62,59,48,50,64,57,48,0,47,47],
[59,52,49,63,61,55,56,58,62,62,53,0,51],
[56,44,49,58,58,53,49,55,57,54,53,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 28, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,51,56,51,46,46,53,37,40,57,42,41],
[45,0,44,47,46,43,43,37,33,43,51,39,41],
[49,56,0,54,53,44,45,49,50,48,44,46,55],
[44,53,46,0,43,43,45,54,40,48,43,39,48],
[49,54,47,57,0,48,47,49,43,51,53,45,46],
[54,57,56,57,52,0,44,49,37,39,54,47,50],
[54,57,55,55,53,56,0,57,52,50,51,50,51],
[47,63,51,46,51,51,43,0,52,42,54,45,51],
[63,67,50,60,57,63,48,48,0,55,56,53,57],
[60,57,52,52,49,61,50,58,45,0,55,48,59],
[43,49,56,57,47,46,49,46,44,45,0,44,45],
[58,61,54,61,55,53,50,55,47,52,56,0,56],
[59,59,45,52,54,50,49,49,43,41,55,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 29, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,12,34,63,39,17,38,29,23,33,59,1],
[87,0,54,40,64,60,62,62,62,38,43,60,55],
[88,46,0,44,88,66,68,56,56,42,66,66,71],
[66,60,56,0,63,50,56,50,49,54,47,61,44],
[37,36,12,37,0,38,22,20,44,37,43,59,22],
[61,40,34,50,62,0,51,48,40,42,41,52,40],
[83,38,32,44,78,49,0,54,49,23,46,54,56],
[62,38,44,50,80,52,46,0,50,22,57,52,32],
[71,38,44,51,56,60,51,50,0,22,38,43,50],
[77,62,58,46,63,58,77,78,78,0,72,71,66],
[67,57,34,53,57,59,54,43,62,28,0,65,57],
[41,40,34,39,41,48,46,48,57,29,35,0,42],
[99,45,29,56,78,60,44,68,50,34,43,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 30, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,47,51,53,58,53,50,53,49,45,51,50],
[50,0,43,48,51,54,50,54,49,46,45,51,45],
[53,57,0,57,61,58,55,53,52,51,50,53,49],
[49,52,43,0,56,54,53,59,51,44,50,53,46],
[47,49,39,44,0,45,47,49,42,46,41,39,40],
[42,46,42,46,55,0,43,51,44,43,48,47,40],
[47,50,45,47,53,57,0,53,47,44,44,44,40],
[50,46,47,41,51,49,47,0,51,39,41,47,45],
[47,51,48,49,58,56,53,49,0,46,46,49,52],
[51,54,49,56,54,57,56,61,54,0,50,51,47],
[55,55,50,50,59,52,56,59,54,50,0,51,52],
[49,49,47,47,61,53,56,53,51,49,49,0,43],
[50,55,51,54,60,60,60,55,48,53,48,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 31, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,55,41,41,28,45,47,81,53,44,53,45],
[56,0,58,54,56,39,55,47,89,47,69,55,61],
[45,42,0,24,52,38,26,23,67,39,31,27,44],
[59,46,76,0,47,60,47,45,65,50,63,41,77],
[59,44,48,53,0,52,47,49,53,42,33,45,61],
[72,61,62,40,48,0,52,36,73,55,47,49,47],
[55,45,74,53,53,48,0,37,76,49,50,36,45],
[53,53,77,55,51,64,63,0,68,39,44,48,58],
[19,11,33,35,47,27,24,32,0,35,28,22,38],
[47,53,61,50,58,45,51,61,65,0,58,43,65],
[56,31,69,37,67,53,50,56,72,42,0,42,63],
[47,45,73,59,55,51,64,52,78,57,58,0,56],
[55,39,56,23,39,53,55,42,62,35,37,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 32, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,52,57,50,53,60,67,43,59,59,53,49],
[38,0,46,50,44,52,54,58,53,45,59,43,52],
[48,54,0,46,50,59,65,64,40,51,57,38,52],
[43,50,54,0,53,65,57,56,51,50,56,42,50],
[50,56,50,47,0,70,58,63,49,51,57,53,65],
[47,48,41,35,30,0,50,52,33,36,45,28,45],
[40,46,35,43,42,50,0,45,37,44,51,46,45],
[33,42,36,44,37,48,55,0,47,43,51,42,44],
[57,47,60,49,51,67,63,53,0,51,58,51,67],
[41,55,49,50,49,64,56,57,49,0,62,48,61],
[41,41,43,44,43,55,49,49,42,38,0,36,46],
[47,57,62,58,47,72,54,58,49,52,64,0,75],
[51,48,48,50,35,55,55,56,33,39,54,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 33, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,49,52,54,45,48,55,62,39,51,48,49],
[48,0,42,58,49,45,47,48,56,39,39,53,46],
[51,58,0,56,51,50,49,52,51,46,52,62,54],
[48,42,44,0,52,47,47,46,43,41,46,54,56],
[46,51,49,48,0,40,47,50,53,44,44,49,57],
[55,55,50,53,60,0,51,54,65,59,56,66,65],
[52,53,51,53,53,49,0,55,58,47,42,48,54],
[45,52,48,54,50,46,45,0,51,45,40,54,47],
[38,44,49,57,47,35,42,49,0,43,42,56,44],
[61,61,54,59,56,41,53,55,57,0,51,62,55],
[49,61,48,54,56,44,58,60,58,49,0,61,59],
[52,47,38,46,51,34,52,46,44,38,39,0,47],
[51,54,46,44,43,35,46,53,56,45,41,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 34, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,58,30,31,22,35,41,36,51,22,10,68],
[67,0,59,63,51,40,53,79,50,75,65,43,82],
[42,41,0,34,26,26,36,37,49,59,15,18,67],
[70,37,66,0,45,23,56,55,43,68,23,38,70],
[69,49,74,55,0,51,59,59,73,59,27,35,93],
[78,60,74,77,49,0,65,56,52,66,49,23,75],
[65,47,64,44,41,35,0,54,53,79,16,36,86],
[59,21,63,45,41,44,46,0,54,81,41,39,73],
[64,50,51,57,27,48,47,46,0,35,42,21,79],
[49,25,41,32,41,34,21,19,65,0,13,3,76],
[78,35,85,77,73,51,84,59,58,87,0,60,87],
[90,57,82,62,65,77,64,61,79,97,40,0,83],
[32,18,33,30,7,25,14,27,21,24,13,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 35, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,44,47,36,30,57,46,44,50,58,37,40],
[60,0,64,57,54,59,57,59,60,59,53,49,50],
[56,36,0,56,61,38,55,42,49,55,45,40,50],
[53,43,44,0,47,33,53,49,38,51,55,40,32],
[64,46,39,53,0,38,52,66,43,62,61,52,52],
[70,41,62,67,62,0,67,57,63,67,64,46,48],
[43,43,45,47,48,33,0,48,56,40,51,50,53],
[54,41,58,51,34,43,52,0,43,51,66,43,53],
[56,40,51,62,57,37,44,57,0,57,41,43,61],
[50,41,45,49,38,33,60,49,43,0,57,36,57],
[42,47,55,45,39,36,49,34,59,43,0,41,34],
[63,51,60,60,48,54,50,57,57,64,59,0,55],
[60,50,50,68,48,52,47,47,39,43,66,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 36, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,34,42,33,39,44,38,32,28,43,39,38],
[55,0,49,51,56,49,62,42,55,44,54,52,59],
[66,51,0,54,60,53,65,46,51,55,58,54,59],
[58,49,46,0,49,47,64,43,45,48,50,41,53],
[67,44,40,51,0,48,47,32,51,35,47,42,48],
[61,51,47,53,52,0,69,46,59,48,55,47,47],
[56,38,35,36,53,31,0,42,36,40,45,34,42],
[62,58,54,57,68,54,58,0,47,50,59,51,45],
[68,45,49,55,49,41,64,53,0,40,54,41,47],
[72,56,45,52,65,52,60,50,60,0,50,46,57],
[57,46,42,50,53,45,55,41,46,50,0,49,40],
[61,48,46,59,58,53,66,49,59,54,51,0,47],
[62,41,41,47,52,53,58,55,53,43,60,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 37, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,48,40,69,53,58,55,74,39,35,58,57],
[38,0,45,50,49,48,40,39,45,26,31,46,66],
[52,55,0,36,65,41,64,47,55,54,53,43,59],
[60,50,64,0,59,53,62,54,52,41,52,61,71],
[31,51,35,41,0,31,32,38,39,22,42,37,62],
[47,52,59,47,69,0,66,35,64,44,52,41,62],
[42,60,36,38,68,34,0,53,46,35,41,52,69],
[45,61,53,46,62,65,47,0,60,42,67,57,74],
[26,55,45,48,61,36,54,40,0,31,32,35,60],
[61,74,46,59,78,56,65,58,69,0,64,53,63],
[65,69,47,48,58,48,59,33,68,36,0,54,56],
[42,54,57,39,63,59,48,43,65,47,46,0,65],
[43,34,41,29,38,38,31,26,40,37,44,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 38, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,47,46,46,48,39,51,59,39,58,48,45],
[58,0,51,46,52,55,49,48,59,51,55,58,49],
[53,49,0,46,44,53,52,50,54,48,53,59,43],
[54,54,54,0,50,48,40,46,50,44,47,54,45],
[54,48,56,50,0,52,40,54,61,40,55,51,40],
[52,45,47,52,48,0,48,53,54,37,48,56,45],
[61,51,48,60,60,52,0,60,59,51,52,51,54],
[49,52,50,54,46,47,40,0,61,40,53,52,47],
[41,41,46,50,39,46,41,39,0,40,49,47,33],
[61,49,52,56,60,63,49,60,60,0,58,60,53],
[42,45,47,53,45,52,48,47,51,42,0,52,43],
[52,42,41,46,49,44,49,48,53,40,48,0,49],
[55,51,57,55,60,55,46,53,67,47,57,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 39, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,40,49,40,43,46,42,43,39,51,44,53],
[62,0,46,57,45,54,50,51,56,56,56,52,58],
[60,54,0,63,51,53,50,51,58,53,53,54,63],
[51,43,37,0,38,47,38,36,44,44,39,42,54],
[60,55,49,62,0,54,49,53,58,52,57,57,66],
[57,46,47,53,46,0,46,43,54,47,50,51,58],
[54,50,50,62,51,54,0,53,51,54,56,51,54],
[58,49,49,64,47,57,47,0,53,48,56,50,64],
[57,44,42,56,42,46,49,47,0,51,51,46,56],
[61,44,47,56,48,53,46,52,49,0,51,50,60],
[49,44,47,61,43,50,44,44,49,49,0,44,54],
[56,48,46,58,43,49,49,50,54,50,56,0,59],
[47,42,37,46,34,42,46,36,44,40,46,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 40, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,51,47,39,45,44,51,44,45,43,52,49],
[54,0,46,57,45,56,51,56,47,49,57,53,56],
[49,54,0,48,41,49,43,54,48,48,46,50,47],
[53,43,52,0,52,45,51,48,46,45,56,54,54],
[61,55,59,48,0,50,48,58,52,60,57,54,51],
[55,44,51,55,50,0,49,59,54,55,57,47,54],
[56,49,57,49,52,51,0,60,56,43,53,51,60],
[49,44,46,52,42,41,40,0,43,39,42,42,45],
[56,53,52,54,48,46,44,57,0,49,59,53,54],
[55,51,52,55,40,45,57,61,51,0,44,59,47],
[57,43,54,44,43,43,47,58,41,56,0,52,52],
[48,47,50,46,46,53,49,58,47,41,48,0,59],
[51,44,53,46,49,46,40,55,46,53,48,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 41, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,49,50,41,37,52,31,54,46,57,52,54],
[39,0,52,48,53,27,50,23,48,45,63,47,59],
[51,48,0,20,27,28,58,35,37,38,40,36,35],
[50,52,80,0,58,62,58,48,55,59,65,70,65],
[59,47,73,42,0,29,67,36,46,49,54,63,54],
[63,73,72,38,71,0,51,43,58,48,63,53,71],
[48,50,42,42,33,49,0,43,42,47,41,40,41],
[69,77,65,52,64,57,57,0,47,57,49,71,62],
[46,52,63,45,54,42,58,53,0,52,46,50,60],
[54,55,62,41,51,52,53,43,48,0,43,61,53],
[43,37,60,35,46,37,59,51,54,57,0,37,52],
[48,53,64,30,37,47,60,29,50,39,63,0,52],
[46,41,65,35,46,29,59,38,40,47,48,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 42, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,53,51,53,58,60,43,55,55,58,46,58],
[54,0,52,48,44,50,64,44,42,49,48,42,57],
[47,48,0,48,51,55,54,46,51,48,52,42,52],
[49,52,52,0,55,65,46,42,46,60,55,50,48],
[47,56,49,45,0,51,56,42,52,53,49,45,50],
[42,50,45,35,49,0,44,38,54,44,45,35,54],
[40,36,46,54,44,56,0,50,45,48,42,42,45],
[57,56,54,58,58,62,50,0,57,55,58,50,56],
[45,58,49,54,48,46,55,43,0,45,53,44,51],
[45,51,52,40,47,56,52,45,55,0,41,46,41],
[42,52,48,45,51,55,58,42,47,59,0,48,58],
[54,58,58,50,55,65,58,50,56,54,52,0,65],
[42,43,48,52,50,46,55,44,49,59,42,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 43, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,56,56,60,57,61,55,61,61,51,45,69],
[39,0,46,51,49,55,55,45,58,43,35,46,56],
[44,54,0,50,47,53,55,54,55,48,41,53,52],
[44,49,50,0,39,58,59,44,58,45,37,47,54],
[40,51,53,61,0,50,57,51,52,46,42,41,59],
[43,45,47,42,50,0,55,43,48,42,43,37,51],
[39,45,45,41,43,45,0,49,48,37,36,46,50],
[45,55,46,56,49,57,51,0,58,41,29,41,52],
[39,42,45,42,48,52,52,42,0,47,38,25,41],
[39,57,52,55,54,58,63,59,53,0,40,42,57],
[49,65,59,63,58,57,64,71,62,60,0,56,62],
[55,54,47,53,59,63,54,59,75,58,44,0,62],
[31,44,48,46,41,49,50,48,59,43,38,38,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 44, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,50,56,58,52,69,56,50,61,42,55,44],
[39,0,46,50,46,54,57,44,45,45,55,39,37],
[50,54,0,50,46,48,56,47,50,46,58,46,44],
[44,50,50,0,48,52,58,49,43,52,52,61,47],
[42,54,54,52,0,52,52,53,39,53,48,44,30],
[48,46,52,48,48,0,56,50,41,48,50,40,38],
[31,43,44,42,48,44,0,46,39,43,54,32,39],
[44,56,53,51,47,50,54,0,45,52,53,46,44],
[50,55,50,57,61,59,61,55,0,46,57,52,55],
[39,55,54,48,47,52,57,48,54,0,47,44,34],
[58,45,42,48,52,50,46,47,43,53,0,36,51],
[45,61,54,39,56,60,68,54,48,56,64,0,50],
[56,63,56,53,70,62,61,56,45,66,49,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 45, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,49,55,43,49,44,46,50,59,47,58,46],
[53,0,57,60,52,46,48,52,53,56,55,55,50],
[51,43,0,45,44,40,45,52,45,50,49,46,48],
[45,40,55,0,38,40,51,42,55,60,46,59,46],
[57,48,56,62,0,56,62,63,62,56,61,62,59],
[51,54,60,60,44,0,58,41,49,64,60,61,51],
[56,52,55,49,38,42,0,54,51,60,43,52,56],
[54,48,48,58,37,59,46,0,67,59,60,56,46],
[50,47,55,45,38,51,49,33,0,59,53,46,45],
[41,44,50,40,44,36,40,41,41,0,50,41,43],
[53,45,51,54,39,40,57,40,47,50,0,47,43],
[42,45,54,41,38,39,48,44,54,59,53,0,46],
[54,50,52,54,41,49,44,54,55,57,57,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 46, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,6,35,40,49,45,6,20,44,31,30,44],
[53,0,28,55,70,65,64,40,68,79,75,58,53],
[94,72,0,70,49,97,71,57,45,75,88,61,93],
[65,45,30,0,70,67,58,33,65,50,73,35,63],
[60,30,51,30,0,67,25,58,48,54,55,31,49],
[51,35,3,33,33,0,28,8,26,51,30,32,33],
[55,36,29,42,75,72,0,36,73,79,58,37,61],
[94,60,43,67,42,92,64,0,63,69,61,56,86],
[80,32,55,35,52,74,27,37,0,79,55,40,56],
[56,21,25,50,46,49,21,31,21,0,46,11,44],
[69,25,12,27,45,70,42,39,45,54,0,16,46],
[70,42,39,65,69,68,63,44,60,89,84,0,89],
[56,47,7,37,51,67,39,14,44,56,54,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 47, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,55,58,49,58,53,57,60,56,63,49,54],
[46,0,49,54,52,57,51,64,62,55,59,46,48],
[45,51,0,55,48,61,56,58,57,52,54,48,58],
[42,46,45,0,46,59,56,59,58,49,54,49,54],
[51,48,52,54,0,56,50,57,52,59,47,53,58],
[42,43,39,41,44,0,51,58,52,50,54,46,51],
[47,49,44,44,50,49,0,51,45,52,49,44,49],
[43,36,42,41,43,42,49,0,45,46,46,42,43],
[40,38,43,42,48,48,55,55,0,50,50,43,42],
[44,45,48,51,41,50,48,54,50,0,49,48,52],
[37,41,46,46,53,46,51,54,50,51,0,49,52],
[51,54,52,51,47,54,56,58,57,52,51,0,53],
[46,52,42,46,42,49,51,57,58,48,48,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 48, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,70,56,32,43,39,47,56,75,27,61,36,60],
[30,0,52,23,57,24,57,42,66,28,29,37,43],
[44,48,0,47,62,39,72,71,81,42,57,51,66],
[68,77,53,0,72,72,81,56,65,46,58,64,76],
[57,43,38,28,0,11,38,29,70,0,47,31,48],
[61,76,61,28,89,0,62,42,61,46,61,64,47],
[53,43,28,19,62,38,0,28,62,46,53,36,47],
[44,58,29,44,71,58,72,0,75,61,77,79,76],
[25,34,19,35,30,39,38,25,0,28,24,38,57],
[73,72,58,54,100,54,54,39,72,0,72,66,73],
[39,71,43,42,53,39,47,23,76,28,0,46,42],
[64,63,49,36,69,36,64,21,62,34,54,0,64],
[40,57,34,24,52,53,53,24,43,27,58,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 49, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,46,48,52,52,47,50,54,53,46,46,44],
[51,0,52,56,55,46,47,48,47,56,49,53,49],
[54,48,0,56,59,51,56,49,51,52,55,49,53],
[52,44,44,0,49,46,41,38,46,40,45,45,45],
[48,45,41,51,0,48,44,42,45,50,51,54,45],
[48,54,49,54,52,0,45,51,50,55,56,47,48],
[53,53,44,59,56,55,0,55,47,59,48,50,50],
[50,52,51,62,58,49,45,0,50,49,48,48,54],
[46,53,49,54,55,50,53,50,0,53,48,49,49],
[47,44,48,60,50,45,41,51,47,0,45,47,47],
[54,51,45,55,49,44,52,52,52,55,0,49,50],
[54,47,51,55,46,53,50,52,51,53,51,0,51],
[56,51,47,55,55,52,50,46,51,53,50,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 50, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,46,43,61,50,58,55,35,55,59,33,60],
[45,0,46,52,50,45,52,53,58,59,52,50,61],
[54,54,0,59,53,75,42,60,62,60,79,61,70],
[57,48,41,0,60,56,37,51,63,54,63,52,65],
[39,50,47,40,0,47,50,50,40,53,64,45,53],
[50,55,25,44,53,0,49,54,40,49,60,45,58],
[42,48,58,63,50,51,0,62,51,54,67,42,65],
[45,47,40,49,50,46,38,0,46,40,50,47,48],
[65,42,38,37,60,60,49,54,0,51,58,56,61],
[45,41,40,46,47,51,46,60,49,0,65,47,59],
[41,48,21,37,36,40,33,50,42,35,0,33,43],
[67,50,39,48,55,55,58,53,44,53,67,0,65],
[40,39,30,35,47,42,35,52,39,41,57,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 51, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,54,52,51,56,48,57,51,63,52,55,57],
[45,0,48,45,46,61,44,54,46,60,46,50,49],
[46,52,0,52,48,53,46,46,45,61,43,54,48],
[48,55,48,0,49,51,48,50,50,59,44,53,48],
[49,54,52,51,0,52,42,52,48,58,40,58,52],
[44,39,47,49,48,0,39,46,44,48,44,56,50],
[52,56,54,52,58,61,0,60,48,61,53,62,60],
[43,46,54,50,48,54,40,0,44,54,42,49,45],
[49,54,55,50,52,56,52,56,0,58,48,54,48],
[37,40,39,41,42,52,39,46,42,0,36,46,45],
[48,54,57,56,60,56,47,58,52,64,0,59,59],
[45,50,46,47,42,44,38,51,46,54,41,0,47],
[43,51,52,52,48,50,40,55,52,55,41,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 52, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,55,51,49,40,50,50,50,51,55,65,22],
[62,0,60,61,71,56,71,60,66,38,78,59,22],
[45,40,0,34,56,17,32,60,38,26,49,26,15],
[49,39,66,0,70,27,43,43,49,54,59,58,19],
[51,29,44,30,0,6,49,49,33,34,38,37,4],
[60,44,83,73,94,0,58,49,64,64,76,75,42],
[50,29,68,57,51,42,0,63,27,49,61,21,17],
[50,40,40,57,51,51,37,0,50,33,56,44,11],
[50,34,62,51,67,36,73,50,0,44,56,54,28],
[49,62,74,46,66,36,51,67,56,0,82,72,55],
[45,22,51,41,62,24,39,44,44,18,0,50,29],
[35,41,74,42,63,25,79,56,46,28,50,0,40],
[78,78,85,81,96,58,83,89,72,45,71,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 53, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,48,30,54,46,40,51,47,43,64,51,37],
[51,0,55,45,35,56,35,38,51,55,55,37,49],
[52,45,0,35,43,64,40,31,35,43,52,29,36],
[70,55,65,0,53,63,49,49,49,51,77,46,40],
[46,65,57,47,0,51,44,44,48,59,55,58,56],
[54,44,36,37,49,0,38,43,46,47,50,44,53],
[60,65,60,51,56,62,0,57,64,54,57,52,50],
[49,62,69,51,56,57,43,0,42,45,61,53,35],
[53,49,65,51,52,54,36,58,0,58,66,48,51],
[57,45,57,49,41,53,46,55,42,0,48,31,41],
[36,45,48,23,45,50,43,39,34,52,0,34,43],
[49,63,71,54,42,56,48,47,52,69,66,0,44],
[63,51,64,60,44,47,50,65,49,59,57,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 54, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,71,62,77,77,52,58,45,57,58,66,72,87],
[29,0,38,55,46,49,56,45,58,56,19,58,80],
[38,62,0,64,47,49,70,56,86,66,35,60,86],
[23,45,36,0,32,39,58,49,58,48,25,45,65],
[23,54,53,68,0,38,58,48,50,58,37,50,69],
[48,51,51,61,62,0,67,37,53,45,31,38,63],
[42,44,30,42,42,33,0,33,32,43,39,32,51],
[55,55,44,51,52,63,67,0,72,47,50,74,81],
[43,42,14,42,50,47,68,28,0,44,30,51,68],
[42,44,34,52,42,55,57,53,56,0,33,54,83],
[34,81,65,75,63,69,61,50,70,67,0,61,77],
[28,42,40,55,50,62,68,26,49,46,39,0,70],
[13,20,14,35,31,37,49,19,32,17,23,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 55, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,46,52,48,48,46,41,47,48,50,49,47],
[55,0,53,53,54,48,45,47,51,46,55,48,55],
[54,47,0,52,49,51,49,51,48,47,55,53,55],
[48,47,48,0,50,48,42,45,47,51,54,47,49],
[52,46,51,50,0,53,49,52,49,53,54,43,54],
[52,52,49,52,47,0,44,45,44,56,60,47,52],
[54,55,51,58,51,56,0,52,58,61,63,47,61],
[59,53,49,55,48,55,48,0,50,65,57,57,62],
[53,49,52,53,51,56,42,50,0,51,55,46,50],
[52,54,53,49,47,44,39,35,49,0,56,47,51],
[50,45,45,46,46,40,37,43,45,44,0,46,47],
[51,52,47,53,57,53,53,43,54,53,54,0,57],
[53,45,45,51,46,48,39,38,50,49,53,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 56, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,86,38,69,19,66,48,60,48,48,48,44,44],
[14,0,30,59,14,63,39,30,58,17,28,43,43],
[62,70,0,83,42,70,70,66,70,51,47,47,47],
[31,41,17,0,17,80,38,39,60,19,45,60,60],
[81,86,58,83,0,68,70,84,70,70,47,43,69],
[34,37,30,20,32,0,39,36,21,21,22,21,36],
[52,61,30,62,30,61,0,60,61,59,42,43,40],
[40,70,34,61,16,64,40,0,48,21,47,43,47],
[52,42,30,40,30,79,39,52,0,19,20,21,18],
[52,83,49,81,30,79,41,79,81,0,63,43,59],
[52,72,53,55,53,78,58,53,80,37,0,22,74],
[56,57,53,40,57,79,57,57,79,57,78,0,58],
[56,57,53,40,31,64,60,53,82,41,26,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 57, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,39,33,49,45,57,38,34,60,53,41,36],
[69,0,62,44,59,67,72,58,54,71,69,64,49],
[61,38,0,54,57,50,60,56,45,56,61,53,49],
[67,56,46,0,62,61,66,60,50,64,69,67,56],
[51,41,43,38,0,56,57,51,50,58,54,54,40],
[55,33,50,39,44,0,51,43,49,58,53,45,37],
[43,28,40,34,43,49,0,42,45,52,52,42,38],
[62,42,44,40,49,57,58,0,51,61,59,63,56],
[66,46,55,50,50,51,55,49,0,61,53,64,46],
[40,29,44,36,42,42,48,39,39,0,41,44,39],
[47,31,39,31,46,47,48,41,47,59,0,52,30],
[59,36,47,33,46,55,58,37,36,56,48,0,39],
[64,51,51,44,60,63,62,44,54,61,70,61,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 58, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,59,57,45,50,49,50,57,55,53,51,48],
[48,0,52,49,46,54,51,52,51,47,53,48,50],
[41,48,0,51,50,48,51,48,56,53,56,50,55],
[43,51,49,0,47,51,51,52,57,52,50,49,43],
[55,54,50,53,0,52,50,53,53,57,55,54,53],
[50,46,52,49,48,0,50,46,48,49,52,47,54],
[51,49,49,49,50,50,0,46,45,52,60,47,54],
[50,48,52,48,47,54,54,0,53,54,56,49,59],
[43,49,44,43,47,52,55,47,0,51,45,38,49],
[45,53,47,48,43,51,48,46,49,0,52,49,54],
[47,47,44,50,45,48,40,44,55,48,0,43,49],
[49,52,50,51,46,53,53,51,62,51,57,0,54],
[52,50,45,57,47,46,46,41,51,46,51,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 59, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,52,50,53,50,53,50,44,48,55,46,44],
[54,0,50,59,57,56,59,50,54,64,55,51,52],
[48,50,0,55,58,47,60,51,46,57,58,53,44],
[50,41,45,0,44,44,42,49,41,43,52,45,44],
[47,43,42,56,0,46,49,49,48,48,58,43,52],
[50,44,53,56,54,0,51,55,51,58,53,52,46],
[47,41,40,58,51,49,0,53,42,48,53,45,38],
[50,50,49,51,51,45,47,0,50,53,55,48,45],
[56,46,54,59,52,49,58,50,0,58,54,52,48],
[52,36,43,57,52,42,52,47,42,0,55,44,44],
[45,45,42,48,42,47,47,45,46,45,0,47,49],
[54,49,47,55,57,48,55,52,48,56,53,0,47],
[56,48,56,56,48,54,62,55,52,56,51,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 60, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,59,58,50,56,42,55,53,53,51,51,51],
[52,0,71,64,58,65,50,66,59,65,62,64,67],
[41,29,0,44,38,57,44,58,52,48,41,45,42],
[42,36,56,0,41,48,39,54,45,47,46,50,53],
[50,42,62,59,0,67,50,60,53,65,60,60,58],
[44,35,43,52,33,0,47,58,44,49,49,38,47],
[58,50,56,61,50,53,0,59,52,56,63,52,49],
[45,34,42,46,40,42,41,0,48,54,53,44,46],
[47,41,48,55,47,56,48,52,0,56,49,53,51],
[47,35,52,53,35,51,44,46,44,0,50,47,46],
[49,38,59,54,40,51,37,47,51,50,0,40,39],
[49,36,55,50,40,62,48,56,47,53,60,0,50],
[49,33,58,47,42,53,51,54,49,54,61,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 61, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,46,54,56,48,34,48,40,37,44,47,39],
[39,0,46,47,47,48,38,49,43,43,46,50,40],
[54,54,0,52,55,46,48,57,39,50,49,51,48],
[46,53,48,0,51,45,42,49,45,46,49,50,39],
[44,53,45,49,0,36,37,51,44,39,48,42,37],
[52,52,54,55,64,0,40,53,49,45,44,53,48],
[66,62,52,58,63,60,0,57,60,48,58,52,55],
[52,51,43,51,49,47,43,0,45,42,41,49,37],
[60,57,61,55,56,51,40,55,0,34,47,56,46],
[63,57,50,54,61,55,52,58,66,0,48,61,48],
[56,54,51,51,52,56,42,59,53,52,0,59,47],
[53,50,49,50,58,47,48,51,44,39,41,0,38],
[61,60,52,61,63,52,45,63,54,52,53,62,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 62, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,50,45,42,52,50,53,43,46,52,39,62],
[53,0,56,43,47,60,53,46,46,48,50,40,54],
[50,44,0,46,37,46,46,55,51,40,43,39,54],
[55,57,54,0,45,59,56,53,58,53,52,51,60],
[58,53,63,55,0,60,47,51,58,50,64,49,59],
[48,40,54,41,40,0,49,50,41,46,49,47,55],
[50,47,54,44,53,51,0,53,44,51,55,44,59],
[47,54,45,47,49,50,47,0,53,42,55,50,53],
[57,54,49,42,42,59,56,47,0,52,52,45,54],
[54,52,60,47,50,54,49,58,48,0,47,47,55],
[48,50,57,48,36,51,45,45,48,53,0,40,56],
[61,60,61,49,51,53,56,50,55,53,60,0,62],
[38,46,46,40,41,45,41,47,46,45,44,38,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 63, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,44,54,51,52,53,44,52,48,51,54,50],
[46,0,45,50,53,51,54,42,49,46,53,52,52],
[56,55,0,56,56,58,65,54,51,50,54,62,58],
[46,50,44,0,52,51,49,51,47,42,50,52,50],
[49,47,44,48,0,48,46,47,51,47,55,54,50],
[48,49,42,49,52,0,48,47,54,46,50,49,52],
[47,46,35,51,54,52,0,44,43,49,51,49,52],
[56,58,46,49,53,53,56,0,54,49,53,59,57],
[48,51,49,53,49,46,57,46,0,51,50,53,50],
[52,54,50,58,53,54,51,51,49,0,55,54,57],
[49,47,46,50,45,50,49,47,50,45,0,50,49],
[46,48,38,48,46,51,51,41,47,46,50,0,50],
[50,48,42,50,50,48,48,43,50,43,51,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 64, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,67,40,75,41,48,48,48,43,56,49,51],
[52,0,59,55,72,43,62,55,51,55,49,42,69],
[33,41,0,38,69,44,45,38,42,59,51,55,40],
[60,45,62,0,63,47,55,62,44,49,56,58,43],
[25,28,31,37,0,39,29,39,32,32,47,43,35],
[59,57,56,53,61,0,62,57,54,63,78,59,49],
[52,38,55,45,71,38,0,43,39,41,66,50,34],
[52,45,62,38,61,43,57,0,47,52,48,57,52],
[52,49,58,56,68,46,61,53,0,59,72,64,54],
[57,45,41,51,68,37,59,48,41,0,60,63,43],
[44,51,49,44,53,22,34,52,28,40,0,44,45],
[51,58,45,42,57,41,50,43,36,37,56,0,40],
[49,31,60,57,65,51,66,48,46,57,55,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 65, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,50,45,43,50,54,47,53,49,49,52,51],
[53,0,44,48,48,54,53,47,48,58,43,54,49],
[50,56,0,54,49,56,55,61,51,64,50,57,65],
[55,52,46,0,46,55,48,47,52,59,52,50,57],
[57,52,51,54,0,51,47,49,48,64,45,62,53],
[50,46,44,45,49,0,44,49,47,59,44,55,48],
[46,47,45,52,53,56,0,50,44,57,46,55,51],
[53,53,39,53,51,51,50,0,46,58,44,47,46],
[47,52,49,48,52,53,56,54,0,61,49,49,54],
[51,42,36,41,36,41,43,42,39,0,36,47,48],
[51,57,50,48,55,56,54,56,51,64,0,54,57],
[48,46,43,50,38,45,45,53,51,53,46,0,45],
[49,51,35,43,47,52,49,54,46,52,43,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 66, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,51,46,49,39,47,45,56,44,46,49,49],
[53,0,50,52,56,43,46,42,56,47,47,54,49],
[49,50,0,42,50,41,46,48,56,43,46,48,46],
[54,48,58,0,53,47,48,53,52,52,53,48,54],
[51,44,50,47,0,42,49,46,53,44,50,48,43],
[61,57,59,53,58,0,58,57,58,50,56,59,61],
[53,54,54,52,51,42,0,55,59,48,47,59,51],
[55,58,52,47,54,43,45,0,53,51,48,51,46],
[44,44,44,48,47,42,41,47,0,41,41,52,44],
[56,53,57,48,56,50,52,49,59,0,52,58,56],
[54,53,54,47,50,44,53,52,59,48,0,52,46],
[51,46,52,52,52,41,41,49,48,42,48,0,55],
[51,51,54,46,57,39,49,54,56,44,54,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 67, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,52,60,50,56,56,50,50,49,47,48,52],
[42,0,48,52,45,55,54,45,44,47,43,40,44],
[48,52,0,59,54,56,53,55,48,55,45,50,52],
[40,48,41,0,48,51,46,46,44,48,41,42,51],
[50,55,46,52,0,57,54,50,51,50,45,45,55],
[44,45,44,49,43,0,47,45,42,44,38,36,43],
[44,46,47,54,46,53,0,52,44,49,47,46,48],
[50,55,45,54,50,55,48,0,43,45,44,48,56],
[50,56,52,56,49,58,56,57,0,48,48,48,53],
[51,53,45,52,50,56,51,55,52,0,41,47,47],
[53,57,55,59,55,62,53,56,52,59,0,49,57],
[52,60,50,58,55,64,54,52,52,53,51,0,55],
[48,56,48,49,45,57,52,44,47,53,43,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 68, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,52,77,77,52,30,30,52,53,22,55,30],
[70,0,100,100,77,100,78,100,45,75,70,70,75],
[48,0,0,25,55,53,0,0,22,23,45,48,23],
[23,0,75,0,30,75,30,30,45,23,45,48,53],
[23,23,45,70,0,45,23,23,45,23,45,48,23],
[48,0,47,25,55,0,0,0,22,23,47,25,0],
[70,22,100,70,77,100,0,70,45,45,70,70,45],
[70,0,100,70,77,100,30,0,45,45,70,48,75],
[48,55,78,55,55,78,55,55,0,78,70,48,78],
[47,25,77,77,77,77,55,55,22,0,47,25,55],
[78,30,55,55,55,53,30,30,30,53,0,78,30],
[45,30,52,52,52,75,30,52,52,75,22,0,52],
[70,25,77,47,77,100,55,25,22,45,70,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 69, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,49,36,43,34,51,55,54,57,61,45,44],
[38,0,39,28,30,36,37,38,37,46,39,35,41],
[51,61,0,33,48,48,55,49,50,54,58,35,41],
[64,72,67,0,67,46,57,52,69,62,65,55,60],
[57,70,52,33,0,44,54,66,51,52,59,39,38],
[66,64,52,54,56,0,62,47,51,53,59,58,54],
[49,63,45,43,46,38,0,53,56,52,52,46,46],
[45,62,51,48,34,53,47,0,50,55,54,49,48],
[46,63,50,31,49,49,44,50,0,50,52,37,41],
[43,54,46,38,48,47,48,45,50,0,63,44,41],
[39,61,42,35,41,41,48,46,48,37,0,40,46],
[55,65,65,45,61,42,54,51,63,56,60,0,56],
[56,59,59,40,62,46,54,52,59,59,54,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 70, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,60,51,59,57,63,55,55,63,56,39,47],
[52,0,49,48,58,61,61,56,51,72,60,46,50],
[40,51,0,42,57,51,53,55,53,56,64,48,53],
[49,52,58,0,65,55,60,52,57,65,52,42,46],
[41,42,43,35,0,47,50,45,54,59,50,39,36],
[43,39,49,45,53,0,51,65,57,62,54,52,56],
[37,39,47,40,50,49,0,55,48,49,49,38,52],
[45,44,45,48,55,35,45,0,47,50,54,53,57],
[45,49,47,43,46,43,52,53,0,54,52,38,39],
[37,28,44,35,41,38,51,50,46,0,39,30,36],
[44,40,36,48,50,46,51,46,48,61,0,44,52],
[61,54,52,58,61,48,62,47,62,70,56,0,61],
[53,50,47,54,64,44,48,43,61,64,48,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 71, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,63,69,72,66,69,48,60,65,68,54,59,73],
[37,0,63,55,58,57,55,50,56,67,45,45,75],
[31,37,0,62,59,49,40,40,45,62,35,43,62],
[28,45,38,0,58,42,36,38,40,60,35,43,53],
[34,42,41,42,0,34,33,40,42,58,33,32,48],
[31,43,51,58,66,0,42,43,42,51,43,46,55],
[52,45,60,64,67,58,0,57,60,63,40,48,66],
[40,50,60,62,60,57,43,0,53,75,42,46,61],
[35,44,55,60,58,58,40,47,0,48,45,44,66],
[32,33,38,40,42,49,37,25,52,0,40,42,48],
[46,55,65,65,67,57,60,58,55,60,0,58,62],
[41,55,57,57,68,54,52,54,56,58,42,0,74],
[27,25,38,47,52,45,34,39,34,52,38,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 72, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,52,46,57,58,43,43,47,31,52,39,32],
[47,0,55,45,57,47,46,51,43,44,43,44,39],
[48,45,0,49,41,44,55,38,42,39,50,31,50],
[54,55,51,0,49,46,46,48,55,46,38,40,48],
[43,43,59,51,0,45,57,56,48,39,53,35,45],
[42,53,56,54,55,0,54,40,46,40,53,36,43],
[57,54,45,54,43,46,0,50,42,59,58,50,46],
[57,49,62,52,44,60,50,0,49,51,46,49,40],
[53,57,58,45,52,54,58,51,0,52,58,49,48],
[69,56,61,54,61,60,41,49,48,0,62,59,43],
[48,57,50,62,47,47,42,54,42,38,0,34,37],
[61,56,69,60,65,64,50,51,51,41,66,0,48],
[68,61,50,52,55,57,54,60,52,57,63,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 73, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,55,53,51,60,55,44,54,41,52,52,52],
[46,0,55,63,60,59,47,59,43,36,50,48,50],
[45,45,0,46,54,46,46,48,39,37,40,43,45],
[47,37,54,0,50,53,47,53,48,42,46,45,55],
[49,40,46,50,0,44,49,59,41,41,47,42,52],
[40,41,54,47,56,0,45,54,46,44,56,41,49],
[45,53,54,53,51,55,0,54,42,48,47,51,53],
[56,41,52,47,41,46,46,0,42,47,44,52,46],
[46,57,61,52,59,54,58,58,0,50,54,59,50],
[59,64,63,58,59,56,52,53,50,0,48,50,61],
[48,50,60,54,53,44,53,56,46,52,0,49,52],
[48,52,57,55,58,59,49,48,41,50,51,0,54],
[48,50,55,45,48,51,47,54,50,39,48,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 74, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,37,43,46,62,41,60,58,53,53,63,58,47],
[63,0,48,47,48,54,57,49,56,56,65,55,54],
[57,52,0,53,49,54,66,45,60,58,68,58,57],
[54,53,47,0,60,42,56,60,51,48,54,57,47],
[38,52,51,40,0,59,61,47,51,47,56,54,39],
[59,46,46,58,41,0,65,53,57,54,57,64,48],
[40,43,34,44,39,35,0,30,41,36,49,48,41],
[42,51,55,40,53,47,70,0,52,50,60,52,41],
[47,44,40,49,49,43,59,48,0,46,48,38,46],
[47,44,42,52,53,46,64,50,54,0,64,58,36],
[37,35,32,46,44,43,51,40,52,36,0,45,34],
[42,45,42,43,46,36,52,48,62,42,55,0,35],
[53,46,43,53,61,52,59,59,54,64,66,65,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 75, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,51,54,57,58,47,62,51,55,53,59,52],
[50,0,54,48,46,49,54,44,51,52,57,50,46],
[49,46,0,40,51,48,55,50,39,46,47,49,43],
[46,52,60,0,60,58,56,57,49,59,64,58,58],
[43,54,49,40,0,52,40,42,47,47,53,44,46],
[42,51,52,42,48,0,45,54,45,43,62,54,53],
[53,46,45,44,60,55,0,51,44,40,54,48,43],
[38,56,50,43,58,46,49,0,47,41,49,47,47],
[49,49,61,51,53,55,56,53,0,45,52,58,48],
[45,48,54,41,53,57,60,59,55,0,65,51,46],
[47,43,53,36,47,38,46,51,48,35,0,47,43],
[41,50,51,42,56,46,52,53,42,49,53,0,52],
[48,54,57,42,54,47,57,53,52,54,57,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 76, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,41,25,59,0,67,33,59,33,50,25,25],
[75,0,41,100,75,42,50,75,50,84,92,75,51],
[59,59,0,84,59,34,75,84,34,84,51,84,26],
[75,0,16,0,50,42,42,8,34,8,51,0,0],
[41,25,41,50,0,0,41,25,8,50,50,25,25],
[100,58,66,58,100,0,100,58,59,58,76,58,25],
[33,50,25,58,59,0,0,58,8,58,50,58,25],
[67,25,16,92,75,42,42,0,50,58,51,25,26],
[41,50,66,66,92,41,92,50,0,50,50,50,25],
[67,16,16,92,50,42,42,42,50,0,67,16,26],
[50,8,49,49,50,24,50,49,50,33,0,33,0],
[75,25,16,100,75,42,42,75,50,84,67,0,26],
[75,49,74,100,75,75,75,74,75,74,100,74,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 77, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,72,54,65,61,59,63,49,51,55,65,56],
[45,0,46,41,50,50,62,49,49,36,32,40,53],
[28,54,0,48,47,58,50,37,36,37,43,37,38],
[46,59,52,0,49,50,50,51,41,39,51,57,54],
[35,50,53,51,0,39,51,35,45,34,43,40,44],
[39,50,42,50,61,0,52,41,35,41,41,36,39],
[41,38,50,50,49,48,0,45,51,35,41,38,53],
[37,51,63,49,65,59,55,0,49,32,36,48,52],
[51,51,64,59,55,65,49,51,0,43,51,46,50],
[49,64,63,61,66,59,65,68,57,0,44,53,58],
[45,68,57,49,57,59,59,64,49,56,0,46,58],
[35,60,63,43,60,64,62,52,54,47,54,0,62],
[44,47,62,46,56,61,47,48,50,42,42,38,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 78, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,49,49,46,52,55,49,40,44,43,56,52],
[61,0,46,48,51,57,58,49,43,51,46,59,51],
[51,54,0,57,57,54,51,49,48,52,50,63,63],
[51,52,43,0,56,47,50,40,46,53,39,49,50],
[54,49,43,44,0,46,49,45,32,36,42,50,53],
[48,43,46,53,54,0,62,40,40,44,35,48,44],
[45,42,49,50,51,38,0,45,49,38,42,44,47],
[51,51,51,60,55,60,55,0,46,49,37,57,62],
[60,57,52,54,68,60,51,54,0,51,49,58,65],
[56,49,48,47,64,56,62,51,49,0,51,53,47],
[57,54,50,61,58,65,58,63,51,49,0,65,63],
[44,41,37,51,50,52,56,43,42,47,35,0,43],
[48,49,37,50,47,56,53,38,35,53,37,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 79, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,51,53,50,45,53,49,56,52,48,63,60],
[43,0,53,52,51,43,55,50,46,49,55,60,55],
[49,47,0,50,46,40,53,41,49,46,45,48,56],
[47,48,50,0,53,50,52,50,53,49,42,53,56],
[50,49,54,47,0,53,48,49,53,53,45,49,57],
[55,57,60,50,47,0,63,49,57,48,48,52,62],
[47,45,47,48,52,37,0,44,50,42,49,47,55],
[51,50,59,50,51,51,56,0,55,52,52,54,58],
[44,54,51,47,47,43,50,45,0,53,51,51,57],
[48,51,54,51,47,52,58,48,47,0,47,56,62],
[52,45,55,58,55,52,51,48,49,53,0,55,56],
[37,40,52,47,51,48,53,46,49,44,45,0,50],
[40,45,44,44,43,38,45,42,43,38,44,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 80, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,72,37,48,37,46,41,41,48,45,47,53],
[53,0,68,51,47,55,55,58,55,59,52,51,65],
[28,32,0,21,42,35,34,35,33,35,49,40,42],
[63,49,79,0,56,56,52,54,46,60,64,59,54],
[52,53,58,44,0,51,42,41,37,45,44,59,49],
[63,45,65,44,49,0,39,40,28,54,53,56,62],
[54,45,66,48,58,61,0,60,48,63,63,62,52],
[59,42,65,46,59,60,40,0,31,61,65,62,62],
[59,45,67,54,63,72,52,69,0,65,63,59,59],
[52,41,65,40,55,46,37,39,35,0,52,39,51],
[55,48,51,36,56,47,37,35,37,48,0,46,54],
[53,49,60,41,41,44,38,38,41,61,54,0,52],
[47,35,58,46,51,38,48,38,41,49,46,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 81, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,56,54,53,53,47,56,48,45,47,47,52],
[54,0,48,54,57,52,54,54,55,52,48,46,46],
[44,52,0,49,52,43,42,51,46,43,43,43,43],
[46,46,51,0,53,46,48,52,48,45,53,41,53],
[47,43,48,47,0,37,41,48,46,41,43,41,46],
[47,48,57,54,63,0,51,56,51,48,51,49,54],
[53,46,58,52,59,49,0,60,50,48,47,47,53],
[44,46,49,48,52,44,40,0,48,49,45,49,49],
[52,45,54,52,54,49,50,52,0,48,43,51,54],
[55,48,57,55,59,52,52,51,52,0,52,46,53],
[53,52,57,47,57,49,53,55,57,48,0,46,52],
[53,54,57,59,59,51,53,51,49,54,54,0,57],
[48,54,57,47,54,46,47,51,46,47,48,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 82, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,48,56,33,51,47,18,75,56,39,18,51],
[44,0,44,32,47,47,43,32,80,36,53,36,51],
[52,56,0,33,33,33,29,36,37,38,14,36,56],
[44,68,67,0,29,47,81,28,75,90,58,27,47],
[67,53,67,71,0,47,66,51,80,70,62,50,65],
[49,53,67,53,53,0,49,18,76,58,53,13,53],
[53,57,71,19,34,51,0,42,80,59,62,41,56],
[82,68,64,72,49,82,58,0,95,67,50,4,71],
[25,20,63,25,20,24,20,5,0,43,45,5,20],
[44,64,62,10,30,42,41,33,57,0,30,33,53],
[61,47,86,42,38,47,38,50,55,70,0,45,65],
[82,64,64,73,50,87,59,96,95,67,55,0,67],
[49,49,44,53,35,47,44,29,80,47,35,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 83, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,53,49,57,44,42,53,35,57,44,58,50],
[66,0,58,55,46,53,51,57,55,61,58,52,60],
[47,42,0,38,50,48,42,55,47,57,38,50,44],
[51,45,62,0,50,46,46,63,56,54,62,52,59],
[43,54,50,50,0,52,45,59,52,58,56,60,49],
[56,47,52,54,48,0,41,60,47,55,49,44,54],
[58,49,58,54,55,59,0,59,51,54,55,56,62],
[47,43,45,37,41,40,41,0,42,54,45,47,52],
[65,45,53,44,48,53,49,58,0,54,55,54,54],
[43,39,43,46,42,45,46,46,46,0,42,51,46],
[56,42,62,38,44,51,45,55,45,58,0,54,51],
[42,48,50,48,40,56,44,53,46,49,46,0,47],
[50,40,56,41,51,46,38,48,46,54,49,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 84, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,53,50,59,59,48,56,57,56,47,52,62],
[44,0,61,53,57,52,49,53,46,45,47,53,54],
[47,39,0,48,48,52,42,50,49,40,39,48,51],
[50,47,52,0,52,57,45,55,53,50,42,52,52],
[41,43,52,48,0,51,43,54,50,50,37,52,55],
[41,48,48,43,49,0,43,53,42,45,46,49,46],
[52,51,58,55,57,57,0,51,56,44,54,49,50],
[44,47,50,45,46,47,49,0,49,49,49,49,50],
[43,54,51,47,50,58,44,51,0,36,43,46,48],
[44,55,60,50,50,55,56,51,64,0,48,52,56],
[53,53,61,58,63,54,46,51,57,52,0,54,59],
[48,47,52,48,48,51,51,51,54,48,46,0,60],
[38,46,49,48,45,54,50,50,52,44,41,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 85, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,55,48,54,48,46,37,52,55,43,54,39],
[42,0,57,48,41,45,43,38,53,53,42,46,38],
[45,43,0,46,46,55,42,53,51,43,46,47,39],
[52,52,54,0,51,50,40,45,57,55,36,51,41],
[46,59,54,49,0,57,58,57,55,56,52,46,44],
[52,55,45,50,43,0,46,41,45,48,42,58,30],
[54,57,58,60,42,54,0,44,50,53,46,51,40],
[63,62,47,55,43,59,56,0,51,60,49,52,51],
[48,47,49,43,45,55,50,49,0,56,55,60,50],
[45,47,57,45,44,52,47,40,44,0,42,48,38],
[57,58,54,64,48,58,54,51,45,58,0,59,58],
[46,54,53,49,54,42,49,48,40,52,41,0,38],
[61,62,61,59,56,70,60,49,50,62,42,62,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 86, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,29,54,36,39,42,57,44,55,50,42,43],
[43,0,38,49,45,50,52,43,54,45,62,53,53],
[71,62,0,59,50,51,57,58,60,61,64,53,52],
[46,51,41,0,38,50,51,52,58,52,47,49,50],
[64,55,50,62,0,60,62,38,56,45,68,57,56],
[61,50,49,50,40,0,54,45,54,47,55,52,47],
[58,48,43,49,38,46,0,45,53,50,49,44,46],
[43,57,42,48,62,55,55,0,41,45,57,49,51],
[56,46,40,42,44,46,47,59,0,57,50,48,50],
[45,55,39,48,55,53,50,55,43,0,60,56,52],
[50,38,36,53,32,45,51,43,50,40,0,40,45],
[58,47,47,51,43,48,56,51,52,44,60,0,51],
[57,47,48,50,44,53,54,49,50,48,55,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 87, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,46,56,46,38,35,44,42,31,44,41,44],
[42,0,39,32,49,45,38,36,39,43,48,38,51],
[54,61,0,37,52,48,54,57,53,45,58,38,50],
[44,68,63,0,50,48,55,51,51,50,53,52,54],
[54,51,48,50,0,40,38,49,52,45,52,45,55],
[62,55,52,52,60,0,50,61,59,54,55,57,68],
[65,62,46,45,62,50,0,69,58,54,60,42,61],
[56,64,43,49,51,39,31,0,55,38,51,34,51],
[58,61,47,49,48,41,42,45,0,45,54,37,58],
[69,57,55,50,55,46,46,62,55,0,55,41,59],
[56,52,42,47,48,45,40,49,46,45,0,38,39],
[59,62,62,48,55,43,58,66,63,59,62,0,58],
[56,49,50,46,45,32,39,49,42,41,61,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 88, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,35,70,70,47,58,47,58,0,22,47,47],
[53,0,22,45,45,58,58,35,75,23,22,22,52],
[65,78,0,70,65,48,36,48,65,35,23,34,77],
[30,55,30,0,42,13,13,25,30,0,0,12,30],
[30,55,35,58,0,35,13,25,52,0,22,34,65],
[53,42,52,87,65,0,36,25,75,53,52,64,64],
[42,42,64,87,87,64,0,55,64,42,64,64,64],
[53,65,52,75,75,75,45,0,75,53,75,52,52],
[42,25,35,70,48,25,36,25,0,0,0,34,47],
[100,77,65,100,100,47,58,47,100,0,22,47,77],
[78,78,77,100,78,48,36,25,100,78,0,77,77],
[53,78,66,88,66,36,36,48,66,53,23,0,88],
[53,48,23,70,35,36,36,48,53,23,23,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 89, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,72,60,36,51,59,39,45,42,24,30,71,44],
[28,0,28,41,43,56,30,25,29,20,24,55,45],
[40,72,0,45,60,62,39,41,61,36,32,42,44],
[64,59,55,0,68,61,43,37,39,42,39,67,39],
[49,57,40,32,0,47,35,25,39,28,25,54,48],
[41,44,38,39,53,0,49,26,46,45,33,56,39],
[61,70,61,57,65,51,0,49,38,53,36,62,51],
[55,75,59,63,75,74,51,0,55,31,58,70,62],
[58,71,39,61,61,54,62,45,0,51,43,69,56],
[76,80,64,58,72,55,47,69,49,0,45,66,62],
[70,76,68,61,75,67,64,42,57,55,0,68,50],
[29,45,58,33,46,44,38,30,31,34,32,0,40],
[56,55,56,61,52,61,49,38,44,38,50,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 90, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,47,52,48,59,53,55,52,41,47,49,45],
[55,0,56,57,59,55,58,51,61,48,48,50,50],
[53,44,0,55,46,48,48,46,53,46,51,50,56],
[48,43,45,0,54,52,56,51,54,42,45,50,54],
[52,41,54,46,0,48,47,50,56,41,45,49,54],
[41,45,52,48,52,0,51,50,55,40,48,52,50],
[47,42,52,44,53,49,0,46,56,49,47,46,54],
[45,49,54,49,50,50,54,0,53,49,47,51,50],
[48,39,47,46,44,45,44,47,0,42,39,45,45],
[59,52,54,58,59,60,51,51,58,0,47,54,56],
[53,52,49,55,55,52,53,53,61,53,0,62,56],
[51,50,50,50,51,48,54,49,55,46,38,0,51],
[55,50,44,46,46,50,46,50,55,44,44,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 91, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,34,60,60,70,46,60,49,50,60,46,70],
[38,0,26,39,48,56,61,47,48,38,51,24,39],
[66,74,0,73,59,57,72,83,72,49,62,48,61],
[40,61,27,0,59,57,57,75,49,53,75,22,62],
[40,52,41,41,0,21,36,63,24,53,41,24,41],
[30,44,43,43,79,0,53,75,52,54,55,53,43],
[54,39,28,43,64,47,0,65,30,43,75,39,63],
[40,53,17,25,37,25,35,0,24,12,37,0,37],
[51,52,28,51,76,48,70,76,0,66,76,50,64],
[50,62,51,47,47,46,57,88,34,0,46,22,46],
[40,49,38,25,59,45,25,63,24,54,0,24,49],
[54,76,52,78,76,47,61,100,50,78,76,0,53],
[30,61,39,38,59,57,37,63,36,54,51,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 92, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,59,47,47,48,47,54,48,55,55,49,51],
[48,0,53,45,44,47,43,51,49,49,48,48,48],
[41,47,0,47,46,44,44,49,42,51,44,44,48],
[53,55,53,0,45,50,45,55,52,52,50,51,52],
[53,56,54,55,0,45,54,48,54,59,54,49,53],
[52,53,56,50,55,0,62,64,58,55,57,55,52],
[53,57,56,55,46,38,0,59,52,45,54,42,52],
[46,49,51,45,52,36,41,0,41,46,43,40,48],
[52,51,58,48,46,42,48,59,0,47,52,46,44],
[45,51,49,48,41,45,55,54,53,0,43,43,44],
[45,52,56,50,46,43,46,57,48,57,0,53,49],
[51,52,56,49,51,45,58,60,54,57,47,0,52],
[49,52,52,48,47,48,48,52,56,56,51,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 93, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,70,58,56,63,67,78,56,49,73,67,88],
[57,0,53,53,56,39,61,53,44,48,53,58,76],
[30,47,0,59,54,40,60,45,47,40,63,54,66],
[42,47,41,0,65,49,53,51,53,47,54,61,83],
[44,44,46,35,0,46,62,56,50,37,47,64,66],
[37,61,60,51,54,0,49,59,48,48,50,68,66],
[33,39,40,47,38,51,0,48,43,32,42,47,60],
[22,47,55,49,44,41,52,0,27,31,44,45,61],
[44,56,53,47,50,52,57,73,0,59,49,71,67],
[51,52,60,53,63,52,68,69,41,0,57,58,76],
[27,47,37,46,53,50,58,56,51,43,0,54,78],
[33,42,46,39,36,32,53,55,29,42,46,0,70],
[12,24,34,17,34,34,40,39,33,24,22,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 94, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,22,31,9,31,31,58,48,9,31,22,39],
[69,0,18,46,17,28,26,37,17,37,10,33,18],
[78,82,0,62,61,66,45,84,42,45,67,61,46],
[69,54,38,0,16,31,39,59,39,20,32,55,56],
[91,83,39,84,0,51,83,59,40,29,48,74,75],
[69,72,34,69,49,0,33,59,34,53,56,33,34],
[69,74,55,61,17,67,0,58,17,37,48,55,33],
[42,63,16,41,41,41,42,0,58,42,25,33,17],
[52,83,58,61,60,66,83,42,0,45,67,74,58],
[91,63,55,80,71,47,63,58,55,0,47,55,55],
[69,90,33,68,52,44,52,75,33,53,0,52,53],
[78,67,39,45,26,67,45,67,26,45,48,0,26],
[61,82,54,44,25,66,67,83,42,45,47,74,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 95, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,53,46,69,42,47,55,39,62,43,47,47],
[39,0,49,51,40,48,49,48,48,53,32,47,37],
[47,51,0,45,64,61,50,62,49,66,51,55,22],
[54,49,55,0,40,58,46,46,46,58,57,61,57],
[31,60,36,60,0,61,51,45,41,38,52,43,38],
[58,52,39,42,39,0,35,35,44,59,41,53,33],
[53,51,50,54,49,65,0,39,54,62,55,61,49],
[45,52,38,54,55,65,61,0,41,57,41,57,39],
[61,52,51,54,59,56,46,59,0,54,35,50,43],
[38,47,34,42,62,41,38,43,46,0,58,47,33],
[57,68,49,43,48,59,45,59,65,42,0,55,39],
[53,53,45,39,57,47,39,43,50,53,45,0,28],
[53,63,78,43,62,67,51,61,57,67,61,72,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 96, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,40,52,41,50,45,41,46,51,48,42,39],
[51,0,50,53,48,50,57,49,55,57,52,50,52],
[60,50,0,60,47,56,56,43,50,56,57,49,48],
[48,47,40,0,46,46,51,51,48,55,46,50,53],
[59,52,53,54,0,56,58,51,49,59,46,54,51],
[50,50,44,54,44,0,53,45,49,58,52,49,42],
[55,43,44,49,42,47,0,41,48,47,44,46,44],
[59,51,57,49,49,55,59,0,55,59,50,48,53],
[54,45,50,52,51,51,52,45,0,59,50,48,51],
[49,43,44,45,41,42,53,41,41,0,42,40,38],
[52,48,43,54,54,48,56,50,50,58,0,46,53],
[58,50,51,50,46,51,54,52,52,60,54,0,53],
[61,48,52,47,49,58,56,47,49,62,47,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 97, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,60,57,50,47,46,61,50,44,53,58,56],
[55,0,49,60,43,42,54,49,47,40,49,52,58],
[40,51,0,47,46,47,48,58,54,40,54,51,57],
[43,40,53,0,47,43,48,52,44,40,47,45,43],
[50,57,54,53,0,47,52,47,50,47,51,49,59],
[53,58,53,57,53,0,54,54,51,55,58,48,55],
[54,46,52,52,48,46,0,52,49,49,49,58,52],
[39,51,42,48,53,46,48,0,48,39,45,54,54],
[50,53,46,56,50,49,51,52,0,48,43,52,56],
[56,60,60,60,53,45,51,61,52,0,49,58,56],
[47,51,46,53,49,42,51,55,57,51,0,52,55],
[42,48,49,55,51,52,42,46,48,42,48,0,49],
[44,42,43,57,41,45,48,46,44,44,45,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 98, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,46,53,39,50,42,45,52,52,55,45,54],
[50,0,54,58,41,59,47,37,56,42,49,43,60],
[54,46,0,57,46,40,44,43,60,54,50,40,58],
[47,42,43,0,42,43,44,39,52,48,39,35,49],
[61,59,54,58,0,52,54,51,62,52,61,47,58],
[50,41,60,57,48,0,41,45,56,46,51,40,58],
[58,53,56,56,46,59,0,50,57,55,54,35,61],
[55,63,57,61,49,55,50,0,64,58,54,51,73],
[48,44,40,48,38,44,43,36,0,42,39,33,38],
[48,58,46,52,48,54,45,42,58,0,50,43,60],
[45,51,50,61,39,49,46,46,61,50,0,34,52],
[55,57,60,65,53,60,65,49,67,57,66,0,64],
[46,40,42,51,42,42,39,27,62,40,48,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 99, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,43,51,47,53,59,45,43,52,53,49,53],
[46,0,40,53,49,48,51,49,51,46,47,47,41],
[57,60,0,53,45,50,58,49,43,50,49,51,51],
[49,47,47,0,48,46,54,43,43,47,51,41,43],
[53,51,55,52,0,50,56,55,47,53,54,54,53],
[47,52,50,54,50,0,46,46,42,52,44,42,48],
[41,49,42,46,44,54,0,38,46,48,43,47,41],
[55,51,51,57,45,54,62,0,42,53,52,47,47],
[57,49,57,57,53,58,54,58,0,57,55,58,52],
[48,54,50,53,47,48,52,47,43,0,50,48,46],
[47,53,51,49,46,56,57,48,45,50,0,50,50],
[51,53,49,59,46,58,53,53,42,52,50,0,49],
[47,59,49,57,47,52,59,53,48,54,50,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 100, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,65,49,57,67,47,43,34,45,43,46,57,37],
[35,0,56,38,45,50,35,36,27,32,45,50,36],
[51,44,0,56,52,32,29,24,40,42,40,53,31],
[43,62,44,0,56,39,35,50,42,49,42,54,42],
[33,55,48,44,0,45,34,48,39,47,51,63,30],
[53,50,68,61,55,0,47,46,49,47,50,67,50],
[57,65,71,65,66,53,0,41,50,55,56,62,43],
[66,64,76,50,52,54,59,0,49,49,59,70,50],
[55,73,60,58,61,51,50,51,0,57,52,69,52],
[57,68,58,51,53,53,45,51,43,0,63,61,48],
[54,55,60,58,49,50,44,41,48,37,0,53,47],
[43,50,47,46,37,33,38,30,31,39,47,0,36],
[63,64,69,58,70,50,57,50,48,52,53,64,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 101, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,74,36,39,62,53,52,43,45,55,39,36,27],
[26,0,20,24,46,21,48,27,24,12,42,17,21],
[64,80,0,41,56,57,63,43,44,46,37,42,44],
[61,76,59,0,62,69,74,45,51,46,54,49,45],
[38,54,44,38,0,62,47,48,53,53,52,22,34],
[47,79,43,31,38,0,62,38,39,44,41,26,31],
[48,52,37,26,53,38,0,53,45,45,47,18,23],
[57,73,57,55,52,62,47,0,49,58,55,47,49],
[55,76,56,49,47,61,55,51,0,44,43,25,43],
[45,88,54,54,47,56,55,42,56,0,46,38,30],
[61,58,63,46,48,59,53,45,57,54,0,36,55],
[64,83,58,51,78,74,82,53,75,62,64,0,49],
[73,79,56,55,66,69,77,51,57,70,45,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 102, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,66,58,43,52,47,38,44,40,44,41,76,48],
[34,0,61,55,53,58,25,35,25,56,41,53,42],
[42,39,0,46,36,33,34,36,42,48,39,52,58],
[57,45,54,0,39,42,37,40,42,52,40,64,41],
[48,47,64,61,0,24,44,61,49,51,41,70,45],
[53,42,67,58,76,0,50,55,53,56,68,68,51],
[62,75,66,63,56,50,0,64,51,77,54,65,57],
[56,65,64,60,39,45,36,0,53,62,41,63,53],
[60,75,58,58,51,47,49,47,0,66,43,64,40],
[56,44,52,48,49,44,23,38,34,0,44,59,32],
[59,59,61,60,59,32,46,59,57,56,0,70,54],
[24,47,48,36,30,32,35,37,36,41,30,0,33],
[52,58,42,59,55,49,43,47,60,68,46,67,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 103, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,37,50,38,35,50,48,50,39,47,46,45,38],
[63,0,62,55,45,54,58,53,60,57,55,53,40],
[50,38,0,38,33,46,53,43,42,43,44,44,36],
[62,45,62,0,47,50,61,43,48,58,53,57,50],
[65,55,67,53,0,55,58,53,49,56,55,54,48],
[50,46,54,50,45,0,52,46,41,49,53,50,39],
[52,42,47,39,42,48,0,45,45,48,48,45,41],
[50,47,57,57,47,54,55,0,53,58,54,59,52],
[61,40,58,52,51,59,55,47,0,50,56,54,39],
[53,43,57,42,44,51,52,42,50,0,55,37,40],
[54,45,56,47,45,47,52,46,44,45,0,47,43],
[55,47,56,43,46,50,55,41,46,63,53,0,46],
[62,60,64,50,52,61,59,48,61,60,57,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 104, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,41,45,67,46,45,44,40,66,66,55,54],
[45,0,40,42,57,27,40,38,45,47,56,46,45],
[59,60,0,56,68,57,45,62,47,60,70,57,48],
[55,58,44,0,65,34,45,40,47,55,70,53,47],
[33,43,32,35,0,34,45,33,39,44,56,38,45],
[54,73,43,66,66,0,50,62,51,59,83,40,56],
[55,60,55,55,55,50,0,59,62,68,71,55,55],
[56,62,38,60,67,38,41,0,44,57,65,48,52],
[60,55,53,53,61,49,38,56,0,56,56,62,59],
[34,53,40,45,56,41,32,43,44,0,53,53,54],
[34,44,30,30,44,17,29,35,44,47,0,39,38],
[45,54,43,47,62,60,45,52,38,47,61,0,54],
[46,55,52,53,55,44,45,48,41,46,62,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 105, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,48,45,44,36,48,42,26,51,44,50,36],
[73,0,78,73,55,66,69,66,49,74,74,74,68],
[52,22,0,48,44,45,50,45,45,49,56,52,34],
[55,27,52,0,47,46,60,34,55,53,57,66,38],
[56,45,56,53,0,44,56,49,50,55,60,56,54],
[64,34,55,54,56,0,52,47,48,59,68,59,49],
[52,31,50,40,44,48,0,31,39,51,58,53,44],
[58,34,55,66,51,53,69,0,48,70,54,68,46],
[74,51,55,45,50,52,61,52,0,55,61,67,52],
[49,26,51,47,45,41,49,30,45,0,56,55,33],
[56,26,44,43,40,32,42,46,39,44,0,60,37],
[50,26,48,34,44,41,47,32,33,45,40,0,27],
[64,32,66,62,46,51,56,54,48,67,63,73,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 106, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,64,43,59,58,61,55,54,56,53,55,57,57],
[36,0,43,42,45,48,57,47,43,54,42,42,42],
[57,57,0,43,61,54,65,55,53,54,49,62,59],
[41,58,57,0,54,54,68,55,49,59,49,56,54],
[42,55,39,46,0,44,58,48,51,49,47,51,50],
[39,52,46,46,56,0,56,44,45,54,55,61,54],
[45,43,35,32,42,44,0,42,45,39,40,45,46],
[46,53,45,45,52,56,58,0,54,56,47,53,59],
[44,57,47,51,49,55,55,46,0,59,46,60,49],
[47,46,46,41,51,46,61,44,41,0,44,44,48],
[45,58,51,51,53,45,60,53,54,56,0,56,62],
[43,58,38,44,49,39,55,47,40,56,44,0,49],
[43,58,41,46,50,46,54,41,51,52,38,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 107, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,51,45,41,55,36,39,44,40,42,40,40],
[56,0,59,50,39,50,47,41,36,57,51,42,56],
[49,41,0,47,35,51,37,37,33,49,42,38,40],
[55,50,53,0,36,52,37,44,47,62,52,58,38],
[59,61,65,64,0,60,50,53,51,57,57,49,59],
[45,50,49,48,40,0,40,42,45,58,51,51,48],
[64,53,63,63,50,60,0,46,54,53,48,53,52],
[61,59,63,56,47,58,54,0,55,56,59,51,49],
[56,64,67,53,49,55,46,45,0,58,50,49,56],
[60,43,51,38,43,42,47,44,42,0,49,48,45],
[58,49,58,48,43,49,52,41,50,51,0,48,53],
[60,58,62,42,51,49,47,49,51,52,52,0,49],
[60,44,60,62,41,52,48,51,44,55,47,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 108, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,53,51,47,49,40,46,52,48,42,49,48],
[52,0,43,53,46,56,42,45,47,46,40,42,42],
[47,57,0,53,42,56,51,44,57,44,54,53,55],
[49,47,47,0,42,45,51,40,53,46,46,43,55],
[53,54,58,58,0,61,52,46,55,47,55,50,50],
[51,44,44,55,39,0,40,35,43,43,50,47,44],
[60,58,49,49,48,60,0,53,53,53,53,46,54],
[54,55,56,60,54,65,47,0,52,53,52,52,59],
[48,53,43,47,45,57,47,48,0,44,46,47,50],
[52,54,56,54,53,57,47,47,56,0,50,54,49],
[58,60,46,54,45,50,47,48,54,50,0,51,58],
[51,58,47,57,50,53,54,48,53,46,49,0,46],
[52,58,45,45,50,56,46,41,50,51,42,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 109, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,50,51,51,54,68,53,58,58,46,56,54],
[47,0,48,63,48,53,62,58,67,52,55,56,54],
[50,52,0,46,48,36,67,60,67,54,49,49,47],
[49,37,54,0,35,39,47,46,50,44,50,50,45],
[49,52,52,65,0,52,61,53,58,60,48,58,60],
[46,47,64,61,48,0,71,66,64,60,55,59,55],
[32,38,33,53,39,29,0,40,38,37,37,33,46],
[47,42,40,54,47,34,60,0,69,58,43,49,41],
[42,33,33,50,42,36,62,31,0,54,35,51,48],
[42,48,46,56,40,40,63,42,46,0,43,51,63],
[54,45,51,50,52,45,63,57,65,57,0,56,58],
[44,44,51,50,42,41,67,51,49,49,44,0,47],
[46,46,53,55,40,45,54,59,52,37,42,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 110, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,43,51,51,44,48,46,47,52,49,37,50],
[47,0,53,56,41,43,48,52,42,45,42,40,54],
[57,47,0,48,45,40,40,49,42,42,48,40,45],
[49,44,52,0,44,47,40,48,48,40,42,44,45],
[49,59,55,56,0,56,57,51,46,49,48,48,50],
[56,57,60,53,44,0,52,50,49,47,57,54,54],
[52,52,60,60,43,48,0,57,56,47,54,55,59],
[54,48,51,52,49,50,43,0,40,44,52,49,48],
[53,58,58,52,54,51,44,60,0,44,48,38,56],
[48,55,58,60,51,53,53,56,56,0,59,58,50],
[51,58,52,58,52,43,46,48,52,41,0,46,48],
[63,60,60,56,52,46,45,51,62,42,54,0,54],
[50,46,55,55,50,46,41,52,44,50,52,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 111, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,62,56,21,35,57,86,41,47,20,83,54],
[53,0,65,24,37,63,37,86,69,83,36,83,37],
[38,35,0,37,28,35,38,57,41,54,27,64,28],
[44,76,63,0,57,64,83,86,77,66,64,93,66],
[79,63,72,43,0,73,66,85,60,76,34,99,56],
[65,37,65,36,27,0,54,73,76,66,43,70,34],
[43,63,62,17,34,46,0,80,52,66,33,70,14],
[14,14,43,14,15,27,20,0,33,47,14,40,14],
[59,31,59,23,40,24,48,67,0,50,30,76,28],
[53,17,46,34,24,34,34,53,50,0,17,79,14],
[80,64,73,36,66,57,67,86,70,83,0,83,47],
[17,17,36,7,1,30,30,60,24,21,17,0,7],
[46,63,72,34,44,66,86,86,72,86,53,93,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 112, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,44,46,44,52,47,48,47,43,50,43,53],
[50,0,42,45,46,53,40,49,50,42,40,45,44],
[56,58,0,55,48,54,52,50,56,46,49,51,50],
[54,55,45,0,42,55,54,54,50,44,44,55,54],
[56,54,52,58,0,54,55,47,53,50,56,47,50],
[48,47,46,45,46,0,43,45,45,37,47,36,48],
[53,60,48,46,45,57,0,50,47,48,46,51,50],
[52,51,50,46,53,55,50,0,52,45,54,46,52],
[53,50,44,50,47,55,53,48,0,44,47,48,51],
[57,58,54,56,50,63,52,55,56,0,52,51,59],
[50,60,51,56,44,53,54,46,53,48,0,51,59],
[57,55,49,45,53,64,49,54,52,49,49,0,50],
[47,56,50,46,50,52,50,48,49,41,41,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 113, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,45,50,49,45,50,44,45,50,46,42,51],
[52,0,48,51,47,52,48,53,50,47,50,47,54],
[55,52,0,48,48,55,51,47,58,56,48,52,50],
[50,49,52,0,50,50,54,46,58,53,50,50,57],
[51,53,52,50,0,53,52,53,50,55,52,45,60],
[55,48,45,50,47,0,50,52,46,55,48,48,51],
[50,52,49,46,48,50,0,49,44,51,52,43,49],
[56,47,53,54,47,48,51,0,57,59,46,52,55],
[55,50,42,42,50,54,56,43,0,52,45,44,56],
[50,53,44,47,45,45,49,41,48,0,49,44,43],
[54,50,52,50,48,52,48,54,55,51,0,49,55],
[58,53,48,50,55,52,57,48,56,56,51,0,53],
[49,46,50,43,40,49,51,45,44,57,45,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 114, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,45,36,45,39,47,39,40,37,39,46,45],
[60,0,50,49,51,54,45,37,44,43,46,55,50],
[55,50,0,36,51,45,49,40,48,48,40,51,51],
[64,51,64,0,48,51,58,44,46,50,53,63,46],
[55,49,49,52,0,42,48,44,45,43,38,54,46],
[61,46,55,49,58,0,55,49,50,48,45,52,51],
[53,55,51,42,52,45,0,40,41,43,45,49,46],
[61,63,60,56,56,51,60,0,61,53,47,61,54],
[60,56,52,54,55,50,59,39,0,52,53,59,52],
[63,57,52,50,57,52,57,47,48,0,44,61,44],
[61,54,60,47,62,55,55,53,47,56,0,57,53],
[54,45,49,37,46,48,51,39,41,39,43,0,46],
[55,50,49,54,54,49,54,46,48,56,47,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 115, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,50,46,59,47,53,42,38,62,43,55,39],
[57,0,63,49,57,44,46,51,33,64,43,58,48],
[50,37,0,37,46,31,52,41,45,61,45,50,48],
[54,51,63,0,79,53,55,52,55,61,44,66,47],
[41,43,54,21,0,30,42,43,38,50,41,52,42],
[53,56,69,47,70,0,57,53,52,53,53,59,55],
[47,54,48,45,58,43,0,47,48,59,46,54,50],
[58,49,59,48,57,47,53,0,49,67,48,62,41],
[62,67,55,45,62,48,52,51,0,63,60,61,48],
[38,36,39,39,50,47,41,33,37,0,37,45,32],
[57,57,55,56,59,47,54,52,40,63,0,55,44],
[45,42,50,34,48,41,46,38,39,55,45,0,47],
[61,52,52,53,58,45,50,59,52,68,56,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 116, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,55,54,54,53,48,50,50,49,49,53,46],
[52,0,49,57,51,47,45,47,45,47,45,53,51],
[45,51,0,50,47,51,42,49,41,47,44,52,49],
[46,43,50,0,47,46,40,46,41,52,42,47,48],
[46,49,53,53,0,45,43,49,51,48,45,55,49],
[47,53,49,54,55,0,48,50,55,64,50,54,52],
[52,55,58,60,57,52,0,56,56,52,48,55,49],
[50,53,51,54,51,50,44,0,55,53,39,49,49],
[50,55,59,59,49,45,44,45,0,48,48,48,44],
[51,53,53,48,52,36,48,47,52,0,48,46,45],
[51,55,56,58,55,50,52,61,52,52,0,58,56],
[47,47,48,53,45,46,45,51,52,54,42,0,45],
[54,49,51,52,51,48,51,51,56,55,44,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 117, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,47,63,53,46,51,52,36,47,59,56,52],
[50,0,57,59,47,47,55,57,50,51,61,54,44],
[53,43,0,60,47,48,49,64,49,47,58,56,38],
[37,41,40,0,44,38,44,53,44,50,54,55,48],
[47,53,53,56,0,55,57,62,46,48,61,55,47],
[54,53,52,62,45,0,59,68,43,50,64,54,47],
[49,45,51,56,43,41,0,62,43,52,59,58,38],
[48,43,36,47,38,32,38,0,39,43,52,40,36],
[64,50,51,56,54,57,57,61,0,58,67,61,54],
[53,49,53,50,52,50,48,57,42,0,59,58,44],
[41,39,42,46,39,36,41,48,33,41,0,50,33],
[44,46,44,45,45,46,42,60,39,42,50,0,36],
[48,56,62,52,53,53,62,64,46,56,67,64,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 118, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,52,53,46,53,43,45,50,49,56,45,53],
[51,0,52,59,49,58,56,56,58,56,45,59,57],
[48,48,0,50,32,49,55,50,43,50,59,51,57],
[47,41,50,0,51,57,45,55,44,46,52,55,59],
[54,51,68,49,0,61,59,57,48,53,56,56,71],
[47,42,51,43,39,0,52,55,47,44,59,56,54],
[57,44,45,55,41,48,0,53,45,42,51,49,51],
[55,44,50,45,43,45,47,0,39,48,49,55,57],
[50,42,57,56,52,53,55,61,0,43,50,58,59],
[51,44,50,54,47,56,58,52,57,0,54,52,56],
[44,55,41,48,44,41,49,51,50,46,0,58,55],
[55,41,49,45,44,44,51,45,42,48,42,0,47],
[47,43,43,41,29,46,49,43,41,44,45,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 119, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,55,73,53,66,92,77,60,74,50,63,48],
[43,0,37,38,19,40,46,57,43,36,23,32,50],
[45,63,0,70,51,68,91,66,60,73,45,54,58],
[27,62,30,0,38,64,81,66,50,58,27,55,54],
[47,81,49,62,0,84,86,68,63,70,64,62,72],
[34,60,32,36,16,0,48,42,35,41,22,31,31],
[8,54,9,19,14,52,0,30,15,18,11,7,33],
[23,43,34,34,32,58,70,0,43,44,40,38,43],
[40,57,40,50,37,65,85,57,0,47,42,31,49],
[26,64,27,42,30,59,82,56,53,0,18,25,46],
[50,77,55,73,36,78,89,60,58,82,0,59,56],
[37,68,46,45,38,69,93,62,69,75,41,0,58],
[52,50,42,46,28,69,67,57,51,54,44,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 120, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,67,34,35,40,44,86,50,44,69,50,61,35],
[33,0,33,48,39,33,66,62,58,33,43,43,39],
[66,67,0,35,39,67,71,35,25,50,49,47,35],
[65,52,65,0,54,65,81,77,73,48,29,65,54],
[60,61,61,46,0,61,86,63,54,63,58,75,35],
[56,67,33,35,39,0,71,68,44,73,49,66,68],
[14,34,29,19,14,29,0,33,39,48,48,29,14],
[50,38,65,23,37,32,67,0,25,54,35,65,37],
[56,42,75,27,46,56,61,75,0,56,39,75,56],
[31,67,50,52,37,27,52,46,44,0,43,60,47],
[50,57,51,71,42,51,52,65,61,57,0,65,42],
[39,57,53,35,25,34,71,35,25,40,35,0,25],
[65,61,65,46,65,32,86,63,44,53,58,75,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 121, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,53,53,43,53,59,48,50,52,51,53,46],
[62,0,57,52,49,52,55,48,53,60,63,55,52],
[47,43,0,54,48,52,56,50,50,54,50,47,54],
[47,48,46,0,52,58,51,47,46,50,59,58,51],
[57,51,52,48,0,50,52,54,45,54,52,47,46],
[47,48,48,42,50,0,50,53,41,54,57,51,40],
[41,45,44,49,48,50,0,44,46,47,48,44,43],
[52,52,50,53,46,47,56,0,47,55,55,57,50],
[50,47,50,54,55,59,54,53,0,59,52,52,53],
[48,40,46,50,46,46,53,45,41,0,49,48,41],
[49,37,50,41,48,43,52,45,48,51,0,49,44],
[47,45,53,42,53,49,56,43,48,52,51,0,44],
[54,48,46,49,54,60,57,50,47,59,56,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 122, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,42,61,50,55,62,45,53,64,46,60,48],
[42,0,36,44,43,48,49,37,40,47,47,47,37],
[58,64,0,57,55,56,49,51,56,63,61,65,57],
[39,56,43,0,51,47,61,48,45,68,46,47,36],
[50,57,45,49,0,37,60,37,50,50,54,54,40],
[45,52,44,53,63,0,58,48,49,48,57,43,56],
[38,51,51,39,40,42,0,42,47,50,37,46,40],
[55,63,49,52,63,52,58,0,51,61,56,60,52],
[47,60,44,55,50,51,53,49,0,53,40,56,42],
[36,53,37,32,50,52,50,39,47,0,45,49,43],
[54,53,39,54,46,43,63,44,60,55,0,54,45],
[40,53,35,53,46,57,54,40,44,51,46,0,46],
[52,63,43,64,60,44,60,48,58,57,55,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 123, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,25,42,42,53,25,55,38,26,31,41,44],
[74,0,41,62,41,53,43,53,51,41,35,51,67],
[75,59,0,72,71,71,45,79,77,60,49,51,69],
[58,38,28,0,27,45,21,38,45,24,33,31,38],
[58,59,29,73,0,63,52,53,57,42,52,55,62],
[47,47,29,55,37,0,42,57,52,28,32,36,53],
[75,57,55,79,48,58,0,59,73,52,62,61,89],
[45,47,21,62,47,43,41,0,43,19,35,34,39],
[62,49,23,55,43,48,27,57,0,32,19,36,53],
[74,59,40,76,58,72,48,81,68,0,61,31,66],
[69,65,51,67,48,68,38,65,81,39,0,61,60],
[59,49,49,69,45,64,39,66,64,69,39,0,55],
[56,33,31,62,38,47,11,61,47,34,40,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 124, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,60,58,61,55,54,54,49,58,59,55,60],
[49,0,46,56,51,37,39,48,42,55,44,49,48],
[40,54,0,59,52,45,45,50,53,49,50,54,51],
[42,44,41,0,41,40,41,34,46,51,45,46,46],
[39,49,48,59,0,44,47,39,55,47,47,50,45],
[45,63,55,60,56,0,44,46,52,55,53,50,65],
[46,61,55,59,53,56,0,50,52,61,53,58,61],
[46,52,50,66,61,54,50,0,55,59,51,53,50],
[51,58,47,54,45,48,48,45,0,46,47,46,53],
[42,45,51,49,53,45,39,41,54,0,46,46,45],
[41,56,50,55,53,47,47,49,53,54,0,53,53],
[45,51,46,54,50,50,42,47,54,54,47,0,51],
[40,52,49,54,55,35,39,50,47,55,47,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 125, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,55,45,59,39,58,44,49,45,49,33,46],
[68,0,65,50,62,50,68,60,65,65,59,47,70],
[45,35,0,46,40,44,48,60,48,45,52,38,53],
[55,50,54,0,47,58,66,50,60,57,67,47,56],
[41,38,60,53,0,44,63,56,49,64,56,45,61],
[61,50,56,42,56,0,57,49,57,49,60,55,55],
[42,32,52,34,37,43,0,42,30,34,49,40,38],
[56,40,40,50,44,51,58,0,59,35,56,34,46],
[51,35,52,40,51,43,70,41,0,58,53,42,51],
[55,35,55,43,36,51,66,65,42,0,46,30,61],
[51,41,48,33,44,40,51,44,47,54,0,38,52],
[67,53,62,53,55,45,60,66,58,70,62,0,75],
[54,30,47,44,39,45,62,54,49,39,48,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 126, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,49,50,37,45,59,51,48,42,54,57,44],
[44,0,48,52,39,45,63,49,52,47,54,50,45],
[51,52,0,54,42,46,64,54,50,54,56,63,48],
[50,48,46,0,35,36,58,52,48,44,45,53,46],
[63,61,58,65,0,53,61,49,56,56,64,56,53],
[55,55,54,64,47,0,69,54,50,54,55,59,49],
[41,37,36,42,39,31,0,44,37,38,39,48,37],
[49,51,46,48,51,46,56,0,46,49,50,54,41],
[52,48,50,52,44,50,63,54,0,43,56,50,45],
[58,53,46,56,44,46,62,51,57,0,51,52,49],
[46,46,44,55,36,45,61,50,44,49,0,50,49],
[43,50,37,47,44,41,52,46,50,48,50,0,48],
[56,55,52,54,47,51,63,59,55,51,51,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 127, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,71,57,43,61,59,48,57,46,48,62,56,50],
[29,0,45,39,44,42,35,44,35,28,42,55,27],
[43,55,0,38,51,42,40,48,38,41,58,53,47],
[57,61,62,0,70,57,54,53,53,54,71,63,46],
[39,56,49,30,0,37,38,41,41,48,46,54,49],
[41,58,58,43,63,0,35,47,44,42,61,54,47],
[52,65,60,46,62,65,0,53,52,60,62,65,62],
[43,56,52,47,59,53,47,0,47,50,51,53,38],
[54,65,62,47,59,56,48,53,0,46,65,68,50],
[52,72,59,46,52,58,40,50,54,0,54,54,53],
[38,58,42,29,54,39,38,49,35,46,0,43,43],
[44,45,47,37,46,46,35,47,32,46,57,0,30],
[50,73,53,54,51,53,38,62,50,47,57,70,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 128, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,44,39,36,47,38,37,44,39,45,38,44],
[61,0,55,44,44,52,47,46,58,45,56,48,55],
[56,45,0,46,43,54,46,44,47,50,55,41,52],
[61,56,54,0,51,46,52,50,50,52,55,49,54],
[64,56,57,49,0,49,51,46,47,54,63,58,49],
[53,48,46,54,51,0,46,46,48,55,52,45,54],
[62,53,54,48,49,54,0,50,51,47,56,53,50],
[63,54,56,50,54,54,50,0,48,55,58,52,52],
[56,42,53,50,53,52,49,52,0,50,50,41,52],
[61,55,50,48,46,45,53,45,50,0,53,49,58],
[55,44,45,45,37,48,44,42,50,47,0,39,49],
[62,52,59,51,42,55,47,48,59,51,61,0,59],
[56,45,48,46,51,46,50,48,48,42,51,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 129, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,56,46,45,55,54,55,60,66,56,53,55],
[44,0,42,48,41,44,37,43,52,58,52,44,54],
[44,58,0,53,41,48,40,46,56,54,52,44,56],
[54,52,47,0,33,45,50,44,56,50,56,50,47],
[55,59,59,67,0,49,49,52,62,64,57,45,62],
[45,56,52,55,51,0,46,51,61,60,50,45,55],
[46,63,60,50,51,54,0,52,62,56,60,40,52],
[45,57,54,56,48,49,48,0,50,62,52,36,60],
[40,48,44,44,38,39,38,50,0,53,57,41,49],
[34,42,46,50,36,40,44,38,47,0,43,41,48],
[44,48,48,44,43,50,40,48,43,57,0,42,55],
[47,56,56,50,55,55,60,64,59,59,58,0,59],
[45,46,44,53,38,45,48,40,51,52,45,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 130, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,60,52,54,51,51,46,60,45,39,47,50],
[46,0,58,41,50,44,40,52,51,47,38,38,44],
[40,42,0,35,46,50,48,47,52,40,44,40,50],
[48,59,65,0,57,59,50,54,57,46,49,39,66],
[46,50,54,43,0,54,55,53,57,45,41,41,46],
[49,56,50,41,46,0,43,52,54,42,41,32,49],
[49,60,52,50,45,57,0,54,55,46,46,32,45],
[54,48,53,46,47,48,46,0,51,44,42,40,48],
[40,49,48,43,43,46,45,49,0,45,23,34,45],
[55,53,60,54,55,58,54,56,55,0,51,45,65],
[61,62,56,51,59,59,54,58,77,49,0,54,64],
[53,62,60,61,59,68,68,60,66,55,46,0,61],
[50,56,50,34,54,51,55,52,55,35,36,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 131, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,54,53,49,55,54,51,51,46,49,46,53],
[53,0,56,47,51,51,47,51,47,44,44,50,48],
[46,44,0,46,50,52,56,44,41,43,50,48,50],
[47,53,54,0,52,51,50,45,50,51,50,51,59],
[51,49,50,48,0,48,49,45,45,44,51,52,44],
[45,49,48,49,52,0,52,43,43,36,53,44,50],
[46,53,44,50,51,48,0,47,39,41,51,40,52],
[49,49,56,55,55,57,53,0,46,49,48,58,48],
[49,53,59,50,55,57,61,54,0,44,59,57,51],
[54,56,57,49,56,64,59,51,56,0,52,55,56],
[51,56,50,50,49,47,49,52,41,48,0,54,45],
[54,50,52,49,48,56,60,42,43,45,46,0,43],
[47,52,50,41,56,50,48,52,49,44,55,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 132, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,51,55,54,46,46,53,45,45,46,48,45],
[48,0,43,55,53,47,43,46,37,47,40,50,47],
[49,57,0,52,52,45,43,48,41,42,31,43,51],
[45,45,48,0,42,47,32,42,41,39,33,41,38],
[46,47,48,58,0,53,48,52,51,45,41,56,48],
[54,53,55,53,47,0,40,50,42,47,44,50,48],
[54,57,57,68,52,60,0,51,53,50,56,48,53],
[47,54,52,58,48,50,49,0,45,46,48,50,50],
[55,63,59,59,49,58,47,55,0,50,47,55,46],
[55,53,58,61,55,53,50,54,50,0,52,52,50],
[54,60,69,67,59,56,44,52,53,48,0,56,51],
[52,50,57,59,44,50,52,50,45,48,44,0,51],
[55,53,49,62,52,52,47,50,54,50,49,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 133, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,64,64,65,50,56,60,63,68,63,54,60],
[42,0,54,60,31,26,49,41,57,58,50,40,44],
[36,46,0,57,53,35,42,28,45,63,46,61,57],
[36,40,43,0,48,41,49,34,45,62,43,58,31],
[35,69,47,52,0,41,59,44,52,66,45,57,59],
[50,74,65,59,59,0,58,49,62,77,63,48,61],
[44,51,58,51,41,42,0,34,58,67,50,50,57],
[40,59,72,66,56,51,66,0,57,72,66,62,63],
[37,43,55,55,48,38,42,43,0,58,63,45,49],
[32,42,37,38,34,23,33,28,42,0,34,48,28],
[37,50,54,57,55,37,50,34,37,66,0,40,55],
[46,60,39,42,43,52,50,38,55,52,60,0,58],
[40,56,43,69,41,39,43,37,51,72,45,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 134, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,43,50,58,47,49,47,47,46,47,52,47],
[48,0,41,41,52,49,51,48,41,45,50,49,47],
[57,59,0,47,60,51,54,58,52,51,61,55,56],
[50,59,53,0,58,56,56,54,48,48,60,58,57],
[42,48,40,42,0,39,43,50,44,41,49,43,39],
[53,51,49,44,61,0,48,49,42,47,55,48,49],
[51,49,46,44,57,52,0,48,49,48,46,49,49],
[53,52,42,46,50,51,52,0,47,49,52,47,53],
[53,59,48,52,56,58,51,53,0,49,55,58,48],
[54,55,49,52,59,53,52,51,51,0,55,51,50],
[53,50,39,40,51,45,54,48,45,45,0,50,47],
[48,51,45,42,57,52,51,53,42,49,50,0,51],
[53,53,44,43,61,51,51,47,52,50,53,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 135, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,55,57,43,62,56,42,71,68,64,50,54],
[49,0,52,62,49,58,66,41,63,75,60,47,45],
[45,48,0,70,58,48,67,48,59,64,66,56,46],
[43,38,30,0,47,53,61,51,49,69,48,49,47],
[57,51,42,53,0,68,73,50,48,67,59,47,61],
[38,42,52,47,32,0,40,22,54,63,40,32,52],
[44,34,33,39,27,60,0,28,46,53,47,29,32],
[58,59,52,49,50,78,72,0,58,88,69,64,60],
[29,37,41,51,52,46,54,42,0,65,57,38,37],
[32,25,36,31,33,37,47,12,35,0,46,38,18],
[36,40,34,52,41,60,53,31,43,54,0,35,35],
[50,53,44,51,53,68,71,36,62,62,65,0,48],
[46,55,54,53,39,48,68,40,63,82,65,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 136, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,51,54,65,44,40,37,36,60,52,47,41],
[51,0,41,71,65,57,56,51,43,70,58,53,56],
[49,59,0,63,54,60,54,55,50,60,51,43,55],
[46,29,37,0,47,32,31,38,42,47,30,15,41],
[35,35,46,53,0,39,42,37,42,32,50,25,28],
[56,43,40,68,61,0,50,55,42,55,71,41,48],
[60,44,46,69,58,50,0,53,47,58,60,49,60],
[63,49,45,62,63,45,47,0,50,54,40,38,51],
[64,57,50,58,58,58,53,50,0,55,62,46,49],
[40,30,40,53,68,45,42,46,45,0,44,41,33],
[48,42,49,70,50,29,40,60,38,56,0,36,51],
[53,47,57,85,75,59,51,62,54,59,64,0,67],
[59,44,45,59,72,52,40,49,51,67,49,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 137, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,53,61,60,57,50,44,51,60,45,58,44],
[49,0,54,54,54,60,55,47,46,49,42,45,51],
[47,46,0,49,46,51,51,51,45,49,41,52,43],
[39,46,51,0,44,54,52,37,50,48,41,40,42],
[40,46,54,56,0,54,46,49,49,57,43,46,44],
[43,40,49,46,46,0,42,46,42,51,39,37,31],
[50,45,49,48,54,58,0,45,47,52,42,55,46],
[56,53,49,63,51,54,55,0,60,52,49,49,44],
[49,54,55,50,51,58,53,40,0,47,47,42,50],
[40,51,51,52,43,49,48,48,53,0,40,40,36],
[55,58,59,59,57,61,58,51,53,60,0,59,50],
[42,55,48,60,54,63,45,51,58,60,41,0,42],
[56,49,57,58,56,69,54,56,50,64,50,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 138, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,33,44,42,56,47,57,56,48,40,41,42],
[53,0,54,49,50,60,55,70,50,58,57,51,53],
[67,46,0,57,62,58,54,66,53,55,55,54,47],
[56,51,43,0,49,51,61,78,51,47,56,46,47],
[58,50,38,51,0,54,55,64,47,43,53,58,50],
[44,40,42,49,46,0,43,56,30,37,42,40,47],
[53,45,46,39,45,57,0,58,47,45,47,38,48],
[43,30,34,22,36,44,42,0,33,39,38,29,38],
[44,50,47,49,53,70,53,67,0,63,63,57,49],
[52,42,45,53,57,63,55,61,37,0,53,50,45],
[60,43,45,44,47,58,53,62,37,47,0,56,58],
[59,49,46,54,42,60,62,71,43,50,44,0,60],
[58,47,53,53,50,53,52,62,51,55,42,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 139, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,63,56,40,53,45,46,48,50,49,49,45],
[51,0,60,46,37,52,51,49,47,47,45,52,51],
[37,40,0,46,37,50,39,46,45,46,52,45,44],
[44,54,54,0,47,57,54,52,45,47,59,49,51],
[60,63,63,53,0,61,61,62,56,56,61,59,50],
[47,48,50,43,39,0,45,52,41,40,49,51,44],
[55,49,61,46,39,55,0,57,45,49,54,50,50],
[54,51,54,48,38,48,43,0,45,44,50,53,55],
[52,53,55,55,44,59,55,55,0,44,55,53,55],
[50,53,54,53,44,60,51,56,56,0,53,62,45],
[51,55,48,41,39,51,46,50,45,47,0,55,51],
[51,48,55,51,41,49,50,47,47,38,45,0,57],
[55,49,56,49,50,56,50,45,45,55,49,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 140, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,48,55,67,49,45,56,62,60,49,57,58],
[43,0,44,53,57,46,47,44,53,60,46,53,48],
[52,56,0,58,57,60,45,53,67,63,52,53,55],
[45,47,42,0,52,46,48,46,59,48,50,59,48],
[33,43,43,48,0,45,37,48,49,52,38,48,46],
[51,54,40,54,55,0,43,45,57,50,48,53,49],
[55,53,55,52,63,57,0,57,64,54,49,55,57],
[44,56,47,54,52,55,43,0,57,59,50,53,57],
[38,47,33,41,51,43,36,43,0,49,36,49,40],
[40,40,37,52,48,50,46,41,51,0,43,47,48],
[51,54,48,50,62,52,51,50,64,57,0,59,61],
[43,47,47,41,52,47,45,47,51,53,41,0,48],
[42,52,45,52,54,51,43,43,60,52,39,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 141, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,52,58,42,52,48,50,37,54,35,58,40],
[51,0,50,53,50,53,45,58,44,54,35,51,52],
[48,50,0,59,50,49,39,49,42,43,38,47,41],
[42,47,41,0,42,45,33,51,36,44,35,49,37],
[58,50,50,58,0,60,55,50,45,56,46,60,50],
[48,47,51,55,40,0,51,50,51,51,35,45,39],
[52,55,61,67,45,49,0,54,44,60,46,59,51],
[50,42,51,49,50,50,46,0,47,49,39,54,47],
[63,56,58,64,55,49,56,53,0,57,43,52,46],
[46,46,57,56,44,49,40,51,43,0,39,45,47],
[65,65,62,65,54,65,54,61,57,61,0,55,50],
[42,49,53,51,40,55,41,46,48,55,45,0,44],
[60,48,59,63,50,61,49,53,54,53,50,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 142, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,55,43,47,56,60,57,53,55,48,52,48],
[41,0,49,45,42,48,52,54,46,47,41,55,44],
[45,51,0,53,42,51,64,57,49,50,42,53,51],
[57,55,47,0,45,51,58,56,47,53,44,44,46],
[53,58,58,55,0,57,64,57,63,50,53,57,59],
[44,52,49,49,43,0,50,49,44,44,42,48,42],
[40,48,36,42,36,50,0,48,41,35,41,39,50],
[43,46,43,44,43,51,52,0,45,42,48,51,49],
[47,54,51,53,37,56,59,55,0,43,43,50,57],
[45,53,50,47,50,56,65,58,57,0,54,54,51],
[52,59,58,56,47,58,59,52,57,46,0,56,58],
[48,45,47,56,43,52,61,49,50,46,44,0,55],
[52,56,49,54,41,58,50,51,43,49,42,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 143, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,43,35,33,41,46,36,45,49,42,38,51],
[60,0,54,48,40,51,41,43,55,54,53,48,59],
[57,46,0,56,42,57,53,51,60,58,54,49,59],
[65,52,44,0,40,52,57,49,51,45,54,50,52],
[67,60,58,60,0,61,55,44,65,54,61,55,58],
[59,49,43,48,39,0,44,44,55,48,57,43,63],
[54,59,47,43,45,56,0,47,57,45,50,53,52],
[64,57,49,51,56,56,53,0,55,57,52,53,64],
[55,45,40,49,35,45,43,45,0,44,45,42,51],
[51,46,42,55,46,52,55,43,56,0,57,50,55],
[58,47,46,46,39,43,50,48,55,43,0,38,54],
[62,52,51,50,45,57,47,47,58,50,62,0,61],
[49,41,41,48,42,37,48,36,49,45,46,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 144, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,56,45,52,54,53,55,47,42,50,55,45],
[49,0,46,38,51,44,48,50,43,29,53,52,42],
[44,54,0,46,52,60,57,47,42,40,49,54,46],
[55,62,54,0,53,53,59,56,50,49,48,60,50],
[48,49,48,47,0,42,48,49,41,34,49,51,43],
[46,56,40,47,58,0,52,49,49,42,46,49,47],
[47,52,43,41,52,48,0,55,44,42,49,47,42],
[45,50,53,44,51,51,45,0,46,43,52,43,45],
[53,57,58,50,59,51,56,54,0,50,65,68,46],
[58,71,60,51,66,58,58,57,50,0,62,58,57],
[50,47,51,52,51,54,51,48,35,38,0,49,48],
[45,48,46,40,49,51,53,57,32,42,51,0,43],
[55,58,54,50,57,53,58,55,54,43,52,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 145, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,77,25,48,57,82,52,47,51,49,59,47],
[46,0,52,43,48,29,71,66,65,70,24,53,70],
[23,48,0,19,42,46,72,66,65,70,67,23,46],
[75,57,81,0,52,32,82,57,47,56,53,81,52],
[52,52,58,48,0,50,99,52,70,74,72,76,71],
[43,71,54,68,50,0,91,68,67,90,49,49,67],
[18,29,28,18,1,9,0,25,24,69,49,33,18],
[48,34,34,43,48,32,75,0,23,74,49,34,71],
[53,35,35,53,30,33,76,77,0,75,58,35,76],
[49,30,30,44,26,10,31,26,25,0,49,35,25],
[51,76,33,47,28,51,51,51,42,51,0,51,47],
[41,47,77,19,24,51,67,66,65,65,49,0,41],
[53,30,54,48,29,33,82,29,24,75,53,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 146, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,50,50,54,54,55,57,49,58,53,59,64],
[49,0,46,48,52,51,57,49,43,50,54,55,57],
[50,54,0,51,58,57,60,60,58,52,51,59,54],
[50,52,49,0,59,49,52,51,51,60,46,51,53],
[46,48,42,41,0,54,55,56,48,53,52,51,54],
[46,49,43,51,46,0,56,60,47,47,39,53,60],
[45,43,40,48,45,44,0,43,44,44,38,47,53],
[43,51,40,49,44,40,57,0,46,58,40,58,46],
[51,57,42,49,52,53,56,54,0,61,38,55,53],
[42,50,48,40,47,53,56,42,39,0,43,51,62],
[47,46,49,54,48,61,62,60,62,57,0,48,62],
[41,45,41,49,49,47,53,42,45,49,52,0,55],
[36,43,46,47,46,40,47,54,47,38,38,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 147, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,30,58,47,25,33,52,26,47,39,37,42],
[60,0,44,66,58,50,54,64,50,46,44,51,60],
[70,56,0,67,48,51,62,64,53,45,60,38,53],
[42,34,33,0,47,29,47,50,25,40,45,40,45],
[53,42,52,53,0,40,56,60,46,50,49,44,55],
[75,50,49,71,60,0,57,66,52,57,70,51,78],
[67,46,38,53,44,43,0,55,51,57,59,36,58],
[48,36,36,50,40,34,45,0,36,52,31,43,41],
[74,50,47,75,54,48,49,64,0,65,51,44,59],
[53,54,55,60,50,43,43,48,35,0,43,50,49],
[61,56,40,55,51,30,41,69,49,57,0,48,66],
[63,49,62,60,56,49,64,57,56,50,52,0,62],
[58,40,47,55,45,22,42,59,41,51,34,38,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 148, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,45,56,57,46,36,42,38,35,42,38,50],
[58,0,67,50,61,52,58,54,57,50,43,46,62],
[55,33,0,45,48,38,51,35,34,35,41,46,37],
[44,50,55,0,50,48,46,42,37,45,51,51,66],
[43,39,52,50,0,46,49,36,33,42,54,50,48],
[54,48,62,52,54,0,58,33,36,48,57,57,56],
[64,42,49,54,51,42,0,33,31,40,47,53,56],
[58,46,65,58,64,67,67,0,61,63,71,59,63],
[62,43,66,63,67,64,69,39,0,50,63,56,58],
[65,50,65,55,58,52,60,37,50,0,63,67,65],
[58,57,59,49,46,43,53,29,37,37,0,52,56],
[62,54,54,49,50,43,47,41,44,33,48,0,52],
[50,38,63,34,52,44,44,37,42,35,44,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 149, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,53,56,58,57,42,39,52,42,53,60,53],
[38,0,46,43,63,51,36,48,50,40,45,68,48],
[47,54,0,51,53,61,41,54,49,50,53,50,42],
[44,57,49,0,63,54,41,45,50,42,42,54,48],
[42,37,47,37,0,43,29,40,43,35,33,40,37],
[43,49,39,46,57,0,34,42,48,42,42,54,41],
[58,64,59,59,71,66,0,54,58,42,66,64,60],
[61,52,46,55,60,58,46,0,54,33,62,59,51],
[48,50,51,50,57,52,42,46,0,52,42,57,42],
[58,60,50,58,65,58,58,67,48,0,58,62,56],
[47,55,47,58,67,58,34,38,58,42,0,66,52],
[40,32,50,46,60,46,36,41,43,38,34,0,38],
[47,52,58,52,63,59,40,49,58,44,48,62,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 150, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,61,49,59,47,49,40,40,42,39,47,57],
[47,0,52,49,55,49,39,44,45,45,36,50,57],
[39,48,0,44,45,40,52,40,45,44,35,46,47],
[51,51,56,0,53,44,42,40,43,35,43,49,54],
[41,45,55,47,0,38,42,40,43,40,35,52,49],
[53,51,60,56,62,0,59,52,47,46,45,53,58],
[51,61,48,58,58,41,0,41,36,42,44,49,54],
[60,56,60,60,60,48,59,0,51,51,50,58,62],
[60,55,55,57,57,53,64,49,0,44,51,57,61],
[58,55,56,65,60,54,58,49,56,0,46,59,59],
[61,64,65,57,65,55,56,50,49,54,0,60,57],
[53,50,54,51,48,47,51,42,43,41,40,0,54],
[43,43,53,46,51,42,46,38,39,41,43,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 151, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,51,40,41,48,41,52,43,49,43,40,40],
[51,0,56,48,44,47,43,48,45,52,42,41,39],
[49,44,0,42,46,51,46,44,42,50,43,42,46],
[60,52,58,0,52,59,53,49,50,48,51,48,45],
[59,56,54,48,0,53,53,52,47,59,52,53,48],
[52,53,49,41,47,0,44,49,44,54,47,48,44],
[59,57,54,47,47,56,0,55,47,51,48,49,47],
[48,52,56,51,48,51,45,0,43,47,45,45,41],
[57,55,58,50,53,56,53,57,0,53,58,53,54],
[51,48,50,52,41,46,49,53,47,0,50,37,43],
[57,58,57,49,48,53,52,55,42,50,0,46,42],
[60,59,58,52,47,52,51,55,47,63,54,0,53],
[60,61,54,55,52,56,53,59,46,57,58,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 152, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,32,32,2,32,63,9,2,32,32,62,60],
[68,0,37,68,38,40,38,38,40,38,30,68,68],
[68,63,0,68,70,70,70,40,70,70,63,100,98],
[68,32,32,0,33,40,70,40,9,70,32,69,98],
[98,62,30,67,0,100,100,70,39,37,60,69,98],
[68,60,30,60,0,0,68,38,9,37,60,67,98],
[37,62,30,30,0,32,0,37,39,30,60,32,67],
[91,62,60,60,30,62,63,0,62,30,60,62,91],
[98,60,30,91,61,91,61,38,0,61,60,60,91],
[68,62,30,30,63,63,70,70,39,0,62,39,68],
[68,70,37,68,40,40,40,40,40,38,0,70,68],
[38,32,0,31,31,33,68,38,40,61,30,0,98],
[40,32,2,2,2,2,33,9,9,32,32,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 153, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,43,49,44,43,49,46,38,48,41,48,45],
[56,0,57,55,56,53,53,56,48,57,57,52,64],
[57,43,0,47,50,46,46,49,48,46,47,60,57],
[51,45,53,0,45,42,48,48,44,54,42,53,53],
[56,44,50,55,0,46,52,55,53,45,52,58,55],
[57,47,54,58,54,0,46,57,49,54,52,50,65],
[51,47,54,52,48,54,0,54,44,56,48,48,54],
[54,44,51,52,45,43,46,0,45,43,48,49,55],
[62,52,52,56,47,51,56,55,0,58,60,53,62],
[52,43,54,46,55,46,44,57,42,0,50,51,52],
[59,43,53,58,48,48,52,52,40,50,0,58,55],
[52,48,40,47,42,50,52,51,47,49,42,0,56],
[55,36,43,47,45,35,46,45,38,48,45,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 154, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,48,47,53,51,35,44,50,41,40,37,43],
[55,0,51,58,54,57,43,51,56,50,43,43,46],
[52,49,0,60,53,54,53,53,53,55,41,51,48],
[53,42,40,0,46,40,45,46,46,48,48,44,47],
[47,46,47,54,0,61,45,54,55,54,40,41,44],
[49,43,46,60,39,0,44,45,52,51,44,41,44],
[65,57,47,55,55,56,0,56,54,59,48,46,49],
[56,49,47,54,46,55,44,0,52,44,47,38,41],
[50,44,47,54,45,48,46,48,0,50,39,48,41],
[59,50,45,52,46,49,41,56,50,0,49,42,49],
[60,57,59,52,60,56,52,53,61,51,0,47,50],
[63,57,49,56,59,59,54,62,52,58,53,0,56],
[57,54,52,53,56,56,51,59,59,51,50,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 155, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,68,35,39,48,46,58,45,46,40,58,47,35],
[32,0,37,32,60,39,44,50,32,40,49,48,38],
[65,63,0,58,79,50,71,53,69,62,65,51,58],
[61,68,42,0,68,54,74,55,48,48,49,57,61],
[52,40,21,32,0,40,59,41,35,24,37,39,28],
[54,61,50,46,60,0,45,41,50,40,67,53,43],
[42,56,29,26,41,55,0,43,27,38,48,49,48],
[55,50,47,45,59,59,57,0,57,52,54,50,45],
[54,68,31,52,65,50,73,43,0,60,45,49,37],
[60,60,38,52,76,60,62,48,40,0,50,61,56],
[42,51,35,51,63,33,52,46,55,50,0,48,63],
[53,52,49,43,61,47,51,50,51,39,52,0,55],
[65,62,42,39,72,57,52,55,63,44,37,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 156, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,55,57,40,48,50,46,54,54,47,48,52],
[49,0,50,64,46,52,55,46,51,44,52,66,52],
[45,50,0,54,45,53,60,54,52,45,50,58,58],
[43,36,46,0,39,47,56,45,51,40,49,49,42],
[60,54,55,61,0,60,57,50,56,52,57,66,56],
[52,48,47,53,40,0,59,51,57,43,46,58,51],
[50,45,40,44,43,41,0,39,40,43,36,49,41],
[54,54,46,55,50,49,61,0,49,52,55,44,50],
[46,49,48,49,44,43,60,51,0,53,47,53,55],
[46,56,55,60,48,57,57,48,47,0,47,57,45],
[53,48,50,51,43,54,64,45,53,53,0,60,46],
[52,34,42,51,34,42,51,56,47,43,40,0,48],
[48,48,42,58,44,49,59,50,45,55,54,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 157, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,55,41,60,60,63,48,54,52,62,55,48],
[52,0,41,51,57,57,56,54,53,55,47,62,51],
[45,59,0,57,50,61,59,47,55,46,55,57,42],
[59,49,43,0,51,46,44,49,59,40,55,60,51],
[40,43,50,49,0,50,48,29,58,53,50,40,37],
[40,43,39,54,50,0,51,46,61,52,55,41,52],
[37,44,41,56,52,49,0,39,62,34,47,50,39],
[52,46,53,51,71,54,61,0,59,70,53,50,39],
[46,47,45,41,42,39,38,41,0,40,49,50,28],
[48,45,54,60,47,48,66,30,60,0,53,53,41],
[38,53,45,45,50,45,53,47,51,47,0,41,32],
[45,38,43,40,60,59,50,50,50,47,59,0,50],
[52,49,58,49,63,48,61,61,72,59,68,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 158, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,53,52,47,54,47,36,63,60,50,48,50],
[39,0,56,47,40,48,49,38,44,45,45,42,49],
[47,44,0,49,48,52,55,44,57,53,53,38,53],
[48,53,51,0,46,51,50,47,59,56,46,44,48],
[53,60,52,54,0,47,56,47,60,65,65,51,57],
[46,52,48,49,53,0,52,33,48,49,50,51,53],
[53,51,45,50,44,48,0,46,60,62,55,49,49],
[64,62,56,53,53,67,54,0,63,66,60,54,49],
[37,56,43,41,40,52,40,37,0,45,47,37,46],
[40,55,47,44,35,51,38,34,55,0,38,46,44],
[50,55,47,54,35,50,45,40,53,62,0,49,47],
[52,58,62,56,49,49,51,46,63,54,51,0,56],
[50,51,47,52,43,47,51,51,54,56,53,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 159, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,67,56,56,52,55,57,68,51,58,61,58,46],
[33,0,44,42,46,38,45,57,46,51,59,49,41],
[44,56,0,46,49,46,48,46,47,54,50,49,47],
[44,58,54,0,47,45,52,51,47,48,54,49,41],
[48,54,51,53,0,46,44,46,42,55,59,43,38],
[45,62,54,55,54,0,47,59,57,59,62,69,55],
[43,55,52,48,56,53,0,63,58,63,62,46,51],
[32,43,54,49,54,41,37,0,50,57,55,48,42],
[49,54,53,53,58,43,42,50,0,60,54,48,45],
[42,49,46,52,45,41,37,43,40,0,51,42,39],
[39,41,50,46,41,38,38,45,46,49,0,41,50],
[42,51,51,51,57,31,54,52,52,58,59,0,46],
[54,59,53,59,62,45,49,58,55,61,50,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 160, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,64,55,49,57,42,90,42,87,39,27,57],
[43,0,68,35,47,54,30,58,42,66,10,50,33],
[36,32,0,48,17,27,26,48,45,82,20,56,36],
[45,65,52,0,65,52,28,77,52,52,52,52,68],
[51,53,83,35,0,73,13,86,65,83,23,43,71],
[43,46,73,48,27,0,23,66,55,96,13,33,44],
[58,70,74,72,87,77,0,90,87,77,45,65,78],
[10,42,52,23,14,34,10,0,10,34,4,34,37],
[58,58,55,48,35,45,13,90,0,78,40,58,58],
[13,34,18,48,17,4,23,66,22,0,0,33,16],
[61,90,80,48,77,87,55,96,60,100,0,84,96],
[73,50,44,48,57,67,35,66,42,67,16,0,76],
[43,67,64,32,29,56,22,63,42,84,4,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 161, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,45,51,42,48,55,50,64,55,49,45,58],
[49,0,45,51,37,51,55,50,62,52,50,45,54],
[55,55,0,57,46,60,59,51,68,57,46,51,63],
[49,49,43,0,33,40,47,39,59,57,47,48,49],
[58,63,54,67,0,57,51,47,60,55,48,53,64],
[52,49,40,60,43,0,55,47,55,53,47,49,62],
[45,45,41,53,49,45,0,50,56,50,48,44,47],
[50,50,49,61,53,53,50,0,54,49,48,54,62],
[36,38,32,41,40,45,44,46,0,47,44,41,50],
[45,48,43,43,45,47,50,51,53,0,41,48,52],
[51,50,54,53,52,53,52,52,56,59,0,42,53],
[55,55,49,52,47,51,56,46,59,52,58,0,67],
[42,46,37,51,36,38,53,38,50,48,47,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 162, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,68,49,62,57,60,54,45,62,53,56,43],
[46,0,53,41,58,59,63,45,49,62,57,43,35],
[32,47,0,44,43,48,60,42,41,52,53,46,31],
[51,59,56,0,60,47,53,44,42,59,55,55,52],
[38,42,57,40,0,57,63,37,41,55,51,41,38],
[43,41,52,53,43,0,52,38,38,45,50,47,31],
[40,37,40,47,37,48,0,41,24,42,52,41,35],
[46,55,58,56,63,62,59,0,49,60,53,55,45],
[55,51,59,58,59,62,76,51,0,56,57,64,48],
[38,38,48,41,45,55,58,40,44,0,49,41,41],
[47,43,47,45,49,50,48,47,43,51,0,53,44],
[44,57,54,45,59,53,59,45,36,59,47,0,43],
[57,65,69,48,62,69,65,55,52,59,56,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 163, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,34,28,29,22,6,28,33,22,33,22,40],
[77,0,77,40,30,29,7,53,52,65,40,41,66],
[66,23,0,52,18,46,30,76,40,81,62,1,76],
[72,60,48,0,24,46,24,48,71,81,81,13,82],
[71,70,82,76,0,46,51,76,48,70,81,48,88],
[78,71,54,54,54,0,77,54,76,76,64,48,76],
[94,93,70,76,49,23,0,76,71,70,58,60,65],
[72,47,24,52,24,46,24,0,46,59,57,13,60],
[67,48,60,29,52,24,29,54,0,70,81,1,66],
[78,35,19,19,30,24,30,41,30,0,40,13,44],
[67,60,38,19,19,36,42,43,19,60,0,13,44],
[78,59,99,87,52,52,40,87,99,87,87,0,99],
[60,34,24,18,12,24,35,40,34,56,56,1,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 164, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,29,60,36,31,44,22,42,42,29,43,31],
[69,0,44,51,65,50,52,38,38,78,45,66,28],
[71,56,0,57,71,57,41,50,36,59,49,69,44],
[40,49,43,0,46,39,52,42,22,66,31,63,36],
[64,35,29,54,0,40,52,45,44,61,39,65,26],
[69,50,43,61,60,0,52,41,51,78,56,65,38],
[56,48,59,48,48,48,0,36,24,58,55,55,49],
[78,62,50,58,55,59,64,0,65,49,49,64,38],
[58,62,64,78,56,49,76,35,0,68,54,65,48],
[58,22,41,34,39,22,42,51,32,0,35,43,30],
[71,55,51,69,61,44,45,51,46,65,0,80,57],
[57,34,31,37,35,35,45,36,35,57,20,0,38],
[69,72,56,64,74,62,51,62,52,70,43,62,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 165, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,55,57,55,51,40,42,52,60,57,64,61],
[48,0,49,49,54,53,52,50,40,54,55,51,47],
[45,51,0,49,49,57,45,47,47,60,60,49,52],
[43,51,51,0,52,49,49,49,51,53,59,49,56],
[45,46,51,48,0,56,38,45,44,42,55,54,53],
[49,47,43,51,44,0,44,41,54,53,52,51,52],
[60,48,55,51,62,56,0,49,47,53,58,54,65],
[58,50,53,51,55,59,51,0,49,58,62,61,63],
[48,60,53,49,56,46,53,51,0,54,53,54,57],
[40,46,40,47,58,47,47,42,46,0,51,44,53],
[43,45,40,41,45,48,42,38,47,49,0,49,37],
[36,49,51,51,46,49,46,39,46,56,51,0,55],
[39,53,48,44,47,48,35,37,43,47,63,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 166, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,44,47,50,45,37,48,43,43,53,39,42],
[49,0,29,41,52,44,41,56,44,46,44,44,44],
[56,71,0,56,56,41,45,64,53,53,57,49,50],
[53,59,44,0,52,43,36,63,39,49,43,42,40],
[50,48,44,48,0,43,40,56,48,47,51,45,38],
[55,56,59,57,57,0,41,56,45,42,43,41,46],
[63,59,55,64,60,59,0,64,55,64,50,51,49],
[52,44,36,37,44,44,36,0,40,43,45,34,39],
[57,56,47,61,52,55,45,60,0,53,53,51,41],
[57,54,47,51,53,58,36,57,47,0,47,45,40],
[47,56,43,57,49,57,50,55,47,53,0,48,37],
[61,56,51,58,55,59,49,66,49,55,52,0,53],
[58,56,50,60,62,54,51,61,59,60,63,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 167, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,53,52,49,55,58,50,58,42,58,60,57],
[49,0,59,53,49,58,57,52,60,46,56,59,64],
[47,41,0,55,47,59,43,47,60,44,53,52,51],
[48,47,45,0,44,50,46,46,51,39,53,52,57],
[51,51,53,56,0,62,57,51,61,41,62,61,53],
[45,42,41,50,38,0,48,36,51,40,53,50,46],
[42,43,57,54,43,52,0,42,54,37,47,47,58],
[50,48,53,54,49,64,58,0,58,51,67,67,62],
[42,40,40,49,39,49,46,42,0,33,50,47,43],
[58,54,56,61,59,60,63,49,67,0,58,59,56],
[42,44,47,47,38,47,53,33,50,42,0,56,51],
[40,41,48,48,39,50,53,33,53,41,44,0,51],
[43,36,49,43,47,54,42,38,57,44,49,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 168, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,42,37,44,45,47,48,42,49,49,42,45],
[55,0,59,54,52,57,52,59,54,49,51,45,55],
[58,41,0,42,47,54,48,52,53,45,45,42,41],
[63,46,58,0,52,54,52,63,54,51,54,53,48],
[56,48,53,48,0,56,48,62,46,49,55,49,50],
[55,43,46,46,44,0,43,50,43,49,49,47,43],
[53,48,52,48,52,57,0,52,52,52,42,46,54],
[52,41,48,37,38,50,48,0,42,49,43,40,41],
[58,46,47,46,54,57,48,58,0,55,52,47,49],
[51,51,55,49,51,51,48,51,45,0,46,49,49],
[51,49,55,46,45,51,58,57,48,54,0,47,46],
[58,55,58,47,51,53,54,60,53,51,53,0,54],
[55,45,59,52,50,57,46,59,51,51,54,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 169, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,54,53,55,47,49,58,61,51,47,39,49],
[52,0,51,52,54,50,50,67,56,47,49,45,54],
[46,49,0,50,45,42,51,69,58,54,45,45,52],
[47,48,50,0,52,53,48,59,52,45,51,37,52],
[45,46,55,48,0,47,50,58,50,55,43,41,52],
[53,50,58,47,53,0,47,58,61,50,42,39,49],
[51,50,49,52,50,53,0,65,63,52,45,42,57],
[42,33,31,41,42,42,35,0,48,41,46,33,45],
[39,44,42,48,50,39,37,52,0,45,36,31,52],
[49,53,46,55,45,50,48,59,55,0,42,41,51],
[53,51,55,49,57,58,55,54,64,58,0,51,54],
[61,55,55,63,59,61,58,67,69,59,49,0,59],
[51,46,48,48,48,51,43,55,48,49,46,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 170, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,45,40,49,47,46,55,47,50,43,41,46],
[54,0,48,53,61,52,52,53,53,52,49,47,50],
[55,52,0,52,59,52,51,60,51,56,44,43,48],
[60,47,48,0,55,56,53,60,54,58,46,48,46],
[51,39,41,45,0,52,46,52,43,47,42,42,36],
[53,48,48,44,48,0,48,53,47,49,46,47,47],
[54,48,49,47,54,52,0,52,46,55,50,53,43],
[45,47,40,40,48,47,48,0,44,49,40,33,39],
[53,47,49,46,57,53,54,56,0,59,48,46,46],
[50,48,44,42,53,51,45,51,41,0,46,40,44],
[57,51,56,54,58,54,50,60,52,54,0,43,52],
[59,53,57,52,58,53,47,67,54,60,57,0,52],
[54,50,52,54,64,53,57,61,54,56,48,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 171, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,51,58,55,61,57,46,54,54,52,55,51],
[46,0,47,50,47,55,48,43,51,48,49,46,44],
[49,53,0,53,51,59,50,51,50,45,52,52,50],
[42,50,47,0,54,55,45,44,57,54,47,44,45],
[45,53,49,46,0,57,51,52,52,50,47,52,50],
[39,45,41,45,43,0,45,39,40,40,44,46,41],
[43,52,50,55,49,55,0,45,51,54,49,48,47],
[54,57,49,56,48,61,55,0,52,54,52,53,51],
[46,49,50,43,48,60,49,48,0,46,51,47,40],
[46,52,55,46,50,60,46,46,54,0,47,48,44],
[48,51,48,53,53,56,51,48,49,53,0,51,48],
[45,54,48,56,48,54,52,47,53,52,49,0,51],
[49,56,50,55,50,59,53,49,60,56,52,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 172, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,38,38,40,50,48,43,48,53,48,45,50],
[52,0,41,41,35,49,50,41,49,64,48,43,47],
[62,59,0,47,58,52,60,49,56,59,62,49,56],
[62,59,53,0,44,55,54,52,58,67,64,56,49],
[60,65,42,56,0,58,54,55,58,59,60,58,57],
[50,51,48,45,42,0,48,49,52,52,47,47,49],
[52,50,40,46,46,52,0,45,54,60,52,46,46],
[57,59,51,48,45,51,55,0,58,58,60,54,50],
[52,51,44,42,42,48,46,42,0,54,55,52,49],
[47,36,41,33,41,48,40,42,46,0,47,38,40],
[52,52,38,36,40,53,48,40,45,53,0,42,47],
[55,57,51,44,42,53,54,46,48,62,58,0,48],
[50,53,44,51,43,51,54,50,51,60,53,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 173, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,47,52,55,45,48,48,55,51,57,51,42],
[44,0,44,45,48,43,42,41,50,46,51,42,36],
[53,56,0,48,55,50,51,54,55,56,53,50,47],
[48,55,52,0,62,44,43,53,56,53,55,49,43],
[45,52,45,38,0,44,45,45,47,44,49,42,30],
[55,57,50,56,56,0,49,50,52,60,66,53,46],
[52,58,49,57,55,51,0,51,53,48,54,48,51],
[52,59,46,47,55,50,49,0,55,52,52,46,52],
[45,50,45,44,53,48,47,45,0,51,56,48,34],
[49,54,44,47,56,40,52,48,49,0,52,48,35],
[43,49,47,45,51,34,46,48,44,48,0,41,38],
[49,58,50,51,58,47,52,54,52,52,59,0,41],
[58,64,53,57,70,54,49,48,66,65,62,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 174, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,51,47,57,48,51,52,49,48,55,47,47],
[45,0,51,54,48,37,46,52,44,47,45,44,42],
[49,49,0,51,58,48,53,46,51,49,51,48,49],
[53,46,49,0,58,42,50,53,50,52,58,52,43],
[43,52,42,42,0,43,42,51,41,41,48,44,45],
[52,63,52,58,57,0,46,59,56,60,58,57,58],
[49,54,47,50,58,54,0,50,52,52,51,54,45],
[48,48,54,47,49,41,50,0,47,43,52,43,39],
[51,56,49,50,59,44,48,53,0,47,48,56,49],
[52,53,51,48,59,40,48,57,53,0,51,48,48],
[45,55,49,42,52,42,49,48,52,49,0,47,47],
[53,56,52,48,56,43,46,57,44,52,53,0,44],
[53,58,51,57,55,42,55,61,51,52,53,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 175, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,60,49,53,59,46,54,54,57,43,47,50],
[51,0,52,55,52,55,48,54,58,57,56,46,49],
[40,48,0,52,47,53,40,46,52,58,48,42,40],
[51,45,48,0,49,59,48,48,53,55,50,48,43],
[47,48,53,51,0,49,46,48,49,51,47,39,44],
[41,45,47,41,51,0,49,55,51,52,43,44,48],
[54,52,60,52,54,51,0,50,54,56,52,51,49],
[46,46,54,52,52,45,50,0,55,56,46,49,43],
[46,42,48,47,51,49,46,45,0,54,42,49,43],
[43,43,42,45,49,48,44,44,46,0,36,39,44],
[57,44,52,50,53,57,48,54,58,64,0,55,51],
[53,54,58,52,61,56,49,51,51,61,45,0,51],
[50,51,60,57,56,52,51,57,57,56,49,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 176, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,42,53,40,39,38,32,38,52,49,50,43],
[62,0,68,61,57,49,61,58,61,57,55,54,61],
[58,32,0,47,46,47,48,35,40,47,53,34,56],
[47,39,53,0,53,48,41,38,42,39,51,51,48],
[60,43,54,47,0,42,52,39,48,50,53,42,54],
[61,51,53,52,58,0,56,43,48,51,65,53,57],
[62,39,52,59,48,44,0,42,45,51,64,49,54],
[68,42,65,62,61,57,58,0,54,56,56,57,60],
[62,39,60,58,52,52,55,46,0,57,62,41,45],
[48,43,53,61,50,49,49,44,43,0,53,48,53],
[51,45,47,49,47,35,36,44,38,47,0,42,56],
[50,46,66,49,58,47,51,43,59,52,58,0,57],
[57,39,44,52,46,43,46,40,55,47,44,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 177, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,42,46,44,30,34,29,19,28,45,20,35],
[81,0,47,62,60,60,52,46,51,52,52,52,62],
[58,53,0,55,60,41,41,26,47,44,54,35,58],
[54,38,45,0,55,29,47,34,34,41,49,34,38],
[56,40,40,45,0,36,34,28,20,35,38,33,39],
[70,40,59,71,64,0,41,38,37,40,44,38,43],
[66,48,59,53,66,59,0,55,53,54,54,44,45],
[71,54,74,66,72,62,45,0,43,40,60,56,62],
[81,49,53,66,80,63,47,57,0,56,50,60,59],
[72,48,56,59,65,60,46,60,44,0,55,51,54],
[55,48,46,51,62,56,46,40,50,45,0,40,48],
[80,48,65,66,67,62,56,44,40,49,60,0,58],
[65,38,42,62,61,57,55,38,41,46,52,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 178, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,53,42,56,55,40,42,48,43,36,41,48],
[59,0,59,58,59,52,46,41,49,49,44,40,46],
[47,41,0,44,48,43,25,37,46,40,28,38,35],
[58,42,56,0,58,62,54,58,52,47,48,54,66],
[44,41,52,42,0,44,38,40,46,41,33,43,49],
[45,48,57,38,56,0,36,35,41,46,44,46,54],
[60,54,75,46,62,64,0,40,50,53,56,58,55],
[58,59,63,42,60,65,60,0,63,64,50,40,61],
[52,51,54,48,54,59,50,37,0,43,41,47,57],
[57,51,60,53,59,54,47,36,57,0,47,45,45],
[64,56,72,52,67,56,44,50,59,53,0,60,55],
[59,60,62,46,57,54,42,60,53,55,40,0,46],
[52,54,65,34,51,46,45,39,43,55,45,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 179, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,62,58,54,49,47,49,60,55,49,43,58],
[48,0,61,59,55,49,50,53,58,53,54,43,58],
[38,39,0,53,50,45,47,52,56,51,46,36,46],
[42,41,47,0,38,43,42,39,51,49,42,33,48],
[46,45,50,62,0,54,46,55,58,60,51,47,57],
[51,51,55,57,46,0,49,47,53,47,45,40,53],
[53,50,53,58,54,51,0,54,56,54,47,43,50],
[51,47,48,61,45,53,46,0,61,53,49,43,46],
[40,42,44,49,42,47,44,39,0,43,40,35,45],
[45,47,49,51,40,53,46,47,57,0,43,38,49],
[51,46,54,58,49,55,53,51,60,57,0,50,49],
[57,57,64,67,53,60,57,57,65,62,50,0,61],
[42,42,54,52,43,47,50,54,55,51,51,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 180, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,54,41,48,49,46,50,42,36,45,49,47],
[56,0,68,57,55,52,48,60,62,50,58,59,60],
[46,32,0,44,54,45,49,41,48,42,45,48,46],
[59,43,56,0,57,54,51,53,54,47,50,50,48],
[52,45,46,43,0,54,51,45,45,37,48,55,46],
[51,48,55,46,46,0,41,55,46,47,51,49,52],
[54,52,51,49,49,59,0,52,52,48,46,59,54],
[50,40,59,47,55,45,48,0,55,49,53,55,55],
[58,38,52,46,55,54,48,45,0,38,46,49,42],
[64,50,58,53,63,53,52,51,62,0,53,65,55],
[55,42,55,50,52,49,54,47,54,47,0,58,48],
[51,41,52,50,45,51,41,45,51,35,42,0,42],
[53,40,54,52,54,48,46,45,58,45,52,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 181, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,49,49,53,51,54,55,62,48,49,51,61],
[49,0,50,48,48,53,50,52,59,57,42,53,55],
[51,50,0,52,51,55,55,53,56,58,52,51,59],
[51,52,48,0,52,54,54,47,52,59,48,48,53],
[47,52,49,48,0,53,47,47,55,51,39,44,56],
[49,47,45,46,47,0,43,45,55,55,44,44,53],
[46,50,45,46,53,57,0,51,51,50,47,46,55],
[45,48,47,53,53,55,49,0,54,55,41,50,55],
[38,41,44,48,45,45,49,46,0,45,37,42,48],
[52,43,42,41,49,45,50,45,55,0,44,42,49],
[51,58,48,52,61,56,53,59,63,56,0,52,62],
[49,47,49,52,56,56,54,50,58,58,48,0,61],
[39,45,41,47,44,47,45,45,52,51,38,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 182, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,51,54,50,57,58,49,51,45,55,53,49],
[46,0,57,59,52,58,59,50,46,47,56,52,51],
[49,43,0,47,46,50,48,42,49,42,47,42,40],
[46,41,53,0,56,60,51,46,49,49,52,46,48],
[50,48,54,44,0,52,51,44,51,47,51,47,46],
[43,42,50,40,48,0,43,43,45,44,43,41,42],
[42,41,52,49,49,57,0,41,51,41,48,46,51],
[51,50,58,54,56,57,59,0,61,46,53,53,46],
[49,54,51,51,49,55,49,39,0,43,51,48,39],
[55,53,58,51,53,56,59,54,57,0,55,50,59],
[45,44,53,48,49,57,52,47,49,45,0,42,47],
[47,48,58,54,53,59,54,47,52,50,58,0,54],
[51,49,60,52,54,58,49,54,61,41,53,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 183, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,52,59,52,55,52,59,63,39,54,57,63],
[52,0,53,58,45,49,56,60,60,51,56,56,54],
[48,47,0,41,50,45,47,52,53,42,46,44,46],
[41,42,59,0,46,45,50,48,48,48,53,54,53],
[48,55,50,54,0,44,52,59,55,40,51,49,56],
[45,51,55,55,56,0,55,53,57,46,54,55,54],
[48,44,53,50,48,45,0,53,55,39,53,60,54],
[41,40,48,52,41,47,47,0,51,33,48,47,46],
[37,40,47,52,45,43,45,49,0,33,39,46,42],
[61,49,58,52,60,54,61,67,67,0,58,60,58],
[46,44,54,47,49,46,47,52,61,42,0,47,41],
[43,44,56,46,51,45,40,53,54,40,53,0,47],
[37,46,54,47,44,46,46,54,58,42,59,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 184, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,52,43,44,57,47,58,52,35,50,49,48],
[55,0,59,49,55,65,56,55,62,60,54,49,57],
[48,41,0,48,49,50,41,49,60,41,43,45,47],
[57,51,52,0,45,52,53,52,59,51,54,54,47],
[56,45,51,55,0,46,58,57,55,38,46,42,49],
[43,35,50,48,54,0,49,44,57,40,46,29,46],
[53,44,59,47,42,51,0,46,57,40,40,47,41],
[42,45,51,48,43,56,54,0,51,46,53,48,48],
[48,38,40,41,45,43,43,49,0,39,50,37,42],
[65,40,59,49,62,60,60,54,61,0,50,40,51],
[50,46,57,46,54,54,60,47,50,50,0,42,47],
[51,51,55,46,58,71,53,52,63,60,58,0,55],
[52,43,53,53,51,54,59,52,58,49,53,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 185, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,52,49,56,54,56,68,51,44,62,48,39],
[45,0,48,36,43,47,47,65,44,44,49,41,33],
[48,52,0,41,54,55,51,57,46,53,59,49,40],
[51,64,59,0,50,54,54,69,53,49,61,57,51],
[44,57,46,50,0,52,56,54,48,50,50,59,39],
[46,53,45,46,48,0,52,66,42,42,55,47,34],
[44,53,49,46,44,48,0,58,49,45,52,50,40],
[32,35,43,31,46,34,42,0,28,28,45,34,27],
[49,56,54,47,52,58,51,72,0,45,57,52,41],
[56,56,47,51,50,58,55,72,55,0,60,52,37],
[38,51,41,39,50,45,48,55,43,40,0,42,44],
[52,59,51,43,41,53,50,66,48,48,58,0,43],
[61,67,60,49,61,66,60,73,59,63,56,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 186, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,51,46,52,44,46,48,51,52,56,49,43],
[49,0,47,50,53,45,50,50,50,51,55,50,43],
[49,53,0,48,46,48,47,51,48,56,54,47,53],
[54,50,52,0,50,50,50,48,50,56,54,57,45],
[48,47,54,50,0,53,57,49,56,51,55,57,48],
[56,55,52,50,47,0,58,53,55,59,54,57,50],
[54,50,53,50,43,42,0,48,49,57,54,51,49],
[52,50,49,52,51,47,52,0,56,53,56,54,48],
[49,50,52,50,44,45,51,44,0,50,53,53,43],
[48,49,44,44,49,41,43,47,50,0,49,49,45],
[44,45,46,46,45,46,46,44,47,51,0,45,46],
[51,50,53,43,43,43,49,46,47,51,55,0,47],
[57,57,47,55,52,50,51,52,57,55,54,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 187, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,59,45,56,52,54,47,51,45,45,54,44],
[43,0,56,50,45,49,61,50,53,33,48,53,49],
[41,44,0,33,36,43,45,39,49,38,35,47,39],
[55,50,67,0,50,58,61,49,61,56,57,63,54],
[44,55,64,50,0,52,56,53,61,59,49,53,55],
[48,51,57,42,48,0,45,51,50,40,43,45,39],
[46,39,55,39,44,55,0,46,47,45,49,42,46],
[53,50,61,51,47,49,54,0,52,48,40,47,38],
[49,47,51,39,39,50,53,48,0,34,53,55,46],
[55,67,62,44,41,60,55,52,66,0,55,57,52],
[55,52,65,43,51,57,51,60,47,45,0,54,43],
[46,47,53,37,47,55,58,53,45,43,46,0,46],
[56,51,61,46,45,61,54,62,54,48,57,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 188, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,57,61,59,44,42,53,47,39,49,43,59],
[56,0,53,62,55,45,46,53,46,40,50,49,57],
[43,47,0,59,58,41,43,41,44,35,48,41,53],
[39,38,41,0,46,29,35,45,31,26,42,45,45],
[41,45,42,54,0,47,44,46,39,31,47,44,48],
[56,55,59,71,53,0,53,58,42,48,55,49,58],
[58,54,57,65,56,47,0,58,54,43,48,53,58],
[47,47,59,55,54,42,42,0,48,43,58,47,59],
[53,54,56,69,61,58,46,52,0,51,58,52,64],
[61,60,65,74,69,52,57,57,49,0,52,52,69],
[51,50,52,58,53,45,52,42,42,48,0,51,53],
[57,51,59,55,56,51,47,53,48,48,49,0,50],
[41,43,47,55,52,42,42,41,36,31,47,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 189, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,55,42,46,50,43,45,50,50,51,48,54],
[47,0,57,51,51,48,55,52,54,55,57,56,55],
[45,43,0,47,42,49,46,36,46,49,45,40,54],
[58,49,53,0,55,56,52,56,59,57,62,51,57],
[54,49,58,45,0,51,56,45,53,47,50,45,54],
[50,52,51,44,49,0,47,39,47,50,41,55,48],
[57,45,54,48,44,53,0,49,55,48,56,45,44],
[55,48,64,44,55,61,51,0,60,58,58,59,57],
[50,46,54,41,47,53,45,40,0,45,55,46,52],
[50,45,51,43,53,50,52,42,55,0,49,44,46],
[49,43,55,38,50,59,44,42,45,51,0,46,53],
[52,44,60,49,55,45,55,41,54,56,54,0,55],
[46,45,46,43,46,52,56,43,48,54,47,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 190, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,54,54,35,45,53,60,41,48,44,35,45],
[55,0,55,55,50,56,58,51,54,46,53,45,45],
[46,45,0,48,38,40,57,48,42,54,35,40,46],
[46,45,52,0,41,43,63,55,59,52,46,37,48],
[65,50,62,59,0,57,63,59,59,55,47,49,59],
[55,44,60,57,43,0,51,47,50,53,40,53,42],
[47,42,43,37,37,49,0,39,40,39,26,39,33],
[40,49,52,45,41,53,61,0,46,49,43,37,39],
[59,46,58,41,41,50,60,54,0,50,41,50,55],
[52,54,46,48,45,47,61,51,50,0,45,45,45],
[56,47,65,54,53,60,74,57,59,55,0,54,53],
[65,55,60,63,51,47,61,63,50,55,46,0,50],
[55,55,54,52,41,58,67,61,45,55,47,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 191, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,47,48,47,51,55,43,52,42,50,46,56],
[38,0,40,36,42,50,49,44,48,39,60,49,53],
[53,60,0,51,54,52,52,46,48,45,65,56,60],
[52,64,49,0,56,56,62,42,56,43,55,51,58],
[53,58,46,44,0,45,51,40,56,43,51,51,64],
[49,50,48,44,55,0,51,38,50,41,56,42,56],
[45,51,48,38,49,49,0,33,52,33,59,46,60],
[57,56,54,58,60,62,67,0,56,55,58,48,70],
[48,52,52,44,44,50,48,44,0,49,55,54,53],
[58,61,55,57,57,59,67,45,51,0,57,60,65],
[50,40,35,45,49,44,41,42,45,43,0,37,52],
[54,51,44,49,49,58,54,52,46,40,63,0,52],
[44,47,40,42,36,44,40,30,47,35,48,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 192, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,52,39,47,42,51,42,52,28,46,42,57],
[53,0,54,53,50,46,45,31,54,45,46,34,44],
[48,46,0,52,55,31,40,42,61,42,57,42,39],
[61,47,48,0,43,53,46,35,63,41,43,36,53],
[53,50,45,57,0,40,44,50,68,45,51,42,42],
[58,54,69,47,60,0,54,48,60,54,60,40,49],
[49,55,60,54,56,46,0,45,62,46,58,57,58],
[58,69,58,65,50,52,55,0,67,57,51,46,56],
[48,46,39,37,32,40,38,33,0,37,44,31,38],
[72,55,58,59,55,46,54,43,63,0,61,53,51],
[54,54,43,57,49,40,42,49,56,39,0,37,48],
[58,66,58,64,58,60,43,54,69,47,63,0,48],
[43,56,61,47,58,51,42,44,62,49,52,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 193, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,55,45,47,47,56,54,57,51,38,42,52],
[52,0,56,46,49,46,54,56,50,56,44,45,56],
[45,44,0,40,42,46,42,53,53,45,36,41,47],
[55,54,60,0,51,52,52,57,59,50,44,41,57],
[53,51,58,49,0,53,51,53,66,58,48,52,48],
[53,54,54,48,47,0,49,48,57,49,39,52,39],
[44,46,58,48,49,51,0,62,61,56,49,47,55],
[46,44,47,43,47,52,38,0,48,58,42,43,49],
[43,50,47,41,34,43,39,52,0,46,37,38,42],
[49,44,55,50,42,51,44,42,54,0,41,41,58],
[62,56,64,56,52,61,51,58,63,59,0,40,56],
[58,55,59,59,48,48,53,57,62,59,60,0,53],
[48,44,53,43,52,61,45,51,58,42,44,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 194, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,40,38,70,60,39,56,41,54,42,48,35],
[40,0,42,41,60,57,41,61,33,69,32,48,39],
[60,58,0,31,64,48,51,47,43,43,16,43,41],
[62,59,69,0,70,60,55,66,51,72,51,48,59],
[30,40,36,30,0,34,37,47,32,40,29,21,31],
[40,43,52,40,66,0,39,47,42,46,20,28,33],
[61,59,49,45,63,61,0,51,51,56,43,45,37],
[44,39,53,34,53,53,49,0,51,43,47,45,45],
[59,67,57,49,68,58,49,49,0,56,51,28,44],
[46,31,57,28,60,54,44,57,44,0,34,47,44],
[58,68,84,49,71,80,57,53,49,66,0,56,59],
[52,52,57,52,79,72,55,55,72,53,44,0,42],
[65,61,59,41,69,67,63,55,56,56,41,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 195, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,66,61,56,32,35,20,31,53,51,53,39,61],
[34,0,57,44,30,5,39,38,32,51,43,51,37],
[39,43,0,63,29,13,36,37,42,47,55,37,72],
[44,56,37,0,23,21,19,22,27,46,29,29,45],
[68,70,71,77,0,30,49,50,47,67,49,61,67],
[65,95,87,79,70,0,50,72,90,71,73,77,96],
[80,61,64,81,51,50,0,42,64,66,64,72,79],
[69,62,63,78,50,28,58,0,66,74,43,64,68],
[47,68,58,73,53,10,36,34,0,50,38,51,59],
[49,49,53,54,33,29,34,26,50,0,40,68,60],
[47,57,45,71,51,27,36,57,62,60,0,50,79],
[61,49,63,71,39,23,28,36,49,32,50,0,70],
[39,63,28,55,33,4,21,32,41,40,21,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 196, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,44,51,43,46,49,55,40,51,51,41,52],
[50,0,51,51,49,42,49,57,45,50,54,48,50],
[56,49,0,51,57,52,52,55,48,52,60,44,59],
[49,49,49,0,46,50,54,45,41,56,60,55,58],
[57,51,43,54,0,47,47,50,44,49,53,45,45],
[54,58,48,50,53,0,51,57,54,48,46,45,49],
[51,51,48,46,53,49,0,54,52,58,65,45,59],
[45,43,45,55,50,43,46,0,39,54,51,45,50],
[60,55,52,59,56,46,48,61,0,59,51,48,50],
[49,50,48,44,51,52,42,46,41,0,62,44,46],
[49,46,40,40,47,54,35,49,49,38,0,35,52],
[59,52,56,45,55,55,55,55,52,56,65,0,50],
[48,50,41,42,55,51,41,50,50,54,48,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 197, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,52,62,54,66,50,52,58,58,50,51,48],
[41,0,39,52,46,54,48,52,56,53,50,45,45],
[48,61,0,69,59,70,58,67,56,56,63,50,57],
[38,48,31,0,41,51,52,50,49,51,64,53,46],
[46,54,41,59,0,62,46,52,54,58,58,47,49],
[34,46,30,49,38,0,40,42,49,46,42,41,45],
[50,52,42,48,54,60,0,52,59,48,52,52,49],
[48,48,33,50,48,58,48,0,49,53,55,47,48],
[42,44,44,51,46,51,41,51,0,46,55,43,42],
[42,47,44,49,42,54,52,47,54,0,59,38,46],
[50,50,37,36,42,58,48,45,45,41,0,42,42],
[49,55,50,47,53,59,48,53,57,62,58,0,45],
[52,55,43,54,51,55,51,52,58,54,58,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 198, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,48,47,46,48,48,48,40,52,48,47,44],
[51,0,48,46,57,50,57,45,51,44,50,47,49],
[52,52,0,49,55,55,53,53,49,50,50,49,47],
[53,54,51,0,49,54,57,47,54,51,49,48,44],
[54,43,45,51,0,49,47,43,50,42,47,49,48],
[52,50,45,46,51,0,52,48,46,51,50,49,51],
[52,43,47,43,53,48,0,47,45,41,53,45,52],
[52,55,47,53,57,52,53,0,55,54,51,52,46],
[60,49,51,46,50,54,55,45,0,43,47,46,46],
[48,56,50,49,58,49,59,46,57,0,57,45,52],
[52,50,50,51,53,50,47,49,53,43,0,45,44],
[53,53,51,52,51,51,55,48,54,55,55,0,46],
[56,51,53,56,52,49,48,54,54,48,56,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 199, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,11,46,15,38,37,33,41,40,39,16,45],
[77,0,68,57,57,50,69,52,61,60,54,39,85],
[89,32,0,54,40,43,46,36,54,52,62,50,82],
[54,43,46,0,8,46,46,26,34,60,47,24,46],
[85,43,60,92,0,51,57,67,50,60,66,50,51],
[62,50,57,54,49,0,65,63,58,71,67,43,88],
[63,31,54,54,43,35,0,52,69,53,40,33,73],
[67,48,64,74,33,37,48,0,38,63,53,37,49],
[59,39,46,66,50,42,31,62,0,57,51,44,51],
[60,40,48,40,40,29,47,37,43,0,52,44,56],
[61,46,38,53,34,33,60,47,49,48,0,39,54],
[84,61,50,76,50,57,67,63,56,56,61,0,69],
[55,15,18,54,49,12,27,51,49,44,46,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 100, 200, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebb/mebb_13_100.csv", index=False, header=False)