
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg
from kemeny import sc

rep = 1
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,67,31,44,48,56,63,44,43,37,39],
[34,0,28,32,32,45,47,34,33,36,31],
[70,73,0,62,54,61,63,43,35,54,40],
[57,69,39,0,66,51,59,54,55,39,44],
[53,69,47,35,0,52,50,43,52,50,40],
[45,56,40,50,49,0,51,32,56,52,36],
[38,54,38,42,51,50,0,42,42,50,39],
[57,67,58,47,58,69,59,0,52,60,46],
[58,68,66,46,49,45,59,49,0,48,39],
[64,65,47,62,51,49,51,41,53,0,51],
[62,70,61,57,61,65,62,55,62,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 1, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,67,69,80,63,33,65,72,51,77,65],
[34,0,47,65,67,37,72,85,38,48,46],
[32,54,0,65,62,54,55,52,42,80,39],
[21,36,36,0,61,40,37,53,23,45,41],
[38,34,39,40,0,18,40,55,27,50,43],
[68,64,47,61,83,0,55,74,43,59,58],
[36,29,46,64,61,46,0,70,25,32,40],
[29,16,49,48,46,27,31,0,29,46,33],
[50,63,59,78,74,58,76,72,0,81,58],
[24,53,21,56,51,42,69,55,20,0,33],
[36,55,62,60,58,43,61,68,43,68,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 2, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,56,39,50,47,42,54,62,45,30],
[54,0,55,36,38,41,58,42,52,39,39],
[45,46,0,48,34,36,37,39,55,39,34],
[62,65,53,0,35,49,46,45,67,50,43],
[51,63,67,66,0,42,54,58,70,62,57],
[54,60,65,52,59,0,62,48,67,60,44],
[59,43,64,55,47,39,0,51,65,63,39],
[47,59,62,56,43,53,50,0,52,49,47],
[39,49,46,34,31,34,36,49,0,24,31],
[56,62,62,51,39,41,38,52,77,0,40],
[71,62,67,58,44,57,62,54,70,61,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 3, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,53,58,63,54,46,54,50,54,55],
[47,0,50,49,54,51,46,47,47,49,48],
[48,51,0,48,57,48,53,47,45,53,48],
[43,52,53,0,61,56,47,51,53,57,55],
[38,47,44,40,0,42,44,46,41,46,40],
[47,50,53,45,59,0,51,50,45,56,51],
[55,55,48,54,57,50,0,48,44,48,49],
[47,54,54,50,55,51,53,0,51,50,53],
[51,54,56,48,60,56,57,50,0,54,50],
[47,52,48,44,55,45,53,51,47,0,51],
[46,53,53,46,61,50,52,48,51,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 4, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,47,53,49,60,45,46,54,52,52],
[49,0,44,40,49,50,49,42,48,50,44],
[54,57,0,54,48,62,64,46,48,66,53],
[48,61,47,0,58,68,54,53,56,56,49],
[52,52,53,43,0,53,61,42,49,47,36],
[41,51,39,33,48,0,50,40,43,53,50],
[56,52,37,47,40,51,0,42,42,49,44],
[55,59,55,48,59,61,59,0,53,54,48],
[47,53,53,45,52,58,59,48,0,55,44],
[49,51,35,45,54,48,52,47,46,0,47],
[49,57,48,52,65,51,57,53,57,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 5, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,47,51,48,54,51,54,52,53,49],
[49,0,45,49,42,50,53,45,51,53,41],
[54,56,0,54,50,50,58,49,48,56,46],
[50,52,47,0,52,46,55,51,50,53,52],
[53,59,51,49,0,58,58,51,47,61,49],
[47,51,51,55,43,0,51,55,50,55,49],
[50,48,43,46,43,50,0,45,51,52,47],
[47,56,52,50,50,46,56,0,52,56,50],
[49,50,53,51,54,51,50,49,0,57,56],
[48,48,45,48,40,46,49,45,44,0,45],
[52,60,55,49,52,52,54,51,45,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 6, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,45,44,43,45,47,51,46,55,41],
[54,0,59,47,55,49,50,53,49,59,52],
[56,42,0,47,51,45,51,54,52,55,51],
[57,54,54,0,55,55,53,51,49,57,49],
[58,46,50,46,0,45,50,44,49,54,49],
[56,52,56,46,56,0,58,52,57,55,52],
[54,51,50,48,51,43,0,52,46,60,50],
[50,48,47,50,57,49,49,0,47,64,52],
[55,52,49,52,52,44,55,54,0,62,51],
[46,42,46,44,47,46,41,37,39,0,41],
[60,49,50,52,52,49,51,49,50,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 7, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,49,62,49,50,54,45,53,47,47],
[53,0,42,59,53,43,60,49,53,55,54],
[52,59,0,53,51,45,54,45,52,44,55],
[39,42,48,0,47,33,49,35,48,37,41],
[52,48,50,54,0,54,57,48,53,45,48],
[51,58,56,68,47,0,56,53,56,49,59],
[47,41,47,52,44,45,0,49,51,45,45],
[56,52,56,66,53,48,52,0,59,49,56],
[48,48,49,53,48,45,50,42,0,39,44],
[54,46,57,64,56,52,56,52,62,0,61],
[54,47,46,60,53,42,56,45,57,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 8, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,53,46,36,34,43,44,41,22,47],
[53,0,58,42,40,24,52,38,45,37,39],
[48,43,0,46,46,38,48,41,40,40,52],
[55,59,55,0,39,52,64,41,38,47,45],
[65,61,55,62,0,53,62,49,53,45,53],
[67,77,63,49,48,0,75,51,65,49,66],
[58,49,53,37,39,26,0,53,46,37,49],
[57,63,60,60,52,50,48,0,44,55,43],
[60,56,61,63,48,36,55,57,0,53,53],
[79,64,61,54,56,52,64,46,48,0,49],
[54,62,49,56,48,35,52,58,48,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 9, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,51,54,51,43,54,53,57,53,50],
[44,0,47,55,45,47,43,51,44,52,47],
[50,54,0,52,49,51,54,51,48,49,55],
[47,46,49,0,48,47,44,44,47,49,48],
[50,56,52,53,0,54,52,54,51,53,51],
[58,54,50,54,47,0,51,50,56,54,47],
[47,58,47,57,49,50,0,56,57,54,50],
[48,50,50,57,47,51,45,0,51,52,52],
[44,57,53,54,50,45,44,50,0,55,55],
[48,49,52,52,48,47,47,49,46,0,47],
[51,54,46,53,50,54,51,49,46,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 10, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,52,45,53,44,42,50,48,43,46],
[57,0,54,46,51,53,50,55,51,45,56],
[49,47,0,41,48,53,39,51,47,43,51],
[56,55,60,0,57,53,58,56,53,48,55],
[48,50,53,44,0,49,45,53,50,44,47],
[57,48,48,48,52,0,48,55,51,51,50],
[59,51,62,43,56,53,0,57,52,45,53],
[51,46,50,45,48,46,44,0,46,36,45],
[53,50,54,48,51,50,49,55,0,47,54],
[58,56,58,53,57,50,56,65,54,0,54],
[55,45,50,46,54,51,48,56,47,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 11, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,47,47,49,47,58,44,43,50,54],
[45,0,46,50,46,49,53,43,53,54,53],
[54,55,0,59,61,62,59,48,57,54,55],
[54,51,42,0,52,51,47,51,51,47,47],
[52,55,40,49,0,46,54,49,50,53,55],
[54,52,39,50,55,0,59,49,51,47,52],
[43,48,42,54,47,42,0,45,50,51,47],
[57,58,53,50,52,52,56,0,57,63,60],
[58,48,44,50,51,50,51,44,0,56,51],
[51,47,47,54,48,54,50,38,45,0,53],
[47,48,46,54,46,49,54,41,50,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 12, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,54,32,61,51,58,44,37,43,51],
[47,0,45,50,43,56,47,38,47,47,42],
[47,56,0,49,54,49,66,52,48,54,53],
[69,51,52,0,57,55,55,56,55,57,45],
[40,58,47,44,0,60,38,38,42,36,35],
[50,45,52,46,41,0,48,42,44,46,44],
[43,54,35,46,63,53,0,50,49,53,48],
[57,63,49,45,63,59,51,0,49,41,38],
[64,54,53,46,59,57,52,52,0,52,43],
[58,54,47,44,65,55,48,60,49,0,43],
[50,59,48,56,66,57,53,63,58,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 13, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,33,37,66,43,39,56,51,41,43],
[52,0,25,38,53,49,29,40,44,40,33],
[68,76,0,52,70,64,49,65,49,73,50],
[64,63,49,0,60,48,52,61,55,54,54],
[35,48,31,41,0,45,27,49,48,48,40],
[58,52,37,53,56,0,33,57,53,38,47],
[62,72,52,49,74,68,0,63,67,65,45],
[45,61,36,40,52,44,38,0,40,51,49],
[50,57,52,46,53,48,34,61,0,49,45],
[60,61,28,47,53,63,36,50,52,0,51],
[58,68,51,47,61,54,56,52,56,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 14, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,56,59,50,45,54,43,55,52,52],
[41,0,52,51,47,44,50,43,53,51,39],
[45,49,0,60,44,47,49,38,55,43,41],
[42,50,41,0,38,39,52,39,51,42,37],
[51,54,57,63,0,58,51,49,58,61,50],
[56,57,54,62,43,0,54,50,53,53,55],
[47,51,52,49,50,47,0,43,50,49,50],
[58,58,63,62,52,51,58,0,55,57,50],
[46,48,46,50,43,48,51,46,0,45,48],
[49,50,58,59,40,48,52,44,56,0,47],
[49,62,60,64,51,46,51,51,53,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 15, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,54,49,58,56,62,54,52,58,53],
[45,0,54,39,45,49,48,36,47,47,54],
[47,47,0,39,46,53,43,43,49,57,55],
[52,62,62,0,51,57,61,47,45,51,52],
[43,56,55,50,0,55,53,53,46,52,56],
[45,52,48,44,46,0,60,42,48,50,48],
[39,53,58,40,48,41,0,42,42,48,54],
[47,65,58,54,48,59,59,0,44,57,59],
[49,54,52,56,55,53,59,57,0,57,64],
[43,54,44,50,49,51,53,44,44,0,55],
[48,47,46,49,45,53,47,42,37,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 16, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,41,37,41,43,46,42,50,43,38],
[57,0,45,45,44,61,55,52,61,60,62],
[60,56,0,58,66,56,55,44,70,67,52],
[64,56,43,0,52,52,63,49,61,58,53],
[60,57,35,49,0,59,52,52,54,56,56],
[58,40,45,49,42,0,45,48,54,47,49],
[55,46,46,38,49,56,0,46,62,51,42],
[59,49,57,52,49,53,55,0,61,59,48],
[51,40,31,40,47,47,39,40,0,46,38],
[58,41,34,43,45,54,50,42,55,0,51],
[63,39,49,48,45,52,59,53,63,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 17, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,55,56,53,47,51,42,43,46,41],
[58,0,47,63,52,51,54,53,54,50,50],
[46,54,0,56,53,49,56,44,53,52,38],
[45,38,45,0,48,45,55,42,45,43,56],
[48,49,48,53,0,44,58,42,41,48,54],
[54,50,52,56,57,0,58,46,53,51,55],
[50,47,45,46,43,43,0,25,45,44,40],
[59,48,57,59,59,55,76,0,45,59,48],
[58,47,48,56,60,48,56,56,0,53,47],
[55,51,49,58,53,50,57,42,48,0,49],
[60,51,63,45,47,46,61,53,54,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 18, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,63,61,68,65,66,57,54,48,60,65],
[38,0,43,62,48,58,44,48,50,51,55],
[40,58,0,64,49,59,60,58,50,62,57],
[33,39,37,0,40,52,43,37,40,35,44],
[36,53,52,61,0,48,53,52,43,57,52],
[35,43,42,49,53,0,43,45,46,42,49],
[44,57,41,58,48,58,0,60,50,53,65],
[47,53,43,64,49,56,41,0,52,47,48],
[53,51,51,61,58,55,51,49,0,56,68],
[41,50,39,66,44,59,48,54,45,0,52],
[36,46,44,57,49,52,36,53,33,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 19, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,46,42,52,47,43,52,51,51,51],
[54,0,54,50,57,54,47,62,49,52,52],
[55,47,0,55,52,58,52,57,53,51,53],
[59,51,46,0,49,55,55,52,53,57,54],
[49,44,49,52,0,54,48,53,53,55,55],
[54,47,43,46,47,0,43,56,44,52,47],
[58,54,49,46,53,58,0,56,47,51,52],
[49,39,44,49,48,45,45,0,44,47,44],
[50,52,48,48,48,57,54,57,0,45,56],
[50,49,50,44,46,49,50,54,56,0,48],
[50,49,48,47,46,54,49,57,45,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 20, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,37,47,55,48,49,38,47,53,46,55],
[64,0,52,58,48,66,62,41,59,58,59],
[54,49,0,54,50,53,46,53,53,48,52],
[46,43,47,0,38,43,39,42,39,36,42],
[53,53,51,63,0,55,50,52,53,48,54],
[52,35,48,58,46,0,32,54,44,45,52],
[63,39,55,62,51,69,0,55,50,49,57],
[54,60,48,59,49,47,46,0,45,52,48],
[48,42,48,62,48,57,51,56,0,54,65],
[55,43,53,65,53,56,52,49,47,0,49],
[46,42,49,59,47,49,44,53,36,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 21, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,43,43,43,40,53,48,56,50,46],
[61,0,48,54,46,52,60,64,65,61,68],
[58,53,0,64,49,38,63,51,64,59,57],
[58,47,37,0,37,42,61,56,61,48,50],
[58,55,52,64,0,42,60,66,55,48,59],
[61,49,63,59,59,0,56,66,64,55,64],
[48,41,38,40,41,45,0,47,63,45,44],
[53,37,50,45,35,35,54,0,50,44,50],
[45,36,37,40,46,37,38,51,0,38,44],
[51,40,42,53,53,46,56,57,63,0,51],
[55,33,44,51,42,37,57,51,57,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 22, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,48,54,39,44,60,50,41,49,49],
[49,0,48,60,39,47,51,46,42,52,53],
[53,53,0,62,45,51,53,51,45,51,48],
[47,41,39,0,35,44,46,45,43,40,42],
[62,62,56,66,0,50,60,59,58,50,52],
[57,54,50,57,51,0,59,53,46,49,49],
[41,50,48,55,41,42,0,39,39,50,55],
[51,55,50,56,42,48,62,0,43,49,54],
[60,59,56,58,43,55,62,58,0,53,58],
[52,49,50,61,51,52,51,52,48,0,53],
[52,48,53,59,49,52,46,47,43,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 23, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,50,47,51,53,48,51,45,49,46],
[50,0,52,48,50,59,49,48,48,45,49],
[51,49,0,48,44,57,45,51,51,45,43],
[54,53,53,0,44,53,45,49,47,42,44],
[50,51,57,57,0,53,42,45,54,45,51],
[48,42,44,48,48,0,38,54,43,39,48],
[53,52,56,56,59,63,0,56,47,49,49],
[50,53,50,52,56,47,45,0,50,46,42],
[56,53,50,54,47,58,54,51,0,45,47],
[52,56,56,59,56,62,52,55,56,0,48],
[55,52,58,57,50,53,52,59,54,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 24, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,52,56,52,44,50,51,49,52,50],
[47,0,43,51,46,43,50,52,51,47,53],
[49,58,0,54,54,46,42,52,51,43,54],
[45,50,47,0,45,44,42,58,48,49,54],
[49,55,47,56,0,44,45,51,51,47,55],
[57,58,55,57,57,0,49,62,56,50,59],
[51,51,59,59,56,52,0,51,50,56,56],
[50,49,49,43,50,39,50,0,45,51,53],
[52,50,50,53,50,45,51,56,0,49,58],
[49,54,58,52,54,51,45,50,52,0,50],
[51,48,47,47,46,42,45,48,43,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 25, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,43,59,63,55,66,51,52,47,69],
[51,0,50,59,59,51,66,54,63,48,63],
[58,51,0,52,54,43,60,59,51,47,56],
[42,42,49,0,52,51,64,48,53,42,58],
[38,42,47,49,0,49,57,49,52,47,53],
[46,50,58,50,52,0,62,51,54,47,54],
[35,35,41,37,44,39,0,40,44,30,52],
[50,47,42,53,52,50,61,0,53,51,57],
[49,38,50,48,49,47,57,48,0,48,58],
[54,53,54,59,54,54,71,50,53,0,64],
[32,38,45,43,48,47,49,44,43,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 26, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,50,38,50,52,56,50,46,53,51],
[50,0,49,47,46,48,51,52,46,50,45],
[51,52,0,44,51,55,53,50,52,46,48],
[63,54,57,0,55,56,60,59,53,49,54],
[51,55,50,46,0,53,55,47,48,49,47],
[49,53,46,45,48,0,52,43,47,44,50],
[45,50,48,41,46,49,0,46,51,48,41],
[51,49,51,42,54,58,55,0,51,46,55],
[55,55,49,48,53,54,50,50,0,45,41],
[48,51,55,52,52,57,53,55,56,0,52],
[50,56,53,47,54,51,60,46,60,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 27, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,47,54,40,55,53,56,50,43,48],
[52,0,43,52,56,51,56,46,55,50,58],
[54,58,0,59,41,60,55,55,53,53,59],
[47,49,42,0,42,62,49,56,53,49,57],
[61,45,60,59,0,68,57,63,52,55,65],
[46,50,41,39,33,0,54,51,49,43,60],
[48,45,46,52,44,47,0,47,45,48,57],
[45,55,46,45,38,50,54,0,53,50,55],
[51,46,48,48,49,52,56,48,0,47,61],
[58,51,48,52,46,58,53,51,54,0,60],
[53,43,42,44,36,41,44,46,40,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 28, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,52,47,43,36,43,53,46,50,39],
[50,0,62,55,58,53,43,49,42,54,48],
[49,39,0,42,49,44,33,47,36,48,42],
[54,46,59,0,42,40,40,48,45,56,36],
[58,43,52,59,0,47,47,55,51,46,53],
[65,48,57,61,54,0,53,53,50,56,53],
[58,58,68,61,54,48,0,58,53,56,44],
[48,52,54,53,46,48,43,0,45,51,44],
[55,59,65,56,50,51,48,56,0,53,41],
[51,47,53,45,55,45,45,50,48,0,44],
[62,53,59,65,48,48,57,57,60,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 29, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,44,48,50,50,54,46,47,53,51],
[59,0,50,45,46,50,60,50,48,63,59],
[57,51,0,49,53,59,61,56,56,60,60],
[53,56,52,0,52,51,60,61,49,59,59],
[51,55,48,49,0,50,56,50,44,54,60],
[51,51,42,50,51,0,58,46,51,58,53],
[47,41,40,41,45,43,0,43,44,47,49],
[55,51,45,40,51,55,58,0,48,57,62],
[54,53,45,52,57,50,57,53,0,51,55],
[48,38,41,42,47,43,54,44,50,0,49],
[50,42,41,42,41,48,52,39,46,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 30, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,40,43,51,57,41,43,51,48,53],
[55,0,54,53,57,60,54,49,59,58,52],
[61,47,0,54,54,54,44,48,53,53,55],
[58,48,47,0,50,46,44,46,42,48,54],
[50,44,47,51,0,50,36,47,46,38,53],
[44,41,47,55,51,0,36,47,47,41,55],
[60,47,57,57,65,65,0,52,53,63,55],
[58,52,53,55,54,54,49,0,49,56,55],
[50,42,48,59,55,54,48,52,0,50,57],
[53,43,48,53,63,60,38,45,51,0,59],
[48,49,46,47,48,46,46,46,44,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 31, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,51,50,47,42,45,39,51,50,45],
[49,0,54,43,51,49,44,47,42,47,51],
[50,47,0,46,48,47,50,49,42,49,46],
[51,58,55,0,53,52,52,50,52,61,51],
[54,50,53,48,0,47,49,47,55,55,58],
[59,52,54,49,54,0,47,51,50,54,46],
[56,57,51,49,52,54,0,51,50,59,46],
[62,54,52,51,54,50,50,0,52,55,53],
[50,59,59,49,46,51,51,49,0,49,54],
[51,54,52,40,46,47,42,46,52,0,48],
[56,50,55,50,43,55,55,48,47,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 32, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,52,71,42,44,50,64,50,31,46],
[70,0,66,67,66,42,62,66,58,52,68],
[49,35,0,52,47,38,43,52,38,26,45],
[30,34,49,0,47,31,37,48,34,23,39],
[59,35,54,54,0,46,36,57,40,39,57],
[57,59,63,70,55,0,62,62,50,44,59],
[51,39,58,64,65,39,0,51,48,34,51],
[37,35,49,53,44,39,50,0,45,37,58],
[51,43,63,67,61,51,53,56,0,43,60],
[70,49,75,78,62,57,67,64,58,0,71],
[55,33,56,62,44,42,50,43,41,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 33, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,40,47,46,41,37,49,48,45,35],
[63,0,52,52,53,47,50,55,58,55,45],
[61,49,0,54,59,44,52,58,56,57,46],
[54,49,47,0,47,45,41,53,52,62,46],
[55,48,42,54,0,40,40,47,55,55,39],
[60,54,57,56,61,0,43,53,62,60,49],
[64,51,49,60,61,58,0,59,63,58,53],
[52,46,43,48,54,48,42,0,53,47,49],
[53,43,45,49,46,39,38,48,0,56,43],
[56,46,44,39,46,41,43,54,45,0,39],
[66,56,55,55,62,52,48,52,58,62,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 34, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,48,51,50,49,53,52,54,54,56],
[45,0,42,46,48,52,52,43,47,52,54],
[53,59,0,60,54,56,54,48,60,64,64],
[50,55,41,0,49,51,45,45,54,55,54],
[51,53,47,52,0,49,44,48,50,56,52],
[52,49,45,50,52,0,53,45,50,56,51],
[48,49,47,56,57,48,0,44,53,54,50],
[49,58,53,56,53,56,57,0,51,55,57],
[47,54,41,47,51,51,48,50,0,59,51],
[47,49,37,46,45,45,47,46,42,0,48],
[45,47,37,47,49,50,51,44,50,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 35, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,40,38,65,67,27,67,67,67,40],
[72,0,40,72,38,74,72,101,74,101,74],
[61,61,0,72,27,63,61,63,61,63,36],
[63,29,29,0,29,63,63,63,63,63,63],
[36,63,74,72,0,101,63,63,101,101,74],
[34,27,38,38,0,0,0,27,38,61,0],
[74,29,40,38,38,101,0,101,74,101,74],
[34,0,38,38,38,74,0,0,72,74,74],
[34,27,40,38,0,63,27,29,0,63,2],
[34,0,38,38,0,40,0,27,38,0,0],
[61,27,65,38,27,101,27,27,99,101,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 36, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,54,51,46,55,51,48,50,55,61],
[53,0,54,48,45,51,52,46,43,47,61],
[47,47,0,46,53,49,49,51,49,47,62],
[50,53,55,0,50,48,51,45,45,33,60],
[55,56,48,51,0,56,46,51,46,46,64],
[46,50,52,53,45,0,49,45,47,49,60],
[50,49,52,50,55,52,0,54,50,42,57],
[53,55,50,56,50,56,47,0,55,51,57],
[51,58,52,56,55,54,51,46,0,51,64],
[46,54,54,68,55,52,59,50,50,0,63],
[40,40,39,41,37,41,44,44,37,38,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 37, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,45,41,32,53,54,43,44,32,41],
[43,0,45,39,32,45,53,51,52,35,47],
[56,56,0,39,39,61,57,42,59,59,52],
[60,62,62,0,55,71,71,67,66,50,65],
[69,69,62,46,0,67,68,59,61,67,63],
[48,56,40,30,34,0,49,35,49,38,30],
[47,48,44,30,33,52,0,43,45,30,42],
[58,50,59,34,42,66,58,0,53,42,51],
[57,49,42,35,40,52,56,48,0,45,49],
[69,66,42,51,34,63,71,59,56,0,62],
[60,54,49,36,38,71,59,50,52,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 38, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,52,53,48,57,44,48,50,54,60],
[56,0,50,53,55,56,55,57,50,61,56],
[49,51,0,46,47,49,44,42,46,52,54],
[48,48,55,0,48,47,43,51,49,57,60],
[53,46,54,53,0,58,50,55,51,64,55],
[44,45,52,54,43,0,48,53,51,55,59],
[57,46,57,58,51,53,0,62,56,61,61],
[53,44,59,50,46,48,39,0,46,54,61],
[51,51,55,52,50,50,45,55,0,53,59],
[47,40,49,44,37,46,40,47,48,0,53],
[41,45,47,41,46,42,40,40,42,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 39, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,63,56,47,50,50,51,42,53,47],
[48,0,53,48,52,39,48,47,48,49,44],
[38,48,0,46,46,38,47,42,39,45,37],
[45,53,55,0,51,42,52,52,51,48,43],
[54,49,55,50,0,42,50,55,51,46,43],
[51,62,63,59,59,0,60,53,55,60,49],
[51,53,54,49,51,41,0,48,45,51,43],
[50,54,59,49,46,48,53,0,51,49,46],
[59,53,62,50,50,46,56,50,0,47,47],
[48,52,56,53,55,41,50,52,54,0,52],
[54,57,64,58,58,52,58,55,54,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 40, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,40,31,63,23,33,31,79,40,49],
[48,0,26,17,26,9,10,17,42,1,48],
[61,75,0,68,61,59,45,36,100,36,68],
[70,84,33,0,68,32,32,59,85,32,54],
[38,75,40,33,0,39,49,31,101,16,71],
[78,92,42,69,62,0,56,69,78,55,48],
[68,91,56,69,52,45,0,68,92,54,70],
[70,84,65,42,70,32,33,0,101,48,70],
[22,59,1,16,0,23,9,0,0,0,31],
[61,100,65,69,85,46,47,53,101,0,71],
[52,53,33,47,30,53,31,31,70,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 41, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,51,49,42,51,53,47,49,51,53],
[55,0,55,53,51,53,49,53,61,53,61],
[50,46,0,60,48,53,52,53,53,53,58],
[52,48,41,0,49,56,53,55,54,53,58],
[59,50,53,52,0,60,54,58,52,58,58],
[50,48,48,45,41,0,50,50,46,53,53],
[48,52,49,48,47,51,0,50,57,49,57],
[54,48,48,46,43,51,51,0,52,58,58],
[52,40,48,47,49,55,44,49,0,48,55],
[50,48,48,48,43,48,52,43,53,0,53],
[48,40,43,43,43,48,44,43,46,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 42, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,50,39,47,37,59,64,44,48,47],
[52,0,58,50,56,36,48,55,57,59,51],
[51,43,0,57,56,45,57,46,46,48,50],
[62,51,44,0,53,50,61,60,57,45,53],
[54,45,45,48,0,43,63,52,50,49,51],
[64,65,56,51,58,0,64,58,50,53,56],
[42,53,44,40,38,37,0,41,45,47,47],
[37,46,55,41,49,43,60,0,47,51,51],
[57,44,55,44,51,51,56,54,0,56,52],
[53,42,53,56,52,48,54,50,45,0,46],
[54,50,51,48,50,45,54,50,49,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 43, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,48,52,41,69,51,47,43,54,47],
[57,0,50,63,54,67,62,54,64,52,57],
[53,51,0,49,43,64,57,47,49,47,48],
[49,38,52,0,45,61,59,38,49,48,36],
[60,47,58,56,0,67,62,51,64,65,57],
[32,34,37,40,34,0,46,31,41,32,29],
[50,39,44,42,39,55,0,37,45,44,40],
[54,47,54,63,50,70,64,0,52,55,49],
[58,37,52,52,37,60,56,49,0,45,51],
[47,49,54,53,36,69,57,46,56,0,53],
[54,44,53,65,44,72,61,52,50,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 44, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,39,56,39,51,55,59,55,34,56],
[58,0,46,56,37,53,56,47,58,50,67],
[62,55,0,72,56,63,49,73,63,57,68],
[45,45,29,0,40,50,22,44,47,24,43],
[62,64,45,61,0,64,44,55,68,41,71],
[50,48,38,51,37,0,40,46,54,39,64],
[46,45,52,79,57,61,0,67,69,45,69],
[42,54,28,57,46,55,34,0,51,36,45],
[46,43,38,54,33,47,32,50,0,34,67],
[67,51,44,77,60,62,56,65,67,0,79],
[45,34,33,58,30,37,32,56,34,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 45, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,51,32,45,44,52,46,45,39,57],
[67,0,66,46,56,57,52,64,63,59,63],
[50,35,0,43,47,55,57,47,49,50,46],
[69,55,58,0,60,58,44,50,68,60,60],
[56,45,54,41,0,55,48,45,50,54,53],
[57,44,46,43,46,0,51,58,46,45,50],
[49,49,44,57,53,50,0,50,53,51,52],
[55,37,54,51,56,43,51,0,59,53,55],
[56,38,52,33,51,55,48,42,0,51,40],
[62,42,51,41,47,56,50,48,50,0,56],
[44,38,55,41,48,51,49,46,61,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 46, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,72,62,55,77,53,49,64,45,52],
[48,0,59,57,55,80,52,45,68,54,47],
[29,42,0,42,45,65,34,20,34,46,44],
[39,44,59,0,48,60,34,41,52,44,31],
[46,46,56,53,0,76,43,49,43,50,55],
[24,21,36,41,25,0,32,38,33,29,38],
[48,49,67,67,58,69,0,55,60,44,47],
[52,56,81,60,52,63,46,0,70,53,51],
[37,33,67,49,58,68,41,31,0,40,45],
[56,47,55,57,51,72,57,48,61,0,58],
[49,54,57,70,46,63,54,50,56,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 47, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,54,55,54,50,52,50,56,57,52],
[44,0,49,50,53,46,61,51,54,57,52],
[47,52,0,56,50,43,52,50,57,57,49],
[46,51,45,0,48,47,39,45,53,56,49],
[47,48,51,53,0,46,52,52,60,51,53],
[51,55,58,54,55,0,48,58,61,58,55],
[49,40,49,62,49,53,0,48,51,55,51],
[51,50,51,56,49,43,53,0,49,49,57],
[45,47,44,48,41,40,50,52,0,62,48],
[44,44,44,45,50,43,46,52,39,0,49],
[49,49,52,52,48,46,50,44,53,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 48, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,59,48,48,41,46,37,42,57,42],
[61,0,70,64,71,60,54,61,66,43,53],
[42,31,0,41,36,37,34,35,48,58,28],
[53,37,60,0,47,44,49,51,51,47,45],
[53,30,65,54,0,45,55,48,57,53,51],
[60,41,64,57,56,0,51,45,49,52,53],
[55,47,67,52,46,50,0,41,58,55,58],
[64,40,66,50,53,56,60,0,67,49,48],
[59,35,53,50,44,52,43,34,0,56,40],
[44,58,43,54,48,49,46,52,45,0,44],
[59,48,73,56,50,48,43,53,61,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 49, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,62,52,48,56,54,54,52,61,57],
[42,0,58,56,53,50,46,41,60,56,47],
[39,43,0,49,46,49,42,45,45,53,47],
[49,45,52,0,47,51,51,44,47,45,51],
[53,48,55,54,0,46,46,51,45,54,49],
[45,51,52,50,55,0,47,44,44,52,52],
[47,55,59,50,55,54,0,46,54,49,54],
[47,60,56,57,50,57,55,0,57,56,54],
[49,41,56,54,56,57,47,44,0,46,46],
[40,45,48,56,47,49,52,45,55,0,52],
[44,54,54,50,52,49,47,47,55,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 50, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,52,55,52,57,53,46,54,56,44],
[46,0,56,49,53,49,56,51,47,56,45],
[49,45,0,47,59,47,51,45,51,57,40],
[46,52,54,0,58,51,54,37,60,58,50],
[49,48,42,43,0,41,41,46,43,46,45],
[44,52,54,50,60,0,53,42,51,56,49],
[48,45,50,47,60,48,0,46,49,57,50],
[55,50,56,64,55,59,55,0,67,62,57],
[47,54,50,41,58,50,52,34,0,53,44],
[45,45,44,43,55,45,44,39,48,0,43],
[57,56,61,51,56,52,51,44,57,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 51, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,61,44,53,33,47,53,22,47,78],
[77,0,65,48,75,50,76,55,32,76,85],
[40,36,0,36,46,52,56,39,31,56,71],
[57,53,65,0,70,43,76,36,51,69,57],
[48,26,55,31,0,45,47,57,24,57,80],
[68,51,49,58,56,0,58,42,41,43,52],
[54,25,45,25,54,43,0,16,41,31,41],
[48,46,62,65,44,59,85,0,60,76,69],
[79,69,70,50,77,60,60,41,0,60,79],
[54,25,45,32,44,58,70,25,41,0,41],
[23,16,30,44,21,49,60,32,22,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 52, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,47,47,48,51,45,52,37,40,44],
[65,0,57,49,64,62,62,55,42,58,59],
[54,44,0,53,59,62,61,57,42,55,54],
[54,52,48,0,61,56,54,52,49,51,55],
[53,37,42,40,0,52,65,51,44,38,42],
[50,39,39,45,49,0,56,41,44,46,46],
[56,39,40,47,36,45,0,39,52,50,42],
[49,46,44,49,50,60,62,0,41,39,50],
[64,59,59,52,57,57,49,60,0,60,50],
[61,43,46,50,63,55,51,62,41,0,52],
[57,42,47,46,59,55,59,51,51,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 53, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,46,55,56,44,57,45,49,49,51],
[46,0,56,55,54,52,54,45,51,58,48],
[55,45,0,56,53,53,58,60,52,55,56],
[46,46,45,0,50,41,49,42,44,48,50],
[45,47,48,51,0,58,50,53,50,55,58],
[57,49,48,60,43,0,55,45,53,45,54],
[44,47,43,52,51,46,0,47,42,51,49],
[56,56,41,59,48,56,54,0,53,57,50],
[52,50,49,57,51,48,59,48,0,48,50],
[52,43,46,53,46,56,50,44,53,0,53],
[50,53,45,51,43,47,52,51,51,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 54, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,62,67,51,48,43,53,48,40,53],
[60,0,49,59,53,55,64,68,52,56,52],
[39,52,0,44,58,54,50,67,55,53,51],
[34,42,57,0,46,50,44,55,37,39,41],
[50,48,43,55,0,53,58,66,57,48,52],
[53,46,47,51,48,0,46,54,42,45,37],
[58,37,51,57,43,55,0,55,30,50,44],
[48,33,34,46,35,47,46,0,37,34,43],
[53,49,46,64,44,59,71,64,0,55,47],
[61,45,48,62,53,56,51,67,46,0,45],
[48,49,50,60,49,64,57,58,54,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 55, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,40,41,49,51,58,46,50,43,40],
[58,0,57,50,64,65,56,59,59,54,58],
[61,44,0,54,62,61,56,61,56,46,51],
[60,51,47,0,59,54,50,52,60,55,57],
[52,37,39,42,0,56,43,48,43,49,51],
[50,36,40,47,45,0,53,53,47,45,42],
[43,45,45,51,58,48,0,54,48,37,42],
[55,42,40,49,53,48,47,0,56,43,45],
[51,42,45,41,58,54,53,45,0,41,44],
[58,47,55,46,52,56,64,58,60,0,59],
[61,43,50,44,50,59,59,56,57,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 56, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,61,49,58,53,48,53,41,54,48],
[52,0,64,48,47,50,40,57,48,48,51],
[40,37,0,43,48,44,43,48,43,39,40],
[52,53,58,0,59,52,42,58,52,44,53],
[43,54,53,42,0,40,41,56,55,45,47],
[48,51,57,49,61,0,44,54,46,44,49],
[53,61,58,59,60,57,0,58,49,46,54],
[48,44,53,43,45,47,43,0,47,44,40],
[60,53,58,49,46,55,52,54,0,53,46],
[47,53,62,57,56,57,55,57,48,0,60],
[53,50,61,48,54,52,47,61,55,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 57, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,42,51,46,53,55,66,61,30,36],
[53,0,52,60,53,72,70,74,50,53,36],
[59,49,0,32,53,49,70,74,54,51,70],
[50,41,69,0,51,52,57,59,40,36,40],
[55,48,48,50,0,60,42,57,51,33,31],
[48,29,52,49,41,0,41,71,44,27,39],
[46,31,31,44,59,60,0,83,55,38,39],
[35,27,27,42,44,30,18,0,35,32,28],
[40,51,47,61,50,57,46,66,0,42,40],
[71,48,50,65,68,74,63,69,59,0,45],
[65,65,31,61,70,62,62,73,61,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 58, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,37,42,50,51,47,56,46,49,48],
[56,0,38,55,52,44,47,57,44,56,57],
[64,63,0,54,52,49,55,61,56,57,55],
[59,46,47,0,57,47,45,51,47,55,55],
[51,49,49,44,0,43,44,48,43,44,43],
[50,57,52,54,58,0,48,57,47,60,58],
[54,54,46,56,57,53,0,72,55,56,59],
[45,44,40,50,53,44,29,0,45,48,52],
[55,57,45,54,58,54,46,56,0,50,53],
[52,45,44,46,57,41,45,53,51,0,48],
[53,44,46,46,58,43,42,49,48,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 59, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,57,62,58,47,53,56,56,59,61],
[49,0,59,55,52,51,62,49,50,63,48],
[44,42,0,56,50,38,45,53,51,51,49],
[39,46,45,0,40,31,44,43,42,50,45],
[43,49,51,61,0,48,51,50,47,57,55],
[54,50,63,70,53,0,53,63,63,58,60],
[48,39,56,57,50,48,0,60,53,52,56],
[45,52,48,58,51,38,41,0,46,39,40],
[45,51,50,59,54,38,48,55,0,62,53],
[42,38,50,51,44,43,49,62,39,0,36],
[40,53,52,56,46,41,45,61,48,65,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 60, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,51,49,59,56,58,50,50,53,51],
[52,0,57,41,46,58,54,61,50,57,52],
[50,44,0,44,57,50,48,55,47,53,54],
[52,60,57,0,60,62,59,70,62,63,50],
[42,55,44,41,0,46,53,46,41,47,50],
[45,43,51,39,55,0,51,60,52,55,49],
[43,47,53,42,48,50,0,53,42,62,38],
[51,40,46,31,55,41,48,0,36,60,40],
[51,51,54,39,60,49,59,65,0,61,53],
[48,44,48,38,54,46,39,41,40,0,32],
[50,49,47,51,51,52,63,61,48,69,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 61, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,55,54,54,45,53,63,62,51,56],
[45,0,52,48,50,45,47,54,48,42,42],
[46,49,0,45,47,42,44,57,49,50,51],
[47,53,56,0,52,46,44,57,51,45,51],
[47,51,54,49,0,42,45,49,52,48,48],
[56,56,59,55,59,0,45,64,58,50,56],
[48,54,57,57,56,56,0,69,56,60,57],
[38,47,44,44,52,37,32,0,46,38,52],
[39,53,52,50,49,43,45,55,0,49,57],
[50,59,51,56,53,51,41,63,52,0,58],
[45,59,50,50,53,45,44,49,44,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 62, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,26,42,34,26,51,40,42,38,34],
[56,0,44,43,42,38,65,42,50,57,34],
[75,57,0,58,61,57,78,57,56,50,55],
[59,58,43,0,52,49,72,66,59,54,45],
[67,59,40,49,0,45,68,59,54,52,52],
[75,63,44,52,56,0,71,51,53,57,57],
[50,36,23,29,33,30,0,45,35,35,22],
[61,59,44,35,42,50,56,0,60,54,41],
[59,51,45,42,47,48,66,41,0,47,44],
[63,44,51,47,49,44,66,47,54,0,48],
[67,67,46,56,49,44,79,60,57,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 63, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,57,53,52,53,67,54,76,50,76],
[47,0,40,60,41,65,66,52,54,49,57],
[44,61,0,61,46,47,70,50,59,44,71],
[48,41,40,0,50,48,55,37,51,43,48],
[49,60,55,51,0,48,68,45,60,54,65],
[48,36,54,53,53,0,74,55,60,64,55],
[34,35,31,46,33,27,0,32,38,38,32],
[47,49,51,64,56,46,69,0,67,58,51],
[25,47,42,50,41,41,63,34,0,39,45],
[51,52,57,58,47,37,63,43,62,0,41],
[25,44,30,53,36,46,69,50,56,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 64, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,51,62,49,51,55,58,50,61,55],
[41,0,44,57,56,46,51,47,47,59,50],
[50,57,0,52,46,49,50,57,48,50,52],
[39,44,49,0,39,42,48,47,44,53,47],
[52,45,55,62,0,54,54,54,51,52,52],
[50,55,52,59,47,0,56,48,52,56,52],
[46,50,51,53,47,45,0,55,52,59,48],
[43,54,44,54,47,53,46,0,44,58,49],
[51,54,53,57,50,49,49,57,0,61,49],
[40,42,51,48,49,45,42,43,40,0,40],
[46,51,49,54,49,49,53,52,52,61,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 65, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,51,65,59,60,71,63,56,49,62],
[49,0,59,65,56,59,71,62,56,59,62],
[50,42,0,52,55,54,65,57,55,53,54],
[36,36,49,0,46,44,67,51,58,51,42],
[42,45,46,55,0,49,61,51,46,44,48],
[41,42,47,57,52,0,60,55,58,50,45],
[30,30,36,34,40,41,0,46,45,33,37],
[38,39,44,50,50,46,55,0,49,42,50],
[45,45,46,43,55,43,56,52,0,45,49],
[52,42,48,50,57,51,68,59,56,0,52],
[39,39,47,59,53,56,64,51,52,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 66, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,43,48,49,63,43,41,42,40,61],
[49,0,39,43,41,44,56,47,45,48,56],
[58,62,0,62,58,61,50,58,58,65,70],
[53,58,39,0,52,49,34,39,54,31,57],
[52,60,43,49,0,47,41,49,49,47,72],
[38,57,40,52,54,0,46,49,44,32,56],
[58,45,51,67,60,55,0,55,53,50,65],
[60,54,43,62,52,52,46,0,51,36,60],
[59,56,43,47,52,57,48,50,0,31,64],
[61,53,36,70,54,69,51,65,70,0,67],
[40,45,31,44,29,45,36,41,37,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 67, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,43,57,63,49,52,45,48,48,49],
[56,0,56,59,56,58,56,50,56,54,59],
[58,45,0,60,53,43,47,44,48,49,50],
[44,42,41,0,47,60,52,45,42,47,50],
[38,45,48,54,0,52,52,43,39,49,45],
[52,43,58,41,49,0,53,51,48,51,64],
[49,45,54,49,49,48,0,51,46,52,44],
[56,51,57,56,58,50,50,0,46,49,54],
[53,45,53,59,62,53,55,55,0,53,62],
[53,47,52,54,52,50,49,52,48,0,52],
[52,42,51,51,56,37,57,47,39,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 68, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,56,53,57,62,50,53,51,60,62],
[40,0,36,46,39,48,43,50,39,55,60],
[45,65,0,50,61,66,60,66,59,68,66],
[48,55,51,0,56,46,66,73,57,55,61],
[44,62,40,45,0,58,60,56,43,52,54],
[39,53,35,55,43,0,61,60,35,61,52],
[51,58,41,35,41,40,0,50,43,63,54],
[48,51,35,28,45,41,51,0,46,56,50],
[50,62,42,44,58,66,58,55,0,65,72],
[41,46,33,46,49,40,38,45,36,0,56],
[39,41,35,40,47,49,47,51,29,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 69, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,49,53,46,48,50,45,53,48,42],
[44,0,34,48,44,46,38,38,46,39,43],
[52,67,0,51,52,53,54,55,60,54,43],
[48,53,50,0,47,46,49,45,45,51,53],
[55,57,49,54,0,47,55,49,56,51,54],
[53,55,48,55,54,0,55,39,51,50,44],
[51,63,47,52,46,46,0,44,43,53,39],
[56,63,46,56,52,62,57,0,55,51,45],
[48,55,41,56,45,50,58,46,0,47,51],
[53,62,47,50,50,51,48,50,54,0,47],
[59,58,58,48,47,57,62,56,50,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 70, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,76,37,30,44,57,67,91,84,78,63],
[25,0,31,34,16,57,45,32,59,66,54],
[64,70,0,51,48,74,71,67,86,87,59],
[71,67,50,0,57,69,65,71,79,71,83],
[57,85,53,44,0,52,73,74,62,92,65],
[44,44,27,32,49,0,30,44,57,74,39],
[34,56,30,36,28,71,0,33,68,64,54],
[10,69,34,30,27,57,68,0,77,64,54],
[17,42,15,22,39,44,33,24,0,61,22],
[23,35,14,30,9,27,37,37,40,0,31],
[38,47,42,18,36,62,47,47,79,70,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 71, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,48,45,47,58,38,48,32,55,40],
[48,0,40,32,49,67,37,53,40,66,50],
[53,61,0,38,47,62,43,58,53,63,51],
[56,69,63,0,51,60,34,57,43,71,43],
[54,52,54,50,0,55,40,44,49,56,52],
[43,34,39,41,46,0,31,42,43,52,39],
[63,64,58,67,61,70,0,72,64,78,46],
[53,48,43,44,57,59,29,0,46,62,36],
[69,61,48,58,52,58,37,55,0,71,48],
[46,35,38,30,45,49,23,39,30,0,38],
[61,51,50,58,49,62,55,65,53,63,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 72, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,76,54,50,66,60,55,62,60,67,47],
[25,0,40,32,54,33,43,56,32,43,51],
[47,61,0,47,55,65,53,61,52,63,60],
[51,69,54,0,61,64,59,63,42,61,43],
[35,47,46,40,0,45,49,57,43,44,52],
[41,68,36,37,56,0,46,57,34,54,49],
[46,58,48,42,52,55,0,56,33,51,42],
[39,45,40,38,44,44,45,0,31,46,40],
[41,69,49,59,58,67,68,70,0,68,58],
[34,58,38,40,57,47,50,55,33,0,42],
[54,50,41,58,49,52,59,61,43,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 73, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,47,47,45,49,46,41,47,36,51],
[56,0,65,52,46,55,59,61,54,47,54],
[54,36,0,44,37,48,48,38,45,41,45],
[54,49,57,0,53,60,47,49,55,36,49],
[56,55,64,48,0,55,58,52,57,42,60],
[52,46,53,41,46,0,51,38,57,39,40],
[55,42,53,54,43,50,0,47,49,39,53],
[60,40,63,52,49,63,54,0,60,51,63],
[54,47,56,46,44,44,52,41,0,37,53],
[65,54,60,65,59,62,62,50,64,0,55],
[50,47,56,52,41,61,48,38,48,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 74, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,48,37,50,48,43,39,45,60,56],
[57,0,60,51,65,55,54,48,47,64,59],
[53,41,0,35,52,53,41,39,29,54,58],
[64,50,66,0,55,50,61,40,34,63,55],
[51,36,49,46,0,64,42,42,36,54,59],
[53,46,48,51,37,0,48,34,49,47,45],
[58,47,60,40,59,53,0,51,52,55,54],
[62,53,62,61,59,67,50,0,47,57,60],
[56,54,72,67,65,52,49,54,0,65,54],
[41,37,47,38,47,54,46,44,36,0,62],
[45,42,43,46,42,56,47,41,47,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 75, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,49,49,44,49,56,51,51,51,52],
[45,0,43,42,40,52,48,41,39,52,45],
[52,58,0,43,44,45,55,50,51,51,53],
[52,59,58,0,48,50,56,57,52,52,57],
[57,61,57,53,0,51,58,51,48,55,55],
[52,49,56,51,50,0,61,53,52,54,48],
[45,53,46,45,43,40,0,46,48,45,47],
[50,60,51,44,50,48,55,0,48,51,45],
[50,62,50,49,53,49,53,53,0,50,49],
[50,49,50,49,46,47,56,50,51,0,46],
[49,56,48,44,46,53,54,56,52,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 76, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,57,53,58,55,48,54,57,54,46],
[51,0,54,47,55,52,49,61,67,48,47],
[44,47,0,46,60,56,52,53,58,50,50],
[48,54,55,0,56,51,56,63,60,52,53],
[43,46,41,45,0,32,40,53,46,45,38],
[46,49,45,50,69,0,56,56,55,55,49],
[53,52,49,45,61,45,0,52,52,50,47],
[47,40,48,38,48,45,49,0,48,51,42],
[44,34,43,41,55,46,49,53,0,46,45],
[47,53,51,49,56,46,51,50,55,0,48],
[55,54,51,48,63,52,54,59,56,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 77, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,43,42,37,45,45,50,42,52,57],
[61,0,58,55,56,46,44,67,50,65,61],
[58,43,0,40,52,43,49,58,60,52,59],
[59,46,61,0,43,45,53,56,51,68,63],
[64,45,49,58,0,51,44,57,55,66,49],
[56,55,58,56,50,0,42,58,52,73,65],
[56,57,52,48,57,59,0,61,52,63,62],
[51,34,43,45,44,43,40,0,40,45,54],
[59,51,41,50,46,49,49,61,0,58,57],
[49,36,49,33,35,28,38,56,43,0,55],
[44,40,42,38,52,36,39,47,44,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 78, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,56,58,64,52,57,75,62,75,47],
[45,0,54,46,50,55,62,59,42,71,47],
[45,47,0,65,75,73,65,75,62,72,69],
[43,55,36,0,67,76,58,84,71,66,56],
[37,51,26,34,0,39,55,47,51,48,47],
[49,46,28,25,62,0,53,70,57,57,46],
[44,39,36,43,46,48,0,50,51,55,28],
[26,42,26,17,54,31,51,0,35,49,51],
[39,59,39,30,50,44,50,66,0,66,46],
[26,30,29,35,53,44,46,52,35,0,51],
[54,54,32,45,54,55,73,50,55,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 79, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,29,38,67,19,54,48,28,30,46],
[84,0,53,40,69,52,69,56,49,59,68],
[72,48,0,72,67,50,66,48,48,63,62],
[63,61,29,0,59,61,66,64,60,42,65],
[34,32,34,42,0,31,55,35,34,45,47],
[82,49,51,40,70,0,66,35,40,20,65],
[47,32,35,35,46,35,0,32,47,26,46],
[53,45,53,37,66,66,69,0,46,40,59],
[73,52,53,41,67,61,54,55,0,44,47],
[71,42,38,59,56,81,75,61,57,0,59],
[55,33,39,36,54,36,55,42,54,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 80, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,41,53,42,44,55,48,46,51,53],
[60,0,62,58,49,50,65,57,47,57,63],
[60,39,0,50,53,48,54,56,51,48,51],
[48,43,51,0,42,48,55,48,40,43,41],
[59,52,48,59,0,54,59,59,58,54,57],
[57,51,53,53,47,0,59,55,52,43,50],
[46,36,47,46,42,42,0,47,42,47,41],
[53,44,45,53,42,46,54,0,48,49,48],
[55,54,50,61,43,49,59,53,0,49,52],
[50,44,53,58,47,58,54,52,52,0,47],
[48,38,50,60,44,51,60,53,49,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 81, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,39,45,38,52,31,38,44,37,41],
[59,0,46,48,49,62,33,40,65,56,64],
[62,55,0,46,50,56,55,38,53,56,63],
[56,53,55,0,52,53,47,58,49,50,59],
[63,52,51,49,0,55,47,41,72,54,68],
[49,39,45,48,46,0,35,35,55,45,54],
[70,68,46,54,54,66,0,52,59,59,61],
[63,61,63,43,60,66,49,0,69,61,74],
[57,36,48,52,29,46,42,32,0,49,48],
[64,45,45,51,47,56,42,40,52,0,42],
[60,37,38,42,33,47,40,27,53,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 82, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,44,49,41,53,39,49,46,53,49],
[58,0,49,46,49,56,40,49,44,54,53],
[57,52,0,57,48,56,48,53,50,54,48],
[52,55,44,0,48,53,44,53,38,54,50],
[60,52,53,53,0,58,50,53,54,61,49],
[48,45,45,48,43,0,38,48,49,51,38],
[62,61,53,57,51,63,0,54,50,58,56],
[52,52,48,48,48,53,47,0,53,59,47],
[55,57,51,63,47,52,51,48,0,52,52],
[48,47,47,47,40,50,43,42,49,0,40],
[52,48,53,51,52,63,45,54,49,61,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 83, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,46,62,48,48,54,64,52,61,56],
[44,0,43,57,53,49,41,60,46,51,52],
[55,58,0,53,55,60,47,67,47,69,45],
[39,44,48,0,48,40,42,55,48,47,48],
[53,48,46,53,0,46,39,46,46,55,52],
[53,52,41,61,55,0,51,56,41,69,50],
[47,60,54,59,62,50,0,60,60,72,58],
[37,41,34,46,55,45,41,0,42,58,50],
[49,55,54,53,55,60,41,59,0,57,41],
[40,50,32,54,46,32,29,43,44,0,37],
[45,49,56,53,49,51,43,51,60,64,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 84, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,64,47,52,48,37,60,46,43,40],
[56,0,69,51,58,46,46,53,56,56,59],
[37,32,0,30,48,32,29,48,39,52,42],
[54,50,71,0,60,50,48,61,56,59,57],
[49,43,53,41,0,39,43,57,51,48,47],
[53,55,69,51,62,0,54,60,49,55,51],
[64,55,72,53,58,47,0,63,66,66,65],
[41,48,53,40,44,41,38,0,51,42,47],
[55,45,62,45,50,52,35,50,0,54,50],
[58,45,49,42,53,46,35,59,47,0,57],
[61,42,59,44,54,50,36,54,51,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 85, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,53,48,48,41,41,43,37,54,49],
[54,0,55,50,54,47,52,56,41,57,51],
[48,46,0,41,42,39,42,47,43,57,43],
[53,51,60,0,53,54,47,55,43,55,55],
[53,47,59,48,0,50,48,46,47,50,48],
[60,54,62,47,51,0,53,50,45,56,50],
[60,49,59,54,53,48,0,55,53,54,52],
[58,45,54,46,55,51,46,0,40,55,52],
[64,60,58,58,54,56,48,61,0,59,58],
[47,44,44,46,51,45,47,46,42,0,52],
[52,50,58,46,53,51,49,49,43,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 86, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,66,57,62,59,42,59,61,54,54],
[50,0,66,43,71,51,58,46,58,29,43],
[35,35,0,40,57,39,39,34,28,32,33],
[44,58,61,0,75,46,37,43,41,41,53],
[39,30,44,26,0,36,46,44,39,39,39],
[42,50,62,55,65,0,47,50,57,55,53],
[59,43,62,64,55,54,0,38,52,55,48],
[42,55,67,58,57,51,63,0,45,65,55],
[40,43,73,60,62,44,49,56,0,35,39],
[47,72,69,60,62,46,46,36,66,0,48],
[47,58,68,48,62,48,53,46,62,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 87, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,60,48,50,58,53,59,56,58,45],
[51,0,56,50,51,57,52,56,48,59,55],
[41,45,0,49,51,53,50,53,51,51,47],
[53,51,52,0,53,53,54,54,56,56,49],
[51,50,50,48,0,56,52,49,49,51,42],
[43,44,48,48,45,0,45,54,41,49,43],
[48,49,51,47,49,56,0,53,47,45,40],
[42,45,48,47,52,47,48,0,51,55,44],
[45,53,50,45,52,60,54,50,0,51,49],
[43,42,50,45,50,52,56,46,50,0,49],
[56,46,54,52,59,58,61,57,52,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 88, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,47,57,49,56,51,50,56,48,43],
[48,0,51,53,55,48,53,52,60,56,49],
[54,50,0,51,49,56,54,48,57,51,55],
[44,48,50,0,48,52,49,49,55,53,56],
[52,46,52,53,0,52,59,52,56,51,50],
[45,53,45,49,49,0,51,49,57,50,48],
[50,48,47,52,42,50,0,54,56,51,44],
[51,49,53,52,49,52,47,0,51,46,43],
[45,41,44,46,45,44,45,50,0,44,44],
[53,45,50,48,50,51,50,55,57,0,49],
[58,52,46,45,51,53,57,58,57,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 89, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,59,53,52,52,50,54,56,46,52],
[50,0,51,51,47,46,46,46,53,47,50],
[42,50,0,50,38,43,45,44,45,41,40],
[48,50,51,0,45,53,46,42,56,45,50],
[49,54,63,56,0,51,53,45,52,50,58],
[49,55,58,48,50,0,44,51,58,49,51],
[51,55,56,55,48,57,0,48,52,52,50],
[47,55,57,59,56,50,53,0,55,53,50],
[45,48,56,45,49,43,49,46,0,51,52],
[55,54,60,56,51,52,49,48,50,0,50],
[49,51,61,51,43,50,51,51,49,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 90, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,56,51,51,46,49,34,47,49,62],
[54,0,39,46,50,45,59,52,47,45,58],
[45,62,0,53,40,48,60,40,41,52,60],
[50,55,48,0,51,43,55,45,41,50,60],
[50,51,61,50,0,47,60,46,48,52,56],
[55,56,53,58,54,0,62,46,52,67,54],
[52,42,41,46,41,39,0,31,37,42,54],
[67,49,61,56,55,55,70,0,59,58,66],
[54,54,60,60,53,49,64,42,0,58,61],
[52,56,49,51,49,34,59,43,43,0,51],
[39,43,41,41,45,47,47,35,40,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 91, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,52,49,56,54,56,43,55,49,47],
[49,0,55,47,53,48,59,49,53,52,45],
[49,46,0,50,56,44,45,49,34,43,45],
[52,54,51,0,57,55,61,59,49,60,54],
[45,48,45,44,0,58,52,46,42,42,51],
[47,53,57,46,43,0,49,49,46,50,40],
[45,42,56,40,49,52,0,43,51,50,43],
[58,52,52,42,55,52,58,0,52,52,48],
[46,48,67,52,59,55,50,49,0,53,48],
[52,49,58,41,59,51,51,49,48,0,54],
[54,56,56,47,50,61,58,53,53,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 92, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,46,47,49,45,46,42,50,38,53],
[55,0,54,54,57,49,51,46,51,52,59],
[55,47,0,52,52,48,49,47,54,43,55],
[54,47,49,0,50,42,47,43,50,41,56],
[52,44,49,51,0,46,51,43,49,43,59],
[56,52,53,59,55,0,55,39,54,47,54],
[55,50,52,54,50,46,0,47,57,42,59],
[59,55,54,58,58,62,54,0,55,46,62],
[51,50,47,51,52,47,44,46,0,43,50],
[63,49,58,60,58,54,59,55,58,0,62],
[48,42,46,45,42,47,42,39,51,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 93, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,52,56,57,52,53,59,50,51,55],
[55,0,50,54,64,50,47,58,53,63,52],
[49,51,0,51,52,49,42,54,46,59,54],
[45,47,50,0,49,46,35,49,59,56,44],
[44,37,49,52,0,42,43,58,47,55,44],
[49,51,52,55,59,0,45,56,57,54,57],
[48,54,59,66,58,56,0,70,59,67,57],
[42,43,47,52,43,45,31,0,42,59,46],
[51,48,55,42,54,44,42,59,0,52,49],
[50,38,42,45,46,47,34,42,49,0,46],
[46,49,47,57,57,44,44,55,52,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 94, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,58,58,62,47,40,49,51,58,61],
[48,0,51,56,47,39,36,35,40,60,52],
[43,50,0,49,48,43,36,46,31,54,60],
[43,45,52,0,46,34,26,41,41,47,48],
[39,54,53,55,0,39,35,44,37,51,58],
[54,62,58,67,62,0,51,45,46,58,58],
[61,65,65,75,66,50,0,55,55,70,68],
[52,66,55,60,57,56,46,0,46,62,72],
[50,61,70,60,64,55,46,55,0,60,61],
[43,41,47,54,50,43,31,39,41,0,48],
[40,49,41,53,43,43,33,29,40,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 95, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,69,65,61,78,57,40,56,61,70],
[42,0,67,55,44,65,45,34,53,36,55],
[32,34,0,41,37,41,53,27,35,31,46],
[36,46,60,0,54,73,45,40,35,60,64],
[40,57,64,47,0,74,47,34,50,51,55],
[23,36,60,28,27,0,51,36,38,28,46],
[44,56,48,56,54,50,0,45,56,42,44],
[61,67,74,61,67,65,56,0,68,44,63],
[45,48,66,66,51,63,45,33,0,53,60],
[40,65,70,41,50,73,59,57,48,0,74],
[31,46,55,37,46,55,57,38,41,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 96, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,65,55,45,46,36,46,41,56,54,61],
[36,0,36,23,45,33,51,29,47,44,41],
[46,65,0,36,46,31,52,56,68,44,56],
[56,78,65,0,51,32,73,54,74,63,57],
[55,56,55,50,0,33,55,40,60,65,48],
[65,68,70,69,68,0,66,47,74,59,52],
[55,50,49,28,46,35,0,42,61,53,41],
[60,72,45,47,61,54,59,0,67,62,45],
[45,54,33,27,41,27,40,34,0,40,38],
[47,57,57,38,36,42,48,39,61,0,43],
[40,60,45,44,53,49,60,56,63,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 97, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,53,37,60,44,44,76,47,47,58],
[41,0,28,64,59,64,66,72,63,59,29],
[48,73,0,67,79,61,53,75,85,79,53],
[64,37,34,0,43,25,39,63,59,37,44],
[41,42,22,58,0,48,66,64,68,46,54],
[57,37,40,76,53,0,47,67,73,43,53],
[57,35,48,62,35,54,0,76,82,53,35],
[25,29,26,38,37,34,25,0,25,25,35],
[54,38,16,42,33,28,19,76,0,12,35],
[54,42,22,64,55,58,48,76,89,0,33],
[43,72,48,57,47,48,66,66,66,68,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 98, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,48,46,51,43,35,48,45,44,48],
[61,0,58,61,63,54,47,60,58,61,56],
[53,43,0,47,52,47,41,47,47,52,52],
[55,40,54,0,49,53,42,45,50,53,49],
[50,38,49,52,0,50,46,45,44,43,49],
[58,47,54,48,51,0,51,56,59,61,62],
[66,54,60,59,55,50,0,54,59,50,54],
[53,41,54,56,56,45,47,0,55,48,54],
[56,43,54,51,57,42,42,46,0,54,54],
[57,40,49,48,58,40,51,53,47,0,46],
[53,45,49,52,52,39,47,47,47,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 99, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,43,41,42,53,42,53,54,52,39],
[49,0,47,36,44,49,48,49,47,48,50],
[58,54,0,44,51,54,52,59,56,54,54],
[60,65,57,0,58,49,51,57,62,59,53],
[59,57,50,43,0,57,54,55,54,49,50],
[48,52,47,52,44,0,51,49,50,55,47],
[59,53,49,50,47,50,0,47,53,51,44],
[48,52,42,44,46,52,54,0,53,52,45],
[47,54,45,39,47,51,48,48,0,56,41],
[49,53,47,42,52,46,50,49,45,0,43],
[62,51,47,48,51,54,57,56,60,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 100, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,56,56,64,67,61,71,50,51,61],
[44,0,53,49,60,56,59,72,51,55,58],
[45,48,0,51,49,47,54,63,39,50,41],
[45,52,50,0,53,53,61,67,40,52,60],
[37,41,52,48,0,51,54,56,44,43,53],
[34,45,54,48,50,0,52,63,38,47,47],
[40,42,47,40,47,49,0,63,43,55,50],
[30,29,38,34,45,38,38,0,34,38,36],
[51,50,62,61,57,63,58,67,0,60,52],
[50,46,51,49,58,54,46,63,41,0,54],
[40,43,60,41,48,54,51,65,49,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 101, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,44,45,44,53,42,33,48,43,50],
[65,0,53,50,57,60,64,62,55,54,61],
[57,48,0,54,59,65,57,47,73,59,58],
[56,51,47,0,44,59,60,51,50,47,48],
[57,44,42,57,0,60,51,43,50,57,57],
[48,41,36,42,41,0,49,38,55,47,59],
[59,37,44,41,50,52,0,32,47,47,47],
[68,39,54,50,58,63,69,0,57,55,60],
[53,46,28,51,51,46,54,44,0,50,55],
[58,47,42,54,44,54,54,46,51,0,54],
[51,40,43,53,44,42,54,41,46,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 102, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,65,64,58,61,51,50,56,66,55,63],
[36,0,55,37,40,51,47,50,47,53,44],
[37,46,0,43,47,49,52,42,48,51,40],
[43,64,58,0,56,61,51,56,55,45,59],
[40,61,54,45,0,61,47,50,67,53,38],
[50,50,52,40,40,0,55,48,51,43,41],
[51,54,49,50,54,46,0,50,55,50,50],
[45,51,59,45,51,53,51,0,55,64,43],
[35,54,53,46,34,50,46,46,0,48,55],
[46,48,50,56,48,58,51,37,53,0,42],
[38,57,61,42,63,60,51,58,46,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 103, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,48,54,58,56,50,56,47,46,49],
[45,0,46,41,48,40,46,43,49,39,43],
[53,55,0,48,67,52,50,60,53,41,56],
[47,60,53,0,70,56,56,57,49,48,49],
[43,53,34,31,0,43,42,43,40,44,41],
[45,61,49,45,58,0,53,55,45,45,37],
[51,55,51,45,59,48,0,46,43,47,47],
[45,58,41,44,58,46,55,0,48,51,45],
[54,52,48,52,61,56,58,53,0,45,45],
[55,62,60,53,57,56,54,50,56,0,46],
[52,58,45,52,60,64,54,56,56,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 104, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,54,58,55,62,36,49,40,38,59],
[54,0,51,49,50,49,38,36,37,30,51],
[47,50,0,47,45,50,51,44,43,47,48],
[43,52,54,0,53,63,43,47,42,35,45],
[46,51,56,48,0,46,26,43,45,51,53],
[39,52,51,38,55,0,41,33,42,41,32],
[65,63,50,58,75,60,0,60,60,57,59],
[52,65,57,54,58,68,41,0,47,66,32],
[61,64,58,59,56,59,41,54,0,45,42],
[63,71,54,66,50,60,44,35,56,0,42],
[42,50,53,56,48,69,42,69,59,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 105, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,42,50,50,61,55,48,54,46,47],
[55,0,48,51,52,61,47,55,56,56,58],
[59,53,0,57,52,58,53,59,54,50,54],
[51,50,44,0,49,60,51,51,54,49,53],
[51,49,49,52,0,59,49,47,48,49,49],
[40,40,43,41,42,0,44,51,47,44,42],
[46,54,48,50,52,57,0,44,55,44,49],
[53,46,42,50,54,50,57,0,50,52,53],
[47,45,47,47,53,54,46,51,0,52,44],
[55,45,51,52,52,57,57,49,49,0,51],
[54,43,47,48,52,59,52,48,57,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 106, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,50,53,51,45,68,51,49,52,40],
[59,0,60,55,45,48,68,55,49,48,53],
[51,41,0,46,39,44,51,48,53,54,42],
[48,46,55,0,50,40,49,51,43,54,53],
[50,56,62,51,0,54,65,63,52,54,43],
[56,53,57,61,47,0,74,62,56,65,53],
[33,33,50,52,36,27,0,57,41,40,37],
[50,46,53,50,38,39,44,0,45,42,39],
[52,52,48,58,49,45,60,56,0,68,43],
[49,53,47,47,47,36,61,59,33,0,41],
[61,48,59,48,58,48,64,62,58,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 107, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,48,46,82,56,69,34,49,72,41],
[39,0,46,31,49,45,53,40,37,66,41],
[53,55,0,37,60,36,60,43,33,55,44],
[55,70,64,0,64,55,66,43,54,66,57],
[19,52,41,37,0,19,31,31,50,69,38],
[45,56,65,46,82,0,64,61,74,79,45],
[32,48,41,35,70,37,0,22,30,49,38],
[67,61,58,58,70,40,79,0,54,79,59],
[52,64,68,47,51,27,71,47,0,56,60],
[29,35,46,35,32,22,52,22,45,0,44],
[60,60,57,44,63,56,63,42,41,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 108, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,50,45,44,45,53,58,49,51,54],
[58,0,61,44,51,53,60,56,58,52,50],
[51,40,0,47,41,54,62,55,57,43,53],
[56,57,54,0,48,57,54,67,50,51,58],
[57,50,60,53,0,56,62,62,59,51,53],
[56,48,47,44,45,0,49,54,51,45,39],
[48,41,39,47,39,52,0,52,48,42,44],
[43,45,46,34,39,47,49,0,46,41,46],
[52,43,44,51,42,50,53,55,0,46,50],
[50,49,58,50,50,56,59,60,55,0,58],
[47,51,48,43,48,62,57,55,51,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 109, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,56,49,53,57,42,46,51,53,52],
[45,0,48,51,47,45,49,46,47,43,55],
[45,53,0,49,49,43,41,47,47,44,51],
[52,50,52,0,55,46,49,48,55,43,46],
[48,54,52,46,0,47,44,48,48,44,45],
[44,56,58,55,54,0,53,50,54,45,57],
[59,52,60,52,57,48,0,52,49,51,58],
[55,55,54,53,53,51,49,0,51,47,55],
[50,54,54,46,53,47,52,50,0,46,54],
[48,58,57,58,57,56,50,54,55,0,61],
[49,46,50,55,56,44,43,46,47,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 110, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,63,56,58,49,52,56,59,49,62],
[45,0,57,41,53,50,44,54,50,54,54],
[38,44,0,42,46,44,37,51,50,46,56],
[45,60,59,0,51,54,50,56,50,54,58],
[43,48,55,50,0,44,46,47,49,47,66],
[52,51,57,47,57,0,50,53,51,55,59],
[49,57,64,51,55,51,0,54,50,41,50],
[45,47,50,45,54,48,47,0,43,47,56],
[42,51,51,51,52,50,51,58,0,50,55],
[52,47,55,47,54,46,60,54,51,0,50],
[39,47,45,43,35,42,51,45,46,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 111, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,47,43,52,41,38,37,40,54,56],
[54,0,41,43,50,42,39,37,37,47,50],
[54,60,0,56,66,50,41,62,55,59,77],
[58,58,45,0,64,56,39,50,58,50,48],
[49,51,35,37,0,34,49,41,37,34,46],
[60,59,51,45,67,0,45,49,49,38,59],
[63,62,60,62,52,56,0,51,45,55,57],
[64,64,39,51,60,52,50,0,41,62,60],
[61,64,46,43,64,52,56,60,0,48,56],
[47,54,42,51,67,63,46,39,53,0,57],
[45,51,24,53,55,42,44,41,45,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 112, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,35,63,53,47,70,32,48,74,65],
[63,0,37,60,74,59,58,63,63,63,61],
[66,64,0,65,75,47,63,62,62,51,73],
[38,41,36,0,75,34,63,57,47,57,56],
[48,27,26,26,0,42,50,46,46,49,39],
[54,42,54,67,59,0,52,46,46,88,54],
[31,43,38,38,51,49,0,36,49,77,53],
[69,38,39,44,55,55,65,0,58,77,60],
[53,38,39,54,55,55,52,43,0,61,57],
[27,38,50,44,52,13,24,24,40,0,29],
[36,40,28,45,62,47,48,41,44,72,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 113, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,47,63,41,42,38,35,34,66,50],
[57,0,24,27,58,69,69,55,26,63,57],
[54,77,0,73,69,49,59,52,61,73,76],
[38,74,28,0,55,42,42,42,28,49,60],
[60,43,32,46,0,70,39,77,34,40,46],
[59,32,52,59,31,0,18,52,47,53,39],
[63,32,42,59,62,83,0,52,44,39,29],
[66,46,49,59,24,49,49,0,37,50,59],
[67,75,40,73,67,54,57,64,0,58,75],
[35,38,28,52,61,48,62,51,43,0,35],
[51,44,25,41,55,62,72,42,26,66,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 114, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,40,41,40,52,50,32,46,49,57],
[50,0,47,56,42,44,43,42,36,47,51],
[61,54,0,51,62,63,61,45,49,50,55],
[60,45,50,0,39,59,53,50,40,53,58],
[61,59,39,62,0,53,60,60,53,66,63],
[49,57,38,42,48,0,50,48,34,47,50],
[51,58,40,48,41,51,0,50,34,42,45],
[69,59,56,51,41,53,51,0,45,49,58],
[55,65,52,61,48,67,67,56,0,53,70],
[52,54,51,48,35,54,59,52,48,0,47],
[44,50,46,43,38,51,56,43,31,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 115, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,57,54,61,49,50,46,49,56,64],
[59,0,57,49,62,55,66,46,55,53,62],
[44,44,0,43,62,45,46,39,40,42,54],
[47,52,58,0,67,53,48,52,52,56,61],
[40,39,39,34,0,47,41,46,30,47,45],
[52,46,56,48,54,0,55,52,48,54,58],
[51,35,55,53,60,46,0,40,42,52,57],
[55,55,62,49,55,49,61,0,47,56,57],
[52,46,61,49,71,53,59,54,0,52,60],
[45,48,59,45,54,47,49,45,49,0,61],
[37,39,47,40,56,43,44,44,41,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 116, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,80,78,81,57,71,41,73,78,78],
[59,0,82,59,81,45,59,61,73,66,59],
[21,19,0,60,63,39,59,23,50,78,40],
[23,42,41,0,63,30,59,23,73,78,7],
[20,20,38,38,0,45,59,20,50,59,38],
[44,56,62,71,56,0,59,23,94,71,51],
[30,42,42,42,42,42,0,30,42,63,42],
[60,40,78,78,81,78,71,0,71,78,78],
[28,28,51,28,51,7,59,30,0,48,28],
[23,35,23,23,42,30,38,23,53,0,23],
[23,42,61,94,63,50,59,23,73,78,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 117, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,52,45,48,61,46,42,48,58,49],
[53,0,57,44,54,60,54,50,51,60,48],
[49,44,0,36,45,49,41,40,39,61,42],
[56,57,65,0,57,65,50,53,55,63,53],
[53,47,56,44,0,60,50,51,49,50,46],
[40,41,52,36,41,0,49,41,47,52,41],
[55,47,60,51,51,52,0,38,41,60,46],
[59,51,61,48,50,60,63,0,55,60,56],
[53,50,62,46,52,54,60,46,0,62,54],
[43,41,40,38,51,49,41,41,39,0,49],
[52,53,59,48,55,60,55,45,47,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 118, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,53,47,43,40,43,52,48,44,47],
[55,0,44,49,45,47,39,44,51,42,39],
[48,57,0,49,49,51,54,52,50,51,51],
[54,52,52,0,49,48,49,56,49,44,45],
[58,56,52,52,0,45,48,56,52,49,47],
[61,54,50,53,56,0,53,53,55,52,49],
[58,62,47,52,53,48,0,55,57,49,52],
[49,57,49,45,45,48,46,0,51,50,42],
[53,50,51,52,49,46,44,50,0,48,47],
[57,59,50,57,52,49,52,51,53,0,45],
[54,62,50,56,54,52,49,59,54,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 119, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,56,58,57,46,60,59,49,43,51],
[46,0,70,45,58,43,49,57,44,45,55],
[45,31,0,37,42,41,52,44,38,42,37],
[43,56,64,0,62,50,58,59,47,45,53],
[44,43,59,39,0,42,56,50,47,45,51],
[55,58,60,51,59,0,63,51,47,59,42],
[41,52,49,43,45,38,0,48,37,40,47],
[42,44,57,42,51,50,53,0,57,44,42],
[52,57,63,54,54,54,64,44,0,54,48],
[58,56,59,56,56,42,61,57,47,0,45],
[50,46,64,48,50,59,54,59,53,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 120, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,59,55,58,59,64,51,53,54,54],
[53,0,53,53,52,56,61,44,46,43,53],
[42,48,0,47,57,48,60,37,41,45,41],
[46,48,54,0,57,51,55,49,46,50,52],
[43,49,44,44,0,50,51,38,41,48,39],
[42,45,53,50,51,0,53,38,50,50,48],
[37,40,41,46,50,48,0,34,37,42,44],
[50,57,64,52,63,63,67,0,58,53,47],
[48,55,60,55,60,51,64,43,0,50,52],
[47,58,56,51,53,51,59,48,51,0,54],
[47,48,60,49,62,53,57,54,49,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 121, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,46,56,42,43,43,46,54,48,52],
[50,0,63,54,53,48,45,48,55,43,46],
[55,38,0,51,53,44,48,47,51,44,53],
[45,47,50,0,41,37,43,50,44,42,41],
[59,48,48,60,0,45,46,48,56,42,51],
[58,53,57,64,56,0,46,51,61,45,58],
[58,56,53,58,55,55,0,50,57,54,55],
[55,53,54,51,53,50,51,0,59,52,58],
[47,46,50,57,45,40,44,42,0,41,42],
[53,58,57,59,59,56,47,49,60,0,63],
[49,55,48,60,50,43,46,43,59,38,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 122, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,70,47,55,69,63,54,53,44,63],
[48,0,56,66,73,78,68,63,49,71,58],
[31,45,0,41,46,66,41,51,47,40,45],
[54,35,60,0,55,69,58,62,58,60,54],
[46,28,55,46,0,62,52,51,37,53,46],
[32,23,35,32,39,0,42,32,17,21,36],
[38,33,60,43,49,59,0,48,32,56,56],
[47,38,50,39,50,69,53,0,31,43,64],
[48,52,54,43,64,84,69,70,0,58,57],
[57,30,61,41,48,80,45,58,43,0,57],
[38,43,56,47,55,65,45,37,44,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 123, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,78,52,82,56,71,38,71,63,54,73],
[23,0,36,37,54,42,41,52,61,38,56],
[49,65,0,68,51,57,47,58,68,42,59],
[19,64,33,0,50,65,46,59,63,44,64],
[45,47,50,51,0,56,66,67,45,44,62],
[30,59,44,36,45,0,33,61,45,43,54],
[63,60,54,55,35,68,0,57,58,59,60],
[30,49,43,42,34,40,44,0,50,37,59],
[38,40,33,38,56,56,43,51,0,30,67],
[47,63,59,57,57,58,42,64,71,0,76],
[28,45,42,37,39,47,41,42,34,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 124, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,55,52,58,53,55,56,44,48,54],
[42,0,48,41,49,59,49,49,41,34,48],
[46,53,0,45,50,54,44,54,45,35,43],
[49,60,56,0,65,61,58,59,48,48,49],
[43,52,51,36,0,50,45,51,47,44,54],
[48,42,47,40,51,0,42,47,41,41,53],
[46,52,57,43,56,59,0,59,51,44,47],
[45,52,47,42,50,54,42,0,43,36,52],
[57,60,56,53,54,60,50,58,0,54,55],
[53,67,66,53,57,60,57,65,47,0,56],
[47,53,58,52,47,48,54,49,46,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 125, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,73,59,64,62,50,56,58,51,71,72],
[28,0,39,44,38,23,31,40,20,54,35],
[42,62,0,43,56,45,41,30,24,38,54],
[37,57,58,0,76,49,54,57,59,65,74],
[39,63,45,25,0,57,53,26,25,41,48],
[51,78,56,52,44,0,61,56,54,63,58],
[45,70,60,47,48,40,0,54,40,44,56],
[43,61,71,44,75,45,47,0,47,63,60],
[50,81,77,42,76,47,61,54,0,59,59],
[30,47,63,36,60,38,57,38,42,0,49],
[29,66,47,27,53,43,45,41,42,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 126, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,32,76,35,41,50,53,50,17,26],
[46,0,32,67,22,36,41,43,54,4,27],
[69,69,0,71,63,45,71,52,55,36,57],
[25,34,30,0,8,45,13,29,40,8,30],
[66,79,38,93,0,49,53,53,50,18,38],
[60,65,56,56,52,0,48,48,45,48,48],
[51,60,30,88,48,53,0,33,50,48,65],
[48,58,49,72,48,53,68,0,68,48,44],
[51,47,46,61,51,56,51,33,0,51,41],
[84,97,65,93,83,53,53,53,50,0,52],
[75,74,44,71,63,53,36,57,60,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 127, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,44,44,49,43,53,55,48,42,50],
[56,0,54,54,55,50,57,57,51,51,54],
[57,47,0,49,46,46,48,55,58,45,53],
[57,47,52,0,57,52,60,66,57,52,59],
[52,46,55,44,0,47,57,60,51,50,46],
[58,51,55,49,54,0,54,61,52,53,49],
[48,44,53,41,44,47,0,49,47,44,44],
[46,44,46,35,41,40,52,0,43,46,43],
[53,50,43,44,50,49,54,58,0,49,45],
[59,50,56,49,51,48,57,55,52,0,50],
[51,47,48,42,55,52,57,58,56,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 128, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,57,61,51,68,56,57,52,47,42],
[47,0,53,46,63,54,50,50,56,37,54],
[44,48,0,47,45,56,59,48,51,45,44],
[40,55,54,0,64,74,52,59,51,52,37],
[50,38,56,37,0,61,38,51,53,44,36],
[33,47,45,27,40,0,37,42,25,36,31],
[45,51,42,49,63,64,0,48,46,45,34],
[44,51,53,42,50,59,53,0,45,49,31],
[49,45,50,50,48,76,55,56,0,41,37],
[54,64,56,49,57,65,56,52,60,0,46],
[59,47,57,64,65,70,67,70,64,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 129, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,56,69,39,54,57,55,50,54,66],
[50,0,63,68,48,57,65,53,50,51,60],
[45,38,0,55,55,52,54,50,39,66,62],
[32,33,46,0,29,40,50,42,42,40,51],
[62,53,46,72,0,55,63,62,54,64,74],
[47,44,49,61,46,0,47,46,43,60,47],
[44,36,47,51,38,54,0,45,37,59,48],
[46,48,51,59,39,55,56,0,40,53,54],
[51,51,62,59,47,58,64,61,0,64,56],
[47,50,35,61,37,41,42,48,37,0,53],
[35,41,39,50,27,54,53,47,45,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 130, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,70,62,37,36,58,37,24,52,24,33],
[31,0,40,43,23,38,44,46,49,15,22],
[39,61,0,60,33,35,51,41,51,30,35],
[64,58,41,0,40,46,45,33,32,38,33],
[65,78,68,61,0,45,48,53,55,31,39],
[43,63,66,55,56,0,39,44,41,37,52],
[64,57,50,56,53,62,0,52,58,33,35],
[77,55,60,68,48,57,49,0,60,52,41],
[49,52,50,69,46,60,43,41,0,30,31],
[77,86,71,63,70,64,68,49,71,0,69],
[68,79,66,68,62,49,66,60,70,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 131, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,54,57,59,58,51,59,49,53,57],
[49,0,49,56,48,53,48,59,50,50,58],
[47,52,0,51,45,55,45,57,46,46,50],
[44,45,50,0,51,54,38,51,44,46,50],
[42,53,56,50,0,49,50,57,44,47,54],
[43,48,46,47,52,0,46,53,43,48,47],
[50,53,56,63,51,55,0,58,47,49,56],
[42,42,44,50,44,48,43,0,40,42,40],
[52,51,55,57,57,58,54,61,0,49,50],
[48,51,55,55,54,53,52,59,52,0,55],
[44,43,51,51,47,54,45,61,51,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 132, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,38,45,42,53,54,50,48,50,49],
[43,0,41,46,48,52,51,47,36,43,46],
[63,60,0,52,46,54,61,52,63,62,51],
[56,55,49,0,47,48,46,51,49,59,51],
[59,53,55,54,0,57,52,50,56,46,58],
[48,49,47,53,44,0,48,47,53,52,56],
[47,50,40,55,49,53,0,52,41,55,47],
[51,54,49,50,51,54,49,0,52,51,54],
[53,65,38,52,45,48,60,49,0,57,54],
[51,58,39,42,55,49,46,50,44,0,43],
[52,55,50,50,43,45,54,47,47,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 133, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,35,57,23,25,32,56,25,26,59],
[56,0,30,47,24,24,25,26,29,30,49],
[66,71,0,82,45,54,44,61,62,45,47],
[44,54,19,0,43,40,40,46,5,30,35],
[78,77,56,58,0,44,32,56,39,61,66],
[76,77,47,61,57,0,62,44,31,50,54],
[69,76,57,61,69,39,0,55,32,53,66],
[45,75,40,55,45,57,46,0,23,28,43],
[76,72,39,96,62,70,69,78,0,56,66],
[75,71,56,71,40,51,48,73,45,0,84],
[42,52,54,66,35,47,35,58,35,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 134, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,57,59,51,58,56,57,50,60,51],
[41,0,50,47,49,52,56,56,42,46,45],
[44,51,0,54,44,48,54,66,55,51,62],
[42,54,47,0,52,55,51,59,42,57,53],
[50,52,57,49,0,56,57,62,48,48,53],
[43,49,53,46,45,0,64,62,52,53,50],
[45,45,47,50,44,37,0,63,42,53,41],
[44,45,35,42,39,39,38,0,36,45,43],
[51,59,46,59,53,49,59,65,0,57,46],
[41,55,50,44,53,48,48,56,44,0,45],
[50,56,39,48,48,51,60,58,55,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 135, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,51,50,44,47,52,47,44,55,54],
[53,0,53,53,55,49,57,44,51,49,52],
[50,48,0,50,47,50,44,47,45,51,49],
[51,48,51,0,46,48,49,47,49,48,50],
[57,46,54,55,0,51,49,47,52,55,54],
[54,52,51,53,50,0,56,57,56,58,51],
[49,44,57,52,52,45,0,51,50,51,54],
[54,57,54,54,54,44,50,0,50,51,51],
[57,50,56,52,49,45,51,51,0,56,55],
[46,52,50,53,46,43,50,50,45,0,58],
[47,49,52,51,47,50,47,50,46,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 136, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,59,46,63,60,48,57,72,55,56],
[42,0,53,52,44,46,48,52,63,51,48],
[42,48,0,51,44,40,36,43,56,44,41],
[55,49,50,0,59,54,60,55,68,63,56],
[38,57,57,42,0,47,50,50,59,46,48],
[41,55,61,47,54,0,44,56,58,49,49],
[53,53,65,41,51,57,0,54,59,63,55],
[44,49,58,46,51,45,47,0,60,51,45],
[29,38,45,33,42,43,42,41,0,44,37],
[46,50,57,38,55,52,38,50,57,0,47],
[45,53,60,45,53,52,46,56,64,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 137, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,39,42,50,40,43,42,45,40,50],
[59,0,51,52,51,52,50,48,59,47,56],
[62,50,0,53,54,47,52,60,51,53,55],
[59,49,48,0,46,58,47,56,52,45,56],
[51,50,47,55,0,47,49,49,54,46,53],
[61,49,54,43,54,0,53,56,61,53,56],
[58,51,49,54,52,48,0,55,62,50,65],
[59,53,41,45,52,45,46,0,55,48,53],
[56,42,50,49,47,40,39,46,0,43,56],
[61,54,48,56,55,48,51,53,58,0,57],
[51,45,46,45,48,45,36,48,45,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 138, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,59,64,54,52,59,62,47,56,70],
[45,0,69,56,47,59,63,58,61,62,68],
[42,32,0,41,35,46,38,32,27,41,53],
[37,45,60,0,37,49,41,48,49,56,59],
[47,54,66,64,0,47,57,52,47,58,66],
[49,42,55,52,54,0,39,42,45,60,54],
[42,38,63,60,44,62,0,42,53,52,39],
[39,43,69,53,49,59,59,0,58,61,70],
[54,40,74,52,54,56,48,43,0,58,58],
[45,39,60,45,43,41,49,40,43,0,71],
[31,33,48,42,35,47,62,31,43,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 139, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,46,49,48,42,49,53,60,57,51],
[59,0,59,59,54,56,50,60,59,62,60],
[55,42,0,49,45,43,41,43,53,45,41],
[52,42,52,0,40,54,51,45,49,61,46],
[53,47,56,61,0,45,46,51,47,56,53],
[59,45,58,47,56,0,44,56,55,56,52],
[52,51,60,50,55,57,0,56,60,58,49],
[48,41,58,56,50,45,45,0,51,53,55],
[41,42,48,52,54,46,41,50,0,55,52],
[44,39,56,40,45,45,43,48,46,0,39],
[50,41,60,55,48,49,52,46,49,62,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 140, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,52,57,55,59,49,64,37,49,54],
[54,0,45,50,50,66,42,51,41,43,53],
[49,56,0,51,56,62,41,45,39,48,64],
[44,51,50,0,58,55,43,44,39,46,54],
[46,51,45,43,0,60,40,50,52,46,53],
[42,35,39,46,41,0,38,48,40,39,49],
[52,59,60,58,61,63,0,64,46,57,64],
[37,50,56,57,51,53,37,0,37,45,43],
[64,60,62,62,49,61,55,64,0,58,59],
[52,58,53,55,55,62,44,56,43,0,53],
[47,48,37,47,48,52,37,58,42,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 141, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,56,55,55,61,62,54,53,66,48],
[55,0,44,54,46,58,62,54,50,54,45],
[45,57,0,57,45,68,61,54,44,53,49],
[46,47,44,0,48,53,55,54,47,53,44],
[46,55,56,53,0,58,58,55,49,53,59],
[40,43,33,48,43,0,53,48,41,50,35],
[39,39,40,46,43,48,0,43,43,50,47],
[47,47,47,47,46,53,58,0,44,41,51],
[48,51,57,54,52,60,58,57,0,54,49],
[35,47,48,48,48,51,51,60,47,0,47],
[53,56,52,57,42,66,54,50,52,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 142, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,56,50,43,49,56,54,54,43,59],
[56,0,56,55,50,50,49,50,60,48,64],
[45,45,0,47,43,46,55,49,51,43,57],
[51,46,54,0,53,48,50,60,49,42,55],
[58,51,58,48,0,51,48,56,58,53,60],
[52,51,55,53,50,0,54,55,60,51,55],
[45,52,46,51,53,47,0,59,50,42,60],
[47,51,52,41,45,46,42,0,59,45,54],
[47,41,50,52,43,41,51,42,0,41,53],
[58,53,58,59,48,50,59,56,60,0,58],
[42,37,44,46,41,46,41,47,48,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 143, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,46,51,47,44,46,37,49,41,52],
[47,0,49,51,41,55,55,41,54,46,47],
[55,52,0,64,46,49,51,48,56,49,51],
[50,50,37,0,42,53,50,35,45,44,51],
[54,60,55,59,0,57,64,61,58,50,47],
[57,46,52,48,44,0,43,41,51,50,53],
[55,46,50,51,37,58,0,37,54,42,48],
[64,60,53,66,40,60,64,0,60,54,58],
[52,47,45,56,43,50,47,41,0,56,49],
[60,55,52,57,51,51,59,47,45,0,59],
[49,54,50,50,54,48,53,43,52,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 144, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,58,49,52,51,62,59,66,54,61],
[43,0,46,50,51,43,47,58,62,51,59],
[43,55,0,43,43,50,49,67,48,53,56],
[52,51,58,0,42,48,53,60,68,58,60],
[49,50,58,59,0,50,56,66,61,58,58],
[50,58,51,53,51,0,59,65,62,62,61],
[39,54,52,48,45,42,0,59,55,57,53],
[42,43,34,41,35,36,42,0,50,50,44],
[35,39,53,33,40,39,46,51,0,49,53],
[47,50,48,43,43,39,44,51,52,0,52],
[40,42,45,41,43,40,48,57,48,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 145, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,52,54,45,60,60,57,54,48,64],
[42,0,48,51,45,50,50,47,47,46,60],
[49,53,0,51,46,52,51,49,45,47,63],
[47,50,50,0,45,50,53,48,47,47,62],
[56,56,55,56,0,55,61,52,50,58,62],
[41,51,49,51,46,0,53,43,45,49,56],
[41,51,50,48,40,48,0,47,43,44,52],
[44,54,52,53,49,58,54,0,47,46,58],
[47,54,56,54,51,56,58,54,0,51,56],
[53,55,54,54,43,52,57,55,50,0,64],
[37,41,38,39,39,45,49,43,45,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 146, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,68,54,56,47,67,56,58,62,62],
[46,0,61,54,59,57,72,46,47,49,55],
[33,40,0,39,56,44,50,38,52,53,50],
[47,47,62,0,55,62,61,53,54,57,69],
[45,42,45,46,0,52,60,46,44,49,66],
[54,44,57,39,49,0,58,46,38,50,53],
[34,29,51,40,41,43,0,25,43,51,43],
[45,55,63,48,55,55,76,0,55,52,62],
[43,54,49,47,57,63,58,46,0,56,66],
[39,52,48,44,52,51,50,49,45,0,44],
[39,46,51,32,35,48,58,39,35,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 147, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,53,49,28,55,44,48,28,45,63],
[62,0,59,35,40,71,38,48,48,56,56],
[48,42,0,44,41,61,43,48,35,41,51],
[52,66,57,0,45,61,35,49,51,44,59],
[73,61,60,56,0,77,46,58,40,52,66],
[46,30,40,40,24,0,34,45,27,36,39],
[57,63,58,66,55,67,0,44,48,50,63],
[53,53,53,52,43,56,57,0,34,51,64],
[73,53,66,50,61,74,53,67,0,68,71],
[56,45,60,57,49,65,51,50,33,0,70],
[38,45,50,42,35,62,38,37,30,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 148, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,58,46,47,53,55,51,51,52,48],
[45,0,49,43,43,48,47,40,49,45,44],
[43,52,0,44,43,42,47,39,54,39,42],
[55,58,57,0,53,57,56,50,52,56,51],
[54,58,58,48,0,53,57,59,50,45,59],
[48,53,59,44,48,0,58,47,45,42,49],
[46,54,54,45,44,43,0,48,47,43,44],
[50,61,62,51,42,54,53,0,49,50,50],
[50,52,47,49,51,56,54,52,0,50,49],
[49,56,62,45,56,59,58,51,51,0,46],
[53,57,59,50,42,52,57,51,52,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 149, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,55,57,55,49,45,57,50,60,63],
[48,0,52,57,52,58,39,50,43,53,51],
[46,49,0,55,41,44,35,40,40,53,48],
[44,44,46,0,52,37,38,46,43,51,52],
[46,49,60,49,0,40,41,49,48,51,49],
[52,43,57,64,61,0,47,61,60,56,57],
[56,62,66,63,60,54,0,50,64,51,65],
[44,51,61,55,52,40,51,0,51,46,58],
[51,58,61,58,53,41,37,50,0,58,48],
[41,48,48,50,50,45,50,55,43,0,56],
[38,50,53,49,52,44,36,43,53,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 150, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,50,45,51,36,38,44,51,46,35],
[44,0,48,30,43,32,38,42,23,36,37],
[51,53,0,37,38,40,41,38,32,39,34],
[56,71,64,0,51,54,53,59,38,44,45],
[50,58,63,50,0,39,45,42,34,42,45],
[65,69,61,47,62,0,44,56,47,45,44],
[63,63,60,48,56,57,0,51,38,54,39],
[57,59,63,42,59,45,50,0,54,44,38],
[50,78,69,63,67,54,63,47,0,47,48],
[55,65,62,57,59,56,47,57,54,0,53],
[66,64,67,56,56,57,62,63,53,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 151, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,56,46,51,35,30,35,49,41,37],
[72,0,61,65,63,50,54,51,63,55,60],
[45,40,0,43,36,42,26,43,45,46,32],
[55,36,58,0,43,43,34,38,50,35,33],
[50,38,65,58,0,38,48,44,48,37,34],
[66,51,59,58,63,0,49,60,58,55,55],
[71,47,75,67,53,52,0,53,66,55,47],
[66,50,58,63,57,41,48,0,48,52,36],
[52,38,56,51,53,43,35,53,0,38,42],
[60,46,55,66,64,46,46,49,63,0,50],
[64,41,69,68,67,46,54,65,59,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 152, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,33,42,58,78,73,37,33,67,22],
[49,0,43,34,55,55,71,46,44,59,49],
[68,58,0,34,55,51,71,34,53,59,49],
[59,67,67,0,46,55,46,21,58,59,59],
[43,46,46,55,0,82,73,63,59,80,26],
[23,46,50,46,19,0,46,29,29,31,23],
[28,30,30,55,28,55,0,34,55,61,32],
[64,55,67,80,38,72,67,0,59,80,51],
[68,57,48,43,42,72,46,42,0,68,49],
[34,42,42,42,21,70,40,21,33,0,34],
[79,52,52,42,75,78,69,50,52,67,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 153, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,49,52,54,52,59,47,55,37,43],
[47,0,52,47,51,54,52,40,52,45,51],
[52,49,0,52,56,58,57,67,60,43,50],
[49,54,49,0,50,42,54,42,51,51,39],
[47,50,45,51,0,50,40,40,54,32,49],
[49,47,43,59,51,0,53,55,41,32,29],
[42,49,44,47,61,48,0,45,63,53,46],
[54,61,34,59,61,46,56,0,55,54,42],
[46,49,41,50,47,60,38,46,0,39,51],
[64,56,58,50,69,69,48,47,62,0,65],
[58,50,51,62,52,72,55,59,50,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 154, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,44,50,49,51,41,47,41,55,48],
[50,0,49,53,42,53,44,52,47,52,37],
[57,52,0,57,53,57,40,45,48,57,45],
[51,48,44,0,52,61,52,51,54,65,50],
[52,59,48,49,0,55,42,48,49,55,43],
[50,48,44,40,46,0,49,49,45,47,38],
[60,57,61,49,59,52,0,52,52,58,51],
[54,49,56,50,53,52,49,0,46,43,50],
[60,54,53,47,52,56,49,55,0,57,44],
[46,49,44,36,46,54,43,58,44,0,38],
[53,64,56,51,58,63,50,51,57,63,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 155, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,57,49,59,57,49,49,48,56,55],
[47,0,48,45,51,48,46,48,49,47,52],
[44,53,0,44,56,53,51,51,51,48,59],
[52,56,57,0,57,54,54,52,44,50,53],
[42,50,45,44,0,46,47,37,43,42,51],
[44,53,48,47,55,0,49,45,52,43,56],
[52,55,50,47,54,52,0,49,48,52,51],
[52,53,50,49,64,56,52,0,50,50,55],
[53,52,50,57,58,49,53,51,0,49,55],
[45,54,53,51,59,58,49,51,52,0,56],
[46,49,42,48,50,45,50,46,46,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 156, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,47,54,51,51,51,52,50,50,49],
[48,0,38,50,47,39,44,53,48,42,58],
[54,63,0,60,52,49,53,54,65,51,56],
[47,51,41,0,45,45,44,47,46,44,53],
[50,54,49,56,0,40,58,50,52,50,52],
[50,62,52,56,61,0,57,58,63,54,59],
[50,57,48,57,43,44,0,57,53,50,59],
[49,48,47,54,51,43,44,0,50,53,55],
[51,53,36,55,49,38,48,51,0,49,61],
[51,59,50,57,51,47,51,48,52,0,48],
[52,43,45,48,49,42,42,46,40,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 157, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,46,58,40,56,56,55,49,52,50],
[47,0,39,60,44,59,46,36,42,54,39],
[55,62,0,60,46,65,55,51,59,56,56],
[43,41,41,0,36,44,42,36,51,41,41],
[61,57,55,65,0,68,58,54,53,70,50],
[45,42,36,57,33,0,49,53,46,46,36],
[45,55,46,59,43,52,0,52,58,58,49],
[46,65,50,65,47,48,49,0,53,63,46],
[52,59,42,50,48,55,43,48,0,52,43],
[49,47,45,60,31,55,43,38,49,0,50],
[51,62,45,60,51,65,52,55,58,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 158, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,42,37,48,24,44,51,37,36,25],
[57,0,50,36,51,48,59,58,51,76,33],
[59,51,0,24,68,32,67,32,60,80,23],
[64,65,77,0,59,41,76,60,60,74,28],
[53,50,33,42,0,44,38,35,37,61,30],
[77,53,69,60,57,0,63,59,36,80,57],
[57,42,34,25,63,38,0,34,45,78,21],
[50,43,69,41,66,42,67,0,56,71,43],
[64,50,41,41,64,65,56,45,0,89,55],
[65,25,21,27,40,21,23,30,12,0,13],
[76,68,78,73,71,44,80,58,46,88,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 159, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,48,63,55,45,52,51,46,54,64],
[40,0,45,50,50,44,47,42,55,36,51],
[53,56,0,55,55,54,51,52,52,50,56],
[38,51,46,0,48,43,46,41,51,48,55],
[46,51,46,53,0,44,46,52,53,48,53],
[56,57,47,58,57,0,52,59,61,57,58],
[49,54,50,55,55,49,0,44,51,46,57],
[50,59,49,60,49,42,57,0,53,50,59],
[55,46,49,50,48,40,50,48,0,50,52],
[47,65,51,53,53,44,55,51,51,0,55],
[37,50,45,46,48,43,44,42,49,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 160, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,54,55,51,53,56,60,47,52,55],
[53,0,58,52,49,55,54,58,52,49,48],
[47,43,0,45,46,49,46,50,38,45,46],
[46,49,56,0,48,52,50,52,45,50,48],
[50,52,55,53,0,52,51,52,46,52,50],
[48,46,52,49,49,0,45,51,42,48,44],
[45,47,55,51,50,56,0,53,47,53,44],
[41,43,51,49,49,50,48,0,43,49,52],
[54,49,63,56,55,59,54,58,0,54,53],
[49,52,56,51,49,53,48,52,47,0,48],
[46,53,55,53,51,57,57,49,48,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 161, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,37,34,55,23,44,18,44,45,45],
[39,0,8,34,53,21,30,4,11,51,27],
[64,93,0,63,76,58,62,46,51,65,79],
[67,67,38,0,76,52,50,40,55,64,48],
[46,48,25,25,0,15,37,28,25,33,35],
[78,80,43,49,86,0,76,49,67,68,59],
[57,71,39,51,64,25,0,22,56,65,48],
[83,97,55,61,73,52,79,0,44,61,56],
[57,90,50,46,76,34,45,57,0,63,81],
[56,50,36,37,68,33,36,40,38,0,56],
[56,74,22,53,66,42,53,45,20,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 162, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,75,43,79,57,67,32,75,76,48,50],
[26,0,26,70,3,74,19,66,45,55,42],
[58,75,0,59,45,75,40,69,69,59,61],
[22,31,42,0,16,46,14,63,32,70,26],
[44,98,56,85,0,101,56,84,59,85,56],
[34,27,26,55,0,0,14,36,45,52,15],
[69,82,61,87,45,87,0,83,62,72,77],
[26,35,32,38,17,65,18,0,59,61,19],
[25,56,32,69,42,56,39,42,0,53,28],
[53,46,42,31,16,49,29,40,48,0,30],
[51,59,40,75,45,86,24,82,73,71,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 163, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,49,53,62,52,50,59,48,48,52],
[51,0,50,47,54,52,58,52,47,52,57],
[52,51,0,51,56,53,53,56,52,50,53],
[48,54,50,0,52,53,55,50,52,51,55],
[39,47,45,49,0,47,52,50,43,44,50],
[49,49,48,48,54,0,53,53,45,48,50],
[51,43,48,46,49,48,0,52,45,41,51],
[42,49,45,51,51,48,49,0,50,47,48],
[53,54,49,49,58,56,56,51,0,52,57],
[53,49,51,50,57,53,60,54,49,0,55],
[49,44,48,46,51,51,50,53,44,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 164, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,63,65,50,66,66,62,48,58,77],
[50,0,49,71,46,74,42,58,50,66,63],
[38,52,0,69,46,52,49,47,54,50,52],
[36,30,32,0,39,33,52,36,33,46,56],
[51,55,55,62,0,53,44,45,54,62,60],
[35,27,49,68,48,0,38,44,46,49,50],
[35,59,52,49,57,63,0,48,36,66,64],
[39,43,54,65,56,57,53,0,24,56,59],
[53,51,47,68,47,55,65,77,0,68,72],
[43,35,51,55,39,52,35,45,33,0,52],
[24,38,49,45,41,51,37,42,29,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 165, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,45,44,57,45,56,47,55,50,53],
[55,0,54,49,55,49,57,54,56,56,54],
[56,47,0,54,60,54,54,53,57,54,58],
[57,52,47,0,60,50,61,53,58,54,54],
[44,46,41,41,0,51,48,50,54,52,46],
[56,52,47,51,50,0,56,51,52,58,56],
[45,44,47,40,53,45,0,54,54,53,55],
[54,47,48,48,51,50,47,0,60,53,48],
[46,45,44,43,47,49,47,41,0,52,52],
[51,45,47,47,49,43,48,48,49,0,48],
[48,47,43,47,55,45,46,53,49,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 166, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,57,47,45,63,39,48,49,43,50],
[56,0,51,46,52,46,32,49,53,48,52],
[44,50,0,35,52,54,44,44,58,40,41],
[54,55,66,0,53,49,51,54,52,53,62],
[56,49,49,48,0,44,31,50,57,43,41],
[38,55,47,52,57,0,37,42,50,42,59],
[62,69,57,50,70,64,0,52,72,58,68],
[53,52,57,47,51,59,49,0,63,50,48],
[52,48,43,49,44,51,29,38,0,37,42],
[58,53,61,48,58,59,43,51,64,0,51],
[51,49,60,39,60,42,33,53,59,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 167, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,58,56,50,52,56,60,47,47,51],
[53,0,65,55,52,54,62,60,45,53,54],
[43,36,0,49,49,49,52,53,43,43,46],
[45,46,52,0,53,49,52,53,42,42,50],
[51,49,52,48,0,45,49,57,42,42,50],
[49,47,52,52,56,0,62,57,46,46,47],
[45,39,49,49,52,39,0,50,37,38,44],
[41,41,48,48,44,44,51,0,45,44,39],
[54,56,58,59,59,55,64,56,0,49,54],
[54,48,58,59,59,55,63,57,52,0,53],
[50,47,55,51,51,54,57,62,47,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 168, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,38,33,41,47,47,41,30,54,46],
[51,0,51,56,48,56,73,54,40,63,55],
[63,50,0,70,59,59,71,50,45,57,44],
[68,45,31,0,53,46,63,43,51,45,49],
[60,53,42,48,0,48,63,36,44,53,50],
[54,45,42,55,53,0,73,34,49,44,49],
[54,28,30,38,38,28,0,39,39,37,40],
[60,47,51,58,65,67,62,0,62,56,51],
[71,61,56,50,57,52,62,39,0,56,53],
[47,38,44,56,48,57,64,45,45,0,52],
[55,46,57,52,51,52,61,50,48,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 169, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,37,56,57,43,47,60,49,53,59],
[47,0,31,40,38,34,32,37,36,40,45],
[64,70,0,59,56,50,53,56,57,60,58],
[45,61,42,0,51,38,37,38,37,47,48],
[44,63,45,50,0,48,46,54,43,48,48],
[58,67,51,63,53,0,52,58,52,60,50],
[54,69,48,64,55,49,0,52,62,50,49],
[41,64,45,63,47,43,49,0,51,51,47],
[52,65,44,64,58,49,39,50,0,44,48],
[48,61,41,54,53,41,51,50,57,0,47],
[42,56,43,53,53,51,52,54,53,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 170, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,43,56,53,44,45,49,46,41,48],
[52,0,51,54,56,53,52,45,52,38,39],
[58,50,0,57,55,50,53,51,44,53,53],
[45,47,44,0,37,52,43,39,33,39,29],
[48,45,46,64,0,43,49,48,40,48,42],
[57,48,51,49,58,0,43,50,48,49,45],
[56,49,48,58,52,58,0,43,47,49,41],
[52,56,50,62,53,51,58,0,53,48,44],
[55,49,57,68,61,53,54,48,0,55,39],
[60,63,48,62,53,52,52,53,46,0,49],
[53,62,48,72,59,56,60,57,62,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 171, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,55,60,58,44,49,55,59,54,49],
[58,0,59,59,66,52,49,58,65,57,56],
[46,42,0,48,57,41,44,52,50,37,49],
[41,42,53,0,53,42,42,51,56,53,50],
[43,35,44,48,0,40,35,44,47,44,44],
[57,49,60,59,61,0,54,61,61,56,61],
[52,52,57,59,66,47,0,57,56,56,60],
[46,43,49,50,57,40,44,0,48,44,45],
[42,36,51,45,54,40,45,53,0,49,47],
[47,44,64,48,57,45,45,57,52,0,48],
[52,45,52,51,57,40,41,56,54,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 172, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,67,61,54,54,53,48,52,47,52,47],
[34,0,51,48,45,41,42,40,47,51,50],
[40,50,0,45,40,41,43,43,42,49,51],
[47,53,56,0,47,45,46,41,50,44,45],
[47,56,61,54,0,44,49,47,51,45,52],
[48,60,60,56,57,0,52,59,49,49,52],
[53,59,58,55,52,49,0,40,59,55,48],
[49,61,58,60,54,42,61,0,51,51,52],
[54,54,59,51,50,52,42,50,0,38,56],
[49,50,52,57,56,52,46,50,63,0,53],
[54,51,50,56,49,49,53,49,45,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 173, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,57,52,45,48,46,45,47,54,45],
[59,0,54,56,50,56,55,51,59,57,52],
[44,47,0,53,41,54,43,49,53,48,45],
[49,45,48,0,48,48,45,47,54,45,39],
[56,51,60,53,0,54,48,47,58,51,59],
[53,45,47,53,47,0,41,55,51,51,47],
[55,46,58,56,53,60,0,53,57,48,51],
[56,50,52,54,54,46,48,0,57,55,45],
[54,42,48,47,43,50,44,44,0,48,38],
[47,44,53,56,50,50,53,46,53,0,48],
[56,49,56,62,42,54,50,56,63,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 174, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,70,47,43,52,58,59,63,68,56,59],
[31,0,39,34,32,38,39,43,33,35,43],
[54,62,0,44,53,51,51,56,55,57,61],
[58,67,57,0,51,51,51,56,60,51,50],
[49,69,48,50,0,54,48,62,60,53,51],
[43,63,50,50,47,0,49,65,47,40,58],
[42,62,50,50,53,52,0,64,54,47,49],
[38,58,45,45,39,36,37,0,42,42,53],
[33,68,46,41,41,54,47,59,0,43,57],
[45,66,44,50,48,61,54,59,58,0,59],
[42,58,40,51,50,43,52,48,44,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 175, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,64,55,58,50,59,53,59,55,52,43],
[37,0,53,54,44,45,45,39,37,55,31],
[46,48,0,62,57,62,38,59,36,54,44],
[43,47,39,0,49,46,42,28,40,47,41],
[51,57,44,52,0,59,39,50,46,48,45],
[42,56,39,55,42,0,36,34,38,62,44],
[48,56,63,59,62,65,0,59,52,61,55],
[42,62,42,73,51,67,42,0,50,61,52],
[46,64,65,61,55,63,49,51,0,57,42],
[49,46,47,54,53,39,40,40,44,0,36],
[58,70,57,60,56,57,46,49,59,65,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 176, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,42,72,42,45,46,44,39,62,79],
[65,0,63,60,42,47,53,44,69,58,75],
[59,38,0,55,43,57,72,69,59,65,69],
[29,41,46,0,47,34,69,37,43,56,77],
[59,59,58,54,0,43,73,64,73,65,71],
[56,54,44,67,58,0,48,45,44,58,80],
[55,48,29,32,28,53,0,34,44,48,60],
[57,57,32,64,37,56,67,0,62,78,69],
[62,32,42,58,28,57,57,39,0,59,59],
[39,43,36,45,36,43,53,23,42,0,48],
[22,26,32,24,30,21,41,32,42,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 177, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,53,60,40,57,53,52,52,61,51],
[41,0,71,35,23,40,38,44,46,55,42],
[48,30,0,35,35,34,44,37,39,40,43],
[41,66,66,0,44,71,66,54,50,62,44],
[61,78,66,57,0,44,55,60,63,64,56],
[44,61,67,30,57,0,49,47,52,62,52],
[48,63,57,35,46,52,0,49,39,46,54],
[49,57,64,47,41,54,52,0,46,54,40],
[49,55,62,51,38,49,62,55,0,48,50],
[40,46,61,39,37,39,55,47,53,0,46],
[50,59,58,57,45,49,47,61,51,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 178, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,62,55,52,54,47,54,52,49,64],
[43,0,55,44,46,61,50,40,55,54,50],
[39,46,0,56,48,52,46,47,53,45,49],
[46,57,45,0,49,53,47,57,60,49,59],
[49,55,53,52,0,51,46,49,48,48,46],
[47,40,49,48,50,0,38,46,44,38,45],
[54,51,55,54,55,63,0,53,47,61,53],
[47,61,54,44,52,55,48,0,50,52,43],
[49,46,48,41,53,57,54,51,0,48,44],
[52,47,56,52,53,63,40,49,53,0,47],
[37,51,52,42,55,56,48,58,57,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 179, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,55,51,51,60,60,61,59,50,47],
[50,0,68,62,54,58,58,61,55,54,44],
[46,33,0,48,42,45,63,52,47,58,47],
[50,39,53,0,47,45,54,50,54,48,35],
[50,47,59,54,0,55,64,54,56,49,55],
[41,43,56,56,46,0,52,49,46,49,41],
[41,43,38,47,37,49,0,54,54,46,38],
[40,40,49,51,47,52,47,0,47,43,43],
[42,46,54,47,45,55,47,54,0,40,40],
[51,47,43,53,52,52,55,58,61,0,61],
[54,57,54,66,46,60,63,58,61,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 180, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,60,42,47,59,60,48,52,43,56],
[50,0,55,56,51,59,57,46,58,53,52],
[41,46,0,46,44,54,50,40,41,49,41],
[59,45,55,0,54,58,61,54,54,50,62],
[54,50,57,47,0,48,49,49,45,43,53],
[42,42,47,43,53,0,61,44,48,45,50],
[41,44,51,40,52,40,0,45,47,45,50],
[53,55,61,47,52,57,56,0,56,54,52],
[49,43,60,47,56,53,54,45,0,54,53],
[58,48,52,51,58,56,56,47,47,0,54],
[45,49,60,39,48,51,51,49,48,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 181, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,56,43,57,46,42,54,45,61,46],
[49,0,58,48,50,45,49,48,46,55,52],
[45,43,0,38,53,47,46,48,43,45,47],
[58,53,63,0,65,48,54,54,43,64,51],
[44,51,48,36,0,49,42,56,40,54,48],
[55,56,54,53,52,0,53,57,50,59,51],
[59,52,55,47,59,48,0,54,55,60,54],
[47,53,53,47,45,44,47,0,40,61,50],
[56,55,58,58,61,51,46,61,0,62,49],
[40,46,56,37,47,42,41,40,39,0,42],
[55,49,54,50,53,50,47,51,52,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 182, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,49,76,72,67,57,62,59,74,75],
[39,0,60,37,49,49,60,34,39,63,53],
[52,41,0,65,51,44,50,43,47,66,46],
[25,64,36,0,52,40,40,50,40,55,50],
[29,52,50,49,0,43,45,52,47,60,72],
[34,52,57,61,58,0,36,54,34,48,52],
[44,41,51,61,56,65,0,52,38,67,58],
[39,67,58,51,49,47,49,0,44,55,38],
[42,62,54,61,54,67,63,57,0,82,64],
[27,38,35,46,41,53,34,46,19,0,71],
[26,48,55,51,29,49,43,63,37,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 183, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,44,56,47,43,40,43,47,49,44],
[56,0,54,58,41,49,48,47,50,46,41],
[57,47,0,58,41,42,39,37,47,47,48],
[45,43,43,0,40,38,39,40,39,33,40],
[54,60,60,61,0,53,54,56,51,51,46],
[58,52,59,63,48,0,57,63,59,51,51],
[61,53,62,62,47,44,0,59,49,56,46],
[58,54,64,61,45,38,42,0,40,47,41],
[54,51,54,62,50,42,52,61,0,44,38],
[52,55,54,68,50,50,45,54,57,0,46],
[57,60,53,61,55,50,55,60,63,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 184, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,64,35,58,51,51,38,31,51,51],
[67,0,57,25,40,62,47,42,24,51,60],
[37,44,0,39,38,31,30,50,25,38,37],
[66,76,62,0,76,76,59,54,63,49,62],
[43,61,63,25,0,65,39,55,47,51,72],
[50,39,70,25,36,0,33,55,47,51,41],
[50,54,71,42,62,68,0,53,47,25,48],
[63,59,51,47,46,46,48,0,24,57,60],
[70,77,76,38,54,54,54,77,0,72,63],
[50,50,63,52,50,50,76,44,29,0,65],
[50,41,64,39,29,60,53,41,38,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 185, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,44,47,43,61,47,50,48,44,51],
[47,0,38,51,41,50,51,48,40,46,51],
[57,63,0,55,48,63,50,52,45,45,51],
[54,50,46,0,46,49,50,51,50,46,52],
[58,60,53,55,0,57,61,50,51,57,55],
[40,51,38,52,44,0,46,45,44,47,47],
[54,50,51,51,40,55,0,56,50,50,52],
[51,53,49,50,51,56,45,0,44,54,51],
[53,61,56,51,50,57,51,57,0,57,55],
[57,55,56,55,44,54,51,47,44,0,54],
[50,50,50,49,46,54,49,50,46,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 186, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,50,62,46,37,46,44,46,25,72],
[73,0,68,72,53,55,72,44,69,48,69],
[51,33,0,72,25,34,72,44,59,38,58],
[39,29,29,0,29,45,53,62,40,22,37],
[55,48,76,72,0,76,72,51,90,30,58],
[64,46,67,56,25,0,67,46,56,39,49],
[55,29,29,48,29,34,0,48,48,56,55],
[57,57,57,39,50,55,53,0,39,32,39],
[55,32,42,61,11,45,53,62,0,38,40],
[76,53,63,79,71,62,45,69,63,0,79],
[29,32,43,64,43,52,46,62,61,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 187, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,54,56,47,51,53,49,51,54,52],
[50,0,52,48,50,45,57,48,52,51,50],
[47,49,0,43,48,52,49,43,47,41,48],
[45,53,58,0,51,54,49,40,46,50,41],
[54,51,53,50,0,54,55,52,54,54,58],
[50,56,49,47,47,0,52,43,49,47,52],
[48,44,52,52,46,49,0,42,47,49,41],
[52,53,58,61,49,58,59,0,59,49,45],
[50,49,54,55,47,52,54,42,0,48,52],
[47,50,60,51,47,54,52,52,53,0,50],
[49,51,53,60,43,49,60,56,49,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 188, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,64,57,65,65,52,73,71,59,71],
[54,0,50,44,56,56,51,57,52,56,42],
[37,51,0,56,29,42,65,64,46,52,48],
[44,57,45,0,45,75,55,77,59,62,53],
[36,45,72,56,0,72,53,66,60,42,39],
[36,45,59,26,29,0,42,60,30,29,55],
[49,50,36,46,48,59,0,76,41,53,59],
[28,44,37,24,35,41,25,0,40,42,33],
[30,49,55,42,41,71,60,61,0,64,60],
[42,45,49,39,59,72,48,59,37,0,51],
[30,59,53,48,62,46,42,68,41,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 189, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,48,50,50,46,48,53,53,47,44],
[57,0,47,52,54,43,60,57,61,54,49],
[53,54,0,59,49,50,49,53,51,51,49],
[51,49,42,0,51,55,53,60,62,54,50],
[51,47,52,50,0,55,54,58,55,48,52],
[55,58,51,46,46,0,59,64,59,57,56],
[53,41,52,48,47,42,0,54,57,51,40],
[48,44,48,41,43,37,47,0,54,46,48],
[48,40,50,39,46,42,44,47,0,42,44],
[54,47,50,47,53,44,50,55,59,0,49],
[57,52,52,51,49,45,61,53,57,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 190, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,41,57,72,53,28,53,43,53,57],
[77,0,62,70,91,57,59,47,43,64,64],
[60,39,0,57,91,39,45,43,39,70,33],
[44,31,44,0,58,60,35,74,60,60,60],
[29,10,10,43,0,39,14,29,39,39,39],
[48,44,62,41,62,0,59,43,33,60,64],
[73,42,56,66,87,42,0,56,42,73,29],
[48,54,58,27,72,58,45,0,45,54,45],
[58,58,62,41,62,68,59,56,0,87,78],
[48,37,31,41,62,41,28,47,14,0,18],
[44,37,68,41,62,37,72,56,23,83,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 191, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,48,45,47,46,50,49,45,40,47],
[60,0,53,58,55,51,56,57,58,50,53],
[53,48,0,56,48,58,53,57,51,49,51],
[56,43,45,0,47,42,50,48,46,45,48],
[54,46,53,54,0,52,53,47,51,43,55],
[55,50,43,59,49,0,53,55,46,54,52],
[51,45,48,51,48,48,0,47,53,50,49],
[52,44,44,53,54,46,54,0,46,47,50],
[56,43,50,55,50,55,48,55,0,56,54],
[61,51,52,56,58,47,51,54,45,0,57],
[54,48,50,53,46,49,52,51,47,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 192, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,74,45,35,68,75,54,47,17,40,37],
[27,0,40,30,49,47,38,46,22,46,17],
[56,61,0,41,65,62,62,53,57,56,32],
[66,71,60,0,84,90,71,82,64,69,48],
[33,52,36,17,0,46,49,53,27,42,25],
[26,54,39,11,55,0,46,43,34,36,19],
[47,63,39,30,52,55,0,26,13,26,17],
[54,55,48,19,48,58,75,0,41,67,37],
[84,79,44,37,74,67,88,60,0,50,64],
[61,55,45,32,59,65,75,34,51,0,48],
[64,84,69,53,76,82,84,64,37,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 193, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,37,41,40,56,44,40,57,66,41],
[70,0,73,74,72,61,77,38,80,72,67],
[64,28,0,71,55,57,60,42,63,61,40],
[60,27,30,0,46,46,58,48,47,48,55],
[61,29,46,55,0,48,66,41,79,54,54],
[45,40,44,55,53,0,68,50,66,41,60],
[57,24,41,43,35,33,0,52,51,59,55],
[61,63,59,53,60,51,49,0,73,53,43],
[44,21,38,54,22,35,50,28,0,24,58],
[35,29,40,53,47,60,42,48,77,0,54],
[60,34,61,46,47,41,46,58,43,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 194, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,47,40,48,51,42,55,41,62,48],
[69,0,50,62,65,52,55,57,45,58,55],
[54,51,0,51,51,38,38,51,40,47,51],
[61,39,50,0,61,48,48,56,51,66,53],
[53,36,50,40,0,43,36,49,35,55,43],
[50,49,63,53,58,0,43,56,44,65,62],
[59,46,63,53,65,58,0,66,57,68,54],
[46,44,50,45,52,45,35,0,49,59,50],
[60,56,61,50,66,57,44,52,0,68,58],
[39,43,54,35,46,36,33,42,33,0,39],
[53,46,50,48,58,39,47,51,43,62,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 195, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,52,58,48,52,51,55,45,48,53],
[48,0,51,47,51,53,49,47,48,53,44],
[49,50,0,49,54,57,51,51,55,53,56],
[43,54,52,0,43,54,47,52,48,51,51],
[53,50,47,58,0,52,53,52,52,51,55],
[49,48,44,47,49,0,53,53,44,49,47],
[50,52,50,54,48,48,0,54,48,55,53],
[46,54,50,49,49,48,47,0,50,48,53],
[56,53,46,53,49,57,53,51,0,56,53],
[53,48,48,50,50,52,46,53,45,0,54],
[48,57,45,50,46,54,48,48,48,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 196, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,49,61,58,46,39,55,50,50,58],
[52,0,56,46,54,48,53,54,54,55,55],
[52,45,0,39,62,39,39,42,42,56,55],
[40,55,62,0,73,47,49,41,53,62,65],
[43,47,39,28,0,43,36,38,41,45,40],
[55,53,62,54,58,0,44,59,63,59,65],
[62,48,62,52,65,57,0,64,52,68,69],
[46,47,59,60,63,42,37,0,50,59,49],
[51,47,59,48,60,38,49,51,0,59,61],
[51,46,45,39,56,42,33,42,42,0,57],
[43,46,46,36,61,36,32,52,40,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 197, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,61,47,48,48,59,56,58,55,51],
[54,0,59,48,46,48,62,57,53,53,53],
[40,42,0,45,53,46,59,49,48,52,49],
[54,53,56,0,51,60,65,58,52,56,48],
[53,55,48,50,0,51,53,57,49,54,50],
[53,53,55,41,50,0,52,52,50,58,49],
[42,39,42,36,48,49,0,42,39,47,40],
[45,44,52,43,44,49,59,0,43,41,50],
[43,48,53,49,52,51,62,58,0,58,49],
[46,48,49,45,47,43,54,60,43,0,47],
[50,48,52,53,51,52,61,51,52,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 198, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,71,61,80,72,43,82,57,60,60],
[41,0,56,67,49,43,57,79,45,39,67],
[30,45,0,49,60,56,32,44,39,43,36],
[40,34,52,0,50,55,53,69,49,32,52],
[21,52,41,51,0,49,47,68,35,45,45],
[29,58,45,46,52,0,36,68,30,34,50],
[58,44,69,48,54,65,0,77,56,42,64],
[19,22,57,32,33,33,24,0,29,32,22],
[44,56,62,52,66,71,45,72,0,57,70],
[41,62,58,69,56,67,59,69,44,0,54],
[41,34,65,49,56,51,37,79,31,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 199, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,40,48,40,52,50,47,55,42,39],
[60,0,51,52,53,51,52,48,52,51,44],
[61,50,0,59,59,57,51,54,57,49,52],
[53,49,42,0,39,61,39,49,54,44,38],
[61,48,42,62,0,61,63,52,61,49,54],
[49,50,44,40,40,0,43,53,54,48,50],
[51,49,50,62,38,58,0,55,53,56,53],
[54,53,47,52,49,48,46,0,56,54,58],
[46,49,44,47,40,47,48,45,0,42,47],
[59,50,52,57,52,53,45,47,59,0,49],
[62,57,49,63,47,51,48,43,54,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 101, 200, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbd/mebbd_11_101.csv", index=False, header=False)