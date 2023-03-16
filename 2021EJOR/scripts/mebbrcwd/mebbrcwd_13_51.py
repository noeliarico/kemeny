
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg
from kemeny import sc

rep = 1
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,27,21,26,22,21,26,20,17,22,31,22,26],
[24,0,22,30,22,19,23,29,23,25,26,23,25],
[30,29,0,29,23,26,25,27,23,21,31,22,28],
[25,21,22,0,20,18,25,20,23,23,28,21,23],
[29,29,28,31,0,24,31,29,29,24,30,28,28],
[30,32,25,33,27,0,31,30,31,27,29,27,31],
[25,28,26,26,20,20,0,27,21,27,28,24,25],
[31,22,24,31,22,21,24,0,23,22,29,23,23],
[34,28,28,28,22,20,30,28,0,25,29,29,26],
[29,26,30,28,27,24,24,29,26,0,28,26,20],
[20,25,20,23,21,22,23,22,22,23,0,19,25],
[29,28,29,30,23,24,27,28,22,25,32,0,25],
[25,26,23,28,23,20,26,28,25,31,26,26,0]])



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
result = np.append(np.array([13, 51, 1, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,32,24,27,26,26,30,28,27,25,30,27],
[22,0,22,20,25,28,21,26,32,23,17,24,24],
[19,29,0,23,27,29,19,30,30,29,24,24,26],
[27,31,28,0,29,30,26,27,28,26,32,23,27],
[24,26,24,22,0,25,29,30,25,25,28,22,25],
[25,23,22,21,26,0,22,26,24,28,18,24,17],
[25,30,32,25,22,29,0,28,25,26,21,28,28],
[21,25,21,24,21,25,23,0,30,21,21,28,22],
[23,19,21,23,26,27,26,21,0,22,20,23,20],
[24,28,22,25,26,23,25,30,29,0,25,28,25],
[26,34,27,19,23,33,30,30,31,26,0,27,24],
[21,27,27,28,29,27,23,23,28,23,24,0,23],
[24,27,25,24,26,34,23,29,31,26,27,28,0]])



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
result = np.append(np.array([13, 51, 2, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,25,27,25,26,22,23,31,27,24,24,24],
[26,0,26,28,27,27,23,20,25,25,32,26,26],
[26,25,0,22,25,21,23,21,27,24,19,26,23],
[24,23,29,0,29,27,30,26,33,23,25,26,28],
[26,24,26,22,0,25,27,25,29,22,30,29,29],
[25,24,30,24,26,0,20,21,32,27,25,25,21],
[29,28,28,21,24,31,0,22,31,25,28,30,27],
[28,31,30,25,26,30,29,0,32,26,25,26,25],
[20,26,24,18,22,19,20,19,0,19,23,21,23],
[24,26,27,28,29,24,26,25,32,0,27,31,32],
[27,19,32,26,21,26,23,26,28,24,0,25,25],
[27,25,25,25,22,26,21,25,30,20,26,0,23],
[27,25,28,23,22,30,24,26,28,19,26,28,0]])



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
result = np.append(np.array([13, 51, 3, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,29,27,26,26,23,27,23,22,23,23,21],
[22,0,25,25,28,30,26,25,22,25,26,24,22],
[22,26,0,22,29,28,22,27,21,22,22,22,19],
[24,26,29,0,27,29,30,29,24,20,23,24,21],
[25,23,22,24,0,24,25,26,18,21,23,22,23],
[25,21,23,22,27,0,23,25,23,18,24,23,22],
[28,25,29,21,26,28,0,26,24,23,29,20,25],
[24,26,24,22,25,26,25,0,21,19,22,20,21],
[28,29,30,27,33,28,27,30,0,25,33,27,26],
[29,26,29,31,30,33,28,32,26,0,28,20,28],
[28,25,29,28,28,27,22,29,18,23,0,19,22],
[28,27,29,27,29,28,31,31,24,31,32,0,23],
[30,29,32,30,28,29,26,30,25,23,29,28,0]])



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
result = np.append(np.array([13, 51, 4, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,13,30,22,24,25,22,32,23,25,21,28],
[17,0,20,24,20,21,25,19,20,18,16,14,14],
[38,31,0,33,26,26,26,22,40,26,32,19,21],
[21,27,18,0,21,22,28,23,30,26,22,20,25],
[29,31,25,30,0,29,25,18,33,21,36,12,28],
[27,30,25,29,22,0,35,14,29,19,28,26,29],
[26,26,25,23,26,16,0,16,25,20,20,17,23],
[29,32,29,28,33,37,35,0,30,34,34,19,31],
[19,31,11,21,18,22,26,21,0,24,22,16,23],
[28,33,25,25,30,32,31,17,27,0,35,21,33],
[26,35,19,29,15,23,31,17,29,16,0,22,29],
[30,37,32,31,39,25,34,32,35,30,29,0,25],
[23,37,30,26,23,22,28,20,28,18,22,26,0]])



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
result = np.append(np.array([13, 51, 5, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,25,26,25,32,30,26,28,30,26,28,29],
[26,0,20,29,21,26,28,27,23,23,24,26,24],
[26,31,0,29,24,30,31,30,25,31,30,31,31],
[25,22,22,0,25,22,22,24,24,27,21,20,18],
[26,30,27,26,0,25,32,28,26,27,29,27,25],
[19,25,21,29,26,0,22,26,19,25,21,23,30],
[21,23,20,29,19,29,0,24,22,26,23,24,25],
[25,24,21,27,23,25,27,0,23,25,20,27,30],
[23,28,26,27,25,32,29,28,0,26,24,26,27],
[21,28,20,24,24,26,25,26,25,0,23,28,27],
[25,27,21,30,22,30,28,31,27,28,0,24,29],
[23,25,20,31,24,28,27,24,25,23,27,0,30],
[22,27,20,33,26,21,26,21,24,24,22,21,0]])



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
result = np.append(np.array([13, 51, 6, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,33,28,24,31,36,28,23,34,37,22,31],
[19,0,27,20,18,15,25,18,15,18,29,17,21],
[18,24,0,26,19,19,29,22,16,29,27,21,22],
[23,31,25,0,25,32,39,32,24,33,36,24,27],
[27,33,32,26,0,25,35,19,26,31,35,19,26],
[20,36,32,19,26,0,31,25,28,31,25,24,21],
[15,26,22,12,16,20,0,13,18,20,28,20,21],
[23,33,29,19,32,26,38,0,29,31,35,28,33],
[28,36,35,27,25,23,33,22,0,38,35,28,28],
[17,33,22,18,20,20,31,20,13,0,28,19,17],
[14,22,24,15,16,26,23,16,16,23,0,18,20],
[29,34,30,27,32,27,31,23,23,32,33,0,26],
[20,30,29,24,25,30,30,18,23,34,31,25,0]])



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
result = np.append(np.array([13, 51, 7, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,29,28,31,32,26,32,36,36,31,32,30],
[28,0,29,27,24,30,30,32,33,31,27,32,26],
[22,22,0,23,28,22,26,27,33,34,24,33,31],
[23,24,28,0,30,29,27,32,32,36,26,32,30],
[20,27,23,21,0,22,25,28,36,31,25,27,30],
[19,21,29,22,29,0,26,34,31,29,23,30,29],
[25,21,25,24,26,25,0,34,29,29,22,29,23],
[19,19,24,19,23,17,17,0,30,25,22,25,26],
[15,18,18,19,15,20,22,21,0,26,25,25,22],
[15,20,17,15,20,22,22,26,25,0,22,32,24],
[20,24,27,25,26,28,29,29,26,29,0,25,28],
[19,19,18,19,24,21,22,26,26,19,26,0,26],
[21,25,20,21,21,22,28,25,29,27,23,25,0]])



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
result = np.append(np.array([13, 51, 8, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,25,26,24,21,30,25,27,21,24,22,22],
[32,0,30,29,29,33,28,28,33,30,27,25,36],
[26,21,0,24,30,26,32,35,36,28,31,29,32],
[25,22,27,0,19,22,23,30,27,25,22,25,30],
[27,22,21,32,0,17,38,33,35,31,36,30,29],
[30,18,25,29,34,0,33,39,32,32,34,29,31],
[21,23,19,28,13,18,0,26,27,26,28,23,24],
[26,23,16,21,18,12,25,0,24,20,8,17,24],
[24,18,15,24,16,19,24,27,0,17,7,19,26],
[30,21,23,26,20,19,25,31,34,0,33,29,26],
[27,24,20,29,15,17,23,43,44,18,0,17,25],
[29,26,22,26,21,22,28,34,32,22,34,0,26],
[29,15,19,21,22,20,27,27,25,25,26,25,0]])



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
result = np.append(np.array([13, 51, 9, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,26,25,22,23,20,24,18,23,28,22,31],
[25,0,26,21,18,28,22,29,21,23,29,21,28],
[25,25,0,23,23,25,25,21,20,21,27,18,30],
[26,30,28,0,24,28,28,28,21,25,28,26,32],
[29,33,28,27,0,32,24,28,26,31,30,27,33],
[28,23,26,23,19,0,22,24,19,27,28,18,29],
[31,29,26,23,27,29,0,26,26,27,27,25,32],
[27,22,30,23,23,27,25,0,23,22,29,25,28],
[33,30,31,30,25,32,25,28,0,28,32,25,32],
[28,28,30,26,20,24,24,29,23,0,31,24,30],
[23,22,24,23,21,23,24,22,19,20,0,20,30],
[29,30,33,25,24,33,26,26,26,27,31,0,34],
[20,23,21,19,18,22,19,23,19,21,21,17,0]])



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
result = np.append(np.array([13, 51, 10, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,25,23,23,25,29,28,25,21,18,28,25],
[30,0,24,23,27,20,32,30,27,22,24,22,22],
[26,27,0,20,21,21,26,25,26,14,20,21,23],
[28,28,31,0,21,23,30,23,32,25,24,23,29],
[28,24,30,30,0,30,26,27,25,24,20,26,23],
[26,31,30,28,21,0,28,30,23,21,21,24,29],
[22,19,25,21,25,23,0,30,23,18,17,18,21],
[23,21,26,28,24,21,21,0,23,19,23,22,22],
[26,24,25,19,26,28,28,28,0,23,22,16,21],
[30,29,37,26,27,30,33,32,28,0,30,25,29],
[33,27,31,27,31,30,34,28,29,21,0,27,25],
[23,29,30,28,25,27,33,29,35,26,24,0,25],
[26,29,28,22,28,22,30,29,30,22,26,26,0]])



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
result = np.append(np.array([13, 51, 11, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,19,30,31,27,33,32,32,33,36,24,22],
[29,0,35,20,26,27,24,33,25,27,21,18,21],
[32,16,0,21,26,22,27,21,20,28,24,12,26],
[21,31,30,0,31,38,47,39,42,31,19,25,32],
[20,25,25,20,0,23,26,20,28,29,25,20,32],
[24,24,29,13,28,0,31,31,32,34,16,24,24],
[18,27,24,4,25,20,0,21,25,24,18,17,20],
[19,18,30,12,31,20,30,0,25,25,20,25,27],
[19,26,31,9,23,19,26,26,0,29,20,26,31],
[18,24,23,20,22,17,27,26,22,0,29,27,22],
[15,30,27,32,26,35,33,31,31,22,0,23,26],
[27,33,39,26,31,27,34,26,25,24,28,0,29],
[29,30,25,19,19,27,31,24,20,29,25,22,0]])



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
result = np.append(np.array([13, 51, 12, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,39,39,34,39,34,39,32,32,32,19,39],
[19,0,38,38,38,27,20,25,38,28,38,38,27],
[12,13,0,32,33,30,2,7,15,15,15,8,23],
[12,13,19,0,20,15,13,0,13,15,8,19,8],
[17,13,18,31,0,28,13,7,24,24,11,19,15],
[12,24,21,36,23,0,13,11,36,26,21,21,0],
[17,31,49,38,38,38,0,38,31,28,31,36,38],
[12,26,44,51,44,40,13,0,44,26,44,31,23],
[19,13,36,38,27,15,20,7,0,9,26,26,15],
[19,23,36,36,27,25,23,25,42,0,29,36,25],
[19,13,36,43,40,30,20,7,25,22,0,36,15],
[32,13,43,32,32,30,15,20,25,15,15,0,30],
[12,24,28,43,36,51,13,28,36,26,36,21,0]])



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
result = np.append(np.array([13, 51, 13, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,27,28,40,37,27,25,28,22,25,33,22],
[29,0,32,33,36,34,24,34,38,20,22,37,29],
[24,19,0,40,39,36,27,35,34,35,29,41,26],
[23,18,11,0,26,19,18,16,29,14,20,24,15],
[11,15,12,25,0,27,22,32,28,18,27,22,23],
[14,17,15,32,24,0,18,35,21,24,24,19,24],
[24,27,24,33,29,33,0,29,33,27,31,36,33],
[26,17,16,35,19,16,22,0,22,19,27,27,11],
[23,13,17,22,23,30,18,29,0,14,12,33,27],
[29,31,16,37,33,27,24,32,37,0,18,30,31],
[26,29,22,31,24,27,20,24,39,33,0,35,30],
[18,14,10,27,29,32,15,24,18,21,16,0,20],
[29,22,25,36,28,27,18,40,24,20,21,31,0]])



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
result = np.append(np.array([13, 51, 14, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,38,31,17,32,23,22,37,32,28,30,39],
[31,0,28,14,24,19,26,25,29,39,22,30,35],
[13,23,0,25,25,27,25,22,25,24,13,32,36],
[20,37,26,0,22,26,22,27,33,29,18,23,37],
[34,27,26,29,0,24,29,34,31,24,18,18,31],
[19,32,24,25,27,0,30,23,33,33,33,32,36],
[28,25,26,29,22,21,0,32,32,35,17,25,32],
[29,26,29,24,17,28,19,0,22,26,22,26,28],
[14,22,26,18,20,18,19,29,0,30,15,22,33],
[19,12,27,22,27,18,16,25,21,0,10,28,38],
[23,29,38,33,33,18,34,29,36,41,0,33,43],
[21,21,19,28,33,19,26,25,29,23,18,0,42],
[12,16,15,14,20,15,19,23,18,13,8,9,0]])



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
result = np.append(np.array([13, 51, 15, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,18,32,22,19,24,22,20,24,17,27,22],
[29,0,11,30,19,21,27,31,22,23,28,33,23],
[33,40,0,31,33,32,27,32,22,35,37,29,22],
[19,21,20,0,22,19,26,26,16,26,23,21,16],
[29,32,18,29,0,26,29,27,11,23,24,29,23],
[32,30,19,32,25,0,32,29,25,22,24,30,25],
[27,24,24,25,22,19,0,30,13,29,31,22,15],
[29,20,19,25,24,22,21,0,20,20,25,30,18],
[31,29,29,35,40,26,38,31,0,23,29,33,30],
[27,28,16,25,28,29,22,31,28,0,26,31,22],
[34,23,14,28,27,27,20,26,22,25,0,28,19],
[24,18,22,30,22,21,29,21,18,20,23,0,25],
[29,28,29,35,28,26,36,33,21,29,32,26,0]])



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
result = np.append(np.array([13, 51, 16, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,24,32,19,34,35,25,23,20,28,31,28],
[23,0,19,19,21,20,23,23,22,22,29,25,21],
[27,32,0,25,28,34,30,29,23,28,33,37,32],
[19,32,26,0,34,22,22,19,20,29,32,37,35],
[32,30,23,17,0,33,29,25,22,25,28,30,32],
[17,31,17,29,18,0,25,13,19,19,25,27,29],
[16,28,21,29,22,26,0,19,28,24,25,24,25],
[26,28,22,32,26,38,32,0,22,27,29,31,28],
[28,29,28,31,29,32,23,29,0,25,26,30,32],
[31,29,23,22,26,32,27,24,26,0,26,35,22],
[23,22,18,19,23,26,26,22,25,25,0,34,25],
[20,26,14,14,21,24,27,20,21,16,17,0,20],
[23,30,19,16,19,22,26,23,19,29,26,31,0]])



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
result = np.append(np.array([13, 51, 17, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,38,29,39,26,26,39,39,39,39,29,39],
[37,0,38,25,37,39,22,51,39,39,41,29,51],
[13,13,0,13,25,25,12,25,23,25,29,13,29],
[22,26,38,0,34,38,34,38,26,26,51,16,38],
[12,14,26,17,0,14,14,14,14,26,39,4,14],
[25,12,26,13,37,0,12,35,39,29,41,25,29],
[25,29,39,17,37,39,0,51,27,29,41,29,39],
[12,0,26,13,37,16,0,0,14,29,41,0,4],
[12,12,28,25,37,12,24,37,0,29,41,24,41],
[12,12,26,25,25,22,22,22,22,0,41,12,26],
[12,10,22,0,12,10,10,10,10,10,0,0,14],
[22,22,38,35,47,26,22,51,27,39,51,0,51],
[12,0,22,13,37,22,12,47,10,25,37,0,0]])



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
result = np.append(np.array([13, 51, 18, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,26,31,28,36,33,27,27,25,27,29,30],
[13,0,17,23,21,25,25,26,15,12,22,17,26],
[25,34,0,34,29,31,33,32,28,32,26,17,30],
[20,28,17,0,23,23,25,22,24,16,16,18,25],
[23,30,22,28,0,29,34,27,27,21,26,23,26],
[15,26,20,28,22,0,37,28,19,21,22,19,25],
[18,26,18,26,17,14,0,22,18,22,14,10,15],
[24,25,19,29,24,23,29,0,14,20,19,15,34],
[24,36,23,27,24,32,33,37,0,17,22,25,24],
[26,39,19,35,30,30,29,31,34,0,32,24,29],
[24,29,25,35,25,29,37,32,29,19,0,21,28],
[22,34,34,33,28,32,41,36,26,27,30,0,29],
[21,25,21,26,25,26,36,17,27,22,23,22,0]])



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
result = np.append(np.array([13, 51, 19, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,32,28,31,25,34,28,35,28,35,30,23],
[20,0,22,27,25,24,22,27,25,25,26,24,22],
[19,29,0,27,30,24,30,25,31,24,27,18,22],
[23,24,24,0,28,22,29,22,29,22,29,26,22],
[20,26,21,23,0,17,23,25,28,23,22,27,21],
[26,27,27,29,34,0,24,29,32,24,28,27,28],
[17,29,21,22,28,27,0,24,23,21,26,22,23],
[23,24,26,29,26,22,27,0,26,22,27,22,24],
[16,26,20,22,23,19,28,25,0,17,19,21,21],
[23,26,27,29,28,27,30,29,34,0,27,29,27],
[16,25,24,22,29,23,25,24,32,24,0,29,27],
[21,27,33,25,24,24,29,29,30,22,22,0,22],
[28,29,29,29,30,23,28,27,30,24,24,29,0]])



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
result = np.append(np.array([13, 51, 20, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,27,24,28,32,24,20,27,32,24,26,24],
[32,0,22,28,29,30,20,31,28,32,18,21,24],
[24,29,0,26,31,34,27,35,20,24,23,25,23],
[27,23,25,0,29,27,17,27,21,28,23,17,16],
[23,22,20,22,0,18,22,29,20,29,17,21,20],
[19,21,17,24,33,0,22,27,16,25,14,24,23],
[27,31,24,34,29,29,0,27,30,32,24,26,27],
[31,20,16,24,22,24,24,0,20,28,22,28,19],
[24,23,31,30,31,35,21,31,0,24,25,20,20],
[19,19,27,23,22,26,19,23,27,0,26,28,17],
[27,33,28,28,34,37,27,29,26,25,0,26,20],
[25,30,26,34,30,27,25,23,31,23,25,0,23],
[27,27,28,35,31,28,24,32,31,34,31,28,0]])



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
result = np.append(np.array([13, 51, 21, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,22,20,21,18,20,27,22,24,27,22,26],
[32,0,26,26,24,21,27,31,18,20,23,22,27],
[29,25,0,23,27,25,29,26,21,24,29,27,31],
[31,25,28,0,27,16,30,28,21,26,28,25,28],
[30,27,24,24,0,24,26,32,26,20,26,19,27],
[33,30,26,35,27,0,22,33,27,30,30,32,32],
[31,24,22,21,25,29,0,31,21,27,27,24,26],
[24,20,25,23,19,18,20,0,15,21,26,20,25],
[29,33,30,30,25,24,30,36,0,29,29,29,31],
[27,31,27,25,31,21,24,30,22,0,26,22,27],
[24,28,22,23,25,21,24,25,22,25,0,20,28],
[29,29,24,26,32,19,27,31,22,29,31,0,34],
[25,24,20,23,24,19,25,26,20,24,23,17,0]])



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
result = np.append(np.array([13, 51, 22, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,21,21,23,30,24,16,23,21,35,18,17],
[23,0,26,20,26,23,27,23,26,30,34,20,26],
[30,25,0,31,29,28,32,31,36,31,36,31,26],
[30,31,20,0,28,30,30,24,26,25,32,26,26],
[28,25,22,23,0,29,22,18,23,23,32,28,22],
[21,28,23,21,22,0,23,25,28,27,35,28,23],
[27,24,19,21,29,28,0,19,28,26,37,24,24],
[35,28,20,27,33,26,32,0,31,34,36,29,26],
[28,25,15,25,28,23,23,20,0,18,26,25,22],
[30,21,20,26,28,24,25,17,33,0,30,25,20],
[16,17,15,19,19,16,14,15,25,21,0,22,18],
[33,31,20,25,23,23,27,22,26,26,29,0,26],
[34,25,25,25,29,28,27,25,29,31,33,25,0]])



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
result = np.append(np.array([13, 51, 23, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,28,32,30,20,30,30,30,19,21,18,22],
[27,0,27,29,26,27,25,31,26,27,25,23,18],
[23,24,0,34,24,19,30,29,27,22,23,31,14],
[19,22,17,0,25,20,25,26,22,20,23,22,19],
[21,25,27,26,0,20,26,30,19,23,20,23,16],
[31,24,32,31,31,0,33,29,31,32,27,24,22],
[21,26,21,26,25,18,0,31,30,21,24,23,18],
[21,20,22,25,21,22,20,0,23,23,21,20,21],
[21,25,24,29,32,20,21,28,0,26,23,23,19],
[32,24,29,31,28,19,30,28,25,0,24,25,22],
[30,26,28,28,31,24,27,30,28,27,0,16,26],
[33,28,20,29,28,27,28,31,28,26,35,0,20],
[29,33,37,32,35,29,33,30,32,29,25,31,0]])



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
result = np.append(np.array([13, 51, 24, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,31,25,34,34,19,35,26,22,24,27,22],
[24,0,26,15,25,31,21,31,27,25,28,29,26],
[20,25,0,14,31,25,22,30,23,16,25,33,16],
[26,36,37,0,32,33,24,31,35,29,27,31,30],
[17,26,20,19,0,29,17,23,18,8,16,22,14],
[17,20,26,18,22,0,20,26,24,12,24,27,19],
[32,30,29,27,34,31,0,35,31,23,36,29,28],
[16,20,21,20,28,25,16,0,27,20,22,16,19],
[25,24,28,16,33,27,20,24,0,12,23,26,21],
[29,26,35,22,43,39,28,31,39,0,35,35,26],
[27,23,26,24,35,27,15,29,28,16,0,25,20],
[24,22,18,20,29,24,22,35,25,16,26,0,18],
[29,25,35,21,37,32,23,32,30,25,31,33,0]])



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
result = np.append(np.array([13, 51, 25, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,27,25,24,25,24,25,25,29,31,27,23],
[30,0,23,29,22,26,28,29,21,31,29,29,31],
[24,28,0,26,24,28,26,25,27,26,26,29,25],
[26,22,25,0,26,25,23,34,24,28,29,31,31],
[27,29,27,25,0,25,25,32,22,30,27,32,29],
[26,25,23,26,26,0,26,28,21,26,28,27,24],
[27,23,25,28,26,25,0,30,22,27,27,34,26],
[26,22,26,17,19,23,21,0,20,26,23,22,21],
[26,30,24,27,29,30,29,31,0,32,27,35,28],
[22,20,25,23,21,25,24,25,19,0,25,22,23],
[20,22,25,22,24,23,24,28,24,26,0,24,24],
[24,22,22,20,19,24,17,29,16,29,27,0,26],
[28,20,26,20,22,27,25,30,23,28,27,25,0]])



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
result = np.append(np.array([13, 51, 26, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,29,41,22,34,37,34,32,32,35,41,47],
[32,0,21,43,33,36,36,43,40,33,37,43,43],
[22,30,0,47,27,34,34,23,37,34,37,30,34],
[10,8,4,0,14,33,21,8,22,14,16,22,33],
[29,18,24,37,0,30,23,30,37,18,30,37,37],
[17,15,17,18,21,0,21,11,22,15,8,25,29],
[14,15,17,30,28,30,0,26,22,14,15,34,38],
[17,8,28,43,21,40,25,0,32,24,23,29,51],
[19,11,14,29,14,29,29,19,0,7,31,26,25],
[19,18,17,37,33,36,37,27,44,0,27,41,51],
[16,14,14,35,21,43,36,28,20,24,0,35,39],
[10,8,21,29,14,26,17,22,25,10,16,0,36],
[4,8,17,18,14,22,13,0,26,0,12,15,0]])



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
result = np.append(np.array([13, 51, 27, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,32,30,30,32,25,32,28,25,30,31,25],
[26,0,33,29,30,32,28,33,28,21,26,27,26],
[19,18,0,22,28,28,20,25,21,21,22,19,21],
[21,22,29,0,30,26,23,28,23,20,22,26,23],
[21,21,23,21,0,28,25,23,21,18,22,21,17],
[19,19,23,25,23,0,20,24,17,14,22,19,20],
[26,23,31,28,26,31,0,31,27,28,28,30,24],
[19,18,26,23,28,27,20,0,20,19,24,21,22],
[23,23,30,28,30,34,24,31,0,18,24,26,21],
[26,30,30,31,33,37,23,32,33,0,28,31,27],
[21,25,29,29,29,29,23,27,27,23,0,24,22],
[20,24,32,25,30,32,21,30,25,20,27,0,24],
[26,25,30,28,34,31,27,29,30,24,29,27,0]])



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
result = np.append(np.array([13, 51, 28, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,26,14,42,19,12,21,26,20,27,31,31],
[32,0,13,22,23,23,22,26,18,23,32,28,28],
[25,38,0,15,30,24,24,24,19,25,30,40,30],
[37,29,36,0,37,20,32,22,27,22,22,46,46],
[9,28,21,14,0,14,21,14,10,18,18,21,33],
[32,28,27,31,37,0,31,21,32,46,36,31,46],
[39,29,27,19,30,20,0,9,20,15,20,37,30],
[30,25,27,29,37,30,42,0,23,25,36,37,30],
[25,33,32,24,41,19,31,28,0,34,41,31,39],
[31,28,26,29,33,5,36,26,17,0,26,36,45],
[24,19,21,29,33,15,31,15,10,25,0,31,24],
[20,23,11,5,30,20,14,14,20,15,20,0,35],
[20,23,21,5,18,5,21,21,12,6,27,16,0]])



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
result = np.append(np.array([13, 51, 29, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,27,22,24,33,7,20,24,24,19,13,20],
[34,0,31,26,24,39,8,35,21,28,18,25,31],
[24,20,0,24,23,33,14,30,21,15,18,24,29],
[29,25,27,0,28,28,20,36,32,23,35,34,30],
[27,27,28,23,0,37,18,31,28,31,31,33,38],
[18,12,18,23,14,0,13,14,18,19,17,16,17],
[44,43,37,31,33,38,0,40,28,31,34,25,34],
[31,16,21,15,20,37,11,0,17,22,20,23,20],
[27,30,30,19,23,33,23,34,0,23,35,24,33],
[27,23,36,28,20,32,20,29,28,0,27,29,30],
[32,33,33,16,20,34,17,31,16,24,0,33,38],
[38,26,27,17,18,35,26,28,27,22,18,0,28],
[31,20,22,21,13,34,17,31,18,21,13,23,0]])



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
result = np.append(np.array([13, 51, 30, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,23,27,28,31,34,33,35,35,36,23,31],
[32,0,25,20,21,30,31,30,29,33,26,25,31],
[28,26,0,29,23,29,35,29,31,33,23,27,32],
[24,31,22,0,22,27,27,24,28,27,24,25,31],
[23,30,28,29,0,25,36,26,37,35,32,21,32],
[20,21,22,24,26,0,28,23,28,25,29,20,17],
[17,20,16,24,15,23,0,24,31,27,23,18,24],
[18,21,22,27,25,28,27,0,26,28,22,21,24],
[16,22,20,23,14,23,20,25,0,27,28,18,21],
[16,18,18,24,16,26,24,23,24,0,22,19,15],
[15,25,28,27,19,22,28,29,23,29,0,19,24],
[28,26,24,26,30,31,33,30,33,32,32,0,35],
[20,20,19,20,19,34,27,27,30,36,27,16,0]])



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
result = np.append(np.array([13, 51, 31, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,28,25,22,19,24,39,30,25,28,32,41],
[25,0,23,15,29,27,28,30,27,28,25,38,32],
[23,28,0,23,20,27,26,29,22,20,23,36,28],
[26,36,28,0,25,22,28,30,37,30,28,32,34],
[29,22,31,26,0,19,18,29,28,26,24,30,29],
[32,24,24,29,32,0,32,40,29,23,30,35,33],
[27,23,25,23,33,19,0,28,32,29,23,33,29],
[12,21,22,21,22,11,23,0,31,23,18,28,34],
[21,24,29,14,23,22,19,20,0,19,18,28,25],
[26,23,31,21,25,28,22,28,32,0,20,38,24],
[23,26,28,23,27,21,28,33,33,31,0,33,25],
[19,13,15,19,21,16,18,23,23,13,18,0,18],
[10,19,23,17,22,18,22,17,26,27,26,33,0]])



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
result = np.append(np.array([13, 51, 32, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,28,27,31,20,28,28,36,27,25,24,23],
[16,0,27,22,26,17,25,23,32,25,21,24,16],
[23,24,0,19,25,21,21,26,30,23,23,21,22],
[24,29,32,0,27,29,31,25,39,24,32,28,20],
[20,25,26,24,0,18,25,20,30,21,26,21,21],
[31,34,30,22,33,0,31,29,36,27,27,32,27],
[23,26,30,20,26,20,0,23,30,23,26,22,18],
[23,28,25,26,31,22,28,0,34,22,27,21,18],
[15,19,21,12,21,15,21,17,0,19,24,16,13],
[24,26,28,27,30,24,28,29,32,0,29,31,29],
[26,30,28,19,25,24,25,24,27,22,0,26,23],
[27,27,30,23,30,19,29,30,35,20,25,0,25],
[28,35,29,31,30,24,33,33,38,22,28,26,0]])



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
result = np.append(np.array([13, 51, 33, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,36,36,34,29,27,32,24,28,35,30,35],
[24,0,33,35,26,29,33,24,30,29,31,29,28],
[15,18,0,27,30,18,22,19,24,21,24,22,22],
[15,16,24,0,24,20,23,19,23,21,21,21,18],
[17,25,21,27,0,24,21,19,29,23,18,27,29],
[22,22,33,31,27,0,25,23,29,30,27,27,32],
[24,18,29,28,30,26,0,23,27,30,27,22,25],
[19,27,32,32,32,28,28,0,31,23,27,26,29],
[27,21,27,28,22,22,24,20,0,26,25,25,24],
[23,22,30,30,28,21,21,28,25,0,21,28,29],
[16,20,27,30,33,24,24,24,26,30,0,26,25],
[21,22,29,30,24,24,29,25,26,23,25,0,24],
[16,23,29,33,22,19,26,22,27,22,26,27,0]])



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
result = np.append(np.array([13, 51, 34, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,30,21,43,36,29,32,34,43,35,36,25],
[32,0,41,21,38,44,29,44,43,32,35,42,21],
[21,10,0,10,27,27,11,27,18,28,14,24,10],
[30,30,41,0,31,32,34,37,35,43,23,30,16],
[8,13,24,20,0,23,9,13,24,30,17,11,18],
[15,7,24,19,28,0,15,28,28,32,27,33,21],
[22,22,40,17,42,36,0,41,39,40,33,40,23],
[19,7,24,14,38,23,10,0,33,30,18,18,10],
[17,8,33,16,27,23,12,18,0,26,10,16,17],
[8,19,23,8,21,19,11,21,25,0,6,23,16],
[16,16,37,28,34,24,18,33,41,45,0,37,26],
[15,9,27,21,40,18,11,33,35,28,14,0,8],
[26,30,41,35,33,30,28,41,34,35,25,43,0]])



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
result = np.append(np.array([13, 51, 35, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,23,23,25,29,21,21,24,26,19,25,21],
[37,0,22,32,30,36,31,29,26,31,29,28,24],
[28,29,0,29,29,32,30,31,31,30,31,30,25],
[28,19,22,0,27,26,22,20,20,30,23,27,23],
[26,21,22,24,0,25,29,23,19,22,25,29,21],
[22,15,19,25,26,0,29,14,19,23,23,27,20],
[30,20,21,29,22,22,0,25,24,26,24,32,22],
[30,22,20,31,28,37,26,0,26,32,24,31,22],
[27,25,20,31,32,32,27,25,0,28,21,30,26],
[25,20,21,21,29,28,25,19,23,0,24,32,21],
[32,22,20,28,26,28,27,27,30,27,0,30,27],
[26,23,21,24,22,24,19,20,21,19,21,0,19],
[30,27,26,28,30,31,29,29,25,30,24,32,0]])



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
result = np.append(np.array([13, 51, 36, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,50,37,29,42,21,35,26,42,32,40,26],
[23,0,27,39,13,23,17,13,13,34,35,29,25],
[1,24,0,36,25,14,21,35,26,28,28,40,22],
[14,12,15,0,13,15,21,12,6,15,16,25,22],
[22,38,26,38,0,27,29,30,28,27,27,24,24],
[9,28,37,36,24,0,29,23,14,42,31,39,22],
[30,34,30,30,22,22,0,34,34,22,26,24,31],
[16,38,16,39,21,28,17,0,20,27,32,22,18],
[25,38,25,45,23,37,17,31,0,38,37,35,25],
[9,17,23,36,24,9,29,24,13,0,31,29,21],
[19,16,23,35,24,20,25,19,14,20,0,35,22],
[11,22,11,26,27,12,27,29,16,22,16,0,24],
[25,26,29,29,27,29,20,33,26,30,29,27,0]])



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
result = np.append(np.array([13, 51, 37, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,22,30,31,32,32,26,33,23,27,28,30],
[25,0,25,26,29,33,27,26,29,26,24,25,33],
[29,26,0,25,26,31,36,29,30,28,27,25,31],
[21,25,26,0,35,29,34,24,28,28,23,30,29],
[20,22,25,16,0,26,29,19,29,24,21,25,20],
[19,18,20,22,25,0,25,23,32,24,24,20,19],
[19,24,15,17,22,26,0,21,25,24,18,23,24],
[25,25,22,27,32,28,30,0,34,30,28,27,25],
[18,22,21,23,22,19,26,17,0,21,14,19,24],
[28,25,23,23,27,27,27,21,30,0,25,33,25],
[24,27,24,28,30,27,33,23,37,26,0,19,30],
[23,26,26,21,26,31,28,24,32,18,32,0,30],
[21,18,20,22,31,32,27,26,27,26,21,21,0]])



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
result = np.append(np.array([13, 51, 38, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,26,26,28,22,25,21,21,27,25,22,25],
[25,0,28,22,27,26,25,22,27,30,27,22,26],
[25,23,0,24,28,19,23,22,27,21,26,25,23],
[25,29,27,0,27,21,27,18,26,23,29,23,29],
[23,24,23,24,0,24,21,21,22,24,22,25,24],
[29,25,32,30,27,0,30,25,24,25,27,29,29],
[26,26,28,24,30,21,0,22,22,31,26,24,25],
[30,29,29,33,30,26,29,0,25,29,34,30,32],
[30,24,24,25,29,27,29,26,0,27,28,24,26],
[24,21,30,28,27,26,20,22,24,0,27,27,28],
[26,24,25,22,29,24,25,17,23,24,0,28,24],
[29,29,26,28,26,22,27,21,27,24,23,0,26],
[26,25,28,22,27,22,26,19,25,23,27,25,0]])



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
result = np.append(np.array([13, 51, 39, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,32,26,30,28,36,24,24,28,26,28,33],
[22,0,28,25,28,27,35,22,26,28,23,23,25],
[19,23,0,21,22,26,29,17,21,20,22,22,25],
[25,26,30,0,27,30,36,27,30,28,27,27,28],
[21,23,29,24,0,24,31,17,21,22,21,23,26],
[23,24,25,21,27,0,33,23,23,24,22,25,27],
[15,16,22,15,20,18,0,16,25,20,19,19,21],
[27,29,34,24,34,28,35,0,27,23,25,26,32],
[27,25,30,21,30,28,26,24,0,23,21,24,23],
[23,23,31,23,29,27,31,28,28,0,25,23,25],
[25,28,29,24,30,29,32,26,30,26,0,30,29],
[23,28,29,24,28,26,32,25,27,28,21,0,25],
[18,26,26,23,25,24,30,19,28,26,22,26,0]])



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
result = np.append(np.array([13, 51, 40, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,11,40,29,29,11,0,29,40,0,29,29],
[33,0,11,22,51,11,33,33,51,51,11,51,51],
[40,40,0,40,51,40,40,40,40,40,18,51,51],
[11,29,11,0,29,29,11,11,29,51,11,29,29],
[22,0,0,22,0,0,0,22,18,40,0,40,40],
[22,40,11,22,51,0,33,22,51,40,0,51,51],
[40,18,11,40,51,18,0,40,40,40,18,51,51],
[51,18,11,40,29,29,11,0,29,51,29,29,29],
[22,0,11,22,33,0,11,22,0,40,0,33,51],
[11,0,11,0,11,11,11,0,11,0,11,11,11],
[51,40,33,40,51,51,33,22,51,40,0,51,51],
[22,0,0,22,11,0,0,22,18,40,0,0,51],
[22,0,0,22,11,0,0,22,0,40,0,0,0]])



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
result = np.append(np.array([13, 51, 41, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,30,24,29,26,35,22,33,25,30,25,37],
[13,0,12,26,22,28,34,21,37,21,27,27,34],
[21,39,0,32,25,27,42,27,43,32,28,30,37],
[27,25,19,0,15,30,28,30,43,11,18,21,42],
[22,29,26,36,0,28,35,28,40,31,32,39,42],
[25,23,24,21,23,0,29,25,34,19,23,35,42],
[16,17,9,23,16,22,0,23,38,13,18,22,39],
[29,30,24,21,23,26,28,0,36,21,28,33,39],
[18,14,8,8,11,17,13,15,0,10,6,17,25],
[26,30,19,40,20,32,38,30,41,0,14,32,42],
[21,24,23,33,19,28,33,23,45,37,0,38,37],
[26,24,21,30,12,16,29,18,34,19,13,0,37],
[14,17,14,9,9,9,12,12,26,9,14,14,0]])



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
result = np.append(np.array([13, 51, 42, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,19,39,12,31,35,14,10,6,25,18,23],
[28,0,16,28,11,16,23,11,15,16,16,19,16],
[32,35,0,45,24,40,32,35,24,32,43,35,43],
[12,23,6,0,7,26,12,12,12,8,23,23,12],
[39,40,27,44,0,40,40,24,32,16,39,32,36],
[20,35,11,25,11,0,27,8,12,8,19,22,11],
[16,28,19,39,11,24,0,27,20,16,27,19,21],
[37,40,16,39,27,43,24,0,32,33,32,43,37],
[41,36,27,39,19,39,31,19,0,21,42,36,32],
[45,35,19,43,35,43,35,18,30,0,46,30,35],
[26,35,8,28,12,32,24,19,9,5,0,23,12],
[33,32,16,28,19,29,32,8,15,21,28,0,13],
[28,35,8,39,15,40,30,14,19,16,39,38,0]])



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
result = np.append(np.array([13, 51, 43, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,26,27,27,21,24,24,24,33,29,28,27],
[25,0,26,21,24,21,23,20,24,31,19,15,23],
[25,25,0,29,29,29,25,27,25,32,25,29,31],
[24,30,22,0,31,24,27,25,18,30,28,29,29],
[24,27,22,20,0,25,25,28,21,30,21,24,25],
[30,30,22,27,26,0,28,26,20,33,25,26,29],
[27,28,26,24,26,23,0,28,21,34,26,23,29],
[27,31,24,26,23,25,23,0,25,32,19,16,25],
[27,27,26,33,30,31,30,26,0,34,22,30,30],
[18,20,19,21,21,18,17,19,17,0,19,19,26],
[22,32,26,23,30,26,25,32,29,32,0,21,29],
[23,36,22,22,27,25,28,35,21,32,30,0,31],
[24,28,20,22,26,22,22,26,21,25,22,20,0]])



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
result = np.append(np.array([13, 51, 44, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,26,27,28,31,37,17,34,28,24,26,25],
[24,0,25,29,21,21,43,26,23,23,27,25,30],
[25,26,0,26,23,33,29,19,26,27,27,21,29],
[24,22,25,0,13,23,25,19,35,20,22,23,22],
[23,30,28,38,0,25,33,27,28,21,16,24,27],
[20,30,18,28,26,0,40,25,23,31,22,21,25],
[14,8,22,26,18,11,0,18,20,18,5,14,6],
[34,25,32,32,24,26,33,0,22,20,23,20,30],
[17,28,25,16,23,28,31,29,0,33,24,26,20],
[23,28,24,31,30,20,33,31,18,0,23,22,30],
[27,24,24,29,35,29,46,28,27,28,0,28,33],
[25,26,30,28,27,30,37,31,25,29,23,0,32],
[26,21,22,29,24,26,45,21,31,21,18,19,0]])



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
result = np.append(np.array([13, 51, 45, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,21,24,29,14,11,25,25,20,22,20,12],
[36,0,29,27,27,26,23,25,18,17,20,26,22],
[30,22,0,29,36,25,18,23,22,32,23,28,17],
[27,24,22,0,40,32,22,21,17,26,25,31,21],
[22,24,15,11,0,27,19,19,14,20,24,26,10],
[37,25,26,19,24,0,25,25,21,16,30,19,19],
[40,28,33,29,32,26,0,27,22,21,28,21,18],
[26,26,28,30,32,26,24,0,17,19,19,25,16],
[26,33,29,34,37,30,29,34,0,21,28,27,26],
[31,34,19,25,31,35,30,32,30,0,30,31,26],
[29,31,28,26,27,21,23,32,23,21,0,20,21],
[31,25,23,20,25,32,30,26,24,20,31,0,18],
[39,29,34,30,41,32,33,35,25,25,30,33,0]])



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
result = np.append(np.array([13, 51, 46, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,28,25,32,37,29,28,19,27,26,31,24],
[33,0,24,30,24,34,25,23,25,21,26,28,20],
[23,27,0,28,25,29,32,31,27,27,25,24,23],
[26,21,23,0,28,23,27,30,21,24,22,21,21],
[19,27,26,23,0,30,25,30,23,23,21,23,20],
[14,17,22,28,21,0,24,23,14,11,16,20,19],
[22,26,19,24,26,27,0,28,25,22,20,21,21],
[23,28,20,21,21,28,23,0,17,26,22,23,17],
[32,26,24,30,28,37,26,34,0,32,23,28,30],
[24,30,24,27,28,40,29,25,19,0,16,29,21],
[25,25,26,29,30,35,31,29,28,35,0,27,23],
[20,23,27,30,28,31,30,28,23,22,24,0,20],
[27,31,28,30,31,32,30,34,21,30,28,31,0]])



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
result = np.append(np.array([13, 51, 47, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,36,28,35,34,4,18,34,21,27,30,16],
[17,0,16,30,23,33,3,3,26,12,18,9,9],
[15,35,0,36,35,34,10,20,27,23,29,31,17],
[23,21,15,0,31,22,6,17,25,24,18,29,15],
[16,28,16,20,0,34,4,19,26,21,13,24,10],
[17,18,17,29,17,0,17,20,27,18,20,26,20],
[47,48,41,45,47,34,0,35,42,23,29,41,33],
[33,48,31,34,32,31,16,0,41,35,25,38,25],
[17,25,24,26,25,24,9,10,0,10,10,19,18],
[30,39,28,27,30,33,28,16,41,0,16,38,31],
[24,33,22,33,38,31,22,26,41,35,0,32,25],
[21,42,20,22,27,25,10,13,32,13,19,0,9],
[35,42,34,36,41,31,18,26,33,20,26,42,0]])



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
result = np.append(np.array([13, 51, 48, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,18,17,22,21,11,17,13,22,18,20,17],
[35,0,24,21,31,27,18,32,21,28,27,30,28],
[33,27,0,26,31,25,22,30,25,26,18,25,21],
[34,30,25,0,27,19,20,25,26,29,24,26,26],
[29,20,20,24,0,19,15,20,20,25,24,20,18],
[30,24,26,32,32,0,21,27,18,29,22,29,27],
[40,33,29,31,36,30,0,26,29,32,26,29,22],
[34,19,21,26,31,24,25,0,24,30,26,27,24],
[38,30,26,25,31,33,22,27,0,34,31,29,25],
[29,23,25,22,26,22,19,21,17,0,19,25,24],
[33,24,33,27,27,29,25,25,20,32,0,29,28],
[31,21,26,25,31,22,22,24,22,26,22,0,23],
[34,23,30,25,33,24,29,27,26,27,23,28,0]])



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
result = np.append(np.array([13, 51, 49, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,14,28,25,28,11,24,23,16,30,12,13],
[25,0,25,18,24,21,20,30,25,22,36,11,21],
[37,26,0,35,25,29,28,22,28,29,39,19,33],
[23,33,16,0,20,31,10,29,16,18,33,11,12],
[26,27,26,31,0,20,24,17,22,17,22,26,18],
[23,30,22,20,31,0,18,35,18,18,34,12,15],
[40,31,23,41,27,33,0,30,26,21,33,18,28],
[27,21,29,22,34,16,21,0,31,25,33,20,23],
[28,26,23,35,29,33,25,20,0,20,29,27,21],
[35,29,22,33,34,33,30,26,31,0,40,20,22],
[21,15,12,18,29,17,18,18,22,11,0,15,19],
[39,40,32,40,25,39,33,31,24,31,36,0,31],
[38,30,18,39,33,36,23,28,30,29,32,20,0]])



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
result = np.append(np.array([13, 51, 50, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,22,39,22,50,39,39,39,17,30,22,39],
[29,0,23,31,40,51,39,40,39,17,31,22,27],
[29,28,0,42,29,51,41,42,37,28,29,11,29],
[12,20,9,0,10,51,50,27,37,28,12,20,37],
[29,11,22,41,0,50,50,41,50,28,41,11,28],
[1,0,0,0,1,0,0,1,26,0,0,0,0],
[12,12,10,1,1,51,0,1,26,29,1,11,12],
[12,11,9,24,10,50,50,0,37,28,11,11,11],
[12,12,14,14,1,25,25,14,0,12,1,12,12],
[34,34,23,23,23,51,22,23,39,0,23,33,23],
[21,20,22,39,10,51,50,40,50,28,0,20,37],
[29,29,40,31,40,51,40,40,39,18,31,0,27],
[12,24,22,14,23,51,39,40,39,28,14,24,0]])



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
result = np.append(np.array([13, 51, 51, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,23,21,29,29,13,29,20,24,24,20,26],
[29,0,24,24,30,27,26,32,27,21,25,23,31],
[28,27,0,21,27,22,21,28,31,21,21,25,29],
[30,27,30,0,29,23,29,36,34,25,30,28,29],
[22,21,24,22,0,22,21,27,28,24,25,19,28],
[22,24,29,28,29,0,25,27,28,19,21,30,29],
[38,25,30,22,30,26,0,20,30,24,27,28,26],
[22,19,23,15,24,24,31,0,23,19,17,18,26],
[31,24,20,17,23,23,21,28,0,19,11,25,25],
[27,30,30,26,27,32,27,32,32,0,33,20,29],
[27,26,30,21,26,30,24,34,40,18,0,29,33],
[31,28,26,23,32,21,23,33,26,31,22,0,33],
[25,20,22,22,23,22,25,25,26,22,18,18,0]])



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
result = np.append(np.array([13, 51, 52, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,34,29,37,34,32,29,31,32,30,32,31],
[26,0,34,27,30,34,29,35,31,31,22,30,33],
[17,17,0,19,18,29,16,23,24,19,15,20,21],
[22,24,32,0,25,34,20,35,27,31,19,27,30],
[14,21,33,26,0,35,18,26,22,29,24,21,24],
[17,17,22,17,16,0,18,20,20,19,16,21,17],
[19,22,35,31,33,33,0,26,27,33,22,23,23],
[22,16,28,16,25,31,25,0,18,19,18,20,23],
[20,20,27,24,29,31,24,33,0,26,18,23,24],
[19,20,32,20,22,32,18,32,25,0,18,23,21],
[21,29,36,32,27,35,29,33,33,33,0,26,31],
[19,21,31,24,30,30,28,31,28,28,25,0,21],
[20,18,30,21,27,34,28,28,27,30,20,30,0]])



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
result = np.append(np.array([13, 51, 53, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,0,46,28,17,15,28,18,15,18,30,31],
[7,0,5,31,18,7,20,18,18,22,18,15,0],
[51,46,0,46,28,30,28,35,18,35,36,30,44],
[5,20,5,0,33,22,20,33,18,20,18,28,15],
[23,33,23,18,0,22,15,35,5,22,36,30,31],
[34,44,21,29,29,0,15,33,34,33,34,28,31],
[36,31,23,31,36,36,0,36,36,35,36,15,31],
[23,33,16,18,16,18,15,0,21,22,34,2,16],
[33,33,33,33,46,17,15,30,0,17,46,30,33],
[36,29,16,31,29,18,16,29,34,0,34,15,16],
[33,33,15,33,15,17,15,17,5,17,0,17,31],
[21,36,21,23,21,23,36,49,21,36,34,0,21],
[20,51,7,36,20,20,20,35,18,35,20,30,0]])



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
result = np.append(np.array([13, 51, 54, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,27,27,25,28,32,34,23,29,34,25,29],
[25,0,24,18,19,20,34,34,14,30,27,19,28],
[24,27,0,23,26,31,36,36,33,33,37,28,32],
[24,33,28,0,26,30,35,34,22,32,35,25,28],
[26,32,25,25,0,28,34,25,25,33,33,28,33],
[23,31,20,21,23,0,34,30,19,26,27,28,24],
[19,17,15,16,17,17,0,18,10,19,23,12,25],
[17,17,15,17,26,21,33,0,16,22,26,13,33],
[28,37,18,29,26,32,41,35,0,39,35,28,33],
[22,21,18,19,18,25,32,29,12,0,25,25,35],
[17,24,14,16,18,24,28,25,16,26,0,19,23],
[26,32,23,26,23,23,39,38,23,26,32,0,29],
[22,23,19,23,18,27,26,18,18,16,28,22,0]])



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
result = np.append(np.array([13, 51, 55, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,23,29,25,32,22,28,28,24,27,29,28],
[28,0,22,23,25,30,26,32,32,26,25,31,28],
[28,29,0,30,26,31,24,26,29,24,26,25,26],
[22,28,21,0,28,30,23,30,30,22,23,28,25],
[26,26,25,23,0,27,25,30,23,25,23,25,28],
[19,21,20,21,24,0,19,23,23,23,26,25,21],
[29,25,27,28,26,32,0,28,26,24,27,27,23],
[23,19,25,21,21,28,23,0,28,21,18,21,26],
[23,19,22,21,28,28,25,23,0,23,24,26,23],
[27,25,27,29,26,28,27,30,28,0,26,31,27],
[24,26,25,28,28,25,24,33,27,25,0,25,29],
[22,20,26,23,26,26,24,30,25,20,26,0,23],
[23,23,25,26,23,30,28,25,28,24,22,28,0]])



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
result = np.append(np.array([13, 51, 56, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,31,26,31,28,29,26,34,28,23,28,23],
[31,0,30,25,32,28,35,32,31,30,26,31,24],
[20,21,0,19,30,24,27,22,31,21,22,24,16],
[25,26,32,0,32,25,27,26,32,26,24,29,26],
[20,19,21,19,0,25,27,22,34,21,23,28,23],
[23,23,27,26,26,0,30,25,26,29,27,27,27],
[22,16,24,24,24,21,0,25,26,23,18,24,19],
[25,19,29,25,29,26,26,0,26,28,23,27,23],
[17,20,20,19,17,25,25,25,0,26,24,23,20],
[23,21,30,25,30,22,28,23,25,0,25,28,28],
[28,25,29,27,28,24,33,28,27,26,0,27,27],
[23,20,27,22,23,24,27,24,28,23,24,0,25],
[28,27,35,25,28,24,32,28,31,23,24,26,0]])



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
result = np.append(np.array([13, 51, 57, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,31,31,23,27,37,28,31,28,27,19,28],
[18,0,21,22,31,16,28,21,25,27,22,14,20],
[20,30,0,28,31,20,31,25,34,38,32,28,30],
[20,29,23,0,29,21,24,21,23,23,20,22,22],
[28,20,20,22,0,17,29,24,22,23,26,21,24],
[24,35,31,30,34,0,33,26,30,33,33,28,33],
[14,23,20,27,22,18,0,18,21,18,27,22,25],
[23,30,26,30,27,25,33,0,27,24,28,26,26],
[20,26,17,28,29,21,30,24,0,25,24,22,22],
[23,24,13,28,28,18,33,27,26,0,30,24,28],
[24,29,19,31,25,18,24,23,27,21,0,20,19],
[32,37,23,29,30,23,29,25,29,27,31,0,28],
[23,31,21,29,27,18,26,25,29,23,32,23,0]])



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
result = np.append(np.array([13, 51, 58, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,18,24,22,17,21,21,23,22,23,21,20],
[26,0,28,29,22,24,29,25,27,26,25,31,20],
[33,23,0,31,26,30,31,34,28,31,29,30,25],
[27,22,20,0,28,24,29,24,22,25,23,29,23],
[29,29,25,23,0,23,31,27,26,28,21,25,26],
[34,27,21,27,28,0,26,27,29,30,25,29,25],
[30,22,20,22,20,25,0,22,23,24,19,18,15],
[30,26,17,27,24,24,29,0,25,24,20,28,16],
[28,24,23,29,25,22,28,26,0,27,25,30,26],
[29,25,20,26,23,21,27,27,24,0,20,25,17],
[28,26,22,28,30,26,32,31,26,31,0,34,25],
[30,20,21,22,26,22,33,23,21,26,17,0,20],
[31,31,26,28,25,26,36,35,25,34,26,31,0]])



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
result = np.append(np.array([13, 51, 59, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,23,18,15,15,27,19,23,23,23,22,16],
[32,0,33,21,24,29,31,30,28,31,25,27,25],
[28,18,0,25,25,22,25,24,22,25,22,24,20],
[33,30,26,0,27,21,29,30,24,30,26,25,22],
[36,27,26,24,0,23,27,35,22,30,32,29,27],
[36,22,29,30,28,0,34,30,27,32,28,25,23],
[24,20,26,22,24,17,0,25,25,21,22,25,23],
[32,21,27,21,16,21,26,0,22,25,28,23,24],
[28,23,29,27,29,24,26,29,0,29,22,25,29],
[28,20,26,21,21,19,30,26,22,0,26,21,26],
[28,26,29,25,19,23,29,23,29,25,0,22,21],
[29,24,27,26,22,26,26,28,26,30,29,0,23],
[35,26,31,29,24,28,28,27,22,25,30,28,0]])



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
result = np.append(np.array([13, 51, 60, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,12,21,13,19,16,26,12,9,13,13,22],
[33,0,32,27,25,20,27,30,22,17,17,32,27],
[39,19,0,23,26,24,38,26,33,22,23,19,32],
[30,24,28,0,32,26,30,36,22,23,28,23,23],
[38,26,25,19,0,27,26,31,26,21,23,24,29],
[32,31,27,25,24,0,30,29,23,23,24,28,30],
[35,24,13,21,25,21,0,21,28,12,20,14,26],
[25,21,25,15,20,22,30,0,18,25,22,20,21],
[39,29,18,29,25,28,23,33,0,13,18,17,31],
[42,34,29,28,30,28,39,26,38,0,26,25,28],
[38,34,28,23,28,27,31,29,33,25,0,33,34],
[38,19,32,28,27,23,37,31,34,26,18,0,34],
[29,24,19,28,22,21,25,30,20,23,17,17,0]])



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
result = np.append(np.array([13, 51, 61, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,31,7,11,21,18,35,18,12,28,13,14],
[30,0,35,23,23,18,35,30,28,31,30,25,24],
[20,16,0,9,16,23,27,42,19,13,32,20,25],
[44,28,42,0,24,35,46,44,31,28,40,29,33],
[40,28,35,27,0,27,29,43,32,21,32,17,18],
[30,33,28,16,24,0,46,36,25,18,30,28,17],
[33,16,24,5,22,5,0,27,17,17,11,10,9],
[16,21,9,7,8,15,24,0,9,7,20,22,16],
[33,23,32,20,19,26,34,42,0,20,28,23,25],
[39,20,38,23,30,33,34,44,31,0,34,29,23],
[23,21,19,11,19,21,40,31,23,17,0,31,26],
[38,26,31,22,34,23,41,29,28,22,20,0,17],
[37,27,26,18,33,34,42,35,26,28,25,34,0]])



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
result = np.append(np.array([13, 51, 62, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,18,23,22,18,16,22,21,22,26,20,28],
[29,0,26,27,25,29,15,26,19,28,26,28,25],
[33,25,0,27,24,19,20,20,21,19,31,27,24],
[28,24,24,0,24,23,17,19,24,20,24,25,31],
[29,26,27,27,0,25,21,27,19,24,30,27,35],
[33,22,32,28,26,0,22,22,24,28,36,29,31],
[35,36,31,34,30,29,0,26,21,30,35,31,38],
[29,25,31,32,24,29,25,0,22,26,32,33,30],
[30,32,30,27,32,27,30,29,0,21,33,31,35],
[29,23,32,31,27,23,21,25,30,0,32,28,28],
[25,25,20,27,21,15,16,19,18,19,0,22,27],
[31,23,24,26,24,22,20,18,20,23,29,0,26],
[23,26,27,20,16,20,13,21,16,23,24,25,0]])



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
result = np.append(np.array([13, 51, 63, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,23,30,22,19,32,24,32,27,27,30,34],
[25,0,18,25,19,22,26,27,30,27,22,28,29],
[28,33,0,34,26,26,29,27,38,25,23,26,43],
[21,26,17,0,20,25,27,23,28,28,17,27,36],
[29,32,25,31,0,23,30,28,33,27,27,30,35],
[32,29,25,26,28,0,34,27,34,26,23,26,36],
[19,25,22,24,21,17,0,23,26,25,19,21,29],
[27,24,24,28,23,24,28,0,27,24,24,28,30],
[19,21,13,23,18,17,25,24,0,23,20,19,25],
[24,24,26,23,24,25,26,27,28,0,19,27,34],
[24,29,28,34,24,28,32,27,31,32,0,30,35],
[21,23,25,24,21,25,30,23,32,24,21,0,34],
[17,22,8,15,16,15,22,21,26,17,16,17,0]])



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
result = np.append(np.array([13, 51, 64, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,24,20,22,24,25,24,26,20,21,26,23],
[22,0,23,25,19,27,24,28,24,22,27,25,18],
[27,28,0,21,21,30,23,30,27,24,25,25,17],
[31,26,30,0,30,26,25,29,24,26,27,28,30],
[29,32,30,21,0,24,25,33,25,24,26,24,19],
[27,24,21,25,27,0,23,26,29,26,25,28,27],
[26,27,28,26,26,28,0,30,23,20,22,24,26],
[27,23,21,22,18,25,21,0,20,18,13,20,17],
[25,27,24,27,26,22,28,31,0,26,30,28,22],
[31,29,27,25,27,25,31,33,25,0,27,28,24],
[30,24,26,24,25,26,29,38,21,24,0,28,15],
[25,26,26,23,27,23,27,31,23,23,23,0,26],
[28,33,34,21,32,24,25,34,29,27,36,25,0]])



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
result = np.append(np.array([13, 51, 65, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,20,30,20,11,19,18,20,19,16,22,27],
[37,0,22,37,24,31,34,24,29,34,37,26,40],
[31,29,0,29,26,23,19,26,23,24,23,20,28],
[21,14,22,0,16,13,10,16,21,18,14,16,16],
[31,27,25,35,0,25,32,29,28,33,27,26,27],
[40,20,28,38,26,0,29,30,33,24,26,29,29],
[32,17,32,41,19,22,0,30,31,35,28,30,34],
[33,27,25,35,22,21,21,0,27,28,19,17,22],
[31,22,28,30,23,18,20,24,0,29,22,24,27],
[32,17,27,33,18,27,16,23,22,0,27,25,29],
[35,14,28,37,24,25,23,32,29,24,0,28,27],
[29,25,31,35,25,22,21,34,27,26,23,0,26],
[24,11,23,35,24,22,17,29,24,22,24,25,0]])



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
result = np.append(np.array([13, 51, 66, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,31,32,24,23,15,22,24,23,24,27,24],
[18,0,24,28,25,25,22,22,18,22,22,25,26],
[20,27,0,26,23,19,22,26,25,26,25,21,25],
[19,23,25,0,21,23,13,19,21,17,18,24,18],
[27,26,28,30,0,22,27,30,26,20,27,28,29],
[28,26,32,28,29,0,19,28,20,24,26,23,30],
[36,29,29,38,24,32,0,31,31,25,31,27,33],
[29,29,25,32,21,23,20,0,25,25,27,23,28],
[27,33,26,30,25,31,20,26,0,24,25,27,24],
[28,29,25,34,31,27,26,26,27,0,28,24,36],
[27,29,26,33,24,25,20,24,26,23,0,21,26],
[24,26,30,27,23,28,24,28,24,27,30,0,26],
[27,25,26,33,22,21,18,23,27,15,25,25,0]])



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
result = np.append(np.array([13, 51, 67, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,25,24,24,31,27,23,28,28,26,24,21],
[29,0,33,26,25,29,37,37,25,39,30,35,24],
[26,18,0,22,22,28,32,24,30,35,29,31,26],
[27,25,29,0,26,37,34,25,25,37,33,30,28],
[27,26,29,25,0,36,36,33,28,33,29,36,31],
[20,22,23,14,15,0,28,25,23,28,23,29,23],
[24,14,19,17,15,23,0,23,26,22,19,23,13],
[28,14,27,26,18,26,28,0,24,30,30,32,20],
[23,26,21,26,23,28,25,27,0,20,18,27,17],
[23,12,16,14,18,23,29,21,31,0,28,23,22],
[25,21,22,18,22,28,32,21,33,23,0,24,22],
[27,16,20,21,15,22,28,19,24,28,27,0,20],
[30,27,25,23,20,28,38,31,34,29,29,31,0]])



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
result = np.append(np.array([13, 51, 68, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,24,24,18,30,26,23,16,23,16,25,26],
[19,0,14,15,10,15,17,14,11,21,17,12,20],
[27,37,0,30,21,33,27,28,22,30,19,33,36],
[27,36,21,0,20,32,28,28,21,30,24,23,28],
[33,41,30,31,0,28,30,25,25,30,28,28,33],
[21,36,18,19,23,0,20,18,20,21,20,25,27],
[25,34,24,23,21,31,0,21,17,31,19,22,24],
[28,37,23,23,26,33,30,0,23,27,19,30,28],
[35,40,29,30,26,31,34,28,0,30,24,28,32],
[28,30,21,21,21,30,20,24,21,0,19,23,26],
[35,34,32,27,23,31,32,32,27,32,0,31,26],
[26,39,18,28,23,26,29,21,23,28,20,0,24],
[25,31,15,23,18,24,27,23,19,25,25,27,0]])



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
result = np.append(np.array([13, 51, 69, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,24,17,38,29,26,32,31,25,32,30,30],
[22,0,25,20,27,28,20,29,28,21,27,25,26],
[27,26,0,18,35,29,26,27,27,18,31,31,27],
[34,31,33,0,37,35,25,32,38,29,34,31,33],
[13,24,16,14,0,19,19,20,23,19,24,24,25],
[22,23,22,16,32,0,21,24,23,16,28,25,28],
[25,31,25,26,32,30,0,29,27,26,33,26,29],
[19,22,24,19,31,27,22,0,28,17,28,27,27],
[20,23,24,13,28,28,24,23,0,21,27,26,28],
[26,30,33,22,32,35,25,34,30,0,29,33,32],
[19,24,20,17,27,23,18,23,24,22,0,24,28],
[21,26,20,20,27,26,25,24,25,18,27,0,30],
[21,25,24,18,26,23,22,24,23,19,23,21,0]])



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
result = np.append(np.array([13, 51, 70, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,34,26,39,22,20,27,28,29,28,21,31],
[23,0,26,27,32,29,27,24,34,29,26,25,30],
[17,25,0,26,34,24,22,27,22,43,18,31,27],
[25,24,25,0,31,22,25,24,29,30,20,26,27],
[12,19,17,20,0,17,26,16,26,21,10,24,25],
[29,22,27,29,34,0,25,30,34,42,18,22,35],
[31,24,29,26,25,26,0,33,33,32,19,28,30],
[24,27,24,27,35,21,18,0,32,33,17,22,28],
[23,17,29,22,25,17,18,19,0,30,20,21,20],
[22,22,8,21,30,9,19,18,21,0,14,21,22],
[23,25,33,31,41,33,32,34,31,37,0,30,35],
[30,26,20,25,27,29,23,29,30,30,21,0,31],
[20,21,24,24,26,16,21,23,31,29,16,20,0]])



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
result = np.append(np.array([13, 51, 71, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,41,21,27,17,25,30,33,15,31,19,35],
[22,0,41,14,7,20,28,10,42,27,42,20,27],
[10,10,0,4,7,9,16,16,18,15,31,10,15],
[30,37,47,0,27,20,28,36,38,27,37,30,35],
[24,44,44,24,0,14,22,32,36,21,44,24,31],
[34,31,42,31,37,0,20,30,42,34,31,31,35],
[26,23,35,23,29,31,0,22,34,34,23,23,29],
[21,41,35,15,19,21,29,0,32,27,42,21,42],
[18,9,33,13,15,9,17,19,0,16,38,16,24],
[36,24,36,24,30,17,17,24,35,0,24,13,29],
[20,9,20,14,7,20,28,9,13,27,0,22,6],
[32,31,41,21,27,20,28,30,35,38,29,0,27],
[16,24,36,16,20,16,22,9,27,22,45,24,0]])



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
result = np.append(np.array([13, 51, 72, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,28,28,28,34,37,23,30,33,30,17,29],
[20,0,21,23,21,31,28,13,26,24,16,21,24],
[23,30,0,29,30,34,28,24,28,32,32,27,24],
[23,28,22,0,23,32,30,9,23,29,26,18,25],
[23,30,21,28,0,28,26,15,28,33,25,16,27],
[17,20,17,19,23,0,20,16,23,24,21,16,16],
[14,23,23,21,25,31,0,20,26,25,23,19,18],
[28,38,27,42,36,35,31,0,33,36,34,27,21],
[21,25,23,28,23,28,25,18,0,23,20,21,23],
[18,27,19,22,18,27,26,15,28,0,14,24,17],
[21,35,19,25,26,30,28,17,31,37,0,17,25],
[34,30,24,33,35,35,32,24,30,27,34,0,32],
[22,27,27,26,24,35,33,30,28,34,26,19,0]])



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
result = np.append(np.array([13, 51, 73, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,21,22,25,16,22,29,19,26,21,22,16],
[24,0,25,25,19,24,27,29,20,25,23,29,23],
[30,26,0,21,25,18,30,29,24,28,28,21,20],
[29,26,30,0,29,24,29,32,28,29,27,24,24],
[26,32,26,22,0,26,21,30,20,27,27,27,22],
[35,27,33,27,25,0,31,29,19,30,30,27,29],
[29,24,21,22,30,20,0,32,23,25,28,21,24],
[22,22,22,19,21,22,19,0,19,22,22,21,19],
[32,31,27,23,31,32,28,32,0,30,30,27,28],
[25,26,23,22,24,21,26,29,21,0,21,19,21],
[30,28,23,24,24,21,23,29,21,30,0,25,29],
[29,22,30,27,24,24,30,30,24,32,26,0,25],
[35,28,31,27,29,22,27,32,23,30,22,26,0]])



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
result = np.append(np.array([13, 51, 74, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,22,32,20,16,20,24,8,30,20,27,23],
[29,0,19,23,21,17,19,13,17,19,21,29,19],
[29,32,0,23,27,13,31,29,17,17,28,35,23],
[19,28,28,0,19,16,24,24,10,34,24,39,19],
[31,30,24,32,0,18,30,34,16,22,38,45,25],
[35,34,38,35,33,0,30,22,17,29,28,47,23],
[31,32,20,27,21,21,0,29,13,23,26,37,27],
[27,38,22,27,17,29,22,0,27,27,20,45,29],
[43,34,34,41,35,34,38,24,0,41,38,41,29],
[21,32,34,17,29,22,28,24,10,0,26,29,13],
[31,30,23,27,13,23,25,31,13,25,0,41,21],
[24,22,16,12,6,4,14,6,10,22,10,0,12],
[28,32,28,32,26,28,24,22,22,38,30,39,0]])



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
result = np.append(np.array([13, 51, 75, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,28,25,28,27,25,26,27,28,28,30,25],
[22,0,24,26,28,22,24,22,22,32,24,29,24],
[23,27,0,29,30,24,27,22,26,25,29,30,26],
[26,25,22,0,25,27,20,18,21,18,25,25,26],
[23,23,21,26,0,23,23,18,18,24,24,28,24],
[24,29,27,24,28,0,24,23,24,28,30,29,28],
[26,27,24,31,28,27,0,25,25,33,27,29,26],
[25,29,29,33,33,28,26,0,25,26,25,29,29],
[24,29,25,30,33,27,26,26,0,29,28,30,30],
[23,19,26,33,27,23,18,25,22,0,24,27,27],
[23,27,22,26,27,21,24,26,23,27,0,26,24],
[21,22,21,26,23,22,22,22,21,24,25,0,24],
[26,27,25,25,27,23,25,22,21,24,27,27,0]])



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
result = np.append(np.array([13, 51, 76, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,24,25,28,25,30,24,22,25,32,19,28],
[23,0,23,26,26,21,23,24,25,25,27,23,26],
[27,28,0,29,25,27,20,26,22,26,33,28,31],
[26,25,22,0,26,19,21,23,25,26,26,21,28],
[23,25,26,25,0,27,27,25,25,26,34,23,28],
[26,30,24,32,24,0,26,26,24,27,31,24,30],
[21,28,31,30,24,25,0,28,26,27,36,21,31],
[27,27,25,28,26,25,23,0,25,23,26,24,25],
[29,26,29,26,26,27,25,26,0,25,34,26,29],
[26,26,25,25,25,24,24,28,26,0,34,20,29],
[19,24,18,25,17,20,15,25,17,17,0,16,21],
[32,28,23,30,28,27,30,27,25,31,35,0,32],
[23,25,20,23,23,21,20,26,22,22,30,19,0]])



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
result = np.append(np.array([13, 51, 77, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,33,33,25,26,30,26,34,22,29,26,22],
[13,0,22,22,24,24,26,17,25,20,26,25,16],
[18,29,0,29,19,28,24,15,23,10,23,30,14],
[18,29,22,0,17,26,18,19,27,22,27,17,23],
[26,27,32,34,0,23,29,24,27,29,30,28,24],
[25,27,23,25,28,0,20,18,19,17,22,16,14],
[21,25,27,33,22,31,0,18,22,25,32,16,20],
[25,34,36,32,27,33,33,0,36,27,34,24,27],
[17,26,28,24,24,32,29,15,0,28,33,27,19],
[29,31,41,29,22,34,26,24,23,0,29,28,23],
[22,25,28,24,21,29,19,17,18,22,0,22,16],
[25,26,21,34,23,35,35,27,24,23,29,0,21],
[29,35,37,28,27,37,31,24,32,28,35,30,0]])



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
result = np.append(np.array([13, 51, 78, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,18,16,23,20,15,24,14,24,19,17,22],
[29,0,20,17,30,29,21,32,20,22,14,30,23],
[33,31,0,27,23,20,14,26,18,21,15,23,22],
[35,34,24,0,29,30,24,32,19,30,20,28,28],
[28,21,28,22,0,20,18,29,14,23,13,29,25],
[31,22,31,21,31,0,26,35,21,21,23,30,23],
[36,30,37,27,33,25,0,33,21,25,28,34,35],
[27,19,25,19,22,16,18,0,16,13,14,20,17],
[37,31,33,32,37,30,30,35,0,28,22,34,26],
[27,29,30,21,28,30,26,38,23,0,20,32,31],
[32,37,36,31,38,28,23,37,29,31,0,40,35],
[34,21,28,23,22,21,17,31,17,19,11,0,32],
[29,28,29,23,26,28,16,34,25,20,16,19,0]])



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
result = np.append(np.array([13, 51, 79, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,36,32,36,37,32,22,29,26,35,30,31],
[24,0,33,32,34,30,30,31,29,27,33,31,25],
[15,18,0,18,17,19,28,21,17,22,26,17,21],
[19,19,33,0,28,27,25,21,23,23,28,28,20],
[15,17,34,23,0,28,26,18,24,20,28,24,22],
[14,21,32,24,23,0,29,25,21,22,27,22,28],
[19,21,23,26,25,22,0,19,20,21,25,23,26],
[29,20,30,30,33,26,32,0,27,27,30,28,28],
[22,22,34,28,27,30,31,24,0,25,34,24,29],
[25,24,29,28,31,29,30,24,26,0,37,25,29],
[16,18,25,23,23,24,26,21,17,14,0,22,24],
[21,20,34,23,27,29,28,23,27,26,29,0,27],
[20,26,30,31,29,23,25,23,22,22,27,24,0]])



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
result = np.append(np.array([13, 51, 80, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,21,30,17,24,33,21,26,17,18,25,27],
[29,0,26,27,24,23,31,19,28,18,21,20,29],
[30,25,0,32,29,32,32,19,35,22,27,24,35],
[21,24,19,0,22,20,23,19,21,16,19,17,22],
[34,27,22,29,0,27,36,18,30,26,27,19,29],
[27,28,19,31,24,0,31,15,24,14,17,23,31],
[18,20,19,28,15,20,0,19,15,17,21,22,27],
[30,32,32,32,33,36,32,0,30,25,29,30,32],
[25,23,16,30,21,27,36,21,0,22,25,27,32],
[34,33,29,35,25,37,34,26,29,0,30,19,31],
[33,30,24,32,24,34,30,22,26,21,0,28,30],
[26,31,27,34,32,28,29,21,24,32,23,0,24],
[24,22,16,29,22,20,24,19,19,20,21,27,0]])



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
result = np.append(np.array([13, 51, 81, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,21,17,26,12,17,16,20,14,13,19,21],
[35,0,26,18,27,34,29,25,27,21,20,20,29],
[30,25,0,22,33,18,20,16,22,26,24,25,24],
[34,33,29,0,28,29,21,24,28,31,21,18,24],
[25,24,18,23,0,17,17,17,27,24,23,18,28],
[39,17,33,22,34,0,25,21,32,19,18,21,29],
[34,22,31,30,34,26,0,29,32,21,27,32,35],
[35,26,35,27,34,30,22,0,24,29,21,34,33],
[31,24,29,23,24,19,19,27,0,25,23,18,32],
[37,30,25,20,27,32,30,22,26,0,29,24,32],
[38,31,27,30,28,33,24,30,28,22,0,20,33],
[32,31,26,33,33,30,19,17,33,27,31,0,35],
[30,22,27,27,23,22,16,18,19,19,18,16,0]])



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
result = np.append(np.array([13, 51, 82, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,20,15,17,25,19,18,20,22,20,17,20],
[26,0,19,20,16,23,17,14,23,21,20,14,20],
[31,32,0,24,24,26,24,22,25,19,22,21,30],
[36,31,27,0,25,29,20,22,22,24,26,22,31],
[34,35,27,26,0,27,19,23,30,28,23,26,31],
[26,28,25,22,24,0,22,22,27,21,22,24,32],
[32,34,27,31,32,29,0,24,30,25,24,27,34],
[33,37,29,29,28,29,27,0,27,23,26,25,30],
[31,28,26,29,21,24,21,24,0,24,21,22,26],
[29,30,32,27,23,30,26,28,27,0,22,22,30],
[31,31,29,25,28,29,27,25,30,29,0,21,30],
[34,37,30,29,25,27,24,26,29,29,30,0,33],
[31,31,21,20,20,19,17,21,25,21,21,18,0]])



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
result = np.append(np.array([13, 51, 83, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,28,43,31,38,39,26,21,45,23,45,31],
[19,0,26,31,25,26,31,24,16,37,18,31,31],
[23,25,0,33,31,22,24,24,12,29,23,37,28],
[8,20,18,0,13,18,23,31,16,33,24,41,20],
[20,26,20,38,0,33,27,30,27,37,24,44,29],
[13,25,29,33,18,0,27,26,25,34,27,39,24],
[12,20,27,28,24,24,0,28,20,35,20,44,29],
[25,27,27,20,21,25,23,0,11,30,18,31,20],
[30,35,39,35,24,26,31,40,0,46,23,47,26],
[6,14,22,18,14,17,16,21,5,0,6,22,10],
[28,33,28,27,27,24,31,33,28,45,0,39,28],
[6,20,14,10,7,12,7,20,4,29,12,0,14],
[20,20,23,31,22,27,22,31,25,41,23,37,0]])



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
result = np.append(np.array([13, 51, 84, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,22,24,23,21,27,19,22,18,29,18,22],
[26,0,28,25,21,19,24,22,24,19,32,21,30],
[29,23,0,26,25,24,27,21,25,18,28,26,28],
[27,26,25,0,23,21,24,19,21,23,29,16,26],
[28,30,26,28,0,25,28,26,25,23,30,17,30],
[30,32,27,30,26,0,29,26,24,29,35,23,30],
[24,27,24,27,23,22,0,24,30,21,32,15,28],
[32,29,30,32,25,25,27,0,27,27,37,27,35],
[29,27,26,30,26,27,21,24,0,19,29,17,24],
[33,32,33,28,28,22,30,24,32,0,39,26,35],
[22,19,23,22,21,16,19,14,22,12,0,19,25],
[33,30,25,35,34,28,36,24,34,25,32,0,30],
[29,21,23,25,21,21,23,16,27,16,26,21,0]])



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
result = np.append(np.array([13, 51, 85, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,23,29,29,37,25,29,29,33,31,37,33],
[22,0,21,18,35,23,6,18,19,23,31,33,17],
[28,30,0,21,32,37,11,23,20,27,33,29,34],
[22,33,30,0,34,31,23,26,20,35,33,42,27],
[22,16,19,17,0,28,11,17,20,19,33,34,28],
[14,28,14,20,23,0,16,20,20,24,24,29,18],
[26,45,40,28,40,35,0,17,29,41,45,32,45],
[22,33,28,25,34,31,34,0,34,47,28,42,28],
[22,32,31,31,31,31,22,17,0,32,41,40,27],
[18,28,24,16,32,27,10,4,19,0,32,38,27],
[20,20,18,18,18,27,6,23,10,19,0,33,11],
[14,18,22,9,17,22,19,9,11,13,18,0,13],
[18,34,17,24,23,33,6,23,24,24,40,38,0]])



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
result = np.append(np.array([13, 51, 86, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,24,35,16,26,14,21,20,28,32,25,11],
[33,0,27,32,19,29,29,21,25,25,38,30,23],
[27,24,0,26,19,31,18,23,24,30,35,21,20],
[16,19,25,0,16,21,10,26,21,27,29,29,18],
[35,32,32,35,0,34,20,30,30,31,32,25,22],
[25,22,20,30,17,0,22,25,23,27,35,28,22],
[37,22,33,41,31,29,0,29,34,35,44,29,27],
[30,30,28,25,21,26,22,0,25,36,35,23,22],
[31,26,27,30,21,28,17,26,0,34,30,35,19],
[23,26,21,24,20,24,16,15,17,0,22,29,12],
[19,13,16,22,19,16,7,16,21,29,0,22,10],
[26,21,30,22,26,23,22,28,16,22,29,0,24],
[40,28,31,33,29,29,24,29,32,39,41,27,0]])



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
result = np.append(np.array([13, 51, 87, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,42,15,15,15,32,26,27,25,37,15,24],
[20,0,42,10,25,10,42,46,27,25,37,25,20],
[9,9,0,19,9,0,17,26,10,9,27,0,9],
[36,41,32,0,41,27,32,36,37,24,37,32,36],
[36,26,42,10,0,10,42,26,27,15,37,5,9],
[36,41,51,24,41,0,41,36,36,24,46,41,19],
[19,9,34,19,9,10,0,26,10,19,10,5,9],
[25,5,25,15,25,15,25,0,10,25,20,25,25],
[24,24,41,14,24,15,41,41,0,24,51,24,24],
[26,26,42,27,36,27,32,26,27,0,37,22,26],
[14,14,24,14,14,5,41,31,0,14,0,5,14],
[36,26,51,19,46,10,46,26,27,29,46,0,29],
[27,31,42,15,42,32,42,26,27,25,37,22,0]])



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
result = np.append(np.array([13, 51, 88, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,32,16,21,21,19,23,6,27,24,17,18],
[24,0,32,40,0,18,24,20,21,14,36,9,15],
[19,19,0,19,19,27,25,9,19,24,21,19,9],
[35,11,32,0,11,19,20,17,14,17,14,11,26],
[30,51,32,40,0,34,34,20,21,33,39,20,18],
[30,33,24,32,17,0,24,20,21,14,34,20,23],
[32,27,26,31,17,27,0,17,14,17,24,17,12],
[28,31,42,34,31,31,34,0,31,34,39,31,19],
[45,30,32,37,30,30,37,20,0,27,24,30,20],
[24,37,27,34,18,37,34,17,24,0,36,14,9],
[27,15,30,37,12,17,27,12,27,15,0,15,15],
[34,42,32,40,31,31,34,20,21,37,36,0,22],
[33,36,42,25,33,28,39,32,31,42,36,29,0]])



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
result = np.append(np.array([13, 51, 89, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,23,21,25,24,28,19,19,28,26,19,21],
[28,0,28,20,24,29,31,21,26,28,27,25,23],
[28,23,0,28,27,24,28,24,23,31,28,25,22],
[30,31,23,0,27,25,26,26,22,29,29,29,30],
[26,27,24,24,0,25,28,18,24,32,25,25,22],
[27,22,27,26,26,0,29,24,26,31,28,23,24],
[23,20,23,25,23,22,0,17,25,30,24,19,21],
[32,30,27,25,33,27,34,0,29,33,31,33,31],
[32,25,28,29,27,25,26,22,0,33,26,30,24],
[23,23,20,22,19,20,21,18,18,0,19,18,22],
[25,24,23,22,26,23,27,20,25,32,0,21,20],
[32,26,26,22,26,28,32,18,21,33,30,0,25],
[30,28,29,21,29,27,30,20,27,29,31,26,0]])



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
result = np.append(np.array([13, 51, 90, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,28,21,22,15,27,19,27,28,32,19,25],
[24,0,19,25,22,20,26,20,32,32,25,21,25],
[23,32,0,26,18,19,25,18,27,32,26,20,27],
[30,26,25,0,23,16,28,23,27,26,26,29,21],
[29,29,33,28,0,24,29,29,38,35,33,30,26],
[36,31,32,35,27,0,34,31,30,38,33,24,30],
[24,25,26,23,22,17,0,20,29,30,25,24,23],
[32,31,33,28,22,20,31,0,30,33,33,22,30],
[24,19,24,24,13,21,22,21,0,34,30,13,27],
[23,19,19,25,16,13,21,18,17,0,20,12,26],
[19,26,25,25,18,18,26,18,21,31,0,18,27],
[32,30,31,22,21,27,27,29,38,39,33,0,28],
[26,26,24,30,25,21,28,21,24,25,24,23,0]])



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
result = np.append(np.array([13, 51, 91, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,38,39,38,38,17,39,39,38,39,39,38],
[12,0,0,13,12,12,12,35,12,12,1,12,12],
[13,51,0,51,34,50,13,35,35,34,23,35,50],
[12,38,0,0,22,34,12,34,0,34,0,34,28],
[13,39,17,29,0,50,29,51,1,28,1,35,28],
[13,39,1,17,1,0,1,35,1,1,1,13,16],
[34,39,38,39,22,50,0,51,22,38,23,34,50],
[12,16,16,17,0,16,0,0,0,16,0,12,16],
[12,39,16,51,50,50,29,51,0,50,17,34,28],
[13,39,17,17,23,50,13,35,1,0,1,35,28],
[12,50,28,51,50,50,28,51,34,50,0,34,50],
[12,39,16,17,16,38,17,39,17,16,17,0,16],
[13,39,1,23,23,35,1,35,23,23,1,35,0]])



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
result = np.append(np.array([13, 51, 92, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,26,21,28,30,14,26,26,23,24,23,26],
[26,0,14,32,21,30,16,33,25,34,34,20,33],
[25,37,0,24,35,28,28,38,34,41,42,35,40],
[30,19,27,0,24,25,13,25,30,28,23,22,33],
[23,30,16,27,0,28,11,40,24,31,25,13,25],
[21,21,23,26,23,0,17,27,33,32,30,14,26],
[37,35,23,38,40,34,0,35,41,34,42,26,38],
[25,18,13,26,11,24,16,0,18,27,27,13,16],
[25,26,17,21,27,18,10,33,0,30,25,14,30],
[28,17,10,23,20,19,17,24,21,0,21,10,26],
[27,17,9,28,26,21,9,24,26,30,0,18,29],
[28,31,16,29,38,37,25,38,37,41,33,0,40],
[25,18,11,18,26,25,13,35,21,25,22,11,0]])



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
result = np.append(np.array([13, 51, 93, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,38,26,29,31,27,30,25,32,31,27,27],
[17,0,22,24,24,18,29,19,23,31,23,22,29],
[13,29,0,26,19,14,24,13,12,26,24,20,23],
[25,27,25,0,19,18,21,21,19,29,24,18,20],
[22,27,32,32,0,22,24,25,14,25,29,19,32],
[20,33,37,33,29,0,33,27,25,36,26,27,31],
[24,22,27,30,27,18,0,28,18,27,28,21,15],
[21,32,38,30,26,24,23,0,20,22,30,23,23],
[26,28,39,32,37,26,33,31,0,28,25,30,33],
[19,20,25,22,26,15,24,29,23,0,24,19,29],
[20,28,27,27,22,25,23,21,26,27,0,23,20],
[24,29,31,33,32,24,30,28,21,32,28,0,25],
[24,22,28,31,19,20,36,28,18,22,31,26,0]])



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
result = np.append(np.array([13, 51, 94, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,22,18,25,20,19,27,20,25,23,25,22],
[28,0,20,23,23,22,23,24,24,26,25,26,24],
[29,31,0,19,25,28,24,26,24,28,30,26,27],
[33,28,32,0,28,33,20,29,26,27,21,27,23],
[26,28,26,23,0,24,25,23,20,22,26,25,21],
[31,29,23,18,27,0,27,23,28,29,25,25,28],
[32,28,27,31,26,24,0,32,26,29,30,25,29],
[24,27,25,22,28,28,19,0,28,29,28,24,25],
[31,27,27,25,31,23,25,23,0,27,24,26,24],
[26,25,23,24,29,22,22,22,24,0,25,22,24],
[28,26,21,30,25,26,21,23,27,26,0,23,23],
[26,25,25,24,26,26,26,27,25,29,28,0,22],
[29,27,24,28,30,23,22,26,27,27,28,29,0]])



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
result = np.append(np.array([13, 51, 95, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,28,29,24,26,25,27,24,18,22,21,21],
[23,0,29,26,24,23,22,25,26,24,27,24,25],
[23,22,0,24,18,25,25,26,25,21,27,23,22],
[22,25,27,0,15,24,25,24,25,18,22,24,21],
[27,27,33,36,0,25,28,28,29,26,31,29,27],
[25,28,26,27,26,0,29,24,26,25,31,25,28],
[26,29,26,26,23,22,0,27,26,17,27,26,24],
[24,26,25,27,23,27,24,0,27,20,27,24,21],
[27,25,26,26,22,25,25,24,0,20,25,23,25],
[33,27,30,33,25,26,34,31,31,0,29,29,27],
[29,24,24,29,20,20,24,24,26,22,0,22,19],
[30,27,28,27,22,26,25,27,28,22,29,0,25],
[30,26,29,30,24,23,27,30,26,24,32,26,0]])



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
result = np.append(np.array([13, 51, 96, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,16,22,26,35,20,32,25,29,30,28,16],
[26,0,23,31,19,42,26,29,33,37,34,36,21],
[35,28,0,32,26,33,28,22,39,41,41,24,32],
[29,20,19,0,26,35,23,25,27,27,32,25,23],
[25,32,25,25,0,30,24,26,31,35,29,31,25],
[16,9,18,16,21,0,15,23,19,21,23,16,17],
[31,25,23,28,27,36,0,24,30,32,30,32,26],
[19,22,29,26,25,28,27,0,30,31,31,33,26],
[26,18,12,24,20,32,21,21,0,17,24,22,16],
[22,14,10,24,16,30,19,20,34,0,24,25,12],
[21,17,10,19,22,28,21,20,27,27,0,16,16],
[23,15,27,26,20,35,19,18,29,26,35,0,21],
[35,30,19,28,26,34,25,25,35,39,35,30,0]])



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
result = np.append(np.array([13, 51, 97, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,29,27,22,24,24,25,27,27,23,23,23],
[33,0,29,34,27,34,25,24,28,26,24,28,22],
[22,22,0,23,22,22,21,26,24,24,23,24,19],
[24,17,28,0,21,24,19,19,21,19,18,17,24],
[29,24,29,30,0,27,22,25,23,27,24,29,23],
[27,17,29,27,24,0,23,21,25,22,23,22,18],
[27,26,30,32,29,28,0,26,23,28,29,30,28],
[26,27,25,32,26,30,25,0,28,29,30,26,24],
[24,23,27,30,28,26,28,23,0,26,22,20,20],
[24,25,27,32,24,29,23,22,25,0,22,26,23],
[28,27,28,33,27,28,22,21,29,29,0,32,25],
[28,23,27,34,22,29,21,25,31,25,19,0,22],
[28,29,32,27,28,33,23,27,31,28,26,29,0]])



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
result = np.append(np.array([13, 51, 98, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,21,20,14,26,20,21,19,17,20,16,23],
[34,0,31,30,24,33,29,22,27,26,26,26,24],
[30,20,0,24,17,24,23,26,28,19,21,25,28],
[31,21,27,0,21,25,27,24,27,21,22,22,25],
[37,27,34,30,0,30,27,23,30,27,34,28,30],
[25,18,27,26,21,0,26,23,21,24,22,20,29],
[31,22,28,24,24,25,0,23,25,24,24,23,27],
[30,29,25,27,28,28,28,0,31,24,28,29,28],
[32,24,23,24,21,30,26,20,0,22,19,20,21],
[34,25,32,30,24,27,27,27,29,0,25,26,30],
[31,25,30,29,17,29,27,23,32,26,0,24,26],
[35,25,26,29,23,31,28,22,31,25,27,0,29],
[28,27,23,26,21,22,24,23,30,21,25,22,0]])



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
result = np.append(np.array([13, 51, 99, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,22,28,26,27,26,23,28,23,24,33,29],
[25,0,22,28,26,26,25,21,25,24,28,32,27],
[29,29,0,28,33,31,30,29,28,23,28,34,31],
[23,23,23,0,26,24,22,27,23,20,28,31,28],
[25,25,18,25,0,22,16,22,27,22,28,30,26],
[24,25,20,27,29,0,23,25,28,23,30,30,32],
[25,26,21,29,35,28,0,25,26,26,32,33,30],
[28,30,22,24,29,26,26,0,29,27,30,33,32],
[23,26,23,28,24,23,25,22,0,26,24,28,29],
[28,27,28,31,29,28,25,24,25,0,31,30,29],
[27,23,23,23,23,21,19,21,27,20,0,28,27],
[18,19,17,20,21,21,18,18,23,21,23,0,24],
[22,24,20,23,25,19,21,19,22,22,24,27,0]])



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
result = np.append(np.array([13, 51, 100, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,25,26,25,27,26,19,26,22,28,25,20],
[25,0,24,22,29,23,28,18,26,25,30,25,21],
[26,27,0,28,21,26,36,27,25,28,24,30,27],
[25,29,23,0,28,22,21,23,31,26,23,25,19],
[26,22,30,23,0,24,26,21,25,21,27,22,21],
[24,28,25,29,27,0,24,24,31,26,25,21,18],
[25,23,15,30,25,27,0,19,21,26,20,21,20],
[32,33,24,28,30,27,32,0,28,27,32,30,25],
[25,25,26,20,26,20,30,23,0,29,26,23,25],
[29,26,23,25,30,25,25,24,22,0,26,25,30],
[23,21,27,28,24,26,31,19,25,25,0,24,20],
[26,26,21,26,29,30,30,21,28,26,27,0,24],
[31,30,24,32,30,33,31,26,26,21,31,27,0]])



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
result = np.append(np.array([13, 51, 101, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,24,24,19,21,26,20,27,22,24,27,21],
[25,0,25,26,20,23,26,20,27,27,23,27,25],
[27,26,0,28,22,23,26,27,28,30,22,28,27],
[27,25,23,0,19,24,24,21,27,27,26,24,23],
[32,31,29,32,0,24,29,29,29,32,26,30,27],
[30,28,28,27,27,0,30,24,25,33,26,26,28],
[25,25,25,27,22,21,0,25,21,25,21,24,26],
[31,31,24,30,22,27,26,0,28,29,27,29,28],
[24,24,23,24,22,26,30,23,0,27,23,17,26],
[29,24,21,24,19,18,26,22,24,0,19,24,24],
[27,28,29,25,25,25,30,24,28,32,0,27,29],
[24,24,23,27,21,25,27,22,34,27,24,0,22],
[30,26,24,28,24,23,25,23,25,27,22,29,0]])



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
result = np.append(np.array([13, 51, 102, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,27,26,27,27,25,27,28,29,25,30,31],
[31,0,27,30,30,31,30,30,25,36,28,27,29],
[24,24,0,29,24,25,27,28,22,31,26,23,34],
[25,21,22,0,25,23,22,24,26,29,26,21,31],
[24,21,27,26,0,25,18,23,21,31,22,30,27],
[24,20,26,28,26,0,17,28,27,28,21,27,30],
[26,21,24,29,33,34,0,29,30,33,28,32,31],
[24,21,23,27,28,23,22,0,23,32,21,23,24],
[23,26,29,25,30,24,21,28,0,34,26,29,32],
[22,15,20,22,20,23,18,19,17,0,20,24,25],
[26,23,25,25,29,30,23,30,25,31,0,26,30],
[21,24,28,30,21,24,19,28,22,27,25,0,29],
[20,22,17,20,24,21,20,27,19,26,21,22,0]])



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
result = np.append(np.array([13, 51, 103, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,27,16,19,22,19,16,21,17,27,19,23],
[31,0,29,27,29,27,27,19,27,25,33,24,28],
[24,22,0,17,23,20,22,19,25,23,21,23,20],
[35,24,34,0,29,31,27,26,23,27,34,29,32],
[32,22,28,22,0,26,25,19,22,17,32,25,22],
[29,24,31,20,25,0,25,26,21,20,31,28,26],
[32,24,29,24,26,26,0,25,29,24,31,29,28],
[35,32,32,25,32,25,26,0,30,28,31,24,24],
[30,24,26,28,29,30,22,21,0,27,31,27,27],
[34,26,28,24,34,31,27,23,24,0,29,28,26],
[24,18,30,17,19,20,20,20,20,22,0,21,20],
[32,27,28,22,26,23,22,27,24,23,30,0,30],
[28,23,31,19,29,25,23,27,24,25,31,21,0]])



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
result = np.append(np.array([13, 51, 104, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,25,22,25,26,29,28,23,24,28,28,27],
[22,0,27,23,19,23,23,26,23,24,28,25,24],
[26,24,0,21,25,28,30,23,22,24,29,23,23],
[29,28,30,0,31,28,28,23,27,26,29,30,29],
[26,32,26,20,0,23,26,28,24,23,31,26,22],
[25,28,23,23,28,0,28,21,21,22,28,28,26],
[22,28,21,23,25,23,0,24,22,22,24,28,25],
[23,25,28,28,23,30,27,0,26,27,28,30,30],
[28,28,29,24,27,30,29,25,0,29,30,25,28],
[27,27,27,25,28,29,29,24,22,0,33,28,27],
[23,23,22,22,20,23,27,23,21,18,0,23,23],
[23,26,28,21,25,23,23,21,26,23,28,0,24],
[24,27,28,22,29,25,26,21,23,24,28,27,0]])



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
result = np.append(np.array([13, 51, 105, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,35,35,29,21,22,28,15,15,23,12,24],
[32,0,41,41,36,20,28,27,24,22,29,21,23],
[16,10,0,20,29,20,10,20,20,17,13,9,14],
[16,10,31,0,36,13,14,28,10,17,21,10,17],
[22,15,22,15,0,21,13,20,12,22,11,4,20],
[30,31,31,38,30,0,34,35,34,12,20,27,35],
[29,23,41,37,38,17,0,43,15,15,23,23,24],
[23,24,31,23,31,16,8,0,23,16,17,17,24],
[36,27,31,41,39,17,36,28,0,27,16,23,27],
[36,29,34,34,29,39,36,35,24,0,22,29,31],
[28,22,38,30,40,31,28,34,35,29,0,28,30],
[39,30,42,41,47,24,28,34,28,22,23,0,28],
[27,28,37,34,31,16,27,27,24,20,21,23,0]])



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
result = np.append(np.array([13, 51, 106, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,22,29,29,40,22,22,44,44,36,8,25],
[43,0,14,21,21,32,14,21,43,43,43,11,25],
[29,37,0,29,7,32,15,18,43,29,43,22,18],
[22,30,22,0,0,25,8,0,36,22,36,22,11],
[22,30,44,51,0,44,19,19,44,36,36,30,36],
[11,19,19,26,7,0,8,0,25,22,11,11,11],
[29,37,36,43,32,43,0,18,43,43,43,22,32],
[29,30,33,51,32,51,33,0,36,36,36,22,25],
[7,8,8,15,7,26,8,15,0,11,7,8,0],
[7,8,22,29,15,29,8,15,40,0,32,8,25],
[15,8,8,15,15,40,8,15,44,19,0,8,0],
[43,40,29,29,21,40,29,29,43,43,43,0,32],
[26,26,33,40,15,40,19,26,51,26,51,19,0]])



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
result = np.append(np.array([13, 51, 107, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,27,33,28,31,19,20,24,14,28,21,21],
[24,0,27,29,29,28,20,21,16,22,21,15,22],
[24,24,0,28,24,32,23,19,13,17,25,22,23],
[18,22,23,0,15,21,11,18,20,15,15,16,22],
[23,22,27,36,0,27,25,24,27,19,31,19,26],
[20,23,19,30,24,0,22,13,20,12,26,14,18],
[32,31,28,40,26,29,0,29,22,24,32,29,29],
[31,30,32,33,27,38,22,0,23,29,31,26,21],
[27,35,38,31,24,31,29,28,0,24,31,33,31],
[37,29,34,36,32,39,27,22,27,0,36,28,30],
[23,30,26,36,20,25,19,20,20,15,0,18,24],
[30,36,29,35,32,37,22,25,18,23,33,0,25],
[30,29,28,29,25,33,22,30,20,21,27,26,0]])



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
result = np.append(np.array([13, 51, 108, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,27,20,19,32,32,22,29,25,23,21,18],
[27,0,27,29,26,26,23,26,29,27,23,23,16],
[24,24,0,27,29,27,34,22,36,27,25,24,23],
[31,22,24,0,23,34,29,26,29,31,21,26,24],
[32,25,22,28,0,28,35,31,30,32,27,25,23],
[19,25,24,17,23,0,28,22,24,22,22,19,21],
[19,28,17,22,16,23,0,22,20,20,21,20,12],
[29,25,29,25,20,29,29,0,32,30,19,25,24],
[22,22,15,22,21,27,31,19,0,28,20,16,14],
[26,24,24,20,19,29,31,21,23,0,23,23,16],
[28,28,26,30,24,29,30,32,31,28,0,25,23],
[30,28,27,25,26,32,31,26,35,28,26,0,26],
[33,35,28,27,28,30,39,27,37,35,28,25,0]])



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
result = np.append(np.array([13, 51, 109, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,26,27,24,30,26,21,26,21,27,26,25],
[25,0,30,33,27,34,26,30,24,21,28,27,26],
[25,21,0,28,24,27,21,24,17,18,22,22,22],
[24,18,23,0,23,28,21,24,21,19,21,22,25],
[27,24,27,28,0,28,26,30,22,23,25,24,27],
[21,17,24,23,23,0,20,24,21,20,23,19,21],
[25,25,30,30,25,31,0,28,22,25,25,28,31],
[30,21,27,27,21,27,23,0,21,22,25,27,23],
[25,27,34,30,29,30,29,30,0,24,26,32,26],
[30,30,33,32,28,31,26,29,27,0,25,26,33],
[24,23,29,30,26,28,26,26,25,26,0,28,25],
[25,24,29,29,27,32,23,24,19,25,23,0,24],
[26,25,29,26,24,30,20,28,25,18,26,27,0]])



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
result = np.append(np.array([13, 51, 110, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,27,26,30,31,39,26,16,25,28,12,23],
[30,0,25,23,10,29,20,28,16,23,28,31,20],
[24,26,0,23,10,37,34,13,16,34,28,21,29],
[25,28,28,0,17,31,28,20,19,36,24,21,28],
[21,41,41,34,0,50,45,32,24,30,29,32,26],
[20,22,14,20,1,0,31,11,14,31,25,22,10],
[12,31,17,23,6,20,0,10,3,21,15,21,8],
[25,23,38,31,19,40,41,0,25,34,28,30,24],
[35,35,35,32,27,37,48,26,0,37,36,19,43],
[26,28,17,15,21,20,30,17,14,0,29,22,16],
[23,23,23,27,22,26,36,23,15,22,0,14,22],
[39,20,30,30,19,29,30,21,32,29,37,0,29],
[28,31,22,23,25,41,43,27,8,35,29,22,0]])



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
result = np.append(np.array([13, 51, 111, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,18,41,27,27,26,24,40,40,49,16,40],
[21,0,21,21,37,21,21,21,23,33,37,21,33],
[33,30,0,25,27,23,22,33,24,24,49,22,24],
[10,30,26,0,26,26,26,10,12,24,26,10,40],
[24,14,24,25,0,24,24,24,24,24,24,22,24],
[24,30,28,25,27,0,38,24,24,24,49,10,40],
[25,30,29,25,27,13,0,25,14,25,41,11,40],
[27,30,18,41,27,27,26,0,40,40,49,16,40],
[11,28,27,39,27,27,37,11,0,33,37,27,49],
[11,18,27,27,27,27,26,11,18,0,37,16,26],
[2,14,2,25,27,2,10,2,14,14,0,0,24],
[35,30,29,41,29,41,40,35,24,35,51,0,40],
[11,18,27,11,27,11,11,11,2,25,27,11,0]])



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
result = np.append(np.array([13, 51, 112, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,29,25,29,23,26,24,25,24,35,25,26],
[29,0,31,26,33,25,34,26,36,24,36,25,31],
[22,20,0,17,25,20,26,20,27,19,27,17,27],
[26,25,34,0,28,28,33,29,26,26,30,25,29],
[22,18,26,23,0,22,28,29,26,19,32,23,25],
[28,26,31,23,29,0,31,26,29,24,32,27,29],
[25,17,25,18,23,20,0,26,25,22,28,22,23],
[27,25,31,22,22,25,25,0,25,24,26,23,26],
[26,15,24,25,25,22,26,26,0,24,33,23,25],
[27,27,32,25,32,27,29,27,27,0,33,24,30],
[16,15,24,21,19,19,23,25,18,18,0,20,18],
[26,26,34,26,28,24,29,28,28,27,31,0,31],
[25,20,24,22,26,22,28,25,26,21,33,20,0]])



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
result = np.append(np.array([13, 51, 113, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,21,22,34,27,26,26,20,21,43,28,12],
[23,0,27,21,20,26,29,26,21,28,30,27,20],
[30,24,0,35,36,31,29,15,25,26,45,22,28],
[29,30,16,0,14,20,28,21,30,17,37,29,27],
[17,31,15,37,0,30,35,22,18,26,38,29,29],
[24,25,20,31,21,0,22,22,24,23,25,23,21],
[25,22,22,23,16,29,0,13,22,15,31,27,22],
[25,25,36,30,29,29,38,0,31,24,32,35,29],
[31,30,26,21,33,27,29,20,0,29,35,27,33],
[30,23,25,34,25,28,36,27,22,0,37,27,29],
[8,21,6,14,13,26,20,19,16,14,0,27,7],
[23,24,29,22,22,28,24,16,24,24,24,0,29],
[39,31,23,24,22,30,29,22,18,22,44,22,0]])



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
result = np.append(np.array([13, 51, 114, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,25,25,22,42,22,25,21,22,24,20,28],
[21,0,19,19,21,28,18,18,25,22,25,13,22],
[26,32,0,37,26,41,31,20,34,26,33,20,31],
[26,32,14,0,23,31,24,14,25,15,36,23,31],
[29,30,25,28,0,41,25,21,23,27,25,21,30],
[9,23,10,20,10,0,13,17,22,15,21,17,18],
[29,33,20,27,26,38,0,29,28,26,26,22,30],
[26,33,31,37,30,34,22,0,36,19,39,26,40],
[30,26,17,26,28,29,23,15,0,14,32,23,36],
[29,29,25,36,24,36,25,32,37,0,33,16,34],
[27,26,18,15,26,30,25,12,19,18,0,20,32],
[31,38,31,28,30,34,29,25,28,35,31,0,35],
[23,29,20,20,21,33,21,11,15,17,19,16,0]])



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
result = np.append(np.array([13, 51, 115, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,27,18,21,20,22,26,23,26,22,29,26],
[26,0,26,17,26,22,21,23,23,30,26,27,28],
[24,25,0,23,26,24,21,25,25,27,22,32,29],
[33,34,28,0,30,28,25,28,31,33,26,30,30],
[30,25,25,21,0,23,21,27,21,22,22,32,25],
[31,29,27,23,28,0,25,28,25,27,31,31,27],
[29,30,30,26,30,26,0,30,28,24,26,33,28],
[25,28,26,23,24,23,21,0,26,24,26,32,25],
[28,28,26,20,30,26,23,25,0,28,27,32,29],
[25,21,24,18,29,24,27,27,23,0,23,27,27],
[29,25,29,25,29,20,25,25,24,28,0,29,27],
[22,24,19,21,19,20,18,19,19,24,22,0,23],
[25,23,22,21,26,24,23,26,22,24,24,28,0]])



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
result = np.append(np.array([13, 51, 116, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,17,20,22,14,25,24,23,19,22,20,20],
[24,0,21,19,29,28,22,28,14,19,27,22,14],
[34,30,0,21,23,23,32,32,23,22,32,20,26],
[31,32,30,0,23,29,32,35,30,23,22,22,27],
[29,22,28,28,0,27,32,30,26,26,22,21,24],
[37,23,28,22,24,0,25,37,19,19,27,24,21],
[26,29,19,19,19,26,0,31,26,24,26,22,21],
[27,23,19,16,21,14,20,0,20,17,21,15,17],
[28,37,28,21,25,32,25,31,0,23,32,21,28],
[32,32,29,28,25,32,27,34,28,0,32,32,27],
[29,24,19,29,29,24,25,30,19,19,0,17,15],
[31,29,31,29,30,27,29,36,30,19,34,0,24],
[31,37,25,24,27,30,30,34,23,24,36,27,0]])



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
result = np.append(np.array([13, 51, 117, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,24,27,27,23,25,26,31,21,26,30,25],
[28,0,28,26,23,28,25,28,26,21,17,30,22],
[27,23,0,18,22,21,23,22,23,21,15,27,16],
[24,25,33,0,21,28,26,24,25,27,27,29,25],
[24,28,29,30,0,23,22,24,31,24,24,30,22],
[28,23,30,23,28,0,24,26,24,27,27,27,25],
[26,26,28,25,29,27,0,27,34,22,23,32,27],
[25,23,29,27,27,25,24,0,32,25,21,32,23],
[20,25,28,26,20,27,17,19,0,17,22,28,22],
[30,30,30,24,27,24,29,26,34,0,24,32,26],
[25,34,36,24,27,24,28,30,29,27,0,34,24],
[21,21,24,22,21,24,19,19,23,19,17,0,18],
[26,29,35,26,29,26,24,28,29,25,27,33,0]])



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
result = np.append(np.array([13, 51, 118, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,25,26,29,24,24,30,27,26,22,27,28],
[26,0,32,30,29,27,25,35,29,31,27,20,27],
[26,19,0,24,24,25,17,22,21,23,14,17,24],
[25,21,27,0,29,28,19,32,29,22,22,23,32],
[22,22,27,22,0,24,20,32,27,26,24,17,26],
[27,24,26,23,27,0,21,27,21,26,19,18,25],
[27,26,34,32,31,30,0,28,28,28,26,23,29],
[21,16,29,19,19,24,23,0,19,27,20,18,26],
[24,22,30,22,24,30,23,32,0,28,22,20,27],
[25,20,28,29,25,25,23,24,23,0,19,20,30],
[29,24,37,29,27,32,25,31,29,32,0,27,28],
[24,31,34,28,34,33,28,33,31,31,24,0,33],
[23,24,27,19,25,26,22,25,24,21,23,18,0]])



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
result = np.append(np.array([13, 51, 119, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,17,24,25,20,17,20,19,27,21,17,25],
[23,0,21,25,18,23,19,17,24,18,22,19,24],
[34,30,0,33,29,27,18,31,27,26,27,26,22],
[27,26,18,0,21,15,17,20,21,17,17,17,22],
[26,33,22,30,0,26,27,26,27,27,28,23,23],
[31,28,24,36,25,0,24,28,22,28,30,28,25],
[34,32,33,34,24,27,0,25,26,25,26,28,24],
[31,34,20,31,25,23,26,0,23,26,24,29,30],
[32,27,24,30,24,29,25,28,0,32,29,29,29],
[24,33,25,34,24,23,26,25,19,0,22,22,24],
[30,29,24,34,23,21,25,27,22,29,0,24,31],
[34,32,25,34,28,23,23,22,22,29,27,0,28],
[26,27,29,29,28,26,27,21,22,27,20,23,0]])



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
result = np.append(np.array([13, 51, 120, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,16,23,22,24,20,25,23,23,25,21,23],
[21,0,20,22,22,27,23,20,25,20,31,22,24],
[35,31,0,25,26,30,26,29,30,29,34,25,27],
[28,29,26,0,26,33,25,30,31,29,29,26,29],
[29,29,25,25,0,30,27,21,25,22,33,25,27],
[27,24,21,18,21,0,21,21,24,20,25,23,21],
[31,28,25,26,24,30,0,26,31,24,29,25,22],
[26,31,22,21,30,30,25,0,22,20,31,24,23],
[28,26,21,20,26,27,20,29,0,27,29,21,24],
[28,31,22,22,29,31,27,31,24,0,34,30,30],
[26,20,17,22,18,26,22,20,22,17,0,16,21],
[30,29,26,25,26,28,26,27,30,21,35,0,29],
[28,27,24,22,24,30,29,28,27,21,30,22,0]])



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
result = np.append(np.array([13, 51, 121, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,24,28,25,19,18,22,22,15,23,20,21],
[24,0,22,18,27,24,21,21,21,24,27,21,27],
[27,29,0,19,27,25,27,31,27,21,29,20,26],
[23,33,32,0,26,26,27,25,26,24,27,25,28],
[26,24,24,25,0,20,17,25,27,20,25,21,27],
[32,27,26,25,31,0,24,31,29,26,28,28,35],
[33,30,24,24,34,27,0,35,29,26,31,22,31],
[29,30,20,26,26,20,16,0,27,17,26,16,26],
[29,30,24,25,24,22,22,24,0,21,28,18,30],
[36,27,30,27,31,25,25,34,30,0,30,22,31],
[28,24,22,24,26,23,20,25,23,21,0,19,19],
[31,30,31,26,30,23,29,35,33,29,32,0,30],
[30,24,25,23,24,16,20,25,21,20,32,21,0]])



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
result = np.append(np.array([13, 51, 122, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,27,31,30,25,33,23,27,22,29,32,25],
[27,0,24,21,24,28,32,22,25,26,33,26,28],
[24,27,0,38,25,24,29,29,29,21,20,27,27],
[20,30,13,0,23,17,26,21,22,18,19,20,19],
[21,27,26,28,0,24,22,26,28,22,25,29,34],
[26,23,27,34,27,0,32,25,34,23,26,28,28],
[18,19,22,25,29,19,0,25,24,25,24,26,26],
[28,29,22,30,25,26,26,0,30,22,29,27,32],
[24,26,22,29,23,17,27,21,0,18,24,25,27],
[29,25,30,33,29,28,26,29,33,0,27,29,25],
[22,18,31,32,26,25,27,22,27,24,0,29,25],
[19,25,24,31,22,23,25,24,26,22,22,0,28],
[26,23,24,32,17,23,25,19,24,26,26,23,0]])



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
result = np.append(np.array([13, 51, 123, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,28,32,34,31,25,27,22,32,31,25,27],
[21,0,25,27,26,26,28,25,22,35,32,27,28],
[23,26,0,29,34,28,25,26,26,29,28,26,27],
[19,24,22,0,31,27,29,34,26,23,28,32,23],
[17,25,17,20,0,27,27,22,17,25,22,24,24],
[20,25,23,24,24,0,25,27,22,27,28,26,24],
[26,23,26,22,24,26,0,31,25,28,27,30,28],
[24,26,25,17,29,24,20,0,22,27,27,21,25],
[29,29,25,25,34,29,26,29,0,28,27,24,30],
[19,16,22,28,26,24,23,24,23,0,27,22,26],
[20,19,23,23,29,23,24,24,24,24,0,22,25],
[26,24,25,19,27,25,21,30,27,29,29,0,21],
[24,23,24,28,27,27,23,26,21,25,26,30,0]])



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
result = np.append(np.array([13, 51, 124, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,12,12,21,20,16,25,10,10,26,11,14],
[35,0,15,21,32,26,36,39,31,36,32,16,28],
[39,36,0,27,39,39,33,30,30,36,31,28,22],
[39,30,24,0,39,47,31,27,28,28,28,31,42],
[30,19,12,12,0,23,23,13,12,19,26,4,4],
[31,25,12,4,28,0,20,20,19,19,26,25,17],
[35,15,18,20,28,31,0,23,12,24,28,15,18],
[26,12,21,24,38,31,28,0,19,21,28,15,19],
[41,20,21,23,39,32,39,32,0,23,28,20,24],
[41,15,15,23,32,32,27,30,28,0,33,21,24],
[25,19,20,23,25,25,23,23,23,18,0,14,18],
[40,35,23,20,47,26,36,36,31,30,37,0,34],
[37,23,29,9,47,34,33,32,27,27,33,17,0]])



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
result = np.append(np.array([13, 51, 125, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,46,25,28,22,30,36,30,42,31,32,39],
[20,0,34,29,33,29,24,30,21,44,30,23,32],
[5,17,0,16,10,12,11,7,12,24,13,23,14],
[26,22,35,0,20,25,29,32,22,45,22,25,28],
[23,18,41,31,0,24,20,31,20,40,30,24,31],
[29,22,39,26,27,0,23,31,25,44,38,25,44],
[21,27,40,22,31,28,0,24,19,38,35,35,23],
[15,21,44,19,20,20,27,0,24,39,25,30,32],
[21,30,39,29,31,26,32,27,0,48,42,40,40],
[9,7,27,6,11,7,13,12,3,0,13,16,16],
[20,21,38,29,21,13,16,26,9,38,0,17,27],
[19,28,28,26,27,26,16,21,11,35,34,0,29],
[12,19,37,23,20,7,28,19,11,35,24,22,0]])



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
result = np.append(np.array([13, 51, 126, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,40,26,28,28,33,18,24,29,23,26,37],
[25,0,38,38,43,30,37,29,30,30,26,29,39],
[11,13,0,19,23,18,25,13,20,25,17,10,25],
[25,13,32,0,26,24,26,30,21,18,18,21,30],
[23,8,28,25,0,21,25,20,32,20,15,18,29],
[23,21,33,27,30,0,29,23,19,31,19,24,36],
[18,14,26,25,26,22,0,20,19,29,23,16,31],
[33,22,38,21,31,28,31,0,30,28,23,31,33],
[27,21,31,30,19,32,32,21,0,30,16,29,33],
[22,21,26,33,31,20,22,23,21,0,20,23,33],
[28,25,34,33,36,32,28,28,35,31,0,24,40],
[25,22,41,30,33,27,35,20,22,28,27,0,43],
[14,12,26,21,22,15,20,18,18,18,11,8,0]])



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
result = np.append(np.array([13, 51, 127, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,30,31,28,36,25,29,32,25,28,30,32],
[22,0,23,26,27,27,27,26,34,22,24,20,28],
[21,28,0,31,24,24,21,21,26,21,26,26,31],
[20,25,20,0,28,26,25,19,27,21,22,21,28],
[23,24,27,23,0,23,19,20,24,17,21,19,29],
[15,24,27,25,28,0,21,22,26,13,21,18,31],
[26,24,30,26,32,30,0,27,36,26,28,23,32],
[22,25,30,32,31,29,24,0,29,23,25,24,33],
[19,17,25,24,27,25,15,22,0,20,21,22,26],
[26,29,30,30,34,38,25,28,31,0,25,28,36],
[23,27,25,29,30,30,23,26,30,26,0,28,32],
[21,31,25,30,32,33,28,27,29,23,23,0,32],
[19,23,20,23,22,20,19,18,25,15,19,19,0]])



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
result = np.append(np.array([13, 51, 128, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,24,33,27,27,27,27,32,24,28,29,27],
[22,0,29,24,24,20,31,28,27,26,27,26,21],
[27,22,0,24,25,21,27,26,32,25,33,25,26],
[18,27,27,0,23,26,25,29,24,27,26,26,23],
[24,27,26,28,0,21,25,24,28,23,24,24,28],
[24,31,30,25,30,0,30,27,27,30,31,30,26],
[24,20,24,26,26,21,0,24,24,28,22,23,28],
[24,23,25,22,27,24,27,0,26,27,25,19,22],
[19,24,19,27,23,24,27,25,0,22,30,18,22],
[27,25,26,24,28,21,23,24,29,0,24,21,23],
[23,24,18,25,27,20,29,26,21,27,0,22,23],
[22,25,26,25,27,21,28,32,33,30,29,0,18],
[24,30,25,28,23,25,23,29,29,28,28,33,0]])



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
result = np.append(np.array([13, 51, 129, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,31,22,22,26,27,29,23,31,32,28,29],
[18,0,25,17,17,19,19,23,20,25,25,26,32],
[20,26,0,22,25,27,30,28,28,27,25,31,27],
[29,34,29,0,25,29,24,33,28,34,28,30,35],
[29,34,26,26,0,23,26,29,25,31,27,25,33],
[25,32,24,22,28,0,30,31,27,33,30,32,30],
[24,32,21,27,25,21,0,29,26,30,24,26,33],
[22,28,23,18,22,20,22,0,24,24,25,22,24],
[28,31,23,23,26,24,25,27,0,25,27,27,29],
[20,26,24,17,20,18,21,27,26,0,20,22,28],
[19,26,26,23,24,21,27,26,24,31,0,34,21],
[23,25,20,21,26,19,25,29,24,29,17,0,31],
[22,19,24,16,18,21,18,27,22,23,30,20,0]])



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
result = np.append(np.array([13, 51, 130, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,32,26,24,24,25,21,32,31,28,30,27],
[32,0,34,31,33,30,26,31,36,32,23,33,29],
[19,17,0,21,21,22,19,21,21,21,17,16,23],
[25,20,30,0,26,25,25,24,28,26,25,26,21],
[27,18,30,25,0,23,24,17,29,25,18,22,21],
[27,21,29,26,28,0,32,32,32,31,24,28,28],
[26,25,32,26,27,19,0,29,36,27,29,23,25],
[30,20,30,27,34,19,22,0,28,28,26,30,27],
[19,15,30,23,22,19,15,23,0,21,22,28,19],
[20,19,30,25,26,20,24,23,30,0,18,21,18],
[23,28,34,26,33,27,22,25,29,33,0,31,31],
[21,18,35,25,29,23,28,21,23,30,20,0,24],
[24,22,28,30,30,23,26,24,32,33,20,27,0]])



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
result = np.append(np.array([13, 51, 131, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,20,30,25,29,32,36,33,28,28,35,32],
[24,0,24,26,22,27,17,23,24,24,21,29,28],
[31,27,0,32,32,33,33,29,34,30,24,41,30],
[21,25,19,0,26,21,24,28,24,28,18,29,22],
[26,29,19,25,0,23,31,32,36,28,31,32,21],
[22,24,18,30,28,0,28,22,20,29,20,31,32],
[19,34,18,27,20,23,0,24,26,26,20,37,26],
[15,28,22,23,19,29,27,0,22,18,20,20,29],
[18,27,17,27,15,31,25,29,0,26,22,31,26],
[23,27,21,23,23,22,25,33,25,0,16,26,25],
[23,30,27,33,20,31,31,31,29,35,0,31,32],
[16,22,10,22,19,20,14,31,20,25,20,0,22],
[19,23,21,29,30,19,25,22,25,26,19,29,0]])



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
result = np.append(np.array([13, 51, 132, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,22,23,28,25,21,21,20,27,33,19,23],
[29,0,26,18,34,26,31,32,31,30,26,25,35],
[29,25,0,14,33,24,31,28,21,22,24,22,16],
[28,33,37,0,36,31,35,34,25,30,27,28,24],
[23,17,18,15,0,22,15,29,16,21,25,27,19],
[26,25,27,20,29,0,26,30,21,28,18,16,28],
[30,20,20,16,36,25,0,28,22,23,26,18,15],
[30,19,23,17,22,21,23,0,25,27,24,19,15],
[31,20,30,26,35,30,29,26,0,25,32,34,26],
[24,21,29,21,30,23,28,24,26,0,26,26,37],
[18,25,27,24,26,33,25,27,19,25,0,24,28],
[32,26,29,23,24,35,33,32,17,25,27,0,24],
[28,16,35,27,32,23,36,36,25,14,23,27,0]])



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
result = np.append(np.array([13, 51, 133, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,36,26,27,35,29,34,17,29,28,32,37],
[27,0,28,19,23,18,27,26,18,20,15,30,28],
[15,23,0,19,25,24,23,22,19,18,26,23,26],
[25,32,32,0,32,29,26,27,27,20,26,38,29],
[24,28,26,19,0,29,30,29,24,27,24,38,31],
[16,33,27,22,22,0,25,24,18,17,18,28,25],
[22,24,28,25,21,26,0,20,19,17,17,26,26],
[17,25,29,24,22,27,31,0,18,18,30,31,35],
[34,33,32,24,27,33,32,33,0,33,32,37,32],
[22,31,33,31,24,34,34,33,18,0,26,32,33],
[23,36,25,25,27,33,34,21,19,25,0,37,27],
[19,21,28,13,13,23,25,20,14,19,14,0,31],
[14,23,25,22,20,26,25,16,19,18,24,20,0]])



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
result = np.append(np.array([13, 51, 134, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,17,25,19,21,15,28,23,25,22,19,28],
[21,0,14,25,14,20,20,24,16,27,16,11,22],
[34,37,0,27,29,26,20,39,23,31,31,25,36],
[26,26,24,0,11,22,17,27,21,26,22,20,29],
[32,37,22,40,0,35,26,34,26,32,24,33,37],
[30,31,25,29,16,0,16,32,24,35,32,19,28],
[36,31,31,34,25,35,0,31,25,33,31,25,27],
[23,27,12,24,17,19,20,0,25,27,21,15,18],
[28,35,28,30,25,27,26,26,0,32,28,24,27],
[26,24,20,25,19,16,18,24,19,0,16,17,24],
[29,35,20,29,27,19,20,30,23,35,0,18,33],
[32,40,26,31,18,32,26,36,27,34,33,0,29],
[23,29,15,22,14,23,24,33,24,27,18,22,0]])



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
result = np.append(np.array([13, 51, 135, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,7,31,16,25,25,31,25,16,13,23,5],
[35,0,38,42,27,39,51,38,29,38,23,40,32],
[44,13,0,34,25,29,28,36,25,29,18,41,9],
[20,9,17,0,19,11,18,19,16,21,9,34,10],
[35,24,26,32,0,28,41,36,38,27,22,21,35],
[26,12,22,40,23,0,18,38,14,25,18,36,14],
[26,0,23,33,10,33,0,32,23,27,16,31,10],
[20,13,15,32,15,13,19,0,13,21,11,17,15],
[26,22,26,35,13,37,28,38,0,27,29,30,20],
[35,13,22,30,24,26,24,30,24,0,11,33,15],
[38,28,33,42,29,33,35,40,22,40,0,40,18],
[28,11,10,17,30,15,20,34,21,18,11,0,18],
[46,19,42,41,16,37,41,36,31,36,33,33,0]])



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
result = np.append(np.array([13, 51, 136, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,25,43,29,29,42,27,44,19,41,33,38],
[7,0,14,28,21,21,26,26,36,26,25,25,9],
[26,37,0,30,29,38,31,36,38,21,28,27,28],
[8,23,21,0,20,19,15,27,17,15,17,0,17],
[22,30,22,31,0,32,39,33,30,22,39,31,32],
[22,30,13,32,19,0,22,42,30,16,22,22,18],
[9,25,20,36,12,29,0,34,39,28,33,33,18],
[24,25,15,24,18,9,17,0,32,25,24,24,11],
[7,15,13,34,21,21,12,19,0,19,18,25,2],
[32,25,30,36,29,35,23,26,32,0,41,33,25],
[10,26,23,34,12,29,18,27,33,10,0,22,22],
[18,26,24,51,20,29,18,27,26,18,29,0,20],
[13,42,23,34,19,33,33,40,49,26,29,31,0]])



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
result = np.append(np.array([13, 51, 137, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,31,29,27,19,30,22,21,31,9,18,15],
[24,0,28,36,19,22,22,33,22,22,12,28,19],
[20,23,0,20,26,22,21,18,22,22,15,15,27],
[22,15,31,0,22,16,25,15,13,25,13,22,7],
[24,32,25,29,0,24,25,21,31,31,24,24,19],
[32,29,29,35,27,0,21,25,26,33,23,41,12],
[21,29,30,26,26,30,0,30,12,24,5,30,17],
[29,18,33,36,30,26,21,0,22,22,15,24,22],
[30,29,29,38,20,25,39,29,0,45,21,30,21],
[20,29,29,26,20,18,27,29,6,0,6,24,5],
[42,39,36,38,27,28,46,36,30,45,0,40,24],
[33,23,36,29,27,10,21,27,21,27,11,0,12],
[36,32,24,44,32,39,34,29,30,46,27,39,0]])



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
result = np.append(np.array([13, 51, 138, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,26,25,17,22,26,21,17,17,23,16,15],
[27,0,25,18,19,25,26,23,28,18,26,19,17],
[25,26,0,23,18,25,23,23,19,19,24,13,14],
[26,33,28,0,22,23,25,22,24,21,28,21,27],
[34,32,33,29,0,32,33,31,25,25,23,23,29],
[29,26,26,28,19,0,25,24,24,22,24,25,21],
[25,25,28,26,18,26,0,28,22,16,24,19,18],
[30,28,28,29,20,27,23,0,20,21,26,22,26],
[34,23,32,27,26,27,29,31,0,25,25,23,25],
[34,33,32,30,26,29,35,30,26,0,23,27,20],
[28,25,27,23,28,27,27,25,26,28,0,22,26],
[35,32,38,30,28,26,32,29,28,24,29,0,29],
[36,34,37,24,22,30,33,25,26,31,25,22,0]])



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
result = np.append(np.array([13, 51, 139, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,24,23,21,23,21,21,18,16,16,17,25],
[41,0,39,31,28,30,24,23,26,21,19,29,32],
[27,12,0,19,15,18,22,22,17,22,14,22,22],
[28,20,32,0,33,29,32,28,30,25,24,31,34],
[30,23,36,18,0,28,33,29,31,23,21,31,40],
[28,21,33,22,23,0,25,28,25,28,23,27,34],
[30,27,29,19,18,26,0,25,27,24,24,30,33],
[30,28,29,23,22,23,26,0,23,27,16,30,27],
[33,25,34,21,20,26,24,28,0,28,18,30,28],
[35,30,29,26,28,23,27,24,23,0,26,24,33],
[35,32,37,27,30,28,27,35,33,25,0,30,36],
[34,22,29,20,20,24,21,21,21,27,21,0,29],
[26,19,29,17,11,17,18,24,23,18,15,22,0]])



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
result = np.append(np.array([13, 51, 140, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,31,20,31,24,30,29,22,22,29,24,31],
[26,0,22,26,23,17,32,15,14,19,24,26,31],
[20,29,0,22,28,25,26,26,18,22,25,23,33],
[31,25,29,0,31,28,32,25,30,25,26,27,31],
[20,28,23,20,0,26,28,20,23,25,24,26,28],
[27,34,26,23,25,0,33,25,24,23,27,26,29],
[21,19,25,19,23,18,0,23,21,27,27,28,25],
[22,36,25,26,31,26,28,0,22,26,31,26,34],
[29,37,33,21,28,27,30,29,0,26,27,24,34],
[29,32,29,26,26,28,24,25,25,0,24,31,28],
[22,27,26,25,27,24,24,20,24,27,0,26,27],
[27,25,28,24,25,25,23,25,27,20,25,0,29],
[20,20,18,20,23,22,26,17,17,23,24,22,0]])



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
result = np.append(np.array([13, 51, 141, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,23,31,13,25,25,22,21,17,15,18,27],
[22,0,24,29,22,28,18,26,27,21,20,19,30],
[28,27,0,32,26,26,23,30,30,29,28,24,34],
[20,22,19,0,13,28,17,27,31,15,23,22,28],
[38,29,25,38,0,38,35,42,42,42,31,33,42],
[26,23,25,23,13,0,19,17,19,13,15,13,23],
[26,33,28,34,16,32,0,22,29,23,21,24,24],
[29,25,21,24,9,34,29,0,21,16,21,13,21],
[30,24,21,20,9,32,22,30,0,25,23,10,28],
[34,30,22,36,9,38,28,35,26,0,29,24,31],
[36,31,23,28,20,36,30,30,28,22,0,27,31],
[33,32,27,29,18,38,27,38,41,27,24,0,39],
[24,21,17,23,9,28,27,30,23,20,20,12,0]])



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
result = np.append(np.array([13, 51, 142, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,23,31,22,28,21,27,28,24,27,22,22],
[30,0,27,31,22,25,24,27,25,20,29,22,22],
[28,24,0,33,26,26,28,27,34,30,32,26,30],
[20,20,18,0,18,25,20,23,23,24,18,16,20],
[29,29,25,33,0,29,24,25,28,24,30,23,23],
[23,26,25,26,22,0,20,28,27,25,26,22,24],
[30,27,23,31,27,31,0,32,29,27,29,21,30],
[24,24,24,28,26,23,19,0,25,25,25,23,30],
[23,26,17,28,23,24,22,26,0,20,24,18,20],
[27,31,21,27,27,26,24,26,31,0,29,23,23],
[24,22,19,33,21,25,22,26,27,22,0,20,21],
[29,29,25,35,28,29,30,28,33,28,31,0,28],
[29,29,21,31,28,27,21,21,31,28,30,23,0]])



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
result = np.append(np.array([13, 51, 143, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,31,31,38,38,13,15,15,22,44,38,15],
[20,0,15,7,7,22,0,9,20,7,28,9,7],
[20,36,0,20,23,51,13,9,20,20,28,22,20],
[20,44,31,0,38,51,13,15,22,35,28,38,35],
[13,44,28,13,0,35,26,28,26,33,28,22,28],
[13,29,0,0,16,0,0,0,0,0,26,0,13],
[38,51,38,38,25,51,0,9,38,38,51,38,22],
[36,42,42,36,23,51,42,0,49,49,42,36,49],
[36,31,31,29,25,51,13,2,0,20,44,38,22],
[29,44,31,16,18,51,13,2,31,0,44,31,15],
[7,23,23,23,23,25,0,9,7,7,0,25,7],
[13,42,29,13,29,51,13,15,13,20,26,0,26],
[36,44,31,16,23,38,29,2,29,36,44,25,0]])



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
result = np.append(np.array([13, 51, 144, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,32,15,28,25,23,27,25,24,44,38,20],
[22,0,35,29,21,27,29,23,28,25,38,34,19],
[19,16,0,24,22,8,6,16,25,23,21,32,1],
[36,22,27,0,27,22,17,26,42,26,34,48,7],
[23,30,29,24,0,22,26,23,39,28,42,38,14],
[26,24,43,29,29,0,28,21,29,28,37,32,19],
[28,22,45,34,25,23,0,20,28,34,37,32,10],
[24,28,35,25,28,30,31,0,30,26,39,35,28],
[26,23,26,9,12,22,23,21,0,20,33,32,12],
[27,26,28,25,23,23,17,25,31,0,31,34,17],
[7,13,30,17,9,14,14,12,18,20,0,19,3],
[13,17,19,3,13,19,19,16,19,17,32,0,3],
[31,32,50,44,37,32,41,23,39,34,48,48,0]])



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
result = np.append(np.array([13, 51, 145, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,28,32,27,23,24,23,27,27,22,21,20],
[19,0,29,25,23,23,25,22,22,23,28,26,24],
[23,22,0,22,23,18,16,18,22,23,20,19,18],
[19,26,29,0,25,25,24,27,25,26,21,20,22],
[24,28,28,26,0,25,25,28,25,30,26,23,20],
[28,28,33,26,26,0,29,27,29,31,25,26,28],
[27,26,35,27,26,22,0,29,26,26,28,23,24],
[28,29,33,24,23,24,22,0,25,24,28,23,24],
[24,29,29,26,26,22,25,26,0,26,25,23,23],
[24,28,28,25,21,20,25,27,25,0,29,19,21],
[29,23,31,30,25,26,23,23,26,22,0,23,28],
[30,25,32,31,28,25,28,28,28,32,28,0,26],
[31,27,33,29,31,23,27,27,28,30,23,25,0]])



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
result = np.append(np.array([13, 51, 146, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,19,17,30,30,23,24,23,21,20,29,16],
[22,0,27,19,32,36,25,20,21,24,27,24,24],
[32,24,0,24,29,30,25,24,28,24,28,27,31],
[34,32,27,0,27,31,31,26,31,29,29,33,25],
[21,19,22,24,0,21,18,26,25,24,22,22,14],
[21,15,21,20,30,0,22,22,23,25,24,23,20],
[28,26,26,20,33,29,0,28,25,30,23,27,24],
[27,31,27,25,25,29,23,0,26,28,23,24,21],
[28,30,23,20,26,28,26,25,0,25,19,24,20],
[30,27,27,22,27,26,21,23,26,0,28,25,22],
[31,24,23,22,29,27,28,28,32,23,0,32,20],
[22,27,24,18,29,28,24,27,27,26,19,0,21],
[35,27,20,26,37,31,27,30,31,29,31,30,0]])



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
result = np.append(np.array([13, 51, 147, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,29,25,21,34,28,26,26,32,27,27,29],
[27,0,26,24,23,34,35,25,28,32,24,25,27],
[22,25,0,25,14,25,33,22,28,31,23,28,26],
[26,27,26,0,17,27,30,19,31,34,28,34,32],
[30,28,37,34,0,36,36,22,30,36,26,31,36],
[17,17,26,24,15,0,32,22,19,27,26,20,23],
[23,16,18,21,15,19,0,17,22,26,19,20,19],
[25,26,29,32,29,29,34,0,34,33,26,35,33],
[25,23,23,20,21,32,29,17,0,26,20,30,23],
[19,19,20,17,15,24,25,18,25,0,21,18,22],
[24,27,28,23,25,25,32,25,31,30,0,27,27],
[24,26,23,17,20,31,31,16,21,33,24,0,24],
[22,24,25,19,15,28,32,18,28,29,24,27,0]])



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
result = np.append(np.array([13, 51, 148, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,51,40,33,30,34,33,33,33,33,44,44],
[28,0,38,38,36,26,38,27,47,38,21,47,31],
[0,13,0,10,19,9,25,4,13,13,14,19,35],
[11,13,41,0,23,9,34,4,23,23,4,30,34],
[18,15,32,28,0,18,32,22,34,15,14,37,25],
[21,25,42,42,33,0,25,24,44,35,14,44,35],
[17,13,26,17,19,26,0,17,19,19,14,36,40],
[18,24,47,47,29,27,34,0,40,40,14,40,40],
[18,4,38,28,17,7,32,11,0,21,14,47,35],
[18,13,38,28,36,16,32,11,30,0,14,47,35],
[18,30,37,47,37,37,37,37,37,37,0,37,30],
[7,4,32,21,14,7,15,11,4,4,14,0,25],
[7,20,16,17,26,16,11,11,16,16,21,26,0]])



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
result = np.append(np.array([13, 51, 149, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,33,27,30,27,23,25,29,26,26,23,24],
[20,0,23,22,20,20,21,21,30,23,24,27,22],
[18,28,0,16,26,23,27,21,26,23,23,21,27],
[24,29,35,0,27,27,27,21,23,31,24,25,25],
[21,31,25,24,0,21,21,19,22,20,31,22,22],
[24,31,28,24,30,0,26,27,26,23,30,28,24],
[28,30,24,24,30,25,0,23,24,23,33,17,28],
[26,30,30,30,32,24,28,0,29,30,30,33,32],
[22,21,25,28,29,25,27,22,0,22,34,23,29],
[25,28,28,20,31,28,28,21,29,0,31,23,25],
[25,27,28,27,20,21,18,21,17,20,0,23,25],
[28,24,30,26,29,23,34,18,28,28,28,0,30],
[27,29,24,26,29,27,23,19,22,26,26,21,0]])



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
result = np.append(np.array([13, 51, 150, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,26,30,24,20,26,27,19,24,27,20,24],
[30,0,23,27,33,19,30,24,23,32,27,26,30],
[25,28,0,29,31,26,28,31,23,34,24,27,31],
[21,24,22,0,27,19,20,19,24,27,22,25,27],
[27,18,20,24,0,15,20,16,14,20,20,26,30],
[31,32,25,32,36,0,31,30,28,32,26,31,29],
[25,21,23,31,31,20,0,18,27,23,23,29,29],
[24,27,20,32,35,21,33,0,26,23,24,31,32],
[32,28,28,27,37,23,24,25,0,29,28,28,32],
[27,19,17,24,31,19,28,28,22,0,23,26,26],
[24,24,27,29,31,25,28,27,23,28,0,25,26],
[31,25,24,26,25,20,22,20,23,25,26,0,30],
[27,21,20,24,21,22,22,19,19,25,25,21,0]])



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
result = np.append(np.array([13, 51, 151, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,24,22,23,21,21,22,21,22,30,28,28],
[25,0,21,23,18,20,21,29,18,19,23,28,26],
[27,30,0,24,25,29,28,24,21,30,29,32,28],
[29,28,27,0,31,26,25,30,21,28,30,33,33],
[28,33,26,20,0,22,23,33,22,20,30,32,27],
[30,31,22,25,29,0,21,31,25,24,32,30,30],
[30,30,23,26,28,30,0,31,25,26,33,34,31],
[29,22,27,21,18,20,20,0,20,23,28,25,26],
[30,33,30,30,29,26,26,31,0,27,25,34,32],
[29,32,21,23,31,27,25,28,24,0,30,32,32],
[21,28,22,21,21,19,18,23,26,21,0,28,26],
[23,23,19,18,19,21,17,26,17,19,23,0,29],
[23,25,23,18,24,21,20,25,19,19,25,22,0]])



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
result = np.append(np.array([13, 51, 152, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,50,15,35,25,43,35,32,32,40,33,25],
[19,0,44,33,36,25,43,25,34,25,41,26,25],
[1,7,0,0,18,0,15,7,16,7,14,16,7],
[36,18,51,0,36,32,44,43,33,32,33,33,26],
[16,15,33,15,0,15,40,22,22,33,40,23,15],
[26,26,51,19,36,0,44,18,33,25,41,33,26],
[8,8,36,7,11,7,0,8,23,25,15,26,8],
[16,26,44,8,29,33,43,0,23,25,41,33,34],
[19,17,35,18,29,18,28,28,0,25,25,19,25],
[19,26,44,19,18,26,26,26,26,0,23,26,16],
[11,10,37,18,11,10,36,10,26,28,0,19,0],
[18,25,35,18,28,18,25,18,32,25,32,0,25],
[26,26,44,25,36,25,43,17,26,35,51,26,0]])



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
result = np.append(np.array([13, 51, 153, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,22,30,35,30,29,28,24,28,35,34,29],
[25,0,25,26,36,24,26,19,23,17,29,29,21],
[29,26,0,25,28,23,30,27,25,19,33,34,24],
[21,25,26,0,33,21,28,19,26,19,29,31,25],
[16,15,23,18,0,22,22,15,28,10,30,25,20],
[21,27,28,30,29,0,29,23,29,21,35,25,28],
[22,25,21,23,29,22,0,24,26,23,30,27,21],
[23,32,24,32,36,28,27,0,22,23,40,33,31],
[27,28,26,25,23,22,25,29,0,17,32,31,29],
[23,34,32,32,41,30,28,28,34,0,33,36,33],
[16,22,18,22,21,16,21,11,19,18,0,26,26],
[17,22,17,20,26,26,24,18,20,15,25,0,20],
[22,30,27,26,31,23,30,20,22,18,25,31,0]])



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
result = np.append(np.array([13, 51, 154, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,18,15,23,29,15,23,23,12,32,17,23],
[28,0,20,10,25,28,18,30,18,26,40,8,20],
[33,31,0,24,24,36,13,36,31,34,39,20,39],
[36,41,27,0,28,34,19,32,31,20,35,27,47],
[28,26,27,23,0,28,18,35,25,15,44,14,37],
[22,23,15,17,23,0,12,13,25,22,16,21,26],
[36,33,38,32,33,39,0,32,24,32,41,31,32],
[28,21,15,19,16,38,19,0,18,22,27,15,32],
[28,33,20,20,26,26,27,33,0,19,33,27,39],
[39,25,17,31,36,29,19,29,32,0,39,20,38],
[19,11,12,16,7,35,10,24,18,12,0,12,18],
[34,43,31,24,37,30,20,36,24,31,39,0,39],
[28,31,12,4,14,25,19,19,12,13,33,12,0]])



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
result = np.append(np.array([13, 51, 155, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,10,18,35,27,27,35,21,26,29,29,10],
[33,0,16,35,41,33,17,43,38,33,33,41,43],
[41,35,0,35,51,43,17,40,38,41,51,51,51],
[33,16,16,0,41,33,22,33,21,16,16,16,16],
[16,10,0,10,0,21,0,15,21,16,21,11,10],
[24,18,8,18,30,0,17,23,21,24,34,24,23],
[24,34,34,29,51,34,0,34,29,34,34,34,34],
[16,8,11,18,36,28,17,0,21,16,19,19,21],
[30,13,13,30,30,30,22,30,0,24,24,24,13],
[25,18,10,35,35,27,17,35,27,0,46,29,27],
[22,18,0,35,30,17,17,32,27,5,0,19,10],
[22,10,0,35,40,27,17,32,27,22,32,0,32],
[41,8,0,35,41,28,17,30,38,24,41,19,0]])



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
result = np.append(np.array([13, 51, 156, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,19,25,26,27,29,30,28,25,30,27,32],
[24,0,18,23,22,28,26,24,24,24,26,22,24],
[32,33,0,25,30,33,27,29,29,27,31,31,34],
[26,28,26,0,25,32,29,31,30,28,32,30,29],
[25,29,21,26,0,25,28,27,27,22,26,29,29],
[24,23,18,19,26,0,23,28,25,24,31,25,28],
[22,25,24,22,23,28,0,26,27,24,28,23,28],
[21,27,22,20,24,23,25,0,23,28,29,29,27],
[23,27,22,21,24,26,24,28,0,23,23,27,28],
[26,27,24,23,29,27,27,23,28,0,31,28,30],
[21,25,20,19,25,20,23,22,28,20,0,19,26],
[24,29,20,21,22,26,28,22,24,23,32,0,27],
[19,27,17,22,22,23,23,24,23,21,25,24,0]])



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
result = np.append(np.array([13, 51, 157, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,27,26,23,25,27,28,24,26,23,24,26],
[26,0,25,29,22,23,28,28,27,24,24,23,28],
[24,26,0,29,22,26,31,26,29,28,23,26,26],
[25,22,22,0,22,24,24,24,25,23,22,24,24],
[28,29,29,29,0,29,34,24,30,31,29,28,30],
[26,28,25,27,22,0,25,25,27,25,21,22,32],
[24,23,20,27,17,26,0,24,23,23,22,23,24],
[23,23,25,27,27,26,27,0,29,28,26,22,27],
[27,24,22,26,21,24,28,22,0,24,21,22,28],
[25,27,23,28,20,26,28,23,27,0,22,25,28],
[28,27,28,29,22,30,29,25,30,29,0,25,29],
[27,28,25,27,23,29,28,29,29,26,26,0,28],
[25,23,25,27,21,19,27,24,23,23,22,23,0]])



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
result = np.append(np.array([13, 51, 158, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,25,18,19,24,23,27,30,29,24,21,24],
[28,0,25,24,24,27,24,29,29,27,30,19,23],
[26,26,0,23,16,28,24,29,27,33,22,24,23],
[33,27,28,0,27,23,25,31,28,33,30,25,30],
[32,27,35,24,0,31,29,34,33,36,31,30,28],
[27,24,23,28,20,0,27,35,24,34,23,24,28],
[28,27,27,26,22,24,0,32,28,34,28,22,34],
[24,22,22,20,17,16,19,0,23,29,21,19,18],
[21,22,24,23,18,27,23,28,0,28,23,20,25],
[22,24,18,18,15,17,17,22,23,0,22,18,20],
[27,21,29,21,20,28,23,30,28,29,0,23,22],
[30,32,27,26,21,27,29,32,31,33,28,0,29],
[27,28,28,21,23,23,17,33,26,31,29,22,0]])



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
result = np.append(np.array([13, 51, 159, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,19,20,24,22,6,4,14,18,6,8,14],
[32,0,22,25,17,20,9,13,22,17,16,9,15],
[32,29,0,40,16,18,20,19,21,28,21,10,26],
[31,26,11,0,21,16,14,9,19,19,9,11,9],
[27,34,35,30,0,25,15,19,26,18,16,17,26],
[29,31,33,35,26,0,22,23,39,29,22,20,40],
[45,42,31,37,36,29,0,22,41,30,24,30,28],
[47,38,32,42,32,28,29,0,37,25,29,32,33],
[37,29,30,32,25,12,10,14,0,8,16,17,16],
[33,34,23,32,33,22,21,26,43,0,15,27,29],
[45,35,30,42,35,29,27,22,35,36,0,24,35],
[43,42,41,40,34,31,21,19,34,24,27,0,27],
[37,36,25,42,25,11,23,18,35,22,16,24,0]])



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
result = np.append(np.array([13, 51, 160, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,38,16,23,23,16,19,28,16,17,17,16],
[32,0,32,20,26,25,32,13,22,32,26,11,32],
[13,19,0,16,23,16,12,19,29,16,19,16,16],
[35,31,35,0,30,35,18,19,35,45,35,36,30],
[28,25,28,21,0,23,12,13,28,21,22,13,12],
[28,26,35,16,28,0,28,26,29,28,29,13,28],
[35,19,39,33,39,23,0,20,35,33,27,24,33],
[32,38,32,32,38,25,31,0,29,32,32,32,32],
[23,29,22,16,23,22,16,22,0,22,16,16,22],
[35,19,35,6,30,23,18,19,29,0,26,20,24],
[34,25,32,16,29,22,24,19,35,25,0,22,16],
[34,40,35,15,38,38,27,19,35,31,29,0,32],
[35,19,35,21,39,23,18,19,29,27,35,19,0]])



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
result = np.append(np.array([13, 51, 161, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,25,24,29,35,28,22,14,30,24,22,22],
[29,0,36,23,27,35,29,16,13,30,27,22,27],
[26,15,0,18,24,35,18,19,2,19,27,23,19],
[27,28,33,0,30,37,26,26,18,26,35,28,27],
[22,24,27,21,0,31,24,20,8,18,31,20,29],
[16,16,16,14,20,0,12,12,8,22,20,17,21],
[23,22,33,25,27,39,0,21,17,14,32,27,27],
[29,35,32,25,31,39,30,0,30,29,30,22,31],
[37,38,49,33,43,43,34,21,0,37,39,40,43],
[21,21,32,25,33,29,37,22,14,0,31,18,25],
[27,24,24,16,20,31,19,21,12,20,0,13,25],
[29,29,28,23,31,34,24,29,11,33,38,0,29],
[29,24,32,24,22,30,24,20,8,26,26,22,0]])



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
result = np.append(np.array([13, 51, 162, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,23,24,23,32,27,27,22,29,31,32,24],
[20,0,19,21,19,20,19,23,20,18,24,21,21],
[28,32,0,21,22,32,25,26,22,28,23,31,27],
[27,30,30,0,24,28,24,28,22,30,29,33,24],
[28,32,29,27,0,28,19,30,22,32,28,31,22],
[19,31,19,23,23,0,22,21,17,30,23,31,21],
[24,32,26,27,32,29,0,26,28,32,29,30,22],
[24,28,25,23,21,30,25,0,19,27,25,32,23],
[29,31,29,29,29,34,23,32,0,31,31,32,28],
[22,33,23,21,19,21,19,24,20,0,27,32,17],
[20,27,28,22,23,28,22,26,20,24,0,30,22],
[19,30,20,18,20,20,21,19,19,19,21,0,17],
[27,30,24,27,29,30,29,28,23,34,29,34,0]])



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
result = np.append(np.array([13, 51, 163, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,23,36,28,24,21,25,18,25,21,32,25],
[25,0,23,37,34,21,20,29,26,26,27,27,29],
[28,28,0,38,38,20,23,30,22,28,21,27,27],
[15,14,13,0,19,16,17,18,16,17,19,22,19],
[23,17,13,32,0,20,18,32,18,19,19,24,20],
[27,30,31,35,31,0,28,27,25,29,23,26,30],
[30,31,28,34,33,23,0,31,27,28,29,30,34],
[26,22,21,33,19,24,20,0,21,21,17,20,25],
[33,25,29,35,33,26,24,30,0,25,26,29,32],
[26,25,23,34,32,22,23,30,26,0,24,22,29],
[30,24,30,32,32,28,22,34,25,27,0,30,30],
[19,24,24,29,27,25,21,31,22,29,21,0,25],
[26,22,24,32,31,21,17,26,19,22,21,26,0]])



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
result = np.append(np.array([13, 51, 164, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,21,28,20,23,14,19,20,24,22,21,25],
[31,0,19,31,22,28,19,20,23,26,23,21,27],
[30,32,0,31,19,31,24,21,31,24,30,25,31],
[23,20,20,0,17,25,19,14,26,18,15,21,23],
[31,29,32,34,0,33,26,25,29,30,31,29,32],
[28,23,20,26,18,0,15,16,21,22,26,21,22],
[37,32,27,32,25,36,0,29,33,34,32,28,32],
[32,31,30,37,26,35,22,0,30,31,28,29,33],
[31,28,20,25,22,30,18,21,0,25,27,26,27],
[27,25,27,33,21,29,17,20,26,0,25,29,29],
[29,28,21,36,20,25,19,23,24,26,0,24,27],
[30,30,26,30,22,30,23,22,25,22,27,0,24],
[26,24,20,28,19,29,19,18,24,22,24,27,0]])



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
result = np.append(np.array([13, 51, 165, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,17,23,28,24,27,17,23,24,25,20,28],
[30,0,21,25,25,29,27,21,23,22,26,24,29],
[34,30,0,22,33,25,35,28,26,27,29,27,25],
[28,26,29,0,31,27,33,24,29,30,33,27,26],
[23,26,18,20,0,27,27,20,23,26,25,23,24],
[27,22,26,24,24,0,31,21,24,27,27,24,23],
[24,24,16,18,24,20,0,22,19,24,22,12,24],
[34,30,23,27,31,30,29,0,31,26,33,28,33],
[28,28,25,22,28,27,32,20,0,31,32,26,26],
[27,29,24,21,25,24,27,25,20,0,25,23,26],
[26,25,22,18,26,24,29,18,19,26,0,19,23],
[31,27,24,24,28,27,39,23,25,28,32,0,27],
[23,22,26,25,27,28,27,18,25,25,28,24,0]])



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
result = np.append(np.array([13, 51, 166, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,26,22,29,22,24,21,22,24,21,22,25],
[26,0,26,25,23,23,26,26,20,20,20,19,24],
[25,25,0,22,24,21,21,23,20,19,22,22,21],
[29,26,29,0,25,26,24,24,22,21,24,25,23],
[22,28,27,26,0,29,26,25,20,21,24,21,22],
[29,28,30,25,22,0,23,23,22,20,27,26,26],
[27,25,30,27,25,28,0,29,26,20,26,28,26],
[30,25,28,27,26,28,22,0,20,22,27,27,24],
[29,31,31,29,31,29,25,31,0,22,25,21,26],
[27,31,32,30,30,31,31,29,29,0,30,33,25],
[30,31,29,27,27,24,25,24,26,21,0,24,24],
[29,32,29,26,30,25,23,24,30,18,27,0,26],
[26,27,30,28,29,25,25,27,25,26,27,25,0]])



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
result = np.append(np.array([13, 51, 167, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,21,21,20,28,23,20,26,15,24,18,26],
[28,0,18,23,20,26,23,21,22,16,19,21,24],
[30,33,0,31,24,28,29,27,25,18,22,22,28],
[30,28,20,0,19,26,34,27,27,22,24,28,31],
[31,31,27,32,0,34,34,23,27,27,32,26,25],
[23,25,23,25,17,0,23,20,20,15,26,21,27],
[28,28,22,17,17,28,0,22,21,19,22,20,22],
[31,30,24,24,28,31,29,0,27,23,33,27,26],
[25,29,26,24,24,31,30,24,0,22,29,29,26],
[36,35,33,29,24,36,32,28,29,0,31,21,29],
[27,32,29,27,19,25,29,18,22,20,0,24,28],
[33,30,29,23,25,30,31,24,22,30,27,0,23],
[25,27,23,20,26,24,29,25,25,22,23,28,0]])



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
result = np.append(np.array([13, 51, 168, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,26,27,25,31,24,26,21,29,30,26,28],
[27,0,24,32,30,36,26,29,29,29,25,26,31],
[25,27,0,29,24,31,23,23,25,29,26,27,25],
[24,19,22,0,27,29,23,23,20,16,23,28,28],
[26,21,27,24,0,25,24,18,23,26,26,22,24],
[20,15,20,22,26,0,20,20,15,19,19,13,21],
[27,25,28,28,27,31,0,27,28,27,28,29,25],
[25,22,28,28,33,31,24,0,27,28,27,29,29],
[30,22,26,31,28,36,23,24,0,26,22,28,27],
[22,22,22,35,25,32,24,23,25,0,23,28,29],
[21,26,25,28,25,32,23,24,29,28,0,32,30],
[25,25,24,23,29,38,22,22,23,23,19,0,23],
[23,20,26,23,27,30,26,22,24,22,21,28,0]])



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
result = np.append(np.array([13, 51, 169, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,21,21,14,27,27,27,20,24,31,25,36],
[34,0,32,27,28,38,40,34,25,31,38,29,43],
[30,19,0,22,20,27,36,35,28,27,35,30,40],
[30,24,29,0,18,23,35,33,21,28,31,31,36],
[37,23,31,33,0,37,28,31,22,32,42,33,39],
[24,13,24,28,14,0,26,31,22,27,26,19,31],
[24,11,15,16,23,25,0,27,18,26,29,20,31],
[24,17,16,18,20,20,24,0,16,22,28,21,27],
[31,26,23,30,29,29,33,35,0,21,38,30,37],
[27,20,24,23,19,24,25,29,30,0,31,27,43],
[20,13,16,20,9,25,22,23,13,20,0,22,28],
[26,22,21,20,18,32,31,30,21,24,29,0,32],
[15,8,11,15,12,20,20,24,14,8,23,19,0]])



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
result = np.append(np.array([13, 51, 170, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,25,18,23,20,24,24,21,18,21,24,23],
[27,0,26,26,21,26,20,19,24,21,22,24,28],
[26,25,0,15,20,21,24,22,22,24,22,23,30],
[33,25,36,0,22,26,25,25,25,24,24,30,28],
[28,30,31,29,0,24,25,26,23,20,23,24,29],
[31,25,30,25,27,0,28,26,21,24,22,25,28],
[27,31,27,26,26,23,0,26,24,24,28,23,30],
[27,32,29,26,25,25,25,0,26,25,19,28,28],
[30,27,29,26,28,30,27,25,0,25,25,29,29],
[33,30,27,27,31,27,27,26,26,0,22,31,26],
[30,29,29,27,28,29,23,32,26,29,0,30,31],
[27,27,28,21,27,26,28,23,22,20,21,0,28],
[28,23,21,23,22,23,21,23,22,25,20,23,0]])



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
result = np.append(np.array([13, 51, 171, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,27,29,25,25,24,27,27,24,25,26,28],
[27,0,25,25,23,26,27,22,17,24,23,20,23],
[24,26,0,27,22,26,26,23,25,20,27,20,34],
[22,26,24,0,26,28,27,22,24,20,23,21,31],
[26,28,29,25,0,26,28,22,31,21,28,30,30],
[26,25,25,23,25,0,23,26,26,24,25,23,31],
[27,24,25,24,23,28,0,23,23,21,25,19,29],
[24,29,28,29,29,25,28,0,26,25,28,27,26],
[24,34,26,27,20,25,28,25,0,26,30,21,29],
[27,27,31,31,30,27,30,26,25,0,28,26,30],
[26,28,24,28,23,26,26,23,21,23,0,17,27],
[25,31,31,30,21,28,32,24,30,25,34,0,33],
[23,28,17,20,21,20,22,25,22,21,24,18,0]])



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
result = np.append(np.array([13, 51, 172, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,34,25,31,35,24,20,25,25,17,25,25],
[30,0,31,19,32,37,25,20,23,32,21,28,33],
[17,20,0,17,22,17,15,14,14,20,21,19,12],
[26,32,34,0,34,23,28,29,30,33,25,28,34],
[20,19,29,17,0,16,22,22,20,21,20,22,25],
[16,14,34,28,35,0,20,25,28,35,25,26,32],
[27,26,36,23,29,31,0,14,24,29,21,21,29],
[31,31,37,22,29,26,37,0,28,30,23,25,32],
[26,28,37,21,31,23,27,23,0,23,31,23,20],
[26,19,31,18,30,16,22,21,28,0,19,14,28],
[34,30,30,26,31,26,30,28,20,32,0,23,28],
[26,23,32,23,29,25,30,26,28,37,28,0,31],
[26,18,39,17,26,19,22,19,31,23,23,20,0]])



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
result = np.append(np.array([13, 51, 173, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,43,31,35,31,34,41,35,23,30,30,26],
[25,0,41,14,35,24,26,27,22,18,29,28,22],
[8,10,0,14,29,19,13,25,12,20,12,24,17],
[20,37,37,0,31,24,22,26,17,28,27,27,27],
[16,16,22,20,0,27,14,26,28,19,19,28,18],
[20,27,32,27,24,0,20,18,21,30,30,26,30],
[17,25,38,29,37,31,0,39,32,32,27,39,29],
[10,24,26,25,25,33,12,0,24,25,20,32,29],
[16,29,39,34,23,30,19,27,0,29,20,35,23],
[28,33,31,23,32,21,19,26,22,0,35,25,36],
[21,22,39,24,32,21,24,31,31,16,0,27,32],
[21,23,27,24,23,25,12,19,16,26,24,0,24],
[25,29,34,24,33,21,22,22,28,15,19,27,0]])



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
result = np.append(np.array([13, 51, 174, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,26,31,25,27,31,13,20,21,26,16,33],
[22,0,19,32,13,19,21,26,15,9,21,14,14],
[25,32,0,36,22,31,26,25,29,24,25,27,29],
[20,19,15,0,14,18,18,7,14,13,21,13,16],
[26,38,29,37,0,32,27,28,30,26,33,23,35],
[24,32,20,33,19,0,19,21,22,28,29,28,23],
[20,30,25,33,24,32,0,21,22,14,25,22,27],
[38,25,26,44,23,30,30,0,24,21,28,22,34],
[31,36,22,37,21,29,29,27,0,12,24,11,21],
[30,42,27,38,25,23,37,30,39,0,26,25,27],
[25,30,26,30,18,22,26,23,27,25,0,21,26],
[35,37,24,38,28,23,29,29,40,26,30,0,34],
[18,37,22,35,16,28,24,17,30,24,25,17,0]])



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
result = np.append(np.array([13, 51, 175, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,28,35,34,31,39,27,28,35,41,19,25],
[21,0,26,29,32,22,30,22,25,20,32,11,16],
[23,25,0,27,27,28,28,8,23,21,30,16,15],
[16,22,24,0,25,24,17,9,29,20,23,21,12],
[17,19,24,26,0,30,29,29,23,26,35,21,8],
[20,29,23,27,21,0,32,18,19,14,34,19,21],
[12,21,23,34,22,19,0,18,30,31,23,21,11],
[24,29,43,42,22,33,33,0,32,31,31,35,27],
[23,26,28,22,28,32,21,19,0,24,26,24,12],
[16,31,30,31,25,37,20,20,27,0,38,18,14],
[10,19,21,28,16,17,28,20,25,13,0,9,5],
[32,40,35,30,30,32,30,16,27,33,42,0,24],
[26,35,36,39,43,30,40,24,39,37,46,27,0]])



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
result = np.append(np.array([13, 51, 176, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,21,32,27,28,28,27,30,24,22,27,23],
[24,0,25,36,23,27,32,28,34,23,26,31,28],
[30,26,0,31,26,24,30,34,31,25,32,26,26],
[19,15,20,0,23,19,26,23,27,24,30,30,24],
[24,28,25,28,0,28,36,34,30,27,29,30,28],
[23,24,27,32,23,0,33,28,30,21,30,29,31],
[23,19,21,25,15,18,0,25,24,21,29,21,18],
[24,23,17,28,17,23,26,0,29,21,28,28,21],
[21,17,20,24,21,21,27,22,0,21,28,25,26],
[27,28,26,27,24,30,30,30,30,0,27,33,23],
[29,25,19,21,22,21,22,23,23,24,0,25,17],
[24,20,25,21,21,22,30,23,26,18,26,0,24],
[28,23,25,27,23,20,33,30,25,28,34,27,0]])



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
result = np.append(np.array([13, 51, 177, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,24,28,27,28,32,27,27,23,27,23,27],
[18,0,22,23,24,23,25,28,24,15,24,19,26],
[27,29,0,29,27,29,36,27,24,25,28,21,31],
[23,28,22,0,29,30,33,28,24,23,18,22,28],
[24,27,24,22,0,28,30,25,21,22,23,23,29],
[23,28,22,21,23,0,27,22,23,19,23,23,30],
[19,26,15,18,21,24,0,20,22,14,20,14,25],
[24,23,24,23,26,29,31,0,22,24,21,28,33],
[24,27,27,27,30,28,29,29,0,21,24,25,28],
[28,36,26,28,29,32,37,27,30,0,25,26,30],
[24,27,23,33,28,28,31,30,27,26,0,28,32],
[28,32,30,29,28,28,37,23,26,25,23,0,34],
[24,25,20,23,22,21,26,18,23,21,19,17,0]])



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
result = np.append(np.array([13, 51, 178, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,25,24,25,19,25,24,25,28,28,30,22],
[32,0,25,20,15,23,22,23,27,26,31,30,21],
[26,26,0,31,24,29,30,26,26,30,28,28,27],
[27,31,20,0,26,31,30,31,26,31,30,30,27],
[26,36,27,25,0,29,25,30,24,29,28,32,22],
[32,28,22,20,22,0,20,21,25,28,31,37,17],
[26,29,21,21,26,31,0,28,26,28,26,31,23],
[27,28,25,20,21,30,23,0,27,31,32,30,22],
[26,24,25,25,27,26,25,24,0,27,22,31,24],
[23,25,21,20,22,23,23,20,24,0,20,31,25],
[23,20,23,21,23,20,25,19,29,31,0,26,19],
[21,21,23,21,19,14,20,21,20,20,25,0,23],
[29,30,24,24,29,34,28,29,27,26,32,28,0]])



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
result = np.append(np.array([13, 51, 179, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,27,27,20,29,33,23,27,29,25,20,20],
[26,0,32,21,26,25,31,24,21,27,27,18,23],
[24,19,0,19,21,21,27,25,24,23,24,16,23],
[24,30,32,0,28,27,29,24,24,27,23,25,28],
[31,25,30,23,0,21,26,24,23,26,24,23,19],
[22,26,30,24,30,0,29,29,25,26,28,22,19],
[18,20,24,22,25,22,0,16,23,27,21,20,22],
[28,27,26,27,27,22,35,0,29,29,22,23,25],
[24,30,27,27,28,26,28,22,0,29,28,23,26],
[22,24,28,24,25,25,24,22,22,0,24,21,22],
[26,24,27,28,27,23,30,29,23,27,0,25,25],
[31,33,35,26,28,29,31,28,28,30,26,0,21],
[31,28,28,23,32,32,29,26,25,29,26,30,0]])



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
result = np.append(np.array([13, 51, 180, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,28,24,31,25,27,25,30,26,29,27,37],
[22,0,23,23,32,23,21,27,21,18,30,20,27],
[23,28,0,26,30,19,25,27,23,22,31,28,22],
[27,28,25,0,31,26,24,29,22,23,26,25,33],
[20,19,21,20,0,21,30,17,17,18,26,26,21],
[26,28,32,25,30,0,27,31,27,28,30,31,36],
[24,30,26,27,21,24,0,22,25,18,20,18,27],
[26,24,24,22,34,20,29,0,20,21,30,24,27],
[21,30,28,29,34,24,26,31,0,34,29,25,26],
[25,33,29,28,33,23,33,30,17,0,30,24,30],
[22,21,20,25,25,21,31,21,22,21,0,21,21],
[24,31,23,26,25,20,33,27,26,27,30,0,23],
[14,24,29,18,30,15,24,24,25,21,30,28,0]])



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
result = np.append(np.array([13, 51, 181, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,16,20,19,20,27,15,14,29,22,20,17],
[21,0,23,19,33,28,24,19,20,25,23,31,18],
[35,28,0,24,34,35,23,29,23,32,29,28,30],
[31,32,27,0,35,29,37,26,20,34,30,25,27],
[32,18,17,16,0,15,27,20,18,25,27,22,19],
[31,23,16,22,36,0,29,36,23,36,34,18,31],
[24,27,28,14,24,22,0,25,25,21,28,25,21],
[36,32,22,25,31,15,26,0,32,36,33,25,34],
[37,31,28,31,33,28,26,19,0,30,31,30,31],
[22,26,19,17,26,15,30,15,21,0,33,20,22],
[29,28,22,21,24,17,23,18,20,18,0,18,20],
[31,20,23,26,29,33,26,26,21,31,33,0,32],
[34,33,21,24,32,20,30,17,20,29,31,19,0]])



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
result = np.append(np.array([13, 51, 182, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,20,27,26,28,23,24,25,33,17,22,23],
[28,0,29,27,18,25,20,23,23,30,26,25,20],
[31,22,0,29,24,21,17,28,27,29,25,29,24],
[24,24,22,0,23,26,22,28,22,38,18,22,20],
[25,33,27,28,0,22,25,24,31,27,27,26,26],
[23,26,30,25,29,0,18,22,35,27,27,25,24],
[28,31,34,29,26,33,0,29,31,37,23,25,29],
[27,28,23,23,27,29,22,0,28,33,17,24,25],
[26,28,24,29,20,16,20,23,0,27,18,29,22],
[18,21,22,13,24,24,14,18,24,0,20,20,27],
[34,25,26,33,24,24,28,34,33,31,0,32,23],
[29,26,22,29,25,26,26,27,22,31,19,0,25],
[28,31,27,31,25,27,22,26,29,24,28,26,0]])



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
result = np.append(np.array([13, 51, 183, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,21,17,18,24,19,31,29,16,18,20,29],
[28,0,24,24,21,29,19,36,31,25,17,22,25],
[30,27,0,21,33,31,18,35,30,29,23,23,28],
[34,27,30,0,27,35,18,31,32,21,21,22,27],
[33,30,18,24,0,32,19,29,29,28,20,19,35],
[27,22,20,16,19,0,18,28,23,19,18,19,26],
[32,32,33,33,32,33,0,38,37,32,24,29,41],
[20,15,16,20,22,23,13,0,17,19,14,15,19],
[22,20,21,19,22,28,14,34,0,23,13,19,23],
[35,26,22,30,23,32,19,32,28,0,27,17,32],
[33,34,28,30,31,33,27,37,38,24,0,35,30],
[31,29,28,29,32,32,22,36,32,34,16,0,29],
[22,26,23,24,16,25,10,32,28,19,21,22,0]])



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
result = np.append(np.array([13, 51, 184, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,27,23,31,26,22,29,29,32,31,36,35],
[23,0,18,20,27,15,21,19,18,30,20,24,21],
[24,33,0,25,25,25,23,19,27,28,25,32,27],
[28,31,26,0,22,26,23,18,30,33,26,33,28],
[20,24,26,29,0,27,26,24,33,31,22,32,29],
[25,36,26,25,24,0,32,28,22,31,26,33,32],
[29,30,28,28,25,19,0,30,29,28,25,36,26],
[22,32,32,33,27,23,21,0,32,32,31,36,25],
[22,33,24,21,18,29,22,19,0,25,24,37,24],
[19,21,23,18,20,20,23,19,26,0,18,25,18],
[20,31,26,25,29,25,26,20,27,33,0,36,23],
[15,27,19,18,19,18,15,15,14,26,15,0,11],
[16,30,24,23,22,19,25,26,27,33,28,40,0]])



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
result = np.append(np.array([13, 51, 185, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,31,20,31,25,33,20,33,21,29,25,19],
[30,0,44,24,33,29,44,33,40,32,43,34,35],
[20,7,0,19,13,22,23,22,32,21,30,13,22],
[31,27,32,0,22,33,36,22,40,22,39,28,24],
[20,18,38,29,0,33,37,28,34,34,40,34,29],
[26,22,29,18,18,0,30,17,36,22,32,27,24],
[18,7,28,15,14,21,0,17,18,16,30,23,24],
[31,18,29,29,23,34,34,0,37,20,34,24,22],
[18,11,19,11,17,15,33,14,0,19,20,14,18],
[30,19,30,29,17,29,35,31,32,0,33,21,31],
[22,8,21,12,11,19,21,17,31,18,0,10,23],
[26,17,38,23,17,24,28,27,37,30,41,0,34],
[32,16,29,27,22,27,27,29,33,20,28,17,0]])



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
result = np.append(np.array([13, 51, 186, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,16,24,18,21,20,24,23,18,21,25,26],
[32,0,24,36,26,28,25,30,28,26,24,25,24],
[35,27,0,26,21,28,26,31,30,27,27,23,33],
[27,15,25,0,25,19,21,29,28,27,22,27,22],
[33,25,30,26,0,30,29,30,31,29,22,23,28],
[30,23,23,32,21,0,21,28,28,25,25,21,29],
[31,26,25,30,22,30,0,22,27,25,26,24,27],
[27,21,20,22,21,23,29,0,27,18,24,26,26],
[28,23,21,23,20,23,24,24,0,25,24,23,19],
[33,25,24,24,22,26,26,33,26,0,22,19,26],
[30,27,24,29,29,26,25,27,27,29,0,29,22],
[26,26,28,24,28,30,27,25,28,32,22,0,26],
[25,27,18,29,23,22,24,25,32,25,29,25,0]])



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
result = np.append(np.array([13, 51, 187, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,15,1,12,14,23,17,15,5,10,30,7],
[31,0,21,13,9,16,22,25,20,10,10,36,9],
[36,30,0,6,12,18,36,29,14,20,10,27,19],
[50,38,45,0,26,22,36,30,26,25,12,37,36],
[39,42,39,25,0,13,33,28,28,20,12,38,38],
[37,35,33,29,38,0,31,33,27,24,26,36,32],
[28,29,15,15,18,20,0,28,18,17,19,28,24],
[34,26,22,21,23,18,23,0,26,23,23,35,22],
[36,31,37,25,23,24,33,25,0,32,23,41,37],
[46,41,31,26,31,27,34,28,19,0,26,42,32],
[41,41,41,39,39,25,32,28,28,25,0,42,42],
[21,15,24,14,13,15,23,16,10,9,9,0,7],
[44,42,32,15,13,19,27,29,14,19,9,44,0]])



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
result = np.append(np.array([13, 51, 188, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,27,12,15,27,25,12,14,13,14,2,14],
[51,0,42,21,51,51,51,14,29,36,38,38,14],
[24,9,0,21,24,11,49,12,11,9,21,24,14],
[39,30,30,0,30,30,30,17,17,30,26,30,29],
[36,0,27,21,0,23,49,12,14,22,23,17,14],
[24,0,40,21,28,0,49,12,0,13,36,15,12],
[26,0,2,21,2,2,0,2,2,2,11,17,14],
[39,37,39,34,39,39,49,0,39,22,51,39,42],
[37,22,40,34,37,51,49,12,0,22,36,37,12],
[38,15,42,21,29,38,49,29,29,0,38,17,29],
[37,13,30,25,28,15,40,0,15,13,0,30,14],
[49,13,27,21,34,36,34,12,14,34,21,0,14],
[37,37,37,22,37,39,37,9,39,22,37,37,0]])



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
result = np.append(np.array([13, 51, 189, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,24,26,15,24,26,19,18,25,20,22,22],
[23,0,22,19,18,28,25,22,22,25,22,21,30],
[27,29,0,29,20,29,29,23,30,29,22,28,31],
[25,32,22,0,20,28,31,28,24,32,21,27,31],
[36,33,31,31,0,37,32,24,24,32,28,25,29],
[27,23,22,23,14,0,22,18,15,28,19,19,17],
[25,26,22,20,19,29,0,22,20,28,22,21,29],
[32,29,28,23,27,33,29,0,19,27,23,25,26],
[33,29,21,27,27,36,31,32,0,32,27,27,29],
[26,26,22,19,19,23,23,24,19,0,16,16,27],
[31,29,29,30,23,32,29,28,24,35,0,24,33],
[29,30,23,24,26,32,30,26,24,35,27,0,33],
[29,21,20,20,22,34,22,25,22,24,18,18,0]])



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
result = np.append(np.array([13, 51, 190, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,13,28,15,16,34,18,26,16,14,23,14],
[31,0,21,27,24,18,35,22,31,15,16,19,29],
[38,30,0,26,35,29,42,24,41,24,32,34,29],
[23,24,25,0,23,24,37,30,31,18,28,30,23],
[36,27,16,28,0,20,41,16,24,25,25,29,26],
[35,33,22,27,31,0,37,28,31,27,34,33,34],
[17,16,9,14,10,14,0,13,14,13,25,13,24],
[33,29,27,21,35,23,38,0,35,30,24,29,28],
[25,20,10,20,27,20,37,16,0,24,22,28,24],
[35,36,27,33,26,24,38,21,27,0,25,27,24],
[37,35,19,23,26,17,26,27,29,26,0,21,34],
[28,32,17,21,22,18,38,22,23,24,30,0,29],
[37,22,22,28,25,17,27,23,27,27,17,22,0]])



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
result = np.append(np.array([13, 51, 191, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,32,26,31,24,31,29,25,32,27,28,31],
[21,0,27,28,30,21,30,25,19,22,23,26,25],
[19,24,0,26,22,16,21,28,22,23,30,30,20],
[25,23,25,0,26,25,31,25,21,26,33,27,28],
[20,21,29,25,0,19,20,21,21,24,30,27,24],
[27,30,35,26,32,0,27,29,25,22,34,37,33],
[20,21,30,20,31,24,0,24,21,23,34,30,22],
[22,26,23,26,30,22,27,0,22,22,28,26,25],
[26,32,29,30,30,26,30,29,0,21,31,30,25],
[19,29,28,25,27,29,28,29,30,0,24,25,31],
[24,28,21,18,21,17,17,23,20,27,0,18,23],
[23,25,21,24,24,14,21,25,21,26,33,0,22],
[20,26,31,23,27,18,29,26,26,20,28,29,0]])



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
result = np.append(np.array([13, 51, 192, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,35,19,29,24,28,31,33,28,37,35,20],
[16,0,19,20,18,20,17,31,26,23,37,33,10],
[16,32,0,20,26,17,12,27,27,29,38,40,33],
[32,31,31,0,24,20,33,38,31,35,38,41,15],
[22,33,25,27,0,19,10,33,33,25,38,39,23],
[27,31,34,31,32,0,20,31,31,32,35,33,23],
[23,34,39,18,41,31,0,42,29,35,40,46,32],
[20,20,24,13,18,20,9,0,20,31,30,29,9],
[18,25,24,20,18,20,22,31,0,31,40,45,24],
[23,28,22,16,26,19,16,20,20,0,27,21,13],
[14,14,13,13,13,16,11,21,11,24,0,18,8],
[16,18,11,10,12,18,5,22,6,30,33,0,3],
[31,41,18,36,28,28,19,42,27,38,43,48,0]])



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
result = np.append(np.array([13, 51, 193, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,28,24,27,25,26,22,25,26,31,21,17],
[23,0,26,28,29,27,30,25,22,27,37,33,28],
[23,25,0,29,30,25,34,26,25,29,33,24,25],
[27,23,22,0,28,15,23,22,15,22,31,22,19],
[24,22,21,23,0,13,24,19,14,25,31,28,15],
[26,24,26,36,38,0,27,23,19,26,30,26,23],
[25,21,17,28,27,24,0,22,23,27,34,28,22],
[29,26,25,29,32,28,29,0,22,30,33,26,25],
[26,29,26,36,37,32,28,29,0,33,34,30,24],
[25,24,22,29,26,25,24,21,18,0,23,27,23],
[20,14,18,20,20,21,17,18,17,28,0,17,24],
[30,18,27,29,23,25,23,25,21,24,34,0,25],
[34,23,26,32,36,28,29,26,27,28,27,26,0]])



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
result = np.append(np.array([13, 51, 194, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,23,18,19,26,20,19,19,22,21,21,23],
[28,0,29,20,22,29,29,25,27,27,23,24,24],
[28,22,0,19,21,29,23,20,22,26,21,21,22],
[33,31,32,0,28,29,32,28,28,30,25,27,29],
[32,29,30,23,0,31,32,27,26,31,25,27,24],
[25,22,22,22,20,0,24,20,25,27,22,19,23],
[31,22,28,19,19,27,0,21,23,25,25,21,25],
[32,26,31,23,24,31,30,0,28,28,27,29,31],
[32,24,29,23,25,26,28,23,0,25,22,21,28],
[29,24,25,21,20,24,26,23,26,0,23,22,29],
[30,28,30,26,26,29,26,24,29,28,0,24,27],
[30,27,30,24,24,32,30,22,30,29,27,0,30],
[28,27,29,22,27,28,26,20,23,22,24,21,0]])



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
result = np.append(np.array([13, 51, 195, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,25,19,8,20,11,15,39,22,22,22,21],
[19,0,25,19,11,16,16,30,30,22,20,17,21],
[26,26,0,27,21,26,14,27,40,28,9,26,23],
[32,32,24,0,22,28,18,27,41,33,18,32,31],
[43,40,30,29,0,28,24,34,47,34,20,34,34],
[31,35,25,23,23,0,17,27,31,23,18,29,32],
[40,35,37,33,27,34,0,32,44,31,36,22,36],
[36,21,24,24,17,24,19,0,32,28,26,23,24],
[12,21,11,10,4,20,7,19,0,16,7,17,18],
[29,29,23,18,17,28,20,23,35,0,16,23,26],
[29,31,42,33,31,33,15,25,44,35,0,37,28],
[29,34,25,19,17,22,29,28,34,28,14,0,28],
[30,30,28,20,17,19,15,27,33,25,23,23,0]])



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
result = np.append(np.array([13, 51, 196, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,23,31,27,20,28,24,29,26,27,26,25],
[19,0,23,28,28,23,24,25,29,29,26,25,25],
[28,28,0,32,29,34,28,31,30,24,31,23,31],
[20,23,19,0,21,26,19,24,26,15,24,18,31],
[24,23,22,30,0,27,30,24,29,22,27,23,25],
[31,28,17,25,24,0,24,30,31,24,32,21,26],
[23,27,23,32,21,27,0,28,27,29,30,21,24],
[27,26,20,27,27,21,23,0,25,23,28,25,25],
[22,22,21,25,22,20,24,26,0,24,21,21,24],
[25,22,27,36,29,27,22,28,27,0,25,24,32],
[24,25,20,27,24,19,21,23,30,26,0,21,28],
[25,26,28,33,28,30,30,26,30,27,30,0,25],
[26,26,20,20,26,25,27,26,27,19,23,26,0]])



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
result = np.append(np.array([13, 51, 197, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,34,27,26,29,20,28,24,30,26,21,30],
[23,0,30,21,20,14,17,22,16,24,16,15,25],
[17,21,0,10,20,12,25,17,15,21,27,14,19],
[24,30,41,0,24,18,25,23,30,23,29,24,35],
[25,31,31,27,0,20,19,24,24,26,33,24,24],
[22,37,39,33,31,0,29,29,26,26,32,21,31],
[31,34,26,26,32,22,0,27,19,25,30,21,24],
[23,29,34,28,27,22,24,0,22,35,26,17,27],
[27,35,36,21,27,25,32,29,0,28,33,29,28],
[21,27,30,28,25,25,26,16,23,0,26,13,23],
[25,35,24,22,18,19,21,25,18,25,0,21,21],
[30,36,37,27,27,30,30,34,22,38,30,0,26],
[21,26,32,16,27,20,27,24,23,28,30,25,0]])



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
result = np.append(np.array([13, 51, 198, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,24,25,30,30,31,35,31,33,21,21,28],
[36,0,27,21,29,20,23,26,20,29,40,20,28],
[27,24,0,32,30,39,40,26,32,33,19,19,29],
[26,30,19,0,27,37,28,26,9,22,26,8,36],
[21,22,21,24,0,21,23,11,20,22,30,12,22],
[21,31,12,14,30,0,28,35,20,22,27,19,28],
[20,28,11,23,28,23,0,21,19,39,26,18,18],
[16,25,25,25,40,16,30,0,25,24,31,32,41],
[20,31,19,42,31,31,32,26,0,31,21,21,30],
[18,22,18,29,29,29,12,27,20,0,20,20,19],
[30,11,32,25,21,24,25,20,30,31,0,7,19],
[30,31,32,43,39,32,33,19,30,31,44,0,39],
[23,23,22,15,29,23,33,10,21,32,32,12,0]])



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
result = np.append(np.array([13, 51, 199, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,20,28,20,29,21,28,24,30,29,25,26],
[31,0,26,30,22,32,27,29,29,25,25,36,28],
[31,25,0,31,26,31,27,30,24,33,27,25,31],
[23,21,20,0,22,35,26,27,26,28,32,28,31],
[31,29,25,29,0,40,29,24,32,33,31,33,32],
[22,19,20,16,11,0,13,18,27,21,19,16,19],
[30,24,24,25,22,38,0,28,29,32,32,31,27],
[23,22,21,24,27,33,23,0,22,30,27,25,27],
[27,22,27,25,19,24,22,29,0,33,22,24,24],
[21,26,18,23,18,30,19,21,18,0,19,27,27],
[22,26,24,19,20,32,19,24,29,32,0,27,24],
[26,15,26,23,18,35,20,26,27,24,24,0,26],
[25,23,20,20,19,32,24,24,27,24,27,25,0]])



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
result = np.append(np.array([13, 51, 200, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbrcwd/mebbrcwd_13_51.csv", index=False, header=False)