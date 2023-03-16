
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,25,79,54,26,25,54,50,73,26,50,54],
[76,0,79,76,76,51,54,48,101,29,51,54],
[22,22,0,22,23,0,76,47,23,0,72,54],
[47,25,79,0,48,25,54,47,48,0,50,54],
[75,25,78,53,0,25,54,50,73,53,50,54],
[76,50,101,76,76,0,76,47,101,29,72,54],
[47,47,25,47,47,25,0,47,47,0,50,53],
[51,53,54,54,51,54,54,0,76,54,53,29],
[28,0,78,53,28,0,54,25,0,28,50,54],
[75,72,101,101,48,72,101,47,73,0,72,54],
[51,50,29,51,51,29,51,48,51,29,0,29],
[47,47,47,47,47,47,48,72,47,47,72,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 1, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,68,41,57,40,62,71,58,69,40,19],
[61,0,45,38,75,58,55,59,68,63,35,65],
[33,56,0,61,59,60,50,73,60,82,60,39],
[60,63,40,0,63,57,63,66,78,64,45,64],
[44,26,42,38,0,31,50,55,34,58,29,21],
[61,43,41,44,70,0,31,54,53,46,42,43],
[39,46,51,38,51,70,0,55,63,58,51,32],
[30,42,28,35,46,47,46,0,56,46,24,33],
[43,33,41,23,67,48,38,45,0,48,16,45],
[32,38,19,37,43,55,43,55,53,0,55,34],
[61,66,41,56,72,59,50,77,85,46,0,63],
[82,36,62,37,80,58,69,68,56,67,38,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 2, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,51,51,61,54,49,47,42,50,49,50],
[54,0,52,49,48,43,48,43,43,46,51,42],
[50,49,0,50,54,49,58,51,43,50,44,51],
[50,52,51,0,57,48,67,54,52,53,45,54],
[40,53,47,44,0,47,45,48,41,43,54,51],
[47,58,52,53,54,0,46,50,46,45,56,45],
[52,53,43,34,56,55,0,42,47,54,49,46],
[54,58,50,47,53,51,59,0,45,47,52,52],
[59,58,58,49,60,55,54,56,0,45,55,45],
[51,55,51,48,58,56,47,54,56,0,54,45],
[52,50,57,56,47,45,52,49,46,47,0,48],
[51,59,50,47,50,56,55,49,56,56,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 3, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,53,49,53,58,50,57,49,51,53,56],
[42,0,43,49,39,45,52,49,38,51,43,49],
[48,58,0,46,46,48,53,48,43,53,45,60],
[52,52,55,0,48,59,57,46,51,57,50,64],
[48,62,55,53,0,52,61,58,55,54,56,65],
[43,56,53,42,49,0,52,45,49,49,52,59],
[51,49,48,44,40,49,0,47,43,52,45,51],
[44,52,53,55,43,56,54,0,51,49,48,55],
[52,63,58,50,46,52,58,50,0,56,51,56],
[50,50,48,44,47,52,49,52,45,0,46,47],
[48,58,56,51,45,49,56,53,50,55,0,57],
[45,52,41,37,36,42,50,46,45,54,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 4, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,63,59,46,55,49,61,55,50,58,56,49],
[38,0,54,49,49,48,51,59,47,51,49,49],
[42,47,0,49,45,41,48,51,44,48,47,43],
[55,52,52,0,54,57,57,59,48,51,50,51],
[46,52,56,47,0,49,56,57,45,53,55,58],
[52,53,60,44,52,0,59,52,57,49,48,56],
[40,50,53,44,45,42,0,49,45,45,47,52],
[46,42,50,42,44,49,52,0,37,49,46,44],
[51,54,57,53,56,44,56,64,0,53,57,54],
[43,50,53,50,48,52,56,52,48,0,49,54],
[45,52,54,51,46,53,54,55,44,52,0,51],
[52,52,58,50,43,45,49,57,47,47,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 5, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,50,54,54,60,52,61,52,59,54,56],
[45,0,42,41,44,46,47,41,46,47,51,47],
[51,59,0,48,51,48,55,58,52,54,49,57],
[47,60,53,0,47,65,53,59,53,51,53,49],
[47,57,50,54,0,62,51,53,50,58,44,53],
[41,55,53,36,39,0,46,44,36,54,41,47],
[49,54,46,48,50,55,0,51,49,47,42,41],
[40,60,43,42,48,57,50,0,49,62,52,47],
[49,55,49,48,51,65,52,52,0,62,63,58],
[42,54,47,50,43,47,54,39,39,0,41,50],
[47,50,52,48,57,60,59,49,38,60,0,50],
[45,54,44,52,48,54,60,54,43,51,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 6, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,63,64,60,63,67,50,53,55,73,66,55],
[38,0,52,43,49,32,45,44,46,42,56,31],
[37,49,0,60,52,51,50,54,52,59,47,48],
[41,58,41,0,56,47,46,49,52,64,66,49],
[38,52,49,45,0,35,51,47,51,50,61,41],
[34,69,50,54,66,0,58,51,60,65,57,49],
[51,56,51,55,50,43,0,57,51,62,68,54],
[48,57,47,52,54,50,44,0,49,65,54,47],
[46,55,49,49,50,41,50,52,0,61,67,48],
[28,59,42,37,51,36,39,36,40,0,48,24],
[35,45,54,35,40,44,33,47,34,53,0,39],
[46,70,53,52,60,52,47,54,53,77,62,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 7, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,50,43,41,42,48,64,52,48,42,35],
[40,0,47,42,40,36,48,45,45,51,36,39],
[51,54,0,51,56,35,46,54,54,48,51,42],
[58,59,50,0,48,46,58,63,58,54,51,52],
[60,61,45,53,0,42,52,60,54,49,56,50],
[59,65,66,55,59,0,62,70,56,55,52,44],
[53,53,55,43,49,39,0,54,51,42,43,38],
[37,56,47,38,41,31,47,0,50,43,41,35],
[49,56,47,43,47,45,50,51,0,52,56,50],
[53,50,53,47,52,46,59,58,49,0,42,44],
[59,65,50,50,45,49,58,60,45,59,0,57],
[66,62,59,49,51,57,63,66,51,57,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 8, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,36,62,55,46,59,48,62,41,55,41],
[52,0,46,59,61,50,54,41,47,50,57,45],
[65,55,0,57,59,46,66,53,55,41,54,46],
[39,42,44,0,50,41,47,38,42,37,42,35],
[46,40,42,51,0,44,50,35,55,36,55,45],
[55,51,55,60,57,0,59,58,57,64,49,52],
[42,47,35,54,51,42,0,52,49,42,59,34],
[53,60,48,63,66,43,49,0,55,64,60,61],
[39,54,46,59,46,44,52,46,0,51,57,50],
[60,51,60,64,65,37,59,37,50,0,59,62],
[46,44,47,59,46,52,42,41,44,42,0,44],
[60,56,55,66,56,49,67,40,51,39,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 9, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,51,44,47,49,48,56,46,53,52,37],
[44,0,46,41,48,43,51,50,54,44,48,43],
[50,55,0,50,46,58,49,54,54,56,55,51],
[57,60,51,0,52,58,57,50,53,51,59,47],
[54,53,55,49,0,52,55,64,55,57,57,52],
[52,58,43,43,49,0,55,54,50,47,54,47],
[53,50,52,44,46,46,0,51,51,53,53,48],
[45,51,47,51,37,47,50,0,48,55,53,45],
[55,47,47,48,46,51,50,53,0,51,54,44],
[48,57,45,50,44,54,48,46,50,0,52,46],
[49,53,46,42,44,47,48,48,47,49,0,45],
[64,58,50,54,49,54,53,56,57,55,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 10, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,61,34,45,54,42,55,44,62,64,65],
[56,0,59,51,48,63,51,61,58,54,57,56],
[40,42,0,45,45,60,47,53,41,47,50,51],
[67,50,56,0,52,53,45,64,57,54,55,54],
[56,53,56,49,0,63,56,60,56,60,60,69],
[47,38,41,48,38,0,47,45,42,48,45,48],
[59,50,54,56,45,54,0,64,45,68,57,48],
[46,40,48,37,41,56,37,0,48,53,44,49],
[57,43,60,44,45,59,56,53,0,59,63,59],
[39,47,54,47,41,53,33,48,42,0,44,54],
[37,44,51,46,41,56,44,57,38,57,0,56],
[36,45,50,47,32,53,53,52,42,47,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 11, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,53,51,52,42,54,41,37,64,41,50],
[48,0,52,41,38,56,62,44,41,49,45,50],
[48,49,0,44,55,48,57,45,37,52,50,42],
[50,60,57,0,62,55,52,47,47,62,53,49],
[49,63,46,39,0,37,52,33,27,55,41,34],
[59,45,53,46,64,0,52,43,46,65,41,48],
[47,39,44,49,49,49,0,38,38,61,48,48],
[60,57,56,54,68,58,63,0,42,64,45,61],
[64,60,64,54,74,55,63,59,0,74,50,62],
[37,52,49,39,46,36,40,37,27,0,41,25],
[60,56,51,48,60,60,53,56,51,60,0,59],
[51,51,59,52,67,53,53,40,39,76,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 12, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,53,47,45,46,52,45,42,46,47,41],
[59,0,56,45,53,49,50,46,50,53,46,47],
[48,45,0,43,46,50,49,45,51,49,45,45],
[54,56,58,0,46,50,58,43,55,59,49,51],
[56,48,55,55,0,44,45,51,56,51,45,43],
[55,52,51,51,57,0,48,54,54,55,49,45],
[49,51,52,43,56,53,0,47,58,50,47,43],
[56,55,56,58,50,47,54,0,63,58,53,54],
[59,51,50,46,45,47,43,38,0,49,48,42],
[55,48,52,42,50,46,51,43,52,0,51,42],
[54,55,56,52,56,52,54,48,53,50,0,50],
[60,54,56,50,58,56,58,47,59,59,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 13, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,66,49,36,55,43,34,38,50,51,54,46],
[35,0,46,36,48,35,46,37,43,43,49,30],
[52,55,0,35,53,43,46,42,41,52,49,47],
[65,65,66,0,63,66,59,48,69,59,64,57],
[46,53,48,38,0,38,34,33,51,52,41,45],
[58,66,58,35,63,0,45,48,58,51,52,52],
[67,55,55,42,67,56,0,50,54,47,53,45],
[63,64,59,53,68,53,51,0,47,65,61,49],
[51,58,60,32,50,43,47,54,0,49,51,45],
[50,58,49,42,49,50,54,36,52,0,54,50],
[47,52,52,37,60,49,48,40,50,47,0,38],
[55,71,54,44,56,49,56,52,56,51,63,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 14, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,68,15,45,40,61,73,61,58,40,38],
[73,0,58,48,45,25,61,73,58,45,58,25],
[33,43,0,15,15,25,61,43,33,30,25,23],
[86,53,86,0,68,68,46,71,86,43,86,53],
[56,56,86,33,0,25,61,71,71,61,43,56],
[61,76,76,33,76,0,61,61,61,76,73,41],
[40,40,40,55,40,40,0,40,58,30,55,25],
[28,28,58,30,30,40,61,0,76,43,40,38],
[40,43,68,15,30,40,43,25,0,30,40,38],
[43,56,71,58,40,25,71,58,71,0,58,56],
[61,43,76,15,58,28,46,61,61,43,0,28],
[63,76,78,48,45,60,76,63,63,45,73,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 15, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,56,51,49,53,49,46,40,52,46,45],
[53,0,62,54,51,55,50,53,47,55,56,47],
[45,39,0,42,52,45,43,48,38,51,45,39],
[50,47,59,0,55,56,54,50,46,58,48,46],
[52,50,49,46,0,50,44,43,51,49,50,50],
[48,46,56,45,51,0,50,35,41,47,55,44],
[52,51,58,47,57,51,0,43,47,56,55,51],
[55,48,53,51,58,66,58,0,50,59,56,50],
[61,54,63,55,50,60,54,51,0,60,53,51],
[49,46,50,43,52,54,45,42,41,0,49,42],
[55,45,56,53,51,46,46,45,48,52,0,39],
[56,54,62,55,51,57,50,51,50,59,62,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 16, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,46,48,49,35,52,48,37,48,46,44],
[48,0,45,52,62,43,46,60,38,45,46,40],
[55,56,0,65,58,52,56,63,50,52,49,44],
[53,49,36,0,49,42,43,49,33,34,45,39],
[52,39,43,52,0,38,41,52,36,47,43,45],
[66,58,49,59,63,0,61,61,55,49,57,53],
[49,55,45,58,60,40,0,54,40,49,49,44],
[53,41,38,52,49,40,47,0,42,48,48,46],
[64,63,51,68,65,46,61,59,0,59,53,58],
[53,56,49,67,54,52,52,53,42,0,56,52],
[55,55,52,56,58,44,52,53,48,45,0,48],
[57,61,57,62,56,48,57,55,43,49,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 17, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,51,53,53,44,48,37,51,46,47,47],
[41,0,42,55,46,38,48,35,43,38,52,35],
[50,59,0,58,53,47,49,39,51,41,46,42],
[48,46,43,0,50,42,47,39,44,39,47,42],
[48,55,48,51,0,42,42,30,39,35,46,46],
[57,63,54,59,59,0,61,40,47,41,46,46],
[53,53,52,54,59,40,0,45,59,38,46,42],
[64,66,62,62,71,61,56,0,59,44,59,53],
[50,58,50,57,62,54,42,42,0,37,62,44],
[55,63,60,62,66,60,63,57,64,0,64,50],
[54,49,55,54,55,55,55,42,39,37,0,50],
[54,66,59,59,55,55,59,48,57,51,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 18, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,44,46,42,48,37,56,43,52,50,50],
[46,0,45,45,55,58,50,61,47,49,54,53],
[57,56,0,59,49,52,57,56,53,67,54,53],
[55,56,42,0,55,51,52,53,47,54,54,51],
[59,46,52,46,0,49,58,52,49,50,50,51],
[53,43,49,50,52,0,49,51,54,48,45,52],
[64,51,44,49,43,52,0,56,39,48,51,53],
[45,40,45,48,49,50,45,0,38,53,51,43],
[58,54,48,54,52,47,62,63,0,55,57,49],
[49,52,34,47,51,53,53,48,46,0,48,48],
[51,47,47,47,51,56,50,50,44,53,0,46],
[51,48,48,50,50,49,48,58,52,53,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 19, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,42,54,55,40,51,55,48,64,48,52],
[45,0,36,53,49,51,42,40,44,53,41,45],
[59,65,0,58,60,50,53,57,54,47,52,58],
[47,48,43,0,44,40,34,41,41,49,36,45],
[46,52,41,57,0,51,39,56,53,40,42,40],
[61,50,51,61,50,0,53,50,52,57,53,56],
[50,59,48,67,62,48,0,54,49,49,46,48],
[46,61,44,60,45,51,47,0,50,47,41,51],
[53,57,47,60,48,49,52,51,0,52,37,54],
[37,48,54,52,61,44,52,54,49,0,42,52],
[53,60,49,65,59,48,55,60,64,59,0,52],
[49,56,43,56,61,45,53,50,47,49,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 20, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,49,39,34,32,36,33,42,34,30,53],
[66,0,60,46,64,43,59,58,68,49,54,60],
[52,41,0,36,53,35,37,48,48,37,31,38],
[62,55,65,0,53,49,48,56,62,53,48,59],
[67,37,48,48,0,34,35,44,56,42,40,51],
[69,58,66,52,67,0,45,63,63,62,64,58],
[65,42,64,53,66,56,0,45,53,49,53,59],
[68,43,53,45,57,38,56,0,58,51,50,53],
[59,33,53,39,45,38,48,43,0,43,36,57],
[67,52,64,48,59,39,52,50,58,0,50,58],
[71,47,70,53,61,37,48,51,65,51,0,65],
[48,41,63,42,50,43,42,48,44,43,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 21, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,57,55,38,49,45,54,54,46,49,43],
[58,0,49,52,48,59,48,69,58,60,56,43],
[44,52,0,49,57,53,44,63,49,45,52,44],
[46,49,52,0,53,47,42,59,51,69,57,50],
[63,53,44,48,0,57,42,66,49,63,58,52],
[52,42,48,54,44,0,38,51,40,48,63,38],
[56,53,57,59,59,63,0,71,65,61,69,50],
[47,32,38,42,35,50,30,0,25,46,40,33],
[47,43,52,50,52,61,36,76,0,45,61,50],
[55,41,56,32,38,53,40,55,56,0,57,31],
[52,45,49,44,43,38,32,61,40,44,0,37],
[58,58,57,51,49,63,51,68,51,70,64,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 22, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,52,64,49,59,52,48,61,64,55,49],
[43,0,45,46,42,51,38,38,46,49,44,38],
[49,56,0,58,40,54,48,45,66,55,42,47],
[37,55,43,0,31,52,44,45,45,44,52,45],
[52,59,61,70,0,63,48,61,63,57,60,59],
[42,50,47,49,38,0,43,46,59,47,41,41],
[49,63,53,57,53,58,0,51,51,52,51,51],
[53,63,56,56,40,55,50,0,58,55,52,58],
[40,55,35,56,38,42,50,43,0,51,48,44],
[37,52,46,57,44,54,49,46,50,0,48,50],
[46,57,59,49,41,60,50,49,53,53,0,56],
[52,63,54,56,42,60,50,43,57,51,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 23, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,47,39,49,66,64,39,53,50,48,43],
[57,0,42,51,60,77,64,56,62,57,46,47],
[54,59,0,52,46,58,77,73,61,58,75,61],
[62,50,49,0,58,76,82,60,73,78,68,56],
[52,41,55,43,0,64,66,48,50,54,51,53],
[35,24,43,25,37,0,71,51,49,34,46,35],
[37,37,24,19,35,30,0,44,44,41,56,46],
[62,45,28,41,53,50,57,0,40,57,39,47],
[48,39,40,28,51,52,57,61,0,39,45,49],
[51,44,43,23,47,67,60,44,62,0,66,57],
[53,55,26,33,50,55,45,62,56,35,0,53],
[58,54,40,45,48,66,55,54,52,44,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 24, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,32,32,32,32,0,41,32,0,32,0],
[101,0,32,60,60,32,60,41,60,32,60,28],
[69,69,0,69,101,41,69,41,69,41,69,69],
[69,41,32,0,101,73,41,41,28,41,0,28],
[69,41,0,0,0,0,0,41,28,0,0,0],
[69,69,60,28,101,0,28,41,28,0,28,28],
[101,41,32,60,101,73,0,41,60,73,60,28],
[60,60,60,60,60,60,60,0,60,32,60,28],
[69,41,32,73,73,73,41,41,0,41,41,41],
[101,69,60,60,101,101,28,69,60,0,60,28],
[69,41,32,101,101,73,41,41,60,41,0,69],
[101,73,32,73,101,73,73,73,60,73,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 25, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,57,53,58,56,58,55,51,49,55,75],
[54,0,50,47,63,57,68,56,53,60,53,60],
[44,51,0,51,57,45,61,51,48,54,47,66],
[48,54,50,0,54,55,57,57,49,53,62,67],
[43,38,44,47,0,49,57,43,45,55,55,66],
[45,44,56,46,52,0,58,49,40,56,52,64],
[43,33,40,44,44,43,0,43,36,43,38,61],
[46,45,50,44,58,52,58,0,48,43,54,65],
[50,48,53,52,56,61,65,53,0,46,61,55],
[52,41,47,48,46,45,58,58,55,0,55,60],
[46,48,54,39,46,49,63,47,40,46,0,60],
[26,41,35,34,35,37,40,36,46,41,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 26, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,47,48,47,45,56,50,55,48,51,49],
[50,0,55,45,46,45,57,49,60,45,53,52],
[54,46,0,55,54,50,63,56,61,48,53,51],
[53,56,46,0,45,48,53,52,56,49,46,49],
[54,55,47,56,0,58,63,60,57,51,52,48],
[56,56,51,53,43,0,53,62,62,52,53,51],
[45,44,38,48,38,48,0,47,50,45,42,43],
[51,52,45,49,41,39,54,0,51,46,44,47],
[46,41,40,45,44,39,51,50,0,43,43,45],
[53,56,53,52,50,49,56,55,58,0,59,50],
[50,48,48,55,49,48,59,57,58,42,0,49],
[52,49,50,52,53,50,58,54,56,51,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 27, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,53,60,51,51,49,52,57,48,53,56],
[50,0,55,55,59,54,54,57,62,52,56,60],
[48,46,0,54,47,46,51,50,55,48,53,57],
[41,46,47,0,42,47,42,48,56,37,45,41],
[50,42,54,59,0,44,48,53,54,45,53,53],
[50,47,55,54,57,0,51,55,60,45,52,52],
[52,47,50,59,53,50,0,57,57,46,54,55],
[49,44,51,53,48,46,44,0,56,47,50,48],
[44,39,46,45,47,41,44,45,0,39,39,45],
[53,49,53,64,56,56,55,54,62,0,54,60],
[48,45,48,56,48,49,47,51,62,47,0,48],
[45,41,44,60,48,49,46,53,56,41,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 28, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,57,52,56,57,55,46,52,53,53,43],
[51,0,58,44,53,52,53,51,60,45,54,40],
[44,43,0,48,52,46,43,46,47,39,55,37],
[49,57,53,0,61,64,57,50,63,56,57,53],
[45,48,49,40,0,43,43,43,54,45,47,28],
[44,49,55,37,58,0,54,44,54,45,48,45],
[46,48,58,44,58,47,0,48,56,51,49,43],
[55,50,55,51,58,57,53,0,56,48,62,47],
[49,41,54,38,47,47,45,45,0,39,50,40],
[48,56,62,45,56,56,50,53,62,0,53,43],
[48,47,46,44,54,53,52,39,51,48,0,41],
[58,61,64,48,73,56,58,54,61,58,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 29, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,64,65,43,74,43,35,58,49,35,50,43],
[37,0,38,72,38,38,20,52,44,38,38,66],
[36,63,0,79,73,48,41,55,79,47,72,79],
[58,29,22,0,54,29,28,36,36,22,54,58],
[27,63,28,47,0,63,34,42,70,41,21,64],
[58,63,53,72,38,0,35,49,67,42,39,89],
[66,81,60,73,67,66,0,60,87,65,45,73],
[43,49,46,65,59,52,41,0,65,35,31,59],
[52,57,22,65,31,34,14,36,0,35,39,43],
[66,63,54,79,60,59,36,66,66,0,60,87],
[51,63,29,47,80,62,56,70,62,41,0,64],
[58,35,22,43,37,12,28,42,58,14,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 30, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,49,40,46,39,31,49,34,44,36,47],
[58,0,38,49,50,45,46,53,51,50,37,55],
[52,63,0,43,69,44,48,54,56,45,35,68],
[61,52,58,0,69,38,49,59,51,50,48,44],
[55,51,32,32,0,36,34,43,41,47,31,48],
[62,56,57,63,65,0,50,70,59,56,57,60],
[70,55,53,52,67,51,0,64,53,63,50,55],
[52,48,47,42,58,31,37,0,39,46,40,50],
[67,50,45,50,60,42,48,62,0,57,39,56],
[57,51,56,51,54,45,38,55,44,0,36,53],
[65,64,66,53,70,44,51,61,62,65,0,59],
[54,46,33,57,53,41,46,51,45,48,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 31, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,37,48,52,58,63,48,66,63,32,50],
[59,0,55,41,56,62,67,71,71,101,35,68],
[64,46,0,32,42,42,42,80,56,75,27,44],
[53,60,69,0,28,51,50,77,45,64,31,46],
[49,45,59,73,0,68,84,73,88,88,78,48],
[43,39,59,50,33,0,53,53,36,67,29,44],
[38,34,59,51,17,48,0,40,44,64,16,15],
[53,30,21,24,28,48,61,0,32,63,16,31],
[35,30,45,56,13,65,57,69,0,66,33,29],
[38,0,26,37,13,34,37,38,35,0,35,28],
[69,66,74,70,23,72,85,85,68,66,0,60],
[51,33,57,55,53,57,86,70,72,73,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 32, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,48,52,66,51,34,41,41,37,46,26],
[62,0,48,61,51,65,52,57,53,46,61,45],
[53,53,0,49,57,72,39,35,50,59,51,35],
[49,40,52,0,35,36,39,33,48,45,49,43],
[35,50,44,66,0,60,43,54,49,45,49,38],
[50,36,29,65,41,0,29,48,33,62,37,31],
[67,49,62,62,58,72,0,66,54,69,55,67],
[60,44,66,68,47,53,35,0,62,55,56,63],
[60,48,51,53,52,68,47,39,0,56,47,48],
[64,55,42,56,56,39,32,46,45,0,49,49],
[55,40,50,52,52,64,46,45,54,52,0,48],
[75,56,66,58,63,70,34,38,53,52,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 33, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,50,59,58,43,58,50,44,59,37,68],
[73,0,56,47,64,46,47,56,40,60,51,56],
[51,45,0,49,39,34,80,32,51,61,36,40],
[42,54,52,0,64,36,65,41,18,51,53,43],
[43,37,62,37,0,28,57,42,29,38,37,36],
[58,55,67,65,73,0,68,52,43,67,41,68],
[43,54,21,36,44,33,0,52,46,20,27,54],
[51,45,69,60,59,49,49,0,71,53,37,60],
[57,61,50,83,72,58,55,30,0,35,51,63],
[42,41,40,50,63,34,81,48,66,0,27,49],
[64,50,65,48,64,60,74,64,50,74,0,65],
[33,45,61,58,65,33,47,41,38,52,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 34, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,44,51,60,50,55,53,53,40,46,51],
[54,0,43,50,56,57,57,56,60,48,47,52],
[57,58,0,57,59,53,57,62,59,56,48,56],
[50,51,44,0,56,60,54,53,52,46,49,50],
[41,45,42,45,0,54,48,46,49,46,48,41],
[51,44,48,41,47,0,49,45,49,40,41,48],
[46,44,44,47,53,52,0,47,45,37,42,43],
[48,45,39,48,55,56,54,0,55,44,44,49],
[48,41,42,49,52,52,56,46,0,43,44,50],
[61,53,45,55,55,61,64,57,58,0,55,50],
[55,54,53,52,53,60,59,57,57,46,0,60],
[50,49,45,51,60,53,58,52,51,51,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 35, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,39,62,62,56,52,65,59,63,76,54],
[42,0,68,73,75,57,69,54,63,53,64,60],
[62,33,0,59,52,38,54,44,45,44,62,50],
[39,28,42,0,49,42,56,45,30,63,55,42],
[39,26,49,52,0,49,36,47,49,56,62,49],
[45,44,63,59,52,0,42,62,61,56,59,49],
[49,32,47,45,65,59,0,59,52,66,64,34],
[36,47,57,56,54,39,42,0,46,44,56,45],
[42,38,56,71,52,40,49,55,0,51,76,44],
[38,48,57,38,45,45,35,57,50,0,55,30],
[25,37,39,46,39,42,37,45,25,46,0,35],
[47,41,51,59,52,52,67,56,57,71,66,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 36, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,51,51,44,40,38,45,43,40,44,47],
[65,0,60,58,51,50,52,53,55,54,56,54],
[50,41,0,52,44,47,45,44,49,35,44,44],
[50,43,49,0,42,46,56,43,39,45,39,56],
[57,50,57,59,0,52,49,49,47,48,51,54],
[61,51,54,55,49,0,50,52,54,52,47,59],
[63,49,56,45,52,51,0,48,50,40,49,57],
[56,48,57,58,52,49,53,0,49,52,56,52],
[58,46,52,62,54,47,51,52,0,50,54,55],
[61,47,66,56,53,49,61,49,51,0,51,54],
[57,45,57,62,50,54,52,45,47,50,0,58],
[54,47,57,45,47,42,44,49,46,47,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 37, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,45,54,58,57,52,52,57,51,57,60],
[44,0,47,56,53,46,52,46,50,47,48,49],
[56,54,0,61,63,54,52,50,58,55,58,52],
[47,45,40,0,49,42,49,51,51,44,47,53],
[43,48,38,52,0,47,46,46,40,42,46,47],
[44,55,47,59,54,0,57,46,54,51,42,56],
[49,49,49,52,55,44,0,49,42,46,48,54],
[49,55,51,50,55,55,52,0,52,50,60,55],
[44,51,43,50,61,47,59,49,0,49,57,59],
[50,54,46,57,59,50,55,51,52,0,58,59],
[44,53,43,54,55,59,53,41,44,43,0,51],
[41,52,49,48,54,45,47,46,42,42,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 38, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,50,44,43,49,50,43,51,49,56,57],
[53,0,55,49,34,56,41,55,53,56,61,73],
[51,46,0,41,38,55,35,44,58,53,68,52],
[57,52,60,0,45,59,56,54,65,61,69,66],
[58,67,63,56,0,69,50,61,68,65,60,61],
[52,45,46,42,32,0,41,44,56,62,49,52],
[51,60,66,45,51,60,0,63,62,54,69,67],
[58,46,57,47,40,57,38,0,59,57,50,60],
[50,48,43,36,33,45,39,42,0,47,45,53],
[52,45,48,40,36,39,47,44,54,0,54,58],
[45,40,33,32,41,52,32,51,56,47,0,49],
[44,28,49,35,40,49,34,41,48,43,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 39, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,45,43,39,43,49,49,46,50,40,40],
[56,0,51,48,51,52,54,48,59,53,53,47],
[56,50,0,52,51,50,54,56,52,58,46,49],
[58,53,49,0,48,48,47,56,51,59,44,50],
[62,50,50,53,0,52,54,58,59,57,52,50],
[58,49,51,53,49,0,56,53,56,58,49,55],
[52,47,47,54,47,45,0,52,50,50,47,46],
[52,53,45,45,43,48,49,0,49,53,45,43],
[55,42,49,50,42,45,51,52,0,54,47,42],
[51,48,43,42,44,43,51,48,47,0,43,42],
[61,48,55,57,49,52,54,56,54,58,0,48],
[61,54,52,51,51,46,55,58,59,59,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 40, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,53,47,32,37,39,54,39,51,44,38],
[60,0,44,53,49,46,61,61,51,53,50,53],
[48,57,0,35,30,31,47,46,28,42,42,35],
[54,48,66,0,46,38,39,52,36,58,53,51],
[69,52,71,55,0,43,69,60,46,72,57,61],
[64,55,70,63,58,0,61,60,47,67,55,71],
[62,40,54,62,32,40,0,50,30,50,41,48],
[47,40,55,49,41,41,51,0,41,50,43,45],
[62,50,73,65,55,54,71,60,0,65,55,57],
[50,48,59,43,29,34,51,51,36,0,50,42],
[57,51,59,48,44,46,60,58,46,51,0,51],
[63,48,66,50,40,30,53,56,44,59,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 41, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,43,60,43,70,33,70,16,43,14,60],
[68,0,56,68,66,78,39,72,55,56,65,60],
[58,45,0,68,45,68,58,72,45,58,43,33],
[41,33,33,0,62,83,39,72,18,39,14,50],
[58,35,56,39,0,95,46,89,45,68,53,60],
[31,23,33,18,6,0,35,62,18,6,16,21],
[68,62,43,62,55,66,0,82,45,72,70,43],
[31,29,29,29,12,39,19,0,31,29,33,16],
[85,46,56,83,56,83,56,70,0,66,31,60],
[58,45,43,62,33,95,29,72,35,0,43,60],
[87,36,58,87,48,85,31,68,70,58,0,56],
[41,41,68,51,41,80,58,85,41,41,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 42, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,49,31,43,41,36,37,45,63,47,40],
[50,0,29,33,25,47,15,28,32,44,39,24],
[52,72,0,57,57,67,62,50,65,55,63,64],
[70,68,44,0,45,53,40,64,61,72,72,30],
[58,76,44,56,0,76,61,53,48,80,75,70],
[60,54,34,48,25,0,18,33,44,52,69,11],
[65,86,39,61,40,83,0,51,62,69,70,46],
[64,73,51,37,48,68,50,0,41,74,65,32],
[56,69,36,40,53,57,39,60,0,73,63,39],
[38,57,46,29,21,49,32,27,28,0,37,23],
[54,62,38,29,26,32,31,36,38,64,0,22],
[61,77,37,71,31,90,55,69,62,78,79,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 43, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,41,44,46,47,49,55,53,48,56,52],
[57,0,53,54,57,57,57,69,57,50,64,63],
[60,48,0,52,50,57,53,55,59,52,58,60],
[57,47,49,0,44,58,44,55,49,56,61,55],
[55,44,51,57,0,57,48,58,56,55,64,62],
[54,44,44,43,44,0,47,54,51,51,57,54],
[52,44,48,57,53,54,0,60,52,56,61,62],
[46,32,46,46,43,47,41,0,51,48,49,49],
[48,44,42,52,45,50,49,50,0,45,59,55],
[53,51,49,45,46,50,45,53,56,0,56,56],
[45,37,43,40,37,44,40,52,42,45,0,51],
[49,38,41,46,39,47,39,52,46,45,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 44, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,52,51,40,37,57,41,40,42,50,45],
[50,0,44,46,39,43,50,30,40,48,43,54],
[49,57,0,55,47,48,52,49,58,56,59,59],
[50,55,46,0,45,46,58,43,48,48,54,54],
[61,62,54,56,0,53,65,42,55,53,56,69],
[64,58,53,55,48,0,56,58,46,58,65,58],
[44,51,49,43,36,45,0,48,47,51,48,48],
[60,71,52,58,59,43,53,0,59,61,61,62],
[61,61,43,53,46,55,54,42,0,63,48,69],
[59,53,45,53,48,43,50,40,38,0,47,59],
[51,58,42,47,45,36,53,40,53,54,0,54],
[56,47,42,47,32,43,53,39,32,42,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 45, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,51,45,41,41,48,55,39,51,49,45],
[49,0,53,49,41,37,43,46,42,51,43,52],
[50,48,0,52,51,41,45,52,44,50,50,51],
[56,52,49,0,42,49,45,49,49,51,52,58],
[60,60,50,59,0,51,54,54,57,54,54,57],
[60,64,60,52,50,0,54,58,52,56,55,57],
[53,58,56,56,47,47,0,53,49,48,52,58],
[46,55,49,52,47,43,48,0,40,55,48,53],
[62,59,57,52,44,49,52,61,0,55,50,62],
[50,50,51,50,47,45,53,46,46,0,53,55],
[52,58,51,49,47,46,49,53,51,48,0,57],
[56,49,50,43,44,44,43,48,39,46,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 46, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,42,52,53,53,38,57,50,46,40,57],
[56,0,44,53,54,52,42,51,50,45,51,56],
[59,57,0,58,54,57,53,59,56,49,53,62],
[49,48,43,0,49,46,46,53,45,46,42,54],
[48,47,47,52,0,46,42,62,54,51,42,60],
[48,49,44,55,55,0,44,57,49,48,44,55],
[63,59,48,55,59,57,0,65,49,52,57,58],
[44,50,42,48,39,44,36,0,39,42,40,48],
[51,51,45,56,47,52,52,62,0,50,47,65],
[55,56,52,55,50,53,49,59,51,0,46,54],
[61,50,48,59,59,57,44,61,54,55,0,62],
[44,45,39,47,41,46,43,53,36,47,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 47, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,47,52,40,51,47,48,50,50,45,54],
[66,0,45,59,45,59,53,57,54,62,54,55],
[54,56,0,54,53,57,61,56,62,58,49,55],
[49,42,47,0,43,51,54,49,54,57,44,50],
[61,56,48,58,0,65,50,48,55,62,55,60],
[50,42,44,50,36,0,46,43,47,49,40,48],
[54,48,40,47,51,55,0,51,51,53,40,54],
[53,44,45,52,53,58,50,0,54,57,45,49],
[51,47,39,47,46,54,50,47,0,53,45,47],
[51,39,43,44,39,52,48,44,48,0,37,46],
[56,47,52,57,46,61,61,56,56,64,0,53],
[47,46,46,51,41,53,47,52,54,55,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 48, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,85,18,52,18,18,18,36,49,49,54],
[83,0,101,67,101,36,36,36,52,83,67,85],
[16,0,0,0,52,0,18,18,52,34,0,54],
[83,34,101,0,70,34,36,36,52,83,49,85],
[49,0,49,31,0,0,18,18,18,49,49,85],
[83,65,101,67,101,0,54,54,70,101,49,85],
[83,65,83,65,83,47,0,65,65,47,65,83],
[83,65,83,65,83,47,36,0,52,65,49,67],
[65,49,49,49,83,31,36,49,0,65,49,67],
[52,18,67,18,52,0,54,36,36,0,18,54],
[52,34,101,52,52,52,36,52,52,83,0,70],
[47,16,47,16,16,16,18,34,34,47,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 49, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,49,48,45,47,59,56,45,58,52,56],
[53,0,56,55,51,58,58,51,57,65,47,57],
[52,45,0,50,48,53,53,53,48,57,55,52],
[53,46,51,0,46,49,52,49,46,55,51,49],
[56,50,53,55,0,51,57,51,45,60,56,50],
[54,43,48,52,50,0,54,52,45,54,51,51],
[42,43,48,49,44,47,0,43,43,52,46,48],
[45,50,48,52,50,49,58,0,45,55,53,56],
[56,44,53,55,56,56,58,56,0,62,54,55],
[43,36,44,46,41,47,49,46,39,0,37,45],
[49,54,46,50,45,50,55,48,47,64,0,50],
[45,44,49,52,51,50,53,45,46,56,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 50, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,43,55,51,51,49,49,54,46,47,47],
[51,0,47,47,50,48,51,45,48,58,53,51],
[58,54,0,51,62,55,47,57,53,61,55,53],
[46,54,50,0,55,49,54,45,48,55,50,46],
[50,51,39,46,0,52,48,51,50,48,48,49],
[50,53,46,52,49,0,52,51,49,57,52,51],
[52,50,54,47,53,49,0,51,50,58,53,49],
[52,56,44,56,50,50,50,0,48,53,41,52],
[47,53,48,53,51,52,51,53,0,55,50,54],
[55,43,40,46,53,44,43,48,46,0,43,43],
[54,48,46,51,53,49,48,60,51,58,0,50],
[54,50,48,55,52,50,52,49,47,58,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 51, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,51,54,61,53,51,50,45,48,49,48],
[51,0,51,48,54,46,47,52,48,53,47,56],
[50,50,0,55,48,47,47,45,48,42,47,53],
[47,53,46,0,58,51,57,49,51,48,44,48],
[40,47,53,43,0,52,49,48,44,48,44,50],
[48,55,54,50,49,0,47,47,47,41,51,46],
[50,54,54,44,52,54,0,51,40,54,46,51],
[51,49,56,52,53,54,50,0,49,49,46,52],
[56,53,53,50,57,54,61,52,0,59,52,65],
[53,48,59,53,53,60,47,52,42,0,44,51],
[52,54,54,57,57,50,55,55,49,57,0,58],
[53,45,48,53,51,55,50,49,36,50,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 52, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,54,59,51,57,62,50,48,71,63,54],
[43,0,36,57,50,43,57,51,45,58,57,65],
[47,65,0,67,62,59,83,53,57,62,59,59],
[42,44,34,0,50,49,52,42,45,58,49,55],
[50,51,39,51,0,55,44,49,43,54,49,57],
[44,58,42,52,46,0,53,53,52,69,60,55],
[39,44,18,49,57,48,0,40,54,62,45,56],
[51,50,48,59,52,48,61,0,49,63,66,61],
[53,56,44,56,58,49,47,52,0,67,51,55],
[30,43,39,43,47,32,39,38,34,0,50,39],
[38,44,42,52,52,41,56,35,50,51,0,53],
[47,36,42,46,44,46,45,40,46,62,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 53, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,37,50,52,51,48,48,43,52,51,40,53],
[64,0,52,59,60,57,60,60,62,50,55,62],
[51,49,0,51,53,57,42,51,54,50,45,51],
[49,42,50,0,49,43,47,46,49,50,46,49],
[50,41,48,52,0,49,45,54,53,48,56,56],
[53,44,44,58,52,0,53,50,57,49,55,58],
[53,41,59,54,56,48,0,52,49,55,51,50],
[58,41,50,55,47,51,49,0,48,46,49,52],
[49,39,47,52,48,44,52,53,0,48,50,58],
[50,51,51,51,53,52,46,55,53,0,49,51],
[61,46,56,55,45,46,50,52,51,52,0,51],
[48,39,50,52,45,43,51,49,43,50,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 54, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,44,61,48,50,56,49,52,54,51,46],
[51,0,53,58,50,56,57,49,51,51,49,51],
[57,48,0,58,55,46,57,52,51,53,48,43],
[40,43,43,0,49,38,47,41,48,29,37,42],
[53,51,46,52,0,56,51,52,52,44,51,49],
[51,45,55,63,45,0,55,60,57,45,45,49],
[45,44,44,54,50,46,0,40,55,36,47,45],
[52,52,49,60,49,41,61,0,47,52,53,48],
[49,50,50,53,49,44,46,54,0,40,47,55],
[47,50,48,72,57,56,65,49,61,0,55,52],
[50,52,53,64,50,56,54,48,54,46,0,57],
[55,50,58,59,52,52,56,53,46,49,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 55, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,47,56,56,52,48,59,48,58,52,53],
[42,0,50,58,51,38,44,56,42,55,47,53],
[54,51,0,60,58,54,46,53,56,54,53,58],
[45,43,41,0,49,36,42,41,43,50,40,49],
[45,50,43,52,0,40,49,52,42,49,42,51],
[49,63,47,65,61,0,52,60,51,55,58,62],
[53,57,55,59,52,49,0,62,48,53,49,53],
[42,45,48,60,49,41,39,0,36,45,44,48],
[53,59,45,58,59,50,53,65,0,55,50,64],
[43,46,47,51,52,46,48,56,46,0,47,50],
[49,54,48,61,59,43,52,57,51,54,0,54],
[48,48,43,52,50,39,48,53,37,51,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 56, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,53,54,44,54,57,44,58,43,39,44],
[58,0,54,60,46,59,63,41,63,49,50,50],
[48,47,0,57,46,48,55,47,59,48,46,48],
[47,41,44,0,41,48,50,42,55,43,46,47],
[57,55,55,60,0,49,55,53,59,51,55,53],
[47,42,53,53,52,0,58,36,55,45,42,40],
[44,38,46,51,46,43,0,43,56,52,42,38],
[57,60,54,59,48,65,58,0,66,47,47,50],
[43,38,42,46,42,46,45,35,0,46,42,40],
[58,52,53,58,50,56,49,54,55,0,51,56],
[62,51,55,55,46,59,59,54,59,50,0,48],
[57,51,53,54,48,61,63,51,61,45,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 57, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,50,43,47,37,41,48,50,40,41,37],
[41,0,49,48,51,44,41,54,54,46,51,43],
[51,52,0,50,61,53,44,58,60,45,53,43],
[58,53,51,0,54,49,46,55,52,54,50,42],
[54,50,40,47,0,40,42,48,47,46,49,44],
[64,57,48,52,61,0,51,56,53,52,49,51],
[60,60,57,55,59,50,0,51,60,51,61,49],
[53,47,43,46,53,45,50,0,49,49,55,38],
[51,47,41,49,54,48,41,52,0,46,52,42],
[61,55,56,47,55,49,50,52,55,0,52,46],
[60,50,48,51,52,52,40,46,49,49,0,41],
[64,58,58,59,57,50,52,63,59,55,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 58, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,44,48,42,50,45,48,49,49,40,41],
[53,0,45,42,50,42,48,45,54,49,39,40],
[57,56,0,53,53,48,53,55,56,61,44,50],
[53,59,48,0,56,51,56,56,63,60,55,54],
[59,51,48,45,0,53,54,56,61,55,44,49],
[51,59,53,50,48,0,52,50,52,59,46,49],
[56,53,48,45,47,49,0,52,60,52,45,46],
[53,56,46,45,45,51,49,0,55,52,35,48],
[52,47,45,38,40,49,41,46,0,47,37,37],
[52,52,40,41,46,42,49,49,54,0,44,44],
[61,62,57,46,57,55,56,66,64,57,0,47],
[60,61,51,47,52,52,55,53,64,57,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 59, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,55,44,47,54,46,59,49,48,58,47],
[47,0,57,47,45,51,47,48,50,47,54,45],
[46,44,0,42,37,48,41,47,41,42,46,50],
[57,54,59,0,46,57,49,53,50,46,59,52],
[54,56,64,55,0,56,53,51,49,49,56,52],
[47,50,53,44,45,0,41,47,44,46,49,43],
[55,54,60,52,48,60,0,55,46,48,52,44],
[42,53,54,48,50,54,46,0,48,47,55,48],
[52,51,60,51,52,57,55,53,0,51,52,46],
[53,54,59,55,52,55,53,54,50,0,51,53],
[43,47,55,42,45,52,49,46,49,50,0,47],
[54,56,51,49,49,58,57,53,55,48,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 60, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,47,55,46,43,39,45,41,42,39,53],
[46,0,45,45,49,43,48,40,35,33,43,42],
[54,56,0,55,51,47,53,47,44,35,50,61],
[46,56,46,0,61,48,60,40,45,54,57,55],
[55,52,50,40,0,51,55,53,51,45,48,51],
[58,58,54,53,50,0,52,47,53,52,45,45],
[62,53,48,41,46,49,0,47,52,50,49,60],
[56,61,54,61,48,54,54,0,50,59,62,55],
[60,66,57,56,50,48,49,51,0,53,47,55],
[59,68,66,47,56,49,51,42,48,0,43,53],
[62,58,51,44,53,56,52,39,54,58,0,52],
[48,59,40,46,50,56,41,46,46,48,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 61, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,63,55,47,49,50,50,50,52,62,60],
[52,0,58,56,41,42,50,41,49,53,55,62],
[38,43,0,62,50,52,48,50,62,53,47,55],
[46,45,39,0,38,29,45,43,55,57,52,42],
[54,60,51,63,0,51,45,53,62,48,66,56],
[52,59,49,72,50,0,52,47,56,62,55,72],
[51,51,53,56,56,49,0,54,57,58,54,60],
[51,60,51,58,48,54,47,0,60,58,57,54],
[51,52,39,46,39,45,44,41,0,43,56,50],
[49,48,48,44,53,39,43,43,58,0,56,52],
[39,46,54,49,35,46,47,44,45,45,0,60],
[41,39,46,59,45,29,41,47,51,49,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 62, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,45,36,28,41,43,50,41,36,32,38],
[62,0,40,47,47,58,50,54,47,53,55,42],
[56,61,0,50,53,64,57,64,53,55,51,43],
[65,54,51,0,45,52,51,64,50,45,53,45],
[73,54,48,56,0,62,61,74,67,62,61,54],
[60,43,37,49,39,0,51,60,52,34,54,45],
[58,51,44,50,40,50,0,70,53,54,53,45],
[51,47,37,37,27,41,31,0,34,37,35,27],
[60,54,48,51,34,49,48,67,0,43,48,41],
[65,48,46,56,39,67,47,64,58,0,60,41],
[69,46,50,48,40,47,48,66,53,41,0,21],
[63,59,58,56,47,56,56,74,60,60,80,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 63, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,31,58,38,58,55,47,52,62,37,53],
[60,0,45,36,28,70,39,50,39,59,38,49],
[70,56,0,63,49,79,52,63,60,78,59,59],
[43,65,38,0,50,63,43,41,30,52,38,58],
[63,73,52,51,0,75,62,50,49,70,50,72],
[43,31,22,38,26,0,25,27,28,42,39,50],
[46,62,49,58,39,76,0,64,55,70,57,62],
[54,51,38,60,51,74,37,0,37,58,44,60],
[49,62,41,71,52,73,46,64,0,73,62,67],
[39,42,23,49,31,59,31,43,28,0,33,55],
[64,63,42,63,51,62,44,57,39,68,0,57],
[48,52,42,43,29,51,39,41,34,46,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 64, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,90,0,0,49,41,41,41,41,0,90],
[101,0,90,49,60,49,41,90,90,41,90,90],
[11,11,0,11,11,49,11,11,52,41,11,90],
[101,52,90,0,60,49,52,52,101,41,101,90],
[101,41,90,41,0,90,41,41,90,41,90,90],
[52,52,52,52,11,0,52,52,52,41,52,52],
[60,60,90,49,60,49,0,49,90,90,49,90],
[60,11,90,49,60,49,52,0,90,41,60,90],
[60,11,49,0,11,49,11,11,0,41,11,90],
[60,60,60,60,60,60,11,60,60,0,60,60],
[101,11,90,0,11,49,52,41,90,41,0,90],
[11,11,11,11,11,49,11,11,11,41,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 65, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,44,36,42,39,42,49,50,41,45,46],
[50,0,50,51,58,53,49,55,59,48,54,51],
[57,51,0,57,49,51,48,54,61,50,52,54],
[65,50,44,0,49,67,51,55,60,57,57,55],
[59,43,52,52,0,58,49,54,56,51,53,52],
[62,48,50,34,43,0,39,48,57,35,51,51],
[59,52,53,50,52,62,0,51,53,55,54,55],
[52,46,47,46,47,53,50,0,59,52,55,50],
[51,42,40,41,45,44,48,42,0,40,49,42],
[60,53,51,44,50,66,46,49,61,0,60,54],
[56,47,49,44,48,50,47,46,52,41,0,51],
[55,50,47,46,49,50,46,51,59,47,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 66, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,53,50,52,43,50,44,45,47,48,43],
[55,0,61,61,62,44,56,53,57,58,56,53],
[48,40,0,42,42,40,43,33,39,41,39,44],
[51,40,59,0,56,45,55,56,47,46,56,47],
[49,39,59,45,0,38,48,45,46,40,48,44],
[58,57,61,56,63,0,51,50,53,46,61,46],
[51,45,58,46,53,50,0,51,52,45,52,50],
[57,48,68,45,56,51,50,0,56,55,49,51],
[56,44,62,54,55,48,49,45,0,49,49,47],
[54,43,60,55,61,55,56,46,52,0,53,55],
[53,45,62,45,53,40,49,52,52,48,0,51],
[58,48,57,54,57,55,51,50,54,46,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 67, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,50,51,55,45,55,46,53,50,52,59],
[42,0,47,43,46,43,42,44,46,38,53,43],
[51,54,0,53,46,46,55,48,53,50,55,61],
[50,58,48,0,55,43,53,56,57,43,59,59],
[46,55,55,46,0,51,52,42,38,43,49,59],
[56,58,55,58,50,0,53,51,50,58,56,64],
[46,59,46,48,49,48,0,48,42,40,46,52],
[55,57,53,45,59,50,53,0,47,49,50,63],
[48,55,48,44,63,51,59,54,0,48,51,57],
[51,63,51,58,58,43,61,52,53,0,54,54],
[49,48,46,42,52,45,55,51,50,47,0,51],
[42,58,40,42,42,37,49,38,44,47,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 68, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,48,55,51,50,51,59,52,49,46,49],
[44,0,54,49,43,57,46,51,53,42,58,36],
[53,47,0,45,56,56,51,46,58,38,62,49],
[46,52,56,0,42,62,52,43,53,38,46,45],
[50,58,45,59,0,62,47,50,60,53,49,49],
[51,44,45,39,39,0,33,47,35,36,44,49],
[50,55,50,49,54,68,0,62,60,43,56,48],
[42,50,55,58,51,54,39,0,55,52,43,43],
[49,48,43,48,41,66,41,46,0,39,45,42],
[52,59,63,63,48,65,58,49,62,0,63,56],
[55,43,39,55,52,57,45,58,56,38,0,38],
[52,65,52,56,52,52,53,58,59,45,63,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 69, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,58,59,54,51,52,49,52,57,50,57],
[56,0,58,55,45,56,53,53,51,56,48,55],
[43,43,0,55,45,45,45,42,53,46,43,50],
[42,46,46,0,43,45,47,50,45,49,45,55],
[47,56,56,58,0,57,59,59,57,54,52,61],
[50,45,56,56,44,0,45,50,55,47,49,52],
[49,48,56,54,42,56,0,47,55,52,51,56],
[52,48,59,51,42,51,54,0,55,48,42,54],
[49,50,48,56,44,46,46,46,0,52,40,52],
[44,45,55,52,47,54,49,53,49,0,49,56],
[51,53,58,56,49,52,50,59,61,52,0,61],
[44,46,51,46,40,49,45,47,49,45,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 70, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,38,51,57,35,54,48,48,43,47,48],
[50,0,47,38,59,36,50,54,48,65,55,41],
[63,54,0,58,66,64,59,54,47,71,49,57],
[50,63,43,0,58,50,56,63,58,53,54,68],
[44,42,35,43,0,38,43,48,36,55,38,45],
[66,65,37,51,63,0,47,59,51,60,55,54],
[47,51,42,45,58,54,0,60,55,67,53,51],
[53,47,47,38,53,42,41,0,47,54,45,44],
[53,53,54,43,65,50,46,54,0,67,54,60],
[58,36,30,48,46,41,34,47,34,0,41,47],
[54,46,52,47,63,46,48,56,47,60,0,53],
[53,60,44,33,56,47,50,57,41,54,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 71, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,71,52,77,81,63,78,46,74,89,76,53],
[30,0,23,71,57,42,30,39,20,61,57,64],
[49,78,0,61,78,48,65,30,44,79,70,49],
[24,30,40,0,50,33,37,13,17,61,29,42],
[20,44,23,51,0,19,24,13,17,61,48,9],
[38,59,53,68,82,0,64,55,47,90,55,69],
[23,71,36,64,77,37,0,30,34,73,65,61],
[55,62,71,88,88,46,71,0,71,94,74,45],
[27,81,57,84,84,54,67,30,0,73,83,73],
[12,40,22,40,40,11,28,7,28,0,27,11],
[25,44,31,72,53,46,36,27,18,74,0,30],
[48,37,52,59,92,32,40,56,28,90,71,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 72, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,45,45,46,50,44,58,39,51,48,47],
[48,0,33,36,51,33,37,46,34,43,45,39],
[56,68,0,43,66,50,58,64,43,51,57,62],
[56,65,58,0,65,57,50,63,48,53,59,61],
[55,50,35,36,0,38,31,49,27,39,39,49],
[51,68,51,44,63,0,50,55,47,52,56,49],
[57,64,43,51,70,51,0,53,46,61,62,53],
[43,55,37,38,52,46,48,0,34,47,43,47],
[62,67,58,53,74,54,55,67,0,52,50,58],
[50,58,50,48,62,49,40,54,49,0,55,53],
[53,56,44,42,62,45,39,58,51,46,0,50],
[54,62,39,40,52,52,48,54,43,48,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 73, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,53,47,60,58,57,65,52,51,60,62],
[48,0,53,54,63,52,61,64,54,53,55,57],
[48,48,0,47,49,45,51,51,42,46,50,43],
[54,47,54,0,61,54,60,61,59,55,57,58],
[41,38,52,40,0,52,52,51,49,44,45,52],
[43,49,56,47,49,0,57,60,48,44,46,48],
[44,40,50,41,49,44,0,55,52,44,46,48],
[36,37,50,40,50,41,46,0,44,40,43,48],
[49,47,59,42,52,53,49,57,0,52,54,51],
[50,48,55,46,57,57,57,61,49,0,49,62],
[41,46,51,44,56,55,55,58,47,52,0,50],
[39,44,58,43,49,53,53,53,50,39,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 74, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,46,44,49,45,48,46,41,43,47,46],
[54,0,50,43,59,48,50,50,50,52,52,49],
[55,51,0,46,56,47,47,51,50,49,58,50],
[57,58,55,0,59,55,50,49,57,52,57,50],
[52,42,45,42,0,49,37,46,42,44,43,42],
[56,53,54,46,52,0,54,45,50,51,49,58],
[53,51,54,51,64,47,0,59,50,48,47,59],
[55,51,50,52,55,56,42,0,46,45,48,55],
[60,51,51,44,59,51,51,55,0,56,55,55],
[58,49,52,49,57,50,53,56,45,0,50,49],
[54,49,43,44,58,52,54,53,46,51,0,52],
[55,52,51,51,59,43,42,46,46,52,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 75, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,49,54,49,36,29,47,47,46,41,40],
[60,0,48,49,48,34,48,51,43,51,39,39],
[52,53,0,52,45,37,51,43,58,57,33,43],
[47,52,49,0,53,45,33,43,54,62,42,36],
[52,53,56,48,0,33,52,36,51,63,32,52],
[65,67,64,56,68,0,47,44,63,56,54,58],
[72,53,50,68,49,54,0,44,66,59,47,48],
[54,50,58,58,65,57,57,0,51,64,41,45],
[54,58,43,47,50,38,35,50,0,68,31,33],
[55,50,44,39,38,45,42,37,33,0,28,40],
[60,62,68,59,69,47,54,60,70,73,0,58],
[61,62,58,65,49,43,53,56,68,61,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 76, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,57,59,62,49,63,46,53,59,60,48],
[57,0,44,58,60,37,26,39,49,44,48,38],
[44,57,0,46,48,42,42,45,57,36,52,41],
[42,43,55,0,43,32,31,31,32,39,34,43],
[39,41,53,58,0,38,35,19,42,36,45,50],
[52,64,59,69,63,0,69,52,66,43,49,55],
[38,75,59,70,66,32,0,47,77,38,48,47],
[55,62,56,70,82,49,54,0,79,52,40,72],
[48,52,44,69,59,35,24,22,0,32,32,52],
[42,57,65,62,65,58,63,49,69,0,50,55],
[41,53,49,67,56,52,53,61,69,51,0,56],
[53,63,60,58,51,46,54,29,49,46,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 77, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,47,50,48,57,47,56,57,53,47,47],
[48,0,48,48,47,61,52,56,52,48,53,53],
[54,53,0,53,59,62,50,57,63,57,44,50],
[51,53,48,0,53,63,55,50,64,51,50,45],
[53,54,42,48,0,58,48,48,54,48,52,43],
[44,40,39,38,43,0,43,41,52,39,40,37],
[54,49,51,46,53,58,0,51,57,53,48,50],
[45,45,44,51,53,60,50,0,54,51,42,51],
[44,49,38,37,47,49,44,47,0,41,36,46],
[48,53,44,50,53,62,48,50,60,0,49,48],
[54,48,57,51,49,61,53,59,65,52,0,56],
[54,48,51,56,58,64,51,50,55,53,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 78, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,55,66,52,60,45,67,50,53,57,61],
[46,0,46,55,62,50,38,58,43,43,59,44],
[46,55,0,72,49,62,54,58,56,52,48,51],
[35,46,29,0,45,47,49,49,51,49,41,49],
[49,39,52,56,0,61,39,44,52,51,37,52],
[41,51,39,54,40,0,53,52,39,36,37,51],
[56,63,47,52,62,48,0,54,56,60,50,48],
[34,43,43,52,57,49,47,0,40,49,39,54],
[51,58,45,50,49,62,45,61,0,51,44,54],
[48,58,49,52,50,65,41,52,50,0,49,53],
[44,42,53,60,64,64,51,62,57,52,0,56],
[40,57,50,52,49,50,53,47,47,48,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 79, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,37,40,40,51,36,34,51,34,41,46],
[57,0,51,58,52,53,54,49,58,58,43,62],
[64,50,0,50,52,53,60,48,61,52,62,63],
[61,43,51,0,45,47,57,43,58,57,53,59],
[61,49,49,56,0,50,49,46,43,50,56,49],
[50,48,48,54,51,0,39,49,48,41,47,44],
[65,47,41,44,52,62,0,42,47,50,48,44],
[67,52,53,58,55,52,59,0,53,57,46,64],
[50,43,40,43,58,53,54,48,0,47,46,54],
[67,43,49,44,51,60,51,44,54,0,40,54],
[60,58,39,48,45,54,53,55,55,61,0,48],
[55,39,38,42,52,57,57,37,47,47,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 80, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,35,37,52,37,42,38,45,26,42,53],
[59,0,56,44,47,61,39,53,62,41,46,65],
[66,45,0,39,70,71,58,58,62,35,58,70],
[64,57,62,0,69,54,49,40,63,42,60,64],
[49,54,31,32,0,37,46,47,26,31,38,50],
[64,40,30,47,64,0,57,36,51,34,55,38],
[59,62,43,52,55,44,0,51,52,55,43,61],
[63,48,43,61,54,65,50,0,56,34,50,63],
[56,39,39,38,75,50,49,45,0,47,35,55],
[75,60,66,59,70,67,46,67,54,0,53,56],
[59,55,43,41,63,46,58,51,66,48,0,46],
[48,36,31,37,51,63,40,38,46,45,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 81, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,58,53,45,61,54,58,52,53,55,56],
[43,0,53,51,54,54,48,54,43,48,49,48],
[43,48,0,52,38,45,44,44,40,36,45,42],
[48,50,49,0,45,41,42,45,52,45,52,53],
[56,47,63,56,0,58,44,54,63,48,50,60],
[40,47,56,60,43,0,46,47,53,43,52,54],
[47,53,57,59,57,55,0,47,52,48,60,60],
[43,47,57,56,47,54,54,0,53,50,59,54],
[49,58,61,49,38,48,49,48,0,50,54,58],
[48,53,65,56,53,58,53,51,51,0,53,61],
[46,52,56,49,51,49,41,42,47,48,0,53],
[45,53,59,48,41,47,41,47,43,40,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 82, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,55,49,57,44,47,54,52,54,46,57],
[51,0,46,54,58,46,48,55,44,50,43,56],
[46,55,0,58,55,51,56,49,39,52,49,56],
[52,47,43,0,49,44,44,46,48,46,46,51],
[44,43,46,52,0,46,46,53,44,50,39,47],
[57,55,50,57,55,0,47,54,48,51,49,52],
[54,53,45,57,55,54,0,52,49,51,52,49],
[47,46,52,55,48,47,49,0,46,50,42,52],
[49,57,62,53,57,53,52,55,0,52,52,55],
[47,51,49,55,51,50,50,51,49,0,47,56],
[55,58,52,55,62,52,49,59,49,54,0,53],
[44,45,45,50,54,49,52,49,46,45,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 83, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,59,46,52,51,47,47,57,39,56,58],
[58,0,53,57,58,53,52,46,56,52,58,52],
[42,48,0,48,48,47,48,44,43,48,57,49],
[55,44,53,0,59,46,50,50,47,43,51,47],
[49,43,53,42,0,40,49,48,53,41,47,53],
[50,48,54,55,61,0,49,49,53,51,59,53],
[54,49,53,51,52,52,0,51,52,43,55,55],
[54,55,57,51,53,52,50,0,47,49,58,51],
[44,45,58,54,48,48,49,54,0,40,58,52],
[62,49,53,58,60,50,58,52,61,0,56,56],
[45,43,44,50,54,42,46,43,43,45,0,46],
[43,49,52,54,48,48,46,50,49,45,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 84, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,46,45,65,52,48,57,48,59,50,44],
[49,0,52,55,57,60,57,66,40,73,60,47],
[55,49,0,59,46,54,51,57,47,72,47,52],
[56,46,42,0,53,55,44,50,30,65,53,40],
[36,44,55,48,0,39,40,38,37,63,42,34],
[49,41,47,46,62,0,45,60,29,61,35,36],
[53,44,50,57,61,56,0,63,50,66,43,38],
[44,35,44,51,63,41,38,0,45,59,33,50],
[53,61,54,71,64,72,51,56,0,69,66,48],
[42,28,29,36,38,40,35,42,32,0,45,32],
[51,41,54,48,59,66,58,68,35,56,0,37],
[57,54,49,61,67,65,63,51,53,69,64,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 85, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,52,68,44,60,45,33,34,40,49,51],
[60,0,61,57,57,65,54,57,50,57,45,59],
[49,40,0,56,37,59,50,51,49,51,47,55],
[33,44,45,0,42,51,47,40,40,33,39,45],
[57,44,64,59,0,77,53,39,51,39,55,52],
[41,36,42,50,24,0,29,28,25,34,40,40],
[56,47,51,54,48,72,0,55,51,44,56,58],
[68,44,50,61,62,73,46,0,57,52,42,58],
[67,51,52,61,50,76,50,44,0,53,57,65],
[61,44,50,68,62,67,57,49,48,0,42,62],
[52,56,54,62,46,61,45,59,44,59,0,49],
[50,42,46,56,49,61,43,43,36,39,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 86, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,52,48,54,43,47,47,48,40,41,53],
[49,0,49,49,51,54,45,49,53,50,46,59],
[49,52,0,49,58,49,45,48,48,49,48,49],
[53,52,52,0,52,50,52,55,51,51,45,50],
[47,50,43,49,0,46,49,47,43,50,38,48],
[58,47,52,51,55,0,48,46,47,49,46,53],
[54,56,56,49,52,53,0,52,48,49,45,47],
[54,52,53,46,54,55,49,0,46,43,43,51],
[53,48,53,50,58,54,53,55,0,56,52,54],
[61,51,52,50,51,52,52,58,45,0,44,53],
[60,55,53,56,63,55,56,58,49,57,0,53],
[48,42,52,51,53,48,54,50,47,48,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 87, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,56,48,45,39,51,38,53,40,42,42],
[70,0,59,51,71,54,49,51,70,44,49,62],
[45,42,0,56,59,52,53,37,53,56,52,59],
[53,50,45,0,61,59,49,52,39,46,51,59],
[56,30,42,40,0,34,57,32,45,32,35,47],
[62,47,49,42,67,0,51,47,46,48,63,54],
[50,52,48,52,44,50,0,29,38,54,33,50],
[63,50,64,49,69,54,72,0,51,49,61,45],
[48,31,48,62,56,55,63,50,0,44,42,44],
[61,57,45,55,69,53,47,52,57,0,71,53],
[59,52,49,50,66,38,68,40,59,30,0,61],
[59,39,42,42,54,47,51,56,57,48,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 88, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,39,48,34,49,48,40,55,36,50,45],
[56,0,52,54,36,51,53,54,53,51,56,47],
[62,49,0,53,38,53,47,40,56,41,47,49],
[53,47,48,0,33,53,40,37,44,37,53,44],
[67,65,63,68,0,65,54,50,59,56,78,60],
[52,50,48,48,36,0,41,47,61,49,45,41],
[53,48,54,61,47,60,0,55,61,43,56,53],
[61,47,61,64,51,54,46,0,70,40,56,48],
[46,48,45,57,42,40,40,31,0,29,50,38],
[65,50,60,64,45,52,58,61,72,0,56,62],
[51,45,54,48,23,56,45,45,51,45,0,52],
[56,54,52,57,41,60,48,53,63,39,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 89, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,60,50,54,52,57,54,48,69,51,49],
[40,0,52,39,50,51,48,46,56,62,45,45],
[41,49,0,51,44,50,46,40,48,54,50,40],
[51,62,50,0,51,68,57,57,55,68,56,51],
[47,51,57,50,0,52,48,57,51,61,60,52],
[49,50,51,33,49,0,61,42,40,68,50,41],
[44,53,55,44,53,40,0,53,44,57,58,58],
[47,55,61,44,44,59,48,0,47,66,50,49],
[53,45,53,46,50,61,57,54,0,71,49,51],
[32,39,47,33,40,33,44,35,30,0,34,29],
[50,56,51,45,41,51,43,51,52,67,0,44],
[52,56,61,50,49,60,43,52,50,72,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 90, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,37,30,57,55,52,49,55,42,37,31],
[55,0,56,39,54,37,58,41,47,59,60,43],
[64,45,0,34,39,63,50,64,64,76,37,61],
[71,62,67,0,41,58,58,67,67,70,62,55],
[44,47,62,60,0,78,52,78,78,60,39,60],
[46,64,38,43,23,0,59,58,73,59,38,54],
[49,43,51,43,49,42,0,46,52,45,31,49],
[52,60,37,34,23,43,55,0,30,65,28,44],
[46,54,37,34,23,28,49,71,0,59,28,44],
[59,42,25,31,41,42,56,36,42,0,55,45],
[64,41,64,39,62,63,70,73,73,46,0,53],
[70,58,40,46,41,47,52,57,57,56,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 91, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,50,58,67,51,48,77,60,41,54,49],
[50,0,48,66,64,52,48,64,68,50,47,69],
[51,53,0,57,49,58,68,52,76,43,42,50],
[43,35,44,0,64,34,45,55,69,56,51,48],
[34,37,52,37,0,41,52,49,59,28,49,32],
[50,49,43,67,60,0,56,70,65,59,48,44],
[53,53,33,56,49,45,0,63,67,35,47,54],
[24,37,49,46,52,31,38,0,53,47,37,27],
[41,33,25,32,42,36,34,48,0,29,41,42],
[60,51,58,45,73,42,66,54,72,0,46,50],
[47,54,59,50,52,53,54,64,60,55,0,46],
[52,32,51,53,69,57,47,74,59,51,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 92, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,49,54,49,40,50,60,44,61,44,55],
[41,0,40,43,31,27,36,56,35,39,41,42],
[52,61,0,56,45,51,38,63,46,57,51,59],
[47,58,45,0,40,38,39,56,40,49,41,51],
[52,70,56,61,0,50,46,72,58,63,52,61],
[61,74,50,63,51,0,45,67,56,61,41,61],
[51,65,63,62,55,56,0,74,64,62,49,64],
[41,45,38,45,29,34,27,0,34,35,36,47],
[57,66,55,61,43,45,37,67,0,59,57,57],
[40,62,44,52,38,40,39,66,42,0,43,56],
[57,60,50,60,49,60,52,65,44,58,0,60],
[46,59,42,50,40,40,37,54,44,45,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 93, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,60,47,43,47,42,56,49,40,42,55],
[50,0,52,47,45,37,47,46,37,39,48,50],
[41,49,0,48,48,40,45,49,38,42,40,47],
[54,54,53,0,52,50,52,55,48,45,43,52],
[58,56,53,49,0,51,45,52,42,48,44,52],
[54,64,61,51,50,0,58,51,54,54,56,56],
[59,54,56,49,56,43,0,61,50,61,55,55],
[45,55,52,46,49,50,40,0,45,39,41,39],
[52,64,63,53,59,47,51,56,0,59,56,54],
[61,62,59,56,53,47,40,62,42,0,55,51],
[59,53,61,58,57,45,46,60,45,46,0,59],
[46,51,54,49,49,45,46,62,47,50,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 94, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,43,51,50,49,47,43,48,53,48,41],
[49,0,46,49,56,41,45,48,60,50,45,42],
[58,55,0,52,53,54,42,46,57,52,45,39],
[50,52,49,0,49,48,46,46,45,56,44,43],
[51,45,48,52,0,45,48,49,46,51,48,50],
[52,60,47,53,56,0,57,48,56,48,49,43],
[54,56,59,55,53,44,0,41,57,50,48,52],
[58,53,55,55,52,53,60,0,53,50,49,47],
[53,41,44,56,55,45,44,48,0,52,47,43],
[48,51,49,45,50,53,51,51,49,0,49,37],
[53,56,56,57,53,52,53,52,54,52,0,47],
[60,59,62,58,51,58,49,54,58,64,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 95, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,48,38,51,51,52,44,56,38,46,44],
[44,0,50,27,38,39,49,39,51,43,55,38],
[53,51,0,35,42,48,51,47,49,49,55,43],
[63,74,66,0,53,57,62,56,76,53,56,50],
[50,63,59,48,0,60,60,54,59,52,57,42],
[50,62,53,44,41,0,54,43,62,53,47,51],
[49,52,50,39,41,47,0,44,52,39,47,47],
[57,62,54,45,47,58,57,0,53,48,53,49],
[45,50,52,25,42,39,49,48,0,44,51,41],
[63,58,52,48,49,48,62,53,57,0,55,52],
[55,46,46,45,44,54,54,48,50,46,0,48],
[57,63,58,51,59,50,54,52,60,49,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 96, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,47,53,55,54,47,60,58,52,58,50],
[52,0,54,62,53,59,49,54,57,50,58,59],
[54,47,0,60,59,53,50,57,58,51,56,51],
[48,39,41,0,49,49,37,49,54,46,52,53],
[46,48,42,52,0,51,55,51,47,52,54,48],
[47,42,48,52,50,0,45,55,58,49,50,50],
[54,52,51,64,46,56,0,60,60,54,59,56],
[41,47,44,52,50,46,41,0,49,45,50,44],
[43,44,43,47,54,43,41,52,0,44,52,42],
[49,51,50,55,49,52,47,56,57,0,60,53],
[43,43,45,49,47,51,42,51,49,41,0,44],
[51,42,50,48,53,51,45,57,59,48,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 97, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,43,56,51,64,53,52,48,55,44,53],
[42,0,39,47,46,58,42,49,46,53,44,35],
[58,62,0,49,54,62,46,62,52,54,47,44],
[45,54,52,0,49,59,48,51,51,46,46,48],
[50,55,47,52,0,51,45,61,57,55,48,53],
[37,43,39,42,50,0,34,51,40,43,39,43],
[48,59,55,53,56,67,0,67,62,61,53,52],
[49,52,39,50,40,50,34,0,51,50,47,46],
[53,55,49,50,44,61,39,50,0,57,41,35],
[46,48,47,55,46,58,40,51,44,0,49,42],
[57,57,54,55,53,62,48,54,60,52,0,50],
[48,66,57,53,48,58,49,55,66,59,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 98, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,51,52,44,42,43,47,52,43,48,45],
[60,0,55,53,49,43,45,56,58,49,51,48],
[50,46,0,49,43,48,48,53,48,46,49,46],
[49,48,52,0,47,49,52,58,56,51,53,48],
[57,52,58,54,0,50,52,53,54,52,41,51],
[59,58,53,52,51,0,43,55,57,47,49,61],
[58,56,53,49,49,58,0,53,59,51,51,49],
[54,45,48,43,48,46,48,0,52,42,45,47],
[49,43,53,45,47,44,42,49,0,46,40,52],
[58,52,55,50,49,54,50,59,55,0,52,47],
[53,50,52,48,60,52,50,56,61,49,0,54],
[56,53,55,53,50,40,52,54,49,54,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 99, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,55,53,47,65,66,55,59,49,58,52],
[48,0,61,56,44,56,59,49,52,53,61,57],
[46,40,0,49,39,51,56,42,51,45,49,54],
[48,45,52,0,41,54,61,55,46,41,59,49],
[54,57,62,60,0,54,67,49,58,51,54,50],
[36,45,50,47,47,0,54,49,43,53,54,55],
[35,42,45,40,34,47,0,42,38,44,50,44],
[46,52,59,46,52,52,59,0,53,50,65,56],
[42,49,50,55,43,58,63,48,0,49,54,44],
[52,48,56,60,50,48,57,51,52,0,51,52],
[43,40,52,42,47,47,51,36,47,50,0,48],
[49,44,47,52,51,46,57,45,57,49,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 100, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,58,58,53,53,52,56,49,45,53,57],
[50,0,56,49,49,48,45,54,47,42,51,49],
[43,45,0,49,49,54,49,48,47,44,47,50],
[43,52,52,0,45,50,44,40,44,44,47,52],
[48,52,52,56,0,50,50,48,46,44,56,50],
[48,53,47,51,51,0,35,47,44,41,49,49],
[49,56,52,57,51,66,0,53,53,54,58,62],
[45,47,53,61,53,54,48,0,47,44,52,52],
[52,54,54,57,55,57,48,54,0,52,58,57],
[56,59,57,57,57,60,47,57,49,0,60,59],
[48,50,54,54,45,52,43,49,43,41,0,49],
[44,52,51,49,51,52,39,49,44,42,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 101, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,43,53,47,47,47,51,52,54,46,55],
[51,0,47,50,47,47,50,52,47,44,43,55],
[58,54,0,52,56,49,54,55,46,54,50,62],
[48,51,49,0,51,56,51,51,49,42,46,56],
[54,54,45,50,0,51,57,61,57,48,53,61],
[54,54,52,45,50,0,51,57,43,54,55,58],
[54,51,47,50,44,50,0,51,46,43,46,51],
[50,49,46,50,40,44,50,0,37,51,48,60],
[49,54,55,52,44,58,55,64,0,51,54,64],
[47,57,47,59,53,47,58,50,50,0,52,63],
[55,58,51,55,48,46,55,53,47,49,0,58],
[46,46,39,45,40,43,50,41,37,38,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 102, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,50,50,48,44,51,58,41,42,43,43],
[53,0,43,49,53,40,54,54,37,48,49,48],
[51,58,0,56,53,45,54,58,44,43,53,49],
[51,52,45,0,51,43,50,54,37,42,37,50],
[53,48,48,50,0,41,53,52,39,42,39,41],
[57,61,56,58,60,0,58,61,44,51,49,54],
[50,47,47,51,48,43,0,54,42,41,40,48],
[43,47,43,47,49,40,47,0,39,39,43,42],
[60,64,57,64,62,57,59,62,0,48,49,61],
[59,53,58,59,59,50,60,62,53,0,54,56],
[58,52,48,64,62,52,61,58,52,47,0,49],
[58,53,52,51,60,47,53,59,40,45,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 103, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,84,63,55,72,72,38,55,45,60,73,73],
[17,0,18,32,32,38,20,51,59,22,33,50],
[38,83,0,39,44,61,48,56,77,38,42,69],
[46,69,62,0,44,77,53,45,65,46,69,76],
[29,69,57,57,0,56,45,66,66,55,42,54],
[29,63,40,24,45,0,28,46,43,34,29,47],
[63,81,53,48,56,73,0,65,59,34,69,63],
[46,50,45,56,35,55,36,0,58,19,50,54],
[56,42,24,36,35,58,42,43,0,39,66,75],
[41,79,63,55,46,67,67,82,62,0,54,75],
[28,68,59,32,59,72,32,51,35,47,0,76],
[28,51,32,25,47,54,38,47,26,26,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 104, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,50,51,51,59,52,47,50,46,51,49],
[50,0,52,55,47,39,42,30,47,43,55,37],
[51,49,0,55,48,48,46,51,53,45,49,47],
[50,46,46,0,38,43,40,36,62,45,55,40],
[50,54,53,63,0,51,53,48,60,43,53,51],
[42,62,53,58,50,0,51,43,58,51,57,41],
[49,59,55,61,48,50,0,48,55,51,59,47],
[54,71,50,65,53,58,53,0,56,49,56,52],
[51,54,48,39,41,43,46,45,0,48,51,38],
[55,58,56,56,58,50,50,52,53,0,55,49],
[50,46,52,46,48,44,42,45,50,46,0,52],
[52,64,54,61,50,60,54,49,63,52,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 105, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,48,46,48,48,47,45,50,48,50,36],
[55,0,50,52,54,58,44,51,51,55,51,52],
[53,51,0,46,50,48,48,56,50,52,53,41],
[55,49,55,0,55,58,46,49,50,51,56,46],
[53,47,51,46,0,51,45,50,49,45,53,41],
[53,43,53,43,50,0,47,54,52,52,52,43],
[54,57,53,55,56,54,0,55,55,49,53,45],
[56,50,45,52,51,47,46,0,55,49,50,40],
[51,50,51,51,52,49,46,46,0,53,49,48],
[53,46,49,50,56,49,52,52,48,0,51,46],
[51,50,48,45,48,49,48,51,52,50,0,46],
[65,49,60,55,60,58,56,61,53,55,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 106, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,39,39,1,40,30,30,0,70,1,30],
[101,0,70,100,32,71,61,62,31,70,32,61],
[62,31,0,31,31,70,30,62,1,70,31,31],
[62,1,70,0,1,71,30,62,1,70,32,31],
[100,69,70,100,0,100,69,100,39,69,100,100],
[61,30,31,30,1,0,30,61,0,69,30,30],
[71,40,71,71,32,71,0,62,71,70,32,32],
[71,39,39,39,1,40,39,0,39,40,40,0],
[101,70,100,100,62,101,30,62,0,70,62,62],
[31,31,31,31,32,32,31,61,31,0,31,31],
[100,69,70,69,1,71,69,61,39,70,0,30],
[71,40,70,70,1,71,69,101,39,70,71,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 107, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,67,57,58,63,68,46,55,68,44,72,52],
[34,0,48,55,33,60,42,36,35,22,45,17],
[44,53,0,53,49,56,51,51,71,46,74,34],
[43,46,48,0,31,60,45,58,58,33,52,32],
[38,68,52,70,0,67,34,45,57,42,58,36],
[33,41,45,41,34,0,30,56,41,25,48,29],
[55,59,50,56,67,71,0,41,61,48,73,62],
[46,65,50,43,56,45,60,0,50,34,53,48],
[33,66,30,43,44,60,40,51,0,50,60,30],
[57,79,55,68,59,76,53,67,51,0,57,49],
[29,56,27,49,43,53,28,48,41,44,0,45],
[49,84,67,69,65,72,39,53,71,52,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 108, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,42,61,45,50,48,47,56,50,58,55],
[49,0,49,51,48,50,51,48,49,61,62,56],
[59,52,0,45,47,48,55,49,45,51,56,46],
[40,50,56,0,44,44,45,49,36,50,56,45],
[56,53,54,57,0,52,52,54,58,54,66,46],
[51,51,53,57,49,0,53,53,52,62,56,51],
[53,50,46,56,49,48,0,44,44,52,60,50],
[54,53,52,52,47,48,57,0,52,50,64,50],
[45,52,56,65,43,49,57,49,0,59,59,51],
[51,40,50,51,47,39,49,51,42,0,45,47],
[43,39,45,45,35,45,41,37,42,56,0,44],
[46,45,55,56,55,50,51,51,50,54,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 109, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,48,61,47,63,57,40,53,58,67,50],
[51,0,43,61,37,64,55,43,62,64,50,52],
[53,58,0,66,45,68,67,55,66,70,68,61],
[40,40,35,0,36,52,51,33,51,53,56,51],
[54,64,56,65,0,69,60,45,63,56,66,58],
[38,37,33,49,32,0,39,34,35,42,54,48],
[44,46,34,50,41,62,0,38,48,55,64,51],
[61,58,46,68,56,67,63,0,67,59,79,67],
[48,39,35,50,38,66,53,34,0,51,63,48],
[43,37,31,48,45,59,46,42,50,0,58,55],
[34,51,33,45,35,47,37,22,38,43,0,46],
[51,49,40,50,43,53,50,34,53,46,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 110, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,63,48,54,49,63,57,56,63,55,50],
[44,0,51,39,56,55,46,47,48,59,47,43],
[38,50,0,46,48,51,56,55,45,57,55,49],
[53,62,55,0,56,57,61,61,46,61,50,58],
[47,45,53,45,0,39,54,53,48,57,54,40],
[52,46,50,44,62,0,56,51,44,65,49,43],
[38,55,45,40,47,45,0,46,47,57,44,43],
[44,54,46,40,48,50,55,0,46,56,46,45],
[45,53,56,55,53,57,54,55,0,55,51,48],
[38,42,44,40,44,36,44,45,46,0,41,37],
[46,54,46,51,47,52,57,55,50,60,0,39],
[51,58,52,43,61,58,58,56,53,64,62,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 111, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,49,50,65,47,58,67,62,71,52,51],
[55,0,55,61,69,48,61,73,73,76,60,68],
[52,46,0,48,63,48,52,65,60,77,38,49],
[51,40,53,0,56,53,58,67,53,75,56,56],
[36,32,38,45,0,36,36,52,51,54,36,48],
[54,53,53,48,65,0,59,65,65,72,51,68],
[43,40,49,43,65,42,0,61,55,59,41,57],
[34,28,36,34,49,36,40,0,33,51,31,54],
[39,28,41,48,50,36,46,68,0,63,43,56],
[30,25,24,26,47,29,42,50,38,0,28,43],
[49,41,63,45,65,50,60,70,58,73,0,67],
[50,33,52,45,53,33,44,47,45,58,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 112, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,49,55,52,53,49,48,48,46,50,51],
[41,0,42,50,42,43,46,50,46,52,50,45],
[52,59,0,53,52,45,46,52,50,52,51,45],
[46,51,48,0,40,44,45,43,51,54,49,46],
[49,59,49,61,0,43,43,52,47,48,51,52],
[48,58,56,57,58,0,48,50,50,57,50,54],
[52,55,55,56,58,53,0,56,48,56,53,57],
[53,51,49,58,49,51,45,0,51,56,52,53],
[53,55,51,50,54,51,53,50,0,52,42,51],
[55,49,49,47,53,44,45,45,49,0,50,45],
[51,51,50,52,50,51,48,49,59,51,0,51],
[50,56,56,55,49,47,44,48,50,56,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 113, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,46,52,46,38,58,47,40,48,38,34],
[57,0,51,44,65,48,65,48,34,55,60,49],
[55,50,0,50,64,47,75,38,48,47,71,45],
[49,57,51,0,59,46,54,28,43,46,40,42],
[55,36,37,42,0,44,60,34,16,40,47,40],
[63,53,54,55,57,0,66,57,48,68,70,50],
[43,36,26,47,41,35,0,22,28,31,53,42],
[54,53,63,73,67,44,79,0,59,61,73,58],
[61,67,53,58,85,53,73,42,0,76,67,52],
[53,46,54,55,61,33,70,40,25,0,56,59],
[63,41,30,61,54,31,48,28,34,45,0,57],
[67,52,56,59,61,51,59,43,49,42,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 114, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,42,51,57,49,54,47,55,45,50,45],
[59,0,45,52,63,57,60,52,58,57,65,56],
[59,56,0,42,49,41,49,47,57,58,57,48],
[50,49,59,0,63,59,52,53,53,58,55,52],
[44,38,52,38,0,43,47,52,51,48,50,34],
[52,44,60,42,58,0,55,40,53,39,57,51],
[47,41,52,49,54,46,0,47,52,43,61,50],
[54,49,54,48,49,61,54,0,54,53,58,50],
[46,43,44,48,50,48,49,47,0,43,48,35],
[56,44,43,43,53,62,58,48,58,0,61,54],
[51,36,44,46,51,44,40,43,53,40,0,50],
[56,45,53,49,67,50,51,51,66,47,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 115, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,48,51,52,50,46,48,57,52,54,53],
[42,0,45,50,54,47,47,54,52,47,53,50],
[53,56,0,56,60,61,49,61,62,57,59,55],
[50,51,45,0,53,47,45,53,51,44,55,43],
[49,47,41,48,0,47,41,46,56,40,53,46],
[51,54,40,54,54,0,46,55,57,51,61,50],
[55,54,52,56,60,55,0,52,55,48,59,50],
[53,47,40,48,55,46,49,0,48,48,55,50],
[44,49,39,50,45,44,46,53,0,49,51,51],
[49,54,44,57,61,50,53,53,52,0,50,50],
[47,48,42,46,48,40,42,46,50,51,0,46],
[48,51,46,58,55,51,51,51,50,51,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 116, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,51,44,60,47,46,50,50,46,57,51],
[57,0,60,57,63,60,56,56,49,55,59,52],
[50,41,0,48,65,47,47,53,44,45,46,48],
[57,44,53,0,64,43,53,57,52,54,49,51],
[41,38,36,37,0,48,41,35,41,43,39,38],
[54,41,54,58,53,0,44,47,45,53,44,39],
[55,45,54,48,60,57,0,60,48,50,45,52],
[51,45,48,44,66,54,41,0,43,42,45,48],
[51,52,57,49,60,56,53,58,0,57,57,58],
[55,46,56,47,58,48,51,59,44,0,48,42],
[44,42,55,52,62,57,56,56,44,53,0,53],
[50,49,53,50,63,62,49,53,43,59,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 117, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,40,41,48,47,32,39,55,50,51,50],
[57,0,57,58,54,55,44,49,62,55,56,52],
[61,44,0,48,57,57,48,45,56,59,48,54],
[60,43,53,0,53,65,47,53,58,54,48,50],
[53,47,44,48,0,55,43,45,58,49,53,46],
[54,46,44,36,46,0,45,49,51,52,47,45],
[69,57,53,54,58,56,0,45,68,60,44,44],
[62,52,56,48,56,52,56,0,62,56,55,49],
[46,39,45,43,43,50,33,39,0,51,43,46],
[51,46,42,47,52,49,41,45,50,0,47,45],
[50,45,53,53,48,54,57,46,58,54,0,42],
[51,49,47,51,55,56,57,52,55,56,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 118, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,56,41,45,40,79,51,55,43,48,75],
[67,0,40,32,53,44,61,36,37,57,48,68],
[45,61,0,32,61,44,63,49,52,45,46,73],
[60,69,69,0,63,62,57,52,41,73,66,64],
[56,48,40,38,0,33,44,46,25,46,63,45],
[61,57,57,39,68,0,69,54,51,45,55,69],
[22,40,38,44,57,32,0,42,1,40,62,34],
[50,65,52,49,55,47,59,0,46,47,57,66],
[46,64,49,60,76,50,100,55,0,46,65,73],
[58,44,56,28,55,56,61,54,55,0,66,60],
[53,53,55,35,38,46,39,44,36,35,0,41],
[26,33,28,37,56,32,67,35,28,41,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 119, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,61,44,50,41,50,46,44,42,45,50],
[48,0,51,44,41,40,43,52,33,34,40,41],
[40,50,0,36,48,37,47,42,32,28,43,37],
[57,57,65,0,60,43,51,53,45,30,46,57],
[51,60,53,41,0,38,47,55,40,34,46,50],
[60,61,64,58,63,0,61,64,45,50,57,54],
[51,58,54,50,54,40,0,49,52,39,50,51],
[55,49,59,48,46,37,52,0,40,43,48,46],
[57,68,69,56,61,56,49,61,0,57,51,59],
[59,67,73,71,67,51,62,58,44,0,59,69],
[56,61,58,55,55,44,51,53,50,42,0,46],
[51,60,64,44,51,47,50,55,42,32,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 120, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,45,51,53,50,53,51,45,53,57,49],
[54,0,54,56,47,59,48,52,43,55,54,43],
[56,47,0,60,55,55,45,60,52,52,51,50],
[50,45,41,0,51,52,49,55,40,50,45,47],
[48,54,46,50,0,55,47,54,45,43,53,46],
[51,42,46,49,46,0,38,49,39,55,42,44],
[48,53,56,52,54,63,0,53,46,58,54,51],
[50,49,41,46,47,52,48,0,47,42,48,49],
[56,58,49,61,56,62,55,54,0,58,55,47],
[48,46,49,51,58,46,43,59,43,0,47,41],
[44,47,50,56,48,59,47,53,46,54,0,48],
[52,58,51,54,55,57,50,52,54,60,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 121, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,72,48,60,50,50,41,65,43,50,54,49],
[29,0,28,50,35,21,27,32,43,25,28,37],
[53,73,0,61,55,52,53,51,67,37,67,52],
[41,51,40,0,53,40,34,49,70,44,34,62],
[51,66,46,48,0,41,38,58,69,48,54,65],
[51,80,49,61,60,0,44,55,59,44,55,54],
[60,74,48,67,63,57,0,77,72,56,68,64],
[36,69,50,52,43,46,24,0,41,28,51,42],
[58,58,34,31,32,42,29,60,0,44,41,46],
[51,76,64,57,53,57,45,73,57,0,61,65],
[47,73,34,67,47,46,33,50,60,40,0,58],
[52,64,49,39,36,47,37,59,55,36,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 122, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,50,62,60,58,61,53,59,64,49,59],
[54,0,57,61,56,58,59,50,51,57,50,51],
[51,44,0,52,56,57,57,49,48,48,48,47],
[39,40,49,0,51,44,51,44,51,45,45,48],
[41,45,45,50,0,50,48,49,49,48,48,52],
[43,43,44,57,51,0,45,43,62,49,44,52],
[40,42,44,50,53,56,0,48,44,53,58,50],
[48,51,52,57,52,58,53,0,51,56,53,52],
[42,50,53,50,52,39,57,50,0,53,53,45],
[37,44,53,56,53,52,48,45,48,0,45,49],
[52,51,53,56,53,57,43,48,48,56,0,47],
[42,50,54,53,49,49,51,49,56,52,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 123, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,39,34,40,29,34,43,66,48,58,39],
[71,0,77,62,64,51,42,69,58,63,75,67],
[62,24,0,31,44,28,53,54,62,57,65,48],
[67,39,70,0,37,43,51,59,76,59,75,41],
[61,37,57,64,0,42,36,62,65,61,73,56],
[72,50,73,58,59,0,73,62,72,72,80,71],
[67,59,48,50,65,28,0,50,56,64,73,45],
[58,32,47,42,39,39,51,0,64,56,72,55],
[35,43,39,25,36,29,45,37,0,28,47,33],
[53,38,44,42,40,29,37,45,73,0,51,41],
[43,26,36,26,28,21,28,29,54,50,0,26],
[62,34,53,60,45,30,56,46,68,60,75,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 124, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,45,64,37,42,51,42,60,53,41,53],
[46,0,38,64,38,47,47,37,60,47,51,35],
[56,63,0,53,47,42,52,34,58,47,39,48],
[37,37,48,0,41,35,38,23,50,47,41,47],
[64,63,54,60,0,47,54,43,55,67,55,53],
[59,54,59,66,54,0,57,54,71,57,46,51],
[50,54,49,63,47,44,0,33,68,51,52,51],
[59,64,67,78,58,47,68,0,69,68,58,65],
[41,41,43,51,46,30,33,32,0,43,43,41],
[48,54,54,54,34,44,50,33,58,0,38,44],
[60,50,62,60,46,55,49,43,58,63,0,39],
[48,66,53,54,48,50,50,36,60,57,62,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 125, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,48,51,55,44,51,52,39,40,51,50],
[49,0,46,51,54,42,48,49,47,41,51,45],
[53,55,0,51,55,55,53,54,56,45,64,44],
[50,50,50,0,56,56,51,61,50,41,57,49],
[46,47,46,45,0,48,42,53,44,42,56,47],
[57,59,46,45,53,0,53,49,45,41,53,55],
[50,53,48,50,59,48,0,58,53,43,68,49],
[49,52,47,40,48,52,43,0,47,39,60,41],
[62,54,45,51,57,56,48,54,0,49,58,50],
[61,60,56,60,59,60,58,62,52,0,63,50],
[50,50,37,44,45,48,33,41,43,38,0,42],
[51,56,57,52,54,46,52,60,51,51,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 126, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,46,46,42,42,48,51,49,52,45,51],
[61,0,49,52,55,54,56,49,48,63,53,48],
[55,52,0,50,52,52,53,49,58,65,48,47],
[55,49,51,0,50,46,57,55,51,55,52,53],
[59,46,49,51,0,54,56,50,57,59,52,54],
[59,47,49,55,47,0,54,53,50,53,51,52],
[53,45,48,44,45,47,0,49,52,50,46,51],
[50,52,52,46,51,48,52,0,51,56,52,45],
[52,53,43,50,44,51,49,50,0,58,48,41],
[49,38,36,46,42,48,51,45,43,0,43,37],
[56,48,53,49,49,50,55,49,53,58,0,53],
[50,53,54,48,47,49,50,56,60,64,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 127, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,53,48,54,55,47,47,48,45,43,55],
[49,0,50,48,43,47,48,41,42,44,46,46],
[48,51,0,51,47,57,50,48,50,51,48,57],
[53,53,50,0,44,48,51,49,54,55,50,53],
[47,58,54,57,0,48,50,53,57,53,50,53],
[46,54,44,53,53,0,51,45,47,50,50,48],
[54,53,51,50,51,50,0,50,43,53,50,45],
[54,60,53,52,48,56,51,0,53,48,46,52],
[53,59,51,47,44,54,58,48,0,51,51,47],
[56,57,50,46,48,51,48,53,50,0,40,48],
[58,55,53,51,51,51,51,55,50,61,0,45],
[46,55,44,48,48,53,56,49,54,53,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 128, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,51,50,42,54,52,49,51,48,56,51],
[41,0,46,35,41,51,40,38,36,42,49,40],
[50,55,0,44,42,60,41,51,39,49,55,44],
[51,66,57,0,60,60,56,55,50,56,56,55],
[59,60,59,41,0,61,48,53,46,51,67,59],
[47,50,41,41,40,0,46,50,43,43,47,43],
[49,61,60,45,53,55,0,47,35,56,55,52],
[52,63,50,46,48,51,54,0,44,52,53,51],
[50,65,62,51,55,58,66,57,0,52,61,56],
[53,59,52,45,50,58,45,49,49,0,52,51],
[45,52,46,45,34,54,46,48,40,49,0,47],
[50,61,57,46,42,58,49,50,45,50,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 129, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,98,57,78,12,23,49,69,28,80,89,57],
[3,0,29,48,0,23,49,23,0,52,52,45],
[44,72,0,72,44,44,23,44,53,73,44,37],
[23,53,29,0,0,23,49,41,20,52,23,45],
[89,101,57,101,0,60,68,60,48,89,89,57],
[78,78,57,78,41,0,49,69,28,81,89,57],
[52,52,78,52,33,52,0,52,49,81,72,49],
[32,78,57,60,41,32,49,0,12,44,52,57],
[73,101,48,81,53,73,52,89,0,73,89,69],
[21,49,28,49,12,20,20,57,28,0,60,28],
[12,49,57,78,12,12,29,49,12,41,0,57],
[44,56,64,56,44,44,52,44,32,73,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 130, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,41,57,49,40,58,52,51,51,47,42],
[56,0,43,59,52,48,53,53,53,49,53,53],
[60,58,0,61,49,46,53,51,51,49,56,51],
[44,42,40,0,42,38,48,48,43,38,42,40],
[52,49,52,59,0,52,52,66,54,53,54,55],
[61,53,55,63,49,0,60,58,58,54,51,55],
[43,48,48,53,49,41,0,55,47,43,47,50],
[49,48,50,53,35,43,46,0,50,46,40,40],
[50,48,50,58,47,43,54,51,0,52,50,54],
[50,52,52,63,48,47,58,55,49,0,52,52],
[54,48,45,59,47,50,54,61,51,49,0,50],
[59,48,50,61,46,46,51,61,47,49,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 131, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,43,60,60,60,43,36,59,44,44,60],
[42,0,77,101,101,101,84,77,101,77,77,101],
[58,24,0,70,35,60,69,1,60,27,44,35],
[41,0,31,0,34,59,41,0,16,31,1,25],
[41,0,66,67,0,59,76,67,35,32,36,60],
[41,0,41,42,42,0,41,32,10,42,1,50],
[58,17,32,60,25,60,0,1,25,32,1,25],
[65,24,100,101,34,69,100,0,69,65,54,70],
[42,0,41,85,66,91,76,32,0,42,36,66],
[57,24,74,70,69,59,69,36,59,0,44,70],
[57,24,57,100,65,100,100,47,65,57,0,66],
[41,0,66,76,41,51,76,31,35,31,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 132, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,48,61,51,52,45,59,52,55,54,55],
[49,0,43,58,49,52,46,51,51,52,50,47],
[53,58,0,60,57,58,57,58,47,55,59,59],
[40,43,41,0,42,42,45,52,40,47,45,46],
[50,52,44,59,0,53,50,55,47,50,53,53],
[49,49,43,59,48,0,41,53,49,50,43,54],
[56,55,44,56,51,60,0,62,45,57,58,50],
[42,50,43,49,46,48,39,0,45,46,51,51],
[49,50,54,61,54,52,56,56,0,58,57,55],
[46,49,46,54,51,51,44,55,43,0,45,46],
[47,51,42,56,48,58,43,50,44,56,0,51],
[46,54,42,55,48,47,51,50,46,55,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 133, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,42,46,49,40,40,46,48,47,42,43],
[45,0,38,51,56,49,46,46,51,45,45,43],
[59,63,0,56,60,55,50,66,58,61,49,54],
[55,50,45,0,48,47,48,49,47,51,53,53],
[52,45,41,53,0,51,51,48,45,49,45,45],
[61,52,46,54,50,0,53,51,58,51,41,47],
[61,55,51,53,50,48,0,57,53,46,47,53],
[55,55,35,52,53,50,44,0,51,49,43,47],
[53,50,43,54,56,43,48,50,0,48,46,52],
[54,56,40,50,52,50,55,52,53,0,51,54],
[59,56,52,48,56,60,54,58,55,50,0,64],
[58,58,47,48,56,54,48,54,49,47,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 134, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,48,59,91,76,31,72,23,57,36,64],
[67,0,55,62,77,47,36,64,31,52,39,51],
[53,46,0,75,80,54,36,69,53,54,46,61],
[42,39,26,0,64,52,33,35,22,39,9,27],
[10,24,21,37,0,41,23,41,13,39,19,18],
[25,54,47,49,60,0,25,56,33,41,15,25],
[70,65,65,68,78,76,0,71,43,81,39,60],
[29,37,32,66,60,45,30,0,16,37,13,46],
[78,70,48,79,88,68,58,85,0,70,56,85],
[44,49,47,62,62,60,20,64,31,0,28,29],
[65,62,55,92,82,86,62,88,45,73,0,70],
[37,50,40,74,83,76,41,55,16,72,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 135, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,20,25,12,33,26,25,21,50,11,34],
[72,0,50,46,33,38,44,37,52,65,33,57],
[81,51,0,45,49,48,41,38,45,70,37,61],
[76,55,56,0,41,47,42,38,47,63,43,62],
[89,68,52,60,0,63,51,67,49,72,58,58],
[68,63,53,54,38,0,24,22,37,50,28,49],
[75,57,60,59,50,77,0,60,52,53,47,59],
[76,64,63,63,34,79,41,0,40,71,55,64],
[80,49,56,54,52,64,49,61,0,69,41,51],
[51,36,31,38,29,51,48,30,32,0,24,55],
[90,68,64,58,43,73,54,46,60,77,0,52],
[67,44,40,39,43,52,42,37,50,46,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 136, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,44,51,47,55,45,52,51,58,50,51],
[48,0,42,46,38,52,42,53,40,58,47,45],
[57,59,0,54,50,46,51,58,49,55,50,54],
[50,55,47,0,46,58,46,55,54,50,52,50],
[54,63,51,55,0,62,48,54,55,59,52,54],
[46,49,55,43,39,0,41,50,38,55,45,43],
[56,59,50,55,53,60,0,55,55,56,53,60],
[49,48,43,46,47,51,46,0,39,50,40,53],
[50,61,52,47,46,63,46,62,0,54,48,57],
[43,43,46,51,42,46,45,51,47,0,46,45],
[51,54,51,49,49,56,48,61,53,55,0,52],
[50,56,47,51,47,58,41,48,44,56,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 137, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,51,52,59,61,54,55,57,45,50,56],
[42,0,50,47,58,55,49,59,54,42,49,54],
[50,51,0,49,61,53,47,60,59,47,52,50],
[49,54,52,0,53,46,61,68,54,52,54,61],
[42,43,40,48,0,51,48,47,51,40,48,53],
[40,46,48,55,50,0,44,50,49,39,46,57],
[47,52,54,40,53,57,0,61,56,55,54,48],
[46,42,41,33,54,51,40,0,48,33,45,49],
[44,47,42,47,50,52,45,53,0,40,44,51],
[56,59,54,49,61,62,46,68,61,0,59,56],
[51,52,49,47,53,55,47,56,57,42,0,53],
[45,47,51,40,48,44,53,52,50,45,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 138, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,47,26,33,22,50,45,51,48,45,50],
[73,0,67,47,65,71,57,63,58,44,67,58],
[54,34,0,34,53,59,67,47,61,61,64,64],
[75,54,67,0,49,53,67,73,78,54,94,71],
[68,36,48,52,0,66,63,64,57,54,81,78],
[79,30,42,48,35,0,47,69,58,47,57,58],
[51,44,34,34,38,54,0,36,47,32,44,63],
[56,38,54,28,37,32,65,0,46,50,33,65],
[50,43,40,23,44,43,54,55,0,49,35,56],
[53,57,40,47,47,54,69,51,52,0,61,69],
[56,34,37,7,20,44,57,68,66,40,0,73],
[51,43,37,30,23,43,38,36,45,32,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 139, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,48,37,48,53,53,52,41,45,45,53],
[56,0,56,51,55,59,54,49,47,51,39,51],
[53,45,0,45,50,47,53,44,56,52,44,43],
[64,50,56,0,60,56,65,59,64,54,53,57],
[53,46,51,41,0,58,53,51,47,47,40,56],
[48,42,54,45,43,0,44,45,42,47,43,47],
[48,47,48,36,48,57,0,46,53,52,39,52],
[49,52,57,42,50,56,55,0,51,43,49,56],
[60,54,45,37,54,59,48,50,0,51,44,55],
[56,50,49,47,54,54,49,58,50,0,42,55],
[56,62,57,48,61,58,62,52,57,59,0,58],
[48,50,58,44,45,54,49,45,46,46,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 140, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,57,53,53,53,55,58,60,44,50,57],
[42,0,45,42,45,41,50,56,45,47,44,40],
[44,56,0,48,56,44,51,59,63,51,58,52],
[48,59,53,0,56,48,43,66,58,43,53,49],
[48,56,45,45,0,36,51,50,54,40,50,50],
[48,60,57,53,65,0,53,53,55,51,53,53],
[46,51,50,58,50,48,0,54,57,44,48,44],
[43,45,42,35,51,48,47,0,49,45,48,46],
[41,56,38,43,47,46,44,52,0,35,54,42],
[57,54,50,58,61,50,57,56,66,0,65,50],
[51,57,43,48,51,48,53,53,47,36,0,46],
[44,61,49,52,51,48,57,55,59,51,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 141, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,56,47,60,56,51,53,46,54,51,49],
[52,0,52,49,57,49,43,57,52,55,53,55],
[45,49,0,46,54,48,44,49,46,51,50,51],
[54,52,55,0,57,58,55,50,46,49,56,49],
[41,44,47,44,0,50,43,50,40,50,45,41],
[45,52,53,43,51,0,47,46,35,56,55,51],
[50,58,57,46,58,54,0,59,46,59,54,55],
[48,44,52,51,51,55,42,0,51,52,49,52],
[55,49,55,55,61,66,55,50,0,61,58,53],
[47,46,50,52,51,45,42,49,40,0,44,50],
[50,48,51,45,56,46,47,52,43,57,0,49],
[52,46,50,52,60,50,46,49,48,51,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 142, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,49,43,44,51,41,48,50,59,46,48],
[57,0,52,51,50,58,49,52,54,52,55,57],
[52,49,0,47,43,57,58,44,47,55,52,53],
[58,50,54,0,47,54,54,53,56,55,47,60],
[57,51,58,54,0,65,43,56,55,59,52,65],
[50,43,44,47,36,0,44,42,41,44,50,53],
[60,52,43,47,58,57,0,51,53,61,62,55],
[53,49,57,48,45,59,50,0,54,58,57,60],
[51,47,54,45,46,60,48,47,0,50,56,52],
[42,49,46,46,42,57,40,43,51,0,42,52],
[55,46,49,54,49,51,39,44,45,59,0,55],
[53,44,48,41,36,48,46,41,49,49,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 143, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,68,35,63,63,40,64,52,58,79,47,33],
[33,0,38,38,54,50,44,44,38,50,38,38],
[66,63,0,67,77,81,83,43,47,59,47,71],
[38,63,34,0,59,39,66,47,47,44,41,42],
[38,47,24,42,0,10,28,33,46,30,29,28],
[61,51,20,62,91,0,47,33,42,56,33,51],
[37,57,18,35,73,54,0,33,47,47,41,46],
[49,57,58,54,68,68,68,0,34,53,44,62],
[43,63,54,54,55,59,54,67,0,54,43,49],
[22,51,42,57,71,45,54,48,47,0,41,55],
[54,63,54,60,72,68,60,57,58,60,0,42],
[68,63,30,59,73,50,55,39,52,46,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 144, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,56,48,45,50,48,38,44,53,44,43],
[56,0,55,51,51,52,48,53,50,53,51,53],
[45,46,0,45,59,55,49,45,54,54,56,50],
[53,50,56,0,62,57,45,43,57,57,52,53],
[56,50,42,39,0,60,48,46,62,52,40,50],
[51,49,46,44,41,0,49,42,52,54,48,45],
[53,53,52,56,53,52,0,46,50,69,50,56],
[63,48,56,58,55,59,55,0,50,59,54,58],
[57,51,47,44,39,49,51,51,0,59,40,42],
[48,48,47,44,49,47,32,42,42,0,45,39],
[57,50,45,49,61,53,51,47,61,56,0,51],
[58,48,51,48,51,56,45,43,59,62,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 145, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,47,51,49,61,48,51,51,54,47,45],
[49,0,37,49,36,55,38,45,44,66,41,45],
[54,64,0,64,52,58,45,58,55,57,61,45],
[50,52,37,0,40,52,46,50,49,49,48,38],
[52,65,49,61,0,65,63,64,58,56,55,57],
[40,46,43,49,36,0,44,53,45,53,53,51],
[53,63,56,55,38,57,0,56,48,56,52,50],
[50,56,43,51,37,48,45,0,41,59,46,45],
[50,57,46,52,43,56,53,60,0,57,51,57],
[47,35,44,52,45,48,45,42,44,0,40,43],
[54,60,40,53,46,48,49,55,50,61,0,58],
[56,56,56,63,44,50,51,56,44,58,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 146, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,48,57,42,43,39,49,53,38,51,50],
[48,0,51,58,52,56,44,62,65,55,51,63],
[53,50,0,50,47,42,47,54,60,40,59,49],
[44,43,51,0,45,46,48,50,53,32,57,50],
[59,49,54,56,0,48,38,58,57,47,57,50],
[58,45,59,55,53,0,47,44,54,45,51,56],
[62,57,54,53,63,54,0,59,55,49,59,62],
[52,39,47,51,43,57,42,0,46,49,50,56],
[48,36,41,48,44,47,46,55,0,45,49,49],
[63,46,61,69,54,56,52,52,56,0,65,62],
[50,50,42,44,44,50,42,51,52,36,0,60],
[51,38,52,51,51,45,39,45,52,39,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 147, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,57,65,66,51,60,54,59,50,57,60],
[47,0,58,63,57,46,61,51,67,53,49,60],
[44,43,0,52,55,47,56,50,55,50,54,58],
[36,38,49,0,52,46,50,42,38,48,42,48],
[35,44,46,49,0,39,49,50,48,51,47,51],
[50,55,54,55,62,0,66,63,58,54,58,61],
[41,40,45,51,52,35,0,42,47,50,41,59],
[47,50,51,59,51,38,59,0,62,51,61,57],
[42,34,46,63,53,43,54,39,0,49,45,52],
[51,48,51,53,50,47,51,50,52,0,55,59],
[44,52,47,59,54,43,60,40,56,46,0,54],
[41,41,43,53,50,40,42,44,49,42,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 148, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,64,66,70,66,55,59,66,50,57,55],
[48,0,48,65,57,56,44,57,66,52,49,47],
[37,53,0,53,56,52,40,49,50,48,39,48],
[35,36,48,0,42,55,39,38,43,53,43,38],
[31,44,45,59,0,44,42,48,57,48,36,37],
[35,45,49,46,57,0,39,46,59,42,43,48],
[46,57,61,62,59,62,0,57,64,58,58,51],
[42,44,52,63,53,55,44,0,52,50,49,48],
[35,35,51,58,44,42,37,49,0,35,41,40],
[51,49,53,48,53,59,43,51,66,0,50,38],
[44,52,62,58,65,58,43,52,60,51,0,51],
[46,54,53,63,64,53,50,53,61,63,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 149, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,66,52,65,61,53,55,60,61,53,43],
[52,0,50,51,44,57,59,54,58,58,44,40],
[35,51,0,61,46,52,50,49,61,61,57,46],
[49,50,40,0,49,52,57,59,57,63,38,40],
[36,57,55,52,0,46,48,55,54,64,47,41],
[40,44,49,49,55,0,58,57,57,61,39,50],
[48,42,51,44,53,43,0,48,54,59,41,45],
[46,47,52,42,46,44,53,0,51,59,49,43],
[41,43,40,44,47,44,47,50,0,52,37,44],
[40,43,40,38,37,40,42,42,49,0,37,39],
[48,57,44,63,54,62,60,52,64,64,0,51],
[58,61,55,61,60,51,56,58,57,62,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 150, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,50,62,57,57,52,52,47,65,48,54],
[51,0,44,63,58,52,47,50,45,57,50,53],
[51,57,0,58,62,52,52,52,48,60,49,45],
[39,38,43,0,53,53,42,43,41,43,42,39],
[44,43,39,48,0,49,43,45,38,48,48,36],
[44,49,49,48,52,0,44,47,42,46,42,46],
[49,54,49,59,58,57,0,52,51,62,58,52],
[49,51,49,58,56,54,49,0,51,59,53,58],
[54,56,53,60,63,59,50,50,0,60,57,51],
[36,44,41,58,53,55,39,42,41,0,49,42],
[53,51,52,59,53,59,43,48,44,52,0,54],
[47,48,56,62,65,55,49,43,50,59,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 151, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,47,40,40,41,55,51,51,43,50,45],
[65,0,50,51,51,47,55,51,59,53,61,57],
[54,51,0,42,44,45,54,47,44,49,52,51],
[61,50,59,0,62,58,61,56,52,56,60,53],
[61,50,57,39,0,55,57,49,46,45,52,50],
[60,54,56,43,46,0,54,53,43,53,56,52],
[46,46,47,40,44,47,0,50,49,47,55,45],
[50,50,54,45,52,48,51,0,50,44,51,49],
[50,42,57,49,55,58,52,51,0,49,53,59],
[58,48,52,45,56,48,54,57,52,0,61,50],
[51,40,49,41,49,45,46,50,48,40,0,53],
[56,44,50,48,51,49,56,52,42,51,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 152, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,38,62,39,38,51,41,45,45,41,49],
[48,0,44,57,50,48,55,45,54,56,42,57],
[63,57,0,64,47,46,62,53,52,51,51,58],
[39,44,37,0,36,40,56,47,44,44,49,42],
[62,51,54,65,0,54,64,53,58,60,49,59],
[63,53,55,61,47,0,57,49,59,53,49,53],
[50,46,39,45,37,44,0,39,47,41,48,44],
[60,56,48,54,48,52,62,0,46,56,60,48],
[56,47,49,57,43,42,54,55,0,61,41,54],
[56,45,50,57,41,48,60,45,40,0,43,50],
[60,59,50,52,52,52,53,41,60,58,0,54],
[52,44,43,59,42,48,57,53,47,51,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 153, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,57,36,59,34,58,58,53,54,61,55],
[46,0,58,56,62,51,56,50,48,56,55,53],
[44,43,0,45,54,44,45,47,47,45,48,52],
[65,45,56,0,60,53,58,60,59,64,67,56],
[42,39,47,41,0,43,41,50,46,41,45,45],
[67,50,57,48,58,0,66,55,55,61,61,63],
[43,45,56,43,60,35,0,47,58,57,48,62],
[43,51,54,41,51,46,54,0,47,46,54,50],
[48,53,54,42,55,46,43,54,0,48,51,48],
[47,45,56,37,60,40,44,55,53,0,57,54],
[40,46,53,34,56,40,53,47,50,44,0,43],
[46,48,49,45,56,38,39,51,53,47,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 154, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,44,49,44,54,48,53,53,56,54,42],
[48,0,46,56,47,60,52,51,55,50,56,46],
[57,55,0,61,48,59,54,52,54,56,53,46],
[52,45,40,0,40,55,45,48,47,53,52,41],
[57,54,53,61,0,60,49,54,56,58,59,45],
[47,41,42,46,41,0,42,44,47,49,41,41],
[53,49,47,56,52,59,0,50,51,58,55,52],
[48,50,49,53,47,57,51,0,51,47,55,47],
[48,46,47,54,45,54,50,50,0,55,57,48],
[45,51,45,48,43,52,43,54,46,0,48,47],
[47,45,48,49,42,60,46,46,44,53,0,44],
[59,55,55,60,56,60,49,54,53,54,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 155, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,55,34,45,51,43,48,56,43,44,29],
[59,0,68,55,64,61,51,55,43,68,47,56],
[46,33,0,28,31,69,50,45,42,53,46,33],
[67,46,73,0,72,59,44,52,45,60,64,47],
[56,37,70,29,0,66,52,47,50,59,46,44],
[50,40,32,42,35,0,38,43,46,48,52,36],
[58,50,51,57,49,63,0,53,49,67,51,54],
[53,46,56,49,54,58,48,0,57,69,55,44],
[45,58,59,56,51,55,52,44,0,59,54,58],
[58,33,48,41,42,53,34,32,42,0,39,32],
[57,54,55,37,55,49,50,46,47,62,0,53],
[72,45,68,54,57,65,47,57,43,69,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 156, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,47,46,45,50,46,57,43,48,50,44],
[52,0,51,54,52,56,54,58,46,48,54,40],
[54,50,0,50,47,53,52,60,48,47,52,42],
[55,47,51,0,42,51,55,48,51,45,50,43],
[56,49,54,59,0,54,54,55,52,51,50,51],
[51,45,48,50,47,0,51,53,43,50,51,41],
[55,47,49,46,47,50,0,52,48,52,51,42],
[44,43,41,53,46,48,49,0,43,44,51,39],
[58,55,53,50,49,58,53,58,0,51,54,50],
[53,53,54,56,50,51,49,57,50,0,56,42],
[51,47,49,51,51,50,50,50,47,45,0,37],
[57,61,59,58,50,60,59,62,51,59,64,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 157, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,58,64,64,58,53,52,58,59,49,61],
[40,0,51,55,50,46,52,43,54,59,44,30],
[43,50,0,51,33,46,36,48,53,56,39,40],
[37,46,50,0,51,39,31,43,54,61,47,51],
[37,51,68,50,0,46,39,46,56,50,43,47],
[43,55,55,62,55,0,41,46,59,59,57,43],
[48,49,65,70,62,60,0,56,73,55,63,57],
[49,58,53,58,55,55,45,0,55,46,40,55],
[43,47,48,47,45,42,28,46,0,48,47,28],
[42,42,45,40,51,42,46,55,53,0,40,46],
[52,57,62,54,58,44,38,61,54,61,0,53],
[40,71,61,50,54,58,44,46,73,55,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 158, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,48,61,45,62,58,48,45,41,64,44],
[43,0,30,55,41,51,29,46,45,35,46,48],
[53,71,0,63,48,55,45,56,53,53,63,59],
[40,46,38,0,55,48,31,31,38,22,48,33],
[56,60,53,46,0,51,40,48,41,51,36,45],
[39,50,46,53,50,0,34,42,41,48,45,42],
[43,72,56,70,61,67,0,61,57,61,62,57],
[53,55,45,70,53,59,40,0,34,43,56,41],
[56,56,48,63,60,60,44,67,0,54,56,57],
[60,66,48,79,50,53,40,58,47,0,59,52],
[37,55,38,53,65,56,39,45,45,42,0,46],
[57,53,42,68,56,59,44,60,44,49,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 159, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,40,48,54,46,56,49,46,58,58,51],
[53,0,41,55,47,52,55,52,46,57,53,48],
[61,60,0,60,57,55,61,47,51,61,69,53],
[53,46,41,0,53,53,58,53,51,57,64,50],
[47,54,44,48,0,48,56,43,51,53,62,47],
[55,49,46,48,53,0,56,48,47,55,60,44],
[45,46,40,43,45,45,0,42,41,44,57,43],
[52,49,54,48,58,53,59,0,55,61,64,56],
[55,55,50,50,50,54,60,46,0,54,62,47],
[43,44,40,44,48,46,57,40,47,0,59,47],
[43,48,32,37,39,41,44,37,39,42,0,41],
[50,53,48,51,54,57,58,45,54,54,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 160, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,53,61,46,48,25,51,46,38,43,42],
[59,0,57,72,54,61,47,61,57,56,49,53],
[48,44,0,57,42,52,50,57,38,39,46,40],
[40,29,44,0,36,41,35,47,35,24,37,31],
[55,47,59,65,0,45,52,62,42,47,54,49],
[53,40,49,60,56,0,49,47,46,37,50,40],
[76,54,51,66,49,52,0,60,45,49,45,47],
[50,40,44,54,39,54,41,0,46,33,46,43],
[55,44,63,66,59,55,56,55,0,51,62,51],
[63,45,62,77,54,64,52,68,50,0,50,59],
[58,52,55,64,47,51,56,55,39,51,0,52],
[59,48,61,70,52,61,54,58,50,42,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 161, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,83,47,64,64,56,47,84,42,65,65,66],
[18,0,43,0,44,53,61,54,25,48,37,44],
[54,58,0,35,47,54,48,41,25,58,54,44],
[37,101,66,0,84,89,84,84,61,48,54,62],
[37,57,54,17,0,54,57,54,53,57,36,36],
[45,48,47,12,47,0,65,66,25,48,66,48],
[54,40,53,17,44,36,0,71,53,57,36,53],
[17,47,60,17,47,35,30,0,25,48,17,25],
[59,76,76,40,48,76,48,76,0,59,59,58],
[36,53,43,53,44,53,44,53,42,0,18,43],
[36,64,47,47,65,35,65,84,42,83,0,47],
[35,57,57,39,65,53,48,76,43,58,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 162, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,45,66,41,38,62,58,58,49,49,33],
[42,0,41,53,49,51,49,63,36,51,56,41],
[56,60,0,65,49,48,65,72,45,47,65,50],
[35,48,36,0,45,48,53,46,47,36,44,36],
[60,52,52,56,0,46,66,60,51,53,62,42],
[63,50,53,53,55,0,51,52,42,55,63,52],
[39,52,36,48,35,50,0,46,41,45,53,40],
[43,38,29,55,41,49,55,0,46,43,50,48],
[43,65,56,54,50,59,60,55,0,53,64,34],
[52,50,54,65,48,46,56,58,48,0,65,46],
[52,45,36,57,39,38,48,51,37,36,0,49],
[68,60,51,65,59,49,61,53,67,55,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 163, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,65,47,54,61,56,58,68,63,55,63,45],
[36,0,41,30,45,34,43,51,49,45,45,35],
[54,60,0,44,56,51,51,63,57,52,50,45],
[47,71,57,0,66,48,56,69,61,65,67,54],
[40,56,45,35,0,40,48,57,52,47,44,50],
[45,67,50,53,61,0,64,69,56,56,65,54],
[43,58,50,45,53,37,0,61,49,58,57,45],
[33,50,38,32,44,32,40,0,44,38,38,40],
[38,52,44,40,49,45,52,57,0,48,43,57],
[46,56,49,36,54,45,43,63,53,0,54,47],
[38,56,51,34,57,36,44,63,58,47,0,50],
[56,66,56,47,51,47,56,61,44,54,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 164, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,49,53,58,43,50,51,58,41,47,42],
[51,0,57,40,57,47,40,59,59,34,44,46],
[52,44,0,47,68,58,54,54,60,51,41,50],
[48,61,54,0,54,59,63,54,67,49,54,51],
[43,44,33,47,0,41,41,46,40,30,28,38],
[58,54,43,42,60,0,49,54,44,45,51,48],
[51,61,47,38,60,52,0,52,59,48,48,38],
[50,42,47,47,55,47,49,0,59,35,41,44],
[43,42,41,34,61,57,42,42,0,49,47,42],
[60,67,50,52,71,56,53,66,52,0,54,45],
[54,57,60,47,73,50,53,60,54,47,0,40],
[59,55,51,50,63,53,63,57,59,56,61,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 165, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,66,49,59,55,61,53,49,52,53,48],
[50,0,60,52,52,57,55,54,52,46,53,44],
[35,41,0,45,44,42,45,51,42,38,40,45],
[52,49,56,0,50,51,58,61,43,48,50,43],
[42,49,57,51,0,55,55,53,49,41,44,48],
[46,44,59,50,46,0,50,51,43,46,43,49],
[40,46,56,43,46,51,0,55,42,46,47,44],
[48,47,50,40,48,50,46,0,47,46,49,43],
[52,49,59,58,52,58,59,54,0,47,47,51],
[49,55,63,53,60,55,55,55,54,0,55,48],
[48,48,61,51,57,58,54,52,54,46,0,49],
[53,57,56,58,53,52,57,58,50,53,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 166, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,52,47,46,41,43,43,52,42,40,40],
[57,0,54,52,47,46,57,58,53,53,53,50],
[49,47,0,53,51,54,55,54,53,44,50,42],
[54,49,48,0,46,51,49,49,45,52,46,44],
[55,54,50,55,0,57,53,56,61,50,53,45],
[60,55,47,50,44,0,50,52,53,46,50,42],
[58,44,46,52,48,51,0,52,51,49,50,44],
[58,43,47,52,45,49,49,0,57,50,52,44],
[49,48,48,56,40,48,50,44,0,51,50,38],
[59,48,57,49,51,55,52,51,50,0,48,49],
[61,48,51,55,48,51,51,49,51,53,0,51],
[61,51,59,57,56,59,57,57,63,52,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 167, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,71,49,47,62,60,54,66,63,57,63],
[54,0,65,48,60,54,64,69,65,52,62,60],
[30,36,0,43,38,52,46,39,51,41,47,53],
[52,53,58,0,51,49,63,48,72,50,53,70],
[54,41,63,50,0,46,65,65,54,56,67,45],
[39,47,49,52,55,0,60,46,56,44,47,63],
[41,37,55,38,36,41,0,40,62,34,43,37],
[47,32,62,53,36,55,61,0,55,50,59,61],
[35,36,50,29,47,45,39,46,0,46,49,48],
[38,49,60,51,45,57,67,51,55,0,50,60],
[44,39,54,48,34,54,58,42,52,51,0,52],
[38,41,48,31,56,38,64,40,53,41,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 168, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,42,56,45,44,38,46,54,42,45,47],
[51,0,43,58,49,50,48,50,53,48,56,45],
[59,58,0,55,52,52,52,51,49,51,56,52],
[45,43,46,0,42,46,43,44,44,39,41,41],
[56,52,49,59,0,52,45,54,52,52,55,51],
[57,51,49,55,49,0,44,50,51,50,54,52],
[63,53,49,58,56,57,0,56,58,54,60,52],
[55,51,50,57,47,51,45,0,50,51,55,48],
[47,48,52,57,49,50,43,51,0,44,48,48],
[59,53,50,62,49,51,47,50,57,0,55,48],
[56,45,45,60,46,47,41,46,53,46,0,46],
[54,56,49,60,50,49,49,53,53,53,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 169, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,46,53,51,52,58,49,49,46,50,51],
[47,0,51,45,53,47,54,50,39,46,50,46],
[55,50,0,50,50,49,55,53,48,47,48,52],
[48,56,51,0,55,48,52,55,47,44,44,46],
[50,48,51,46,0,49,46,55,48,40,40,46],
[49,54,52,53,52,0,49,54,45,48,43,43],
[43,47,46,49,55,52,0,52,50,46,42,51],
[52,51,48,46,46,47,49,0,42,44,45,51],
[52,62,53,54,53,56,51,59,0,50,53,48],
[55,55,54,57,61,53,55,57,51,0,50,53],
[51,51,53,57,61,58,59,56,48,51,0,52],
[50,55,49,55,55,58,50,50,53,48,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 170, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,43,51,66,63,51,51,68,49,58,76],
[42,0,46,53,56,59,53,56,46,61,61,59],
[58,55,0,55,53,65,46,62,54,65,58,67],
[50,48,46,0,51,66,40,53,57,47,55,46],
[35,45,48,50,0,44,43,42,50,50,55,47],
[38,42,36,35,57,0,33,49,45,55,49,47],
[50,48,55,61,58,68,0,68,51,59,61,63],
[50,45,39,48,59,52,33,0,39,56,54,48],
[33,55,47,44,51,56,50,62,0,59,68,53],
[52,40,36,54,51,46,42,45,42,0,48,50],
[43,40,43,46,46,52,40,47,33,53,0,37],
[25,42,34,55,54,54,38,53,48,51,64,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 171, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,61,55,58,52,46,64,64,53,65,57],
[46,0,52,42,57,53,52,60,59,46,42,62],
[40,49,0,48,50,43,44,52,54,34,39,48],
[46,59,53,0,54,59,48,53,66,45,56,57],
[43,44,51,47,0,56,52,58,56,45,51,53],
[49,48,58,42,45,0,51,56,67,41,55,67],
[55,49,57,53,49,50,0,59,58,59,49,55],
[37,41,49,48,43,45,42,0,58,41,53,63],
[37,42,47,35,45,34,43,43,0,31,60,43],
[48,55,67,56,56,60,42,60,70,0,55,79],
[36,59,62,45,50,46,52,48,41,46,0,49],
[44,39,53,44,48,34,46,38,58,22,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 172, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,58,62,52,45,52,52,46,50,57,45],
[65,0,64,59,51,50,62,53,45,49,60,55],
[43,37,0,43,38,38,33,52,37,32,50,39],
[39,42,58,0,46,49,46,47,47,49,60,47],
[49,50,63,55,0,57,55,56,51,51,54,52],
[56,51,63,52,44,0,59,57,52,48,61,57],
[49,39,68,55,46,42,0,54,48,47,52,45],
[49,48,49,54,45,44,47,0,46,40,52,51],
[55,56,64,54,50,49,53,55,0,54,55,57],
[51,52,69,52,50,53,54,61,47,0,65,57],
[44,41,51,41,47,40,49,49,46,36,0,44],
[56,46,62,54,49,44,56,50,44,44,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 173, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,43,60,44,39,53,56,42,61,55,46],
[45,0,36,50,48,42,42,49,27,46,48,29],
[58,65,0,57,49,47,55,58,51,48,53,47],
[41,51,44,0,42,46,47,48,27,42,49,31],
[57,53,52,59,0,38,51,60,44,46,48,46],
[62,59,54,55,63,0,44,59,34,62,54,43],
[48,59,46,54,50,57,0,61,30,45,57,43],
[45,52,43,53,41,42,40,0,30,52,43,40],
[59,74,50,74,57,67,71,71,0,58,59,56],
[40,55,53,59,55,39,56,49,43,0,49,41],
[46,53,48,52,53,47,44,58,42,52,0,41],
[55,72,54,70,55,58,58,61,45,60,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 174, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,41,49,42,47,53,54,53,56,68,56],
[52,0,51,60,44,49,49,67,54,59,52,64],
[60,50,0,63,52,53,56,57,50,63,70,67],
[52,41,38,0,52,55,61,54,56,53,50,50],
[59,57,49,49,0,50,61,55,53,59,44,64],
[54,52,48,46,51,0,48,57,52,52,59,58],
[48,52,45,40,40,53,0,47,50,46,46,52],
[47,34,44,47,46,44,54,0,55,47,42,52],
[48,47,51,45,48,49,51,46,0,44,44,51],
[45,42,38,48,42,49,55,54,57,0,47,57],
[33,49,31,51,57,42,55,59,57,54,0,53],
[45,37,34,51,37,43,49,49,50,44,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 175, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,73,67,56,16,92,72,64,60,72,81,85],
[28,0,70,62,32,48,46,59,34,70,62,62],
[34,31,0,1,18,34,35,31,34,43,34,48],
[45,39,100,0,21,61,65,66,65,74,50,62],
[85,69,83,80,0,80,67,67,48,80,90,85],
[9,53,67,40,21,0,56,64,61,53,53,40],
[29,55,66,36,34,45,0,45,31,43,34,59],
[37,42,70,35,34,37,56,0,47,59,50,56],
[41,67,67,36,53,40,70,54,0,85,67,54],
[29,31,58,27,21,48,58,42,16,0,50,46],
[20,39,67,51,11,48,67,51,34,51,0,54],
[16,39,53,39,16,61,42,45,47,55,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 176, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,52,53,52,54,58,52,52,51,48,50],
[51,0,53,50,53,53,46,48,42,43,47,46],
[49,48,0,48,54,51,55,43,47,49,50,48],
[48,51,53,0,50,53,57,50,44,46,52,53],
[49,48,47,51,0,50,52,46,41,47,45,45],
[47,48,50,48,51,0,49,47,37,43,49,46],
[43,55,46,44,49,52,0,46,38,47,50,51],
[49,53,58,51,55,54,55,0,46,53,48,50],
[49,59,54,57,60,64,63,55,0,58,51,52],
[50,58,52,55,54,58,54,48,43,0,50,50],
[53,54,51,49,56,52,51,53,50,51,0,52],
[51,55,53,48,56,55,50,51,49,51,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 177, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,49,59,48,41,60,46,49,58,49,45],
[70,0,64,61,57,56,53,59,52,66,58,48],
[52,37,0,64,61,39,51,51,56,68,48,41],
[42,40,37,0,51,35,42,46,59,52,43,44],
[53,44,40,50,0,34,49,46,48,46,44,37],
[60,45,62,66,67,0,50,58,59,66,52,50],
[41,48,50,59,52,51,0,47,55,64,52,48],
[55,42,50,55,55,43,54,0,51,59,41,51],
[52,49,45,42,53,42,46,50,0,60,38,48],
[43,35,33,49,55,35,37,42,41,0,42,39],
[52,43,53,58,57,49,49,60,63,59,0,51],
[56,53,60,57,64,51,53,50,53,62,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 178, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,71,51,68,48,62,47,62,61,44,56,51],
[30,0,31,54,41,47,41,41,45,31,44,38],
[50,70,0,56,47,53,53,58,65,52,56,53],
[33,47,45,0,45,31,40,46,44,35,40,34],
[53,60,54,56,0,48,61,55,54,46,46,38],
[39,54,48,70,53,0,59,55,56,50,59,42],
[54,60,48,61,40,42,0,49,57,43,64,39],
[39,60,43,55,46,46,52,0,56,51,53,52],
[40,56,36,57,47,45,44,45,0,30,47,40],
[57,70,49,66,55,51,58,50,71,0,61,49],
[45,57,45,61,55,42,37,48,54,40,0,32],
[50,63,48,67,63,59,62,49,61,52,69,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 179, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,60,55,50,58,51,55,44,60,47,59],
[52,0,50,47,36,47,46,60,34,37,45,46],
[41,51,0,38,29,50,38,60,44,57,38,33],
[46,54,63,0,52,46,52,67,43,48,42,49],
[51,65,72,49,0,52,58,80,54,57,42,61],
[43,54,51,55,49,0,45,56,43,58,50,47],
[50,55,63,49,43,56,0,65,52,52,50,49],
[46,41,41,34,21,45,36,0,36,27,34,34],
[57,67,57,58,47,58,49,65,0,44,55,43],
[41,64,44,53,44,43,49,74,57,0,43,44],
[54,56,63,59,59,51,51,67,46,58,0,61],
[42,55,68,52,40,54,52,67,58,57,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 180, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,44,33,48,28,39,37,56,43,33,37],
[54,0,52,34,53,37,41,50,61,45,55,49],
[57,49,0,42,58,49,44,25,43,51,29,54],
[68,67,59,0,65,56,49,53,62,52,43,61],
[53,48,43,36,0,32,31,35,61,33,33,48],
[73,64,52,45,69,0,45,38,62,58,46,59],
[62,60,57,52,70,56,0,39,58,48,38,58],
[64,51,76,48,66,63,62,0,64,52,49,66],
[45,40,58,39,40,39,43,37,0,35,27,45],
[58,56,50,49,68,43,53,49,66,0,51,58],
[68,46,72,58,68,55,63,52,74,50,0,56],
[64,52,47,40,53,42,43,35,56,43,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 181, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,74,52,46,47,46,46,30,24,46,25,46],
[27,0,51,27,27,27,27,51,0,51,52,29],
[49,50,0,49,49,44,49,27,0,27,25,24],
[55,74,52,0,96,51,96,52,51,68,47,46],
[54,74,52,5,0,51,27,52,5,73,25,46],
[55,74,57,50,50,0,50,79,6,74,52,29],
[55,74,52,5,74,51,0,30,29,51,52,51],
[71,50,74,49,49,22,71,0,22,95,69,46],
[77,101,101,50,96,95,72,79,0,95,96,95],
[55,50,74,33,28,27,50,6,6,0,47,24],
[76,49,76,54,76,49,49,32,5,54,0,51],
[55,72,77,55,55,72,50,55,6,77,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 182, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,57,53,50,57,57,57,54,52,52,53],
[46,0,57,49,46,49,43,60,51,49,50,51],
[44,44,0,41,42,50,51,51,50,49,57,45],
[48,52,60,0,52,62,47,58,60,56,62,53],
[51,55,59,49,0,57,52,58,54,44,48,50],
[44,52,51,39,44,0,50,51,51,46,50,47],
[44,58,50,54,49,51,0,59,58,52,63,52],
[44,41,50,43,43,50,42,0,46,46,51,37],
[47,50,51,41,47,50,43,55,0,47,52,49],
[49,52,52,45,57,55,49,55,54,0,54,47],
[49,51,44,39,53,51,38,50,49,47,0,51],
[48,50,56,48,51,54,49,64,52,54,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 183, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,44,46,53,49,55,47,51,51,48,47],
[59,0,46,46,52,45,50,44,44,54,49,45],
[57,55,0,45,55,46,53,48,49,50,53,56],
[55,55,56,0,56,56,47,56,49,55,54,48],
[48,49,46,45,0,53,48,43,39,48,50,39],
[52,56,55,45,48,0,45,51,52,55,54,49],
[46,51,48,54,53,56,0,54,49,59,51,50],
[54,57,53,45,58,50,47,0,46,51,55,35],
[50,57,52,52,62,49,52,55,0,58,41,44],
[50,47,51,46,53,46,42,50,43,0,43,36],
[53,52,48,47,51,47,50,46,60,58,0,49],
[54,56,45,53,62,52,51,66,57,65,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 184, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,64,56,63,47,40,43,47,48,54,53,46],
[37,0,44,39,38,39,30,36,34,33,40,34],
[45,57,0,53,30,55,40,46,40,47,44,42],
[38,62,48,0,51,56,51,48,48,45,62,48],
[54,63,71,50,0,59,53,55,52,47,56,51],
[61,62,46,45,42,0,39,44,40,52,46,55],
[58,71,61,50,48,62,0,51,43,50,51,50],
[54,65,55,53,46,57,50,0,50,47,46,49],
[53,67,61,53,49,61,58,51,0,55,52,56],
[47,68,54,56,54,49,51,54,46,0,67,53],
[48,61,57,39,45,55,50,55,49,34,0,49],
[55,67,59,53,50,46,51,52,45,48,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 185, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,58,43,60,58,49,49,59,74,57,55],
[62,0,63,45,60,52,54,54,60,58,43,58],
[43,38,0,47,43,45,39,38,46,53,35,47],
[58,56,54,0,46,55,56,49,60,51,56,50],
[41,41,58,55,0,50,49,52,60,50,52,53],
[43,49,56,46,51,0,53,55,66,51,47,63],
[52,47,62,45,52,48,0,46,66,59,55,52],
[52,47,63,52,49,46,55,0,60,58,60,56],
[42,41,55,41,41,35,35,41,0,52,49,47],
[27,43,48,50,51,50,42,43,49,0,45,46],
[44,58,66,45,49,54,46,41,52,56,0,52],
[46,43,54,51,48,38,49,45,54,55,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 186, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,52,59,46,55,47,52,56,48,49,52],
[54,0,50,51,54,50,51,51,58,48,57,56],
[49,51,0,49,51,49,54,49,53,51,48,58],
[42,50,52,0,44,53,45,52,53,53,48,50],
[55,47,50,57,0,54,48,52,55,46,52,60],
[46,51,52,48,47,0,47,45,56,43,57,53],
[54,50,47,56,53,54,0,50,58,52,56,55],
[49,50,52,49,49,56,51,0,55,51,50,57],
[45,43,48,48,46,45,43,46,0,46,41,46],
[53,53,50,48,55,58,49,50,55,0,55,55],
[52,44,53,53,49,44,45,51,60,46,0,53],
[49,45,43,51,41,48,46,44,55,46,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 187, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,58,58,53,52,55,52,50,61,63,63],
[53,0,46,60,49,56,54,43,48,67,59,60],
[43,55,0,60,39,50,54,30,42,60,54,49],
[43,41,41,0,30,44,46,45,43,49,52,49],
[48,52,62,71,0,54,64,43,57,60,60,63],
[49,45,51,57,47,0,44,43,38,64,51,55],
[46,47,47,55,37,57,0,41,45,60,55,52],
[49,58,71,56,58,58,60,0,52,68,65,59],
[51,53,59,58,44,63,56,49,0,65,54,61],
[40,34,41,52,41,37,41,33,36,0,54,53],
[38,42,47,49,41,50,46,36,47,47,0,57],
[38,41,52,52,38,46,49,42,40,48,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 188, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,51,58,41,57,50,65,48,42,66,49],
[54,0,38,59,39,48,56,73,42,48,53,49],
[50,63,0,60,55,56,54,66,47,52,64,56],
[43,42,41,0,51,57,42,54,58,42,65,54],
[60,62,46,50,0,52,52,62,58,51,67,58],
[44,53,45,44,49,0,53,74,41,43,66,57],
[51,45,47,59,49,48,0,53,49,48,65,45],
[36,28,35,47,39,27,48,0,39,50,49,51],
[53,59,54,43,43,60,52,62,0,56,61,45],
[59,53,49,59,50,58,53,51,45,0,62,54],
[35,48,37,36,34,35,36,52,40,39,0,42],
[52,52,45,47,43,44,56,50,56,47,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 189, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,53,55,60,56,48,46,60,62,66,61],
[56,0,44,40,50,48,61,47,66,62,67,59],
[48,57,0,59,56,58,58,60,60,62,64,55],
[46,61,42,0,51,64,54,37,50,61,66,61],
[41,51,45,50,0,63,57,47,51,59,65,67],
[45,53,43,37,38,0,57,49,36,48,61,47],
[53,40,43,47,44,44,0,48,57,52,59,49],
[55,54,41,64,54,52,53,0,65,56,56,56],
[41,35,41,51,50,65,44,36,0,50,56,54],
[39,39,39,40,42,53,49,45,51,0,63,36],
[35,34,37,35,36,40,42,45,45,38,0,50],
[40,42,46,40,34,54,52,45,47,65,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 190, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,42,41,47,49,39,49,41,46,44,44],
[51,0,41,45,48,45,50,49,42,40,50,41],
[59,60,0,58,53,58,63,61,53,55,50,55],
[60,56,43,0,61,57,52,55,53,58,52,49],
[54,53,48,40,0,51,46,59,47,43,45,54],
[52,56,43,44,50,0,57,49,49,46,45,48],
[62,51,38,49,55,44,0,55,50,55,48,44],
[52,52,40,46,42,52,46,0,42,40,48,38],
[60,59,48,48,54,52,51,59,0,49,54,48],
[55,61,46,43,58,55,46,61,52,0,52,51],
[57,51,51,49,56,56,53,53,47,49,0,48],
[57,60,46,52,47,53,57,63,53,50,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 191, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,33,52,39,65,60,50,39,40,26,52],
[41,0,32,51,38,45,57,42,51,35,39,58],
[68,69,0,61,43,56,54,51,63,44,58,79],
[49,50,40,0,45,50,42,34,40,46,32,66],
[62,63,58,56,0,67,62,39,51,67,49,65],
[36,56,45,51,34,0,62,37,48,36,28,52],
[41,44,47,59,39,39,0,50,32,39,41,52],
[51,59,50,67,62,64,51,0,54,56,64,71],
[62,50,38,61,50,53,69,47,0,36,39,63],
[61,66,57,55,34,65,62,45,65,0,31,70],
[75,62,43,69,52,73,60,37,62,70,0,55],
[49,43,22,35,36,49,49,30,38,31,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 192, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,51,49,58,54,48,53,51,53,49,49],
[45,0,46,47,51,58,49,55,46,44,46,47],
[50,55,0,59,54,58,46,56,49,46,51,53],
[52,54,42,0,54,51,52,53,44,51,51,51],
[43,50,47,47,0,49,50,51,48,41,56,50],
[47,43,43,50,52,0,41,53,40,43,44,45],
[53,52,55,49,51,60,0,55,50,42,52,54],
[48,46,45,48,50,48,46,0,45,42,49,51],
[50,55,52,57,53,61,51,56,0,50,58,52],
[48,57,55,50,60,58,59,59,51,0,57,58],
[52,55,50,50,45,57,49,52,43,44,0,51],
[52,54,48,50,51,56,47,50,49,43,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 193, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,53,53,48,56,59,54,46,47,58,66],
[44,0,46,44,46,52,53,54,43,43,50,59],
[48,55,0,47,58,60,53,63,53,46,56,64],
[48,57,54,0,50,62,54,62,52,47,51,61],
[53,55,43,51,0,54,59,57,42,54,49,61],
[45,49,41,39,47,0,45,48,51,43,39,61],
[42,48,48,47,42,56,0,54,46,51,57,56],
[47,47,38,39,44,53,47,0,50,44,49,62],
[55,58,48,49,59,50,55,51,0,47,55,48],
[54,58,55,54,47,58,50,57,54,0,60,69],
[43,51,45,50,52,62,44,52,46,41,0,67],
[35,42,37,40,40,40,45,39,53,32,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 194, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,63,65,43,67,69,62,66,65,65,57],
[52,0,64,59,54,54,63,51,58,51,63,49],
[38,37,0,38,54,45,60,43,43,48,58,44],
[36,42,63,0,41,47,63,40,44,52,41,45],
[58,47,47,60,0,63,65,59,55,58,61,53],
[34,47,56,54,38,0,67,43,44,53,47,40],
[32,38,41,38,36,34,0,31,35,43,33,26],
[39,50,58,61,42,58,70,0,61,58,64,55],
[35,43,58,57,46,57,66,40,0,48,57,48],
[36,50,53,49,43,48,58,43,53,0,41,51],
[36,38,43,60,40,54,68,37,44,60,0,51],
[44,52,57,56,48,61,75,46,53,50,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 195, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,50,52,53,56,38,48,47,56,54,44],
[52,0,50,49,56,55,50,48,51,63,58,51],
[51,51,0,49,51,62,49,51,53,60,51,53],
[49,52,52,0,53,58,51,53,52,55,55,49],
[48,45,50,48,0,53,49,48,45,52,47,52],
[45,46,39,43,48,0,43,45,51,56,54,50],
[63,51,52,50,52,58,0,47,55,48,49,47],
[53,53,50,48,53,56,54,0,53,59,60,49],
[54,50,48,49,56,50,46,48,0,51,55,48],
[45,38,41,46,49,45,53,42,50,0,56,47],
[47,43,50,46,54,47,52,41,46,45,0,45],
[57,50,48,52,49,51,54,52,53,54,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 196, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,49,51,56,50,40,41,42,55,52,48],
[51,0,69,63,39,54,34,52,43,41,51,38],
[52,32,0,48,40,58,37,36,27,36,43,36],
[50,38,53,0,57,45,30,44,48,41,37,47],
[45,62,61,44,0,56,41,52,54,50,48,34],
[51,47,43,56,45,0,26,46,39,46,41,35],
[61,67,64,71,60,75,0,57,60,52,49,48],
[60,49,65,57,49,55,44,0,48,54,61,46],
[59,58,74,53,47,62,41,53,0,50,49,40],
[46,60,65,60,51,55,49,47,51,0,44,58],
[49,50,58,64,53,60,52,40,52,57,0,47],
[53,63,65,54,67,66,53,55,61,43,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 197, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,52,51,57,62,46,84,28,35,54,34],
[41,0,38,48,52,45,40,64,31,31,48,39],
[49,63,0,36,50,34,45,68,26,29,70,35],
[50,53,65,0,56,56,49,84,58,42,64,51],
[44,49,51,45,0,39,59,84,29,32,53,47],
[39,56,67,45,62,0,42,57,45,36,60,55],
[55,61,56,52,42,59,0,76,55,42,54,55],
[17,37,33,17,17,44,25,0,16,22,41,31],
[73,70,75,43,72,56,46,85,0,63,82,34],
[66,70,72,59,69,65,59,79,38,0,84,46],
[47,53,31,37,48,41,47,60,19,17,0,31],
[67,62,66,50,54,46,46,70,67,55,70,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 198, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,44,53,55,51,64,56,38,59,39,49],
[49,0,33,49,46,46,44,52,38,55,37,54],
[57,68,0,54,63,57,64,68,53,70,48,59],
[48,52,47,0,56,39,49,48,51,59,51,59],
[46,55,38,45,0,32,60,62,49,61,44,64],
[50,55,44,62,69,0,66,55,44,58,46,57],
[37,57,37,52,41,35,0,52,42,49,38,56],
[45,49,33,53,39,46,49,0,43,46,25,53],
[63,63,48,50,52,57,59,58,0,57,55,63],
[42,46,31,42,40,43,52,55,44,0,31,51],
[62,64,53,50,57,55,63,76,46,70,0,61],
[52,47,42,42,37,44,45,48,38,50,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 199, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,46,62,43,51,46,55,50,53,47,55],
[43,0,50,49,46,39,50,41,44,44,45,50],
[55,51,0,55,57,55,49,44,47,57,49,56],
[39,52,46,0,38,40,46,38,40,45,37,49],
[58,55,44,63,0,53,51,56,51,58,56,57],
[50,62,46,61,48,0,49,49,43,57,46,57],
[55,51,52,55,50,52,0,40,47,56,49,53],
[46,60,57,63,45,52,61,0,58,57,49,60],
[51,57,54,61,50,58,54,43,0,58,53,60],
[48,57,44,56,43,44,45,44,43,0,43,43],
[54,56,52,64,45,55,52,52,48,58,0,64],
[46,51,45,52,44,44,48,41,41,58,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 101, 200, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebb/mebb_12_101.csv", index=False, header=False)