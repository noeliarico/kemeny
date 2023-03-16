
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg
from kemeny import sc

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,55,69,49,55,53,69,47,53],
[46,0,48,47,54,48,57,53,42],
[32,53,0,46,44,42,57,48,38],
[52,54,55,0,49,54,56,48,37],
[46,47,57,52,0,55,67,51,42],
[48,53,59,47,46,0,52,47,38],
[32,44,44,45,34,49,0,36,33],
[54,48,53,53,50,54,65,0,38],
[48,59,63,64,59,63,68,63,0]])



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
result = np.append(np.array([9, 101, 1, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,56,54,47,48,58,55,47],
[40,0,44,57,41,49,49,49,43],
[45,57,0,60,54,50,53,55,52],
[47,44,41,0,41,43,46,38,47],
[54,60,47,60,0,50,58,51,48],
[53,52,51,58,51,0,56,45,55],
[43,52,48,55,43,45,0,43,43],
[46,52,46,63,50,56,58,0,51],
[54,58,49,54,53,46,58,50,0]])



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
result = np.append(np.array([9, 101, 2, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,69,64,56,47,60,56,52,51],
[32,0,38,33,37,51,44,41,41],
[37,63,0,35,45,47,56,56,39],
[45,68,66,0,36,48,48,46,41],
[54,64,56,65,0,61,50,49,53],
[41,50,54,53,40,0,56,55,55],
[45,57,45,53,51,45,0,49,45],
[49,60,45,55,52,46,52,0,38],
[50,60,62,60,48,46,56,63,0]])



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
result = np.append(np.array([9, 101, 3, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,47,49,60,45,53,53,44],
[49,0,50,49,50,50,50,56,40],
[54,51,0,50,46,43,46,50,45],
[52,52,51,0,51,52,50,55,50],
[41,51,55,50,0,49,48,48,37],
[56,51,58,49,52,0,49,55,40],
[48,51,55,51,53,52,0,48,53],
[48,45,51,46,53,46,53,0,45],
[57,61,56,51,64,61,48,56,0]])



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
result = np.append(np.array([9, 101, 4, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,48,49,58,46,40,46,44],
[51,0,53,46,56,52,51,50,48],
[53,48,0,52,58,46,45,50,46],
[52,55,49,0,57,47,54,55,45],
[43,45,43,44,0,44,44,47,40],
[55,49,55,54,57,0,52,53,58],
[61,50,56,47,57,49,0,53,48],
[55,51,51,46,54,48,48,0,46],
[57,53,55,56,61,43,53,55,0]])



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
result = np.append(np.array([9, 101, 5, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,55,47,50,47,48,59,39],
[42,0,46,44,46,48,50,53,41],
[46,55,0,55,51,52,44,48,45],
[54,57,46,0,48,52,55,59,43],
[51,55,50,53,0,55,52,53,55],
[54,53,49,49,46,0,55,55,54],
[53,51,57,46,49,46,0,51,42],
[42,48,53,42,48,46,50,0,42],
[62,60,56,58,46,47,59,59,0]])



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
result = np.append(np.array([9, 101, 6, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,50,56,59,43,55,66,57],
[46,0,45,55,73,57,56,74,65],
[51,56,0,65,77,56,44,62,71],
[45,46,36,0,65,61,37,62,53],
[42,28,24,36,0,38,23,52,39],
[58,44,45,40,63,0,53,73,65],
[46,45,57,64,78,48,0,58,71],
[35,27,39,39,49,28,43,0,55],
[44,36,30,48,62,36,30,46,0]])



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
result = np.append(np.array([9, 101, 7, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,48,54,66,54,98,62,54],
[65,0,27,54,42,54,74,62,54],
[53,74,0,54,54,54,50,38,74],
[47,47,47,0,66,27,44,38,41],
[35,59,47,35,0,59,35,23,53],
[47,47,47,74,42,0,56,38,77],
[3,27,51,57,66,45,0,18,45],
[39,39,63,63,78,63,83,0,81],
[47,47,27,60,48,24,56,20,0]])



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
result = np.append(np.array([9, 101, 8, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,36,18,18,28,5,19,19],
[83,0,88,61,62,62,28,57,38],
[65,13,0,36,51,23,28,52,14],
[83,40,65,0,33,50,43,29,29],
[83,39,50,68,0,68,28,41,33],
[73,39,78,51,33,0,18,47,51],
[96,73,73,58,73,83,0,41,73],
[82,44,49,72,60,54,60,0,37],
[82,63,87,72,68,50,28,64,0]])



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
result = np.append(np.array([9, 101, 9, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,39,26,42,33,36,47,44],
[59,0,52,48,64,51,58,51,50],
[62,49,0,44,60,53,44,55,44],
[75,53,57,0,56,58,57,62,47],
[59,37,41,45,0,38,43,59,50],
[68,50,48,43,63,0,49,39,58],
[65,43,57,44,58,52,0,41,62],
[54,50,46,39,42,62,60,0,62],
[57,51,57,54,51,43,39,39,0]])



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
result = np.append(np.array([9, 101, 10, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,45,46,54,47,54,58,52],
[49,0,48,52,61,58,53,58,71],
[56,53,0,53,58,50,59,63,65],
[55,49,48,0,61,54,55,57,56],
[47,40,43,40,0,44,48,56,63],
[54,43,51,47,57,0,49,56,57],
[47,48,42,46,53,52,0,54,64],
[43,43,38,44,45,45,47,0,53],
[49,30,36,45,38,44,37,48,0]])



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
result = np.append(np.array([9, 101, 11, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,50,59,50,49,58,43,45],
[42,0,50,46,43,44,49,44,41],
[51,51,0,52,44,54,53,47,47],
[42,55,49,0,45,51,54,43,48],
[51,58,57,56,0,55,52,51,44],
[52,57,47,50,46,0,51,44,43],
[43,52,48,47,49,50,0,44,45],
[58,57,54,58,50,57,57,0,52],
[56,60,54,53,57,58,56,49,0]])



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
result = np.append(np.array([9, 101, 12, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,49,59,46,53,45,45,53],
[45,0,36,42,46,36,39,28,33],
[52,65,0,58,52,38,44,46,44],
[42,59,43,0,46,42,48,34,39],
[55,55,49,55,0,55,45,37,42],
[48,65,63,59,46,0,42,45,52],
[56,62,57,53,56,59,0,43,49],
[56,73,55,67,64,56,58,0,45],
[48,68,57,62,59,49,52,56,0]])



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
result = np.append(np.array([9, 101, 13, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,19,101,73,49,71,19,25],
[52,0,24,52,46,24,46,43,52],
[82,77,0,101,95,55,77,19,47],
[0,49,0,0,0,19,19,19,0],
[28,55,6,101,0,55,47,19,25],
[52,77,46,82,46,0,41,65,52],
[30,55,24,82,54,60,0,43,30],
[82,58,82,82,82,36,58,0,28],
[76,49,54,101,76,49,71,73,0]])



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
result = np.append(np.array([9, 101, 14, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,42,49,53,45,53,56,47],
[44,0,41,51,58,43,50,37,49],
[59,60,0,54,59,56,52,47,50],
[52,50,47,0,44,51,40,44,48],
[48,43,42,57,0,42,43,40,46],
[56,58,45,50,59,0,54,47,52],
[48,51,49,61,58,47,0,47,47],
[45,64,54,57,61,54,54,0,58],
[54,52,51,53,55,49,54,43,0]])



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
result = np.append(np.array([9, 101, 15, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,50,40,49,50,43,46,43],
[57,0,52,47,54,49,52,46,50],
[51,49,0,45,54,51,52,51,55],
[61,54,56,0,53,48,51,52,49],
[52,47,47,48,0,49,45,47,51],
[51,52,50,53,52,0,50,49,50],
[58,49,49,50,56,51,0,47,49],
[55,55,50,49,54,52,54,0,54],
[58,51,46,52,50,51,52,47,0]])



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
result = np.append(np.array([9, 101, 16, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,52,49,49,48,38,52,39],
[57,0,58,44,55,54,54,62,52],
[49,43,0,47,53,54,61,60,42],
[52,57,54,0,54,58,61,66,49],
[52,46,48,47,0,51,50,52,40],
[53,47,47,43,50,0,52,49,43],
[63,47,40,40,51,49,0,58,42],
[49,39,41,35,49,52,43,0,41],
[62,49,59,52,61,58,59,60,0]])



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
result = np.append(np.array([9, 101, 17, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,37,59,66,44,60,72,69],
[43,0,54,70,72,47,61,74,78],
[64,47,0,64,68,62,65,70,78],
[42,31,37,0,43,43,62,62,53],
[35,29,33,58,0,41,44,59,53],
[57,54,39,58,60,0,74,63,71],
[41,40,36,39,57,27,0,58,59],
[29,27,31,39,42,38,43,0,49],
[32,23,23,48,48,30,42,52,0]])



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
result = np.append(np.array([9, 101, 18, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,50,58,49,62,61,52,66],
[49,0,54,60,58,66,62,50,61],
[51,47,0,55,53,59,49,44,57],
[43,41,46,0,44,56,42,40,52],
[52,43,48,57,0,57,57,47,55],
[39,35,42,45,44,0,38,41,43],
[40,39,52,59,44,63,0,49,54],
[49,51,57,61,54,60,52,0,54],
[35,40,44,49,46,58,47,47,0]])



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
result = np.append(np.array([9, 101, 19, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,54,63,61,44,67,61,53],
[48,0,52,66,51,52,48,56,59],
[47,49,0,65,50,47,59,54,58],
[38,35,36,0,41,35,37,52,44],
[40,50,51,60,0,43,44,48,52],
[57,49,54,66,58,0,60,68,66],
[34,53,42,64,57,41,0,51,45],
[40,45,47,49,53,33,50,0,50],
[48,42,43,57,49,35,56,51,0]])



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
result = np.append(np.array([9, 101, 20, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,41,58,43,48,52,49,55],
[43,0,42,50,47,43,53,49,47],
[60,59,0,58,55,49,62,48,52],
[43,51,43,0,47,43,52,44,48],
[58,54,46,54,0,49,53,47,49],
[53,58,52,58,52,0,61,47,55],
[49,48,39,49,48,40,0,47,47],
[52,52,53,57,54,54,54,0,50],
[46,54,49,53,52,46,54,51,0]])



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
result = np.append(np.array([9, 101, 21, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,46,47,48,48,42,46,53],
[53,0,53,49,51,49,50,50,52],
[55,48,0,46,56,51,46,49,54],
[54,52,55,0,51,50,50,55,57],
[53,50,45,50,0,51,49,54,49],
[53,52,50,51,50,0,49,55,52],
[59,51,55,51,52,52,0,56,50],
[55,51,52,46,47,46,45,0,57],
[48,49,47,44,52,49,51,44,0]])



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
result = np.append(np.array([9, 101, 22, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,65,56,70,73,36,56,52,48],
[36,0,59,45,65,46,59,39,45],
[45,42,0,70,81,36,34,24,41],
[31,56,31,0,38,59,31,44,52],
[28,36,20,63,0,35,33,33,48],
[65,55,65,42,66,0,31,31,63],
[45,42,67,70,68,70,0,26,63],
[49,62,77,57,68,70,75,0,50],
[53,56,60,49,53,38,38,51,0]])



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
result = np.append(np.array([9, 101, 23, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,56,50,63,59,48,63,61],
[51,0,47,57,55,54,56,52,48],
[45,54,0,37,50,61,52,49,38],
[51,44,64,0,60,69,45,65,50],
[38,46,51,41,0,64,50,44,36],
[42,47,40,32,37,0,43,43,30],
[53,45,49,56,51,58,0,56,52],
[38,49,52,36,57,58,45,0,47],
[40,53,63,51,65,71,49,54,0]])



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
result = np.append(np.array([9, 101, 24, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,52,53,49,52,53,52,51],
[49,0,52,53,48,53,49,58,41],
[49,49,0,43,53,53,55,54,45],
[48,48,58,0,50,59,55,57,47],
[52,53,48,51,0,55,50,53,50],
[49,48,48,42,46,0,50,50,43],
[48,52,46,46,51,51,0,57,51],
[49,43,47,44,48,51,44,0,37],
[50,60,56,54,51,58,50,64,0]])



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
result = np.append(np.array([9, 101, 25, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,53,56,55,55,57,44,54],
[49,0,49,46,49,53,54,47,53],
[48,52,0,47,52,52,55,55,52],
[45,55,54,0,48,56,57,53,49],
[46,52,49,53,0,51,52,51,48],
[46,48,49,45,50,0,49,43,54],
[44,47,46,44,49,52,0,45,48],
[57,54,46,48,50,58,56,0,51],
[47,48,49,52,53,47,53,50,0]])



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
result = np.append(np.array([9, 101, 26, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,50,44,46,54,51,53,48],
[50,0,39,47,34,50,42,52,43],
[51,62,0,45,49,53,56,58,52],
[57,54,56,0,50,55,52,59,52],
[55,67,52,51,0,49,53,57,51],
[47,51,48,46,52,0,50,50,48],
[50,59,45,49,48,51,0,56,48],
[48,49,43,42,44,51,45,0,44],
[53,58,49,49,50,53,53,57,0]])



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
result = np.append(np.array([9, 101, 27, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,65,52,60,53,54,59,50,57],
[36,0,45,44,58,39,40,40,45],
[49,56,0,45,56,44,57,52,59],
[41,57,56,0,55,47,50,52,46],
[48,43,45,46,0,37,45,38,52],
[47,62,57,54,64,0,45,50,52],
[42,61,44,51,56,56,0,43,52],
[51,61,49,49,63,51,58,0,60],
[44,56,42,55,49,49,49,41,0]])



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
result = np.append(np.array([9, 101, 28, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,57,50,45,62,57,52,44],
[45,0,49,43,44,43,54,36,39],
[44,52,0,54,52,49,61,44,51],
[51,58,47,0,58,57,57,46,41],
[56,57,49,43,0,48,62,34,48],
[39,58,52,44,53,0,49,45,44],
[44,47,40,44,39,52,0,38,40],
[49,65,57,55,67,56,63,0,51],
[57,62,50,60,53,57,61,50,0]])



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
result = np.append(np.array([9, 101, 29, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,79,56,63,52,35,28,51,57],
[22,0,49,21,15,49,49,28,15],
[45,52,0,28,45,56,22,24,52],
[38,80,73,0,38,72,43,52,45],
[49,86,56,63,0,77,77,58,70],
[66,52,45,29,24,0,43,24,45],
[73,52,79,58,24,58,0,51,52],
[50,73,77,49,43,77,50,0,43],
[44,86,49,56,31,56,49,58,0]])



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
result = np.append(np.array([9, 101, 30, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,32,82,49,31,63,37,29],
[53,0,35,80,38,34,34,45,35],
[69,66,0,82,50,34,35,30,18],
[19,21,19,0,16,8,18,19,18],
[52,63,51,85,0,35,43,46,18],
[70,67,67,93,66,0,49,21,31],
[38,67,66,83,58,52,0,65,47],
[64,56,71,82,55,80,36,0,62],
[72,66,83,83,83,70,54,39,0]])



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
result = np.append(np.array([9, 101, 31, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,42,43,53,45,47,68,62],
[41,0,65,42,51,43,38,74,51],
[59,36,0,32,57,40,43,49,48],
[58,59,69,0,69,45,48,69,53],
[48,50,44,32,0,52,55,56,53],
[56,58,61,56,49,0,48,76,69],
[54,63,58,53,46,53,0,70,50],
[33,27,52,32,45,25,31,0,42],
[39,50,53,48,48,32,51,59,0]])



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
result = np.append(np.array([9, 101, 32, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,53,50,43,38,40,53,48],
[55,0,51,57,49,55,54,65,57],
[48,50,0,63,60,45,60,59,51],
[51,44,38,0,46,33,43,52,46],
[58,52,41,55,0,41,47,55,43],
[63,46,56,68,60,0,65,66,53],
[61,47,41,58,54,36,0,48,41],
[48,36,42,49,46,35,53,0,48],
[53,44,50,55,58,48,60,53,0]])



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
result = np.append(np.array([9, 101, 33, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,47,63,55,54,55,48,55],
[48,0,57,64,69,49,57,62,55],
[54,44,0,52,54,42,50,48,46],
[38,37,49,0,40,35,41,37,40],
[46,32,47,61,0,41,45,51,47],
[47,52,59,66,60,0,66,50,55],
[46,44,51,60,56,35,0,44,52],
[53,39,53,64,50,51,57,0,51],
[46,46,55,61,54,46,49,50,0]])



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
result = np.append(np.array([9, 101, 34, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,27,45,45,27,57,45,36],
[80,0,57,71,83,45,39,27,36],
[74,44,0,65,47,18,59,18,18],
[56,30,36,0,39,6,39,24,0],
[56,18,54,62,0,24,39,42,36],
[74,56,83,95,77,0,59,47,62],
[44,62,42,62,62,42,0,42,36],
[56,74,83,77,59,54,59,0,44],
[65,65,83,101,65,39,65,57,0]])



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
result = np.append(np.array([9, 101, 35, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,76,68,84,68,53,46,54],
[44,0,49,63,79,54,55,54,50],
[25,52,0,71,65,59,48,42,42],
[33,38,30,0,48,62,59,44,23],
[17,22,36,53,0,24,31,25,26],
[33,47,42,39,77,0,50,39,32],
[48,46,53,42,70,51,0,41,46],
[55,47,59,57,76,62,60,0,32],
[47,51,59,78,75,69,55,69,0]])



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
result = np.append(np.array([9, 101, 36, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,45,55,48,48,59,53,48],
[42,0,37,43,34,34,55,37,40],
[56,64,0,60,48,46,58,49,58],
[46,58,41,0,42,41,60,45,52],
[53,67,53,59,0,44,56,54,54],
[53,67,55,60,57,0,65,45,52],
[42,46,43,41,45,36,0,39,48],
[48,64,52,56,47,56,62,0,59],
[53,61,43,49,47,49,53,42,0]])



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
result = np.append(np.array([9, 101, 37, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,25,25,47,39,25,22,22],
[82,0,47,101,78,83,60,71,59],
[76,54,0,57,71,67,44,37,34],
[76,0,44,0,44,74,57,50,59],
[54,23,30,57,0,52,35,60,25],
[62,18,34,27,49,0,27,49,49],
[76,41,57,44,66,74,0,44,54],
[79,30,64,51,41,52,57,0,59],
[79,42,67,42,76,52,47,42,0]])



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
result = np.append(np.array([9, 101, 38, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,65,63,63,59,94,31,65,65],
[36,0,68,63,62,99,62,70,70],
[38,33,0,31,38,33,36,7,2],
[38,38,70,0,64,101,64,70,70],
[42,39,63,37,0,68,31,65,65],
[7,2,68,0,33,0,31,33,28],
[70,39,65,37,70,70,0,65,39],
[36,31,94,31,36,68,36,0,31],
[36,31,99,31,36,73,62,70,0]])



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
result = np.append(np.array([9, 101, 39, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,60,53,61,65,66,43,54],
[41,0,50,51,51,56,56,56,41],
[41,51,0,48,45,50,56,54,47],
[48,50,53,0,56,65,64,53,49],
[40,50,56,45,0,53,60,39,40],
[36,45,51,36,48,0,48,42,30],
[35,45,45,37,41,53,0,45,42],
[58,45,47,48,62,59,56,0,46],
[47,60,54,52,61,71,59,55,0]])



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
result = np.append(np.array([9, 101, 40, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,29,55,23,11,22,28,44],
[91,0,65,66,76,54,50,69,67],
[72,36,0,68,43,39,35,54,58],
[46,35,33,0,36,32,32,44,39],
[78,25,58,65,0,53,51,57,88],
[90,47,62,69,48,0,53,54,73],
[79,51,66,69,50,48,0,69,88],
[73,32,47,57,44,47,32,0,63],
[57,34,43,62,13,28,13,38,0]])



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
result = np.append(np.array([9, 101, 41, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,56,47,52,46,41,51,51],
[59,0,62,60,55,55,48,57,52],
[45,39,0,46,43,35,41,47,39],
[54,41,55,0,56,51,43,48,46],
[49,46,58,45,0,47,48,47,51],
[55,46,66,50,54,0,52,51,53],
[60,53,60,58,53,49,0,67,52],
[50,44,54,53,54,50,34,0,49],
[50,49,62,55,50,48,49,52,0]])



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
result = np.append(np.array([9, 101, 42, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,52,45,40,38,45,42,52],
[49,0,55,46,42,55,54,46,55],
[49,46,0,42,48,48,56,48,53],
[56,55,59,0,47,45,64,60,48],
[61,59,53,54,0,45,54,55,61],
[63,46,53,56,56,0,62,56,57],
[56,47,45,37,47,39,0,40,58],
[59,55,53,41,46,45,61,0,47],
[49,46,48,53,40,44,43,54,0]])



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
result = np.append(np.array([9, 101, 43, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,61,37,59,55,45,63,53],
[40,0,40,41,56,57,31,45,42],
[40,61,0,61,59,55,59,54,49],
[64,60,40,0,66,51,48,53,45],
[42,45,42,35,0,43,47,31,35],
[46,44,46,50,58,0,40,52,36],
[56,70,42,53,54,61,0,54,46],
[38,56,47,48,70,49,47,0,45],
[48,59,52,56,66,65,55,56,0]])



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
result = np.append(np.array([9, 101, 44, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,56,62,56,49,47,54,56],
[44,0,51,49,45,47,50,60,53],
[45,50,0,54,54,64,60,65,50],
[39,52,47,0,44,55,39,54,47],
[45,56,47,57,0,50,50,67,59],
[52,54,37,46,51,0,50,55,58],
[54,51,41,62,51,51,0,54,58],
[47,41,36,47,34,46,47,0,48],
[45,48,51,54,42,43,43,53,0]])



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
result = np.append(np.array([9, 101, 45, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,44,50,53,55,55,57,56],
[42,0,32,49,43,51,36,55,43],
[57,69,0,55,58,58,49,62,63],
[51,52,46,0,60,58,55,58,49],
[48,58,43,41,0,58,54,44,54],
[46,50,43,43,43,0,50,45,52],
[46,65,52,46,47,51,0,48,57],
[44,46,39,43,57,56,53,0,48],
[45,58,38,52,47,49,44,53,0]])



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
result = np.append(np.array([9, 101, 46, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,46,47,49,41,40,36,52],
[59,0,46,54,55,55,55,47,63],
[55,55,0,52,53,49,48,52,57],
[54,47,49,0,48,45,52,37,53],
[52,46,48,53,0,47,56,46,63],
[60,46,52,56,54,0,51,46,54],
[61,46,53,49,45,50,0,44,49],
[65,54,49,64,55,55,57,0,63],
[49,38,44,48,38,47,52,38,0]])



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
result = np.append(np.array([9, 101, 47, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,51,53,50,58,51,44,56],
[47,0,58,47,51,56,48,52,53],
[50,43,0,52,46,51,53,47,57],
[48,54,49,0,53,54,53,40,49],
[51,50,55,48,0,51,54,47,61],
[43,45,50,47,50,0,53,40,49],
[50,53,48,48,47,48,0,42,54],
[57,49,54,61,54,61,59,0,60],
[45,48,44,52,40,52,47,41,0]])



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
result = np.append(np.array([9, 101, 48, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,56,55,54,54,49,51,52],
[51,0,52,62,55,53,55,51,50],
[45,49,0,56,45,47,47,50,46],
[46,39,45,0,45,37,48,44,44],
[47,46,56,56,0,49,48,44,56],
[47,48,54,64,52,0,51,50,46],
[52,46,54,53,53,50,0,49,49],
[50,50,51,57,57,51,52,0,49],
[49,51,55,57,45,55,52,52,0]])



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
result = np.append(np.array([9, 101, 49, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,52,46,56,53,58,54,61],
[60,0,56,59,73,49,60,66,55],
[49,45,0,57,55,61,63,59,66],
[55,42,44,0,44,48,53,46,65],
[45,28,46,57,0,47,55,51,59],
[48,52,40,53,54,0,58,53,58],
[43,41,38,48,46,43,0,45,55],
[47,35,42,55,50,48,56,0,65],
[40,46,35,36,42,43,46,36,0]])



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
result = np.append(np.array([9, 101, 50, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,59,56,59,53,52,44,46],
[50,0,70,63,57,65,56,51,49],
[42,31,0,34,46,44,44,31,28],
[45,38,67,0,49,56,51,40,45],
[42,44,55,52,0,62,47,42,44],
[48,36,57,45,39,0,42,38,38],
[49,45,57,50,54,59,0,46,41],
[57,50,70,61,59,63,55,0,57],
[55,52,73,56,57,63,60,44,0]])



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
result = np.append(np.array([9, 101, 51, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,55,48,48,47,46,47,46],
[46,0,50,48,45,45,44,46,51],
[46,51,0,49,46,47,43,37,48],
[53,53,52,0,47,51,46,43,49],
[53,56,55,54,0,51,53,47,48],
[54,56,54,50,50,0,49,45,51],
[55,57,58,55,48,52,0,47,53],
[54,55,64,58,54,56,54,0,49],
[55,50,53,52,53,50,48,52,0]])



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
result = np.append(np.array([9, 101, 52, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,62,33,44,49,55,54,44],
[58,0,42,39,42,67,57,46,58],
[39,59,0,48,53,69,78,65,62],
[68,62,53,0,50,67,62,64,65],
[57,59,48,51,0,58,71,60,65],
[52,34,32,34,43,0,60,50,41],
[46,44,23,39,30,41,0,38,44],
[47,55,36,37,41,51,63,0,48],
[57,43,39,36,36,60,57,53,0]])



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
result = np.append(np.array([9, 101, 53, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,62,55,53,47,59,65,57],
[44,0,46,56,46,45,52,55,54],
[39,55,0,54,50,44,59,60,43],
[46,45,47,0,43,41,48,57,44],
[48,55,51,58,0,50,57,69,50],
[54,56,57,60,51,0,51,62,48],
[42,49,42,53,44,50,0,54,44],
[36,46,41,44,32,39,47,0,41],
[44,47,58,57,51,53,57,60,0]])



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
result = np.append(np.array([9, 101, 54, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,56,46,46,48,54,41,55],
[48,0,45,46,41,52,49,41,42],
[45,56,0,44,40,46,49,48,49],
[55,55,57,0,57,50,46,47,54],
[55,60,61,44,0,53,57,43,56],
[53,49,55,51,48,0,53,51,53],
[47,52,52,55,44,48,0,40,48],
[60,60,53,54,58,50,61,0,60],
[46,59,52,47,45,48,53,41,0]])



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
result = np.append(np.array([9, 101, 55, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,49,50,54,55,55,50,47],
[47,0,45,50,46,46,47,45,40],
[52,56,0,52,51,53,50,46,43],
[51,51,49,0,49,57,49,51,38],
[47,55,50,52,0,53,47,52,51],
[46,55,48,44,48,0,54,48,48],
[46,54,51,52,54,47,0,50,40],
[51,56,55,50,49,53,51,0,43],
[54,61,58,63,50,53,61,58,0]])



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
result = np.append(np.array([9, 101, 56, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,44,50,45,47,49,38,44],
[51,0,45,47,43,51,54,46,45],
[57,56,0,59,43,51,52,52,50],
[51,54,42,0,49,50,44,47,50],
[56,58,58,52,0,56,50,47,43],
[54,50,50,51,45,0,52,48,52],
[52,47,49,57,51,49,0,53,50],
[63,55,49,54,54,53,48,0,49],
[57,56,51,51,58,49,51,52,0]])



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
result = np.append(np.array([9, 101, 57, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,49,48,54,57,59,51,51],
[50,0,50,47,53,57,59,50,46],
[52,51,0,57,49,54,45,48,38],
[53,54,44,0,53,60,46,47,43],
[47,48,52,48,0,61,58,56,50],
[44,44,47,41,40,0,56,50,47],
[42,42,56,55,43,45,0,50,45],
[50,51,53,54,45,51,51,0,46],
[50,55,63,58,51,54,56,55,0]])



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
result = np.append(np.array([9, 101, 58, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,47,42,46,57,57,35,59],
[60,0,46,45,39,51,45,58,55],
[54,55,0,46,59,51,57,45,62],
[59,56,55,0,48,63,54,67,60],
[55,62,42,53,0,50,64,53,60],
[44,50,50,38,51,0,50,46,54],
[44,56,44,47,37,51,0,43,53],
[66,43,56,34,48,55,58,0,60],
[42,46,39,41,41,47,48,41,0]])



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
result = np.append(np.array([9, 101, 59, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,58,58,55,57,45,45,56],
[54,0,42,60,49,50,51,53,46],
[43,59,0,63,60,52,51,48,49],
[43,41,38,0,47,40,38,43,41],
[46,52,41,54,0,45,49,46,44],
[44,51,49,61,56,0,50,49,47],
[56,50,50,63,52,51,0,49,48],
[56,48,53,58,55,52,52,0,49],
[45,55,52,60,57,54,53,52,0]])



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
result = np.append(np.array([9, 101, 60, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,68,21,30,55,65,43,64,31],
[33,0,28,30,29,54,44,43,44],
[80,73,0,56,71,67,64,68,47],
[71,71,45,0,57,62,60,59,62],
[46,72,30,44,0,61,45,55,51],
[36,47,34,39,40,0,38,47,38],
[58,57,37,41,56,63,0,64,36],
[37,58,33,42,46,54,37,0,40],
[70,57,54,39,50,63,65,61,0]])



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
result = np.append(np.array([9, 101, 61, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,68,57,50,69,75,63,56,59],
[33,0,46,37,39,52,35,27,43],
[44,55,0,50,65,61,45,43,41],
[51,64,51,0,63,54,50,43,46],
[32,62,36,38,0,48,44,35,42],
[26,49,40,47,53,0,42,31,42],
[38,66,56,51,57,59,0,42,55],
[45,74,58,58,66,70,59,0,55],
[42,58,60,55,59,59,46,46,0]])



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
result = np.append(np.array([9, 101, 62, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,44,48,56,56,57,45,49],
[56,0,51,55,51,55,51,50,51],
[57,50,0,55,56,62,57,65,60],
[53,46,46,0,54,55,60,48,53],
[45,50,45,47,0,52,47,45,48],
[45,46,39,46,49,0,55,46,47],
[44,50,44,41,54,46,0,48,47],
[56,51,36,53,56,55,53,0,55],
[52,50,41,48,53,54,54,46,0]])



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
result = np.append(np.array([9, 101, 63, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,53,30,41,36,40,35,42],
[55,0,68,41,47,32,46,40,53],
[48,33,0,36,38,37,42,41,39],
[71,60,65,0,57,48,58,55,62],
[60,54,63,44,0,47,53,43,45],
[65,69,64,53,54,0,64,50,67],
[61,55,59,43,48,37,0,47,43],
[66,61,60,46,58,51,54,0,51],
[59,48,62,39,56,34,58,50,0]])



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
result = np.append(np.array([9, 101, 64, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,58,39,40,50,47,50,49],
[46,0,48,53,40,46,46,52,49],
[43,53,0,46,51,46,48,51,53],
[62,48,55,0,49,49,51,56,57],
[61,61,50,52,0,52,55,62,47],
[51,55,55,52,49,0,55,65,50],
[54,55,53,50,46,46,0,49,52],
[51,49,50,45,39,36,52,0,53],
[52,52,48,44,54,51,49,48,0]])



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
result = np.append(np.array([9, 101, 65, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,41,45,40,47,38,46,47],
[56,0,46,59,44,50,50,55,45],
[60,55,0,48,50,53,53,44,53],
[56,42,53,0,54,58,48,55,57],
[61,57,51,47,0,71,43,55,55],
[54,51,48,43,30,0,42,44,50],
[63,51,48,53,58,59,0,55,44],
[55,46,57,46,46,57,46,0,46],
[54,56,48,44,46,51,57,55,0]])



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
result = np.append(np.array([9, 101, 66, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,39,34,31,39,34,48,23],
[74,0,62,67,59,56,60,64,47],
[62,39,0,33,55,34,46,62,37],
[67,34,68,0,51,53,44,56,48],
[70,42,46,50,0,61,61,62,29],
[62,45,67,48,40,0,53,72,52],
[67,41,55,57,40,48,0,56,41],
[53,37,39,45,39,29,45,0,37],
[78,54,64,53,72,49,60,64,0]])



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
result = np.append(np.array([9, 101, 67, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,39,42,33,44,53,34,41],
[63,0,44,45,41,47,53,52,55],
[62,57,0,61,51,39,59,65,55],
[59,56,40,0,45,37,53,41,47],
[68,60,50,56,0,53,58,57,56],
[57,54,62,64,48,0,66,50,54],
[48,48,42,48,43,35,0,42,52],
[67,49,36,60,44,51,59,0,49],
[60,46,46,54,45,47,49,52,0]])



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
result = np.append(np.array([9, 101, 68, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,60,57,48,61,56,57,52],
[43,0,53,53,49,52,40,38,47],
[41,48,0,44,38,50,41,48,48],
[44,48,57,0,49,55,46,54,48],
[53,52,63,52,0,60,50,56,53],
[40,49,51,46,41,0,44,46,46],
[45,61,60,55,51,57,0,47,46],
[44,63,53,47,45,55,54,0,49],
[49,54,53,53,48,55,55,52,0]])



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
result = np.append(np.array([9, 101, 69, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,45,27,38,55,59,44,43],
[51,0,52,34,57,39,62,52,43],
[56,49,0,35,28,36,67,42,67],
[74,67,66,0,78,46,95,64,67],
[63,44,73,23,0,42,71,27,62],
[46,62,65,55,59,0,73,73,62],
[42,39,34,6,30,28,0,11,38],
[57,49,59,37,74,28,90,0,50],
[58,58,34,34,39,39,63,51,0]])



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
result = np.append(np.array([9, 101, 70, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,44,64,47,62,49,46,49],
[49,0,47,52,47,48,43,46,49],
[57,54,0,65,49,58,55,45,57],
[37,49,36,0,37,46,43,39,41],
[54,54,52,64,0,58,49,50,49],
[39,53,43,55,43,0,38,43,43],
[52,58,46,58,52,63,0,55,52],
[55,55,56,62,51,58,46,0,56],
[52,52,44,60,52,58,49,45,0]])



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
result = np.append(np.array([9, 101, 71, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,48,51,53,48,54,50,52],
[55,0,52,57,53,52,52,58,46],
[53,49,0,53,49,49,52,58,49],
[50,44,48,0,50,43,50,57,47],
[48,48,52,51,0,50,49,56,48],
[53,49,52,58,51,0,51,53,44],
[47,49,49,51,52,50,0,56,45],
[51,43,43,44,45,48,45,0,42],
[49,55,52,54,53,57,56,59,0]])



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
result = np.append(np.array([9, 101, 72, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,51,59,56,48,54,54,59],
[49,0,45,55,48,51,49,52,54],
[50,56,0,57,56,50,51,55,56],
[42,46,44,0,44,36,44,47,51],
[45,53,45,57,0,43,48,51,61],
[53,50,51,65,58,0,55,60,55],
[47,52,50,57,53,46,0,54,52],
[47,49,46,54,50,41,47,0,48],
[42,47,45,50,40,46,49,53,0]])



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
result = np.append(np.array([9, 101, 73, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,49,49,54,57,53,53,56],
[46,0,51,48,47,52,52,49,49],
[52,50,0,48,56,50,52,54,47],
[52,53,53,0,53,50,50,60,48],
[47,54,45,48,0,46,50,52,49],
[44,49,51,51,55,0,49,57,46],
[48,49,49,51,51,52,0,51,48],
[48,52,47,41,49,44,50,0,46],
[45,52,54,53,52,55,53,55,0]])



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
result = np.append(np.array([9, 101, 74, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,56,53,55,50,57,52,58],
[52,0,54,53,59,49,54,51,57],
[45,47,0,50,47,43,46,53,56],
[48,48,51,0,50,46,52,45,49],
[46,42,54,51,0,45,46,38,52],
[51,52,58,55,56,0,51,50,52],
[44,47,55,49,55,50,0,54,53],
[49,50,48,56,63,51,47,0,58],
[43,44,45,52,49,49,48,43,0]])



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
result = np.append(np.array([9, 101, 75, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,40,47,48,51,47,44,51],
[51,0,52,49,50,53,46,52,46],
[61,49,0,48,53,46,47,48,50],
[54,52,53,0,50,53,47,56,52],
[53,51,48,51,0,56,45,51,50],
[50,48,55,48,45,0,46,55,49],
[54,55,54,54,56,55,0,53,48],
[57,49,53,45,50,46,48,0,47],
[50,55,51,49,51,52,53,54,0]])



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
result = np.append(np.array([9, 101, 76, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,53,53,56,53,50,52,52],
[47,0,56,55,48,53,44,49,55],
[48,45,0,48,44,54,43,52,48],
[48,46,53,0,35,45,43,50,51],
[45,53,57,66,0,54,62,56,56],
[48,48,47,56,47,0,55,53,48],
[51,57,58,58,39,46,0,58,57],
[49,52,49,51,45,48,43,0,48],
[49,46,53,50,45,53,44,53,0]])



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
result = np.append(np.array([9, 101, 77, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,43,47,45,45,46,33,45],
[55,0,51,52,58,46,63,56,49],
[58,50,0,46,57,42,48,55,40],
[54,49,55,0,50,42,63,44,55],
[56,43,44,51,0,51,62,43,54],
[56,55,59,59,50,0,56,44,49],
[55,38,53,38,39,45,0,39,45],
[68,45,46,57,58,57,62,0,54],
[56,52,61,46,47,52,56,47,0]])



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
result = np.append(np.array([9, 101, 78, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,21,41,35,42,46,36,31],
[61,0,38,63,57,57,55,49,60],
[80,63,0,59,55,58,53,56,46],
[60,38,42,0,46,51,56,56,53],
[66,44,46,55,0,54,59,55,64],
[59,44,43,50,47,0,48,42,48],
[55,46,48,45,42,53,0,40,48],
[65,52,45,45,46,59,61,0,52],
[70,41,55,48,37,53,53,49,0]])



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
result = np.append(np.array([9, 101, 79, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,61,45,42,63,64,46,34],
[43,0,50,34,39,57,46,42,34],
[40,51,0,49,45,50,50,46,40],
[56,67,52,0,40,62,61,53,38],
[59,62,56,61,0,49,61,53,55],
[38,44,51,39,52,0,50,42,39],
[37,55,51,40,40,51,0,32,35],
[55,59,55,48,48,59,69,0,47],
[67,67,61,63,46,62,66,54,0]])



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
result = np.append(np.array([9, 101, 80, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,63,66,61,57,50,57,58,64],
[38,0,53,58,48,52,51,50,53],
[35,48,0,48,32,41,48,43,41],
[40,43,53,0,35,47,44,46,55],
[44,53,69,66,0,55,51,54,59],
[51,49,60,54,46,0,46,64,68],
[44,50,53,57,50,55,0,53,57],
[43,51,58,55,47,37,48,0,49],
[37,48,60,46,42,33,44,52,0]])



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
result = np.append(np.array([9, 101, 81, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,66,65,56,55,44,53,52,70],
[35,0,58,56,47,41,61,44,53],
[36,43,0,52,54,48,48,49,52],
[45,45,49,0,62,49,57,47,68],
[46,54,47,39,0,50,41,45,53],
[57,60,53,52,51,0,58,43,57],
[48,40,53,44,60,43,0,54,60],
[49,57,52,54,56,58,47,0,64],
[31,48,49,33,48,44,41,37,0]])



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
result = np.append(np.array([9, 101, 82, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,43,43,45,50,48,46,47],
[56,0,47,50,53,56,52,53,53],
[58,54,0,52,58,49,53,50,54],
[58,51,49,0,46,51,46,55,54],
[56,48,43,55,0,51,47,54,51],
[51,45,52,50,50,0,53,50,57],
[53,49,48,55,54,48,0,51,43],
[55,48,51,46,47,51,50,0,52],
[54,48,47,47,50,44,58,49,0]])



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
result = np.append(np.array([9, 101, 83, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,66,70,58,58,66,57,42,54],
[35,0,30,33,41,30,26,30,38],
[31,71,0,63,63,50,16,26,17],
[43,68,38,0,42,42,34,42,46],
[43,60,38,59,0,63,34,55,46],
[35,71,51,59,38,0,37,21,29],
[44,75,85,67,67,64,0,40,69],
[59,71,75,59,46,80,61,0,50],
[47,63,84,55,55,72,32,51,0]])



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
result = np.append(np.array([9, 101, 84, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,51,42,34,45,70,36,52],
[57,0,48,56,54,55,70,52,64],
[50,53,0,45,44,57,68,45,54],
[59,45,56,0,46,58,77,51,47],
[67,47,57,55,0,71,75,55,63],
[56,46,44,43,30,0,76,43,50],
[31,31,33,24,26,25,0,27,45],
[65,49,56,50,46,58,74,0,56],
[49,37,47,54,38,51,56,45,0]])



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
result = np.append(np.array([9, 101, 85, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,48,45,47,55,56,57,45],
[57,0,47,54,47,56,52,52,50],
[53,54,0,52,49,57,60,53,51],
[56,47,49,0,54,64,53,53,58],
[54,54,52,47,0,60,51,52,51],
[46,45,44,37,41,0,48,49,50],
[45,49,41,48,50,53,0,55,47],
[44,49,48,48,49,52,46,0,53],
[56,51,50,43,50,51,54,48,0]])



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
result = np.append(np.array([9, 101, 86, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,37,35,58,54,43,47,34,35],
[64,0,52,57,46,33,31,28,27],
[66,49,0,49,50,43,34,35,31],
[43,44,52,0,57,48,54,45,43],
[47,55,51,44,0,60,45,32,31],
[58,68,58,53,41,0,40,35,37],
[54,70,67,47,56,61,0,54,31],
[67,73,66,56,69,66,47,0,51],
[66,74,70,58,70,64,70,50,0]])



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
result = np.append(np.array([9, 101, 87, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,63,54,60,54,44,52,43],
[41,0,47,45,48,43,40,49,44],
[38,54,0,49,52,44,57,44,51],
[47,56,52,0,53,52,56,54,49],
[41,53,49,48,0,52,62,50,48],
[47,58,57,49,49,0,42,45,53],
[57,61,44,45,39,59,0,49,47],
[49,52,57,47,51,56,52,0,52],
[58,57,50,52,53,48,54,49,0]])



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
result = np.append(np.array([9, 101, 88, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,51,49,47,53,56,55,53],
[46,0,50,54,44,51,57,49,45],
[50,51,0,42,42,46,46,52,50],
[52,47,59,0,57,51,51,57,50],
[54,57,59,44,0,48,47,50,49],
[48,50,55,50,53,0,56,57,51],
[45,44,55,50,54,45,0,56,47],
[46,52,49,44,51,44,45,0,48],
[48,56,51,51,52,50,54,53,0]])



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
result = np.append(np.array([9, 101, 89, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,47,48,53,50,54,55,44],
[52,0,48,59,60,43,61,58,55],
[54,53,0,61,48,47,53,42,48],
[53,42,40,0,40,39,47,41,44],
[48,41,53,61,0,35,51,48,51],
[51,58,54,62,66,0,54,54,49],
[47,40,48,54,50,47,0,40,38],
[46,43,59,60,53,47,61,0,46],
[57,46,53,57,50,52,63,55,0]])



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
result = np.append(np.array([9, 101, 90, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,70,48,64,60,63,33,54],
[70,0,66,45,74,80,80,54,60],
[31,35,0,51,34,71,57,35,56],
[53,56,50,0,45,59,49,46,56],
[37,27,67,56,0,63,73,46,51],
[41,21,30,42,38,0,26,40,40],
[38,21,44,52,28,75,0,37,49],
[68,47,66,55,55,61,64,0,51],
[47,41,45,45,50,61,52,50,0]])



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
result = np.append(np.array([9, 101, 91, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,51,49,51,55,56,53,56],
[50,0,56,53,50,55,55,46,52],
[50,45,0,44,42,44,48,41,50],
[52,48,57,0,45,57,55,49,51],
[50,51,59,56,0,58,49,52,53],
[46,46,57,44,43,0,49,48,49],
[45,46,53,46,52,52,0,44,47],
[48,55,60,52,49,53,57,0,55],
[45,49,51,50,48,52,54,46,0]])



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
result = np.append(np.array([9, 101, 92, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,41,46,45,36,47,43,41],
[59,0,48,48,71,52,57,55,51],
[60,53,0,48,69,57,62,76,57],
[55,53,53,0,55,43,65,65,62],
[56,30,32,46,0,42,55,60,46],
[65,49,44,58,59,0,59,62,58],
[54,44,39,36,46,42,0,39,40],
[58,46,25,36,41,39,62,0,32],
[60,50,44,39,55,43,61,69,0]])



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
result = np.append(np.array([9, 101, 93, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,44,52,45,53,52,54,47],
[54,0,52,48,51,55,51,52,48],
[57,49,0,55,45,52,48,46,48],
[49,53,46,0,47,54,54,51,43],
[56,50,56,54,0,55,47,50,53],
[48,46,49,47,46,0,50,48,51],
[49,50,53,47,54,51,0,54,47],
[47,49,55,50,51,53,47,0,49],
[54,53,53,58,48,50,54,52,0]])



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
result = np.append(np.array([9, 101, 94, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,75,53,50,64,44,51,51,52],
[26,0,41,17,17,24,24,18,24],
[48,60,0,12,23,35,7,7,14],
[51,84,89,0,35,58,15,15,15],
[37,84,78,66,0,56,50,49,27],
[57,77,66,43,45,0,49,49,49],
[50,77,94,86,51,52,0,43,50],
[50,83,94,86,52,52,58,0,34],
[49,77,87,86,74,52,51,67,0]])



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
result = np.append(np.array([9, 101, 95, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,53,65,59,55,52,63,49],
[50,0,48,53,52,53,48,59,53],
[48,53,0,57,56,49,48,57,49],
[36,48,44,0,46,42,47,57,48],
[42,49,45,55,0,46,45,55,50],
[46,48,52,59,55,0,47,53,52],
[49,53,53,54,56,54,0,56,57],
[38,42,44,44,46,48,45,0,47],
[52,48,52,53,51,49,44,54,0]])



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
result = np.append(np.array([9, 101, 96, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,63,52,54,54,51,56,60],
[57,0,63,49,64,60,57,60,56],
[38,38,0,59,54,40,47,46,50],
[49,52,42,0,53,44,45,45,51],
[47,37,47,48,0,43,44,44,43],
[47,41,61,57,58,0,51,52,53],
[50,44,54,56,57,50,0,47,49],
[45,41,55,56,57,49,54,0,52],
[41,45,51,50,58,48,52,49,0]])



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
result = np.append(np.array([9, 101, 97, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,51,49,49,49,52,60,51],
[49,0,51,45,54,50,67,58,50],
[50,50,0,50,50,52,50,51,46],
[52,56,51,0,53,49,53,61,44],
[52,47,51,48,0,54,48,56,51],
[52,51,49,52,47,0,56,58,45],
[49,34,51,48,53,45,0,55,48],
[41,43,50,40,45,43,46,0,49],
[50,51,55,57,50,56,53,52,0]])



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
result = np.append(np.array([9, 101, 98, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,54,52,55,55,55,53,53],
[53,0,59,52,55,52,59,48,54],
[47,42,0,44,42,53,49,43,46],
[49,49,57,0,52,56,55,45,52],
[46,46,59,49,0,56,51,51,45],
[46,49,48,45,45,0,53,45,46],
[46,42,52,46,50,48,0,44,44],
[48,53,58,56,50,56,57,0,49],
[48,47,55,49,56,55,57,52,0]])



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
result = np.append(np.array([9, 101, 99, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,52,44,69,73,45,66,57],
[49,0,51,24,62,72,58,64,54],
[49,50,0,44,75,52,25,51,64],
[57,77,57,0,67,60,62,50,67],
[32,39,26,34,0,50,27,53,47],
[28,29,49,41,51,0,39,53,45],
[56,43,76,39,74,62,0,59,61],
[35,37,50,51,48,48,42,0,44],
[44,47,37,34,54,56,40,57,0]])



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
result = np.append(np.array([9, 101, 100, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,42,57,44,55,49,42,54],
[41,0,50,57,39,54,43,46,55],
[59,51,0,49,49,50,54,47,49],
[44,44,52,0,39,40,36,38,51],
[57,62,52,62,0,57,57,48,53],
[46,47,51,61,44,0,43,41,62],
[52,58,47,65,44,58,0,53,56],
[59,55,54,63,53,60,48,0,55],
[47,46,52,50,48,39,45,46,0]])



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
result = np.append(np.array([9, 101, 101, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,48,40,43,59,43,56,48],
[51,0,52,48,51,63,69,41,60],
[53,49,0,65,40,64,67,47,63],
[61,53,36,0,42,56,55,51,58],
[58,50,61,59,0,74,68,69,64],
[42,38,37,45,27,0,50,43,39],
[58,32,34,46,33,51,0,40,49],
[45,60,54,50,32,58,61,0,51],
[53,41,38,43,37,62,52,50,0]])



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
result = np.append(np.array([9, 101, 102, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,65,48,57,50,52,51,63],
[49,0,64,47,42,42,48,40,52],
[36,37,0,50,39,38,42,40,44],
[53,54,51,0,50,46,46,46,54],
[44,59,62,51,0,42,47,44,57],
[51,59,63,55,59,0,50,56,51],
[49,53,59,55,54,51,0,41,59],
[50,61,61,55,57,45,60,0,58],
[38,49,57,47,44,50,42,43,0]])



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
result = np.append(np.array([9, 101, 103, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,39,49,63,52,65,32,45],
[57,0,71,37,46,49,69,40,44],
[62,30,0,28,69,67,80,61,51],
[52,64,73,0,53,53,73,47,49],
[38,55,32,48,0,60,63,24,44],
[49,52,34,48,41,0,76,32,50],
[36,32,21,28,38,25,0,48,34],
[69,61,40,54,77,69,53,0,50],
[56,57,50,52,57,51,67,51,0]])



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
result = np.append(np.array([9, 101, 104, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,46,48,46,42,49,43,49],
[52,0,53,49,52,56,55,53,48],
[55,48,0,47,53,54,58,47,58],
[53,52,54,0,44,49,54,53,56],
[55,49,48,57,0,46,51,53,53],
[59,45,47,52,55,0,50,48,51],
[52,46,43,47,50,51,0,44,46],
[58,48,54,48,48,53,57,0,52],
[52,53,43,45,48,50,55,49,0]])



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
result = np.append(np.array([9, 101, 105, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,57,45,59,43,43,50,50],
[42,0,48,41,50,23,37,37,40],
[44,53,0,54,53,33,40,44,42],
[56,60,47,0,60,40,48,50,41],
[42,51,48,41,0,28,25,34,43],
[58,78,68,61,73,0,55,46,62],
[58,64,61,53,76,46,0,57,48],
[51,64,57,51,67,55,44,0,57],
[51,61,59,60,58,39,53,44,0]])



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
result = np.append(np.array([9, 101, 106, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,44,35,45,43,46,34,45],
[65,0,46,81,72,61,74,53,35],
[57,55,0,56,64,43,48,47,53],
[66,20,45,0,58,62,64,38,31],
[56,29,37,43,0,34,33,45,36],
[58,40,58,39,67,0,62,62,37],
[55,27,53,37,68,39,0,39,35],
[67,48,54,63,56,39,62,0,49],
[56,66,48,70,65,64,66,52,0]])



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
result = np.append(np.array([9, 101, 107, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,39,39,49,68,53,76,52],
[48,0,55,52,48,75,52,61,66],
[62,46,0,38,38,61,46,73,56],
[62,49,63,0,52,69,56,64,64],
[52,53,63,49,0,62,52,71,63],
[33,26,40,32,39,0,26,53,39],
[48,49,55,45,49,75,0,62,59],
[25,40,28,37,30,48,39,0,50],
[49,35,45,37,38,62,42,51,0]])



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
result = np.append(np.array([9, 101, 108, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,27,32,18,13,38,14,22],
[80,0,72,40,51,75,45,66,50],
[74,29,0,41,36,26,29,33,48],
[69,61,60,0,44,53,41,58,58],
[83,50,65,57,0,39,59,63,56],
[88,26,75,48,62,0,54,61,49],
[63,56,72,60,42,47,0,49,52],
[87,35,68,43,38,40,52,0,34],
[79,51,53,43,45,52,49,67,0]])



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
result = np.append(np.array([9, 101, 109, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,51,50,37,46,48,43,55],
[55,0,53,48,44,55,44,44,48],
[50,48,0,46,50,47,50,42,41],
[51,53,55,0,51,60,39,51,60],
[64,57,51,50,0,54,48,45,53],
[55,46,54,41,47,0,51,52,54],
[53,57,51,62,53,50,0,49,58],
[58,57,59,50,56,49,52,0,54],
[46,53,60,41,48,47,43,47,0]])



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
result = np.append(np.array([9, 101, 110, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,51,52,53,49,47,51,52],
[47,0,50,51,47,52,49,51,50],
[50,51,0,51,50,58,54,48,57],
[49,50,50,0,52,49,48,57,55],
[48,54,51,49,0,58,52,48,56],
[52,49,43,52,43,0,47,51,54],
[54,52,47,53,49,54,0,52,47],
[50,50,53,44,53,50,49,0,51],
[49,51,44,46,45,47,54,50,0]])



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
result = np.append(np.array([9, 101, 111, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,37,28,38,35,42,34,33],
[49,0,39,34,43,32,53,62,48],
[64,62,0,51,46,47,70,46,51],
[73,67,50,0,50,47,55,57,49],
[63,58,55,51,0,43,64,45,67],
[66,69,54,54,58,0,56,65,47],
[59,48,31,46,37,45,0,52,45],
[67,39,55,44,56,36,49,0,42],
[68,53,50,52,34,54,56,59,0]])



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
result = np.append(np.array([9, 101, 112, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,48,64,54,70,68,61,63],
[42,0,33,43,52,55,64,50,48],
[53,68,0,60,56,57,67,48,69],
[37,58,41,0,47,55,54,59,60],
[47,49,45,54,0,64,53,54,69],
[31,46,44,46,37,0,51,48,55],
[33,37,34,47,48,50,0,57,57],
[40,51,53,42,47,53,44,0,63],
[38,53,32,41,32,46,44,38,0]])



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
result = np.append(np.array([9, 101, 113, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,51,58,52,46,59,55,61],
[52,0,54,57,45,56,50,41,53],
[50,47,0,51,51,46,56,46,51],
[43,44,50,0,56,48,46,50,55],
[49,56,50,45,0,48,53,50,55],
[55,45,55,53,53,0,61,51,54],
[42,51,45,55,48,40,0,51,54],
[46,60,55,51,51,50,50,0,58],
[40,48,50,46,46,47,47,43,0]])



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
result = np.append(np.array([9, 101, 114, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,43,45,34,46,44,54,46],
[48,0,50,45,37,38,41,48,47],
[58,51,0,48,39,42,48,50,54],
[56,56,53,0,53,43,44,55,55],
[67,64,62,48,0,52,56,63,59],
[55,63,59,58,49,0,54,65,58],
[57,60,53,57,45,47,0,53,58],
[47,53,51,46,38,36,48,0,48],
[55,54,47,46,42,43,43,53,0]])



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
result = np.append(np.array([9, 101, 115, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,47,37,46,50,39,43,50],
[56,0,47,51,69,54,53,51,67],
[54,54,0,45,57,48,51,47,52],
[64,50,56,0,47,53,47,56,51],
[55,32,44,54,0,48,45,46,56],
[51,47,53,48,53,0,54,53,53],
[62,48,50,54,56,47,0,59,54],
[58,50,54,45,55,48,42,0,46],
[51,34,49,50,45,48,47,55,0]])



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
result = np.append(np.array([9, 101, 116, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,50,53,65,59,56,59,54],
[45,0,51,47,51,57,49,44,43],
[51,50,0,51,55,52,48,49,51],
[48,54,50,0,51,58,50,50,45],
[36,50,46,50,0,51,43,37,48],
[42,44,49,43,50,0,44,42,47],
[45,52,53,51,58,57,0,44,50],
[42,57,52,51,64,59,57,0,54],
[47,58,50,56,53,54,51,47,0]])



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
result = np.append(np.array([9, 101, 117, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,44,56,42,62,47,48,51],
[57,0,49,56,35,56,43,49,40],
[57,52,0,47,37,58,47,60,46],
[45,45,54,0,44,58,52,48,55],
[59,66,64,57,0,68,47,57,57],
[39,45,43,43,33,0,46,57,44],
[54,58,54,49,54,55,0,50,41],
[53,52,41,53,44,44,51,0,46],
[50,61,55,46,44,57,60,55,0]])



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
result = np.append(np.array([9, 101, 118, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,55,51,46,57,47,52,55],
[48,0,56,58,52,58,52,51,56],
[46,45,0,45,41,44,53,47,39],
[50,43,56,0,53,58,48,47,46],
[55,49,60,48,0,56,56,54,56],
[44,43,57,43,45,0,47,43,49],
[54,49,48,53,45,54,0,51,57],
[49,50,54,54,47,58,50,0,54],
[46,45,62,55,45,52,44,47,0]])



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
result = np.append(np.array([9, 101, 119, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,40,42,51,50,51,42,47],
[55,0,51,55,57,48,62,48,55],
[61,50,0,53,63,53,50,54,64],
[59,46,48,0,55,46,55,49,61],
[50,44,38,46,0,44,47,38,57],
[51,53,48,55,57,0,57,49,58],
[50,39,51,46,54,44,0,43,57],
[59,53,47,52,63,52,58,0,62],
[54,46,37,40,44,43,44,39,0]])



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
result = np.append(np.array([9, 101, 120, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,48,54,51,43,49,52,45],
[50,0,56,50,49,47,41,43,41],
[53,45,0,54,53,50,45,46,49],
[47,51,47,0,52,46,51,49,50],
[50,52,48,49,0,39,39,39,45],
[58,54,51,55,62,0,54,41,53],
[52,60,56,50,62,47,0,44,55],
[49,58,55,52,62,60,57,0,50],
[56,60,52,51,56,48,46,51,0]])



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
result = np.append(np.array([9, 101, 121, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,48,52,52,49,50,48,58],
[41,0,48,42,47,37,45,42,46],
[53,53,0,42,59,52,48,52,56],
[49,59,59,0,52,47,56,47,55],
[49,54,42,49,0,51,50,49,57],
[52,64,49,54,50,0,53,55,57],
[51,56,53,45,51,48,0,51,51],
[53,59,49,54,52,46,50,0,58],
[43,55,45,46,44,44,50,43,0]])



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
result = np.append(np.array([9, 101, 122, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,55,58,52,51,54,57,57],
[59,0,44,55,56,49,60,58,51],
[46,57,0,49,46,49,64,51,42],
[43,46,52,0,49,54,63,51,46],
[49,45,55,52,0,51,54,45,45],
[50,52,52,47,50,0,65,53,47],
[47,41,37,38,47,36,0,45,35],
[44,43,50,50,56,48,56,0,41],
[44,50,59,55,56,54,66,60,0]])



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
result = np.append(np.array([9, 101, 123, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,69,101,56,56,69,24,56],
[77,0,101,101,56,32,101,56,101],
[32,0,0,101,56,32,69,24,56],
[0,0,0,0,56,32,24,24,32],
[45,45,45,45,0,77,45,45,45],
[45,69,69,69,24,0,69,69,69],
[32,0,32,77,56,32,0,56,32],
[77,45,77,77,56,32,45,0,77],
[45,0,45,69,56,32,69,24,0]])



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
result = np.append(np.array([9, 101, 124, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,43,43,43,40,37,43,44],
[53,0,41,44,46,48,43,42,38],
[58,60,0,53,53,46,50,48,53],
[58,57,48,0,53,55,52,50,46],
[58,55,48,48,0,53,49,44,46],
[61,53,55,46,48,0,52,43,50],
[64,58,51,49,52,49,0,51,50],
[58,59,53,51,57,58,50,0,54],
[57,63,48,55,55,51,51,47,0]])



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
result = np.append(np.array([9, 101, 125, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,46,45,46,40,47,38,43],
[57,0,52,47,48,41,56,46,46],
[55,49,0,47,47,44,50,45,56],
[56,54,54,0,54,56,56,47,42],
[55,53,54,47,0,46,48,43,48],
[61,60,57,45,55,0,62,54,48],
[54,45,51,45,53,39,0,41,50],
[63,55,56,54,58,47,60,0,48],
[58,55,45,59,53,53,51,53,0]])



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
result = np.append(np.array([9, 101, 126, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,61,64,57,58,47,49,60],
[53,0,63,71,62,55,55,51,50],
[40,38,0,67,40,39,42,39,34],
[37,30,34,0,33,29,46,40,34],
[44,39,61,68,0,44,45,42,42],
[43,46,62,72,57,0,56,52,46],
[54,46,59,55,56,45,0,63,47],
[52,50,62,61,59,49,38,0,44],
[41,51,67,67,59,55,54,57,0]])



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
result = np.append(np.array([9, 101, 127, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,101,68,0,101,37,31,101,31],
[0,0,31,0,31,0,31,31,31],
[33,70,0,33,70,70,33,101,64],
[101,101,68,0,101,70,64,101,31],
[0,70,31,0,0,37,31,31,31],
[64,101,31,31,64,0,64,64,31],
[70,70,68,37,70,37,0,101,31],
[0,70,0,0,70,37,0,0,0],
[70,70,37,70,70,70,70,101,0]])



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
result = np.append(np.array([9, 101, 128, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,70,75,43,53,82,78,63,51],
[31,0,53,41,49,65,56,53,40],
[26,48,0,41,38,52,55,47,36],
[58,60,60,0,54,70,49,29,51],
[48,52,63,47,0,66,67,54,61],
[19,36,49,31,35,0,52,30,55],
[23,45,46,52,34,49,0,54,60],
[38,48,54,72,47,71,47,0,56],
[50,61,65,50,40,46,41,45,0]])



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
result = np.append(np.array([9, 101, 129, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,48,58,54,51,49,50,54],
[48,0,48,53,46,50,51,47,50],
[53,53,0,51,55,52,47,51,62],
[43,48,50,0,49,47,50,49,50],
[47,55,46,52,0,48,49,40,50],
[50,51,49,54,53,0,51,46,55],
[52,50,54,51,52,50,0,53,55],
[51,54,50,52,61,55,48,0,59],
[47,51,39,51,51,46,46,42,0]])



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
result = np.append(np.array([9, 101, 130, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,41,45,48,51,39,46,44],
[53,0,44,47,45,56,43,35,49],
[60,57,0,50,57,57,56,49,56],
[56,54,51,0,58,58,39,53,53],
[53,56,44,43,0,58,48,45,55],
[50,45,44,43,43,0,39,47,50],
[62,58,45,62,53,62,0,67,65],
[55,66,52,48,56,54,34,0,46],
[57,52,45,48,46,51,36,55,0]])



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
result = np.append(np.array([9, 101, 131, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,42,46,53,45,42,62,43],
[62,0,60,57,50,60,53,70,40],
[59,41,0,52,51,59,45,59,45],
[55,44,49,0,58,61,48,64,52],
[48,51,50,43,0,51,43,58,50],
[56,41,42,40,50,0,39,58,40],
[59,48,56,53,58,62,0,66,46],
[39,31,42,37,43,43,35,0,32],
[58,61,56,49,51,61,55,69,0]])



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
result = np.append(np.array([9, 101, 132, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,51,56,47,42,56,51,51],
[54,0,56,45,46,48,53,46,52],
[50,45,0,51,54,47,57,54,49],
[45,56,50,0,50,50,65,55,50],
[54,55,47,51,0,52,58,52,53],
[59,53,54,51,49,0,52,58,62],
[45,48,44,36,43,49,0,50,46],
[50,55,47,46,49,43,51,0,51],
[50,49,52,51,48,39,55,50,0]])



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
result = np.append(np.array([9, 101, 133, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,42,53,52,46,44,54,58],
[56,0,56,61,55,50,52,58,63],
[59,45,0,53,52,51,51,51,61],
[48,40,48,0,51,43,47,43,50],
[49,46,49,50,0,46,53,44,50],
[55,51,50,58,55,0,55,52,61],
[57,49,50,54,48,46,0,52,55],
[47,43,50,58,57,49,49,0,54],
[43,38,40,51,51,40,46,47,0]])



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
result = np.append(np.array([9, 101, 134, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,52,32,55,28,48,40,57],
[48,0,44,40,44,37,65,33,54],
[49,57,0,66,66,53,73,44,83],
[69,61,35,0,56,54,62,52,40],
[46,57,35,45,0,27,42,41,51],
[73,64,48,47,74,0,88,34,72],
[53,36,28,39,59,13,0,43,44],
[61,68,57,49,60,67,58,0,67],
[44,47,18,61,50,29,57,34,0]])



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
result = np.append(np.array([9, 101, 135, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,72,43,52,52,38,57,66,57],
[29,0,37,39,37,47,44,41,44],
[58,64,0,64,51,49,57,61,66],
[49,62,37,0,39,46,59,44,55],
[49,64,50,62,0,52,60,43,64],
[63,54,52,55,49,0,63,60,54],
[44,57,44,42,41,38,0,50,49],
[35,60,40,57,58,41,51,0,44],
[44,57,35,46,37,47,52,57,0]])



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
result = np.append(np.array([9, 101, 136, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,49,55,42,48,41,36,47],
[62,0,54,55,51,51,52,45,55],
[52,47,0,43,44,54,40,51,56],
[46,46,58,0,46,53,43,43,54],
[59,50,57,55,0,58,53,46,54],
[53,50,47,48,43,0,44,41,51],
[60,49,61,58,48,57,0,46,55],
[65,56,50,58,55,60,55,0,64],
[54,46,45,47,47,50,46,37,0]])



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
result = np.append(np.array([9, 101, 137, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,15,78,36,15,20,17,53],
[86,0,58,78,36,95,63,60,81],
[86,43,0,78,27,52,48,39,81],
[23,23,23,0,6,38,26,17,38],
[65,65,74,95,0,74,48,39,101],
[86,6,49,63,27,0,48,39,81],
[81,38,53,75,53,53,0,32,81],
[84,41,62,84,62,62,69,0,101],
[48,20,20,63,0,20,20,0,0]])



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
result = np.append(np.array([9, 101, 138, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,38,46,42,44,43,49,50],
[60,0,41,42,51,53,47,54,56],
[63,60,0,51,40,48,59,41,58],
[55,59,50,0,43,56,67,44,61],
[59,50,61,58,0,51,49,46,46],
[57,48,53,45,50,0,64,34,49],
[58,54,42,34,52,37,0,43,59],
[52,47,60,57,55,67,58,0,60],
[51,45,43,40,55,52,42,41,0]])



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
result = np.append(np.array([9, 101, 139, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,58,55,47,49,56,55,49],
[51,0,50,51,39,46,49,53,53],
[43,51,0,55,46,50,51,54,48],
[46,50,46,0,47,47,53,49,51],
[54,62,55,54,0,58,62,57,48],
[52,55,51,54,43,0,52,53,51],
[45,52,50,48,39,49,0,56,54],
[46,48,47,52,44,48,45,0,56],
[52,48,53,50,53,50,47,45,0]])



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
result = np.append(np.array([9, 101, 140, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,46,64,55,66,71,44,63],
[57,0,57,55,36,48,72,55,38],
[55,44,0,47,55,66,64,46,35],
[37,46,54,0,18,45,52,54,45],
[46,65,46,83,0,54,69,44,63],
[35,53,35,56,47,0,61,36,52],
[30,29,37,49,32,40,0,46,37],
[57,46,55,47,57,65,55,0,62],
[38,63,66,56,38,49,64,39,0]])



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
result = np.append(np.array([9, 101, 141, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,55,35,45,44,46,55,66],
[41,0,47,34,23,37,37,48,56],
[46,54,0,48,37,51,48,48,64],
[66,67,53,0,56,56,50,58,70],
[56,78,64,45,0,45,46,76,71],
[57,64,50,45,56,0,55,63,67],
[55,64,53,51,55,46,0,57,53],
[46,53,53,43,25,38,44,0,64],
[35,45,37,31,30,34,48,37,0]])



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
result = np.append(np.array([9, 101, 142, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,51,55,61,54,59,56,52],
[58,0,46,59,61,54,59,61,48],
[50,55,0,64,59,45,53,57,54],
[46,42,37,0,47,40,45,46,37],
[40,40,42,54,0,49,45,56,47],
[47,47,56,61,52,0,56,62,48],
[42,42,48,56,56,45,0,52,48],
[45,40,44,55,45,39,49,0,41],
[49,53,47,64,54,53,53,60,0]])



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
result = np.append(np.array([9, 101, 143, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,67,52,50,46,55,44,41],
[46,0,58,45,42,27,47,32,44],
[34,43,0,33,42,34,35,29,30],
[49,56,68,0,43,35,50,54,36],
[51,59,59,58,0,61,47,40,44],
[55,74,67,66,40,0,58,60,55],
[46,54,66,51,54,43,0,49,40],
[57,69,72,47,61,41,52,0,46],
[60,57,71,65,57,46,61,55,0]])



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
result = np.append(np.array([9, 101, 144, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,37,51,39,37,45,46,49],
[54,0,39,49,52,52,66,50,51],
[64,62,0,43,53,65,60,66,62],
[50,52,58,0,50,50,75,59,55],
[62,49,48,51,0,64,58,58,62],
[64,49,36,51,37,0,51,40,54],
[56,35,41,26,43,50,0,42,39],
[55,51,35,42,43,61,59,0,62],
[52,50,39,46,39,47,62,39,0]])



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
result = np.append(np.array([9, 101, 145, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,59,65,52,52,69,57,36],
[51,0,43,54,54,43,70,60,32],
[42,58,0,52,53,63,70,55,39],
[36,47,49,0,54,47,76,47,44],
[49,47,48,47,0,53,63,49,39],
[49,58,38,54,48,0,64,57,55],
[32,31,31,25,38,37,0,36,24],
[44,41,46,54,52,44,65,0,39],
[65,69,62,57,62,46,77,62,0]])



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
result = np.append(np.array([9, 101, 146, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,50,50,43,51,38,46,57],
[51,0,47,51,48,51,51,51,58],
[51,54,0,48,39,52,44,52,52],
[51,50,53,0,44,49,40,51,55],
[58,53,62,57,0,57,48,51,56],
[50,50,49,52,44,0,44,42,55],
[63,50,57,61,53,57,0,50,57],
[55,50,49,50,50,59,51,0,53],
[44,43,49,46,45,46,44,48,0]])



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
result = np.append(np.array([9, 101, 147, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,68,64,70,67,60,60,44,59],
[33,0,47,47,43,49,40,34,36],
[37,54,0,55,55,54,45,38,40],
[31,54,46,0,56,56,41,42,41],
[34,58,46,45,0,52,53,57,55],
[41,52,47,45,49,0,45,48,38],
[41,61,56,60,48,56,0,43,53],
[57,67,63,59,44,53,58,0,49],
[42,65,61,60,46,63,48,52,0]])



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
result = np.append(np.array([9, 101, 148, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,59,52,56,50,58,49,55],
[55,0,54,50,61,55,63,53,54],
[42,47,0,47,56,49,62,48,49],
[49,51,54,0,58,56,62,53,47],
[45,40,45,43,0,47,54,47,43],
[51,46,52,45,54,0,60,53,49],
[43,38,39,39,47,41,0,42,36],
[52,48,53,48,54,48,59,0,47],
[46,47,52,54,58,52,65,54,0]])



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
result = np.append(np.array([9, 101, 149, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,60,48,48,47,48,42,41],
[58,0,55,53,50,53,54,62,71],
[41,46,0,49,50,57,40,65,59],
[53,48,52,0,46,54,54,62,49],
[53,51,51,55,0,55,50,50,64],
[54,48,44,47,46,0,46,48,64],
[53,47,61,47,51,55,0,67,55],
[59,39,36,39,51,53,34,0,48],
[60,30,42,52,37,37,46,53,0]])



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
result = np.append(np.array([9, 101, 150, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,60,54,56,64,50,62,52],
[51,0,48,45,49,56,46,59,50],
[41,53,0,49,50,46,40,48,44],
[47,56,52,0,49,52,51,62,55],
[45,52,51,52,0,43,51,54,52],
[37,45,55,49,58,0,50,51,51],
[51,55,61,50,50,51,0,60,50],
[39,42,53,39,47,50,41,0,46],
[49,51,57,46,49,50,51,55,0]])



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
result = np.append(np.array([9, 101, 151, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,40,34,39,37,36,24,37],
[60,0,50,28,59,63,44,41,46],
[61,51,0,33,53,53,49,40,42],
[67,73,68,0,63,64,49,56,55],
[62,42,48,38,0,48,42,50,36],
[64,38,48,37,53,0,46,52,29],
[65,57,52,52,59,55,0,55,48],
[77,60,61,45,51,49,46,0,49],
[64,55,59,46,65,72,53,52,0]])



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
result = np.append(np.array([9, 101, 152, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,58,56,60,44,51,57,62],
[48,0,56,48,47,51,55,53,62],
[43,45,0,49,42,50,50,58,50],
[45,53,52,0,50,47,58,48,64],
[41,54,59,51,0,49,46,50,57],
[57,50,51,54,52,0,65,56,70],
[50,46,51,43,55,36,0,38,60],
[44,48,43,53,51,45,63,0,52],
[39,39,51,37,44,31,41,49,0]])



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
result = np.append(np.array([9, 101, 153, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,43,53,51,58,52,38,47],
[45,0,40,55,51,44,48,36,51],
[58,61,0,62,63,57,60,52,50],
[48,46,39,0,46,44,47,39,40],
[50,50,38,55,0,46,43,39,42],
[43,57,44,57,55,0,51,43,48],
[49,53,41,54,58,50,0,50,47],
[63,65,49,62,62,58,51,0,56],
[54,50,51,61,59,53,54,45,0]])



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
result = np.append(np.array([9, 101, 154, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,51,29,54,75,34,47,58],
[70,0,48,29,70,68,51,42,43],
[50,53,0,36,57,66,37,50,74],
[72,72,65,0,79,87,41,72,53],
[47,31,44,22,0,59,36,39,54],
[26,33,35,14,42,0,22,19,23],
[67,50,64,60,65,79,0,78,74],
[54,59,51,29,62,82,23,0,54],
[43,58,27,48,47,78,27,47,0]])



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
result = np.append(np.array([9, 101, 155, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,50,26,55,56,44,57,53],
[45,0,33,36,61,45,30,38,49],
[51,68,0,47,58,58,55,55,64],
[75,65,54,0,64,50,45,57,57],
[46,40,43,37,0,47,43,36,47],
[45,56,43,51,54,0,47,30,55],
[57,71,46,56,58,54,0,55,56],
[44,63,46,44,65,71,46,0,57],
[48,52,37,44,54,46,45,44,0]])



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
result = np.append(np.array([9, 101, 156, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,55,58,62,51,55,51,38],
[51,0,53,65,64,55,46,61,57],
[46,48,0,68,61,53,41,51,33],
[43,36,33,0,53,33,39,53,27],
[39,37,40,48,0,39,41,50,33],
[50,46,48,68,62,0,41,59,35],
[46,55,60,62,60,60,0,57,43],
[50,40,50,48,51,42,44,0,45],
[63,44,68,74,68,66,58,56,0]])



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
result = np.append(np.array([9, 101, 157, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,59,52,42,47,61,51,47],
[55,0,63,64,49,48,60,56,52],
[42,38,0,51,50,42,42,45,39],
[49,37,50,0,34,34,46,51,42],
[59,52,51,67,0,45,46,53,48],
[54,53,59,67,56,0,58,55,49],
[40,41,59,55,55,43,0,46,40],
[50,45,56,50,48,46,55,0,42],
[54,49,62,59,53,52,61,59,0]])



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
result = np.append(np.array([9, 101, 158, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,55,61,52,76,45,59,62],
[51,0,48,56,55,73,55,53,59],
[46,53,0,55,50,70,62,61,65],
[40,45,46,0,68,55,60,56,44],
[49,46,51,33,0,63,47,46,53],
[25,28,31,46,38,0,33,24,43],
[56,46,39,41,54,68,0,55,55],
[42,48,40,45,55,77,46,0,60],
[39,42,36,57,48,58,46,41,0]])



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
result = np.append(np.array([9, 101, 159, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,63,47,54,39,48,38,47,46],
[38,0,47,56,47,44,41,45,42],
[54,54,0,62,53,65,42,60,44],
[47,45,39,0,41,41,54,39,36],
[62,54,48,60,0,59,58,68,37],
[53,57,36,60,42,0,43,60,27],
[63,60,59,47,43,58,0,64,56],
[54,56,41,62,33,41,37,0,36],
[55,59,57,65,64,74,45,65,0]])



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
result = np.append(np.array([9, 101, 160, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,57,63,42,62,49,57,64],
[58,0,61,51,50,61,51,49,65],
[44,40,0,45,59,54,41,44,46],
[38,50,56,0,53,50,52,35,52],
[59,51,42,48,0,62,51,57,68],
[39,40,47,51,39,0,57,44,44],
[52,50,60,49,50,44,0,24,51],
[44,52,57,66,44,57,77,0,68],
[37,36,55,49,33,57,50,33,0]])



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
result = np.append(np.array([9, 101, 161, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,61,81,44,54,75,70,47],
[49,0,65,75,58,65,64,72,58],
[40,36,0,58,43,57,59,70,57],
[20,26,43,0,43,38,59,47,51],
[57,43,58,58,0,43,56,58,68],
[47,36,44,63,58,0,65,53,49],
[26,37,42,42,45,36,0,62,57],
[31,29,31,54,43,48,39,0,58],
[54,43,44,50,33,52,44,43,0]])



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
result = np.append(np.array([9, 101, 162, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,52,52,54,52,52,50,44],
[54,0,52,65,57,49,44,51,46],
[49,49,0,52,46,42,48,51,39],
[49,36,49,0,48,41,47,46,37],
[47,44,55,53,0,42,47,50,48],
[49,52,59,60,59,0,53,54,52],
[49,57,53,54,54,48,0,50,48],
[51,50,50,55,51,47,51,0,42],
[57,55,62,64,53,49,53,59,0]])



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
result = np.append(np.array([9, 101, 163, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,59,52,59,56,43,54,66],
[47,0,53,49,55,46,45,52,63],
[42,48,0,49,50,47,43,54,60],
[49,52,52,0,55,42,51,49,56],
[42,46,51,46,0,48,44,54,57],
[45,55,54,59,53,0,43,54,60],
[58,56,58,50,57,58,0,52,62],
[47,49,47,52,47,47,49,0,63],
[35,38,41,45,44,41,39,38,0]])



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
result = np.append(np.array([9, 101, 164, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,89,71,60,59,65,29,59],
[42,0,70,49,64,69,64,39,44],
[12,31,0,63,15,53,26,28,28],
[30,52,38,0,38,39,38,46,48],
[41,37,86,63,0,68,58,49,46],
[42,32,48,62,33,0,42,67,50],
[36,37,75,63,43,59,0,38,37],
[72,62,73,55,52,34,63,0,74],
[42,57,73,53,55,51,64,27,0]])



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
result = np.append(np.array([9, 101, 165, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,52,41,44,52,53,50,49],
[65,0,62,59,58,63,48,61,57],
[49,39,0,54,46,49,49,51,48],
[60,42,47,0,42,49,57,50,41],
[57,43,55,59,0,57,46,50,51],
[49,38,52,52,44,0,52,56,49],
[48,53,52,44,55,49,0,50,47],
[51,40,50,51,51,45,51,0,46],
[52,44,53,60,50,52,54,55,0]])



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
result = np.append(np.array([9, 101, 166, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,50,40,71,61,44,38,50],
[54,0,77,46,76,73,76,75,55],
[51,24,0,39,79,60,51,43,23],
[61,55,62,0,82,72,82,53,38],
[30,25,22,19,0,40,51,23,22],
[40,28,41,29,61,0,40,33,18],
[57,25,50,19,50,61,0,56,51],
[63,26,58,48,78,68,45,0,58],
[51,46,78,63,79,83,50,43,0]])



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
result = np.append(np.array([9, 101, 167, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,52,52,52,66,60,57,63],
[55,0,51,45,52,61,59,51,61],
[49,50,0,49,53,56,64,50,56],
[49,56,52,0,47,48,53,47,52],
[49,49,48,54,0,53,51,52,58],
[35,40,45,53,48,0,52,56,53],
[41,42,37,48,50,49,0,54,51],
[44,50,51,54,49,45,47,0,48],
[38,40,45,49,43,48,50,53,0]])



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
result = np.append(np.array([9, 101, 168, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,50,48,52,56,47,45,47],
[53,0,50,47,50,51,51,47,59],
[51,51,0,53,47,54,50,46,48],
[53,54,48,0,47,55,54,52,44],
[49,51,54,54,0,59,49,52,57],
[45,50,47,46,42,0,45,48,38],
[54,50,51,47,52,56,0,55,51],
[56,54,55,49,49,53,46,0,45],
[54,42,53,57,44,63,50,56,0]])



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
result = np.append(np.array([9, 101, 169, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,56,54,54,47,50,54,42],
[51,0,48,56,58,46,55,47,48],
[45,53,0,54,52,46,55,51,45],
[47,45,47,0,48,47,47,49,45],
[47,43,49,53,0,49,45,43,49],
[54,55,55,54,52,0,55,48,46],
[51,46,46,54,56,46,0,44,53],
[47,54,50,52,58,53,57,0,43],
[59,53,56,56,52,55,48,58,0]])



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
result = np.append(np.array([9, 101, 170, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,55,65,57,63,60,49,64],
[52,0,60,52,57,53,66,53,50],
[46,41,0,48,50,54,59,54,56],
[36,49,53,0,44,49,56,45,49],
[44,44,51,57,0,49,64,51,54],
[38,48,47,52,52,0,56,45,63],
[41,35,42,45,37,45,0,48,46],
[52,48,47,56,50,56,53,0,64],
[37,51,45,52,47,38,55,37,0]])



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
result = np.append(np.array([9, 101, 171, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,49,41,48,58,60,43,50],
[56,0,49,49,55,57,61,47,53],
[52,52,0,43,50,55,53,46,48],
[60,52,58,0,56,66,55,48,44],
[53,46,51,45,0,53,62,56,55],
[43,44,46,35,48,0,54,45,43],
[41,40,48,46,39,47,0,47,35],
[58,54,55,53,45,56,54,0,50],
[51,48,53,57,46,58,66,51,0]])



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
result = np.append(np.array([9, 101, 172, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,43,59,38,53,66,64,57],
[54,0,40,53,53,54,68,61,49],
[58,61,0,52,63,43,62,66,63],
[42,48,49,0,66,58,64,68,66],
[63,48,38,35,0,59,55,49,68],
[48,47,58,43,42,0,59,51,55],
[35,33,39,37,46,42,0,51,65],
[37,40,35,33,52,50,50,0,59],
[44,52,38,35,33,46,36,42,0]])



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
result = np.append(np.array([9, 101, 173, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,65,64,51,59,58,82,49],
[43,0,44,65,50,49,71,62,45],
[36,57,0,61,44,42,51,57,44],
[37,36,40,0,35,46,35,59,56],
[50,51,57,66,0,50,55,63,42],
[42,52,59,55,51,0,58,67,52],
[43,30,50,66,46,43,0,51,50],
[19,39,44,42,38,34,50,0,46],
[52,56,57,45,59,49,51,55,0]])



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
result = np.append(np.array([9, 101, 174, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,48,49,54,54,59,48,55],
[56,0,49,54,53,59,64,51,54],
[53,52,0,50,51,53,58,53,47],
[52,47,51,0,51,53,67,60,56],
[47,48,50,50,0,52,62,52,45],
[47,42,48,48,49,0,53,49,59],
[42,37,43,34,39,48,0,45,44],
[53,50,48,41,49,52,56,0,52],
[46,47,54,45,56,42,57,49,0]])



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
result = np.append(np.array([9, 101, 175, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,50,60,61,49,58,51,50],
[43,0,55,51,50,39,56,53,53],
[51,46,0,47,58,50,52,58,69],
[41,50,54,0,56,46,44,51,62],
[40,51,43,45,0,44,59,50,63],
[52,62,51,55,57,0,58,49,66],
[43,45,49,57,42,43,0,52,54],
[50,48,43,50,51,52,49,0,54],
[51,48,32,39,38,35,47,47,0]])



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
result = np.append(np.array([9, 101, 176, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,59,53,56,51,54,55,48],
[48,0,52,54,50,52,50,51,46],
[42,49,0,55,54,43,45,47,47],
[48,47,46,0,44,41,41,45,39],
[45,51,47,57,0,44,47,47,49],
[50,49,58,60,57,0,43,51,55],
[47,51,56,60,54,58,0,52,54],
[46,50,54,56,54,50,49,0,50],
[53,55,54,62,52,46,47,51,0]])



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
result = np.append(np.array([9, 101, 177, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,54,46,41,47,53,47,45],
[56,0,66,52,53,53,56,61,48],
[47,35,0,44,47,44,52,46,48],
[55,49,57,0,55,53,56,61,51],
[60,48,54,46,0,54,59,51,46],
[54,48,57,48,47,0,46,67,46],
[48,45,49,45,42,55,0,56,47],
[54,40,55,40,50,34,45,0,45],
[56,53,53,50,55,55,54,56,0]])



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
result = np.append(np.array([9, 101, 178, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,40,49,32,36,35,25,42],
[55,0,64,61,56,40,44,24,36],
[61,37,0,55,36,56,53,32,32],
[52,40,46,0,36,38,32,22,18],
[69,45,65,65,0,59,58,33,54],
[65,61,45,63,42,0,55,57,62],
[66,57,48,69,43,46,0,37,46],
[76,77,69,79,68,44,64,0,70],
[59,65,69,83,47,39,55,31,0]])



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
result = np.append(np.array([9, 101, 179, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,55,59,42,54,48,42,49],
[52,0,53,59,52,54,48,46,50],
[46,48,0,55,42,46,45,53,49],
[42,42,46,0,37,48,47,42,46],
[59,49,59,64,0,59,56,50,51],
[47,47,55,53,42,0,34,43,48],
[53,53,56,54,45,67,0,51,56],
[59,55,48,59,51,58,50,0,52],
[52,51,52,55,50,53,45,49,0]])



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
result = np.append(np.array([9, 101, 180, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,47,52,61,48,51,45,53],
[42,0,36,50,50,48,47,31,48],
[54,65,0,49,50,52,57,45,51],
[49,51,52,0,64,42,56,47,39],
[40,51,51,37,0,42,39,36,40],
[53,53,49,59,59,0,58,44,57],
[50,54,44,45,62,43,0,51,47],
[56,70,56,54,65,57,50,0,51],
[48,53,50,62,61,44,54,50,0]])



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
result = np.append(np.array([9, 101, 181, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,49,48,55,69,57,54,53],
[50,0,51,55,66,64,55,55,52],
[52,50,0,45,56,55,50,57,53],
[53,46,56,0,55,56,54,59,55],
[46,35,45,46,0,54,50,47,41],
[32,37,46,45,47,0,52,49,47],
[44,46,51,47,51,49,0,49,51],
[47,46,44,42,54,52,52,0,45],
[48,49,48,46,60,54,50,56,0]])



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
result = np.append(np.array([9, 101, 182, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,54,54,54,52,50,58,56],
[46,0,42,51,46,51,48,51,46],
[47,59,0,56,55,53,47,55,53],
[47,50,45,0,45,49,41,50,44],
[47,55,46,56,0,50,41,56,51],
[49,50,48,52,51,0,53,51,50],
[51,53,54,60,60,48,0,50,49],
[43,50,46,51,45,50,51,0,44],
[45,55,48,57,50,51,52,57,0]])



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
result = np.append(np.array([9, 101, 183, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,39,56,46,49,44,47,38],
[45,0,38,44,43,42,39,42,26],
[62,63,0,67,53,59,51,53,39],
[45,57,34,0,34,54,53,44,45],
[55,58,48,67,0,56,50,56,42],
[52,59,42,47,45,0,42,64,51],
[57,62,50,48,51,59,0,53,38],
[54,59,48,57,45,37,48,0,27],
[63,75,62,56,59,50,63,74,0]])



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
result = np.append(np.array([9, 101, 184, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,46,27,40,45,52,38,47],
[62,0,55,53,45,61,59,48,61],
[55,46,0,46,44,49,54,51,46],
[74,48,55,0,63,60,66,64,64],
[61,56,57,38,0,55,65,49,58],
[56,40,52,41,46,0,54,54,58],
[49,42,47,35,36,47,0,44,41],
[63,53,50,37,52,47,57,0,55],
[54,40,55,37,43,43,60,46,0]])



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
result = np.append(np.array([9, 101, 185, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,45,49,53,44,51,59,50],
[51,0,55,50,50,47,44,51,44],
[56,46,0,42,44,51,47,46,51],
[52,51,59,0,60,43,54,55,46],
[48,51,57,41,0,45,47,52,46],
[57,54,50,58,56,0,51,56,55],
[50,57,54,47,54,50,0,49,54],
[42,50,55,46,49,45,52,0,49],
[51,57,50,55,55,46,47,52,0]])



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
result = np.append(np.array([9, 101, 186, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,55,65,53,42,48,52,52],
[47,0,47,44,42,41,41,39,38],
[46,54,0,54,42,50,56,53,54],
[36,57,47,0,41,33,38,52,44],
[48,59,59,60,0,46,48,54,48],
[59,60,51,68,55,0,56,49,59],
[53,60,45,63,53,45,0,56,56],
[49,62,48,49,47,52,45,0,56],
[49,63,47,57,53,42,45,45,0]])



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
result = np.append(np.array([9, 101, 187, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,54,40,56,57,45,36,59],
[52,0,80,58,65,68,50,58,82],
[47,21,0,37,56,45,32,36,59],
[61,43,64,0,61,72,61,58,66],
[45,36,45,40,0,56,54,49,60],
[44,33,56,29,45,0,49,46,55],
[56,51,69,40,47,52,0,52,67],
[65,43,65,43,52,55,49,0,62],
[42,19,42,35,41,46,34,39,0]])



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
result = np.append(np.array([9, 101, 188, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,49,41,51,62,43,55,55],
[52,0,48,40,50,55,43,61,57],
[52,53,0,46,38,51,55,61,57],
[60,61,55,0,47,61,61,60,62],
[50,51,63,54,0,55,46,67,62],
[39,46,50,40,46,0,38,47,50],
[58,58,46,40,55,63,0,52,64],
[46,40,40,41,34,54,49,0,44],
[46,44,44,39,39,51,37,57,0]])



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
result = np.append(np.array([9, 101, 189, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,34,48,52,36,38,25,32],
[58,0,39,63,58,51,41,42,47],
[67,62,0,53,47,52,51,35,54],
[53,38,48,0,37,42,44,28,35],
[49,43,54,64,0,47,43,26,38],
[65,50,49,59,54,0,63,51,61],
[63,60,50,57,58,38,0,31,45],
[76,59,66,73,75,50,70,0,52],
[69,54,47,66,63,40,56,49,0]])



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
result = np.append(np.array([9, 101, 190, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,20,20,20,20,20,20,41],
[60,0,46,46,80,80,80,54,67],
[81,55,0,101,54,54,54,75,41],
[81,55,0,0,54,54,54,75,41],
[81,21,47,47,0,46,54,41,21],
[81,21,47,47,55,0,75,75,21],
[81,21,47,47,47,26,0,41,21],
[81,47,26,26,60,26,60,0,47],
[60,34,60,60,80,80,80,54,0]])



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
result = np.append(np.array([9, 101, 191, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,54,62,70,69,63,65,61],
[52,0,53,53,38,34,47,44,67],
[47,48,0,30,63,51,66,35,55],
[39,48,71,0,64,39,54,36,70],
[31,63,38,37,0,53,48,35,51],
[32,67,50,62,48,0,58,35,68],
[38,54,35,47,53,43,0,42,50],
[36,57,66,65,66,66,59,0,63],
[40,34,46,31,50,33,51,38,0]])



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
result = np.append(np.array([9, 101, 192, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,50,61,56,52,52,48,51],
[58,0,54,57,63,53,58,49,55],
[51,47,0,48,53,51,47,43,44],
[40,44,53,0,50,46,50,47,48],
[45,38,48,51,0,55,51,45,43],
[49,48,50,55,46,0,45,52,47],
[49,43,54,51,50,56,0,49,52],
[53,52,58,54,56,49,52,0,53],
[50,46,57,53,58,54,49,48,0]])



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
result = np.append(np.array([9, 101, 193, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,78,26,18,58,35,41,58],
[43,0,38,26,35,64,55,18,41],
[23,63,0,6,23,46,23,29,63],
[75,75,95,0,58,58,58,41,75],
[83,66,78,43,0,84,95,61,66],
[43,37,55,43,17,0,37,17,34],
[66,46,78,43,6,64,0,29,46],
[60,83,72,60,40,84,72,0,60],
[43,60,38,26,35,67,55,41,0]])



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
result = np.append(np.array([9, 101, 194, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,49,47,50,52,46,56,56],
[54,0,54,48,51,51,59,53,58],
[52,47,0,46,48,46,56,45,61],
[54,53,55,0,47,51,49,49,61],
[51,50,53,54,0,51,52,49,62],
[49,50,55,50,50,0,52,49,58],
[55,42,45,52,49,49,0,45,58],
[45,48,56,52,52,52,56,0,55],
[45,43,40,40,39,43,43,46,0]])



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
result = np.append(np.array([9, 101, 195, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,61,57,54,52,48,60,51],
[48,0,58,60,57,54,52,60,55],
[40,43,0,46,43,41,44,46,50],
[44,41,55,0,43,45,39,40,46],
[47,44,58,58,0,52,44,45,47],
[49,47,60,56,49,0,40,49,58],
[53,49,57,62,57,61,0,47,59],
[41,41,55,61,56,52,54,0,52],
[50,46,51,55,54,43,42,49,0]])



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
result = np.append(np.array([9, 101, 196, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,88,50,47,70,58,54,53],
[69,0,67,69,47,69,58,50,69],
[13,34,0,50,13,34,22,22,45],
[51,32,51,0,51,53,62,52,53],
[54,54,88,50,0,62,90,54,62],
[31,32,67,48,39,0,50,20,21],
[43,43,79,39,11,51,0,32,51],
[47,51,79,49,47,81,69,0,81],
[48,32,56,48,39,80,50,20,0]])



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
result = np.append(np.array([9, 101, 197, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,42,56,101,74,65,51,79],
[59,0,72,50,72,88,49,52,63],
[59,29,0,27,72,61,23,38,63],
[45,51,74,0,45,74,36,51,49],
[0,29,29,56,0,29,0,38,50],
[27,13,40,27,72,0,49,38,63],
[36,52,78,65,101,52,0,52,92],
[50,49,63,50,63,63,49,0,63],
[22,38,38,52,51,38,9,38,0]])



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
result = np.append(np.array([9, 101, 198, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,79,47,57,57,57,76,53,43],
[22,0,47,36,36,36,43,36,46],
[54,54,0,40,40,40,54,35,54],
[44,65,61,0,57,40,62,39,64],
[44,65,61,44,0,41,44,39,64],
[44,65,61,61,60,0,43,61,60],
[25,58,47,39,57,58,0,53,43],
[48,65,66,62,62,40,48,0,50],
[58,55,47,37,37,41,58,51,0]])



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
result = np.append(np.array([9, 101, 199, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,49,45,47,44,48,44,48],
[48,0,50,47,51,44,49,54,46],
[52,51,0,44,44,46,57,45,46],
[56,54,57,0,50,52,59,51,56],
[54,50,57,51,0,46,54,49,51],
[57,57,55,49,55,0,47,46,52],
[53,52,44,42,47,54,0,46,44],
[57,47,56,50,52,55,55,0,43],
[53,55,55,45,50,49,57,58,0]])



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
result = np.append(np.array([9, 101, 200, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbd/mebbd_9_101.csv", index=False, header=False)