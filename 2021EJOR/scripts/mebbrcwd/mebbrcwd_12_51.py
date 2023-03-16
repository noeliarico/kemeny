
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg
from kemeny import sc

rep = 1
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,30,27,24,22,22,23,27,32,19,17,24],
[21,0,21,23,19,22,24,28,25,21,25,28],
[24,30,0,21,25,29,20,18,27,22,23,27],
[27,28,30,0,25,24,22,19,26,20,20,27],
[29,32,26,26,0,20,27,27,33,20,19,28],
[29,29,22,27,31,0,27,27,26,27,22,25],
[28,27,31,29,24,24,0,25,30,23,17,26],
[24,23,33,32,24,24,26,0,30,28,26,31],
[19,26,24,25,18,25,21,21,0,16,17,24],
[32,30,29,31,31,24,28,23,35,0,19,31],
[34,26,28,31,32,29,34,25,34,32,0,36],
[27,23,24,24,23,26,25,20,27,20,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 1, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,41,28,14,13,28,26,37,14,26,28],
[38,0,41,38,38,27,28,24,51,15,27,28],
[10,10,0,10,11,0,38,23,11,0,36,28],
[23,13,41,0,24,13,28,23,24,0,26,28],
[37,13,40,27,0,13,28,26,37,27,26,28],
[38,24,51,38,38,0,38,23,51,15,36,28],
[23,23,13,23,23,13,0,23,23,0,26,27],
[25,27,28,28,25,28,28,0,38,28,27,15],
[14,0,40,27,14,0,28,13,0,14,26,28],
[37,36,51,51,24,36,51,23,37,0,36,28],
[25,24,15,25,25,15,25,24,25,15,0,15],
[23,23,23,23,23,23,24,36,23,23,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 2, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,30,28,28,29,28,29,24,30,33,30],
[28,0,32,25,23,30,33,29,29,28,32,29],
[21,19,0,27,20,28,21,25,22,21,25,26],
[23,26,24,0,19,22,25,23,19,28,28,26],
[23,28,31,32,0,26,26,27,25,24,26,28],
[22,21,23,29,25,0,24,24,20,25,29,26],
[23,18,30,26,25,27,0,24,27,30,26,26],
[22,22,26,28,24,27,27,0,21,29,32,34],
[27,22,29,32,26,31,24,30,0,26,28,28],
[21,23,30,23,27,26,21,22,25,0,29,24],
[18,19,26,23,25,22,25,19,23,22,0,24],
[21,22,25,25,23,25,25,17,23,27,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 3, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,21,29,22,34,22,22,29,28,26,32],
[15,0,8,27,18,26,27,10,17,23,20,8],
[30,43,0,35,33,34,28,35,35,35,32,23],
[22,24,16,0,32,34,28,8,38,30,13,23],
[29,33,18,19,0,24,17,17,18,30,18,22],
[17,25,17,17,27,0,15,17,18,25,12,5],
[29,24,23,23,34,36,0,15,31,33,15,23],
[29,41,16,43,34,34,36,0,43,40,23,23],
[22,34,16,13,33,33,20,8,0,34,16,15],
[23,28,16,21,21,26,18,11,17,0,20,23],
[25,31,19,38,33,39,36,28,35,31,0,31],
[19,43,28,28,29,46,28,28,36,28,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 4, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,27,25,28,20,24,24,24,29,23,19],
[25,0,22,25,27,22,21,25,25,24,23,23],
[24,29,0,30,29,26,29,30,26,32,23,25],
[26,26,21,0,28,19,22,25,25,30,22,24],
[23,24,22,23,0,23,24,27,22,29,24,22],
[31,29,25,32,28,0,24,27,20,30,24,29],
[27,30,22,29,27,27,0,25,25,34,29,27],
[27,26,21,26,24,24,26,0,25,30,17,26],
[27,26,25,26,29,31,26,26,0,28,25,28],
[22,27,19,21,22,21,17,21,23,0,19,20],
[28,28,28,29,27,27,22,34,26,32,0,28],
[32,28,26,27,29,22,24,25,23,31,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 5, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,28,22,26,26,32,29,30,30,31,29],
[20,0,18,15,13,19,22,18,22,29,17,23],
[23,33,0,21,21,28,29,20,27,29,29,34],
[29,36,30,0,26,32,35,21,33,36,28,34],
[25,38,30,25,0,27,33,34,37,35,30,28],
[25,32,23,19,24,0,27,24,29,31,29,32],
[19,29,22,16,18,24,0,24,24,30,20,21],
[22,33,31,30,17,27,27,0,29,32,23,29],
[21,29,24,18,14,22,27,22,0,32,19,22],
[21,22,22,15,16,20,21,19,19,0,19,18],
[20,34,22,23,21,22,31,28,32,32,0,21],
[22,28,17,17,23,19,30,22,29,33,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 6, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,33,27,33,22,34,30,28,30,25,26],
[19,0,27,23,27,24,30,31,27,26,22,28],
[18,24,0,22,24,20,27,26,25,22,18,20],
[24,28,29,0,28,26,33,27,29,28,27,32],
[18,24,27,23,0,20,30,28,25,27,20,27],
[29,27,31,25,31,0,29,32,32,29,21,29],
[17,21,24,18,21,22,0,21,27,19,16,24],
[21,20,25,24,23,19,30,0,21,25,21,26],
[23,24,26,22,26,19,24,30,0,23,18,26],
[21,25,29,23,24,22,32,26,28,0,19,26],
[26,29,33,24,31,30,35,30,33,32,0,34],
[25,23,31,19,24,22,27,25,25,25,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 7, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,26,14,31,21,27,30,20,29,28,29],
[34,0,27,18,24,24,33,29,23,35,32,36],
[25,24,0,19,23,21,33,32,18,37,28,25],
[37,33,32,0,33,27,32,35,27,25,34,28],
[20,27,28,18,0,29,27,32,21,30,24,24],
[30,27,30,24,22,0,33,33,16,36,43,26],
[24,18,18,19,24,18,0,18,18,16,21,25],
[21,22,19,16,19,18,33,0,11,27,33,22],
[31,28,33,24,30,35,33,40,0,39,48,42],
[22,16,14,26,21,15,35,24,12,0,20,20],
[23,19,23,17,27,8,30,18,3,31,0,24],
[22,15,26,23,27,25,26,29,9,31,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 8, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,30,29,31,28,24,30,29,24,31,32],
[18,0,21,22,20,26,16,18,17,15,19,22],
[21,30,0,28,23,24,26,25,28,25,27,29],
[22,29,23,0,24,26,24,22,29,23,24,33],
[20,31,28,27,0,27,23,19,26,25,24,27],
[23,25,27,25,24,0,22,21,25,28,24,29],
[27,35,25,27,28,29,0,32,27,25,29,35],
[21,33,26,29,32,30,19,0,25,27,27,28],
[22,34,23,22,25,26,24,26,0,20,25,28],
[27,36,26,28,26,23,26,24,31,0,26,29],
[20,32,24,27,27,27,22,24,26,25,0,27],
[19,29,22,18,24,22,16,23,23,22,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 9, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,31,32,25,34,25,29,30,37,36,28],
[24,0,22,23,23,18,26,27,23,27,30,21],
[20,29,0,26,28,27,28,29,29,30,30,26],
[19,28,25,0,25,27,22,27,24,30,39,22],
[26,28,23,26,0,20,26,22,25,24,33,19],
[17,33,24,24,31,0,26,20,22,27,31,25],
[26,25,23,29,25,25,0,31,27,27,36,25],
[22,24,22,24,29,31,20,0,21,30,34,26],
[21,28,22,27,26,29,24,30,0,26,33,23],
[14,24,21,21,27,24,24,21,25,0,27,17],
[15,21,21,12,18,20,15,17,18,24,0,17],
[23,30,25,29,32,26,26,25,28,34,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 10, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,22,19,22,20,17,31,18,26,23,23],
[24,0,25,25,17,22,22,27,21,28,24,20],
[29,26,0,26,21,20,25,31,25,31,23,24],
[32,26,25,0,24,26,20,29,26,29,25,26],
[29,34,30,27,0,28,23,34,26,29,26,27],
[31,29,31,25,23,0,26,33,24,33,31,27],
[34,29,26,31,28,25,0,37,27,32,30,25],
[20,24,20,22,17,18,14,0,15,23,18,19],
[33,30,26,25,25,27,24,36,0,31,30,24],
[25,23,20,22,22,18,19,28,20,0,21,23],
[28,27,28,26,25,20,21,33,21,30,0,20],
[28,31,27,25,24,24,26,32,27,28,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 11, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,51,33,26,47,41,27,51,31,38,24],
[18,0,32,7,10,18,25,33,25,25,18,5],
[0,19,0,22,8,25,12,15,20,22,12,13],
[18,44,29,0,18,18,37,33,26,26,22,22],
[25,41,43,33,0,39,38,35,47,35,38,31],
[4,33,26,33,12,0,26,19,34,26,38,16],
[10,26,39,14,13,25,0,27,40,27,27,12],
[24,18,36,18,16,32,24,0,36,16,31,16],
[0,26,31,25,4,17,11,15,0,19,24,9],
[20,26,29,25,16,25,24,35,32,0,31,16],
[13,33,39,29,13,13,24,20,27,20,0,20],
[27,46,38,29,20,35,39,35,42,35,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 12, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,32,25,31,32,20,20,25,26,33,41],
[13,0,21,23,21,21,15,20,25,21,15,28],
[19,30,0,24,31,32,27,22,22,18,19,22],
[26,28,27,0,31,37,21,22,24,20,21,29],
[20,30,20,20,0,30,23,12,15,19,18,28],
[19,30,19,14,21,0,16,14,17,19,23,24],
[31,36,24,30,28,35,0,14,22,23,29,34],
[31,31,29,29,39,37,37,0,27,22,28,32],
[26,26,29,27,36,34,29,24,0,27,22,35],
[25,30,33,31,32,32,28,29,24,0,28,30],
[18,36,32,30,33,28,22,23,29,23,0,27],
[10,23,29,22,23,27,17,19,16,21,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 13, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,20,26,24,16,19,4,17,24,21,32],
[28,0,21,28,24,22,29,17,25,23,26,28],
[31,30,0,23,23,22,31,13,23,21,28,31],
[25,23,28,0,19,15,20,11,15,25,21,28],
[27,27,28,32,0,20,28,23,23,25,25,26],
[35,29,29,36,31,0,27,22,19,31,27,35],
[32,22,20,31,23,24,0,23,33,27,26,31],
[47,34,38,40,28,29,28,0,25,31,30,39],
[34,26,28,36,28,32,18,26,0,27,29,31],
[27,28,30,26,26,20,24,20,24,0,25,27],
[30,25,23,30,26,24,25,21,22,26,0,28],
[19,23,20,23,25,16,20,12,20,24,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 14, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,34,23,21,26,25,21,22,31,21,26],
[37,0,31,23,33,18,22,30,31,24,26,31],
[17,20,0,17,18,15,10,13,18,25,13,16],
[28,28,34,0,31,29,21,27,28,24,22,26],
[30,18,33,20,0,26,20,30,26,34,15,31],
[25,33,36,22,25,0,20,23,33,33,19,26],
[26,29,41,30,31,31,0,27,36,40,25,35],
[30,21,38,24,21,28,24,0,24,28,16,23],
[29,20,33,23,25,18,15,27,0,23,10,17],
[20,27,26,27,17,18,11,23,28,0,14,27],
[30,25,38,29,36,32,26,35,41,37,0,35],
[25,20,35,25,20,25,16,28,34,24,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 15, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,20,29,29,17,26,15,23,23,25,21],
[30,0,25,31,29,26,24,20,22,31,33,28],
[31,26,0,23,26,21,27,23,24,27,24,25],
[22,20,28,0,28,24,25,18,21,18,22,20],
[22,22,25,23,0,21,28,15,23,26,28,27],
[34,25,30,27,30,0,30,27,30,32,26,30],
[25,27,24,26,23,21,0,23,27,27,30,22],
[36,31,28,33,36,24,28,0,30,34,31,36],
[28,29,27,30,28,21,24,21,0,34,31,32],
[28,20,24,33,25,19,24,17,17,0,26,32],
[26,18,27,29,23,25,21,20,20,25,0,23],
[30,23,26,31,24,21,29,15,19,19,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 16, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,25,27,29,19,24,21,23,30,23,18],
[26,0,26,25,18,24,24,20,36,30,22,27],
[26,25,0,25,23,32,30,26,32,33,27,25],
[24,26,26,0,21,24,22,28,26,29,22,23],
[22,33,28,30,0,29,27,27,33,35,28,27],
[32,27,19,27,22,0,24,27,33,33,26,26],
[27,27,21,29,24,27,0,28,25,24,23,23],
[30,31,25,23,24,24,23,0,30,28,28,27],
[28,15,19,25,18,18,26,21,0,31,20,25],
[21,21,18,22,16,18,27,23,20,0,15,14],
[28,29,24,29,23,25,28,23,31,36,0,31],
[33,24,26,28,24,25,28,24,26,37,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 17, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,33,27,28,25,33,29,26,28,30,28],
[26,0,21,17,27,22,28,29,19,24,27,22],
[18,30,0,21,28,22,27,30,24,27,20,24],
[24,34,30,0,34,28,32,35,30,31,33,29],
[23,24,23,17,0,20,27,19,17,19,18,22],
[26,29,29,23,31,0,35,30,25,27,27,31],
[18,23,24,19,24,16,0,25,25,25,26,24],
[22,22,21,16,32,21,26,0,23,22,26,23],
[25,32,27,21,34,26,26,28,0,28,28,24],
[23,27,24,20,32,24,26,29,23,0,25,20],
[21,24,31,18,33,24,25,25,23,26,0,24],
[23,29,27,22,29,20,27,28,27,31,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 18, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,27,22,20,26,26,25,21,25,28,13],
[22,0,20,20,25,16,22,17,29,21,17,15],
[24,31,0,22,17,29,26,25,20,29,29,18],
[29,31,29,0,31,32,29,17,25,23,23,20],
[31,26,34,20,0,29,23,27,25,29,22,26],
[25,35,22,19,22,0,25,25,25,24,26,17],
[25,29,25,22,28,26,0,24,30,33,25,19],
[26,34,26,34,24,26,27,0,27,30,23,21],
[30,22,31,26,26,26,21,24,0,30,26,22],
[26,30,22,28,22,27,18,21,21,0,22,20],
[23,34,22,28,29,25,26,28,25,29,0,20],
[38,36,33,31,25,34,32,30,29,31,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 19, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,22,22,25,26,27,23,20,26,25,17],
[18,0,29,18,34,27,28,20,29,21,28,21],
[29,22,0,23,25,33,26,27,27,29,32,29],
[29,33,28,0,29,31,27,20,29,25,25,25],
[26,17,26,22,0,29,26,28,25,26,32,18],
[25,24,18,20,22,0,28,22,18,18,20,21],
[24,23,25,24,25,23,0,22,23,25,30,24],
[28,31,24,31,23,29,29,0,30,24,33,28],
[31,22,24,22,26,33,28,21,0,23,34,20],
[25,30,22,26,25,33,26,27,28,0,30,19],
[26,23,19,26,19,31,21,18,17,21,0,23],
[34,30,22,26,33,30,27,23,31,32,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 20, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,22,25,25,29,29,27,20,27,27,28],
[24,0,17,24,23,30,24,22,20,28,18,21],
[29,34,0,31,31,30,31,31,24,30,26,33],
[26,27,20,0,26,30,24,26,29,23,26,28],
[26,28,20,25,0,26,25,29,27,27,22,26],
[22,21,21,21,25,0,20,24,24,26,23,23],
[22,27,20,27,26,31,0,30,23,29,25,21],
[24,29,20,25,22,27,21,0,24,27,16,26],
[31,31,27,22,24,27,28,27,0,31,28,27],
[24,23,21,28,24,25,22,24,20,0,24,31],
[24,33,25,25,29,28,26,35,23,27,0,28],
[23,30,18,23,25,28,30,25,24,20,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 21, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,36,22,34,28,26,29,24,29,32,24],
[27,0,31,22,27,25,21,29,25,25,28,22],
[15,20,0,16,22,21,18,23,19,22,28,14],
[29,29,35,0,26,28,21,30,27,27,30,22],
[17,24,29,25,0,24,24,26,23,27,25,25],
[23,26,30,23,27,0,26,23,20,27,25,23],
[25,30,33,30,27,25,0,30,25,35,29,28],
[22,22,28,21,25,28,21,0,19,26,23,18],
[27,26,32,24,28,31,26,32,0,31,33,25],
[22,26,29,24,24,24,16,25,20,0,28,22],
[19,23,23,21,26,26,22,28,18,23,0,20],
[27,29,37,29,26,28,23,33,26,29,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 22, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,4,4,39,4,22,22,34,22,30,39],
[16,0,4,16,33,4,4,4,16,16,12,33],
[47,47,0,12,47,12,30,30,47,30,30,51],
[47,35,39,0,51,17,35,39,47,47,47,39],
[12,18,4,0,0,0,18,4,12,0,30,4],
[47,47,39,34,51,0,39,22,51,51,30,51],
[29,47,21,16,33,12,0,16,29,29,12,33],
[29,47,21,12,47,29,35,0,29,29,30,33],
[17,35,4,4,39,0,22,22,0,4,30,21],
[29,35,21,4,51,0,22,22,47,0,30,39],
[21,39,21,4,21,21,39,21,21,21,0,21],
[12,18,0,12,47,0,18,18,30,12,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 23, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,34,32,25,23,21,18,31,34,31,30],
[25,0,26,32,25,19,25,26,31,30,26,29],
[17,25,0,27,24,18,16,15,29,18,22,23],
[19,19,24,0,19,19,21,13,25,23,28,21],
[26,26,27,32,0,27,30,25,27,26,35,28],
[28,32,33,32,24,0,27,24,30,27,33,31],
[30,26,35,30,21,24,0,21,30,25,31,25],
[33,25,36,38,26,27,30,0,33,27,35,34],
[20,20,22,26,24,21,21,18,0,18,22,25],
[17,21,33,28,25,24,26,24,33,0,29,25],
[20,25,29,23,16,18,20,16,29,22,0,22],
[21,22,28,30,23,20,26,17,26,26,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 24, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,29,24,19,23,29,20,22,25,18,23],
[30,0,29,21,25,24,27,22,25,27,18,21],
[22,22,0,22,21,24,23,22,26,23,21,22],
[27,30,29,0,19,21,28,20,28,28,25,24],
[32,26,30,32,0,22,26,26,31,26,23,20],
[28,27,27,30,29,0,26,28,30,30,23,21],
[22,24,28,23,25,25,0,22,28,24,19,20],
[31,29,29,31,25,23,29,0,34,31,27,27],
[29,26,25,23,20,21,23,17,0,22,21,20],
[26,24,28,23,25,21,27,20,29,0,25,20],
[33,33,30,26,28,28,32,24,30,26,0,29],
[28,30,29,27,31,30,31,24,31,31,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 25, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,27,13,25,21,30,31,28,9,28,22],
[25,0,28,14,37,25,24,36,33,20,23,26],
[24,23,0,21,25,13,27,41,38,11,30,20],
[38,37,30,0,34,27,29,43,33,14,28,31],
[26,14,26,17,0,8,28,27,30,12,30,18],
[30,26,38,24,43,0,30,44,38,19,30,34],
[21,27,24,22,23,21,0,32,29,16,16,20],
[20,15,10,8,24,7,19,0,21,14,20,16],
[23,18,13,18,21,13,22,30,0,9,18,18],
[42,31,40,37,39,32,35,37,42,0,43,24],
[23,28,21,23,21,21,35,31,33,8,0,24],
[29,25,31,20,33,17,31,35,33,27,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 26, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,17,19,23,21,22,24,23,22,23,25],
[30,0,22,22,21,20,30,25,29,23,22,23],
[34,29,0,22,27,21,31,31,29,30,23,25],
[32,29,29,0,24,29,32,33,28,28,25,26],
[28,30,24,27,0,24,29,25,28,24,28,25],
[30,31,30,22,27,0,35,29,29,27,29,25],
[29,21,20,19,22,16,0,27,20,23,20,23],
[27,26,20,18,26,22,24,0,20,25,22,23],
[28,22,22,23,23,22,31,31,0,25,22,21],
[29,28,21,23,27,24,28,26,26,0,22,24],
[28,29,28,26,23,22,31,29,29,29,0,25],
[26,28,26,25,26,26,28,28,30,27,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 27, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,22,15,25,16,18,29,15,23,31,15],
[18,0,31,19,26,17,28,13,21,27,25,20],
[29,20,0,15,23,12,22,21,14,20,25,15],
[36,32,36,0,30,29,38,31,33,32,37,25],
[26,25,28,21,0,22,26,27,26,26,26,28],
[35,34,39,22,29,0,25,20,32,26,36,23],
[33,23,29,13,25,26,0,23,19,19,20,21],
[22,38,30,20,24,31,28,0,23,31,30,25],
[36,30,37,18,25,19,32,28,0,24,34,26],
[28,24,31,19,25,25,32,20,27,0,33,25],
[20,26,26,14,25,15,31,21,17,18,0,15],
[36,31,36,26,23,28,30,26,25,26,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 28, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,28,24,20,29,28,20,24,24,24,24],
[23,0,32,28,24,22,24,25,25,25,24,28],
[23,19,0,20,21,25,21,25,24,22,22,26],
[27,23,31,0,21,26,21,22,27,28,26,28],
[31,27,30,30,0,33,24,30,25,26,23,29],
[22,29,26,25,18,0,23,25,23,24,26,34],
[23,27,30,30,27,28,0,22,31,25,26,33],
[31,26,26,29,21,26,29,0,30,27,28,33],
[27,26,27,24,26,28,20,21,0,20,25,31],
[27,26,29,23,25,27,26,24,31,0,24,33],
[27,27,29,25,28,25,25,23,26,27,0,33],
[27,23,25,23,22,17,18,18,20,18,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 29, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,18,23,15,18,18,21,16,29,18,23],
[24,0,14,23,16,15,16,21,14,24,21,14],
[33,37,0,31,31,28,31,35,24,33,29,28],
[28,28,20,0,15,18,20,24,13,27,25,18],
[36,35,20,36,0,26,20,31,21,28,26,26],
[33,36,23,33,25,0,24,30,26,31,25,21],
[33,35,20,31,31,27,0,32,22,32,28,30],
[30,30,16,27,20,21,19,0,17,23,21,27],
[35,37,27,38,30,25,29,34,0,29,30,27],
[22,27,18,24,23,20,19,28,22,0,18,24],
[33,30,22,26,25,26,23,30,21,33,0,29],
[28,37,23,33,25,30,21,24,24,27,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 30, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,25,26,21,28,22,22,15,24,22,20],
[26,0,27,27,23,27,20,24,19,23,24,20],
[26,24,0,25,22,26,25,24,18,28,22,20],
[25,24,26,0,26,27,27,27,21,25,22,19],
[30,28,29,25,0,27,25,22,25,26,25,26],
[23,24,25,24,24,0,22,16,16,20,24,20],
[29,31,26,24,26,29,0,25,22,25,26,25],
[29,27,27,24,29,35,26,0,21,27,27,22],
[36,32,33,30,26,35,29,30,0,30,27,24],
[27,28,23,26,25,31,26,24,21,0,23,19],
[29,27,29,29,26,27,25,24,24,28,0,22],
[31,31,31,32,25,31,26,29,27,32,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 31, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,22,17,19,21,22,19,19,22,20,26],
[30,0,24,28,31,25,26,27,24,26,27,27],
[29,27,0,25,22,28,29,24,26,23,22,27],
[34,23,26,0,26,26,25,26,21,24,26,26],
[32,20,29,25,0,27,26,29,24,27,24,26],
[30,26,23,25,24,0,29,26,29,23,24,28],
[29,25,22,26,25,22,0,26,23,24,27,26],
[32,24,27,25,22,25,25,0,25,27,27,27],
[32,27,25,30,27,22,28,26,0,23,24,31],
[29,25,28,27,24,28,27,24,28,0,29,30],
[31,24,29,25,27,27,24,24,27,22,0,28],
[25,24,24,25,25,23,25,24,20,21,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 32, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,37,37,47,36,25,40,40,32,28,36,15],
[14,0,29,21,32,22,10,39,21,21,25,7],
[14,22,0,35,32,22,14,43,14,21,28,7],
[4,30,16,0,29,16,8,30,8,15,23,8],
[15,19,19,22,0,23,15,37,15,15,19,26],
[26,29,29,35,28,0,22,29,22,14,32,15],
[11,41,37,43,36,29,0,44,19,28,29,15],
[11,12,8,21,14,22,7,0,18,14,22,15],
[19,30,37,43,36,29,32,33,0,43,44,27],
[23,30,30,36,36,37,23,37,8,0,41,27],
[15,26,23,28,32,19,22,29,7,10,0,11],
[36,44,44,43,25,36,36,36,24,24,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 33, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,29,29,19,23,29,26,24,25,26,27],
[23,0,19,30,26,25,25,23,22,16,26,19],
[22,32,0,32,26,23,26,26,20,23,28,23],
[22,21,19,0,17,21,17,18,17,12,23,18],
[32,25,25,34,0,23,25,25,22,26,23,27],
[28,26,28,30,28,0,29,26,20,23,23,25],
[22,26,25,34,26,22,0,24,21,25,29,28],
[25,28,25,33,26,25,27,0,20,24,26,30],
[27,29,31,34,29,31,30,31,0,22,35,28],
[26,35,28,39,25,28,26,27,29,0,27,25],
[25,25,23,28,28,28,22,25,16,24,0,24],
[24,32,28,33,24,26,23,21,23,26,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 34, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,26,27,23,27,18,22,29,30,23,23],
[30,0,27,33,26,27,26,25,29,27,24,26],
[25,24,0,29,26,32,22,24,28,29,21,25],
[24,18,22,0,27,27,25,25,24,21,25,22],
[28,25,25,24,0,30,18,21,24,22,21,27],
[24,24,19,24,21,0,20,18,24,17,17,25],
[33,25,29,26,33,31,0,28,35,30,26,27],
[29,26,27,26,30,33,23,0,25,23,26,28],
[22,22,23,27,27,27,16,26,0,22,26,21],
[21,24,22,30,29,34,21,28,29,0,22,23],
[28,27,30,26,30,34,25,25,25,29,0,29],
[28,25,26,29,24,26,24,23,30,28,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 35, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,25,34,27,35,23,30,18,22,29,22],
[25,0,17,33,23,30,17,31,19,22,26,21],
[26,34,0,35,29,30,26,29,21,28,30,25],
[17,18,16,0,18,28,16,20,16,20,22,16],
[24,28,22,33,0,28,21,28,23,19,33,23],
[16,21,21,23,23,0,14,25,17,17,24,16],
[28,34,25,35,30,37,0,28,26,30,27,28],
[21,20,22,31,23,26,23,0,19,20,25,20],
[33,32,30,35,28,34,25,32,0,30,30,26],
[29,29,23,31,32,34,21,31,21,0,29,22],
[22,25,21,29,18,27,24,26,21,22,0,16],
[29,30,26,35,28,35,23,31,25,29,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 36, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,24,33,23,23,23,31,21,22,19,35],
[21,0,20,38,27,31,28,27,26,17,26,36],
[27,31,0,27,27,22,26,27,24,17,11,36],
[18,13,24,0,27,17,18,20,21,7,21,28],
[28,24,24,24,0,19,28,25,16,14,13,26],
[28,20,29,34,32,0,23,25,28,22,31,28],
[28,23,25,33,23,28,0,28,16,20,18,40],
[20,24,24,31,26,26,23,0,19,20,17,31],
[30,25,27,30,35,23,35,32,0,22,20,38],
[29,34,34,44,37,29,31,31,29,0,24,35],
[32,25,40,30,38,20,33,34,31,27,0,33],
[16,15,15,23,25,23,11,20,13,16,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 37, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,22,27,31,25,30,28,25,28,21,29],
[19,0,23,19,23,19,23,27,24,21,13,15],
[29,28,0,27,24,28,30,27,22,24,25,21],
[24,32,24,0,24,28,33,20,24,28,21,25],
[20,28,27,27,0,22,31,28,28,32,20,18],
[26,32,23,23,29,0,27,19,24,27,19,27],
[21,28,21,18,20,24,0,19,19,25,18,18],
[23,24,24,31,23,32,32,0,27,28,28,20],
[26,27,29,27,23,27,32,24,0,26,22,19],
[23,30,27,23,19,24,26,23,25,0,13,25],
[30,38,26,30,31,32,33,23,29,38,0,26],
[22,36,30,26,33,24,33,31,32,26,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 38, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,37,27,29,29,25,30,37,38,28,37,28],
[14,0,15,19,20,17,13,21,23,28,23,19],
[24,36,0,27,27,20,28,35,33,32,29,37],
[22,32,24,0,38,31,23,33,34,26,32,30],
[22,31,24,13,0,26,22,25,28,25,24,21],
[26,34,31,20,25,0,22,36,32,29,34,28],
[21,38,23,28,29,29,0,24,30,32,30,35],
[14,30,16,18,26,15,27,0,31,28,20,27],
[13,28,18,17,23,19,21,20,0,23,22,19],
[23,23,19,25,26,22,19,23,28,0,26,29],
[14,28,22,19,27,17,21,31,29,25,0,21],
[23,32,14,21,30,23,16,24,32,22,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 39, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,27,29,28,28,16,37,28,16,22,22],
[29,0,36,36,35,21,23,35,35,22,29,29],
[24,15,0,45,38,24,31,31,31,31,24,31],
[22,15,6,0,28,24,13,21,37,15,22,13],
[23,16,13,23,0,16,14,23,16,9,7,16],
[23,30,27,27,35,0,21,35,22,16,27,28],
[35,28,20,38,37,30,0,35,37,37,22,36],
[14,16,20,30,28,16,16,0,29,9,16,30],
[23,16,20,14,35,29,14,22,0,16,29,14],
[35,29,20,36,42,35,14,42,35,0,29,27],
[29,22,27,29,44,24,29,35,22,22,0,23],
[29,22,20,38,35,23,15,21,37,24,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 40, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,34,29,27,26,36,24,28,34,25,27],
[17,0,25,32,18,23,31,26,20,32,28,23],
[17,26,0,24,17,17,24,19,18,27,19,24],
[22,19,27,0,14,17,27,22,17,24,26,25],
[24,33,34,37,0,32,31,30,25,37,31,30],
[25,28,34,34,19,0,28,32,26,32,29,25],
[15,20,27,24,20,23,0,17,15,29,26,22],
[27,25,32,29,21,19,34,0,25,28,27,30],
[23,31,33,34,26,25,36,26,0,34,29,26],
[17,19,24,27,14,19,22,23,17,0,21,24],
[26,23,32,25,20,22,25,24,22,30,0,23],
[24,28,27,26,21,26,29,21,25,27,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 41, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,13,23,23,16,37,14,21,29,32,20],
[19,0,11,27,21,21,26,14,21,19,21,12],
[38,40,0,25,27,20,38,22,32,25,23,20],
[28,24,26,0,32,22,34,10,16,15,15,13],
[28,30,24,19,0,27,24,13,19,21,18,7],
[35,30,31,29,24,0,38,27,28,29,33,21],
[14,25,13,17,27,13,0,14,19,18,19,18],
[37,37,29,41,38,24,37,0,38,39,33,36],
[30,30,19,35,32,23,32,13,0,31,30,19],
[22,32,26,36,30,22,33,12,20,0,31,18],
[19,30,28,36,33,18,32,18,21,20,0,19],
[31,39,31,38,44,30,33,15,32,33,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 42, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,26,29,22,27,32,19,30,31,23,25],
[24,0,32,27,21,25,22,15,31,23,23,25],
[25,19,0,27,15,27,25,17,30,24,13,19],
[22,24,24,0,15,25,21,19,19,20,22,19],
[29,30,36,36,0,32,28,29,34,29,24,31],
[24,26,24,26,19,0,25,24,33,17,18,24],
[19,29,26,30,23,26,0,23,26,22,21,26],
[32,36,34,32,22,27,28,0,35,25,24,27],
[21,20,21,32,17,18,25,16,0,18,18,19],
[20,28,27,31,22,34,29,26,33,0,27,32],
[28,28,38,29,27,33,30,27,33,24,0,34],
[26,26,32,32,20,27,25,24,32,19,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 43, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,25,26,28,27,29,27,31,23,24,25],
[21,0,22,26,27,28,29,32,33,26,29,23],
[26,29,0,30,30,30,29,28,31,29,32,25],
[25,25,21,0,29,29,29,31,32,28,25,27],
[23,24,21,22,0,21,23,30,25,28,24,23],
[24,23,21,22,30,0,26,27,27,27,29,25],
[22,22,22,22,28,25,0,26,27,22,24,20],
[24,19,23,20,21,24,25,0,28,22,22,20],
[20,18,20,19,26,24,24,23,0,24,23,18],
[28,25,22,23,23,24,29,29,27,0,24,22],
[27,22,19,26,27,22,27,29,28,27,0,22],
[26,28,26,24,28,26,31,31,33,29,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 44, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,26,23,23,18,20,25,22,21,31,23],
[37,0,31,31,24,26,35,27,33,31,32,28],
[25,20,0,29,26,16,22,18,23,20,28,19],
[28,20,22,0,22,22,17,24,20,26,26,14],
[28,27,25,29,0,22,32,29,22,19,29,25],
[33,25,35,29,29,0,31,23,27,30,34,28],
[31,16,29,34,19,20,0,21,23,27,28,19],
[26,24,33,27,22,28,30,0,23,26,31,25],
[29,18,28,31,29,24,28,28,0,25,27,19],
[30,20,31,25,32,21,24,25,26,0,31,21],
[20,19,23,25,22,17,23,20,24,20,0,16],
[28,23,32,37,26,23,32,26,32,30,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 45, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,22,20,27,28,22,28,32,23,19,25],
[17,0,20,19,25,19,19,22,29,26,20,22],
[29,31,0,23,27,24,24,28,22,31,19,26],
[31,32,28,0,35,24,23,28,28,29,27,24],
[24,26,24,16,0,18,20,19,29,23,15,19],
[23,32,27,27,33,0,21,23,32,30,27,26],
[29,32,27,28,31,30,0,27,29,33,24,29],
[23,29,23,23,32,28,24,0,31,28,25,26],
[19,22,29,23,22,19,22,20,0,25,19,22],
[28,25,20,22,28,21,18,23,26,0,21,24],
[32,31,32,24,36,24,27,26,32,30,0,26],
[26,29,25,27,32,25,22,25,29,27,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 46, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,38,21,27,23,27,21,10,27,10,10],
[30,0,51,13,40,13,40,34,23,40,13,23],
[13,0,0,0,17,13,17,11,0,17,0,10],
[30,38,51,0,40,23,40,34,23,40,40,40],
[24,11,34,11,0,13,34,34,24,51,24,10],
[28,38,38,28,38,0,38,21,38,38,38,27],
[24,11,34,11,17,13,0,21,0,27,0,10],
[30,17,40,17,17,30,30,0,17,27,17,27],
[41,28,51,28,27,13,51,34,0,38,28,27],
[24,11,34,11,0,13,24,24,13,0,24,10],
[41,38,51,11,27,13,51,34,23,27,0,10],
[41,28,41,11,41,24,41,24,24,41,41,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 47, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,15,29,19,22,26,19,21,21,24,21],
[32,0,31,23,32,31,40,37,38,17,40,29],
[36,20,0,35,33,40,46,35,39,23,40,35],
[22,28,16,0,25,31,39,28,24,22,28,20],
[32,19,18,26,0,34,47,34,29,12,24,21],
[29,20,11,20,17,0,20,35,37,20,23,26],
[25,11,5,12,4,31,0,20,21,6,18,12],
[32,14,16,23,17,16,31,0,40,8,25,20],
[30,13,12,27,22,14,30,11,0,16,18,25],
[30,34,28,29,39,31,45,43,35,0,40,19],
[27,11,11,23,27,28,33,26,33,11,0,12],
[30,22,16,31,30,25,39,31,26,32,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 48, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,22,30,28,27,22,18,28,28,23,43],
[28,0,25,28,28,25,20,22,33,29,25,38],
[29,26,0,31,33,26,27,30,35,34,15,34],
[21,23,20,0,28,30,9,14,22,28,16,26],
[23,23,18,23,0,23,11,21,19,31,13,32],
[24,26,25,21,28,0,17,21,36,28,24,31],
[29,31,24,42,40,34,0,25,37,33,29,37],
[33,29,21,37,30,30,26,0,19,37,24,32],
[23,18,16,29,32,15,14,32,0,29,9,33],
[23,22,17,23,20,23,18,14,22,0,23,37],
[28,26,36,35,38,27,22,27,42,28,0,39],
[8,13,17,25,19,20,14,19,18,14,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 49, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,30,32,32,25,28,37,18,26,26,33],
[19,0,31,14,3,13,16,25,25,16,16,21],
[21,20,0,20,20,13,22,14,21,20,20,27],
[19,37,31,0,25,24,14,37,31,27,27,27],
[19,48,31,26,0,25,27,37,37,26,28,33],
[26,38,38,27,26,0,21,37,38,21,27,27],
[23,35,29,37,24,30,0,37,29,49,14,31],
[14,26,37,14,14,14,14,0,14,14,8,25],
[33,26,30,20,14,13,22,37,0,32,14,27],
[25,35,31,24,25,30,2,37,19,0,16,27],
[25,35,31,24,23,24,37,43,37,35,0,44],
[18,30,24,24,18,24,20,26,24,24,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 50, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,17,11,9,11,18,21,19,11,14,18],
[31,0,22,13,15,17,23,28,24,21,22,20],
[34,29,0,28,34,27,38,34,35,24,33,20],
[40,38,23,0,18,24,30,29,32,29,27,29],
[42,36,17,33,0,31,37,28,33,20,25,28],
[40,34,24,27,20,0,32,31,33,27,27,29],
[33,28,13,21,14,19,0,20,25,22,24,21],
[30,23,17,22,23,20,31,0,26,19,14,23],
[32,27,16,19,18,18,26,25,0,14,24,17],
[40,30,27,22,31,24,29,32,37,0,30,31],
[37,29,18,24,26,24,27,37,27,21,0,22],
[33,31,31,22,23,22,30,28,34,20,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 51, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,25,29,22,26,31,27,30,25,30,27],
[21,0,26,28,25,27,26,30,30,25,30,26],
[26,25,0,30,24,27,31,27,33,26,27,27],
[22,23,21,0,21,28,23,31,33,18,25,25],
[29,26,27,30,0,27,31,32,33,25,32,30],
[25,24,24,23,24,0,30,27,28,21,30,25],
[20,25,20,28,20,21,0,29,29,19,26,29],
[24,21,24,20,19,24,22,0,27,19,27,20],
[21,21,18,18,18,23,22,24,0,19,21,22],
[26,26,25,33,26,30,32,32,32,0,30,32],
[21,21,24,26,19,21,25,24,30,21,0,22],
[24,25,24,26,21,26,22,31,29,19,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 52, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,26,28,33,27,19,16,29,25,26,28],
[27,0,29,27,38,26,19,23,31,29,27,30],
[25,22,0,19,29,21,20,21,30,21,27,30],
[23,24,32,0,30,21,19,17,28,22,26,30],
[18,13,22,21,0,22,18,18,32,19,22,19],
[24,25,30,30,29,0,20,29,29,25,23,29],
[32,32,31,32,33,31,0,22,32,29,30,33],
[35,28,30,34,33,22,29,0,35,28,32,32],
[22,20,21,23,19,22,19,16,0,25,20,22],
[26,22,30,29,32,26,22,23,26,0,27,28],
[25,24,24,25,29,28,21,19,31,24,0,25],
[23,21,21,21,32,22,18,19,29,23,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 53, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,33,30,26,27,27,25,27,26,29,24],
[22,0,30,23,24,22,25,26,28,19,27,21],
[18,21,0,22,21,19,21,25,21,17,25,21],
[21,28,29,0,26,28,28,25,33,26,27,26],
[25,27,30,25,0,19,20,24,30,24,26,19],
[24,29,32,23,32,0,29,25,30,25,25,26],
[24,26,30,23,31,22,0,27,31,26,26,26],
[26,25,26,26,27,26,24,0,26,22,30,25],
[24,23,30,18,21,21,20,25,0,20,23,21],
[25,32,34,25,27,26,25,29,31,0,28,24],
[22,24,26,24,25,26,25,21,28,23,0,23],
[27,30,30,25,32,25,25,26,30,27,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 54, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,24,23,25,21,23,30,27,24,25,30],
[33,0,27,26,26,30,24,35,27,28,32,30],
[27,24,0,24,21,26,23,30,28,27,25,30],
[28,25,27,0,26,31,28,32,32,28,30,35],
[26,25,30,25,0,35,25,31,30,26,32,32],
[30,21,25,20,16,0,20,28,25,26,23,26],
[28,27,28,23,26,31,0,32,31,26,29,36],
[21,16,21,19,20,23,19,0,25,21,21,26],
[24,24,23,19,21,26,20,26,0,18,21,24],
[27,23,24,23,25,25,25,30,33,0,27,30],
[26,19,26,21,19,28,22,30,30,24,0,28],
[21,21,21,16,19,25,15,25,27,21,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 55, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,24,24,34,23,23,30,31,26,31,20],
[20,0,21,20,31,21,25,23,20,27,26,15],
[27,30,0,28,33,25,31,29,25,27,27,26],
[27,31,23,0,26,26,23,27,26,31,19,25],
[17,20,18,25,0,20,16,22,20,18,27,17],
[28,30,26,25,31,0,27,34,30,32,24,24],
[28,26,20,28,35,24,0,24,25,23,27,22],
[21,28,22,24,29,17,27,0,23,29,22,20],
[20,31,26,25,31,21,26,28,0,31,27,20],
[25,24,24,20,33,19,28,22,20,0,28,20],
[20,25,24,32,24,27,24,29,24,23,0,22],
[31,36,25,26,34,27,29,31,31,31,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 56, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,12,33,17,17,10,31,15,13,23,24],
[27,0,19,38,20,27,25,35,23,14,20,29],
[39,32,0,36,22,35,32,38,38,31,29,29],
[18,13,15,0,23,16,21,24,21,19,18,25],
[34,31,29,28,0,26,35,37,25,27,28,33],
[34,24,16,35,25,0,30,31,29,28,18,33],
[41,26,19,30,16,21,0,33,29,20,26,28],
[20,16,13,27,14,20,18,0,23,22,16,24],
[36,28,13,30,26,22,22,28,0,16,22,23],
[38,37,20,32,24,23,31,29,35,0,26,35],
[28,31,22,33,23,33,25,35,29,25,0,34],
[27,22,22,26,18,18,23,27,28,16,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 57, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,26,20,21,16,26,10,18,21,27,18],
[23,0,29,25,24,18,27,15,19,26,26,13],
[25,22,0,20,30,21,24,16,26,17,32,20],
[31,26,31,0,28,17,34,20,29,31,26,19],
[30,27,21,23,0,29,26,16,21,22,39,24],
[35,33,30,34,22,0,32,29,25,31,28,28],
[25,24,27,17,25,19,0,19,29,33,25,18],
[41,36,35,31,35,22,32,0,33,33,36,18],
[33,32,25,22,30,26,22,18,0,22,29,21],
[30,25,34,20,29,20,18,18,29,0,29,19],
[24,25,19,25,12,23,26,15,22,22,0,20],
[33,38,31,32,27,23,33,33,30,32,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 58, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,35,18,25,29,9,45,38,27,45,29],
[15,0,28,11,31,29,15,40,26,20,33,29],
[16,23,0,14,16,29,11,36,18,18,36,9],
[33,40,37,0,31,29,26,49,44,18,49,27],
[26,20,35,20,0,29,15,40,18,13,31,20],
[22,22,22,22,22,0,9,34,20,17,22,22],
[42,36,40,25,36,42,0,45,31,31,36,20],
[6,11,15,2,11,17,6,0,11,6,2,2],
[13,25,33,7,33,31,20,40,0,13,40,29],
[24,31,33,33,38,34,20,45,38,0,45,29],
[6,18,15,2,20,29,15,49,11,6,0,9],
[22,22,42,24,31,29,31,49,22,22,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 59, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,27,25,34,42,37,17,23,22,19,25],
[23,0,18,15,24,39,11,8,22,23,26,16],
[24,33,0,18,26,45,34,12,22,27,34,24],
[26,36,33,0,33,34,34,35,24,34,30,26],
[17,27,25,18,0,45,22,8,16,17,28,8],
[9,12,6,17,6,0,9,10,7,7,8,2],
[14,40,17,17,29,42,0,11,21,21,25,11],
[34,43,39,16,43,41,40,0,31,30,39,31],
[28,29,29,27,35,44,30,20,0,34,36,20],
[29,28,24,17,34,44,30,21,17,0,42,13],
[32,25,17,21,23,43,26,12,15,9,0,7],
[26,35,27,25,43,49,40,20,31,38,44,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 60, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,22,26,32,25,23,28,28,23,34,26],
[24,0,27,35,31,27,27,28,32,25,33,24],
[29,24,0,24,24,23,18,22,26,24,34,22],
[25,16,27,0,26,22,21,23,26,28,32,24],
[19,20,27,25,0,19,20,24,17,25,28,22],
[26,24,28,29,32,0,25,25,31,32,31,26],
[28,24,33,30,31,26,0,30,23,28,32,32],
[23,23,29,28,27,26,21,0,28,26,34,26],
[23,19,25,25,34,20,28,23,0,29,37,32],
[28,26,27,23,26,19,23,25,22,0,32,24],
[17,18,17,19,23,20,19,17,14,19,0,18],
[25,27,29,27,29,25,19,25,19,27,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 61, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,19,25,28,25,32,17,27,26,31,22],
[18,0,16,21,30,25,28,19,19,18,24,20],
[32,35,0,27,35,37,30,23,29,30,27,32],
[26,30,24,0,38,30,29,27,22,22,27,26],
[23,21,16,13,0,25,22,14,14,17,20,20],
[26,26,14,21,26,0,29,17,22,16,23,21],
[19,23,21,22,29,22,0,20,16,21,20,20],
[34,32,28,24,37,34,31,0,28,29,28,29],
[24,32,22,29,37,29,35,23,0,20,25,27],
[25,33,21,29,34,35,30,22,31,0,25,28],
[20,27,24,24,31,28,31,23,26,26,0,24],
[29,31,19,25,31,30,31,22,24,23,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 62, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,20,9,3,22,10,14,20,15,7,22],
[48,0,29,19,28,30,31,19,38,37,24,32],
[31,22,0,21,22,38,14,24,28,23,13,28],
[42,32,30,0,30,29,31,33,27,34,24,32],
[48,23,29,21,0,32,14,21,40,20,24,32],
[29,21,13,22,19,0,12,22,10,21,13,21],
[41,20,37,20,37,39,0,20,31,28,30,39],
[37,32,27,18,30,29,31,0,27,31,34,32],
[31,13,23,24,11,41,20,24,0,23,13,21],
[36,14,28,17,31,30,23,20,28,0,35,33],
[44,27,38,27,27,38,21,17,38,16,0,49],
[29,19,23,19,19,30,12,19,30,18,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 63, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,30,30,30,24,24,36,17,28,29,30],
[40,0,41,26,39,39,25,42,33,38,32,29],
[21,10,0,20,27,20,19,22,21,25,25,23],
[21,25,31,0,26,17,32,35,11,31,16,14],
[21,12,24,25,0,24,22,34,18,21,22,20],
[27,12,31,34,27,0,28,40,20,27,18,33],
[27,26,32,19,29,23,0,42,17,34,22,20],
[15,9,29,16,17,11,9,0,11,28,16,11],
[34,18,30,40,33,31,34,40,0,40,25,25],
[23,13,26,20,30,24,17,23,11,0,22,20],
[22,19,26,35,29,33,29,35,26,29,0,29],
[21,22,28,37,31,18,31,40,26,31,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 64, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,25,25,46,9,39,16,25,23,30,39],
[21,0,30,30,37,23,30,30,14,14,35,30],
[26,21,0,14,30,30,39,30,23,28,44,28],
[26,21,37,0,35,35,44,35,28,28,30,28],
[5,14,21,16,0,14,35,21,5,5,30,5],
[42,28,21,16,37,0,35,21,30,19,21,35],
[12,21,12,7,16,16,0,16,16,12,37,12],
[35,21,21,16,30,30,35,0,21,35,21,35],
[26,37,28,23,46,21,35,30,0,19,30,35],
[28,37,23,23,46,32,39,16,32,0,37,37],
[21,16,7,21,21,30,14,30,21,14,0,21],
[12,21,23,23,46,16,39,16,16,14,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 65, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,17,34,30,23,7,38,0,30,21,16],
[44,0,17,36,36,31,37,38,22,44,31,17],
[34,34,0,34,34,27,20,21,34,43,21,34],
[17,15,17,0,31,31,15,24,8,31,38,24],
[21,15,17,20,0,8,28,24,8,37,29,24],
[28,20,24,20,43,0,28,24,28,51,21,29],
[44,14,31,36,23,23,0,38,22,44,23,23],
[13,13,30,27,27,27,13,0,13,36,27,22],
[51,29,17,43,43,23,29,38,0,43,30,16],
[21,7,8,20,14,0,7,15,8,0,21,7],
[30,20,30,13,22,30,28,24,21,30,0,30],
[35,34,17,27,27,22,28,29,35,44,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 66, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,30,21,16,21,14,19,35,19,21,19],
[51,0,51,35,35,51,14,19,35,35,51,35],
[21,0,0,21,16,21,14,5,5,5,5,5],
[30,16,30,0,16,21,30,35,35,35,21,35],
[35,16,35,35,0,35,30,35,35,35,21,35],
[30,0,30,30,16,0,14,19,35,19,21,19],
[37,37,37,21,21,37,0,37,37,37,37,37],
[32,32,46,16,16,32,14,0,51,37,32,51],
[16,16,46,16,16,16,14,0,0,21,32,35],
[32,16,46,16,16,32,14,14,30,0,16,51],
[30,0,46,30,30,30,14,19,19,35,0,35],
[32,16,46,16,16,32,14,0,16,0,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 67, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,17,23,18,24,29,23,28,28,29,19],
[25,0,14,16,23,16,23,23,32,23,26,25],
[34,37,0,30,22,22,34,24,36,28,24,32],
[28,35,21,0,29,24,34,26,36,35,32,35],
[33,28,29,22,0,29,33,29,21,23,25,25],
[27,35,29,27,22,0,37,30,40,34,29,31],
[22,28,17,17,18,14,0,20,27,28,23,25],
[28,28,27,25,22,21,31,0,34,28,23,23],
[23,19,15,15,30,11,24,17,0,24,29,14],
[23,28,23,16,28,17,23,23,27,0,27,19],
[22,25,27,19,26,22,28,28,22,24,0,20],
[32,26,19,16,26,20,26,28,37,32,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 68, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,23,23,46,51,24,42,23,46,32,42],
[19,0,23,19,42,42,19,19,19,46,23,42],
[28,28,0,23,23,51,28,28,23,23,51,46],
[28,32,28,0,28,47,5,28,24,27,28,23],
[5,9,28,23,0,47,24,5,19,46,28,23],
[0,9,0,4,4,0,0,0,4,4,0,0],
[27,32,23,46,27,51,0,27,46,27,32,27],
[9,32,23,23,46,51,24,0,23,46,32,27],
[28,32,28,27,32,47,5,28,0,27,28,23],
[5,5,28,24,5,47,24,5,24,0,28,23],
[19,28,0,23,23,51,19,19,23,23,0,42],
[9,9,5,28,28,51,24,24,28,28,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 69, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,22,20,23,22,24,22,20,22,16,18],
[35,0,29,30,27,30,32,26,29,28,26,24],
[29,22,0,26,27,25,26,29,25,30,21,21],
[31,21,25,0,23,24,22,28,24,28,22,21],
[28,24,24,28,0,27,28,31,30,25,21,23],
[29,21,26,27,24,0,30,23,28,26,22,27],
[27,19,25,29,23,21,0,25,21,21,18,19],
[29,25,22,23,20,28,26,0,23,24,22,21],
[31,22,26,27,21,23,30,28,0,29,21,19],
[29,23,21,23,26,25,30,27,22,0,23,20],
[35,25,30,29,30,29,33,29,30,28,0,25],
[33,27,30,30,28,24,32,30,32,31,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 70, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,22,27,11,15,12,31,18,30,29,41],
[11,0,8,15,4,8,10,16,19,23,17,15],
[29,43,0,34,10,23,14,33,24,37,42,37],
[24,36,17,0,7,22,17,24,20,28,31,29],
[40,47,41,44,0,31,34,43,23,44,50,33],
[36,43,28,29,20,0,32,32,20,31,46,41],
[39,41,37,34,17,19,0,37,30,33,37,43],
[20,35,18,27,8,19,14,0,24,26,29,21],
[33,32,27,31,28,31,21,27,0,31,35,27],
[21,28,14,23,7,20,18,25,20,0,31,18],
[22,34,9,20,1,5,14,22,16,20,0,30],
[10,36,14,22,18,10,8,30,24,33,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 71, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,22,15,12,19,24,22,29,24,15,12],
[32,0,38,20,27,24,28,30,41,26,26,34],
[29,13,0,23,19,19,20,22,31,16,18,23],
[36,31,28,0,26,18,28,26,39,26,17,32],
[39,24,32,25,0,22,27,24,37,32,32,30],
[32,27,32,33,29,0,27,30,30,29,23,27],
[27,23,31,23,24,24,0,17,28,29,29,27],
[29,21,29,25,27,21,34,0,37,31,24,29],
[22,10,20,12,14,21,23,14,0,12,14,19],
[27,25,35,25,19,22,22,20,39,0,15,25],
[36,25,33,34,19,28,22,27,37,36,0,27],
[39,17,28,19,21,24,24,22,32,26,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 72, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,25,20,19,22,22,25,20,25,25,29],
[26,0,32,26,23,28,23,25,24,29,33,36],
[26,19,0,23,20,18,20,25,20,24,26,27],
[31,25,28,0,26,31,26,23,27,32,30,35],
[32,28,31,25,0,31,24,25,29,36,34,32],
[29,23,33,20,20,0,23,28,26,28,33,25],
[29,28,31,25,27,28,0,28,30,26,30,31],
[26,26,26,28,26,23,23,0,30,26,35,31],
[31,27,31,24,22,25,21,21,0,26,32,27],
[26,22,27,19,15,23,25,25,25,0,34,30],
[26,18,25,21,17,18,21,16,19,17,0,22],
[22,15,24,16,19,26,20,20,24,21,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 73, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,25,31,39,26,30,36,41,29,36,23],
[21,0,27,30,38,20,29,31,31,37,28,31],
[26,24,0,34,38,26,24,38,38,38,37,29],
[20,21,17,0,28,17,20,25,26,29,30,19],
[12,13,13,23,0,12,25,22,24,21,24,11],
[25,31,25,34,39,0,29,27,33,30,38,20],
[21,22,27,31,26,22,0,30,24,31,22,20],
[15,20,13,26,29,24,21,0,22,27,25,16],
[10,20,13,25,27,18,27,29,0,31,28,24],
[22,14,13,22,30,21,20,24,20,0,23,26],
[15,23,14,21,27,13,29,26,23,28,0,20],
[28,20,22,32,40,31,31,35,27,25,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 74, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,28,23,24,25,27,34,28,27,31,30],
[18,0,21,20,20,25,19,30,24,18,24,28],
[23,30,0,24,26,23,25,27,29,29,23,29],
[28,31,27,0,27,31,23,31,31,21,25,31],
[27,31,25,24,0,31,28,32,28,28,26,29],
[26,26,28,20,20,0,27,24,26,20,23,20],
[24,32,26,28,23,24,0,32,28,31,34,30],
[17,21,24,20,19,27,19,0,22,21,18,23],
[23,27,22,20,23,25,23,29,0,23,22,25],
[24,33,22,30,23,31,20,30,28,0,27,31],
[20,27,28,26,25,28,17,33,29,24,0,26],
[21,23,22,20,22,31,21,28,26,20,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 75, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,16,21,26,25,22,23,27,26,29,22],
[25,0,25,23,31,25,22,33,30,22,32,24],
[35,26,0,23,31,29,29,33,32,34,36,36],
[30,28,28,0,28,28,25,31,26,33,33,27],
[25,20,20,23,0,26,18,24,22,23,34,24],
[26,26,22,23,25,0,20,30,19,28,29,27],
[29,29,22,26,33,31,0,31,34,28,35,32],
[28,18,18,20,27,21,20,0,24,23,26,16],
[24,21,19,25,29,32,17,27,0,22,33,26],
[25,29,17,18,28,23,23,28,29,0,32,28],
[22,19,15,18,17,22,16,25,18,19,0,21],
[29,27,15,24,27,24,19,35,25,23,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 76, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,28,25,28,32,28,28,26,29,30,23],
[22,0,24,22,23,29,27,28,27,22,29,23],
[23,27,0,25,24,27,25,25,23,19,25,21],
[26,29,26,0,27,28,25,29,25,26,28,21],
[23,28,27,24,0,30,28,27,28,27,30,28],
[19,22,24,23,21,0,26,26,26,21,28,23],
[23,24,26,26,23,25,0,26,26,26,22,24],
[23,23,26,22,24,25,25,0,26,26,28,22],
[25,24,28,26,23,25,25,25,0,22,28,24],
[22,29,32,25,24,30,25,25,29,0,29,24],
[21,22,26,23,21,23,29,23,23,22,0,21],
[28,28,30,30,23,28,27,29,27,27,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 77, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,22,34,21,28,26,31,19,27,26,22],
[29,0,33,32,25,35,23,25,27,26,20,21],
[29,18,0,31,31,26,23,21,27,30,19,20],
[17,19,20,0,22,20,21,25,15,20,18,20],
[30,26,20,29,0,23,25,22,16,25,19,19],
[23,16,25,31,28,0,26,31,23,23,23,28],
[25,28,28,30,26,25,0,30,23,29,21,20],
[20,26,30,26,29,20,21,0,16,27,21,24],
[32,24,24,36,35,28,28,35,0,28,26,22],
[24,25,21,31,26,28,22,24,23,0,12,26],
[25,31,32,33,32,28,30,30,25,39,0,33],
[29,30,31,31,32,23,31,27,29,25,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 78, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,25,40,32,28,47,40,28,36,35,40],
[16,0,25,33,27,29,28,20,16,29,27,25],
[26,26,0,33,28,24,38,18,26,31,31,31],
[11,18,18,0,19,21,35,30,14,19,29,14],
[19,24,23,32,0,25,28,32,21,28,34,20],
[23,22,27,30,26,0,38,37,24,29,34,26],
[4,23,13,16,23,13,0,25,13,13,27,16],
[11,31,33,21,19,14,26,0,25,25,22,17],
[23,35,25,37,30,27,38,26,0,36,35,29],
[15,22,20,32,23,22,38,26,15,0,33,35],
[16,24,20,22,17,17,24,29,16,18,0,18],
[11,26,20,37,31,25,35,34,22,16,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 79, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,25,26,31,29,29,27,24,26,24,23],
[26,0,26,26,27,27,25,28,27,28,27,28],
[26,25,0,25,31,27,24,32,21,25,19,24],
[25,25,26,0,32,28,31,33,26,26,24,26],
[20,24,20,19,0,23,20,29,23,26,21,24],
[22,24,24,23,28,0,27,30,24,21,17,25],
[22,26,27,20,31,24,0,27,23,25,23,19],
[24,23,19,18,22,21,24,0,19,24,15,23],
[27,24,30,25,28,27,28,32,0,27,26,29],
[25,23,26,25,25,30,26,27,24,0,19,31],
[27,24,32,27,30,34,28,36,25,32,0,32],
[28,23,27,25,27,26,32,28,22,20,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 80, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,22,21,25,19,29,20,29,26,28,23],
[27,0,23,21,27,23,35,23,28,25,28,29],
[29,28,0,22,25,25,27,34,33,28,35,25],
[30,30,29,0,27,27,32,33,28,25,35,28],
[26,24,26,24,0,29,31,27,31,25,36,32],
[32,28,26,24,22,0,35,31,38,28,35,27],
[22,16,24,19,20,16,0,25,31,19,30,25],
[31,28,17,18,24,20,26,0,30,27,31,28],
[22,23,18,23,20,13,20,21,0,21,23,24],
[25,26,23,26,26,23,32,24,30,0,28,29],
[23,23,16,16,15,16,21,20,28,23,0,27],
[28,22,26,23,19,24,26,23,27,22,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 81, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,27,25,24,26,27,22,22,27,29,24],
[32,0,26,31,26,26,24,22,25,23,28,26],
[24,25,0,28,16,23,30,27,23,19,24,26],
[26,20,23,0,22,25,27,18,22,23,20,24],
[27,25,35,29,0,26,35,24,20,25,27,29],
[25,25,28,26,25,0,30,31,25,25,28,30],
[24,27,21,24,16,21,0,23,27,23,23,25],
[29,29,24,33,27,20,28,0,28,30,28,30],
[29,26,28,29,31,26,24,23,0,33,24,26],
[24,28,32,28,26,26,28,21,18,0,27,24],
[22,23,27,31,24,23,28,23,27,24,0,23],
[27,25,25,27,22,21,26,21,25,27,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 82, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,26,20,28,23,20,18,13,20,21,22],
[21,0,18,17,18,19,14,14,10,18,11,12],
[25,33,0,24,24,24,21,15,21,24,20,13],
[31,34,27,0,20,32,26,22,27,26,16,17],
[23,33,27,31,0,21,27,20,28,23,19,18],
[28,32,27,19,30,0,27,24,17,22,22,22],
[31,37,30,25,24,24,0,20,15,26,28,21],
[33,37,36,29,31,27,31,0,30,24,25,26],
[38,41,30,24,23,34,36,21,0,31,26,29],
[31,33,27,25,28,29,25,27,20,0,27,29],
[30,40,31,35,32,29,23,26,25,24,0,29],
[29,39,38,34,33,29,30,25,22,22,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 83, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,19,25,19,18,23,17,24,23,20,28],
[37,0,19,30,25,31,29,27,31,28,25,26],
[32,32,0,29,32,28,32,25,33,34,27,33],
[26,21,22,0,24,20,27,20,23,25,20,24],
[32,26,19,27,0,27,28,16,29,34,24,32],
[33,20,23,31,24,0,32,25,22,26,26,28],
[28,22,19,24,23,19,0,23,23,29,18,30],
[34,24,26,31,35,26,28,0,26,33,20,28],
[27,20,18,28,22,29,28,25,0,27,22,26],
[28,23,17,26,17,25,22,18,24,0,19,20],
[31,26,24,31,27,25,33,31,29,32,0,27],
[23,25,18,27,19,23,21,23,25,31,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 84, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,23,25,22,21,35,31,26,24,26,23],
[29,0,29,27,20,26,25,23,23,26,16,14],
[28,22,0,26,24,25,28,23,28,30,26,20],
[26,24,25,0,19,34,26,21,30,23,19,16],
[29,31,27,32,0,33,37,23,32,22,22,16],
[30,25,26,17,18,0,29,23,24,21,13,16],
[16,26,23,25,14,22,0,21,19,20,14,14],
[20,28,28,30,28,28,30,0,28,31,23,24],
[25,28,23,21,19,27,32,23,0,24,20,19],
[27,25,21,28,29,30,31,20,27,0,19,20],
[25,35,25,32,29,38,37,28,31,32,0,27],
[28,37,31,35,35,35,37,27,32,31,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 85, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,26,31,32,29,23,27,29,22,32,21],
[29,0,28,29,33,33,23,39,28,28,26,24],
[25,23,0,28,37,27,28,41,33,27,27,25],
[20,22,23,0,20,26,23,29,21,21,17,15],
[19,18,14,31,0,34,17,32,33,21,25,26],
[22,18,24,25,17,0,26,35,28,25,28,26],
[28,28,23,28,34,25,0,37,28,29,29,26],
[24,12,10,22,19,16,14,0,19,21,25,15],
[22,23,18,30,18,23,23,32,0,24,19,19],
[29,23,24,30,30,26,22,30,27,0,19,25],
[19,25,24,34,26,23,22,26,32,32,0,23],
[30,27,26,36,25,25,25,36,32,26,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 86, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,26,27,22,22,29,29,21,32,23,28],
[26,0,27,27,25,27,29,33,30,36,24,34],
[25,24,0,29,20,23,29,33,24,31,29,28],
[24,24,22,0,23,21,29,28,22,31,29,27],
[29,26,31,28,0,22,30,31,24,31,30,29],
[29,24,28,30,29,0,30,34,27,33,27,29],
[22,22,22,22,21,21,0,23,20,27,23,25],
[22,18,18,23,20,17,28,0,17,22,24,26],
[30,21,27,29,27,24,31,34,0,34,25,29],
[19,15,20,20,20,18,24,29,17,0,17,21],
[28,27,22,22,21,24,28,27,26,34,0,28],
[23,17,23,24,22,22,26,25,22,30,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 87, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,29,30,28,32,28,29,31,30,28,22],
[22,0,26,23,24,23,27,25,25,32,27,31],
[22,25,0,23,29,22,22,22,29,27,28,24],
[21,28,28,0,30,28,31,23,26,28,31,25],
[23,27,22,21,0,27,25,25,25,29,24,24],
[19,28,29,23,24,0,23,26,26,33,29,28],
[23,24,29,20,26,28,0,26,29,30,28,24],
[22,26,29,28,26,25,25,0,23,22,24,18],
[20,26,22,25,26,25,22,28,0,26,27,28],
[21,19,24,23,22,18,21,29,25,0,22,20],
[23,24,23,20,27,22,23,27,24,29,0,18],
[29,20,27,26,27,23,27,33,23,31,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 88, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,27,29,30,22,21,29,27,24,22,17],
[28,0,33,32,34,26,25,31,26,23,28,26],
[24,18,0,29,31,25,24,29,22,21,22,21],
[22,19,22,0,29,18,20,28,20,24,18,19],
[21,17,20,22,0,21,21,21,19,21,23,19],
[29,25,26,33,30,0,29,34,25,26,27,31],
[30,26,27,31,30,22,0,29,29,27,24,23],
[22,20,22,23,30,17,22,0,19,25,22,21],
[24,25,29,31,32,26,22,32,0,26,22,28],
[27,28,30,27,30,25,24,26,25,0,21,25],
[29,23,29,33,28,24,27,29,29,30,0,27],
[34,25,30,32,32,20,28,30,23,26,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 89, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,25,22,19,21,25,25,21,22,24,22],
[27,0,32,30,25,29,26,27,27,24,23,24],
[26,19,0,22,27,24,24,28,17,20,22,21],
[29,21,29,0,23,28,24,28,21,18,26,22],
[32,26,24,28,0,28,21,31,24,29,29,25],
[30,22,27,23,23,0,22,27,23,15,24,17],
[26,25,27,27,30,29,0,28,22,29,31,27],
[26,24,23,23,20,24,23,0,25,19,27,22],
[30,24,34,30,27,28,29,26,0,21,30,21],
[29,27,31,33,22,36,22,32,30,0,33,26],
[27,28,29,25,22,27,20,24,21,18,0,21],
[29,27,30,29,26,34,24,29,30,25,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 90, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,27,31,26,28,27,29,25,25,29,26],
[26,0,25,32,29,22,22,27,27,26,28,23],
[24,26,0,33,25,24,27,29,28,27,28,24],
[20,19,18,0,20,22,19,20,19,24,21,16],
[25,22,26,31,0,27,26,27,24,27,28,25],
[23,29,27,29,24,0,23,28,28,25,29,21],
[24,29,24,32,25,28,0,29,22,23,22,18],
[22,24,22,31,24,23,22,0,25,23,25,26],
[26,24,23,32,27,23,29,26,0,29,25,24],
[26,25,24,27,24,26,28,28,22,0,28,24],
[22,23,23,30,23,22,29,26,26,23,0,22],
[25,28,27,35,26,30,33,25,27,27,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 91, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,37,17,38,37,36,25,37,28,11,36],
[21,0,34,16,33,28,33,11,12,15,26,21],
[14,17,0,24,15,24,16,13,18,15,17,27],
[34,35,27,0,35,33,34,33,35,37,24,35],
[13,18,36,16,0,38,26,15,17,10,6,28],
[14,23,27,18,13,0,28,8,7,8,12,5],
[15,18,35,17,25,23,0,11,14,20,9,17],
[26,40,38,18,36,43,40,0,18,18,17,30],
[14,39,33,16,34,44,37,33,0,15,18,37],
[23,36,36,14,41,43,31,33,36,0,15,37],
[40,25,34,27,45,39,42,34,33,36,0,42],
[15,30,24,16,23,46,34,21,14,14,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 92, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,28,27,24,35,26,24,22,30,24,28],
[28,0,21,28,29,35,29,27,28,38,28,33],
[23,30,0,33,29,32,31,29,31,34,30,33],
[24,23,18,0,26,35,26,22,23,35,23,29],
[27,22,22,25,0,33,26,24,25,33,26,29],
[16,16,19,16,18,0,20,19,20,29,23,20],
[25,22,20,25,25,31,0,21,29,33,25,31],
[27,24,22,29,27,32,30,0,21,34,32,28],
[29,23,20,28,26,31,22,30,0,33,29,28],
[21,13,17,16,18,22,18,17,18,0,19,12],
[27,23,21,28,25,28,26,19,22,32,0,25],
[23,18,18,22,22,31,20,23,23,39,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 93, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,24,32,26,21,25,18,29,28,16,24],
[30,0,30,29,34,24,29,27,30,27,25,27],
[27,21,0,27,24,25,22,26,29,27,26,24],
[19,22,24,0,21,17,23,20,28,26,21,19],
[25,17,27,30,0,19,20,18,30,24,21,21],
[30,27,26,34,32,0,27,24,32,28,26,28],
[26,22,29,28,31,24,0,26,25,28,23,21],
[33,24,25,31,33,27,25,0,29,26,27,19],
[22,21,22,23,21,19,26,22,0,27,21,21],
[23,24,24,25,27,23,23,25,24,0,26,22],
[35,26,25,30,30,25,28,24,30,25,0,25],
[27,24,27,32,30,23,30,32,30,29,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 94, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,2,27,13,28,27,13,25,16,13,4],
[33,0,10,37,21,22,35,23,35,14,21,10],
[49,41,0,37,23,41,37,39,35,41,35,14],
[24,14,14,0,25,26,49,35,25,16,25,24],
[38,30,28,26,0,30,26,51,14,30,23,26],
[23,29,10,25,21,0,25,25,35,15,21,12],
[24,16,14,2,25,26,0,25,25,18,11,2],
[38,28,12,16,0,26,26,0,14,16,12,12],
[26,16,16,26,37,16,26,37,0,16,27,26],
[35,37,10,35,21,36,33,35,35,0,21,10],
[38,30,16,26,28,30,40,39,24,30,0,28],
[47,41,37,27,25,39,49,39,25,41,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 95, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,23,25,24,27,27,22,22,23,23,32],
[31,0,27,28,34,29,29,29,25,31,26,39],
[28,24,0,26,29,28,29,26,28,31,27,31],
[26,23,25,0,29,26,25,24,29,26,23,33],
[27,17,22,22,0,27,22,21,24,24,21,30],
[24,22,23,25,24,0,24,24,25,20,25,27],
[24,22,22,26,29,27,0,25,27,24,26,31],
[29,22,25,27,30,27,26,0,22,24,28,28],
[29,26,23,22,27,26,24,29,0,25,23,37],
[28,20,20,25,27,31,27,27,26,0,27,33],
[28,25,24,28,30,26,25,23,28,24,0,31],
[19,12,20,18,21,24,20,23,14,18,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 96, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,20,21,31,29,34,32,35,27,22,29],
[29,0,27,26,37,30,39,26,33,29,32,25],
[31,24,0,32,37,31,34,26,34,29,30,28],
[30,25,19,0,31,32,28,28,25,24,25,25],
[20,14,14,20,0,21,23,17,25,20,22,20],
[22,21,20,19,30,0,27,17,27,21,26,20],
[17,12,17,23,28,24,0,19,26,26,25,18],
[19,25,25,23,34,34,32,0,32,24,25,25],
[16,18,17,26,26,24,25,19,0,24,27,22],
[24,22,22,27,31,30,25,27,27,0,25,24],
[29,19,21,26,29,25,26,26,24,26,0,18],
[22,26,23,26,31,31,33,26,29,27,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 97, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,27,38,25,32,23,38,38,29,30,35],
[21,0,23,27,27,28,31,40,35,31,24,39],
[24,28,0,36,31,28,19,45,28,23,18,29],
[13,24,15,0,13,28,26,46,18,28,13,38],
[26,24,20,38,0,27,23,33,39,35,28,31],
[19,23,23,23,24,0,27,30,33,31,26,34],
[28,20,32,25,28,24,0,37,25,29,24,34],
[13,11,6,5,18,21,14,0,21,16,18,26],
[13,16,23,33,12,18,26,30,0,26,11,22],
[22,20,28,23,16,20,22,35,25,0,24,31],
[21,27,33,38,23,25,27,33,40,27,0,31],
[16,12,22,13,20,17,17,25,29,20,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 98, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,22,27,26,26,25,25,22,26,29,22],
[25,0,25,26,27,26,26,31,26,23,30,27],
[29,26,0,27,28,23,25,29,26,28,28,31],
[24,25,24,0,25,27,26,28,26,26,24,21],
[25,24,23,26,0,25,21,26,25,25,29,24],
[25,25,28,24,26,0,25,29,23,29,30,30],
[26,25,26,25,30,26,0,29,26,27,28,26],
[26,20,22,23,25,22,22,0,22,25,22,23],
[29,25,25,25,26,28,25,29,0,25,27,26],
[25,28,23,25,26,22,24,26,26,0,26,24],
[22,21,23,27,22,21,23,29,24,25,0,24],
[29,24,20,30,27,21,25,28,25,27,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 99, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,20,24,24,25,26,23,25,25,27,23],
[27,0,24,25,28,21,29,24,28,20,24,23],
[31,27,0,27,36,23,32,31,32,34,30,33],
[27,26,24,0,38,25,35,32,33,27,32,29],
[27,23,15,13,0,15,26,19,29,18,23,19],
[26,30,28,26,36,0,28,25,26,25,30,25],
[25,22,19,16,25,23,0,14,25,22,18,19],
[28,27,20,19,32,26,37,0,26,20,23,27],
[26,23,19,18,22,25,26,25,0,20,26,22],
[26,31,17,24,33,26,29,31,31,0,32,28],
[24,27,21,19,28,21,33,28,25,19,0,20],
[28,28,18,22,32,26,32,24,29,23,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 100, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,28,23,33,30,23,30,29,34,24,27],
[24,0,28,18,31,22,21,25,24,34,27,22],
[23,23,0,28,31,22,23,23,19,28,23,21],
[28,33,23,0,28,28,26,27,28,31,32,25],
[18,20,20,23,0,24,23,26,20,27,19,21],
[21,29,29,23,27,0,21,25,23,31,23,19],
[28,30,28,25,28,30,0,26,30,27,26,22],
[21,26,28,24,25,26,25,0,24,31,21,18],
[22,27,32,23,31,28,21,27,0,31,24,17],
[17,17,23,20,24,20,24,20,20,0,18,23],
[27,24,28,19,32,28,25,30,27,33,0,25],
[24,29,30,26,30,32,29,33,34,28,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 101, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,28,30,26,22,23,24,24,29,22,25],
[25,0,26,40,30,31,29,30,30,38,30,28],
[23,25,0,28,22,25,18,19,17,29,21,26],
[21,11,23,0,25,24,15,24,20,25,16,20],
[25,21,29,26,0,22,21,19,19,25,16,27],
[29,20,26,27,29,0,18,20,26,25,18,25],
[28,22,33,36,30,33,0,25,25,30,22,33],
[27,21,32,27,32,31,26,0,27,29,23,29],
[27,21,34,31,32,25,26,24,0,28,26,32],
[22,13,22,26,26,26,21,22,23,0,19,24],
[29,21,30,35,35,33,29,28,25,32,0,28],
[26,23,25,31,24,26,18,22,19,27,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 102, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,26,29,30,30,34,31,29,20,29,27],
[30,0,20,23,24,27,35,28,29,22,27,30],
[25,31,0,28,30,22,30,30,19,34,28,29],
[22,28,23,0,28,28,25,31,34,25,23,27],
[21,27,21,23,0,22,28,27,27,29,22,32],
[21,24,29,23,29,0,30,20,22,31,25,26],
[17,16,21,26,23,21,0,23,17,21,20,20],
[20,23,21,20,24,31,28,0,22,20,26,22],
[22,22,32,17,24,29,34,29,0,28,22,24],
[31,29,17,26,22,20,30,31,23,0,27,28],
[22,24,23,28,29,26,31,25,29,24,0,25],
[24,21,22,24,19,25,31,29,27,23,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 103, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,36,39,34,35,32,31,24,25,34,38],
[24,0,28,26,29,27,26,34,22,27,30,26],
[15,23,0,24,30,22,20,25,19,26,22,22],
[12,25,27,0,17,16,21,24,11,28,20,17],
[17,22,21,34,0,15,21,24,19,12,19,16],
[16,24,29,35,36,0,27,25,27,30,17,24],
[19,25,31,30,30,24,0,34,20,26,23,28],
[20,17,26,27,27,26,17,0,12,20,25,22],
[27,29,32,40,32,24,31,39,0,24,31,32],
[26,24,25,23,39,21,25,31,27,0,34,28],
[17,21,29,31,32,34,28,26,20,17,0,24],
[13,25,29,34,35,27,23,29,19,23,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 104, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,24,26,19,25,21,29,21,22,22,24],
[24,0,17,21,25,24,21,25,15,15,23,19],
[27,34,0,29,25,39,34,36,29,32,33,24],
[25,30,22,0,21,20,26,30,22,19,26,21],
[32,26,26,30,0,31,30,34,26,25,28,30],
[26,27,12,31,20,0,26,28,24,15,27,21],
[30,30,17,25,21,25,0,33,26,22,34,20],
[22,26,15,21,17,23,18,0,15,16,27,17],
[30,36,22,29,25,27,25,36,0,23,37,26],
[29,36,19,32,26,36,29,35,28,0,36,21],
[29,28,18,25,23,24,17,24,14,15,0,8],
[27,32,27,30,21,30,31,34,25,30,43,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 105, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,23,23,18,24,22,24,20,27,18,19],
[32,0,32,25,19,35,24,29,21,30,22,25],
[28,19,0,30,21,29,22,32,24,30,20,25],
[28,26,21,0,21,30,20,24,20,25,22,30],
[33,32,30,30,0,37,29,32,29,37,25,29],
[27,16,22,21,14,0,20,22,21,23,20,20],
[29,27,29,31,22,31,0,33,28,35,29,27],
[27,22,19,27,19,29,18,0,23,24,19,24],
[31,30,27,31,22,30,23,28,0,28,28,30],
[24,21,21,26,14,28,16,27,23,0,19,21],
[33,29,31,29,26,31,22,32,23,32,0,29],
[32,26,26,21,22,31,24,27,21,30,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 106, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,18,17,9,17,20,12,22,11,17,22],
[28,0,21,11,12,21,33,21,34,24,29,24],
[33,30,0,31,22,28,43,34,29,21,24,32],
[34,40,20,0,17,37,42,31,26,25,23,33],
[42,39,29,34,0,34,27,27,41,24,28,38],
[34,30,23,14,17,0,43,32,25,25,13,34],
[31,18,8,9,24,8,0,7,31,7,18,17],
[39,30,17,20,24,19,44,0,28,24,11,32],
[29,17,22,25,10,26,20,23,0,16,11,16],
[40,27,30,26,27,26,44,27,35,0,23,27],
[34,22,27,28,23,38,33,40,40,28,0,32],
[29,27,19,18,13,17,34,19,35,24,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 107, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,29,23,30,26,40,21,27,24,21,24],
[21,0,23,19,25,25,41,24,19,31,22,28],
[22,28,0,11,27,31,38,28,31,31,22,18],
[28,32,40,0,42,33,42,34,32,40,34,25],
[21,26,24,9,0,23,32,25,29,30,18,16],
[25,26,20,18,28,0,36,13,25,28,14,21],
[11,10,13,9,19,15,0,24,20,18,25,10],
[30,27,23,17,26,38,27,0,26,34,17,19],
[24,32,20,19,22,26,31,25,0,29,18,25],
[27,20,20,11,21,23,33,17,22,0,21,20],
[30,29,29,17,33,37,26,34,33,30,0,28],
[27,23,33,26,35,30,41,32,26,31,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 108, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,26,18,22,22,24,24,28,26,23,29],
[24,0,30,26,27,26,24,28,32,26,29,31],
[25,21,0,24,19,17,22,21,28,26,21,27],
[33,25,27,0,27,31,26,26,30,32,29,34],
[29,24,32,24,0,25,24,24,29,28,27,28],
[29,25,34,20,26,0,22,25,28,23,24,31],
[27,27,29,25,27,29,0,26,31,30,27,31],
[27,23,30,25,27,26,25,0,29,30,28,30],
[23,19,23,21,22,23,20,22,0,21,25,24],
[25,25,25,19,23,28,21,21,30,0,28,30],
[28,22,30,22,24,27,24,23,26,23,0,33],
[22,20,24,17,23,20,20,21,27,21,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 109, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,24,19,18,21,28,27,21,24,26,23],
[26,0,30,25,25,32,27,27,20,22,26,29],
[27,21,0,23,20,27,21,23,21,21,27,19],
[32,26,28,0,25,33,29,30,26,30,28,23],
[33,26,31,26,0,33,29,36,29,26,32,25],
[30,19,24,18,18,0,27,22,21,15,26,21],
[23,24,30,22,22,24,0,26,23,20,26,24],
[24,24,28,21,15,29,25,0,26,23,28,22],
[30,31,30,25,22,30,28,25,0,23,30,24],
[27,29,30,21,25,36,31,28,28,0,28,27],
[25,25,24,23,19,25,25,23,21,23,0,25],
[28,22,32,28,26,30,27,29,27,24,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 110, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,19,18,14,23,25,29,16,17,22,33],
[21,0,34,26,33,40,29,29,22,23,24,39],
[32,17,0,20,26,35,23,19,26,21,16,36],
[33,25,31,0,26,45,22,30,16,20,36,33],
[37,18,25,25,0,29,23,30,31,23,27,44],
[28,11,16,6,22,0,5,16,12,11,19,24],
[26,22,28,29,28,46,0,37,40,29,24,31],
[22,22,32,21,21,35,14,0,17,20,19,35],
[35,29,25,35,20,39,11,34,0,36,30,24],
[34,28,30,31,28,40,22,31,15,0,32,33],
[29,27,35,15,24,32,27,32,21,19,0,34],
[18,12,15,18,7,27,20,16,27,18,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 111, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,27,26,24,25,23,23,28,26,27,31],
[22,0,29,26,25,21,27,22,25,21,27,26],
[24,22,0,25,22,21,22,21,20,21,20,27],
[25,25,26,0,29,21,25,23,22,19,25,28],
[27,26,29,22,0,23,26,19,21,22,24,33],
[26,30,30,30,28,0,25,24,26,28,27,32],
[28,24,29,26,25,26,0,27,21,20,24,28],
[28,29,30,28,32,27,24,0,26,24,27,32],
[23,26,31,29,30,25,30,25,0,28,25,32],
[25,30,30,32,29,23,31,27,23,0,24,28],
[24,24,31,26,27,24,27,24,26,27,0,34],
[20,25,24,23,18,19,23,19,19,23,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 112, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,21,24,29,26,28,33,27,24,30,25],
[25,0,21,24,32,27,21,33,23,23,33,23],
[30,30,0,25,32,26,27,28,23,26,35,28],
[27,27,26,0,27,23,28,30,23,28,28,24],
[22,19,19,24,0,17,14,29,18,16,30,24],
[25,24,25,28,34,0,22,29,22,21,37,28],
[23,30,24,23,37,29,0,33,28,26,35,28],
[18,18,23,21,22,22,18,0,20,19,32,24],
[24,28,28,28,33,29,23,31,0,26,35,24],
[27,28,25,23,35,30,25,32,25,0,35,26],
[21,18,16,23,21,14,16,19,16,16,0,19],
[26,28,23,27,27,23,23,27,27,25,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 113, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,1,15,33,1,33,18,19,19,14,19],
[37,0,19,33,51,37,51,36,37,37,50,37],
[50,32,0,50,51,37,50,36,50,19,32,19],
[36,18,1,0,51,37,37,36,36,19,32,19],
[18,0,0,0,0,18,18,18,36,18,32,18],
[50,14,14,14,33,0,50,50,32,33,14,33],
[18,0,1,14,33,1,0,18,18,1,14,1],
[33,15,15,15,33,1,33,0,33,1,15,15],
[32,14,1,15,15,19,33,18,0,19,14,19],
[32,14,32,32,33,18,50,50,32,0,14,51],
[37,1,19,19,19,37,37,36,37,37,0,37],
[32,14,32,32,33,18,50,36,32,0,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 114, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,24,30,20,24,29,49,24,38,22,30],
[11,0,21,30,19,26,11,28,25,27,22,27],
[27,30,0,29,26,14,10,30,20,20,33,20],
[21,21,22,0,14,8,18,30,13,22,23,28],
[31,32,25,37,0,10,20,33,13,22,34,26],
[27,25,37,43,41,0,15,30,14,28,34,31],
[22,40,41,33,31,36,0,31,41,38,39,41],
[2,23,21,21,18,21,20,0,21,22,22,26],
[27,26,31,38,38,37,10,30,0,19,24,29],
[13,24,31,29,29,23,13,29,32,0,21,28],
[29,29,18,28,17,17,12,29,27,30,0,30],
[21,24,31,23,25,20,10,25,22,23,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 115, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,51,46,46,21,46,46,51,26,46,26,51],
[0,0,46,21,21,21,21,46,21,46,21,51],
[5,5,0,0,21,0,0,30,5,46,26,30],
[5,30,51,0,26,46,46,30,5,46,26,30],
[30,30,30,25,0,25,25,30,30,46,51,30],
[5,30,51,5,26,0,21,30,5,51,26,30],
[5,30,51,5,26,30,0,30,5,51,26,30],
[0,5,21,21,21,21,21,0,26,21,26,26],
[25,30,46,46,21,46,46,25,0,46,26,51],
[5,5,5,5,5,0,0,30,5,0,26,30],
[25,30,25,25,0,25,25,25,25,25,0,30],
[0,0,21,21,21,21,21,25,0,21,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 116, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,22,27,33,25,36,26,28,32,27,31],
[29,0,29,29,33,22,30,34,26,35,32,32],
[29,22,0,29,29,30,35,31,19,37,26,32],
[24,22,22,0,23,24,31,26,19,24,21,31],
[18,18,22,28,0,27,29,26,18,33,18,30],
[26,29,21,27,24,0,24,30,19,28,25,31],
[15,21,16,20,22,27,0,18,17,24,14,26],
[25,17,20,25,25,21,33,0,23,30,14,27],
[23,25,32,32,33,32,34,28,0,34,27,40],
[19,16,14,27,18,23,27,21,17,0,17,22],
[24,19,25,30,33,26,37,37,24,34,0,33],
[20,19,19,20,21,20,25,24,11,29,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 117, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,21,13,18,17,24,28,19,15,20,25],
[29,0,21,21,21,25,23,27,15,18,27,22],
[30,30,0,31,30,36,27,33,25,20,30,32],
[38,30,20,0,37,23,22,32,35,18,33,29],
[33,30,21,14,0,27,19,31,25,19,29,33],
[34,26,15,28,24,0,25,28,27,28,33,32],
[27,28,24,29,32,26,0,20,25,25,27,31],
[23,24,18,19,20,23,31,0,13,23,24,23],
[32,36,26,16,26,24,26,38,0,21,31,22],
[36,33,31,33,32,23,26,28,30,0,39,35],
[31,24,21,18,22,18,24,27,20,12,0,30],
[26,29,19,22,18,19,20,28,29,16,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 118, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,26,30,25,31,25,28,24,35,31,29],
[21,0,16,20,20,15,16,18,17,29,23,19],
[25,35,0,22,29,16,30,29,26,32,35,34],
[21,31,29,0,31,23,26,28,30,33,29,35],
[26,31,22,20,0,14,26,24,24,29,26,33],
[20,36,35,28,37,0,35,33,32,37,34,38],
[26,35,21,25,25,16,0,28,25,37,34,24],
[23,33,22,23,27,18,23,0,22,27,29,27],
[27,34,25,21,27,19,26,29,0,27,25,22],
[16,22,19,18,22,14,14,24,24,0,26,21],
[20,28,16,22,25,17,17,22,26,25,0,19],
[22,32,17,16,18,13,27,24,29,30,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 119, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,28,26,17,25,24,23,27,26,21,24],
[32,0,30,31,27,33,34,33,28,35,25,35],
[23,21,0,26,20,29,22,23,24,24,21,25],
[25,20,25,0,20,25,22,22,19,26,23,19],
[34,24,31,31,0,28,31,32,24,32,32,26],
[26,18,22,26,23,0,25,25,22,28,26,25],
[27,17,29,29,20,26,0,25,20,25,22,25],
[28,18,28,29,19,26,26,0,27,27,28,26],
[24,23,27,32,27,29,31,24,0,32,27,29],
[25,16,27,25,19,23,26,24,19,0,21,21],
[30,26,30,28,19,25,29,23,24,30,0,22],
[27,16,26,32,25,26,26,25,22,30,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 120, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,26,24,31,24,30,32,26,25,31,27],
[19,0,25,27,29,23,31,31,26,25,28,25],
[25,26,0,23,24,24,25,25,19,21,25,17],
[27,24,28,0,30,25,28,30,27,25,28,24],
[20,22,27,21,0,24,29,25,23,22,23,21],
[27,28,27,26,27,0,31,32,24,21,26,23],
[21,20,26,23,22,20,0,27,24,20,21,24],
[19,20,26,21,26,19,24,0,20,20,22,21],
[25,25,32,24,28,27,27,31,0,25,30,24],
[26,26,30,26,29,30,31,31,26,0,25,30],
[20,23,26,23,28,25,30,29,21,26,0,25],
[24,26,34,27,30,28,27,30,27,21,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 121, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,17,16,9,16,15,18,8,15,9,11],
[40,0,27,38,35,36,28,29,25,33,28,24],
[34,24,0,26,20,24,30,32,24,32,25,27],
[35,13,25,0,23,32,22,29,18,21,17,15],
[42,16,31,28,0,40,25,28,24,24,21,20],
[35,15,27,19,11,0,19,32,17,21,16,20],
[36,23,21,29,26,32,0,36,26,31,24,27],
[33,22,19,22,23,19,15,0,23,27,15,18],
[43,26,27,33,27,34,25,28,0,37,23,28],
[36,18,19,30,27,30,20,24,14,0,22,16],
[42,23,26,34,30,35,27,36,28,29,0,31],
[40,27,24,36,31,31,24,33,23,35,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 122, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,26,24,26,19,15,27,25,19,33,14],
[29,0,28,30,34,31,20,35,26,26,27,27],
[25,23,0,32,21,30,20,20,27,12,34,12],
[27,21,19,0,22,20,24,28,23,25,33,25],
[25,17,30,29,0,31,19,37,32,18,27,31],
[32,20,21,31,20,0,19,27,32,9,31,22],
[36,31,31,27,32,32,0,36,46,18,39,20],
[24,16,31,23,14,24,15,0,20,19,32,24],
[26,25,24,28,19,19,5,31,0,17,25,21],
[32,25,39,26,33,42,33,32,34,0,37,25],
[18,24,17,18,24,20,12,19,26,14,0,20],
[37,24,39,26,20,29,31,27,30,26,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 123, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,21,24,31,18,26,21,22,24,20,27],
[31,0,25,34,38,27,26,27,26,34,22,32],
[30,26,0,29,34,32,20,29,22,31,31,29],
[27,17,22,0,37,25,20,19,25,27,23,23],
[20,13,17,14,0,12,11,17,20,19,17,16],
[33,24,19,26,39,0,25,25,24,23,20,30],
[25,25,31,31,40,26,0,28,23,22,18,36],
[30,24,22,32,34,26,23,0,27,26,22,32],
[29,25,29,26,31,27,28,24,0,27,23,30],
[27,17,20,24,32,28,29,25,24,0,22,29],
[31,29,20,28,34,31,33,29,28,29,0,38],
[24,19,22,28,35,21,15,19,21,22,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 124, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,23,24,21,22,15,31,34,29,20,18],
[30,0,24,25,33,20,25,38,37,25,27,24],
[28,27,0,23,32,21,24,38,42,26,21,25],
[27,26,28,0,33,30,20,26,36,24,29,30],
[30,18,19,18,0,25,8,29,30,25,18,19],
[29,31,30,21,26,0,26,23,39,23,24,29],
[36,26,27,31,43,25,0,40,37,37,26,32],
[20,13,13,25,22,28,11,0,23,14,20,24],
[17,14,9,15,21,12,14,28,0,23,14,13],
[22,26,25,27,26,28,14,37,28,0,24,26],
[31,24,30,22,33,27,25,31,37,27,0,33],
[33,27,26,21,32,22,19,27,38,25,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 125, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,22,26,22,25,23,27,28,28,33,26],
[21,0,21,21,19,23,19,21,27,23,31,23],
[29,30,0,25,28,26,21,29,29,28,36,25],
[25,30,26,0,26,27,24,26,25,22,31,26],
[29,32,23,25,0,29,26,24,24,22,32,27],
[26,28,25,24,22,0,23,21,20,19,33,26],
[28,32,30,27,25,28,0,27,27,29,31,23],
[24,30,22,25,27,30,24,0,27,29,33,23],
[23,24,22,26,27,31,24,24,0,24,33,22],
[23,28,23,29,29,32,22,22,27,0,31,26],
[18,20,15,20,19,18,20,18,18,20,0,19],
[25,28,26,25,24,25,28,28,29,25,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 126, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,27,35,34,42,28,44,35,27,28,21],
[9,0,24,17,24,42,10,25,10,9,27,18],
[24,27,0,29,35,42,29,26,36,1,20,28],
[16,34,22,0,15,41,17,32,31,0,26,17],
[17,27,16,36,0,34,18,24,36,1,35,18],
[9,9,9,10,17,0,10,10,10,1,20,2],
[23,41,22,34,33,41,0,32,42,14,26,17],
[7,26,25,19,27,41,19,0,26,7,19,20],
[16,41,15,20,15,41,9,25,0,8,19,18],
[24,42,50,51,50,50,37,44,43,0,43,36],
[23,24,31,25,16,31,25,32,32,8,0,17],
[30,33,23,34,33,49,34,31,33,15,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 127, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,22,47,19,17,24,30,17,19,3,37],
[32,0,31,35,26,21,28,23,26,32,8,30],
[29,20,0,51,25,18,25,20,9,18,16,29],
[4,16,0,0,16,14,25,0,0,5,0,20],
[32,25,26,35,0,21,25,23,30,32,9,32],
[34,30,33,37,30,0,20,30,33,35,30,34],
[27,23,26,26,26,31,0,14,26,28,14,27],
[21,28,31,51,28,21,37,0,26,31,12,46],
[34,25,42,51,21,18,25,25,0,34,21,34],
[32,19,33,46,19,16,23,20,17,0,19,46],
[48,43,35,51,42,21,37,39,30,32,0,46],
[14,21,22,31,19,17,24,5,17,5,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 128, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,23,24,35,26,29,34,34,27,26,27],
[37,0,41,42,36,31,33,31,34,31,22,33],
[28,10,0,27,36,24,32,33,33,26,27,15],
[27,9,24,0,31,18,20,26,34,27,25,32],
[16,15,15,20,0,25,22,15,26,18,20,18],
[25,20,27,33,26,0,27,15,24,24,22,30],
[22,18,19,31,29,24,0,18,22,26,18,31],
[17,20,18,25,36,36,33,0,27,33,31,25],
[17,17,18,17,25,27,29,24,0,27,20,26],
[24,20,25,24,33,27,25,18,24,0,27,28],
[25,29,24,26,31,29,33,20,31,24,0,27],
[24,18,36,19,33,21,20,26,25,23,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 129, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,24,22,24,19,30,22,18,27,20,23],
[24,0,24,26,24,23,30,29,22,25,24,24],
[27,27,0,36,29,23,34,26,27,33,23,27],
[29,25,15,0,22,16,24,23,19,24,20,20],
[27,27,22,29,0,25,28,25,26,27,24,23],
[32,28,28,35,26,0,33,31,25,33,30,34],
[21,21,17,27,23,18,0,25,19,27,22,21],
[29,22,25,28,26,20,26,0,20,28,19,19],
[33,29,24,32,25,26,32,31,0,34,25,23],
[24,26,18,27,24,18,24,23,17,0,18,19],
[31,27,28,31,27,21,29,32,26,33,0,27],
[28,27,24,31,28,17,30,32,28,32,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 130, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,30,32,35,29,27,37,25,30,38,32],
[19,0,27,31,38,21,23,39,33,27,35,29],
[21,24,0,19,29,30,17,25,24,16,25,25],
[19,20,32,0,30,31,26,26,26,27,20,41],
[16,13,22,21,0,18,15,38,12,15,13,14],
[22,30,21,20,33,0,21,24,29,27,27,27],
[24,28,34,25,36,30,0,28,37,43,29,40],
[14,12,26,25,13,27,23,0,19,23,12,25],
[26,18,27,25,39,22,14,32,0,7,34,43],
[21,24,35,24,36,24,8,28,44,0,30,40],
[13,16,26,31,38,24,22,39,17,21,0,35],
[19,22,26,10,37,24,11,26,8,11,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 131, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,16,13,13,9,14,9,13,13,19,22],
[38,0,19,33,32,33,30,35,28,15,39,33],
[35,32,0,28,36,19,24,20,24,19,28,24],
[38,18,23,0,39,18,24,17,21,12,29,30],
[38,19,15,12,0,11,16,8,16,11,24,19],
[42,18,32,33,40,0,35,34,33,27,46,45],
[37,21,27,27,35,16,0,23,31,17,30,22],
[42,16,31,34,43,17,28,0,29,27,31,45],
[38,23,27,30,35,18,20,22,0,17,19,30],
[38,36,32,39,40,24,34,24,34,0,38,33],
[32,12,23,22,27,5,21,20,32,13,0,23],
[29,18,27,21,32,6,29,6,21,18,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 132, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,28,25,19,31,23,14,30,29,17,22],
[31,0,22,31,18,35,16,26,25,28,13,23],
[23,29,0,30,13,32,25,17,22,20,10,28],
[26,20,21,0,17,31,19,15,30,27,15,26],
[32,33,38,34,0,34,32,23,26,24,23,38],
[20,16,19,20,17,0,20,9,18,21,11,19],
[28,35,26,32,19,31,0,20,35,25,27,32],
[37,25,34,36,28,42,31,0,36,34,23,23],
[21,26,29,21,25,33,16,15,0,21,18,26],
[22,23,31,24,27,30,26,17,30,0,16,27],
[34,38,41,36,28,40,24,28,33,35,0,38],
[29,28,23,25,13,32,19,28,25,24,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 133, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,29,32,25,22,28,30,30,29,27,29],
[26,0,26,31,23,25,24,21,21,27,27,24],
[22,25,0,32,25,25,33,21,17,29,29,29],
[19,20,19,0,21,19,27,20,19,17,20,23],
[26,28,26,30,0,23,27,23,26,31,26,28],
[29,26,26,32,28,0,27,21,22,27,28,30],
[23,27,18,24,24,24,0,17,20,23,22,26],
[21,30,30,31,28,30,34,0,22,27,29,34],
[21,30,34,32,25,29,31,29,0,30,30,32],
[22,24,22,34,20,24,28,24,21,0,30,31],
[24,24,22,31,25,23,29,22,21,21,0,28],
[22,27,22,28,23,21,25,17,19,20,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 134, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,17,21,9,21,33,24,17,23,22,19],
[20,0,14,10,24,5,13,19,14,14,19,6],
[34,37,0,25,16,28,33,21,14,11,25,22],
[30,41,26,0,24,18,23,14,16,22,33,16],
[42,27,35,27,0,21,25,27,31,29,29,14],
[30,46,23,33,30,0,23,19,23,23,40,23],
[18,38,18,28,26,28,0,18,14,15,36,18],
[27,32,30,37,24,32,33,0,30,30,29,26],
[34,37,37,35,20,28,37,21,0,24,33,27],
[28,37,40,29,22,28,36,21,27,0,29,23],
[29,32,26,18,22,11,15,22,18,22,0,15],
[32,45,29,35,37,28,33,25,24,28,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 135, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,26,27,25,25,24,24,21,26,25,27],
[29,0,17,30,30,27,29,27,27,28,31,25],
[25,34,0,33,28,27,32,32,21,25,34,24],
[24,21,18,0,30,20,21,28,21,22,24,18],
[26,21,23,21,0,23,27,26,25,21,21,24],
[26,24,24,31,28,0,27,25,25,20,28,20],
[27,22,19,30,24,24,0,28,28,20,25,27],
[27,24,19,23,25,26,23,0,18,20,23,22],
[30,24,30,30,26,26,23,33,0,23,26,30],
[25,23,26,29,30,31,31,31,28,0,24,25],
[26,20,17,27,30,23,26,28,25,27,0,23],
[24,26,27,33,27,31,24,29,21,26,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 136, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,24,35,40,22,19,32,22,24,33,23],
[23,0,27,24,21,29,31,27,21,31,26,27],
[27,24,0,36,26,38,29,26,28,23,32,30],
[16,27,15,0,24,29,22,27,22,22,23,22],
[11,30,25,27,0,26,17,24,26,22,19,16],
[29,22,13,22,25,0,21,21,21,24,22,22],
[32,20,22,29,34,30,0,27,27,28,26,25],
[19,24,25,24,27,30,24,0,25,23,21,25],
[29,30,23,29,25,30,24,26,0,21,31,28],
[27,20,28,29,29,27,23,28,30,0,38,29],
[18,25,19,28,32,29,25,30,20,13,0,29],
[28,24,21,29,35,29,26,26,23,22,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 137, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,17,24,30,23,27,27,26,24,26,25],
[29,0,26,25,26,29,29,29,21,29,31,26],
[34,25,0,27,31,28,34,31,27,33,29,30],
[27,26,24,0,26,24,24,25,21,26,25,24],
[21,25,20,25,0,16,22,22,20,24,26,22],
[28,22,23,27,35,0,23,31,25,28,25,27],
[24,22,17,27,29,28,0,26,24,25,22,22],
[24,22,20,26,29,20,25,0,22,24,20,32],
[25,30,24,30,31,26,27,29,0,30,31,25],
[27,22,18,25,27,23,26,27,21,0,33,28],
[25,20,22,26,25,26,29,31,20,18,0,21],
[26,25,21,27,29,24,29,19,26,23,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 138, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,23,25,26,29,25,26,23,24,30,23],
[21,0,27,17,16,19,22,29,18,26,22,26],
[28,24,0,28,22,26,29,24,29,31,29,35],
[26,34,23,0,22,23,23,24,24,23,20,24],
[25,35,29,29,0,36,31,28,33,28,30,31],
[22,32,25,28,15,0,13,16,23,25,26,23],
[26,29,22,28,20,38,0,20,21,24,32,28],
[25,22,27,27,23,35,31,0,26,30,30,28],
[28,33,22,27,18,28,30,25,0,27,24,28],
[27,25,20,28,23,26,27,21,24,0,31,33],
[21,29,22,31,21,25,19,21,27,20,0,21],
[28,25,16,27,20,28,23,23,23,18,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 139, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,27,22,23,25,33,27,22,16,14,23],
[26,0,15,29,31,19,27,24,19,24,23,25],
[24,36,0,34,26,31,27,22,18,28,21,20],
[29,22,17,0,28,22,33,8,23,11,19,22],
[28,20,25,23,0,15,37,28,19,29,12,24],
[26,32,20,29,36,0,37,19,14,29,28,22],
[18,24,24,18,14,14,0,18,18,24,16,8],
[24,27,29,43,23,32,33,0,34,10,18,17],
[29,32,33,28,32,37,33,17,0,22,30,26],
[35,27,23,40,22,22,27,41,29,0,20,22],
[37,28,30,32,39,23,35,33,21,31,0,33],
[28,26,31,29,27,29,43,34,25,29,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 140, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,13,29,17,20,23,20,16,19,9,14],
[34,0,32,31,24,39,31,36,24,46,31,21],
[38,19,0,31,31,28,18,27,18,38,26,25],
[22,20,20,0,17,17,24,22,10,28,17,15],
[34,27,20,34,0,27,27,30,19,24,22,24],
[31,12,23,34,24,0,11,12,24,31,19,23],
[28,20,33,27,24,40,0,23,29,32,32,19],
[31,15,24,29,21,39,28,0,14,34,19,18],
[35,27,33,41,32,27,22,37,0,31,23,28],
[32,5,13,23,27,20,19,17,20,0,20,17],
[42,20,25,34,29,32,19,32,28,31,0,33],
[37,30,26,36,27,28,32,33,23,34,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 141, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,23,20,29,18,30,20,24,15,28,28],
[26,0,21,23,28,30,28,20,25,28,31,28],
[28,30,0,28,31,31,32,22,24,27,31,32],
[31,28,23,0,28,30,32,27,31,25,34,26],
[22,23,20,23,0,28,27,24,23,19,24,27],
[33,21,20,21,23,0,31,20,28,19,30,26],
[21,23,19,19,24,20,0,19,25,15,28,18],
[31,31,29,24,27,31,32,0,23,25,33,26],
[27,26,27,20,28,23,26,28,0,22,33,25],
[36,23,24,26,32,32,36,26,29,0,36,29],
[23,20,20,17,27,21,23,18,18,15,0,21],
[23,23,19,25,24,25,33,25,26,22,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 142, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,26,25,24,23,27,24,29,28,25,33],
[32,0,25,24,29,27,28,28,31,25,22,32],
[25,26,0,27,26,28,24,27,27,27,24,32],
[26,27,24,0,27,27,22,24,27,25,23,32],
[27,22,25,24,0,27,30,26,32,29,23,31],
[28,24,23,24,24,0,25,26,32,27,22,33],
[24,23,27,29,21,26,0,24,24,28,23,33],
[27,23,24,27,25,25,27,0,31,28,27,30],
[22,20,24,24,19,19,27,20,0,25,19,28],
[23,26,24,26,22,24,23,23,26,0,26,30],
[26,29,27,28,28,29,28,24,32,25,0,33],
[18,19,19,19,20,18,18,21,23,21,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 143, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,31,33,28,28,33,23,37,29,24,30],
[20,0,30,22,32,25,28,33,27,35,20,23],
[20,21,0,26,26,24,27,24,21,27,26,22],
[18,29,25,0,23,32,32,28,25,26,22,21],
[23,19,25,28,0,25,24,23,32,32,26,26],
[23,26,27,19,26,0,25,28,28,29,23,27],
[18,23,24,19,27,26,0,24,24,26,22,26],
[28,18,27,23,28,23,27,0,23,24,23,26],
[14,24,30,26,19,23,27,28,0,30,23,25],
[22,16,24,25,19,22,25,27,21,0,17,22],
[27,31,25,29,25,28,29,28,28,34,0,28],
[21,28,29,30,25,24,25,25,26,29,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 144, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,28,25,22,28,26,23,23,28,25,27],
[29,0,28,28,27,28,30,27,25,28,25,31],
[23,23,0,24,22,27,28,26,27,28,25,28],
[26,23,27,0,20,21,25,23,20,21,23,25],
[29,24,29,31,0,28,29,27,26,26,26,31],
[23,23,24,30,23,0,26,25,25,24,25,24],
[25,21,23,26,22,25,0,27,26,27,20,33],
[28,24,25,28,24,26,24,0,24,30,24,24],
[28,26,24,31,25,26,25,27,0,29,26,31],
[23,23,23,30,25,27,24,21,22,0,19,26],
[26,26,26,28,25,26,31,27,25,32,0,26],
[24,20,23,26,20,27,18,27,20,25,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 145, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,18,29,28,25,24,39,29,26,17,32],
[30,0,11,30,20,27,23,38,29,27,20,30],
[33,40,0,31,31,34,34,43,32,24,22,37],
[22,21,20,0,16,24,20,26,22,18,17,25],
[23,31,20,35,0,30,28,35,31,34,28,27],
[26,24,17,27,21,0,24,30,21,25,22,19],
[27,28,17,31,23,27,0,31,23,35,18,26],
[12,13,8,25,16,21,20,0,13,21,13,13],
[22,22,19,29,20,30,28,38,0,28,25,21],
[25,24,27,33,17,26,16,30,23,0,21,24],
[34,31,29,34,23,29,33,38,26,30,0,24],
[19,21,14,26,24,32,25,38,30,27,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 146, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,42,19,42,28,42,42,42,25,42,19,19],
[9,0,19,9,11,11,11,2,2,9,11,0],
[32,32,0,32,11,34,34,34,34,32,11,9],
[9,42,19,0,28,28,42,42,25,2,28,2],
[23,40,40,23,0,25,25,23,25,23,23,23],
[9,40,17,23,26,0,23,23,25,0,9,0],
[9,40,17,9,26,28,0,0,2,0,9,0],
[9,49,17,9,28,28,51,0,25,9,11,0],
[26,49,17,26,26,26,49,26,0,26,26,26],
[9,42,19,49,28,51,51,42,25,0,28,17],
[32,40,40,23,28,42,42,40,25,23,0,23],
[32,51,42,49,28,51,51,51,25,34,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 147, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,28,29,30,30,26,27,26,27,28,25],
[24,0,26,26,33,30,28,24,33,27,33,27],
[23,25,0,25,28,32,25,20,29,32,28,20],
[22,25,26,0,26,32,31,26,27,27,28,22],
[21,18,23,25,0,27,25,27,27,23,29,18],
[21,21,19,19,24,0,22,18,24,25,27,17],
[25,23,26,20,26,29,0,26,21,24,30,26],
[24,27,31,25,24,33,25,0,26,26,34,22],
[25,18,22,24,24,27,30,25,0,32,27,24],
[24,24,19,24,28,26,27,25,19,0,25,21],
[23,18,23,23,22,24,21,17,24,26,0,15],
[26,24,31,29,33,34,25,29,27,30,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 148, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,22,16,23,17,25,29,29,25,29,20],
[34,0,28,26,29,25,28,31,38,31,30,33],
[29,23,0,27,26,28,31,25,39,28,17,28],
[35,25,24,0,30,23,28,26,36,30,26,30],
[28,22,25,21,0,23,22,23,32,23,24,22],
[34,26,23,28,28,0,32,36,34,30,26,23],
[26,23,20,23,29,19,0,27,33,19,26,22],
[22,20,26,25,28,15,24,0,31,31,28,19],
[22,13,12,15,19,17,18,20,0,17,19,19],
[26,20,23,21,28,21,32,20,34,0,20,23],
[22,21,34,25,27,25,25,23,32,31,0,24],
[31,18,23,21,29,28,29,32,32,28,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 149, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,4,47,15,24,24,23,32,9,24,32],
[23,0,0,47,15,9,0,23,32,9,38,23],
[47,51,0,47,24,24,24,38,47,24,47,47],
[4,4,4,0,4,13,4,23,27,9,4,23],
[36,36,27,47,0,32,32,23,32,32,32,32],
[27,42,27,38,19,0,42,23,27,9,42,23],
[27,51,27,47,19,9,0,23,32,9,42,23],
[28,28,13,28,28,28,28,0,51,28,28,28],
[19,19,4,24,19,24,19,0,0,9,19,0],
[42,42,27,42,19,42,42,23,42,0,42,27],
[27,13,4,47,19,9,9,23,32,9,0,23],
[19,28,4,28,19,28,28,23,51,24,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 150, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,32,26,33,40,33,25,10,33,15,31],
[12,0,18,17,30,27,25,9,16,26,10,20],
[19,33,0,35,27,30,22,15,15,24,8,23],
[25,34,16,0,29,32,17,9,15,24,10,25],
[18,21,24,22,0,32,17,2,15,25,17,40],
[11,24,21,19,19,0,11,12,10,27,9,19],
[18,26,29,34,34,40,0,21,9,32,18,34],
[26,42,36,42,49,39,30,0,25,33,31,47],
[41,35,36,36,36,41,42,26,0,26,23,32],
[18,25,27,27,26,24,19,18,25,0,16,26],
[36,41,43,41,34,42,33,20,28,35,0,34],
[20,31,28,26,11,32,17,4,19,25,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 151, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,25,29,27,20,23,24,21,31,22,33],
[21,0,21,26,17,15,18,22,18,19,18,25],
[26,30,0,26,28,26,19,28,25,30,28,35],
[22,25,25,0,22,20,18,23,20,24,18,27],
[24,34,23,29,0,27,22,31,27,25,26,35],
[31,36,25,31,24,0,23,30,28,35,17,34],
[28,33,32,33,29,28,0,36,32,32,25,31],
[27,29,23,28,20,21,15,0,21,21,19,27],
[30,33,26,31,24,23,19,30,0,26,29,33],
[20,32,21,27,26,16,19,30,25,0,21,35],
[29,33,23,33,25,34,26,32,22,30,0,33],
[18,26,16,24,16,17,20,24,18,16,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 152, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,29,28,25,27,20,23,28,19,25,21],
[27,0,24,23,19,25,23,21,23,20,24,26],
[22,27,0,22,23,25,23,26,24,20,27,23],
[23,28,29,0,23,28,21,24,26,23,27,19],
[26,32,28,28,0,27,24,27,27,20,23,25],
[24,26,26,23,24,0,26,21,31,25,27,24],
[31,28,28,30,27,25,0,31,26,28,31,24],
[28,30,25,27,24,30,20,0,31,24,29,21],
[23,28,27,25,24,20,25,20,0,21,29,20],
[32,31,31,28,31,26,23,27,30,0,30,24],
[26,27,24,24,28,24,20,22,22,21,0,22],
[30,25,28,32,26,27,27,30,31,27,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 153, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,25,29,21,25,30,30,24,22,26,26],
[29,0,25,27,24,20,21,31,22,25,28,25],
[26,26,0,35,25,22,22,24,19,20,26,20],
[22,24,16,0,22,22,20,24,24,18,16,18],
[30,27,26,29,0,22,27,32,23,27,29,27],
[26,31,29,29,29,0,28,32,23,22,27,26],
[21,30,29,31,24,23,0,31,23,22,25,26],
[21,20,27,27,19,19,20,0,19,15,27,17],
[27,29,32,27,28,28,28,32,0,22,28,27],
[29,26,31,33,24,29,29,36,29,0,28,29],
[25,23,25,35,22,24,26,24,23,23,0,25],
[25,26,31,33,24,25,25,34,24,22,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 154, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,29,20,34,27,21,25,18,25,20,31],
[27,0,31,27,33,22,35,21,25,25,31,37],
[22,20,0,19,41,17,22,21,23,28,16,40],
[31,24,32,0,44,26,32,29,24,27,24,41],
[17,18,10,7,0,15,13,19,13,18,13,23],
[24,29,34,25,36,0,25,26,22,28,27,31],
[30,16,29,19,38,26,0,19,13,22,22,32],
[26,30,30,22,32,25,32,0,28,24,24,35],
[33,26,28,27,38,29,38,23,0,26,29,34],
[26,26,23,24,33,23,29,27,25,0,20,30],
[31,20,35,27,38,24,29,27,22,31,0,25],
[20,14,11,10,28,20,19,16,17,21,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 155, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,3,3,20,20,3,0,20,20,3,0],
[48,0,20,33,51,20,20,17,33,33,20,17],
[48,31,0,33,51,38,38,35,33,51,21,17],
[48,18,18,0,38,35,35,18,35,35,21,35],
[31,0,0,13,0,17,0,0,17,30,0,0],
[31,31,13,16,34,0,16,18,30,16,3,0],
[48,31,13,16,51,35,0,18,30,33,3,0],
[51,34,16,33,51,33,33,0,33,33,16,20],
[31,18,18,16,34,21,21,18,0,34,21,0],
[31,18,0,16,21,35,18,18,17,0,3,0],
[48,31,30,30,51,48,48,35,30,48,0,17],
[51,34,34,16,51,51,51,31,51,51,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 156, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,27,26,27,28,31,37,29,25,29,38],
[21,0,29,20,20,21,23,25,24,16,20,33],
[24,22,0,23,21,20,18,21,25,21,22,22],
[25,31,28,0,21,23,25,28,25,21,28,33],
[24,31,30,30,0,28,33,37,29,28,26,38],
[23,30,31,28,23,0,27,27,26,25,22,38],
[20,28,33,26,18,24,0,30,30,22,18,29],
[14,26,30,23,14,24,21,0,20,20,16,28],
[22,27,26,26,22,25,21,31,0,23,23,31],
[26,35,30,30,23,26,29,31,28,0,26,31],
[22,31,29,23,25,29,33,35,28,25,0,37],
[13,18,29,18,13,13,22,23,20,20,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 157, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,25,31,26,26,23,24,24,27,20,27],
[28,0,30,32,32,33,23,29,26,29,27,30],
[26,21,0,25,23,27,18,24,27,23,30,26],
[20,19,26,0,26,32,19,23,30,31,22,21],
[25,19,28,25,0,28,18,21,20,29,26,20],
[25,18,24,19,23,0,14,18,23,26,24,24],
[28,28,33,32,33,37,0,24,32,33,26,32],
[27,22,27,28,30,33,27,0,21,30,26,23],
[27,25,24,21,31,28,19,30,0,27,27,25],
[24,22,28,20,22,25,18,21,24,0,25,23],
[31,24,21,29,25,27,25,25,24,26,0,23],
[24,21,25,30,31,27,19,28,26,28,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 158, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,18,15,31,21,27,16,28,11,29,8],
[28,0,39,31,36,19,25,21,26,16,25,27],
[33,12,0,12,16,11,20,16,21,20,15,22],
[36,20,39,0,44,27,35,29,24,24,26,29],
[20,15,35,7,0,23,17,26,5,13,25,25],
[30,32,40,24,28,0,32,17,25,12,22,15],
[24,26,31,16,34,19,0,19,16,21,26,19],
[35,30,35,22,25,34,32,0,22,31,32,25],
[23,25,30,27,46,26,35,29,0,21,25,20],
[40,35,31,27,38,39,30,20,30,0,37,26],
[22,26,36,25,26,29,25,19,26,14,0,21],
[43,24,29,22,26,36,32,26,31,25,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 159, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,35,36,23,38,34,28,30,28,27,30],
[35,0,50,43,41,45,34,44,36,41,25,34],
[16,1,0,24,9,35,17,18,11,9,6,15],
[15,8,27,0,16,37,22,17,19,8,13,16],
[28,10,42,35,0,30,26,30,22,28,26,26],
[13,6,16,14,21,0,20,15,20,6,18,21],
[17,17,34,29,25,31,0,29,29,19,20,26],
[23,7,33,34,21,36,22,0,30,9,16,16],
[21,15,40,32,29,31,22,21,0,21,27,20],
[23,10,42,43,23,45,32,42,30,0,18,22],
[24,26,45,38,25,33,31,35,24,33,0,18],
[21,17,36,35,25,30,25,35,31,29,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 160, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,24,31,25,28,25,28,26,25,27,27],
[22,0,23,28,22,22,26,27,30,22,26,25],
[27,28,0,29,25,31,21,24,25,23,23,21],
[20,23,22,0,20,22,20,21,25,23,20,22],
[26,29,26,31,0,23,29,32,30,27,30,30],
[23,29,20,29,28,0,31,25,29,22,25,24],
[26,25,30,31,22,20,0,21,25,24,21,28],
[23,24,27,30,19,26,30,0,26,26,22,28],
[25,21,26,26,21,22,26,25,0,22,21,26],
[26,29,28,28,24,29,27,25,29,0,27,25],
[24,25,28,31,21,26,30,29,30,24,0,29],
[24,26,30,29,21,27,23,23,25,26,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 161, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,38,24,13,31,23,33,35,37,30,30,19],
[13,0,13,15,25,19,25,25,27,31,27,13],
[27,38,0,22,23,25,19,26,32,29,25,18],
[38,36,29,0,33,21,37,38,39,38,22,32],
[20,26,28,18,0,24,35,32,26,24,13,14],
[28,32,26,30,27,0,21,42,36,36,25,22],
[18,26,32,14,16,30,0,26,38,23,25,20],
[16,26,25,13,19,9,25,0,28,18,15,18],
[14,24,19,12,25,15,13,23,0,13,15,20],
[21,20,22,13,27,15,28,33,38,0,26,17],
[21,24,26,29,38,26,26,36,36,25,0,24],
[32,38,33,19,37,29,31,33,31,34,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 162, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,25,27,31,30,35,22,31,29,33,22],
[23,0,25,21,31,32,27,30,32,29,29,36],
[26,26,0,20,29,34,27,29,31,25,27,33],
[24,30,31,0,26,32,26,24,31,25,26,35],
[20,20,22,25,0,29,22,16,22,22,24,20],
[21,19,17,19,22,0,26,24,21,24,27,23],
[16,24,24,25,29,25,0,18,33,24,27,19],
[29,21,22,27,35,27,33,0,32,24,23,28],
[20,19,20,20,29,30,18,19,0,23,23,24],
[22,22,26,26,29,27,27,27,28,0,37,26],
[18,22,24,25,27,24,24,28,28,14,0,31],
[29,15,18,16,31,28,32,23,27,25,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 163, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,28,25,27,26,21,26,24,26,25,26],
[26,0,19,26,26,24,23,26,24,23,26,26],
[23,32,0,29,28,30,24,27,28,28,24,26],
[26,25,22,0,31,22,24,26,22,24,23,30],
[24,25,23,20,0,25,25,26,22,19,23,27],
[25,27,21,29,26,0,24,29,28,26,27,28],
[30,28,27,27,26,27,0,31,22,27,25,28],
[25,25,24,25,25,22,20,0,20,24,21,29],
[27,27,23,29,29,23,29,31,0,28,24,31],
[25,28,23,27,32,25,24,27,23,0,24,26],
[26,25,27,28,28,24,26,30,27,27,0,31],
[25,25,25,21,24,23,23,22,20,25,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 164, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,24,17,20,28,20,28,23,23,25,29],
[31,0,30,20,23,16,30,21,20,21,26,23],
[27,21,0,21,24,18,28,24,26,18,20,28],
[34,31,30,0,31,23,32,34,24,32,33,33],
[31,28,27,20,0,23,33,30,24,28,28,29],
[23,35,33,28,28,0,32,34,38,36,30,28],
[31,21,23,19,18,19,0,25,15,18,23,22],
[23,30,27,17,21,17,26,0,23,30,25,25],
[28,31,25,27,27,13,36,28,0,25,32,22],
[28,30,33,19,23,15,33,21,26,0,27,24],
[26,25,31,18,23,21,28,26,19,24,0,30],
[22,28,23,18,22,23,29,26,29,27,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 165, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,0,0,9,12,25,0,0,0,12,0],
[39,0,26,12,28,19,32,26,26,7,26,19],
[51,25,0,25,29,37,35,32,13,32,32,44],
[51,39,26,0,35,29,42,26,14,16,26,28],
[42,23,22,16,0,22,35,10,7,16,23,22],
[39,32,14,22,29,0,32,36,14,29,39,16],
[26,19,16,9,16,19,0,16,7,16,19,9],
[51,25,19,25,41,15,35,0,7,29,32,24],
[51,25,38,37,44,37,44,44,0,32,32,44],
[51,44,19,35,35,22,35,22,19,0,31,31],
[39,25,19,25,28,12,32,19,19,20,0,12],
[51,32,7,23,29,35,42,27,7,20,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 166, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,20,24,29,24,22,19,19,28,19,25],
[30,0,24,30,35,36,36,33,22,32,33,31],
[31,27,0,32,39,31,33,33,18,22,33,25],
[27,21,19,0,27,26,20,23,26,18,25,26],
[22,16,12,24,0,17,30,19,10,26,24,19],
[27,15,20,25,34,0,28,22,21,22,26,18],
[29,15,18,31,21,23,0,21,22,26,21,17],
[32,18,18,28,32,29,30,0,21,22,23,26],
[32,29,33,25,41,30,29,30,0,27,29,29],
[23,19,29,33,25,29,25,29,24,0,27,34],
[32,18,18,26,27,25,30,28,22,24,0,23],
[26,20,26,25,32,33,34,25,22,17,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 167, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,31,25,26,32,28,22,35,24,28,18],
[23,0,26,26,21,31,21,16,25,19,20,25],
[20,25,0,17,28,29,23,23,28,31,25,27],
[26,25,34,0,28,31,26,22,32,34,28,30],
[25,30,23,23,0,32,28,25,19,26,21,25],
[19,20,22,20,19,0,17,18,21,20,17,13],
[23,30,28,25,23,34,0,26,36,22,24,22],
[29,35,28,29,26,33,25,0,31,21,21,22],
[16,26,23,19,32,30,15,20,0,22,20,17],
[27,32,20,17,25,31,29,30,29,0,34,26],
[23,31,26,23,30,34,27,30,31,17,0,26],
[33,26,24,21,26,38,29,29,34,25,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 168, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,23,28,22,26,29,23,24,26,23,31],
[23,0,27,28,23,29,24,25,23,26,26,26],
[28,24,0,24,27,28,24,24,24,26,26,24],
[23,23,27,0,23,28,23,22,24,24,27,24],
[29,28,24,28,0,28,25,29,29,26,29,31],
[25,22,23,23,23,0,22,25,24,23,22,28],
[22,27,27,28,26,29,0,28,28,25,24,27],
[28,26,27,29,22,26,23,0,22,25,28,28],
[27,28,27,27,22,27,23,29,0,27,25,27],
[25,25,25,27,25,28,26,26,24,0,26,25],
[28,25,25,24,22,29,27,23,26,25,0,28],
[20,25,27,27,20,23,24,23,24,26,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 169, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,24,24,24,26,28,33,22,27,26,23],
[21,0,18,21,28,24,27,28,32,24,25,31],
[27,33,0,27,24,28,31,35,27,36,28,29],
[27,30,24,0,27,25,31,29,26,31,28,27],
[27,23,27,24,0,30,29,32,24,23,28,26],
[25,27,23,26,21,0,30,30,25,24,29,29],
[23,24,20,20,22,21,0,28,20,24,22,24],
[18,23,16,22,19,21,23,0,21,19,19,22],
[29,19,24,25,27,26,31,30,0,22,28,27],
[24,27,15,20,28,27,27,32,29,0,24,24],
[25,26,23,23,23,22,29,32,23,27,0,21],
[28,20,22,24,25,22,27,29,24,27,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 170, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,15,24,15,24,24,6,24,33,6,9],
[27,0,24,15,15,33,24,24,24,15,15,18],
[36,27,0,33,15,24,33,33,33,33,24,27],
[27,36,18,0,9,33,36,15,42,51,9,18],
[36,36,36,42,0,51,36,24,42,42,27,36],
[27,18,27,18,0,0,27,24,18,27,18,27],
[27,27,18,15,15,24,0,24,24,33,0,9],
[45,27,18,36,27,27,27,0,36,36,18,36],
[27,27,18,9,9,33,27,15,0,42,9,18],
[18,36,18,0,9,24,18,15,9,0,0,9],
[45,36,27,42,24,33,51,33,42,51,0,45],
[42,33,24,33,15,24,42,15,33,42,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 171, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,26,27,29,26,31,23,29,25,26,25],
[24,0,30,26,24,22,21,20,28,21,23,23],
[25,21,0,21,24,20,23,23,24,25,26,25],
[24,25,30,0,26,26,24,23,26,23,25,27],
[22,27,27,25,0,27,24,21,28,29,26,25],
[25,29,31,25,24,0,25,28,25,30,27,27],
[20,30,28,27,27,26,0,20,26,24,25,27],
[28,31,28,28,30,23,31,0,28,22,27,29],
[22,23,27,25,23,26,25,23,0,22,23,19],
[26,30,26,28,22,21,27,29,29,0,25,28],
[25,28,25,26,25,24,26,24,28,26,0,26],
[26,28,26,24,26,24,24,22,32,23,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 172, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,24,28,27,26,30,26,27,23,25,26],
[26,0,25,26,28,24,28,29,28,22,26,28],
[27,26,0,27,27,27,26,27,28,24,23,23],
[23,25,24,0,25,27,25,23,23,25,22,27],
[24,23,24,26,0,23,23,20,21,20,26,26],
[25,27,24,24,28,0,21,24,28,22,23,26],
[21,23,25,26,28,30,0,26,27,26,30,30],
[25,22,24,28,31,27,25,0,27,22,25,24],
[24,23,23,28,30,23,24,24,0,26,27,26],
[28,29,27,26,31,29,25,29,25,0,29,25],
[26,25,28,29,25,28,21,26,24,22,0,26],
[25,23,28,24,25,25,21,27,25,26,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 173, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,29,24,23,25,21,28,20,20,27,32],
[24,0,25,18,17,21,14,25,16,16,27,15],
[22,26,0,22,20,26,18,22,18,20,26,20],
[27,33,29,0,20,29,24,23,20,20,30,21],
[28,34,31,31,0,25,26,28,25,28,38,28],
[26,30,25,22,26,0,16,26,18,17,25,19],
[30,37,33,27,25,35,0,24,31,25,28,26],
[23,26,29,28,23,25,27,0,19,21,29,27],
[31,35,33,31,26,33,20,32,0,23,32,32],
[31,35,31,31,23,34,26,30,28,0,31,30],
[24,24,25,21,13,26,23,22,19,20,0,27],
[19,36,31,30,23,32,25,24,19,21,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 174, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,19,28,24,15,27,9,19,32,27,32],
[32,0,42,29,34,29,42,24,29,42,28,42],
[32,9,0,23,14,34,28,9,23,32,22,22],
[23,22,28,0,33,20,28,23,15,32,28,28],
[27,17,37,18,0,29,37,31,14,41,17,31],
[36,22,17,31,22,0,32,22,9,32,22,22],
[24,9,23,23,14,19,0,14,23,28,9,9],
[42,27,42,28,20,29,37,0,29,41,27,32],
[32,22,28,36,37,42,28,22,0,32,32,27],
[19,9,19,19,10,19,23,10,19,0,0,5],
[24,23,29,23,34,29,42,24,19,51,0,23],
[19,9,29,23,20,29,42,19,24,46,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 175, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,23,16,22,23,24,14,18,25,15,16],
[39,0,30,18,22,21,27,26,23,31,16,21],
[28,21,0,15,24,23,21,21,14,27,16,12],
[35,33,36,0,31,27,30,29,22,31,21,22],
[29,29,27,20,0,27,24,22,19,23,10,15],
[28,30,28,24,24,0,26,21,16,28,15,16],
[27,24,30,21,27,25,0,24,16,25,21,16],
[37,25,30,22,29,30,27,0,24,30,25,21],
[33,28,37,29,32,35,35,27,0,31,19,26],
[26,20,24,20,28,23,26,21,20,0,15,17],
[36,35,35,30,41,36,30,26,32,36,0,19],
[35,30,39,29,36,35,35,30,25,34,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 176, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,25,27,29,25,28,33,24,23,23,26],
[23,0,21,21,24,19,27,24,19,22,27,22],
[26,30,0,26,25,26,28,29,21,23,27,27],
[24,30,25,0,27,27,28,30,18,20,27,24],
[22,27,26,24,0,25,31,28,16,23,25,23],
[26,32,25,24,26,0,29,29,22,26,28,30],
[23,24,23,23,20,22,0,24,22,19,21,23],
[18,27,22,21,23,22,27,0,19,21,23,21],
[27,32,30,33,35,29,29,32,0,21,27,31],
[28,29,28,31,28,25,32,30,30,0,32,25],
[28,24,24,24,26,23,30,28,24,19,0,22],
[25,29,24,27,28,21,28,30,20,26,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 177, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,23,24,27,33,20,26,22,28,27,27],
[31,0,33,19,24,30,23,25,19,29,29,26],
[28,18,0,19,25,26,14,21,15,24,21,26],
[27,32,32,0,25,29,26,28,23,32,27,28],
[24,27,26,26,0,24,23,21,19,30,21,31],
[18,21,25,22,27,0,19,24,22,26,26,22],
[31,28,37,25,28,32,0,29,25,28,28,32],
[25,26,30,23,30,27,22,0,28,34,29,35],
[29,32,36,28,32,29,26,23,0,37,31,35],
[23,22,27,19,21,25,23,17,14,0,20,27],
[24,22,30,24,30,25,23,22,20,31,0,28],
[24,25,25,23,20,29,19,16,16,24,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 178, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,34,24,25,15,37,27,26,26,25,26],
[21,0,31,28,24,21,31,16,24,37,29,18],
[17,20,0,24,20,22,39,26,20,26,27,20],
[27,23,27,0,23,18,32,29,28,19,19,10],
[26,27,31,28,0,25,36,28,22,26,26,9],
[36,30,29,33,26,0,42,31,27,26,29,16],
[14,20,12,19,15,9,0,31,25,20,14,9],
[24,35,25,22,23,20,20,0,41,31,21,15],
[25,27,31,23,29,24,26,10,0,27,24,13],
[25,14,25,32,25,25,31,20,24,0,22,18],
[26,22,24,32,25,22,37,30,27,29,0,22],
[25,33,31,41,42,35,42,36,38,33,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 179, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,21,23,19,25,24,23,24,28,24,28],
[26,0,23,27,19,26,24,24,24,29,33,26],
[30,28,0,24,21,29,30,24,26,31,27,32],
[28,24,27,0,22,29,26,21,26,29,30,27],
[32,32,30,29,0,30,31,29,24,29,29,30],
[26,25,22,22,21,0,23,20,27,20,28,28],
[27,27,21,25,20,28,0,22,21,27,32,28],
[28,27,27,30,22,31,29,0,26,27,30,27],
[27,27,25,25,27,24,30,25,0,28,27,26],
[23,22,20,22,22,31,24,24,23,0,24,29],
[27,18,24,21,22,23,19,21,24,27,0,32],
[23,25,19,24,21,23,23,24,25,22,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 180, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,18,15,19,14,22,11,23,19,20,18],
[29,0,26,29,32,30,25,23,20,24,26,26],
[33,25,0,15,32,26,34,26,26,26,31,29],
[36,22,36,0,29,33,30,28,27,26,31,22],
[32,19,19,22,0,22,18,16,22,21,21,26],
[37,21,25,18,29,0,26,25,16,23,26,20],
[29,26,17,21,33,25,0,20,21,26,25,29],
[40,28,25,23,35,26,31,0,29,34,38,28],
[28,31,25,24,29,35,30,22,0,27,25,27],
[32,27,25,25,30,28,25,17,24,0,25,21],
[31,25,20,20,30,25,26,13,26,26,0,29],
[33,25,22,29,25,31,22,23,24,30,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 181, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,28,2,29,34,37,6,4,14,30,24],
[27,0,18,14,27,28,15,6,6,12,18,18],
[23,33,0,14,23,36,33,18,6,14,18,12],
[49,37,37,0,39,38,37,25,35,40,49,38],
[22,24,28,12,0,34,37,28,14,24,28,12],
[17,23,15,13,17,0,17,17,15,14,27,14],
[14,36,18,14,14,34,0,20,6,14,18,26],
[45,45,33,26,23,34,31,0,14,26,30,26],
[47,45,45,16,37,36,45,37,0,24,39,24],
[37,39,37,11,27,37,37,25,27,0,27,18],
[21,33,33,2,23,24,33,21,12,24,0,26],
[27,33,39,13,39,37,25,25,27,33,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 182, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,23,19,25,17,23,14,25,17,21,14],
[32,0,26,25,28,29,27,26,29,32,32,27],
[28,25,0,20,22,19,26,23,29,28,27,19],
[32,26,31,0,35,35,36,25,31,23,30,32],
[26,23,29,16,0,23,23,16,25,21,29,19],
[34,22,32,16,28,0,32,24,34,20,23,18],
[28,24,25,15,28,19,0,17,30,18,21,18],
[37,25,28,26,35,27,34,0,45,21,31,29],
[26,22,22,20,26,17,21,6,0,15,20,18],
[34,19,23,28,30,31,33,30,36,0,22,27],
[30,19,24,21,22,28,30,20,31,29,0,19],
[37,24,32,19,32,33,33,22,33,24,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 183, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,19,27,25,32,28,22,24,33,31,22],
[30,0,29,30,35,32,28,29,28,38,39,25],
[32,22,0,27,35,31,25,23,24,33,33,21],
[24,21,24,0,31,35,21,28,20,35,38,23],
[26,16,16,20,0,26,23,21,15,26,28,16],
[19,19,20,16,25,0,33,28,23,35,32,16],
[23,23,26,30,28,18,0,28,28,30,37,21],
[29,22,28,23,30,23,23,0,23,40,28,17],
[27,23,27,31,36,28,23,28,0,33,31,30],
[18,13,18,16,25,16,21,11,18,0,23,18],
[20,12,18,13,23,19,14,23,20,28,0,27],
[29,26,30,28,35,35,30,34,21,33,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 184, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,18,25,27,38,21,33,42,27,26,33],
[24,0,27,32,27,37,32,26,37,26,33,31],
[33,24,0,36,28,31,31,42,35,28,29,38],
[26,19,15,0,30,26,29,28,26,26,15,30],
[24,24,23,21,0,32,28,39,33,25,21,35],
[13,14,20,25,19,0,17,32,36,28,25,36],
[30,19,20,22,23,34,0,33,38,31,24,26],
[18,25,9,23,12,19,18,0,31,19,19,30],
[9,14,16,25,18,15,13,20,0,14,18,23],
[24,25,23,25,26,23,20,32,37,0,25,19],
[25,18,22,36,30,26,27,32,33,26,0,34],
[18,20,13,21,16,15,25,21,28,32,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 185, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,23,19,29,25,28,24,24,17,24,17],
[29,0,29,20,35,31,33,20,25,21,20,23],
[28,22,0,16,27,32,33,17,24,14,14,27],
[32,31,35,0,36,34,33,25,24,20,24,34],
[22,16,24,15,0,26,22,17,17,14,15,18],
[26,20,19,17,25,0,23,12,19,17,14,23],
[23,18,18,18,29,28,0,20,19,15,17,20],
[27,31,34,26,34,39,31,0,25,21,23,34],
[27,26,27,27,34,32,32,26,0,28,22,29],
[34,30,37,31,37,34,36,30,23,0,27,31],
[27,31,37,27,36,37,34,28,29,24,0,30],
[34,28,24,17,33,28,31,17,22,20,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 186, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,34,23,23,24,33,25,24,28,27,23],
[26,0,25,28,27,24,30,23,24,27,28,19],
[17,26,0,22,23,22,25,20,20,20,25,16],
[28,23,29,0,25,19,27,26,30,31,31,24],
[28,24,28,26,0,28,33,28,24,24,26,20],
[27,27,29,32,23,0,28,24,32,29,31,27],
[18,21,26,24,18,23,0,28,22,23,24,19],
[26,28,31,25,23,27,23,0,23,23,27,24],
[27,27,31,21,27,19,29,28,0,20,29,21],
[23,24,31,20,27,22,28,28,31,0,27,20],
[24,23,26,20,25,20,27,24,22,24,0,21],
[28,32,35,27,31,24,32,27,30,31,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 187, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,14,31,17,13,31,51,31,38,51,31],
[17,0,17,17,17,13,31,51,17,24,51,17],
[37,34,0,31,17,13,31,51,31,38,51,31],
[20,34,20,0,37,20,38,51,37,24,51,38],
[34,34,34,14,0,20,18,38,18,34,38,38],
[38,38,38,31,31,0,18,51,31,38,51,18],
[20,20,20,13,33,33,0,33,13,20,33,20],
[0,0,0,0,13,0,18,0,4,20,14,4],
[20,34,20,14,33,20,38,47,0,20,34,34],
[13,27,13,27,17,13,31,31,31,0,31,31],
[0,0,0,0,13,0,18,37,17,20,0,4],
[20,34,20,13,13,33,31,47,17,20,47,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 188, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,24,21,27,21,13,23,19,15,19,18],
[32,0,30,21,28,30,17,25,23,26,23,29],
[27,21,0,22,30,21,13,29,16,21,21,26],
[30,30,29,0,38,31,23,35,31,36,35,31],
[24,23,21,13,0,22,20,27,32,26,27,28],
[30,21,30,20,29,0,26,30,33,31,28,25],
[38,34,38,28,31,25,0,36,33,39,29,31],
[28,26,22,16,24,21,15,0,27,20,22,21],
[32,28,35,20,19,18,18,24,0,28,28,32],
[36,25,30,15,25,20,12,31,23,0,19,23],
[32,28,30,16,24,23,22,29,23,32,0,29],
[33,22,25,20,23,26,20,30,19,28,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 189, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,27,30,29,29,23,26,27,26,26,28],
[25,0,30,27,27,28,22,31,23,29,23,27],
[24,21,0,26,23,23,22,31,23,27,25,26],
[21,24,25,0,23,27,19,29,21,25,20,21],
[22,24,28,28,0,29,25,27,27,25,27,26],
[22,23,28,24,22,0,24,27,27,26,21,25],
[28,29,29,32,26,27,0,30,28,28,25,26],
[25,20,20,22,24,24,21,0,24,23,21,23],
[24,28,28,30,24,24,23,27,0,26,28,22],
[25,22,24,26,26,25,23,28,25,0,24,26],
[25,28,26,31,24,30,26,30,23,27,0,28],
[23,24,25,30,25,26,25,28,29,25,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 190, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,24,30,25,28,24,23,25,28,29,26],
[33,0,32,30,25,30,28,25,25,35,31,28],
[27,19,0,18,21,28,28,18,19,24,26,19],
[21,21,33,0,24,26,26,22,18,29,30,25],
[26,26,30,27,0,29,28,27,26,32,29,21],
[23,21,23,25,22,0,23,19,19,28,28,23],
[27,23,23,25,23,28,0,19,23,29,27,23],
[28,26,33,29,24,32,32,0,27,34,34,27],
[26,26,32,33,25,32,28,24,0,34,31,23],
[23,16,27,22,19,23,22,17,17,0,21,23],
[22,20,25,21,22,23,24,17,20,30,0,21],
[25,23,32,26,30,28,28,24,28,28,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 191, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,27,21,22,20,26,25,25,21,25,21],
[25,0,27,18,28,24,20,26,25,22,25,24],
[24,24,0,17,22,23,26,24,19,21,29,24],
[30,33,34,0,27,28,33,31,25,26,33,32],
[29,23,29,24,0,24,27,30,28,21,29,22],
[31,27,28,23,27,0,26,30,23,25,29,24],
[25,31,25,18,24,25,0,27,26,24,27,23],
[26,25,27,20,21,21,24,0,21,20,24,24],
[26,26,32,26,23,28,25,30,0,23,27,27],
[30,29,30,25,30,26,27,31,28,0,28,24],
[26,26,22,18,22,22,24,27,24,23,0,21],
[30,27,27,19,29,27,28,27,24,27,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 192, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,28,28,30,23,30,23,34,25,27,31],
[25,0,28,30,35,26,24,25,38,33,25,31],
[23,23,0,26,36,25,28,32,31,29,27,29],
[23,21,25,0,32,32,27,33,30,35,30,27],
[21,16,15,19,0,26,21,18,24,23,19,17],
[28,25,26,19,25,0,29,19,25,24,22,27],
[21,27,23,24,30,22,0,20,28,24,26,23],
[28,26,19,18,33,32,31,0,28,32,18,23],
[17,13,20,21,27,26,23,23,0,28,17,14],
[26,18,22,16,28,27,27,19,23,0,19,24],
[24,26,24,21,32,29,25,33,34,32,0,25],
[20,20,22,24,34,24,28,28,37,27,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 193, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,24,16,27,15,25,29,14,14,21,19],
[33,0,32,25,25,27,29,27,30,27,29,34],
[27,19,0,18,27,26,27,29,22,22,23,26],
[35,26,33,0,28,22,27,34,31,24,27,37],
[24,26,24,23,0,16,25,29,16,17,19,25],
[36,24,25,29,35,0,35,34,25,17,24,33],
[26,22,24,24,26,16,0,25,22,19,18,27],
[22,24,22,17,22,17,26,0,17,17,20,25],
[37,21,29,20,35,26,29,34,0,24,27,30],
[37,24,29,27,34,34,32,34,27,0,31,30],
[30,22,28,24,32,27,33,31,24,20,0,28],
[32,17,25,14,26,18,24,26,21,21,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 194, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,30,29,26,32,31,24,26,26,26,37],
[23,0,30,31,24,30,29,29,29,29,26,32],
[21,21,0,31,23,27,26,27,21,21,23,31],
[22,20,20,0,22,30,24,27,22,22,20,27],
[25,27,28,29,0,24,28,26,21,25,21,28],
[19,21,24,21,27,0,22,24,25,21,15,28],
[20,22,25,27,23,29,0,26,24,24,22,31],
[27,22,24,24,25,27,25,0,22,22,28,32],
[25,22,30,29,30,26,27,29,0,21,24,33],
[25,22,30,29,26,30,27,29,30,0,25,26],
[25,25,28,31,30,36,29,23,27,26,0,31],
[14,19,20,24,23,23,20,19,18,25,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 195, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,21,27,30,26,36,19,21,36,23,17],
[34,0,38,34,38,21,51,34,30,36,38,42],
[30,13,0,17,16,26,32,9,34,26,19,17],
[24,17,34,0,24,21,34,34,34,30,34,24],
[21,13,35,27,0,34,40,40,34,36,27,25],
[25,30,25,30,17,0,30,17,17,30,25,30],
[15,0,19,17,11,21,0,7,21,26,8,32],
[32,17,42,17,11,34,44,0,34,26,22,32],
[30,21,17,17,17,34,30,17,0,34,17,25],
[15,15,25,21,15,21,25,25,17,0,25,19],
[28,13,32,17,24,26,43,29,34,26,0,24],
[34,9,34,27,26,21,19,19,26,32,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 196, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,28,41,39,33,40,21,32,27,31,20],
[21,0,24,25,29,21,29,29,28,40,27,21],
[23,27,0,23,29,20,23,22,25,29,30,12],
[10,26,28,0,15,13,21,14,25,29,29,11],
[12,22,22,36,0,23,23,10,17,21,23,11],
[18,30,31,38,28,0,31,16,29,31,29,11],
[11,22,28,30,28,20,0,20,28,31,26,14],
[30,22,29,37,41,35,31,0,26,36,30,26],
[19,23,26,26,34,22,23,25,0,27,25,20],
[24,11,22,22,30,20,20,15,24,0,22,11],
[20,24,21,22,28,22,25,21,26,29,0,15],
[31,30,39,40,40,40,37,25,31,40,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 197, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,25,31,29,30,33,37,32,31,29,32],
[29,0,27,22,31,25,27,30,26,35,27,27],
[26,24,0,33,29,32,27,30,32,25,32,30],
[20,29,18,0,27,26,30,28,25,26,23,25],
[22,20,22,24,0,27,21,28,21,20,23,20],
[21,26,19,25,24,0,21,35,26,28,31,28],
[18,24,24,21,30,30,0,25,26,25,23,23],
[14,21,21,23,23,16,26,0,29,22,24,19],
[19,25,19,26,30,25,25,22,0,28,23,25],
[20,16,26,25,31,23,26,29,23,0,23,20],
[22,24,19,28,28,20,28,27,28,28,0,26],
[19,24,21,26,31,23,28,32,26,31,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 198, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,33,30,24,26,32,10,28,14,25,42],
[31,0,19,26,24,29,25,19,26,26,25,25],
[18,32,0,22,27,31,25,23,28,17,31,26],
[21,25,29,0,27,25,23,16,18,9,31,26],
[27,27,24,24,0,26,22,26,14,13,28,21],
[25,22,20,26,25,0,22,30,12,26,31,26],
[19,26,26,28,29,29,0,26,26,19,29,25],
[41,32,28,35,25,21,25,0,18,35,31,36],
[23,25,23,33,37,39,25,33,0,27,22,33],
[37,25,34,42,38,25,32,16,24,0,38,41],
[26,26,20,20,23,20,22,20,29,13,0,26],
[9,26,25,25,30,25,26,15,18,10,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 199, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,17,27,30,27,19,24,22,23,27,25],
[24,0,17,25,26,35,23,33,32,26,33,28],
[34,34,0,36,30,31,33,39,34,23,26,27],
[24,26,15,0,19,24,13,22,30,27,24,22],
[21,25,21,32,0,29,28,29,35,26,29,26],
[24,16,20,27,22,0,18,25,23,20,25,17],
[32,28,18,38,23,33,0,31,34,28,31,27],
[27,18,12,29,22,26,20,0,28,23,29,22],
[29,19,17,21,16,28,17,23,0,20,26,21],
[28,25,28,24,25,31,23,28,31,0,23,29],
[24,18,25,27,22,26,20,22,25,28,0,16],
[26,23,24,29,25,34,24,29,30,22,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 51, 200, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbrcwd/mebbrcwd_12_51.csv", index=False, header=False)