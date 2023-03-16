
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg
from kemeny import sc

rep = 1
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,20,19,25,22,19,30,30,15,32,36,34,19],
[30,0,30,28,30,25,25,30,19,33,34,38,32],
[31,20,0,23,30,23,28,34,23,37,38,36,27],
[25,22,27,0,25,21,32,30,23,25,27,31,24],
[28,20,20,25,0,21,20,31,22,27,31,33,25],
[31,25,27,29,29,0,23,34,20,25,36,30,25],
[20,25,22,18,30,27,0,25,26,36,32,27,32],
[20,20,16,20,19,16,25,0,21,26,25,28,23],
[35,31,27,27,28,30,24,29,0,39,41,32,34],
[18,17,13,25,23,25,14,24,11,0,21,21,18],
[14,16,12,23,19,14,18,25,9,29,0,24,12],
[16,12,14,19,17,20,23,22,18,29,26,0,18],
[31,18,23,26,25,25,18,27,16,32,38,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 1, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,18,23,20,26,20,25,20,20,24,19,17],
[30,0,26,27,21,31,24,31,27,29,32,28,27],
[32,24,0,30,28,28,33,31,24,26,27,33,31],
[27,23,20,0,24,32,26,34,26,25,27,29,24],
[30,29,22,26,0,31,24,31,24,31,31,27,24],
[24,19,22,18,19,0,23,22,23,23,23,22,24],
[30,26,17,24,26,27,0,28,23,22,21,27,28],
[25,19,19,16,19,28,22,0,21,24,24,24,21],
[30,23,26,24,26,27,27,29,0,28,30,31,26],
[30,21,24,25,19,27,28,26,22,0,22,26,24],
[26,18,23,23,19,27,29,26,20,28,0,23,26],
[31,22,17,21,23,28,23,26,19,24,27,0,28],
[33,23,19,26,26,26,22,29,24,26,24,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 2, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,27,29,21,29,30,32,28,31,34,24,27],
[26,0,30,24,26,29,27,28,22,25,30,26,29],
[23,20,0,27,26,29,23,28,24,24,30,26,31],
[21,26,23,0,24,32,27,35,23,31,26,23,31],
[29,24,24,26,0,30,31,33,22,26,34,27,30],
[21,21,21,18,20,0,28,33,16,21,28,25,29],
[20,23,27,23,19,22,0,28,19,26,25,24,24],
[18,22,22,15,17,17,22,0,16,19,24,15,21],
[22,28,26,27,28,34,31,34,0,29,33,25,30],
[19,25,26,19,24,29,24,31,21,0,25,24,26],
[16,20,20,24,16,22,25,26,17,25,0,22,21],
[26,24,24,27,23,25,26,35,25,26,28,0,30],
[23,21,19,19,20,21,26,29,20,24,29,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 3, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,14,18,21,15,18,17,21,16,22,21,20],
[30,0,16,31,25,16,21,23,28,19,25,26,27],
[36,34,0,32,33,32,33,31,30,25,32,28,36],
[32,19,18,0,26,18,19,16,24,17,27,22,30],
[29,25,17,24,0,17,24,25,26,16,27,23,24],
[35,34,18,32,33,0,30,30,32,24,30,21,30],
[32,29,17,31,26,20,0,27,25,22,29,26,29],
[33,27,19,34,25,20,23,0,27,19,32,32,23],
[29,22,20,26,24,18,25,23,0,17,23,25,29],
[34,31,25,33,34,26,28,31,33,0,30,28,28],
[28,25,18,23,23,20,21,18,27,20,0,20,29],
[29,24,22,28,27,29,24,18,25,22,30,0,31],
[30,23,14,20,26,20,21,27,21,22,21,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 4, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,36,24,36,28,33,28,37,28,26,26,32],
[19,0,17,17,27,26,19,29,27,26,19,19,34],
[14,33,0,27,31,30,20,35,33,32,23,22,31],
[26,33,23,0,31,35,26,29,30,25,29,23,34],
[14,23,19,19,0,20,25,33,24,15,25,15,32],
[22,24,20,15,30,0,25,29,23,26,12,20,22],
[17,31,30,24,25,25,0,29,24,18,20,16,30],
[22,21,15,21,17,21,21,0,32,16,21,26,27],
[13,23,17,20,26,27,26,18,0,18,17,14,24],
[22,24,18,25,35,24,32,34,32,0,24,25,30],
[24,31,27,21,25,38,30,29,33,26,0,26,28],
[24,31,28,27,35,30,34,24,36,25,24,0,28],
[18,16,19,16,18,28,20,23,26,20,22,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 5, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,23,33,35,25,19,44,20,24,23,35,35],
[15,0,20,31,37,38,12,32,26,25,16,37,34],
[27,30,0,28,28,22,23,33,21,21,25,28,35],
[17,19,22,0,24,22,27,23,8,13,27,21,28],
[15,13,22,26,0,19,12,15,11,11,18,20,30],
[25,12,28,28,31,0,22,36,11,26,24,26,34],
[31,38,27,23,38,28,0,31,16,27,17,38,37],
[6,18,17,27,35,14,19,0,8,7,19,17,35],
[30,24,29,42,39,39,34,42,0,21,36,42,37],
[26,25,29,37,39,24,23,43,29,0,29,33,41],
[27,34,25,23,32,26,33,31,14,21,0,34,35],
[15,13,22,29,30,24,12,33,8,17,16,0,28],
[15,16,15,22,20,16,13,15,13,9,15,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 6, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,23,23,28,28,25,27,26,23,26,26,25],
[27,0,29,25,29,28,28,29,21,25,28,28,25],
[27,21,0,20,26,22,25,23,28,23,20,30,24],
[27,25,30,0,35,31,35,26,32,28,28,33,30],
[22,21,24,15,0,23,25,24,22,23,23,27,23],
[22,22,28,19,27,0,19,21,24,21,26,26,18],
[25,22,25,15,25,31,0,24,20,20,26,33,26],
[23,21,27,24,26,29,26,0,26,24,26,28,22],
[24,29,22,18,28,26,30,24,0,24,29,30,32],
[27,25,27,22,27,29,30,26,26,0,28,35,33],
[24,22,30,22,27,24,24,24,21,22,0,29,21],
[24,22,20,17,23,24,17,22,20,15,21,0,19],
[25,25,26,20,27,32,24,28,18,17,29,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 7, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,30,30,23,27,30,28,28,24,21,24,26],
[19,0,25,20,23,25,25,26,24,24,25,23,19],
[20,25,0,18,26,22,21,32,21,21,21,22,19],
[20,30,32,0,24,33,36,32,29,27,24,24,28],
[27,27,24,26,0,28,30,33,23,26,29,25,22],
[23,25,28,17,22,0,27,24,24,21,23,23,24],
[20,25,29,14,20,23,0,27,26,24,24,22,21],
[22,24,18,18,17,26,23,0,21,17,17,16,17],
[22,26,29,21,27,26,24,29,0,24,27,21,19],
[26,26,29,23,24,29,26,33,26,0,21,16,22],
[29,25,29,26,21,27,26,33,23,29,0,22,23],
[26,27,28,26,25,27,28,34,29,34,28,0,24],
[24,31,31,22,28,26,29,33,31,28,27,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 8, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,14,18,19,15,13,20,21,16,20,13,21],
[26,0,16,21,23,22,24,22,17,17,17,16,20],
[36,34,0,26,28,20,21,22,29,23,28,17,22],
[32,29,24,0,30,18,24,30,29,23,22,20,27],
[31,27,22,20,0,21,15,23,27,17,28,15,27],
[35,28,30,32,29,0,34,24,33,24,27,28,33],
[37,26,29,26,35,16,0,26,26,27,29,21,37],
[30,28,28,20,27,26,24,0,25,20,24,16,30],
[29,33,21,21,23,17,24,25,0,23,22,18,26],
[34,33,27,27,33,26,23,30,27,0,32,24,38],
[30,33,22,28,22,23,21,26,28,18,0,25,30],
[37,34,33,30,35,22,29,34,32,26,25,0,30],
[29,30,28,23,23,17,13,20,24,12,20,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 9, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,30,13,28,17,25,22,25,25,21,24,17],
[26,0,24,24,28,25,30,23,29,26,23,22,25],
[20,26,0,19,28,28,20,27,21,23,25,28,25],
[37,26,31,0,36,23,25,32,33,36,22,27,26],
[22,22,22,14,0,16,22,19,24,22,20,12,20],
[33,25,22,27,34,0,26,34,23,26,24,25,26],
[25,20,30,25,28,24,0,35,28,28,28,28,31],
[28,27,23,18,31,16,15,0,21,22,16,25,26],
[25,21,29,17,26,27,22,29,0,19,22,23,21],
[25,24,27,14,28,24,22,28,31,0,25,24,28],
[29,27,25,28,30,26,22,34,28,25,0,22,29],
[26,28,22,23,38,25,22,25,27,26,28,0,27],
[33,25,25,24,30,24,19,24,29,22,21,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 10, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,25,25,29,35,24,26,28,26,26,28,26],
[21,0,15,14,19,24,22,20,19,19,18,15,17],
[25,35,0,21,27,28,24,27,26,27,28,24,23],
[25,36,29,0,34,34,20,26,29,27,27,30,23],
[21,31,23,16,0,28,22,23,24,24,22,25,19],
[15,26,22,16,22,0,16,19,19,19,19,21,19],
[26,28,26,30,28,34,0,24,28,28,31,28,20],
[24,30,23,24,27,31,26,0,32,23,26,31,20],
[22,31,24,21,26,31,22,18,0,23,26,26,18],
[24,31,23,23,26,31,22,27,27,0,29,32,23],
[24,32,22,23,28,31,19,24,24,21,0,23,18],
[22,35,26,20,25,29,22,19,24,18,27,0,26],
[24,33,27,27,31,31,30,30,32,27,32,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 11, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,26,25,22,27,27,21,21,27,28,23,29],
[23,0,21,17,21,21,22,16,20,18,23,18,25],
[24,29,0,27,26,26,29,26,22,25,31,23,30],
[25,33,23,0,26,24,32,23,23,26,29,22,29],
[28,29,24,24,0,22,27,22,21,26,29,24,35],
[23,29,24,26,28,0,29,23,23,26,26,27,24],
[23,28,21,18,23,21,0,19,23,22,24,21,26],
[29,34,24,27,28,27,31,0,27,23,29,29,32],
[29,30,28,27,29,27,27,23,0,28,30,23,33],
[23,32,25,24,24,24,28,27,22,0,29,23,25],
[22,27,19,21,21,24,26,21,20,21,0,20,26],
[27,32,27,28,26,23,29,21,27,27,30,0,28],
[21,25,20,21,15,26,24,18,17,25,24,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 12, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,24,33,25,16,26,21,25,23,31,32,32],
[26,0,25,34,29,24,26,23,27,26,32,34,31],
[26,25,0,26,21,23,25,22,24,26,29,32,25],
[17,16,24,0,24,15,20,13,22,26,26,30,23],
[25,21,29,26,0,23,27,21,31,29,29,33,27],
[34,26,27,35,27,0,33,26,27,25,31,36,26],
[24,24,25,30,23,17,0,20,23,19,22,29,28],
[29,27,28,37,29,24,30,0,31,34,31,34,35],
[25,23,26,28,19,23,27,19,0,25,24,33,27],
[27,24,24,24,21,25,31,16,25,0,33,32,26],
[19,18,21,24,21,19,28,19,26,17,0,27,20],
[18,16,18,20,17,14,21,16,17,18,23,0,19],
[18,19,25,27,23,24,22,15,23,24,30,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 13, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,25,27,26,31,31,33,36,32,29,32,30],
[22,0,23,29,22,26,23,26,30,29,28,32,29],
[25,27,0,26,27,24,30,31,30,33,30,34,32],
[23,21,24,0,24,24,24,29,30,29,25,29,29],
[24,28,23,26,0,28,29,33,36,31,30,33,28],
[19,24,26,26,22,0,25,33,30,28,26,31,29],
[19,27,20,26,21,25,0,30,28,27,24,31,26],
[17,24,19,21,17,17,20,0,25,26,23,23,21],
[14,20,20,20,14,20,22,25,0,26,22,27,23],
[18,21,17,21,19,22,23,24,24,0,23,30,23],
[21,22,20,25,20,24,26,27,28,27,0,28,25],
[18,18,16,21,17,19,19,27,23,20,22,0,22],
[20,21,18,21,22,21,24,29,27,27,25,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 14, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,29,24,29,30,28,24,28,29,25,25,25],
[22,0,19,26,31,28,30,22,19,30,22,23,24],
[21,31,0,29,31,33,28,23,26,35,23,28,22],
[26,24,21,0,28,28,24,23,26,25,31,27,24],
[21,19,19,22,0,25,24,24,23,23,19,25,15],
[20,22,17,22,25,0,22,20,20,27,19,25,22],
[22,20,22,26,26,28,0,19,21,24,26,26,19],
[26,28,27,27,26,30,31,0,25,29,27,27,25],
[22,31,24,24,27,30,29,25,0,32,23,29,26],
[21,20,15,25,27,23,26,21,18,0,23,22,19],
[25,28,27,19,31,31,24,23,27,27,0,30,25],
[25,27,22,23,25,25,24,23,21,28,20,0,19],
[25,26,28,26,35,28,31,25,24,31,25,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 15, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,24,25,24,23,28,29,28,26,22,36,36],
[23,0,18,20,16,18,22,18,29,14,11,20,20],
[26,32,0,21,26,33,23,32,34,28,24,26,26],
[25,30,29,0,23,28,27,24,25,30,21,32,31],
[26,34,24,27,0,31,29,35,42,26,19,31,32],
[27,32,17,22,19,0,20,25,30,12,16,23,19],
[22,28,27,23,21,30,0,36,31,31,22,36,32],
[21,32,18,26,15,25,14,0,33,26,19,33,31],
[22,21,16,25,8,20,19,17,0,21,14,25,22],
[24,36,22,20,24,38,19,24,29,0,30,28,26],
[28,39,26,29,31,34,28,31,36,20,0,32,35],
[14,30,24,18,19,27,14,17,25,22,18,0,24],
[14,30,24,19,18,31,18,19,28,24,15,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 16, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,27,14,19,25,40,24,26,32,27,29,27],
[21,0,20,17,13,13,32,22,20,29,22,24,18],
[23,30,0,26,15,32,37,29,15,35,20,31,27],
[36,33,24,0,20,35,29,28,23,35,20,32,36],
[31,37,35,30,0,35,42,32,19,36,25,34,29],
[25,37,18,15,15,0,35,32,20,33,31,32,32],
[10,18,13,21,8,15,0,29,15,33,17,14,24],
[26,28,21,22,18,18,21,0,21,37,16,14,30],
[24,30,35,27,31,30,35,29,0,42,36,31,39],
[18,21,15,15,14,17,17,13,8,0,20,15,27],
[23,28,30,30,25,19,33,34,14,30,0,24,33],
[21,26,19,18,16,18,36,36,19,35,26,0,28],
[23,32,23,14,21,18,26,20,11,23,17,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 17, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,31,27,21,35,25,27,36,35,30,34,36],
[23,0,32,22,24,30,27,18,31,33,30,29,33],
[19,18,0,21,16,33,20,21,20,28,21,21,31],
[23,28,29,0,33,32,28,26,24,21,18,33,33],
[29,26,34,17,0,34,28,25,29,32,28,29,28],
[15,20,17,18,16,0,23,22,20,27,23,17,26],
[25,23,30,22,22,27,0,22,29,30,33,31,32],
[23,32,29,24,25,28,28,0,25,30,28,26,29],
[14,19,30,26,21,30,21,25,0,31,34,31,29],
[15,17,22,29,18,23,20,20,19,0,27,27,33],
[20,20,29,32,22,27,17,22,16,23,0,29,32],
[16,21,29,17,21,33,19,24,19,23,21,0,31],
[14,17,19,17,22,24,18,21,21,17,18,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 18, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,21,23,27,22,22,15,12,22,23,20,26],
[27,0,26,25,25,28,25,22,20,22,26,26,28],
[29,24,0,23,27,22,25,15,21,17,20,18,30],
[27,25,27,0,28,25,32,20,21,25,25,28,31],
[23,25,23,22,0,25,24,18,19,24,22,23,27],
[28,22,28,25,25,0,25,20,17,26,25,22,28],
[28,25,25,18,26,25,0,20,20,24,21,20,28],
[35,28,35,30,32,30,30,0,25,25,29,31,34],
[38,30,29,29,31,33,30,25,0,22,29,25,33],
[28,28,33,25,26,24,26,25,28,0,30,26,28],
[27,24,30,25,28,25,29,21,21,20,0,24,29],
[30,24,32,22,27,28,30,19,25,24,26,0,29],
[24,22,20,19,23,22,22,16,17,22,21,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 19, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,28,24,35,17,31,29,41,28,50,28,30],
[14,0,31,15,19,17,9,32,34,22,28,31,31],
[22,19,0,15,26,9,22,23,32,23,35,22,24],
[26,35,35,0,35,35,22,23,26,35,35,29,29],
[15,31,24,15,0,18,24,24,26,24,36,18,25],
[33,33,41,15,32,0,37,29,32,35,41,36,44],
[19,41,28,28,26,13,0,28,32,19,26,28,29],
[21,18,27,27,26,21,22,0,27,29,29,27,21],
[9,16,18,24,24,18,18,23,0,26,33,18,25],
[22,28,27,15,26,15,31,21,24,0,41,27,22],
[0,22,15,15,14,9,24,21,17,9,0,15,22],
[22,19,28,21,32,14,22,23,32,23,35,0,15],
[20,19,26,21,25,6,21,29,25,28,28,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 20, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,23,24,20,25,30,25,26,23,23,28,23],
[27,0,24,24,26,22,29,31,26,24,23,23,22],
[27,26,0,16,20,22,25,23,24,21,22,23,23],
[26,26,34,0,23,27,32,23,31,26,26,25,28],
[30,24,30,27,0,30,29,28,27,25,20,28,26],
[25,28,28,23,20,0,27,25,20,21,20,22,26],
[20,21,25,18,21,23,0,24,25,18,17,21,22],
[25,19,27,27,22,25,26,0,27,23,25,25,23],
[24,24,26,19,23,30,25,23,0,23,21,22,23],
[27,26,29,24,25,29,32,27,27,0,30,27,25],
[27,27,28,24,30,30,33,25,29,20,0,29,24],
[22,27,27,25,22,28,29,25,28,23,21,0,25],
[27,28,27,22,24,24,28,27,27,25,26,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 21, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,0,26,17,24,24,0,50,0,0,50,26],
[41,0,17,50,41,41,24,41,50,24,17,50,41],
[50,33,0,50,50,24,33,33,50,24,41,50,50],
[24,0,0,0,24,24,24,24,33,24,0,33,24],
[33,9,0,26,0,24,24,9,33,24,0,33,9],
[26,9,26,26,26,0,33,9,26,0,17,50,26],
[26,26,17,26,26,17,0,26,26,0,17,50,26],
[50,9,17,26,41,41,24,0,50,24,17,50,50],
[0,0,0,17,17,24,24,0,0,0,0,24,17],
[50,26,26,26,26,50,50,26,50,0,17,50,26],
[50,33,9,50,50,33,33,33,50,33,0,50,50],
[0,0,0,17,17,0,0,0,26,0,0,0,17],
[24,9,0,26,41,24,24,0,33,24,0,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 22, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,46,37,34,35,22,34,38,36,25,21,47],
[15,0,49,31,43,27,24,24,40,41,27,23,40],
[4,1,0,16,13,20,1,7,11,18,4,7,18],
[13,19,34,0,28,24,18,6,16,17,28,23,29],
[16,7,37,22,0,25,13,7,16,30,15,13,41],
[15,23,30,26,25,0,19,19,22,29,27,22,22],
[28,26,49,32,37,31,0,29,26,35,25,29,40],
[16,26,43,44,43,31,21,0,32,29,34,29,37],
[12,10,39,34,34,28,24,18,0,23,33,33,40],
[14,9,32,33,20,21,15,21,27,0,21,23,27],
[25,23,46,22,35,23,25,16,17,29,0,34,35],
[29,27,43,27,37,28,21,21,17,27,16,0,44],
[3,10,32,21,9,28,10,13,10,23,15,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 23, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,27,17,20,28,23,22,27,16,19,25,25],
[28,0,33,30,36,35,38,32,33,24,29,34,29],
[23,17,0,17,20,13,16,33,21,18,19,18,6],
[33,20,33,0,27,32,26,23,32,30,22,33,29],
[30,14,30,23,0,35,29,27,27,26,23,22,30],
[22,15,37,18,15,0,21,29,22,25,21,22,25],
[27,12,34,24,21,29,0,30,32,27,32,26,28],
[28,18,17,27,23,21,20,0,30,20,17,17,21],
[23,17,29,18,23,28,18,20,0,17,11,10,28],
[34,26,32,20,24,25,23,30,33,0,26,22,21],
[31,21,31,28,27,29,18,33,39,24,0,32,29],
[25,16,32,17,28,28,24,33,40,28,18,0,31],
[25,21,44,21,20,25,22,29,22,29,21,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 24, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,28,21,19,33,21,24,26,23,21,26,29],
[25,0,22,12,18,22,22,26,24,24,15,22,22],
[22,28,0,21,27,29,26,27,28,27,17,31,31],
[29,38,29,0,27,30,28,26,32,28,23,27,28],
[31,32,23,23,0,30,30,32,29,26,25,21,29],
[17,28,21,20,20,0,17,26,24,26,21,19,25],
[29,28,24,22,20,33,0,29,29,26,21,23,27],
[26,24,23,24,18,24,21,0,22,25,22,23,26],
[24,26,22,18,21,26,21,28,0,21,16,19,25],
[27,26,23,22,24,24,24,25,29,0,18,22,31],
[29,35,33,27,25,29,29,28,34,32,0,31,34],
[24,28,19,23,29,31,27,27,31,28,19,0,34],
[21,28,19,22,21,25,23,24,25,19,16,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 25, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,27,25,34,25,25,29,26,33,22,29,19],
[30,0,29,23,36,23,28,25,24,39,32,28,26],
[23,21,0,21,36,29,25,23,25,21,23,20,27],
[25,27,29,0,35,28,25,25,27,36,31,26,26],
[16,14,14,15,0,19,15,14,19,19,19,19,19],
[25,27,21,22,31,0,26,24,33,32,33,33,26],
[25,22,25,25,35,24,0,23,26,32,14,25,20],
[21,25,27,25,36,26,27,0,32,32,17,26,16],
[24,26,25,23,31,17,24,18,0,33,26,26,26],
[17,11,29,14,31,18,18,18,17,0,15,27,15],
[28,18,27,19,31,17,36,33,24,35,0,27,31],
[21,22,30,24,31,17,25,24,24,23,23,0,23],
[31,24,23,24,31,24,30,34,24,35,19,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 26, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,35,27,17,32,26,35,24,22,23,32,32],
[20,0,30,31,20,22,30,33,19,22,36,39,38],
[15,20,0,22,19,22,19,24,16,10,32,22,27],
[23,19,28,0,23,29,29,46,27,23,34,36,29],
[33,30,31,27,0,39,30,31,13,21,28,37,28],
[18,28,28,21,11,0,18,23,10,20,30,35,22],
[24,20,31,21,20,32,0,32,24,27,41,35,29],
[15,17,26,4,19,27,18,0,19,6,26,21,21],
[26,31,34,23,37,40,26,31,0,14,30,38,33],
[28,28,40,27,29,30,23,44,36,0,28,44,32],
[27,14,18,16,22,20,9,24,20,22,0,22,22],
[18,11,28,14,13,15,15,29,12,6,28,0,13],
[18,12,23,21,22,28,21,29,17,18,28,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 27, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,2,12,13,7,32,11,10,17,13,16,11],
[39,0,20,25,23,19,23,30,6,34,19,29,25],
[48,30,0,29,39,31,37,25,19,40,46,31,20],
[38,25,21,0,34,13,31,21,10,39,25,21,26],
[37,27,11,16,0,18,31,30,8,33,25,21,25],
[43,31,19,37,32,0,39,33,28,31,25,43,33],
[18,27,13,19,19,11,0,21,4,23,20,17,6],
[39,20,25,29,20,17,29,0,8,33,23,35,29],
[40,44,31,40,42,22,46,42,0,44,35,31,42],
[33,16,10,11,17,19,27,17,6,0,22,17,10],
[37,31,4,25,25,25,30,27,15,28,0,27,20],
[34,21,19,29,29,7,33,15,19,33,23,0,19],
[39,25,30,24,25,17,44,21,8,40,30,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 28, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,25,29,22,32,24,26,24,24,25,27,23],
[20,0,21,20,22,24,21,26,20,22,23,19,19],
[25,29,0,26,23,28,25,25,24,29,26,26,23],
[21,30,24,0,27,24,17,24,26,27,29,25,26],
[28,28,27,23,0,29,26,26,22,25,30,26,22],
[18,26,22,26,21,0,21,19,23,22,27,22,19],
[26,29,25,33,24,29,0,29,26,30,26,24,24],
[24,24,25,26,24,31,21,0,21,25,27,20,25],
[26,30,26,24,28,27,24,29,0,25,25,25,23],
[26,28,21,23,25,28,20,25,25,0,28,26,20],
[25,27,24,21,20,23,24,23,25,22,0,21,20],
[23,31,24,25,24,28,26,30,25,24,29,0,21],
[27,31,27,24,28,31,26,25,27,30,30,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 29, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,23,23,21,25,17,24,28,26,27,24,26],
[24,0,23,23,26,22,15,22,25,24,26,24,22],
[27,27,0,27,31,25,25,28,28,25,31,26,27],
[27,27,23,0,29,22,19,26,25,24,24,23,28],
[29,24,19,21,0,18,15,22,25,27,21,24,24],
[25,28,25,28,32,0,20,31,28,30,31,30,29],
[33,35,25,31,35,30,0,29,36,29,31,32,35],
[26,28,22,24,28,19,21,0,27,31,30,26,25],
[22,25,22,25,25,22,14,23,0,27,25,22,22],
[24,26,25,26,23,20,21,19,23,0,25,26,22],
[23,24,19,26,29,19,19,20,25,25,0,24,23],
[26,26,24,27,26,20,18,24,28,24,26,0,26],
[24,28,23,22,26,21,15,25,28,28,27,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 30, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,28,21,26,25,22,29,26,29,27,29,32],
[27,0,25,23,22,19,29,30,19,22,23,24,25],
[22,25,0,19,24,24,27,25,21,24,26,29,30],
[29,27,31,0,24,20,31,29,24,29,26,32,29],
[24,28,26,26,0,22,25,28,26,20,28,24,30],
[25,31,26,30,28,0,21,29,24,31,29,32,30],
[28,21,23,19,25,29,0,28,22,28,24,25,27],
[21,20,25,21,22,21,22,0,18,23,23,21,25],
[24,31,29,26,24,26,28,32,0,30,25,33,32],
[21,28,26,21,30,19,22,27,20,0,22,21,22],
[23,27,24,24,22,21,26,27,25,28,0,28,27],
[21,26,21,18,26,18,25,29,17,29,22,0,27],
[18,25,20,21,20,20,23,25,18,28,23,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 31, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,34,48,24,34,48,34,15,34,48,29,48],
[16,0,26,40,7,24,38,26,5,26,38,21,38],
[16,24,0,45,7,29,43,31,10,36,48,12,33],
[2,10,5,0,5,19,43,29,15,34,48,0,33],
[26,43,43,45,0,29,43,31,10,48,48,31,43],
[16,26,21,31,21,0,26,12,15,50,31,2,16],
[2,12,7,7,7,24,0,2,15,26,5,2,16],
[16,24,19,21,19,38,48,0,29,38,38,16,14],
[35,45,40,35,40,35,35,21,0,40,40,35,35],
[16,24,14,16,2,0,24,12,10,0,19,2,14],
[2,12,2,2,2,19,45,12,10,31,0,2,16],
[21,29,38,50,19,48,48,34,15,48,48,0,38],
[2,12,17,17,7,34,34,36,15,36,34,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 32, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,28,24,25,25,22,25,21,26,33,25,21],
[21,0,27,17,25,22,21,23,17,27,24,23,25],
[22,23,0,30,28,24,22,18,16,24,30,26,24],
[26,33,20,0,26,24,18,23,14,27,28,25,25],
[25,25,22,24,0,25,24,14,17,21,33,26,24],
[25,28,26,26,25,0,19,21,25,34,28,30,28],
[28,29,28,32,26,31,0,26,23,29,33,33,31],
[25,27,32,27,36,29,24,0,24,28,34,32,28],
[29,33,34,36,33,25,27,26,0,29,32,27,31],
[24,23,26,23,29,16,21,22,21,0,29,21,26],
[17,26,20,22,17,22,17,16,18,21,0,19,13],
[25,27,24,25,24,20,17,18,23,29,31,0,27],
[29,25,26,25,26,22,19,22,19,24,37,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 33, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,21,18,16,25,36,27,18,10,16,21,25],
[31,0,24,31,25,27,29,41,26,23,26,27,27],
[29,26,0,17,21,29,31,26,25,19,31,23,29],
[32,19,33,0,24,25,35,46,30,30,30,21,29],
[34,25,29,26,0,38,34,41,32,24,35,25,31],
[25,23,21,25,12,0,23,27,16,18,22,14,24],
[14,21,19,15,16,27,0,22,22,10,18,21,27],
[23,9,24,4,9,23,28,0,17,13,16,11,21],
[32,24,25,20,18,34,28,33,0,25,33,24,30],
[40,27,31,20,26,32,40,37,25,0,27,30,30],
[34,24,19,20,15,28,32,34,17,23,0,28,18],
[29,23,27,29,25,36,29,39,26,20,22,0,29],
[25,23,21,21,19,26,23,29,20,20,32,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 34, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,25,22,22,24,21,18,28,21,23,19,21],
[26,0,30,22,29,29,23,22,25,27,27,21,23],
[25,20,0,20,21,22,23,15,23,21,23,18,14],
[28,28,30,0,25,30,27,18,24,17,26,22,19],
[28,21,29,25,0,23,23,20,27,21,25,26,25],
[26,21,28,20,27,0,21,22,23,18,25,23,16],
[29,27,27,23,27,29,0,22,28,19,31,26,22],
[32,28,35,32,30,28,28,0,31,25,28,28,26],
[22,25,27,26,23,27,22,19,0,20,27,22,20],
[29,23,29,33,29,32,31,25,30,0,30,25,19],
[27,23,27,24,25,25,19,22,23,20,0,21,20],
[31,29,32,28,24,27,24,22,28,25,29,0,22],
[29,27,36,31,25,34,28,24,30,31,30,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 35, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,15,12,15,24,6,16,26,17,14,24,6],
[34,0,21,21,20,39,6,25,42,37,43,34,22],
[35,29,0,20,23,46,5,26,45,35,34,34,20],
[38,29,30,0,28,39,8,30,48,30,35,38,27],
[35,30,27,22,0,27,26,27,37,38,34,17,30],
[26,11,4,11,23,0,5,18,23,20,14,15,21],
[44,44,45,42,24,45,0,27,42,45,43,32,40],
[34,25,24,20,23,32,23,0,44,25,24,11,23],
[24,8,5,2,13,27,8,6,0,10,4,16,4],
[33,13,15,20,12,30,5,25,40,0,34,24,30],
[36,7,16,15,16,36,7,26,46,16,0,27,15],
[26,16,16,12,33,35,18,39,34,26,23,0,23],
[44,28,30,23,20,29,10,27,46,20,35,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 36, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,24,22,17,19,22,19,22,20,28,25,21],
[21,0,21,27,22,27,28,27,24,20,29,30,24],
[26,29,0,25,21,24,25,28,23,21,27,27,21],
[28,23,25,0,16,24,21,22,24,16,26,32,28],
[33,28,29,34,0,28,29,27,26,25,29,31,29],
[31,23,26,26,22,0,23,27,28,21,25,28,25],
[28,22,25,29,21,27,0,23,25,23,24,32,27],
[31,23,22,28,23,23,27,0,27,22,28,33,29],
[28,26,27,26,24,22,25,23,0,19,28,30,27],
[30,30,29,34,25,29,27,28,31,0,29,28,30],
[22,21,23,24,21,25,26,22,22,21,0,28,22],
[25,20,23,18,19,22,18,17,20,22,22,0,17],
[29,26,29,22,21,25,23,21,23,20,28,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 37, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,20,24,22,26,25,21,18,25,21,22,20],
[26,0,20,25,26,28,25,27,28,27,26,25,24],
[30,30,0,30,26,29,29,26,26,34,27,21,23],
[26,25,20,0,25,34,24,21,23,25,22,25,18],
[28,24,24,25,0,29,24,22,23,29,21,21,20],
[24,22,21,16,21,0,19,25,24,25,21,22,19],
[25,25,21,26,26,31,0,24,21,27,28,22,21],
[29,23,24,29,28,25,26,0,32,31,22,26,24],
[32,22,24,27,27,26,29,18,0,27,21,23,21],
[25,23,16,25,21,25,23,19,23,0,19,23,17],
[29,24,23,28,29,29,22,28,29,31,0,32,26],
[28,25,29,25,29,28,28,24,27,27,18,0,23],
[30,26,27,32,30,31,29,26,29,33,24,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 38, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,35,24,26,19,23,19,25,23,17,31,12],
[30,0,41,26,22,13,24,33,25,31,21,32,19],
[15,9,0,17,9,4,10,19,14,18,8,9,10],
[26,24,33,0,24,10,22,35,22,25,20,28,19],
[24,28,41,26,0,22,26,31,27,30,29,32,24],
[31,37,46,40,28,0,29,36,36,33,28,38,25],
[27,26,40,28,24,21,0,33,26,29,15,35,19],
[31,17,31,15,19,14,17,0,18,19,14,27,15],
[25,25,36,28,23,14,24,32,0,30,16,28,18],
[27,19,32,25,20,17,21,31,20,0,18,29,25],
[33,29,42,30,21,22,35,36,34,32,0,39,17],
[19,18,41,22,18,12,15,23,22,21,11,0,13],
[38,31,40,31,26,25,31,35,32,25,33,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 39, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,24,18,24,20,19,18,22,25,20,26,18],
[29,0,25,29,25,29,25,24,32,32,29,26,26],
[26,25,0,23,26,27,29,22,28,28,28,29,21],
[32,21,27,0,29,28,25,20,22,29,24,23,18],
[26,25,24,21,0,26,27,24,24,25,22,26,23],
[30,21,23,22,24,0,25,24,28,30,26,24,22],
[31,25,21,25,23,25,0,23,26,31,31,29,26],
[32,26,28,30,26,26,27,0,30,30,31,28,24],
[28,18,22,28,26,22,24,20,0,33,24,21,15],
[25,18,22,21,25,20,19,20,17,0,24,24,18],
[30,21,22,26,28,24,19,19,26,26,0,23,22],
[24,24,21,27,24,26,21,22,29,26,27,0,22],
[32,24,29,32,27,28,24,26,35,32,28,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 40, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,33,24,19,24,21,26,27,20,29,24,27],
[28,0,37,32,23,28,18,34,25,23,27,27,26],
[17,13,0,24,16,19,15,24,18,14,24,21,20],
[26,18,26,0,22,27,17,26,25,19,24,24,23],
[31,27,34,28,0,27,23,32,28,22,25,26,26],
[26,22,31,23,23,0,25,27,28,21,24,28,27],
[29,32,35,33,27,25,0,31,24,29,28,25,29],
[24,16,26,24,18,23,19,0,23,14,23,15,24],
[23,25,32,25,22,22,26,27,0,19,27,26,30],
[30,27,36,31,28,29,21,36,31,0,27,25,29],
[21,23,26,26,25,26,22,27,23,23,0,25,24],
[26,23,29,26,24,22,25,35,24,25,25,0,22],
[23,24,30,27,24,23,21,26,20,21,26,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 41, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,27,31,27,19,36,25,27,22,25,28,19],
[21,0,33,33,33,21,37,25,30,21,23,31,15],
[23,17,0,29,23,20,31,27,35,23,18,32,23],
[19,17,21,0,23,15,21,20,30,20,19,15,10],
[23,17,27,27,0,23,34,21,26,21,25,21,17],
[31,29,30,35,27,0,31,31,30,23,31,28,27],
[14,13,19,29,16,19,0,22,26,19,17,15,13],
[25,25,23,30,29,19,28,0,18,16,21,23,16],
[23,20,15,20,24,20,24,32,0,8,18,23,11],
[28,29,27,30,29,27,31,34,42,0,35,23,27],
[25,27,32,31,25,19,33,29,32,15,0,21,28],
[22,19,18,35,29,22,35,27,27,27,29,0,20],
[31,35,27,40,33,23,37,34,39,23,22,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 42, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,27,33,13,20,18,29,17,19,29,25,33],
[31,0,19,41,17,25,30,38,23,20,28,17,41],
[23,31,0,33,18,35,33,28,19,32,41,27,41],
[17,9,17,0,9,11,1,22,7,9,19,8,29],
[37,33,32,41,0,25,30,23,23,32,43,29,43],
[30,25,15,39,25,0,17,22,18,26,35,32,25],
[32,20,17,49,20,33,0,22,28,27,29,28,35],
[21,12,22,28,27,28,28,0,20,19,29,21,35],
[33,27,31,43,27,32,22,30,0,27,37,26,47],
[31,30,18,41,18,24,23,31,23,0,35,39,31],
[21,22,9,31,7,15,21,21,13,15,0,14,35],
[25,33,23,42,21,18,22,29,24,11,36,0,36],
[17,9,9,21,7,25,15,15,3,19,15,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 43, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,32,32,50,50,25,50,50,32,43,7,50],
[18,0,7,25,18,25,18,25,25,18,18,18,50],
[18,43,0,25,18,25,18,25,25,18,18,18,43],
[18,25,25,0,43,18,18,43,25,43,18,18,43],
[0,32,32,7,0,25,25,25,25,25,18,0,50],
[0,25,25,32,25,0,18,32,25,25,0,0,25],
[25,32,32,32,25,32,0,32,32,25,25,0,32],
[0,25,25,7,25,18,18,0,25,25,18,0,25],
[0,25,25,25,25,25,18,25,0,25,0,0,25],
[18,32,32,7,25,25,25,25,25,0,18,25,50],
[7,32,32,32,32,50,25,32,50,32,0,7,32],
[43,32,32,32,50,50,50,50,50,25,43,0,50],
[0,0,7,7,0,25,18,25,25,0,18,0,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 44, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,31,39,38,31,21,30,37,31,29,31,20],
[19,0,28,26,24,22,21,29,26,22,22,20,23],
[19,22,0,19,19,20,15,22,25,17,16,18,14],
[11,24,31,0,23,23,9,23,28,20,17,14,21],
[12,26,31,27,0,24,18,21,20,16,16,16,18],
[19,28,30,27,26,0,21,26,32,15,23,21,18],
[29,29,35,41,32,29,0,35,40,29,30,23,26],
[20,21,28,27,29,24,15,0,23,23,15,18,22],
[13,24,25,22,30,18,10,27,0,22,27,21,13],
[19,28,33,30,34,35,21,27,28,0,28,22,24],
[21,28,34,33,34,27,20,35,23,22,0,21,28],
[19,30,32,36,34,29,27,32,29,28,29,0,20],
[30,27,36,29,32,32,24,28,37,26,22,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 45, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,23,23,23,33,30,24,27,33,32,30,23],
[31,0,27,27,32,31,27,30,32,38,35,24,24],
[27,23,0,22,30,30,29,25,28,30,28,23,29],
[27,23,28,0,34,29,27,26,33,33,30,25,24],
[27,18,20,16,0,23,22,22,24,37,21,22,18],
[17,19,20,21,27,0,29,24,23,27,31,25,17],
[20,23,21,23,28,21,0,22,27,28,30,24,19],
[26,20,25,24,28,26,28,0,28,28,26,20,23],
[23,18,22,17,26,27,23,22,0,28,29,18,19],
[17,12,20,17,13,23,22,22,22,0,24,21,16],
[18,15,22,20,29,19,20,24,21,26,0,18,18],
[20,26,27,25,28,25,26,30,32,29,32,0,24],
[27,26,21,26,32,33,31,27,31,34,32,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 46, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,22,22,21,18,19,21,20,23,25,22,22],
[30,0,23,23,18,18,20,26,25,26,22,23,31],
[28,27,0,22,21,23,17,23,23,22,20,23,27],
[28,27,28,0,27,28,24,35,21,24,26,30,33],
[29,32,29,23,0,27,23,33,22,28,28,26,32],
[32,32,27,22,23,0,23,26,24,25,26,25,28],
[31,30,33,26,27,27,0,30,22,27,25,32,34],
[29,24,27,15,17,24,20,0,24,22,19,21,29],
[30,25,27,29,28,26,28,26,0,30,24,31,30],
[27,24,28,26,22,25,23,28,20,0,24,22,31],
[25,28,30,24,22,24,25,31,26,26,0,25,32],
[28,27,27,20,24,25,18,29,19,28,25,0,30],
[28,19,23,17,18,22,16,21,20,19,18,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 47, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,25,27,34,26,29,30,30,29,34,26,34],
[21,0,26,24,26,24,24,26,36,18,28,20,34],
[25,24,0,30,33,30,29,28,28,27,24,22,43],
[23,26,20,0,22,21,20,33,26,22,19,22,27],
[16,24,17,28,0,22,22,24,20,17,25,17,24],
[24,26,20,29,28,0,24,31,33,24,29,25,32],
[21,26,21,30,28,26,0,31,24,21,28,30,37],
[20,24,22,17,26,19,19,0,28,15,21,21,26],
[20,14,22,24,30,17,26,22,0,13,28,19,30],
[21,32,23,28,33,26,29,35,37,0,25,30,29],
[16,22,26,31,25,21,22,29,22,25,0,23,32],
[24,30,28,28,33,25,20,29,31,20,27,0,32],
[16,16,7,23,26,18,13,24,20,21,18,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 48, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,18,20,11,25,22,20,23,27,22,18,21],
[25,0,18,19,16,17,21,23,27,18,22,18,24],
[32,32,0,28,22,27,23,25,29,31,22,27,22],
[30,31,22,0,25,19,33,21,22,33,28,25,26],
[39,34,28,25,0,32,28,24,32,34,28,33,33],
[25,33,23,31,18,0,29,27,33,33,24,22,21],
[28,29,27,17,22,21,0,21,26,30,23,25,22],
[30,27,25,29,26,23,29,0,36,27,28,34,28],
[27,23,21,28,18,17,24,14,0,29,23,20,23],
[23,32,19,17,16,17,20,23,21,0,13,23,16],
[28,28,28,22,22,26,27,22,27,37,0,23,23],
[32,32,23,25,17,28,25,16,30,27,27,0,27],
[29,26,28,24,17,29,28,22,27,34,27,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 49, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,25,32,26,30,29,31,25,21,27,27,31],
[23,0,21,25,22,27,23,24,29,12,21,17,24],
[25,29,0,31,27,30,23,31,31,22,24,29,28],
[18,25,19,0,28,28,21,32,26,20,24,21,30],
[24,28,23,22,0,29,27,27,30,17,29,19,29],
[20,23,20,22,21,0,18,26,23,15,19,26,24],
[21,27,27,29,23,32,0,30,28,26,30,26,27],
[19,26,19,18,23,24,20,0,25,14,22,18,29],
[25,21,19,24,20,27,22,25,0,14,18,15,25],
[29,38,28,30,33,35,24,36,36,0,33,36,35],
[23,29,26,26,21,31,20,28,32,17,0,29,28],
[23,33,21,29,31,24,24,32,35,14,21,0,31],
[19,26,22,20,21,26,23,21,25,15,22,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 50, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,30,33,24,31,21,28,22,31,24,27,25],
[15,0,21,28,24,21,15,20,18,25,22,18,24],
[20,29,0,26,25,24,20,20,20,32,24,20,24],
[17,22,24,0,23,20,21,25,17,21,19,23,17],
[26,26,25,27,0,29,27,27,20,26,24,23,17],
[19,29,26,30,21,0,17,21,14,27,19,24,20],
[29,35,30,29,23,33,0,29,24,31,27,28,26],
[22,30,30,25,23,29,21,0,19,30,23,25,22],
[28,32,30,33,30,36,26,31,0,29,30,25,26],
[19,25,18,29,24,23,19,20,21,0,24,21,14],
[26,28,26,31,26,31,23,27,20,26,0,23,22],
[23,32,30,27,27,26,22,25,25,29,27,0,25],
[25,26,26,33,33,30,24,28,24,36,28,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 51, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,28,27,32,27,32,28,26,30,26,28,31],
[28,0,25,25,27,28,28,29,26,28,27,24,29],
[22,25,0,22,28,20,31,33,24,27,26,27,27],
[23,25,28,0,23,25,26,27,25,28,24,29,26],
[18,23,22,27,0,21,29,25,22,29,24,26,28],
[23,22,30,25,29,0,28,29,26,28,27,27,28],
[18,22,19,24,21,22,0,22,17,19,19,18,22],
[22,21,17,23,25,21,28,0,23,24,21,22,25],
[24,24,26,25,28,24,33,27,0,28,26,27,28],
[20,22,23,22,21,22,31,26,22,0,24,21,25],
[24,23,24,26,26,23,31,29,24,26,0,28,31],
[22,26,23,21,24,23,32,28,23,29,22,0,26],
[19,21,23,24,22,22,28,25,22,25,19,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 52, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,24,25,18,24,24,33,28,23,25,22,21],
[29,0,21,31,24,26,25,36,26,18,28,28,30],
[26,29,0,35,26,27,24,33,30,24,28,25,32],
[25,19,15,0,22,25,19,37,23,21,28,28,27],
[32,26,24,28,0,31,25,35,32,26,30,31,25],
[26,24,23,25,19,0,21,31,29,23,26,28,19],
[26,25,26,31,25,29,0,37,31,33,28,26,28],
[17,14,17,13,15,19,13,0,19,10,21,25,23],
[22,24,20,27,18,21,19,31,0,30,23,24,22],
[27,32,26,29,24,27,17,40,20,0,30,29,26],
[25,22,22,22,20,24,22,29,27,20,0,25,17],
[28,22,25,22,19,22,24,25,26,21,25,0,22],
[29,20,18,23,25,31,22,27,28,24,33,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 53, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,20,23,20,18,24,26,23,24,16,26,23],
[35,0,25,25,25,30,27,25,28,27,25,29,24],
[30,25,0,22,28,26,32,25,25,29,22,29,29],
[27,25,28,0,25,23,23,19,26,23,19,23,29],
[30,25,22,25,0,23,27,26,29,27,28,25,25],
[32,20,24,27,27,0,26,26,28,24,24,31,22],
[26,23,18,27,23,24,0,24,30,17,24,30,22],
[24,25,25,31,24,24,26,0,27,26,23,30,27],
[27,22,25,24,21,22,20,23,0,24,25,23,26],
[26,23,21,27,23,26,33,24,26,0,22,32,31],
[34,25,28,31,22,26,26,27,25,28,0,27,26],
[24,21,21,27,25,19,20,20,27,18,23,0,25],
[27,26,21,21,25,28,28,23,24,19,24,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 54, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,20,31,22,26,34,34,28,20,28,28,27],
[23,0,24,34,23,28,35,34,28,16,34,34,37],
[30,26,0,32,21,23,25,34,32,25,34,28,29],
[19,16,18,0,14,15,18,22,17,11,25,23,20],
[28,27,29,36,0,26,30,37,29,21,31,31,30],
[24,22,27,35,24,0,35,26,31,17,39,31,34],
[16,15,25,32,20,15,0,26,23,12,28,22,26],
[16,16,16,28,13,24,24,0,21,21,25,27,22],
[22,22,18,33,21,19,27,29,0,19,28,24,27],
[30,34,25,39,29,33,38,29,31,0,32,38,35],
[22,16,16,25,19,11,22,25,22,18,0,12,18],
[22,16,22,27,19,19,28,23,26,12,38,0,24],
[23,13,21,30,20,16,24,28,23,15,32,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 55, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,28,31,31,22,22,29,25,19,27,25,30],
[24,0,24,31,24,25,29,18,29,21,28,26,26],
[22,26,0,33,32,24,30,19,27,17,30,30,28],
[19,19,17,0,23,16,28,25,28,18,22,20,18],
[19,26,18,27,0,19,23,17,32,15,16,23,24],
[28,25,26,34,31,0,31,25,30,23,26,30,33],
[28,21,20,22,27,19,0,23,25,24,22,18,23],
[21,32,31,25,33,25,27,0,32,18,29,24,30],
[25,21,23,22,18,20,25,18,0,22,22,22,22],
[31,29,33,32,35,27,26,32,28,0,25,30,34],
[23,22,20,28,34,24,28,21,28,25,0,27,26],
[25,24,20,30,27,20,32,26,28,20,23,0,28],
[20,24,22,32,26,17,27,20,28,16,24,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 56, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,26,33,29,27,28,30,29,28,34,26,29],
[25,0,25,22,24,31,21,28,28,28,27,26,28],
[24,25,0,22,24,31,22,26,28,29,30,19,27],
[17,28,28,0,26,27,23,31,25,28,29,21,29],
[21,26,26,24,0,35,27,22,25,28,23,25,26],
[23,19,19,23,15,0,16,24,21,22,22,15,23],
[22,29,28,27,23,34,0,26,16,25,30,23,28],
[20,22,24,19,28,26,24,0,29,26,27,28,30],
[21,22,22,25,25,29,34,21,0,29,27,18,30],
[22,22,21,22,22,28,25,24,21,0,24,24,24],
[16,23,20,21,27,28,20,23,23,26,0,18,20],
[24,24,31,29,25,35,27,22,32,26,32,0,34],
[21,22,23,21,24,27,22,20,20,26,30,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 57, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,21,25,23,35,27,33,11,18,33,35,23],
[16,0,5,0,2,23,19,14,6,6,17,19,8],
[29,45,0,29,27,18,38,41,21,17,39,28,17],
[25,50,21,0,27,23,32,39,18,15,33,35,25],
[27,48,23,23,0,25,27,44,22,6,31,31,23],
[15,27,32,27,25,0,34,35,17,25,35,42,25],
[23,31,12,18,23,16,0,35,6,16,14,28,18],
[17,36,9,11,6,15,15,0,12,6,23,25,17],
[39,44,29,32,28,33,44,38,0,21,29,31,19],
[32,44,33,35,44,25,34,44,29,0,35,37,39],
[17,33,11,17,19,15,36,27,21,15,0,31,8],
[15,31,22,15,19,8,22,25,19,13,19,0,19],
[27,42,33,25,27,25,32,33,31,11,42,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 58, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,32,27,36,27,30,26,28,30,31,35,26],
[30,0,28,33,24,23,33,23,23,29,25,28,15],
[18,22,0,23,28,26,33,26,23,25,25,20,17],
[23,17,27,0,24,24,23,18,20,26,22,31,22],
[14,26,22,26,0,26,23,17,20,26,24,26,15],
[23,27,24,26,24,0,24,25,20,21,24,25,14],
[20,17,17,27,27,26,0,11,12,21,15,33,14],
[24,27,24,32,33,25,39,0,25,32,27,36,24],
[22,27,27,30,30,30,38,25,0,35,22,36,24],
[20,21,25,24,24,29,29,18,15,0,22,31,14],
[19,25,25,28,26,26,35,23,28,28,0,31,28],
[15,22,30,19,24,25,17,14,14,19,19,0,16],
[24,35,33,28,35,36,36,26,26,36,22,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 59, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,31,29,34,25,33,29,21,24,30,30,24],
[23,0,27,26,26,25,30,23,22,23,27,26,23],
[19,23,0,24,28,21,27,26,19,20,24,24,18],
[21,24,26,0,26,23,28,23,21,27,24,25,23],
[16,24,22,24,0,16,23,24,17,24,24,23,25],
[25,25,29,27,34,0,28,26,18,25,29,26,27],
[17,20,23,22,27,22,0,26,21,18,21,19,17],
[21,27,24,27,26,24,24,0,17,27,27,26,30],
[29,28,31,29,33,32,29,33,0,28,27,27,25],
[26,27,30,23,26,25,32,23,22,0,30,28,27],
[20,23,26,26,26,21,29,23,23,20,0,22,21],
[20,24,26,25,27,24,31,24,23,22,28,0,23],
[26,27,32,27,25,23,33,20,25,23,29,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 60, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,25,28,24,28,24,28,21,11,14,17,20],
[31,0,23,26,36,43,31,37,22,28,30,28,34],
[25,27,0,14,33,34,33,29,20,26,26,22,32],
[22,24,36,0,30,32,35,29,24,24,24,22,32],
[26,14,17,20,0,32,27,28,20,24,20,21,20],
[22,7,16,18,18,0,20,29,16,13,15,11,23],
[26,19,17,15,23,30,0,27,23,24,19,12,29],
[22,13,21,21,22,21,23,0,24,14,13,14,29],
[29,28,30,26,30,34,27,26,0,29,22,30,27],
[39,22,24,26,26,37,26,36,21,0,9,20,31],
[36,20,24,26,30,35,31,37,28,41,0,23,33],
[33,22,28,28,29,39,38,36,20,30,27,0,37],
[30,16,18,18,30,27,21,21,23,19,17,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 61, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,25,33,29,31,21,22,33,29,27,17,24],
[23,0,18,25,21,24,17,19,23,29,31,22,24],
[25,32,0,35,34,30,22,30,28,34,30,31,24],
[17,25,15,0,18,23,13,17,18,21,24,15,19],
[21,29,16,32,0,25,25,10,26,24,25,20,22],
[19,26,20,27,25,0,15,13,21,26,21,12,18],
[29,33,28,37,25,35,0,20,25,29,30,20,29],
[28,31,20,33,40,37,30,0,29,30,39,32,27],
[17,27,22,32,24,29,25,21,0,21,29,19,24],
[21,21,16,29,26,24,21,20,29,0,28,18,22],
[23,19,20,26,25,29,20,11,21,22,0,14,13],
[33,28,19,35,30,38,30,18,31,32,36,0,32],
[26,26,26,31,28,32,21,23,26,28,37,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 62, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,24,41,25,29,35,34,22,32,36,39,19],
[20,0,20,38,28,31,28,23,34,16,30,37,30],
[26,30,0,29,30,32,42,37,16,30,28,34,29],
[9,12,21,0,14,22,22,12,6,14,9,22,11],
[25,22,20,36,0,29,27,27,26,25,22,45,22],
[21,19,18,28,21,0,31,19,16,17,13,34,24],
[15,22,8,28,23,19,0,13,16,19,18,25,26],
[16,27,13,38,23,31,37,0,14,14,10,37,20],
[28,16,34,44,24,34,34,36,0,26,31,34,30],
[18,34,20,36,25,33,31,36,24,0,34,39,19],
[14,20,22,41,28,37,32,40,19,16,0,44,19],
[11,13,16,28,5,16,25,13,16,11,6,0,8],
[31,20,21,39,28,26,24,30,20,31,31,42,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 63, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,14,14,16,13,16,27,17,21,21,19,21],
[38,0,28,28,30,30,25,28,24,30,39,37,31],
[36,22,0,25,20,34,20,36,31,38,38,31,35],
[36,22,25,0,27,26,15,37,26,24,31,32,26],
[34,20,30,23,0,26,18,27,28,26,32,28,23],
[37,20,16,24,24,0,26,29,23,23,39,30,27],
[34,25,30,35,32,24,0,31,34,27,31,25,26],
[23,22,14,13,23,21,19,0,15,26,27,21,21],
[33,26,19,24,22,27,16,35,0,38,34,28,31],
[29,20,12,26,24,27,23,24,12,0,28,30,24],
[29,11,12,19,18,11,19,23,16,22,0,20,21],
[31,13,19,18,22,20,25,29,22,20,30,0,25],
[29,19,15,24,27,23,24,29,19,26,29,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 64, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,20,24,23,18,37,39,35,20,25,19,24],
[15,0,25,19,14,13,26,21,28,18,30,17,24],
[30,25,0,24,26,23,28,27,42,40,26,28,21],
[26,31,26,0,31,21,26,30,31,24,28,25,21],
[27,36,24,19,0,14,25,33,28,22,22,17,19],
[32,37,27,29,36,0,33,39,35,19,27,21,25],
[13,24,22,24,25,17,0,28,31,23,30,25,23],
[11,29,23,20,17,11,22,0,26,16,25,17,27],
[15,22,8,19,22,15,19,24,0,14,12,7,8],
[30,32,10,26,28,31,27,34,36,0,20,26,14],
[25,20,24,22,28,23,20,25,38,30,0,27,27],
[31,33,22,25,33,29,25,33,43,24,23,0,18],
[26,26,29,29,31,25,27,23,42,36,23,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 65, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,16,27,25,33,10,27,23,6,34,22,9],
[35,0,33,27,27,45,20,28,25,14,36,28,18],
[34,17,0,34,30,38,34,34,23,19,34,25,23],
[23,23,16,0,30,43,16,11,16,21,16,12,21],
[25,23,20,20,0,24,13,13,10,19,22,16,28],
[17,5,12,7,26,0,7,4,10,13,12,8,17],
[40,30,16,34,37,43,0,34,27,31,44,31,21],
[23,22,16,39,37,46,16,0,21,24,29,22,28],
[27,25,27,34,40,40,23,29,0,21,39,11,25],
[44,36,31,29,31,37,19,26,29,0,39,31,36],
[16,14,16,34,28,38,6,21,11,11,0,12,13],
[28,22,25,38,34,42,19,28,39,19,38,0,23],
[41,32,27,29,22,33,29,22,25,14,37,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 66, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,25,34,11,34,25,14,16,16,39,14,25],
[25,0,36,36,27,36,25,25,25,25,25,30,36],
[25,14,0,34,0,23,14,14,16,25,39,14,23],
[16,14,16,0,0,23,0,0,16,16,25,14,0],
[39,23,50,50,0,34,23,23,25,25,39,14,23],
[16,14,27,27,16,0,16,0,16,16,25,30,16],
[25,25,36,50,27,34,0,23,25,25,39,14,20],
[36,25,36,50,27,50,27,0,36,36,25,41,36],
[34,25,34,34,25,34,25,14,0,36,39,25,34],
[34,25,25,34,25,34,25,14,14,0,39,14,25],
[11,25,11,25,11,25,11,25,11,11,0,25,11],
[36,20,36,36,36,20,36,9,25,36,25,0,20],
[25,14,27,50,27,34,30,14,16,25,39,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 67, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,27,24,25,27,23,24,27,29,25,28,23],
[27,0,29,25,24,27,24,25,30,31,20,20,27],
[23,21,0,26,28,31,23,24,26,30,22,29,26],
[26,25,24,0,29,26,24,25,23,26,22,28,27],
[25,26,22,21,0,31,25,28,24,28,21,27,25],
[23,23,19,24,19,0,24,22,21,26,22,24,23],
[27,26,27,26,25,26,0,26,26,33,23,24,32],
[26,25,26,25,22,28,24,0,28,30,16,16,27],
[23,20,24,27,26,29,24,22,0,29,18,27,25],
[21,19,20,24,22,24,17,20,21,0,18,21,27],
[25,30,28,28,29,28,27,34,32,32,0,23,27],
[22,30,21,22,23,26,26,34,23,29,27,0,32],
[27,23,24,23,25,27,18,23,25,23,23,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 68, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,22,29,20,18,9,33,11,24,25,24,25],
[38,0,29,33,24,29,21,36,19,23,26,18,30],
[28,21,0,45,21,30,18,40,32,42,34,32,43],
[21,17,5,0,24,10,15,31,26,19,22,21,31],
[30,26,29,26,0,24,23,39,20,36,17,32,28],
[32,21,20,40,26,0,16,36,35,22,33,26,31],
[41,29,32,35,27,34,0,39,26,35,29,20,36],
[17,14,10,19,11,14,11,0,10,17,11,7,26],
[39,31,18,24,30,15,24,40,0,27,17,21,36],
[26,27,8,31,14,28,15,33,23,0,16,12,31],
[25,24,16,28,33,17,21,39,33,34,0,28,28],
[26,32,18,29,18,24,30,43,29,38,22,0,39],
[25,20,7,19,22,19,14,24,14,19,22,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 69, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,39,20,35,27,26,28,28,32,14,27,13],
[24,0,31,27,32,29,20,25,27,26,25,27,25],
[11,19,0,25,17,15,19,20,18,25,12,17,18],
[30,23,25,0,26,30,37,33,30,26,30,26,30],
[15,18,33,24,0,23,17,17,22,35,19,26,14],
[23,21,35,20,27,0,32,17,17,31,21,29,15],
[24,30,31,13,33,18,0,27,22,31,18,19,22],
[22,25,30,17,33,33,23,0,18,38,21,33,16],
[22,23,32,20,28,33,28,32,0,33,23,34,24],
[18,24,25,24,15,19,19,12,17,0,17,16,16],
[36,25,38,20,31,29,32,29,27,33,0,36,27],
[23,23,33,24,24,21,31,17,16,34,14,0,15],
[37,25,32,20,36,35,28,34,26,34,23,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 70, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,29,25,24,20,36,20,31,30,26,17,27],
[34,0,32,23,41,40,27,33,35,32,36,31,29],
[21,18,0,21,29,30,28,29,28,26,25,20,25],
[25,27,29,0,34,31,23,26,34,23,22,21,21],
[26,9,21,16,0,24,20,15,24,25,19,9,13],
[30,10,20,19,26,0,30,23,36,26,15,19,22],
[14,23,22,27,30,20,0,24,33,32,28,21,26],
[30,17,21,24,35,27,26,0,38,28,26,15,27],
[19,15,22,16,26,14,17,12,0,26,14,10,15],
[20,18,24,27,25,24,18,22,24,0,26,21,24],
[24,14,25,28,31,35,22,24,36,24,0,29,20],
[33,19,30,29,41,31,29,35,40,29,21,0,30],
[23,21,25,29,37,28,24,23,35,26,30,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 71, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,22,23,24,21,18,22,19,33,27,23,16],
[30,0,21,25,26,15,21,15,15,26,28,20,20],
[28,29,0,33,26,21,25,24,17,32,33,30,19],
[27,25,17,0,22,14,21,22,8,30,24,24,21],
[26,24,24,28,0,24,19,23,16,32,31,25,20],
[29,35,29,36,26,0,30,19,25,37,31,29,33],
[32,29,25,29,31,20,0,21,24,36,29,23,25],
[28,35,26,28,27,31,29,0,20,39,35,33,27],
[31,35,33,42,34,25,26,30,0,38,36,26,23],
[17,24,18,20,18,13,14,11,12,0,16,19,25],
[23,22,17,26,19,19,21,15,14,34,0,20,27],
[27,30,20,26,25,21,27,17,24,31,30,0,22],
[34,30,31,29,30,17,25,23,27,25,23,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 72, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,21,21,24,20,13,24,13,19,22,22,27],
[31,0,28,26,30,24,17,24,23,21,26,29,32],
[29,22,0,23,29,24,22,24,20,24,22,29,28],
[29,24,27,0,19,21,20,20,27,18,21,24,30],
[26,20,21,31,0,14,15,13,25,20,21,20,22],
[30,26,26,29,36,0,23,23,24,28,26,33,29],
[37,33,28,30,35,27,0,24,27,29,23,25,31],
[26,26,26,30,37,27,26,0,24,27,24,29,31],
[37,27,30,23,25,26,23,26,0,30,30,29,27],
[31,29,26,32,30,22,21,23,20,0,21,27,30],
[28,24,28,29,29,24,27,26,20,29,0,27,29],
[28,21,21,26,30,17,25,21,21,23,23,0,23],
[23,18,22,20,28,21,19,19,23,20,21,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 73, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,23,23,27,25,22,20,22,18,17,21,23],
[33,0,28,28,33,27,25,30,34,26,27,27,28],
[27,22,0,23,26,25,21,26,24,20,21,24,24],
[27,22,27,0,28,24,23,25,22,21,16,20,25],
[23,17,24,22,0,21,25,23,27,23,19,23,20],
[25,23,25,26,29,0,20,20,26,23,22,22,22],
[28,25,29,27,25,30,0,23,30,26,23,22,24],
[30,20,24,25,27,30,27,0,28,22,15,19,19],
[28,16,26,28,23,24,20,22,0,24,20,23,22],
[32,24,30,29,27,27,24,28,26,0,26,22,28],
[33,23,29,34,31,28,27,35,30,24,0,25,26],
[29,23,26,30,27,28,28,31,27,28,25,0,27],
[27,22,26,25,30,28,26,31,28,22,24,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 74, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,24,25,27,35,22,31,24,26,29,23,28],
[24,0,25,21,27,29,26,32,22,29,23,25,31],
[26,25,0,19,20,29,24,28,26,24,22,24,28],
[25,29,31,0,29,35,30,35,31,32,30,28,35],
[23,23,30,21,0,33,23,27,20,27,27,22,29],
[15,21,21,15,17,0,23,18,19,19,20,24,20],
[28,24,26,20,27,27,0,20,22,27,25,25,23],
[19,18,22,15,23,32,30,0,16,25,22,20,28],
[26,28,24,19,30,31,28,34,0,27,22,27,26],
[24,21,26,18,23,31,23,25,23,0,24,18,21],
[21,27,28,20,23,30,25,28,28,26,0,27,30],
[27,25,26,22,28,26,25,30,23,32,23,0,28],
[22,19,22,15,21,30,27,22,24,29,20,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 75, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,27,26,29,37,43,44,30,28,30,21,22],
[20,0,21,26,24,36,27,37,21,27,28,20,21],
[23,29,0,36,23,30,43,36,37,28,37,29,36],
[24,24,14,0,24,31,24,30,24,15,30,2,24],
[21,26,27,26,0,26,33,37,27,33,27,26,28],
[13,14,20,19,24,0,26,43,20,20,14,13,27],
[7,23,7,26,17,24,0,30,15,16,31,8,9],
[6,13,14,20,13,7,20,0,14,14,7,13,21],
[20,29,13,26,23,30,35,36,0,22,30,14,20],
[22,23,22,35,17,30,34,36,28,0,31,30,23],
[20,22,13,20,23,36,19,43,20,19,0,7,15],
[29,30,21,48,24,37,42,37,36,20,43,0,37],
[28,29,14,26,22,23,41,29,30,27,35,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 76, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,29,29,25,29,27,33,19,32,37,33,33],
[15,0,15,18,22,21,26,26,21,26,29,29,29],
[21,35,0,31,28,30,30,33,26,26,33,33,33],
[21,32,19,0,31,29,32,29,23,29,30,35,21],
[25,28,22,19,0,22,30,25,24,28,34,38,24],
[21,29,20,21,28,0,28,31,23,27,32,34,28],
[23,24,20,18,20,22,0,26,21,29,26,25,20],
[17,24,17,21,25,19,24,0,17,21,26,21,27],
[31,29,24,27,26,27,29,33,0,29,34,34,30],
[18,24,24,21,22,23,21,29,21,0,25,33,22],
[13,21,17,20,16,18,24,24,16,25,0,21,25],
[17,21,17,15,12,16,25,29,16,17,29,0,24],
[17,21,17,29,26,22,30,23,20,28,25,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 77, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,34,29,33,30,26,25,21,22,31,28,30],
[17,0,22,26,19,23,23,15,16,20,25,17,20],
[16,28,0,28,28,26,23,20,18,22,27,18,27],
[21,24,22,0,22,24,22,21,17,19,23,19,21],
[17,31,22,28,0,28,25,24,20,25,25,24,20],
[20,27,24,26,22,0,23,19,18,19,25,22,24],
[24,27,27,28,25,27,0,28,22,26,31,24,27],
[25,35,30,29,26,31,22,0,27,23,30,21,29],
[29,34,32,33,30,32,28,23,0,25,32,27,33],
[28,30,28,31,25,31,24,27,25,0,29,20,28],
[19,25,23,27,25,25,19,20,18,21,0,19,20],
[22,33,32,31,26,28,26,29,23,30,31,0,30],
[20,30,23,29,30,26,23,21,17,22,30,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 78, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,24,30,25,21,28,27,31,27,32,27,28],
[31,0,31,26,26,24,30,33,35,28,35,30,31],
[26,19,0,25,21,22,26,24,33,25,29,20,26],
[20,24,25,0,21,25,30,29,29,22,28,23,25],
[25,24,29,29,0,22,29,27,32,29,29,24,27],
[29,26,28,25,28,0,27,26,31,26,30,26,25],
[22,20,24,20,21,23,0,20,25,21,23,24,25],
[23,17,26,21,23,24,30,0,26,22,27,23,22],
[19,15,17,21,18,19,25,24,0,25,20,16,20],
[23,22,25,28,21,24,29,28,25,0,29,32,30],
[18,15,21,22,21,20,27,23,30,21,0,21,20],
[23,20,30,27,26,24,26,27,34,18,29,0,27],
[22,19,24,25,23,25,25,28,30,20,30,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 79, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,23,27,32,30,32,25,35,30,33,27,31],
[16,0,19,19,27,22,22,25,20,23,24,21,24],
[27,31,0,27,35,28,26,34,28,25,29,28,34],
[23,31,23,0,31,28,26,22,27,24,25,27,23],
[18,23,15,19,0,28,22,20,19,17,26,17,19],
[20,28,22,22,22,0,18,29,26,19,25,24,24],
[18,28,24,24,28,32,0,28,20,21,23,20,21],
[25,25,16,28,30,21,22,0,27,22,26,29,23],
[15,30,22,23,31,24,30,23,0,22,28,20,27],
[20,27,25,26,33,31,29,28,28,0,26,20,23],
[17,26,21,25,24,25,27,24,22,24,0,22,21],
[23,29,22,23,33,26,30,21,30,30,28,0,32],
[19,26,16,27,31,26,29,27,23,27,29,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 80, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,25,23,28,32,24,24,31,29,31,26,27],
[28,0,19,28,27,29,23,28,32,35,31,34,28],
[25,31,0,28,29,32,25,29,36,32,28,28,25],
[27,22,22,0,35,25,22,26,38,30,24,30,27],
[22,23,21,15,0,17,21,21,26,28,21,22,27],
[18,21,18,25,33,0,20,25,28,27,29,31,24],
[26,27,25,28,29,30,0,26,27,31,28,29,21],
[26,22,21,24,29,25,24,0,32,31,23,24,24],
[19,18,14,12,24,22,23,18,0,28,22,21,15],
[21,15,18,20,22,23,19,19,22,0,27,24,20],
[19,19,22,26,29,21,22,27,28,23,0,28,27],
[24,16,22,20,28,19,21,26,29,26,22,0,24],
[23,22,25,23,23,26,29,26,35,30,23,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 81, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,29,22,28,23,25,25,29,28,27,24,23],
[27,0,28,21,29,23,31,24,24,25,26,29,28],
[21,22,0,13,28,22,24,21,22,27,28,18,22],
[28,29,37,0,33,30,36,26,33,33,34,25,28],
[22,21,22,17,0,24,22,21,21,22,25,22,23],
[27,27,28,20,26,0,29,26,25,25,33,24,26],
[25,19,26,14,28,21,0,23,21,27,27,22,24],
[25,26,29,24,29,24,27,0,27,25,27,28,26],
[21,26,28,17,29,25,29,23,0,29,26,26,28],
[22,25,23,17,28,25,23,25,21,0,32,23,26],
[23,24,22,16,25,17,23,23,24,18,0,20,23],
[26,21,32,25,28,26,28,22,24,27,30,0,30],
[27,22,28,22,27,24,26,24,22,24,27,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 82, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,25,24,28,27,25,26,26,27,31,27,28],
[17,0,20,24,23,21,23,20,21,26,23,22,21],
[25,30,0,29,23,32,24,18,26,20,27,27,24],
[26,26,21,0,31,24,19,24,27,30,28,22,24],
[22,27,27,19,0,26,21,19,24,27,25,28,22],
[23,29,18,26,24,0,21,23,27,25,23,30,23],
[25,27,26,31,29,29,0,22,30,28,31,30,29],
[24,30,32,26,31,27,28,0,31,28,31,30,28],
[24,29,24,23,26,23,20,19,0,23,24,25,31],
[23,24,30,20,23,25,22,22,27,0,22,28,31],
[19,27,23,22,25,27,19,19,26,28,0,26,26],
[23,28,23,28,22,20,20,20,25,22,24,0,23],
[22,29,26,26,28,27,21,22,19,19,24,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 83, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,12,15,22,23,17,11,32,34,26,8,18],
[16,0,14,15,18,15,6,16,37,25,17,19,20],
[38,36,0,24,27,34,19,30,41,44,31,33,25],
[35,35,26,0,32,39,26,35,35,44,39,18,32],
[28,32,23,18,0,32,9,22,37,32,40,19,29],
[27,35,16,11,18,0,16,21,41,44,27,18,27],
[33,44,31,24,41,34,0,30,50,44,31,27,34],
[39,34,20,15,28,29,20,0,34,34,37,11,29],
[18,13,9,15,13,9,0,16,0,22,17,13,0],
[16,25,6,6,18,6,6,16,28,0,23,11,6],
[24,33,19,11,10,23,19,13,33,27,0,21,21],
[42,31,17,32,31,32,23,39,37,39,29,0,29],
[32,30,25,18,21,23,16,21,50,44,29,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 84, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,22,15,20,11,10,27,29,19,20,23,22],
[36,0,33,34,22,36,26,38,36,33,31,42,22],
[28,17,0,29,18,28,21,37,25,31,24,33,22],
[35,16,21,0,28,28,23,31,23,29,19,31,29],
[30,28,32,22,0,25,26,37,26,33,25,29,31],
[39,14,22,22,25,0,17,28,29,30,23,36,31],
[40,24,29,27,24,33,0,39,36,35,21,28,28],
[23,12,13,19,13,22,11,0,24,17,17,25,19],
[21,14,25,27,24,21,14,26,0,28,12,27,23],
[31,17,19,21,17,20,15,33,22,0,20,20,16],
[30,19,26,31,25,27,29,33,38,30,0,37,25],
[27,8,17,19,21,14,22,25,23,30,13,0,21],
[28,28,28,21,19,19,22,31,27,34,25,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 85, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,23,23,22,22,26,22,20,28,26,19,20],
[24,0,29,21,25,21,25,23,23,31,26,20,23],
[27,21,0,23,28,22,26,28,18,30,25,21,26],
[27,29,27,0,27,24,30,27,21,33,22,24,29],
[28,25,22,23,0,21,25,28,22,29,27,24,21],
[28,29,28,26,29,0,28,28,24,32,27,19,26],
[24,25,24,20,25,22,0,19,20,26,23,21,24],
[28,27,22,23,22,22,31,0,23,29,28,20,26],
[30,27,32,29,28,26,30,27,0,30,32,25,28],
[22,19,20,17,21,18,24,21,20,0,21,17,19],
[24,24,25,28,23,23,27,22,18,29,0,20,24],
[31,30,29,26,26,31,29,30,25,33,30,0,25],
[30,27,24,21,29,24,26,24,22,31,26,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 86, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,23,22,29,23,19,29,29,27,19,35,22],
[22,0,19,26,20,21,15,20,23,20,15,27,25],
[27,31,0,19,27,22,28,24,24,28,24,24,24],
[28,24,31,0,20,27,24,24,21,17,24,31,29],
[21,30,23,30,0,24,20,25,23,19,26,28,29],
[27,29,28,23,26,0,28,17,27,21,32,21,27],
[31,35,22,26,30,22,0,33,31,26,27,33,34],
[21,30,26,26,25,33,17,0,28,24,31,25,32],
[21,27,26,29,27,23,19,22,0,20,19,21,27],
[23,30,22,33,31,29,24,26,30,0,30,27,25],
[31,35,26,26,24,18,23,19,31,20,0,30,27],
[15,23,26,19,22,29,17,25,29,23,20,0,24],
[28,25,26,21,21,23,16,18,23,25,23,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 87, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,17,8,16,13,14,18,16,5,23,19,21],
[40,0,33,21,35,34,31,26,31,25,30,32,29],
[33,17,0,13,25,19,28,24,17,17,34,27,25],
[42,29,37,0,42,33,37,21,29,28,34,33,32],
[34,15,25,8,0,21,19,18,22,18,25,22,23],
[37,16,31,17,29,0,24,23,26,19,32,35,26],
[36,19,22,13,31,26,0,17,18,17,26,22,28],
[32,24,26,29,32,27,33,0,24,25,32,34,32],
[34,19,33,21,28,24,32,26,0,25,33,37,25],
[45,25,33,22,32,31,33,25,25,0,32,36,31],
[27,20,16,16,25,18,24,18,17,18,0,24,22],
[31,18,23,17,28,15,28,16,13,14,26,0,30],
[29,21,25,18,27,24,22,18,25,19,28,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 88, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,20,25,28,27,28,30,33,27,28,25,30],
[31,0,30,29,29,29,25,33,32,26,27,24,26],
[30,20,0,24,30,29,28,23,27,28,25,23,22],
[25,21,26,0,25,30,20,25,25,28,17,25,25],
[22,21,20,25,0,27,21,26,27,18,20,23,20],
[23,21,21,20,23,0,24,23,21,17,16,22,19],
[22,25,22,30,29,26,0,31,31,28,19,22,28],
[20,17,27,25,24,27,19,0,25,22,23,19,28],
[17,18,23,25,23,29,19,25,0,24,18,23,20],
[23,24,22,22,32,33,22,28,26,0,23,28,29],
[22,23,25,33,30,34,31,27,32,27,0,25,28],
[25,26,27,25,27,28,28,31,27,22,25,0,32],
[20,24,28,25,30,31,22,22,30,21,22,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 89, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,29,27,25,24,28,28,34,29,29,24,34],
[19,0,18,23,24,26,23,25,27,30,23,21,30],
[21,32,0,31,27,28,27,27,35,31,27,25,41],
[23,27,19,0,22,29,21,17,22,29,21,18,33],
[25,26,23,28,0,29,20,25,29,29,24,24,31],
[26,24,22,21,21,0,22,20,26,24,23,21,28],
[22,27,23,29,30,28,0,28,26,31,28,26,29],
[22,25,23,33,25,30,22,0,23,27,27,21,31],
[16,23,15,28,21,24,24,27,0,25,25,19,28],
[21,20,19,21,21,26,19,23,25,0,23,24,27],
[21,27,23,29,26,27,22,23,25,27,0,21,27],
[26,29,25,32,26,29,24,29,31,26,29,0,31],
[16,20,9,17,19,22,21,19,22,23,23,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 90, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,22,20,14,21,22,18,23,21,26,20,21],
[37,0,29,23,25,31,34,26,29,28,30,29,25],
[28,21,0,23,24,27,30,24,23,24,30,28,23],
[30,27,27,0,24,25,28,22,28,24,24,28,26],
[36,25,26,26,0,31,34,22,32,26,29,32,29],
[29,19,23,25,19,0,24,16,24,21,22,26,22],
[28,16,20,22,16,26,0,17,25,22,24,22,19],
[32,24,26,28,28,34,33,0,29,28,29,33,28],
[27,21,27,22,18,26,25,21,0,21,25,26,24],
[29,22,26,26,24,29,28,22,29,0,27,28,24],
[24,20,20,26,21,28,26,21,25,23,0,23,17],
[30,21,22,22,18,24,28,17,24,22,27,0,27],
[29,25,27,24,21,28,31,22,26,26,33,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 91, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,15,35,1,28,28,22,14,15,15,21,15],
[35,0,21,42,15,35,28,22,42,29,43,42,8],
[35,29,0,49,22,42,28,22,42,22,50,35,1],
[15,8,1,0,1,21,21,1,7,1,22,14,1],
[49,35,28,49,0,42,28,29,49,36,49,42,14],
[22,15,8,29,8,0,28,1,7,8,8,22,8],
[22,22,22,29,22,22,0,8,21,22,22,22,22],
[28,28,28,49,21,49,42,0,28,28,28,21,28],
[36,8,8,43,1,43,29,22,0,29,50,43,8],
[35,21,28,49,14,42,28,22,21,0,28,42,14],
[35,7,0,28,1,42,28,22,0,22,0,35,0],
[29,8,15,36,8,28,28,29,7,8,15,0,15],
[35,42,49,49,36,42,28,22,42,36,50,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 92, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,27,26,24,23,20,23,21,22,21,28,26],
[26,0,26,28,26,25,23,29,23,23,25,29,32],
[23,24,0,29,25,25,22,22,25,24,23,32,26],
[24,22,21,0,24,26,23,21,25,20,24,29,27],
[26,24,25,26,0,24,24,23,23,29,28,30,27],
[27,25,25,24,26,0,26,27,28,26,28,27,27],
[30,27,28,27,26,24,0,31,31,21,26,30,31],
[27,21,28,29,27,23,19,0,24,21,26,29,24],
[29,27,25,25,27,22,19,26,0,23,24,29,29],
[28,27,26,30,21,24,29,29,27,0,21,33,29],
[29,25,27,26,22,22,24,24,26,29,0,29,33],
[22,21,18,21,20,23,20,21,21,17,21,0,28],
[24,18,24,23,23,23,19,26,21,21,17,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 93, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,20,24,27,24,29,23,16,26,35,16,35],
[27,0,8,23,18,24,23,14,19,25,23,28,32],
[30,42,0,28,39,36,33,37,25,33,36,28,36],
[26,27,22,0,30,18,30,21,29,31,18,20,40],
[23,32,11,20,0,26,35,11,30,14,21,16,27],
[26,26,14,32,24,0,19,23,27,32,27,25,42],
[21,27,17,20,15,31,0,12,17,25,32,26,26],
[27,36,13,29,39,27,38,0,24,23,24,26,36],
[34,31,25,21,20,23,33,26,0,24,34,27,27],
[24,25,17,19,36,18,25,27,26,0,18,19,27],
[15,27,14,32,29,23,18,26,16,32,0,24,25],
[34,22,22,30,34,25,24,24,23,31,26,0,35],
[15,18,14,10,23,8,24,14,23,23,25,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 94, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,25,21,14,14,22,12,32,42,32,25,24],
[18,0,1,28,21,10,22,12,25,29,31,35,23],
[25,49,0,29,35,10,33,36,50,46,31,50,49],
[29,22,21,0,39,28,22,18,43,38,32,43,22],
[36,29,15,11,0,15,22,25,50,39,32,22,29],
[36,40,40,22,35,0,23,26,50,50,43,50,40],
[28,28,17,28,28,27,0,19,43,38,21,39,28],
[38,38,14,32,25,24,31,0,49,38,31,42,31],
[18,25,0,7,0,0,7,1,0,27,18,17,11],
[8,21,4,12,11,0,12,12,23,0,21,25,21],
[18,19,19,18,18,7,29,19,32,29,0,19,18],
[25,15,0,7,28,0,11,8,33,25,31,0,21],
[26,27,1,28,21,10,22,19,39,29,32,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 95, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,18,24,27,22,26,23,24,28,20,21,22],
[29,0,26,30,29,25,35,26,22,34,29,28,28],
[32,24,0,24,27,23,30,21,25,31,28,23,25],
[26,20,26,0,27,25,27,19,21,34,25,17,23],
[23,21,23,23,0,23,29,21,20,30,23,22,25],
[28,25,27,25,27,0,28,24,23,32,25,22,24],
[24,15,20,23,21,22,0,19,20,26,26,18,22],
[27,24,29,31,29,26,31,0,24,32,26,23,27],
[26,28,25,29,30,27,30,26,0,31,29,21,26],
[22,16,19,16,20,18,24,18,19,0,20,17,18],
[30,21,22,25,27,25,24,24,21,30,0,20,22],
[29,22,27,33,28,28,32,27,29,33,30,0,30],
[28,22,25,27,25,26,28,23,24,32,28,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 96, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,23,17,17,22,27,27,25,27,24,24,28],
[30,0,23,21,25,27,27,25,26,21,20,35,25],
[27,27,0,23,28,24,26,30,23,23,27,32,21],
[33,29,27,0,20,28,31,29,26,24,25,30,24],
[33,25,22,30,0,19,33,27,19,31,26,29,27],
[28,23,26,22,31,0,26,23,23,26,21,26,19],
[23,23,24,19,17,24,0,28,21,19,25,37,19],
[23,25,20,21,23,27,22,0,24,19,20,30,24],
[25,24,27,24,31,27,29,26,0,29,22,28,17],
[23,29,27,26,19,24,31,31,21,0,30,32,26],
[26,30,23,25,24,29,25,30,28,20,0,32,21],
[26,15,18,20,21,24,13,20,22,18,18,0,18],
[22,25,29,26,23,31,31,26,33,24,29,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 97, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,28,20,36,30,28,33,29,27,28,30,28],
[22,0,29,22,34,32,26,32,31,26,29,31,25],
[22,21,0,16,30,28,25,26,25,25,27,31,26],
[30,28,34,0,35,30,25,29,36,31,34,31,31],
[14,16,20,15,0,20,20,18,27,19,21,26,20],
[20,18,22,20,30,0,24,25,25,22,25,27,25],
[22,24,25,25,30,26,0,26,29,25,27,29,28],
[17,18,24,21,32,25,24,0,29,21,24,29,24],
[21,19,25,14,23,25,21,21,0,20,24,24,18],
[23,24,25,19,31,28,25,29,30,0,24,29,24],
[22,21,23,16,29,25,23,26,26,26,0,28,27],
[20,19,19,19,24,23,21,21,26,21,22,0,24],
[22,25,24,19,30,25,22,26,32,26,23,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 98, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,24,26,19,27,41,29,24,28,21,22,25],
[28,0,26,21,18,29,30,32,25,27,19,27,24],
[26,24,0,18,29,36,38,29,25,30,25,27,30],
[24,29,32,0,16,31,28,27,22,35,25,28,29],
[31,32,21,34,0,34,48,28,29,39,38,36,27],
[23,21,14,19,16,0,23,17,19,25,19,18,18],
[9,20,12,22,2,27,0,17,20,16,14,26,12],
[21,18,21,23,22,33,33,0,16,36,20,27,22],
[26,25,25,28,21,31,30,34,0,31,32,27,19],
[22,23,20,15,11,25,34,14,19,0,13,29,22],
[29,31,25,25,12,31,36,30,18,37,0,39,30],
[28,23,23,22,14,32,24,23,23,21,11,0,31],
[25,26,20,21,23,32,38,28,31,28,20,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 99, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,31,29,31,31,28,22,31,32,26,19,34],
[23,0,24,28,24,26,25,19,27,21,17,20,25],
[19,26,0,29,26,25,25,22,26,27,22,23,26],
[21,22,21,0,21,27,24,19,27,24,19,24,25],
[19,26,24,29,0,22,24,20,18,20,18,17,22],
[19,24,25,23,28,0,28,15,26,21,16,17,29],
[22,25,25,26,26,22,0,26,21,24,19,24,26],
[28,31,28,31,30,35,24,0,29,23,20,21,27],
[19,23,24,23,32,24,29,21,0,25,16,13,25],
[18,29,23,26,30,29,26,27,25,0,18,21,23],
[24,33,28,31,32,34,31,30,34,32,0,27,30],
[31,30,27,26,33,33,26,29,37,29,23,0,30],
[16,25,24,25,28,21,24,23,25,27,20,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 100, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,26,27,36,26,33,32,25,24,25,27,25],
[18,0,23,20,24,21,22,25,25,21,27,17,18],
[24,27,0,21,22,21,26,25,24,22,22,24,22],
[23,30,29,0,26,22,25,27,23,26,31,28,26],
[14,26,28,24,0,20,16,23,18,19,23,16,14],
[24,29,29,28,30,0,26,27,24,23,26,20,23],
[17,28,24,25,34,24,0,31,23,24,28,20,19],
[18,25,25,23,27,23,19,0,17,18,23,20,20],
[25,25,26,27,32,26,27,33,0,21,26,18,26],
[26,29,28,24,31,27,26,32,29,0,28,24,26],
[25,23,28,19,27,24,22,27,24,22,0,17,21],
[23,33,26,22,34,30,30,30,32,26,33,0,30],
[25,32,28,24,36,27,31,30,24,24,29,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 101, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,19,20,27,32,32,26,32,36,37,32,38],
[7,0,15,15,20,28,19,14,19,19,15,25,14],
[31,35,0,25,26,39,37,37,38,23,36,38,37],
[30,35,25,0,13,20,25,19,30,29,24,25,33],
[23,30,24,37,0,26,30,24,36,30,37,37,32],
[18,22,11,30,24,0,23,23,30,23,23,30,23],
[18,31,13,25,20,27,0,20,36,12,24,30,21],
[24,36,13,31,26,27,30,0,31,30,31,25,32],
[18,31,12,20,14,20,14,19,0,19,25,26,20],
[14,31,27,21,20,27,38,20,31,0,26,31,33],
[13,35,14,26,13,27,26,19,25,24,0,25,32],
[18,25,12,25,13,20,20,25,24,19,25,0,26],
[12,36,13,17,18,27,29,18,30,17,18,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 102, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,29,23,27,29,22,35,34,36,26,33,22],
[29,0,29,24,28,23,18,35,35,31,29,33,22],
[21,21,0,18,23,23,22,29,28,27,29,26,22],
[27,26,32,0,30,24,29,30,29,33,28,33,25],
[23,22,27,20,0,30,21,30,38,25,27,32,17],
[21,27,27,26,20,0,27,25,24,32,25,33,24],
[28,32,28,21,29,23,0,36,31,28,25,30,24],
[15,15,21,20,20,25,14,0,34,32,28,27,14],
[16,15,22,21,12,26,19,16,0,24,22,26,16],
[14,19,23,17,25,18,22,18,26,0,26,29,16],
[24,21,21,22,23,25,25,22,28,24,0,28,21],
[17,17,24,17,18,17,20,23,24,21,22,0,20],
[28,28,28,25,33,26,26,36,34,34,29,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 103, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,26,30,28,25,31,26,23,31,21,36,27],
[29,0,32,30,39,30,36,30,28,34,24,36,33],
[24,18,0,19,22,21,16,25,22,17,24,21,16],
[20,20,31,0,23,22,20,22,21,19,25,27,24],
[22,11,28,27,0,21,28,31,18,29,26,26,24],
[25,20,29,28,29,0,25,31,22,27,36,25,27],
[19,14,34,30,22,25,0,32,29,30,24,33,24],
[24,20,25,28,19,19,18,0,25,28,27,24,27],
[27,22,28,29,32,28,21,25,0,27,31,21,34],
[19,16,33,31,21,23,20,22,23,0,26,21,22],
[29,26,26,25,24,14,26,23,19,24,0,25,18],
[14,14,29,23,24,25,17,26,29,29,25,0,18],
[23,17,34,26,26,23,26,23,16,28,32,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 104, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,21,20,19,40,35,40,26,12,26,11,24],
[28,0,27,27,22,43,43,43,29,25,23,14,15],
[29,23,0,34,24,34,33,39,31,24,26,29,21],
[30,23,16,0,29,33,26,34,25,23,20,18,20],
[31,28,26,21,0,38,35,38,30,30,20,14,15],
[10,7,16,17,12,0,17,30,20,11,20,9,14],
[15,7,17,24,15,33,0,28,20,15,7,9,5],
[10,7,11,16,12,20,22,0,20,12,2,4,1],
[24,21,19,25,20,30,30,30,0,25,25,17,16],
[38,25,26,27,20,39,35,38,25,0,29,14,19],
[24,27,24,30,30,30,43,48,25,21,0,20,20],
[39,36,21,32,36,41,41,46,33,36,30,0,34],
[26,35,29,30,35,36,45,49,34,31,30,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 105, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,23,25,26,21,28,18,24,25,23,27,21],
[26,0,32,34,30,25,31,30,32,29,32,29,26],
[27,18,0,24,28,21,25,16,28,26,33,22,23],
[25,16,26,0,29,27,26,24,27,25,26,24,19],
[24,20,22,21,0,23,26,22,26,25,32,26,24],
[29,25,29,23,27,0,33,29,32,29,34,32,28],
[22,19,25,24,24,17,0,18,28,29,30,23,18],
[32,20,34,26,28,21,32,0,32,29,35,28,30],
[26,18,22,23,24,18,22,18,0,20,31,23,21],
[25,21,24,25,25,21,21,21,30,0,30,21,22],
[27,18,17,24,18,16,20,15,19,20,0,20,21],
[23,21,28,26,24,18,27,22,27,29,30,0,29],
[29,24,27,31,26,22,32,20,29,28,29,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 106, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,21,25,2,25,2,2,3,0,7,6,3],
[45,0,19,23,4,23,20,22,23,22,22,24,25],
[29,31,0,29,29,31,6,4,29,29,6,31,29],
[25,27,21,0,6,27,21,22,23,24,23,27,25],
[48,46,21,44,0,48,21,20,44,41,25,48,44],
[25,27,19,23,2,0,2,0,23,0,4,6,2],
[48,30,44,29,29,48,0,27,28,29,5,32,28],
[48,28,46,28,30,50,23,0,26,30,25,32,30],
[47,27,21,27,6,27,22,24,0,24,24,26,25],
[50,28,21,26,9,50,21,20,26,0,25,32,25],
[43,28,44,27,25,46,45,25,26,25,0,31,26],
[44,26,19,23,2,44,18,18,24,18,19,0,19],
[47,25,21,25,6,48,22,20,25,25,24,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 107, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,27,25,28,27,25,26,27,28,27,29,25],
[22,0,24,26,28,22,24,22,22,32,24,28,24],
[23,26,0,29,30,24,27,22,26,25,29,29,26],
[25,24,21,0,25,27,20,18,21,18,24,24,26],
[22,22,20,25,0,23,22,18,18,24,23,27,23],
[23,28,26,23,27,0,23,23,23,27,29,28,27],
[25,26,23,30,28,27,0,25,25,33,26,28,26],
[24,28,28,32,32,27,25,0,24,25,24,28,28],
[23,28,24,29,32,27,25,26,0,29,27,29,29],
[22,18,25,32,26,23,17,25,21,0,23,26,26],
[23,26,21,26,27,21,24,26,23,27,0,25,24],
[21,22,21,26,23,22,22,22,21,24,25,0,24],
[25,26,24,24,27,23,24,22,21,24,26,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 108, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,29,27,25,26,21,26,26,28,29,30,32],
[21,0,26,23,22,25,22,27,26,23,24,30,28],
[21,24,0,24,20,22,18,21,20,23,27,23,31],
[23,27,26,0,21,28,25,23,24,26,31,31,25],
[25,28,30,29,0,31,27,28,25,28,32,33,28],
[24,25,28,22,19,0,20,25,25,30,29,30,29],
[29,28,32,25,23,30,0,33,25,31,31,33,31],
[24,23,29,27,22,25,17,0,20,25,27,30,28],
[24,24,30,26,25,25,25,30,0,27,26,29,28],
[22,27,27,24,22,20,19,25,23,0,25,28,29],
[21,26,23,19,18,21,19,23,24,25,0,31,29],
[20,20,27,19,17,20,17,20,21,22,19,0,22],
[18,22,19,25,22,21,19,22,22,21,21,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 109, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,21,35,32,24,29,31,38,30,22,22,33],
[27,0,21,20,21,21,28,31,26,30,17,19,21],
[29,29,0,23,22,19,33,37,24,32,14,24,27],
[15,30,27,0,25,17,17,16,27,18,8,20,34],
[18,29,28,25,0,26,29,30,33,29,17,28,39],
[26,29,31,33,24,0,34,34,34,40,23,30,33],
[21,22,17,33,21,16,0,22,30,33,18,14,33],
[19,19,13,34,20,16,28,0,26,24,20,19,34],
[12,24,26,23,17,16,20,24,0,15,20,19,33],
[20,20,18,32,21,10,17,26,35,0,25,21,31],
[28,33,36,42,33,27,32,30,30,25,0,38,41],
[28,31,26,30,22,20,36,31,31,29,12,0,34],
[17,29,23,16,11,17,17,16,17,19,9,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 110, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,24,25,29,23,29,23,19,24,25,19,28],
[24,0,25,26,27,25,25,28,28,25,27,25,32],
[26,25,0,31,27,34,21,26,28,27,33,28,32],
[25,24,19,0,27,28,16,22,26,23,26,20,28],
[21,23,23,23,0,22,23,22,22,25,32,18,27],
[27,25,16,22,28,0,25,24,20,22,25,20,29],
[21,25,29,34,27,25,0,27,25,25,32,18,33],
[27,22,24,28,28,26,23,0,25,21,25,22,27],
[31,22,22,24,28,30,25,25,0,25,25,27,31],
[26,25,23,27,25,28,25,29,25,0,30,21,33],
[25,23,17,24,18,25,18,25,25,20,0,21,24],
[31,25,22,30,32,30,32,28,23,29,29,0,32],
[22,18,18,22,23,21,17,23,19,17,26,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 111, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,17,22,26,26,19,20,12,22,25,21,19],
[18,0,9,20,25,20,21,13,14,19,28,17,19],
[33,41,0,26,33,37,26,28,25,29,31,28,19],
[28,30,24,0,36,33,28,29,20,22,26,23,25],
[24,25,17,14,0,30,20,13,10,23,20,13,22],
[24,30,13,17,20,0,15,13,5,24,19,20,15],
[31,29,24,22,30,35,0,21,22,29,32,24,19],
[30,37,22,21,37,37,29,0,21,36,27,27,23],
[38,36,25,30,40,45,28,29,0,34,27,35,26],
[28,31,21,28,27,26,21,14,16,0,24,15,23],
[25,22,19,24,30,31,18,23,23,26,0,25,25],
[29,33,22,27,37,30,26,23,15,35,25,0,29],
[31,31,31,25,28,35,31,27,24,27,25,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 112, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,31,26,32,23,28,27,35,32,34,25,28],
[31,0,23,30,29,35,21,26,32,37,29,27,31],
[19,27,0,30,25,25,26,24,24,30,34,26,24],
[24,20,20,0,26,22,20,25,29,24,24,20,26],
[18,21,25,24,0,16,19,18,25,35,22,24,18],
[27,15,25,28,34,0,22,24,26,30,29,29,28],
[22,29,24,30,31,28,0,29,27,31,31,32,28],
[23,24,26,25,32,26,21,0,28,27,32,24,24],
[15,18,26,21,25,24,23,22,0,31,21,20,18],
[18,13,20,26,15,20,19,23,19,0,25,18,21],
[16,21,16,26,28,21,19,18,29,25,0,22,26],
[25,23,24,30,26,21,18,26,30,32,28,0,22],
[22,19,26,24,32,22,22,26,32,29,24,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 113, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,20,21,21,29,20,23,20,28,28,25,21],
[26,0,23,24,27,38,27,34,25,30,29,34,29],
[30,27,0,27,32,29,27,21,23,30,20,30,21],
[29,26,23,0,23,32,28,26,24,31,29,27,21],
[29,23,18,27,0,27,23,26,23,23,22,32,24],
[21,12,21,18,23,0,23,30,19,18,21,25,17],
[30,23,23,22,27,27,0,25,20,28,27,32,29],
[27,16,29,24,24,20,25,0,17,19,19,26,21],
[30,25,27,26,27,31,30,33,0,25,32,35,22],
[22,20,20,19,27,32,22,31,25,0,21,28,22],
[22,21,30,21,28,29,23,31,18,29,0,31,19],
[25,16,20,23,18,25,18,24,15,22,19,0,22],
[29,21,29,29,26,33,21,29,28,28,31,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 114, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,27,28,31,36,32,24,32,33,23,14,27],
[20,0,15,20,24,18,28,22,18,15,18,15,3],
[23,35,0,19,21,25,42,23,21,36,25,17,18],
[22,30,31,0,37,25,38,28,20,28,25,28,17],
[19,26,29,13,0,25,40,16,31,36,23,23,14],
[14,32,25,25,25,0,41,22,25,30,11,21,17],
[18,22,8,12,10,9,0,14,12,18,9,14,16],
[26,28,27,22,34,28,36,0,22,35,29,30,23],
[18,32,29,30,19,25,38,28,0,30,20,11,26],
[17,35,14,22,14,20,32,15,20,0,21,14,15],
[27,32,25,25,27,39,41,21,30,29,0,15,22],
[36,35,33,22,27,29,36,20,39,36,35,0,38],
[23,47,32,33,36,33,34,27,24,35,28,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 115, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,23,26,27,25,27,21,20,18,20,20,21],
[33,0,31,28,25,36,32,29,27,27,29,30,26],
[27,19,0,30,34,29,24,22,25,25,27,25,23],
[24,22,20,0,25,28,23,19,26,22,24,20,23],
[23,25,16,25,0,21,22,20,21,24,26,21,25],
[25,14,21,22,29,0,20,20,24,17,24,21,21],
[23,18,26,27,28,30,0,29,26,20,25,29,27],
[29,21,28,31,30,30,21,0,17,26,26,33,26],
[30,23,25,24,29,26,24,33,0,27,26,29,33],
[32,23,25,28,26,33,30,24,23,0,29,30,32],
[30,21,23,26,24,26,25,24,24,21,0,21,26],
[30,20,25,30,29,29,21,17,21,20,29,0,21],
[29,24,27,27,25,29,23,24,17,18,24,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 116, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,33,23,26,25,27,32,35,24,22,31,27],
[29,0,31,26,32,35,29,29,29,26,31,20,30],
[17,19,0,29,24,25,22,30,22,29,24,21,23],
[27,24,21,0,28,21,25,33,28,26,30,30,21],
[24,18,26,22,0,24,18,29,28,25,31,24,24],
[25,15,25,29,26,0,19,32,38,21,29,25,24],
[23,21,28,25,32,31,0,33,36,28,38,31,26],
[18,21,20,17,21,18,17,0,28,24,26,22,16],
[15,21,28,22,22,12,14,22,0,22,23,24,14],
[26,24,21,24,25,29,22,26,28,0,31,19,22],
[28,19,26,20,19,21,12,24,27,19,0,22,24],
[19,30,29,20,26,25,19,28,26,31,28,0,16],
[23,20,27,29,26,26,24,34,36,28,26,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 117, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,25,24,24,28,31,22,26,26,20,26,19],
[26,0,22,26,25,23,24,21,28,23,21,23,19],
[25,28,0,21,25,27,28,22,28,26,22,26,19],
[26,24,29,0,26,25,28,20,27,24,19,25,19],
[26,25,25,24,0,23,29,23,32,22,17,23,19],
[22,27,23,25,27,0,28,21,29,27,23,22,21],
[19,26,22,22,21,22,0,22,29,26,20,24,15],
[28,29,28,30,27,29,28,0,32,32,22,23,16],
[24,22,22,23,18,21,21,18,0,20,16,22,21],
[24,27,24,26,28,23,24,18,30,0,25,25,20],
[30,29,28,31,33,27,30,28,34,25,0,26,27],
[24,27,24,25,27,28,26,27,28,25,24,0,20],
[31,31,31,31,31,29,35,34,29,30,23,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 118, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,10,32,24,24,30,26,31,19,24,12,16],
[18,0,12,29,10,8,18,9,4,14,15,4,19],
[40,38,0,44,19,24,31,26,31,27,41,35,32],
[18,21,6,0,9,13,12,13,14,13,20,1,7],
[26,40,31,41,0,27,33,27,42,38,40,21,41],
[26,42,26,37,23,0,29,14,29,36,36,18,28],
[20,32,19,38,17,21,0,24,31,30,24,11,22],
[24,41,24,37,23,36,26,0,32,31,30,32,29],
[19,46,19,36,8,21,19,18,0,27,27,9,20],
[31,36,23,37,12,14,20,19,23,0,20,23,30],
[26,35,9,30,10,14,26,20,23,30,0,12,28],
[38,46,15,49,29,32,39,18,41,27,38,0,25],
[34,31,18,43,9,22,28,21,30,20,22,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 119, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,25,25,26,26,25,21,25,22,26,27,23],
[26,0,29,22,27,26,24,26,26,18,28,26,28],
[25,21,0,24,30,29,24,25,28,21,27,26,25],
[25,28,26,0,29,27,27,25,26,26,29,23,26],
[24,23,20,21,0,26,24,28,20,18,25,23,24],
[24,24,21,23,24,0,23,24,20,21,27,22,23],
[25,26,26,23,26,27,0,23,29,22,33,21,28],
[29,24,25,25,22,26,27,0,24,29,28,28,29],
[25,24,22,24,30,30,21,26,0,21,31,24,26],
[28,32,29,24,32,29,28,21,29,0,38,28,30],
[24,22,23,21,25,23,17,22,19,12,0,24,21],
[23,24,24,27,27,28,29,22,26,22,26,0,25],
[27,22,25,24,26,27,22,21,24,20,29,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 120, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,20,23,19,19,22,19,20,24,27,21,26],
[27,0,21,26,25,19,27,28,25,28,28,21,27],
[30,29,0,25,17,22,17,24,21,26,28,16,28],
[27,24,25,0,24,25,23,29,22,31,26,27,28],
[31,25,33,26,0,25,24,24,25,36,37,27,28],
[31,31,28,25,25,0,28,26,22,30,33,29,26],
[28,23,33,27,26,22,0,29,19,32,24,23,31],
[31,22,26,21,26,24,21,0,17,33,27,26,29],
[30,25,29,28,25,28,31,33,0,28,27,28,30],
[26,22,24,19,14,20,18,17,22,0,24,22,25],
[23,22,22,24,13,17,26,23,23,26,0,19,25],
[29,29,34,23,23,21,27,24,22,28,31,0,31],
[24,23,22,22,22,24,19,21,20,25,25,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 121, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,30,40,15,16,17,17,26,27,26,32,20],
[22,0,29,22,24,10,16,15,25,38,34,18,25],
[20,21,0,17,18,11,17,13,17,23,22,20,13],
[10,28,33,0,18,22,7,23,22,25,26,26,21],
[35,26,32,32,0,17,9,14,36,32,28,27,32],
[34,40,39,28,33,0,15,33,38,36,43,37,31],
[33,34,33,43,41,35,0,22,30,34,28,29,33],
[33,35,37,27,36,17,28,0,37,31,31,30,34],
[24,25,33,28,14,12,20,13,0,27,26,22,15],
[23,12,27,25,18,14,16,19,23,0,17,19,19],
[24,16,28,24,22,7,22,19,24,33,0,23,25],
[18,32,30,24,23,13,21,20,28,31,27,0,24],
[30,25,37,29,18,19,17,16,35,31,25,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 122, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,21,17,31,24,23,18,19,19,23,25,19],
[29,0,25,23,24,29,32,20,27,25,26,27,20],
[29,25,0,29,34,21,28,24,25,25,24,28,18],
[33,27,21,0,30,22,25,28,22,22,23,30,26],
[19,26,16,20,0,24,27,20,20,22,21,28,20],
[26,21,29,28,26,0,27,26,29,23,22,25,23],
[27,18,22,25,23,23,0,22,27,23,25,27,17],
[32,30,26,22,30,24,28,0,24,24,26,35,23],
[31,23,25,28,30,21,23,26,0,28,24,31,20],
[31,25,25,28,28,27,27,26,22,0,26,31,28],
[27,24,26,27,29,28,25,24,26,24,0,27,26],
[25,23,22,20,22,25,23,15,19,19,23,0,22],
[31,30,32,24,30,27,33,27,30,22,24,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 123, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,28,22,16,23,24,18,20,25,19,26,21],
[26,0,28,31,28,25,26,29,23,32,26,27,30],
[22,22,0,30,25,25,29,21,19,22,30,25,26],
[28,19,20,0,26,24,27,18,22,26,22,25,20],
[34,22,25,24,0,23,30,31,23,34,29,21,34],
[27,25,25,26,27,0,28,23,18,26,21,24,26],
[26,24,21,23,20,22,0,23,14,19,23,26,21],
[32,21,29,32,19,27,27,0,23,25,27,25,28],
[30,27,31,28,27,32,36,27,0,31,26,25,27],
[25,18,28,24,16,24,31,25,19,0,23,26,26],
[31,24,20,28,21,29,27,23,24,27,0,25,32],
[24,23,25,25,29,26,24,25,25,24,25,0,26],
[29,20,24,30,16,24,29,22,23,24,18,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 124, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,21,32,25,22,24,25,29,19,13,23,23],
[28,0,25,32,32,27,29,29,35,30,19,41,27],
[29,25,0,35,28,22,23,18,35,29,20,29,29],
[18,18,15,0,23,20,27,16,33,24,16,23,29],
[25,18,22,27,0,21,20,18,28,27,16,29,30],
[28,23,28,30,29,0,25,28,31,28,29,34,29],
[26,21,27,23,30,25,0,24,24,27,24,36,20],
[25,21,32,34,32,22,26,0,29,20,18,36,30],
[21,15,15,17,22,19,26,21,0,14,18,25,25],
[31,20,21,26,23,22,23,30,36,0,20,32,23],
[37,31,30,34,34,21,26,32,32,30,0,36,24],
[27,9,21,27,21,16,14,14,25,18,14,0,21],
[27,23,21,21,20,21,30,20,25,27,26,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 125, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,25,20,26,24,26,25,24,22,28,21,20],
[24,0,19,28,21,25,26,22,25,27,27,23,26],
[25,31,0,26,30,25,28,30,30,29,34,31,24],
[30,22,24,0,22,24,22,29,25,22,29,27,22],
[24,29,20,28,0,25,24,31,28,23,28,22,27],
[26,25,25,26,25,0,23,29,27,26,29,24,25],
[24,24,22,28,26,27,0,26,25,23,25,23,23],
[25,28,20,21,19,21,24,0,22,22,25,20,22],
[26,25,20,25,22,23,25,28,0,27,28,24,26],
[28,23,21,28,27,24,27,28,23,0,30,24,23],
[22,23,16,21,22,21,25,25,22,20,0,22,23],
[29,27,19,23,28,26,27,30,26,26,28,0,22],
[30,24,26,28,23,25,27,28,24,27,27,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 126, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,25,25,25,22,25,23,19,25,31,22,23],
[27,0,24,31,31,27,32,29,25,34,31,24,29],
[25,26,0,27,27,22,31,23,20,30,27,26,25],
[25,19,23,0,26,22,25,23,19,21,27,23,23],
[25,19,23,24,0,20,26,26,23,24,31,20,24],
[28,23,28,28,30,0,28,30,28,32,33,27,26],
[25,18,19,25,24,22,0,25,17,22,25,24,21],
[27,21,27,27,24,20,25,0,22,28,29,25,21],
[31,25,30,31,27,22,33,28,0,26,32,28,24],
[25,16,20,29,26,18,28,22,24,0,26,23,23],
[19,19,23,23,19,17,25,21,18,24,0,24,20],
[28,26,24,27,30,23,26,25,22,27,26,0,23],
[27,21,25,27,26,24,29,29,26,27,30,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 127, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,18,15,17,15,19,21,24,19,17,21,22],
[28,0,20,22,22,18,22,23,27,27,29,24,27],
[32,30,0,17,26,18,22,23,27,25,28,24,28],
[35,28,33,0,24,28,21,23,30,24,17,23,26],
[33,28,24,26,0,21,22,27,22,24,24,27,26],
[35,32,32,22,29,0,26,28,34,31,25,28,32],
[31,28,28,29,28,24,0,31,32,31,29,23,31],
[29,27,27,27,23,22,19,0,30,32,26,25,25],
[26,23,23,20,28,16,18,20,0,19,23,21,23],
[31,23,25,26,26,19,19,18,31,0,23,20,24],
[33,21,22,33,26,25,21,24,27,27,0,25,25],
[29,26,26,27,23,22,27,25,29,30,25,0,24],
[28,23,22,24,24,18,19,25,27,26,25,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 128, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,24,19,26,23,21,25,20,20,21,18,27],
[30,0,19,23,27,23,31,27,28,29,23,19,32],
[26,31,0,25,28,30,24,33,24,29,28,22,31],
[31,27,25,0,28,27,29,35,28,29,25,25,32],
[24,23,22,22,0,25,22,22,24,26,30,17,29],
[27,27,20,23,25,0,27,27,26,25,24,15,29],
[29,19,26,21,28,23,0,26,19,28,26,17,27],
[25,23,17,15,28,23,24,0,20,19,21,17,30],
[30,22,26,22,26,24,31,30,0,25,21,22,29],
[30,21,21,21,24,25,22,31,25,0,29,23,25],
[29,27,22,25,20,26,24,29,29,21,0,19,31],
[32,31,28,25,33,35,33,33,28,27,31,0,36],
[23,18,19,18,21,21,23,20,21,25,19,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 129, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,25,23,28,23,28,24,27,22,22,23,24],
[29,0,22,21,29,22,28,24,27,22,21,25,24],
[25,28,0,17,28,22,28,27,28,30,28,27,27],
[27,29,33,0,32,27,25,25,27,29,26,24,30],
[22,21,22,18,0,21,25,23,23,19,18,23,20],
[27,28,28,23,29,0,27,25,29,31,26,27,26],
[22,22,22,25,25,23,0,22,23,20,22,24,22],
[26,26,23,25,27,25,28,0,28,21,23,22,22],
[23,23,22,23,27,21,27,22,0,23,20,21,21],
[28,28,20,21,31,19,30,29,27,0,27,23,25],
[28,29,22,24,32,24,28,27,30,23,0,31,26],
[27,25,23,26,27,23,26,28,29,27,19,0,24],
[26,26,23,20,30,24,28,28,29,25,24,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 130, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,24,25,22,25,22,21,17,19,22,20,19],
[27,0,20,23,25,21,22,25,18,22,23,16,19],
[26,30,0,27,28,18,31,31,18,26,24,28,23],
[25,27,23,0,28,27,19,24,23,25,26,24,23],
[28,25,22,22,0,27,29,26,28,26,33,23,27],
[25,29,32,23,23,0,22,31,29,33,28,23,21],
[28,28,19,31,21,28,0,20,25,30,20,23,27],
[29,25,19,26,24,19,30,0,26,24,27,24,27],
[33,32,32,27,22,21,25,24,0,23,26,28,26],
[31,28,24,25,24,17,20,26,27,0,23,22,32],
[28,27,26,24,17,22,30,23,24,27,0,19,25],
[30,34,22,26,27,27,27,26,22,28,31,0,27],
[31,31,27,27,23,29,23,23,24,18,25,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 131, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,24,22,22,24,22,25,24,20,26,26,28],
[24,0,22,20,15,19,19,18,24,19,20,21,27],
[26,28,0,19,17,24,21,29,21,24,23,17,24],
[28,30,31,0,21,25,29,28,31,29,28,31,32],
[28,35,33,29,0,30,27,32,29,30,20,29,35],
[26,31,26,25,20,0,25,30,27,25,26,23,24],
[28,31,29,21,23,25,0,31,34,30,27,30,30],
[25,32,21,22,18,20,19,0,26,20,26,28,24],
[26,26,29,19,21,23,16,24,0,21,23,24,27],
[30,31,26,21,20,25,20,30,29,0,26,29,29],
[24,30,27,22,30,24,23,24,27,24,0,25,28],
[24,29,33,19,21,27,20,22,26,21,25,0,23],
[22,23,26,18,15,26,20,26,23,21,22,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 132, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,19,23,18,17,23,18,27,23,21,25,24],
[28,0,23,26,28,25,26,22,24,20,26,23,28],
[31,27,0,27,26,26,24,24,24,24,24,29,25],
[27,24,23,0,28,26,19,20,23,18,23,21,22],
[32,22,24,22,0,20,21,25,23,24,24,28,25],
[33,25,24,24,30,0,25,24,25,28,27,29,26],
[27,24,26,31,29,25,0,26,23,28,24,28,29],
[32,28,26,30,25,26,24,0,27,28,29,28,22],
[23,26,26,27,27,25,27,23,0,22,27,19,21],
[27,30,26,32,26,22,22,22,28,0,27,27,31],
[29,24,26,27,26,23,26,21,23,23,0,20,25],
[25,27,21,29,22,21,22,22,31,23,30,0,20],
[26,22,25,28,25,24,21,28,29,19,25,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 133, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,18,38,27,39,45,20,43,36,20,25,38],
[30,0,18,32,18,39,34,20,23,25,34,23,18],
[32,32,0,50,27,32,27,20,25,45,27,25,38],
[12,18,0,0,18,12,27,20,5,18,7,16,0],
[23,32,23,32,0,32,34,38,32,18,27,32,27],
[11,11,18,38,18,0,27,20,16,36,11,11,29],
[5,16,23,23,16,23,0,11,5,29,0,5,18],
[30,30,30,30,12,30,39,0,23,30,25,23,23],
[7,27,25,45,18,34,45,27,0,36,16,11,18],
[14,25,5,32,32,14,21,20,14,0,9,14,9],
[30,16,23,43,23,39,50,25,34,41,0,16,34],
[25,27,25,34,18,39,45,27,39,36,34,0,27],
[12,32,12,50,23,21,32,27,32,41,16,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 134, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,24,26,25,24,24,28,25,23,27,29,33],
[26,0,23,27,25,28,26,29,21,26,22,24,28],
[26,27,0,26,28,29,27,32,21,25,27,23,34],
[24,23,24,0,23,21,24,28,27,25,23,23,32],
[25,25,22,27,0,27,21,26,21,30,24,31,32],
[26,22,21,29,23,0,19,27,26,25,24,31,29],
[26,24,23,26,29,31,0,30,26,26,27,26,30],
[22,21,18,22,24,23,20,0,20,25,20,17,26],
[25,29,29,23,29,24,24,30,0,32,27,30,35],
[27,24,25,25,20,25,24,25,18,0,23,25,31],
[23,28,23,27,26,26,23,30,23,27,0,25,28],
[21,26,27,27,19,19,24,33,20,25,25,0,30],
[17,22,16,18,18,21,20,24,15,19,22,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 135, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,29,27,30,21,22,26,24,23,28,22,22],
[31,0,35,27,30,24,22,29,27,27,29,33,28],
[21,15,0,23,21,15,13,22,20,15,21,19,20],
[23,23,27,0,22,19,22,28,24,23,25,21,23],
[20,20,29,28,0,21,22,26,27,20,22,24,20],
[29,26,35,31,29,0,29,34,28,25,30,25,29],
[28,28,37,28,28,21,0,30,29,25,29,31,23],
[24,21,28,22,24,16,20,0,24,23,25,23,21],
[26,23,30,26,23,22,21,26,0,19,27,24,23],
[27,23,35,27,30,25,25,27,31,0,29,31,28],
[22,21,29,25,28,20,21,25,23,21,0,20,20],
[28,17,31,29,26,25,19,27,26,19,30,0,25],
[28,22,30,27,30,21,27,29,27,22,30,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 136, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,19,24,28,26,29,13,19,23,27,24,20],
[23,0,19,20,23,22,25,18,25,24,18,20,22],
[31,31,0,33,33,26,34,28,31,35,23,34,33],
[26,30,17,0,34,21,33,24,29,28,22,27,28],
[22,27,17,16,0,24,25,13,28,24,25,27,21],
[24,28,24,29,26,0,30,26,21,26,26,21,22],
[21,25,16,17,25,20,0,14,30,25,26,22,21],
[37,32,22,26,37,24,36,0,29,30,30,36,30],
[31,25,19,21,22,29,20,21,0,24,23,24,24],
[27,26,15,22,26,24,25,20,26,0,20,23,18],
[23,32,27,28,25,24,24,20,27,30,0,26,24],
[26,30,16,23,23,29,28,14,26,27,24,0,21],
[30,28,17,22,29,28,29,20,26,32,26,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 137, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,15,27,24,21,23,11,13,9,25,11,26],
[23,0,20,12,25,20,23,11,28,17,15,16,15],
[35,30,0,25,29,30,27,26,29,8,27,18,27],
[23,38,25,0,29,19,18,16,18,17,28,16,28],
[26,25,21,21,0,20,34,13,28,6,17,17,37],
[29,30,20,31,30,0,18,27,19,19,40,26,31],
[27,27,23,32,16,32,0,28,21,22,29,19,16],
[39,39,24,34,37,23,22,0,21,11,30,11,36],
[37,22,21,32,22,31,29,29,0,6,37,27,22],
[41,33,42,33,44,31,28,39,44,0,42,24,32],
[25,35,23,22,33,10,21,20,13,8,0,7,31],
[39,34,32,34,33,24,31,39,23,26,43,0,33],
[24,35,23,22,13,19,34,14,28,18,19,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 138, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,33,29,25,24,31,36,33,30,27,26,32],
[11,0,25,24,22,23,24,24,26,23,22,14,16],
[17,25,0,29,33,25,24,31,21,22,22,17,24],
[21,26,21,0,19,20,24,29,23,26,22,19,27],
[25,28,17,31,0,20,25,28,25,26,18,21,24],
[26,27,25,30,30,0,26,30,29,25,21,21,24],
[19,26,26,26,25,24,0,29,19,25,20,22,28],
[14,26,19,21,22,20,21,0,20,13,19,16,20],
[17,24,29,27,25,21,31,30,0,22,18,14,26],
[20,27,28,24,24,25,25,37,28,0,24,27,29],
[23,28,28,28,32,29,30,31,32,26,0,23,30],
[24,36,33,31,29,29,28,34,36,23,27,0,28],
[18,34,26,23,26,26,22,30,24,21,20,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 139, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,21,26,25,15,24,24,17,22,15,17,19],
[31,0,31,27,26,19,30,27,18,27,19,22,24],
[29,19,0,28,31,24,28,24,24,31,21,22,29],
[24,23,22,0,31,26,32,25,18,24,21,23,23],
[25,24,19,19,0,20,23,25,21,23,19,21,21],
[35,31,26,24,30,0,34,28,28,31,22,26,31],
[26,20,22,18,27,16,0,21,20,20,17,22,21],
[26,23,26,25,25,22,29,0,21,22,19,25,22],
[33,32,26,32,29,22,30,29,0,29,25,24,25],
[28,23,19,26,27,19,30,28,21,0,19,18,19],
[35,31,29,29,31,28,33,31,25,31,0,24,34],
[33,28,28,27,29,24,28,25,26,32,26,0,27],
[31,26,21,27,29,19,29,28,25,31,16,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 140, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,29,21,27,26,32,32,27,26,26,25,25],
[24,0,26,25,24,28,31,29,28,32,28,27,26],
[21,24,0,21,23,26,29,28,26,24,26,25,21],
[29,25,29,0,25,27,27,25,28,28,22,25,23],
[23,26,27,25,0,24,30,28,21,28,27,23,23],
[24,22,24,23,26,0,28,24,23,26,22,23,24],
[18,19,21,23,20,22,0,26,20,24,20,20,19],
[18,21,22,25,22,26,24,0,19,30,19,24,21],
[23,22,24,22,29,27,30,31,0,23,23,19,26],
[24,18,26,22,22,24,26,20,27,0,26,23,24],
[24,22,24,28,23,28,30,31,27,24,0,22,28],
[25,23,25,25,27,27,30,26,31,27,28,0,31],
[25,24,29,27,27,26,31,29,24,26,22,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 141, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,17,23,23,26,29,20,26,27,27,28,25],
[29,0,25,26,21,31,30,26,27,29,30,25,30],
[33,25,0,24,25,30,28,25,26,31,24,24,24],
[27,24,26,0,27,27,32,24,25,27,30,27,29],
[27,29,25,23,0,25,25,24,24,24,27,26,26],
[24,19,20,23,25,0,28,23,22,20,24,24,28],
[21,20,22,18,25,22,0,22,23,25,27,22,22],
[30,24,25,26,26,27,28,0,25,29,26,28,29],
[24,23,24,25,26,28,27,25,0,31,30,25,29],
[23,21,19,23,26,30,25,21,19,0,25,24,24],
[23,20,26,20,23,26,23,24,20,25,0,20,25],
[22,25,26,23,24,26,28,22,25,26,30,0,28],
[25,20,26,21,24,22,28,21,21,26,25,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 142, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,34,31,28,29,20,31,19,23,25,7,31],
[27,0,37,34,26,25,25,29,25,25,30,19,25],
[16,13,0,23,24,27,19,18,23,26,26,17,28],
[19,16,27,0,28,27,26,20,19,33,28,14,20],
[22,24,26,22,0,35,19,28,16,34,20,12,29],
[21,25,23,23,15,0,17,29,26,18,16,16,30],
[30,25,31,24,31,33,0,38,15,25,21,21,27],
[19,21,32,30,22,21,12,0,20,19,20,14,25],
[31,25,27,31,34,24,35,30,0,30,21,18,25],
[27,25,24,17,16,32,25,31,20,0,19,22,20],
[25,20,24,22,30,34,29,30,29,31,0,25,22],
[43,31,33,36,38,34,29,36,32,28,25,0,29],
[19,25,22,30,21,20,23,25,25,30,28,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 143, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,26,19,28,26,25,25,28,28,26,24,27],
[26,0,28,20,24,24,25,26,26,29,22,21,23],
[24,22,0,21,19,25,22,28,29,27,27,24,20],
[31,30,29,0,24,24,23,24,27,32,25,25,27],
[22,26,31,26,0,24,16,24,28,24,20,24,23],
[24,26,25,26,26,0,23,25,27,23,23,22,22],
[25,25,28,27,34,27,0,25,27,28,28,26,26],
[25,24,22,26,26,25,25,0,27,28,26,26,25],
[22,24,21,23,22,23,23,23,0,24,20,23,24],
[22,21,23,18,26,27,22,22,26,0,25,25,25],
[24,28,23,25,30,27,22,24,30,25,0,27,24],
[26,29,26,25,26,28,24,24,27,25,23,0,24],
[23,27,30,23,27,28,24,25,26,25,26,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 144, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,33,31,33,33,32,25,25,33,33,29,37],
[26,0,27,28,31,25,34,19,16,32,33,23,33],
[17,23,0,22,28,21,26,11,18,22,25,23,19],
[19,22,28,0,25,18,32,19,15,31,25,16,22],
[17,19,22,25,0,13,20,18,14,21,21,16,20],
[17,25,29,32,37,0,34,17,17,25,35,25,24],
[18,16,24,18,30,16,0,19,13,22,21,16,17],
[25,31,39,31,32,33,31,0,24,30,34,27,26],
[25,34,32,35,36,33,37,26,0,35,39,25,35],
[17,18,28,19,29,25,28,20,15,0,31,32,25],
[17,17,25,25,29,15,29,16,11,19,0,19,15],
[21,27,27,34,34,25,34,23,25,18,31,0,26],
[13,17,31,28,30,26,33,24,15,25,35,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 145, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,31,32,26,26,20,28,25,22,24,26,26],
[22,0,27,28,25,27,23,25,26,27,20,23,28],
[19,23,0,27,21,25,20,25,20,24,19,22,27],
[18,22,23,0,19,19,15,22,21,22,17,23,23],
[24,25,29,31,0,24,22,27,29,23,28,21,28],
[24,23,25,31,26,0,21,20,24,20,20,21,26],
[30,27,30,35,28,29,0,29,30,28,25,30,30],
[22,25,25,28,23,30,21,0,25,28,22,26,24],
[25,24,30,29,21,26,20,25,0,24,26,27,32],
[28,23,26,28,27,30,22,22,26,0,25,21,28],
[26,30,31,33,22,30,25,28,24,25,0,25,29],
[24,27,28,27,29,29,20,24,23,29,25,0,29],
[24,22,23,27,22,24,20,26,18,22,21,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 146, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,24,5,45,26,20,0,13,31,20,25,40],
[30,0,10,10,31,31,14,5,18,30,18,11,33],
[26,40,0,25,31,21,34,26,38,25,34,39,29],
[45,40,25,0,50,37,20,32,44,31,20,25,40],
[5,19,19,0,0,0,20,0,13,11,19,24,19],
[24,19,29,13,50,0,25,16,29,36,24,29,39],
[30,36,16,30,30,25,0,30,38,36,24,10,36],
[50,45,24,18,50,34,20,0,33,44,25,30,45],
[37,32,12,6,37,21,12,17,0,31,12,17,32],
[19,20,25,19,39,14,14,6,19,0,20,19,14],
[30,32,16,30,31,26,26,25,38,30,0,31,25],
[25,39,11,25,26,21,40,20,33,31,19,0,39],
[10,17,21,10,31,11,14,5,18,36,25,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 147, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,34,20,28,26,28,26,24,19,29,31,26],
[23,0,28,29,34,33,26,30,24,18,32,31,29],
[16,22,0,16,28,25,36,19,22,20,23,27,20],
[30,21,34,0,33,40,38,29,33,28,36,33,37],
[22,16,22,17,0,24,27,23,18,17,30,19,28],
[24,17,25,10,26,0,28,23,22,16,31,19,24],
[22,24,14,12,23,22,0,22,12,19,26,20,20],
[24,20,31,21,27,27,28,0,31,25,30,32,26],
[26,26,28,17,32,28,38,19,0,21,29,23,21],
[31,32,30,22,33,34,31,25,29,0,27,30,30],
[21,18,27,14,20,19,24,20,21,23,0,21,21],
[19,19,23,17,31,31,30,18,27,20,29,0,27],
[24,21,30,13,22,26,30,24,29,20,29,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 148, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,26,32,28,34,29,27,26,25,26,36,32],
[20,0,21,29,25,35,24,30,17,23,20,28,27],
[24,29,0,26,28,32,17,28,21,25,19,26,28],
[18,21,24,0,28,33,21,24,20,19,20,28,29],
[22,25,22,22,0,29,24,32,13,25,19,22,30],
[16,15,18,17,21,0,17,27,19,21,13,24,24],
[21,26,33,29,26,33,0,31,25,26,26,30,34],
[23,20,22,26,18,23,19,0,17,23,14,30,24],
[24,33,29,30,37,31,25,33,0,28,29,35,28],
[25,27,25,31,25,29,24,27,22,0,19,28,29],
[24,30,31,30,31,37,24,36,21,31,0,39,28],
[14,22,24,22,28,26,20,20,15,22,11,0,28],
[18,23,22,21,20,26,16,26,22,21,22,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 149, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,18,22,23,21,29,24,26,28,30,25,20],
[33,0,27,25,26,31,31,25,30,31,31,33,25],
[32,23,0,25,24,28,31,24,28,31,32,30,26],
[28,25,25,0,27,26,28,27,28,27,31,27,24],
[27,24,26,23,0,32,30,22,27,26,28,29,18],
[29,19,22,24,18,0,28,24,25,29,26,30,21],
[21,19,19,22,20,22,0,15,21,22,26,27,17],
[26,25,26,23,28,26,35,0,29,29,32,30,19],
[24,20,22,22,23,25,29,21,0,22,26,23,20],
[22,19,19,23,24,21,28,21,28,0,30,27,14],
[20,19,18,19,22,24,24,18,24,20,0,25,14],
[25,17,20,23,21,20,23,20,27,23,25,0,17],
[30,25,24,26,32,29,33,31,30,36,36,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 150, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,24,29,26,21,21,31,29,27,21,19,19],
[30,0,21,30,27,33,20,34,24,30,24,19,23],
[26,29,0,32,28,30,27,30,27,22,24,33,30],
[21,20,18,0,22,20,19,21,18,21,19,16,19],
[24,23,22,28,0,23,22,28,26,23,22,14,18],
[29,17,20,30,27,0,26,24,25,23,21,18,23],
[29,30,23,31,28,24,0,37,26,32,20,23,21],
[19,16,20,29,22,26,13,0,21,23,14,13,17],
[21,26,23,32,24,25,24,29,0,28,25,25,26],
[23,20,28,29,27,27,18,27,22,0,19,18,18],
[29,26,26,31,28,29,30,36,25,31,0,24,24],
[31,31,17,34,36,32,27,37,25,32,26,0,23],
[31,27,20,31,32,27,29,33,24,32,26,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 151, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,18,34,48,15,21,33,18,21,33,29,33],
[15,0,18,16,15,16,36,34,0,34,16,15,16],
[32,32,0,30,30,30,32,32,17,32,30,30,32],
[16,34,20,0,29,17,21,35,34,20,32,29,35],
[2,35,20,21,0,17,21,21,20,21,35,14,21],
[35,34,20,33,33,0,21,20,20,20,18,15,20],
[29,14,18,29,29,29,0,14,14,14,14,29,14],
[17,16,18,15,29,30,36,0,2,2,14,29,17],
[32,50,33,16,30,30,36,48,0,36,48,29,32],
[29,16,18,30,29,30,36,48,14,0,30,29,15],
[17,34,20,18,15,32,36,36,2,20,0,29,3],
[21,35,20,21,36,35,21,21,21,21,21,0,21],
[17,34,18,15,29,30,36,33,18,35,47,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 152, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,20,23,21,18,25,22,19,29,29,20,15],
[29,0,30,26,25,31,26,20,26,37,31,29,25],
[30,20,0,30,23,32,28,22,29,38,33,29,22],
[27,24,20,0,27,30,28,22,19,28,38,23,20],
[29,25,27,23,0,36,26,26,25,32,31,27,18],
[32,19,18,20,14,0,29,19,24,27,29,25,12],
[25,24,22,22,24,21,0,22,17,30,29,18,18],
[28,30,28,28,24,31,28,0,24,38,35,30,26],
[31,24,21,31,25,26,33,26,0,39,30,28,20],
[21,13,12,22,18,23,20,12,11,0,23,15,13],
[21,19,17,12,19,21,21,15,20,27,0,21,10],
[30,21,21,27,23,25,32,20,22,35,29,0,20],
[35,25,28,30,32,38,32,24,30,37,40,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 153, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,43,23,43,43,43,26,23,43,43,43,37],
[27,0,43,43,37,43,43,26,43,26,43,43,20],
[7,7,0,23,37,43,43,20,23,26,26,26,20],
[27,7,27,0,44,44,37,27,27,20,33,27,27],
[7,13,13,6,0,43,26,26,6,26,26,26,20],
[7,7,7,6,7,0,6,27,7,0,33,27,7],
[7,7,7,13,24,44,0,27,7,20,33,27,7],
[24,24,30,23,24,23,23,0,23,23,23,43,17],
[27,7,27,23,44,43,43,27,0,20,26,27,20],
[7,24,24,30,24,50,30,27,30,0,50,44,24],
[7,7,24,17,24,17,17,27,24,0,0,44,0],
[7,7,24,23,24,23,23,7,23,6,6,0,0],
[13,30,30,23,30,43,43,33,30,26,50,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 154, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,21,24,27,27,24,28,26,26,25,27,27],
[22,0,23,20,23,21,27,18,21,23,25,22,21],
[29,27,0,20,30,23,28,25,20,24,22,26,24],
[26,30,30,0,30,26,30,29,25,31,29,30,30],
[23,27,20,20,0,20,20,19,23,20,22,21,23],
[23,29,27,24,30,0,25,26,24,24,29,28,28],
[26,23,22,20,30,25,0,24,22,20,24,22,20],
[22,32,25,21,31,24,26,0,28,21,24,26,26],
[24,29,30,25,27,26,28,22,0,21,24,27,26],
[24,27,26,19,30,26,30,29,29,0,29,26,22],
[25,25,28,21,28,21,26,26,26,21,0,26,24],
[23,28,24,20,29,22,28,24,23,24,24,0,30],
[23,29,26,20,27,22,30,24,24,28,26,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 155, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,25,50,25,25,25,25,0,25,50,25,25],
[25,0,25,25,0,50,25,25,25,50,25,25,25],
[25,25,0,25,0,50,25,0,0,25,25,0,0],
[0,25,25,0,25,25,25,25,0,25,25,0,25],
[25,50,50,25,0,50,50,25,25,50,50,25,50],
[25,0,0,25,0,0,0,0,0,25,25,0,0],
[25,25,25,25,0,50,0,0,0,25,50,0,25],
[25,25,50,25,25,50,50,0,25,50,50,25,50],
[50,25,50,50,25,50,50,25,0,25,50,50,25],
[25,0,25,25,0,25,25,0,25,0,25,25,0],
[0,25,25,25,0,25,0,0,0,25,0,0,0],
[25,25,50,50,25,50,50,25,0,25,50,0,25],
[25,25,50,25,0,50,25,0,25,50,50,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 156, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,38,32,36,27,31,34,25,27,29,35,37],
[21,0,19,21,25,23,32,28,26,24,25,21,25],
[12,31,0,26,24,29,36,16,22,24,26,24,21],
[18,29,24,0,22,28,24,19,28,17,26,27,22],
[14,25,26,28,0,14,30,18,19,14,25,16,21],
[23,27,21,22,36,0,25,22,22,28,24,16,23],
[19,18,14,26,20,25,0,28,23,25,27,20,26],
[16,22,34,31,32,28,22,0,19,16,22,20,29],
[25,24,28,22,31,28,27,31,0,24,27,28,24],
[23,26,26,33,36,22,25,34,26,0,32,19,28],
[21,25,24,24,25,26,23,28,23,18,0,15,18],
[15,29,26,23,34,34,30,30,22,31,35,0,37],
[13,25,29,28,29,27,24,21,26,22,32,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 157, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,30,26,28,27,28,26,29,17,27,26,22],
[24,0,26,24,27,21,29,21,28,18,23,23,26],
[20,24,0,22,21,22,22,19,27,20,21,21,20],
[24,26,28,0,24,25,31,29,23,20,23,26,28],
[22,23,29,26,0,22,29,26,26,20,28,25,27],
[23,29,28,25,28,0,26,25,24,19,22,23,23],
[22,21,28,19,21,24,0,20,28,18,24,25,23],
[24,29,31,21,24,25,30,0,29,17,21,27,25],
[21,22,23,27,24,26,22,21,0,22,28,24,26],
[33,32,30,30,30,31,32,33,28,0,26,25,30],
[23,27,29,27,22,28,26,29,22,24,0,27,27],
[24,27,29,24,25,27,25,23,26,25,23,0,26],
[28,24,30,22,23,27,27,25,24,20,23,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 158, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,28,30,20,18,20,26,20,25,35,24,18],
[28,0,31,29,21,28,30,32,30,27,35,26,27],
[22,19,0,26,23,20,20,24,23,28,31,20,22],
[20,21,24,0,13,18,28,28,24,25,27,21,19],
[30,29,27,37,0,28,32,34,30,28,34,28,24],
[32,22,30,32,22,0,31,30,27,35,35,30,28],
[30,20,30,22,18,19,0,29,23,23,29,22,19],
[24,18,26,22,16,20,21,0,21,23,23,18,19],
[30,20,27,26,20,23,27,29,0,26,28,23,21],
[25,23,22,25,22,15,27,27,24,0,33,22,18],
[15,15,19,23,16,15,21,27,22,17,0,22,15],
[26,24,30,29,22,20,28,32,27,28,28,0,25],
[32,23,28,31,26,22,31,31,29,32,35,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 159, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,23,19,16,30,23,22,22,14,16,19,17],
[20,0,14,12,12,20,19,19,16,14,12,10,17],
[27,36,0,31,23,34,31,24,24,22,24,24,25],
[31,38,19,0,28,24,32,18,23,19,31,26,28],
[34,38,27,22,0,30,26,24,27,25,20,22,28],
[20,30,16,26,20,0,24,26,24,21,23,18,22],
[27,31,19,18,24,26,0,23,24,22,18,17,21],
[28,31,26,32,26,24,27,0,32,17,28,23,31],
[28,34,26,27,23,26,26,18,0,17,23,27,29],
[36,36,28,31,25,29,28,33,33,0,32,24,32],
[34,38,26,19,30,27,32,22,27,18,0,29,36],
[31,40,26,24,28,32,33,27,23,26,21,0,27],
[33,33,25,22,22,28,29,19,21,18,14,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 160, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,26,29,24,26,24,22,20,28,23,30,34],
[26,0,22,22,25,24,22,18,20,21,20,28,23],
[24,28,0,26,31,31,25,20,25,28,26,34,33],
[21,28,24,0,26,23,21,18,19,23,21,23,25],
[26,25,19,24,0,19,22,16,18,17,19,24,25],
[24,26,19,27,31,0,30,18,21,22,18,29,26],
[26,28,25,29,28,20,0,25,29,21,24,28,27],
[28,32,30,32,34,32,25,0,22,27,24,34,34],
[30,30,25,31,32,29,21,28,0,22,23,30,32],
[22,29,22,27,33,28,29,23,28,0,24,32,26],
[27,30,24,29,31,32,26,26,27,26,0,31,31],
[20,22,16,27,26,21,22,16,20,18,19,0,21],
[16,27,17,25,25,24,23,16,18,24,19,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 161, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,22,21,27,22,26,23,25,20,23,29,22],
[26,0,23,18,20,26,19,22,26,16,23,24,21],
[28,27,0,20,22,28,23,25,26,22,23,32,20],
[29,32,30,0,23,31,27,30,31,25,30,26,27],
[23,30,28,27,0,25,29,20,29,24,24,29,25],
[28,24,22,19,25,0,25,21,25,20,19,25,26],
[24,31,27,23,21,25,0,23,32,23,24,29,24],
[27,28,25,20,30,29,27,0,29,21,26,30,26],
[25,24,24,19,21,25,18,21,0,18,17,25,18],
[30,34,28,25,26,30,27,29,32,0,27,28,29],
[27,27,27,20,26,31,26,24,33,23,0,31,26],
[21,26,18,24,21,25,21,20,25,22,19,0,17],
[28,29,30,23,25,24,26,24,32,21,24,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 162, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,18,8,14,21,10,17,15,14,21,24,19],
[33,0,18,8,21,23,17,15,18,16,30,31,27],
[32,32,0,20,32,31,21,23,26,21,28,30,33],
[42,42,30,0,32,36,23,25,33,30,33,40,34],
[36,29,18,18,0,28,17,19,11,15,28,33,19],
[29,27,19,14,22,0,14,21,15,12,31,34,24],
[40,33,29,27,33,36,0,25,29,18,33,40,27],
[33,35,27,25,31,29,25,0,33,19,36,39,27],
[35,32,24,17,39,35,21,17,0,23,38,36,23],
[36,34,29,20,35,38,32,31,27,0,31,37,29],
[29,20,22,17,22,19,17,14,12,19,0,37,26],
[26,19,20,10,17,16,10,11,14,13,13,0,23],
[31,23,17,16,31,26,23,23,27,21,24,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 163, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,29,38,27,18,26,25,29,26,22,30,31],
[17,0,32,28,24,21,25,22,26,24,16,27,30],
[21,18,0,28,29,18,19,18,24,22,23,20,24],
[12,22,22,0,24,20,23,24,23,19,15,23,26],
[23,26,21,26,0,21,21,19,21,24,15,17,31],
[32,29,32,30,29,0,32,23,33,21,19,25,36],
[24,25,31,27,29,18,0,23,30,24,23,23,36],
[25,28,32,26,31,27,27,0,35,27,24,26,32],
[21,24,26,27,29,17,20,15,0,26,25,19,28],
[24,26,28,31,26,29,26,23,24,0,20,29,34],
[28,34,27,35,35,31,27,26,25,30,0,33,39],
[20,23,30,27,33,25,27,24,31,21,17,0,28],
[19,20,26,24,19,14,14,18,22,16,11,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 164, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,25,25,26,21,25,23,26,32,31,30,30],
[22,0,22,22,17,21,32,23,26,33,35,25,25],
[25,28,0,20,18,12,32,19,29,36,28,32,23],
[25,28,30,0,32,27,25,28,24,33,29,27,27],
[24,33,32,18,0,26,31,26,26,40,28,31,32],
[29,29,38,23,24,0,33,30,34,43,35,37,38],
[25,18,18,25,19,17,0,24,22,24,34,20,15],
[27,27,31,22,24,20,26,0,30,38,32,35,28],
[24,24,21,26,24,16,28,20,0,37,30,35,25],
[18,17,14,17,10,7,26,12,13,0,20,25,21],
[19,15,22,21,22,15,16,18,20,30,0,23,19],
[20,25,18,23,19,13,30,15,15,25,27,0,21],
[20,25,27,23,18,12,35,22,25,29,31,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 165, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,19,18,17,26,18,18,23,29,28,22,16],
[28,0,24,20,13,26,16,14,22,22,15,18,8],
[31,26,0,23,21,26,14,16,36,34,35,32,16],
[32,30,27,0,30,31,26,25,27,40,32,30,25],
[33,37,29,20,0,29,11,23,24,30,28,25,22],
[24,24,24,19,21,0,22,21,31,30,16,23,24],
[32,34,36,24,39,28,0,26,32,37,35,31,22],
[32,36,34,25,27,29,24,0,33,42,30,32,19],
[27,28,14,23,26,19,18,17,0,29,32,27,18],
[21,28,16,10,20,20,13,8,21,0,18,21,8],
[22,35,15,18,22,34,15,20,18,32,0,36,8],
[28,32,18,20,25,27,19,18,23,29,14,0,22],
[34,42,34,25,28,26,28,31,32,42,42,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 166, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,35,24,26,37,49,27,49,27,49,28,27],
[14,0,8,0,26,14,26,0,26,12,26,12,12],
[15,42,0,15,26,30,41,28,26,12,41,28,12],
[26,50,35,0,26,41,41,27,26,12,41,27,27],
[24,24,24,24,0,38,49,24,37,35,49,24,35],
[13,36,20,9,12,0,20,13,20,12,20,13,12],
[1,24,9,9,1,30,0,1,23,13,42,1,13],
[23,50,22,23,26,37,49,0,34,34,49,36,34],
[1,24,24,24,13,30,27,16,0,12,42,28,27],
[23,38,38,38,15,38,37,16,38,0,50,16,16],
[1,24,9,9,1,30,8,1,8,0,0,1,0],
[22,38,22,23,26,37,49,14,22,34,49,0,34],
[23,38,38,23,15,38,37,16,23,34,50,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 167, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,35,31,32,31,22,36,33,21,19,32,22],
[27,0,30,36,29,28,28,37,36,20,29,30,24],
[15,20,0,22,31,29,16,31,34,16,19,24,23],
[19,14,28,0,27,29,15,25,26,21,31,24,29],
[18,21,19,23,0,24,17,26,26,15,18,29,21],
[19,22,21,21,26,0,17,26,33,20,22,26,23],
[28,22,34,35,33,33,0,38,37,26,28,32,27],
[14,13,19,25,24,24,12,0,22,22,18,20,21],
[17,14,16,24,24,17,13,28,0,22,18,15,22],
[29,30,34,29,35,30,24,28,28,0,29,33,25],
[31,21,31,19,32,28,22,32,32,21,0,32,22],
[18,20,26,26,21,24,18,30,35,17,18,0,19],
[28,26,27,21,29,27,23,29,28,25,28,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 168, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,7,16,7,22,32,8,16,36,16,1,15],
[42,0,12,12,12,26,33,13,25,45,12,18,10],
[43,38,0,33,18,18,35,32,32,46,26,18,25],
[34,38,17,0,5,15,33,16,27,38,27,19,25],
[43,38,32,45,0,29,45,26,29,46,37,15,37],
[28,24,32,35,21,0,33,21,19,33,27,7,32],
[18,17,15,17,5,17,0,4,10,15,17,4,25],
[42,37,18,34,24,29,46,0,33,46,25,31,25],
[34,25,18,23,21,31,40,17,0,39,16,17,19],
[14,5,4,12,4,17,35,4,11,0,11,4,10],
[34,38,24,23,13,23,33,25,34,39,0,18,32],
[49,32,32,31,35,43,46,19,33,46,32,0,32],
[35,40,25,25,13,18,25,25,31,40,18,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 169, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,38,26,29,28,26,27,29,20,33,30,30],
[18,0,29,29,28,32,14,35,21,25,21,30,30],
[12,21,0,21,19,23,15,20,20,21,12,18,23],
[24,21,29,0,24,24,17,25,21,26,22,21,24],
[21,22,31,26,0,30,17,24,21,31,24,18,21],
[22,18,27,26,20,0,12,29,21,24,26,26,19],
[24,36,35,33,33,38,0,36,28,26,33,30,30],
[23,15,30,25,26,21,14,0,22,26,24,23,26],
[21,29,30,29,29,29,22,28,0,18,25,29,23],
[30,25,29,24,19,26,24,24,32,0,29,20,21],
[17,29,38,28,26,24,17,26,25,21,0,29,23],
[20,20,32,29,32,24,20,27,21,30,21,0,24],
[20,20,27,26,29,31,20,24,27,29,27,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 170, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,23,22,20,20,24,20,30,21,22,29,19],
[38,0,35,29,23,35,35,28,33,26,22,39,33],
[27,15,0,15,19,23,26,20,22,18,20,31,18],
[28,21,35,0,22,31,30,19,32,25,26,32,27],
[30,27,31,28,0,21,30,26,32,25,25,36,30],
[30,15,27,19,29,0,26,24,26,26,24,32,24],
[26,15,24,20,20,24,0,20,27,21,19,29,24],
[30,22,30,31,24,26,30,0,36,16,19,39,21],
[20,17,28,18,18,24,23,14,0,15,21,29,18],
[29,24,32,25,25,24,29,34,35,0,20,34,26],
[28,28,30,24,25,26,31,31,29,30,0,40,29],
[21,11,19,18,14,18,21,11,21,16,10,0,12],
[31,17,32,23,20,26,26,29,32,24,21,38,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 171, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,29,27,36,29,33,34,26,29,25,30,27],
[21,0,30,25,30,24,29,38,26,32,29,21,25],
[21,20,0,26,28,22,21,24,22,22,17,22,18],
[23,25,24,0,32,29,20,36,24,25,24,29,28],
[14,20,22,18,0,20,18,28,20,25,19,14,19],
[21,26,28,21,30,0,26,33,18,27,21,20,23],
[17,21,29,30,32,24,0,29,22,28,25,20,27],
[16,12,26,14,22,17,21,0,11,24,14,14,21],
[24,24,28,26,30,32,28,39,0,29,23,26,29],
[21,18,28,25,25,23,22,26,21,0,21,20,28],
[25,21,33,26,31,29,25,36,27,29,0,26,27],
[20,29,28,21,36,30,30,36,24,30,24,0,29],
[23,25,32,22,31,27,23,29,21,22,23,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 172, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,27,26,37,29,26,31,21,32,23,25,39],
[23,0,33,29,29,30,30,30,18,25,24,23,32],
[23,17,0,26,28,24,22,32,21,27,18,20,31],
[24,21,24,0,29,28,25,32,24,28,20,23,27],
[13,21,22,21,0,19,24,28,21,29,21,19,29],
[21,20,26,22,31,0,26,29,15,30,13,21,28],
[24,20,28,25,26,24,0,35,15,23,22,21,32],
[19,20,18,18,22,21,15,0,15,17,20,19,29],
[29,32,29,26,29,35,35,35,0,24,37,28,33],
[18,25,23,22,21,20,27,33,26,0,21,18,34],
[27,26,32,30,29,37,28,30,13,29,0,29,37],
[25,27,30,27,31,29,29,31,22,32,21,0,37],
[11,18,19,23,21,22,18,21,17,16,13,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 173, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,23,24,25,22,25,17,24,26,27,25,24],
[21,0,28,21,16,20,25,21,25,30,22,22,21],
[27,22,0,22,15,21,26,21,22,23,17,21,21],
[26,29,28,0,20,21,23,25,22,22,19,24,26],
[25,34,35,30,0,29,35,34,25,31,26,27,27],
[28,30,29,29,21,0,31,24,25,29,25,26,25],
[25,25,24,27,15,19,0,21,17,23,17,23,18],
[33,29,29,25,16,26,29,0,20,31,26,24,28],
[26,25,28,28,25,25,33,30,0,33,23,28,30],
[24,20,27,28,19,21,27,19,17,0,18,24,25],
[23,28,33,31,24,25,33,24,27,32,0,31,32],
[25,28,29,26,23,24,27,26,22,26,19,0,24],
[26,29,29,24,23,25,32,22,20,25,18,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 174, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,23,23,22,21,21,19,27,26,21,18,18],
[26,0,33,28,28,27,25,22,27,27,29,29,26],
[27,17,0,26,30,22,21,14,23,21,19,19,17],
[27,22,24,0,28,23,27,20,27,23,25,19,16],
[28,22,20,22,0,22,23,23,31,24,20,19,20],
[29,23,28,27,28,0,26,25,23,28,29,23,19],
[29,25,29,23,27,24,0,20,26,18,28,25,22],
[31,28,36,30,27,25,30,0,32,27,28,28,24],
[23,23,27,23,19,27,24,18,0,24,24,21,21],
[24,23,29,27,26,22,32,23,26,0,22,24,18],
[29,21,31,25,30,21,22,22,26,28,0,24,20],
[32,21,31,31,31,27,25,22,29,26,26,0,22],
[32,24,33,34,30,31,28,26,29,32,30,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 175, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,24,23,24,24,21,23,21,17,25,26,24],
[23,0,26,21,24,24,20,23,23,20,31,23,23],
[26,24,0,25,24,25,23,24,27,24,26,22,25],
[27,29,25,0,25,30,30,21,28,28,31,28,26],
[26,26,26,25,0,28,23,24,24,24,28,28,22],
[26,26,25,20,22,0,24,24,20,24,26,24,24],
[29,30,27,20,27,26,0,28,23,22,26,25,27],
[27,27,26,29,26,26,22,0,23,26,27,25,24],
[29,27,23,22,26,30,27,27,0,27,30,26,23],
[33,30,26,22,26,26,28,24,23,0,30,26,27],
[25,19,24,19,22,24,24,23,20,20,0,17,23],
[24,27,28,22,22,26,25,25,24,24,33,0,26],
[26,27,25,24,28,26,23,26,27,23,27,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 176, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,24,35,28,29,26,33,26,31,32,25,29],
[22,0,26,32,27,34,28,28,33,23,32,25,26],
[26,24,0,26,25,27,25,25,29,23,29,21,25],
[15,18,24,0,26,25,18,24,22,22,19,22,21],
[22,23,25,24,0,28,26,18,25,23,32,26,25],
[21,16,23,25,22,0,21,24,24,20,23,22,21],
[24,22,25,32,24,29,0,27,29,23,30,23,22],
[17,22,25,26,32,26,23,0,21,24,32,23,20],
[24,17,21,28,25,26,21,29,0,27,27,21,25],
[19,27,27,28,27,30,27,26,23,0,30,27,26],
[18,18,21,31,18,27,20,18,23,20,0,16,20],
[25,25,29,28,24,28,27,27,29,23,34,0,25],
[21,24,25,29,25,29,28,30,25,24,30,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 177, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,29,30,28,21,31,22,26,22,27,29,32],
[26,0,23,27,29,25,29,23,27,19,27,30,26],
[21,27,0,24,25,26,26,23,24,20,28,25,28],
[20,23,26,0,25,23,28,24,21,17,28,26,28],
[22,21,25,25,0,19,24,19,25,22,20,28,28],
[29,25,24,27,31,0,32,28,27,20,28,33,35],
[19,21,24,22,26,18,0,20,25,17,21,27,27],
[28,27,27,26,31,22,30,0,31,25,28,27,30],
[24,23,26,29,25,23,25,19,0,21,24,23,32],
[28,31,30,33,28,30,33,25,29,0,26,30,31],
[23,23,22,22,30,22,29,22,26,24,0,26,25],
[21,20,25,24,22,17,23,23,27,20,24,0,30],
[18,24,22,22,22,15,23,20,18,19,25,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 178, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,34,27,34,20,26,21,12,33,20,30,36],
[20,0,28,11,26,30,24,25,19,27,16,24,30],
[16,22,0,26,32,28,22,27,17,23,12,17,28],
[23,39,24,0,30,22,32,22,28,33,18,29,35],
[16,24,18,20,0,25,19,18,15,29,9,21,38],
[30,20,22,28,25,0,31,22,29,34,12,27,34],
[24,26,28,18,31,19,0,26,13,32,19,24,38],
[29,25,23,28,32,28,24,0,22,36,16,25,32],
[38,31,33,22,35,21,37,28,0,35,27,38,39],
[17,23,27,17,21,16,18,14,15,0,11,16,28],
[30,34,38,32,41,38,31,34,23,39,0,34,43],
[20,26,33,21,29,23,26,25,12,34,16,0,38],
[14,20,22,15,12,16,12,18,11,22,7,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 179, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,26,24,23,25,21,18,24,31,23,29,23],
[28,0,21,19,22,21,19,19,24,24,26,29,24],
[24,29,0,23,27,24,17,22,23,30,29,31,26],
[26,31,27,0,27,29,23,21,27,30,29,35,30],
[27,28,23,23,0,24,22,20,21,25,24,31,30],
[25,29,26,21,26,0,22,25,28,29,24,32,27],
[29,31,33,27,28,28,0,21,29,30,28,34,31],
[32,31,28,29,30,25,29,0,30,31,32,38,29],
[26,26,27,23,29,22,21,20,0,26,27,33,26],
[19,26,20,20,25,21,20,19,24,0,23,32,23],
[27,24,21,21,26,26,22,18,23,27,0,27,28],
[21,21,19,15,19,18,16,12,17,18,23,0,22],
[27,26,24,20,20,23,19,21,24,27,22,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 180, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,34,32,32,33,21,31,29,21,26,27,39],
[23,0,29,30,25,26,19,27,28,23,26,29,32],
[16,21,0,22,26,25,18,24,27,19,26,22,31],
[18,20,28,0,23,28,25,21,24,12,22,34,35],
[18,25,24,27,0,30,21,22,26,25,26,28,34],
[17,24,25,22,20,0,16,24,20,16,23,26,29],
[29,31,32,25,29,34,0,33,29,22,32,27,34],
[19,23,26,29,28,26,17,0,23,23,29,29,25],
[21,22,23,26,24,30,21,27,0,20,21,25,31],
[29,27,31,38,25,34,28,27,30,0,28,30,38],
[24,24,24,28,24,27,18,21,29,22,0,24,30],
[23,21,28,16,22,24,23,21,25,20,26,0,30],
[11,18,19,15,16,21,16,25,19,12,20,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 181, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,39,10,34,34,18,27,17,15,23,34,28],
[23,0,29,17,25,28,17,24,12,15,23,33,29],
[11,21,0,7,29,27,17,12,15,18,15,14,19],
[40,33,43,0,39,38,30,35,25,24,27,37,26],
[16,25,21,11,0,19,19,19,20,16,17,24,26],
[16,22,23,12,31,0,17,19,15,20,17,25,21],
[32,33,33,20,31,33,0,31,20,28,25,29,30],
[23,26,38,15,31,31,19,0,17,18,22,30,31],
[33,38,35,25,30,35,30,33,0,30,25,39,35],
[35,35,32,26,34,30,22,32,20,0,24,30,28],
[27,27,35,23,33,33,25,28,25,26,0,36,32],
[16,17,36,13,26,25,21,20,11,20,14,0,29],
[22,21,31,24,24,29,20,19,15,22,18,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 182, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,27,27,27,31,33,25,29,36,32,23,31],
[15,0,28,28,37,26,20,25,21,27,20,28,29],
[23,22,0,23,28,23,23,29,23,28,21,23,25],
[23,22,27,0,33,25,30,27,26,32,25,29,32],
[23,13,22,17,0,20,21,20,28,34,23,19,32],
[19,24,27,25,30,0,20,32,16,31,24,29,25],
[17,30,27,20,29,30,0,24,27,35,31,23,37],
[25,25,21,23,30,18,26,0,21,35,23,22,24],
[21,29,27,24,22,34,23,29,0,31,24,33,30],
[14,23,22,18,16,19,15,15,19,0,15,21,23],
[18,30,29,25,27,26,19,27,26,35,0,23,30],
[27,22,27,21,31,21,27,28,17,29,27,0,32],
[19,21,25,18,18,25,13,26,20,27,20,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 183, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,21,24,22,28,22,25,25,19,22,23,23],
[30,0,27,28,28,28,32,27,32,27,26,24,24],
[29,23,0,27,21,25,21,21,27,23,25,22,31],
[26,22,23,0,29,26,29,22,29,23,21,23,25],
[28,22,29,21,0,24,23,21,29,18,22,21,27],
[22,22,25,24,26,0,24,22,28,20,22,25,25],
[28,18,29,21,27,26,0,21,29,26,22,21,27],
[25,23,29,28,29,28,29,0,29,27,24,25,26],
[25,18,23,21,21,22,21,21,0,19,20,18,21],
[31,23,27,27,32,30,24,23,31,0,23,23,28],
[28,24,25,29,28,28,28,26,30,27,0,27,25],
[27,26,28,27,29,25,29,25,32,27,23,0,25],
[27,26,19,25,23,25,23,24,29,22,25,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 184, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,29,22,25,21,28,30,20,24,26,25,23],
[20,0,25,19,12,17,16,20,21,19,22,17,17],
[21,25,0,24,19,21,25,21,22,25,22,22,19],
[28,31,26,0,18,25,27,30,28,27,28,26,28],
[25,38,31,32,0,29,35,33,32,33,30,25,28],
[29,33,29,25,21,0,32,30,27,25,28,25,24],
[22,34,25,23,15,18,0,25,26,19,22,17,24],
[20,30,29,20,17,20,25,0,24,23,18,21,20],
[30,29,28,22,18,23,24,26,0,27,21,23,19],
[26,31,25,23,17,25,31,27,23,0,23,27,24],
[24,28,28,22,20,22,28,32,29,27,0,23,25],
[25,33,28,24,25,25,33,29,27,23,27,0,28],
[27,33,31,22,22,26,26,30,31,26,25,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 185, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,30,22,22,23,23,22,27,26,27,24,23],
[28,0,27,26,26,25,26,27,28,27,22,28,24],
[20,23,0,22,21,22,21,23,23,22,22,22,19],
[28,24,28,0,24,24,25,24,28,23,30,27,22],
[28,24,29,26,0,23,27,20,29,25,23,24,23],
[27,25,28,26,27,0,32,31,33,28,28,29,26],
[27,24,29,25,23,18,0,26,27,22,27,20,21],
[28,23,27,26,30,19,24,0,24,25,26,27,23],
[23,22,27,22,21,17,23,26,0,21,26,27,17],
[24,23,28,27,25,22,28,25,29,0,25,25,16],
[23,28,28,20,27,22,23,24,24,25,0,28,22],
[26,22,28,23,26,21,30,23,23,25,22,0,21],
[27,26,31,28,27,24,29,27,33,34,28,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 186, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,26,27,24,22,22,20,23,31,22,21,26],
[23,0,19,27,21,17,31,25,16,27,23,24,20],
[24,31,0,31,22,30,33,27,25,35,24,28,23],
[23,23,19,0,22,20,23,27,18,26,19,16,18],
[26,29,28,28,0,28,31,27,21,28,22,29,25],
[28,33,20,30,22,0,28,31,20,32,19,26,22],
[28,19,17,27,19,22,0,23,18,32,19,23,18],
[30,25,23,23,23,19,27,0,23,28,21,20,22],
[27,34,25,32,29,30,32,27,0,39,26,31,23],
[19,23,15,24,22,18,18,22,11,0,24,19,14],
[28,27,26,31,28,31,31,29,24,26,0,26,23],
[29,26,22,34,21,24,27,30,19,31,24,0,25],
[24,30,27,32,25,28,32,28,27,36,27,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 187, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,21,16,30,30,18,39,30,27,32,44,28],
[23,0,29,19,17,26,24,13,29,29,34,24,23],
[29,21,0,15,22,24,17,24,20,26,18,23,23],
[34,31,35,0,20,31,25,24,32,37,29,28,22],
[20,33,28,30,0,18,12,21,22,29,22,23,27],
[20,24,26,19,32,0,18,24,29,33,33,26,26],
[32,26,33,25,38,32,0,28,31,36,28,37,32],
[11,37,26,26,29,26,22,0,30,23,36,26,17],
[20,21,30,18,28,21,19,20,0,29,23,16,29],
[23,21,24,13,21,17,14,27,21,0,16,25,16],
[18,16,32,21,28,17,22,14,27,34,0,24,24],
[6,26,27,22,27,24,13,24,34,25,26,0,25],
[22,27,27,28,23,24,18,33,21,34,26,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 188, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,20,30,33,28,24,28,27,24,28,18,22],
[28,0,19,30,25,26,22,28,29,23,27,22,24],
[30,31,0,36,25,32,27,34,29,31,34,22,27],
[20,20,14,0,23,24,24,24,21,27,24,21,25],
[17,25,25,27,0,33,25,25,26,24,26,24,20],
[22,24,18,26,17,0,17,19,21,17,21,14,15],
[26,28,23,26,25,33,0,32,25,29,29,22,24],
[22,22,16,26,25,31,18,0,26,27,25,19,21],
[23,21,21,29,24,29,25,24,0,24,23,26,24],
[26,27,19,23,26,33,21,23,26,0,24,21,26],
[22,23,16,26,24,29,21,25,27,26,0,20,19],
[32,28,28,29,26,36,28,31,24,29,30,0,27],
[28,26,23,25,30,35,26,29,26,24,31,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 189, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,14,35,18,23,28,27,31,31,20,15,23],
[19,0,14,34,20,27,37,30,35,28,19,21,28],
[36,36,0,40,26,30,44,34,34,43,25,32,28],
[15,16,10,0,17,16,27,29,31,32,8,20,28],
[32,30,24,33,0,34,36,28,33,32,19,22,24],
[27,23,20,34,16,0,36,26,30,35,20,30,21],
[22,13,6,23,14,14,0,20,27,26,7,15,21],
[23,20,16,21,22,24,30,0,37,34,13,18,21],
[19,15,16,19,17,20,23,13,0,32,10,18,15],
[19,22,7,18,18,15,24,16,18,0,10,10,15],
[30,31,25,42,31,30,43,37,40,40,0,24,38],
[35,29,18,30,28,20,35,32,32,40,26,0,26],
[27,22,22,22,26,29,29,29,35,35,12,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 190, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,47,25,25,38,40,25,38,28,25,40,25],
[35,0,50,32,40,50,40,40,50,50,40,32,25],
[3,0,0,17,18,28,32,7,20,21,15,22,25],
[25,18,33,0,30,33,33,33,21,33,33,40,35],
[25,10,32,20,0,43,35,22,23,31,40,42,35],
[12,0,22,17,7,0,25,12,20,13,22,29,17],
[10,10,18,17,15,25,0,8,25,21,18,7,25],
[25,10,43,17,28,38,42,0,38,31,28,32,25],
[12,0,30,29,27,30,25,12,0,33,20,19,25],
[22,0,29,17,19,37,29,19,17,0,19,19,17],
[25,10,35,17,10,28,32,22,30,31,0,22,17],
[10,18,28,10,8,21,43,18,31,31,28,0,28],
[25,25,25,15,15,33,25,25,25,33,33,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 191, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,25,18,20,19,17,18,20,31,23,24,13],
[26,0,26,22,21,21,23,24,18,29,21,28,22],
[25,24,0,21,19,18,26,17,15,30,28,24,21],
[32,28,29,0,27,26,27,25,25,30,27,28,30],
[30,29,31,23,0,23,31,28,19,31,21,30,23],
[31,29,32,24,27,0,31,26,27,36,27,28,17],
[33,27,24,23,19,19,0,17,15,27,26,25,23],
[32,26,33,25,22,24,33,0,17,31,25,29,21],
[30,32,35,25,31,23,35,33,0,37,29,32,23],
[19,21,20,20,19,14,23,19,13,0,21,19,16],
[27,29,22,23,29,23,24,25,21,29,0,26,24],
[26,22,26,22,20,22,25,21,18,31,24,0,17],
[37,28,29,20,27,33,27,29,27,34,26,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 192, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,35,22,20,21,29,35,26,24,19,18,16],
[35,0,38,21,22,28,36,28,27,33,24,24,25],
[15,12,0,18,18,15,18,28,18,24,13,10,20],
[28,29,32,0,23,22,31,27,27,31,18,16,21],
[30,28,32,27,0,28,43,35,22,32,23,23,26],
[29,22,35,28,22,0,32,35,33,32,27,25,28],
[21,14,32,19,7,18,0,23,23,21,12,15,12],
[15,22,22,23,15,15,27,0,16,25,15,13,17],
[24,23,32,23,28,17,27,34,0,33,17,16,19],
[26,17,26,19,18,18,29,25,17,0,17,14,16],
[31,26,37,32,27,23,38,35,33,33,0,19,33],
[32,26,40,34,27,25,35,37,34,36,31,0,31],
[34,25,30,29,24,22,38,33,31,34,17,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 193, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,46,32,30,28,36,30,35,32,33,24,35],
[21,0,38,32,21,20,33,19,20,39,32,18,20],
[4,12,0,18,16,29,15,25,19,27,31,17,14],
[18,18,32,0,22,31,26,24,30,27,29,15,25],
[20,29,34,28,0,28,30,24,31,24,30,17,35],
[22,30,21,19,22,0,27,21,21,25,22,16,26],
[14,17,35,24,20,23,0,17,18,25,31,18,36],
[20,31,25,26,26,29,33,0,30,32,39,29,33],
[15,30,31,20,19,29,32,20,0,32,37,21,29],
[18,11,23,23,26,25,25,18,18,0,30,17,19],
[17,18,19,21,20,28,19,11,13,20,0,11,15],
[26,32,33,35,33,34,32,21,29,33,39,0,38],
[15,30,36,25,15,24,14,17,21,31,35,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 194, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,20,20,7,32,22,18,31,22,37,14,15],
[19,0,21,8,15,25,26,18,24,15,37,11,15],
[30,29,0,30,15,19,26,29,18,15,37,22,26],
[30,42,20,0,7,25,33,18,24,22,37,25,26],
[43,35,35,43,0,43,37,36,24,44,44,35,44],
[18,25,31,25,7,0,25,25,20,33,33,25,22],
[28,24,24,17,13,25,0,29,17,28,43,35,32],
[32,32,21,32,14,25,21,0,32,21,32,32,32],
[19,26,32,26,26,30,33,18,0,33,37,18,26],
[28,35,35,28,6,17,22,29,17,0,36,28,25],
[13,13,13,13,6,17,7,18,13,14,0,13,13],
[36,39,28,25,15,25,15,18,32,22,37,0,26],
[35,35,24,24,6,28,18,18,24,25,37,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 195, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,35,36,26,35,31,27,33,20,24,40,31],
[26,0,32,27,21,26,26,20,29,29,30,36,30],
[15,18,0,20,19,22,32,31,24,22,21,37,32],
[14,23,30,0,16,30,31,27,21,20,15,40,32],
[24,29,31,34,0,28,31,21,17,23,17,43,34],
[15,24,28,20,22,0,28,34,19,29,21,36,34],
[19,24,18,19,19,22,0,26,21,22,15,31,32],
[23,30,19,23,29,16,24,0,17,28,26,36,34],
[17,21,26,29,33,31,29,33,0,27,27,42,38],
[30,21,28,30,27,21,28,22,23,0,36,40,37],
[26,20,29,35,33,29,35,24,23,14,0,38,35],
[10,14,13,10,7,14,19,14,8,10,12,0,15],
[19,20,18,18,16,16,18,16,12,13,15,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 196, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,29,44,31,16,19,31,10,44,29,19,15],
[31,0,27,27,27,31,27,27,35,40,27,18,29],
[21,23,0,40,15,19,6,31,10,31,28,23,17],
[6,23,10,0,19,10,10,19,10,19,4,25,21],
[19,23,35,31,0,31,23,44,23,35,27,23,30],
[34,19,31,40,19,0,19,31,10,44,32,25,21],
[31,23,44,40,27,31,0,27,8,31,40,23,15],
[19,23,19,31,6,19,23,0,23,23,19,23,15],
[40,15,40,40,27,40,42,27,0,40,40,27,27],
[6,10,19,31,15,6,19,27,10,0,15,6,17],
[21,23,22,46,23,18,10,31,10,35,0,25,17],
[31,32,27,25,27,25,27,27,23,44,25,0,30],
[35,21,33,29,20,29,35,35,23,33,33,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 197, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,21,30,22,22,23,22,25,23,20,25,21],
[28,0,22,33,25,28,24,24,24,21,22,29,28],
[29,28,0,34,24,27,19,24,29,23,17,31,27],
[20,17,16,0,16,21,12,17,23,14,17,20,17],
[28,25,26,34,0,27,25,25,32,26,22,26,31],
[28,22,23,29,23,0,19,20,27,23,18,25,26],
[27,26,31,38,25,31,0,28,28,30,20,31,25],
[28,26,26,33,25,30,22,0,31,25,25,26,27],
[25,26,21,27,18,23,22,19,0,22,17,26,26],
[27,29,27,36,24,27,20,25,28,0,21,31,26],
[30,28,33,33,28,32,30,25,33,29,0,27,28],
[25,21,19,30,24,25,19,24,24,19,23,0,24],
[29,22,23,33,19,24,25,23,24,24,22,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 198, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,40,44,28,25,37,35,28,20,32,30,32],
[18,0,35,37,21,21,31,34,21,24,44,16,29],
[10,15,0,32,22,20,24,35,14,15,20,20,22],
[6,13,18,0,3,3,16,11,3,6,18,11,3],
[22,29,28,47,0,35,31,23,23,11,29,18,33],
[25,29,30,47,15,0,38,30,8,13,39,18,36],
[13,19,26,34,19,12,0,25,11,6,24,14,19],
[15,16,15,39,27,20,25,0,8,14,32,13,22],
[22,29,36,47,27,42,39,42,0,35,47,26,42],
[30,26,35,44,39,37,44,36,15,0,37,18,36],
[18,6,30,32,21,11,26,18,3,13,0,17,19],
[20,34,30,39,32,32,36,37,24,32,33,0,26],
[18,21,28,47,17,14,31,28,8,14,31,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 199, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,23,25,14,18,13,29,18,12,24,22,26],
[38,0,32,37,19,20,28,35,22,16,26,28,39],
[27,18,0,24,18,23,19,30,23,20,23,24,34],
[25,13,26,0,14,18,19,25,15,6,20,20,26],
[36,31,32,36,0,28,31,34,21,28,27,26,40],
[32,30,27,32,22,0,23,27,31,29,24,26,35],
[37,22,31,31,19,27,0,37,18,21,24,21,35],
[21,15,20,25,16,23,13,0,15,19,20,27,31],
[32,28,27,35,29,19,32,35,0,21,21,34,32],
[38,34,30,44,22,21,29,31,29,0,31,26,37],
[26,24,27,30,23,26,26,30,29,19,0,29,34],
[28,22,26,30,24,24,29,23,16,24,21,0,30],
[24,11,16,24,10,15,15,19,18,13,16,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 50, 200, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbd/mebbd_13_50.csv", index=False, header=False)