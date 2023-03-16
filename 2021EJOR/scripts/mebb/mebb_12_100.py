
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,25,78,53,26,25,53,50,73,26,50,53],
[75,0,78,75,75,51,53,48,100,28,51,53],
[22,22,0,22,23,0,75,47,23,0,72,53],
[47,25,78,0,48,25,53,47,48,0,50,53],
[74,25,77,52,0,25,53,50,73,52,50,53],
[75,49,100,75,75,0,75,47,100,28,72,53],
[47,47,25,47,47,25,0,47,47,0,50,52],
[50,52,53,53,50,53,53,0,75,53,52,28],
[27,0,77,52,27,0,53,25,0,27,50,53],
[74,72,100,100,48,72,100,47,73,0,72,53],
[50,49,28,50,50,28,50,48,50,28,0,28],
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
result = np.append(np.array([12, 100, 1, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,48,47,49,43,44,46,41,52,49,47],
[55,0,51,48,49,46,49,50,51,51,52,51],
[52,49,0,52,49,46,56,49,46,57,48,51],
[53,52,48,0,49,40,57,49,47,52,51,47],
[51,51,51,51,0,47,56,51,44,54,57,55],
[57,54,54,60,53,0,52,54,45,55,55,50],
[56,51,44,43,44,48,0,47,46,57,53,49],
[54,50,51,51,49,46,53,0,44,56,49,49],
[59,49,54,53,56,55,54,56,0,56,54,52],
[48,49,43,48,46,45,43,44,44,0,47,43],
[51,48,52,49,43,45,47,51,46,53,0,52],
[53,49,49,53,45,50,51,51,48,57,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 2, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,60,49,58,45,62,57,49,58,46,53],
[39,0,51,48,51,49,59,60,50,53,40,52],
[40,49,0,47,47,42,53,50,46,47,39,42],
[51,52,53,0,55,51,65,56,49,56,52,60],
[42,49,53,45,0,46,62,55,48,57,45,56],
[55,51,58,49,54,0,58,53,56,53,40,57],
[38,41,47,35,38,42,0,43,43,41,31,49],
[43,40,50,44,45,47,57,0,40,49,45,50],
[51,50,54,51,52,44,57,60,0,56,41,55],
[42,47,53,44,43,47,59,51,44,0,38,51],
[54,60,61,48,55,60,69,55,59,62,0,62],
[47,48,58,40,44,43,51,50,45,49,38,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 3, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,48,53,44,55,39,52,43,51,55,53],
[43,0,38,39,36,43,34,33,32,33,43,38],
[52,62,0,47,44,42,40,44,40,45,48,56],
[47,61,53,0,40,61,47,49,41,41,47,55],
[56,64,56,60,0,59,47,49,51,49,50,51],
[45,57,58,39,41,0,42,36,45,45,42,51],
[61,66,60,53,53,58,0,65,49,50,56,53],
[48,67,56,51,51,64,35,0,39,54,56,51],
[57,68,60,59,49,55,51,61,0,54,61,64],
[49,67,55,59,51,55,50,46,46,0,54,59],
[45,57,52,53,50,58,44,44,39,46,0,48],
[47,62,44,45,49,49,47,49,36,41,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 4, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,44,37,66,66,40,56,66,69,73,71],
[44,0,53,36,53,58,39,43,54,42,72,51],
[56,47,0,44,29,61,54,34,54,40,64,54],
[63,64,56,0,44,76,34,51,69,44,83,46],
[34,47,71,56,0,73,64,63,80,62,90,71],
[34,42,39,24,27,0,27,19,39,20,87,27],
[60,61,46,66,36,73,0,49,85,64,68,47],
[44,57,66,49,37,81,51,0,59,37,88,63],
[34,46,46,31,20,61,15,41,0,37,70,46],
[31,58,60,56,38,80,36,63,63,0,87,50],
[27,28,36,17,10,13,32,12,30,13,0,27],
[29,49,46,54,29,73,53,37,54,50,73,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 5, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,47,51,50,52,47,57,50,58,52,48],
[48,0,47,55,47,51,48,50,48,56,45,44],
[53,53,0,59,53,49,54,64,57,59,59,53],
[49,45,41,0,47,49,43,53,50,53,46,52],
[50,53,47,53,0,53,52,60,50,53,51,50],
[48,49,51,51,47,0,48,56,50,54,54,44],
[53,52,46,57,48,52,0,63,51,54,50,48],
[43,50,36,47,40,44,37,0,47,52,47,42],
[50,52,43,50,50,50,49,53,0,55,53,47],
[42,44,41,47,47,46,46,48,45,0,44,45],
[48,55,41,54,49,46,50,53,47,56,0,47],
[52,56,47,48,50,56,52,58,53,55,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 6, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,47,52,65,51,47,47,54,52,59,46],
[52,0,45,43,58,54,42,44,52,43,55,45],
[53,55,0,53,57,64,40,51,61,43,61,43],
[48,57,47,0,64,66,36,44,46,52,54,44],
[35,42,43,36,0,47,39,42,51,45,48,31],
[49,46,36,34,53,0,44,43,51,41,43,35],
[53,58,60,64,61,56,0,65,64,54,60,49],
[53,56,49,56,58,57,35,0,66,50,62,43],
[46,48,39,54,49,49,36,34,0,40,56,45],
[48,57,57,48,55,59,46,50,60,0,65,52],
[41,45,39,46,52,57,40,38,44,35,0,29],
[54,55,57,56,69,65,51,57,55,48,71,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 7, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,49,42,57,41,33,31,41,57,48,53],
[53,0,46,52,62,56,37,48,45,67,52,60],
[51,54,0,52,52,48,38,28,40,61,45,47],
[58,48,48,0,58,46,40,38,47,54,53,52],
[43,38,48,42,0,37,33,42,37,54,45,44],
[59,44,52,54,63,0,38,39,45,54,44,50],
[67,63,62,60,67,62,0,42,61,76,56,61],
[69,52,72,62,58,61,58,0,45,70,54,58],
[59,55,60,53,63,55,39,55,0,63,56,53],
[43,33,39,46,46,46,24,30,37,0,44,40],
[52,48,55,47,55,56,44,46,44,56,0,39],
[47,40,53,48,56,50,39,42,47,60,61,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 8, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,45,53,56,45,56,51,51,54,53,45],
[52,0,48,42,46,48,51,45,49,50,50,48],
[55,52,0,45,52,53,53,47,53,54,47,48],
[47,58,55,0,51,54,52,51,56,54,53,53],
[44,54,48,49,0,49,51,44,52,52,53,47],
[55,52,47,46,51,0,57,53,53,58,51,51],
[44,49,47,48,49,43,0,49,49,44,52,46],
[49,55,53,49,56,47,51,0,45,58,55,52],
[49,51,47,44,48,47,51,55,0,55,52,50],
[46,50,46,46,48,42,56,42,45,0,50,43],
[47,50,53,47,47,49,48,45,48,50,0,49],
[55,52,52,47,53,49,54,48,50,57,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 9, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,55,46,47,47,48,56,40,55,52,41],
[49,0,51,45,54,43,52,55,47,47,51,50],
[45,49,0,50,51,51,51,54,46,54,53,57],
[54,55,50,0,53,55,54,53,48,51,55,50],
[53,46,49,47,0,49,50,65,50,57,54,51],
[53,57,49,45,51,0,58,58,48,54,56,53],
[52,48,49,46,50,42,0,55,48,54,50,53],
[44,45,46,47,35,42,45,0,42,46,50,44],
[60,53,54,52,50,52,52,58,0,51,56,51],
[45,53,46,49,43,46,46,54,49,0,49,51],
[48,49,47,45,46,44,50,50,44,51,0,47],
[59,50,43,50,49,47,47,56,49,49,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 10, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,42,54,36,69,53,59,75,56,63,43],
[47,0,56,45,29,65,61,55,79,47,60,52],
[58,44,0,37,36,64,61,48,86,46,65,45],
[46,55,63,0,53,73,72,53,75,72,45,43],
[64,71,64,47,0,73,71,63,82,56,73,49],
[31,35,36,27,27,0,39,40,65,40,51,22],
[47,39,39,28,29,61,0,39,70,37,49,41],
[41,45,52,47,37,60,61,0,70,62,61,40],
[25,21,14,25,18,35,30,30,0,24,39,19],
[44,53,54,28,44,60,63,38,76,0,56,45],
[37,40,35,55,27,49,51,39,61,44,0,20],
[57,48,55,57,51,78,59,60,81,55,80,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 11, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,68,56,52,47,46,34,53,68,59,57],
[43,0,41,55,35,28,40,39,68,62,49,52],
[32,59,0,59,48,42,39,42,72,55,51,51],
[44,45,41,0,45,41,34,32,58,62,58,52],
[48,65,52,55,0,48,50,49,67,59,69,67],
[53,72,58,59,52,0,44,45,72,62,57,60],
[54,60,61,66,50,56,0,46,72,59,67,55],
[66,61,58,68,51,55,54,0,73,50,69,69],
[47,32,28,42,33,28,28,27,0,41,29,38],
[32,38,45,38,41,38,41,50,59,0,52,36],
[41,51,49,42,31,43,33,31,71,48,0,50],
[43,48,49,48,33,40,45,31,62,64,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 12, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,64,62,47,29,75,17,38,55,18,24],
[41,0,51,43,32,34,52,31,22,51,28,33],
[36,49,0,23,46,46,56,19,25,51,40,20],
[38,57,77,0,38,36,55,37,47,60,43,30],
[53,68,54,62,0,28,70,29,20,42,23,23],
[71,66,54,64,72,0,79,31,52,65,37,38],
[25,48,44,45,30,21,0,24,17,51,20,4],
[83,69,81,63,71,69,76,0,50,57,57,32],
[62,78,75,53,80,48,83,50,0,74,42,54],
[45,49,49,40,58,35,49,43,26,0,54,44],
[82,72,60,57,77,63,80,43,58,46,0,57],
[76,67,80,70,77,62,96,68,46,56,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 13, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,71,33,59,63,69,46,53,38,58,50,51],
[29,0,43,28,33,74,43,42,38,53,53,41],
[67,57,0,49,64,59,46,52,38,74,64,41],
[41,72,51,0,69,84,54,44,64,65,65,64],
[37,67,36,31,0,54,39,43,23,53,56,33],
[31,26,41,16,46,0,21,31,41,59,46,34],
[54,57,54,46,61,79,0,57,28,74,61,62],
[47,58,48,56,57,69,43,0,35,67,61,55],
[62,62,62,36,77,59,72,65,0,79,66,65],
[42,47,26,35,47,41,26,33,21,0,23,21],
[50,47,36,35,44,54,39,39,34,77,0,62],
[49,59,59,36,67,66,38,45,35,79,38,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 14, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,64,49,45,56,45,40,43,38,45,49,52],
[36,0,30,33,46,47,35,34,39,39,40,50],
[51,70,0,42,59,54,30,47,49,56,42,62],
[55,67,58,0,48,53,44,55,44,57,48,63],
[44,54,41,52,0,51,41,40,43,35,37,62],
[55,53,46,47,49,0,34,55,43,46,32,46],
[60,65,70,56,59,66,0,51,50,68,47,63],
[57,66,53,45,60,45,49,0,52,53,53,56],
[62,61,51,56,57,57,50,48,0,61,50,64],
[55,61,44,43,65,54,32,47,39,0,51,69],
[51,60,58,52,63,68,53,47,50,49,0,66],
[48,50,38,37,38,54,37,44,36,31,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 15, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,58,51,43,46,56,45,43,46,43,43],
[64,0,62,49,51,47,56,47,52,52,41,48],
[42,38,0,39,38,40,51,41,48,45,37,40],
[49,51,61,0,39,45,61,45,53,56,43,48],
[57,49,62,61,0,40,56,51,57,52,40,40],
[54,53,60,55,60,0,60,56,56,50,47,45],
[44,44,49,39,44,40,0,41,48,41,38,41],
[55,53,59,55,49,44,59,0,60,60,51,54],
[57,48,52,47,43,44,52,40,0,44,42,39],
[54,48,55,44,48,50,59,40,56,0,50,43],
[57,59,63,57,60,53,62,49,58,50,0,54],
[57,52,60,52,60,55,59,46,61,57,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 16, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,49,39,46,42,29,33,44,37,35,34],
[38,0,49,46,43,35,45,36,41,42,48,34],
[51,51,0,41,44,42,47,35,41,38,51,42],
[61,54,59,0,35,50,42,43,55,43,54,43],
[54,57,56,65,0,47,48,49,54,55,48,57],
[58,65,58,50,53,0,48,53,59,47,44,46],
[71,55,53,58,52,52,0,48,57,42,59,50],
[67,64,65,57,51,47,52,0,50,51,55,47],
[56,59,59,45,46,41,43,50,0,41,51,46],
[63,58,62,57,45,53,58,49,59,0,60,55],
[65,52,49,46,52,56,41,45,49,40,0,41],
[66,66,58,57,43,54,50,53,54,45,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 17, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,41,45,37,45,43,40,36,49,41,42],
[56,0,48,48,48,48,44,49,45,53,50,40],
[59,52,0,51,51,55,55,53,46,59,46,49],
[55,52,49,0,45,53,46,52,44,57,49,44],
[63,52,49,55,0,53,48,51,52,51,47,52],
[55,52,45,47,47,0,44,41,43,47,50,37],
[57,56,45,54,52,56,0,53,46,53,51,55],
[60,51,47,48,49,59,47,0,49,55,49,51],
[64,55,54,56,48,57,54,51,0,58,46,51],
[51,47,41,43,49,53,47,45,42,0,38,40],
[59,50,54,51,53,50,49,51,54,62,0,51],
[58,60,51,56,48,63,45,49,49,60,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 18, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,49,51,49,53,46,48,46,58,51,51],
[45,0,44,55,49,56,48,46,47,48,54,46],
[51,56,0,61,54,56,52,48,52,56,53,53],
[49,45,39,0,54,49,47,43,47,49,52,48],
[51,51,46,46,0,51,53,41,48,43,48,51],
[47,44,44,51,49,0,45,40,43,40,42,46],
[54,52,48,53,47,55,0,49,54,53,53,52],
[52,54,52,57,59,60,51,0,49,51,53,52],
[54,53,48,53,52,57,46,51,0,53,63,54],
[42,52,44,51,57,60,47,49,47,0,50,45],
[49,46,47,48,52,58,47,47,37,50,0,51],
[49,54,47,52,49,54,48,48,46,55,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 19, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,80,49,55,59,48,53,75,67,74,68],
[55,0,61,64,49,64,41,73,63,64,68,65],
[20,39,0,37,52,47,26,42,57,53,42,43],
[51,36,63,0,35,48,51,51,63,58,56,57],
[45,51,48,65,0,64,37,72,72,60,74,62],
[41,36,53,52,36,0,35,65,70,51,35,56],
[52,59,74,49,63,65,0,58,82,60,62,76],
[47,27,58,49,28,35,42,0,58,54,49,46],
[25,37,43,37,28,30,18,42,0,62,39,53],
[33,36,47,42,40,49,40,46,38,0,35,49],
[26,32,58,44,26,65,38,51,61,65,0,65],
[32,35,57,43,38,44,24,54,47,51,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 20, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,43,52,51,41,48,51,52,53,45,48],
[46,0,50,57,56,54,51,45,51,55,48,49],
[57,50,0,53,55,56,47,52,55,56,45,57],
[48,43,47,0,47,49,41,44,45,45,40,44],
[49,44,45,53,0,56,46,39,57,41,47,37],
[59,46,44,51,44,0,46,47,55,45,46,55],
[52,49,53,59,54,54,0,52,49,54,43,45],
[49,55,48,56,61,53,48,0,56,53,49,48],
[48,49,45,55,43,45,51,44,0,43,40,45],
[47,45,44,55,59,55,46,47,57,0,48,46],
[55,52,55,60,53,54,57,51,60,52,0,46],
[52,51,43,56,63,45,55,52,55,54,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 21, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,46,49,47,46,46,47,48,51,43,47],
[55,0,51,49,51,46,56,54,60,55,51,50],
[54,49,0,56,56,48,50,52,48,56,52,47],
[51,51,44,0,50,45,49,48,51,53,49,52],
[53,49,44,50,0,43,47,47,47,54,46,44],
[54,54,52,55,57,0,54,48,52,57,59,55],
[54,44,50,51,53,46,0,45,43,50,60,47],
[53,46,48,52,53,52,55,0,48,53,57,48],
[52,40,52,49,53,48,57,52,0,53,53,51],
[49,45,44,47,46,43,50,47,47,0,50,44],
[57,49,48,51,54,41,40,43,47,50,0,47],
[53,50,53,48,56,45,53,52,49,56,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 22, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,53,53,48,51,56,45,60,49,53,56],
[45,0,48,41,44,46,43,37,44,42,47,46],
[47,52,0,46,45,46,45,47,51,47,52,53],
[47,59,54,0,54,52,48,54,57,51,58,63],
[52,56,55,46,0,55,49,51,55,57,53,55],
[49,54,54,48,45,0,46,51,55,48,53,60],
[44,57,55,52,51,54,0,47,54,56,55,54],
[55,63,53,46,49,49,53,0,57,53,47,58],
[40,56,49,43,45,45,46,43,0,50,51,48],
[51,58,53,49,43,52,44,47,50,0,51,58],
[47,53,48,42,47,47,45,53,49,49,0,61],
[44,54,47,37,45,40,46,42,52,42,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 23, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,60,46,45,55,58,50,58,61,55,53],
[40,0,51,40,38,48,48,50,48,54,43,49],
[40,49,0,42,40,48,49,50,49,46,42,44],
[54,60,58,0,51,53,57,58,52,54,48,53],
[55,62,60,49,0,62,56,55,55,55,52,54],
[45,52,52,47,38,0,46,55,50,54,49,40],
[42,52,51,43,44,54,0,46,46,54,44,48],
[50,50,50,42,45,45,54,0,48,46,44,52],
[42,52,51,48,45,50,54,52,0,54,51,51],
[39,46,54,46,45,46,46,54,46,0,47,50],
[45,57,58,52,48,51,56,56,49,53,0,52],
[47,51,56,47,46,60,52,48,49,50,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 24, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,49,54,42,36,39,39,47,48,44,47],
[70,0,54,66,48,50,66,46,60,60,49,60],
[51,46,0,65,49,44,53,37,52,49,50,50],
[46,34,35,0,36,30,37,36,40,47,34,31],
[58,52,51,64,0,50,59,49,48,51,45,53],
[64,50,56,70,50,0,61,47,52,54,55,58],
[61,34,47,63,41,39,0,44,48,49,42,46],
[61,54,63,64,51,53,56,0,49,48,50,54],
[53,40,48,60,52,48,52,51,0,46,49,46],
[52,40,51,53,49,46,51,52,54,0,46,54],
[56,51,50,66,55,45,58,50,51,54,0,44],
[53,40,50,69,47,42,54,46,54,46,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 25, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,67,46,55,55,65,55,51,54,51,46,52],
[33,0,41,53,52,49,52,42,53,51,42,47],
[54,59,0,53,51,59,53,48,47,59,45,57],
[45,47,47,0,53,49,48,38,46,47,42,50],
[45,48,49,47,0,51,47,41,51,44,40,48],
[35,51,41,51,49,0,49,32,47,44,42,47],
[45,48,47,52,53,51,0,44,43,52,45,50],
[49,58,52,62,59,68,56,0,58,57,54,53],
[46,47,53,54,49,53,57,42,0,50,48,46],
[49,49,41,53,56,56,48,43,50,0,50,60],
[54,58,55,58,60,58,55,46,52,50,0,57],
[48,53,43,50,52,53,50,47,54,40,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 26, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,47,42,48,44,58,50,53,51,47,50],
[50,0,58,44,47,44,60,48,58,55,47,54],
[53,42,0,50,50,45,61,53,59,50,50,51],
[58,56,50,0,45,45,56,52,59,58,45,52],
[52,53,50,55,0,56,64,57,58,55,53,53],
[56,56,55,55,44,0,56,60,56,57,54,52],
[42,40,39,44,36,44,0,47,45,49,38,47],
[50,52,47,48,43,40,53,0,48,49,40,47],
[47,42,41,41,42,44,55,52,0,48,45,43],
[49,45,50,42,45,43,51,51,52,0,53,48],
[53,53,50,55,47,46,62,60,55,47,0,51],
[50,46,49,48,47,48,53,53,57,52,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 27, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,54,44,39,35,38,38,45,43,40,51],
[64,0,55,62,57,50,61,50,53,51,49,62],
[46,45,0,49,43,27,43,55,45,45,41,45],
[56,38,51,0,50,33,45,43,43,41,43,46],
[61,43,57,50,0,34,43,46,52,37,42,57],
[65,50,73,67,66,0,53,63,71,59,61,68],
[62,39,57,55,57,47,0,52,58,51,53,57],
[62,50,45,57,54,37,48,0,45,60,55,56],
[55,47,55,57,48,29,42,55,0,37,61,59],
[57,49,55,59,63,41,49,40,63,0,57,58],
[60,51,59,57,58,39,47,45,39,43,0,43],
[49,38,55,54,43,32,43,44,41,42,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 28, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,45,53,48,42,47,44,58,40,53,51],
[42,0,42,46,44,37,39,43,43,39,43,41],
[55,58,0,63,49,44,57,46,54,50,51,57],
[47,54,37,0,46,47,38,43,61,41,38,42],
[52,56,51,54,0,43,50,54,55,49,58,51],
[58,63,56,53,57,0,53,59,61,45,54,57],
[53,61,43,62,50,47,0,55,57,41,49,50],
[56,57,54,57,46,41,45,0,55,43,56,53],
[42,57,46,39,45,39,43,45,0,45,38,46],
[60,61,50,59,51,55,59,57,55,0,49,56],
[47,57,49,62,42,46,51,44,62,51,0,45],
[49,59,43,58,49,43,50,47,54,44,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 29, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,60,68,57,55,53,50,59,60,55,52],
[45,0,54,50,44,43,48,54,62,46,50,38],
[40,46,0,51,46,37,47,47,46,43,55,50],
[32,50,49,0,50,46,56,41,66,53,55,56],
[43,56,54,50,0,31,37,44,63,55,50,41],
[45,57,63,54,69,0,58,49,66,61,48,58],
[47,52,53,44,63,42,0,47,61,53,55,60],
[50,46,53,59,56,51,53,0,49,56,65,53],
[41,38,54,34,37,34,39,51,0,45,45,41],
[40,54,57,47,45,39,47,44,55,0,49,49],
[45,50,45,45,50,52,45,35,55,51,0,46],
[48,62,50,44,59,42,40,47,59,51,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 30, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,55,39,49,51,40,43,44,46,45,48],
[54,0,52,48,53,52,42,46,50,53,45,49],
[45,48,0,44,54,48,46,45,48,46,42,58],
[61,52,56,0,58,50,52,50,46,55,48,51],
[51,47,46,42,0,48,44,42,47,51,41,49],
[49,48,52,50,52,0,50,50,49,51,48,51],
[60,58,54,48,56,50,0,52,48,59,54,56],
[57,54,55,50,58,50,48,0,42,54,47,57],
[56,50,52,54,53,51,52,58,0,57,48,56],
[54,47,54,45,49,49,41,46,43,0,43,44],
[55,55,58,52,59,52,46,53,52,57,0,54],
[52,51,42,49,51,49,44,43,44,56,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 31, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,35,73,29,31,51,67,28,24,40,37],
[78,0,65,59,59,49,71,68,62,48,69,67],
[65,35,0,85,37,62,51,76,44,46,57,36],
[27,41,15,0,8,52,30,45,42,25,30,29],
[71,41,63,92,0,56,62,69,51,65,55,51],
[69,51,38,48,44,0,43,55,45,51,41,61],
[49,29,49,70,38,57,0,66,30,56,52,50],
[33,32,24,55,31,45,34,0,45,30,38,29],
[72,38,56,58,49,55,70,55,0,53,46,68],
[76,52,54,75,35,49,44,70,47,0,54,61],
[60,31,43,70,45,59,48,62,54,46,0,45],
[63,33,64,71,49,39,50,71,32,39,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 32, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,89,56,89,61,50,41,50,55,50,56,56],
[11,0,6,40,46,40,41,35,46,0,41,41],
[44,94,0,94,61,55,46,40,40,5,61,41],
[11,60,6,0,11,15,41,0,11,0,6,6],
[39,54,39,89,0,50,35,35,79,0,35,35],
[50,60,45,85,50,0,41,35,50,39,45,6],
[59,59,54,59,65,59,0,15,59,54,54,60],
[50,65,60,100,65,65,85,0,50,54,65,60],
[45,54,60,89,21,50,41,50,0,15,56,56],
[50,100,95,100,100,61,46,46,85,0,61,41],
[44,59,39,94,65,55,46,35,44,39,0,41],
[44,59,59,94,65,94,40,40,44,59,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 33, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,36,66,100,15,10,0,49,0,98,7],
[44,0,44,59,100,42,10,10,51,36,100,51],
[64,56,0,64,66,15,17,15,15,0,64,15],
[34,41,36,0,43,41,2,0,49,34,49,41],
[0,0,34,57,0,0,2,0,42,0,57,7],
[85,58,85,59,100,0,51,51,51,36,100,58],
[90,90,83,98,98,49,0,90,49,34,98,90],
[100,90,85,100,100,49,10,0,49,34,98,98],
[51,49,85,51,58,49,51,51,0,51,51,58],
[100,64,100,66,100,64,66,66,49,0,98,64],
[2,0,36,51,43,0,2,2,49,2,0,7],
[93,49,85,59,93,42,10,2,42,36,93,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 34, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,58,44,58,48,58,54,47,44,46,52],
[45,0,59,40,53,52,46,46,51,34,29,46],
[42,41,0,37,41,39,42,37,34,36,37,43],
[56,60,63,0,57,76,50,43,53,45,48,59],
[42,47,59,43,0,65,46,45,56,53,46,47],
[52,48,61,24,35,0,52,36,45,35,39,48],
[42,54,58,50,54,48,0,46,41,43,39,38],
[46,54,63,57,55,64,54,0,54,35,40,51],
[53,49,66,47,44,55,59,46,0,44,43,48],
[56,66,64,55,47,65,57,65,56,0,52,57],
[54,71,63,52,54,61,61,60,57,48,0,70],
[48,54,57,41,53,52,62,49,52,43,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 35, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,25,13,29,35,9,63,21,26,12,30],
[91,0,91,66,53,100,32,62,74,74,95,66],
[75,9,0,46,57,35,37,63,46,18,46,63],
[87,34,54,0,54,51,34,88,42,42,46,30],
[71,47,43,46,0,64,46,59,71,47,75,46],
[65,0,65,49,36,0,28,45,65,37,40,40],
[91,68,63,66,54,72,0,67,91,68,67,38],
[37,38,37,12,41,55,33,0,41,46,41,12],
[79,26,54,58,29,35,9,59,0,46,34,26],
[74,26,82,58,53,63,32,54,54,0,57,58],
[88,5,54,54,25,60,33,59,66,43,0,59],
[70,34,37,70,54,60,62,88,74,42,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 36, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,56,56,60,53,69,71,64,79,58,49],
[43,0,62,32,67,38,68,83,61,51,70,60],
[44,38,0,37,71,60,73,44,48,62,53,47],
[44,68,63,0,73,63,63,72,78,74,79,56],
[40,33,29,27,0,36,60,39,43,40,35,32],
[47,62,40,37,64,0,69,53,51,60,53,54],
[31,32,27,37,40,31,0,50,41,46,49,48],
[29,17,56,28,61,47,50,0,36,33,53,24],
[36,39,52,22,57,49,59,64,0,35,41,30],
[21,49,38,26,60,40,54,67,65,0,50,28],
[42,30,47,21,65,47,51,47,59,50,0,43],
[51,40,53,44,68,46,52,76,70,72,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 37, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,100,72,71,43,52,43,72,100,52,100,52],
[0,0,0,0,0,0,43,43,0,52,0,43],
[28,100,0,71,71,71,52,100,100,71,100,71],
[29,100,29,0,43,0,72,72,48,52,57,43],
[57,100,29,57,0,28,72,91,57,71,57,71],
[48,100,29,100,72,0,72,91,100,81,100,81],
[57,57,48,28,28,28,0,100,57,71,57,71],
[28,57,0,28,9,9,0,0,28,52,57,52],
[0,100,0,52,43,0,43,72,0,52,100,52],
[48,48,29,48,29,19,29,48,48,0,48,48],
[0,100,0,43,43,0,43,43,0,52,0,43],
[48,57,29,57,29,19,29,48,48,52,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 38, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,38,50,52,46,55,50,47,44,60,45],
[48,0,45,57,55,55,56,55,48,43,54,47],
[62,55,0,49,59,59,53,53,52,49,49,53],
[50,43,51,0,55,52,55,58,46,48,51,48],
[48,45,41,45,0,49,48,50,47,42,53,53],
[54,45,41,48,51,0,47,48,53,42,49,47],
[45,44,47,45,52,53,0,46,43,45,44,43],
[50,45,47,42,50,52,54,0,54,51,56,52],
[53,52,48,54,53,47,57,46,0,46,56,50],
[56,57,51,52,58,58,55,49,54,0,57,55],
[40,46,51,49,47,51,56,44,44,43,0,45],
[55,53,47,52,47,53,57,48,50,45,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 39, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,35,49,35,33,42,45,37,52,50,40],
[44,0,46,51,48,45,40,49,56,52,55,51],
[65,54,0,62,51,45,44,55,53,56,53,55],
[51,49,38,0,52,37,42,53,43,56,41,49],
[65,52,49,48,0,47,52,57,47,62,69,52],
[67,55,55,63,53,0,59,65,50,66,63,69],
[58,60,56,58,48,41,0,59,51,62,58,58],
[55,51,45,47,43,35,41,0,36,55,46,41],
[63,44,47,57,53,50,49,64,0,68,53,55],
[48,48,44,44,38,34,38,45,32,0,42,40],
[50,45,47,59,31,37,42,54,47,58,0,44],
[60,49,45,51,48,31,42,59,45,60,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 40, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,31,48,26,39,76,48,48,39,48,39],
[74,0,59,59,28,50,74,74,59,22,50,74],
[69,41,0,72,41,39,91,41,76,39,39,63],
[52,41,28,0,45,28,52,52,37,0,28,52],
[74,72,59,55,0,22,74,74,59,22,50,74],
[61,50,61,72,78,0,83,61,100,55,83,83],
[24,26,9,48,26,17,0,17,48,17,26,41],
[52,26,59,48,26,39,83,0,76,22,48,91],
[52,41,24,63,41,0,52,24,0,24,0,24],
[61,78,61,100,78,45,83,78,76,0,54,69],
[52,50,61,72,50,17,74,52,100,46,0,52],
[61,26,37,48,26,17,59,9,76,31,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 41, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,46,43,43,41,47,57,53,50,49,39],
[57,0,49,57,55,52,62,53,58,55,59,58],
[54,51,0,51,60,49,58,58,57,54,53,56],
[57,43,49,0,53,43,52,53,51,52,52,55],
[57,45,40,47,0,39,62,50,54,54,50,55],
[59,48,51,57,61,0,56,56,54,56,55,57],
[53,38,42,48,38,44,0,58,42,44,46,45],
[43,47,42,47,50,44,42,0,49,44,50,49],
[47,42,43,49,46,46,58,51,0,54,44,47],
[50,45,46,48,46,44,56,56,46,0,46,47],
[51,41,47,48,50,45,54,50,56,54,0,48],
[61,42,44,45,45,43,55,51,53,53,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 42, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,46,57,44,57,47,53,40,47,53,48],
[49,0,49,48,50,61,54,57,58,46,53,51],
[54,51,0,54,55,52,56,53,47,36,53,43],
[43,52,46,0,47,60,46,58,45,38,48,42],
[56,50,45,53,0,55,49,57,40,46,52,48],
[43,39,48,40,45,0,50,44,52,33,54,42],
[53,46,44,54,51,50,0,55,48,52,49,41],
[47,43,47,42,43,56,45,0,41,47,47,39],
[60,42,53,55,60,48,52,59,0,44,50,47],
[53,54,64,62,54,67,48,53,56,0,57,49],
[47,47,47,52,48,46,51,53,50,43,0,43],
[52,49,57,58,52,58,59,61,53,51,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 43, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,49,46,64,51,54,63,60,52,66,61],
[38,0,31,33,50,35,28,58,34,30,40,48],
[51,69,0,42,60,47,60,70,53,61,56,73],
[54,67,58,0,57,57,46,67,54,53,61,67],
[36,50,40,43,0,49,43,58,40,47,50,51],
[49,65,53,43,51,0,50,63,48,44,56,52],
[46,72,40,54,57,50,0,63,62,52,67,64],
[37,42,30,33,42,37,37,0,42,38,37,38],
[40,66,47,46,60,52,38,58,0,49,62,57],
[48,70,39,47,53,56,48,62,51,0,60,62],
[34,60,44,39,50,44,33,63,38,40,0,53],
[39,52,27,33,49,48,36,62,43,38,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 44, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,45,62,47,52,47,55,52,44,46,38],
[54,0,51,56,48,54,45,57,61,42,42,42],
[55,49,0,61,52,55,41,51,59,42,48,34],
[38,44,39,0,43,49,43,57,49,44,32,32],
[53,52,48,57,0,50,44,59,52,53,40,46],
[48,46,45,51,50,0,53,58,60,46,43,49],
[53,55,59,57,56,47,0,53,67,57,43,51],
[45,43,49,43,41,42,47,0,55,51,45,49],
[48,39,41,51,48,40,33,45,0,42,38,35],
[56,58,58,56,47,54,43,49,58,0,38,49],
[54,58,52,68,60,57,57,55,62,62,0,49],
[62,58,66,68,54,51,49,51,65,51,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 45, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,50,62,58,49,55,55,46,54,53,33],
[41,0,56,60,46,61,51,62,56,55,50,54],
[50,44,0,54,44,65,50,63,32,57,29,39],
[38,40,46,0,50,62,66,67,55,48,39,32],
[42,54,56,50,0,53,44,60,49,44,40,34],
[51,39,35,38,47,0,47,58,52,47,35,33],
[45,49,50,34,56,53,0,67,49,37,37,22],
[45,38,37,33,40,42,33,0,34,60,25,32],
[54,44,68,45,51,48,51,66,0,53,46,50],
[46,45,43,52,56,53,63,40,47,0,38,44],
[47,50,71,61,60,65,63,75,54,62,0,62],
[67,46,61,68,66,67,78,68,50,56,38,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 46, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,54,50,46,50,52,42,47,43,57,46],
[51,0,46,45,44,43,52,37,42,44,50,52],
[46,54,0,50,47,47,45,48,52,46,55,47],
[50,55,50,0,54,48,50,50,47,46,56,50],
[54,56,53,46,0,54,49,43,51,46,59,55],
[50,57,53,52,46,0,52,51,51,44,57,54],
[48,48,55,50,51,48,0,47,54,47,55,51],
[58,63,52,50,57,49,53,0,61,55,57,60],
[53,58,48,53,49,49,46,39,0,51,54,58],
[57,56,54,54,54,56,53,45,49,0,57,64],
[43,50,45,44,41,43,45,43,46,43,0,51],
[54,48,53,50,45,46,49,40,42,36,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 47, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,70,52,59,56,54,49,60,59,60,53],
[61,0,62,63,73,62,65,52,59,73,65,50],
[30,38,0,47,50,48,57,36,42,56,47,36],
[48,37,53,0,73,55,71,54,46,68,67,51],
[41,27,50,27,0,47,46,28,48,49,48,40],
[44,38,52,45,53,0,59,51,52,62,62,46],
[46,35,43,29,54,41,0,41,39,52,50,42],
[51,48,64,46,72,49,59,0,56,66,55,53],
[40,41,58,54,52,48,61,44,0,48,50,36],
[41,27,44,32,51,38,48,34,52,0,49,40],
[40,35,53,33,52,38,50,45,50,51,0,40],
[47,50,64,49,60,54,58,47,64,60,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 48, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,27,64,55,53,62,45,65,60,61,53],
[49,0,54,51,60,60,75,62,60,72,70,53],
[73,46,0,75,70,56,83,64,75,68,89,61],
[36,49,25,0,57,49,68,42,54,54,48,46],
[45,40,30,43,0,42,51,36,38,54,39,40],
[47,40,44,51,58,0,58,56,50,52,44,49],
[38,25,17,32,49,42,0,33,52,44,50,48],
[55,38,36,58,64,44,67,0,73,60,50,54],
[35,40,25,46,62,50,48,27,0,44,49,54],
[40,28,32,46,46,48,56,40,56,0,60,51],
[39,30,11,52,61,56,50,50,51,40,0,41],
[47,47,39,54,60,51,52,46,46,49,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 49, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,44,57,45,43,58,51,54,53,55,51],
[47,0,48,53,52,43,56,45,61,51,48,54],
[56,52,0,57,49,49,57,43,53,46,42,52],
[43,47,43,0,39,39,47,40,45,45,46,54],
[55,48,51,61,0,45,66,49,59,52,63,51],
[57,57,51,61,55,0,58,47,64,52,59,63],
[42,44,43,53,34,42,0,30,54,40,47,48],
[49,55,57,60,51,53,70,0,61,63,47,56],
[46,39,47,55,41,36,46,39,0,43,49,56],
[47,49,54,55,48,48,60,37,57,0,59,52],
[45,52,58,54,37,41,53,53,51,41,0,49],
[49,46,48,46,49,37,52,44,44,48,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 50, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,42,41,41,46,45,41,43,50,56,52],
[57,0,42,46,45,54,43,45,46,51,53,43],
[58,58,0,47,55,55,54,45,55,64,55,57],
[59,54,53,0,55,53,62,48,57,56,54,58],
[59,55,45,45,0,58,45,32,42,50,56,50],
[54,46,45,47,42,0,55,41,43,48,50,49],
[55,57,46,38,55,45,0,49,43,54,52,51],
[59,55,55,52,68,59,51,0,51,62,47,56],
[57,54,45,43,58,57,57,49,0,53,54,52],
[50,49,36,44,50,52,46,38,47,0,50,47],
[44,47,45,46,44,50,48,53,46,50,0,46],
[48,57,43,42,50,51,49,44,48,53,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 51, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,52,48,37,48,44,54,48,42,38,44],
[52,0,53,50,49,53,51,51,53,50,47,48],
[48,47,0,51,41,50,44,62,49,43,40,45],
[52,50,49,0,44,40,49,59,48,46,36,39],
[63,51,59,56,0,59,58,59,65,43,50,55],
[52,47,50,60,41,0,48,49,53,44,39,36],
[56,49,56,51,42,52,0,55,49,50,50,54],
[46,49,38,41,41,51,45,0,50,45,30,44],
[52,47,51,52,35,47,51,50,0,48,38,48],
[58,50,57,54,57,56,50,55,52,0,43,47],
[62,53,60,64,50,61,50,70,62,57,0,49],
[56,52,55,61,45,64,46,56,52,53,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 52, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,66,64,54,62,73,77,55,62,65,52],
[50,0,65,78,50,44,58,72,53,65,62,51],
[34,35,0,62,30,38,48,63,44,58,47,36],
[36,22,38,0,27,35,50,48,37,55,45,32],
[46,50,70,73,0,58,62,77,58,68,61,50],
[38,56,62,65,42,0,57,69,59,65,56,37],
[27,42,52,50,38,43,0,71,29,49,29,32],
[23,28,37,52,23,31,29,0,32,52,43,36],
[45,47,56,63,42,41,71,68,0,68,50,51],
[38,35,42,45,32,35,51,48,32,0,38,23],
[35,38,53,55,39,44,71,57,50,62,0,46],
[48,49,64,68,50,63,68,64,49,77,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 53, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,56,56,64,58,58,57,48,51,55,58],
[45,0,57,49,56,52,55,53,47,55,55,61],
[44,43,0,52,41,48,45,42,43,41,46,56],
[44,51,48,0,53,55,56,51,49,54,45,50],
[36,44,59,47,0,54,50,46,41,47,43,52],
[42,48,52,45,46,0,49,45,44,45,54,51],
[42,45,55,44,50,51,0,50,41,49,47,57],
[43,47,58,49,54,55,50,0,50,54,45,57],
[52,53,57,51,59,56,59,50,0,55,54,67],
[49,45,59,46,53,55,51,46,45,0,43,61],
[45,45,54,55,57,46,53,55,46,57,0,59],
[42,39,44,50,48,49,43,43,33,39,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 54, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,68,62,53,69,67,49,50,70,64,57],
[41,0,52,45,50,57,53,45,52,61,51,61],
[32,48,0,49,48,56,61,39,52,52,48,56],
[38,55,51,0,52,75,64,40,56,64,62,60],
[47,50,52,48,0,64,51,50,52,69,58,59],
[31,43,44,25,36,0,53,38,46,61,44,35],
[33,47,39,36,49,47,0,29,59,54,42,59],
[51,55,61,60,50,62,71,0,53,70,74,63],
[50,48,48,44,48,54,41,47,0,59,58,50],
[30,39,48,36,31,39,46,30,41,0,45,34],
[36,49,52,38,42,56,58,26,42,55,0,50],
[43,39,44,40,41,65,41,37,50,66,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 55, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,53,49,45,58,52,50,58,43,47,52],
[52,0,62,62,51,57,58,51,54,52,49,54],
[47,38,0,47,45,59,53,49,45,50,42,49],
[51,38,53,0,45,49,48,51,45,40,41,46],
[55,49,55,55,0,54,59,62,53,45,52,56],
[42,43,41,51,46,0,52,43,46,41,38,47],
[48,42,47,52,41,48,0,50,54,41,36,53],
[50,49,51,49,38,57,50,0,55,45,47,48],
[42,46,55,55,47,54,46,45,0,43,38,52],
[57,48,50,60,55,59,59,55,57,0,48,53],
[53,51,58,59,48,62,64,53,62,52,0,54],
[48,46,51,54,44,53,47,52,48,47,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 56, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,66,54,47,47,27,48,67,27,47,58,36],
[34,0,48,43,35,21,43,40,32,36,35,43],
[46,52,0,47,35,33,36,48,33,35,44,42],
[53,57,53,0,55,38,49,55,39,49,50,57],
[53,65,65,45,0,45,55,62,43,50,43,49],
[73,79,67,62,55,0,66,83,57,67,66,50],
[52,57,64,51,45,34,0,68,44,37,55,53],
[33,60,52,45,38,17,32,0,21,31,34,37],
[73,68,67,61,57,43,56,79,0,55,54,57],
[53,64,65,51,50,33,63,69,45,0,52,51],
[42,65,56,50,57,34,45,66,46,48,0,51],
[64,57,58,43,51,50,47,63,43,49,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 57, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,54,55,51,56,58,49,56,50,44,52],
[54,0,59,59,50,53,60,46,60,53,52,53],
[46,41,0,53,49,46,51,45,54,49,46,52],
[45,41,47,0,48,53,53,41,51,44,44,50],
[49,50,51,52,0,48,52,49,53,49,53,53],
[44,47,54,47,52,0,56,40,53,48,48,48],
[42,40,49,47,48,44,0,44,47,50,43,39],
[51,54,55,59,51,60,56,0,61,50,47,53],
[44,40,46,49,47,47,53,39,0,48,46,47],
[50,47,51,56,51,52,50,50,52,0,51,52],
[56,48,54,56,47,52,57,53,54,49,0,48],
[48,47,48,50,47,52,61,47,53,48,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 58, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,45,46,45,47,47,55,52,44,58,43],
[49,0,50,54,50,46,46,56,58,46,59,54],
[55,50,0,45,54,47,43,56,55,53,57,57],
[54,46,55,0,49,52,50,55,54,52,52,50],
[55,50,46,51,0,51,43,56,57,50,54,51],
[53,54,53,48,49,0,44,55,49,47,53,55],
[53,54,57,50,57,56,0,56,58,52,62,54],
[45,44,44,45,44,45,44,0,48,47,46,48],
[48,42,45,46,43,51,42,52,0,48,54,50],
[56,54,47,48,50,53,48,53,52,0,53,52],
[42,41,43,48,46,47,38,54,46,47,0,46],
[57,46,43,50,49,45,46,52,50,48,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 59, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,58,50,55,56,46,58,54,50,59,50],
[46,0,56,48,45,48,42,44,48,43,47,44],
[42,44,0,43,40,50,45,51,43,42,42,48],
[50,52,57,0,51,56,49,48,50,45,55,50],
[45,55,60,49,0,56,50,48,48,49,50,48],
[44,52,50,44,44,0,39,42,43,44,44,40],
[54,58,55,51,50,61,0,55,46,48,50,46],
[42,56,49,52,52,58,45,0,52,46,49,48],
[46,52,57,50,52,57,54,48,0,50,47,45],
[50,57,58,55,51,56,52,54,50,0,53,53],
[41,53,58,45,50,56,50,51,53,47,0,50],
[50,56,52,50,52,60,54,52,55,47,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 60, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,45,54,56,53,48,43,57,49,48,53],
[55,0,45,47,53,42,53,45,50,37,48,50],
[55,55,0,60,60,53,49,52,54,48,56,61],
[46,53,40,0,59,49,54,44,56,55,53,54],
[44,47,40,41,0,43,52,45,48,41,36,50],
[47,58,47,51,57,0,45,40,47,50,41,44],
[52,47,51,46,48,55,0,47,50,50,48,60],
[57,55,48,56,55,60,53,0,53,55,57,53],
[43,50,46,44,52,53,50,47,0,52,42,55],
[51,63,52,45,59,50,50,45,48,0,48,50],
[52,52,44,47,64,59,52,43,58,52,0,55],
[47,50,39,46,50,56,40,47,45,50,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 61, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,38,40,40,44,42,44,46,42,37,46],
[56,0,50,50,55,52,49,34,65,49,50,60],
[62,50,0,49,55,62,51,51,61,59,51,55],
[60,50,51,0,39,63,52,45,48,47,45,55],
[60,45,45,61,0,62,56,38,58,52,57,50],
[56,48,38,37,38,0,45,34,49,36,43,46],
[58,51,49,48,44,55,0,45,55,56,53,45],
[56,66,49,55,62,66,55,0,57,55,41,60],
[54,35,39,52,42,51,45,43,0,38,48,49],
[58,51,41,53,48,64,44,45,62,0,51,55],
[63,50,49,55,43,57,47,59,52,49,0,60],
[54,40,45,45,50,54,55,40,51,45,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 62, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,45,50,40,39,38,41,42,47,47,31],
[65,0,70,69,53,60,51,55,57,44,56,58],
[55,30,0,39,43,39,34,32,41,43,45,49],
[50,31,61,0,46,43,42,39,42,43,45,37],
[60,47,57,54,0,49,42,65,53,45,57,47],
[61,40,61,57,51,0,38,42,59,41,55,40],
[62,49,66,58,58,62,0,55,59,39,58,42],
[59,45,68,61,35,58,45,0,59,48,51,39],
[58,43,59,58,47,41,41,41,0,36,54,51],
[53,56,57,57,55,59,61,52,64,0,55,48],
[53,44,55,55,43,45,42,49,46,45,0,45],
[69,42,51,63,53,60,58,61,49,52,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 63, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,44,52,46,51,49,54,53,48,51,46],
[47,0,42,50,51,51,45,46,51,46,61,42],
[56,58,0,56,58,52,57,57,56,57,64,49],
[48,50,44,0,48,49,52,45,49,46,45,42],
[54,49,42,52,0,45,43,51,49,49,54,45],
[49,49,48,51,55,0,46,45,41,44,53,56],
[51,55,43,48,57,54,0,58,54,47,56,46],
[46,54,43,55,49,55,42,0,53,50,56,47],
[47,49,44,51,51,59,46,47,0,44,50,41],
[52,54,43,54,51,56,53,50,56,0,55,47],
[49,39,36,55,46,47,44,44,50,45,0,43],
[54,58,51,58,55,44,54,53,59,53,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 64, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,53,58,52,48,44,56,46,56,56,52],
[48,0,46,45,37,52,38,45,39,50,49,55],
[47,54,0,60,43,50,38,53,47,37,47,46],
[42,55,40,0,43,40,37,55,34,44,43,51],
[48,63,57,57,0,58,56,57,47,50,58,64],
[52,48,50,60,42,0,28,51,40,41,47,44],
[56,62,62,63,44,72,0,58,58,52,65,61],
[44,55,47,45,43,49,42,0,45,36,38,55],
[54,61,53,66,53,60,42,55,0,55,46,57],
[44,50,63,56,50,59,48,64,45,0,52,64],
[44,51,53,57,42,53,35,62,54,48,0,64],
[48,45,54,49,36,56,39,45,43,36,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 65, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,45,50,50,43,42,55,45,49,46,50],
[49,0,38,46,50,46,45,53,42,56,49,46],
[55,62,0,53,64,56,55,65,48,54,53,61],
[50,54,47,0,56,55,46,58,45,49,56,57],
[50,50,36,44,0,41,38,54,38,48,46,52],
[57,54,44,45,59,0,49,55,45,54,51,49],
[58,55,45,54,62,51,0,52,49,57,55,58],
[45,47,35,42,46,45,48,0,38,44,46,43],
[55,58,52,55,62,55,51,62,0,52,50,53],
[51,44,46,51,52,46,43,56,48,0,54,53],
[54,51,47,44,54,49,45,54,50,46,0,52],
[50,54,39,43,48,51,42,57,47,47,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 66, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,48,54,43,48,49,50,48,48,44,48],
[55,0,49,60,56,63,56,56,50,65,50,51],
[52,51,0,51,49,59,51,54,51,55,53,50],
[46,40,49,0,47,49,47,43,41,52,46,38],
[57,44,51,53,0,54,59,55,41,59,56,43],
[52,37,41,51,46,0,46,51,42,54,47,48],
[51,44,49,53,41,54,0,47,42,49,36,44],
[50,44,46,57,45,49,53,0,47,50,51,45],
[52,50,49,59,59,58,58,53,0,56,54,50],
[52,35,45,48,41,46,51,50,44,0,41,43],
[56,50,47,54,44,53,64,49,46,59,0,43],
[52,49,50,62,57,52,56,55,50,57,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 67, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,48,48,46,47,57,60,55,59,59,50],
[45,0,43,62,54,48,53,55,49,58,63,44],
[52,57,0,54,43,56,40,50,36,49,55,44],
[52,38,46,0,50,38,48,51,57,53,57,43],
[54,46,57,50,0,48,57,60,51,58,58,45],
[53,52,44,62,52,0,54,56,51,53,58,40],
[43,47,60,52,43,46,0,54,42,53,50,41],
[40,45,50,49,40,44,46,0,39,54,49,42],
[45,51,64,43,49,49,58,61,0,50,62,43],
[41,42,51,47,42,47,47,46,50,0,51,47],
[41,37,45,43,42,42,50,51,38,49,0,41],
[50,56,56,57,55,60,59,58,57,53,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 68, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,62,58,55,67,70,55,51,63,55,68],
[50,0,56,50,54,53,55,59,56,52,51,56],
[38,44,0,40,50,47,49,53,42,50,52,48],
[42,50,60,0,56,58,59,59,57,62,60,61],
[45,46,50,44,0,50,52,49,52,55,47,56],
[33,47,53,42,50,0,54,58,55,42,52,53],
[30,45,51,41,48,46,0,48,45,46,44,43],
[45,41,47,41,51,42,52,0,44,53,45,48],
[49,44,58,43,48,45,55,56,0,57,62,48],
[37,48,50,38,45,58,54,47,43,0,49,54],
[45,49,48,40,53,48,56,55,38,51,0,45],
[32,44,52,39,44,47,57,52,52,46,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 69, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,46,53,43,41,52,51,45,47,50,45],
[56,0,48,51,45,51,51,52,54,48,51,51],
[54,52,0,56,55,51,65,49,58,50,54,53],
[47,49,44,0,42,49,49,40,54,47,46,45],
[57,55,45,58,0,44,55,55,55,45,58,60],
[59,49,49,51,56,0,46,53,56,49,56,52],
[48,49,35,51,45,54,0,49,56,46,48,43],
[49,48,51,60,45,47,51,0,51,55,53,53],
[55,46,42,46,45,44,44,49,0,47,46,44],
[53,52,50,53,55,51,54,45,53,0,48,50],
[50,49,46,54,42,44,52,47,54,52,0,50],
[55,49,47,55,40,48,57,47,56,50,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 70, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,41,38,51,40,53,30,33,44,28,48],
[59,0,49,66,68,63,60,49,57,70,52,56],
[59,51,0,60,53,55,48,48,47,55,63,52],
[62,34,40,0,68,59,50,26,42,44,43,37],
[49,32,47,32,0,33,35,31,39,32,39,38],
[60,37,45,41,67,0,49,42,46,44,51,52],
[47,40,52,50,65,51,0,47,44,40,39,58],
[70,51,52,74,69,58,53,0,59,56,41,58],
[67,43,53,58,61,54,56,41,0,49,53,49],
[56,30,45,56,68,56,60,44,51,0,40,56],
[72,48,37,57,61,49,61,59,47,60,0,63],
[52,44,48,63,62,48,42,42,51,44,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 71, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,51,53,43,48,49,50,52,47,57,51],
[44,0,49,44,38,47,39,39,55,45,50,49],
[49,51,0,52,46,44,44,51,58,48,57,48],
[47,56,48,0,42,48,46,43,49,41,50,49],
[57,62,54,58,0,60,51,50,50,47,56,58],
[52,53,56,52,40,0,46,44,45,43,57,55],
[51,61,56,54,49,54,0,48,54,49,58,58],
[50,61,49,57,50,56,52,0,56,53,62,53],
[48,45,42,51,50,55,46,44,0,43,58,43],
[53,55,52,59,53,57,51,47,57,0,58,45],
[43,50,43,50,44,43,42,38,42,42,0,44],
[49,51,52,51,42,45,42,47,57,55,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 72, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,65,51,55,56,58,50,58,63,46,56],
[39,0,58,51,58,47,25,49,38,53,47,42],
[35,42,0,39,39,32,22,29,38,41,33,39],
[49,49,61,0,69,65,37,54,46,61,70,49],
[45,42,61,31,0,41,30,32,36,42,28,31],
[44,53,68,35,59,0,32,32,44,63,44,36],
[42,75,78,63,70,68,0,63,64,71,57,66],
[50,51,71,46,68,68,37,0,52,70,42,59],
[42,62,62,54,64,56,36,48,0,62,62,60],
[37,47,59,39,58,37,29,30,38,0,48,52],
[54,53,67,30,72,56,43,58,38,52,0,34],
[44,58,61,51,69,64,34,41,40,48,66,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 73, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,71,39,57,57,68,73,45,64,68,52,71],
[29,0,31,35,43,45,44,31,61,43,39,46],
[61,69,0,42,75,51,67,52,68,51,54,64],
[43,65,58,0,48,62,73,43,70,68,57,53],
[43,57,25,52,0,50,62,31,55,48,42,53],
[32,55,49,38,50,0,42,39,56,47,49,58],
[27,56,33,27,38,58,0,42,60,53,43,50],
[55,69,48,57,69,61,58,0,69,49,51,50],
[36,39,32,30,45,44,40,31,0,54,24,44],
[32,57,49,32,52,53,47,51,46,0,48,51],
[48,61,46,43,58,51,57,49,76,52,0,52],
[29,54,36,47,47,42,50,50,56,49,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 74, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,52,60,56,53,56,63,53,56,48,52],
[43,0,57,51,49,54,50,57,51,44,44,48],
[48,43,0,66,54,51,53,52,52,51,43,48],
[40,49,34,0,44,44,38,46,45,42,37,35],
[44,51,46,56,0,55,49,56,59,48,48,51],
[47,46,49,56,45,0,51,54,45,43,45,46],
[44,50,47,62,51,49,0,58,48,48,48,51],
[37,43,48,54,44,46,42,0,42,44,37,38],
[47,49,48,55,41,55,52,58,0,52,43,48],
[44,56,49,58,52,57,52,56,48,0,44,49],
[52,56,57,63,52,55,52,63,57,56,0,48],
[48,52,52,65,49,54,49,62,52,51,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 75, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,44,46,38,42,48,53,44,42,50,47],
[50,0,45,45,52,35,49,48,56,52,50,49],
[56,55,0,43,46,41,51,54,52,42,56,50],
[54,55,57,0,47,44,49,57,54,51,55,53],
[62,48,54,53,0,44,47,47,47,48,55,42],
[58,65,59,56,56,0,50,59,58,49,65,53],
[52,51,49,51,53,50,0,55,56,49,52,52],
[47,52,46,43,53,41,45,0,55,45,46,46],
[56,44,48,46,53,42,44,45,0,47,53,50],
[58,48,58,49,52,51,51,55,53,0,56,49],
[50,50,44,45,45,35,48,54,47,44,0,39],
[53,51,50,47,58,47,48,54,50,51,61,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 76, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,59,49,56,47,43,57,62,52,49,56],
[54,0,54,60,58,50,61,47,55,52,48,54],
[41,46,0,52,51,46,52,43,42,58,48,57],
[51,40,48,0,50,46,53,47,58,53,56,55],
[44,42,49,50,0,46,39,60,53,57,53,51],
[53,50,54,54,54,0,47,50,50,57,47,58],
[57,39,48,47,61,53,0,47,47,46,54,46],
[43,53,57,53,40,50,53,0,59,55,48,49],
[38,45,58,42,47,50,53,41,0,57,54,52],
[48,48,42,47,43,43,54,45,43,0,40,54],
[51,52,52,44,47,53,46,52,46,60,0,62],
[44,46,43,45,49,42,54,51,48,46,38,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 77, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,75,76,34,53,46,56,91,76,75,67,91],
[25,0,38,34,53,38,43,71,71,37,25,63],
[24,62,0,33,24,55,42,61,90,46,53,62],
[66,66,67,0,67,66,37,85,66,66,67,66],
[47,47,76,33,0,75,27,90,75,75,38,47],
[54,62,45,34,25,0,43,63,63,90,54,63],
[44,57,58,63,73,57,0,91,91,57,67,91],
[9,29,39,15,10,37,9,0,29,57,38,29],
[24,29,10,34,25,37,9,71,0,37,39,62],
[25,63,54,34,25,10,43,43,63,0,54,63],
[33,75,47,33,62,46,33,62,61,46,0,90],
[9,37,38,34,53,37,9,71,38,37,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 78, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,65,50,51,51,33,53,56,57,38,58,55],
[35,0,34,41,49,40,33,30,43,46,36,41],
[50,66,0,65,66,56,45,64,46,51,71,67],
[49,59,35,0,60,41,35,62,37,53,33,46],
[49,51,34,40,0,37,46,52,56,52,42,49],
[67,60,44,59,63,0,45,50,54,50,65,35],
[47,67,55,65,54,55,0,58,65,41,61,71],
[44,70,36,38,48,50,42,0,38,45,54,55],
[43,57,54,63,44,46,35,62,0,53,45,48],
[62,54,49,47,48,50,59,55,47,0,57,58],
[42,64,29,67,58,35,39,46,55,43,0,44],
[45,59,33,54,51,65,29,45,52,42,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 79, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,61,44,48,52,44,53,63,45,64,63],
[58,0,53,52,54,52,43,57,61,55,58,61],
[39,47,0,43,43,47,43,45,50,51,52,54],
[56,48,57,0,48,51,50,50,49,49,52,51],
[52,46,57,52,0,45,54,49,60,53,54,59],
[48,48,53,49,55,0,38,54,57,52,58,61],
[56,57,57,50,46,62,0,60,53,49,60,62],
[47,43,55,50,51,46,40,0,49,53,53,56],
[37,39,50,51,40,43,47,51,0,41,55,51],
[55,45,49,51,47,48,51,47,59,0,54,66],
[36,42,48,48,46,42,40,47,45,46,0,51],
[37,39,46,49,41,39,38,44,49,34,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 80, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,37,31,42,52,52,46,53,52,44,46,38],
[63,0,50,53,54,58,68,66,46,58,68,56],
[69,50,0,58,52,58,64,64,64,64,66,60],
[58,47,42,0,57,59,55,52,52,50,51,52],
[48,46,48,43,0,43,53,51,48,49,50,38],
[48,42,42,41,57,0,46,58,50,51,49,52],
[54,32,36,45,47,54,0,45,53,45,46,43],
[47,34,36,48,49,42,55,0,46,48,39,47],
[48,54,36,48,52,50,47,54,0,50,51,47],
[56,42,36,50,51,49,55,52,50,0,61,48],
[54,32,34,49,50,51,54,61,49,39,0,39],
[62,44,40,48,62,48,57,53,53,52,61,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 81, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,56,48,51,50,50,49,47,41,52,51],
[48,0,56,47,55,55,49,56,50,59,47,57],
[44,44,0,33,38,55,53,47,39,51,40,40],
[52,53,67,0,58,52,50,58,63,58,55,60],
[49,45,62,42,0,57,48,45,51,57,49,53],
[50,45,45,48,43,0,48,43,42,46,48,42],
[50,51,47,50,52,52,0,55,43,57,49,49],
[51,44,53,42,55,57,45,0,47,38,41,41],
[53,50,61,37,49,58,57,53,0,53,47,44],
[59,41,49,42,43,54,43,62,47,0,44,56],
[48,53,60,45,51,52,51,59,53,56,0,48],
[49,43,60,40,47,58,51,59,56,44,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 82, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,57,52,51,70,28,43,55,59,28,44],
[45,0,58,46,32,70,51,44,79,59,49,61],
[43,42,0,43,47,56,32,59,60,46,46,42],
[48,54,57,0,39,63,54,55,67,61,51,57],
[49,68,53,61,0,60,41,37,63,69,52,54],
[30,30,44,37,40,0,40,34,40,51,41,40],
[72,49,68,46,59,60,0,52,53,57,33,42],
[57,56,41,45,63,66,48,0,53,65,32,58],
[45,21,40,33,37,60,47,47,0,49,33,52],
[41,41,54,39,31,49,43,35,51,0,17,40],
[72,51,54,49,48,59,67,68,67,83,0,64],
[56,39,58,43,46,60,58,42,48,60,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 83, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,53,45,50,32,58,45,49,39,52,52],
[52,0,51,52,59,53,49,54,55,54,55,57],
[47,49,0,55,58,47,44,46,51,36,51,45],
[55,48,45,0,50,49,40,48,53,40,52,36],
[50,41,42,50,0,51,46,51,53,45,41,42],
[68,47,53,51,49,0,51,49,62,48,61,56],
[42,51,56,60,54,49,0,50,63,39,64,43],
[55,46,54,52,49,51,50,0,51,46,56,45],
[51,45,49,47,47,38,37,49,0,39,55,47],
[61,46,64,60,55,52,61,54,61,0,67,60],
[48,45,49,48,59,39,36,44,45,33,0,39],
[48,43,55,64,58,44,57,55,53,40,61,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 84, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,51,46,46,53,50,52,63,56,54,55],
[55,0,46,48,54,54,59,56,59,55,54,62],
[49,54,0,51,50,52,49,46,58,55,54,54],
[54,52,49,0,58,60,53,53,63,53,59,61],
[54,46,50,42,0,53,60,47,61,54,48,55],
[47,46,48,40,47,0,50,46,58,51,46,54],
[50,41,51,47,40,50,0,47,48,52,44,51],
[48,44,54,47,53,54,53,0,57,59,53,55],
[37,41,42,37,39,42,52,43,0,48,41,49],
[44,45,45,47,46,49,48,41,52,0,54,48],
[46,46,46,41,52,54,56,47,59,46,0,52],
[45,38,46,39,45,46,49,45,51,52,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 85, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,58,50,43,54,58,48,64,41,59,55],
[55,0,64,45,42,54,55,56,58,45,54,49],
[42,36,0,43,41,45,47,37,48,34,50,36],
[50,55,57,0,42,59,59,51,54,42,53,44],
[57,58,59,58,0,61,55,58,60,47,61,50],
[46,46,55,41,39,0,54,47,56,42,50,43],
[42,45,53,41,45,46,0,48,54,39,55,46],
[52,44,63,49,42,53,52,0,61,42,57,45],
[36,42,52,46,40,44,46,39,0,31,50,39],
[59,55,66,58,53,58,61,58,69,0,60,47],
[41,46,50,47,39,50,45,43,50,40,0,38],
[45,51,64,56,50,57,54,55,61,53,62,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 86, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,53,64,57,50,67,67,54,61,49,71],
[42,0,48,26,41,17,21,51,60,26,42,41],
[47,52,0,47,44,27,51,54,46,45,22,53],
[36,74,53,0,61,37,50,50,53,56,45,69],
[43,59,56,39,0,38,48,60,38,41,42,48],
[50,83,73,63,62,0,68,66,67,50,48,57],
[33,79,49,50,52,32,0,72,54,37,50,58],
[33,49,46,50,40,34,28,0,30,38,45,63],
[46,40,54,47,62,33,46,70,0,39,23,60],
[39,74,55,44,59,50,63,62,61,0,45,53],
[51,58,78,55,58,52,50,55,77,55,0,72],
[29,59,47,31,52,43,42,37,40,47,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 87, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,63,48,39,54,40,48,57,27,42,54],
[47,0,56,40,28,26,54,36,31,29,37,53],
[37,44,0,32,30,27,33,39,24,30,42,43],
[52,60,68,0,54,54,44,54,46,51,61,46],
[61,72,70,46,0,41,55,54,39,42,44,58],
[46,74,73,46,59,0,54,47,70,43,73,51],
[60,46,67,56,45,46,0,54,43,37,69,55],
[52,64,61,46,46,53,46,0,52,34,53,44],
[43,69,76,54,61,30,57,48,0,36,62,46],
[73,71,70,49,58,57,63,66,64,0,72,58],
[58,63,58,39,56,27,31,47,38,28,0,47],
[46,47,57,54,42,49,45,56,54,42,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 88, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,58,48,48,52,51,57,46,46,46,59],
[44,0,58,47,49,50,49,51,46,48,51,56],
[42,42,0,46,48,37,41,41,46,45,36,46],
[52,53,54,0,56,54,55,56,48,50,47,65],
[52,51,52,44,0,52,47,53,47,56,42,55],
[48,50,63,46,48,0,49,52,46,50,47,55],
[49,51,59,45,53,51,0,51,50,52,43,57],
[43,49,59,44,47,48,49,0,48,46,42,49],
[54,54,54,52,53,54,50,52,0,56,52,56],
[54,52,55,50,44,50,48,54,44,0,44,54],
[54,49,64,53,58,53,57,58,48,56,0,61],
[41,44,54,35,45,45,43,51,44,46,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 89, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,37,41,52,44,48,58,70,51,38,41,35],
[63,0,66,72,78,75,58,70,54,40,39,80],
[59,34,0,52,61,65,57,62,54,45,48,63],
[48,28,48,0,43,74,47,51,55,48,21,30],
[56,22,39,57,0,69,60,45,30,39,31,56],
[52,25,35,26,31,0,35,35,27,24,20,56],
[42,42,43,53,40,65,0,58,34,41,44,52],
[30,30,38,49,55,65,42,0,5,58,41,48],
[49,46,46,45,70,73,66,95,0,66,66,44],
[62,60,55,52,61,76,59,42,34,0,30,63],
[59,61,52,79,69,80,56,59,34,70,0,60],
[65,20,37,70,44,44,48,52,56,37,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 90, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,39,53,49,43,44,51,42,43,49,48],
[55,0,46,54,53,46,52,50,53,50,51,53],
[61,54,0,56,50,48,52,51,48,52,53,41],
[47,46,44,0,50,45,46,50,44,45,50,47],
[51,47,50,50,0,45,52,56,49,42,56,52],
[57,54,52,55,55,0,67,45,54,57,54,51],
[56,48,48,54,48,33,0,41,33,50,43,54],
[49,50,49,50,44,55,59,0,46,52,52,49],
[58,47,52,56,51,46,67,54,0,53,44,53],
[57,50,48,55,58,43,50,48,47,0,53,46],
[51,49,47,50,44,46,57,48,56,47,0,46],
[52,47,59,53,48,49,46,51,47,54,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 91, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,51,45,39,40,47,37,47,41,39,28],
[59,0,69,50,59,57,61,68,62,60,68,53],
[49,31,0,42,41,43,48,41,38,40,41,33],
[55,50,58,0,49,52,65,55,58,57,60,32],
[61,41,59,51,0,51,62,55,50,60,47,51],
[60,43,57,48,49,0,56,50,55,51,54,38],
[53,39,52,35,38,44,0,43,56,41,50,38],
[63,32,59,45,45,50,57,0,49,54,52,38],
[53,38,62,42,50,45,44,51,0,53,51,43],
[59,40,60,43,40,49,59,46,47,0,57,55],
[61,32,59,40,53,46,50,48,49,43,0,45],
[72,47,67,68,49,62,62,62,57,45,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 92, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,45,43,47,48,50,43,54,46,48,52],
[55,0,45,44,47,49,48,47,48,50,53,49],
[55,55,0,44,47,50,46,47,47,53,51,53],
[57,56,56,0,52,54,50,50,55,53,45,56],
[53,53,53,48,0,57,52,49,54,55,49,52],
[52,51,50,46,43,0,48,39,50,52,46,48],
[50,52,54,50,48,52,0,45,49,49,51,54],
[57,53,53,50,51,61,55,0,55,52,55,53],
[46,52,53,45,46,50,51,45,0,51,48,52],
[54,50,47,47,45,48,51,48,49,0,50,47],
[52,47,49,55,51,54,49,45,52,50,0,54],
[48,51,47,44,48,52,46,47,48,53,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 93, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,60,46,54,55,51,54,49,54,50,54],
[42,0,40,41,47,44,51,50,50,45,50,49],
[40,60,0,48,59,55,48,53,52,51,51,56],
[54,59,52,0,57,50,54,58,49,51,56,55],
[46,53,41,43,0,49,53,51,49,42,53,56],
[45,56,45,50,51,0,50,54,54,49,53,55],
[49,49,52,46,47,50,0,51,42,51,51,49],
[46,50,47,42,49,46,49,0,41,44,44,53],
[51,50,48,51,51,46,58,59,0,56,52,55],
[46,55,49,49,58,51,49,56,44,0,47,54],
[50,50,49,44,47,47,49,56,48,53,0,50],
[46,51,44,45,44,45,51,47,45,46,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 94, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,41,40,51,49,47,54,54,52,53,49],
[48,0,43,43,52,47,38,36,55,54,52,60],
[59,57,0,54,60,45,52,43,60,53,56,58],
[60,57,46,0,56,44,44,48,59,61,63,61],
[49,48,40,44,0,49,43,48,55,61,56,56],
[51,53,55,56,51,0,39,47,62,54,64,61],
[53,62,48,56,57,61,0,51,58,59,56,66],
[46,64,57,52,52,53,49,0,58,61,57,64],
[46,45,40,41,45,38,42,42,0,56,52,40],
[48,46,47,39,39,46,41,39,44,0,49,50],
[47,48,44,37,44,36,44,43,48,51,0,44],
[51,40,42,39,44,39,34,36,60,50,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 95, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,45,54,47,42,51,49,51,47,49,44],
[54,0,52,69,50,49,60,49,48,48,57,51],
[55,48,0,61,60,54,56,53,53,51,52,46],
[46,31,39,0,46,46,44,47,45,43,48,50],
[53,50,40,54,0,45,67,49,44,49,52,45],
[58,51,46,54,55,0,66,59,53,53,47,48],
[49,40,44,56,33,34,0,48,50,41,46,44],
[51,51,47,53,51,41,52,0,50,46,50,42],
[49,52,47,55,56,47,50,50,0,41,51,44],
[53,52,49,57,51,47,59,54,59,0,62,56],
[51,43,48,52,48,53,54,50,49,38,0,51],
[56,49,54,50,55,52,56,58,56,44,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 96, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,45,46,36,26,27,29,50,46,55,28],
[72,0,46,80,67,44,47,73,62,55,46,50],
[55,54,0,48,55,53,60,63,69,45,56,61],
[54,20,52,0,25,41,56,52,61,42,25,28],
[64,33,45,75,0,38,32,52,54,62,40,27],
[74,56,47,59,62,0,46,64,57,47,49,58],
[73,53,40,44,68,54,0,52,68,62,38,42],
[71,27,37,48,48,36,48,0,48,43,31,30],
[50,38,31,39,46,43,32,52,0,39,41,53],
[54,45,55,58,38,53,38,57,61,0,42,42],
[45,54,44,75,60,51,62,69,59,58,0,60],
[72,50,39,72,73,42,58,70,47,58,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 97, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,63,60,39,44,58,38,45,29,50,53],
[57,0,61,49,52,45,70,50,61,42,37,60],
[37,39,0,41,26,46,52,38,28,22,33,38],
[40,51,59,0,54,51,63,56,37,33,55,49],
[61,48,74,46,0,52,68,43,38,41,42,59],
[56,55,54,49,48,0,50,51,44,23,44,66],
[42,30,48,37,32,50,0,47,41,32,37,50],
[62,50,62,44,57,49,53,0,39,39,39,47],
[55,39,72,63,62,56,59,61,0,54,40,68],
[71,58,78,67,59,77,68,61,46,0,51,65],
[50,63,67,45,58,56,63,61,60,49,0,59],
[47,40,62,51,41,34,50,53,32,35,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 98, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,59,94,70,64,60,59,50,67,73,72],
[38,0,45,51,33,17,38,34,38,30,29,42],
[41,55,0,60,46,35,50,46,47,46,32,63],
[6,49,40,0,54,33,18,42,31,44,28,45],
[30,67,54,46,0,42,46,61,56,62,34,49],
[36,83,65,67,58,0,61,65,59,80,54,83],
[40,62,50,82,54,39,0,55,52,55,51,59],
[41,66,54,58,39,35,45,0,45,50,32,68],
[50,62,53,69,44,41,48,55,0,55,47,47],
[33,70,54,56,38,20,45,50,45,0,45,61],
[27,71,68,72,66,46,49,68,53,55,0,55],
[28,58,37,55,51,17,41,32,53,39,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 99, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,63,43,52,24,55,53,57,66,46,33],
[46,0,74,55,42,46,12,35,47,51,43,34],
[37,26,0,23,38,37,18,34,41,56,42,23],
[57,45,77,0,56,60,51,50,58,50,57,38],
[48,58,62,44,0,48,36,46,45,74,35,28],
[76,54,63,40,52,0,59,65,51,67,29,45],
[45,88,82,49,64,41,0,42,66,70,54,61],
[47,65,66,50,54,35,58,0,59,35,55,42],
[43,53,59,42,55,49,34,41,0,50,45,38],
[34,49,44,50,26,33,30,65,50,0,41,23],
[54,57,58,43,65,71,46,45,55,59,0,48],
[67,66,77,62,72,55,39,58,62,77,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 100, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,59,49,53,58,60,57,55,50,53,50],
[48,0,60,48,51,56,55,56,45,53,48,46],
[41,40,0,43,43,47,48,41,51,48,40,45],
[51,52,57,0,46,56,61,49,46,48,53,44],
[47,49,57,54,0,59,60,51,58,50,55,48],
[42,44,53,44,41,0,55,39,36,60,47,51],
[40,45,52,39,40,45,0,50,40,48,41,43],
[43,44,59,51,49,61,50,0,43,54,53,45],
[45,55,49,54,42,64,60,57,0,56,55,49],
[50,47,52,52,50,40,52,46,44,0,50,42],
[47,52,60,47,45,53,59,47,45,50,0,44],
[50,54,55,56,52,49,57,55,51,58,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 101, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,48,55,48,52,57,59,50,58,52,73],
[49,0,50,44,42,44,51,58,61,60,43,62],
[52,50,0,45,38,52,55,63,56,56,40,60],
[45,56,55,0,28,60,35,58,58,65,52,79],
[52,58,62,72,0,59,49,43,47,54,53,67],
[48,56,48,40,41,0,33,61,55,55,56,63],
[43,49,45,65,51,67,0,69,49,65,50,82],
[41,42,37,42,57,39,31,0,50,44,46,54],
[50,39,44,42,53,45,51,50,0,62,53,60],
[42,40,44,35,46,45,35,56,38,0,49,49],
[48,57,60,48,47,44,50,54,47,51,0,63],
[27,38,40,21,33,37,18,46,40,51,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 102, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,54,57,51,51,50,53,51,53,56,54],
[52,0,52,51,45,50,48,53,49,49,52,45],
[46,48,0,46,47,50,50,48,45,51,52,49],
[43,49,54,0,47,53,52,45,52,42,53,45],
[49,55,53,53,0,53,54,55,54,51,55,53],
[49,50,50,47,47,0,44,53,45,46,52,44],
[50,52,50,48,46,56,0,49,48,45,49,50],
[47,47,52,55,45,47,51,0,44,53,55,51],
[49,51,55,48,46,55,52,56,0,52,58,50],
[47,51,49,58,49,54,55,47,48,0,51,52],
[44,48,48,47,45,48,51,45,42,49,0,46],
[46,55,51,55,47,56,50,49,50,48,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 103, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,53,55,46,40,47,53,60,56,46,54],
[55,0,56,57,58,41,51,53,41,52,43,48],
[47,44,0,53,54,36,53,48,44,54,49,57],
[45,43,47,0,51,50,48,51,44,45,48,56],
[54,42,46,49,0,48,57,62,51,44,57,55],
[60,59,64,50,52,0,55,63,53,69,62,66],
[53,49,47,52,43,45,0,43,32,45,43,40],
[47,47,52,49,38,37,57,0,42,51,54,68],
[40,59,56,56,49,47,68,58,0,52,53,78],
[44,48,46,55,56,31,55,49,48,0,45,54],
[54,57,51,52,43,38,57,46,47,55,0,61],
[46,52,43,44,45,34,60,32,22,46,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 104, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,40,39,39,51,42,44,43,50,48,44],
[53,0,40,38,45,57,48,47,45,51,52,51],
[60,60,0,46,53,62,51,50,50,59,55,58],
[61,62,54,0,59,59,55,64,49,63,56,58],
[61,55,47,41,0,62,54,46,47,59,55,53],
[49,43,38,41,38,0,48,41,45,51,55,50],
[58,52,49,45,46,52,0,50,53,55,53,52],
[56,53,50,36,54,59,50,0,52,52,47,54],
[57,55,50,51,53,55,47,48,0,57,61,53],
[50,49,41,37,41,49,45,48,43,0,44,46],
[52,48,45,44,45,45,47,53,39,56,0,57],
[56,49,42,42,47,50,48,46,47,54,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 105, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,50,51,52,48,47,56,43,42,45,46],
[58,0,45,49,50,46,55,54,41,47,48,46],
[50,55,0,56,52,51,50,55,44,47,50,50],
[49,51,44,0,48,49,49,55,36,45,36,44],
[48,50,48,52,0,46,50,51,38,47,40,41],
[52,54,49,51,54,0,50,56,40,47,46,47],
[53,45,50,51,50,50,0,55,42,44,44,45],
[44,46,45,45,49,44,45,0,38,42,45,42],
[57,59,56,64,62,60,58,62,0,49,50,57],
[58,53,53,55,53,53,56,58,51,0,52,46],
[55,52,50,64,60,54,56,55,50,48,0,47],
[54,54,50,56,59,53,55,58,43,54,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 106, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,48,44,47,39,44,46,48,42,46,43],
[54,0,45,46,44,50,45,46,50,50,51,47],
[52,55,0,54,45,55,57,57,53,50,53,51],
[56,54,46,0,53,55,52,59,59,52,50,49],
[53,56,55,47,0,51,51,57,53,54,45,54],
[61,50,45,45,49,0,47,49,50,52,44,45],
[56,55,43,48,49,53,0,58,52,54,48,49],
[54,54,43,41,43,51,42,0,49,48,47,47],
[52,50,47,41,47,50,48,51,0,49,44,42],
[58,50,50,48,46,48,46,52,51,0,46,49],
[54,49,47,50,55,56,52,53,56,54,0,54],
[57,53,49,51,46,55,51,53,58,51,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 107, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,55,48,48,55,47,36,55,59,46,42],
[51,0,51,64,53,51,55,37,63,59,60,49],
[45,49,0,48,56,52,52,42,62,49,58,45],
[52,36,52,0,44,42,40,40,64,55,44,35],
[52,47,44,56,0,55,57,41,67,50,51,44],
[45,49,48,58,45,0,54,37,70,52,53,51],
[53,45,48,60,43,46,0,40,66,53,53,58],
[64,63,58,60,59,63,60,0,67,65,61,46],
[45,37,38,36,33,30,34,33,0,36,40,34],
[41,41,51,45,50,48,47,35,64,0,54,51],
[54,40,42,56,49,47,47,39,60,46,0,47],
[58,51,55,65,56,49,42,54,66,49,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 108, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,51,53,51,56,49,47,58,46,53,47],
[55,0,58,56,62,57,52,49,55,54,51,56],
[49,42,0,44,47,47,50,45,50,43,40,45],
[47,44,56,0,51,47,51,44,48,44,48,49],
[49,38,53,49,0,45,45,48,46,46,46,43],
[44,43,53,53,55,0,46,41,52,53,49,48],
[51,48,50,49,55,54,0,52,50,46,49,44],
[53,51,55,56,52,59,48,0,49,47,50,52],
[42,45,50,52,54,48,50,51,0,51,46,51],
[54,46,57,56,54,47,54,53,49,0,50,53],
[47,49,60,52,54,51,51,50,54,50,0,51],
[53,44,55,51,57,52,56,48,49,47,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 109, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,57,33,41,38,65,50,43,58,51,38],
[47,0,61,50,61,57,63,45,56,56,57,49],
[43,39,0,35,46,48,63,39,43,51,51,37],
[67,50,65,0,44,51,61,39,53,70,62,59],
[59,39,54,56,0,59,73,46,51,66,49,44],
[62,43,52,49,41,0,62,33,56,64,48,54],
[35,37,37,39,27,38,0,37,36,45,35,27],
[50,55,61,61,54,67,63,0,65,51,70,58],
[57,44,57,47,49,44,64,35,0,53,57,49],
[42,44,49,30,34,36,55,49,47,0,49,32],
[49,43,49,38,51,52,65,30,43,51,0,44],
[62,51,63,41,56,46,73,42,51,68,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 110, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,59,56,59,61,59,59,47,58,52,58],
[49,0,52,55,55,42,50,56,44,53,43,53],
[41,48,0,46,55,41,41,56,34,50,46,50],
[44,45,54,0,58,44,44,60,46,57,51,47],
[41,45,45,42,0,43,46,55,39,46,40,39],
[39,58,59,56,57,0,57,60,54,62,55,55],
[41,50,59,56,54,43,0,61,51,52,50,51],
[41,44,44,40,45,40,39,0,40,43,42,48],
[53,56,66,54,61,46,49,60,0,54,47,52],
[42,47,50,43,54,38,48,57,46,0,47,45],
[48,57,54,49,60,45,50,58,53,53,0,50],
[42,47,50,53,61,45,49,52,48,55,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 111, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,65,54,55,54,48,47,50,64,41,62,45],
[35,0,45,45,52,46,46,48,55,31,44,39],
[46,55,0,61,59,39,58,52,57,44,56,38],
[45,55,39,0,52,43,43,51,52,36,50,36],
[46,48,41,48,0,47,40,43,53,36,58,41],
[52,54,61,57,53,0,53,56,65,40,55,51],
[53,54,42,57,60,47,0,41,48,42,57,46],
[50,52,48,49,57,44,59,0,58,36,52,52],
[36,45,43,48,47,35,52,42,0,35,49,33],
[59,69,56,64,64,60,58,64,65,0,64,49],
[38,56,44,50,42,45,43,48,51,36,0,44],
[55,61,62,64,59,49,54,48,67,51,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 112, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,50,62,63,67,55,50,72,69,45,62],
[45,0,47,50,59,46,64,43,55,45,49,59],
[50,53,0,40,64,57,54,62,61,45,50,68],
[38,50,60,0,75,61,60,49,65,64,44,63],
[37,41,36,25,0,47,47,53,52,54,29,49],
[33,54,43,39,53,0,40,52,46,58,29,40],
[45,36,46,40,53,60,0,53,61,58,34,52],
[50,57,38,51,47,48,47,0,54,46,37,52],
[28,45,39,35,48,54,39,46,0,44,39,44],
[31,55,55,36,46,42,42,54,56,0,36,51],
[55,51,50,56,71,71,66,63,61,64,0,68],
[38,41,32,37,51,60,48,48,56,49,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 113, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,53,54,61,51,50,60,62,45,54,68],
[44,0,50,44,52,53,51,50,53,42,49,63],
[47,50,0,44,45,47,44,52,51,33,45,49],
[46,56,56,0,55,54,42,48,55,54,57,55],
[39,48,55,45,0,48,40,38,47,37,49,47],
[49,47,53,46,52,0,43,49,59,36,48,65],
[50,49,56,58,60,57,0,42,50,39,59,63],
[40,50,48,52,62,51,58,0,50,51,44,57],
[38,47,49,45,53,41,50,50,0,38,42,55],
[55,58,67,46,63,64,61,49,62,0,57,67],
[46,51,55,43,51,52,41,56,58,43,0,53],
[32,37,51,45,53,35,37,43,45,33,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 114, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,53,52,48,55,56,52,47,50,51,61],
[46,0,45,47,33,46,50,52,48,48,44,45],
[47,55,0,57,46,57,49,55,45,51,55,61],
[48,53,43,0,50,55,49,52,45,45,47,51],
[52,67,54,50,0,50,53,53,48,51,50,53],
[45,54,43,45,50,0,47,48,49,44,41,54],
[44,50,51,51,47,53,0,56,44,50,45,52],
[48,48,45,48,47,52,44,0,47,45,50,56],
[53,52,55,55,52,51,56,53,0,46,52,59],
[50,52,49,55,49,56,50,55,54,0,51,54],
[49,56,45,53,50,59,55,50,48,49,0,53],
[39,55,39,49,47,46,48,44,41,46,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 115, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,29,33,55,39,29,48,46,33,58,56],
[47,0,48,46,60,38,43,54,42,40,55,36],
[71,52,0,49,65,52,42,66,56,62,69,69],
[67,54,51,0,72,41,42,57,55,52,74,59],
[45,40,35,28,0,23,25,38,46,19,55,41],
[61,62,48,59,77,0,56,51,52,45,70,66],
[71,57,58,58,75,44,0,61,50,40,87,66],
[52,46,34,43,62,49,39,0,44,40,51,53],
[54,58,44,45,54,48,50,56,0,43,66,60],
[67,60,38,48,81,55,60,60,57,0,68,66],
[42,45,31,26,45,30,13,49,34,32,0,45],
[44,64,31,41,59,34,34,47,40,34,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 116, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,64,48,63,62,52,57,56,54,43,50],
[51,0,52,65,63,59,53,59,63,59,48,66],
[36,48,0,55,49,59,36,41,60,45,37,44],
[52,35,45,0,53,49,43,46,48,40,36,40],
[37,37,51,47,0,47,41,43,48,36,39,53],
[38,41,41,51,53,0,45,49,54,48,41,47],
[48,47,64,57,59,55,0,49,54,49,49,54],
[43,41,59,54,57,51,51,0,51,57,50,58],
[44,37,40,52,52,46,46,49,0,52,37,58],
[46,41,55,60,64,52,51,43,48,0,39,58],
[57,52,63,64,61,59,51,50,63,61,0,59],
[50,34,56,60,47,53,46,42,42,42,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 117, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,44,48,53,50,48,45,52,46,51,55],
[60,0,54,55,54,55,52,56,66,57,50,53],
[56,46,0,49,48,46,47,42,50,50,49,51],
[52,45,51,0,51,50,50,48,57,49,46,46],
[47,46,52,49,0,46,47,46,56,47,49,47],
[50,45,54,50,54,0,45,49,58,50,53,56],
[52,48,53,50,53,55,0,41,59,50,51,47],
[55,44,58,52,54,51,59,0,57,47,51,48],
[48,34,50,43,44,42,41,43,0,46,47,47],
[54,43,50,51,53,50,50,53,54,0,50,47],
[49,50,51,54,51,47,49,49,53,50,0,51],
[45,47,49,54,53,44,53,52,53,53,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 118, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,52,45,45,45,51,53,52,60,49,59],
[49,0,59,48,45,47,49,54,47,58,52,50],
[48,41,0,42,42,41,53,47,43,47,47,48],
[55,52,58,0,50,43,56,51,51,57,49,56],
[55,55,58,50,0,53,57,58,50,61,54,59],
[55,53,59,57,47,0,61,62,54,58,49,54],
[49,51,47,44,43,39,0,43,41,45,47,48],
[47,46,53,49,42,38,57,0,47,55,46,53],
[48,53,57,49,50,46,59,53,0,62,49,47],
[40,42,53,43,39,42,55,45,38,0,52,41],
[51,48,53,51,46,51,53,54,51,48,0,51],
[41,50,52,44,41,46,52,47,53,59,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 119, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,76,66,44,56,39,38,55,62,41,27,55],
[24,0,16,28,32,10,40,53,19,19,13,32],
[34,84,0,46,57,54,50,46,37,45,38,29],
[56,72,54,0,54,30,31,57,51,26,25,70],
[44,68,43,46,0,12,48,56,21,25,11,38],
[61,90,46,70,88,0,53,73,54,68,63,50],
[62,60,50,69,52,47,0,49,58,49,45,59],
[45,47,54,43,44,27,51,0,49,44,23,41],
[38,81,63,49,79,46,42,51,0,48,29,39],
[59,81,55,74,75,32,51,56,52,0,34,67],
[73,87,62,75,89,37,55,77,71,66,0,64],
[45,68,71,30,62,50,41,59,61,33,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 120, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,42,38,50,52,50,57,42,45,42,39],
[52,0,51,42,47,47,46,61,38,47,39,35],
[58,49,0,51,56,52,41,62,50,44,49,44],
[62,58,49,0,54,59,57,62,37,44,47,51],
[50,53,44,46,0,49,51,62,44,39,52,40],
[48,53,48,41,51,0,50,58,41,46,39,33],
[50,54,59,43,49,50,0,58,46,50,53,44],
[43,39,38,38,38,42,42,0,33,30,40,38],
[58,62,50,63,56,59,54,67,0,50,60,51],
[55,53,56,56,61,54,50,70,50,0,50,47],
[58,61,51,53,48,61,47,60,40,50,0,44],
[61,65,56,49,60,67,56,62,49,53,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 121, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,47,56,48,54,51,54,48,57,55,52],
[49,0,48,62,50,49,51,46,55,56,49,51],
[53,52,0,63,53,52,54,51,49,53,52,54],
[44,38,37,0,53,44,42,44,50,49,46,48],
[52,50,47,47,0,42,43,50,50,50,52,53],
[46,51,48,56,58,0,43,48,56,55,47,54],
[49,49,46,58,57,57,0,53,55,60,61,55],
[46,54,49,56,50,52,47,0,50,52,53,54],
[52,45,51,50,50,44,45,50,0,52,54,46],
[43,44,47,51,50,45,40,48,48,0,47,50],
[45,51,48,54,48,53,39,47,46,53,0,46],
[48,49,46,52,47,46,45,46,54,50,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 122, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,56,57,66,54,58,53,57,55,56,52],
[54,0,58,55,56,56,50,53,50,58,51,53],
[44,42,0,45,57,44,52,49,42,47,49,46],
[43,45,55,0,58,49,53,46,49,50,53,49],
[34,44,43,42,0,45,42,47,47,49,47,44],
[46,44,56,51,55,0,51,50,54,56,50,51],
[42,50,48,47,58,49,0,47,52,56,48,52],
[47,47,51,54,53,50,53,0,55,57,52,49],
[43,50,58,51,53,46,48,45,0,48,46,47],
[45,42,53,50,51,44,44,43,52,0,47,50],
[44,49,51,47,53,50,52,48,54,53,0,50],
[48,47,54,51,56,49,48,51,53,50,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 123, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,55,56,52,57,57,53,46,52,60,57],
[45,0,45,49,49,54,51,48,40,42,53,57],
[45,55,0,58,50,54,57,56,49,54,60,57],
[44,51,42,0,49,48,53,51,45,48,56,57],
[48,51,50,51,0,50,50,50,40,47,50,52],
[43,46,46,52,50,0,49,55,46,46,52,54],
[43,49,43,47,50,51,0,46,50,45,52,45],
[47,52,44,49,50,45,54,0,43,40,51,51],
[54,60,51,55,60,54,50,57,0,53,56,57],
[48,58,46,52,53,54,55,60,47,0,58,61],
[40,47,40,44,50,48,48,49,44,42,0,54],
[43,43,43,43,48,46,55,49,43,39,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 124, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,30,41,36,39,41,34,37,49,28,46],
[60,0,30,46,36,45,40,38,60,51,43,48],
[70,70,0,46,42,53,47,47,49,59,52,61],
[59,54,54,0,44,48,54,46,66,66,32,61],
[64,64,58,56,0,55,45,47,56,65,34,69],
[61,55,47,52,45,0,37,39,50,50,45,56],
[59,60,53,46,55,63,0,55,46,55,42,42],
[66,62,53,54,53,61,45,0,52,66,48,60],
[63,40,51,34,44,50,54,48,0,43,29,43],
[51,49,41,34,35,50,45,34,57,0,36,51],
[72,57,48,68,66,55,58,52,71,64,0,67],
[54,52,39,39,31,44,58,40,57,49,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 125, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,54,41,43,40,51,43,43,42,46,44],
[54,0,51,46,55,48,55,43,39,55,50,52],
[46,49,0,38,41,36,45,34,37,35,47,41],
[59,54,62,0,59,53,58,50,50,55,54,59],
[57,45,59,41,0,37,49,48,47,48,52,48],
[60,52,64,47,63,0,57,48,54,59,53,53],
[49,45,55,42,51,43,0,46,56,48,59,44],
[57,57,66,50,52,52,54,0,47,53,53,55],
[57,61,63,50,53,46,44,53,0,63,55,40],
[58,45,65,45,52,41,52,47,37,0,56,46],
[54,50,53,46,48,47,41,47,45,44,0,38],
[56,48,59,41,52,47,56,45,60,54,62,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 126, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,46,53,53,49,46,50,42,47,51,48],
[44,0,46,49,51,51,47,46,46,42,49,43],
[54,54,0,60,49,54,49,56,52,48,58,42],
[47,51,40,0,51,57,43,63,44,41,54,45],
[47,49,51,49,0,58,49,52,51,48,52,54],
[51,49,46,43,42,0,43,43,38,36,48,48],
[54,53,51,57,51,57,0,64,52,45,63,45],
[50,54,44,37,48,57,36,0,50,44,53,45],
[58,54,48,56,49,62,48,50,0,50,58,44],
[53,58,52,59,52,64,55,56,50,0,55,46],
[49,51,42,46,48,52,37,47,42,45,0,40],
[52,57,58,55,46,52,55,55,56,54,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 127, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,46,44,33,50,43,49,53,35,65,66],
[44,0,39,53,45,33,37,31,44,32,43,55],
[54,61,0,43,54,45,58,49,54,61,72,63],
[56,47,57,0,43,47,57,52,56,57,67,72],
[67,55,46,57,0,45,51,67,62,59,62,74],
[50,67,55,53,55,0,47,49,76,48,65,64],
[57,63,42,43,49,53,0,51,56,52,63,69],
[51,69,51,48,33,51,49,0,63,45,64,55],
[47,56,46,44,38,24,44,37,0,43,49,62],
[65,68,39,43,41,52,48,55,57,0,80,67],
[35,57,28,33,38,35,37,36,51,20,0,40],
[34,45,37,28,26,36,31,45,38,33,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 128, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,46,48,49,43,58,52,46,45,53,47],
[57,0,50,50,57,53,64,57,45,59,50,54],
[54,50,0,50,50,53,58,56,53,58,46,50],
[52,50,50,0,51,42,65,57,49,48,57,54],
[51,43,50,49,0,49,56,49,48,53,54,52],
[57,47,47,58,51,0,61,57,49,46,56,55],
[42,36,42,35,44,39,0,50,41,38,39,42],
[48,43,44,43,51,43,50,0,45,47,50,44],
[54,55,47,51,52,51,59,55,0,56,55,46],
[55,41,42,52,47,54,62,53,44,0,52,53],
[47,50,54,43,46,44,61,50,45,48,0,51],
[53,46,50,46,48,45,58,56,54,47,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 129, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,55,60,57,55,48,56,53,56,46,58],
[44,0,52,50,48,56,49,45,49,53,43,51],
[45,48,0,52,51,59,47,54,54,50,55,55],
[40,50,48,0,44,49,48,51,51,55,45,46],
[43,52,49,56,0,56,53,55,54,52,47,50],
[45,44,41,51,44,0,50,41,41,48,44,45],
[52,51,53,52,47,50,0,46,47,52,47,48],
[44,55,46,49,45,59,54,0,51,47,40,48],
[47,51,46,49,46,59,53,49,0,52,47,46],
[44,47,50,45,48,52,48,53,48,0,41,44],
[54,57,45,55,53,56,53,60,53,59,0,49],
[42,49,45,54,50,55,52,52,54,56,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 130, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,64,37,66,55,46,37,44,43,37,52,68],
[36,0,43,30,19,33,10,34,35,24,50,44],
[63,57,0,52,45,52,33,43,48,46,67,61],
[34,70,48,0,42,53,28,43,38,45,52,54],
[45,81,55,58,0,51,32,57,34,34,66,74],
[54,67,48,47,49,0,38,34,44,42,53,50],
[63,90,67,72,68,62,0,44,46,61,72,75],
[56,66,57,57,43,66,56,0,50,57,75,74],
[57,65,52,62,66,56,54,50,0,61,77,60],
[63,76,54,55,66,58,39,43,39,0,71,67],
[48,50,33,48,34,47,28,25,23,29,0,51],
[32,56,39,46,26,50,25,26,40,33,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 131, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,48,48,43,53,56,63,55,54,65,47],
[41,0,44,43,41,50,49,45,44,45,55,46],
[52,56,0,56,46,50,53,57,50,54,58,46],
[52,57,44,0,51,49,55,56,48,51,58,50],
[57,59,54,49,0,59,52,54,47,55,64,55],
[47,50,50,51,41,0,51,52,46,49,58,42],
[44,51,47,45,48,49,0,55,44,54,62,43],
[37,55,43,44,46,48,45,0,41,41,49,44],
[45,56,50,52,53,54,56,59,0,44,62,43],
[46,55,46,49,45,51,46,59,56,0,58,53],
[35,45,42,42,36,42,38,51,38,42,0,45],
[53,54,54,50,45,58,57,56,57,47,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 132, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,41,44,41,39,52,37,44,37,34,43],
[61,0,43,58,52,54,50,48,57,50,57,54],
[59,57,0,53,50,52,53,53,52,49,63,55],
[56,42,47,0,56,55,59,50,53,41,53,46],
[59,48,50,44,0,48,54,51,50,49,54,55],
[61,46,48,45,52,0,52,51,52,47,51,47],
[48,50,47,41,46,48,0,47,48,43,51,52],
[63,52,47,50,49,49,53,0,50,51,50,54],
[56,43,48,47,50,48,52,50,0,51,53,58],
[63,50,51,59,51,53,57,49,49,0,58,54],
[66,43,37,47,46,49,49,50,47,42,0,52],
[57,46,45,54,45,53,48,46,42,46,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 133, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,57,59,32,42,62,65,60,65,49,39],
[53,0,55,43,36,37,55,51,57,65,57,38],
[43,45,0,44,29,34,63,39,43,53,50,38],
[41,57,56,0,53,54,58,54,53,72,62,52],
[68,64,71,47,0,57,64,63,64,74,66,66],
[58,63,66,46,43,0,70,49,64,58,57,56],
[38,45,37,42,36,30,0,47,45,43,38,38],
[35,49,61,46,37,51,53,0,62,46,39,33],
[40,43,57,47,36,36,55,38,0,61,45,51],
[35,35,47,28,26,42,57,54,39,0,31,41],
[51,43,50,38,34,43,62,61,55,69,0,53],
[61,62,62,48,34,44,62,67,49,59,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 134, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,38,47,45,50,50,46,47,45,40,48],
[55,0,42,57,46,46,55,52,56,53,48,47],
[62,58,0,67,47,57,56,57,61,56,58,52],
[53,43,33,0,42,39,51,46,48,44,38,43],
[55,54,53,58,0,58,60,56,59,57,50,54],
[50,54,43,61,42,0,52,57,54,51,51,42],
[50,45,44,49,40,48,0,49,49,49,41,35],
[54,48,43,54,44,43,51,0,50,48,47,44],
[53,44,39,52,41,46,51,50,0,52,49,48],
[55,47,44,56,43,49,51,52,48,0,48,40],
[60,52,42,62,50,49,59,53,51,52,0,48],
[52,53,48,57,46,58,65,56,52,60,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 135, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,46,42,61,67,73,56,60,47,49,45],
[51,0,51,45,68,78,63,55,63,39,61,41],
[54,49,0,55,73,70,69,59,65,53,62,63],
[58,55,45,0,71,61,65,58,55,47,63,28],
[39,32,27,29,0,53,51,45,42,38,59,31],
[33,22,30,39,47,0,48,51,51,45,51,27],
[27,37,31,35,49,52,0,44,33,37,44,37],
[44,45,41,42,55,49,56,0,36,45,46,24],
[40,37,35,45,58,49,67,64,0,35,61,34],
[53,61,47,53,62,55,63,55,65,0,48,48],
[51,39,38,37,41,49,56,54,39,52,0,39],
[55,59,37,72,69,73,63,76,66,52,61,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 136, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,61,61,46,100,61,85,46,61,46,85],
[54,0,61,61,15,100,15,100,61,61,61,54],
[39,39,0,0,39,39,39,39,0,39,0,39],
[39,39,100,0,39,39,39,39,0,85,0,39],
[54,85,61,61,0,100,54,100,61,100,46,54],
[0,0,61,61,0,0,0,0,46,46,0,0],
[39,85,61,61,46,100,0,85,46,46,46,85],
[15,0,61,61,0,100,15,0,61,61,0,54],
[54,39,100,100,39,54,54,39,0,100,0,39],
[39,39,61,15,0,54,54,39,0,0,0,39],
[54,39,100,100,54,100,54,100,100,100,0,54],
[15,46,61,61,46,100,15,46,61,61,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 137, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,64,59,58,54,43,56,53,56,54,38,66],
[36,0,33,45,49,39,47,42,33,49,29,40],
[41,67,0,59,59,54,59,47,43,51,49,47],
[42,55,41,0,54,36,52,43,41,49,38,37],
[46,51,41,46,0,51,49,54,54,47,40,52],
[57,61,46,64,49,0,68,53,58,58,53,72],
[44,53,41,48,51,32,0,40,48,44,42,38],
[47,58,53,57,46,47,60,0,53,46,47,66],
[44,67,57,59,46,42,52,47,0,52,51,62],
[46,51,49,51,53,42,56,54,48,0,55,40],
[62,71,51,62,60,47,58,53,49,45,0,57],
[34,60,53,63,48,28,62,34,38,60,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 138, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,54,60,50,50,51,60,61,53,53,53],
[49,0,42,58,43,52,50,55,55,54,49,46],
[46,58,0,60,50,50,58,59,53,54,58,53],
[40,42,40,0,41,42,48,53,48,50,49,48],
[50,57,50,59,0,53,61,62,56,57,58,57],
[50,48,50,58,47,0,45,63,56,60,48,54],
[49,50,42,52,39,55,0,54,51,56,50,42],
[40,45,41,47,38,37,46,0,46,46,49,48],
[39,45,47,52,44,44,49,54,0,49,46,50],
[47,46,46,50,43,40,44,54,51,0,42,45],
[47,51,42,51,42,52,50,51,54,58,0,52],
[47,54,47,52,43,46,58,52,50,55,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 139, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,49,54,59,47,49,57,53,47,49,52],
[51,0,50,46,59,54,43,50,55,42,51,45],
[51,50,0,49,62,55,47,62,51,46,51,55],
[46,54,51,0,54,56,50,51,47,50,54,50],
[41,41,38,46,0,46,52,43,39,41,41,44],
[53,46,45,44,54,0,49,48,51,50,41,46],
[51,57,53,50,48,51,0,57,52,43,51,53],
[43,50,38,49,57,52,43,0,53,42,47,55],
[47,45,49,53,61,49,48,47,0,40,47,53],
[53,58,54,50,59,50,57,58,60,0,55,53],
[51,49,49,46,59,59,49,53,53,45,0,50],
[48,55,45,50,56,54,47,45,47,47,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 140, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,36,39,36,54,43,50,26,44,29,44],
[67,0,58,58,53,54,56,60,55,61,46,53],
[64,42,0,48,53,50,47,52,53,55,41,49],
[61,42,52,0,46,59,47,46,40,54,40,51],
[64,47,47,54,0,58,52,62,44,59,47,49],
[46,46,50,41,42,0,34,40,41,40,33,37],
[57,44,53,53,48,66,0,60,43,53,51,52],
[50,40,48,54,38,60,40,0,35,50,38,45],
[74,45,47,60,56,59,57,65,0,67,40,54],
[56,39,45,46,41,60,47,50,33,0,34,46],
[71,54,59,60,53,67,49,62,60,66,0,54],
[56,47,51,49,51,63,48,55,46,54,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 141, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,53,49,49,54,50,53,56,58,58,54],
[50,0,49,52,48,55,47,58,49,63,58,55],
[47,51,0,50,46,46,50,57,49,55,51,49],
[51,48,50,0,50,56,48,59,57,55,55,53],
[51,52,54,50,0,61,50,57,59,58,52,53],
[46,45,54,44,39,0,40,53,45,57,49,47],
[50,53,50,52,50,60,0,57,57,58,55,58],
[47,42,43,41,43,47,43,0,42,52,49,55],
[44,51,51,43,41,55,43,58,0,53,50,58],
[42,37,45,45,42,43,42,48,47,0,46,43],
[42,42,49,45,48,51,45,51,50,54,0,52],
[46,45,51,47,47,53,42,45,42,57,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 142, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,55,54,60,69,50,55,58,46,53,51],
[38,0,43,47,60,64,46,56,60,41,47,52],
[45,57,0,54,68,63,50,62,64,50,56,53],
[46,53,46,0,58,56,59,62,59,48,54,55],
[40,40,32,42,0,56,39,42,51,39,44,49],
[31,36,37,44,44,0,31,43,46,32,40,43],
[50,54,50,41,61,69,0,62,60,48,55,51],
[45,44,38,38,58,57,38,0,49,37,49,46],
[42,40,36,41,49,54,40,51,0,44,44,45],
[54,59,50,52,61,68,52,63,56,0,57,55],
[47,53,44,46,56,60,45,51,56,43,0,51],
[49,48,47,45,51,57,49,54,55,45,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 143, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,49,48,50,59,65,42,62,45,59,60],
[55,0,56,44,48,68,61,39,52,40,62,55],
[51,44,0,42,39,63,58,35,50,55,56,56],
[52,56,58,0,62,72,73,52,60,47,68,75],
[50,52,61,38,0,64,72,41,62,55,49,59],
[41,32,37,28,36,0,68,36,45,34,37,52],
[35,39,42,27,28,32,0,24,40,39,33,45],
[58,61,65,48,59,64,76,0,61,55,62,56],
[38,48,50,40,38,55,60,39,0,52,53,53],
[55,60,45,53,45,66,61,45,48,0,63,65],
[41,38,44,32,51,63,67,38,47,37,0,57],
[40,45,44,25,41,48,55,44,47,35,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 144, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,37,22,8,0,31,13,26,38,29,43,28],
[63,0,68,60,28,47,52,53,27,43,20,35],
[78,32,0,50,42,51,58,34,48,44,52,48],
[92,40,50,0,54,47,60,38,56,38,56,37],
[100,72,58,46,0,51,43,61,77,57,60,64],
[69,53,49,53,49,0,73,55,57,47,69,62],
[87,48,42,40,57,27,0,46,53,53,51,36],
[74,47,66,62,39,45,54,0,47,45,35,37],
[62,73,52,44,23,43,47,53,0,44,26,56],
[71,57,56,62,43,53,47,55,56,0,61,67],
[57,80,48,44,40,31,49,65,74,39,0,44],
[72,65,52,63,36,38,64,63,44,33,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 145, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,37,44,47,51,51,50,52,37,53,53,44],
[63,0,65,56,63,63,53,70,43,55,49,52],
[56,35,0,54,57,52,37,63,42,50,34,38],
[53,44,46,0,60,55,52,58,42,48,55,42],
[49,37,43,40,0,48,48,54,26,55,42,43],
[49,37,48,45,52,0,42,57,45,50,45,56],
[50,47,63,48,52,58,0,68,45,55,43,49],
[48,30,37,42,46,43,32,0,28,57,41,51],
[63,57,58,58,74,55,55,72,0,65,45,61],
[47,45,50,52,45,50,45,43,35,0,36,48],
[47,51,66,45,58,55,57,59,55,64,0,56],
[56,48,62,58,57,44,51,49,39,52,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 146, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,51,48,53,53,56,56,50,43,47,51],
[44,0,45,47,49,46,52,53,46,49,42,42],
[49,55,0,54,56,49,57,54,60,53,55,48],
[52,53,46,0,57,52,47,59,54,41,49,48],
[47,51,44,43,0,43,53,53,52,42,45,48],
[47,54,51,48,57,0,50,47,48,47,46,47],
[44,48,43,53,47,50,0,48,55,46,42,39],
[44,47,46,41,47,53,52,0,53,46,45,47],
[50,54,40,46,48,52,45,47,0,41,47,44],
[57,51,47,59,58,53,54,54,59,0,58,48],
[53,58,45,51,55,54,58,55,53,42,0,48],
[49,58,52,52,52,53,61,53,56,52,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 147, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,49,51,36,56,54,48,46,53,53,56],
[48,0,49,45,47,44,48,38,42,49,50,47],
[51,51,0,52,48,43,47,49,36,50,52,57],
[49,55,48,0,52,47,49,41,47,53,55,58],
[64,53,52,48,0,56,66,54,50,57,61,69],
[44,56,57,53,44,0,54,57,46,59,59,51],
[46,52,53,51,34,46,0,50,49,63,50,53],
[52,62,51,59,46,43,50,0,42,48,57,53],
[54,58,64,53,50,54,51,58,0,52,58,58],
[47,51,50,47,43,41,37,52,48,0,48,61],
[47,50,48,45,39,41,50,43,42,52,0,55],
[44,53,43,42,31,49,47,47,42,39,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 148, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,56,44,60,48,49,50,48,54,51,52],
[51,0,52,47,59,49,47,56,54,53,55,57],
[44,48,0,46,52,42,45,50,46,49,48,54],
[56,53,54,0,63,52,52,49,48,44,54,51],
[40,41,48,37,0,41,42,43,40,40,43,47],
[52,51,58,48,59,0,47,51,42,55,49,58],
[51,53,55,48,58,53,0,59,46,54,52,56],
[50,44,50,51,57,49,41,0,46,48,51,56],
[52,46,54,52,60,58,54,54,0,55,55,56],
[46,47,51,56,60,45,46,52,45,0,51,59],
[49,45,52,46,57,51,48,49,45,49,0,52],
[48,43,46,49,53,42,44,44,44,41,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 149, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,54,53,53,52,46,44,62,50,50,51],
[51,0,49,56,48,52,41,48,60,41,43,59],
[46,51,0,48,45,51,56,39,61,41,50,55],
[47,44,52,0,43,46,50,51,59,47,45,55],
[47,52,55,57,0,69,44,55,56,43,50,70],
[48,48,49,54,31,0,47,44,52,37,47,61],
[54,59,44,50,56,53,0,44,65,55,64,64],
[56,52,61,49,45,56,56,0,61,55,56,58],
[38,40,39,41,44,48,35,39,0,35,49,48],
[50,59,59,53,57,63,45,45,65,0,54,56],
[50,57,50,55,50,53,36,44,51,46,0,54],
[49,41,45,45,30,39,36,42,52,44,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 150, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,59,65,44,62,62,46,55,46,56,51],
[55,0,59,69,50,64,67,60,73,43,53,57],
[41,41,0,59,39,62,56,40,48,43,53,43],
[35,31,41,0,35,43,52,35,67,36,36,41],
[56,50,61,65,0,64,67,59,75,57,47,56],
[38,36,38,57,36,0,57,55,58,41,38,53],
[38,33,44,48,33,43,0,51,61,37,30,27],
[54,40,60,65,41,45,49,0,68,40,47,45],
[45,27,52,33,25,42,39,32,0,33,38,44],
[54,57,57,64,43,59,63,60,67,0,50,57],
[44,47,47,64,53,62,70,53,62,50,0,52],
[49,43,57,59,44,47,73,55,56,43,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 151, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,56,48,45,43,48,43,50,55,51,45],
[53,0,52,53,49,41,37,56,47,47,55,43],
[44,48,0,51,59,41,41,46,48,41,57,53],
[52,47,49,0,44,44,42,44,47,42,52,49],
[55,51,41,56,0,54,45,55,58,44,56,52],
[57,59,59,56,46,0,45,48,51,48,55,51],
[52,63,59,58,55,55,0,55,51,61,62,50],
[57,44,54,56,45,52,45,0,41,51,57,55],
[50,53,52,53,42,49,49,59,0,51,51,48],
[45,53,59,58,56,52,39,49,49,0,60,54],
[49,45,43,48,44,45,38,43,49,40,0,49],
[55,57,47,51,48,49,50,45,52,46,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 152, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,54,45,68,57,50,60,50,46,49,44],
[45,0,52,58,67,54,59,68,43,53,55,50],
[46,48,0,47,62,51,47,62,47,58,49,35],
[55,42,53,0,59,44,54,64,41,62,58,46],
[32,33,38,41,0,36,44,55,30,50,39,36],
[43,46,49,56,64,0,49,61,38,54,51,46],
[50,41,53,46,56,51,0,65,44,36,60,41],
[40,32,38,36,45,39,35,0,26,34,35,37],
[50,57,53,59,70,62,56,74,0,62,57,54],
[54,47,42,38,50,46,64,66,38,0,45,35],
[51,45,51,42,61,49,40,65,43,55,0,47],
[56,50,65,54,64,54,59,63,46,65,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 153, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,70,59,59,71,55,57,58,49,72,65,59],
[30,0,45,59,55,51,37,51,55,61,47,53],
[41,55,0,52,60,52,43,51,45,67,44,52],
[41,41,48,0,47,38,31,40,39,37,27,29],
[29,45,40,53,0,33,39,55,46,51,41,37],
[45,49,48,62,67,0,44,63,50,65,57,61],
[43,63,57,69,61,56,0,58,58,75,57,47],
[42,49,49,60,45,37,42,0,51,53,49,35],
[51,45,55,61,54,50,42,49,0,73,49,45],
[28,39,33,63,49,35,25,47,27,0,45,41],
[35,53,56,73,59,43,43,51,51,55,0,40],
[41,47,48,71,63,39,53,65,55,59,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 154, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,48,59,50,56,44,53,56,48,55,62],
[40,0,47,57,53,50,48,51,52,55,44,53],
[52,53,0,54,56,52,50,51,55,53,57,54],
[41,43,46,0,52,49,48,43,50,47,52,51],
[50,47,44,48,0,52,43,48,45,51,52,48],
[44,50,48,51,48,0,48,48,48,52,52,51],
[56,52,50,52,57,52,0,56,48,57,54,55],
[47,49,49,57,52,52,44,0,49,61,58,60],
[44,48,45,50,55,52,52,51,0,55,44,53],
[52,45,47,53,49,48,43,39,45,0,52,56],
[45,56,43,48,48,48,46,42,56,48,0,59],
[38,47,46,49,52,49,45,40,47,44,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 155, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,100,97,77,68,68,48,77,49,77,48,51],
[0,0,49,28,20,48,0,28,29,0,28,3],
[3,51,0,48,68,48,48,48,20,23,48,51],
[23,72,52,0,20,51,3,28,32,3,3,3],
[32,80,32,80,0,31,32,57,32,32,80,32],
[32,52,52,49,69,0,49,49,52,52,49,52],
[52,100,52,97,68,51,0,77,52,72,97,23],
[23,72,52,72,43,51,23,0,52,43,43,43],
[51,71,80,68,68,48,48,48,0,51,68,51],
[23,100,77,97,68,48,28,57,49,0,48,51],
[52,72,52,97,20,51,3,57,32,52,0,3],
[49,97,49,97,68,48,77,57,49,49,97,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 156, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,53,58,59,58,43,54,63,46,49,53],
[45,0,51,50,47,52,42,50,57,48,42,43],
[47,49,0,41,52,50,38,48,48,47,43,48],
[42,50,59,0,48,48,45,47,52,60,52,46],
[41,53,48,52,0,43,41,46,55,51,43,49],
[42,48,50,52,57,0,40,46,50,43,47,53],
[57,58,62,55,59,60,0,58,69,48,53,62],
[46,50,52,53,54,54,42,0,48,44,52,48],
[37,43,52,48,45,50,31,52,0,41,49,44],
[54,52,53,40,49,57,52,56,59,0,42,53],
[51,58,57,48,57,53,47,48,51,58,0,49],
[47,57,52,54,51,47,38,52,56,47,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 157, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,57,57,59,60,51,56,56,45,57,51],
[48,0,44,54,48,54,55,54,46,51,44,45],
[43,56,0,54,53,56,51,57,59,51,47,47],
[43,46,46,0,46,52,47,57,44,45,45,36],
[41,52,47,54,0,48,51,55,53,55,49,42],
[40,46,44,48,52,0,46,55,51,48,40,50],
[49,45,49,53,49,54,0,49,46,45,45,46],
[44,46,43,43,45,45,51,0,45,49,47,48],
[44,54,41,56,47,49,54,55,0,49,48,46],
[55,49,49,55,45,52,55,51,51,0,46,48],
[43,56,53,55,51,60,55,53,52,54,0,47],
[49,55,53,64,58,50,54,52,54,52,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 158, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,60,54,58,62,58,56,63,48,54,43],
[48,0,54,63,59,48,58,52,56,51,53,48],
[40,46,0,50,48,51,44,47,55,39,39,39],
[46,37,50,0,60,50,51,51,49,44,38,47],
[42,41,52,40,0,45,38,41,52,39,45,42],
[38,52,49,50,55,0,59,52,49,45,46,44],
[42,42,56,49,62,41,0,41,55,42,46,40],
[44,48,53,49,59,48,59,0,53,36,46,42],
[37,44,45,51,48,51,45,47,0,45,36,36],
[52,49,61,56,61,55,58,64,55,0,48,54],
[46,47,61,62,55,54,54,54,64,52,0,43],
[57,52,61,53,58,56,60,58,64,46,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 159, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,40,65,57,56,35,71,56,34,48,43],
[40,0,49,59,45,46,55,38,29,29,21,32],
[60,51,0,81,61,64,45,52,55,50,43,61],
[35,41,19,0,24,13,27,31,39,31,29,27],
[43,55,39,76,0,42,57,54,53,32,52,35],
[44,54,36,87,58,0,45,64,63,43,41,54],
[65,45,55,73,43,55,0,56,44,39,56,34],
[29,62,48,69,46,36,44,0,39,52,53,54],
[44,71,45,61,47,37,56,61,0,54,53,57],
[66,71,50,69,68,57,61,48,46,0,59,43],
[52,79,57,71,48,59,44,47,47,41,0,56],
[57,68,39,73,65,46,66,46,43,57,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 160, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,50,58,54,55,48,47,46,55,56,52],
[49,0,54,61,54,53,50,53,50,59,60,54],
[50,46,0,52,57,50,50,48,42,55,52,50],
[42,39,48,0,50,53,42,45,43,49,48,44],
[46,46,43,50,0,51,45,47,41,46,55,41],
[45,47,50,47,49,0,42,46,39,48,49,49],
[52,50,50,58,55,58,0,50,52,56,63,53],
[53,47,52,55,53,54,50,0,49,57,58,59],
[54,50,58,57,59,61,48,51,0,61,60,52],
[45,41,45,51,54,52,44,43,39,0,53,47],
[44,40,48,52,45,51,37,42,40,47,0,47],
[48,46,50,56,59,51,47,41,48,53,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 161, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,56,45,43,43,59,55,52,49,46,55],
[64,0,63,49,48,48,53,52,58,52,57,61],
[44,37,0,42,31,37,50,44,40,39,46,48],
[55,51,58,0,56,58,54,58,55,46,52,49],
[57,52,69,44,0,58,59,57,54,44,47,60],
[57,52,63,42,42,0,50,58,46,50,45,51],
[41,47,50,46,41,50,0,51,42,43,42,47],
[45,48,56,42,43,42,49,0,53,42,40,52],
[48,42,60,45,46,54,58,47,0,44,46,58],
[51,48,61,54,56,50,57,58,56,0,55,58],
[54,43,54,48,53,55,58,60,54,45,0,58],
[45,39,52,51,40,49,53,48,42,42,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 162, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,49,49,47,47,59,59,60,58,56,54],
[45,0,41,45,39,47,54,55,51,52,49,45],
[51,59,0,54,52,48,54,44,53,49,52,50],
[51,55,46,0,52,49,58,52,57,59,51,53],
[53,61,48,48,0,50,63,56,60,61,59,53],
[53,53,52,51,50,0,59,54,65,56,53,58],
[41,46,46,42,37,41,0,46,53,47,38,42],
[41,45,56,48,44,46,54,0,54,54,45,46],
[40,49,47,43,40,35,47,46,0,41,44,45],
[42,48,51,41,39,44,53,46,59,0,45,51],
[44,51,48,49,41,47,62,55,56,55,0,48],
[46,55,50,47,47,42,58,54,55,49,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 163, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,50,58,32,48,49,63,35,49,57,47],
[59,0,41,73,54,66,65,61,42,69,67,59],
[50,59,0,79,46,76,63,77,55,60,80,62],
[42,27,21,0,27,46,40,52,45,44,37,51],
[68,46,54,73,0,56,62,79,37,44,68,62],
[52,34,24,54,44,0,50,62,32,42,46,43],
[51,35,37,60,38,50,0,57,32,52,53,34],
[37,39,23,48,21,38,43,0,25,40,42,39],
[65,58,45,55,63,68,68,75,0,58,75,64],
[51,31,40,56,56,58,48,60,42,0,61,43],
[43,33,20,63,32,54,47,58,25,39,0,42],
[53,41,38,49,38,57,66,61,36,57,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 164, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,63,60,47,55,51,52,52,51,52,55],
[50,0,64,54,52,57,55,53,57,54,56,60],
[37,36,0,48,36,47,43,42,41,40,41,48],
[40,46,52,0,40,49,42,49,46,44,45,52],
[53,48,64,60,0,59,53,55,53,53,60,57],
[45,43,53,51,41,0,46,49,37,44,51,52],
[49,45,57,58,47,54,0,51,48,55,52,58],
[48,47,58,51,45,51,49,0,49,50,56,61],
[48,43,59,54,47,63,52,51,0,52,51,59],
[49,46,60,56,47,56,45,50,48,0,50,60],
[48,44,59,55,40,49,48,44,49,50,0,60],
[45,40,52,48,43,48,42,39,41,40,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 165, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,54,54,46,49,51,51,51,53,47,50],
[45,0,49,46,50,47,45,50,47,52,52,50],
[46,51,0,50,46,43,44,46,43,48,53,42],
[46,54,50,0,46,37,44,47,46,54,51,54],
[54,50,54,54,0,55,48,55,50,58,59,58],
[51,53,57,63,45,0,51,56,57,53,57,49],
[49,55,56,56,52,49,0,53,49,58,50,50],
[49,50,54,53,45,44,47,0,46,52,54,58],
[49,53,57,54,50,43,51,54,0,49,51,63],
[47,48,52,46,42,47,42,48,51,0,52,46],
[53,48,47,49,41,43,50,46,49,48,0,47],
[50,50,58,46,42,51,50,42,37,54,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 166, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,56,50,65,61,82,66,50,72,71,73],
[40,0,63,50,43,45,50,50,66,59,50,45],
[44,37,0,35,50,48,55,55,57,55,65,49],
[50,50,65,0,56,58,54,79,49,75,68,59],
[35,57,50,44,0,59,44,52,45,78,67,51],
[39,55,52,42,41,0,42,28,44,77,44,37],
[18,50,45,46,56,58,0,34,57,63,51,42],
[34,50,45,21,48,72,66,0,56,68,67,62],
[50,34,43,51,55,56,43,44,0,66,53,68],
[28,41,45,25,22,23,37,32,34,0,46,37],
[29,50,35,32,33,56,49,33,47,54,0,59],
[27,55,51,41,49,63,58,38,32,63,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 167, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,46,45,48,46,43,50,50,58,45,49],
[56,0,49,49,45,43,37,55,58,56,55,51],
[54,51,0,65,55,51,47,47,51,59,50,48],
[55,51,35,0,50,47,50,56,50,60,57,49],
[52,55,45,50,0,40,38,51,58,53,56,48],
[54,57,49,53,60,0,55,60,63,68,51,64],
[57,63,53,50,62,45,0,58,54,64,65,56],
[50,45,53,44,49,40,42,0,40,63,47,40],
[50,42,49,50,42,37,46,60,0,54,53,44],
[42,44,41,40,47,32,36,37,46,0,33,28],
[55,45,50,43,44,49,35,53,47,67,0,44],
[51,49,52,51,52,36,44,60,56,72,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 168, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,56,38,45,45,48,59,41,40,47,58],
[55,0,54,49,51,50,55,58,54,50,48,57],
[44,46,0,50,55,47,48,61,47,52,49,61],
[62,51,50,0,58,61,52,74,43,58,53,58],
[55,49,45,42,0,53,53,50,39,55,42,66],
[55,50,53,39,47,0,42,62,42,46,45,46],
[52,45,52,48,47,58,0,56,37,55,40,51],
[41,42,39,26,50,38,44,0,27,46,46,49],
[59,46,53,57,61,58,63,73,0,58,51,65],
[60,50,48,42,45,54,45,54,42,0,34,51],
[53,52,51,47,58,55,60,54,49,66,0,62],
[42,43,39,42,34,54,49,51,35,49,38,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 169, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,23,64,21,20,50,27,52,39,49,52],
[48,0,36,58,41,30,58,38,52,44,51,54],
[77,64,0,82,27,29,58,42,44,37,74,49],
[36,42,18,0,17,16,56,35,37,28,59,33],
[79,59,73,83,0,47,77,67,79,60,67,64],
[80,70,71,84,53,0,71,63,69,50,75,45],
[50,42,42,44,23,29,0,41,58,32,55,51],
[73,62,58,65,33,37,59,0,55,58,84,43],
[48,48,56,63,21,31,42,45,0,44,55,42],
[61,56,63,72,40,50,68,42,56,0,62,68],
[51,49,26,41,33,25,45,16,45,38,0,34],
[48,46,51,67,36,55,49,57,58,32,66,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 170, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,46,47,49,43,45,57,51,42,49,50],
[52,0,55,47,45,54,52,52,52,49,55,49],
[54,45,0,49,39,53,46,54,50,53,49,50],
[53,53,51,0,47,55,42,58,56,57,55,51],
[51,55,61,53,0,55,50,57,58,58,57,53],
[57,46,47,45,45,0,55,49,47,52,48,53],
[55,48,54,58,50,45,0,48,56,55,54,50],
[43,48,46,42,43,51,52,0,46,50,42,44],
[49,48,50,44,42,53,44,54,0,53,57,48],
[58,51,47,43,42,48,45,50,47,0,51,52],
[51,45,51,45,43,52,46,58,43,49,0,44],
[50,51,50,49,47,47,50,56,52,48,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 171, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,38,50,54,47,48,49,66,39,56,49],
[59,0,47,40,50,60,52,50,59,58,57,69],
[62,53,0,43,42,52,51,59,68,41,48,60],
[50,60,57,0,43,74,65,59,66,53,57,73],
[46,50,58,57,0,56,49,53,76,56,59,56],
[53,40,48,26,44,0,48,41,61,55,60,56],
[52,48,49,35,51,52,0,43,58,57,58,55],
[51,50,41,41,47,59,57,0,64,40,50,63],
[34,41,32,34,24,39,42,36,0,51,45,34],
[61,42,59,47,44,45,43,60,49,0,38,51],
[44,43,52,43,41,40,42,50,55,62,0,51],
[51,31,40,27,44,44,45,37,66,49,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 172, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,61,43,50,67,50,55,63,50,53,40],
[52,0,55,47,51,62,41,50,52,51,45,43],
[39,45,0,42,35,72,47,50,55,45,50,40],
[57,53,58,0,62,60,44,53,54,62,55,42],
[50,49,65,38,0,63,44,55,51,50,41,36],
[33,38,28,40,37,0,32,36,48,34,40,27],
[50,59,53,56,56,68,0,61,63,66,49,54],
[45,50,50,47,45,64,39,0,58,50,52,44],
[37,48,45,46,49,52,37,42,0,45,45,50],
[50,49,55,38,50,66,34,50,55,0,47,37],
[47,55,50,45,59,60,51,48,55,53,0,54],
[60,57,60,58,64,73,46,56,50,63,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 173, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,55,49,58,60,54,60,48,58,50,51],
[51,0,61,54,58,57,58,60,52,61,56,45],
[45,39,0,47,46,56,54,51,42,53,46,37],
[51,46,53,0,45,54,58,50,55,51,49,50],
[42,42,54,55,0,54,53,53,52,52,46,50],
[40,43,44,46,46,0,44,43,41,50,45,41],
[46,42,46,42,47,56,0,50,49,55,47,43],
[40,40,49,50,47,57,50,0,44,53,45,49],
[52,48,58,45,48,59,51,56,0,56,55,52],
[42,39,47,49,48,50,45,47,44,0,47,42],
[50,44,54,51,54,55,53,55,45,53,0,36],
[49,55,63,50,50,59,57,51,48,58,64,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 174, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,46,48,54,60,55,55,53,45,54,51],
[41,0,39,49,47,49,51,44,51,41,45,44],
[54,61,0,59,63,59,59,53,52,46,58,56],
[52,51,41,0,56,56,63,54,51,54,57,46],
[46,53,37,44,0,49,51,46,44,45,47,41],
[40,51,41,44,51,0,49,50,50,45,52,43],
[45,49,41,37,49,51,0,45,44,50,53,42],
[45,56,47,46,54,50,55,0,49,46,59,49],
[47,49,48,49,56,50,56,51,0,51,54,44],
[55,59,54,46,55,55,50,54,49,0,52,49],
[46,55,42,43,53,48,47,41,46,48,0,40],
[49,56,44,54,59,57,58,51,56,51,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 175, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,38,55,51,33,49,29,39,45,38,50],
[62,0,47,56,55,47,44,44,38,47,44,62],
[62,53,0,58,55,34,50,39,43,45,48,49],
[45,44,42,0,54,30,36,24,27,36,48,46],
[49,45,45,46,0,39,61,41,34,49,31,51],
[67,53,66,70,61,0,49,60,61,65,66,67],
[51,56,50,64,39,51,0,63,42,55,61,54],
[71,56,61,76,59,40,37,0,48,48,60,52],
[61,62,57,73,66,39,58,52,0,60,71,71],
[55,53,55,64,51,35,45,52,40,0,65,42],
[62,56,52,52,69,34,39,40,29,35,0,41],
[50,38,51,54,49,33,46,48,29,58,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 176, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,64,54,46,43,54,58,79,51,40,62,59],
[36,0,68,19,60,54,56,57,44,45,44,61],
[46,32,0,46,61,62,61,54,68,61,50,55],
[54,81,54,0,48,53,72,71,57,64,67,58],
[57,40,39,52,0,54,64,55,40,44,59,45],
[46,46,38,47,46,0,43,47,46,44,51,39],
[42,44,39,28,36,57,0,50,64,41,65,44],
[21,43,46,29,45,53,50,0,35,35,55,47],
[49,56,32,43,60,54,36,65,0,22,37,61],
[60,55,39,36,56,56,59,65,78,0,52,55],
[38,56,50,33,41,49,35,45,63,48,0,65],
[41,39,45,42,55,61,56,53,39,45,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 177, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,75,54,60,48,65,50,62,73,64,52],
[39,0,63,40,35,58,45,59,43,71,60,58],
[25,37,0,36,31,42,26,25,36,52,42,30],
[46,60,64,0,46,61,56,54,45,63,53,60],
[40,65,69,54,0,58,49,44,57,69,69,54],
[52,42,58,39,42,0,46,48,32,61,50,49],
[35,55,74,44,51,54,0,63,40,78,54,69],
[50,41,75,46,56,52,37,0,45,65,66,48],
[38,57,64,55,43,68,60,55,0,70,49,55],
[27,29,48,37,31,39,22,35,30,0,26,36],
[36,40,58,47,31,50,46,34,51,74,0,54],
[48,42,70,40,46,51,31,52,45,64,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 178, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,36,53,49,47,47,43,33,49,54,44],
[48,0,54,39,55,48,44,52,47,44,63,47],
[64,46,0,57,57,52,56,51,43,48,67,64],
[47,61,43,0,63,47,49,49,39,47,64,41],
[51,45,43,37,0,33,36,56,42,33,67,39],
[53,52,48,53,67,0,53,54,53,57,72,55],
[53,56,44,51,64,47,0,49,38,56,72,46],
[57,48,49,51,44,46,51,0,44,45,63,51],
[67,53,57,61,58,47,62,56,0,61,72,48],
[51,56,52,53,67,43,44,55,39,0,72,44],
[46,37,33,36,33,28,28,37,28,28,0,27],
[56,53,36,59,61,45,54,49,52,56,73,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 179, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,41,51,65,57,56,54,62,42,68,64],
[60,0,55,50,67,53,46,49,62,50,73,68],
[59,45,0,47,59,58,56,55,68,55,70,76],
[49,50,53,0,62,55,64,49,67,59,66,76],
[35,33,41,38,0,39,51,35,59,40,54,44],
[43,47,42,45,61,0,50,44,71,43,66,70],
[44,54,44,36,49,50,0,52,60,50,57,58],
[46,51,45,51,65,56,48,0,69,44,55,67],
[38,38,32,33,41,29,40,31,0,38,49,48],
[58,50,45,41,60,57,50,56,62,0,61,69],
[32,27,30,34,46,34,43,45,51,39,0,42],
[36,32,24,24,56,30,42,33,52,31,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 180, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,48,43,56,52,50,56,48,52,53,56],
[55,0,46,48,48,61,53,56,52,50,54,47],
[52,54,0,65,56,50,51,70,55,58,53,67],
[57,52,35,0,42,51,55,69,42,57,54,50],
[44,52,44,58,0,56,50,54,48,46,43,51],
[48,39,50,49,44,0,56,69,43,46,40,64],
[50,47,49,45,50,44,0,62,46,63,46,64],
[44,44,30,31,46,31,38,0,43,44,40,46],
[52,48,45,58,52,57,54,57,0,46,54,61],
[48,50,42,43,54,54,37,56,54,0,48,63],
[47,46,47,46,57,60,54,60,46,52,0,58],
[44,53,33,50,49,36,36,54,39,37,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 181, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,55,46,42,47,49,55,47,45,49,53],
[53,0,57,48,43,47,50,53,53,40,45,57],
[45,43,0,50,48,47,49,52,51,43,50,56],
[54,52,50,0,49,51,48,55,57,45,48,62],
[58,57,52,51,0,47,53,56,55,53,57,56],
[53,53,53,49,53,0,50,44,49,43,47,59],
[51,50,51,52,47,50,0,50,53,39,45,58],
[45,47,48,45,44,56,50,0,44,41,54,58],
[53,47,49,43,45,51,47,56,0,46,49,58],
[55,60,57,55,47,57,61,59,54,0,60,64],
[51,55,50,52,43,53,55,46,51,40,0,52],
[47,43,44,38,44,41,42,42,42,36,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 182, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,44,55,50,51,56,50,49,50,52,57],
[48,0,50,47,49,50,50,48,46,48,52,48],
[56,50,0,54,53,54,59,57,55,50,51,58],
[45,53,46,0,50,51,52,54,54,44,49,54],
[50,51,47,50,0,54,50,55,53,48,43,52],
[49,50,46,49,46,0,46,53,47,50,47,48],
[44,50,41,48,50,54,0,51,54,46,47,55],
[50,52,43,46,45,47,49,0,49,45,44,53],
[51,54,45,46,47,53,46,51,0,46,47,49],
[50,52,50,56,52,50,54,55,54,0,48,53],
[48,48,49,51,57,53,53,56,53,52,0,49],
[43,52,42,46,48,52,45,47,51,47,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 183, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,53,61,59,55,50,56,52,49,57,61],
[48,0,56,58,58,57,59,59,48,58,58,54],
[47,44,0,52,52,51,48,55,50,51,56,48],
[39,42,48,0,52,53,48,49,51,47,52,45],
[41,42,48,48,0,46,52,49,46,51,50,38],
[45,43,49,47,54,0,43,51,47,50,47,45],
[50,41,52,52,48,57,0,57,40,57,51,52],
[44,41,45,51,51,49,43,0,39,48,52,44],
[48,52,50,49,54,53,60,61,0,54,64,57],
[51,42,49,53,49,50,43,52,46,0,50,55],
[43,42,44,48,50,53,49,48,36,50,0,42],
[39,46,52,55,62,55,48,56,43,45,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 184, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,64,44,65,45,61,62,57,57,53,53,54],
[36,0,42,56,50,55,54,51,57,52,56,66],
[56,58,0,63,50,67,67,71,57,62,56,51],
[35,44,37,0,39,50,46,45,42,40,49,51],
[55,50,50,61,0,69,52,54,56,45,57,46],
[39,45,33,50,31,0,50,49,43,49,33,53],
[38,46,33,54,48,50,0,42,54,45,44,54],
[43,49,29,55,46,51,58,0,54,48,49,53],
[43,43,43,58,44,57,46,46,0,45,47,52],
[47,48,38,60,55,51,55,52,55,0,50,62],
[47,44,44,51,43,67,56,51,53,50,0,53],
[46,34,49,49,54,47,46,47,48,38,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 185, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,63,45,39,58,44,50,66,34,50,46],
[49,0,48,58,40,45,41,36,57,41,42,61],
[37,52,0,49,53,58,46,52,54,51,37,39],
[55,42,51,0,46,63,60,46,66,48,36,61],
[61,60,47,54,0,66,43,39,58,58,49,64],
[42,55,42,37,34,0,39,46,39,42,37,55],
[56,59,54,40,57,61,0,40,55,57,43,59],
[50,64,48,54,61,54,60,0,66,59,52,56],
[34,43,46,34,42,61,45,34,0,39,36,52],
[66,59,49,52,42,58,43,41,61,0,54,70],
[50,58,63,64,51,63,57,48,64,46,0,72],
[54,39,61,39,36,45,41,44,48,30,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 186, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,54,41,49,50,50,54,46,46,44,53],
[50,0,52,50,48,53,47,55,49,54,39,55],
[46,48,0,44,47,51,42,54,52,48,44,49],
[59,50,56,0,47,52,50,56,53,54,50,54],
[51,52,53,53,0,56,47,55,54,60,48,55],
[50,47,49,48,44,0,49,55,55,50,50,52],
[50,53,58,50,53,51,0,59,54,56,44,56],
[46,45,46,44,45,45,41,0,48,51,40,50],
[54,51,48,47,46,45,46,52,0,51,43,51],
[54,46,52,46,40,50,44,49,49,0,42,55],
[56,61,56,50,52,50,56,60,57,58,0,66],
[47,45,51,46,45,48,44,50,49,45,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 187, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,40,43,47,56,44,32,37,54,32,55],
[49,0,30,50,56,52,47,49,44,47,39,62],
[60,70,0,53,66,67,63,61,73,78,44,61],
[57,50,47,0,60,78,66,58,60,62,50,73],
[53,44,34,40,0,42,35,28,31,58,32,62],
[44,48,33,22,58,0,56,36,48,55,38,53],
[56,53,37,34,65,44,0,61,52,52,46,56],
[68,51,39,42,72,64,39,0,53,72,47,55],
[63,56,27,40,69,52,48,47,0,54,41,54],
[46,53,22,38,42,45,48,28,46,0,33,32],
[68,61,56,50,68,62,54,53,59,67,0,50],
[45,38,39,27,38,47,44,45,46,68,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 188, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,50,52,40,50,46,48,50,55,68,51],
[45,0,47,48,27,45,55,46,42,51,64,51],
[50,53,0,44,31,45,32,40,48,44,50,56],
[48,52,56,0,43,53,52,51,55,60,72,55],
[60,73,69,57,0,65,55,59,44,75,68,74],
[50,55,55,47,35,0,51,49,51,56,72,59],
[54,45,68,48,45,49,0,52,44,50,53,50],
[52,54,60,49,41,51,48,0,51,66,72,49],
[50,58,52,45,56,49,56,49,0,57,65,55],
[45,49,56,40,25,44,50,34,43,0,59,45],
[32,36,50,28,32,28,47,28,35,41,0,35],
[49,49,44,45,26,41,50,51,45,55,65,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 189, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,51,54,47,45,46,51,50,49,52,45],
[42,0,44,49,45,47,44,44,52,37,50,49],
[49,56,0,48,49,54,38,56,55,50,53,42],
[46,51,52,0,53,48,56,48,56,45,60,42],
[53,55,51,47,0,50,54,57,56,50,58,44],
[55,53,46,52,50,0,47,52,54,43,42,44],
[54,56,62,44,46,53,0,55,66,51,53,47],
[49,56,44,52,43,48,45,0,51,40,51,46],
[50,48,45,44,44,46,34,49,0,41,46,41],
[51,63,50,55,50,57,49,60,59,0,66,50],
[48,50,47,40,42,58,47,49,54,34,0,37],
[55,51,58,58,56,56,53,54,59,50,63,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 190, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,49,55,45,49,56,51,47,56,58,57],
[45,0,44,51,48,48,49,51,45,52,45,49],
[51,56,0,61,46,56,50,50,45,50,50,56],
[45,49,39,0,42,49,47,48,45,46,47,46],
[55,52,54,58,0,48,51,54,51,49,46,62],
[51,52,44,51,52,0,42,48,43,57,49,50],
[44,51,50,53,49,58,0,54,47,50,47,58],
[49,49,50,52,46,52,46,0,49,53,43,52],
[53,55,55,55,49,57,53,51,0,49,43,55],
[44,48,50,54,51,43,50,47,51,0,44,53],
[42,55,50,53,54,51,53,57,57,56,0,53],
[43,51,44,54,38,50,42,48,45,47,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 191, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,49,53,40,53,49,45,41,42,49,48],
[50,0,39,53,49,47,39,41,35,39,38,48],
[51,61,0,62,52,62,42,55,45,52,60,56],
[47,47,38,0,44,47,46,37,39,37,34,52],
[60,51,48,56,0,55,50,50,35,47,54,48],
[47,53,38,53,45,0,42,40,24,25,49,43],
[51,61,58,54,50,58,0,51,46,51,58,55],
[55,59,45,63,50,60,49,0,46,51,51,43],
[59,65,55,61,65,76,54,54,0,49,59,55],
[58,61,48,63,53,75,49,49,51,0,57,51],
[51,62,40,66,46,51,42,49,41,43,0,54],
[52,52,44,48,52,57,45,57,45,49,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 192, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,58,51,52,51,56,53,57,47,47,47],
[53,0,55,53,59,57,44,47,50,42,45,38],
[42,45,0,42,54,46,57,42,56,47,46,48],
[49,47,58,0,52,52,59,48,48,40,48,46],
[48,41,46,48,0,34,48,46,42,42,37,47],
[49,43,54,48,66,0,48,46,43,39,51,46],
[44,56,43,41,52,52,0,49,43,41,43,43],
[47,53,58,52,54,54,51,0,48,50,46,42],
[43,50,44,52,58,57,57,52,0,47,50,45],
[53,58,53,60,58,61,59,50,53,0,42,48],
[53,55,54,52,63,49,57,54,50,58,0,50],
[53,62,52,54,53,54,57,58,55,52,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 193, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,51,52,48,48,54,50,47,51,51,46],
[55,0,56,54,49,53,51,50,47,52,49,48],
[49,44,0,58,55,52,56,44,44,53,52,43],
[48,46,42,0,48,45,51,50,42,47,49,54],
[52,51,45,52,0,52,52,50,41,52,49,42],
[52,47,48,55,48,0,50,50,45,48,53,43],
[46,49,44,49,48,50,0,42,43,53,54,53],
[50,50,56,50,50,50,58,0,43,55,50,52],
[53,53,56,58,59,55,57,57,0,59,44,53],
[49,48,47,53,48,52,47,45,41,0,53,49],
[49,51,48,51,51,47,46,50,56,47,0,50],
[54,52,57,46,58,57,47,48,47,51,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 194, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,46,55,57,54,46,48,59,54,57,53],
[48,0,49,50,48,54,50,51,52,48,58,48],
[54,51,0,53,45,48,45,50,44,48,53,49],
[45,50,47,0,47,52,50,51,54,48,55,48],
[43,52,55,53,0,58,47,51,54,54,62,50],
[46,46,52,48,42,0,45,46,56,51,52,47],
[54,50,55,50,53,55,0,58,55,49,55,49],
[52,49,50,49,49,54,42,0,49,53,54,55],
[41,48,56,46,46,44,45,51,0,50,55,44],
[46,52,52,52,46,49,51,47,50,0,58,44],
[43,42,47,45,38,48,45,46,45,42,0,49],
[47,52,51,52,50,53,51,45,56,56,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 195, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,57,62,50,53,50,44,45,47,57,45],
[48,0,55,56,50,53,52,45,50,45,59,54],
[43,45,0,52,48,50,54,44,38,49,46,41],
[38,44,48,0,43,46,45,48,36,42,52,45],
[50,50,52,57,0,53,55,49,50,49,52,44],
[47,47,50,54,47,0,47,50,38,38,49,44],
[50,48,46,55,45,53,0,46,41,43,58,50],
[56,55,56,52,51,50,54,0,45,57,62,53],
[55,50,62,64,50,62,59,55,0,50,54,48],
[53,55,51,58,51,62,57,43,50,0,55,50],
[43,41,54,48,48,51,42,38,46,45,0,46],
[55,46,59,55,56,56,50,47,52,50,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 196, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,44,23,48,60,39,57,34,39,41,43],
[70,0,63,59,57,59,62,67,51,63,66,47],
[56,37,0,48,53,50,57,58,32,44,47,30],
[77,41,52,0,58,59,62,61,36,55,45,39],
[52,43,47,42,0,56,59,72,38,54,55,38],
[40,41,50,41,44,0,51,52,29,52,42,38],
[61,38,43,38,41,49,0,47,32,29,45,44],
[43,33,42,39,28,48,53,0,29,39,44,28],
[66,49,68,64,62,71,68,71,0,69,54,68],
[61,37,56,45,46,48,71,61,31,0,46,40],
[59,34,53,55,45,58,55,56,46,54,0,44],
[57,53,70,61,62,62,56,72,32,60,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 197, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,58,54,49,59,47,45,52,53,50,51],
[53,0,46,51,42,66,44,44,48,40,52,46],
[42,54,0,48,38,59,51,52,44,49,50,45],
[46,49,52,0,51,56,54,53,48,46,54,47],
[51,58,62,49,0,62,55,60,53,61,53,58],
[41,34,41,44,38,0,36,41,46,42,46,40],
[53,56,49,46,45,64,0,45,52,52,54,45],
[55,56,48,47,40,59,55,0,53,48,55,50],
[48,52,56,52,47,54,48,47,0,49,51,47],
[47,60,51,54,39,58,48,52,51,0,54,42],
[50,48,50,46,47,54,46,45,49,46,0,56],
[49,54,55,53,42,60,55,50,53,58,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 198, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,48,69,46,62,53,59,46,64,58,35],
[51,0,48,71,55,52,65,56,47,64,59,54],
[52,52,0,65,54,49,62,54,44,61,59,50],
[31,29,35,0,36,45,33,45,40,41,34,38],
[54,45,46,64,0,67,61,55,48,65,66,47],
[38,48,51,55,33,0,50,52,47,38,42,41],
[47,35,38,67,39,50,0,59,45,47,54,54],
[41,44,46,55,45,48,41,0,46,45,43,34],
[54,53,56,60,52,53,55,54,0,45,62,51],
[36,36,39,59,35,62,53,55,55,0,52,33],
[42,41,41,66,34,58,46,57,38,48,0,38],
[65,46,50,62,53,59,46,66,49,67,62,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 199, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,52,49,46,45,58,47,50,57,51,47],
[43,0,50,47,42,46,43,46,46,43,52,47],
[48,50,0,49,38,51,52,37,43,51,38,45],
[51,53,51,0,44,53,51,49,45,52,47,51],
[54,58,62,56,0,50,46,48,54,52,51,53],
[55,54,49,47,50,0,49,45,54,47,45,52],
[42,57,48,49,54,51,0,45,43,52,45,49],
[53,54,63,51,52,55,55,0,46,53,54,53],
[50,54,57,55,46,46,57,54,0,51,55,55],
[43,57,49,48,48,53,48,47,49,0,42,48],
[49,48,62,53,49,55,55,46,45,58,0,51],
[53,53,55,49,47,48,51,47,45,52,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 100, 200, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebb/mebb_12_100.csv", index=False, header=False)