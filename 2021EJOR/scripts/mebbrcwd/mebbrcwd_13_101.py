
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg
from kemeny import sc

rep = 1
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,47,52,48,43,49,51,57,38,55,57,53,44],
[54,0,54,52,42,57,51,60,47,50,56,63,50],
[49,47,0,49,48,55,55,58,43,52,54,57,52],
[53,49,52,0,51,52,57,58,47,56,55,56,42],
[58,59,53,50,0,60,49,59,56,56,60,60,50],
[52,44,46,49,41,0,49,53,42,49,53,54,50],
[50,50,46,44,52,52,0,57,43,60,53,56,49],
[44,41,43,43,42,48,44,0,46,50,50,52,50],
[63,54,58,54,45,59,58,55,0,60,69,65,54],
[46,51,49,45,45,52,41,51,41,0,45,50,40],
[44,45,47,46,41,48,48,51,32,56,0,51,41],
[48,38,44,45,41,47,45,49,36,51,50,0,41],
[57,51,49,59,51,51,52,51,47,61,60,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 1, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,63,63,49,54,52,58,60,55,53,60,59,61],
[38,0,46,51,53,44,43,43,49,46,44,43,48],
[38,55,0,48,47,50,42,46,43,45,52,44,52],
[52,50,53,0,60,54,56,51,51,51,57,45,63],
[47,48,54,41,0,47,60,55,49,44,53,53,54],
[49,57,51,47,54,0,54,58,53,59,45,56,54],
[43,58,59,45,41,47,0,53,43,54,55,50,59],
[41,58,55,50,46,43,48,0,52,45,52,48,50],
[46,52,58,50,52,48,58,49,0,47,53,52,48],
[48,55,56,50,57,42,47,56,54,0,57,56,54],
[41,57,49,44,48,56,46,49,48,44,0,45,49],
[42,58,57,56,48,45,51,53,49,45,56,0,54],
[40,53,49,38,47,47,42,51,53,47,52,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 2, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,51,55,49,49,53,56,51,47,51,46,51],
[50,0,45,53,50,51,58,52,46,46,47,47,47],
[50,56,0,56,54,56,53,58,53,53,56,51,50],
[46,48,45,0,51,48,55,52,52,44,44,44,44],
[52,51,47,50,0,52,56,57,48,46,56,45,52],
[52,50,45,53,49,0,53,52,49,41,50,49,57],
[48,43,48,46,45,48,0,47,47,43,50,42,53],
[45,49,43,49,44,49,54,0,43,44,42,38,51],
[50,55,48,49,53,52,54,58,0,51,57,49,54],
[54,55,48,57,55,60,58,57,50,0,57,46,63],
[50,54,45,57,45,51,51,59,44,44,0,38,53],
[55,54,50,57,56,52,59,63,52,55,63,0,55],
[50,54,51,57,49,44,48,50,47,38,48,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 3, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,47,49,50,46,44,50,52,43,49,47,48],
[62,0,57,57,58,49,54,57,58,53,58,53,50],
[54,44,0,44,49,48,46,51,52,43,49,44,49],
[52,44,57,0,48,41,50,48,54,47,51,48,56],
[51,43,52,53,0,49,51,46,52,49,48,52,50],
[55,52,53,60,52,0,51,56,55,47,48,57,61],
[57,47,55,51,50,50,0,58,60,49,51,52,52],
[51,44,50,53,55,45,43,0,49,45,51,45,45],
[49,43,49,47,49,46,41,52,0,43,44,42,45],
[58,48,58,54,52,54,52,56,58,0,52,55,51],
[52,43,52,50,53,53,50,50,57,49,0,50,52],
[54,48,57,53,49,44,49,56,59,46,51,0,54],
[53,51,52,45,51,40,49,56,56,50,49,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 4, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,63,52,67,59,54,62,57,49,47,57,55,49],
[38,0,46,55,47,38,43,45,37,35,40,36,42],
[49,55,0,62,56,54,57,64,43,50,44,50,56],
[34,46,39,0,42,42,44,49,31,40,50,34,41],
[42,54,45,59,0,53,48,55,31,45,42,38,45],
[47,63,47,59,48,0,47,48,53,45,52,48,55],
[39,58,44,57,53,54,0,59,49,44,50,42,54],
[44,56,37,52,46,53,42,0,43,47,42,42,48],
[52,64,58,70,70,48,52,58,0,50,59,58,59],
[54,66,51,61,56,56,57,54,51,0,54,52,47],
[44,61,57,51,59,49,51,59,42,47,0,50,57],
[46,65,51,67,63,53,59,59,43,49,51,0,56],
[52,59,45,60,56,46,47,53,42,54,44,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 5, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,45,29,46,47,37,33,40,50,40,57,39],
[60,0,49,51,57,61,44,47,44,48,40,57,37],
[56,52,0,52,61,46,41,67,56,61,62,55,41],
[72,50,49,0,51,56,40,40,52,66,47,70,35],
[55,44,40,50,0,54,49,39,52,57,46,45,38],
[54,40,55,45,47,0,32,51,40,48,37,40,36],
[64,57,60,61,52,69,0,52,54,62,58,49,54],
[68,54,34,61,62,50,49,0,56,58,56,52,45],
[61,57,45,49,49,61,47,45,0,39,45,46,37],
[51,53,40,35,44,53,39,43,62,0,54,51,29],
[61,61,39,54,55,64,43,45,56,47,0,57,35],
[44,44,46,31,56,61,52,49,55,50,44,0,39],
[62,64,60,66,63,65,47,56,64,72,66,62,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 6, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,45,49,48,65,54,46,41,36,47,48,44],
[50,0,30,31,52,46,43,48,39,52,47,36,41],
[56,71,0,51,58,74,52,56,46,52,55,67,53],
[52,70,50,0,69,56,46,49,48,53,63,59,64],
[53,49,43,32,0,63,58,48,37,45,55,44,48],
[36,55,27,45,38,0,37,31,38,38,44,39,36],
[47,58,49,55,43,64,0,51,58,50,51,48,49],
[55,53,45,52,53,70,50,0,47,48,56,45,45],
[60,62,55,53,64,63,43,54,0,45,58,49,48],
[65,49,49,48,56,63,51,53,56,0,50,57,48],
[54,54,46,38,46,57,50,45,43,51,0,55,47],
[53,65,34,42,57,62,53,56,52,44,46,0,43],
[57,60,48,37,53,65,52,56,53,53,54,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 7, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,60,50,53,52,52,58,60,54,64,52,57],
[40,0,52,53,56,42,36,48,54,46,54,45,47],
[41,49,0,50,56,45,51,52,52,46,55,42,46],
[51,48,51,0,57,45,46,54,49,39,55,41,44],
[48,45,45,44,0,40,40,52,52,53,45,55,42],
[49,59,56,56,61,0,52,62,60,48,61,57,51],
[49,65,50,55,61,49,0,47,61,48,59,50,53],
[43,53,49,47,49,39,54,0,54,45,57,52,42],
[41,47,49,52,49,41,40,47,0,47,49,42,47],
[47,55,55,62,48,53,53,56,54,0,60,65,58],
[37,47,46,46,56,40,42,44,52,41,0,49,43],
[49,56,59,60,46,44,51,49,59,36,52,0,48],
[44,54,55,57,59,50,48,59,54,43,58,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 8, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,39,47,42,44,45,73,49,37,55,51,55],
[55,0,47,58,57,60,51,67,48,52,59,47,49],
[62,54,0,55,44,62,53,70,71,53,75,39,48],
[54,43,46,0,48,49,47,77,51,47,52,49,45],
[59,44,57,53,0,47,45,71,49,51,69,56,50],
[57,41,39,52,54,0,32,63,47,28,65,32,39],
[56,50,48,54,56,69,0,66,65,45,68,55,57],
[28,34,31,24,30,38,35,0,33,19,36,37,31],
[52,53,30,50,52,54,36,68,0,43,62,58,57],
[64,49,48,54,50,73,56,82,58,0,60,55,42],
[46,42,26,49,32,36,33,65,39,41,0,40,39],
[50,54,62,52,45,69,46,64,43,46,61,0,49],
[46,52,53,56,51,62,44,70,44,59,62,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 9, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,49,46,42,42,50,43,56,56,55,38,40],
[50,0,55,53,51,57,54,57,52,60,60,49,51],
[52,46,0,45,41,42,55,46,53,58,54,41,34],
[55,48,56,0,44,55,52,47,54,47,47,54,47],
[59,50,60,57,0,48,55,49,58,58,53,48,44],
[59,44,59,46,53,0,55,55,55,54,55,49,43],
[51,47,46,49,46,46,0,48,48,53,54,45,44],
[58,44,55,54,52,46,53,0,60,52,46,46,48],
[45,49,48,47,43,46,53,41,0,49,55,40,39],
[45,41,43,54,43,47,48,49,52,0,54,38,35],
[46,41,47,54,48,46,47,55,46,47,0,42,43],
[63,52,60,47,53,52,56,55,61,63,59,0,44],
[61,50,67,54,57,58,57,53,62,66,58,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 10, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,46,50,44,54,54,40,44,46,49,43,40],
[52,0,51,48,45,52,50,52,53,52,46,45,48],
[55,50,0,55,45,59,60,49,55,57,50,45,45],
[51,53,46,0,47,62,52,43,53,47,48,48,42],
[57,56,56,54,0,62,56,48,52,53,53,52,47],
[47,49,42,39,39,0,43,48,47,46,45,45,44],
[47,51,41,49,45,58,0,45,47,50,55,45,42],
[61,49,52,58,53,53,56,0,62,64,51,54,51],
[57,48,46,48,49,54,54,39,0,46,42,47,45],
[55,49,44,54,48,55,51,37,55,0,43,47,41],
[52,55,51,53,48,56,46,50,59,58,0,61,49],
[58,56,56,53,49,56,56,47,54,54,40,0,52],
[61,53,56,59,54,57,59,50,56,60,52,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 11, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,59,37,48,44,45,45,45,60,49,59,41],
[46,0,55,51,43,56,44,41,56,60,58,59,54],
[42,46,0,40,48,47,45,37,49,49,48,55,38],
[64,50,61,0,59,54,53,43,49,62,59,54,42],
[53,58,53,42,0,59,62,54,57,50,57,66,55],
[57,45,54,47,42,0,49,45,57,57,57,49,52],
[56,57,56,48,39,52,0,46,46,67,66,60,58],
[56,60,64,58,47,56,55,0,56,65,66,65,52],
[56,45,52,52,44,44,55,45,0,65,51,54,38],
[41,41,52,39,51,44,34,36,36,0,43,53,44],
[52,43,53,42,44,44,35,35,50,58,0,52,48],
[42,42,46,47,35,52,41,36,47,48,49,0,45],
[60,47,63,59,46,49,43,49,63,57,53,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 12, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,50,58,40,45,48,48,50,51,55,61,47],
[49,0,64,69,48,50,47,61,48,43,49,66,59],
[51,37,0,70,34,36,35,58,40,38,49,57,45],
[43,32,31,0,37,41,28,45,43,37,32,51,34],
[61,53,67,64,0,55,48,68,61,50,53,59,58],
[56,51,65,60,46,0,54,53,58,52,54,65,59],
[53,54,66,73,53,47,0,68,46,63,50,71,59],
[53,40,43,56,33,48,33,0,49,41,39,46,48],
[51,53,61,58,40,43,55,52,0,46,55,64,61],
[50,58,63,64,51,49,38,60,55,0,52,53,61],
[46,52,52,69,48,47,51,62,46,49,0,57,54],
[40,35,44,50,42,36,30,55,37,48,44,0,45],
[54,42,56,67,43,42,42,53,40,40,47,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 13, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,60,57,60,55,49,63,56,46,53,52,51],
[43,0,45,49,43,47,40,54,47,45,51,50,34],
[41,56,0,48,47,45,54,53,45,42,52,58,28],
[44,52,53,0,49,46,49,42,48,45,49,51,40],
[41,58,54,52,0,52,53,54,42,38,42,46,37],
[46,54,56,55,49,0,52,48,49,40,55,51,46],
[52,61,47,52,48,49,0,51,52,47,57,53,48],
[38,47,48,59,47,53,50,0,54,49,52,49,42],
[45,54,56,53,59,52,49,47,0,46,49,53,45],
[55,56,59,56,63,61,54,52,55,0,61,61,48],
[48,50,49,52,59,46,44,49,52,40,0,46,45],
[49,51,43,50,55,50,48,52,48,40,55,0,41],
[50,67,73,61,64,55,53,59,56,53,56,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 14, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,49,58,52,60,53,57,62,57,62,54,48],
[49,0,52,44,55,52,53,57,59,39,44,41,43],
[52,49,0,61,63,63,51,59,61,50,49,52,52],
[43,57,40,0,63,55,46,54,52,46,50,54,52],
[49,46,38,38,0,54,53,51,53,42,49,46,43],
[41,49,38,46,47,0,39,47,50,42,48,50,39],
[48,48,50,55,48,62,0,53,61,55,59,55,44],
[44,44,42,47,50,54,48,0,56,41,53,50,46],
[39,42,40,49,48,51,40,45,0,32,43,44,40],
[44,62,51,55,59,59,46,60,69,0,55,61,56],
[39,57,52,51,52,53,42,48,58,46,0,51,44],
[47,60,49,47,55,51,46,51,57,40,50,0,45],
[53,58,49,49,58,62,57,55,61,45,57,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 15, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,61,59,50,58,48,51,54,61,46,57,60],
[42,0,45,51,51,47,44,41,52,58,45,56,41],
[40,56,0,47,50,42,39,45,47,55,47,51,48],
[42,50,54,0,44,47,45,47,49,53,38,54,38],
[51,50,51,57,0,54,57,53,55,62,51,55,53],
[43,54,59,54,47,0,42,48,51,58,42,54,48],
[53,57,62,56,44,59,0,55,46,60,50,54,51],
[50,60,56,54,48,53,46,0,54,57,53,57,48],
[47,49,54,52,46,50,55,47,0,57,53,46,47],
[40,43,46,48,39,43,41,44,44,0,42,46,34],
[55,56,54,63,50,59,51,48,48,59,0,57,47],
[44,45,50,47,46,47,47,44,55,55,44,0,48],
[41,60,53,63,48,53,50,53,54,67,54,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 16, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,52,56,39,41,54,49,49,58,53,45,43],
[53,0,55,52,46,49,62,53,54,65,49,58,54],
[49,46,0,44,50,50,60,60,61,54,52,50,54],
[45,49,57,0,50,52,60,54,54,57,53,51,40],
[62,55,51,51,0,46,55,59,52,60,63,63,53],
[60,52,51,49,55,0,58,60,55,56,64,55,58],
[47,39,41,41,46,43,0,50,33,50,44,43,37],
[52,48,41,47,42,41,51,0,37,44,55,45,36],
[52,47,40,47,49,46,68,64,0,54,58,42,45],
[43,36,47,44,41,45,51,57,47,0,54,46,42],
[48,52,49,48,38,37,57,46,43,47,0,35,42],
[56,43,51,50,38,46,58,56,59,55,66,0,60],
[58,47,47,61,48,43,64,65,56,59,59,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 17, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,42,44,46,40,46,48,53,54,39,43,44],
[59,0,45,45,42,53,49,49,54,56,44,55,46],
[59,56,0,43,55,51,61,52,57,56,47,56,49],
[57,56,58,0,52,50,50,54,58,55,50,48,60],
[55,59,46,49,0,52,46,49,58,50,54,49,51],
[61,48,50,51,49,0,50,53,55,50,46,56,42],
[55,52,40,51,55,51,0,53,57,54,48,53,50],
[53,52,49,47,52,48,48,0,53,51,47,52,56],
[48,47,44,43,43,46,44,48,0,55,46,47,48],
[47,45,45,46,51,51,47,50,46,0,44,58,46],
[62,57,54,51,47,55,53,54,55,57,0,52,51],
[58,46,45,53,52,45,48,49,54,43,49,0,49],
[57,55,52,41,50,59,51,45,53,55,50,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 18, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,60,40,47,29,44,38,60,43,43,49,46],
[41,0,56,38,43,51,34,34,59,50,34,38,32],
[41,45,0,32,40,44,38,34,52,35,37,48,39],
[61,63,69,0,56,47,58,50,66,44,59,50,47],
[54,58,61,45,0,53,35,43,53,52,61,54,43],
[72,50,57,54,48,0,53,49,51,59,48,48,57],
[57,67,63,43,66,48,0,37,60,51,49,46,41],
[63,67,67,51,58,52,64,0,71,52,56,54,40],
[41,42,49,35,48,50,41,30,0,37,49,40,40],
[58,51,66,57,49,42,50,49,64,0,52,66,41],
[58,67,64,42,40,53,52,45,52,49,0,43,45],
[52,63,53,51,47,53,55,47,61,35,58,0,48],
[55,69,62,54,58,44,60,61,61,60,56,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 19, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,51,39,32,52,40,44,26,40,40,35,56],
[85,0,59,49,55,86,49,54,51,75,64,20,66],
[50,42,0,37,39,63,49,50,39,50,49,25,39],
[62,52,64,0,67,62,46,59,38,62,53,46,66],
[69,46,62,34,0,67,46,73,56,49,54,35,69],
[49,15,38,39,34,0,38,41,18,26,38,23,31],
[61,52,52,55,55,63,0,68,27,63,74,51,55],
[57,47,51,42,28,60,33,0,39,60,48,35,27],
[75,50,62,63,45,83,74,62,0,53,61,50,63],
[61,26,51,39,52,75,38,41,48,0,46,27,48],
[61,37,52,48,47,63,27,53,40,55,0,13,42],
[66,81,76,55,66,78,50,66,51,74,88,0,66],
[45,35,62,35,32,70,46,74,38,53,59,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 20, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,46,58,43,50,49,48,45,32,42,55,50],
[57,0,73,65,61,67,73,46,59,53,47,66,46],
[55,28,0,51,45,37,48,42,44,41,45,46,47],
[43,36,50,0,45,28,42,46,51,45,43,53,52],
[58,40,56,56,0,44,58,36,48,36,57,57,45],
[51,34,64,73,57,0,64,49,47,54,49,54,49],
[52,28,53,59,43,37,0,48,41,34,28,48,50],
[53,55,59,55,65,52,53,0,56,34,46,58,36],
[56,42,57,50,53,54,60,45,0,56,39,63,44],
[69,48,60,56,65,47,67,67,45,0,45,67,53],
[59,54,56,58,44,52,73,55,62,56,0,54,55],
[46,35,55,48,44,47,53,43,38,34,47,0,52],
[51,55,54,49,56,52,51,65,57,48,46,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 21, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,41,39,48,43,52,48,49,54,47,52,48],
[50,0,47,49,61,60,60,62,51,59,49,61,56],
[60,54,0,48,62,62,56,55,50,55,51,59,57],
[62,52,53,0,59,63,63,62,62,61,49,63,57],
[53,40,39,42,0,56,54,61,52,54,42,62,50],
[58,41,39,38,45,0,45,56,47,51,47,58,47],
[49,41,45,38,47,56,0,54,59,54,51,53,55],
[53,39,46,39,40,45,47,0,45,48,45,48,51],
[52,50,51,39,49,54,42,56,0,51,49,57,52],
[47,42,46,40,47,50,47,53,50,0,37,55,42],
[54,52,50,52,59,54,50,56,52,64,0,55,56],
[49,40,42,38,39,43,48,53,44,46,46,0,52],
[53,45,44,44,51,54,46,50,49,59,45,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 22, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,40,47,47,43,42,44,48,48,46,47,39],
[55,0,52,49,50,51,48,43,49,53,53,53,47],
[61,49,0,52,55,55,47,51,54,59,56,62,50],
[54,52,49,0,55,49,41,43,48,50,55,53,44],
[54,51,46,46,0,45,42,38,49,50,48,48,47],
[58,50,46,52,56,0,49,41,45,53,53,50,45],
[59,53,54,60,59,52,0,49,52,58,55,54,49],
[57,58,50,58,63,60,52,0,53,62,59,57,50],
[53,52,47,53,52,56,49,48,0,56,48,50,50],
[53,48,42,51,51,48,43,39,45,0,52,52,50],
[55,48,45,46,53,48,46,42,53,49,0,48,44],
[54,48,39,48,53,51,47,44,51,49,53,0,52],
[62,54,51,57,54,56,52,51,51,51,57,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 23, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,54,60,63,56,53,40,58,42,62,57,62],
[44,0,51,44,37,48,51,39,44,46,46,41,61],
[47,50,0,60,54,70,55,55,39,46,48,58,71],
[41,57,41,0,48,62,51,51,48,39,59,51,67],
[38,64,47,53,0,67,50,46,46,42,54,61,59],
[45,53,31,39,34,0,47,47,40,35,49,23,56],
[48,50,46,50,51,54,0,52,47,53,50,43,73],
[61,62,46,50,55,54,49,0,54,49,40,33,65],
[43,57,62,53,55,61,54,47,0,51,52,60,60],
[59,55,55,62,59,66,48,52,50,0,55,58,75],
[39,55,53,42,47,52,51,61,49,46,0,45,60],
[44,60,43,50,40,78,58,68,41,43,56,0,77],
[39,40,30,34,42,45,28,36,41,26,41,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 24, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,47,41,50,54,33,43,46,49,42,47,49],
[60,0,53,49,65,58,46,59,62,61,63,50,53],
[54,48,0,54,51,52,39,54,43,43,55,49,46],
[60,52,47,0,53,53,38,51,41,47,44,47,42],
[51,36,50,48,0,37,46,52,50,55,41,54,44],
[47,43,49,48,64,0,38,52,45,50,42,50,41],
[68,55,62,63,55,63,0,56,61,64,59,64,49],
[58,42,47,50,49,49,45,0,51,49,34,50,38],
[55,39,58,60,51,56,40,50,0,52,52,50,49],
[52,40,58,54,46,51,37,52,49,0,56,40,41],
[59,38,46,57,60,59,42,67,49,45,0,52,51],
[54,51,52,54,47,51,37,51,51,61,49,0,43],
[52,48,55,59,57,60,52,63,52,60,50,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 25, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,55,57,56,47,46,52,46,44,57,45,46],
[54,0,54,58,54,49,43,49,41,52,58,46,48],
[46,47,0,54,50,41,41,44,43,45,41,38,57],
[44,43,47,0,43,43,40,53,41,41,41,35,47],
[45,47,51,58,0,52,45,49,45,52,53,41,52],
[54,52,60,58,49,0,43,49,42,39,50,53,51],
[55,58,60,61,56,58,0,55,54,52,53,48,58],
[49,52,57,48,52,52,46,0,51,43,52,49,56],
[55,60,58,60,56,59,47,50,0,51,51,51,57],
[57,49,56,60,49,62,49,58,50,0,52,53,61],
[44,43,60,60,48,51,48,49,50,49,0,46,50],
[56,55,63,66,60,48,53,52,50,48,55,0,63],
[55,53,44,54,49,50,43,45,44,40,51,38,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 26, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,49,48,48,64,48,45,56,49,51,52,59],
[55,0,52,45,49,60,48,60,61,55,50,57,55],
[52,49,0,52,51,60,45,48,58,53,48,50,55],
[53,56,49,0,60,55,50,60,61,49,54,56,54],
[53,52,50,41,0,51,50,55,43,47,46,44,55],
[37,41,41,46,50,0,40,44,44,43,49,51,39],
[53,53,56,51,51,61,0,58,55,49,50,52,51],
[56,41,53,41,46,57,43,0,55,47,39,46,56],
[45,40,43,40,58,57,46,46,0,48,47,42,49],
[52,46,48,52,54,58,52,54,53,0,53,58,51],
[50,51,53,47,55,52,51,62,54,48,0,47,61],
[49,44,51,45,57,50,49,55,59,43,54,0,51],
[42,46,46,47,46,62,50,45,52,50,40,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 27, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,59,54,59,53,53,62,56,59,59,46,57],
[45,0,51,49,53,46,49,54,56,46,53,42,53],
[42,50,0,49,54,57,48,51,49,48,56,41,54],
[47,52,52,0,58,55,51,56,54,54,55,41,56],
[42,48,47,43,0,57,47,52,47,48,53,47,60],
[48,55,44,46,44,0,51,53,49,49,55,43,60],
[48,52,53,50,54,50,0,52,51,56,55,52,56],
[39,47,50,45,49,48,49,0,52,51,54,44,55],
[45,45,52,47,54,52,50,49,0,53,54,48,65],
[42,55,53,47,53,52,45,50,48,0,61,48,61],
[42,48,45,46,48,46,46,47,47,40,0,40,54],
[55,59,60,60,54,58,49,57,53,53,61,0,67],
[44,48,47,45,41,41,45,46,36,40,47,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 28, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,53,45,47,35,47,52,47,46,48,54,37],
[56,0,69,56,57,53,63,61,51,59,53,62,45],
[48,32,0,47,42,45,48,54,43,48,42,52,41],
[56,45,54,0,56,47,55,48,39,53,44,58,51],
[54,44,59,45,0,42,54,59,46,54,44,52,46],
[66,48,56,54,59,0,49,58,59,61,49,54,54],
[54,38,53,46,47,52,0,46,43,47,38,47,41],
[49,40,47,53,42,43,55,0,47,46,43,55,38],
[54,50,58,62,55,42,58,54,0,55,51,60,55],
[55,42,53,48,47,40,54,55,46,0,45,54,34],
[53,48,59,57,57,52,63,58,50,56,0,69,52],
[47,39,49,43,49,47,54,46,41,47,32,0,42],
[64,56,60,50,55,47,60,63,46,67,49,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 29, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,35,45,32,47,44,39,40,35,43,42,43],
[61,0,54,52,47,56,52,43,54,50,50,48,54],
[66,47,0,56,54,54,59,46,48,52,54,50,53],
[56,49,45,0,52,47,58,45,47,49,48,46,48],
[69,54,47,49,0,56,49,43,52,48,52,52,54],
[54,45,47,54,45,0,63,46,57,45,51,47,52],
[57,49,42,43,52,38,0,46,44,44,45,43,50],
[62,58,55,56,58,55,55,0,49,46,58,54,52],
[61,47,53,54,49,44,57,52,0,46,49,47,54],
[66,51,49,52,53,56,57,55,55,0,54,47,58],
[58,51,47,53,49,50,56,43,52,47,0,53,49],
[59,53,51,55,49,54,58,47,54,54,48,0,50],
[58,47,48,53,47,49,51,49,47,43,52,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 30, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,43,50,46,44,46,56,50,48,55,51,55],
[58,0,53,54,57,52,50,53,57,56,63,47,52],
[58,48,0,53,55,54,50,55,57,55,58,58,59],
[51,47,48,0,49,46,45,48,49,47,49,41,44],
[55,44,46,52,0,50,48,57,58,48,62,52,50],
[57,49,47,55,51,0,52,57,58,45,63,51,49],
[55,51,51,56,53,49,0,59,63,63,55,52,56],
[45,48,46,53,44,44,42,0,50,47,53,44,53],
[51,44,44,52,43,43,38,51,0,53,54,45,49],
[53,45,46,54,53,56,38,54,48,0,58,52,52],
[46,38,43,52,39,38,46,48,47,43,0,44,43],
[50,54,43,60,49,50,49,57,56,49,57,0,60],
[46,49,42,57,51,52,45,48,52,49,58,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 31, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,65,35,55,61,47,40,57,54,65,60,51,61],
[36,0,48,41,45,45,33,52,55,79,45,43,67],
[66,53,0,63,60,52,37,62,64,69,64,50,71],
[46,60,38,0,42,55,55,60,52,79,59,36,74],
[40,56,41,59,0,51,45,71,61,63,53,50,62],
[54,56,49,46,50,0,46,61,66,58,61,48,75],
[61,68,64,46,56,55,0,85,61,86,59,52,64],
[44,49,39,41,30,40,16,0,48,46,39,38,55],
[47,46,37,49,40,35,40,53,0,80,65,37,76],
[36,22,32,22,38,43,15,55,21,0,41,33,47],
[41,56,37,42,48,40,42,62,36,60,0,44,47],
[50,58,51,65,51,53,49,63,64,68,57,0,65],
[40,34,30,27,39,26,37,46,25,54,54,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 32, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,41,48,42,46,63,50,23,31,61,21,34],
[62,0,74,78,45,62,60,64,59,59,68,41,47],
[60,27,0,46,46,25,59,49,16,48,45,22,39],
[53,23,55,0,37,35,54,45,41,42,51,43,36],
[59,56,55,64,0,44,47,38,35,47,54,31,48],
[55,39,76,66,57,0,43,55,44,45,61,29,40],
[38,41,42,47,54,58,0,31,17,31,53,28,31],
[51,37,52,56,63,46,70,0,47,41,72,25,48],
[78,42,85,60,66,57,84,54,0,59,68,51,48],
[70,42,53,59,54,56,70,60,42,0,51,41,50],
[40,33,56,50,47,40,48,29,33,50,0,19,56],
[80,60,79,58,70,72,73,76,50,60,82,0,44],
[67,54,62,65,53,61,70,53,53,51,45,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 33, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,52,53,56,50,56,54,54,53,51,54,58],
[54,0,50,54,54,53,52,49,49,47,61,57,59],
[49,51,0,47,53,48,54,51,48,52,48,49,51],
[48,47,54,0,56,48,47,46,51,49,52,55,58],
[45,47,48,45,0,40,49,41,47,38,46,47,50],
[51,48,53,53,61,0,52,54,47,46,63,54,61],
[45,49,47,54,52,49,0,51,49,45,54,53,51],
[47,52,50,55,60,47,50,0,49,43,53,56,53],
[47,52,53,50,54,54,52,52,0,50,55,55,56],
[48,54,49,52,63,55,56,58,51,0,52,63,56],
[50,40,53,49,55,38,47,48,46,49,0,52,48],
[47,44,52,46,54,47,48,45,46,38,49,0,53],
[43,42,50,43,51,40,50,48,45,45,53,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 34, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,53,43,34,35,31,37,31,48,38,38,36],
[58,0,56,60,61,63,66,47,39,66,52,69,54],
[48,45,0,36,42,40,33,42,43,52,51,47,57],
[58,41,65,0,41,44,40,37,39,53,38,52,41],
[67,40,59,60,0,43,49,56,45,60,53,54,63],
[66,38,61,57,58,0,46,54,40,63,53,46,63],
[70,35,68,61,52,55,0,51,51,50,63,59,60],
[64,54,59,64,45,47,50,0,35,65,61,50,53],
[70,62,58,62,56,61,50,66,0,58,57,69,58],
[53,35,49,48,41,38,51,36,43,0,55,55,41],
[63,49,50,63,48,48,38,40,44,46,0,51,47],
[63,32,54,49,47,55,42,51,32,46,50,0,50],
[65,47,44,60,38,38,41,48,43,60,54,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 35, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,61,53,57,54,62,47,49,55,55,48,59],
[57,0,55,45,53,56,60,47,44,52,53,50,59],
[40,46,0,42,48,47,49,42,43,50,47,44,46],
[48,56,59,0,55,56,54,47,46,64,58,51,51],
[44,48,53,46,0,48,53,42,46,51,47,42,47],
[47,45,54,45,53,0,52,43,54,52,54,39,56],
[39,41,52,47,48,49,0,47,41,51,44,45,47],
[54,54,59,54,59,58,54,0,58,59,59,45,57],
[52,57,58,55,55,47,60,43,0,52,54,51,55],
[46,49,51,37,50,49,50,42,49,0,43,46,48],
[46,48,54,43,54,47,57,42,47,58,0,45,55],
[53,51,57,50,59,62,56,56,50,55,56,0,69],
[42,42,55,50,54,45,54,44,46,53,46,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 36, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,85,63,64,63,57,63,70,58,73,53,50,70],
[16,0,12,34,44,41,35,37,17,33,25,31,21],
[38,89,0,67,52,57,76,79,37,64,48,70,57],
[37,67,34,0,49,60,62,61,52,55,44,56,43],
[38,57,49,52,0,48,48,50,17,41,34,37,41],
[44,60,44,41,53,0,60,37,37,60,46,63,60],
[38,66,25,39,53,41,0,70,26,51,35,47,49],
[31,64,22,40,51,64,31,0,37,44,28,41,40],
[43,84,64,49,84,64,75,64,0,92,49,57,55],
[28,68,37,46,60,41,50,57,9,0,25,44,41],
[48,76,53,57,67,55,66,73,52,76,0,50,64],
[51,70,31,45,64,38,54,60,44,57,51,0,62],
[31,80,44,58,60,41,52,61,46,60,37,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 37, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,55,51,55,50,54,46,53,50,62,47,56],
[53,0,60,54,44,54,53,44,54,59,38,54,72],
[46,41,0,48,53,52,55,45,55,41,54,45,52],
[50,47,53,0,38,60,52,34,55,43,42,33,53],
[46,57,48,63,0,58,45,43,55,44,60,51,63],
[51,47,49,41,43,0,48,41,47,39,48,35,47],
[47,48,46,49,56,53,0,37,50,35,60,45,59],
[55,57,56,67,58,60,64,0,72,47,53,49,63],
[48,47,46,46,46,54,51,29,0,41,51,25,51],
[51,42,60,58,57,62,66,54,60,0,46,49,53],
[39,63,47,59,41,53,41,48,50,55,0,58,50],
[54,47,56,68,50,66,56,52,76,52,43,0,60],
[45,29,49,48,38,54,42,38,50,48,51,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 38, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,45,48,49,45,42,53,46,41,50,47,48],
[47,0,47,49,45,42,45,56,41,48,52,47,52],
[56,54,0,53,48,45,48,55,43,45,56,47,51],
[53,52,48,0,51,52,50,53,50,48,53,49,54],
[52,56,53,50,0,54,48,56,44,47,59,53,52],
[56,59,56,49,47,0,54,56,48,55,65,56,62],
[59,56,53,51,53,47,0,59,53,52,58,50,55],
[48,45,46,48,45,45,42,0,41,43,47,42,45],
[55,60,58,51,57,53,48,60,0,51,57,55,56],
[60,53,56,53,54,46,49,58,50,0,62,48,52],
[51,49,45,48,42,36,43,54,44,39,0,45,55],
[54,54,54,52,48,45,51,59,46,53,56,0,57],
[53,49,50,47,49,39,46,56,45,49,46,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 39, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,51,59,47,55,47,57,54,44,59,52,53],
[51,0,52,51,51,46,52,57,55,48,56,42,54],
[50,49,0,54,46,54,46,58,51,45,56,44,54],
[42,50,47,0,38,50,48,49,50,43,48,43,54],
[54,50,55,63,0,57,52,61,55,55,59,50,62],
[46,55,47,51,44,0,48,59,44,45,58,43,51],
[54,49,55,53,49,53,0,60,53,53,51,47,59],
[44,44,43,52,40,42,41,0,47,47,50,39,50],
[47,46,50,51,46,57,48,54,0,41,60,40,54],
[57,53,56,58,46,56,48,54,60,0,57,44,60],
[42,45,45,53,42,43,50,51,41,44,0,38,53],
[49,59,57,58,51,58,54,62,61,57,63,0,55],
[48,47,47,47,39,50,42,51,47,41,48,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 40, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,66,63,60,46,60,56,42,48,55,49,51,49],
[35,0,53,57,43,47,54,45,48,53,45,51,48],
[38,48,0,44,37,45,47,39,45,39,38,49,42],
[41,44,57,0,53,60,53,52,52,54,57,49,46],
[55,58,64,48,0,53,58,45,40,55,38,63,57],
[41,54,56,41,48,0,55,48,50,55,45,52,56],
[45,47,54,48,43,46,0,37,44,56,49,55,51],
[59,56,62,49,56,53,64,0,58,58,56,61,58],
[53,53,56,49,61,51,57,43,0,55,62,54,49],
[46,48,62,47,46,46,45,43,46,0,46,51,50],
[52,56,63,44,63,56,52,45,39,55,0,59,56],
[50,50,52,52,38,49,46,40,47,50,42,0,51],
[52,53,59,55,44,45,50,43,52,51,45,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 41, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,57,59,51,54,47,49,53,54,56,59,54],
[44,0,49,58,50,57,52,47,48,53,46,54,45],
[44,52,0,61,51,59,57,49,49,46,60,53,56],
[42,43,40,0,43,57,48,44,49,37,48,52,44],
[50,51,50,58,0,62,47,45,48,45,55,59,52],
[47,44,42,44,39,0,40,38,43,46,54,53,49],
[54,49,44,53,54,61,0,53,52,57,55,50,56],
[52,54,52,57,56,63,48,0,47,44,51,52,54],
[48,53,52,52,53,58,49,54,0,56,54,51,50],
[47,48,55,64,56,55,44,57,45,0,54,53,48],
[45,55,41,53,46,47,46,50,47,47,0,57,58],
[42,47,48,49,42,48,51,49,50,48,44,0,45],
[47,56,45,57,49,52,45,47,51,53,43,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 42, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,48,54,53,40,47,57,48,53,45,46,61],
[48,0,49,42,41,43,55,56,40,45,47,43,55],
[53,52,0,53,53,48,42,55,49,51,47,45,54],
[47,59,48,0,52,41,43,58,60,40,45,44,56],
[48,60,48,49,0,43,50,52,50,52,54,42,54],
[61,58,53,60,58,0,56,64,56,48,50,47,69],
[54,46,59,58,51,45,0,59,49,43,42,47,59],
[44,45,46,43,49,37,42,0,43,38,44,47,49],
[53,61,52,41,51,45,52,58,0,45,51,42,58],
[48,56,50,61,49,53,58,63,56,0,49,58,63],
[56,54,54,56,47,51,59,57,50,52,0,58,63],
[55,58,56,57,59,54,54,54,59,43,43,0,56],
[40,46,47,45,47,32,42,52,43,38,38,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 43, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,57,57,72,64,65,48,55,72,77,38,63],
[50,0,52,60,52,56,52,47,66,66,61,47,56],
[44,49,0,60,46,56,52,52,46,57,65,50,71],
[44,41,41,0,56,55,38,41,58,70,58,40,57],
[29,49,55,45,0,62,54,47,46,55,71,48,64],
[37,45,45,46,39,0,50,44,43,56,48,44,48],
[36,49,49,63,47,51,0,52,49,60,64,34,61],
[53,54,49,60,54,57,49,0,64,65,57,51,60],
[46,35,55,43,55,58,52,37,0,62,59,43,65],
[29,35,44,31,46,45,41,36,39,0,60,33,46],
[24,40,36,43,30,53,37,44,42,41,0,33,46],
[63,54,51,61,53,57,67,50,58,68,68,0,68],
[38,45,30,44,37,53,40,41,36,55,55,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 44, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,48,49,54,55,52,49,45,54,49,49,59],
[48,0,46,49,51,58,49,47,47,51,46,52,51],
[53,55,0,52,54,56,51,50,43,54,45,49,52],
[52,52,49,0,53,62,54,51,49,56,51,50,53],
[47,50,47,48,0,53,47,44,48,55,42,51,53],
[46,43,45,39,48,0,48,38,41,41,39,50,48],
[49,52,50,47,54,53,0,51,45,52,46,52,57],
[52,54,51,50,57,63,50,0,51,55,47,49,54],
[56,54,58,52,53,60,56,50,0,52,48,54,50],
[47,50,47,45,46,60,49,46,49,0,40,48,53],
[52,55,56,50,59,62,55,54,53,61,0,51,62],
[52,49,52,51,50,51,49,52,47,53,50,0,55],
[42,50,49,48,48,53,44,47,51,48,39,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 45, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,47,55,57,59,53,46,59,65,35,51,54],
[54,0,46,70,62,51,51,61,56,68,54,58,59],
[54,55,0,62,58,60,50,59,68,71,46,57,42],
[46,31,39,0,43,50,37,37,51,59,36,44,41],
[44,39,43,58,0,45,54,47,74,58,49,48,47],
[42,50,41,51,56,0,53,41,62,60,50,42,53],
[48,50,51,64,47,48,0,64,66,63,52,47,44],
[55,40,42,64,54,60,37,0,55,73,48,36,48],
[42,45,33,50,27,39,35,46,0,62,39,44,49],
[36,33,30,42,43,41,38,28,39,0,35,39,36],
[66,47,55,65,52,51,49,53,62,66,0,43,58],
[50,43,44,57,53,59,54,65,57,62,58,0,50],
[47,42,59,60,54,48,57,53,52,65,43,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 46, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,54,46,55,42,62,39,46,55,48,51,60],
[56,0,55,37,44,48,65,63,68,54,49,44,63],
[47,46,0,36,48,52,65,56,59,49,59,41,54],
[55,64,65,0,52,48,70,57,66,66,61,46,74],
[46,57,53,49,0,54,58,57,57,62,62,40,67],
[59,53,49,53,47,0,56,56,53,56,63,44,59],
[39,36,36,31,43,45,0,41,64,49,47,26,56],
[62,38,45,44,44,45,60,0,54,56,46,34,63],
[55,33,42,35,44,48,37,47,0,45,44,42,44],
[46,47,52,35,39,45,52,45,56,0,48,43,58],
[53,52,42,40,39,38,54,55,57,53,0,46,59],
[50,57,60,55,61,57,75,67,59,58,55,0,69],
[41,38,47,27,34,42,45,38,57,43,42,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 47, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,52,51,52,50,53,43,53,60,54,49,44],
[54,0,56,44,46,56,56,51,50,52,55,47,47],
[49,45,0,55,55,53,57,50,51,59,55,50,52],
[50,57,46,0,51,55,55,57,51,55,54,51,48],
[49,55,46,50,0,54,56,56,51,59,50,48,49],
[51,45,48,46,47,0,54,46,50,56,52,45,50],
[48,45,44,46,45,47,0,48,48,56,57,46,48],
[58,50,51,44,45,55,53,0,52,61,56,50,58],
[48,51,50,50,50,51,53,49,0,54,45,46,45],
[41,49,42,46,42,45,45,40,47,0,44,45,48],
[47,46,46,47,51,49,44,45,56,57,0,47,46],
[52,54,51,50,53,56,55,51,55,56,54,0,50],
[57,54,49,53,52,51,53,43,56,53,55,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 48, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,40,41,47,46,49,48,47,39,60,38,47],
[55,0,45,59,48,44,49,48,53,54,60,57,67],
[61,56,0,52,60,49,53,57,57,59,72,61,61],
[60,42,49,0,43,43,44,53,46,43,53,53,49],
[54,53,41,58,0,52,51,59,56,51,64,45,61],
[55,57,52,58,49,0,45,54,49,46,56,48,59],
[52,52,48,57,50,56,0,48,46,54,66,44,59],
[53,53,44,48,42,47,53,0,38,44,57,40,53],
[54,48,44,55,45,52,55,63,0,58,65,53,54],
[62,47,42,58,50,55,47,57,43,0,64,45,52],
[41,41,29,48,37,45,35,44,36,37,0,37,54],
[63,44,40,48,56,53,57,61,48,56,64,0,58],
[54,34,40,52,40,42,42,48,47,49,47,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 49, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,47,54,56,49,35,48,41,37,45,47,39],
[39,0,47,47,47,49,39,49,44,43,47,50,40],
[54,54,0,52,55,47,48,57,40,50,50,51,48],
[47,54,49,0,52,46,43,50,46,47,50,50,40],
[45,54,46,49,0,37,38,52,45,39,49,42,37],
[52,52,54,55,64,0,40,53,49,45,44,53,48],
[66,62,53,58,63,61,0,57,61,48,59,52,55],
[53,52,44,51,49,48,44,0,46,42,42,49,37],
[60,57,61,55,56,52,40,55,0,34,48,56,46],
[64,58,51,54,62,56,53,59,67,0,49,61,49],
[56,54,51,51,52,57,42,59,53,52,0,59,47],
[54,51,50,51,59,48,49,52,45,40,42,0,39],
[62,61,53,61,64,53,46,64,55,52,54,62,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 50, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,64,48,0,48,0,48,48,48,0,48,48],
[101,0,101,85,37,101,53,101,101,85,53,101,101],
[37,0,0,37,37,37,37,85,85,37,37,37,37],
[53,16,64,0,53,64,53,101,64,101,16,101,101],
[101,64,64,48,0,64,64,64,64,48,64,64,64],
[53,0,64,37,37,0,37,85,64,37,37,101,101],
[101,48,64,48,37,64,0,48,64,85,64,64,64],
[53,0,16,0,37,16,53,0,64,37,16,16,16],
[53,0,16,37,37,37,37,37,0,37,37,37,53],
[53,16,64,0,53,64,16,64,64,0,16,64,64],
[101,48,64,85,37,64,37,85,64,85,0,101,101],
[53,0,64,0,37,0,37,85,64,37,0,0,64],
[53,0,64,0,37,0,37,85,48,37,0,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 51, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,37,48,43,57,51,52,41,38,49,36,53],
[60,0,52,59,57,68,53,50,55,56,54,47,49],
[64,49,0,53,48,55,55,60,53,48,43,49,58],
[53,42,48,0,42,55,52,47,50,46,45,45,50],
[58,44,53,59,0,55,47,45,52,46,57,45,47],
[44,33,46,46,46,0,50,43,39,42,40,42,47],
[50,48,46,49,54,51,0,47,39,55,39,43,54],
[49,51,41,54,56,58,54,0,53,50,52,54,51],
[60,46,48,51,49,62,62,48,0,50,49,45,48],
[63,45,53,55,55,59,46,51,51,0,48,54,49],
[52,47,58,56,44,61,62,49,52,53,0,46,50],
[65,54,52,56,56,59,58,47,56,47,55,0,53],
[48,52,43,51,54,54,47,50,53,52,51,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 52, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,38,42,54,48,48,42,43,38,54,40,52],
[48,0,48,48,39,52,36,46,45,40,48,39,48],
[63,53,0,50,47,56,57,51,53,46,54,43,53],
[59,53,51,0,51,45,53,44,58,45,53,47,49],
[47,62,54,50,0,58,48,53,55,49,49,51,62],
[53,49,45,56,43,0,43,54,57,49,43,38,42],
[53,65,44,48,53,58,0,56,64,57,60,54,63],
[59,55,50,57,48,47,45,0,56,49,57,56,52],
[58,56,48,43,46,44,37,45,0,46,44,42,48],
[63,61,55,56,52,52,44,52,55,0,54,59,56],
[47,53,47,48,52,58,41,44,57,47,0,44,48],
[61,62,58,54,50,63,47,45,59,42,57,0,52],
[49,53,48,52,39,59,38,49,53,45,53,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 53, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,43,43,41,44,50,38,52,44,44,50,42],
[51,0,44,47,48,46,52,36,46,52,38,54,46],
[58,57,0,53,52,54,52,51,52,65,45,62,56],
[58,54,48,0,47,55,48,46,52,55,48,54,51],
[60,53,49,54,0,47,48,47,55,60,42,63,52],
[57,55,47,46,54,0,51,42,49,60,50,58,51],
[51,49,49,53,53,50,0,43,43,49,44,55,45],
[63,65,50,55,54,59,58,0,59,58,53,63,49],
[49,55,49,49,46,52,58,42,0,56,48,53,49],
[57,49,36,46,41,41,52,43,45,0,41,54,44],
[57,63,56,53,59,51,57,48,53,60,0,61,56],
[51,47,39,47,38,43,46,38,48,47,40,0,36],
[59,55,45,50,49,50,56,52,52,57,45,65,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 54, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,67,73,42,47,66,55,54,56,41,68,42,50],
[34,0,46,51,36,67,43,27,50,32,24,57,34],
[28,55,0,42,35,66,40,34,49,31,28,30,55],
[59,50,59,0,33,78,68,42,63,34,33,54,50],
[54,65,66,68,0,68,71,34,67,45,40,64,68],
[35,34,35,23,33,0,21,27,48,6,25,24,36],
[46,58,61,33,30,80,0,39,44,26,36,49,38],
[47,74,67,59,67,74,62,0,46,53,41,64,58],
[45,51,52,38,34,53,57,55,0,36,19,51,44],
[60,69,70,67,56,95,75,48,65,0,60,85,52],
[33,77,73,68,61,76,65,60,82,41,0,62,47],
[59,44,71,47,37,77,52,37,50,16,39,0,45],
[51,67,46,51,33,65,63,43,57,49,54,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 55, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,44,49,56,51,46,41,45,51,52,48,45],
[52,0,48,49,48,48,48,48,49,50,51,47,46],
[57,53,0,56,56,50,52,54,50,55,47,59,56],
[52,52,45,0,58,48,51,51,47,51,52,49,52],
[45,53,45,43,0,44,48,47,48,46,46,46,47],
[50,53,51,53,57,0,50,56,45,47,54,43,51],
[55,53,49,50,53,51,0,47,51,55,56,53,45],
[60,53,47,50,54,45,54,0,43,50,51,54,47],
[56,52,51,54,53,56,50,58,0,51,55,51,47],
[50,51,46,50,55,54,46,51,50,0,47,47,45],
[49,50,54,49,55,47,45,50,46,54,0,49,48],
[53,54,42,52,55,58,48,47,50,54,52,0,52],
[56,55,45,49,54,50,56,54,54,56,53,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 56, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,61,62,56,53,61,66,57,61,55,51,49],
[45,0,51,50,48,48,55,55,45,57,47,44,42],
[40,50,0,53,54,51,55,63,48,59,49,48,39],
[39,51,48,0,53,49,47,51,49,57,38,40,45],
[45,53,47,48,0,53,47,60,42,56,47,43,40],
[48,53,50,52,48,0,51,52,51,53,42,44,46],
[40,46,46,54,54,50,0,63,45,57,42,46,44],
[35,46,38,50,41,49,38,0,39,49,39,40,42],
[44,56,53,52,59,50,56,62,0,53,43,43,53],
[40,44,42,44,45,48,44,52,48,0,39,40,39],
[46,54,52,63,54,59,59,62,58,62,0,48,52],
[50,57,53,61,58,57,55,61,58,61,53,0,54],
[52,59,62,56,61,55,57,59,48,62,49,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 57, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,41,42,56,49,62,43,39,53,55,57,47],
[52,0,53,48,63,53,61,54,51,48,62,56,53],
[60,48,0,48,72,47,67,49,66,50,68,66,58],
[59,53,53,0,68,45,54,53,54,62,60,49,65],
[45,38,29,33,0,29,47,40,41,40,38,36,36],
[52,48,54,56,72,0,68,58,59,60,66,76,68],
[39,40,34,47,54,33,0,38,38,34,47,38,53],
[58,47,52,48,61,43,63,0,58,47,61,57,63],
[62,50,35,47,60,42,63,43,0,48,53,48,46],
[48,53,51,39,61,41,67,54,53,0,56,52,51],
[46,39,33,41,63,35,54,40,48,45,0,54,58],
[44,45,35,52,65,25,63,44,53,49,47,0,59],
[54,48,43,36,65,33,48,38,55,50,43,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 58, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,57,44,50,58,58,50,59,46,53,46,53],
[43,0,49,60,57,53,51,57,51,46,51,50,53],
[44,52,0,53,61,53,48,54,46,45,48,46,52],
[57,41,48,0,49,56,51,50,53,46,42,45,51],
[51,44,40,52,0,49,48,55,47,39,49,40,55],
[43,48,48,45,52,0,56,53,54,40,54,36,55],
[43,50,53,50,53,45,0,60,45,41,43,45,55],
[51,44,47,51,46,48,41,0,49,44,39,52,49],
[42,50,55,48,54,47,56,52,0,52,44,46,50],
[55,55,56,55,62,61,60,57,49,0,52,51,64],
[48,50,53,59,52,47,58,62,57,49,0,51,57],
[55,51,55,56,61,65,56,49,55,50,50,0,64],
[48,48,49,50,46,46,46,52,51,37,44,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 59, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,38,45,56,56,50,55,56,68,46,49,52],
[52,0,43,50,45,59,50,42,62,60,49,55,41],
[63,58,0,55,46,75,62,55,64,70,48,54,44],
[56,51,46,0,59,68,67,56,64,59,64,57,48],
[45,56,55,42,0,69,46,46,50,50,47,49,45],
[45,42,26,33,32,0,37,41,41,37,41,44,38],
[51,51,39,34,55,64,0,51,55,46,55,37,46],
[46,59,46,45,55,60,50,0,50,55,49,50,43],
[45,39,37,37,51,60,46,51,0,54,35,54,38],
[33,41,31,42,51,64,55,46,47,0,51,35,41],
[55,52,53,37,54,60,46,52,66,50,0,56,42],
[52,46,47,44,52,57,64,51,47,66,45,0,41],
[49,60,57,53,56,63,55,58,63,60,59,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 60, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,52,51,50,52,47,47,49,40,60,46,46],
[51,0,53,48,49,47,54,48,61,45,54,44,52],
[49,48,0,51,47,48,46,41,54,45,54,41,49],
[50,53,50,0,44,46,54,52,51,43,56,47,55],
[51,52,54,57,0,54,54,58,54,46,60,51,54],
[49,54,53,55,47,0,49,51,52,47,55,49,51],
[54,47,55,47,47,52,0,53,53,41,52,47,52],
[54,53,60,49,43,50,48,0,54,40,51,46,53],
[52,40,47,50,47,49,48,47,0,42,57,43,52],
[61,56,56,58,55,54,60,61,59,0,61,50,58],
[41,47,47,45,41,46,49,50,44,40,0,44,47],
[55,57,60,54,50,52,54,55,58,51,57,0,57],
[55,49,52,46,47,50,49,48,49,43,54,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 61, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,37,37,15,46,15,15,15,15,37,37,37],
[86,0,86,44,37,64,62,15,37,22,64,68,62],
[64,15,0,22,15,46,40,15,15,0,39,46,0],
[64,57,79,0,57,64,40,33,33,57,57,42,42],
[86,64,86,44,0,86,62,37,37,46,64,68,86],
[55,37,55,37,15,0,55,15,15,15,15,37,37],
[86,39,61,61,39,46,0,39,61,39,61,46,46],
[86,86,86,68,64,86,62,0,40,64,64,68,86],
[86,64,86,68,64,86,40,61,0,42,64,68,86],
[86,79,101,44,55,86,62,37,59,0,101,68,62],
[64,37,62,44,37,86,40,37,37,0,0,68,44],
[64,33,55,59,33,64,55,33,33,33,33,0,18],
[64,39,101,59,15,64,55,15,15,39,57,83,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 62, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,62,52,42,58,50,54,53,56,55,59,55],
[62,0,51,47,48,53,49,44,47,45,50,50,50],
[39,50,0,51,45,51,43,45,51,56,52,42,51],
[49,54,50,0,46,45,45,47,31,43,41,40,58],
[59,53,56,55,0,42,58,45,52,51,68,57,61],
[43,48,50,56,59,0,44,38,37,54,43,51,61],
[51,52,58,56,43,57,0,54,50,49,58,53,60],
[47,57,56,54,56,63,47,0,54,54,53,61,63],
[48,54,50,70,49,64,51,47,0,57,51,52,54],
[45,56,45,58,50,47,52,47,44,0,48,50,64],
[46,51,49,60,33,58,43,48,50,53,0,51,58],
[42,51,59,61,44,50,48,40,49,51,50,0,55],
[46,51,50,43,40,40,41,38,47,37,43,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 63, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,58,42,46,48,39,48,42,47,47,52,45],
[54,0,47,48,41,45,42,55,45,55,43,49,60],
[43,54,0,35,39,48,41,44,39,39,48,46,52],
[59,53,66,0,50,59,55,66,53,53,53,53,61],
[55,60,62,51,0,56,51,58,47,52,50,56,61],
[53,56,53,42,45,0,44,48,34,45,47,52,55],
[62,59,60,46,50,57,0,59,49,54,54,59,54],
[53,46,57,35,43,53,42,0,36,50,50,54,59],
[59,56,62,48,54,67,52,65,0,51,60,55,61],
[54,46,62,48,49,56,47,51,50,0,47,48,59],
[54,58,53,48,51,54,47,51,41,54,0,55,60],
[49,52,55,48,45,49,42,47,46,53,46,0,53],
[56,41,49,40,40,46,47,42,40,42,41,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 64, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,44,62,54,57,38,36,43,40,56,26,59],
[55,0,36,72,67,66,61,26,58,50,52,36,53],
[57,65,0,66,73,63,53,59,52,48,73,42,59],
[39,29,35,0,33,40,45,27,30,18,25,18,34],
[47,34,28,68,0,58,34,23,36,38,48,32,62],
[44,35,38,61,43,0,32,28,20,43,37,17,44],
[63,40,48,56,67,69,0,50,52,53,50,43,53],
[65,75,42,74,78,73,51,0,51,59,73,48,73],
[58,43,49,71,65,81,49,50,0,47,64,52,55],
[61,51,53,83,63,58,48,42,54,0,59,29,67],
[45,49,28,76,53,64,51,28,37,42,0,34,57],
[75,65,59,83,69,84,58,53,49,72,67,0,64],
[42,48,42,67,39,57,48,28,46,34,44,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 65, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,63,56,42,50,42,80,52,68,79,74,67],
[48,0,58,69,37,56,43,83,48,67,67,86,56],
[38,43,0,61,32,56,37,75,46,64,67,60,49],
[45,32,40,0,30,43,38,46,38,64,63,37,47],
[59,64,69,71,0,65,54,80,50,78,79,78,73],
[51,45,45,58,36,0,43,63,54,48,83,49,44],
[59,58,64,63,47,58,0,68,48,58,71,66,74],
[21,18,26,55,21,38,33,0,39,54,63,45,48],
[49,53,55,63,51,47,53,62,0,36,72,56,60],
[33,34,37,37,23,53,43,47,65,0,64,45,39],
[22,34,34,38,22,18,30,38,29,37,0,46,40],
[27,15,41,64,23,52,35,56,45,56,55,0,55],
[34,45,52,54,28,57,27,53,41,62,61,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 66, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,50,55,48,45,46,39,53,52,51,40,45],
[52,0,62,57,48,52,51,48,64,56,53,51,56],
[51,39,0,53,47,41,39,37,50,49,43,31,44],
[46,44,48,0,46,36,39,40,52,39,39,32,42],
[53,53,54,55,0,48,52,55,52,49,50,40,54],
[56,49,60,65,53,0,53,48,53,53,54,46,50],
[55,50,62,62,49,48,0,47,51,51,57,48,54],
[62,53,64,61,46,53,54,0,56,59,55,44,59],
[48,37,51,49,49,48,50,45,0,46,47,36,49],
[49,45,52,62,52,48,50,42,55,0,45,40,49],
[50,48,58,62,51,47,44,46,54,56,0,46,52],
[61,50,70,69,61,55,53,57,65,61,55,0,59],
[56,45,57,59,47,51,47,42,52,52,49,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 67, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,50,65,68,49,66,35,53,72,62,84,62],
[49,0,39,66,64,54,54,43,64,57,68,78,45],
[51,62,0,66,53,56,42,51,43,59,57,60,60],
[36,35,35,0,46,47,35,37,46,40,45,50,45],
[33,37,48,55,0,21,58,29,50,54,35,68,43],
[52,47,45,54,80,0,71,47,54,57,62,65,61],
[35,47,59,66,43,30,0,38,60,57,46,79,53],
[66,58,50,64,72,54,63,0,67,69,69,80,58],
[48,37,58,55,51,47,41,34,0,58,47,52,54],
[29,44,42,61,47,44,44,32,43,0,39,58,30],
[39,33,44,56,66,39,55,32,54,62,0,71,50],
[17,23,41,51,33,36,22,21,49,43,30,0,44],
[39,56,41,56,58,40,48,43,47,71,51,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 68, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,57,60,57,47,56,42,45,47,66,41,47],
[49,0,62,35,43,46,59,53,38,47,60,41,53],
[44,39,0,53,58,57,41,41,45,51,54,30,52],
[41,66,48,0,41,49,57,59,48,47,51,43,60],
[44,58,43,60,0,51,56,44,61,57,67,38,62],
[54,55,44,52,50,0,49,53,62,47,60,51,60],
[45,42,60,44,45,52,0,57,49,47,38,56,58],
[59,48,60,42,57,48,44,0,46,44,47,61,61],
[56,63,56,53,40,39,52,55,0,53,42,41,59],
[54,54,50,54,44,54,54,57,48,0,52,48,63],
[35,41,47,50,34,41,63,54,59,49,0,44,55],
[60,60,71,58,63,50,45,40,60,53,57,0,60],
[54,48,49,41,39,41,43,40,42,38,46,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 69, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,59,59,61,54,53,48,54,66,55,65,55],
[49,0,48,47,44,47,44,43,52,49,60,55,49],
[42,53,0,48,50,46,43,42,49,50,57,57,50],
[42,54,53,0,51,53,52,49,55,53,63,56,52],
[40,57,51,50,0,50,49,47,50,52,56,63,54],
[47,54,55,48,51,0,47,55,61,55,51,60,53],
[48,57,58,49,52,54,0,44,60,57,60,57,59],
[53,58,59,52,54,46,57,0,54,53,60,64,58],
[47,49,52,46,51,40,41,47,0,45,52,56,52],
[35,52,51,48,49,46,44,48,56,0,50,57,47],
[46,41,44,38,45,50,41,41,49,51,0,51,43],
[36,46,44,45,38,41,44,37,45,44,50,0,46],
[46,52,51,49,47,48,42,43,49,54,58,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 70, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,62,52,55,55,46,64,52,48,51,51,57],
[49,0,59,54,62,56,49,54,62,56,54,50,61],
[39,42,0,47,48,47,45,48,47,43,46,45,51],
[49,47,54,0,54,45,54,46,48,41,44,55,58],
[46,39,53,47,0,52,42,47,48,50,48,46,52],
[46,45,54,56,49,0,45,55,49,39,53,48,58],
[55,52,56,47,59,56,0,57,54,52,53,52,54],
[37,47,53,55,54,46,44,0,50,52,45,56,50],
[49,39,54,53,53,52,47,51,0,48,40,47,56],
[53,45,58,60,51,62,49,49,53,0,49,54,62],
[50,47,55,57,53,48,48,56,61,52,0,55,61],
[50,51,56,46,55,53,49,45,54,47,46,0,58],
[44,40,50,43,49,43,47,51,45,39,40,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 71, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,57,52,46,64,53,50,52,49,56,47,57],
[50,0,59,59,61,54,56,57,59,51,54,52,60],
[44,42,0,52,46,51,47,48,48,45,51,51,59],
[49,42,49,0,53,48,55,45,51,40,44,48,54],
[55,40,55,48,0,52,46,41,51,46,49,43,57],
[37,47,50,53,49,0,42,47,44,35,50,40,52],
[48,45,54,46,55,59,0,50,59,52,63,48,62],
[51,44,53,56,60,54,51,0,51,48,54,53,60],
[49,42,53,50,50,57,42,50,0,54,45,55,54],
[52,50,56,61,55,66,49,53,47,0,47,51,63],
[45,47,50,57,52,51,38,47,56,54,0,54,59],
[54,49,50,53,58,61,53,48,46,50,47,0,62],
[44,41,42,47,44,49,39,41,47,38,42,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 72, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,59,65,42,49,68,54,49,56,40,55,54],
[41,0,49,44,37,29,56,46,36,38,40,57,37],
[42,52,0,54,42,44,66,44,50,51,45,63,41],
[36,57,47,0,27,41,53,52,35,51,37,51,42],
[59,64,59,74,0,50,70,57,51,57,52,49,55],
[52,72,57,60,51,0,72,63,50,60,60,67,57],
[33,45,35,48,31,29,0,41,35,47,33,33,41],
[47,55,57,49,44,38,60,0,35,49,43,41,50],
[52,65,51,66,50,51,66,66,0,58,50,60,49],
[45,63,50,50,44,41,54,52,43,0,39,53,49],
[61,61,56,64,49,41,68,58,51,62,0,58,51],
[46,44,38,50,52,34,68,60,41,48,43,0,42],
[47,64,60,59,46,44,60,51,52,52,50,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 73, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,56,47,47,52,49,49,46,59,53,52,52],
[48,0,50,43,43,47,43,52,52,46,43,46,48],
[45,51,0,48,51,51,51,52,50,51,47,49,50],
[54,58,53,0,44,56,49,58,54,54,49,54,57],
[54,58,50,57,0,48,55,51,53,62,52,46,57],
[49,54,50,45,53,0,58,58,56,55,51,54,51],
[52,58,50,52,46,43,0,60,50,47,47,44,54],
[52,49,49,43,50,43,41,0,42,46,44,44,48],
[55,49,51,47,48,45,51,59,0,46,48,47,44],
[42,55,50,47,39,46,54,55,55,0,39,44,46],
[48,58,54,52,49,50,54,57,53,62,0,59,51],
[49,55,52,47,55,47,57,57,54,57,42,0,52],
[49,53,51,44,44,50,47,53,57,55,50,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 74, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,37,39,46,40,56,36,68,70,52,50,82,53],
[64,0,51,63,58,58,38,58,72,52,50,65,46],
[62,50,0,52,36,35,55,63,59,52,57,53,52],
[55,38,49,0,55,45,38,55,77,52,32,56,64],
[61,43,65,46,0,49,40,79,59,49,54,51,52],
[45,43,66,56,52,0,59,72,61,49,49,36,47],
[65,63,46,63,61,42,0,68,63,67,44,59,56],
[33,43,38,46,22,29,33,0,45,42,47,36,52],
[31,29,42,24,42,40,38,56,0,38,35,47,47],
[49,49,49,49,52,52,34,59,63,0,30,49,46],
[51,51,44,69,47,52,57,54,66,71,0,51,49],
[19,36,48,45,50,65,42,65,54,52,50,0,62],
[48,55,49,37,49,54,45,49,54,55,52,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 75, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,23,57,23,46,7,29,13,32,54,27,29],
[74,0,43,79,64,76,48,70,69,87,62,59,68],
[78,58,0,83,58,62,59,61,36,68,67,46,33],
[44,22,18,0,28,38,14,56,26,46,35,38,23],
[78,37,43,73,0,61,59,64,50,59,65,59,24],
[55,25,39,63,40,0,43,63,29,57,46,63,32],
[94,53,42,87,42,58,0,55,43,59,85,53,38],
[72,31,40,45,37,38,46,0,30,46,63,34,21],
[88,32,65,75,51,72,58,71,0,59,73,69,24],
[69,14,33,55,42,44,42,55,42,0,42,32,23],
[47,39,34,66,36,55,16,38,28,59,0,36,38],
[74,42,55,63,42,38,48,67,32,69,65,0,40],
[72,33,68,78,77,69,63,80,77,78,63,61,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 76, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,52,61,50,46,49,44,56,46,52,52,48],
[53,0,49,61,52,50,50,45,52,42,49,58,47],
[49,52,0,58,45,38,39,47,47,38,43,57,48],
[40,40,43,0,41,42,40,42,45,33,42,46,35],
[51,49,56,60,0,55,50,49,55,52,51,56,54],
[55,51,63,59,46,0,44,45,51,49,51,55,54],
[52,51,62,61,51,57,0,52,52,53,52,59,50],
[57,56,54,59,52,56,49,0,55,48,52,56,49],
[45,49,54,56,46,50,49,46,0,50,43,55,50],
[55,59,63,68,49,52,48,53,51,0,51,66,45],
[49,52,58,59,50,50,49,49,58,50,0,52,50],
[49,43,44,55,45,46,42,45,46,35,49,0,44],
[53,54,53,66,47,47,51,52,51,56,51,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 77, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,49,65,52,48,48,60,67,44,39,48,67],
[63,0,64,87,49,55,63,70,78,54,54,68,74],
[52,37,0,64,55,53,51,62,76,54,49,61,61],
[36,14,37,0,35,34,36,34,39,39,35,40,41],
[49,52,46,66,0,54,60,56,56,67,43,47,60],
[53,46,48,67,47,0,39,42,60,63,33,41,53],
[53,38,50,65,41,62,0,61,70,46,45,53,63],
[41,31,39,67,45,59,40,0,66,35,43,47,60],
[34,23,25,62,45,41,31,35,0,40,17,34,41],
[57,47,47,62,34,38,55,66,61,0,44,59,54],
[62,47,52,66,58,68,56,58,84,57,0,65,58],
[53,33,40,61,54,60,48,54,67,42,36,0,56],
[34,27,40,60,41,48,38,41,60,47,43,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 78, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,52,45,51,54,62,49,51,54,57,56,59],
[43,0,43,45,45,43,48,58,48,41,44,46,46],
[49,58,0,39,42,41,51,50,41,45,46,42,51],
[56,56,62,0,48,50,56,49,48,45,55,44,46],
[50,56,59,53,0,52,50,57,55,53,52,58,57],
[47,58,60,51,49,0,46,51,50,55,50,44,54],
[39,53,50,45,51,55,0,44,55,51,48,55,45],
[52,43,51,52,44,50,57,0,46,48,49,47,50],
[50,53,60,53,46,51,46,55,0,47,52,55,48],
[47,60,56,56,48,46,50,53,54,0,54,51,51],
[44,57,55,46,49,51,53,52,49,47,0,50,53],
[45,55,59,57,43,57,46,54,46,50,51,0,51],
[42,55,50,55,44,47,56,51,53,50,48,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 79, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,42,63,48,51,43,45,39,55,52,41,31],
[48,0,47,64,52,49,53,49,34,54,38,45,29],
[59,54,0,55,60,52,57,36,40,66,49,57,42],
[38,37,46,0,53,41,46,33,36,56,46,41,36],
[53,49,41,48,0,48,65,51,49,61,63,38,40],
[50,52,49,60,53,0,37,42,49,48,41,46,56],
[58,48,44,55,36,64,0,47,56,52,59,38,39],
[56,52,65,68,50,59,54,0,40,51,42,46,43],
[62,67,61,65,52,52,45,61,0,75,47,55,58],
[46,47,35,45,40,53,49,50,26,0,34,54,19],
[49,63,52,55,38,60,42,59,54,67,0,48,52],
[60,56,44,60,63,55,63,55,46,47,53,0,44],
[70,72,59,65,61,45,62,58,43,82,49,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 80, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,58,47,44,63,41,48,51,33,47,49,40],
[59,0,52,49,46,64,31,66,56,47,41,50,55],
[43,49,0,38,47,64,24,59,41,53,36,38,48],
[54,52,63,0,40,76,39,55,73,47,40,71,57],
[57,55,54,61,0,57,53,62,60,53,51,54,41],
[38,37,37,25,44,0,29,44,48,22,40,30,33],
[60,70,77,62,48,72,0,64,72,56,62,63,53],
[53,35,42,46,39,57,37,0,45,44,41,32,57],
[50,45,60,28,41,53,29,56,0,30,51,55,46],
[68,54,48,54,48,79,45,57,71,0,54,56,48],
[54,60,65,61,50,61,39,60,50,47,0,65,42],
[52,51,63,30,47,71,38,69,46,45,36,0,40],
[61,46,53,44,60,68,48,44,55,53,59,61,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 81, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,50,49,58,53,55,51,41,56,50,52,44],
[53,0,55,61,49,44,58,44,49,55,55,64,49],
[51,46,0,46,42,46,51,38,40,46,47,49,40],
[52,40,55,0,50,48,57,40,47,56,48,54,51],
[43,52,59,51,0,50,51,51,51,53,48,44,38],
[48,57,55,53,51,0,62,52,47,60,48,50,46],
[46,43,50,44,50,39,0,43,38,46,44,41,40],
[50,57,63,61,50,49,58,0,53,61,47,55,55],
[60,52,61,54,50,54,63,48,0,58,54,52,48],
[45,46,55,45,48,41,55,40,43,0,53,40,41],
[51,46,54,53,53,53,57,54,47,48,0,47,48],
[49,37,52,47,57,51,60,46,49,61,54,0,42],
[57,52,61,50,63,55,61,46,53,60,53,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 82, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,67,70,65,68,66,49,68,61,64,75,55,62],
[34,0,42,48,43,53,51,57,52,57,49,41,48],
[31,59,0,59,63,56,51,60,53,59,49,48,67],
[36,53,42,0,49,52,33,48,42,57,35,51,52],
[33,58,38,52,0,48,33,34,42,47,49,53,43],
[35,48,45,49,53,0,47,54,53,59,47,46,37],
[52,50,50,68,68,54,0,53,56,56,60,58,66],
[33,44,41,53,67,47,48,0,43,46,46,53,54],
[40,49,48,59,59,48,45,58,0,50,64,48,51],
[37,44,42,44,54,42,45,55,51,0,51,49,48],
[26,52,52,66,52,54,41,55,37,50,0,59,48],
[46,60,53,50,48,55,43,48,53,52,42,0,51],
[39,53,34,49,58,64,35,47,50,53,53,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 83, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,42,47,51,42,45,45,49,51,56,54,48],
[57,0,51,56,56,41,45,38,47,42,54,58,47],
[59,50,0,55,64,49,46,52,56,51,60,59,53],
[54,45,46,0,57,40,45,42,52,46,52,62,49],
[50,45,37,44,0,44,45,36,51,39,55,51,50],
[59,60,52,61,57,0,51,47,54,45,66,59,51],
[56,56,55,56,56,50,0,51,61,58,62,65,59],
[56,63,49,59,65,54,50,0,52,56,65,66,61],
[52,54,45,49,50,47,40,49,0,45,54,60,59],
[50,59,50,55,62,56,43,45,56,0,54,60,53],
[45,47,41,49,46,35,39,36,47,47,0,48,48],
[47,43,42,39,50,42,36,35,41,41,53,0,47],
[53,54,48,52,51,50,42,40,42,48,53,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 84, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,45,44,53,52,43,44,44,51,51,58,39],
[54,0,52,48,58,55,55,53,46,60,57,52,39],
[56,49,0,41,59,53,56,46,52,54,53,55,41],
[57,53,60,0,58,52,50,44,47,55,54,59,49],
[48,43,42,43,0,46,51,48,51,54,50,58,47],
[49,46,48,49,55,0,50,42,49,58,53,58,51],
[58,46,45,51,50,51,0,45,53,53,53,55,43],
[57,48,55,57,53,59,56,0,58,56,45,54,55],
[57,55,49,54,50,52,48,43,0,54,48,58,41],
[50,41,47,46,47,43,48,45,47,0,39,45,43],
[50,44,48,47,51,48,48,56,53,62,0,59,50],
[43,49,46,42,43,43,46,47,43,56,42,0,40],
[62,62,60,52,54,50,58,46,60,58,51,61,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 85, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,45,62,51,53,56,60,54,55,49,60,65],
[49,0,50,60,42,53,45,51,37,44,47,42,54],
[56,51,0,52,48,54,47,50,51,49,51,49,54],
[39,41,49,0,43,54,44,43,34,40,50,53,45],
[50,59,53,58,0,57,61,53,52,53,43,60,64],
[48,48,47,47,44,0,48,53,42,49,65,57,69],
[45,56,54,57,40,53,0,49,41,54,53,59,57],
[41,50,51,58,48,48,52,0,40,56,62,62,57],
[47,64,50,67,49,59,60,61,0,50,52,60,74],
[46,57,52,61,48,52,47,45,51,0,57,62,70],
[52,54,50,51,58,36,48,39,49,44,0,45,50],
[41,59,52,48,41,44,42,39,41,39,56,0,50],
[36,47,47,56,37,32,44,44,27,31,51,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 86, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,53,53,44,52,47,45,42,51,38,43,51],
[55,0,54,62,45,51,56,49,55,51,46,44,63],
[48,47,0,54,38,50,61,48,53,53,39,45,52],
[48,39,47,0,40,50,49,46,48,48,37,42,52],
[57,56,63,61,0,61,66,45,60,63,53,53,64],
[49,50,51,51,40,0,48,43,47,39,39,37,58],
[54,45,40,52,35,53,0,42,45,51,38,45,48],
[56,52,53,55,56,58,59,0,55,62,50,45,60],
[59,46,48,53,41,54,56,46,0,49,41,43,57],
[50,50,48,53,38,62,50,39,52,0,39,43,54],
[63,55,62,64,48,62,63,51,60,62,0,55,58],
[58,57,56,59,48,64,56,56,58,58,46,0,61],
[50,38,49,49,37,43,53,41,44,47,43,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 87, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,46,55,62,56,56,50,44,54,59,51,47],
[61,0,63,59,57,59,57,63,54,57,70,50,58],
[55,38,0,50,52,60,60,48,42,53,56,54,57],
[46,42,51,0,44,46,48,52,49,51,53,49,41],
[39,44,49,57,0,48,51,49,53,46,53,54,56],
[45,42,41,55,53,0,53,52,47,57,58,42,50],
[45,44,41,53,50,48,0,50,40,45,47,48,50],
[51,38,53,49,52,49,51,0,42,44,51,49,45],
[57,47,59,52,48,54,61,59,0,47,54,40,54],
[47,44,48,50,55,44,56,57,54,0,45,38,50],
[42,31,45,48,48,43,54,50,47,56,0,49,43],
[50,51,47,52,47,59,53,52,61,63,52,0,52],
[54,43,44,60,45,51,51,56,47,51,58,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 88, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,57,69,62,39,18,61,39,45,65,46,36],
[62,0,79,98,101,65,48,78,72,78,101,94,62],
[44,22,0,80,80,60,36,82,35,66,83,57,25],
[32,3,21,0,49,21,22,48,3,44,31,32,17],
[39,0,21,52,0,21,25,55,10,66,54,32,13],
[62,36,41,80,80,0,70,56,53,96,83,80,36],
[83,53,65,79,76,31,0,70,70,88,65,77,60],
[40,23,19,53,46,45,31,0,24,67,78,52,14],
[62,29,66,98,91,48,31,77,0,66,66,75,58],
[56,23,35,57,35,5,13,34,35,0,60,56,35],
[36,0,18,70,47,18,36,23,35,41,0,64,14],
[55,7,44,69,69,21,24,49,26,45,37,0,36],
[65,39,76,84,88,65,41,87,43,66,87,65,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 89, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,55,67,63,55,38,54,59,60,56,45,58],
[55,0,53,69,60,51,43,47,58,68,60,37,56],
[46,48,0,59,51,53,56,38,52,52,54,46,67],
[34,32,42,0,46,39,44,30,43,39,36,42,54],
[38,41,50,55,0,54,48,27,49,51,48,38,45],
[46,50,48,62,47,0,39,38,46,48,57,49,51],
[63,58,45,57,53,62,0,50,63,59,60,51,63],
[47,54,63,71,74,63,51,0,61,70,64,51,68],
[42,43,49,58,52,55,38,40,0,58,48,34,51],
[41,33,49,62,50,53,42,31,43,0,46,47,49],
[45,41,47,65,53,44,41,37,53,55,0,46,53],
[56,64,55,59,63,52,50,50,67,54,55,0,39],
[43,45,34,47,56,50,38,33,50,52,48,62,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 90, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,49,38,48,33,35,19,39,31,36,53,53],
[70,0,65,64,68,63,46,62,69,64,54,70,61],
[52,36,0,48,62,30,49,47,34,48,49,58,32],
[63,37,53,0,65,41,39,57,57,47,59,61,58],
[53,33,39,36,0,44,29,56,44,39,36,51,46],
[68,38,71,60,57,0,55,59,56,48,57,66,62],
[66,55,52,62,72,46,0,64,61,55,50,64,61],
[82,39,54,44,45,42,37,0,50,37,50,65,60],
[62,32,67,44,57,45,40,51,0,48,45,54,53],
[70,37,53,54,62,53,46,64,53,0,58,62,52],
[65,47,52,42,65,44,51,51,56,43,0,78,59],
[48,31,43,40,50,35,37,36,47,39,23,0,44],
[48,40,69,43,55,39,40,41,48,49,42,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 91, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,51,48,60,47,53,51,41,44,49,34,51],
[39,0,42,50,47,43,36,39,32,33,43,42,44],
[50,59,0,44,68,38,52,50,45,35,37,46,40],
[53,51,57,0,75,50,53,47,52,51,53,38,43],
[41,54,33,26,0,37,38,37,43,32,45,30,41],
[54,58,63,51,64,0,54,46,49,50,61,51,48],
[48,65,49,48,63,47,0,52,49,50,48,28,44],
[50,62,51,54,64,55,49,0,52,33,61,52,46],
[60,69,56,49,58,52,52,49,0,50,60,43,48],
[57,68,66,50,69,51,51,68,51,0,51,50,52],
[52,58,64,48,56,40,53,40,41,50,0,36,43],
[67,59,55,63,71,50,73,49,58,51,65,0,44],
[50,57,61,58,60,53,57,55,53,49,58,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 92, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,43,50,63,57,43,64,43,39,61,51,58],
[43,0,44,56,54,62,36,52,24,24,49,48,47],
[58,57,0,40,53,52,39,57,35,30,58,56,53],
[51,45,61,0,47,61,33,45,37,29,33,46,41],
[38,47,48,54,0,70,53,67,34,39,43,57,62],
[44,39,49,40,31,0,34,46,27,25,56,72,52],
[58,65,62,68,48,67,0,74,44,53,66,74,57],
[37,49,44,56,34,55,27,0,46,22,54,64,38],
[58,77,66,64,67,74,57,55,0,38,63,60,58],
[62,77,71,72,62,76,48,79,63,0,70,80,55],
[40,52,43,68,58,45,35,47,38,31,0,53,40],
[50,53,45,55,44,29,27,37,41,21,48,0,50],
[43,54,48,60,39,49,44,63,43,46,61,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 93, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,28,36,14,5,6,11,33,5,27,14,0],
[74,0,67,44,14,15,45,54,40,0,78,24,24],
[73,34,0,53,14,19,19,60,39,19,40,28,14],
[65,57,48,0,14,25,20,45,62,20,68,25,14],
[87,87,87,87,0,56,50,55,53,46,78,30,10],
[96,86,82,76,45,0,35,64,71,35,78,46,24],
[95,56,82,81,51,66,0,69,67,42,72,46,61],
[90,47,41,56,46,37,32,0,22,22,52,46,46],
[68,61,62,39,48,30,34,79,0,30,72,39,39],
[96,101,82,81,55,66,59,79,71,0,78,66,24],
[74,23,61,33,23,23,29,49,29,23,0,23,14],
[87,77,73,76,71,55,55,55,62,35,78,0,29],
[101,77,87,87,91,77,40,55,62,77,87,72,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 94, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,53,46,59,59,48,47,52,52,58,45,58],
[43,0,50,46,46,44,35,44,54,43,36,44,48],
[48,51,0,51,53,55,47,47,51,45,53,47,47],
[55,55,50,0,54,57,44,51,53,52,43,51,56],
[42,55,48,47,0,51,41,38,47,44,45,42,49],
[42,57,46,44,50,0,33,41,51,40,48,41,51],
[53,66,54,57,60,68,0,50,57,54,48,52,60],
[54,57,54,50,63,60,51,0,54,54,58,48,54],
[49,47,50,48,54,50,44,47,0,48,47,42,51],
[49,58,56,49,57,61,47,47,53,0,55,48,56],
[43,65,48,58,56,53,53,43,54,46,0,49,57],
[56,57,54,50,59,60,49,53,59,53,52,0,59],
[43,53,54,45,52,50,41,47,50,45,44,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 95, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,69,48,65,69,71,80,77,43,58,66,55,58],
[32,0,43,71,48,62,62,65,38,47,38,57,38],
[53,58,0,67,47,60,66,64,65,43,71,49,48],
[36,30,34,0,30,36,58,54,17,27,45,38,27],
[32,53,54,71,0,48,72,61,53,56,64,54,45],
[30,39,41,65,53,0,62,50,35,27,52,42,29],
[21,39,35,43,29,39,0,45,22,36,46,28,31],
[24,36,37,47,40,51,56,0,28,31,45,29,36],
[58,63,36,84,48,66,79,73,0,50,66,45,50],
[43,54,58,74,45,74,65,70,51,0,46,56,35],
[35,63,30,56,37,49,55,56,35,55,0,39,55],
[46,44,52,63,47,59,73,72,56,45,62,0,48],
[43,63,53,74,56,72,70,65,51,66,46,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 96, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,52,47,49,32,32,59,35,44,33,50,59],
[63,0,55,48,49,35,37,60,39,46,47,65,63],
[49,46,0,39,25,29,35,39,45,28,24,54,40],
[54,53,62,0,47,35,57,69,48,25,38,72,72],
[52,52,76,54,0,33,37,57,48,35,41,52,65],
[69,66,72,66,68,0,72,75,59,63,43,50,66],
[69,64,66,44,64,29,0,67,45,41,51,61,52],
[42,41,62,32,44,26,34,0,34,26,30,36,58],
[66,62,56,53,53,42,56,67,0,35,45,71,75],
[57,55,73,76,66,38,60,75,66,0,41,69,77],
[68,54,77,63,60,58,50,71,56,60,0,77,76],
[51,36,47,29,49,51,40,65,30,32,24,0,50],
[42,38,61,29,36,35,49,43,26,24,25,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 97, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,43,52,51,49,56,46,48,50,48,47,52],
[54,0,47,56,50,56,56,49,53,48,53,48,54],
[58,54,0,53,54,59,59,52,60,61,50,57,49],
[49,45,48,0,53,52,58,45,58,51,51,52,52],
[50,51,47,48,0,50,55,49,51,53,47,47,53],
[52,45,42,49,51,0,57,50,50,56,48,48,50],
[45,45,42,43,46,44,0,45,43,47,48,44,44],
[55,52,49,56,52,51,56,0,61,61,51,57,57],
[53,48,41,43,50,51,58,40,0,53,43,46,51],
[51,53,40,50,48,45,54,40,48,0,49,46,43],
[53,48,51,50,54,53,53,50,58,52,0,56,54],
[54,53,44,49,54,53,57,44,55,55,45,0,50],
[49,47,52,49,48,51,57,44,50,58,47,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 98, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,61,59,47,72,55,56,59,57,52,59,56],
[47,0,62,70,53,70,60,70,66,57,54,53,66],
[40,39,0,54,43,65,44,42,53,44,44,40,51],
[42,31,47,0,33,56,35,38,35,41,33,35,46],
[54,48,58,68,0,66,42,60,67,59,52,59,55],
[29,31,36,45,35,0,30,40,50,40,40,36,39],
[46,41,57,66,59,71,0,59,68,45,47,55,43],
[45,31,59,63,41,61,42,0,56,39,40,42,49],
[42,35,48,66,34,51,33,45,0,31,35,38,43],
[44,44,57,60,42,61,56,62,70,0,52,54,56],
[49,47,57,68,49,61,54,61,66,49,0,61,51],
[42,48,61,66,42,65,46,59,63,47,40,0,64],
[45,35,50,55,46,62,58,52,58,45,50,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 99, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,53,52,51,46,47,48,48,44,53,47,44],
[52,0,48,52,52,42,45,41,44,48,46,48,47],
[48,53,0,45,52,45,41,47,35,44,44,51,40],
[49,49,56,0,50,45,43,46,44,50,46,44,50],
[50,49,49,51,0,43,43,51,51,44,49,56,46],
[55,59,56,56,58,0,50,53,52,56,57,56,55],
[54,56,60,58,58,51,0,55,52,51,53,56,50],
[53,60,54,55,50,48,46,0,51,52,41,57,50],
[53,57,66,57,50,49,49,50,0,44,55,51,53],
[57,53,57,51,57,45,50,49,57,0,51,51,49],
[48,55,57,55,52,44,48,60,46,50,0,49,54],
[54,53,50,57,45,45,45,44,50,50,52,0,44],
[57,54,61,51,55,46,51,51,48,52,47,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 100, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,50,55,51,59,54,53,49,55,58,45,51],
[51,0,51,48,54,59,55,56,49,54,50,53,53],
[51,50,0,50,48,54,60,52,43,51,58,50,57],
[46,53,51,0,58,66,55,56,40,49,47,52,54],
[50,47,53,43,0,66,57,47,44,46,47,50,61],
[42,42,47,35,35,0,47,46,33,39,53,45,47],
[47,46,41,46,44,54,0,49,33,35,47,42,59],
[48,45,49,45,54,55,52,0,37,44,51,49,54],
[52,52,58,61,57,68,68,64,0,50,59,58,60],
[46,47,50,52,55,62,66,57,51,0,57,47,52],
[43,51,43,54,54,48,54,50,42,44,0,53,52],
[56,48,51,49,51,56,59,52,43,54,48,0,58],
[50,48,44,47,40,54,42,47,41,49,49,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 101, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,53,53,50,51,62,51,53,52,52,53,50],
[51,0,56,45,49,48,57,50,48,50,55,52,50],
[48,45,0,51,50,50,60,55,52,51,51,48,53],
[48,56,50,0,57,54,56,54,51,53,53,54,53],
[51,52,51,44,0,51,56,55,45,47,45,48,43],
[50,53,51,47,50,0,58,59,47,55,53,57,45],
[39,44,41,45,45,43,0,44,45,47,38,45,49],
[50,51,46,47,46,42,57,0,48,51,46,51,49],
[48,53,49,50,56,54,56,53,0,56,49,52,49],
[49,51,50,48,54,46,54,50,45,0,49,54,48],
[49,46,50,48,56,48,63,55,52,52,0,53,47],
[48,49,53,47,53,44,56,50,49,47,48,0,46],
[51,51,48,48,58,56,52,52,52,53,54,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 102, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,47,46,46,45,51,57,51,41,48,46,50],
[56,0,50,51,45,49,47,54,52,51,49,53,54],
[54,51,0,45,53,43,45,61,51,54,52,53,49],
[55,50,56,0,50,51,45,53,48,51,45,50,45],
[55,56,48,51,0,50,51,52,50,46,56,51,51],
[56,52,58,50,51,0,53,59,57,48,54,56,55],
[50,54,56,56,50,48,0,56,55,49,43,56,59],
[44,47,40,48,49,42,45,0,47,46,46,43,40],
[50,49,50,53,51,44,46,54,0,50,42,50,53],
[60,50,47,50,55,53,52,55,51,0,56,50,54],
[53,52,49,56,45,47,58,55,59,45,0,59,46],
[55,48,48,51,50,45,45,58,51,51,42,0,51],
[51,47,52,56,50,46,42,61,48,47,55,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 103, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,44,46,43,45,43,44,47,45,52,52,50],
[50,0,51,54,51,55,56,54,51,65,58,63,60],
[57,50,0,50,43,51,47,57,61,52,51,55,60],
[55,47,51,0,45,52,58,51,53,50,55,61,53],
[58,50,58,56,0,53,58,59,56,58,56,58,59],
[56,46,50,49,48,0,54,50,52,51,57,55,49],
[58,45,54,43,43,47,0,50,42,51,49,48,51],
[57,47,44,50,42,51,51,0,50,38,51,44,48],
[54,50,40,48,45,49,59,51,0,58,53,57,51],
[56,36,49,51,43,50,50,63,43,0,44,50,59],
[49,43,50,46,45,44,52,50,48,57,0,49,53],
[49,38,46,40,43,46,53,57,44,51,52,0,55],
[51,41,41,48,42,52,50,53,50,42,48,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 104, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,45,50,64,34,63,47,57,49,50,53,53],
[57,0,30,51,59,46,57,46,40,45,57,46,48],
[56,71,0,56,64,45,57,55,53,57,70,68,49],
[51,50,45,0,55,38,56,40,35,35,62,46,40],
[37,42,37,46,0,38,47,29,36,29,48,46,27],
[67,55,56,63,63,0,73,51,44,47,61,54,51],
[38,44,44,45,54,28,0,38,35,35,51,44,39],
[54,55,46,61,72,50,63,0,50,49,75,51,55],
[44,61,48,66,65,57,66,51,0,44,67,64,40],
[52,56,44,66,72,54,66,52,57,0,63,54,56],
[51,44,31,39,53,40,50,26,34,38,0,42,35],
[48,55,33,55,55,47,57,50,37,47,59,0,43],
[48,53,52,61,74,50,62,46,61,45,66,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 105, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,73,49,67,54,52,41,50,52,55,69,46],
[41,0,63,42,56,55,54,53,54,44,59,67,40],
[28,38,0,35,41,34,39,34,34,36,50,53,37],
[52,59,66,0,72,61,67,57,57,53,63,60,38],
[34,45,60,29,0,37,39,31,46,37,51,41,38],
[47,46,67,40,64,0,37,41,54,34,57,57,40],
[49,47,62,34,62,64,0,51,51,60,60,68,54],
[60,48,67,44,70,60,50,0,46,61,60,65,43],
[51,47,67,44,55,47,50,55,0,46,70,68,39],
[49,57,65,48,64,67,41,40,55,0,54,61,53],
[46,42,51,38,50,44,41,41,31,47,0,43,33],
[32,34,48,41,60,44,33,36,33,40,58,0,39],
[55,61,64,63,63,61,47,58,62,48,68,62,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 106, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,43,37,43,51,43,41,41,38,48,44,48],
[51,0,51,43,47,52,56,49,50,44,54,48,48],
[58,50,0,43,51,58,52,47,46,50,56,50,48],
[64,58,58,0,56,48,61,55,51,55,59,51,58],
[58,54,50,45,0,50,58,52,45,52,58,58,46],
[50,49,43,53,51,0,54,43,47,50,57,47,49],
[58,45,49,40,43,47,0,46,45,43,57,48,45],
[60,52,54,46,49,58,55,0,50,49,58,52,56],
[60,51,55,50,56,54,56,51,0,45,55,47,54],
[63,57,51,46,49,51,58,52,56,0,61,54,59],
[53,47,45,42,43,44,44,43,46,40,0,43,45],
[57,53,51,50,43,54,53,49,54,47,58,0,57],
[53,53,53,43,55,52,56,45,47,42,56,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 107, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,53,48,50,55,52,53,58,52,50,51,50],
[48,0,49,44,47,48,44,46,51,52,52,41,53],
[48,52,0,50,44,52,47,48,59,42,54,43,58],
[53,57,51,0,47,52,49,49,55,47,55,50,55],
[51,54,57,54,0,54,53,53,60,57,53,49,55],
[46,53,49,49,47,0,43,54,58,46,49,38,54],
[49,57,54,52,48,58,0,50,59,44,53,39,45],
[48,55,53,52,48,47,51,0,50,50,50,38,54],
[43,50,42,46,41,43,42,51,0,45,47,42,48],
[49,49,59,54,44,55,57,51,56,0,54,43,54],
[51,49,47,46,48,52,48,51,54,47,0,42,54],
[50,60,58,51,52,63,62,63,59,58,59,0,56],
[51,48,43,46,46,47,56,47,53,47,47,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 108, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,54,46,45,58,53,49,48,52,49,46,49],
[54,0,53,41,46,52,48,51,43,47,44,47,46],
[47,48,0,40,52,56,56,46,45,44,48,53,47],
[55,60,61,0,54,59,58,50,56,55,54,58,59],
[56,55,49,47,0,55,50,49,48,49,55,51,43],
[43,49,45,42,46,0,56,47,44,37,51,42,45],
[48,53,45,43,51,45,0,43,41,44,52,46,49],
[52,50,55,51,52,54,58,0,49,51,51,57,47],
[53,58,56,45,53,57,60,52,0,49,56,54,51],
[49,54,57,46,52,64,57,50,52,0,48,51,48],
[52,57,53,47,46,50,49,50,45,53,0,51,46],
[55,54,48,43,50,59,55,44,47,50,50,0,42],
[52,55,54,42,58,56,52,54,50,53,55,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 109, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,49,78,38,47,57,51,53,72,31,60,54],
[45,0,45,61,27,39,66,61,52,55,37,57,48],
[52,56,0,67,38,47,59,59,49,67,41,47,43],
[23,40,34,0,31,49,46,30,36,50,41,35,44],
[63,74,63,70,0,64,50,66,79,61,40,55,60],
[54,62,54,52,37,0,52,56,56,53,49,45,52],
[44,35,42,55,51,49,0,30,43,58,46,50,49],
[50,40,42,71,35,45,71,0,48,53,50,45,38],
[48,49,52,65,22,45,58,53,0,59,43,55,67],
[29,46,34,51,40,48,43,48,42,0,40,28,35],
[70,64,60,60,61,52,55,51,58,61,0,49,48],
[41,44,54,66,46,56,51,56,46,73,52,0,47],
[47,53,58,57,41,49,52,63,34,66,53,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 110, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,50,55,61,52,58,59,52,56,58,51,55],
[48,0,51,58,55,55,57,56,50,50,60,54,51],
[51,50,0,58,57,59,63,59,47,55,54,54,56],
[46,43,43,0,52,47,52,50,43,46,47,46,44],
[40,46,44,49,0,53,49,50,43,47,53,50,52],
[49,46,42,54,48,0,50,48,50,51,54,50,54],
[43,44,38,49,52,51,0,53,44,41,54,53,45],
[42,45,42,51,51,53,48,0,40,40,51,52,41],
[49,51,54,58,58,51,57,61,0,51,57,56,60],
[45,51,46,55,54,50,60,61,50,0,59,50,52],
[43,41,47,54,48,47,47,50,44,42,0,45,47],
[50,47,47,55,51,51,48,49,45,51,56,0,46],
[46,50,45,57,49,47,56,60,41,49,54,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 111, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,68,61,66,60,34,39,50,45,56,53,66,52],
[33,0,53,52,44,43,47,51,40,68,53,70,41],
[40,48,0,40,57,39,50,43,38,59,33,60,45],
[35,49,61,0,40,47,45,35,40,55,38,52,45],
[41,57,44,61,0,51,42,45,47,45,43,47,50],
[67,58,62,54,50,0,46,48,59,57,45,62,56],
[62,54,51,56,59,55,0,56,40,74,59,65,41],
[51,50,58,66,56,53,45,0,54,70,63,52,66],
[56,61,63,61,54,42,61,47,0,62,50,66,59],
[45,33,42,46,56,44,27,31,39,0,50,23,40],
[48,48,68,63,58,56,42,38,51,51,0,54,47],
[35,31,41,49,54,39,36,49,35,78,47,0,42],
[49,60,56,56,51,45,60,35,42,61,54,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 112, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,47,58,60,48,53,51,50,52,50,51,52],
[43,0,37,53,53,51,44,49,44,46,43,45,51],
[54,64,0,55,60,47,38,63,48,50,39,54,57],
[43,48,46,0,48,43,38,52,48,48,36,45,42],
[41,48,41,53,0,44,36,46,43,43,42,44,36],
[53,50,54,58,57,0,41,56,45,53,48,48,54],
[48,57,63,63,65,60,0,51,63,57,57,47,54],
[50,52,38,49,55,45,50,0,42,50,48,50,45],
[51,57,53,53,58,56,38,59,0,47,50,41,44],
[49,55,51,53,58,48,44,51,54,0,53,47,51],
[51,58,62,65,59,53,44,53,51,48,0,58,53],
[50,56,47,56,57,53,54,51,60,54,43,0,52],
[49,50,44,59,65,47,47,56,57,50,48,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 113, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,64,64,43,58,48,46,77,80,59,42,58,80],
[37,0,64,43,55,48,24,55,64,55,64,46,55],
[37,37,0,64,46,51,46,80,67,58,67,46,37],
[58,58,37,0,58,48,46,89,80,71,67,64,58],
[43,46,55,43,0,48,46,56,68,61,46,52,46],
[53,53,50,53,53,0,46,50,59,50,53,59,53],
[55,77,55,55,55,55,0,55,86,55,55,46,55],
[24,46,21,12,45,51,46,0,55,21,33,33,24],
[21,37,34,21,33,42,15,46,0,18,33,12,21],
[42,46,43,30,40,51,46,80,83,0,45,24,46],
[59,37,34,34,55,48,46,68,68,56,0,47,38],
[43,55,55,37,49,42,55,68,89,77,54,0,55],
[21,46,64,43,55,48,46,77,80,55,63,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 114, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,37,51,46,42,43,41,45,58,58,55,52,44],
[64,0,54,61,53,57,64,49,59,68,64,54,58],
[50,47,0,53,44,49,45,50,53,49,51,59,45],
[55,40,48,0,45,52,50,53,50,60,57,52,50],
[59,48,57,56,0,61,55,55,67,62,62,58,56],
[58,44,52,49,40,0,53,44,55,60,50,47,50],
[60,37,56,51,46,48,0,47,56,57,59,53,57],
[56,52,51,48,46,57,54,0,58,68,57,59,58],
[43,42,48,51,34,46,45,43,0,58,54,46,38],
[43,33,52,41,39,41,44,33,43,0,46,46,35],
[46,37,50,44,39,51,42,44,47,55,0,42,47],
[49,47,42,49,43,54,48,42,55,55,59,0,43],
[57,43,56,51,45,51,44,43,63,66,54,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 115, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,63,61,72,53,82,65,70,58,59,63,49,50],
[38,0,47,36,41,67,42,58,48,45,40,47,42],
[40,54,0,54,49,65,46,55,67,50,65,47,51],
[29,65,47,0,49,68,50,67,58,44,55,52,48],
[48,60,52,52,0,66,49,67,59,37,62,53,48],
[19,34,36,33,35,0,32,48,37,26,40,41,35],
[36,59,55,51,52,69,0,63,51,48,52,51,53],
[31,43,46,34,34,53,38,0,40,35,43,46,40],
[43,53,34,43,42,64,50,61,0,27,58,45,51],
[42,56,51,57,64,75,53,66,74,0,59,60,43],
[38,61,36,46,39,61,49,58,43,42,0,49,49],
[52,54,54,49,48,60,50,55,56,41,52,0,60],
[51,59,50,53,53,66,48,61,50,58,52,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 116, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,47,58,53,48,49,54,46,59,33,53,55],
[47,0,45,50,51,49,50,51,47,60,36,40,51],
[54,56,0,54,56,59,46,53,54,55,45,45,53],
[43,51,47,0,43,45,46,53,44,47,34,50,44],
[48,50,45,58,0,55,56,56,48,58,40,50,55],
[53,52,42,56,46,0,53,53,51,52,39,44,49],
[52,51,55,55,45,48,0,54,48,55,40,50,51],
[47,50,48,48,45,48,47,0,50,53,35,48,49],
[55,54,47,57,53,50,53,51,0,57,40,47,52],
[42,41,46,54,43,49,46,48,44,0,31,34,47],
[68,65,56,67,61,62,61,66,61,70,0,49,62],
[48,61,56,51,51,57,51,53,54,67,52,0,56],
[46,50,48,57,46,52,50,52,49,54,39,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 117, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,65,50,54,57,63,58,60,56,57,61,58],
[41,0,56,46,39,49,54,42,47,52,45,53,55],
[36,45,0,45,31,58,53,46,58,48,52,61,56],
[51,55,56,0,42,48,56,45,59,51,55,53,56],
[47,62,70,59,0,65,60,56,72,59,61,65,69],
[44,52,43,53,36,0,46,46,51,50,59,47,52],
[38,47,48,45,41,55,0,51,53,48,53,48,59],
[43,59,55,56,45,55,50,0,57,50,64,55,53],
[41,54,43,42,29,50,48,44,0,50,49,49,57],
[45,49,53,50,42,51,53,51,51,0,58,53,46],
[44,56,49,46,40,42,48,37,52,43,0,50,55],
[40,48,40,48,36,54,53,46,52,48,51,0,52],
[43,46,45,45,32,49,42,48,44,55,46,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 118, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,52,62,41,42,49,51,49,47,71,61,58],
[47,0,46,38,43,31,40,45,47,38,54,57,67],
[49,55,0,61,43,55,55,68,60,59,79,71,70],
[39,63,40,0,43,43,45,49,54,29,56,48,54],
[60,58,58,58,0,58,50,72,48,51,73,57,74],
[59,70,46,58,43,0,35,50,60,57,64,54,83],
[52,61,46,56,51,66,0,60,46,51,47,50,65],
[50,56,33,52,29,51,41,0,42,47,56,54,70],
[52,54,41,47,53,41,55,59,0,49,60,57,70],
[54,63,42,72,50,44,50,54,52,0,67,73,74],
[30,47,22,45,28,37,54,45,41,34,0,46,46],
[40,44,30,53,44,47,51,47,44,28,55,0,58],
[43,34,31,47,27,18,36,31,31,27,55,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 119, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,43,35,41,48,44,47,41,48,53,36,53],
[49,0,47,37,44,48,48,48,42,51,45,49,51],
[58,54,0,53,52,55,57,49,56,52,63,50,58],
[66,64,48,0,48,56,51,55,44,41,56,47,54],
[60,57,49,53,0,62,52,51,51,52,62,53,61],
[53,53,46,45,39,0,45,50,46,35,52,43,49],
[57,53,44,50,49,56,0,47,39,47,51,44,52],
[54,53,52,46,50,51,54,0,46,46,58,48,57],
[60,59,45,57,50,55,62,55,0,57,57,57,60],
[53,50,49,60,49,66,54,55,44,0,61,57,55],
[48,56,38,45,39,49,50,43,44,40,0,46,58],
[65,52,51,54,48,58,57,53,44,44,55,0,55],
[48,50,43,47,40,52,49,44,41,46,43,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 120, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,51,37,44,67,54,64,59,48,56,46,65],
[56,0,40,33,46,63,40,58,46,47,54,37,52],
[50,61,0,60,52,58,63,64,66,63,64,72,64],
[64,68,41,0,43,57,67,70,69,68,59,56,72],
[57,55,49,58,0,58,57,63,55,52,70,51,64],
[34,38,43,44,43,0,54,64,56,55,45,42,58],
[47,61,38,34,44,47,0,54,57,49,48,50,57],
[37,43,37,31,38,37,47,0,32,53,38,43,49],
[42,55,35,32,46,45,44,69,0,49,54,41,59],
[53,54,38,33,49,46,52,48,52,0,53,58,46],
[45,47,37,42,31,56,53,63,47,48,0,43,56],
[55,64,29,45,50,59,51,58,60,43,58,0,50],
[36,49,37,29,37,43,44,52,42,55,45,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 121, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,51,46,49,53,49,52,53,53,52,56,53],
[54,0,58,50,48,53,42,49,56,46,49,57,53],
[50,43,0,49,42,58,50,48,55,49,50,52,55],
[55,51,52,0,47,53,53,58,59,53,49,59,56],
[52,53,59,54,0,55,48,52,58,49,52,55,58],
[48,48,43,48,46,0,43,50,53,45,47,50,59],
[52,59,51,48,53,58,0,56,59,52,59,60,56],
[49,52,53,43,49,51,45,0,58,53,43,56,56],
[48,45,46,42,43,48,42,43,0,41,43,48,46],
[48,55,52,48,52,56,49,48,60,0,51,56,58],
[49,52,51,52,49,54,42,58,58,50,0,55,59],
[45,44,49,42,46,51,41,45,53,45,46,0,54],
[48,48,46,45,43,42,45,45,55,43,42,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 122, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,56,58,54,45,53,55,49,54,53,55,52],
[46,0,49,46,52,48,53,48,45,48,52,48,54],
[45,52,0,48,51,48,50,54,52,46,54,49,47],
[43,55,53,0,61,41,45,42,51,56,50,52,53],
[47,49,50,40,0,40,45,47,39,53,53,51,51],
[56,53,53,60,61,0,50,60,43,50,49,58,60],
[48,48,51,56,56,51,0,50,44,51,57,51,49],
[46,53,47,59,54,41,51,0,46,56,47,55,49],
[52,56,49,50,62,58,57,55,0,57,50,54,50],
[47,53,55,45,48,51,50,45,44,0,50,54,52],
[48,49,47,51,48,52,44,54,51,51,0,53,55],
[46,53,52,49,50,43,50,46,47,47,48,0,51],
[49,47,54,48,50,41,52,52,51,49,46,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 123, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,43,60,57,35,38,42,42,38,37,40,46],
[55,0,59,58,72,48,63,45,54,42,34,57,54],
[58,42,0,57,59,44,61,46,46,43,53,51,46],
[41,43,44,0,51,37,44,43,30,41,41,47,59],
[44,29,42,50,0,35,54,35,44,37,46,52,46],
[66,53,57,64,66,0,70,42,49,51,50,57,52],
[63,38,40,57,47,31,0,42,38,39,42,54,51],
[59,56,55,58,66,59,59,0,57,53,54,65,49],
[59,47,55,71,57,52,63,44,0,56,65,54,61],
[63,59,58,60,64,50,62,48,45,0,60,62,57],
[64,67,48,60,55,51,59,47,36,41,0,55,62],
[61,44,50,54,49,44,47,36,47,39,46,0,46],
[55,47,55,42,55,49,50,52,40,44,39,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 124, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,39,50,51,46,48,41,41,46,49,47,45],
[47,0,41,50,58,50,43,50,43,45,51,56,41],
[62,60,0,62,60,60,51,59,56,59,67,50,60],
[51,51,39,0,57,45,46,44,44,42,43,42,40],
[50,43,41,44,0,42,37,38,43,43,46,35,38],
[55,51,41,56,59,0,43,49,47,51,50,51,50],
[53,58,50,55,64,58,0,52,51,46,62,55,57],
[60,51,42,57,63,52,49,0,47,45,55,47,55],
[60,58,45,57,58,54,50,54,0,57,54,48,49],
[55,56,42,59,58,50,55,56,44,0,46,51,50],
[52,50,34,58,55,51,39,46,47,55,0,45,40],
[54,45,51,59,66,50,46,54,53,50,56,0,45],
[56,60,41,61,63,51,44,46,52,51,61,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 125, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,52,49,58,54,56,42,67,33,32,55,41],
[67,0,63,44,64,60,66,41,53,45,66,66,45],
[49,38,0,49,48,50,59,37,46,33,34,43,17],
[52,57,52,0,62,63,67,42,52,42,50,45,45],
[43,37,53,39,0,49,39,23,60,29,32,41,34],
[47,41,51,38,52,0,34,31,50,30,37,44,43],
[45,35,42,34,62,67,0,30,52,48,41,54,50],
[59,60,64,59,78,70,71,0,67,42,53,71,43],
[34,48,55,49,41,51,49,34,0,41,50,49,43],
[68,56,68,59,72,71,53,59,60,0,62,56,48],
[69,35,67,51,69,64,60,48,51,39,0,58,53],
[46,35,58,56,60,57,47,30,52,45,43,0,39],
[60,56,84,56,67,58,51,58,58,53,48,62,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 126, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,63,69,53,57,42,51,60,62,54,60,76],
[55,0,65,52,64,57,51,69,60,48,60,54,72],
[38,36,0,49,53,54,30,38,49,54,52,66,56],
[32,49,52,0,39,59,43,52,61,58,59,61,69],
[48,37,48,62,0,53,32,56,49,54,60,54,53],
[44,44,47,42,48,0,45,52,49,50,60,50,66],
[59,50,71,58,69,56,0,72,71,52,61,67,79],
[50,32,63,49,45,49,29,0,42,52,42,64,62],
[41,41,52,40,52,52,30,59,0,48,52,53,53],
[39,53,47,43,47,51,49,49,53,0,62,55,56],
[47,41,49,42,41,41,40,59,49,39,0,57,60],
[41,47,35,40,47,51,34,37,48,46,44,0,58],
[25,29,45,32,48,35,22,39,48,45,41,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 127, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,45,48,47,40,43,50,43,54,42,47,46],
[55,0,58,53,54,52,50,55,54,67,53,52,60],
[56,43,0,46,47,46,47,50,50,54,47,59,56],
[53,48,55,0,43,46,45,50,50,60,44,51,51],
[54,47,54,58,0,47,53,59,56,53,54,55,55],
[61,49,55,55,54,0,46,60,54,61,54,52,63],
[58,51,54,56,48,55,0,59,50,63,50,48,57],
[51,46,51,51,42,41,42,0,46,48,46,46,54],
[58,47,51,51,45,47,51,55,0,59,55,49,57],
[47,34,47,41,48,40,38,53,42,0,46,46,46],
[59,48,54,57,47,47,51,55,46,55,0,56,52],
[54,49,42,50,46,49,53,55,52,55,45,0,55],
[55,41,45,50,46,38,44,47,44,55,49,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 128, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,48,58,63,48,51,37,30,50,40,57,49],
[62,0,59,48,69,63,51,52,62,54,56,53,61],
[53,42,0,46,60,61,48,46,41,45,51,49,54],
[43,53,55,0,74,66,59,59,46,55,45,45,59],
[38,32,41,27,0,40,33,37,29,27,43,33,43],
[53,38,40,35,61,0,36,50,21,34,39,38,45],
[50,50,53,42,68,65,0,43,43,41,46,46,51],
[64,49,55,42,64,51,58,0,38,48,56,46,70],
[71,39,60,55,72,80,58,63,0,54,61,66,58],
[51,47,56,46,74,67,60,53,47,0,41,54,57],
[61,45,50,56,58,62,55,45,40,60,0,44,52],
[44,48,52,56,68,63,55,55,35,47,57,0,57],
[52,40,47,42,58,56,50,31,43,44,49,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 129, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,43,61,41,55,40,41,40,33,21,54,41],
[74,0,50,80,56,64,58,60,58,48,57,69,54],
[58,51,0,64,47,47,34,49,58,47,42,59,49],
[40,21,37,0,26,42,28,33,32,20,23,43,35],
[60,45,54,75,0,47,54,56,54,41,28,71,52],
[46,37,54,59,54,0,35,39,51,29,29,47,54],
[61,43,67,73,47,66,0,59,67,43,45,74,53],
[60,41,52,68,45,62,42,0,60,27,49,44,58],
[61,43,43,69,47,50,34,41,0,36,37,44,49],
[68,53,54,81,60,72,58,74,65,0,32,66,57],
[80,44,59,78,73,72,56,52,64,69,0,82,65],
[47,32,42,58,30,54,27,57,57,35,19,0,50],
[60,47,52,66,49,47,48,43,52,44,36,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 130, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,55,70,80,65,63,58,51,77,62,48,76],
[43,0,37,44,65,35,42,68,49,69,57,45,60],
[46,64,0,47,55,39,43,76,49,66,68,30,65],
[31,57,54,0,69,43,60,71,59,64,62,50,72],
[21,36,46,32,0,21,52,55,27,50,51,18,52],
[36,66,62,58,80,0,52,67,62,76,61,46,67],
[38,59,58,41,49,49,0,77,42,72,73,40,80],
[43,33,25,30,46,34,24,0,54,53,66,35,54],
[50,52,52,42,74,39,59,47,0,64,57,61,76],
[24,32,35,37,51,25,29,48,37,0,41,43,51],
[39,44,33,39,50,40,28,35,44,60,0,46,49],
[53,56,71,51,83,55,61,66,40,58,55,0,81],
[25,41,36,29,49,34,21,47,25,50,52,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 131, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,30,59,53,41,36,65,54,43,37,56,40],
[67,0,39,67,61,37,34,64,54,57,43,62,50],
[71,62,0,59,62,36,33,70,50,53,44,61,60],
[42,34,42,0,44,34,29,61,36,32,32,58,32],
[48,40,39,57,0,41,36,56,51,59,54,55,49],
[60,64,65,67,60,0,67,72,45,68,38,74,60],
[65,67,68,72,65,34,0,87,51,53,56,75,55],
[36,37,31,40,45,29,14,0,33,19,23,47,27],
[47,47,51,65,50,56,50,68,0,67,60,69,45],
[58,44,48,69,42,33,48,82,34,0,41,74,48],
[64,58,57,69,47,63,45,78,41,60,0,64,53],
[45,39,40,43,46,27,26,54,32,27,37,0,30],
[61,51,41,69,52,41,46,74,56,53,48,71,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 132, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,45,44,26,54,38,44,23,74,11,74,47],
[46,0,43,44,3,43,14,57,11,54,33,77,23],
[56,58,0,68,50,56,38,71,38,89,35,77,47],
[57,57,33,0,57,46,57,89,60,44,57,44,68],
[75,98,51,44,0,43,64,62,78,62,57,74,90],
[47,58,45,55,58,0,46,79,58,56,58,56,58],
[63,87,63,44,37,55,0,74,66,74,45,74,90],
[57,44,30,12,39,22,27,0,24,30,46,56,36],
[78,90,63,41,23,43,35,77,0,74,30,77,77],
[27,47,12,57,39,45,27,71,27,0,24,77,36],
[90,68,66,44,44,43,56,55,71,77,0,77,76],
[27,24,24,57,27,45,27,45,24,24,24,0,24],
[54,78,54,33,11,43,11,65,24,65,25,77,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 133, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,61,56,49,45,52,55,58,51,62,52,58,58],
[40,0,51,44,41,36,53,44,45,56,51,46,48],
[45,50,0,47,46,42,48,45,44,54,51,47,50],
[52,57,54,0,49,46,52,52,48,65,58,60,53],
[56,60,55,52,0,47,57,55,54,64,53,61,59],
[49,65,59,55,54,0,52,57,52,65,58,71,64],
[46,48,53,49,44,49,0,52,48,59,48,46,51],
[43,57,56,49,46,44,49,0,50,61,55,60,58],
[50,56,57,53,47,49,53,51,0,61,58,53,61],
[39,45,47,36,37,36,42,40,40,0,39,43,48],
[49,50,50,43,48,43,53,46,43,62,0,51,51],
[43,55,54,41,40,30,55,41,48,58,50,0,54],
[43,53,51,48,42,37,50,43,40,53,50,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 134, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,46,52,43,49,56,51,64,56,50,46,59],
[49,0,46,52,38,52,56,51,62,53,51,46,55],
[55,55,0,57,46,60,59,51,68,57,46,51,64],
[49,49,44,0,34,40,47,39,59,57,47,48,50],
[58,63,55,67,0,57,51,47,60,55,48,53,65],
[52,49,41,61,44,0,56,48,55,54,48,50,63],
[45,45,42,54,50,45,0,50,56,50,49,44,48],
[50,50,50,62,54,53,51,0,54,50,49,55,63],
[37,39,33,42,41,46,45,47,0,48,45,42,51],
[45,48,44,44,46,47,51,51,53,0,42,49,53],
[51,50,55,54,53,53,52,52,56,59,0,42,54],
[55,55,50,53,48,51,57,46,59,52,59,0,68],
[42,46,37,51,36,38,53,38,50,48,47,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 135, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,55,68,49,63,58,61,55,46,63,54,57,43],
[46,0,53,41,59,60,64,46,50,63,58,44,35],
[33,48,0,44,44,49,61,43,42,53,54,47,32],
[52,60,57,0,61,48,54,45,43,60,56,56,53],
[38,42,57,40,0,58,63,37,41,56,52,42,38],
[43,41,52,53,43,0,52,38,38,46,51,47,31],
[40,37,40,47,38,49,0,41,24,43,53,42,35],
[46,55,58,56,64,63,60,0,49,61,54,56,45],
[55,51,59,58,60,63,77,52,0,57,58,65,48],
[38,38,48,41,45,55,58,40,44,0,49,41,41],
[47,43,47,45,49,50,48,47,43,52,0,53,44],
[44,57,54,45,59,54,59,45,36,60,48,0,43],
[58,66,69,48,63,70,66,56,53,60,57,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 136, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,34,28,29,22,6,28,33,22,33,22,40],
[77,0,77,40,30,29,7,53,52,65,40,41,66],
[67,24,0,53,18,47,31,77,40,82,63,1,77],
[73,61,48,0,24,47,25,49,71,82,82,13,83],
[72,71,83,77,0,47,52,77,48,71,82,48,89],
[79,72,54,54,54,0,78,54,76,76,64,48,76],
[95,94,70,76,49,23,0,76,71,70,58,60,65],
[73,48,24,52,24,47,25,0,46,59,58,13,60],
[68,49,61,30,53,25,30,55,0,71,82,1,67],
[79,36,19,19,30,25,31,42,30,0,41,13,44],
[68,61,38,19,19,37,43,43,19,60,0,13,44],
[79,60,100,88,53,53,41,88,100,88,88,0,100],
[61,35,24,18,12,25,36,41,34,57,57,1,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 137, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,64,71,47,71,78,62,59,65,77,61,73,70],
[37,0,63,57,60,58,47,40,56,61,64,53,41],
[30,38,0,33,40,56,41,37,44,69,53,52,55],
[54,44,68,0,61,57,43,45,56,64,62,61,46],
[30,41,61,40,0,57,40,30,47,68,57,57,42],
[23,43,45,44,44,0,34,50,43,53,55,54,50],
[39,54,60,58,61,67,0,54,58,76,70,65,70],
[42,61,64,56,71,51,47,0,45,64,52,71,49],
[36,45,57,45,54,58,43,56,0,73,54,55,54],
[24,40,32,37,33,48,25,37,28,0,33,51,37],
[40,37,48,39,44,46,31,49,47,68,0,46,54],
[28,48,49,40,44,47,36,30,46,50,55,0,40],
[31,60,46,55,59,51,31,52,47,64,47,61,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 138, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,46,45,44,35,48,39,47,46,53,47,53],
[62,0,50,51,54,45,46,44,44,47,60,48,47],
[55,51,0,49,47,48,45,42,48,48,53,38,46],
[56,50,52,0,46,42,44,42,40,55,45,44,44],
[57,47,54,55,0,48,45,39,45,54,52,45,46],
[66,56,53,59,53,0,48,49,50,58,53,52,58],
[53,55,56,57,56,53,0,40,54,45,63,49,51],
[62,57,59,59,62,52,61,0,54,58,61,49,59],
[54,57,53,61,56,51,47,47,0,41,54,46,58],
[55,54,53,46,47,43,56,43,60,0,52,52,52],
[48,41,48,56,49,48,38,40,47,49,0,45,50],
[54,53,63,57,56,49,52,52,55,49,56,0,59],
[48,54,55,57,55,43,50,42,43,49,51,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 139, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,69,56,68,70,58,50,71,64,58,71,78],
[54,0,52,46,63,70,64,53,85,70,63,69,79],
[32,49,0,52,54,50,61,53,63,68,49,61,70],
[45,55,49,0,60,53,75,60,80,70,46,52,73],
[33,38,47,41,0,35,27,35,43,38,31,50,50],
[31,31,51,48,66,0,34,42,81,48,40,53,56],
[43,37,40,26,74,67,0,35,61,50,51,54,75],
[51,48,48,41,66,59,66,0,77,48,46,76,76],
[30,16,38,21,58,20,40,24,0,32,28,42,40],
[37,31,33,31,63,53,51,53,69,0,46,44,65],
[43,38,52,55,70,61,50,55,73,55,0,61,62],
[30,32,40,49,51,48,47,25,59,57,40,0,50],
[23,22,31,28,51,45,26,25,61,36,39,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 140, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,31,48,42,48,50,40,32,42,50,32,43],
[62,0,44,47,60,57,57,56,41,63,56,54,57],
[70,57,0,69,57,56,57,51,55,75,53,57,47],
[53,54,32,0,48,40,46,49,36,62,37,36,39],
[59,41,44,53,0,48,45,46,43,66,56,44,46],
[53,44,45,61,53,0,46,51,46,62,45,39,51],
[51,44,44,55,56,55,0,49,37,66,48,48,44],
[61,45,50,52,55,50,52,0,44,56,53,45,51],
[69,60,46,65,58,55,64,57,0,74,50,60,54],
[59,38,26,39,35,39,35,45,27,0,34,40,39],
[51,45,48,64,45,56,53,48,51,67,0,48,49],
[69,47,44,65,57,62,53,56,41,61,53,0,57],
[58,44,54,62,55,50,57,50,47,62,52,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 141, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,54,41,27,62,29,47,54,42,58,66,68,41],
[47,0,48,31,56,39,60,61,63,50,60,50,53],
[60,53,0,38,85,50,39,78,60,66,84,68,59],
[74,70,63,0,72,42,44,83,66,57,87,76,59],
[39,45,16,29,0,32,47,41,45,58,63,57,46],
[72,62,51,59,69,0,48,58,65,80,71,81,62],
[54,41,62,57,54,53,0,60,51,48,67,57,71],
[47,40,23,18,60,43,41,0,43,43,56,66,37],
[59,38,41,35,56,36,50,58,0,68,64,64,51],
[43,51,35,44,43,21,53,58,33,0,57,39,50],
[35,41,17,14,38,30,34,45,37,44,0,47,17],
[33,51,33,25,44,20,44,35,37,62,54,0,24],
[60,48,42,42,55,39,30,64,50,51,84,77,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 142, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,50,37,48,49,49,47,48,48,47,48,49],
[50,0,62,60,58,62,60,57,56,53,50,51,52],
[51,39,0,48,44,55,49,46,55,42,49,46,41],
[64,41,53,0,55,57,54,58,59,50,54,59,51],
[53,43,57,46,0,49,48,56,47,45,54,46,48],
[52,39,46,44,52,0,44,45,42,49,49,44,42],
[52,41,52,47,53,57,0,49,51,52,46,46,52],
[54,44,55,43,45,56,52,0,50,53,49,50,48],
[53,45,46,42,54,59,50,51,0,51,52,42,46],
[53,48,59,51,56,52,49,48,50,0,49,50,50],
[54,51,52,47,47,52,55,52,49,52,0,51,48],
[53,50,55,42,55,57,55,51,59,51,50,0,49],
[52,49,60,50,53,59,49,53,55,51,53,52,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 143, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,38,28,25,62,25,49,63,49,28,64,35],
[57,0,36,33,47,53,64,48,80,56,51,54,55],
[63,65,0,69,69,71,63,70,78,54,59,59,44],
[73,68,32,0,68,65,76,64,80,59,54,52,76],
[76,54,32,33,0,63,62,53,83,45,51,47,25],
[39,48,30,36,38,0,38,30,53,46,40,41,18],
[76,37,38,25,39,63,0,42,66,48,22,58,17],
[52,53,31,37,48,71,59,0,75,47,45,49,33],
[38,21,23,21,18,48,35,26,0,43,21,41,35],
[52,45,47,42,56,55,53,54,58,0,31,59,38],
[73,50,42,47,50,61,79,56,80,70,0,51,60],
[37,47,42,49,54,60,43,52,60,42,50,0,24],
[66,46,57,25,76,83,84,68,66,63,41,77,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 144, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,76,62,76,70,53,70,46,70,75,49,61,63],
[25,0,26,55,56,52,29,40,52,80,42,67,42],
[39,75,0,74,40,52,81,42,73,70,45,66,58],
[25,46,27,0,49,49,48,39,50,55,45,51,49],
[31,45,61,52,0,58,51,52,49,63,25,46,66],
[48,49,49,52,43,0,57,30,43,50,29,56,57],
[31,72,20,53,50,44,0,34,46,68,36,68,68],
[55,61,59,62,49,71,67,0,64,67,61,74,57],
[31,49,28,51,52,58,55,37,0,59,35,63,52],
[26,21,31,46,38,51,33,34,42,0,21,38,47],
[52,59,56,56,76,72,65,40,66,80,0,48,68],
[40,34,35,50,55,45,33,27,38,63,53,0,58],
[38,59,43,52,35,44,33,44,49,54,33,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 145, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,51,51,41,40,45,49,39,41,52,41,59],
[54,0,63,53,51,48,55,58,51,57,61,57,65],
[50,38,0,37,34,32,45,45,32,46,44,35,60],
[50,48,64,0,50,45,46,57,45,53,56,44,68],
[60,50,67,51,0,42,54,47,43,46,52,50,61],
[61,53,69,56,59,0,57,50,43,50,56,47,72],
[56,46,56,55,47,44,0,46,41,58,49,37,64],
[52,43,56,44,54,51,55,0,42,49,43,38,63],
[62,50,69,56,58,58,60,59,0,49,60,51,66],
[60,44,55,48,55,51,43,52,52,0,43,49,69],
[49,40,57,45,49,45,52,58,41,58,0,42,64],
[60,44,66,57,51,54,64,63,50,52,59,0,62],
[42,36,41,33,40,29,37,38,35,32,37,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 146, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,60,50,53,68,47,51,37,65,60,65,41],
[55,0,58,57,51,63,62,51,43,52,54,60,55],
[41,43,0,39,45,50,35,42,37,50,41,61,35],
[51,44,62,0,52,44,51,47,43,48,46,55,43],
[48,50,56,49,0,60,55,53,46,45,58,62,57],
[33,38,51,57,41,0,44,49,28,33,38,30,40],
[54,39,66,50,46,57,0,54,36,47,66,68,52],
[50,50,59,54,48,52,47,0,45,46,52,72,49],
[64,58,64,58,55,73,65,56,0,56,49,73,55],
[36,49,51,53,56,68,54,55,45,0,44,66,50],
[41,47,60,55,43,63,35,49,52,57,0,62,65],
[36,41,40,46,39,71,33,29,28,35,39,0,38],
[60,46,66,58,44,61,49,52,46,51,36,63,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 147, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,57,49,55,49,41,66,53,56,48,49,60],
[45,0,54,45,54,47,50,48,55,41,42,46,52],
[44,47,0,44,48,44,45,56,49,45,38,41,51],
[52,56,57,0,54,56,55,67,57,48,52,48,51],
[46,47,53,47,0,50,43,55,50,48,39,39,48],
[52,54,57,45,51,0,54,61,56,43,42,42,52],
[60,51,56,46,58,47,0,59,52,54,46,53,52],
[35,53,45,34,46,40,42,0,49,38,40,34,43],
[48,46,52,44,51,45,49,52,0,48,40,42,47],
[45,60,56,53,53,58,47,63,53,0,48,51,49],
[53,59,63,49,62,59,55,61,61,53,0,46,57],
[52,55,60,53,62,59,48,67,59,50,55,0,57],
[41,49,50,50,53,49,49,58,54,52,44,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 148, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,56,48,61,57,56,70,44,63,55,50,43],
[44,0,44,52,51,58,48,42,57,68,40,43,38],
[45,57,0,55,56,60,62,59,62,65,53,43,57],
[53,49,46,0,64,61,56,66,59,64,37,59,55],
[40,50,45,37,0,51,43,56,39,52,47,42,35],
[44,43,41,40,50,0,40,52,48,61,42,48,41],
[45,53,39,45,58,61,0,54,48,63,41,51,48],
[31,59,42,35,45,49,47,0,42,51,40,45,37],
[57,44,39,42,62,53,53,59,0,60,39,56,38],
[38,33,36,37,49,40,38,50,41,0,37,32,29],
[46,61,48,64,54,59,60,61,62,64,0,44,45],
[51,58,58,42,59,53,50,56,45,69,57,0,51],
[58,63,44,46,66,60,53,64,63,72,56,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 149, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,37,37,37,50,44,40,44,45,41,46,43],
[59,0,43,41,37,48,54,42,52,53,48,50,47],
[64,58,0,47,52,50,60,51,59,56,55,56,53],
[64,60,54,0,45,56,53,54,56,61,61,62,51],
[64,64,49,56,0,55,55,52,58,52,60,66,54],
[51,53,51,45,46,0,53,44,56,46,47,54,49],
[57,47,41,48,46,48,0,48,52,53,47,47,44],
[61,59,50,47,49,57,53,0,60,50,54,56,47],
[57,49,42,45,43,45,49,41,0,47,50,53,48],
[56,48,45,40,49,55,48,51,54,0,52,45,46],
[60,53,46,40,41,54,54,47,51,49,0,53,51],
[55,51,45,39,35,47,54,45,48,56,48,0,42],
[58,54,48,50,47,52,57,54,53,55,50,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 150, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,53,47,46,49,47,54,54,40,47,52,52],
[51,0,55,45,47,48,50,58,57,42,46,53,46],
[48,46,0,37,40,42,47,45,43,33,44,45,35],
[54,56,64,0,49,58,56,56,52,49,49,55,54],
[55,54,61,52,0,52,52,60,48,52,56,51,53],
[52,53,59,43,49,0,54,50,52,41,62,57,53],
[54,51,54,45,49,47,0,49,46,43,46,38,48],
[47,43,56,45,41,51,52,0,43,44,49,46,47],
[47,44,58,49,53,49,55,58,0,46,51,55,45],
[61,59,68,52,49,60,58,57,55,0,53,63,56],
[54,55,57,52,45,39,55,52,50,48,0,52,51],
[49,48,56,46,50,44,63,55,46,38,49,0,52],
[49,55,66,47,48,48,53,54,56,45,50,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 151, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,49,42,39,42,42,43,36,40,37,43,35],
[71,0,62,61,50,57,51,59,50,56,46,58,50],
[52,39,0,47,42,49,47,43,42,49,31,44,49],
[59,40,54,0,47,46,44,37,40,50,46,51,47],
[62,51,59,54,0,53,54,59,51,53,45,50,53],
[59,44,52,55,48,0,51,47,42,54,48,40,56],
[59,50,54,57,47,50,0,55,48,57,37,52,40],
[58,42,58,64,42,54,46,0,42,63,39,60,47],
[65,51,59,61,50,59,53,59,0,51,58,62,54],
[61,45,52,51,48,47,44,38,50,0,36,44,38],
[64,55,70,55,56,53,64,62,43,65,0,69,57],
[58,43,57,50,51,61,49,41,39,57,32,0,43],
[66,51,52,54,48,45,61,54,47,63,44,58,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 152, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,56,48,48,41,42,44,51,44,55,44,39],
[50,0,57,53,49,40,45,52,47,48,55,47,36],
[45,44,0,43,51,45,46,39,52,48,50,42,49],
[53,48,58,0,53,41,56,54,55,55,55,50,41],
[53,52,50,48,0,55,51,51,51,50,53,48,45],
[60,61,56,60,46,0,53,49,56,58,59,53,56],
[59,56,55,45,50,48,0,46,58,53,47,51,48],
[57,49,62,47,50,52,55,0,54,47,54,52,47],
[50,54,49,46,50,45,43,47,0,39,50,55,45],
[57,53,53,46,51,43,48,54,62,0,47,46,49],
[46,46,51,46,48,42,54,47,51,54,0,48,53],
[57,54,59,51,53,48,50,49,46,55,53,0,44],
[62,65,52,60,56,45,53,54,56,52,48,57,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 153, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,51,53,67,54,54,52,55,47,44,57,41],
[45,0,41,46,60,42,46,43,43,54,49,54,51],
[50,60,0,59,63,50,51,57,59,53,67,67,58],
[48,55,42,0,61,44,54,48,58,58,57,61,38],
[34,41,38,40,0,38,30,36,29,32,38,41,36],
[47,59,51,57,63,0,45,55,57,55,46,54,49],
[47,55,50,47,71,56,0,51,53,53,42,58,54],
[49,58,44,53,65,46,50,0,48,31,52,57,37],
[46,58,42,43,72,44,48,53,0,52,49,53,40],
[54,47,48,43,69,46,48,70,49,0,49,66,57],
[57,52,34,44,63,55,59,49,52,52,0,55,51],
[44,47,34,40,60,47,43,44,48,35,46,0,41],
[60,50,43,63,65,52,47,64,61,44,50,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 154, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,49,49,57,52,55,56,47,51,59,55,55],
[45,0,49,44,51,43,45,56,49,50,55,54,48],
[52,52,0,51,54,50,51,55,48,52,56,48,47],
[52,57,50,0,60,59,55,51,51,53,56,63,48],
[44,50,47,41,0,38,44,44,38,46,47,48,38],
[49,58,51,42,63,0,56,56,48,48,59,58,56],
[46,56,50,46,57,45,0,54,48,53,55,50,51],
[45,45,46,50,57,45,47,0,37,51,50,43,43],
[54,52,53,50,63,53,53,64,0,51,54,59,54],
[50,51,49,48,55,53,48,50,50,0,54,51,47],
[42,46,45,45,54,42,46,51,47,47,0,50,46],
[46,47,53,38,53,43,51,58,42,50,51,0,47],
[46,53,54,53,63,45,50,58,47,54,55,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 155, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,30,45,39,71,42,40,49,54,51,30,30],
[62,0,49,68,63,79,63,58,75,48,48,58,45],
[71,52,0,65,55,71,72,70,72,64,56,64,43],
[56,33,36,0,61,66,55,64,79,56,41,45,38],
[62,38,46,40,0,72,58,73,67,41,42,46,44],
[30,22,30,35,29,0,29,36,55,44,15,46,17],
[59,38,29,46,43,72,0,60,80,52,39,44,43],
[61,43,31,37,28,65,41,0,45,44,38,55,31],
[52,26,29,22,34,46,21,56,0,39,26,41,22],
[47,53,37,45,60,57,49,57,62,0,45,55,35],
[50,53,45,60,59,86,62,63,75,56,0,58,64],
[71,43,37,56,55,55,57,46,60,46,43,0,33],
[71,56,58,63,57,84,58,70,79,66,37,68,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 156, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,53,61,55,51,57,54,63,62,61,50,52],
[59,0,48,60,60,59,73,53,59,69,68,58,50],
[48,53,0,56,46,50,54,67,64,64,53,55,55],
[40,41,45,0,34,24,40,47,49,57,45,42,58],
[46,41,55,67,0,35,59,42,53,61,54,50,53],
[50,42,51,77,66,0,48,56,59,52,60,56,63],
[44,28,47,61,42,53,0,41,50,55,50,49,50],
[47,48,34,54,59,45,60,0,64,60,69,47,50],
[38,42,37,52,48,42,51,37,0,63,47,44,38],
[39,32,37,44,40,49,46,41,38,0,48,50,62],
[40,33,48,56,47,41,51,32,54,53,0,48,48],
[51,43,46,59,51,45,52,54,57,51,53,0,46],
[49,51,46,43,48,38,51,51,63,39,53,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 157, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,67,48,46,51,62,54,54,52,56,48,64],
[58,0,69,49,56,51,59,55,62,57,68,53,68],
[34,32,0,47,32,43,44,37,41,44,34,50,48],
[53,52,54,0,51,49,59,51,54,43,57,49,63],
[55,45,69,50,0,54,60,46,55,60,52,67,64],
[50,50,58,52,47,0,55,48,56,57,53,59,71],
[39,42,57,42,41,46,0,41,44,45,36,46,64],
[47,46,64,50,55,53,60,0,56,60,57,47,67],
[47,39,60,47,46,45,57,45,0,54,38,59,68],
[49,44,57,58,41,44,56,41,47,0,45,62,66],
[45,33,67,44,49,48,65,44,63,56,0,53,63],
[53,48,51,52,34,42,55,54,42,39,48,0,59],
[37,33,53,38,37,30,37,34,33,35,38,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 158, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,50,47,52,52,41,50,54,40,47,49,51],
[48,0,53,46,51,54,41,49,60,47,46,51,51],
[51,48,0,43,54,53,49,51,54,50,46,49,53],
[54,55,58,0,59,55,52,53,57,49,47,52,53],
[49,50,47,42,0,53,39,40,48,38,38,50,48],
[49,47,48,46,48,0,40,47,49,43,43,46,51],
[60,60,52,49,62,61,0,49,62,49,48,57,54],
[51,52,50,48,61,54,52,0,58,55,50,55,52],
[47,41,47,44,53,52,39,43,0,37,38,43,44],
[61,54,51,52,63,58,52,46,64,0,51,56,56],
[54,55,55,54,63,58,53,51,63,50,0,53,60],
[52,50,52,49,51,55,44,46,58,45,48,0,52],
[50,50,48,48,53,50,47,49,57,45,41,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 159, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,45,42,49,43,52,56,64,65,36,57,44],
[56,0,57,59,53,63,55,58,60,70,42,51,57],
[56,44,0,52,63,60,56,54,58,63,51,48,40],
[59,42,49,0,53,45,52,53,47,54,51,52,44],
[52,48,38,48,0,44,38,53,54,47,26,46,56],
[58,38,41,56,57,0,41,62,58,67,46,45,56],
[49,46,45,49,63,60,0,69,52,54,59,50,59],
[45,43,47,48,48,39,32,0,55,51,28,48,46],
[37,41,43,54,47,43,49,46,0,44,44,45,42],
[36,31,38,47,54,34,47,50,57,0,34,39,45],
[65,59,50,50,75,55,42,73,57,67,0,61,62],
[44,50,53,49,55,56,51,53,56,62,40,0,51],
[57,44,61,57,45,45,42,55,59,56,39,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 160, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,50,55,56,59,64,54,51,45,50,50,52],
[53,0,60,65,54,67,69,61,59,49,56,53,63],
[51,41,0,50,57,52,59,48,53,46,43,45,53],
[46,36,51,0,50,56,56,50,50,40,50,45,56],
[45,47,44,51,0,52,51,51,48,42,42,45,45],
[42,34,49,45,49,0,47,49,45,43,39,44,49],
[37,32,42,45,50,54,0,45,45,34,44,46,46],
[47,40,53,51,50,52,56,0,54,39,44,49,44],
[50,42,48,51,53,56,56,47,0,38,47,48,41],
[56,52,55,61,59,58,67,62,63,0,52,49,65],
[51,45,58,51,59,62,57,57,54,49,0,45,54],
[51,48,56,56,56,57,55,52,53,52,56,0,59],
[49,38,48,45,56,52,55,57,60,36,47,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 161, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,45,49,45,59,57,60,66,43,48,57,54],
[69,0,55,50,51,55,61,55,67,55,59,64,51],
[56,46,0,47,50,56,50,52,60,37,53,50,49],
[52,51,54,0,43,58,55,52,56,49,61,66,53],
[56,50,51,58,0,55,49,54,60,50,51,61,51],
[42,46,45,43,46,0,48,50,55,43,44,54,52],
[44,40,51,46,52,53,0,48,60,44,55,62,50],
[41,46,49,49,47,51,53,0,60,43,52,60,48],
[35,34,41,45,41,46,41,41,0,40,39,52,34],
[58,46,64,52,51,58,57,58,61,0,54,62,52],
[53,42,48,40,50,57,46,49,62,47,0,62,46],
[44,37,51,35,40,47,39,41,49,39,39,0,46],
[47,50,52,48,50,49,51,53,67,49,55,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 162, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,41,32,27,48,30,49,65,51,47,49,50,65],
[60,0,37,37,54,24,48,60,71,52,55,51,62],
[69,64,0,57,48,61,65,59,55,51,57,52,74],
[74,64,44,0,46,50,63,66,73,60,74,59,76],
[53,47,53,55,0,35,48,72,55,63,70,40,68],
[71,77,40,51,66,0,68,68,64,62,62,66,72],
[52,53,36,38,53,33,0,52,62,48,48,35,58],
[36,41,42,35,29,33,49,0,52,41,35,45,48],
[50,30,46,28,46,37,39,49,0,61,64,39,72],
[54,49,50,41,38,39,53,60,40,0,53,42,58],
[52,46,44,27,31,39,53,66,37,48,0,45,55],
[51,50,49,42,61,35,66,56,62,59,56,0,74],
[36,39,27,25,33,29,43,53,29,43,46,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 163, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,49,46,52,45,52,42,50,37,43,48,47],
[53,0,52,56,47,53,64,45,52,35,47,49,53],
[52,49,0,47,52,50,45,36,48,48,44,49,54],
[55,45,54,0,51,50,56,44,47,50,53,53,53],
[49,54,49,50,0,47,47,46,54,48,44,46,54],
[56,48,51,51,54,0,51,42,50,44,44,50,41],
[49,37,56,45,54,50,0,39,42,40,43,48,45],
[59,56,65,57,55,59,62,0,61,51,54,56,48],
[51,49,53,54,47,51,59,40,0,35,45,56,47],
[64,66,53,51,53,57,61,50,66,0,55,57,56],
[58,54,57,48,57,57,58,47,56,46,0,54,53],
[53,52,52,48,55,51,53,45,45,44,47,0,54],
[54,48,47,48,47,60,56,53,54,45,48,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 164, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,57,46,55,46,47,53,49,46,48,46,55],
[52,0,57,51,53,45,51,53,49,46,52,48,53],
[44,44,0,51,55,44,41,39,43,45,44,40,48],
[55,50,50,0,55,48,50,53,51,45,52,50,50],
[46,48,46,46,0,47,49,44,41,37,43,42,48],
[55,56,57,53,54,0,51,48,38,47,45,47,51],
[54,50,60,51,52,50,0,52,47,45,45,44,50],
[48,48,62,48,57,53,49,0,51,47,54,52,55],
[52,52,58,50,60,63,54,50,0,50,52,49,56],
[55,55,56,56,64,54,56,54,51,0,48,47,53],
[53,49,57,49,58,56,56,47,49,53,0,50,54],
[55,53,61,51,59,54,57,49,52,54,51,0,48],
[46,48,53,51,53,50,51,46,45,48,47,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 165, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,58,39,48,42,38,32,35,60,41,39,32,43],
[43,0,42,32,43,66,48,52,53,54,66,59,51],
[62,59,0,46,60,60,44,51,61,57,77,48,70],
[53,69,55,0,52,62,61,38,50,44,51,63,52],
[59,58,41,49,0,38,42,38,62,43,42,42,70],
[63,35,41,39,63,0,56,46,47,45,53,39,59],
[69,53,57,40,59,45,0,37,51,41,54,51,57],
[66,49,50,63,63,55,64,0,64,70,44,34,59],
[41,48,40,51,39,54,50,37,0,53,49,49,57],
[60,47,44,57,58,56,60,31,48,0,56,46,55],
[62,35,24,50,59,48,47,57,52,45,0,26,52],
[69,42,53,38,59,62,50,67,52,55,75,0,52],
[58,50,31,49,31,42,44,42,44,46,49,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 166, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,53,49,50,50,55,51,57,53,45,51,56],
[45,0,51,47,50,43,47,44,47,52,45,41,52],
[48,50,0,45,49,42,47,46,58,45,42,43,47],
[52,54,56,0,55,51,54,50,60,50,48,41,56],
[51,51,52,46,0,45,49,47,62,57,45,52,50],
[51,58,59,50,56,0,56,46,59,56,51,50,45],
[46,54,54,47,52,45,0,50,60,53,50,50,55],
[50,57,55,51,54,55,51,0,55,60,48,46,57],
[44,54,43,41,39,42,41,46,0,46,43,39,39],
[48,49,56,51,44,45,48,41,55,0,48,44,54],
[56,56,59,53,56,50,51,53,58,53,0,42,54],
[50,60,58,60,49,51,51,55,62,57,59,0,52],
[45,49,54,45,51,56,46,44,62,47,47,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 167, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,37,50,54,46,45,44,52,43,42,49,49,40],
[64,0,60,60,59,44,53,62,53,55,63,60,51],
[51,41,0,49,52,50,51,57,43,42,52,56,46],
[47,41,52,0,41,48,43,51,43,49,49,53,47],
[55,42,49,60,0,48,42,55,45,48,51,56,45],
[56,57,51,53,53,0,48,56,50,44,51,55,48],
[57,48,50,58,59,53,0,54,49,56,56,61,49],
[49,39,44,50,46,45,47,0,36,46,43,52,47],
[58,48,58,58,56,51,52,65,0,41,51,54,49],
[59,46,59,52,53,57,45,55,60,0,58,58,49],
[52,38,49,52,50,50,45,58,50,43,0,49,40],
[52,41,45,48,45,46,40,49,47,43,52,0,47],
[61,50,55,54,56,53,52,54,52,52,61,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 168, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,60,63,44,63,87,57,30,53,80,68,77,57],
[41,0,67,38,60,62,69,66,59,78,57,65,71],
[38,34,0,58,45,57,46,36,52,61,44,45,52],
[57,63,43,0,44,68,68,60,50,72,58,64,64],
[38,41,56,57,0,68,49,41,50,65,50,44,30],
[14,39,44,33,33,0,41,31,58,58,55,36,33],
[44,32,55,33,52,60,0,62,66,79,62,72,36],
[71,35,65,41,60,70,39,0,52,71,74,76,39],
[48,42,49,51,51,43,35,49,0,58,62,76,42],
[21,23,40,29,36,43,22,30,43,0,52,60,29],
[33,44,57,43,51,46,39,27,39,49,0,62,47],
[24,36,56,37,57,65,29,25,25,41,39,0,23],
[44,30,49,37,71,68,65,62,59,72,54,78,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 169, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,54,53,54,61,54,53,49,57,49,50,52],
[52,0,60,58,52,63,59,59,50,58,52,49,60],
[47,41,0,54,51,54,48,59,49,49,52,43,52],
[48,43,47,0,47,52,51,56,52,50,51,51,53],
[47,49,50,54,0,54,50,48,51,52,51,48,49],
[40,38,47,49,47,0,46,49,40,46,38,45,48],
[47,42,53,50,51,55,0,55,49,49,49,48,55],
[48,42,42,45,53,52,46,0,46,53,40,45,48],
[52,51,52,49,50,61,52,55,0,60,49,55,48],
[44,43,52,51,49,55,52,48,41,0,52,44,50],
[52,49,49,50,50,63,52,61,52,49,0,50,50],
[51,52,58,50,53,56,53,56,46,57,51,0,56],
[49,41,49,48,52,53,46,53,53,51,51,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 170, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,53,50,47,52,47,55,44,65,49,47,47],
[52,0,52,48,51,53,54,47,51,53,50,45,52],
[48,49,0,38,49,55,45,55,43,55,44,40,45],
[51,53,63,0,56,58,55,56,58,55,52,50,55],
[54,50,52,45,0,53,50,51,48,51,43,45,49],
[49,48,46,43,48,0,47,54,43,58,47,47,51],
[54,47,56,46,51,54,0,62,47,52,52,43,54],
[46,54,46,45,50,47,39,0,51,56,39,43,44],
[57,50,58,43,53,58,54,50,0,53,42,53,43],
[36,48,46,46,50,43,49,45,48,0,49,39,48],
[52,51,57,49,58,54,49,62,59,52,0,47,48],
[54,56,61,51,56,54,58,58,48,62,54,0,46],
[54,49,56,46,52,50,47,57,58,53,53,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 171, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,48,64,63,50,47,33,50,57,41,46,46,38],
[53,0,61,64,61,47,48,54,54,48,71,42,66],
[37,40,0,68,55,43,29,46,50,39,46,57,46],
[38,37,33,0,45,31,25,47,27,23,37,40,31],
[51,40,46,56,0,40,28,40,40,36,34,49,27],
[54,54,58,70,61,0,54,61,36,55,54,49,42],
[68,53,72,76,73,47,0,71,56,56,58,71,52],
[51,47,55,54,61,40,30,0,44,47,42,48,33],
[44,47,51,74,61,65,45,57,0,54,41,43,42],
[60,53,62,78,65,46,45,54,47,0,39,51,50],
[55,30,55,64,67,47,43,59,60,62,0,58,44],
[55,59,44,61,52,52,30,53,58,50,43,0,42],
[63,35,55,70,74,59,49,68,59,51,57,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 172, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,57,49,50,60,56,54,49,54,62,47,55],
[39,0,40,40,50,48,39,36,46,45,49,43,60],
[44,61,0,53,54,55,55,50,61,46,54,49,60],
[52,61,48,0,59,56,42,52,53,42,49,43,67],
[51,51,47,42,0,54,42,50,56,54,57,53,60],
[41,53,46,45,47,0,45,51,57,45,58,35,55],
[45,62,46,59,59,56,0,48,49,44,54,43,56],
[47,65,51,49,51,50,53,0,46,50,56,38,61],
[52,55,40,48,45,44,52,55,0,47,41,40,50],
[47,56,55,59,47,56,57,51,54,0,63,50,66],
[39,52,47,52,44,43,47,45,60,38,0,41,56],
[54,58,52,58,48,66,58,63,61,51,60,0,59],
[46,41,41,34,41,46,45,40,51,35,45,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 173, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,50,64,54,56,55,57,46,63,48,53,52],
[44,0,43,57,53,58,53,64,54,57,42,57,50],
[51,58,0,64,61,58,54,60,58,56,46,55,61],
[37,44,37,0,50,49,44,47,41,61,40,46,47],
[47,48,40,51,0,53,51,59,44,51,51,59,46],
[45,43,43,52,48,0,55,50,53,47,37,40,47],
[46,48,47,57,50,46,0,57,46,56,55,54,54],
[44,37,41,54,42,51,44,0,37,47,41,48,43],
[55,47,43,60,57,48,55,64,0,56,44,47,53],
[38,44,45,40,50,54,45,54,45,0,42,45,48],
[53,59,55,61,50,64,46,60,57,59,0,64,69],
[48,44,46,55,42,61,47,53,54,56,37,0,54],
[49,51,40,54,55,54,47,58,48,53,32,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 174, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,46,53,45,51,47,62,72,53,47,57,55,43],
[55,0,61,61,58,51,67,59,55,57,69,46,60],
[48,40,0,37,43,35,53,57,47,41,45,47,43],
[56,40,64,0,54,35,50,64,43,49,46,46,38],
[50,43,58,47,0,47,63,55,55,44,46,44,51],
[54,50,66,66,54,0,67,58,56,68,57,64,50],
[39,34,48,51,38,34,0,42,40,38,46,46,28],
[29,42,44,37,46,43,59,0,53,39,56,42,43],
[48,46,54,58,46,45,61,48,0,53,55,44,34],
[54,44,60,52,57,33,63,62,48,0,62,59,36],
[44,32,56,55,55,44,55,45,46,39,0,48,39],
[46,55,54,55,57,37,55,59,57,42,53,0,37],
[58,41,58,63,50,51,73,58,67,65,62,64,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 175, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,56,57,58,61,55,57,55,59,63,59,50],
[42,0,46,48,45,51,55,45,59,55,42,41,47],
[45,55,0,56,55,67,61,51,48,61,55,57,55],
[44,53,45,0,53,58,64,56,47,59,50,50,44],
[43,56,46,48,0,56,49,54,48,65,50,47,47],
[40,50,34,43,45,0,50,46,50,46,47,45,37],
[46,46,40,37,52,51,0,53,52,49,42,50,40],
[44,56,50,45,47,55,48,0,46,52,49,44,40],
[46,42,53,54,53,51,49,55,0,54,54,47,39],
[42,46,40,42,36,55,52,49,47,0,48,52,38],
[38,59,46,51,51,54,59,52,47,53,0,43,51],
[42,60,44,51,54,56,51,57,54,49,58,0,47],
[51,54,46,57,54,64,61,61,62,63,50,54,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 176, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,66,47,51,60,55,60,65,67,56,58,57,65],
[35,0,48,45,40,47,39,51,51,37,46,45,46],
[54,53,0,46,51,50,46,51,64,40,51,44,47],
[50,56,55,0,51,49,49,56,56,47,53,52,52],
[41,61,50,50,0,44,49,55,61,52,51,48,49],
[46,54,51,52,57,0,55,61,59,53,57,53,55],
[41,62,55,52,52,46,0,61,52,51,56,52,52],
[36,50,50,45,46,40,40,0,53,43,52,45,54],
[34,50,37,45,40,42,49,48,0,35,45,47,42],
[45,64,61,54,49,48,50,58,66,0,53,58,57],
[43,55,50,48,50,44,45,49,56,48,0,48,55],
[44,56,57,49,53,48,49,56,54,43,53,0,52],
[36,55,54,49,52,46,49,47,59,44,46,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 177, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,78,46,45,64,65,60,51,57,45,51,59,64],
[23,0,36,27,45,54,41,29,28,30,39,50,42],
[55,65,0,57,64,62,68,74,65,37,60,62,69],
[56,74,44,0,62,66,52,61,75,54,87,61,56],
[37,56,37,39,0,58,49,54,53,38,62,46,47],
[36,47,39,35,43,0,47,57,42,39,47,53,30],
[41,60,33,49,52,54,0,47,51,34,50,51,50],
[50,72,27,40,47,44,54,0,43,26,55,51,39],
[44,73,36,26,48,59,50,58,0,35,58,60,52],
[56,71,64,47,63,62,67,75,66,0,76,64,61],
[50,62,41,14,39,54,51,46,43,25,0,56,46],
[42,51,39,40,55,48,50,50,41,37,45,0,39],
[37,59,32,45,54,71,51,62,49,40,55,62,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 178, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,52,20,31,18,31,57,32,18,36,18,16,45],
[49,0,38,49,55,49,61,66,54,54,49,54,29],
[81,63,0,74,61,70,76,57,41,47,25,48,61],
[70,52,27,0,52,57,70,43,45,62,51,50,75],
[83,46,40,49,0,26,51,51,39,45,39,36,39],
[70,52,31,44,75,0,46,71,19,37,14,31,31],
[44,40,25,31,50,55,0,30,43,49,38,41,18],
[69,35,44,58,50,30,71,0,32,30,13,55,32],
[83,47,60,56,62,82,58,69,0,87,40,60,71],
[65,47,54,39,56,64,52,71,14,0,29,50,29],
[83,52,76,50,62,87,63,88,61,72,0,60,64],
[85,47,53,51,65,70,60,46,41,51,41,0,41],
[56,72,40,26,62,70,83,69,30,72,37,60,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 179, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,57,53,62,58,55,51,56,41,53,36,48,47],
[44,0,47,50,43,55,57,54,31,61,40,46,49],
[48,54,0,36,66,67,52,55,38,57,42,39,33],
[39,51,65,0,67,51,49,57,31,52,53,42,44],
[43,58,35,34,0,36,40,34,35,43,36,51,27],
[46,46,34,50,65,0,49,52,34,42,54,42,32],
[50,44,49,52,61,52,0,54,51,46,40,52,38],
[45,47,46,44,67,49,47,0,26,51,36,46,45],
[60,70,63,70,66,67,50,75,0,64,44,64,47],
[48,40,44,49,58,59,55,50,37,0,29,45,29],
[65,61,59,48,65,47,61,65,57,72,0,67,52],
[53,55,62,59,50,59,49,55,37,56,34,0,46],
[54,52,68,57,74,69,63,56,54,72,49,55,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 180, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,51,51,59,61,47,44,52,53,49,50,59],
[48,0,45,44,59,54,45,47,48,52,48,59,52],
[50,56,0,43,53,54,49,47,45,53,53,58,56],
[50,57,58,0,62,64,53,51,58,56,51,58,59],
[42,42,48,39,0,52,41,41,43,41,39,53,49],
[40,47,47,37,49,0,44,45,42,49,48,53,47],
[54,56,52,48,60,57,0,54,57,54,48,54,66],
[57,54,54,50,60,56,47,0,57,67,55,58,60],
[49,53,56,43,58,59,44,44,0,55,51,57,56],
[48,49,48,45,60,52,47,34,46,0,52,56,56],
[52,53,48,50,62,53,53,46,50,49,0,58,57],
[51,42,43,43,48,48,47,43,44,45,43,0,48],
[42,49,45,42,52,54,35,41,45,45,44,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 181, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,56,56,55,51,70,54,48,49,56,68,62,47],
[45,0,50,53,51,56,61,55,45,57,60,68,51],
[45,51,0,41,51,56,53,47,48,44,56,62,43],
[46,48,60,0,50,73,56,55,66,63,68,74,42],
[50,50,50,51,0,52,57,48,47,58,51,67,45],
[31,45,45,28,49,0,54,45,49,46,55,64,35],
[47,40,48,45,44,47,0,58,52,36,54,64,38],
[53,46,54,46,53,56,43,0,57,56,54,60,41],
[52,56,53,35,54,52,49,44,0,54,58,52,49],
[45,44,57,38,43,55,65,45,47,0,46,52,45],
[33,41,45,33,50,46,47,47,43,55,0,56,44],
[39,33,39,27,34,37,37,41,49,49,45,0,42],
[54,50,58,59,56,66,63,60,52,56,57,59,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 182, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,55,55,46,58,50,58,50,54,61,56,60],
[52,0,57,57,53,61,50,57,51,58,57,55,55],
[46,44,0,48,36,52,37,50,47,45,51,52,48],
[46,44,53,0,46,51,48,51,50,54,56,48,53],
[55,48,65,55,0,60,54,55,56,65,58,56,62],
[43,40,49,50,41,0,49,48,47,47,48,45,49],
[51,51,64,53,47,52,0,52,52,60,53,53,63],
[43,44,51,50,46,53,49,0,49,54,51,53,55],
[51,50,54,51,45,54,49,52,0,48,57,52,58],
[47,43,56,47,36,54,41,47,53,0,49,47,54],
[40,44,50,45,43,53,48,50,44,52,0,53,53],
[45,46,49,53,45,56,48,48,49,54,48,0,52],
[41,46,53,48,39,52,38,46,43,47,48,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 183, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,68,65,61,35,28,38,68,42,62,71,61,60],
[33,0,63,52,34,21,39,48,41,46,61,61,76],
[36,38,0,52,28,9,29,48,20,40,38,42,46],
[40,49,49,0,33,35,12,46,43,24,40,58,64],
[66,67,73,68,0,37,46,77,48,52,54,61,66],
[73,80,92,66,64,0,47,83,54,46,63,79,77],
[63,62,72,89,55,54,0,82,46,43,52,71,97],
[33,53,53,55,24,18,19,0,33,27,40,39,30],
[59,60,81,58,53,47,55,68,0,56,66,71,56],
[39,55,61,77,49,55,58,74,45,0,74,80,74],
[30,40,63,61,47,38,49,61,35,27,0,61,77],
[40,40,59,43,40,22,30,62,30,21,40,0,29],
[41,25,55,37,35,24,4,71,45,27,24,72,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 184, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,54,49,50,48,44,45,48,40,40,58,54],
[50,0,52,46,47,42,45,41,37,43,42,64,54],
[47,49,0,50,55,36,51,48,37,37,37,54,48],
[52,55,51,0,63,43,49,46,47,41,43,56,51],
[51,54,46,38,0,44,49,43,49,45,52,52,54],
[53,59,65,58,57,0,50,54,49,55,56,67,56],
[57,56,50,52,52,51,0,43,45,41,47,66,57],
[56,60,53,55,58,47,58,0,57,51,52,63,58],
[53,64,64,54,52,52,56,44,0,46,59,71,58],
[61,58,64,60,56,46,60,50,55,0,54,69,51],
[61,59,64,58,49,45,54,49,42,47,0,66,57],
[43,37,47,45,49,34,35,38,30,32,35,0,55],
[47,47,53,50,47,45,44,43,43,50,44,46,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 185, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,55,47,47,61,48,46,55,63,63,61,58],
[50,0,57,53,44,52,43,57,56,60,60,54,58],
[46,44,0,51,41,53,46,46,43,49,56,55,45],
[54,48,50,0,58,56,55,49,55,57,65,65,57],
[54,57,60,43,0,54,50,47,57,62,69,68,56],
[40,49,48,45,47,0,48,54,48,57,60,57,51],
[53,58,55,46,51,53,0,58,51,64,63,60,50],
[55,44,55,52,54,47,43,0,53,51,65,59,67],
[46,45,58,46,44,53,50,48,0,56,63,54,45],
[38,41,52,44,39,44,37,50,45,0,57,45,49],
[38,41,45,36,32,41,38,36,38,44,0,36,38],
[40,47,46,36,33,44,41,42,47,56,65,0,45],
[43,43,56,44,45,50,51,34,56,52,63,56,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 186, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,49,51,52,51,51,59,49,47,62,53,54],
[61,0,54,51,52,53,48,59,53,59,58,47,48],
[52,47,0,49,46,49,43,51,53,55,53,48,44],
[50,50,52,0,56,42,39,61,56,42,54,47,49],
[49,49,55,45,0,46,44,52,42,46,53,35,47],
[50,48,52,59,55,0,48,52,49,57,62,55,50],
[50,53,58,62,57,53,0,56,55,55,57,48,59],
[42,42,50,40,49,49,45,0,46,51,53,47,41],
[52,48,48,45,59,52,46,55,0,56,55,51,53],
[54,42,46,59,55,44,46,50,45,0,69,49,57],
[39,43,48,47,48,39,44,48,46,32,0,43,40],
[48,54,53,54,66,46,53,54,50,52,58,0,56],
[47,53,57,52,54,51,42,60,48,44,61,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 187, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,53,50,61,43,56,48,53,45,46,49,51,48],
[48,0,49,55,39,53,50,59,49,45,49,51,49],
[51,52,0,53,39,53,46,50,46,41,50,59,51],
[40,46,48,0,43,43,50,49,41,42,40,48,44],
[58,62,62,58,0,58,53,57,54,53,52,64,48],
[45,48,48,58,43,0,51,53,48,39,47,52,49],
[53,51,55,51,48,50,0,55,50,51,47,52,51],
[48,42,51,52,44,48,46,0,49,40,44,52,51],
[56,52,55,60,47,53,51,52,0,48,50,55,51],
[55,56,60,59,48,62,50,61,53,0,54,57,55],
[52,52,51,61,49,54,54,57,51,47,0,61,51],
[50,50,42,53,37,49,49,49,46,44,40,0,52],
[53,52,50,57,53,52,50,50,50,46,50,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 188, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,54,57,48,53,45,54,41,44,55,45,49],
[56,0,58,44,53,49,59,51,48,49,57,47,49],
[47,43,0,48,52,55,47,45,44,50,48,43,46],
[44,57,53,0,59,51,54,59,44,56,61,47,42],
[53,48,49,42,0,48,47,45,49,51,50,46,41],
[48,52,46,50,53,0,47,58,49,42,55,47,52],
[56,42,54,47,54,54,0,55,43,41,54,52,50],
[47,50,56,42,56,43,46,0,40,47,45,43,42],
[60,53,57,57,52,52,58,61,0,49,53,51,45],
[57,52,51,45,50,59,60,54,52,0,48,52,50],
[46,44,53,40,51,46,47,56,48,53,0,44,43],
[56,54,58,54,55,54,49,58,50,49,57,0,53],
[52,52,55,59,60,49,51,59,56,51,58,48,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 189, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,37,28,44,22,50,28,57,28,37,66,15,15],
[64,0,63,79,77,79,42,77,42,86,66,44,79],
[73,38,0,64,51,64,42,77,42,86,51,29,29],
[57,22,37,0,22,35,22,86,13,57,22,24,37],
[79,24,50,79,0,79,44,92,57,101,66,44,79],
[51,22,37,66,22,0,51,51,13,51,51,24,37],
[73,59,59,79,57,50,0,77,48,86,66,59,50],
[44,24,24,15,9,50,24,0,0,9,24,24,15],
[73,59,59,88,44,88,53,101,0,101,66,53,59],
[64,15,15,44,0,50,15,92,0,0,66,15,15],
[35,35,50,79,35,50,35,77,35,35,0,50,50],
[86,57,72,77,57,77,42,77,48,86,51,0,63],
[86,22,72,64,22,64,51,86,42,86,51,38,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 190, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,57,59,60,46,58,53,52,51,49,48,46],
[63,0,52,68,58,50,62,60,60,66,46,70,52],
[44,49,0,46,49,46,45,54,60,50,43,43,47],
[42,33,55,0,53,47,50,56,46,58,44,41,45],
[41,43,52,48,0,49,38,52,42,47,48,48,52],
[55,51,55,54,52,0,48,64,59,57,54,48,53],
[43,39,56,51,63,53,0,56,44,44,46,46,48],
[48,41,47,45,49,37,45,0,46,44,40,36,50],
[49,41,41,55,59,42,57,55,0,58,45,49,48],
[50,35,51,43,54,44,57,57,43,0,42,49,41],
[52,55,58,57,53,47,55,61,56,59,0,54,53],
[53,31,58,60,53,53,55,65,52,52,47,0,52],
[55,49,54,56,49,48,53,51,53,60,48,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 191, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,59,50,57,59,51,59,48,51,48,53,55,56],
[42,0,38,51,51,33,51,43,42,46,47,51,46],
[51,63,0,53,54,46,49,52,56,55,58,58,56],
[44,50,48,0,59,46,42,35,48,49,55,52,44],
[42,50,47,42,0,37,44,40,51,45,53,62,53],
[50,68,55,55,64,0,61,51,54,55,58,62,61],
[42,50,52,59,57,40,0,49,57,49,50,61,58],
[53,58,49,66,61,50,52,0,57,55,47,53,54],
[50,59,45,53,50,47,44,44,0,48,51,59,59],
[53,55,46,52,56,46,52,46,53,0,53,58,52],
[48,54,43,46,48,43,51,54,50,48,0,61,53],
[46,50,43,49,39,39,40,48,42,43,40,0,51],
[45,55,45,57,48,40,43,47,42,49,48,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 192, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,31,80,32,58,5,31,48,26,31,36,44],
[101,0,58,85,49,58,49,58,74,26,85,80,44],
[70,43,0,80,54,44,0,53,48,44,76,54,44],
[21,16,21,0,32,32,5,5,48,0,5,27,27],
[69,52,47,69,0,69,25,74,74,69,74,80,60],
[43,43,57,69,32,0,16,58,75,52,41,36,27],
[96,52,101,96,76,85,0,58,101,69,85,80,44],
[70,43,48,96,27,43,43,0,48,43,75,27,43],
[53,27,53,53,27,26,0,53,0,53,53,53,44],
[75,75,57,101,32,49,32,58,48,0,85,63,44],
[70,16,25,96,27,60,16,26,48,16,0,36,60],
[65,21,47,74,21,65,21,74,48,38,65,0,65],
[57,57,57,74,41,74,57,58,57,57,41,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 193, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,45,42,43,51,51,52,49,46,49,50,38],
[52,0,54,52,40,51,48,51,45,52,52,51,43],
[56,47,0,47,54,57,57,57,46,50,47,48,47],
[59,49,54,0,45,49,66,57,48,50,50,51,44],
[58,61,47,56,0,63,59,51,51,59,55,53,56],
[50,50,44,52,38,0,50,51,43,56,40,44,50],
[50,53,44,35,42,51,0,49,47,47,47,42,37],
[49,50,44,44,50,50,52,0,43,48,46,46,48],
[52,56,55,53,50,58,54,58,0,63,50,53,47],
[55,49,51,51,42,45,54,53,38,0,55,45,49],
[52,49,54,51,46,61,54,55,51,46,0,58,47],
[51,50,53,50,48,57,59,55,48,56,43,0,52],
[63,58,54,57,45,51,64,53,54,52,54,49,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 194, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,49,46,48,52,41,45,44,43,49,47,50,39],
[52,0,52,46,58,50,54,49,46,53,55,44,51],
[55,49,0,46,52,52,55,57,49,55,53,44,52],
[53,55,55,0,52,45,55,57,45,50,52,51,47],
[49,43,49,49,0,44,46,50,48,52,50,46,43],
[60,51,49,56,57,0,48,51,51,53,51,54,51],
[56,47,46,46,55,53,0,50,44,51,56,46,42],
[57,52,44,44,51,50,51,0,45,57,57,42,52],
[58,55,52,56,53,50,57,56,0,55,62,53,54],
[52,48,46,51,49,48,50,44,46,0,52,51,46],
[54,46,48,49,51,50,45,44,39,49,0,44,45],
[51,57,57,50,55,47,55,59,48,50,57,0,50],
[62,50,49,54,58,50,59,49,47,55,56,51,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 195, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,62,39,46,85,67,64,46,71,68,70,56,62],
[39,0,36,28,75,39,48,45,47,60,28,53,70],
[62,65,0,52,77,58,63,60,58,83,50,68,66],
[55,73,49,0,93,47,74,84,88,91,65,82,68],
[16,26,24,8,0,11,25,41,34,44,18,51,57],
[34,62,43,54,90,0,53,71,69,72,61,69,70],
[37,53,38,27,76,48,0,51,70,71,59,51,57],
[55,56,41,17,60,30,50,0,51,45,43,59,66],
[30,54,43,13,67,32,31,50,0,70,37,56,68],
[33,41,18,10,57,29,30,56,31,0,31,58,56],
[31,73,51,36,83,40,42,58,64,70,0,55,68],
[45,48,33,19,50,32,50,42,45,43,46,0,56],
[39,31,35,33,44,31,44,35,33,45,33,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 196, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,44,42,37,46,48,39,53,47,44,42,51],
[62,0,54,47,48,45,60,53,53,53,52,54,63],
[57,47,0,44,52,50,58,57,57,50,46,55,57],
[59,54,57,0,50,46,53,54,57,47,49,49,61],
[64,53,49,51,0,59,59,49,55,57,50,54,60],
[55,56,51,55,42,0,51,50,55,49,51,45,55],
[53,41,43,48,42,50,0,46,47,47,46,47,52],
[62,48,44,47,52,51,55,0,51,52,50,43,66],
[48,48,44,44,46,46,54,50,0,43,41,45,60],
[54,48,51,54,44,52,54,49,58,0,48,47,57],
[57,49,55,52,51,50,55,51,60,53,0,59,61],
[59,47,46,52,47,56,54,58,56,54,42,0,61],
[50,38,44,40,41,46,49,35,41,44,40,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 197, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,47,54,44,45,50,46,45,48,46,64,48,52],
[54,0,49,50,48,40,47,53,46,49,54,49,55],
[47,52,0,36,41,50,52,43,50,48,52,49,52],
[57,51,65,0,60,52,64,57,50,49,56,59,55],
[56,53,60,41,0,52,54,48,52,47,63,52,51],
[51,61,51,49,49,0,53,50,47,52,62,49,51],
[55,54,49,37,47,48,0,44,44,49,59,50,46],
[56,48,58,44,53,51,57,0,44,50,52,46,53],
[53,55,51,51,49,54,57,57,0,53,63,57,58],
[55,52,53,52,54,49,52,51,48,0,60,54,53],
[37,47,49,45,38,39,42,49,38,41,0,49,45],
[53,52,52,42,49,52,51,55,44,47,52,0,57],
[49,46,49,46,50,50,55,48,43,48,56,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 198, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,50,50,55,56,35,43,54,44,43,47,46,58],
[51,0,43,54,53,51,45,46,36,47,54,49,45],
[51,58,0,57,53,53,49,45,42,48,46,52,50],
[46,47,44,0,52,46,45,43,47,48,53,52,49],
[45,48,48,49,0,46,43,50,49,44,58,55,54],
[66,50,48,55,55,0,53,49,36,40,60,57,60],
[58,56,52,56,58,48,0,51,46,53,53,60,55],
[47,55,56,58,51,52,50,0,45,56,57,47,60],
[57,65,59,54,52,65,55,56,0,49,63,57,62],
[58,54,53,53,57,61,48,45,52,0,64,59,57],
[54,47,55,48,43,41,48,44,38,37,0,42,45],
[55,52,49,49,46,44,41,54,44,42,59,0,56],
[43,56,51,52,47,41,46,41,39,44,56,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 199, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,45,46,50,47,50,49,52,47,50,48,46,46],
[56,0,57,53,53,60,46,54,57,53,59,49,49],
[55,44,0,50,57,62,48,57,52,51,60,44,49],
[51,48,51,0,50,56,42,50,53,52,55,42,43],
[54,48,44,51,0,56,47,55,53,48,54,47,43],
[51,41,39,45,45,0,39,44,46,38,48,39,38],
[52,55,53,59,54,62,0,57,47,56,60,48,46],
[49,47,44,51,46,57,44,0,52,50,52,42,47],
[54,44,49,48,48,55,54,49,0,54,52,47,49],
[51,48,50,49,53,63,45,51,47,0,53,55,52],
[53,42,41,46,47,53,41,49,49,48,0,42,42],
[55,52,57,59,54,62,53,59,54,46,59,0,48],
[55,52,52,58,58,63,55,54,52,49,59,53,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 101, 200, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbrcwd/mebbrcwd_13_101.csv", index=False, header=False)