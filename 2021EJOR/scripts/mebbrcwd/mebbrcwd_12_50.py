
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg
from kemeny import sc

rep = 1
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,29,27,24,21,22,22,26,31,18,17,23],
[21,0,21,23,18,22,23,27,25,21,25,27],
[23,29,0,21,24,28,19,17,26,21,22,26],
[26,27,29,0,24,23,21,18,25,19,19,26],
[29,32,26,26,0,20,26,26,33,20,19,27],
[28,28,22,27,30,0,26,26,25,26,21,24],
[28,27,31,29,24,24,0,24,30,23,17,26],
[24,23,33,32,24,24,26,0,30,28,26,31],
[19,25,24,25,17,25,20,20,0,16,17,23],
[32,29,29,31,30,24,27,22,34,0,19,30],
[33,25,28,31,31,29,33,24,33,31,0,35],
[27,23,24,24,23,26,24,19,27,20,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 1, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,19,27,24,30,22,35,22,28,31,24],
[29,0,26,26,26,24,28,27,25,20,22,21],
[31,24,0,32,16,37,20,30,24,25,26,31],
[23,24,18,0,12,22,21,21,15,28,23,21],
[26,24,34,38,0,27,26,27,27,20,17,23],
[20,26,13,28,23,0,25,31,22,31,31,30],
[28,22,30,29,24,25,0,27,28,24,13,25],
[15,23,20,29,23,19,23,0,19,26,27,30],
[28,25,26,35,23,28,22,31,0,32,31,25],
[22,30,25,22,30,19,26,24,18,0,24,24],
[19,28,24,27,33,19,37,23,19,26,0,25],
[26,29,19,29,27,20,25,20,25,26,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 2, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,21,28,28,26,19,21,29,31,25,24],
[29,0,27,30,36,35,25,29,31,30,28,31],
[29,23,0,31,35,33,21,26,32,34,23,24],
[22,20,19,0,33,32,22,23,33,24,22,20],
[22,14,15,17,0,25,18,12,23,14,18,12],
[24,15,17,18,25,0,15,19,17,20,20,14],
[31,25,29,28,32,35,0,22,30,27,24,26],
[29,21,24,27,38,31,28,0,29,28,22,25],
[21,19,18,17,27,33,20,21,0,17,20,18],
[19,20,16,26,36,30,23,22,33,0,23,26],
[25,22,27,28,32,30,26,28,30,27,0,25],
[26,19,26,30,38,36,24,25,32,24,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 3, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,19,19,23,13,21,14,17,28,20,17],
[25,0,21,19,22,20,20,16,21,24,23,18],
[31,29,0,27,30,27,26,26,18,31,18,30],
[31,31,23,0,31,20,27,20,21,32,24,23],
[27,28,20,19,0,25,22,24,24,35,24,28],
[37,30,23,30,25,0,26,23,14,29,21,27],
[29,30,24,23,28,24,0,23,24,33,30,27],
[36,34,24,30,26,27,27,0,25,35,18,28],
[33,29,32,29,26,36,26,25,0,30,26,29],
[22,26,19,18,15,21,17,15,20,0,13,20],
[30,27,32,26,26,29,20,32,24,37,0,29],
[33,32,20,27,22,23,23,22,21,30,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 4, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,24,25,19,22,17,23,18,20,25,22],
[30,0,29,28,20,25,24,27,24,24,27,26],
[26,21,0,24,21,20,22,20,17,24,24,24],
[25,22,26,0,16,22,24,22,17,21,29,21],
[31,30,29,34,0,28,29,25,26,27,34,33],
[28,25,30,28,22,0,27,27,23,25,30,26],
[33,26,28,26,21,23,0,25,22,27,27,28],
[27,23,30,28,25,23,25,0,18,28,29,22],
[32,26,33,33,24,27,28,32,0,30,31,29],
[30,26,26,29,23,25,23,22,20,0,29,25],
[25,23,26,21,16,20,23,21,19,21,0,24],
[28,24,26,29,17,24,22,28,21,25,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 5, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,31,25,31,23,32,28,28,27,21,27],
[19,0,28,22,29,27,31,30,29,26,22,29],
[19,22,0,22,23,21,25,25,24,20,14,20],
[25,28,28,0,30,26,33,30,31,29,28,35],
[19,21,27,20,0,20,30,29,28,26,19,28],
[27,23,29,24,30,0,24,31,30,25,18,28],
[18,19,25,17,20,26,0,20,29,20,11,28],
[22,20,25,20,21,19,30,0,24,24,19,29],
[22,21,26,19,22,20,21,26,0,23,15,26],
[23,24,30,21,24,25,30,26,27,0,19,28],
[29,28,36,22,31,32,39,31,35,31,0,36],
[23,21,30,15,22,22,22,21,24,22,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 6, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,32,17,29,25,31,23,22,28,26,22],
[27,0,37,25,29,22,34,22,24,28,30,28],
[18,13,0,21,30,23,26,16,17,20,21,20],
[33,25,29,0,33,31,35,28,17,26,32,23],
[21,21,20,17,0,24,30,15,15,31,23,24],
[25,28,27,19,26,0,32,16,20,21,23,26],
[19,16,24,15,20,18,0,20,15,17,23,26],
[27,28,34,22,35,34,30,0,25,26,34,29],
[28,26,33,33,35,30,35,25,0,32,28,31],
[22,22,30,24,19,29,33,24,18,0,30,19],
[24,20,29,18,27,27,27,16,22,20,0,18],
[28,22,30,27,26,24,24,21,19,31,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 7, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,31,21,22,30,29,28,27,30,26,26],
[24,0,34,21,28,29,25,31,30,32,29,24],
[19,16,0,16,17,22,24,29,21,26,23,23],
[29,29,34,0,24,31,28,37,31,30,27,30],
[28,22,33,26,0,27,27,33,26,28,29,31],
[20,21,28,19,23,0,26,30,30,29,24,27],
[21,25,26,22,23,24,0,29,26,25,24,26],
[22,19,21,13,17,20,21,0,22,25,17,19],
[23,20,29,19,24,20,24,28,0,23,25,25],
[20,18,24,20,22,21,25,25,27,0,21,28],
[24,21,27,23,21,26,26,33,25,29,0,22],
[24,26,27,20,19,23,24,31,25,22,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 8, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,21,23,21,27,20,21,19,19,25,27],
[23,0,17,16,14,22,17,19,19,15,20,22],
[29,33,0,26,23,26,21,24,22,21,17,23],
[27,34,24,0,16,39,16,25,20,19,20,20],
[29,36,27,34,0,37,23,28,25,24,23,20],
[23,28,24,11,13,0,17,19,16,16,15,24],
[30,33,29,34,27,33,0,32,29,22,25,21],
[29,31,26,25,22,31,18,0,21,25,25,23],
[31,31,28,30,25,34,21,29,0,20,30,27],
[31,35,29,31,26,34,28,25,30,0,30,33],
[25,30,33,30,27,35,25,25,20,20,0,25],
[23,28,27,30,30,26,29,27,23,17,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 9, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,26,28,22,29,26,28,28,31,31,31],
[26,0,31,25,28,26,24,24,29,32,28,32],
[24,19,0,27,16,23,20,27,28,27,28,26],
[22,25,23,0,24,23,21,24,32,31,27,28],
[28,22,34,26,0,25,17,26,29,31,29,20],
[21,24,27,27,25,0,21,24,31,28,30,32],
[24,26,30,29,33,29,0,27,38,31,30,29],
[22,26,23,26,24,26,23,0,32,30,28,32],
[22,21,22,18,21,19,12,18,0,24,24,22],
[19,18,23,19,19,22,19,20,26,0,28,22],
[19,22,22,23,21,20,20,22,26,22,0,25],
[19,18,24,22,30,18,21,18,28,28,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 10, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,26,24,22,25,26,31,24,29,25,17],
[20,0,27,23,22,23,27,24,24,26,20,21],
[24,23,0,27,25,20,27,29,28,27,24,24],
[26,27,23,0,25,27,26,29,24,26,24,26],
[28,28,25,25,0,28,27,32,26,26,30,28],
[25,27,30,23,22,0,28,31,24,23,22,20],
[24,23,23,24,23,22,0,28,20,26,21,18],
[19,26,21,21,18,19,22,0,21,24,22,15],
[26,26,22,26,24,26,30,29,0,31,28,25],
[21,24,23,24,24,27,24,26,19,0,18,18],
[25,30,26,26,20,28,29,28,22,32,0,26],
[33,29,26,24,22,30,32,35,25,32,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 11, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,20,39,36,23,24,24,30,19,30,22],
[23,0,25,30,30,16,20,18,18,19,28,20],
[30,25,0,28,28,19,25,27,23,17,20,15],
[11,20,22,0,23,18,18,19,19,14,19,12],
[14,20,22,27,0,19,16,16,26,16,27,20],
[27,34,31,32,31,0,28,31,27,28,28,24],
[26,30,25,32,34,22,0,27,32,22,34,22],
[26,32,23,31,34,19,23,0,26,26,28,30],
[20,32,27,31,24,23,18,24,0,30,32,30],
[31,31,33,36,34,22,28,24,20,0,30,28],
[20,22,30,31,23,22,16,22,18,20,0,18],
[28,30,35,38,30,26,28,20,20,22,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 12, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,26,30,32,24,22,28,24,31,24,28],
[22,0,32,31,23,22,24,23,27,33,26,29],
[24,18,0,29,27,33,21,23,25,32,21,25],
[20,19,21,0,23,28,18,22,24,31,21,22],
[18,27,23,27,0,26,16,21,24,29,23,24],
[26,28,17,22,24,0,18,25,25,29,22,23],
[28,26,29,32,34,32,0,26,27,30,25,30],
[22,27,27,28,29,25,24,0,28,29,27,25],
[26,23,25,26,26,25,23,22,0,30,23,28],
[19,17,18,19,21,21,20,21,20,0,14,14],
[26,24,29,29,27,28,25,23,27,36,0,29],
[22,21,25,28,26,27,20,25,22,36,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 13, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,31,17,26,28,16,28,22,31,14,14],
[34,0,39,20,17,29,0,31,20,31,31,22],
[19,11,0,20,0,14,11,14,2,9,9,0],
[33,30,30,0,11,11,16,11,21,14,16,14],
[24,33,50,39,0,31,19,31,41,48,19,17],
[22,21,36,39,19,0,21,5,19,19,5,5],
[34,50,39,34,31,29,0,31,34,48,34,25],
[22,19,36,39,19,45,19,0,36,45,14,5],
[28,30,48,29,9,31,16,14,0,31,14,14],
[19,19,41,36,2,31,2,5,19,0,2,2],
[36,19,41,34,31,45,16,36,36,48,0,22],
[36,28,50,36,33,45,25,45,36,48,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 14, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,32,26,27,24,32,28,25,27,29,27],
[26,0,21,17,26,22,27,29,19,24,26,22],
[18,29,0,20,27,22,26,29,23,27,19,24],
[24,33,30,0,33,28,31,35,30,31,32,29],
[23,24,23,17,0,20,27,19,17,19,18,22],
[26,28,28,22,30,0,34,29,24,26,26,30],
[18,23,24,19,23,16,0,25,25,25,26,24],
[22,21,21,15,31,21,25,0,22,22,25,23],
[25,31,27,20,33,26,25,28,0,28,27,24],
[23,26,23,19,31,24,25,28,22,0,24,20],
[21,24,31,18,32,24,24,25,23,26,0,24],
[23,28,26,21,28,20,26,27,26,30,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 15, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,28,24,29,29,31,29,21,27,22,19],
[19,0,18,19,21,16,31,24,19,12,15,19],
[22,32,0,24,21,23,30,26,20,25,24,31],
[26,31,26,0,24,27,35,21,24,17,20,19],
[21,29,29,26,0,27,25,35,21,25,25,28],
[21,34,27,23,23,0,33,30,21,20,24,26],
[19,19,20,15,25,17,0,22,16,19,15,21],
[21,26,24,29,15,20,28,0,20,20,21,25],
[29,31,30,26,29,29,34,30,0,28,28,23],
[23,38,25,33,25,30,31,30,22,0,27,28],
[28,35,26,30,25,26,35,29,22,23,0,25],
[31,31,19,31,22,24,29,25,27,22,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 16, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,17,20,13,38,17,14,26,28,23,17],
[10,0,10,13,18,23,0,6,15,23,6,6],
[33,40,0,32,26,46,11,20,32,34,34,20],
[30,37,18,0,19,29,17,11,23,31,31,23],
[37,32,24,31,0,38,18,32,38,41,38,27],
[12,27,4,21,12,0,4,9,13,17,18,0],
[33,50,39,33,32,46,0,20,32,29,46,34],
[36,44,30,39,18,41,30,0,44,35,36,26],
[24,35,18,27,12,37,18,6,0,23,32,18],
[22,27,16,19,9,33,21,15,27,0,27,21],
[27,44,16,19,12,32,4,14,18,23,0,15],
[33,44,30,27,23,50,16,24,32,29,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 17, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,22,27,23,33,32,24,24,29,25,29],
[20,0,17,26,19,31,25,18,19,29,16,25],
[28,33,0,27,29,32,28,32,27,33,23,33],
[23,24,23,0,25,33,27,25,28,24,22,28],
[27,31,21,25,0,25,27,30,28,32,18,26],
[17,19,18,17,25,0,19,22,22,24,20,17],
[18,25,22,23,23,31,0,26,24,27,25,23],
[26,32,18,25,20,28,24,0,20,27,10,22],
[26,31,23,22,22,28,26,30,0,33,26,26],
[21,21,17,26,18,26,23,23,17,0,20,30],
[25,34,27,28,32,30,25,40,24,30,0,26],
[21,25,17,22,24,33,27,28,24,20,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 18, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,25,26,29,21,23,24,22,29,25,24],
[19,0,18,21,23,24,19,20,22,22,24,25],
[25,32,0,24,28,24,21,22,24,28,28,26],
[24,29,26,0,25,26,24,22,24,25,27,27],
[21,27,22,25,0,22,24,20,21,21,22,26],
[29,26,26,24,28,0,23,27,25,27,22,26],
[27,31,29,26,26,27,0,24,23,31,24,27],
[26,30,28,28,30,23,26,0,27,28,27,28],
[28,28,26,26,29,25,27,23,0,32,27,28],
[21,28,22,25,29,23,19,22,18,0,25,29],
[25,26,22,23,28,28,26,23,23,25,0,30],
[26,25,24,23,24,24,23,22,22,21,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 19, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,21,17,23,16,17,16,20,26,24,19],
[38,0,33,30,24,32,33,26,31,28,26,29],
[29,17,0,18,17,28,25,19,26,25,30,26],
[33,20,32,0,31,26,23,24,30,30,20,30],
[27,26,33,19,0,23,22,24,24,26,23,28],
[34,18,22,24,27,0,26,20,24,27,25,27],
[33,17,25,27,28,24,0,22,26,27,26,32],
[34,24,31,26,26,30,28,0,28,32,26,30],
[30,19,24,20,26,26,24,22,0,22,28,33],
[24,22,25,20,24,23,23,18,28,0,21,26],
[26,24,20,30,27,25,24,24,22,29,0,24],
[31,21,24,20,22,23,18,20,17,24,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 20, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,25,24,28,23,32,17,23,23,22,17],
[32,0,30,23,36,24,38,22,38,28,25,19],
[25,20,0,26,27,22,23,21,33,29,25,19],
[26,27,24,0,28,25,29,18,27,32,32,24],
[22,14,23,22,0,12,20,23,18,15,20,14],
[27,26,28,25,38,0,30,28,39,35,29,20],
[18,12,27,21,30,20,0,17,26,19,20,10],
[33,28,29,32,27,22,33,0,27,32,37,31],
[27,12,17,23,32,11,24,23,0,17,21,16],
[27,22,21,18,35,15,31,18,33,0,30,19],
[28,25,25,18,30,21,30,13,29,20,0,21],
[33,31,31,26,36,30,40,19,34,31,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 21, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,34,20,26,30,25,29,19,13,31,21],
[30,0,34,23,27,38,25,17,27,22,31,28],
[16,16,0,8,18,16,16,11,12,17,14,10],
[30,27,42,0,32,41,40,29,31,35,31,25],
[24,23,32,18,0,26,25,21,28,21,25,17],
[20,12,34,9,24,0,25,16,15,12,23,13],
[25,25,34,10,25,25,0,19,21,19,28,23],
[21,33,39,21,29,34,31,0,28,27,35,28],
[31,23,38,19,22,35,29,22,0,25,32,26],
[37,28,33,15,29,38,31,23,25,0,37,26],
[19,19,36,19,25,27,22,15,18,13,0,19],
[29,22,40,25,33,37,27,22,24,24,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 22, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,27,29,17,19,26,26,16,26,29,17],
[25,0,24,27,21,22,25,27,24,25,30,25],
[23,26,0,32,20,29,24,25,21,31,31,25],
[21,23,18,0,13,17,20,22,21,29,25,21],
[33,29,30,37,0,31,25,31,30,37,38,30],
[31,28,21,33,19,0,21,28,23,32,31,25],
[24,25,26,30,25,29,0,30,29,31,28,24],
[24,23,25,28,19,22,20,0,28,26,27,25],
[34,26,29,29,20,27,21,22,0,38,31,30],
[24,25,19,21,13,18,19,24,12,0,24,16],
[21,20,19,25,12,19,22,23,19,26,0,19],
[33,25,25,29,20,25,26,25,20,34,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 23, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,18,19,21,19,21,20,19,23,25,25],
[31,0,25,24,27,16,30,30,28,29,28,23],
[32,25,0,22,23,18,24,29,25,24,22,22],
[31,26,28,0,25,27,26,32,27,23,27,25],
[29,23,27,25,0,21,22,27,26,22,32,24],
[31,34,32,23,29,0,33,30,29,29,33,27],
[29,20,26,24,28,17,0,28,26,26,25,28],
[30,20,21,18,23,20,22,0,20,22,26,22],
[31,22,25,23,24,21,24,30,0,27,30,23],
[27,21,26,27,28,21,24,28,23,0,28,23],
[25,22,28,23,18,17,25,24,20,22,0,17],
[25,27,28,25,26,23,22,28,27,27,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 24, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,21,12,25,17,16,19,20,21,25,18],
[22,0,24,18,29,16,25,16,22,27,24,19],
[29,26,0,18,27,20,26,22,24,28,26,19],
[38,32,32,0,27,31,30,27,36,32,27,23],
[25,21,23,23,0,23,20,22,25,24,22,26],
[33,34,30,19,27,0,26,24,30,29,25,23],
[34,25,24,20,30,24,0,23,24,26,25,22],
[31,34,28,23,28,26,27,0,24,29,29,21],
[30,28,26,14,25,20,26,26,0,29,28,22],
[29,23,22,18,26,21,24,21,21,0,26,20],
[25,26,24,23,28,25,25,21,22,24,0,18],
[32,31,31,27,24,27,28,29,28,30,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 25, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,25,12,25,12,25,26,23,11,25,12],
[38,0,28,26,27,39,39,39,39,24,36,14],
[25,22,0,23,25,12,22,26,11,22,36,22],
[38,24,27,0,27,25,13,28,24,24,25,13],
[25,23,25,23,0,12,25,25,25,36,36,25],
[38,11,38,25,38,0,38,38,24,24,24,24],
[25,11,28,37,25,12,0,26,12,22,25,1],
[24,11,24,22,25,12,24,0,11,22,25,24],
[27,11,39,26,25,26,38,39,0,11,25,25],
[39,26,28,26,14,26,28,28,39,0,39,14],
[25,14,14,25,14,26,25,25,25,11,0,0],
[38,36,28,37,25,26,49,26,25,36,50,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 26, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,20,23,14,17,17,19,16,25,21,24],
[29,0,20,20,18,16,20,22,19,28,22,21],
[30,30,0,28,28,25,29,35,26,33,31,29],
[27,30,22,0,18,19,22,28,21,30,29,26],
[36,32,22,32,0,23,25,30,22,29,29,30],
[33,34,25,31,27,0,25,30,32,31,31,27],
[33,30,21,28,25,25,0,31,26,31,30,31],
[31,28,15,22,20,20,19,0,21,27,23,28],
[34,31,24,29,28,18,24,29,0,26,28,23],
[25,22,17,20,21,19,19,23,24,0,23,25],
[29,28,19,21,21,19,20,27,22,27,0,28],
[26,29,21,24,20,23,19,22,27,25,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 27, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,27,26,25,25,24,22,17,25,28,18],
[28,0,29,26,26,26,27,26,22,30,33,22],
[23,21,0,18,24,20,20,21,18,24,25,20],
[24,24,32,0,30,28,28,25,24,29,30,25],
[25,24,26,20,0,23,22,22,25,22,27,22],
[25,24,30,22,27,0,25,19,21,27,31,22],
[26,23,30,22,28,25,0,21,23,28,30,27],
[28,24,29,25,28,31,29,0,25,30,30,25],
[33,28,32,26,25,29,27,25,0,31,30,29],
[25,20,26,21,28,23,22,20,19,0,28,19],
[22,17,25,20,23,19,20,20,20,22,0,16],
[32,28,30,25,28,28,23,25,21,31,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 28, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,23,41,34,25,31,29,28,30,27,19],
[23,0,29,34,39,29,29,41,30,29,24,21],
[27,21,0,36,35,28,28,40,26,26,29,17],
[9,16,14,0,22,19,9,20,12,7,16,10],
[16,11,15,28,0,21,13,22,20,12,15,22],
[25,21,22,31,29,0,23,24,30,21,26,15],
[19,21,22,41,37,27,0,22,23,26,20,20],
[21,9,10,30,28,26,28,0,25,25,21,20],
[22,20,24,38,30,20,27,25,0,40,24,28],
[20,21,24,43,38,29,24,25,10,0,26,25],
[23,26,21,34,35,24,30,29,26,24,0,22],
[31,29,33,40,28,35,30,30,22,25,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 29, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,25,18,24,23,11,22,29,22,21,29],
[31,0,36,26,20,28,26,14,35,33,37,31],
[25,14,0,14,17,14,18,20,18,18,21,23],
[32,24,36,0,34,34,27,30,32,36,38,26],
[26,30,33,16,0,38,15,15,31,29,29,26],
[27,22,36,16,12,0,12,23,29,29,16,27],
[39,24,32,23,35,38,0,38,38,30,39,26],
[28,36,30,20,35,27,12,0,28,30,27,26],
[21,15,32,18,19,21,12,22,0,32,21,26],
[28,17,32,14,21,21,20,20,18,0,19,22],
[29,13,29,12,21,34,11,23,29,31,0,29],
[21,19,27,24,24,23,24,24,24,28,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 30, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,28,21,50,25,41,34,40,43,43,23],
[30,0,27,17,45,25,37,29,39,45,42,39],
[22,23,0,17,22,25,34,28,37,25,37,30],
[29,33,33,0,32,25,29,34,37,32,32,30],
[0,5,28,18,0,14,22,21,28,26,36,23],
[25,25,25,25,36,0,40,30,30,34,40,40],
[9,13,16,21,28,10,0,23,18,27,32,20],
[16,21,22,16,29,20,27,0,34,24,44,18],
[10,11,13,13,22,20,32,16,0,17,42,23],
[7,5,25,18,24,16,23,26,33,0,33,23],
[7,8,13,18,14,10,18,6,8,17,0,11],
[27,11,20,20,27,10,30,32,27,27,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 31, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,26,24,27,15,20,22,21,23,21,26],
[28,0,29,29,35,24,26,30,28,31,25,29],
[24,21,0,26,31,21,20,26,28,25,19,28],
[26,21,24,0,27,22,16,23,21,21,19,24],
[23,15,19,23,0,17,14,22,21,16,19,19],
[35,26,29,28,33,0,22,30,27,29,27,26],
[30,24,30,34,36,28,0,29,24,29,24,30],
[28,20,24,27,28,20,21,0,22,25,25,24],
[29,22,22,29,29,23,26,28,0,28,24,29],
[27,19,25,29,34,21,21,25,22,0,23,26],
[29,25,31,31,31,23,26,25,26,27,0,32],
[24,21,22,26,31,24,20,26,21,24,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 32, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,22,25,22,23,24,20,26,25,24,20],
[31,0,27,28,27,30,27,23,32,32,32,26],
[28,23,0,31,31,26,24,24,25,32,30,29],
[25,22,19,0,22,18,21,22,22,28,26,23],
[28,23,19,28,0,25,23,25,27,27,27,27],
[27,20,24,32,25,0,23,21,22,27,30,27],
[26,23,26,29,27,27,0,23,28,30,32,27],
[30,27,26,28,25,29,27,0,23,29,29,24],
[24,18,25,28,23,28,22,27,0,24,29,26],
[25,18,18,22,23,23,20,21,26,0,26,20],
[26,18,20,24,23,20,18,21,21,24,0,20],
[30,24,21,27,23,23,23,26,24,30,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 33, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,20,25,30,26,28,26,25,29,18,28],
[19,0,18,16,22,16,19,21,20,22,13,17],
[30,32,0,26,31,29,31,23,25,28,24,24],
[25,34,24,0,34,31,32,21,29,28,20,30],
[20,28,19,16,0,19,22,19,23,26,13,15],
[24,34,21,19,31,0,25,18,22,31,20,29],
[22,31,19,18,28,25,0,16,19,24,17,15],
[24,29,27,29,31,32,34,0,29,29,28,24],
[25,30,25,21,27,28,31,21,0,26,24,25],
[21,28,22,22,24,19,26,21,24,0,17,26],
[32,37,26,30,37,30,33,22,26,33,0,28],
[22,33,26,20,35,21,35,26,25,24,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 34, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,30,31,27,24,26,21,32,25,26,30],
[24,0,25,22,25,25,25,21,20,25,24,23],
[20,25,0,23,24,22,25,18,29,23,26,25],
[19,28,27,0,31,27,24,23,31,24,30,23],
[23,25,26,19,0,28,28,23,23,28,24,19],
[26,25,28,23,22,0,26,19,28,28,22,27],
[24,25,25,26,22,24,0,17,30,28,29,23],
[29,29,32,27,27,31,33,0,30,29,21,24],
[18,30,21,19,27,22,20,20,0,26,24,19],
[25,25,27,26,22,22,22,21,24,0,27,23],
[24,26,24,20,26,28,21,29,26,23,0,21],
[20,27,25,27,31,23,27,26,31,27,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 35, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,30,27,21,26,28,25,27,25,27,28],
[21,0,26,24,17,28,20,19,20,30,26,23],
[20,24,0,28,20,21,21,26,21,26,28,28],
[23,26,22,0,20,28,21,30,24,25,26,32],
[29,33,30,30,0,33,27,35,24,33,32,33],
[24,22,29,22,17,0,19,25,24,23,28,27],
[22,30,29,29,23,31,0,25,21,31,25,31],
[25,31,24,20,15,25,25,0,22,27,22,29],
[23,30,29,26,26,26,29,28,0,31,30,30],
[25,20,24,25,17,27,19,23,19,0,22,28],
[23,24,22,24,18,22,25,28,20,28,0,30],
[22,27,22,18,17,23,19,21,20,22,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 36, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,22,31,27,23,42,29,30,19,42,30],
[34,0,20,30,22,21,35,30,23,26,43,33],
[28,30,0,23,36,36,40,31,22,37,48,37],
[19,20,27,0,27,33,36,26,28,29,42,33],
[23,28,14,23,0,36,40,21,23,32,43,33],
[27,29,14,17,14,0,21,21,20,22,30,14],
[8,15,10,14,10,29,0,17,7,18,23,27],
[21,20,19,24,29,29,33,0,27,24,35,30],
[20,27,28,22,27,30,43,23,0,31,43,34],
[31,24,13,21,18,28,32,26,19,0,39,31],
[8,7,2,8,7,20,27,15,7,11,0,12],
[20,17,13,17,17,36,23,20,16,19,38,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 37, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,39,27,28,38,28,39,24,39,39,27,9],
[11,0,9,25,6,15,21,24,12,45,9,15],
[23,41,0,41,26,41,36,32,21,36,24,26],
[22,25,9,0,17,15,20,24,20,36,18,26],
[12,44,24,33,0,33,35,24,30,50,28,21],
[22,35,9,35,17,0,26,35,20,45,18,26],
[11,29,14,30,15,24,0,15,21,36,18,15],
[26,26,18,26,26,15,35,0,15,35,15,35],
[11,38,29,30,20,30,29,35,0,39,38,20],
[11,5,14,14,0,5,14,15,11,0,0,9],
[23,41,26,32,22,32,32,35,12,50,0,32],
[41,35,24,24,29,24,35,15,30,41,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 38, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,30,21,17,26,38,23,27,25,25,26],
[32,0,32,28,28,29,46,25,23,34,31,33],
[20,18,0,13,13,19,30,14,16,19,19,24],
[29,22,37,0,22,30,40,28,26,17,40,37],
[33,22,37,28,0,32,33,31,30,35,30,32],
[24,21,31,20,18,0,35,33,25,28,25,30],
[12,4,20,10,17,15,0,14,12,23,19,19],
[27,25,36,22,19,17,36,0,20,20,23,33],
[23,27,34,24,20,25,38,30,0,32,30,29],
[25,16,31,33,15,22,27,30,18,0,32,29],
[25,19,31,10,20,25,31,27,20,18,0,26],
[24,17,26,13,18,20,31,17,21,21,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 39, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,26,27,26,28,26,15,26,25,24,22],
[25,0,31,22,28,28,25,20,29,25,21,22],
[24,19,0,27,21,26,25,18,27,25,20,19],
[23,28,23,0,22,29,23,20,21,24,27,20],
[24,22,29,28,0,28,24,24,30,27,19,21],
[22,22,24,21,22,0,20,19,28,17,25,19],
[24,25,25,27,26,30,0,24,27,25,25,23],
[35,30,32,30,26,31,26,0,31,28,25,24],
[24,21,23,29,20,22,23,19,0,20,22,18],
[25,25,25,26,23,33,25,22,30,0,25,30],
[26,29,30,23,31,25,25,25,28,25,0,25],
[28,28,31,30,29,31,27,26,32,20,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 40, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,40,28,28,28,17,19,15,35,30,31],
[31,0,37,26,39,39,26,24,34,30,34,37],
[10,13,0,11,19,12,10,10,17,17,18,30],
[22,24,39,0,30,30,17,17,14,17,25,30],
[22,11,31,20,0,22,19,17,2,28,28,30],
[22,11,38,20,28,0,17,19,23,35,34,39],
[33,24,40,33,31,33,0,11,28,35,30,31],
[31,26,40,33,33,31,39,0,17,37,28,44],
[35,16,33,36,48,27,22,33,0,28,38,41],
[15,20,33,33,22,15,15,13,22,0,10,39],
[20,16,32,25,22,16,20,22,12,40,0,31],
[19,13,20,20,20,11,19,6,9,11,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 41, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,19,26,24,27,27,26,28,25,21,32],
[24,0,19,22,20,29,27,21,28,23,22,29],
[31,31,0,28,27,34,30,29,29,24,23,36],
[24,28,22,0,26,33,29,30,28,27,25,28],
[26,30,23,24,0,32,34,26,27,24,26,37],
[23,21,16,17,18,0,24,22,18,22,19,23],
[23,23,20,21,16,26,0,23,23,20,22,31],
[24,29,21,20,24,28,27,0,25,18,17,29],
[22,22,21,22,23,32,27,25,0,25,21,31],
[25,27,26,23,26,28,30,32,25,0,22,28],
[29,28,27,25,24,31,28,33,29,28,0,35],
[18,21,14,22,13,27,19,21,19,22,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 42, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,28,28,29,28,29,28,25,22,30,30],
[23,0,25,33,27,26,30,25,27,25,31,30],
[22,25,0,29,27,24,27,25,26,18,28,26],
[22,17,21,0,20,23,20,24,17,20,24,23],
[21,23,23,30,0,22,28,29,25,28,29,27],
[22,24,26,27,28,0,27,24,23,22,30,28],
[21,20,23,30,22,23,0,27,27,20,30,24],
[22,25,25,26,21,26,23,0,24,20,29,26],
[25,23,24,33,25,27,23,26,0,18,29,30],
[28,25,32,30,22,28,30,30,32,0,31,30],
[20,19,22,26,21,20,20,21,21,19,0,19],
[20,20,24,27,23,22,26,24,20,20,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 43, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,33,21,32,36,37,32,36,39,39,32],
[14,0,36,26,44,32,33,34,32,30,36,24],
[17,14,0,16,21,25,24,19,20,28,18,20],
[29,24,34,0,27,27,27,25,31,30,31,23],
[18,6,29,23,0,25,18,23,22,30,16,14],
[14,18,25,23,25,0,17,16,24,28,27,24],
[13,17,26,23,32,33,0,30,31,29,31,24],
[18,16,31,25,27,34,20,0,29,34,20,11],
[14,18,30,19,28,26,19,21,0,31,18,9],
[11,20,22,20,20,22,21,16,19,0,17,10],
[11,14,32,19,34,23,19,30,32,33,0,19],
[18,26,30,27,36,26,26,39,41,40,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 44, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,26,17,29,29,15,17,17,17,14,17],
[33,0,14,14,12,17,12,14,14,12,9,9],
[24,36,0,33,36,36,22,25,5,36,33,22],
[33,36,17,0,45,45,31,22,14,36,30,19],
[21,38,14,5,0,8,8,8,5,22,19,8],
[21,33,14,5,42,0,28,22,14,30,30,16],
[35,38,28,19,42,22,0,22,19,22,35,38],
[33,36,25,28,42,28,28,0,30,42,39,28],
[33,36,45,36,45,36,31,20,0,36,33,36],
[33,38,14,14,28,20,28,8,14,0,44,30],
[36,41,17,20,31,20,15,11,17,6,0,20],
[33,41,28,31,42,34,12,22,14,20,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 45, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,23,25,25,30,30,23,21,20,23,28],
[27,0,25,24,28,33,22,29,29,20,33,26],
[27,25,0,26,24,28,29,18,27,24,24,29],
[25,26,24,0,26,28,30,23,28,23,28,27],
[25,22,26,24,0,27,24,21,21,19,23,27],
[20,17,22,22,23,0,28,21,19,19,27,21],
[20,28,21,20,26,22,0,18,23,24,22,24],
[27,21,32,27,29,29,32,0,28,27,28,31],
[29,21,23,22,29,31,27,22,0,26,20,22],
[30,30,26,27,31,31,26,23,24,0,26,29],
[27,17,26,22,27,23,28,22,30,24,0,25],
[22,24,21,23,23,29,26,19,28,21,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 46, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,26,15,24,30,20,26,24,25,30,13],
[35,0,22,24,23,26,33,32,34,27,32,22],
[24,28,0,25,26,19,24,21,27,24,26,22],
[35,26,25,0,32,32,27,25,21,23,24,24],
[26,27,24,18,0,22,16,30,18,23,20,18],
[20,24,31,18,28,0,15,27,24,10,26,17],
[30,17,26,23,34,35,0,23,30,31,31,21],
[24,18,29,25,20,23,27,0,21,20,20,19],
[26,16,23,29,32,26,20,29,0,20,30,20],
[25,23,26,27,27,40,19,30,30,0,29,16],
[20,18,24,26,30,24,19,30,20,21,0,25],
[37,28,28,26,32,33,29,31,30,34,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 47, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,28,22,28,25,24,23,26,19,25,30],
[29,0,29,23,30,29,29,26,27,29,26,29],
[22,21,0,21,27,23,26,25,22,23,20,29],
[28,27,29,0,27,24,29,27,23,29,30,31],
[22,20,23,23,0,23,27,19,21,23,26,28],
[25,21,27,26,27,0,27,25,22,27,24,29],
[26,21,24,21,23,23,0,21,20,23,25,28],
[27,24,25,23,31,25,29,0,24,22,27,29],
[24,23,28,27,29,28,30,26,0,21,26,22],
[31,21,27,21,27,23,27,28,29,0,26,27],
[25,24,30,20,24,26,25,23,24,24,0,31],
[20,21,21,19,22,21,22,21,28,23,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 48, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,27,24,22,27,23,22,32,25,21,28],
[25,0,26,21,16,26,22,20,27,24,19,23],
[23,24,0,19,21,24,26,21,25,27,21,27],
[26,29,31,0,23,29,30,25,32,28,18,30],
[28,34,29,27,0,32,29,30,28,29,25,27],
[23,24,26,21,18,0,30,17,30,27,21,27],
[27,28,24,20,21,20,0,22,28,29,19,28],
[28,30,29,25,20,33,28,0,29,24,25,27],
[18,23,25,18,22,20,22,21,0,21,19,23],
[25,26,23,22,21,23,21,26,29,0,25,26],
[29,31,29,32,25,29,31,25,31,25,0,30],
[22,27,23,20,23,23,22,23,27,24,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 49, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,28,31,26,27,33,32,36,31,29,25],
[23,0,22,28,22,27,28,28,28,26,24,26],
[22,28,0,24,22,29,28,30,32,31,20,12],
[19,22,26,0,22,25,21,24,25,31,23,16],
[24,28,28,28,0,32,33,37,35,32,28,22],
[23,23,21,25,18,0,27,27,21,22,23,19],
[17,22,22,29,17,23,0,24,30,25,20,17],
[18,22,20,26,13,23,26,0,23,16,16,13],
[14,22,18,25,15,29,20,27,0,18,17,15],
[19,24,19,19,18,28,25,34,32,0,24,17],
[21,26,30,27,22,27,30,34,33,26,0,16],
[25,24,38,34,28,31,33,37,35,33,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 50, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,26,22,20,22,33,18,22,28,22,26],
[29,0,23,32,23,24,29,21,27,31,18,29],
[24,27,0,33,31,17,29,21,19,27,16,32],
[28,18,17,0,23,13,19,20,14,36,18,17],
[30,27,19,27,0,22,29,19,21,32,25,28],
[28,26,33,37,28,0,24,18,30,33,12,24],
[17,21,21,31,21,26,0,24,30,27,16,28],
[32,29,29,30,31,32,26,0,27,33,20,21],
[28,23,31,36,29,20,20,23,0,32,13,20],
[22,19,23,14,18,17,23,17,18,0,18,24],
[28,32,34,32,25,38,34,30,37,32,0,23],
[24,21,18,33,22,26,22,29,30,26,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 51, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,32,31,23,20,19,26,30,24,19,34],
[29,0,32,35,31,27,27,29,31,30,24,37],
[18,18,0,33,20,19,21,25,22,25,25,30],
[19,15,17,0,17,13,20,19,20,19,17,23],
[27,19,30,33,0,19,24,21,24,22,25,32],
[30,23,31,37,31,0,23,29,35,29,25,35],
[31,23,29,30,26,27,0,24,26,28,31,27],
[24,21,25,31,29,21,26,0,28,31,23,23],
[20,19,28,30,26,15,24,22,0,23,24,27],
[26,20,25,31,28,21,22,19,27,0,24,26],
[31,26,25,33,25,25,19,27,26,26,0,24],
[16,13,20,27,18,15,23,27,23,24,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 52, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,26,29,26,32,24,25,25,24,27,25],
[26,0,25,27,31,33,25,34,35,24,23,30],
[24,25,0,25,24,29,27,26,30,25,25,34],
[21,23,25,0,19,30,19,25,26,16,19,20],
[24,19,26,31,0,26,20,27,26,22,24,22],
[18,17,21,20,24,0,24,24,24,18,21,25],
[26,25,23,31,30,26,0,32,27,20,23,33],
[25,16,24,25,23,26,18,0,30,17,24,26],
[25,15,20,24,24,26,23,20,0,17,18,25],
[26,26,25,34,28,32,30,33,33,0,27,32],
[23,27,25,31,26,29,27,26,32,23,0,32],
[25,20,16,30,28,25,17,24,25,18,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 53, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,23,26,23,26,20,19,26,21,24,24],
[23,0,26,30,25,26,21,23,24,21,23,23],
[27,24,0,28,29,26,26,30,30,21,29,28],
[24,20,22,0,25,27,18,22,28,21,25,25],
[27,25,21,25,0,30,23,28,36,22,28,21],
[24,24,24,23,20,0,18,20,19,18,23,26],
[30,29,24,32,27,32,0,23,28,24,27,27],
[31,27,20,28,22,30,27,0,28,22,34,26],
[24,26,20,22,14,31,22,22,0,25,26,17],
[29,29,29,29,28,32,26,28,25,0,32,23],
[26,27,21,25,22,27,23,16,24,18,0,20],
[26,27,22,25,29,24,23,24,33,27,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 54, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,25,20,29,16,20,24,26,19,28,22],
[32,0,27,16,33,29,28,26,30,23,27,22],
[25,23,0,21,26,27,30,22,23,25,31,16],
[30,34,29,0,28,30,30,22,29,22,22,23],
[21,17,24,22,0,21,24,25,19,18,24,19],
[34,21,23,20,29,0,22,25,22,17,24,19],
[30,22,20,20,26,28,0,20,23,23,23,21],
[26,24,28,28,25,25,30,0,18,17,25,17],
[24,20,27,21,31,28,27,32,0,27,31,28],
[31,27,25,28,32,33,27,33,23,0,35,20],
[22,23,19,28,26,26,27,25,19,15,0,17],
[28,28,34,27,31,31,29,33,22,30,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 55, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,24,28,35,22,21,24,19,22,20,11],
[32,0,27,26,27,28,25,29,25,22,28,17],
[26,23,0,27,30,34,24,24,26,31,28,16],
[22,24,23,0,18,15,19,20,20,20,19,18],
[15,23,20,32,0,24,21,22,17,20,20,16],
[28,22,16,35,26,0,20,27,21,36,21,15],
[29,25,26,31,29,30,0,30,24,32,23,26],
[26,21,26,30,28,23,20,0,27,27,19,23],
[31,25,24,30,33,29,26,23,0,30,25,17],
[28,28,19,30,30,14,18,23,20,0,19,15],
[30,22,22,31,30,29,27,31,25,31,0,21],
[39,33,34,32,34,35,24,27,33,35,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 56, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,33,28,33,28,29,33,26,36,27,41],
[28,0,28,22,28,26,25,24,21,29,25,27],
[17,22,0,28,20,25,23,23,22,28,18,25],
[22,28,22,0,23,22,24,22,19,28,23,24],
[17,22,30,27,0,34,28,21,28,26,29,26],
[22,24,25,28,16,0,30,17,16,25,19,23],
[21,25,27,26,22,20,0,21,25,20,22,26],
[17,26,27,28,29,33,29,0,27,30,21,29],
[24,29,28,31,22,34,25,23,0,26,27,20],
[14,21,22,22,24,25,30,20,24,0,19,21],
[23,25,32,27,21,31,28,29,23,31,0,31],
[9,23,25,26,24,27,24,21,30,29,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 57, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,20,29,34,26,32,27,24,25,32,27],
[22,0,18,22,20,22,25,22,25,25,26,19],
[30,32,0,32,30,22,33,33,26,29,31,26],
[21,28,18,0,24,24,32,25,18,16,24,18],
[16,30,20,26,0,26,30,24,17,25,25,20],
[24,28,28,26,24,0,32,30,18,23,23,18],
[18,25,17,18,20,18,0,23,12,16,21,14],
[23,28,17,25,26,20,27,0,20,21,25,24],
[26,25,24,32,33,32,38,30,0,23,30,28],
[25,25,21,34,25,27,34,29,27,0,33,22],
[18,24,19,26,25,27,29,25,20,17,0,22],
[23,31,24,32,30,32,36,26,22,28,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 58, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,44,31,29,26,32,22,27,31,20,28,29],
[6,0,19,19,18,22,9,15,26,11,14,21],
[19,31,0,23,18,27,19,22,22,20,23,17],
[21,31,27,0,20,19,27,23,26,24,16,29],
[24,32,32,30,0,26,16,26,33,16,30,23],
[18,28,23,31,24,0,24,20,19,20,12,26],
[28,41,31,23,34,26,0,25,26,26,23,29],
[23,35,28,27,24,30,25,0,26,20,25,30],
[19,24,28,24,17,31,24,24,0,19,13,28],
[30,39,30,26,34,30,24,30,31,0,30,29],
[22,36,27,34,20,38,27,25,37,20,0,28],
[21,29,33,21,27,24,21,20,22,21,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 59, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,27,37,27,27,27,26,29,13,21,29],
[18,0,8,26,32,27,27,26,24,13,21,29],
[23,42,0,31,50,32,24,44,42,31,18,42],
[13,24,19,0,32,32,19,21,29,13,26,24],
[23,18,0,18,0,19,0,13,23,0,13,10],
[23,23,18,18,31,0,23,26,23,13,13,23],
[23,23,26,31,50,27,0,39,23,13,34,29],
[24,24,6,29,37,24,11,0,29,19,19,29],
[21,26,8,21,27,27,27,21,0,21,21,24],
[37,37,19,37,50,37,37,31,29,0,26,16],
[29,29,32,24,37,37,16,31,29,24,0,29],
[21,21,8,26,40,27,21,21,26,34,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 60, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,26,32,32,31,31,27,28,36,25,26],
[23,0,27,24,32,27,26,31,27,28,29,29],
[24,23,0,27,32,35,33,23,24,34,25,26],
[18,26,23,0,29,27,25,25,27,27,24,25],
[18,18,18,21,0,21,23,22,21,19,21,16],
[19,23,15,23,29,0,24,25,19,24,20,21],
[19,24,17,25,27,26,0,26,26,29,27,24],
[23,19,27,25,28,25,24,0,24,21,26,25],
[22,23,26,23,29,31,24,26,0,25,23,20],
[14,22,16,23,31,26,21,29,25,0,26,21],
[25,21,25,26,29,30,23,24,27,24,0,28],
[24,21,24,25,34,29,26,25,30,29,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 61, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,40,34,25,34,38,30,31,25,33,36,35],
[10,0,19,16,14,21,17,23,13,19,29,15],
[16,31,0,18,27,34,21,24,20,27,28,29],
[25,34,32,0,30,35,23,26,21,27,31,26],
[16,36,23,20,0,23,19,25,21,23,34,19],
[12,29,16,15,27,0,16,20,17,23,29,19],
[20,33,29,27,31,34,0,28,22,28,37,27],
[19,27,26,24,25,30,22,0,23,24,26,30],
[25,37,30,29,29,33,28,27,0,30,41,34],
[17,31,23,23,27,27,22,26,20,0,34,22],
[14,21,22,19,16,21,13,24,9,16,0,14],
[15,35,21,24,31,31,23,20,16,28,36,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 62, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,19,28,27,33,26,17,31,21,20,19],
[21,0,19,28,27,21,31,29,25,23,17,19],
[31,31,0,32,25,32,27,30,28,26,24,28],
[22,22,18,0,23,24,23,21,18,21,20,20],
[23,23,25,27,0,23,26,24,30,28,28,22],
[17,29,18,26,27,0,26,18,25,18,19,22],
[24,19,23,27,24,24,0,17,24,19,19,21],
[33,21,20,29,26,32,33,0,32,30,28,27],
[19,25,22,32,20,25,26,18,0,22,17,17],
[29,27,24,29,22,32,31,20,28,0,20,20],
[30,33,26,30,22,31,31,22,33,30,0,29],
[31,31,22,30,28,28,29,23,33,30,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 63, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,22,21,18,11,14,32,27,16,21,23],
[30,0,27,27,28,26,33,22,24,22,25,26],
[28,23,0,28,31,15,28,34,26,27,27,30],
[29,23,22,0,29,19,26,32,25,26,34,29],
[32,22,19,21,0,22,32,28,28,32,32,27],
[39,24,35,31,28,0,37,32,35,28,31,34],
[36,17,22,24,18,13,0,28,31,27,21,23],
[18,28,16,18,22,18,22,0,27,24,24,26],
[23,26,24,25,22,15,19,23,0,17,25,24],
[34,28,23,24,18,22,23,26,33,0,24,20],
[29,25,23,16,18,19,29,26,25,26,0,18],
[27,24,20,21,23,16,27,24,26,30,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 64, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,25,24,20,19,21,22,23,23,21,22],
[27,0,26,24,22,24,22,22,28,25,22,25],
[25,24,0,24,22,21,24,22,29,24,24,21],
[26,26,26,0,23,23,26,23,26,28,22,30],
[30,28,28,27,0,24,29,27,26,28,26,29],
[31,26,29,27,26,0,26,27,30,28,22,29],
[29,28,26,24,21,24,0,25,32,27,21,26],
[28,28,28,27,23,23,25,0,28,29,25,26],
[27,22,21,24,24,20,18,22,0,23,19,23],
[27,25,26,22,22,22,23,21,27,0,22,24],
[29,28,26,28,24,28,29,25,31,28,0,31],
[28,25,29,20,21,21,24,24,27,26,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 65, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,32,26,33,24,22,32,23,23,33,28],
[27,0,31,27,31,21,20,34,26,30,33,31],
[18,19,0,22,28,24,20,22,23,17,25,24],
[24,23,28,0,24,27,26,24,22,25,25,31],
[17,19,22,26,0,15,9,20,16,17,28,22],
[26,29,26,23,35,0,26,35,25,23,32,31],
[28,30,30,24,41,24,0,35,26,29,30,34],
[18,16,28,26,30,15,15,0,15,21,31,20],
[27,24,27,28,34,25,24,35,0,28,32,28],
[27,20,33,25,33,27,21,29,22,0,26,31],
[17,17,25,25,22,18,20,19,18,24,0,22],
[22,19,26,19,28,19,16,30,22,19,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 66, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,22,26,33,26,21,22,31,27,38,27],
[28,0,28,38,29,30,28,26,33,28,33,25],
[28,22,0,30,26,28,17,22,31,27,35,24],
[24,12,20,0,25,28,22,24,28,30,37,23],
[17,21,24,25,0,20,21,24,21,29,29,24],
[24,20,22,22,30,0,27,25,29,30,34,25],
[29,22,33,28,29,23,0,35,20,27,34,29],
[28,24,28,26,26,25,15,0,28,26,33,22],
[19,17,19,22,29,21,30,22,0,26,34,27],
[23,22,23,20,21,20,23,24,24,0,29,29],
[12,17,15,13,21,16,16,17,16,21,0,20],
[23,25,26,27,26,25,21,28,23,21,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 67, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,17,24,36,30,28,19,18,21,21,24],
[20,0,22,27,32,32,25,22,14,23,20,23],
[33,28,0,28,38,37,28,20,19,25,29,28],
[26,23,22,0,35,37,33,26,15,23,23,26],
[14,18,12,15,0,28,22,13,12,11,11,23],
[20,18,13,13,22,0,24,9,14,14,13,15],
[22,25,22,17,28,26,0,17,15,20,14,19],
[31,28,30,24,37,41,33,0,22,27,21,27],
[32,36,31,35,38,36,35,28,0,32,23,32],
[29,27,25,27,39,36,30,23,18,0,12,25],
[29,30,21,27,39,37,36,29,27,38,0,33],
[26,27,22,24,27,35,31,23,18,25,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 68, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,19,22,21,18,19,31,22,23,27,23],
[29,0,25,27,23,26,24,31,28,26,29,21],
[31,25,0,22,27,25,27,31,24,23,25,21],
[28,23,28,0,25,26,29,31,29,27,29,22],
[29,27,23,25,0,30,27,31,29,27,29,26],
[32,24,25,24,20,0,24,30,29,25,27,23],
[31,26,23,21,23,26,0,28,24,28,29,23],
[19,19,19,19,19,20,22,0,23,25,28,27],
[28,22,26,21,21,21,26,27,0,23,25,25],
[27,24,27,23,23,25,22,25,27,0,30,24],
[23,21,25,21,21,23,21,22,25,20,0,20],
[27,29,29,28,24,27,27,23,25,26,30,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 69, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,26,24,21,19,26,26,28,24,25,23],
[28,0,24,29,23,20,26,31,27,25,25,26],
[24,26,0,31,25,22,28,28,31,22,22,29],
[26,21,19,0,20,18,21,26,21,27,23,27],
[29,27,25,30,0,25,28,31,24,23,26,28],
[31,30,28,32,25,0,34,32,32,29,26,31],
[24,24,22,29,22,16,0,25,26,30,23,24],
[24,19,22,24,19,18,25,0,25,25,20,19],
[22,23,19,29,26,18,24,25,0,22,21,21],
[26,25,28,23,27,21,20,25,28,0,22,29],
[25,25,28,27,24,24,27,30,29,28,0,27],
[27,24,21,23,22,19,26,31,29,21,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 70, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,22,24,19,27,22,24,19,22,29,22],
[20,0,24,24,27,24,22,22,24,20,32,24],
[28,26,0,25,24,21,23,22,19,20,30,25],
[26,26,25,0,33,21,24,21,19,29,27,26],
[31,23,26,17,0,27,23,23,17,23,32,23],
[23,26,29,29,23,0,24,27,21,26,33,32],
[28,28,27,26,27,26,0,26,27,23,30,27],
[26,28,28,29,27,23,24,0,20,25,28,26],
[31,26,31,31,33,29,23,30,0,29,35,29],
[28,30,30,21,27,24,27,25,21,0,27,31],
[21,18,20,23,18,17,20,22,15,23,0,18],
[28,26,25,24,27,18,23,24,21,19,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 71, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,25,23,26,17,24,29,28,25,27,19],
[26,0,26,30,30,22,31,29,30,29,31,30],
[25,24,0,28,34,26,26,30,31,32,30,29],
[27,20,22,0,29,19,24,25,22,26,25,22],
[24,20,16,21,0,15,26,22,27,27,26,22],
[33,28,24,31,35,0,30,29,32,31,32,27],
[26,19,24,26,24,20,0,29,24,27,25,23],
[21,21,20,25,28,21,21,0,26,23,24,23],
[22,20,19,28,23,18,26,24,0,30,21,23],
[25,21,18,24,23,19,23,27,20,0,21,22],
[23,19,20,25,24,18,25,26,29,29,0,25],
[31,20,21,28,28,23,27,27,27,28,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 72, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,30,30,33,29,26,17,35,21,12,21],
[29,0,23,19,22,26,34,25,41,38,34,26],
[20,27,0,17,12,8,28,16,32,36,24,17],
[20,31,33,0,29,17,28,16,36,41,29,29],
[17,28,38,21,0,38,34,8,42,33,21,38],
[21,24,42,33,12,0,29,17,33,33,21,26],
[24,16,22,22,16,21,0,12,37,37,16,18],
[33,25,34,34,42,33,38,0,37,25,19,30],
[15,9,18,14,8,17,13,13,0,30,12,18],
[29,12,14,9,17,17,13,25,20,0,12,12],
[38,16,26,21,29,29,34,31,38,38,0,21],
[29,24,33,21,12,24,32,20,32,38,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 73, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,17,23,22,29,39,31,20,13,34,27],
[26,0,22,11,21,25,27,31,36,19,28,21],
[33,28,0,18,16,33,40,39,32,13,29,34],
[27,39,32,0,27,27,44,32,33,20,38,22],
[28,29,34,23,0,29,34,29,31,26,29,33],
[21,25,17,23,21,0,27,30,26,14,29,27],
[11,23,10,6,16,23,0,19,22,9,21,23],
[19,19,11,18,21,20,31,0,16,15,19,22],
[30,14,18,17,19,24,28,34,0,19,29,23],
[37,31,37,30,24,36,41,35,31,0,30,31],
[16,22,21,12,21,21,29,31,21,20,0,22],
[23,29,16,28,17,23,27,28,27,19,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 74, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,27,23,21,23,23,32,18,23,28,30],
[20,0,23,18,18,27,20,26,21,21,27,26],
[23,27,0,24,20,21,28,26,22,20,23,25],
[27,32,26,0,25,29,23,33,26,26,28,30],
[29,32,30,25,0,28,23,32,25,28,32,30],
[27,23,29,21,22,0,26,27,27,21,29,24],
[27,30,22,27,27,24,0,34,23,28,28,25],
[18,24,24,17,18,23,16,0,15,19,20,19],
[32,29,28,24,25,23,27,35,0,27,29,27],
[27,29,30,24,22,29,22,31,23,0,27,28],
[22,23,27,22,18,21,22,30,21,23,0,24],
[20,24,25,20,20,26,25,31,23,22,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 75, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,21,24,35,22,31,29,22,20,30,26],
[26,0,26,37,36,26,31,34,22,30,34,30],
[29,24,0,31,38,38,31,32,26,29,28,34],
[26,13,19,0,33,28,19,25,25,21,25,25],
[15,14,12,17,0,16,13,24,19,11,19,17],
[28,24,12,22,34,0,28,27,19,24,25,26],
[19,19,19,31,37,22,0,38,24,30,33,32],
[21,16,18,25,26,23,12,0,23,21,16,25],
[28,28,24,25,31,31,26,27,0,24,28,34],
[30,20,21,29,39,26,20,29,26,0,28,31],
[20,16,22,25,31,25,17,34,22,22,0,21],
[24,20,16,25,33,24,18,25,16,19,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 76, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,19,19,21,23,24,25,28,21,26,26],
[27,0,27,25,27,28,23,34,29,26,28,25],
[31,23,0,18,25,29,26,30,30,29,30,33],
[31,25,32,0,23,31,26,34,26,35,31,31],
[29,23,25,27,0,33,24,30,24,27,32,29],
[27,22,21,19,17,0,24,32,23,28,28,29],
[26,27,24,24,26,26,0,28,25,28,30,30],
[25,16,20,16,20,18,22,0,21,21,25,21],
[22,21,20,24,26,27,25,29,0,25,33,29],
[29,24,21,15,23,22,22,29,25,0,27,29],
[24,22,20,19,18,22,20,25,17,23,0,27],
[24,25,17,19,21,21,20,29,21,21,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 77, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,33,29,31,31,27,25,20,28,32,22],
[28,0,30,27,36,31,35,26,27,24,33,33],
[17,20,0,24,20,22,23,14,25,15,21,17],
[21,23,26,0,26,29,14,20,21,26,28,20],
[19,14,30,24,0,26,22,18,23,26,25,29],
[19,19,28,21,24,0,22,19,25,21,24,16],
[23,15,27,36,28,28,0,27,21,26,22,23],
[25,24,36,30,32,31,23,0,33,32,28,33],
[30,23,25,29,27,25,29,17,0,22,27,25],
[22,26,35,24,24,29,24,18,28,0,25,22],
[18,17,29,22,25,26,28,22,23,25,0,27],
[28,17,33,30,21,34,27,17,25,28,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 78, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,22,26,24,24,22,26,25,22,25,19],
[25,0,26,26,24,28,21,26,28,22,24,21],
[28,24,0,31,24,27,22,29,24,22,24,21],
[24,24,19,0,22,23,20,26,26,22,20,19],
[26,26,26,28,0,25,21,29,24,24,20,27],
[26,22,23,27,25,0,25,28,29,22,25,24],
[28,29,28,30,29,25,0,27,36,28,23,28],
[24,24,21,24,21,22,23,0,28,25,25,25],
[25,22,26,24,26,21,14,22,0,16,19,19],
[28,28,28,28,26,28,22,25,34,0,23,25],
[25,26,26,30,30,25,27,25,31,27,0,24],
[31,29,29,31,23,26,22,25,31,25,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 79, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,30,28,36,31,29,33,30,22,30,29],
[22,0,30,20,26,32,27,27,24,17,24,26],
[20,20,0,21,28,28,26,25,19,19,22,19],
[22,30,29,0,34,35,30,31,21,28,27,24],
[14,24,22,16,0,25,27,22,19,16,19,18],
[19,18,22,15,25,0,26,20,18,18,22,19],
[21,23,24,20,23,24,0,21,19,18,22,23],
[17,23,25,19,28,30,29,0,24,23,22,26],
[20,26,31,29,31,32,31,26,0,27,25,22],
[28,33,31,22,34,32,32,27,23,0,23,31],
[20,26,28,23,31,28,28,28,25,27,0,26],
[21,24,31,26,32,31,27,24,28,19,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 80, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,26,24,30,35,30,27,27,25,31,29],
[24,0,23,26,22,26,21,25,23,27,25,28],
[24,27,0,28,28,29,29,23,28,29,26,27],
[26,24,22,0,27,30,19,28,23,25,28,27],
[20,28,22,23,0,30,26,26,26,28,22,27],
[15,24,21,20,20,0,19,13,18,27,17,23],
[20,29,21,31,24,31,0,23,25,29,21,27],
[23,25,27,22,24,37,27,0,23,26,25,25],
[23,27,22,27,24,32,25,27,0,26,26,29],
[25,23,21,25,22,23,21,24,24,0,25,20],
[19,25,24,22,28,33,29,25,24,25,0,24],
[21,22,23,23,23,27,23,25,21,30,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 81, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,25,30,27,30,34,32,29,32,30,26],
[18,0,26,30,22,24,24,20,20,27,24,24],
[25,24,0,31,25,29,29,20,25,26,26,24],
[20,20,19,0,25,22,30,21,21,19,28,21],
[23,28,25,25,0,33,24,29,26,27,28,24],
[20,26,21,28,17,0,28,29,26,20,27,22],
[16,26,21,20,26,22,0,22,22,20,27,20],
[18,30,30,29,21,21,28,0,24,20,25,21],
[21,30,25,29,24,24,28,26,0,26,25,24],
[18,23,24,31,23,30,30,30,24,0,29,30],
[20,26,24,22,22,23,23,25,25,21,0,18],
[24,26,26,29,26,28,30,29,26,20,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 82, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,30,8,32,22,11,3,11,22,16,15],
[33,0,13,5,15,18,20,5,13,5,13,20],
[20,37,0,12,21,32,15,7,0,42,20,12],
[42,45,38,0,29,35,32,29,22,50,34,34],
[18,35,29,21,0,21,16,8,8,21,29,28],
[28,32,18,15,29,0,18,18,11,29,23,23],
[39,30,35,18,34,32,0,27,13,35,32,39],
[47,45,43,21,42,32,23,0,29,35,47,50],
[39,37,50,28,42,39,37,21,0,42,47,39],
[28,45,8,0,29,21,15,15,8,0,20,15],
[34,37,30,16,21,27,18,3,3,30,0,23],
[35,30,38,16,22,27,11,0,11,35,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 83, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,26,22,25,22,27,23,25,24,31,23],
[21,0,24,20,19,23,27,21,20,20,24,27],
[24,26,0,22,21,22,19,25,27,22,31,20],
[28,30,28,0,28,27,30,30,26,23,34,26],
[25,31,29,22,0,29,28,24,28,26,33,29],
[28,27,28,23,21,0,28,28,27,23,32,25],
[23,23,31,20,22,22,0,25,24,19,30,21],
[27,29,25,20,26,22,25,0,29,23,33,26],
[25,30,23,24,22,23,26,21,0,25,25,23],
[26,30,28,27,24,27,31,27,25,0,28,32],
[19,26,19,16,17,18,20,17,25,22,0,21],
[27,23,30,24,21,25,29,24,27,18,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 84, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,34,28,15,30,27,21,23,19,30,28],
[30,0,28,29,18,18,22,17,21,18,26,24],
[16,22,0,28,19,17,19,17,23,20,24,28],
[22,21,22,0,12,17,26,11,15,17,18,24],
[35,32,31,38,0,29,34,24,27,33,34,42],
[20,32,33,33,21,0,31,29,23,25,26,40],
[23,28,31,24,16,19,0,14,38,27,23,32],
[29,33,33,39,26,21,36,0,34,31,29,34],
[27,29,27,35,23,27,12,16,0,35,23,35],
[31,32,30,33,17,25,23,19,15,0,35,29],
[20,24,26,32,16,24,27,21,27,15,0,26],
[22,26,22,26,8,10,18,16,15,21,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 85, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,28,30,25,26,28,24,27,27,23,26],
[24,0,28,27,30,25,27,24,24,22,23,24],
[22,22,0,25,26,21,23,22,25,23,19,29],
[20,23,25,0,27,24,24,21,26,25,18,30],
[25,20,24,23,0,21,24,21,19,25,24,23],
[24,25,29,26,29,0,22,24,27,28,25,28],
[22,23,27,26,26,28,0,25,20,26,25,25],
[26,26,28,29,29,26,25,0,28,27,24,26],
[23,26,25,24,31,23,30,22,0,27,23,30],
[23,28,27,25,25,22,24,23,23,0,22,27],
[27,27,31,32,26,25,25,26,27,28,0,29],
[24,26,21,20,27,22,25,24,20,23,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 86, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,30,28,32,26,25,25,25,27,25,29],
[21,0,24,22,24,21,23,20,27,20,16,25],
[20,26,0,24,27,23,24,23,22,19,27,25],
[22,28,26,0,35,27,29,23,21,25,24,27],
[18,26,23,15,0,25,22,20,20,18,23,22],
[24,29,27,23,25,0,27,28,25,16,25,28],
[25,27,26,21,28,23,0,22,22,19,24,21],
[25,30,27,27,30,22,28,0,26,24,28,26],
[25,23,28,29,30,25,28,24,0,24,29,26],
[23,30,31,25,32,34,31,26,26,0,31,28],
[25,34,23,26,27,25,26,22,21,19,0,27],
[21,25,25,23,28,22,29,24,24,22,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 87, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,20,25,23,23,24,26,30,24,25,21],
[23,0,27,28,28,25,27,32,30,31,30,31],
[30,23,0,24,24,29,30,29,30,21,30,24],
[25,22,26,0,23,25,25,24,28,23,27,24],
[27,22,26,27,0,27,29,24,29,21,30,31],
[27,25,21,25,23,0,31,25,29,29,30,27],
[26,23,20,25,21,19,0,23,22,20,29,22],
[24,18,21,26,26,25,27,0,29,23,27,26],
[20,20,20,22,21,21,28,21,0,25,29,23],
[26,19,29,27,29,21,30,27,25,0,33,29],
[25,20,20,23,20,20,21,23,21,17,0,21],
[29,19,26,26,19,23,28,24,27,21,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 88, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,31,37,31,28,32,35,21,30,30,27],
[19,0,23,21,28,26,30,23,23,30,23,21],
[19,27,0,26,31,24,24,28,22,30,23,20],
[13,29,24,0,28,21,28,29,19,30,25,27],
[19,22,19,22,0,28,22,23,17,25,22,16],
[22,24,26,29,22,0,32,26,24,26,26,29],
[18,20,26,22,28,18,0,19,22,28,22,22],
[15,27,22,21,27,24,31,0,18,33,19,18],
[29,27,28,31,33,26,28,32,0,28,24,27],
[20,20,20,20,25,24,22,17,22,0,28,21],
[20,27,27,25,28,24,28,31,26,22,0,29],
[23,29,30,23,34,21,28,32,23,29,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 89, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,24,32,28,22,19,21,24,23,24,24],
[35,0,25,26,27,23,26,30,27,29,24,29],
[26,25,0,30,24,24,26,26,29,21,28,25],
[18,24,20,0,27,21,26,26,25,25,31,35],
[22,23,26,23,0,22,32,29,26,33,29,31],
[28,27,26,29,28,0,24,27,26,27,24,33],
[31,24,24,24,18,26,0,29,26,23,21,34],
[29,20,24,24,21,23,21,0,23,22,22,26],
[26,23,21,25,24,24,24,27,0,19,25,35],
[27,21,29,25,17,23,27,28,31,0,26,27],
[26,26,22,19,21,26,29,28,25,24,0,27],
[26,21,25,15,19,17,16,24,15,23,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 90, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,20,35,27,31,21,25,28,23,22,28],
[28,0,26,30,28,37,25,23,30,26,30,28],
[30,24,0,31,29,29,31,29,24,39,31,34],
[15,20,19,0,20,24,15,19,15,22,23,23],
[23,22,21,30,0,28,21,22,20,29,27,29],
[19,13,21,26,22,0,20,23,18,29,19,24],
[29,25,19,35,29,30,0,26,34,29,34,26],
[25,27,21,31,28,27,24,0,28,31,28,20],
[22,20,26,35,30,32,16,22,0,30,32,29],
[27,24,11,28,21,21,21,19,20,0,24,27],
[28,20,19,27,23,31,16,22,18,26,0,26],
[22,22,16,27,21,26,24,30,21,23,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 91, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,34,28,28,26,29,34,25,21,21,21],
[27,0,30,28,18,24,15,28,18,18,22,22],
[16,20,0,16,9,20,12,20,20,13,17,16],
[22,22,34,0,24,18,12,26,17,21,15,14],
[22,32,41,26,0,27,18,28,29,18,25,26],
[24,26,30,32,23,0,21,33,19,20,29,23],
[21,35,38,38,32,29,0,29,28,25,34,27],
[16,22,30,24,22,17,21,0,21,13,19,22],
[25,32,30,33,21,31,22,29,0,22,29,20],
[29,32,37,29,32,30,25,37,28,0,22,26],
[29,28,33,35,25,21,16,31,21,28,0,25],
[29,28,34,36,24,27,23,28,30,24,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 92, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,21,14,23,19,19,22,18,16,17,28],
[26,0,17,19,22,22,20,21,21,16,15,28],
[29,33,0,23,32,27,23,23,27,19,23,29],
[36,31,27,0,31,31,28,33,28,27,24,34],
[27,28,18,19,0,20,22,25,25,18,13,26],
[31,28,23,19,30,0,24,24,19,23,18,31],
[31,30,27,22,28,26,0,24,22,23,23,29],
[28,29,27,17,25,26,26,0,25,21,19,32],
[32,29,23,22,25,31,28,25,0,24,20,33],
[34,34,31,23,32,27,27,29,26,0,26,33],
[33,35,27,26,37,32,27,31,30,24,0,36],
[22,22,21,16,24,19,21,18,17,17,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 93, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,23,26,20,24,27,20,25,29,27,32],
[30,0,18,27,21,28,24,23,23,27,26,26],
[27,32,0,26,27,29,30,22,28,34,26,34],
[24,23,24,0,22,22,25,19,22,27,22,24],
[30,29,23,28,0,28,23,16,21,31,25,28],
[26,22,21,28,22,0,28,21,22,27,23,24],
[23,26,20,25,27,22,0,23,20,33,22,27],
[30,27,28,31,34,29,27,0,24,35,23,27],
[25,27,22,28,29,28,30,26,0,28,28,27],
[21,23,16,23,19,23,17,15,22,0,18,16],
[23,24,24,28,25,27,28,27,22,32,0,25],
[18,24,16,26,22,26,23,23,23,34,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 94, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,42,9,26,9,9,9,18,24,24,27],
[41,0,50,33,50,18,18,18,26,41,33,42],
[8,0,0,0,26,0,9,9,26,17,0,27],
[41,17,50,0,35,17,18,18,26,41,24,42],
[24,0,24,15,0,0,9,9,9,24,24,42],
[41,32,50,33,50,0,27,27,35,50,24,42],
[41,32,41,32,41,23,0,32,32,23,32,41],
[41,32,41,32,41,23,18,0,26,32,24,33],
[32,24,24,24,41,15,18,24,0,32,24,33],
[26,9,33,9,26,0,27,18,18,0,9,27],
[26,17,50,26,26,26,18,26,26,41,0,35],
[23,8,23,8,8,8,9,17,17,23,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 95, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,22,20,22,26,29,30,27,26,27,24],
[25,0,27,24,23,25,23,17,26,24,17,18],
[28,23,0,22,27,23,23,26,24,25,27,20],
[30,26,28,0,19,28,20,22,29,21,22,22],
[28,27,23,31,0,25,26,23,28,23,25,21],
[24,25,27,22,25,0,25,23,25,23,24,21],
[21,27,27,30,24,25,0,21,25,25,22,23],
[20,33,24,28,27,27,29,0,29,31,32,26],
[23,24,26,21,22,25,25,21,0,26,25,20],
[24,26,25,29,27,27,25,19,24,0,20,23],
[23,33,23,28,25,26,28,18,25,30,0,23],
[26,32,30,28,29,29,27,24,30,27,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 96, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,16,24,23,17,18,26,15,27,20,23],
[28,0,25,25,25,25,23,31,30,33,26,33],
[34,25,0,31,26,28,28,36,25,33,37,29],
[26,25,19,0,24,23,28,28,14,23,31,25],
[27,25,24,26,0,18,23,25,18,27,32,21],
[33,25,22,27,32,0,27,27,21,32,24,25],
[32,27,22,22,27,23,0,26,20,27,25,23],
[24,19,14,22,25,23,24,0,11,24,26,24],
[35,20,25,36,32,29,30,39,0,34,32,33],
[23,17,17,27,23,18,23,26,16,0,22,23],
[30,24,13,19,18,26,25,24,18,28,0,24],
[27,17,21,25,29,25,27,26,17,27,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 97, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,37,29,25,26,31,32,30,34,29,30],
[19,0,30,30,23,27,25,31,28,28,23,28],
[13,20,0,24,16,24,22,31,29,21,20,25],
[21,20,26,0,23,19,26,36,21,26,21,22],
[25,27,34,27,0,28,27,30,31,27,29,29],
[24,23,26,31,22,0,23,33,28,21,23,22],
[19,25,28,24,23,27,0,29,24,26,28,28],
[18,19,19,14,20,17,21,0,20,18,21,21],
[20,22,21,29,19,22,26,30,0,25,20,26],
[16,22,29,24,23,29,24,32,25,0,19,27],
[21,27,30,29,21,27,22,29,30,31,0,26],
[20,22,25,28,21,28,22,29,24,23,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 98, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,22,29,23,23,22,23,28,18,19,23],
[22,0,21,24,23,24,25,17,27,26,25,20],
[28,29,0,31,28,31,20,27,25,29,24,28],
[21,26,19,0,23,20,22,19,26,22,17,20],
[27,27,22,27,0,28,26,24,25,19,24,26],
[27,26,19,30,22,0,24,17,24,22,21,20],
[28,25,30,28,24,26,0,25,24,27,26,27],
[27,33,23,31,26,33,25,0,32,34,21,30],
[22,23,25,24,25,26,26,18,0,24,21,26],
[32,24,21,28,31,28,23,16,26,0,22,21],
[31,25,26,33,26,29,24,29,29,28,0,26],
[27,30,22,30,24,30,23,20,24,29,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 99, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,23,26,27,28,24,25,24,25,27,23],
[28,0,29,24,27,25,27,27,24,31,28,30],
[27,21,0,20,29,25,21,27,26,28,27,25],
[24,26,30,0,28,27,27,24,23,28,30,26],
[23,23,21,22,0,25,23,25,24,27,24,24],
[22,25,25,23,25,0,24,28,23,29,30,28],
[26,23,29,23,27,26,0,27,26,32,27,25],
[25,23,23,26,25,22,23,0,18,24,22,21],
[26,26,24,27,26,27,24,32,0,28,28,29],
[25,19,22,22,23,21,18,26,22,0,23,22],
[23,22,23,20,26,20,23,28,22,27,0,23],
[27,20,25,24,26,22,25,29,21,28,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 100, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,26,38,36,29,22,31,29,29,29,14],
[15,0,17,39,39,26,22,28,18,18,26,10],
[24,33,0,44,42,31,26,32,17,29,26,25],
[12,11,6,0,26,14,14,19,11,17,11,8],
[14,11,8,24,0,28,11,20,11,19,10,3],
[21,24,19,36,22,0,23,24,18,20,13,16],
[28,28,24,36,39,27,0,28,29,31,22,28],
[19,22,18,31,30,26,22,0,17,19,25,14],
[21,32,33,39,39,32,21,33,0,31,23,21],
[21,32,21,33,31,30,19,31,19,0,19,23],
[21,24,24,39,40,37,28,25,27,31,0,13],
[36,40,25,42,47,34,22,36,29,27,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 101, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,17,23,22,25,19,32,21,31,21,22],
[25,0,27,28,26,26,21,28,31,32,27,30],
[33,23,0,28,26,29,26,33,26,33,29,22],
[27,22,22,0,25,26,27,30,22,24,24,24],
[28,24,24,25,0,26,20,33,26,32,36,24],
[25,24,21,24,24,0,18,27,27,24,20,22],
[31,29,24,23,30,32,0,31,26,33,29,30],
[18,22,17,20,17,23,19,0,26,23,24,20],
[29,19,24,28,24,23,24,24,0,27,31,26],
[19,18,17,26,18,26,17,27,23,0,25,19],
[29,23,21,26,14,30,21,26,19,25,0,23],
[28,20,28,26,26,28,20,30,24,31,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 102, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,32,29,34,32,36,31,26,31,24,27],
[29,0,28,26,31,30,35,29,25,29,23,26],
[18,22,0,21,22,23,22,20,16,22,14,18],
[21,24,29,0,26,27,32,25,19,25,21,22],
[16,19,28,24,0,27,32,28,21,26,20,19],
[18,20,27,23,23,0,27,22,19,26,18,17],
[14,15,28,18,18,23,0,24,14,19,18,14],
[19,21,30,25,22,28,26,0,20,29,22,18],
[24,25,34,31,29,31,36,30,0,32,28,30],
[19,21,28,25,24,24,31,21,18,0,20,21],
[26,27,36,29,30,32,32,28,22,30,0,23],
[23,24,32,28,31,33,36,32,20,29,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 103, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,33,30,24,30,26,33,22,28,33,28],
[27,0,30,33,25,18,24,29,25,23,30,23],
[17,20,0,31,18,15,22,25,17,18,22,19],
[20,17,19,0,10,19,16,19,16,18,27,17],
[26,25,32,40,0,25,23,29,22,23,33,25],
[20,32,35,31,25,0,22,29,24,23,33,22],
[24,26,28,34,27,28,0,31,19,21,30,19],
[17,21,25,31,21,21,19,0,21,28,28,24],
[28,25,33,34,28,26,31,29,0,27,30,28],
[22,27,32,32,27,27,29,22,23,0,37,25],
[17,20,28,23,17,17,20,22,20,13,0,23],
[22,27,31,33,25,28,31,26,22,25,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 104, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,28,31,29,30,28,28,24,30,30,30],
[24,0,24,26,24,24,28,27,26,31,28,30],
[22,26,0,27,25,31,29,24,24,27,28,30],
[19,24,23,0,28,28,32,26,30,27,29,28],
[21,26,25,22,0,27,24,26,23,32,25,30],
[20,26,19,22,23,0,25,24,25,25,26,25],
[22,22,21,18,26,25,0,28,23,27,29,31],
[22,23,26,24,24,26,22,0,24,28,24,24],
[26,24,26,20,27,25,27,26,0,28,24,34],
[20,19,23,23,18,25,23,22,22,0,24,26],
[20,22,22,21,25,24,21,26,26,26,0,23],
[20,20,20,22,20,25,19,26,16,24,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 105, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,27,33,31,27,22,20,26,26,24,29],
[26,0,25,25,31,28,27,29,27,23,27,28],
[23,25,0,26,29,27,18,23,25,17,23,23],
[17,25,24,0,23,22,27,20,23,25,25,25],
[19,19,21,27,0,23,15,20,22,19,23,21],
[23,22,23,28,27,0,20,22,24,22,23,29],
[28,23,32,23,35,30,0,26,27,29,30,23],
[30,21,27,30,30,28,24,0,27,20,28,20],
[24,23,25,27,28,26,23,23,0,23,30,26],
[24,27,33,25,31,28,21,30,27,0,32,24],
[26,23,27,25,27,27,20,22,20,18,0,22],
[21,22,27,25,29,21,27,30,24,26,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 106, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,25,40,37,30,29,23,23,37,25,31],
[29,0,26,33,27,33,32,17,21,30,27,22],
[25,24,0,28,25,28,21,25,19,36,29,19],
[10,17,22,0,15,19,13,11,17,31,18,16],
[13,23,25,35,0,28,23,28,19,37,24,30],
[20,17,22,31,22,0,22,15,18,24,22,25],
[21,18,29,37,27,28,0,26,15,36,33,34],
[27,33,25,39,22,35,24,0,27,39,34,33],
[27,29,31,33,31,32,35,23,0,36,33,34],
[13,20,14,19,13,26,14,11,14,0,13,17],
[25,23,21,32,26,28,17,16,17,37,0,23],
[19,28,31,34,20,25,16,17,16,33,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 107, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,36,22,16,19,26,32,21,37,34,25,15],
[14,0,16,22,17,14,28,20,25,27,10,17],
[28,34,0,26,14,30,32,27,34,33,18,24],
[34,28,24,0,26,28,31,30,34,38,28,32],
[31,33,36,24,0,34,35,33,34,32,19,32],
[24,36,20,22,16,0,33,19,35,29,16,17],
[18,22,18,19,15,17,0,16,29,18,13,10],
[29,30,23,20,17,31,34,0,38,31,17,12],
[13,25,16,16,16,15,21,12,0,30,14,10],
[16,23,17,12,18,21,32,19,20,0,9,16],
[25,40,32,22,31,34,37,33,36,41,0,29],
[35,33,26,18,18,33,40,38,40,34,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 108, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,20,16,16,16,16,0,36,16,14,16],
[50,0,34,50,50,30,30,50,50,50,14,16],
[30,16,0,16,16,16,16,30,16,16,14,16],
[34,0,34,0,0,0,0,14,20,0,14,16],
[34,0,34,50,0,14,0,34,34,34,14,16],
[34,20,34,50,36,0,16,34,20,50,14,36],
[34,20,34,50,50,34,0,34,34,50,34,36],
[50,0,20,36,16,16,16,0,36,16,14,16],
[14,0,34,30,16,30,16,14,0,30,14,16],
[34,0,34,50,16,0,0,34,20,0,14,16],
[36,36,36,36,36,36,16,36,36,36,0,36],
[34,34,34,34,34,14,14,34,34,34,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 109, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,19,34,22,34,31,21,30,29,19,18],
[28,0,26,40,27,36,37,24,35,28,27,20],
[31,24,0,31,27,35,33,28,30,27,28,21],
[16,10,19,0,16,24,31,17,24,6,14,13],
[28,23,23,34,0,38,38,33,34,25,21,26],
[16,14,15,26,12,0,29,28,28,14,13,17],
[19,13,17,19,12,21,0,11,28,15,7,18],
[29,26,22,33,17,22,39,0,33,27,27,25],
[20,15,20,26,16,22,22,17,0,16,18,25],
[21,22,23,44,25,36,35,23,34,0,20,16],
[31,23,22,36,29,37,43,23,32,30,0,28],
[32,30,29,37,24,33,32,25,25,34,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 110, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,13,30,21,34,11,35,31,38,33,15],
[16,0,27,18,30,29,18,21,16,39,36,22],
[37,23,0,34,28,33,27,31,30,41,35,28],
[20,32,16,0,29,28,11,31,27,34,32,15],
[29,20,22,21,0,30,14,25,23,40,36,25],
[16,21,17,22,20,0,14,22,24,35,32,18],
[39,32,23,39,36,36,0,40,26,38,33,30],
[15,29,19,19,25,28,10,0,17,34,32,19],
[19,34,20,23,27,26,24,33,0,35,33,28],
[12,11,9,16,10,15,12,16,15,0,27,20],
[17,14,15,18,14,18,17,18,17,23,0,25],
[35,28,22,35,25,32,20,31,22,30,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 111, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,31,25,20,22,23,23,24,25,30,26],
[29,0,31,25,26,29,30,33,21,28,25,30],
[19,19,0,24,24,17,26,22,17,24,22,21],
[25,25,26,0,26,24,19,23,21,17,30,24],
[30,24,26,24,0,32,25,25,23,21,33,26],
[28,21,33,26,18,0,24,31,27,22,28,20],
[27,20,24,31,25,26,0,23,24,19,31,24],
[27,17,28,27,25,19,27,0,18,18,27,17],
[26,29,33,29,27,23,26,32,0,27,31,32],
[25,22,26,33,29,28,31,32,23,0,36,26],
[20,25,28,20,17,22,19,23,19,14,0,22],
[24,20,29,26,24,30,26,33,18,24,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 112, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,31,30,21,25,29,32,20,27,27,23],
[21,0,31,32,25,18,28,30,21,28,25,28],
[19,19,0,24,25,16,20,22,18,20,19,25],
[20,18,26,0,27,21,25,21,16,22,21,20],
[29,25,25,23,0,18,28,25,19,23,23,29],
[25,32,34,29,32,0,28,30,25,30,28,27],
[21,22,30,25,22,22,0,28,18,23,27,24],
[18,20,28,29,25,20,22,0,18,23,20,27],
[30,29,32,34,31,25,32,32,0,30,31,35],
[23,22,30,28,27,20,27,27,20,0,25,26],
[23,25,31,29,27,22,23,30,19,25,0,25],
[27,22,25,30,21,23,26,23,15,24,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 113, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,46,32,39,28,28,21,39,28,30,30],
[29,0,37,31,26,15,29,32,30,25,34,27],
[4,13,0,2,27,17,20,16,23,25,25,9],
[18,19,48,0,37,26,34,32,39,25,28,41],
[11,24,23,13,0,12,22,27,16,20,34,13],
[22,35,33,24,38,0,33,35,27,33,40,24],
[22,21,30,16,28,17,0,23,30,30,12,12],
[29,18,34,18,23,15,27,0,30,25,12,27],
[11,20,27,11,34,23,20,20,0,25,20,9],
[22,25,25,25,30,17,20,25,25,0,25,27],
[20,16,25,22,16,10,38,38,30,25,0,18],
[20,23,41,9,37,26,38,23,41,23,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 114, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,30,24,31,31,33,31,31,28,26,30],
[25,0,31,26,34,31,36,27,27,28,29,24],
[20,19,0,27,32,25,27,22,23,24,29,25],
[26,24,23,0,28,29,25,25,27,22,26,26],
[19,16,18,22,0,20,24,20,24,16,25,19],
[19,19,25,21,30,0,26,22,29,17,27,22],
[17,14,23,25,26,24,0,23,21,25,24,19],
[19,23,28,25,30,28,27,0,29,22,28,23],
[19,23,27,23,26,21,29,21,0,24,28,23],
[22,22,26,28,34,33,25,28,26,0,29,26],
[24,21,21,24,25,23,26,22,22,21,0,18],
[20,26,25,24,31,28,31,27,27,24,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 115, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,24,25,27,13,18,21,23,23,21,24],
[19,0,22,26,26,19,23,26,24,24,27,24],
[26,28,0,29,31,24,25,27,27,25,26,28],
[25,24,21,0,27,24,23,23,23,25,23,22],
[23,24,19,23,0,18,21,20,17,23,25,22],
[37,31,26,26,32,0,30,26,25,27,28,31],
[32,27,25,27,29,20,0,22,27,24,28,30],
[29,24,23,27,30,24,28,0,24,27,29,24],
[27,26,23,27,33,25,23,26,0,25,28,26],
[27,26,25,25,27,23,26,23,25,0,28,27],
[29,23,24,27,25,22,22,21,22,22,0,22],
[26,26,22,28,28,19,20,26,24,23,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 116, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,27,26,27,31,33,27,26,19,24,22],
[19,0,29,23,28,25,28,15,24,19,21,18],
[23,21,0,18,24,23,22,22,30,20,23,17],
[24,27,32,0,28,22,27,32,25,26,23,24],
[23,22,26,22,0,27,21,23,23,26,23,19],
[19,25,27,28,23,0,26,22,21,19,18,17],
[17,22,28,23,29,24,0,21,26,23,23,17],
[23,35,28,18,27,28,29,0,28,19,25,23],
[24,26,20,25,27,29,24,22,0,18,25,15],
[31,31,30,24,24,31,27,31,32,0,24,23],
[26,29,27,27,27,32,27,25,25,26,0,26],
[28,32,33,26,31,33,33,27,35,27,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 117, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,26,29,23,26,25,28,29,20,29,24],
[20,0,24,26,23,20,25,29,26,21,30,25],
[24,26,0,23,25,19,23,27,24,22,25,27],
[21,24,27,0,25,27,28,30,27,22,22,23],
[27,27,25,25,0,27,21,29,27,26,27,24],
[24,30,31,23,23,0,24,28,23,22,27,24],
[25,25,27,22,29,26,0,28,26,22,31,28],
[22,21,23,20,21,22,22,0,22,23,17,21],
[21,24,26,23,23,27,24,28,0,21,27,30],
[30,29,28,28,24,28,28,27,29,0,26,27],
[21,20,25,28,23,23,19,33,23,24,0,24],
[26,25,23,27,26,26,22,29,20,23,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 118, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,16,26,20,21,28,20,20,19,22,22],
[30,0,17,23,25,23,28,22,22,21,26,28],
[34,33,0,29,27,27,33,29,27,28,24,35],
[24,27,21,0,24,23,34,24,23,20,23,21],
[30,25,23,26,0,24,36,27,23,24,28,24],
[29,27,23,27,26,0,31,32,22,25,29,28],
[22,22,17,16,14,19,0,20,21,16,17,13],
[30,28,21,26,23,18,30,0,23,19,21,23],
[30,28,23,27,27,28,29,27,0,24,24,27],
[31,29,22,30,26,25,34,31,26,0,19,24],
[28,24,26,27,22,21,33,29,26,31,0,24],
[28,22,15,29,26,22,37,27,23,26,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 119, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,24,27,30,19,17,31,22,30,26,24],
[31,0,21,19,18,18,15,29,22,37,27,24],
[26,29,0,24,35,24,18,29,13,32,26,22],
[23,31,26,0,32,21,13,31,19,30,30,30],
[20,32,15,18,0,18,17,31,16,33,32,27],
[31,32,26,29,32,0,26,42,20,41,33,26],
[33,35,32,37,33,24,0,30,27,24,25,27],
[19,21,21,19,19,8,20,0,23,36,19,29],
[28,28,37,31,34,30,23,27,0,30,25,24],
[20,13,18,20,17,9,26,14,20,0,14,28],
[24,23,24,20,18,17,25,31,25,36,0,28],
[26,26,28,20,23,24,23,21,26,22,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 120, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,31,23,25,29,21,30,25,25,31,24],
[22,0,31,23,19,24,20,21,25,22,23,22],
[19,19,0,20,19,20,20,21,21,19,18,24],
[27,27,30,0,20,27,24,22,22,22,25,24],
[25,31,31,30,0,29,29,25,26,26,29,28],
[21,26,30,23,21,0,21,20,23,27,27,21],
[29,30,30,26,21,29,0,26,23,25,26,19],
[20,29,29,28,25,30,24,0,27,29,28,25],
[25,25,29,28,24,27,27,23,0,26,24,20],
[25,28,31,28,24,23,25,21,24,0,26,27],
[19,27,32,25,21,23,24,22,26,24,0,23],
[26,28,26,26,22,29,31,25,30,23,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 121, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,25,22,23,21,22,26,31,19,21,27],
[29,0,29,34,27,24,31,28,32,31,29,27],
[25,21,0,27,15,18,18,16,21,24,20,25],
[28,16,23,0,24,27,17,29,28,20,20,27],
[27,23,35,26,0,18,23,27,27,22,20,31],
[29,26,32,23,32,0,23,25,35,22,19,28],
[28,19,32,33,27,27,0,23,30,26,26,34],
[24,22,34,21,23,25,27,0,28,23,26,26],
[19,18,29,22,23,15,20,22,0,21,20,28],
[31,19,26,30,28,28,24,27,29,0,17,24],
[29,21,30,30,30,31,24,24,30,33,0,28],
[23,23,25,23,19,22,16,24,22,26,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 122, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,20,25,26,26,23,22,27,22,24,25],
[27,0,21,19,20,23,24,24,26,16,25,22],
[30,29,0,27,28,26,26,27,26,25,26,29],
[25,31,23,0,29,28,26,23,30,28,25,27],
[24,30,22,21,0,23,28,26,27,24,20,28],
[24,27,24,22,27,0,22,21,25,24,22,22],
[27,26,24,24,22,28,0,24,25,25,24,28],
[28,26,23,27,24,29,26,0,27,26,27,24],
[23,24,24,20,23,25,25,23,0,23,18,25],
[28,34,25,22,26,26,25,24,27,0,25,25],
[26,25,24,25,30,28,26,23,32,25,0,27],
[25,28,21,23,22,28,22,26,25,25,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 123, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,34,31,34,25,34,25,30,26,26,35],
[17,0,20,25,30,6,21,16,19,16,29,22],
[16,30,0,22,34,19,34,26,33,15,32,29],
[19,25,28,0,29,16,26,20,24,21,26,24],
[16,20,16,21,0,14,25,25,19,19,24,20],
[25,44,31,34,36,0,34,21,28,29,38,37],
[16,29,16,24,25,16,0,20,23,19,34,22],
[25,34,24,30,25,29,30,0,26,28,33,25],
[20,31,17,26,31,22,27,24,0,20,38,29],
[24,34,35,29,31,21,31,22,30,0,29,30],
[24,21,18,24,26,12,16,17,12,21,0,16],
[15,28,21,26,30,13,28,25,21,20,34,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 124, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,22,15,12,6,13,19,24,10,25,21],
[34,0,22,15,37,22,34,30,27,31,31,24],
[28,28,0,3,28,22,12,18,15,19,18,18],
[35,35,47,0,38,25,22,25,44,19,22,28],
[38,13,22,12,0,22,10,13,31,10,34,19],
[44,28,28,25,28,0,25,25,37,22,34,37],
[37,16,38,28,40,25,0,15,40,25,34,15],
[31,20,32,25,37,25,35,0,34,41,38,37],
[26,23,35,6,19,13,10,16,0,7,13,9],
[40,19,31,31,40,28,25,9,43,0,40,28],
[25,19,32,28,16,16,16,12,37,10,0,15],
[29,26,32,22,31,13,35,13,41,22,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 125, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,32,29,25,23,28,34,30,29,19,22],
[26,0,33,28,20,30,25,27,21,25,18,29],
[18,17,0,24,20,26,28,28,23,24,18,20],
[21,22,26,0,18,25,25,29,21,22,21,27],
[25,30,30,32,0,32,33,38,29,31,25,31],
[27,20,24,25,18,0,25,30,27,25,21,20],
[22,25,22,25,17,25,0,29,26,26,23,22],
[16,23,22,21,12,20,21,0,13,21,13,19],
[20,29,27,29,21,23,24,37,0,23,25,24],
[21,25,26,28,19,25,24,29,27,0,21,20],
[31,32,32,29,25,29,27,37,25,29,0,23],
[28,21,30,23,19,30,28,31,26,30,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 126, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,22,21,25,29,26,25,17,26,21,23],
[28,0,24,21,24,33,29,29,18,27,20,23],
[28,26,0,26,28,31,24,32,20,28,19,28],
[29,29,24,0,29,31,26,26,24,28,26,30],
[25,26,22,21,0,31,22,22,18,31,17,18],
[21,17,19,19,19,0,24,19,14,19,15,15],
[24,21,26,24,28,26,0,31,23,31,26,30],
[25,21,18,24,28,31,19,0,26,24,21,26],
[33,32,30,26,32,36,27,24,0,25,21,30],
[24,23,22,22,19,31,19,26,25,0,18,22],
[29,30,31,24,33,35,24,29,29,32,0,29],
[27,27,22,20,32,35,20,24,20,28,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 127, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,24,29,15,21,23,32,28,35,31,21],
[17,0,18,24,16,28,15,12,26,26,15,21],
[26,32,0,31,29,26,22,29,33,38,26,26],
[21,26,19,0,23,23,24,18,15,33,19,19],
[35,34,21,27,0,27,24,28,32,39,30,24],
[29,22,24,27,23,0,22,27,30,37,25,28],
[27,35,28,26,26,28,0,20,29,31,29,22],
[18,38,21,32,22,23,30,0,23,26,18,18],
[22,24,17,35,18,20,21,27,0,34,27,23],
[15,24,12,17,11,13,19,24,16,0,20,17],
[19,35,24,31,20,25,21,32,23,30,0,21],
[29,29,24,31,26,22,28,32,27,33,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 128, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,22,26,31,25,24,29,28,29,27,29],
[28,0,25,28,31,25,33,26,24,21,19,32],
[28,25,0,26,33,31,29,32,27,28,29,37],
[24,22,24,0,26,24,29,27,23,23,25,28],
[19,19,17,24,0,28,24,28,20,15,15,27],
[25,25,19,26,22,0,26,28,23,11,24,24],
[26,17,21,21,26,24,0,26,27,23,27,25],
[21,24,18,23,22,22,24,0,18,22,17,26],
[22,26,23,27,30,27,23,32,0,19,32,29],
[21,29,22,27,35,39,27,28,31,0,31,27],
[23,31,21,25,35,26,23,33,18,19,0,28],
[21,18,13,22,23,26,25,24,21,23,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 129, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,16,0,10,34,34,50,16,10,26,24],
[40,0,40,24,0,24,24,40,16,0,16,24],
[34,10,0,0,10,34,34,50,16,10,26,24],
[50,26,50,0,10,34,34,50,26,10,26,34],
[40,50,40,40,0,34,34,50,16,10,50,24],
[16,26,16,16,16,0,10,26,16,10,26,24],
[16,26,16,16,16,40,0,26,16,26,26,40],
[0,10,0,0,0,24,24,0,0,0,16,24],
[34,34,34,24,34,34,34,50,0,10,50,24],
[40,50,40,40,40,40,24,50,40,0,40,24],
[24,34,24,24,0,24,24,34,0,10,0,24],
[26,26,26,16,26,26,10,26,26,26,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 130, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,27,26,27,20,27,10,43,17,27,21],
[23,0,41,10,16,39,34,7,35,15,39,7],
[23,9,0,16,18,30,35,9,33,6,23,8],
[24,40,34,0,25,33,40,30,35,30,39,41],
[23,34,32,25,0,33,33,22,42,24,46,22],
[30,11,20,17,17,0,17,17,36,5,31,14],
[23,16,15,10,17,33,0,5,33,9,22,7],
[40,43,41,20,28,33,45,0,40,33,45,34],
[7,15,17,15,8,14,17,10,0,5,24,7],
[33,35,44,20,26,45,41,17,45,0,49,26],
[23,11,27,11,4,19,28,5,26,1,0,5],
[29,43,42,9,28,36,43,16,43,24,45,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 131, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,18,21,15,18,24,28,27,23,25,23],
[26,0,17,25,11,22,20,30,18,21,31,26],
[32,33,0,28,21,20,34,31,36,31,33,29],
[29,25,22,0,21,26,25,22,32,30,28,23],
[35,39,29,29,0,28,36,36,35,34,39,24],
[32,28,30,24,22,0,24,34,34,27,29,33],
[26,30,16,25,14,26,0,30,29,35,37,26],
[22,20,19,28,14,16,20,0,26,28,28,18],
[23,32,14,18,15,16,21,24,0,26,28,25],
[27,29,19,20,16,23,15,22,24,0,34,25],
[25,19,17,22,11,21,13,22,22,16,0,23],
[27,24,21,27,26,17,24,32,25,25,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 132, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,20,17,17,17,21,21,19,17,22,21],
[29,0,26,23,28,29,27,21,25,27,26,25],
[30,24,0,27,20,29,25,24,28,23,28,25],
[33,27,23,0,23,34,27,22,27,26,29,24],
[33,22,30,27,0,32,28,26,28,25,30,29],
[33,21,21,16,18,0,22,19,21,17,25,24],
[29,23,25,23,22,28,0,21,24,21,24,27],
[29,29,26,28,24,31,29,0,32,27,32,26],
[31,25,22,23,22,29,26,18,0,18,28,22],
[33,23,27,24,25,33,29,23,32,0,31,25],
[28,24,22,21,20,25,26,18,22,19,0,22],
[29,25,25,26,21,26,23,24,28,25,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 133, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,14,14,18,21,23,18,19,17,15,4],
[32,0,39,37,31,37,38,32,24,21,24,29],
[36,11,0,25,22,21,21,18,8,20,14,21],
[36,13,25,0,29,28,28,26,20,24,16,14],
[32,19,28,21,0,30,31,32,21,25,28,16],
[29,13,29,22,20,0,27,19,14,13,18,14],
[27,12,29,22,19,23,0,19,19,14,15,14],
[32,18,32,24,18,31,31,0,24,22,17,15],
[31,26,42,30,29,36,31,26,0,23,22,26],
[33,29,30,26,25,37,36,28,27,0,17,22],
[35,26,36,34,22,32,35,33,28,33,0,22],
[46,21,29,36,34,36,36,35,24,28,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 134, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,25,21,28,21,24,27,22,22,21,26],
[22,0,24,23,31,18,23,25,22,24,21,25],
[25,26,0,22,28,20,21,22,24,23,18,28],
[29,27,28,0,31,24,25,32,26,26,31,26],
[22,19,22,19,0,16,17,21,21,19,20,25],
[29,32,30,26,34,0,23,32,28,27,26,30],
[26,27,29,25,33,27,0,34,28,25,26,34],
[23,25,28,18,29,18,16,0,22,25,22,27],
[28,28,26,24,29,22,22,28,0,28,27,25],
[28,26,27,24,31,23,25,25,22,0,30,31],
[29,29,32,19,30,24,24,28,23,20,0,29],
[24,25,22,24,25,20,16,23,25,19,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 135, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,16,17,21,12,9,16,16,8,15,21],
[35,0,29,22,33,29,30,33,31,31,25,36],
[34,21,0,22,32,31,38,25,39,20,33,37],
[33,28,28,0,28,28,28,27,23,15,16,27],
[29,17,18,22,0,27,23,12,32,23,32,23],
[38,21,19,22,23,0,23,30,25,25,26,25],
[41,20,12,22,27,27,0,19,25,18,24,30],
[34,17,25,23,38,20,31,0,37,16,30,28],
[34,19,11,27,18,25,25,13,0,8,21,18],
[42,19,30,35,27,25,32,34,42,0,30,38],
[35,25,17,34,18,24,26,20,29,20,0,13],
[29,14,13,23,27,25,20,22,32,12,37,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 136, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,22,23,15,17,21,25,23,24,28,18],
[23,0,23,22,13,19,22,25,25,21,30,16],
[28,27,0,25,20,22,23,29,34,31,35,19],
[27,28,25,0,18,24,22,19,27,22,25,22],
[35,37,30,32,0,27,30,32,36,34,36,23],
[33,31,28,26,23,0,25,29,24,27,32,28],
[29,28,27,28,20,25,0,37,30,27,36,22],
[25,25,21,31,18,21,13,0,26,26,20,20],
[27,25,16,23,14,26,20,24,0,21,25,19],
[26,29,19,28,16,23,23,24,29,0,29,20],
[22,20,15,25,14,18,14,30,25,21,0,18],
[32,34,31,28,27,22,28,30,31,30,32,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 137, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,23,43,34,21,21,38,27,18,31,35],
[25,0,26,32,23,25,28,28,27,20,28,31],
[27,24,0,25,22,15,24,29,17,14,12,27],
[7,18,25,0,15,4,21,11,10,16,17,19],
[16,27,28,35,0,17,28,31,24,28,20,34],
[29,25,35,46,33,0,26,39,18,31,28,38],
[29,22,26,29,22,24,0,20,15,21,21,33],
[12,22,21,39,19,11,30,0,18,21,16,32],
[23,23,33,40,26,32,35,32,0,24,21,31],
[32,30,36,34,22,19,29,29,26,0,19,31],
[19,22,38,33,30,22,29,34,29,31,0,25],
[15,19,23,31,16,12,17,18,19,19,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 138, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,30,31,29,23,24,29,26,32,31,23],
[24,0,23,28,22,27,24,26,24,29,30,29],
[20,27,0,34,27,26,24,28,28,25,28,25],
[19,22,16,0,19,19,20,24,17,21,23,24],
[21,28,23,31,0,26,27,31,24,26,30,31],
[27,23,24,31,24,0,18,29,21,23,30,22],
[26,26,26,30,23,32,0,28,25,26,32,26],
[21,24,22,26,19,21,22,0,24,20,22,27],
[24,26,22,33,26,29,25,26,0,27,23,27],
[18,21,25,29,24,27,24,30,23,0,27,28],
[19,20,22,27,20,20,18,28,27,23,0,27],
[27,21,25,26,19,28,24,23,23,22,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 139, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,27,22,24,23,31,15,25,21,21,26],
[34,0,31,23,24,20,31,23,25,28,24,25],
[23,19,0,27,20,24,23,15,28,23,22,25],
[28,27,23,0,22,23,28,26,28,29,26,30],
[26,26,30,28,0,29,29,23,30,26,23,31],
[27,30,26,27,21,0,26,23,31,24,23,27],
[19,19,27,22,21,24,0,10,21,26,18,20],
[35,27,35,24,27,27,40,0,30,29,25,28],
[25,25,22,22,20,19,29,20,0,26,21,25],
[29,22,27,21,24,26,24,21,24,0,30,31],
[29,26,28,24,27,27,32,25,29,20,0,32],
[24,25,25,20,19,23,30,22,25,19,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 140, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,26,19,27,20,29,17,25,15,21,28],
[29,0,28,24,30,27,33,23,31,26,28,23],
[24,22,0,21,24,21,25,23,27,17,18,21],
[31,26,29,0,34,21,28,26,33,21,27,26],
[23,20,26,16,0,17,25,15,19,19,16,18],
[30,23,29,29,33,0,26,27,30,21,28,25],
[21,17,25,22,25,24,0,17,32,26,24,25],
[33,27,27,24,35,23,33,0,32,25,29,29],
[25,19,23,17,31,20,18,18,0,23,23,21],
[35,24,33,29,31,29,24,25,27,0,26,32],
[29,22,32,23,34,22,26,21,27,24,0,24],
[22,27,29,24,32,25,25,21,29,18,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 141, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,24,26,32,26,33,24,27,34,30,33],
[31,0,24,27,34,24,27,25,27,34,28,31],
[26,26,0,20,38,30,31,27,22,34,30,27],
[24,23,30,0,32,24,30,17,27,29,22,29],
[18,16,12,18,0,17,16,11,9,25,21,24],
[24,26,20,26,33,0,24,21,20,30,27,22],
[17,23,19,20,34,26,0,17,19,25,22,28],
[26,25,23,33,39,29,33,0,28,33,30,23],
[23,23,28,23,41,30,31,22,0,32,32,34],
[16,16,16,21,25,20,25,17,18,0,17,15],
[20,22,20,28,29,23,28,20,18,33,0,17],
[17,19,23,21,26,28,22,27,16,35,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 142, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,15,24,26,19,25,14,25,32,25,14],
[35,0,26,26,50,30,27,28,27,32,16,36],
[35,24,0,33,48,22,35,17,26,40,26,35],
[26,24,17,0,37,24,18,6,22,44,26,24],
[24,0,2,13,0,21,23,13,21,23,12,1],
[31,20,28,26,29,0,28,16,29,38,16,24],
[25,23,15,32,27,22,0,3,21,31,25,22],
[36,22,33,44,37,34,47,0,36,42,32,37],
[25,23,24,28,29,21,29,14,0,32,13,27],
[18,18,10,6,27,12,19,8,18,0,18,6],
[25,34,24,24,38,34,25,18,37,32,0,36],
[36,14,15,26,49,26,28,13,23,44,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 143, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,41,18,25,42,17,33,19,25,26,33],
[17,0,41,34,25,41,15,24,17,25,26,32],
[9,9,0,26,33,33,16,8,18,26,27,24],
[32,16,24,0,25,31,23,32,24,24,24,32],
[25,25,17,25,0,33,8,15,17,17,26,16],
[8,9,17,19,17,0,15,16,8,10,10,17],
[33,35,34,27,42,35,0,33,34,27,18,35],
[17,26,42,18,35,34,17,0,35,35,26,26],
[31,33,32,26,33,42,16,15,0,25,25,24],
[25,25,24,26,33,40,23,15,25,0,41,25],
[24,24,23,26,24,40,32,24,25,9,0,24],
[17,18,26,18,34,33,15,24,26,25,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 144, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,20,27,22,19,20,24,22,27,19,24],
[25,0,22,26,20,20,25,28,26,34,24,31],
[30,28,0,30,29,25,29,32,25,33,25,31],
[23,24,20,0,22,21,21,24,20,27,21,26],
[28,30,21,28,0,20,26,27,27,32,25,32],
[31,30,25,29,30,0,29,33,30,36,27,32],
[30,25,21,29,24,21,0,28,28,27,24,32],
[26,22,18,26,23,17,22,0,21,20,23,22],
[28,24,25,30,23,20,22,29,0,29,24,27],
[23,16,17,23,18,14,23,30,21,0,21,25],
[31,26,25,29,25,23,26,27,26,29,0,31],
[26,19,19,24,18,18,18,28,23,25,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 145, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,25,30,22,26,25,20,26,31,22,26],
[28,0,21,32,24,30,25,27,24,32,25,24],
[25,29,0,29,29,31,25,29,25,28,26,32],
[20,18,21,0,16,23,21,19,23,24,17,19],
[28,26,21,34,0,29,25,25,23,29,26,27],
[24,20,19,27,21,0,21,24,21,25,23,23],
[25,25,25,29,25,29,0,19,24,24,23,26],
[30,23,21,31,25,26,31,0,28,28,27,24],
[24,26,25,27,27,29,26,22,0,26,21,24],
[19,18,22,26,21,25,26,22,24,0,19,23],
[28,25,24,33,24,27,27,23,29,31,0,27],
[24,26,18,31,23,27,24,26,26,27,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 146, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,6,16,27,27,25,31,22,17,24,29],
[32,0,31,27,20,30,29,30,22,27,37,33],
[44,19,0,28,26,25,37,30,24,35,22,38],
[34,23,22,0,21,31,30,26,19,24,26,34],
[23,30,24,29,0,29,22,35,28,30,32,28],
[23,20,25,19,21,0,25,31,23,24,29,29],
[25,21,13,20,28,25,0,29,23,21,34,28],
[19,20,20,24,15,19,21,0,12,26,24,19],
[28,28,26,31,22,27,27,38,0,30,35,33],
[33,23,15,26,20,26,29,24,20,0,34,25],
[26,13,28,24,18,21,16,26,15,16,0,29],
[21,17,12,16,22,21,22,31,17,25,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 147, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,18,25,25,18,26,29,25,32,27,20],
[26,0,27,28,26,21,22,24,28,31,31,24],
[32,23,0,25,30,20,24,26,22,30,28,21],
[25,22,25,0,28,21,25,19,29,31,29,23],
[25,24,20,22,0,20,26,22,26,31,28,18],
[32,29,30,29,30,0,26,24,29,34,31,30],
[24,28,26,25,24,24,0,21,21,29,24,18],
[21,26,24,31,28,26,29,0,21,37,27,25],
[25,22,28,21,24,21,29,29,0,31,29,21],
[18,19,20,19,19,16,21,13,19,0,20,17],
[23,19,22,21,22,19,26,23,21,30,0,15],
[30,26,29,27,32,20,32,25,29,33,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 148, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,36,34,31,38,36,33,32,29,29,38],
[26,0,31,25,29,29,34,27,30,24,25,34],
[14,19,0,20,17,12,23,20,22,17,15,22],
[16,25,30,0,23,25,28,22,29,30,21,33],
[19,21,33,27,0,25,26,25,28,28,22,39],
[12,21,38,25,25,0,28,29,30,25,20,33],
[14,16,27,22,24,22,0,24,26,24,26,28],
[17,23,30,28,25,21,26,0,30,23,19,35],
[18,20,28,21,22,20,24,20,0,31,22,28],
[21,26,33,20,22,25,26,27,19,0,24,33],
[21,25,35,29,28,30,24,31,28,26,0,28],
[12,16,28,17,11,17,22,15,22,17,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 149, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,39,25,31,31,22,35,23,26,29,32],
[28,0,38,26,28,18,15,38,26,25,23,22],
[11,12,0,15,21,10,17,29,5,6,12,11],
[25,24,35,0,30,24,21,37,29,22,37,25],
[19,22,29,20,0,21,25,20,13,11,29,19],
[19,32,40,26,29,0,20,32,29,15,30,20],
[28,35,33,29,25,30,0,41,16,20,25,31],
[15,12,21,13,30,18,9,0,0,15,15,20],
[27,24,45,21,37,21,34,50,0,16,31,27],
[24,25,44,28,39,35,30,35,34,0,35,25],
[21,27,38,13,21,20,25,35,19,15,0,22],
[18,28,39,25,31,30,19,30,23,25,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 150, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,14,18,23,21,23,25,22,22,20,20],
[26,0,19,22,27,19,16,19,28,25,23,20],
[36,31,0,28,33,27,23,30,25,28,28,27],
[32,28,22,0,33,22,29,28,33,30,20,28],
[27,23,17,17,0,22,26,19,25,25,20,18],
[29,31,23,28,28,0,29,35,35,30,30,20],
[27,34,27,21,24,21,0,32,28,29,26,19],
[25,31,20,22,31,15,18,0,32,29,29,21],
[28,22,25,17,25,15,22,18,0,25,19,16],
[28,25,22,20,25,20,21,21,25,0,18,24],
[30,27,22,30,30,20,24,21,31,32,0,26],
[30,30,23,22,32,30,31,29,34,26,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 151, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,25,23,30,27,25,27,26,26,24,23],
[22,0,19,21,26,26,17,27,17,16,13,22],
[25,31,0,15,24,27,23,31,28,26,22,25],
[27,29,35,0,28,34,19,24,28,30,23,27],
[20,24,26,22,0,18,18,26,22,22,22,25],
[23,24,23,16,32,0,16,26,19,18,16,23],
[25,33,27,31,32,34,0,32,28,25,25,32],
[23,23,19,26,24,24,18,0,20,16,20,23],
[24,33,22,22,28,31,22,30,0,18,20,24],
[24,34,24,20,28,32,25,34,32,0,17,30],
[26,37,28,27,28,34,25,30,30,33,0,35],
[27,28,25,23,25,27,18,27,26,20,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 152, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,26,32,26,22,25,31,38,22,28,26],
[24,0,26,27,29,16,27,29,32,17,20,18],
[24,24,0,27,25,19,25,26,35,23,26,20],
[18,23,23,0,25,20,22,20,34,15,22,16],
[24,21,25,25,0,19,10,19,24,19,18,16],
[28,34,31,30,31,0,28,24,37,29,25,31],
[25,23,25,28,40,22,0,28,32,24,23,24],
[19,21,24,30,31,26,22,0,31,21,22,25],
[12,18,15,16,26,13,18,19,0,21,21,16],
[28,33,27,35,31,21,26,29,29,0,23,24],
[22,30,24,28,32,25,27,28,29,27,0,23],
[24,32,30,34,34,19,26,25,34,26,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 153, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,23,18,26,10,31,16,5,27,33,23],
[30,0,26,25,29,28,33,26,12,40,35,21],
[27,24,0,27,15,26,25,27,26,25,30,27],
[32,25,23,0,12,26,16,13,25,37,38,22],
[24,21,35,38,0,28,29,32,20,33,33,16],
[40,22,24,24,22,0,27,20,5,32,28,25],
[19,17,25,34,21,23,0,24,17,25,36,19],
[34,24,23,37,18,30,26,0,18,29,33,30],
[45,38,24,25,30,45,33,32,0,44,45,45],
[23,10,25,13,17,18,25,21,6,0,16,9],
[17,15,20,12,17,22,14,17,5,34,0,10],
[27,29,23,28,34,25,31,20,5,41,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 154, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,28,36,30,23,26,25,26,34,23,23],
[33,0,36,35,30,24,26,25,28,33,36,35],
[22,14,0,35,24,17,12,12,17,19,19,22],
[14,15,15,0,27,15,11,7,13,26,13,23],
[20,20,26,23,0,18,14,9,19,21,17,24],
[27,26,33,35,32,0,27,19,33,28,25,30],
[24,24,38,39,36,23,0,20,26,30,29,32],
[25,25,38,43,41,31,30,0,34,28,23,37],
[24,22,33,37,31,17,24,16,0,25,24,32],
[16,17,31,24,29,22,20,22,25,0,20,28],
[27,14,31,37,33,25,21,27,26,30,0,23],
[27,15,28,27,26,20,18,13,18,22,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 155, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,20,28,24,21,23,23,22,23,21,25],
[29,0,25,24,24,23,25,22,23,22,24,26],
[30,25,0,22,24,20,24,21,27,22,17,22],
[22,26,28,0,25,22,27,19,20,22,20,26],
[26,26,26,25,0,23,23,23,23,21,18,25],
[29,27,30,28,27,0,28,23,27,27,29,23],
[27,25,26,23,27,22,0,23,29,27,23,23],
[27,28,29,31,27,27,27,0,22,29,29,29],
[28,27,23,30,27,23,21,28,0,21,25,24],
[27,28,28,28,29,23,23,21,29,0,26,24],
[29,26,33,30,32,21,27,21,25,24,0,25],
[25,24,28,24,25,27,27,21,26,26,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 156, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,34,22,27,9,40,16,32,24,9,40,32],
[16,0,14,23,16,33,17,23,31,23,30,24],
[28,36,0,28,28,28,27,20,35,28,49,19],
[23,27,22,0,23,34,24,23,24,9,30,24],
[41,34,22,27,0,41,35,41,43,25,40,32],
[10,17,22,16,9,0,16,22,24,8,31,22],
[34,33,23,26,15,34,0,25,24,15,40,17],
[18,27,30,27,9,28,25,0,34,9,41,18],
[26,19,15,26,7,26,26,16,0,15,32,17],
[41,27,22,41,25,42,35,41,35,0,33,24],
[10,20,1,20,10,19,10,9,18,17,0,11],
[18,26,31,26,18,28,33,32,33,26,39,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 157, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,13,31,38,35,29,38,24,32,28,25],
[27,0,26,26,35,37,34,34,27,31,30,21],
[37,24,0,23,35,33,28,38,27,31,27,16],
[19,24,27,0,34,29,27,31,20,27,28,10],
[12,15,15,16,0,27,24,25,20,26,21,3],
[15,13,17,21,23,0,24,16,14,25,19,11],
[21,16,22,23,26,26,0,25,20,31,31,11],
[12,16,12,19,25,34,25,0,19,30,23,13],
[26,23,23,30,30,36,30,31,0,28,30,19],
[18,19,19,23,24,25,19,20,22,0,18,11],
[22,20,23,22,29,31,19,27,20,32,0,15],
[25,29,34,40,47,39,39,37,31,39,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 158, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,32,28,27,27,23,16,28,29,22,26],
[20,0,26,27,24,25,24,23,30,21,28,27],
[18,24,0,20,19,23,14,14,22,17,20,22],
[22,23,30,0,19,24,19,18,23,25,28,22],
[23,26,31,31,0,29,23,19,28,26,27,24],
[23,25,27,26,21,0,16,18,26,22,28,23],
[27,26,36,31,27,34,0,26,25,24,28,24],
[34,27,36,32,31,32,24,0,32,29,26,29],
[22,20,28,27,22,24,25,18,0,24,24,25],
[21,29,33,25,24,28,26,21,26,0,28,23],
[28,22,30,22,23,22,22,24,26,22,0,27],
[24,23,28,28,26,27,26,21,25,27,23,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 159, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,29,27,28,30,28,25,26,27,21,21,21],
[21,0,22,16,25,24,21,18,25,18,20,23],
[23,28,0,23,23,25,21,22,28,23,19,24],
[22,34,27,0,26,26,21,22,29,19,21,25],
[20,25,27,24,0,23,25,13,25,18,17,25],
[22,26,25,24,27,0,21,22,23,18,19,20],
[25,29,29,29,25,29,0,22,28,24,23,23],
[24,32,28,28,37,28,28,0,29,25,27,27],
[23,25,22,21,25,27,22,21,0,23,20,19],
[29,32,27,31,32,32,26,25,27,0,23,28],
[29,30,31,29,33,31,27,23,30,27,0,25],
[29,27,26,25,25,30,27,23,31,22,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 160, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,19,26,20,41,25,34,33,28,28,19],
[24,0,25,23,26,35,25,31,35,21,22,17],
[31,25,0,28,17,32,31,33,25,19,32,16],
[24,27,22,0,19,33,31,30,28,19,29,17],
[30,24,33,31,0,40,32,32,35,28,30,26],
[9,15,18,17,10,0,16,21,22,13,23,15],
[25,25,19,19,18,34,0,25,31,23,24,19],
[16,19,17,20,18,29,25,0,30,16,15,10],
[17,15,25,22,15,28,19,20,0,21,17,8],
[22,29,31,31,22,37,27,34,29,0,36,20],
[22,28,18,21,20,27,26,35,33,14,0,17],
[31,33,34,33,24,35,31,40,42,30,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 161, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,27,25,26,30,26,30,27,25,25,25],
[24,0,27,21,23,24,16,24,16,20,21,25],
[23,23,0,17,21,24,18,26,22,19,22,17],
[25,29,33,0,27,28,24,28,21,23,26,23],
[24,27,29,23,0,24,20,26,19,20,22,22],
[20,26,26,22,26,0,23,30,24,19,24,22],
[24,34,32,26,30,27,0,33,24,21,28,26],
[20,26,24,22,24,20,17,0,22,18,16,20],
[23,34,28,29,31,26,26,28,0,21,23,27],
[25,30,31,27,30,31,29,32,29,0,30,20],
[25,29,28,24,28,26,22,34,27,20,0,23],
[25,25,33,27,28,28,24,30,23,30,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 162, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,43,22,22,37,19,28,20,21,28,20,12],
[7,0,18,14,18,20,7,16,7,12,10,7],
[28,32,0,27,32,33,19,21,24,32,21,33],
[28,36,23,0,23,30,22,21,29,11,27,28],
[13,32,18,27,0,24,13,25,17,23,23,13],
[31,30,17,20,26,0,22,14,17,18,20,25],
[22,43,31,28,37,28,0,20,16,31,26,21],
[30,34,29,29,25,36,30,0,30,28,21,24],
[29,43,26,21,33,33,34,20,0,25,16,15],
[22,38,18,39,27,32,19,22,25,0,18,19],
[30,40,29,23,27,30,24,29,34,32,0,24],
[38,43,17,22,37,25,29,26,35,31,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 163, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,24,36,33,24,31,33,26,28,20,30],
[24,0,25,24,23,25,22,27,25,20,22,21],
[26,25,0,34,31,23,28,23,24,27,19,25],
[14,26,16,0,25,16,22,23,20,22,15,17],
[17,27,19,25,0,26,22,22,22,24,16,21],
[26,25,27,34,24,0,29,27,28,27,21,22],
[19,28,22,28,28,21,0,25,20,24,22,26],
[17,23,27,27,28,23,25,0,20,25,20,22],
[24,25,26,30,28,22,30,30,0,33,19,26],
[22,30,23,28,26,23,26,25,17,0,20,24],
[30,28,31,35,34,29,28,30,31,30,0,25],
[20,29,25,33,29,28,24,28,24,26,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 164, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,23,20,20,20,25,27,23,29,27,27],
[23,0,35,20,23,32,30,39,34,28,31,33],
[27,15,0,13,14,27,24,12,16,21,17,17],
[30,30,37,0,24,32,33,27,26,29,25,36],
[30,27,36,26,0,27,36,35,36,29,24,32],
[30,18,23,18,23,0,29,18,23,23,16,19],
[25,20,26,17,14,21,0,15,22,33,24,23],
[23,11,38,23,15,32,35,0,24,28,20,32],
[27,16,34,24,14,27,28,26,0,18,26,39],
[21,22,29,21,21,27,17,22,32,0,23,35],
[23,19,33,25,26,34,26,30,24,27,0,36],
[23,17,33,14,18,31,27,18,11,15,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 165, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,21,22,23,11,20,30,18,15,12,22],
[20,0,20,22,32,25,24,35,16,17,19,31],
[29,30,0,26,36,25,25,39,27,28,23,35],
[28,28,24,0,34,30,34,27,24,18,15,30],
[27,18,14,16,0,10,11,17,17,8,9,14],
[39,25,25,20,40,0,29,34,25,16,22,22],
[30,26,25,16,39,21,0,35,29,20,19,28],
[20,15,11,23,33,16,15,0,16,17,10,23],
[32,34,23,26,33,25,21,34,0,21,19,33],
[35,33,22,32,42,34,30,33,29,0,27,37],
[38,31,27,35,41,28,31,40,31,23,0,33],
[28,19,15,20,36,28,22,27,17,13,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 166, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,35,28,36,23,31,29,33,36,27,24,21],
[15,0,16,30,21,27,28,28,26,23,30,25],
[22,34,0,35,26,31,34,28,32,26,30,18],
[14,20,15,0,16,20,21,20,29,21,26,15],
[27,29,24,34,0,33,31,28,31,34,36,28],
[19,23,19,30,17,0,28,19,30,19,19,19],
[21,22,16,29,19,22,0,22,29,17,29,18],
[17,22,22,30,22,31,28,0,28,20,24,21],
[14,24,18,21,19,20,21,22,0,19,20,18],
[23,27,24,29,16,31,33,30,31,0,30,19],
[26,20,20,24,14,31,21,26,30,20,0,21],
[29,25,32,35,22,31,32,29,32,31,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 167, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,28,28,23,22,22,24,21,24,17,25],
[22,0,23,23,28,21,23,24,18,20,21,21],
[22,27,0,30,23,27,22,19,26,26,19,22],
[22,27,20,0,25,25,27,22,24,28,19,25],
[27,22,27,25,0,28,21,19,26,23,15,24],
[28,29,23,25,22,0,26,20,23,25,19,29],
[28,27,28,23,29,24,0,26,24,28,19,23],
[26,26,31,28,31,30,24,0,22,28,22,30],
[29,32,24,26,24,27,26,28,0,31,25,26],
[26,30,24,22,27,25,22,22,19,0,20,22],
[33,29,31,31,35,31,31,28,25,30,0,32],
[25,29,28,25,26,21,27,20,24,28,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 168, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,14,16,20,14,21,17,17,17,21,17],
[33,0,19,23,28,20,26,25,30,25,22,25],
[36,31,0,28,24,23,29,28,30,26,31,32],
[34,27,22,0,25,22,23,23,22,25,29,24],
[30,22,26,25,0,24,30,22,25,25,26,24],
[36,30,27,28,26,0,30,24,29,27,28,32],
[29,24,21,27,20,20,0,19,22,22,25,20],
[33,25,22,27,28,26,31,0,28,30,30,25],
[33,20,20,28,25,21,28,22,0,23,30,23],
[33,25,24,25,25,23,28,20,27,0,23,26],
[29,28,19,21,24,22,25,20,20,27,0,19],
[33,25,18,26,26,18,30,25,27,24,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 169, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,27,24,21,26,24,32,21,20,26,23],
[23,0,24,17,26,20,26,25,23,19,27,21],
[23,26,0,18,24,20,24,21,16,16,24,19],
[26,33,32,0,29,29,29,33,25,22,32,30],
[29,24,26,21,0,24,21,25,19,23,26,18],
[24,30,30,21,26,0,25,27,24,20,30,23],
[26,24,26,21,29,25,0,29,25,15,25,26],
[18,25,29,17,25,23,21,0,24,18,23,22],
[29,27,34,25,31,26,25,26,0,23,29,27],
[30,31,34,28,27,30,35,32,27,0,32,25],
[24,23,26,18,24,20,25,27,21,18,0,26],
[27,29,31,20,32,27,24,28,23,25,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 170, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,31,27,26,29,26,28,26,27,25,30],
[18,0,28,26,26,30,29,26,21,26,24,28],
[19,22,0,24,21,19,26,25,21,23,24,23],
[23,24,26,0,22,23,23,22,26,25,28,28],
[24,24,29,28,0,29,23,25,31,26,25,32],
[21,20,31,27,21,0,28,25,30,28,28,35],
[24,21,24,27,27,22,0,23,24,21,23,31],
[22,24,25,28,25,25,27,0,26,24,25,30],
[24,29,29,24,19,20,26,24,0,27,23,28],
[23,24,27,25,24,22,29,26,23,0,25,28],
[25,26,26,22,25,22,27,25,27,25,0,32],
[20,22,27,22,18,15,19,20,22,22,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 171, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,24,19,20,17,29,23,19,25,21,22],
[27,0,21,25,27,24,30,29,23,29,21,25],
[26,29,0,27,30,29,35,26,19,22,26,25],
[31,25,23,0,25,22,27,25,24,18,22,23],
[30,23,20,25,0,28,30,28,26,24,22,22],
[33,26,21,28,22,0,26,26,27,25,26,25],
[21,20,15,23,20,24,0,20,18,18,21,20],
[27,21,24,25,22,24,30,0,19,24,18,23],
[31,27,31,26,24,23,32,31,0,26,26,27],
[25,21,28,32,26,25,32,26,24,0,23,25],
[29,29,24,28,28,24,29,32,24,27,0,23],
[28,25,25,27,28,25,30,27,23,25,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 172, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,24,15,31,21,26,22,29,22,29,26],
[24,0,26,21,26,22,29,22,27,29,29,27],
[26,24,0,25,27,30,30,22,29,31,30,26],
[35,29,25,0,33,30,32,31,31,31,32,32],
[19,24,23,17,0,18,25,19,27,27,20,22],
[29,28,20,20,32,0,28,23,25,33,26,26],
[24,21,20,18,25,22,0,19,24,27,24,23],
[28,28,28,19,31,27,31,0,27,32,27,26],
[21,23,21,19,23,25,26,23,0,26,25,23],
[28,21,19,19,23,17,23,18,24,0,27,24],
[21,21,20,18,30,24,26,23,25,23,0,21],
[24,23,24,18,28,24,27,24,27,26,29,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 173, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,14,17,24,20,21,22,19,16,21,18],
[28,0,32,20,16,29,34,25,18,22,33,25],
[36,18,0,19,21,21,29,26,24,23,24,21],
[33,30,31,0,16,27,27,23,28,28,27,26],
[26,34,29,34,0,22,25,27,25,24,35,27],
[30,21,29,23,28,0,19,34,28,23,25,28],
[29,16,21,23,25,31,0,27,30,24,24,22],
[28,25,24,27,23,16,23,0,24,23,23,32],
[31,32,26,22,25,22,20,26,0,25,29,24],
[34,28,27,22,26,27,26,27,25,0,36,27],
[29,17,26,23,15,25,26,27,21,14,0,17],
[32,25,29,24,23,22,28,18,26,23,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 174, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,22,31,23,26,28,25,24,23,29,23],
[27,0,32,27,24,24,33,34,25,26,27,27],
[28,18,0,27,20,26,31,26,29,29,25,29],
[19,23,23,0,21,25,23,24,28,17,20,22],
[27,26,30,29,0,28,29,28,28,24,28,26],
[24,26,24,25,22,0,28,25,24,22,20,25],
[22,17,19,27,21,22,0,19,21,18,21,26],
[25,16,24,26,22,25,31,0,21,23,22,24],
[26,25,21,22,22,26,29,29,0,23,22,27],
[27,24,21,33,26,28,32,27,27,0,26,32],
[21,23,25,30,22,30,29,28,28,24,0,23],
[27,23,21,28,24,25,24,26,23,18,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 175, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,33,31,30,33,25,25,29,29,27,26,28],
[17,0,26,26,26,26,21,28,29,26,24,27],
[19,24,0,26,27,21,22,28,24,21,22,22],
[20,24,24,0,21,24,28,31,27,26,18,20],
[17,24,23,29,0,23,21,26,23,26,21,23],
[25,24,29,26,27,0,25,30,27,25,25,25],
[25,29,28,22,29,25,0,29,26,25,22,24],
[21,22,22,19,24,20,21,0,19,22,16,23],
[21,21,26,23,27,23,24,31,0,26,22,26],
[23,24,29,24,24,25,25,28,24,0,18,22],
[24,26,28,32,29,25,28,34,28,32,0,29],
[22,23,28,30,27,25,26,27,24,28,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 176, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,20,18,28,16,32,14,20,13,24,24],
[25,0,21,21,23,27,25,21,18,26,24,27],
[30,29,0,33,31,31,33,22,30,28,33,31],
[32,29,17,0,31,30,32,25,28,26,32,27],
[22,27,19,19,0,26,26,23,20,19,20,25],
[34,23,19,20,24,0,31,22,25,19,22,23],
[18,25,17,18,24,19,0,14,25,15,26,17],
[36,29,28,25,27,28,36,0,25,24,33,28],
[30,32,20,22,30,25,25,25,0,27,32,22],
[37,24,22,24,31,31,35,26,23,0,35,24],
[26,26,17,18,30,28,24,17,18,15,0,22],
[26,23,19,23,25,27,33,22,28,26,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 177, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,21,24,26,20,21,33,27,22,25,29],
[25,0,25,26,20,24,25,25,18,19,27,23],
[29,25,0,26,28,28,27,32,23,24,19,25],
[26,24,24,0,21,29,31,34,29,23,30,20],
[24,30,22,29,0,24,23,30,26,14,24,27],
[30,26,22,21,26,0,25,30,23,25,23,25],
[29,25,23,19,27,25,0,38,30,28,20,29],
[17,25,18,16,20,20,12,0,17,15,18,18],
[23,32,27,21,24,27,20,33,0,20,18,25],
[28,31,26,27,36,25,22,35,30,0,26,32],
[25,23,31,20,26,27,30,32,32,24,0,26],
[21,27,25,30,23,25,21,32,25,18,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 178, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,18,22,21,21,26,30,31,26,29,25],
[25,0,19,22,29,23,30,28,28,32,26,27],
[32,31,0,26,24,30,31,28,31,31,33,27],
[28,28,24,0,31,30,31,32,34,30,32,31],
[29,21,26,19,0,24,31,24,27,30,24,26],
[29,27,20,20,26,0,27,26,34,31,26,30],
[24,20,19,19,19,23,0,23,20,24,22,24],
[20,22,22,18,26,24,27,0,30,32,23,31],
[19,22,19,16,23,16,30,20,0,25,21,27],
[24,18,19,20,20,19,26,18,25,0,27,21],
[21,24,17,18,26,24,28,27,29,23,0,26],
[25,23,23,19,24,20,26,19,23,29,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 179, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,33,24,24,28,37,10,24,33,10],
[40,0,40,40,23,46,50,40,33,27,40,27],
[40,10,0,36,33,33,37,46,33,14,36,19],
[17,10,14,0,10,10,28,23,10,14,14,10],
[26,27,17,40,0,23,50,17,23,31,40,36],
[26,4,17,40,27,0,27,31,0,18,40,13],
[22,0,13,22,0,23,0,13,10,0,22,0],
[13,10,4,27,33,19,37,0,10,18,27,19],
[40,17,17,40,27,50,40,40,0,31,40,13],
[26,23,36,36,19,32,50,32,19,0,50,19],
[17,10,14,36,10,10,28,23,10,0,0,10],
[40,23,31,40,14,37,50,31,37,31,40,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 180, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,26,25,22,24,25,26,32,19,23,22],
[26,0,26,22,22,22,22,27,25,22,18,23],
[24,24,0,22,23,23,23,24,26,22,23,22],
[25,28,28,0,24,28,30,28,23,20,25,22],
[28,28,27,26,0,24,22,26,27,20,26,23],
[26,28,27,22,26,0,23,29,29,25,26,24],
[25,28,27,20,28,27,0,29,28,23,27,27],
[24,23,26,22,24,21,21,0,24,19,23,21],
[18,25,24,27,23,21,22,26,0,22,22,23],
[31,28,28,30,30,25,27,31,28,0,28,26],
[27,32,27,25,24,24,23,27,28,22,0,19],
[28,27,28,28,27,26,23,29,27,24,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 181, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,28,25,31,23,32,32,26,24,35,27,33],
[22,0,22,29,23,23,26,21,22,30,19,23],
[25,28,0,22,22,32,25,24,25,29,28,26],
[19,21,28,0,20,23,25,20,18,26,22,26],
[27,27,28,30,0,31,33,28,25,37,23,37],
[18,27,18,27,19,0,26,23,22,26,19,23],
[18,24,25,25,17,24,0,21,23,28,19,31],
[24,29,26,30,22,27,29,0,20,33,25,32],
[26,28,25,32,25,28,27,30,0,35,22,29],
[15,20,21,24,13,24,22,17,15,0,12,19],
[23,31,22,28,27,31,31,25,28,38,0,28],
[17,27,24,24,13,27,19,18,21,31,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 182, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,32,34,25,25,19,28,22,23,33,24,26],
[18,0,25,17,17,22,21,15,25,23,18,22],
[16,25,0,22,14,19,19,16,16,20,21,21],
[25,33,28,0,23,36,28,30,16,31,29,24],
[25,33,36,27,0,31,30,28,28,31,33,33],
[31,28,31,14,19,0,33,22,13,33,26,29],
[22,29,31,22,20,17,0,20,15,31,32,28],
[28,35,34,20,22,28,30,0,16,39,25,29],
[27,25,34,34,22,37,35,34,0,42,28,32],
[17,27,30,19,19,17,19,11,8,0,24,21],
[26,32,29,21,17,24,18,25,22,26,0,29],
[24,28,29,26,17,21,22,21,18,29,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 183, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1,1,30,1,0,12,1,9,19,0,0],
[49,0,18,49,20,27,49,10,9,27,9,27],
[49,32,0,49,20,39,31,20,31,38,19,27],
[20,1,1,0,1,0,22,10,9,28,0,1],
[49,30,30,49,0,39,49,10,21,27,27,27],
[50,23,11,50,11,0,32,20,19,38,10,1],
[38,1,19,28,1,18,0,1,9,19,0,19],
[49,40,30,40,40,30,49,0,21,18,18,30],
[41,41,19,41,29,31,41,29,0,19,19,19],
[31,23,12,22,23,12,31,32,31,0,0,12],
[50,41,31,50,23,40,50,32,31,50,0,40],
[50,23,23,49,23,49,31,20,31,38,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 184, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,27,16,25,24,25,19,26,24,26,19],
[27,0,26,20,26,23,21,21,35,26,24,26],
[23,24,0,18,26,22,23,16,30,23,21,21],
[34,30,32,0,35,29,27,25,34,33,31,29],
[25,24,24,15,0,24,25,17,26,23,24,17],
[26,27,28,21,26,0,28,21,28,20,27,20],
[25,29,27,23,25,22,0,19,31,21,22,24],
[31,29,34,25,33,29,31,0,33,29,31,24],
[24,15,20,16,24,22,19,17,0,18,21,16],
[26,24,27,17,27,30,29,21,32,0,24,25],
[24,26,29,19,26,23,28,19,29,26,0,24],
[31,24,29,21,33,30,26,26,34,25,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 185, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,22,16,15,22,15,15,11,20,11,7],
[37,0,27,34,29,31,32,25,21,36,27,20],
[28,23,0,30,23,25,15,15,20,25,18,14],
[34,16,20,0,23,21,17,14,20,27,17,18],
[35,21,27,27,0,32,22,17,27,36,34,19],
[28,19,25,29,18,0,17,17,15,29,20,22],
[35,18,35,33,28,33,0,25,21,38,34,30],
[35,25,35,36,33,33,25,0,31,26,27,25],
[39,29,30,30,23,35,29,19,0,32,26,15],
[30,14,25,23,14,21,12,24,18,0,11,14],
[39,23,32,33,16,30,16,23,24,39,0,26],
[43,30,36,32,31,28,20,25,35,36,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 186, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,26,19,18,19,22,25,17,37,28,23],
[36,0,32,25,36,24,18,30,32,37,42,32],
[24,18,0,26,15,12,23,20,24,34,20,20],
[31,25,24,0,28,23,29,28,35,42,30,22],
[32,14,35,22,0,17,18,23,24,33,42,31],
[31,26,38,27,33,0,30,35,25,32,37,25],
[28,32,27,21,32,20,0,25,39,40,31,24],
[25,20,30,22,27,15,25,0,22,27,35,18],
[33,18,26,15,26,25,11,28,0,28,27,22],
[13,13,16,8,17,18,10,23,22,0,20,12],
[22,8,30,20,8,13,19,15,23,30,0,23],
[27,18,30,28,19,25,26,32,28,38,27,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 187, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,23,27,25,19,28,30,25,23,31,29],
[28,0,30,21,20,22,25,25,38,20,25,26],
[27,20,0,29,24,19,25,23,41,23,29,21],
[23,29,21,0,22,20,26,24,35,26,35,22],
[25,30,26,28,0,28,32,21,33,28,33,19],
[31,28,31,30,22,0,24,23,29,28,37,24],
[22,25,25,24,18,26,0,22,34,19,29,19],
[20,25,27,26,29,27,28,0,33,21,29,21],
[25,12,9,15,17,21,16,17,0,20,20,17],
[27,30,27,24,22,22,31,29,30,0,35,25],
[19,25,21,15,17,13,21,21,30,15,0,15],
[21,24,29,28,31,26,31,29,33,25,35,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 188, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,30,25,27,23,19,26,28,22,27,23,28],
[20,0,21,21,18,17,20,29,18,18,22,21],
[25,29,0,25,25,24,23,29,24,29,28,29],
[23,29,25,0,24,20,22,29,23,25,24,27],
[27,32,25,26,0,24,24,34,27,26,28,26],
[31,33,26,30,26,0,22,32,28,31,23,30],
[24,30,27,28,26,28,0,37,29,29,25,27],
[22,21,21,21,16,18,13,0,18,17,18,23],
[28,32,26,27,23,22,21,32,0,27,29,27],
[23,32,21,25,24,19,21,33,23,0,23,28],
[27,28,22,26,22,27,25,32,21,27,0,28],
[22,29,21,23,24,20,23,27,23,22,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 189, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,26,25,22,23,24,33,22,20,20,28],
[25,0,31,31,26,23,28,33,24,29,31,25],
[24,19,0,28,23,21,22,29,17,25,22,22],
[25,19,22,0,23,21,24,30,21,24,18,27],
[28,24,27,27,0,23,28,32,27,31,24,27],
[27,27,29,29,27,0,28,29,22,25,26,24],
[26,22,28,26,22,22,0,31,22,31,23,27],
[17,17,21,20,18,21,19,0,18,19,15,14],
[28,26,33,29,23,28,28,32,0,30,31,26],
[30,21,25,26,19,25,19,31,20,0,20,26],
[30,19,28,32,26,24,27,35,19,30,0,30],
[22,25,28,23,23,26,23,36,24,24,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 190, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,27,29,25,30,26,25,29,21,24,29,28],
[23,0,30,24,30,25,26,26,26,25,26,27],
[21,20,0,18,26,19,17,18,24,23,17,19],
[25,26,32,0,30,31,30,30,26,25,28,32],
[20,20,24,20,0,24,21,23,22,27,17,26],
[24,25,31,19,26,0,22,28,22,24,24,27],
[25,24,33,20,29,28,0,26,26,26,23,28],
[21,24,32,20,27,22,24,0,27,24,22,25],
[29,24,26,24,28,28,24,23,0,27,24,26],
[26,25,27,25,23,26,24,26,23,0,22,26],
[21,24,33,22,33,26,27,28,26,28,0,26],
[22,23,31,18,24,23,22,25,24,24,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 191, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,17,31,26,31,22,17,19,21,27,22],
[26,0,25,28,28,36,18,20,19,18,24,24],
[33,25,0,31,33,37,26,26,27,24,36,25],
[19,22,19,0,24,28,16,18,25,22,17,11],
[24,22,17,26,0,27,12,10,12,20,28,15],
[19,14,13,22,23,0,8,11,10,13,18,19],
[28,32,24,34,38,42,0,25,25,29,27,30],
[33,30,24,32,40,39,25,0,22,33,32,21],
[31,31,23,25,38,40,25,28,0,30,34,19],
[29,32,26,28,30,37,21,17,20,0,29,26],
[23,26,14,33,22,32,23,18,16,21,0,17],
[28,26,25,39,35,31,20,29,31,24,33,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 192, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,19,27,23,18,15,23,19,32,13,17],
[30,0,26,29,34,22,23,23,29,37,26,25],
[31,24,0,29,24,23,20,25,33,32,23,25],
[23,21,21,0,19,21,18,26,26,30,23,25],
[27,16,26,31,0,23,20,27,24,31,23,25],
[32,28,27,29,27,0,25,25,34,33,31,26],
[35,27,30,32,30,25,0,23,34,32,26,29],
[27,27,25,24,23,25,27,0,23,25,25,22],
[31,21,17,24,26,16,16,27,0,27,25,20],
[18,13,18,20,19,17,18,25,23,0,18,16],
[37,24,27,27,27,19,24,25,25,32,0,26],
[33,25,25,25,25,24,21,28,30,34,24,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 193, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,25,31,26,28,27,28,27,29,28,29],
[19,0,24,29,29,25,27,29,28,25,20,22],
[25,26,0,25,27,28,19,26,20,24,20,20],
[19,21,25,0,25,27,22,20,21,28,20,25],
[24,21,23,25,0,24,24,24,19,23,24,24],
[22,25,22,23,26,0,24,23,24,21,24,18],
[23,23,31,28,26,26,0,22,27,25,22,29],
[22,21,24,30,26,27,28,0,19,23,19,21],
[23,22,30,29,31,26,23,31,0,28,26,29],
[21,25,26,22,27,29,25,27,22,0,22,18],
[22,30,30,30,26,26,28,31,24,28,0,24],
[21,28,30,25,26,32,21,29,21,32,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 194, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,26,17,12,17,14,16,21,19,21,8],
[32,0,38,17,36,28,27,32,41,31,38,28],
[24,12,0,17,19,18,14,9,14,20,19,17],
[33,33,33,0,30,26,33,32,39,38,38,22],
[38,14,31,20,0,28,27,27,21,25,23,28],
[33,22,32,24,22,0,19,23,28,28,31,17],
[36,23,36,17,23,31,0,27,34,30,33,33],
[34,18,41,18,23,27,23,0,31,30,30,26],
[29,9,36,11,29,22,16,19,0,29,31,24],
[31,19,30,12,25,22,20,20,21,0,32,22],
[29,12,31,12,27,19,17,20,19,18,0,19],
[42,22,33,28,22,33,17,24,26,28,31,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 195, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,15,20,21,18,26,17,30,18,19,23],
[25,0,18,19,17,22,24,23,23,22,24,17],
[35,32,0,25,21,25,26,28,33,27,28,25],
[30,31,25,0,25,22,27,25,30,24,17,25],
[29,33,29,25,0,32,33,30,29,30,26,30],
[32,28,25,28,18,0,26,22,29,26,20,24],
[24,26,24,23,17,24,0,20,29,20,23,24],
[33,27,22,25,20,28,30,0,29,22,26,25],
[20,27,17,20,21,21,21,21,0,21,15,23],
[32,28,23,26,20,24,30,28,29,0,25,25],
[31,26,22,33,24,30,27,24,35,25,0,30],
[27,33,25,25,20,26,26,25,27,25,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 196, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,14,5,15,21,23,15,18,7,7,21],
[35,0,25,26,26,26,25,20,29,26,28,22],
[36,25,0,33,7,24,35,16,20,19,25,39],
[45,24,17,0,22,28,35,18,13,18,34,33],
[35,24,43,28,0,28,40,23,21,26,28,42],
[29,24,26,22,22,0,26,9,18,12,16,33],
[27,25,15,15,10,24,0,22,28,18,16,14],
[35,30,34,32,27,41,28,0,28,18,26,31],
[32,21,30,37,29,32,22,22,0,23,29,33],
[43,24,31,32,24,38,32,32,27,0,26,30],
[43,22,25,16,22,34,34,24,21,24,0,22],
[29,28,11,17,8,17,36,19,17,20,28,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 197, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,31,40,17,24,33,30,19,29,31,26,31],
[19,0,24,14,31,26,23,19,30,27,17,22],
[10,26,0,17,30,23,25,11,33,27,13,26],
[33,36,33,0,36,33,35,29,22,35,32,22],
[26,19,20,14,0,23,16,13,14,24,24,19],
[17,24,27,17,27,0,15,12,23,20,22,21],
[20,27,25,15,34,35,0,9,26,36,31,22],
[31,31,39,21,37,38,41,0,38,38,29,27],
[21,20,17,28,36,27,24,12,0,26,26,27],
[19,23,23,15,26,30,14,12,24,0,32,23],
[24,33,37,18,26,28,19,21,24,18,0,24],
[19,28,24,28,31,29,28,23,23,27,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 198, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,24,25,23,23,21,16,22,26,25,19,19],
[26,0,20,23,21,20,17,22,21,25,17,19],
[25,30,0,28,24,23,21,28,25,22,22,24],
[27,27,22,0,21,19,19,23,26,24,23,20],
[27,29,26,29,0,25,27,26,25,23,25,21],
[29,30,27,31,25,0,20,27,27,31,25,25],
[34,33,29,31,23,30,0,31,27,28,26,25],
[28,28,22,27,24,23,19,0,18,24,23,23],
[24,29,25,24,25,23,23,32,0,27,24,23],
[25,25,28,26,27,19,22,26,23,0,25,24],
[31,33,28,27,25,25,24,27,26,25,0,24],
[31,31,26,30,29,25,25,27,27,26,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 199, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,24,21,21,28,24,25,25,28,25,29],
[27,0,23,24,27,22,27,19,24,29,29,25],
[26,27,0,25,26,25,25,22,28,27,24,28],
[29,26,25,0,25,22,25,25,24,34,30,28],
[29,23,24,25,0,27,28,28,28,34,30,31],
[22,28,25,28,23,0,25,24,31,32,29,27],
[26,23,25,25,22,25,0,25,21,28,28,29],
[25,31,28,25,22,26,25,0,27,36,26,32],
[25,26,22,26,22,19,29,23,0,32,25,22],
[22,21,23,16,16,18,22,14,18,0,23,23],
[25,21,26,20,20,21,22,24,25,27,0,25],
[21,25,22,22,19,23,21,18,28,27,25,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 50, 200, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbrcwd/mebbrcwd_12_50.csv", index=False, header=False)