
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg
from kemeny import sc

rep = 1
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,16,12,14,12,15,14,19,14,17,15,12,17],
[10,0,7,12,9,13,13,14,10,14,14,14,14],
[14,19,0,17,11,15,15,19,12,19,16,16,14],
[12,14,9,0,11,11,10,17,11,16,12,12,12],
[14,17,15,15,0,15,15,16,13,18,17,17,14],
[11,13,11,15,11,0,13,14,11,13,15,14,13],
[12,13,11,16,11,13,0,16,11,17,13,15,14],
[7,12,7,9,10,12,10,0,11,14,12,13,14],
[12,16,14,15,13,15,15,15,0,17,14,18,14],
[9,12,7,10,8,13,9,12,9,0,12,11,13],
[11,12,10,14,9,11,13,14,12,14,0,12,14],
[14,12,10,14,9,12,11,13,8,15,14,0,11],
[9,12,12,14,12,13,12,12,12,13,12,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 1, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,11,10,8,14,12,8,14,16,15,10],
[16,0,13,16,12,13,15,16,11,13,17,16,14],
[16,13,0,11,15,13,15,18,14,17,18,16,14],
[15,10,15,0,15,10,15,12,12,11,17,15,13],
[16,14,11,11,0,13,12,18,16,14,15,16,15],
[18,13,13,16,13,0,13,16,13,14,19,13,15],
[12,11,11,11,14,13,0,14,14,18,17,15,14],
[14,10,8,14,8,10,12,0,12,12,16,11,17],
[18,15,12,14,10,13,12,14,0,15,18,13,16],
[12,13,9,15,12,12,8,14,11,0,12,14,12],
[10,9,8,9,11,7,9,10,8,14,0,12,6],
[11,10,10,11,10,13,11,15,13,12,14,0,12],
[16,12,12,13,11,11,12,9,10,14,20,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 2, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,13,13,5,4,14,1,15,2,14,0,9],
[23,0,18,19,18,21,18,17,21,13,19,18,12],
[13,8,0,9,6,10,19,12,14,7,19,6,2],
[13,7,17,0,13,15,12,6,20,9,18,13,7],
[21,8,20,13,0,10,19,7,21,7,19,12,10],
[22,5,16,11,16,0,17,9,26,16,23,12,16],
[12,8,7,14,7,9,0,12,14,8,13,6,2],
[25,9,14,20,19,17,14,0,21,9,21,7,9],
[11,5,12,6,5,0,12,5,0,5,16,5,5],
[24,13,19,17,19,10,18,17,21,0,12,14,18],
[12,7,7,8,7,3,13,5,10,14,0,7,7],
[26,8,20,13,14,14,20,19,21,12,19,0,15],
[17,14,24,19,16,10,24,17,21,8,19,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 3, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,5,7,10,10,9,8,9,6,13,7,7],
[14,0,6,16,11,16,9,16,8,6,13,11,17],
[21,20,0,17,20,20,17,17,12,11,19,16,18],
[19,10,9,0,13,10,13,17,13,14,14,12,9],
[16,15,6,13,0,17,10,12,10,6,14,7,9],
[16,10,6,16,9,0,7,10,10,7,15,8,12],
[17,17,9,13,16,19,0,16,7,6,14,12,13],
[18,10,9,9,14,16,10,0,12,7,12,5,8],
[17,18,14,13,16,16,19,14,0,14,22,12,13],
[20,20,15,12,20,19,20,19,12,0,17,15,16],
[13,13,7,12,12,11,12,14,4,9,0,12,12],
[19,15,10,14,19,18,14,21,14,11,14,0,11],
[19,9,8,17,17,14,13,18,13,10,14,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 4, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,19,17,18,19,20,15,15,21,16,13,17],
[6,0,9,9,9,11,8,10,16,12,12,7,15],
[7,17,0,14,13,15,21,8,15,15,12,12,18],
[9,17,12,0,19,14,17,17,16,16,19,17,14],
[8,17,13,7,0,18,17,8,16,16,15,12,16],
[7,15,11,12,8,0,15,8,13,14,11,11,17],
[6,18,5,9,9,11,0,6,13,6,10,10,16],
[11,16,18,9,18,18,20,0,19,19,19,18,17],
[11,10,11,10,10,13,13,7,0,13,13,13,13],
[5,14,11,10,10,12,20,7,13,0,8,8,15],
[10,14,14,7,11,15,16,7,13,18,0,9,16],
[13,19,14,9,14,15,16,8,13,18,17,0,18],
[9,11,8,12,10,9,10,9,13,11,10,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 5, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,16,11,13,12,14,17,15,18,18,11,11],
[14,0,11,9,13,13,14,15,12,15,16,12,12],
[10,15,0,10,11,14,12,13,13,15,15,10,12],
[15,17,16,0,17,17,13,19,13,21,16,14,19],
[13,13,15,9,0,14,10,14,14,16,18,10,13],
[14,13,12,9,12,0,12,18,14,14,17,13,12],
[12,12,14,13,16,14,0,13,15,14,16,13,14],
[9,11,13,7,12,8,13,0,11,13,14,8,11],
[11,14,13,13,12,12,11,15,0,16,14,14,12],
[8,11,11,5,10,12,12,13,10,0,14,14,11],
[8,10,11,10,8,9,10,12,12,12,0,10,7],
[15,14,16,12,16,13,13,18,12,12,16,0,14],
[15,14,14,7,13,14,12,15,14,15,19,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 6, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,16,17,16,11,13,14,13,11,15,12,12],
[8,0,10,10,11,5,9,13,14,8,11,9,7],
[10,16,0,13,14,12,10,12,13,12,11,10,10],
[9,16,13,0,14,9,9,12,13,7,10,8,9],
[10,15,12,12,0,8,6,10,14,8,10,9,10],
[15,21,14,17,18,0,12,18,18,12,15,14,13],
[13,17,16,17,20,14,0,17,16,13,15,15,11],
[12,13,14,14,16,8,9,0,14,12,12,12,10],
[13,12,13,13,12,8,10,12,0,8,11,10,11],
[15,18,14,19,18,14,13,14,18,0,16,16,12],
[11,15,15,16,16,11,11,14,15,10,0,13,8],
[14,17,16,18,17,12,11,14,16,10,13,0,12],
[14,19,16,17,16,13,15,16,15,14,18,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 7, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,11,5,8,6,7,6,10,5,8,11,7],
[19,0,12,14,14,10,13,22,11,7,9,17,15],
[15,14,0,14,17,15,12,17,9,6,14,13,17],
[21,12,12,0,17,8,11,11,11,12,13,21,12],
[18,12,9,9,0,6,12,18,9,8,5,11,13],
[20,16,11,18,20,0,14,18,15,10,15,15,19],
[19,13,14,15,14,12,0,16,10,10,13,13,17],
[20,4,9,15,8,8,10,0,12,3,12,13,8],
[16,15,17,15,17,11,16,14,0,14,13,21,12],
[21,19,20,14,18,16,16,23,12,0,16,15,19],
[18,17,12,13,21,11,13,14,13,10,0,11,16],
[15,9,13,5,15,11,13,13,5,11,15,0,13],
[19,11,9,14,13,7,9,18,14,7,10,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 8, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,8,16,11,11,8,19,8,8,19,19,16],
[15,0,3,16,12,3,0,15,3,12,15,11,16],
[18,23,0,19,23,14,16,26,11,23,23,19,19],
[10,10,7,0,7,10,0,10,3,7,7,11,11],
[15,14,3,19,0,11,8,15,11,15,11,11,16],
[15,23,12,16,15,0,8,23,16,20,23,19,19],
[18,26,10,26,18,18,0,26,11,26,26,11,22],
[7,11,0,16,11,3,0,0,3,8,19,11,8],
[18,23,15,23,15,10,15,23,0,23,23,19,19],
[18,14,3,19,11,6,0,18,3,0,11,11,19],
[7,11,3,19,15,3,0,7,3,15,0,11,8],
[7,15,7,15,15,7,15,15,7,15,15,0,15],
[10,10,7,15,10,7,4,18,7,7,18,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 9, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,18,12,16,18,14,13,14,15,12,15,18],
[10,0,9,10,15,15,11,13,11,16,9,11,16],
[8,17,0,13,15,16,10,12,12,16,12,10,15],
[14,16,13,0,14,18,17,14,13,14,14,12,18],
[10,11,11,12,0,13,15,15,12,11,12,11,15],
[8,11,10,8,13,0,12,11,10,16,6,13,12],
[12,15,16,9,11,14,0,14,11,14,9,13,16],
[13,13,14,12,11,15,12,0,14,14,12,15,16],
[12,15,14,13,14,16,15,12,0,13,11,11,14],
[11,10,10,12,15,10,12,12,13,0,11,10,13],
[14,17,14,12,14,20,17,14,15,15,0,15,17],
[11,15,16,14,15,13,13,11,15,16,11,0,13],
[8,10,11,8,11,14,10,10,12,13,9,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 10, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,12,7,14,13,15,18,16,16,17,14,12],
[10,0,17,15,18,9,15,10,14,12,10,7,10],
[14,9,0,9,17,11,10,13,13,13,13,11,11],
[19,11,17,0,20,14,15,17,19,15,13,10,14],
[12,8,9,6,0,11,12,12,10,8,11,10,8],
[13,17,15,12,15,0,13,17,14,10,15,11,10],
[11,11,16,11,14,13,0,12,13,9,15,8,8],
[8,16,13,9,14,9,14,0,14,8,15,9,8],
[10,12,13,7,16,12,13,12,0,12,12,9,7],
[10,14,13,11,18,16,17,18,14,0,17,12,11],
[9,16,13,13,15,11,11,11,14,9,0,8,8],
[12,19,15,16,16,15,18,17,17,14,18,0,15],
[14,16,15,12,18,16,18,18,19,15,18,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 11, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,16,16,15,16,17,12,10,13,14,18,17],
[13,0,12,10,15,14,18,13,12,14,14,16,16],
[10,14,0,9,15,12,18,11,12,11,9,16,13],
[10,16,17,0,19,15,17,15,16,18,14,18,19],
[11,11,11,7,0,15,14,11,12,11,16,16,13],
[10,12,14,11,11,0,12,11,17,12,17,19,13],
[9,8,8,9,12,14,0,6,11,11,12,12,12],
[14,13,15,11,15,15,20,0,17,10,11,15,12],
[16,14,14,10,14,9,15,9,0,14,14,17,12],
[13,12,15,8,15,14,15,16,12,0,15,17,19],
[12,12,17,12,10,9,14,15,12,11,0,16,11],
[8,10,10,8,10,7,14,11,9,9,10,0,10],
[9,10,13,7,13,13,14,14,14,7,15,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 12, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,12,12,14,15,14,10,12,15,18,14,14],
[13,0,11,10,13,11,10,14,9,19,16,16,16],
[14,15,0,14,14,16,16,14,11,16,14,13,15],
[14,16,12,0,15,13,13,13,18,19,15,15,15],
[12,13,12,11,0,14,12,11,11,15,9,14,13],
[11,15,10,13,12,0,14,14,13,17,16,17,14],
[12,16,10,13,14,12,0,12,9,17,17,15,12],
[16,12,12,13,15,12,14,0,11,18,16,22,13],
[14,17,15,8,15,13,17,15,0,15,16,16,15],
[11,7,10,7,11,9,9,8,11,0,16,11,8],
[8,10,12,11,17,10,9,10,10,10,0,11,12],
[12,10,13,11,12,9,11,4,10,15,15,0,13],
[12,10,11,11,13,12,14,13,11,18,14,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 13, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,16,15,21,21,10,15,26,21,21,15,15],
[16,0,16,5,11,11,21,16,26,11,11,16,16],
[10,10,0,15,21,10,10,10,15,21,21,15,15],
[11,21,11,0,11,11,21,11,26,11,11,16,16],
[5,15,5,15,0,10,10,15,15,21,21,15,15],
[5,15,16,15,16,0,10,15,26,21,11,15,5],
[16,5,16,5,16,16,0,16,16,11,11,16,16],
[11,10,16,15,11,11,10,0,26,11,11,16,16],
[0,0,11,0,11,0,10,0,0,11,11,5,0],
[5,15,5,15,5,5,15,15,15,0,11,5,5],
[5,15,5,15,5,15,15,15,15,15,0,15,15],
[11,10,11,10,11,11,10,10,21,21,11,0,0],
[11,10,11,10,11,21,10,10,26,21,11,26,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 14, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,17,15,8,18,14,15,13,9,12,17,14],
[9,0,12,8,10,17,13,8,10,9,9,13,9],
[9,14,0,9,16,14,8,13,13,7,16,13,12],
[11,18,17,0,8,14,13,14,13,9,13,11,16],
[18,16,10,18,0,16,15,17,14,12,13,18,15],
[8,9,12,12,10,0,9,11,13,7,13,14,12],
[12,13,18,13,11,17,0,11,15,13,16,14,10],
[11,18,13,12,9,15,15,0,12,10,12,16,16],
[13,16,13,13,12,13,11,14,0,10,19,11,11],
[17,17,19,17,14,19,13,16,16,0,16,17,12],
[14,17,10,13,13,13,10,14,7,10,0,13,12],
[9,13,13,15,8,12,12,10,15,9,13,0,8],
[12,17,14,10,11,14,16,10,15,14,14,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 15, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,13,15,20,8,11,12,7,10,10,9,14],
[15,0,13,5,17,13,14,13,10,14,10,14,18],
[13,13,0,9,12,14,14,12,11,10,7,11,14],
[11,21,17,0,16,17,18,15,16,16,14,17,17],
[6,9,14,10,0,10,9,9,6,10,8,9,10],
[18,13,12,9,16,0,14,16,12,13,11,13,17],
[15,12,12,8,17,12,0,9,8,8,7,13,15],
[14,13,14,11,17,10,17,0,16,9,8,10,14],
[19,16,15,10,20,14,18,10,0,12,13,14,17],
[16,12,16,10,16,13,18,17,14,0,13,13,17],
[16,16,19,12,18,15,19,18,13,13,0,12,20],
[17,12,15,9,17,13,13,16,12,13,14,0,16],
[12,8,12,9,16,9,11,12,9,9,6,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 16, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,18,11,12,13,9,17,16,13,15,14,11],
[16,0,11,13,10,17,12,13,14,10,12,11,13],
[8,15,0,12,11,17,9,18,13,11,10,14,13],
[15,13,14,0,15,15,11,18,12,19,15,18,14],
[14,16,15,11,0,14,12,17,15,13,11,9,16],
[13,9,9,11,12,0,10,13,10,11,13,13,9],
[17,14,17,15,14,16,0,20,16,13,20,18,16],
[9,13,8,8,9,13,6,0,9,9,7,12,12],
[10,12,13,14,11,16,10,17,0,9,10,13,10],
[13,16,15,7,13,15,13,17,17,0,14,17,12],
[11,14,16,11,15,13,6,19,16,12,0,14,13],
[12,15,12,8,17,13,8,14,13,9,12,0,8],
[15,13,13,12,10,17,10,14,16,14,13,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 17, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,12,13,11,13,18,12,10,12,16,11,14],
[12,0,13,12,13,11,13,13,9,10,15,10,15],
[14,13,0,16,13,13,17,15,9,13,16,12,15],
[13,14,10,0,11,13,18,14,11,12,15,10,12],
[15,13,13,15,0,14,16,15,7,12,18,10,17],
[13,15,13,13,12,0,16,13,11,13,14,13,11],
[8,13,9,8,10,10,0,11,10,10,13,10,12],
[14,13,11,12,11,13,15,0,10,9,14,11,12],
[16,17,17,15,19,15,16,16,0,19,19,13,18],
[14,16,13,14,14,13,16,17,7,0,17,11,13],
[10,11,10,11,8,12,13,12,7,9,0,10,11],
[15,16,14,16,16,13,16,15,13,15,16,0,15],
[12,11,11,14,9,15,14,14,8,13,15,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 18, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,14,10,17,17,13,15,20,15,12,17,15],
[15,0,12,8,15,16,12,15,19,14,16,18,12],
[12,14,0,12,15,14,17,18,21,16,12,18,14],
[16,18,14,0,19,23,13,24,21,20,19,21,13],
[9,11,11,7,0,8,9,17,23,13,7,15,16],
[9,10,12,3,18,0,13,18,21,12,12,15,13],
[13,14,9,13,17,13,0,21,19,14,13,18,14],
[11,11,8,2,9,8,5,0,17,10,8,9,9],
[6,7,5,5,3,5,7,9,0,10,6,11,13],
[11,12,10,6,13,14,12,16,16,0,10,23,13],
[14,10,14,7,19,14,13,18,20,16,0,15,12],
[9,8,8,5,11,11,8,17,15,3,11,0,13],
[11,14,12,13,10,13,12,17,13,13,14,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 19, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,11,13,13,14,20,18,17,16,18,19,19],
[4,0,8,12,8,8,11,7,15,15,17,15,9],
[15,18,0,13,16,11,17,17,15,21,19,16,18],
[13,14,13,0,13,9,17,14,17,17,16,13,19],
[13,18,10,13,0,14,18,18,20,17,19,18,15],
[12,18,15,17,12,0,18,16,16,16,16,18,16],
[6,15,9,9,8,8,0,8,11,11,13,13,14],
[8,19,9,12,8,10,18,0,13,18,17,11,12],
[9,11,11,9,6,10,15,13,0,18,14,14,11],
[10,11,5,9,9,10,15,8,8,0,14,14,11],
[8,9,7,10,7,10,13,9,12,12,0,16,10],
[7,11,10,13,8,8,13,15,12,12,10,0,11],
[7,17,8,7,11,10,12,14,15,15,16,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 20, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,11,8,16,15,6,10,11,10,11,10],
[16,0,12,14,16,18,20,14,14,16,15,14,11],
[16,14,0,12,13,18,16,10,13,16,13,13,10],
[15,12,14,0,13,13,13,9,13,13,14,12,14],
[18,10,13,13,0,15,17,11,13,14,14,15,13],
[10,8,8,13,11,0,13,9,8,11,12,13,12],
[11,6,10,13,9,13,0,8,8,10,16,15,15],
[20,12,16,17,15,17,18,0,14,14,18,15,14],
[16,12,13,13,13,18,18,12,0,12,17,14,12],
[15,10,10,13,12,15,16,12,14,0,15,14,13],
[16,11,13,12,12,14,10,8,9,11,0,16,15],
[15,12,13,14,11,13,11,11,12,12,10,0,13],
[16,15,16,12,13,14,11,12,14,13,11,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 21, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,21,14,18,11,22,19,14,19,16,19,19,15],
[5,0,9,13,11,11,14,13,8,10,15,12,12],
[12,17,0,20,16,21,19,17,17,21,17,18,16],
[8,13,6,0,8,11,16,12,16,16,16,17,16],
[15,15,10,18,0,19,17,15,16,14,16,19,14],
[4,15,5,15,7,0,15,12,11,15,15,18,12],
[7,12,7,10,9,11,0,12,8,8,15,14,8],
[12,13,9,14,11,14,14,0,14,13,14,17,14],
[7,18,9,10,10,15,18,12,0,17,15,18,12],
[10,16,5,10,12,11,18,13,9,0,17,11,14],
[7,11,9,10,10,11,11,12,11,9,0,14,11],
[7,14,8,9,7,8,12,9,8,15,12,0,9],
[11,14,10,10,12,14,18,12,14,12,15,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 22, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,18,10,13,18,14,10,14,18,15,13,16],
[14,0,15,13,11,15,14,14,13,19,13,13,13],
[8,11,0,8,7,15,14,10,8,16,13,9,11],
[16,13,18,0,11,21,10,12,15,20,12,11,18],
[13,15,19,15,0,19,14,14,15,19,14,16,16],
[8,11,11,5,7,0,13,10,8,12,14,11,12],
[12,12,12,16,12,13,0,12,11,19,15,8,15],
[16,12,16,14,12,16,14,0,16,20,14,8,13],
[12,13,18,11,11,18,15,10,0,20,16,10,16],
[8,7,10,6,7,14,7,6,6,0,14,6,10],
[11,13,13,14,12,12,11,12,10,12,0,11,16],
[13,13,17,15,10,15,18,18,16,20,15,0,13],
[10,13,15,8,10,14,11,13,10,16,10,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 23, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,10,13,11,11,11,9,14,13,8,17,13],
[18,0,16,14,13,13,15,14,20,18,19,20,17],
[16,10,0,17,10,15,15,16,16,16,14,16,12],
[13,12,9,0,17,12,16,12,14,11,8,15,15],
[15,13,16,9,0,17,14,19,18,16,16,16,12],
[15,13,11,14,9,0,15,13,13,20,15,17,15],
[15,11,11,10,12,11,0,11,15,13,11,19,13],
[17,12,10,14,7,13,15,0,13,17,13,16,11],
[12,6,10,12,8,13,11,13,0,16,14,15,13],
[13,8,10,15,10,6,13,9,10,0,13,16,11],
[18,7,12,18,10,11,15,13,12,13,0,20,15],
[9,6,10,11,10,9,7,10,11,10,6,0,11],
[13,9,14,11,14,11,13,15,13,15,11,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 24, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,12,11,11,9,13,7,11,10,6,10,9],
[14,0,19,13,9,13,16,10,16,14,15,13,14],
[14,7,0,6,7,6,13,8,15,10,9,9,11],
[15,13,20,0,9,14,16,11,20,16,14,13,15],
[15,17,19,17,0,16,18,15,15,14,13,18,18],
[17,13,20,12,10,0,17,11,17,15,12,12,13],
[13,10,13,10,8,9,0,10,13,8,14,9,13],
[19,16,18,15,11,15,16,0,17,14,12,9,15],
[15,10,11,6,11,9,13,9,0,12,10,10,11],
[16,12,16,10,12,11,18,12,14,0,12,13,16],
[20,11,17,12,13,14,12,14,16,14,0,14,19],
[16,13,17,13,8,14,17,17,16,13,12,0,12],
[17,12,15,11,8,13,13,11,15,10,7,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 25, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,19,17,11,17,12,12,13,10,14,15,15],
[7,0,8,9,9,8,9,9,6,6,12,10,11],
[7,18,0,9,11,9,11,8,7,9,14,9,10],
[9,17,17,0,13,11,13,10,11,10,13,16,14],
[15,17,15,13,0,17,12,18,19,14,12,20,19],
[9,18,17,15,9,0,14,8,11,10,14,13,14],
[14,17,15,13,14,12,0,15,18,9,11,14,16],
[14,17,18,16,8,18,11,0,10,10,14,14,14],
[13,20,19,15,7,15,8,16,0,8,11,15,15],
[16,20,17,16,12,16,17,16,18,0,15,17,20],
[12,14,12,13,14,12,15,12,15,11,0,14,14],
[11,16,17,10,6,13,12,12,11,9,12,0,14],
[11,15,16,12,7,12,10,12,11,6,12,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 26, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,17,11,8,15,15,17,19,15,9,15,10],
[11,0,13,3,7,7,12,13,18,16,2,13,7],
[9,13,0,9,13,13,14,15,20,18,13,15,13],
[15,23,17,0,14,17,15,15,19,20,10,19,14],
[18,19,13,12,0,18,15,21,21,22,11,19,10],
[11,19,13,9,8,0,19,15,15,19,0,15,10],
[11,14,12,11,11,7,0,16,17,17,6,14,13],
[9,13,11,11,5,11,10,0,16,14,4,13,5],
[7,8,6,7,5,11,9,10,0,9,4,4,5],
[11,10,8,6,4,7,9,12,17,0,0,10,0],
[17,24,13,16,15,26,20,22,22,26,0,16,15],
[11,13,11,7,7,11,12,13,22,16,10,0,7],
[16,19,13,12,16,16,13,21,21,26,11,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 27, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,10,15,8,12,15,11,11,12,18,12,12],
[17,0,14,15,12,16,19,18,20,14,23,16,14],
[16,12,0,16,12,16,16,14,16,18,22,14,17],
[11,11,10,0,8,16,15,12,12,16,16,12,7],
[18,14,14,18,0,11,19,17,18,17,16,15,16],
[14,10,10,10,15,0,20,12,14,14,15,18,12],
[11,7,10,11,7,6,0,12,10,11,11,9,11],
[15,8,12,14,9,14,14,0,12,14,22,11,10],
[15,6,10,14,8,12,16,14,0,14,18,9,17],
[14,12,8,10,9,12,15,12,12,0,17,9,10],
[8,3,4,10,10,11,15,4,8,9,0,10,11],
[14,10,12,14,11,8,17,15,17,17,16,0,12],
[14,12,9,19,10,14,15,16,9,16,15,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 28, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,12,9,19,5,7,16,14,19,19,12,11],
[10,0,12,12,16,5,7,15,17,11,15,12,11],
[14,14,0,6,16,6,8,20,14,13,23,10,16],
[17,14,20,0,14,14,11,14,17,19,19,12,15],
[7,10,10,12,0,3,10,12,10,9,12,2,8],
[21,21,20,12,23,0,18,23,17,22,23,13,22],
[19,19,18,15,16,8,0,19,17,19,15,12,11],
[10,11,6,12,14,3,7,0,10,15,11,9,8],
[12,9,12,9,16,9,9,16,0,12,15,9,12],
[7,15,13,7,17,4,7,11,14,0,17,7,10],
[7,11,3,7,14,3,11,15,11,9,0,11,10],
[14,14,16,14,24,13,14,17,17,19,15,0,11],
[15,15,10,11,18,4,15,18,14,16,16,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 29, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,10,21,23,13,9,13,17,20,17,16,17],
[11,0,10,17,18,12,9,14,11,14,18,16,11],
[16,16,0,16,17,15,12,16,15,16,15,18,19],
[5,9,10,0,13,10,9,11,8,7,4,13,12],
[3,8,9,13,0,8,10,5,10,9,8,13,11],
[13,14,11,16,18,0,12,13,17,15,7,19,15],
[17,17,14,17,16,14,0,16,13,14,15,20,17],
[13,12,10,15,21,13,10,0,13,17,11,13,16],
[9,15,11,18,16,9,13,13,0,14,13,14,15],
[6,12,10,19,17,11,12,9,12,0,12,13,11],
[9,8,11,22,18,19,11,15,13,14,0,15,17],
[10,10,8,13,13,7,6,13,12,13,11,0,15],
[9,15,7,14,15,11,9,10,11,15,9,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 30, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,6,5,5,12,12,13,5,10,8,9,9],
[19,0,13,9,11,17,20,12,12,17,11,10,15],
[20,13,0,11,9,17,16,14,11,14,14,14,12],
[21,17,15,0,12,18,19,17,14,19,15,13,19],
[21,15,17,14,0,19,19,14,11,13,11,14,11],
[14,9,9,8,7,0,13,11,10,12,9,11,12],
[14,6,10,7,7,13,0,13,11,8,9,12,6],
[13,14,12,9,12,15,13,0,8,11,12,12,10],
[21,14,15,12,15,16,15,18,0,11,15,12,11],
[16,9,12,7,13,14,18,15,15,0,12,13,11],
[18,15,12,11,15,17,17,14,11,14,0,13,13],
[17,16,12,13,12,15,14,14,14,13,13,0,11],
[17,11,14,7,15,14,20,16,15,15,13,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 31, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,14,18,8,18,16,17,17,15,17,18,11],
[9,0,8,12,9,14,12,15,11,13,8,9,13],
[12,18,0,13,13,19,9,12,15,15,18,16,12],
[8,14,13,0,8,13,16,18,10,15,14,10,12],
[18,17,13,18,0,20,13,16,19,15,17,16,17],
[8,12,7,13,6,0,9,11,5,11,12,10,11],
[10,14,17,10,13,17,0,12,18,11,18,12,15],
[9,11,14,8,10,15,14,0,15,12,17,12,11],
[9,15,11,16,7,21,8,11,0,12,14,14,12],
[11,13,11,11,11,15,15,14,14,0,16,13,9],
[9,18,8,12,9,14,8,9,12,10,0,15,13],
[8,17,10,16,10,16,14,14,12,13,11,0,12],
[15,13,14,14,9,15,11,15,14,17,13,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 32, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,3,12,9,6,3,6,11,10,3,9,4],
[16,0,9,13,9,16,10,9,13,13,10,13,7],
[23,17,0,17,15,16,8,11,17,20,5,14,10],
[14,13,9,0,15,12,16,7,20,16,10,16,7],
[17,17,11,11,0,19,8,14,14,11,11,11,7],
[20,10,10,14,7,0,10,10,11,13,11,13,8],
[23,16,18,10,18,16,0,15,17,22,10,15,16],
[20,17,15,19,12,16,11,0,17,20,10,13,7],
[15,13,9,6,12,15,9,9,0,16,12,9,9],
[16,13,6,10,15,13,4,6,10,0,4,10,10],
[23,16,21,16,15,15,16,16,14,22,0,15,13],
[17,13,12,10,15,13,11,13,17,16,11,0,10],
[22,19,16,19,19,18,10,19,17,16,13,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 33, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,18,16,14,13,17,7,17,13,12,17,14],
[15,0,10,13,13,10,16,10,9,12,13,14,10],
[8,16,0,9,14,8,11,10,5,14,8,9,9],
[10,13,17,0,14,13,18,10,14,14,13,13,12],
[12,13,12,12,0,10,10,9,8,8,4,8,10],
[13,16,18,13,16,0,9,14,16,14,12,8,13],
[9,10,15,8,16,17,0,8,14,17,10,14,8],
[19,16,16,16,17,12,18,0,15,15,16,15,18],
[9,17,21,12,18,10,12,11,0,14,10,14,15],
[13,14,12,12,18,12,9,11,12,0,11,10,8],
[14,13,18,13,22,14,16,10,16,15,0,14,16],
[9,12,17,13,18,18,12,11,12,16,12,0,13],
[12,16,17,14,16,13,18,8,11,18,10,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 34, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,23,17,11,14,17,18,14,13,15,18,17,13],
[3,0,10,12,7,4,7,8,5,2,7,4,8],
[9,16,0,15,10,12,12,15,14,16,10,11,12],
[15,14,11,0,13,10,12,14,14,11,18,12,13],
[12,19,16,13,0,11,20,14,13,13,12,13,11],
[9,22,14,16,15,0,13,11,17,15,15,11,12],
[8,19,14,14,6,13,0,10,13,10,14,14,13],
[12,18,11,12,12,15,16,0,15,14,15,13,9],
[13,21,12,12,13,9,13,11,0,11,16,16,15],
[11,24,10,15,13,11,16,12,15,0,15,12,11],
[8,19,16,8,14,11,12,11,10,11,0,9,11],
[9,22,15,14,13,15,12,13,10,14,17,0,15],
[13,18,14,13,15,14,13,17,11,15,15,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 35, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,11,22,16,12,14,17,10,15,11,14,13],
[14,0,13,21,13,12,12,12,11,13,8,11,13],
[15,13,0,17,15,17,17,18,12,14,11,14,18],
[4,5,9,0,4,6,7,6,1,11,2,2,9],
[10,13,11,22,0,10,13,13,8,16,11,8,13],
[14,14,9,20,16,0,15,16,15,17,16,16,17],
[12,14,9,19,13,11,0,16,14,15,13,13,15],
[9,14,8,20,13,10,10,0,10,15,12,14,13],
[16,15,14,25,18,11,12,16,0,16,13,15,13],
[11,13,12,15,10,9,11,11,10,0,7,8,12],
[15,18,15,24,15,10,13,14,13,19,0,18,16],
[12,15,12,24,18,10,13,12,11,18,8,0,13],
[13,13,8,17,13,9,11,13,13,14,10,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 36, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,13,7,13,11,9,12,12,10,11,13,9],
[16,0,13,12,18,15,13,15,13,11,14,15,11],
[13,13,0,12,17,11,12,19,15,13,17,14,12],
[19,14,14,0,15,15,13,14,16,16,14,18,12],
[13,8,9,11,0,13,10,10,13,12,13,12,9],
[15,11,15,11,13,0,9,14,12,13,10,14,11],
[17,13,14,13,16,17,0,14,13,15,17,17,16],
[14,11,7,12,16,12,12,0,12,10,13,12,9],
[14,13,11,10,13,14,13,14,0,12,13,13,11],
[16,15,13,10,14,13,11,16,14,0,16,12,12],
[15,12,9,12,13,16,9,13,13,10,0,15,10],
[13,11,12,8,14,12,9,14,13,14,11,0,11],
[17,15,14,14,17,15,10,17,15,14,16,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 37, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,14,12,12,19,14,12,16,13,11,16,15],
[12,0,10,7,9,11,10,13,11,13,8,13,11],
[12,16,0,13,15,18,15,15,17,16,10,20,18],
[14,19,13,0,15,17,14,14,17,15,11,15,16],
[14,17,11,11,0,16,16,16,15,14,13,13,15],
[7,15,8,9,10,0,10,11,13,13,9,11,12],
[12,16,11,12,10,16,0,14,15,14,10,14,14],
[14,13,11,12,10,15,12,0,12,13,12,14,14],
[10,15,9,9,11,13,11,14,0,12,7,13,14],
[13,13,10,11,12,13,12,13,14,0,8,14,16],
[15,18,16,15,13,17,16,14,19,18,0,17,18],
[10,13,6,11,13,15,12,12,13,12,9,0,16],
[11,15,8,10,11,14,12,12,12,10,8,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 38, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,11,20,20,18,20,20,20,20,20,20,20],
[6,0,15,16,2,17,17,22,24,9,18,13,15],
[15,11,0,9,11,15,11,18,11,18,20,16,9],
[6,10,17,0,8,8,10,24,10,17,20,15,15],
[6,24,15,18,0,24,24,24,24,15,18,15,24],
[8,9,11,18,2,0,11,18,20,11,20,9,9],
[6,9,15,16,2,15,0,24,24,11,18,13,13],
[6,4,8,2,2,8,2,0,10,11,2,6,2],
[6,2,15,16,2,6,2,16,0,11,18,7,7],
[6,17,8,9,11,15,15,15,15,0,11,15,15],
[6,8,6,6,8,6,8,24,8,15,0,6,6],
[6,13,10,11,11,17,13,20,19,11,20,0,11],
[6,11,17,11,2,17,13,24,19,11,20,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 39, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,8,9,8,14,8,8,8,16,14,8,23],
[17,0,15,19,8,18,19,12,6,16,21,19,25],
[18,11,0,9,9,16,19,9,7,17,22,5,17],
[17,7,17,0,6,21,21,10,3,15,17,7,21],
[18,18,17,20,0,18,19,10,3,13,22,20,25],
[12,8,10,5,8,0,10,4,4,15,11,11,21],
[18,7,7,5,7,16,0,9,3,17,11,5,17],
[18,14,17,16,16,22,17,0,13,16,24,15,21],
[18,20,19,23,23,22,23,13,0,16,24,23,23],
[10,10,9,11,13,11,9,10,10,0,13,11,17],
[12,5,4,9,4,15,15,2,2,13,0,5,19],
[18,7,21,19,6,15,21,11,3,15,21,0,25],
[3,1,9,5,1,5,9,5,3,9,7,1,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 40, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,4,9,5,6,11,6,6,9,10,10,9],
[19,0,11,13,12,12,7,13,10,16,14,17,13],
[22,15,0,12,17,13,11,12,9,19,19,16,14],
[17,13,14,0,15,10,11,9,7,17,13,11,12],
[21,14,9,11,0,9,13,12,6,16,15,13,11],
[20,14,13,16,17,0,16,14,14,14,11,20,16],
[15,19,15,15,13,10,0,14,10,18,16,14,11],
[20,13,14,17,14,12,12,0,10,13,12,21,14],
[20,16,17,19,20,12,16,16,0,18,16,17,20],
[17,10,7,9,10,12,8,13,8,0,10,12,8],
[16,12,7,13,11,15,10,14,10,16,0,15,13],
[16,9,10,15,13,6,12,5,9,14,11,0,11],
[17,13,12,14,15,10,15,12,6,18,13,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 41, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,4,13,4,8,8,14,7,14,4,4,8],
[18,0,12,18,13,11,13,22,13,17,9,4,14],
[22,14,0,18,9,7,17,22,9,14,15,14,10],
[13,8,8,0,8,4,8,13,7,8,13,8,4],
[22,13,17,18,0,7,17,22,13,13,22,10,13],
[18,15,19,22,19,0,10,23,13,14,19,14,10],
[18,13,9,18,9,16,0,22,12,19,9,9,13],
[12,4,4,13,4,3,4,0,7,10,9,4,4],
[19,13,17,19,13,13,14,19,0,19,17,13,9],
[12,9,12,18,13,12,7,16,7,0,9,4,13],
[22,17,11,13,4,7,17,17,9,17,0,10,10],
[22,22,12,18,16,12,17,22,13,22,16,0,18],
[18,12,16,22,13,16,13,22,17,13,16,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 42, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,12,6,18,15,11,11,11,14,15,15,14],
[13,0,19,12,18,18,18,21,12,7,12,14,18],
[14,7,0,12,16,16,18,14,14,9,15,17,17],
[20,14,14,0,24,18,10,16,16,13,17,15,18],
[8,8,10,2,0,10,9,8,3,8,10,13,10],
[11,8,10,8,16,0,9,11,7,7,10,15,10],
[15,8,8,16,17,17,0,11,8,11,18,18,20],
[15,5,12,10,18,15,15,0,9,7,13,15,20],
[15,14,12,10,23,19,18,17,0,6,19,23,24],
[12,19,17,13,18,19,15,19,20,0,19,20,18],
[11,14,11,9,16,16,8,13,7,7,0,12,12],
[11,12,9,11,13,11,8,11,3,6,14,0,16],
[12,8,9,8,16,16,6,6,2,8,14,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 43, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,11,18,14,15,13,16,12,10,14,13,13],
[8,0,9,13,10,13,8,13,9,7,13,9,12],
[15,17,0,16,14,18,16,16,13,14,14,11,13],
[8,13,10,0,10,11,12,10,11,7,10,9,11],
[12,16,12,16,0,15,14,15,13,9,14,12,13],
[11,13,8,15,11,0,12,13,11,10,13,11,11],
[13,18,10,14,12,14,0,15,11,10,11,9,10],
[10,13,10,16,11,13,11,0,9,9,14,8,13],
[14,17,13,15,13,15,15,17,0,10,14,16,9],
[16,19,12,19,17,16,16,17,16,0,18,14,15],
[12,13,12,16,12,13,15,12,12,8,0,10,11],
[13,17,15,17,14,15,17,18,10,12,16,0,12],
[13,14,13,15,13,15,16,13,17,11,15,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 44, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,12,14,18,13,11,14,13,11,12,16,16],
[13,0,12,15,12,10,11,13,10,13,13,17,16],
[14,14,0,16,15,13,14,15,16,12,10,13,17],
[12,11,10,0,16,11,15,13,15,14,10,14,17],
[8,14,11,10,0,5,11,11,11,7,5,13,12],
[13,16,13,15,21,0,13,14,13,13,12,18,18],
[15,15,12,11,15,13,0,13,10,12,10,15,18],
[12,13,11,13,15,12,13,0,12,10,12,14,16],
[13,16,10,11,15,13,16,14,0,11,8,14,14],
[15,13,14,12,19,13,14,16,15,0,8,15,17],
[14,13,16,16,21,14,16,14,18,18,0,17,21],
[10,9,13,12,13,8,11,12,12,11,9,0,10],
[10,10,9,9,14,8,8,10,12,9,5,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 45, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,10,17,11,15,16,13,10,17,16,13,12],
[14,0,7,14,10,11,12,11,11,12,10,8,8],
[16,19,0,16,12,12,17,11,11,16,13,12,11],
[9,12,10,0,9,11,10,10,10,14,12,9,9],
[15,16,14,17,0,14,16,18,16,19,15,14,13],
[11,15,14,15,12,0,11,15,12,15,13,14,10],
[10,14,9,16,10,15,0,9,13,15,13,11,10],
[13,15,15,16,8,11,17,0,13,16,15,13,11],
[16,15,15,16,10,14,13,13,0,14,15,11,8],
[9,14,10,12,7,11,11,10,12,0,13,8,6],
[10,16,13,14,11,13,13,11,11,13,0,10,8],
[13,18,14,17,12,12,15,13,15,18,16,0,13],
[14,18,15,17,13,16,16,15,18,20,18,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 46, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,9,9,12,10,10,9,10,5,16,10],
[16,0,13,8,8,15,11,10,12,11,7,13,12],
[16,13,0,10,10,12,14,11,12,11,13,12,14],
[17,18,16,0,15,17,17,15,13,17,16,18,17],
[17,18,16,11,0,13,16,8,11,13,12,18,15],
[14,11,14,9,13,0,10,8,10,7,6,16,8],
[16,15,12,9,10,16,0,10,9,11,7,12,12],
[16,16,15,11,18,18,16,0,13,15,13,18,16],
[17,14,14,13,15,16,17,13,0,11,14,16,14],
[16,15,15,9,13,19,15,11,15,0,12,14,12],
[21,19,13,10,14,20,19,13,12,14,0,18,17],
[10,13,14,8,8,10,14,8,10,12,8,0,10],
[16,14,12,9,11,18,14,10,12,14,9,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 47, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,9,11,13,12,15,13,15,11,16,16,12],
[13,0,10,11,9,16,12,12,10,9,15,10,16],
[17,16,0,12,15,18,15,12,17,15,19,14,15],
[15,15,14,0,15,14,17,10,12,11,19,15,17],
[13,17,11,11,0,16,16,15,14,10,14,12,17],
[14,10,8,12,10,0,10,14,11,12,15,15,15],
[11,14,11,9,10,16,0,17,13,13,16,10,16],
[13,14,14,16,11,12,9,0,10,11,23,11,16],
[11,16,9,14,12,15,13,16,0,13,15,13,16],
[15,17,11,15,16,14,13,15,13,0,18,16,18],
[10,11,7,7,12,11,10,3,11,8,0,7,10],
[10,16,12,11,14,11,16,15,13,10,19,0,18],
[14,10,11,9,9,11,10,10,10,8,16,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 48, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,18,19,13,18,16,15,18,16,19,19,18],
[4,0,7,8,6,10,9,8,5,11,11,11,10],
[8,19,0,17,13,14,13,13,10,16,16,17,17],
[7,18,9,0,12,12,8,10,8,14,10,13,14],
[13,20,13,14,0,15,16,13,13,14,15,15,17],
[8,16,12,14,11,0,8,11,11,16,15,17,13],
[10,17,13,18,10,18,0,15,14,17,14,19,19],
[11,18,13,16,13,15,11,0,15,16,14,16,17],
[8,21,16,18,13,15,12,11,0,17,13,16,15],
[10,15,10,12,12,10,9,10,9,0,11,9,12],
[7,15,10,16,11,11,12,12,13,15,0,13,9],
[7,15,9,13,11,9,7,10,10,17,13,0,14],
[8,16,9,12,9,13,7,9,11,14,17,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 49, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,10,13,9,10,10,13,10,10,6,13,9],
[14,0,10,15,13,10,14,14,10,11,7,12,8],
[16,16,0,11,12,9,11,14,13,13,10,14,11],
[13,11,15,0,10,12,10,18,11,12,10,13,13],
[17,13,14,16,0,17,15,16,16,12,12,18,14],
[16,16,17,14,9,0,12,14,9,12,7,10,15],
[16,12,15,16,11,14,0,13,15,11,9,17,15],
[13,12,12,8,10,12,13,0,9,14,10,12,10],
[16,16,13,15,10,17,11,17,0,14,16,18,15],
[16,15,13,14,14,14,15,12,12,0,10,16,11],
[20,19,16,16,14,19,17,16,10,16,0,19,14],
[13,14,12,13,8,16,9,14,8,10,7,0,14],
[17,18,15,13,12,11,11,16,11,15,12,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 50, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,14,13,14,19,9,17,13,10,14,14,17],
[14,0,13,13,20,19,12,13,12,18,19,7,15],
[12,13,0,16,14,18,8,10,15,12,15,5,12],
[13,13,10,0,14,13,10,9,13,9,16,8,12],
[12,6,12,12,0,12,4,9,10,8,12,8,13],
[7,7,8,13,14,0,5,9,9,3,13,5,9],
[17,14,18,16,22,21,0,16,15,11,20,13,18],
[9,13,16,17,17,17,10,0,10,8,16,7,12],
[13,14,11,13,16,17,11,16,0,9,19,9,19],
[16,8,14,17,18,23,15,18,17,0,16,8,10],
[12,7,11,10,14,13,6,10,7,10,0,8,8],
[12,19,21,18,18,21,13,19,17,18,18,0,15],
[9,11,14,14,13,17,8,14,7,16,18,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 51, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,21,21,20,21,14,19,26,16,18,9,19],
[0,0,7,10,18,19,12,12,19,1,13,7,7],
[5,19,0,14,13,26,5,14,19,13,11,9,5],
[5,16,12,0,15,21,12,14,16,15,18,9,7],
[6,8,13,11,0,20,13,15,6,8,13,8,6],
[5,7,0,5,6,0,5,14,6,5,6,7,0],
[12,14,21,14,13,21,0,20,14,9,17,15,11],
[7,14,12,12,11,12,6,0,12,7,17,6,11],
[0,7,7,10,20,20,12,14,0,2,13,9,0],
[10,25,13,11,18,21,17,19,24,0,18,12,12],
[8,13,15,8,13,20,9,9,13,8,0,10,8],
[17,19,17,17,18,19,11,20,17,14,16,0,16],
[7,19,21,19,20,26,15,15,26,14,18,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 52, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,13,15,10,8,14,11,11,18,11,8,9],
[15,0,13,15,14,12,12,15,15,16,14,15,14],
[13,13,0,14,14,10,12,15,16,19,14,15,13],
[11,11,12,0,11,8,11,14,11,13,9,11,11],
[16,12,12,15,0,12,15,14,15,17,14,16,10],
[18,14,16,18,14,0,14,11,15,16,13,13,11],
[12,14,14,15,11,12,0,14,15,21,16,12,13],
[15,11,11,12,12,15,12,0,13,15,11,11,12],
[15,11,10,15,11,11,11,13,0,13,12,9,13],
[8,10,7,13,9,10,5,11,13,0,12,7,10],
[15,12,12,17,12,13,10,15,14,14,0,13,15],
[18,11,11,15,10,13,14,15,17,19,13,0,12],
[17,12,13,15,16,15,13,14,13,16,11,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 53, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,19,16,10,15,10,18,16,16,15,15,16,15],
[7,0,11,10,15,11,15,16,15,11,9,12,14],
[10,15,0,11,10,10,13,11,13,11,14,9,9],
[16,16,15,0,13,15,21,13,21,17,15,18,18],
[11,11,16,13,0,14,16,13,17,12,8,12,15],
[16,15,16,11,12,0,16,17,13,11,13,13,18],
[8,11,13,5,10,10,0,7,12,15,7,11,10],
[10,10,15,13,13,9,19,0,15,14,11,14,18],
[10,11,13,5,9,13,14,11,0,12,10,14,11],
[11,15,15,9,14,15,11,12,14,0,10,10,13],
[11,17,12,11,18,13,19,15,16,16,0,14,15],
[10,14,17,8,14,13,15,12,12,16,12,0,14],
[11,12,17,8,11,8,16,8,15,13,11,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 54, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,6,19,6,13,6,16,11,6,11,6,8],
[20,0,20,15,7,12,20,12,24,16,20,12,18],
[20,6,0,15,7,7,7,18,16,16,10,7,13],
[7,11,11,0,8,12,13,16,11,11,11,7,5],
[20,19,19,18,0,20,13,16,19,19,13,13,13],
[13,14,19,14,6,0,14,16,19,11,19,6,8],
[20,6,19,13,13,12,0,16,19,16,16,7,13],
[10,14,8,10,10,10,10,0,19,14,13,10,8],
[15,2,10,15,7,7,7,7,0,5,7,7,13],
[20,10,10,15,7,15,10,12,21,0,20,2,8],
[15,6,16,15,13,7,10,13,19,6,0,2,8],
[20,14,19,19,13,20,19,16,19,24,24,0,13],
[18,8,13,21,13,18,13,18,13,18,18,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 55, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,11,13,15,20,15,13,16,12,13,16,14],
[16,0,13,15,16,18,10,16,19,17,8,17,14],
[15,13,0,11,12,20,15,14,20,15,9,13,11],
[13,11,15,0,14,20,14,11,19,10,12,15,13],
[11,10,14,12,0,17,10,9,15,14,5,13,10],
[6,8,6,6,9,0,6,11,15,7,9,11,8],
[11,16,11,12,16,20,0,19,20,12,13,16,13],
[13,10,12,15,17,15,7,0,19,17,11,16,11],
[10,7,6,7,11,11,6,7,0,10,4,11,6],
[14,9,11,16,12,19,14,9,16,0,6,14,9],
[13,18,17,14,21,17,13,15,22,20,0,22,20],
[10,9,13,11,13,15,10,10,15,12,4,0,11],
[12,12,15,13,16,18,13,15,20,17,6,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 56, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,15,17,19,13,15,9,15,12,23,11,12],
[9,0,15,12,9,7,12,9,13,7,16,9,11],
[11,11,0,18,16,8,14,12,18,9,17,17,16],
[9,14,8,0,16,9,11,14,8,8,19,12,13],
[7,17,10,10,0,4,12,11,11,9,20,16,7],
[13,19,18,17,22,0,9,15,14,11,23,19,15],
[11,14,12,15,14,17,0,9,14,10,26,12,13],
[17,17,14,12,15,11,17,0,18,14,25,15,14],
[11,13,8,18,15,12,12,8,0,5,16,14,12],
[14,19,17,18,17,15,16,12,21,0,21,17,15],
[3,10,9,7,6,3,0,1,10,5,0,9,5],
[15,17,9,14,10,7,14,11,12,9,17,0,8],
[14,15,10,13,19,11,13,12,14,11,21,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 57, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,13,10,11,14,12,9,11,11,13,7,12],
[14,0,14,11,17,14,12,11,16,16,15,8,14],
[13,12,0,15,13,14,15,11,16,15,15,9,14],
[16,15,11,0,12,19,16,12,17,14,14,10,16],
[15,9,13,14,0,16,10,9,15,12,13,10,14],
[12,12,12,7,10,0,13,13,16,16,12,10,12],
[14,14,11,10,16,13,0,12,15,16,16,10,13],
[17,15,15,14,17,13,14,0,19,19,17,14,15],
[15,10,10,9,11,10,11,7,0,11,8,8,12],
[15,10,11,12,14,10,10,7,15,0,11,12,10],
[13,11,11,12,13,14,10,9,18,15,0,10,12],
[19,18,17,16,16,16,16,12,18,14,16,0,18],
[14,12,12,10,12,14,13,11,14,16,14,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 58, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,15,13,12,11,16,8,11,12,11,17,9],
[12,0,14,12,10,13,15,11,12,12,11,16,6],
[11,12,0,10,4,11,14,6,6,17,8,9,7],
[13,14,16,0,15,14,16,7,10,15,12,17,6],
[14,16,22,11,0,14,18,10,9,16,9,12,6],
[15,13,15,12,12,0,13,12,14,10,12,17,7],
[10,11,12,10,8,13,0,9,9,12,9,14,6],
[18,15,20,19,16,14,17,0,16,17,13,20,11],
[15,14,20,16,17,12,17,10,0,14,11,16,9],
[14,14,9,11,10,16,14,9,12,0,7,16,5],
[15,15,18,14,17,14,17,13,15,19,0,23,13],
[9,10,17,9,14,9,12,6,10,10,3,0,7],
[17,20,19,20,20,19,20,15,17,21,13,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 59, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,18,15,23,15,23,23,22,18,23,11,14],
[0,0,13,5,13,0,13,5,12,13,13,10,5],
[8,13,0,13,21,6,6,10,20,10,19,10,10],
[11,21,13,0,17,6,19,14,20,9,19,10,10],
[3,13,5,9,0,5,10,5,7,0,18,10,10],
[11,26,20,20,21,0,22,22,15,20,22,18,25],
[3,13,20,7,16,4,0,9,15,7,18,10,17],
[3,21,16,12,21,4,17,0,15,15,17,13,13],
[4,14,6,6,19,11,11,11,0,6,19,11,10],
[8,13,16,17,26,6,19,11,20,0,19,10,10],
[3,13,7,7,8,4,8,9,7,7,0,13,8],
[15,16,16,16,16,8,16,13,15,16,13,0,15],
[12,21,16,16,16,1,9,13,16,16,18,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 60, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,16,12,13,11,13,12,11,12,11,13,6],
[12,0,20,11,8,8,11,12,10,11,9,13,10],
[10,6,0,7,5,7,8,10,7,7,8,6,9],
[14,15,19,0,12,12,12,16,13,14,13,13,12],
[13,18,21,14,0,15,16,14,16,15,14,16,13],
[15,18,19,14,11,0,15,16,14,15,11,14,13],
[13,15,18,14,10,11,0,14,12,13,11,17,10],
[14,14,16,10,12,10,12,0,11,13,10,13,9],
[15,16,19,13,10,12,14,15,0,13,9,15,11],
[14,15,19,12,11,11,13,13,13,0,12,15,13],
[15,17,18,13,12,15,15,16,17,14,0,17,10],
[13,13,20,13,10,12,9,13,11,11,9,0,8],
[20,16,17,14,13,13,16,17,15,13,16,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 61, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,13,9,12,11,11,9,14,14,13,12,12],
[18,0,14,13,11,21,17,13,20,21,19,12,16],
[13,12,0,12,10,17,18,11,17,17,18,14,14],
[17,13,14,0,14,20,16,11,16,22,18,13,13],
[14,15,16,12,0,16,13,10,14,16,16,9,14],
[15,5,9,6,10,0,12,7,14,16,14,11,11],
[15,9,8,10,13,14,0,11,16,18,17,10,14],
[17,13,15,15,16,19,15,0,18,21,18,11,16],
[12,6,9,10,12,12,10,8,0,13,12,11,11],
[12,5,9,4,10,10,8,5,13,0,15,7,7],
[13,7,8,8,10,12,9,8,14,11,0,10,12],
[14,14,12,13,17,15,16,15,15,19,16,0,15],
[14,10,12,13,12,15,12,10,15,19,14,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 62, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,11,23,11,23,11,11,14,11,0,0,11],
[14,0,14,26,11,26,14,14,14,11,3,3,14],
[15,12,0,15,12,15,15,15,15,12,12,15,15],
[3,0,11,0,11,3,11,0,3,11,0,0,11],
[15,15,14,15,0,15,3,3,15,0,15,3,14],
[3,0,11,23,11,0,11,11,3,11,0,0,11],
[15,12,11,15,23,15,0,12,15,12,12,15,11],
[15,12,11,26,23,15,14,0,15,11,12,3,14],
[12,12,11,23,11,23,11,11,0,11,12,0,11],
[15,15,14,15,26,15,14,15,15,0,15,3,14],
[26,23,14,26,11,26,14,14,14,11,0,14,14],
[26,23,11,26,23,26,11,23,26,23,12,0,11],
[15,12,11,15,12,15,15,12,15,12,12,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 63, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,16,15,9,17,16,15,16,14,12,15,13],
[12,0,24,15,17,15,15,19,25,15,14,19,17],
[10,2,0,15,8,10,6,13,16,15,6,7,12],
[11,11,11,0,12,11,10,10,12,11,12,10,10],
[17,9,18,14,0,8,8,12,19,14,14,8,14],
[9,11,16,15,18,0,12,11,17,10,12,7,16],
[10,11,20,16,18,14,0,20,11,10,11,17,17],
[11,7,13,16,14,15,6,0,17,16,12,7,11],
[10,1,10,14,7,9,15,9,0,10,7,14,12],
[12,11,11,15,12,16,16,10,16,0,15,15,16],
[14,12,20,14,12,14,15,14,19,11,0,14,17],
[11,7,19,16,18,19,9,19,12,11,12,0,10],
[13,9,14,16,12,10,9,15,14,10,9,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 64, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,9,14,12,10,7,9,8,7,16,10,8],
[18,0,9,15,14,15,11,15,18,11,21,13,19],
[17,17,0,14,15,16,8,17,16,14,20,15,17],
[12,11,12,0,12,13,10,14,16,16,17,9,13],
[14,12,11,14,0,9,11,14,12,9,16,8,12],
[16,11,10,13,17,0,13,18,11,18,25,17,14],
[19,15,18,16,15,13,0,18,16,13,19,15,15],
[17,11,9,12,12,8,8,0,12,7,14,6,10],
[18,8,10,10,14,15,10,14,0,13,19,14,16],
[19,15,12,10,17,8,13,19,13,0,17,15,14],
[10,5,6,9,10,1,7,12,7,9,0,4,9],
[16,13,11,17,18,9,11,20,12,11,22,0,12],
[18,7,9,13,14,12,11,16,10,12,17,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 65, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,11,16,17,16,16,20,21,12,26,8,6],
[10,0,6,13,17,10,17,15,12,10,16,3,12],
[15,20,0,13,17,15,16,21,21,16,21,12,15],
[10,13,13,0,5,13,13,9,14,14,19,10,8],
[9,9,9,21,0,9,9,18,15,9,14,7,4],
[10,16,11,13,17,0,16,14,12,10,21,8,8],
[10,9,10,13,17,10,0,15,12,9,19,12,5],
[6,11,5,17,8,12,11,0,7,5,17,3,12],
[5,14,5,12,11,14,14,19,0,4,14,8,9],
[14,16,10,12,17,16,17,21,22,0,20,17,11],
[0,10,5,7,12,5,7,9,12,6,0,8,2],
[18,23,14,16,19,18,14,23,18,9,18,0,9],
[20,14,11,18,22,18,21,14,17,15,24,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 66, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,16,13,10,12,12,13,10,11,19,13,13],
[14,0,18,15,11,13,10,15,9,13,15,12,12],
[10,8,0,12,11,9,8,12,7,9,13,13,8],
[13,11,14,0,13,16,10,12,13,12,15,12,14],
[16,15,15,13,0,13,14,18,13,12,13,13,15],
[14,13,17,10,13,0,14,15,12,11,15,14,15],
[14,16,18,16,12,12,0,15,8,15,17,13,16],
[13,11,14,14,8,11,11,0,8,8,14,9,11],
[16,17,19,13,13,14,18,18,0,12,19,18,16],
[15,13,17,14,14,15,11,18,14,0,17,10,13],
[7,11,13,11,13,11,9,12,7,9,0,10,11],
[13,14,13,14,13,12,13,17,8,16,16,0,13],
[13,14,18,12,11,11,10,15,10,13,15,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 67, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,17,14,15,12,15,13,14,12,15,14,12],
[11,0,12,14,11,11,12,11,11,10,15,15,8],
[9,14,0,11,9,10,14,13,11,8,14,15,7],
[12,12,15,0,14,10,12,9,7,8,15,11,8],
[11,15,17,12,0,11,15,12,11,10,13,11,12],
[14,15,16,16,15,0,13,12,12,9,19,13,14],
[11,14,12,14,11,13,0,9,10,10,15,11,12],
[13,15,13,17,14,14,17,0,17,17,16,17,11],
[12,15,15,19,15,14,16,9,0,15,16,16,11],
[14,16,18,18,16,17,16,9,11,0,18,18,11],
[11,11,12,11,13,7,11,10,10,8,0,11,9],
[12,11,11,15,15,13,15,9,10,8,15,0,8],
[14,18,19,18,14,12,14,15,15,15,17,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 68, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,12,11,11,14,11,14,13,13,12,14,16],
[18,0,14,15,13,12,15,16,17,15,15,18,13],
[14,12,0,11,9,14,17,11,14,14,15,15,12],
[15,11,15,0,10,11,14,11,18,17,14,14,13],
[15,13,17,16,0,17,19,16,15,11,14,14,17],
[12,14,12,15,9,0,13,12,13,13,15,14,11],
[15,11,9,12,7,13,0,15,13,15,12,15,17],
[12,10,15,15,10,14,11,0,15,14,16,15,15],
[13,9,12,8,11,13,13,11,0,15,10,15,16],
[13,11,12,9,15,13,11,12,11,0,15,15,15],
[14,11,11,12,12,11,14,10,16,11,0,14,13],
[12,8,11,12,12,12,11,11,11,11,12,0,15],
[10,13,14,13,9,15,9,11,10,11,13,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 69, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,18,15,21,16,10,19,19,15,17,14,14],
[9,0,15,9,12,14,10,15,14,13,15,10,13],
[8,11,0,4,15,10,7,13,11,6,12,13,5],
[11,17,22,0,16,15,10,15,19,13,13,12,16],
[5,14,11,10,0,12,8,12,9,6,9,10,8],
[10,12,16,11,14,0,11,12,14,5,14,13,12],
[16,16,19,16,18,15,0,18,20,12,19,18,14],
[7,11,13,11,14,14,8,0,15,10,12,10,11],
[7,12,15,7,17,12,6,11,0,3,15,12,8],
[11,13,20,13,20,21,14,16,23,0,18,15,14],
[9,11,14,13,17,12,7,14,11,8,0,11,11],
[12,16,13,14,16,13,8,16,14,11,15,0,10],
[12,13,21,10,18,14,12,15,18,12,15,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 70, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,16,21,18,9,15,11,16,15,14,16,6],
[13,0,16,17,15,6,11,14,15,12,11,12,14],
[10,10,0,16,3,7,12,5,15,8,6,7,11],
[5,9,10,0,9,4,2,6,12,8,6,5,6],
[8,11,23,17,0,9,15,9,15,8,13,10,11],
[17,20,19,22,17,0,17,16,25,17,15,15,12],
[11,15,14,24,11,9,0,13,17,14,13,7,9],
[15,12,21,20,17,10,13,0,13,15,13,12,13],
[10,11,11,14,11,1,9,13,0,12,12,5,5],
[11,14,18,18,18,9,12,11,14,0,15,11,11],
[12,15,20,20,13,11,13,13,14,11,0,12,12],
[10,14,19,21,16,11,19,14,21,15,14,0,10],
[20,12,15,20,15,14,17,13,21,15,14,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 71, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,13,15,19,17,17,16,15,15,11,14,15],
[11,0,12,16,14,18,14,13,13,18,10,16,15],
[13,14,0,17,15,18,16,16,17,17,11,19,12],
[11,10,9,0,13,9,15,11,12,14,10,11,11],
[7,12,11,13,0,18,13,16,11,13,12,16,13],
[9,8,8,17,8,0,11,12,12,13,12,14,10],
[9,12,10,11,13,15,0,12,11,12,10,16,15],
[10,13,10,15,10,14,14,0,11,11,9,17,16],
[11,13,9,14,15,14,15,15,0,15,15,14,15],
[11,8,9,12,13,13,14,15,11,0,9,14,8],
[15,16,15,16,14,14,16,17,11,17,0,18,16],
[12,10,7,15,10,12,10,9,12,12,8,0,14],
[11,11,14,15,13,16,11,10,11,18,10,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 72, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,15,8,5,13,4,4,17,19,15,12,15],
[9,0,10,10,6,14,9,5,13,10,9,7,12],
[11,16,0,7,9,13,9,6,18,16,16,15,17],
[18,16,19,0,8,16,9,10,15,18,22,12,18],
[21,20,17,18,0,18,14,17,18,18,21,12,20],
[13,12,13,10,8,0,11,6,15,21,15,15,14],
[22,17,17,17,12,15,0,10,19,20,22,12,18],
[22,21,20,16,9,20,16,0,18,17,19,16,22],
[9,13,8,11,8,11,7,8,0,14,12,1,7],
[7,16,10,8,8,5,6,9,12,0,15,5,14],
[11,17,10,4,5,11,4,7,14,11,0,7,13],
[14,19,11,14,14,11,14,10,25,21,19,0,16],
[11,14,9,8,6,12,8,4,19,12,13,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 73, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,11,15,14,15,15,12,18,14,17,13,12],
[10,0,10,14,12,15,16,12,9,15,13,12,13],
[15,16,0,14,13,19,15,9,18,17,17,15,14],
[11,12,12,0,13,13,11,15,13,15,13,15,16],
[12,14,13,13,0,17,14,10,15,17,13,19,12],
[11,11,7,13,9,0,10,9,8,15,12,9,7],
[11,10,11,15,12,16,0,9,14,13,18,13,9],
[14,14,17,11,16,17,17,0,16,19,17,16,13],
[8,17,8,13,11,18,12,10,0,14,10,15,16],
[12,11,9,11,9,11,13,7,12,0,13,12,13],
[9,13,9,13,13,14,8,9,16,13,0,9,13],
[13,14,11,11,7,17,13,10,11,14,17,0,10],
[14,13,12,10,14,19,17,13,10,13,13,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 74, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,18,21,20,13,15,14,18,14,12,19,17],
[16,0,14,12,16,10,16,13,16,11,20,16,16],
[8,12,0,13,13,16,8,19,14,11,11,11,14],
[5,14,13,0,13,8,14,14,17,13,13,10,13],
[6,10,13,13,0,9,13,14,15,12,9,11,12],
[13,16,10,18,17,0,13,15,19,10,16,17,14],
[11,10,18,12,13,13,0,15,21,17,11,17,17],
[12,13,7,12,12,11,11,0,13,7,16,12,13],
[8,10,12,9,11,7,5,13,0,8,13,15,16],
[12,15,15,13,14,16,9,19,18,0,15,16,18],
[14,6,15,13,17,10,15,10,13,11,0,11,14],
[7,10,15,16,15,9,9,14,11,10,15,0,8],
[9,10,12,13,14,12,9,13,10,8,12,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 75, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,21,14,16,18,13,16,14,21,21,16,17],
[16,0,21,18,14,18,13,21,14,19,16,23,21],
[5,5,0,14,9,14,5,14,5,9,11,16,10],
[12,8,12,0,12,21,9,26,10,11,18,23,17],
[10,12,17,14,0,18,9,25,10,16,16,25,19],
[8,8,12,5,8,0,2,12,5,4,12,13,8],
[13,13,21,17,17,24,0,17,14,24,19,26,20],
[10,5,12,0,1,14,9,0,5,8,10,12,12],
[12,12,21,16,16,21,12,21,0,16,18,25,17],
[5,7,17,15,10,22,2,18,10,0,18,15,9],
[5,10,15,8,10,14,7,16,8,8,0,10,10],
[10,3,10,3,1,13,0,14,1,11,16,0,9],
[9,5,16,9,7,18,6,14,9,17,16,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 76, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,5,8,9,10,7,18,11,13,10,9,10],
[14,0,13,12,13,14,13,15,13,14,13,9,15],
[21,13,0,15,14,16,10,23,17,18,17,14,19],
[18,14,11,0,8,15,11,18,12,18,14,12,17],
[17,13,12,18,0,14,11,18,12,16,15,11,11],
[16,12,10,11,12,0,12,18,13,17,14,10,11],
[19,13,16,15,15,14,0,18,14,19,14,11,14],
[8,11,3,8,8,8,8,0,9,10,9,7,5],
[15,13,9,14,14,13,12,17,0,15,11,12,9],
[13,12,8,8,10,9,7,16,11,0,7,11,10],
[16,13,9,12,11,12,12,17,15,19,0,9,14],
[17,17,12,14,15,16,15,19,14,15,17,0,14],
[16,11,7,9,15,15,12,21,17,16,12,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 77, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,11,12,15,12,13,14,11,14,14,11,12],
[14,0,15,16,15,14,12,16,16,14,15,11,18],
[15,11,0,13,15,15,14,14,12,15,12,12,18],
[14,10,13,0,12,14,10,16,13,14,9,9,13],
[11,11,11,14,0,13,11,14,9,10,11,10,11],
[14,12,11,12,13,0,12,14,15,14,12,11,13],
[13,14,12,16,15,14,0,15,13,15,12,15,17],
[12,10,12,10,12,12,11,0,11,11,9,10,11],
[15,10,14,13,17,11,13,15,0,11,14,12,12],
[12,12,11,12,16,12,11,15,15,0,11,13,11],
[12,11,14,17,15,14,14,17,12,15,0,13,15],
[15,15,14,17,16,15,11,16,14,13,13,0,15],
[14,8,8,13,15,13,9,15,14,15,11,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 78, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,11,15,13,15,13,16,17,17,9,12,17],
[12,0,10,15,16,18,10,14,16,13,12,13,17],
[15,16,0,16,16,14,14,17,17,13,12,16,16],
[11,11,10,0,13,15,12,14,10,14,9,14,18],
[13,10,10,13,0,16,11,17,9,16,9,17,12],
[11,8,12,11,10,0,8,13,10,10,7,13,13],
[13,16,12,14,15,18,0,16,15,12,11,18,17],
[10,12,9,12,9,13,10,0,10,7,10,13,15],
[9,10,9,16,17,16,11,16,0,11,12,14,15],
[9,13,13,12,10,16,14,19,15,0,14,13,12],
[17,14,14,17,17,19,15,16,14,12,0,18,19],
[14,13,10,12,9,13,8,13,12,13,8,0,12],
[9,9,10,8,14,13,9,11,11,14,7,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 79, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,10,11,10,9,7,8,11,11,11,8,10],
[17,0,10,10,11,10,11,13,14,12,15,12,17],
[16,16,0,7,12,12,9,11,13,13,13,12,9],
[15,16,19,0,17,11,18,15,15,18,19,14,17],
[16,15,14,9,0,13,13,11,14,16,13,16,17],
[17,16,14,15,13,0,15,15,17,15,15,12,14],
[19,15,17,8,13,11,0,13,16,16,17,14,14],
[18,13,15,11,15,11,13,0,17,13,14,15,17],
[15,12,13,11,12,9,10,9,0,13,12,10,11],
[15,14,13,8,10,11,10,13,13,0,9,11,12],
[15,11,13,7,13,11,9,12,14,17,0,8,9],
[18,14,14,12,10,14,12,11,16,15,18,0,18],
[16,9,17,9,9,12,12,9,15,14,17,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 80, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,16,17,16,18,12,17,15,12,16,17,12],
[12,0,15,14,16,14,13,15,15,7,12,13,15],
[10,11,0,13,15,13,12,12,12,9,10,11,10],
[9,12,13,0,16,12,13,16,14,9,10,14,12],
[10,10,11,10,0,15,11,13,13,6,10,9,10],
[8,12,13,14,11,0,10,13,11,4,10,14,10],
[14,13,14,13,15,16,0,15,17,13,14,18,14],
[9,11,14,10,13,13,11,0,13,9,12,11,11],
[11,11,14,12,13,15,9,13,0,6,8,10,10],
[14,19,17,17,20,22,13,17,20,0,14,18,15],
[10,14,16,16,16,16,12,14,18,12,0,17,14],
[9,13,15,12,17,12,8,15,16,8,9,0,12],
[14,11,16,14,16,16,12,15,16,11,12,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 81, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,9,14,10,15,10,13,12,13,11,12,6],
[10,0,9,11,10,10,7,11,10,13,11,8,7],
[17,17,0,16,11,17,17,18,14,17,15,12,14],
[12,15,10,0,10,12,15,14,10,12,12,12,5],
[16,16,15,16,0,17,17,19,13,17,15,13,7],
[11,16,9,14,9,0,12,12,8,15,12,15,7],
[16,19,9,11,9,14,0,17,13,14,10,12,9],
[13,15,8,12,7,14,9,0,11,14,10,10,6],
[14,16,12,16,13,18,13,15,0,15,13,12,11],
[13,13,9,14,9,11,12,12,11,0,13,11,6],
[15,15,11,14,11,14,16,16,13,13,0,11,7],
[14,18,14,14,13,11,14,16,14,15,15,0,9],
[20,19,12,21,19,19,17,20,15,20,19,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 82, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,17,21,10,0,4,14,14,13,0,15,11],
[12,0,13,8,9,1,5,8,8,5,0,7,12],
[9,13,0,20,9,9,9,12,12,13,4,13,16],
[5,18,6,0,9,0,5,5,8,5,0,15,8],
[16,17,17,17,0,11,16,12,11,9,11,18,15],
[26,25,17,26,15,0,12,18,14,19,13,19,15],
[22,21,17,21,10,14,0,18,14,15,14,15,21],
[12,18,14,21,14,8,8,0,14,12,8,15,15],
[12,18,14,18,15,12,12,12,0,5,7,11,12],
[13,21,13,21,17,7,11,14,21,0,7,22,11],
[26,26,22,26,15,13,12,18,19,19,0,19,16],
[11,19,13,11,8,7,11,11,15,4,7,0,15],
[15,14,10,18,11,11,5,11,14,15,10,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 83, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,18,17,22,17,13,18,16,18,16,17,18],
[13,0,15,12,11,11,13,16,11,10,16,13,12],
[8,11,0,9,14,11,11,15,14,14,10,15,10],
[9,14,17,0,16,15,12,18,16,17,13,18,17],
[4,15,12,10,0,15,13,12,10,15,11,13,15],
[9,15,15,11,11,0,8,15,13,14,12,13,16],
[13,13,15,14,13,18,0,16,10,11,11,13,12],
[8,10,11,8,14,11,10,0,11,14,13,8,7],
[10,15,12,10,16,13,16,15,0,14,17,13,15],
[8,16,12,9,11,12,15,12,12,0,13,9,13],
[10,10,16,13,15,14,15,13,9,13,0,18,13],
[9,13,11,8,13,13,13,18,13,17,8,0,14],
[8,14,16,9,11,10,14,19,11,13,13,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 84, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,10,12,15,18,14,26,16,16,17,15,21],
[15,0,10,13,10,23,15,18,14,18,15,17,16],
[16,16,0,16,19,19,11,19,13,14,14,16,22],
[14,13,10,0,13,17,15,21,17,17,18,14,17],
[11,16,7,13,0,20,15,18,17,18,15,20,23],
[8,3,7,9,6,0,7,11,13,7,7,8,10],
[12,11,15,11,11,19,0,16,11,10,14,15,19],
[0,8,7,5,8,15,10,0,7,6,11,9,15],
[10,12,13,9,9,13,15,19,0,11,12,9,16],
[10,8,12,9,8,19,16,20,15,0,19,13,16],
[9,11,12,8,11,19,12,15,14,7,0,12,15],
[11,9,10,12,6,18,11,17,17,13,14,0,13],
[5,10,4,9,3,16,7,11,10,10,11,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 85, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,15,16,18,14,14,14,10,13,15,17,16],
[12,0,12,13,17,12,18,13,14,10,18,15,14],
[11,14,0,13,13,13,15,15,11,14,13,13,14],
[10,13,13,0,15,12,17,10,10,8,16,14,15],
[8,9,13,11,0,7,14,13,10,9,11,15,12],
[12,14,13,14,19,0,17,14,9,11,16,17,15],
[12,8,11,9,12,9,0,12,8,10,6,11,13],
[12,13,11,16,13,12,14,0,8,10,15,13,16],
[16,12,15,16,16,17,18,18,0,13,15,13,17],
[13,16,12,18,17,15,16,16,13,0,18,17,13],
[11,8,13,10,15,10,20,11,11,8,0,11,14],
[9,11,13,12,11,9,15,13,13,9,15,0,16],
[10,12,12,11,14,11,13,10,9,13,12,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 86, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,6,2,8,8,3,10,11,8,2,10,10],
[19,0,11,9,12,18,10,6,19,20,5,12,18],
[20,15,0,16,10,17,14,10,16,17,10,19,16],
[24,17,10,0,20,19,12,19,20,20,15,18,20],
[18,14,16,6,0,15,14,14,16,20,12,18,20],
[18,8,9,7,11,0,5,8,14,11,6,9,14],
[23,16,12,14,12,21,0,16,21,12,8,22,16],
[16,20,16,7,12,18,10,0,18,18,18,15,19],
[15,7,10,6,10,12,5,8,0,11,5,8,10],
[18,6,9,6,6,15,14,8,15,0,6,18,14],
[24,21,16,11,14,20,18,8,21,20,0,22,16],
[16,14,7,8,8,17,4,11,18,8,4,0,11],
[16,8,10,6,6,12,10,7,16,12,10,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 87, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,12,14,13,13,14,11,14,14,11,12,14],
[10,0,10,12,10,14,13,13,13,14,11,12,12],
[14,16,0,14,11,13,15,11,14,11,11,10,11],
[12,14,12,0,14,11,13,10,13,10,13,8,11],
[13,16,15,12,0,13,10,14,13,11,12,12,11],
[13,12,13,15,13,0,12,12,15,10,11,13,8],
[12,13,11,13,16,14,0,12,15,11,12,13,10],
[15,13,15,16,12,14,14,0,15,12,13,11,14],
[12,13,12,13,13,11,11,11,0,12,14,13,11],
[12,12,15,16,15,16,15,14,14,0,15,18,13],
[15,15,15,13,14,15,14,13,12,11,0,14,10],
[14,14,16,18,14,13,13,15,13,8,12,0,14],
[12,14,15,15,15,18,16,12,15,13,16,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 88, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,12,11,12,8,14,17,13,11,13,13,16],
[14,0,11,8,14,13,14,15,13,14,12,15,16],
[14,15,0,11,14,14,17,17,15,11,13,18,15],
[15,18,15,0,14,10,15,13,15,15,13,14,17],
[14,12,12,12,0,9,12,14,15,13,14,14,16],
[18,13,12,16,17,0,19,20,14,12,15,19,17],
[12,12,9,11,14,7,0,14,14,12,10,16,13],
[9,11,9,13,12,6,12,0,13,13,11,14,15],
[13,13,11,11,11,12,12,13,0,12,11,13,14],
[15,12,15,11,13,14,14,13,14,0,12,17,14],
[13,14,13,13,12,11,16,15,15,14,0,14,13],
[13,11,8,12,12,7,10,12,13,9,12,0,13],
[10,10,11,9,10,9,13,11,12,12,13,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 89, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,19,20,18,16,16,20,12,14,19,13,19],
[9,0,17,16,14,12,15,12,13,13,13,11,14],
[7,9,0,14,17,9,9,13,13,12,11,9,12],
[6,10,12,0,13,6,9,10,7,11,10,6,11],
[8,12,9,13,0,10,8,8,14,9,8,11,15],
[10,14,17,20,16,0,14,12,16,14,16,13,18],
[10,11,17,17,18,12,0,16,17,13,16,11,13],
[6,14,13,16,18,14,10,0,14,11,11,13,15],
[14,13,13,19,12,10,9,12,0,12,15,13,14],
[12,13,14,15,17,12,13,15,14,0,12,15,17],
[7,13,15,16,18,10,10,15,11,14,0,13,16],
[13,15,17,20,15,13,15,13,13,11,13,0,20],
[7,12,14,15,11,8,13,11,12,9,10,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 90, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,13,14,13,9,9,8,9,8,10,11,16],
[17,0,13,16,14,14,15,11,15,13,16,16,18],
[13,13,0,14,14,10,14,8,11,11,15,18,16],
[12,10,12,0,13,11,13,12,10,12,15,13,16],
[13,12,12,13,0,12,15,10,13,11,13,10,20],
[17,12,16,15,14,0,11,11,12,13,14,15,16],
[17,11,12,13,11,15,0,9,13,13,15,9,16],
[18,15,18,14,16,15,17,0,17,13,17,15,21],
[17,11,15,16,13,14,13,9,0,13,13,14,16],
[18,13,15,14,15,13,13,13,13,0,12,16,20],
[16,10,11,11,13,12,11,9,13,14,0,12,17],
[15,10,8,13,16,11,17,11,12,10,14,0,16],
[10,8,10,10,6,10,10,5,10,6,9,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 91, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,13,8,22,18,12,16,14,21,16,16,9],
[17,0,16,15,19,26,19,20,17,15,16,17,12],
[13,10,0,10,17,19,7,15,11,14,8,12,6],
[18,11,16,0,19,24,15,19,12,17,14,15,11],
[4,7,9,7,0,17,5,10,8,14,7,7,11],
[8,0,7,2,9,0,4,8,7,13,7,9,11],
[14,7,19,11,21,22,0,17,16,16,13,14,10],
[10,6,11,7,16,18,9,0,9,15,6,5,7],
[12,9,15,14,18,19,10,17,0,17,12,14,10],
[5,11,12,9,12,13,10,11,9,0,2,6,12],
[10,10,18,12,19,19,13,20,14,24,0,16,13],
[10,9,14,11,19,17,12,21,12,20,10,0,8],
[17,14,20,15,15,15,16,19,16,14,13,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 92, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,16,14,19,19,14,14,14,17,12,14,9],
[18,0,17,19,18,19,20,22,16,20,18,18,11],
[10,9,0,15,13,12,17,13,14,15,18,14,10],
[12,7,11,0,15,16,13,11,11,14,13,15,9],
[7,8,13,11,0,10,12,14,7,12,11,13,7],
[7,7,14,10,16,0,16,10,8,12,14,16,10],
[12,6,9,13,14,10,0,14,12,15,11,15,8],
[12,4,13,15,12,16,12,0,13,15,14,15,7],
[12,10,12,15,19,18,14,13,0,14,10,14,11],
[9,6,11,12,14,14,11,11,12,0,13,15,8],
[14,8,8,13,15,12,15,12,16,13,0,15,14],
[12,8,12,11,13,10,11,11,12,11,11,0,8],
[17,15,16,17,19,16,18,19,15,18,12,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 93, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,15,14,6,12,7,9,16,13,10,10,6],
[19,0,12,17,10,13,10,9,13,10,19,12,9],
[11,14,0,14,17,23,8,17,17,17,14,14,14],
[12,9,12,0,9,9,9,9,10,16,12,12,12],
[20,16,9,17,0,17,17,7,14,10,23,19,13],
[14,13,3,17,9,0,11,4,10,16,14,13,9],
[19,16,18,17,9,15,0,12,19,13,16,19,15],
[17,17,9,17,19,22,14,0,13,19,17,20,16],
[10,13,9,16,12,16,7,13,0,12,13,10,13],
[13,16,9,10,16,10,13,7,14,0,16,19,13],
[16,7,12,14,3,12,10,9,13,10,0,12,9],
[16,14,12,14,7,13,7,6,16,7,14,0,9],
[20,17,12,14,13,17,11,10,13,13,17,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 94, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,13,15,16,11,13,19,14,13,11,9,16],
[17,0,22,18,17,20,10,21,17,14,20,9,18],
[13,4,0,11,13,12,9,14,12,6,12,1,14],
[11,8,15,0,17,16,9,19,18,11,11,6,18],
[10,9,13,9,0,8,4,7,7,9,10,6,8],
[15,6,14,10,18,0,9,13,12,10,9,1,13],
[13,16,17,17,22,17,0,17,14,15,17,6,15],
[7,5,12,7,19,13,9,0,15,11,9,8,9],
[12,9,14,8,19,14,12,11,0,10,9,3,12],
[13,12,20,15,17,16,11,15,16,0,16,13,17],
[15,6,14,15,16,17,9,17,17,10,0,7,14],
[17,17,25,20,20,25,20,18,23,13,19,0,19],
[10,8,12,8,18,13,11,17,14,9,12,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 95, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,8,11,12,18,13,16,12,4,10,6,13],
[14,0,7,10,9,15,14,12,12,8,9,10,15],
[18,19,0,9,8,12,18,14,11,8,10,7,14],
[15,16,17,0,18,15,17,20,11,14,13,14,15],
[14,17,18,8,0,16,15,19,12,8,8,10,13],
[8,11,14,11,10,0,14,16,8,7,8,11,10],
[13,12,8,9,11,12,0,16,12,4,5,6,14],
[10,14,12,6,7,10,10,0,6,7,9,8,10],
[14,14,15,15,14,18,14,20,0,6,8,10,12],
[22,18,18,12,18,19,22,19,20,0,14,13,22],
[16,17,16,13,18,18,21,17,18,12,0,13,15],
[20,16,19,12,16,15,20,18,16,13,13,0,19],
[13,11,12,11,13,16,12,16,14,4,11,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 96, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,14,17,15,19,16,23,12,19,15,15,15],
[15,0,16,16,18,17,16,17,10,17,15,14,18],
[12,10,0,15,13,17,12,13,15,14,14,10,15],
[9,10,11,0,10,14,10,14,11,11,12,11,5],
[11,8,13,16,0,14,15,13,12,9,7,13,7],
[7,9,9,12,12,0,11,11,10,7,10,9,7],
[10,10,14,16,11,15,0,13,9,10,10,10,13],
[3,9,13,12,13,15,13,0,9,8,8,13,9],
[14,16,11,15,14,16,17,17,0,18,13,15,10],
[7,9,12,15,17,19,16,18,8,0,11,11,9],
[11,11,12,14,19,16,16,18,13,15,0,15,14],
[11,12,16,15,13,17,16,13,11,15,11,0,13],
[11,8,11,21,19,19,13,17,16,17,12,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 97, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,17,14,15,15,15,17,20,16,14,12,15],
[8,0,11,9,10,12,14,10,11,11,10,11,8],
[9,15,0,9,14,13,12,14,14,11,11,11,11],
[12,17,17,0,17,17,15,16,16,15,13,15,14],
[11,16,12,9,0,16,14,10,14,12,11,13,11],
[11,14,13,9,10,0,13,14,12,9,10,14,9],
[11,12,14,11,12,13,0,11,12,13,12,12,11],
[9,16,12,10,16,12,15,0,15,13,12,12,12],
[6,15,12,10,12,14,14,11,0,15,9,13,11],
[10,15,15,11,14,17,13,13,11,0,13,13,10],
[12,16,15,13,15,16,14,14,17,13,0,15,14],
[14,15,15,11,13,12,14,14,13,13,11,0,13],
[11,18,15,12,15,17,15,14,15,16,12,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 98, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,15,17,18,13,16,20,14,13,15,11,18],
[14,0,18,20,21,12,16,18,17,15,13,15,11],
[11,8,0,12,12,10,12,17,9,11,12,10,11],
[9,6,14,0,13,9,10,12,14,14,8,15,9],
[8,5,14,13,0,7,13,11,11,9,13,12,6],
[13,14,16,17,19,0,16,16,16,17,14,13,10],
[10,10,14,16,13,10,0,13,14,13,10,11,8],
[6,8,9,14,15,10,13,0,11,10,10,11,8],
[12,9,17,12,15,10,12,15,0,13,9,14,10],
[13,11,15,12,17,9,13,16,13,0,9,13,11],
[11,13,14,18,13,12,16,16,17,17,0,12,10],
[15,11,16,11,14,13,15,15,12,13,14,0,14],
[8,15,15,17,20,16,18,18,16,15,16,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 99, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,9,15,12,12,8,17,14,15,6,14,14],
[14,0,7,11,14,14,10,19,17,18,6,17,18],
[17,19,0,15,19,16,19,20,19,18,12,17,16],
[11,15,11,0,10,12,13,12,13,13,7,10,15],
[14,12,7,16,0,14,11,15,9,17,6,14,14],
[14,12,10,14,12,0,13,12,7,13,8,18,11],
[18,16,7,13,15,13,0,17,16,17,14,13,14],
[9,7,6,14,11,14,9,0,10,13,6,17,12],
[12,9,7,13,17,19,10,16,0,13,8,18,12],
[11,8,8,13,9,13,9,13,13,0,6,15,12],
[20,20,14,19,20,18,12,20,18,20,0,25,20],
[12,9,9,16,12,8,13,9,8,11,1,0,12],
[12,8,10,11,12,15,12,14,14,14,6,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 100, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,10,16,11,16,14,9,10,13,12,13],
[13,0,14,12,14,13,17,14,11,13,13,8,10],
[13,12,0,13,16,10,15,16,9,12,14,11,11],
[16,14,13,0,16,14,17,16,12,16,14,11,15],
[10,12,10,10,0,10,13,15,11,12,12,8,15],
[15,13,16,12,16,0,17,16,10,10,17,11,14],
[10,9,11,9,13,9,0,15,10,8,11,7,9],
[12,12,10,10,11,10,11,0,8,12,13,10,14],
[17,15,17,14,15,16,16,18,0,14,15,10,14],
[16,13,14,10,14,16,18,14,12,0,14,12,14],
[13,13,12,12,14,9,15,13,11,12,0,13,14],
[14,18,15,15,18,15,19,16,16,14,13,0,14],
[13,16,15,11,11,12,17,12,12,12,12,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 101, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,17,13,16,15,21,11,11,15,14,16,16],
[11,0,14,12,16,14,18,11,14,11,11,11,13],
[9,12,0,9,11,11,14,8,11,8,9,11,11],
[13,14,17,0,16,14,21,14,14,13,14,15,14],
[10,10,15,10,0,11,15,6,9,7,9,10,11],
[11,12,15,12,15,0,21,13,12,11,13,16,12],
[5,8,12,5,11,5,0,7,10,7,8,9,9],
[15,15,18,12,20,13,19,0,15,9,13,13,17],
[15,12,15,12,17,14,16,11,0,11,10,12,10],
[11,15,18,13,19,15,19,17,15,0,13,15,14],
[12,15,17,12,17,13,18,13,16,13,0,19,14],
[10,15,15,11,16,10,17,13,14,11,7,0,14],
[10,13,15,12,15,14,17,9,16,12,12,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 102, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,11,11,13,9,15,12,12,15,14,12,16],
[13,0,18,13,12,14,19,16,15,17,12,16,18],
[15,8,0,11,13,16,12,7,9,10,12,8,17],
[15,13,15,0,13,16,15,15,15,18,11,15,17],
[13,14,13,13,0,12,15,13,13,12,12,12,14],
[17,12,10,10,14,0,15,9,12,11,14,13,17],
[11,7,14,11,11,11,0,11,13,9,15,12,17],
[14,10,19,11,13,17,15,0,10,14,12,11,18],
[14,11,17,11,13,14,13,16,0,13,13,14,17],
[11,9,16,8,14,15,17,12,13,0,16,14,14],
[12,14,14,15,14,12,11,14,13,10,0,12,15],
[14,10,18,11,14,13,14,15,12,12,14,0,15],
[10,8,9,9,12,9,9,8,9,12,11,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 103, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,12,15,16,16,13,11,14,14,16,11,14],
[14,0,9,12,14,13,11,12,12,15,17,13,13],
[14,17,0,16,18,16,14,16,14,15,19,16,13],
[11,14,10,0,15,16,13,14,10,13,18,11,13],
[10,12,8,11,0,11,12,7,8,12,12,11,10],
[10,13,10,10,15,0,11,10,9,12,15,9,11],
[13,15,12,13,14,15,0,10,12,11,16,12,13],
[15,14,10,12,19,16,16,0,12,14,18,15,12],
[12,14,12,16,18,17,14,14,0,12,17,12,16],
[12,11,11,13,14,14,15,12,14,0,18,14,13],
[10,9,7,8,14,11,10,8,9,8,0,11,8],
[15,13,10,15,15,17,14,11,14,12,15,0,15],
[12,13,13,13,16,15,13,14,10,13,18,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 104, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1,0,16,1,10,16,4,9,8,1,4,1],
[25,0,8,25,18,25,22,18,15,26,19,26,19],
[26,18,0,26,19,25,23,11,16,18,19,18,19],
[10,1,0,0,4,10,7,10,8,8,11,4,4],
[25,8,7,22,0,17,22,10,15,8,16,11,16],
[16,1,1,16,9,0,16,1,9,8,9,1,9],
[10,4,3,19,4,10,0,10,12,11,11,4,4],
[22,8,15,16,16,25,16,0,9,16,23,16,9],
[17,11,10,18,11,17,14,17,0,11,18,11,11],
[18,0,8,18,18,18,15,10,15,0,19,19,19],
[25,7,7,15,10,17,15,3,8,7,0,11,12],
[22,0,8,22,15,25,22,10,15,7,15,0,16],
[25,7,7,22,10,17,22,17,15,7,14,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 105, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,12,13,11,14,15,16,13,15,16,11,11],
[14,0,14,15,13,15,12,15,14,17,18,15,13],
[14,12,0,15,11,20,12,16,19,21,19,16,13],
[13,11,11,0,12,14,8,13,13,17,13,14,12],
[15,13,15,14,0,15,12,14,16,16,15,13,11],
[12,11,6,12,11,0,11,12,12,12,16,12,12],
[11,14,14,18,14,15,0,12,17,17,15,11,12],
[10,11,10,13,12,14,14,0,12,17,15,12,11],
[13,12,7,13,10,14,9,14,0,19,15,14,12],
[11,9,5,9,10,14,9,9,7,0,11,13,11],
[10,8,7,13,11,10,11,11,11,15,0,10,9],
[15,11,10,12,13,14,15,14,12,13,16,0,12],
[15,13,13,14,15,14,14,15,14,15,17,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 106, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,5,10,6,9,13,9,8,11,10,10,10],
[23,0,13,16,10,21,18,8,13,16,18,18,18],
[21,13,0,15,9,14,19,16,18,22,20,18,13],
[16,10,11,0,13,14,14,12,16,15,13,14,12],
[20,16,17,13,0,15,21,13,18,16,14,18,19],
[17,5,12,12,11,0,17,11,14,17,14,16,11],
[13,8,7,12,5,9,0,10,14,12,7,16,10],
[17,18,10,14,13,15,16,0,12,13,15,17,14],
[18,13,8,10,8,12,12,14,0,12,10,14,15],
[15,10,4,11,10,9,14,13,14,0,10,12,6],
[16,8,6,13,12,12,19,11,16,16,0,15,12],
[16,8,8,12,8,10,10,9,12,14,11,0,11],
[16,8,13,14,7,15,16,12,11,20,14,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 107, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,15,20,9,18,14,18,11,12,19,18,8],
[15,0,15,15,12,19,13,18,13,12,22,17,8],
[11,11,0,12,8,13,11,12,10,12,12,12,7],
[6,11,14,0,7,18,15,10,9,11,11,10,11],
[17,14,18,19,0,17,18,19,10,15,18,17,13],
[8,7,13,8,9,0,10,9,11,12,13,13,9],
[12,13,15,11,8,16,0,12,10,13,15,17,7],
[8,8,14,16,7,17,14,0,10,12,12,14,12],
[15,13,16,17,16,15,16,16,0,11,21,16,10],
[14,14,14,15,11,14,13,14,15,0,18,16,11],
[7,4,14,15,8,13,11,14,5,8,0,13,8],
[8,9,14,16,9,13,9,12,10,10,13,0,9],
[18,18,19,15,13,17,19,14,16,15,18,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 108, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,10,19,7,15,18,7,6,4,12,9,12],
[14,0,8,14,7,8,11,5,7,8,8,10,8],
[16,18,0,22,13,19,16,18,13,16,21,18,21],
[7,12,4,0,4,12,7,7,7,5,12,12,7],
[19,19,13,22,0,19,19,11,16,8,19,16,17],
[11,18,7,14,7,0,15,5,7,5,10,12,7],
[8,15,10,19,7,11,0,13,10,8,13,10,11],
[19,21,8,19,15,21,13,0,16,17,16,23,19],
[20,19,13,19,10,19,16,10,0,11,21,19,16],
[22,18,10,21,18,21,18,9,15,0,23,15,18],
[14,18,5,14,7,16,13,10,5,3,0,12,7],
[17,16,8,14,10,14,16,3,7,11,14,0,6],
[14,18,5,19,9,19,15,7,10,8,19,20,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 109, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,8,11,12,8,8,9,12,16,14,11,4],
[15,0,12,11,16,13,7,12,11,16,11,10,8],
[18,14,0,18,18,15,13,11,16,19,17,19,15],
[15,15,8,0,18,9,12,10,12,15,12,17,10],
[14,10,8,8,0,10,7,10,9,14,7,12,6],
[18,13,11,17,16,0,12,9,11,19,11,20,11],
[18,19,13,14,19,14,0,17,13,18,15,16,15],
[17,14,15,16,16,17,9,0,13,19,12,14,10],
[14,15,10,14,17,15,13,13,0,18,11,14,11],
[10,10,7,11,12,7,8,7,8,0,8,13,6],
[12,15,9,14,19,15,11,14,15,18,0,12,11],
[15,16,7,9,14,6,10,12,12,13,14,0,10],
[22,18,11,16,20,15,11,16,15,20,15,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 110, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,18,17,23,11,18,5,15,18,15,17,18],
[17,0,16,17,17,9,19,2,16,20,10,12,17],
[8,10,0,17,14,15,11,11,3,11,19,18,18],
[9,9,9,0,11,14,11,8,5,12,18,18,21],
[3,9,12,15,0,11,17,8,2,15,12,17,15],
[15,17,11,12,15,0,20,17,11,18,14,12,17],
[8,7,15,15,9,6,0,5,3,18,13,15,16],
[21,24,15,18,18,9,21,0,15,21,10,12,21],
[11,10,23,21,24,15,23,11,0,20,19,21,18],
[8,6,15,14,11,8,8,5,6,0,12,14,20],
[11,16,7,8,14,12,13,16,7,14,0,17,22],
[9,14,8,8,9,14,11,14,5,12,9,0,20],
[8,9,8,5,11,9,10,5,8,6,4,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 111, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,18,16,19,14,23,8,16,14,14,16,13],
[10,0,12,13,10,13,18,8,9,12,9,12,11],
[8,14,0,9,14,14,19,9,11,12,10,11,17],
[10,13,17,0,11,12,18,11,13,11,10,17,14],
[7,16,12,15,0,10,17,12,12,13,6,15,12],
[12,13,12,14,16,0,21,11,11,13,9,13,13],
[3,8,7,8,9,5,0,7,8,10,2,9,5],
[18,18,17,15,14,15,19,0,12,14,12,15,15],
[10,17,15,13,14,15,18,14,0,18,11,14,11],
[12,14,14,15,13,13,16,12,8,0,8,11,13],
[12,17,16,16,20,17,24,14,15,18,0,17,16],
[10,14,15,9,11,13,17,11,12,15,9,0,15],
[13,15,9,12,14,13,21,11,15,13,10,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 112, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,17,17,23,13,13,17,21,15,17,16,9],
[15,0,16,17,17,18,17,11,16,10,10,18,17],
[9,10,0,11,19,13,12,7,12,9,11,13,9],
[9,9,15,0,18,9,9,11,8,9,8,17,12],
[3,9,7,8,0,16,12,4,8,3,11,13,6],
[13,8,13,17,10,0,10,8,14,8,10,13,10],
[13,9,14,17,14,16,0,8,9,6,13,10,10],
[9,15,19,15,22,18,18,0,12,6,10,14,9],
[5,10,14,18,18,12,17,14,0,7,11,17,10],
[11,16,17,17,23,18,20,20,19,0,14,17,12],
[9,16,15,18,15,16,13,16,15,12,0,12,12],
[10,8,13,9,13,13,16,12,9,9,14,0,5],
[17,9,17,14,20,16,16,17,16,14,14,21,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 113, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,17,14,14,17,21,12,14,17,18,11,11],
[6,0,18,7,8,21,11,12,12,9,12,9,5],
[9,8,0,9,8,14,14,15,11,7,15,16,7],
[12,19,17,0,10,19,14,12,7,12,15,10,7],
[12,18,18,16,0,17,15,7,11,20,21,13,16],
[9,5,12,7,9,0,14,11,14,14,14,10,5],
[5,15,12,12,11,12,0,13,12,9,23,2,11],
[14,14,11,14,19,15,13,0,14,18,21,9,14],
[12,14,15,19,15,12,14,12,0,12,19,10,7],
[9,17,19,14,6,12,17,8,14,0,18,13,6],
[8,14,11,11,5,12,3,5,7,8,0,5,9],
[15,17,10,16,13,16,24,17,16,13,21,0,16],
[15,21,19,19,10,21,15,12,19,20,17,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 114, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,14,15,11,21,15,13,8,16,16,17,13],
[17,0,12,12,6,14,10,9,9,11,17,16,8],
[12,14,0,13,9,14,12,14,14,12,15,13,8],
[11,14,13,0,6,12,9,18,9,12,13,10,10],
[15,20,17,20,0,20,15,17,13,15,17,15,16],
[5,12,12,14,6,0,11,15,5,8,8,10,9],
[11,16,14,17,11,15,0,18,13,10,12,13,10],
[13,17,12,8,9,11,8,0,10,10,16,15,12],
[18,17,12,17,13,21,13,16,0,19,15,16,13],
[10,15,14,14,11,18,16,16,7,0,8,13,9],
[10,9,11,13,9,18,14,10,11,18,0,13,10],
[9,10,13,16,11,16,13,11,10,13,13,0,12],
[13,18,18,16,10,17,16,14,13,17,16,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 115, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,16,9,11,18,14,12,12,12,15,15,18],
[16,0,15,12,14,18,12,15,15,16,18,16,17],
[10,11,0,15,8,13,12,11,11,10,7,14,17],
[17,14,11,0,13,17,10,19,10,14,15,14,13],
[15,12,18,13,0,20,10,16,17,14,22,18,20],
[8,8,13,9,6,0,6,15,9,8,6,11,10],
[12,14,14,16,16,20,0,17,13,16,12,20,16],
[14,11,15,7,10,11,9,0,10,14,12,11,6],
[14,11,15,16,9,17,13,16,0,15,8,15,19],
[14,10,16,12,12,18,10,12,11,0,11,15,14],
[11,8,19,11,4,20,14,14,18,15,0,15,16],
[11,10,12,12,8,15,6,15,11,11,11,0,11],
[8,9,9,13,6,16,10,20,7,12,10,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 116, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,12,11,9,15,5,9,10,10,9,8,9],
[17,0,11,12,12,17,11,11,11,12,12,13,14],
[14,15,0,15,13,14,12,12,14,10,12,14,13],
[15,14,11,0,13,13,10,13,13,13,10,15,15],
[17,14,13,13,0,18,9,12,14,13,14,15,14],
[11,9,12,13,8,0,9,10,10,12,10,11,13],
[21,15,14,16,17,17,0,13,17,14,11,15,16],
[17,15,14,13,14,16,13,0,14,15,13,17,14],
[16,15,12,13,12,16,9,12,0,13,13,12,16],
[16,14,16,13,13,14,12,11,13,0,8,16,15],
[17,14,14,16,12,16,15,13,13,18,0,14,16],
[18,13,12,11,11,15,11,9,14,10,12,0,14],
[17,12,13,11,12,13,10,12,10,11,10,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 117, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,11,13,13,11,8,12,12,15,15,13,8],
[13,0,11,8,13,13,6,20,12,14,15,13,10],
[15,15,0,11,16,12,7,17,13,11,11,7,6],
[13,18,15,0,17,10,10,17,13,18,14,13,13],
[13,13,10,9,0,9,8,15,12,12,12,9,6],
[15,13,14,16,17,0,9,16,14,13,13,13,9],
[18,20,19,16,18,17,0,18,17,18,17,16,7],
[14,6,9,9,11,10,8,0,11,13,12,10,6],
[14,14,13,13,14,12,9,15,0,17,16,13,8],
[11,12,15,8,14,13,8,13,9,0,11,11,9],
[11,11,15,12,14,13,9,14,10,15,0,15,10],
[13,13,19,13,17,13,10,16,13,15,11,0,10],
[18,16,20,13,20,17,19,20,18,17,16,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 118, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,14,15,14,14,13,12,15,11,13,15,13],
[14,0,12,13,14,12,17,16,19,14,18,20,14],
[12,14,0,10,8,10,10,14,12,12,12,17,11],
[11,13,16,0,11,9,16,15,13,13,10,13,12],
[12,12,18,15,0,15,19,18,18,16,15,20,14],
[12,14,16,17,11,0,16,13,15,13,14,17,14],
[13,9,16,10,7,10,0,12,13,12,10,14,12],
[14,10,12,11,8,13,14,0,17,10,10,15,10],
[11,7,14,13,8,11,13,9,0,11,12,11,10],
[15,12,14,13,10,13,14,16,15,0,15,14,11],
[13,8,14,16,11,12,16,16,14,11,0,15,11],
[11,6,9,13,6,9,12,11,15,12,11,0,12],
[13,12,15,14,12,12,14,16,16,15,15,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 119, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,9,9,11,15,5,16,13,12,10,11,13],
[12,0,6,8,11,12,9,15,15,11,9,9,14],
[17,20,0,14,15,14,11,18,15,15,15,15,15],
[17,18,12,0,18,15,13,15,16,17,15,14,17],
[15,15,11,8,0,15,10,13,13,14,13,14,14],
[11,14,12,11,11,0,10,12,11,11,11,12,14],
[21,17,15,13,16,16,0,15,17,15,12,17,15],
[10,11,8,11,13,14,11,0,15,13,9,11,14],
[13,11,11,10,13,15,9,11,0,12,9,13,15],
[14,15,11,9,12,15,11,13,14,0,13,12,12],
[16,17,11,11,13,15,14,17,17,13,0,16,14],
[15,17,11,12,12,14,9,15,13,14,10,0,16],
[13,12,11,9,12,12,11,12,11,14,12,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 120, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,20,20,13,13,13,13,16,13,20,20,9],
[24,0,23,21,11,21,21,14,21,24,21,24,21],
[6,3,0,10,3,17,3,14,6,3,3,3,13],
[6,5,16,0,14,17,8,13,5,17,3,8,6],
[13,15,23,12,0,24,15,23,12,24,13,15,13],
[13,5,9,9,2,0,5,2,5,10,7,12,15],
[13,5,23,18,11,21,0,11,12,24,7,10,10],
[13,12,12,13,3,24,15,0,12,13,13,13,13],
[10,5,20,21,14,21,14,14,0,21,10,10,10],
[13,2,23,9,2,16,2,13,5,0,9,9,12],
[6,5,23,23,13,19,19,13,16,17,0,8,15],
[6,2,23,18,11,14,16,13,16,17,18,0,10],
[17,5,13,20,13,11,16,13,16,14,11,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 121, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,13,8,14,20,16,9,12,15,7,16,19],
[18,0,17,6,12,19,18,15,13,14,8,13,18],
[13,9,0,8,10,20,14,8,15,13,5,15,13],
[18,20,18,0,13,23,20,19,13,19,11,16,20],
[12,14,16,13,0,21,18,12,10,14,13,16,16],
[6,7,6,3,5,0,14,7,10,9,1,8,5],
[10,8,12,6,8,12,0,10,6,10,12,10,10],
[17,11,18,7,14,19,16,0,11,15,10,15,17],
[14,13,11,13,16,16,20,15,0,13,11,14,15],
[11,12,13,7,12,17,16,11,13,0,9,14,8],
[19,18,21,15,13,25,14,16,15,17,0,16,19],
[10,13,11,10,10,18,16,11,12,12,10,0,9],
[7,8,13,6,10,21,16,9,11,18,7,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 122, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,15,15,18,15,17,17,13,16,11,15,13],
[11,0,16,13,16,17,15,17,11,13,13,18,13],
[11,10,0,15,12,13,13,14,13,10,11,14,13],
[11,13,11,0,15,15,12,14,13,15,13,11,13],
[8,10,14,11,0,13,11,13,11,13,10,13,11],
[11,9,13,11,13,0,10,15,10,12,7,13,13],
[9,11,13,14,15,16,0,14,12,14,11,14,11],
[9,9,12,12,13,11,12,0,9,13,7,11,13],
[13,15,13,13,15,16,14,17,0,16,12,16,13],
[10,13,16,11,13,14,12,13,10,0,11,15,11],
[15,13,15,13,16,19,15,19,14,15,0,12,14],
[11,8,12,15,13,13,12,15,10,11,14,0,9],
[13,13,13,13,15,13,15,13,13,15,12,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 123, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,14,11,17,16,11,11,14,12,17,13,14],
[10,0,12,12,9,13,14,16,9,11,17,10,18],
[12,14,0,10,16,19,14,16,17,15,14,10,22],
[15,14,16,0,14,18,14,13,16,13,15,12,17],
[9,17,10,12,0,18,13,12,14,12,14,18,15],
[10,13,7,8,8,0,10,9,11,6,13,11,15],
[15,12,12,12,13,16,0,17,16,15,19,14,20],
[15,10,10,13,14,17,9,0,14,14,19,14,19],
[12,17,9,10,12,15,10,12,0,11,14,13,17],
[14,15,11,13,14,20,11,12,15,0,16,9,15],
[9,9,12,11,12,13,7,7,12,10,0,9,11],
[13,16,16,14,8,15,12,12,13,17,17,0,18],
[12,8,4,9,11,11,6,7,9,11,15,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 124, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,19,16,18,16,14,15,11,12,15,14,15],
[10,0,12,12,11,13,9,5,8,10,14,10,9],
[7,14,0,14,14,12,8,9,8,11,12,9,13],
[10,14,12,0,11,14,10,13,9,12,11,10,10],
[8,15,12,15,0,13,12,13,12,12,11,9,10],
[10,13,14,12,13,0,8,9,8,10,11,11,11],
[12,17,18,16,14,18,0,16,13,16,17,15,15],
[11,21,17,13,13,17,10,0,13,10,14,10,14],
[15,18,18,17,14,18,13,13,0,14,15,15,15],
[14,16,15,14,14,16,10,16,12,0,15,11,15],
[11,12,14,15,15,15,9,12,11,11,0,11,12],
[12,16,17,16,17,15,11,16,11,15,15,0,16],
[11,17,13,16,16,15,11,12,11,11,14,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 125, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,6,13,10,9,8,16,11,11,12,6,7],
[15,0,12,18,17,15,11,16,8,17,14,7,9],
[20,14,0,15,14,9,14,15,10,16,12,11,17],
[13,8,11,0,14,11,9,21,11,10,12,7,14],
[16,9,12,12,0,12,11,14,7,10,13,4,12],
[17,11,17,15,14,0,10,14,9,11,16,9,13],
[18,15,12,17,15,16,0,19,12,11,11,7,12],
[10,10,11,5,12,12,7,0,13,8,11,8,14],
[15,18,16,15,19,17,14,13,0,19,15,13,13],
[15,9,10,16,16,15,15,18,7,0,10,10,14],
[14,12,14,14,13,10,15,15,11,16,0,10,12],
[20,19,15,19,22,17,19,18,13,16,16,0,14],
[19,17,9,12,14,13,14,12,13,12,14,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 126, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,17,10,2,20,16,14,9,9,6,19,18],
[10,0,19,15,7,22,18,17,8,17,10,16,18],
[9,7,0,11,6,19,19,17,7,8,8,17,12],
[16,11,15,0,9,20,21,14,12,9,13,17,21],
[24,19,20,17,0,23,24,17,12,12,15,19,24],
[6,4,7,6,3,0,14,17,4,9,1,14,9],
[10,8,7,5,2,12,0,11,3,9,1,11,10],
[12,9,9,12,9,9,15,0,10,9,6,9,13],
[17,18,19,14,14,22,23,16,0,12,9,14,16],
[17,9,18,17,14,17,17,17,14,0,14,17,14],
[20,16,18,13,11,25,25,20,17,12,0,19,24],
[7,10,9,9,7,12,15,17,12,9,7,0,18],
[8,8,14,5,2,17,16,13,10,12,2,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 127, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,12,13,16,16,9,13,12,14,12,15,12],
[18,0,13,16,18,18,14,17,18,18,15,17,17],
[14,13,0,14,16,17,10,13,13,12,12,12,12],
[13,10,12,0,19,16,11,16,17,14,11,15,12],
[10,8,10,7,0,11,7,11,8,11,9,7,10],
[10,8,9,10,15,0,9,12,11,13,13,14,10],
[17,12,16,15,19,17,0,15,12,16,13,16,11],
[13,9,13,10,15,14,11,0,13,14,9,11,11],
[14,8,13,9,18,15,14,13,0,16,12,12,12],
[12,8,14,12,15,13,10,12,10,0,10,11,11],
[14,11,14,15,17,13,13,17,14,16,0,14,15],
[11,9,14,11,19,12,10,15,14,15,12,0,12],
[14,9,14,14,16,16,15,15,14,15,11,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 128, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,15,13,6,21,17,14,18,10,12,17,20],
[11,0,11,7,6,15,15,16,12,6,14,12,11],
[11,15,0,17,11,14,14,11,13,7,10,6,12],
[13,19,9,0,8,16,18,19,14,7,9,13,14],
[20,20,15,18,0,21,23,22,16,13,14,18,21],
[5,11,12,10,5,0,9,9,12,8,12,10,9],
[9,11,12,8,3,17,0,14,16,5,8,10,13],
[12,10,15,7,4,17,12,0,14,8,8,10,15],
[8,14,13,12,10,14,10,12,0,8,10,10,11],
[16,20,19,19,13,18,21,18,18,0,16,20,16],
[14,12,16,17,12,14,18,18,16,10,0,7,17],
[9,14,20,13,8,16,16,16,16,6,19,0,13],
[6,15,14,12,5,17,13,11,15,10,9,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 129, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,15,10,21,10,10,21,9,9,15,7,10],
[16,0,19,8,19,19,18,20,19,19,14,5,11],
[11,7,0,14,20,15,15,20,8,20,6,2,7],
[16,18,12,0,12,13,18,25,11,19,12,13,12],
[5,7,6,14,0,2,7,21,1,13,7,2,2],
[16,7,11,13,24,0,7,25,5,19,6,7,7],
[16,8,11,8,19,19,0,20,11,19,6,5,6],
[5,6,6,1,5,1,6,0,0,8,5,1,0],
[17,7,18,15,25,21,15,26,0,20,6,7,8],
[17,7,6,7,13,7,7,18,6,0,7,7,8],
[11,12,20,14,19,20,20,21,20,19,0,12,12],
[19,21,24,13,24,19,21,25,19,19,14,0,20],
[16,15,19,14,24,19,20,26,18,18,14,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 130, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,26,26,8,18,18,26,18,10,8,18,8,18],
[0,0,10,8,18,8,8,8,0,0,10,0,18],
[0,16,0,8,8,8,16,8,0,8,18,8,8],
[18,18,18,0,10,10,26,18,18,10,18,8,18],
[8,8,18,16,0,8,16,8,8,8,18,8,8],
[8,18,18,16,18,0,26,8,8,8,18,8,18],
[0,18,10,0,10,0,0,0,0,0,10,0,10],
[8,18,18,8,18,18,26,0,8,8,18,8,18],
[16,26,26,8,18,18,26,18,0,8,26,16,26],
[18,26,18,16,18,18,26,18,18,0,18,8,26],
[8,16,8,8,8,8,16,8,0,8,0,8,8],
[18,26,18,18,18,18,26,18,10,18,18,0,18],
[8,8,18,8,18,8,16,8,0,0,18,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 131, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,15,12,12,13,18,14,17,16,13,15,13],
[15,0,13,10,13,12,14,15,13,17,14,16,10],
[11,13,0,11,13,11,13,18,18,15,14,18,8],
[14,16,15,0,15,13,14,13,19,13,14,14,15],
[14,13,13,11,0,15,16,14,19,13,11,16,14],
[13,14,15,13,11,0,18,14,12,17,13,17,16],
[8,12,13,12,10,8,0,15,14,15,10,14,8],
[12,11,8,13,12,12,11,0,11,17,10,13,11],
[9,13,8,7,7,14,12,15,0,16,11,11,9],
[10,9,11,13,13,9,11,9,10,0,13,14,9],
[13,12,12,12,15,13,16,16,15,13,0,14,11],
[11,10,8,12,10,9,12,13,15,12,12,0,10],
[13,16,18,11,12,10,18,15,17,17,15,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 132, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,16,18,19,26,15,10,21,16,15,14,9],
[10,0,12,17,13,18,13,9,12,7,7,13,5],
[10,14,0,10,6,18,8,2,7,7,7,6,0],
[8,9,16,0,19,18,21,15,13,9,8,14,8],
[7,13,20,7,0,13,3,9,7,2,7,11,13],
[0,8,8,8,13,0,8,10,8,3,3,8,1],
[11,13,18,5,23,18,0,9,13,8,13,11,11],
[16,17,24,11,17,16,17,0,19,12,19,17,17],
[5,14,19,13,19,18,13,7,0,12,7,19,12],
[10,19,19,17,24,23,18,14,14,0,19,19,11],
[11,19,19,18,19,23,13,7,19,7,0,19,12],
[12,13,20,12,15,18,15,9,7,7,7,0,13],
[17,21,26,18,13,25,15,9,14,15,14,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 133, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,14,13,15,15,12,14,15,16,15,11,16],
[11,0,11,11,13,10,11,12,17,11,12,10,13],
[12,15,0,12,15,16,9,13,16,15,16,13,14],
[13,15,14,0,18,15,15,13,17,17,15,11,15],
[11,13,11,8,0,13,9,12,11,15,14,12,12],
[11,16,10,11,13,0,12,14,17,17,15,12,16],
[14,15,17,11,17,14,0,13,20,18,14,12,15],
[12,14,13,13,14,12,13,0,17,17,16,12,17],
[11,9,10,9,15,9,6,9,0,11,11,10,15],
[10,15,11,9,11,9,8,9,15,0,13,11,15],
[11,14,10,11,12,11,12,10,15,13,0,12,14],
[15,16,13,15,14,14,14,14,16,15,14,0,12],
[10,13,12,11,14,10,11,9,11,11,12,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 134, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,0,11,12,3,11,4,11,22,19,22,15],
[22,0,0,11,26,3,19,18,11,22,22,22,18],
[26,26,0,11,26,15,19,18,14,22,22,22,18],
[15,15,15,0,15,15,12,15,15,22,15,26,26],
[14,0,0,11,0,3,11,4,11,14,14,22,15],
[23,23,11,11,23,0,19,15,11,22,19,22,15],
[15,7,7,14,15,7,0,7,14,22,22,22,18],
[22,8,8,11,22,11,19,0,19,22,22,22,23],
[15,15,12,11,15,15,12,7,0,22,11,22,26],
[4,4,4,4,12,4,4,4,4,0,4,26,4],
[7,4,4,11,12,7,4,4,15,22,0,22,15],
[4,4,4,0,4,4,4,4,4,0,4,0,4],
[11,8,8,0,11,11,8,3,0,22,11,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 135, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,19,13,12,8,13,22,12,13,16,13,16],
[12,0,13,7,12,7,8,14,8,18,16,11,10],
[7,13,0,11,9,5,9,11,9,11,14,9,14],
[13,19,15,0,17,10,13,16,16,15,18,15,18],
[14,14,17,9,0,11,14,22,11,16,19,11,20],
[18,19,21,16,15,0,12,21,17,15,19,17,15],
[13,18,17,13,12,14,0,18,13,15,19,15,14],
[4,12,15,10,4,5,8,0,8,11,15,13,10],
[14,18,17,10,15,9,13,18,0,14,19,13,16],
[13,8,15,11,10,11,11,15,12,0,16,11,13],
[10,10,12,8,7,7,7,11,7,10,0,14,9],
[13,15,17,11,15,9,11,13,13,15,12,0,13],
[10,16,12,8,6,11,12,16,10,13,17,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 136, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,16,9,10,8,11,11,11,12,11,13,11],
[14,0,18,13,14,11,13,18,13,17,16,14,14],
[10,8,0,7,9,7,8,11,10,12,6,13,9],
[17,13,19,0,14,11,16,16,15,19,13,15,15],
[16,12,17,12,0,12,13,15,15,12,12,12,17],
[18,15,19,15,14,0,15,15,16,15,15,11,15],
[15,13,18,10,13,11,0,12,14,15,9,14,15],
[15,8,15,10,11,11,14,0,14,16,12,12,15],
[15,13,16,11,11,10,12,12,0,10,12,10,13],
[14,9,14,7,14,11,11,10,16,0,9,10,15],
[15,10,20,13,14,11,17,14,14,17,0,15,15],
[13,12,13,11,14,15,12,14,16,16,11,0,13],
[15,12,17,11,9,11,11,11,13,11,11,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 137, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,10,5,5,7,15,4,11,1,16,10,9],
[18,0,14,18,18,14,22,13,23,13,19,12,17],
[16,12,0,19,10,15,20,5,12,4,19,10,18],
[21,8,7,0,7,13,25,11,11,6,19,7,12],
[21,8,16,19,0,16,21,5,18,14,20,6,14],
[19,12,11,13,10,0,19,10,15,5,20,5,10],
[11,4,6,1,5,7,0,5,11,5,6,3,10],
[22,13,21,15,21,16,21,0,19,9,25,6,14],
[15,3,14,15,8,11,15,7,0,7,10,5,6],
[25,13,22,20,12,21,21,17,19,0,20,16,22],
[10,7,7,7,6,6,20,1,16,6,0,5,10],
[16,14,16,19,20,21,23,20,21,10,21,0,13],
[17,9,8,14,12,16,16,12,20,4,16,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 138, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,10,12,5,12,6,7,14,6,9,10,7],
[19,0,15,14,11,24,8,10,19,14,15,16,13],
[16,11,0,13,8,17,16,12,15,12,12,11,13],
[14,12,13,0,9,13,6,13,23,20,11,9,17],
[21,15,18,17,0,21,14,10,19,17,10,18,13],
[14,2,9,13,5,0,6,8,17,14,9,5,7],
[20,18,10,20,12,20,0,14,17,16,18,19,15],
[19,16,14,13,16,18,12,0,20,19,11,14,11],
[12,7,11,3,7,9,9,6,0,3,9,8,6],
[20,12,14,6,9,12,10,7,23,0,6,9,9],
[17,11,14,15,16,17,8,15,17,20,0,11,15],
[16,10,15,17,8,21,7,12,18,17,15,0,16],
[19,13,13,9,13,19,11,15,20,17,11,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 139, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,12,10,12,16,5,15,15,9,17,14,13],
[8,0,12,3,15,10,9,7,13,6,15,9,14],
[14,14,0,11,20,11,8,16,15,14,16,14,17],
[16,23,15,0,25,12,14,17,14,14,21,19,19],
[14,11,6,1,0,7,6,15,9,9,13,10,9],
[10,16,15,14,19,0,10,16,15,12,18,13,18],
[21,17,18,12,20,16,0,21,16,21,21,14,15],
[11,19,10,9,11,10,5,0,13,11,17,14,12],
[11,13,11,12,17,11,10,13,0,10,17,14,17],
[17,20,12,12,17,14,5,15,16,0,13,10,17],
[9,11,10,5,13,8,5,9,9,13,0,5,12],
[12,17,12,7,16,13,12,12,12,16,21,0,15],
[13,12,9,7,17,8,11,14,9,9,14,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 140, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,12,8,18,14,7,12,13,14,6,17,4],
[12,0,13,17,16,16,11,12,10,16,5,16,11],
[14,13,0,11,17,15,16,16,9,14,6,16,7],
[18,9,15,0,12,14,16,14,12,15,14,19,8],
[8,10,9,14,0,15,13,15,9,15,4,13,7],
[12,10,11,12,11,0,14,7,15,9,9,13,11],
[19,15,10,10,13,12,0,12,16,12,10,13,14],
[14,14,10,12,11,19,14,0,18,10,13,15,14],
[13,16,17,14,17,11,10,8,0,17,9,15,11],
[12,10,12,11,11,17,14,16,9,0,10,17,10],
[20,21,20,12,22,17,16,13,17,16,0,21,20],
[9,10,10,7,13,13,13,11,11,9,5,0,4],
[22,15,19,18,19,15,12,12,15,16,6,22,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 141, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,19,16,10,11,0,19,11,16,16,11,10],
[15,0,13,13,7,13,5,13,13,18,15,15,15],
[7,13,0,16,10,5,2,16,11,18,10,10,10],
[10,13,10,0,15,2,2,8,3,5,10,10,7],
[16,19,16,11,0,11,8,19,11,11,16,16,16],
[15,13,21,24,15,0,13,21,11,18,18,23,10],
[26,21,24,24,18,13,0,24,11,18,21,21,18],
[7,13,10,18,7,5,2,0,13,10,2,2,10],
[15,13,15,23,15,15,15,13,0,18,10,15,15],
[10,8,8,21,15,8,8,16,8,0,8,10,7],
[10,11,16,16,10,8,5,24,16,18,0,18,10],
[15,11,16,16,10,3,5,24,11,16,8,0,10],
[16,11,16,19,10,16,8,16,11,19,16,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 142, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,8,7,9,12,9,6,12,1,12,9,8],
[16,0,12,10,13,15,12,7,16,8,9,12,14],
[18,14,0,6,12,12,14,9,12,6,16,13,12],
[19,16,20,0,22,17,16,9,17,11,16,15,16],
[17,13,14,4,0,11,10,4,12,5,11,11,7],
[14,11,14,9,15,0,14,7,13,8,15,19,10],
[17,14,12,10,16,12,0,6,11,9,15,10,14],
[20,19,17,17,22,19,20,0,19,13,19,20,14],
[14,10,14,9,14,13,15,7,0,8,13,16,8],
[25,18,20,15,21,18,17,13,18,0,16,21,15],
[14,17,10,10,15,11,11,7,13,10,0,10,11],
[17,14,13,11,15,7,16,6,10,5,16,0,13],
[18,12,14,10,19,16,12,12,18,11,15,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 143, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,7,13,9,9,11,13,8,10,12,10,11],
[16,0,13,16,10,11,13,12,14,16,15,13,15],
[19,13,0,15,13,13,11,13,11,14,14,17,13],
[13,10,11,0,11,12,11,11,10,13,12,11,12],
[17,16,13,15,0,15,15,19,13,17,17,18,21],
[17,15,13,14,11,0,14,16,13,16,17,14,12],
[15,13,15,15,11,12,0,16,13,17,17,16,15],
[13,14,13,15,7,10,10,0,13,14,12,11,16],
[18,12,15,16,13,13,13,13,0,20,16,15,16],
[16,10,12,13,9,10,9,12,6,0,13,12,13],
[14,11,12,14,9,9,9,14,10,13,0,12,13],
[16,13,9,15,8,12,10,15,11,14,14,0,13],
[15,11,13,14,5,14,11,10,10,13,13,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 144, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,0,7,8,2,7,7,16,9,9,2,10],
[11,0,0,0,6,0,0,7,10,7,7,0,1],
[26,26,0,18,18,26,23,24,24,20,20,12,26],
[19,26,8,0,8,18,23,13,16,15,9,18,26],
[18,20,8,18,0,18,17,8,18,8,8,10,18],
[24,26,0,8,8,0,23,14,17,7,8,12,24],
[19,26,3,3,9,3,0,10,19,10,10,12,19],
[19,19,2,13,18,12,16,0,16,12,13,12,19],
[10,16,2,10,8,9,7,10,0,9,10,2,10],
[17,19,6,11,18,19,16,14,17,0,13,18,17],
[17,19,6,17,18,18,16,13,16,13,0,18,17],
[24,26,14,8,16,14,14,14,24,8,8,0,24],
[16,25,0,0,8,2,7,7,16,9,9,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 145, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,8,11,13,10,12,14,5,4,14,11,11],
[19,0,12,11,14,11,11,14,13,11,14,13,13],
[18,14,0,19,19,16,19,18,15,10,12,11,16],
[15,15,7,0,20,14,16,15,13,8,13,10,15],
[13,12,7,6,0,7,8,8,10,7,9,7,7],
[16,15,10,12,19,0,12,15,14,12,13,11,17],
[14,15,7,10,18,14,0,14,12,10,14,10,11],
[12,12,8,11,18,11,12,0,10,8,16,6,13],
[21,13,11,13,16,12,14,16,0,14,12,13,16],
[22,15,16,18,19,14,16,18,12,0,13,13,18],
[12,12,14,13,17,13,12,10,14,13,0,9,19],
[15,13,15,16,19,15,16,20,13,13,17,0,17],
[15,13,10,11,19,9,15,13,10,8,7,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 146, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,14,11,8,16,13,11,13,10,13,11,14],
[14,0,16,13,12,14,15,14,15,15,16,11,12],
[12,10,0,13,11,15,15,12,11,10,15,11,10],
[15,13,13,0,13,13,12,11,15,12,18,11,14],
[18,14,15,13,0,15,16,10,18,12,17,11,14],
[10,12,11,13,11,0,12,8,12,12,13,10,13],
[13,11,11,14,10,14,0,11,13,7,15,7,9],
[15,12,14,15,16,18,15,0,17,12,20,9,15],
[13,11,15,11,8,14,13,9,0,8,12,9,9],
[16,11,16,14,14,14,19,14,18,0,16,13,12],
[13,10,11,8,9,13,11,6,14,10,0,10,11],
[15,15,15,15,15,16,19,17,17,13,16,0,19],
[12,14,16,12,12,13,17,11,17,14,15,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 147, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,15,4,4,4,4,4,11,26,15,0,4],
[11,0,4,11,11,7,4,11,11,15,4,0,4],
[11,22,0,11,11,11,4,11,11,22,22,11,11],
[22,15,15,0,4,15,0,4,26,22,15,11,15],
[22,15,15,22,0,18,15,22,22,22,15,11,15],
[22,19,15,11,8,0,4,4,11,26,15,15,15],
[22,22,22,26,11,22,0,15,26,22,26,22,26],
[22,15,15,22,4,22,11,0,22,22,15,11,15],
[15,15,15,0,4,15,0,4,0,15,11,11,11],
[0,11,4,4,4,0,4,4,11,0,15,0,4],
[11,22,4,11,11,11,0,11,15,11,0,4,4],
[26,26,15,15,15,11,4,15,15,26,22,0,19],
[22,22,15,11,11,11,0,11,15,22,22,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 148, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,9,10,11,16,13,9,15,15,13,12],
[13,0,10,8,9,8,11,14,8,14,12,14,11],
[13,16,0,10,12,14,17,12,9,10,13,16,13],
[17,18,16,0,14,11,14,13,11,16,14,17,15],
[16,17,14,12,0,10,16,15,13,13,15,15,16],
[15,18,12,15,16,0,16,17,15,16,15,19,15],
[10,15,9,12,10,10,0,13,10,15,16,12,13],
[13,12,14,13,11,9,13,0,9,9,14,15,8],
[17,18,17,15,13,11,16,17,0,13,18,16,16],
[11,12,16,10,13,10,11,17,13,0,15,16,10],
[11,14,13,12,11,11,10,12,8,11,0,12,13],
[13,12,10,9,11,7,14,11,10,10,14,0,15],
[14,15,13,11,10,11,13,18,10,16,13,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 149, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,10,10,2,10,8,9,11,8,11,10,8],
[15,0,13,13,3,15,14,11,9,11,11,11,15],
[16,13,0,14,11,26,23,3,14,12,12,13,15],
[16,13,12,0,11,16,14,11,14,19,12,21,10],
[24,23,15,15,0,15,14,15,18,11,11,19,15],
[16,11,0,10,11,0,17,1,14,9,12,11,11],
[18,12,3,12,12,9,0,5,14,14,14,14,5],
[17,15,23,15,11,25,21,0,17,17,13,19,15],
[15,17,12,12,8,12,12,9,0,8,11,8,14],
[18,15,14,7,15,17,12,9,18,0,9,13,8],
[15,15,14,14,15,14,12,13,15,17,0,19,12],
[16,15,13,5,7,15,12,7,18,13,7,0,7],
[18,11,11,16,11,15,21,11,12,18,14,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 150, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,22,14,17,13,14,17,14,16,17,15,18,18],
[4,0,7,14,11,7,15,10,7,9,9,9,12],
[12,19,0,14,11,11,17,10,12,12,11,13,13],
[9,12,12,0,13,8,12,11,12,6,15,14,20],
[13,15,15,13,0,11,14,14,11,14,12,16,18],
[12,19,15,18,15,0,16,13,16,12,16,14,21],
[9,11,9,14,12,10,0,12,12,9,13,13,18],
[12,16,16,15,12,13,14,0,12,11,9,12,20],
[10,19,14,14,15,10,14,14,0,15,16,15,13],
[9,17,14,20,12,14,17,15,11,0,12,13,18],
[11,17,15,11,14,10,13,17,10,14,0,13,18],
[8,17,13,12,10,12,13,14,11,13,13,0,18],
[8,14,13,6,8,5,8,6,13,8,8,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 151, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,12,9,18,11,12,19,16,9,16,23,20],
[10,0,14,8,21,13,15,16,9,13,17,9,19],
[14,12,0,13,18,17,8,21,18,6,19,13,23],
[17,18,13,0,18,16,14,12,15,8,19,16,20],
[8,5,8,8,0,15,4,20,12,4,15,11,21],
[15,13,9,10,11,0,9,16,13,6,13,20,20],
[14,11,18,12,22,17,0,24,17,13,21,14,24],
[7,10,5,14,6,10,2,0,7,7,18,7,14],
[10,17,8,11,14,13,9,19,0,4,13,11,18],
[17,13,20,18,22,20,13,19,22,0,18,14,18],
[10,9,7,7,11,13,5,8,13,8,0,7,11],
[3,17,13,10,15,6,12,19,15,12,19,0,21],
[6,7,3,6,5,6,2,12,8,8,15,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 152, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,15,15,14,11,16,13,19,13,8,15,18],
[11,0,14,10,12,9,17,12,15,13,10,19,14],
[11,12,0,8,16,12,16,8,16,10,9,16,15],
[11,16,18,0,16,13,21,14,14,16,10,18,15],
[12,14,10,10,0,11,16,12,15,12,10,16,17],
[15,17,14,13,15,0,14,14,15,14,10,18,17],
[10,9,10,5,10,12,0,11,11,11,11,18,13],
[13,14,18,12,14,12,15,0,17,11,13,20,15],
[7,11,10,12,11,11,15,9,0,8,10,13,9],
[13,13,16,10,14,12,15,15,18,0,14,19,14],
[18,16,17,16,16,16,15,13,16,12,0,18,17],
[11,7,10,8,10,8,8,6,13,7,8,0,8],
[8,12,11,11,9,9,13,11,17,12,9,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 153, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,9,10,9,6,10,9,9,10,7,14,6],
[16,0,11,11,10,6,7,6,6,12,13,16,13],
[17,15,0,17,12,8,11,11,8,6,7,15,13],
[16,15,9,0,11,7,7,0,6,6,11,11,6],
[17,16,14,15,0,13,12,6,12,11,12,11,7],
[20,20,18,19,13,0,14,13,19,19,16,19,11],
[16,19,15,19,14,12,0,10,12,6,12,11,15],
[17,20,15,26,20,13,16,0,12,6,12,17,22],
[17,20,18,20,14,7,14,14,0,14,16,19,16],
[16,14,20,20,15,7,20,20,12,0,12,25,16],
[19,13,19,15,14,10,14,14,10,14,0,24,20],
[12,10,11,15,15,7,15,9,7,1,2,0,17],
[20,13,13,20,19,15,11,4,10,10,6,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 154, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,13,14,11,11,13,9,16,12,13,15,15],
[11,0,11,12,10,9,10,9,13,11,16,12,15],
[13,15,0,12,9,12,16,14,13,15,13,12,12],
[12,14,14,0,12,16,16,13,16,14,16,17,19],
[15,16,17,14,0,9,18,11,14,13,15,18,17],
[15,17,14,10,17,0,14,12,15,12,16,14,18],
[13,16,10,10,8,12,0,14,13,11,13,11,14],
[17,17,12,13,15,14,12,0,11,14,14,17,14],
[10,13,13,10,12,11,13,15,0,13,12,12,13],
[14,15,11,12,13,14,15,12,13,0,13,14,13],
[13,10,13,10,11,10,13,12,14,13,0,12,13],
[11,14,14,9,8,12,15,9,14,12,14,0,15],
[11,11,14,7,9,8,12,12,13,13,13,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 155, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,19,19,15,20,17,20,17,16,19,16,20],
[13,0,19,17,9,12,14,14,12,11,14,14,19],
[7,7,0,18,12,15,10,11,11,15,12,12,19],
[7,9,8,0,8,5,5,6,7,6,6,11,11],
[11,17,14,18,0,15,12,15,14,10,15,16,18],
[6,14,11,21,11,0,13,11,11,11,16,13,15],
[9,12,16,21,14,13,0,15,12,10,13,16,16],
[6,12,15,20,11,15,11,0,13,9,16,14,16],
[9,14,15,19,12,15,14,13,0,9,9,10,15],
[10,15,11,20,16,15,16,17,17,0,18,19,18],
[7,12,14,20,11,10,13,10,17,8,0,12,14],
[10,12,14,15,10,13,10,12,16,7,14,0,14],
[6,7,7,15,8,11,10,10,11,8,12,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 156, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,13,16,13,15,11,16,12,11,16,15],
[13,0,9,16,16,18,17,15,13,12,13,15,13],
[13,17,0,13,16,16,15,11,12,10,10,14,11],
[13,10,13,0,14,11,9,8,16,10,9,12,12],
[10,10,10,12,0,11,12,9,12,11,10,12,10],
[13,8,10,15,15,0,14,12,12,7,11,11,10],
[11,9,11,17,14,12,0,15,14,10,10,12,9],
[15,11,15,18,17,14,11,0,16,10,12,11,11],
[10,13,14,10,14,14,12,10,0,14,10,14,12],
[14,14,16,16,15,19,16,16,12,0,11,17,13],
[15,13,16,17,16,15,16,14,16,15,0,17,12],
[10,11,12,14,14,15,14,15,12,9,9,0,8],
[11,13,15,14,16,16,17,15,14,13,14,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 157, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,15,19,18,10,14,13,13,13,15,17,17],
[6,0,10,16,15,9,11,12,10,9,12,13,13],
[11,16,0,17,17,12,13,18,12,10,17,16,20],
[7,10,9,0,16,13,12,9,11,3,9,10,13],
[8,11,9,10,0,6,13,11,13,6,9,11,14],
[16,17,14,13,20,0,15,14,12,13,14,10,20],
[12,15,13,14,13,11,0,14,13,8,13,12,18],
[13,14,8,17,15,12,12,0,10,6,8,10,16],
[13,16,14,15,13,14,13,16,0,10,18,15,12],
[13,17,16,23,20,13,18,20,16,0,17,18,22],
[11,14,9,17,17,12,13,18,8,9,0,9,13],
[9,13,10,16,15,16,14,16,11,8,17,0,16],
[9,13,6,13,12,6,8,10,14,4,13,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 158, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,6,13,12,1,12,17,14,12,0,6,12],
[20,0,18,14,16,14,22,26,16,23,8,20,25],
[20,8,0,13,15,3,21,19,16,19,0,15,14],
[13,12,13,0,19,7,19,19,16,16,7,13,18],
[14,10,11,7,0,7,21,26,16,23,7,13,23],
[25,12,23,19,19,0,19,23,20,19,19,19,19],
[14,4,5,7,5,7,0,5,8,11,1,11,10],
[9,0,7,7,0,3,21,0,10,13,0,9,13],
[12,10,10,10,10,6,18,16,0,10,4,12,16],
[14,3,7,10,3,7,15,13,16,0,3,3,15],
[26,18,26,19,19,7,25,26,22,23,0,19,25],
[20,6,11,13,13,7,15,17,14,23,7,0,12],
[14,1,12,8,3,7,16,13,10,11,1,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 159, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,15,12,10,16,12,11,14,12,13,11,12],
[21,0,16,11,11,21,17,20,16,19,19,21,15],
[11,10,0,11,11,22,12,11,9,21,14,14,14],
[14,15,15,0,12,26,13,16,6,22,17,14,14],
[16,15,15,14,0,26,18,14,9,21,16,17,10],
[10,5,4,0,0,0,9,5,2,11,7,11,1],
[14,9,14,13,8,17,0,9,13,15,13,11,12],
[15,6,15,10,12,21,17,0,11,16,16,10,12],
[12,10,17,20,17,24,13,15,0,16,15,18,12],
[14,7,5,4,5,15,11,10,10,0,13,12,12],
[13,7,12,9,10,19,13,10,11,13,0,13,8],
[15,5,12,12,9,15,15,16,8,14,13,0,15],
[14,11,12,12,16,25,14,14,14,14,18,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 160, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,10,17,15,12,16,14,14,15,12,15,14],
[12,0,13,17,15,13,16,14,11,15,13,15,13],
[16,13,0,13,12,9,12,11,10,11,11,13,12],
[9,9,13,0,11,13,11,12,12,14,10,17,11],
[11,11,14,15,0,14,16,12,14,14,14,17,11],
[14,13,17,13,12,0,14,13,10,14,10,12,13],
[10,10,14,15,10,12,0,13,9,10,11,14,10],
[12,12,15,14,14,13,13,0,13,16,11,14,10],
[12,15,16,14,12,16,17,13,0,12,12,14,11],
[11,11,15,12,12,12,16,10,14,0,9,13,7],
[14,13,15,16,12,16,15,15,14,17,0,14,12],
[11,11,13,9,9,14,12,12,12,13,12,0,13],
[12,13,14,15,15,13,16,16,15,19,14,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 161, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,14,16,9,24,13,17,15,11,13,11,15],
[13,0,7,11,13,11,7,14,10,13,14,8,11],
[12,19,0,16,15,23,11,25,15,17,16,16,19],
[10,15,10,0,11,24,14,21,10,15,14,11,22],
[17,13,11,15,0,15,19,21,18,18,14,15,15],
[2,15,3,2,11,0,5,10,6,9,11,1,1],
[13,19,15,12,7,21,0,19,10,13,14,15,19],
[9,12,1,5,5,16,7,0,7,6,5,5,3],
[11,16,11,16,8,20,16,19,0,15,10,14,17],
[15,13,9,11,8,17,13,20,11,0,13,13,11],
[13,12,10,12,12,15,12,21,16,13,0,12,11],
[15,18,10,15,11,25,11,21,12,13,14,0,21],
[11,15,7,4,11,25,7,23,9,15,15,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 162, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,9,10,8,10,13,14,9,12,10,13,12],
[11,0,5,10,8,9,14,11,8,11,7,11,13],
[17,21,0,15,12,15,17,18,14,17,11,20,19],
[16,16,11,0,10,14,19,16,11,13,9,13,11],
[18,18,14,16,0,13,18,18,16,15,13,14,13],
[16,17,11,12,13,0,16,13,12,15,11,18,15],
[13,12,9,7,8,10,0,11,11,13,9,10,10],
[12,15,8,10,8,13,15,0,13,15,10,16,14],
[17,18,12,15,10,14,15,13,0,15,9,13,12],
[14,15,9,13,11,11,13,11,11,0,11,16,13],
[16,19,15,17,13,15,17,16,17,15,0,16,15],
[13,15,6,13,12,8,16,10,13,10,10,0,7],
[14,13,7,15,13,11,16,12,14,13,11,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 163, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,13,13,11,17,17,15,13,15,15,12,16],
[14,0,13,13,14,13,9,13,18,11,10,11,9],
[13,13,0,12,13,16,12,15,13,12,12,16,16],
[13,13,14,0,14,13,10,15,13,12,14,18,15],
[15,12,13,12,0,14,14,14,12,15,12,15,14],
[9,13,10,13,12,0,10,10,12,9,12,12,9],
[9,17,14,16,12,16,0,15,17,12,13,16,14],
[11,13,11,11,12,16,11,0,12,9,16,16,14],
[13,8,13,13,14,14,9,14,0,12,10,14,13],
[11,15,14,14,11,17,14,17,14,0,16,15,17],
[11,16,14,12,14,14,13,10,16,10,0,14,11],
[14,15,10,8,11,14,10,10,12,11,12,0,15],
[10,17,10,11,12,17,12,12,13,9,15,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 164, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,19,8,13,17,12,11,12,15,10,11,14],
[13,0,14,6,14,9,11,11,16,6,9,12,16],
[7,12,0,2,9,5,6,7,12,8,6,8,8],
[18,20,24,0,11,19,18,19,19,20,17,15,20],
[13,12,17,15,0,15,11,11,14,15,14,15,16],
[9,17,21,7,11,0,10,12,15,16,9,12,12],
[14,15,20,8,15,16,0,12,16,19,16,16,18],
[15,15,19,7,15,14,14,0,19,16,12,13,20],
[14,10,14,7,12,11,10,7,0,12,9,10,11],
[11,20,18,6,11,10,7,10,14,0,13,11,15],
[16,17,20,9,12,17,10,14,17,13,0,14,17],
[15,14,18,11,11,14,10,13,16,15,12,0,14],
[12,10,18,6,10,14,8,6,15,11,9,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 165, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,13,8,14,9,9,11,9,10,11,11,13],
[19,0,16,10,17,17,16,15,14,16,19,13,18],
[13,10,0,9,10,7,9,8,10,14,9,7,10],
[18,16,17,0,17,14,16,13,10,18,19,15,15],
[12,9,16,9,0,11,11,8,11,15,11,11,9],
[17,9,19,12,15,0,14,12,16,17,15,10,15],
[17,10,17,10,15,12,0,15,12,15,14,13,13],
[15,11,18,13,18,14,11,0,15,16,15,10,12],
[17,12,16,16,15,10,14,11,0,13,16,12,13],
[16,10,12,8,11,9,11,10,13,0,12,9,11],
[15,7,17,7,15,11,12,11,10,14,0,11,13],
[15,13,19,11,15,16,13,16,14,17,15,0,17],
[13,8,16,11,17,11,13,14,13,15,13,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 166, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,12,13,15,18,16,13,14,10,16,11,14],
[14,0,12,13,14,17,17,14,9,9,16,12,13],
[14,14,0,13,16,19,15,13,15,13,17,16,16],
[13,13,13,0,15,16,13,14,12,11,16,11,12],
[11,12,10,11,0,15,12,11,10,8,14,9,11],
[8,9,7,10,11,0,12,11,10,8,15,6,14],
[10,9,11,13,14,14,0,16,10,11,15,10,13],
[13,12,13,12,15,15,10,0,13,11,19,9,16],
[12,17,11,14,16,16,16,13,0,13,15,10,13],
[16,17,13,15,18,18,15,15,13,0,13,12,14],
[10,10,9,10,12,11,11,7,11,13,0,6,14],
[15,14,10,15,17,20,16,17,16,14,20,0,17],
[12,13,10,14,15,12,13,10,13,12,12,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 167, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,15,3,10,17,16,5,8,5,12,1,8],
[16,0,13,1,2,12,16,7,13,9,9,9,8],
[11,13,0,12,9,18,11,8,12,13,15,11,7],
[23,25,14,0,12,16,21,6,13,19,18,16,7],
[16,24,17,14,0,19,19,7,15,16,17,9,11],
[9,14,8,10,7,0,14,4,6,7,11,9,10],
[10,10,15,5,7,12,0,5,13,10,10,3,6],
[21,19,18,20,19,22,21,0,18,19,23,15,10],
[18,13,14,13,11,20,13,8,0,14,13,13,7],
[21,17,13,7,10,19,16,7,12,0,12,17,6],
[14,17,11,8,9,15,16,3,13,14,0,10,10],
[25,17,15,10,17,17,23,11,13,9,16,0,15],
[18,18,19,19,15,16,20,16,19,20,16,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 168, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,17,13,13,14,17,16,17,14,14,17,14],
[11,0,9,9,11,11,13,18,14,11,8,15,9],
[9,17,0,7,15,12,16,17,15,16,11,17,13],
[13,17,19,0,14,18,19,18,17,16,16,17,15],
[13,15,11,12,0,14,15,14,14,13,12,16,12],
[12,15,14,8,12,0,13,15,15,12,13,14,14],
[9,13,10,7,11,13,0,16,11,11,9,16,11],
[10,8,9,8,12,11,10,0,8,10,7,14,7],
[9,12,11,9,12,11,15,18,0,11,13,20,14],
[12,15,10,10,13,14,15,16,15,0,13,18,11],
[12,18,15,10,14,13,17,19,13,13,0,23,17],
[9,11,9,9,10,12,10,12,6,8,3,0,13],
[12,17,13,11,14,12,15,19,12,15,9,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 169, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,13,17,12,15,15,11,15,16,11,14,17],
[10,0,3,12,7,10,10,5,11,8,5,9,7],
[13,23,0,19,16,15,19,18,19,17,14,16,20],
[9,14,7,0,9,11,11,9,14,11,10,10,9],
[14,19,10,17,0,13,13,12,12,15,19,10,16],
[11,16,11,15,13,0,16,15,15,15,11,13,17],
[11,16,7,15,13,10,0,11,12,11,10,13,11],
[15,21,8,17,14,11,15,0,17,9,9,11,16],
[11,15,7,12,14,11,14,9,0,15,11,9,10],
[10,18,9,15,11,11,15,17,11,0,7,9,16],
[15,21,12,16,7,15,16,17,15,19,0,11,18],
[12,17,10,16,16,13,13,15,17,17,15,0,16],
[9,19,6,17,10,9,15,10,16,10,8,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 170, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,2,2,2,13,15,0,2,11,0,2,13],
[24,0,24,24,24,24,26,11,11,24,11,11,24],
[24,2,0,13,13,13,26,0,2,11,11,2,13],
[24,2,13,0,13,13,26,0,0,11,11,2,13],
[24,2,13,13,0,13,15,0,0,11,0,2,24],
[13,2,13,13,13,0,13,13,13,13,13,13,13],
[11,0,0,0,11,13,0,0,0,11,11,0,11],
[26,15,26,26,26,13,26,0,15,24,24,15,26],
[24,15,24,26,26,13,26,11,0,24,11,15,26],
[15,2,15,15,15,13,15,2,2,0,2,2,15],
[26,15,15,15,26,13,15,2,15,24,0,15,26],
[24,15,24,24,24,13,26,11,11,24,11,0,24],
[13,2,13,13,2,13,15,0,0,11,0,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 171, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,14,14,12,15,12,11,10,13,14,16,14],
[14,0,17,15,12,13,10,15,10,15,16,15,12],
[12,9,0,14,13,15,12,12,11,12,16,16,15],
[12,11,12,0,13,15,11,11,9,14,15,13,14],
[14,14,13,13,0,16,14,15,13,17,17,18,15],
[11,13,11,11,10,0,11,12,12,13,16,16,12],
[14,16,14,15,12,15,0,12,10,16,15,16,14],
[15,11,14,15,11,14,14,0,14,17,14,16,15],
[16,16,15,17,13,14,16,12,0,14,18,14,17],
[13,11,14,12,9,13,10,9,12,0,14,15,12],
[12,10,10,11,9,10,11,12,8,12,0,13,13],
[10,11,10,13,8,10,10,10,12,11,13,0,13],
[12,14,11,12,11,14,12,11,9,14,13,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 172, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,15,15,18,15,16,15,15,15,12,16,13],
[8,0,13,11,10,10,10,11,14,10,12,10,9],
[11,13,0,10,10,11,9,9,10,11,10,10,10],
[11,15,16,0,13,12,11,12,13,14,14,15,14],
[8,16,16,13,0,12,9,12,11,10,13,11,8],
[11,16,15,14,14,0,11,14,13,14,13,11,12],
[10,16,17,15,17,15,0,15,14,13,18,16,14],
[11,15,17,14,14,12,11,0,14,12,13,14,12],
[11,12,16,13,15,13,12,12,0,11,12,11,14],
[11,16,15,12,16,12,13,14,15,0,12,13,13],
[14,14,16,12,13,13,8,13,14,14,0,13,15],
[10,16,16,11,15,15,10,12,15,13,13,0,11],
[13,17,16,12,18,14,12,14,12,13,11,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 173, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,12,12,6,10,11,12,10,15,11,7,13],
[17,0,13,16,8,15,16,16,9,16,11,12,19],
[14,13,0,12,12,17,16,12,11,14,14,11,15],
[14,10,14,0,9,15,11,12,11,12,11,10,15],
[20,18,14,17,0,20,17,15,10,18,17,15,19],
[16,11,9,11,6,0,9,9,8,16,14,10,15],
[15,10,10,15,9,17,0,9,15,15,14,11,15],
[14,10,14,14,11,17,17,0,13,14,15,11,16],
[16,17,15,15,16,18,11,13,0,18,18,16,16],
[11,10,12,14,8,10,11,12,8,0,12,11,13],
[15,15,12,15,9,12,12,11,8,14,0,11,14],
[19,14,15,16,11,16,15,15,10,15,15,0,16],
[13,7,11,11,7,11,11,10,10,13,12,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 174, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,14,14,11,14,9,21,9,17,13,14,12],
[12,0,17,12,15,16,11,18,14,14,14,15,15],
[12,9,0,11,12,13,9,18,9,12,15,14,10],
[12,14,15,0,11,15,10,16,11,16,14,14,11],
[15,11,14,15,0,13,11,14,11,14,14,13,14],
[12,10,13,11,13,0,9,20,8,11,12,13,9],
[17,15,17,16,15,17,0,18,17,17,12,18,15],
[5,8,8,10,12,6,8,0,4,12,7,8,8],
[17,12,17,15,15,18,9,22,0,17,19,23,14],
[9,12,14,10,12,15,9,14,9,0,13,11,11],
[13,12,11,12,12,14,14,19,7,13,0,11,16],
[12,11,12,12,13,13,8,18,3,15,15,0,12],
[14,11,16,15,12,17,11,18,12,15,10,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 175, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,12,24,19,24,22,21,20,22,15,20,19,14],
[14,0,26,21,19,14,21,14,19,21,26,19,8],
[2,0,0,2,3,8,4,8,8,10,8,5,2],
[7,5,24,0,15,8,19,13,17,15,8,19,7],
[2,7,23,11,0,17,11,17,10,10,15,14,11],
[4,12,18,18,9,0,18,14,10,19,19,18,11],
[5,5,22,7,15,8,0,11,6,8,6,17,0],
[6,12,18,13,9,12,15,0,14,10,15,18,6],
[4,7,18,9,16,16,20,12,0,10,15,13,9],
[11,5,16,11,16,7,18,16,16,0,15,9,6],
[6,0,18,18,11,7,20,11,11,11,0,11,6],
[7,7,21,7,12,8,9,8,13,17,15,0,7],
[12,18,24,19,15,15,26,20,17,20,20,19,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 176, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,17,15,20,8,18,15,13,17,11,17,14],
[16,0,16,14,21,14,19,15,9,19,14,17,18],
[9,10,0,9,11,12,6,13,7,9,10,9,8],
[11,12,17,0,12,12,15,17,12,13,13,11,14],
[6,5,15,14,0,6,15,16,7,17,10,9,13],
[18,12,14,14,20,0,19,16,8,18,19,15,19],
[8,7,20,11,11,7,0,18,13,19,8,9,12],
[11,11,13,9,10,10,8,0,13,15,11,7,13],
[13,17,19,14,19,18,13,13,0,16,16,13,20],
[9,7,17,13,9,8,7,11,10,0,10,5,14],
[15,12,16,13,16,7,18,15,10,16,0,13,9],
[9,9,17,15,17,11,17,19,13,21,13,0,13],
[12,8,18,12,13,7,14,13,6,12,17,13,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 177, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,20,19,15,14,15,16,17,12,13,17,19],
[9,0,13,11,11,13,15,11,9,7,8,11,16],
[6,13,0,11,10,4,11,16,9,8,12,13,13],
[7,15,15,0,13,13,10,15,16,17,12,15,15],
[11,15,16,13,0,11,15,15,9,9,7,14,17],
[12,13,22,13,15,0,14,15,13,17,16,17,20],
[11,11,15,16,11,12,0,15,14,13,14,16,15],
[10,15,10,11,11,11,11,0,12,16,15,13,10],
[9,17,17,10,17,13,12,14,0,13,8,14,15],
[14,19,18,9,17,9,13,10,13,0,10,14,12],
[13,18,14,14,19,10,12,11,18,16,0,15,16],
[9,15,13,11,12,9,10,13,12,12,11,0,12],
[7,10,13,11,9,6,11,16,11,14,10,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 178, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,14,21,15,19,13,19,14,18,13,15,17],
[9,0,7,14,11,10,8,11,10,9,9,8,9],
[12,19,0,20,11,14,11,19,12,12,12,18,11],
[5,12,6,0,13,11,11,16,11,12,11,10,7],
[11,15,15,13,0,6,6,11,12,11,6,12,8],
[7,16,12,15,20,0,11,16,11,13,8,11,7],
[13,18,15,15,20,15,0,17,16,17,14,17,14],
[7,15,7,10,15,10,9,0,9,9,6,13,7],
[12,16,14,15,14,15,10,17,0,14,11,16,9],
[8,17,14,14,15,13,9,17,12,0,12,13,9],
[13,17,14,15,20,18,12,20,15,14,0,16,12],
[11,18,8,16,14,15,9,13,10,13,10,0,9],
[9,17,15,19,18,19,12,19,17,17,14,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 179, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,15,14,11,12,9,13,11,9,17,7],
[13,0,19,18,12,10,17,16,13,11,14,13,12],
[13,7,0,14,13,9,11,9,13,11,15,12,12],
[11,8,12,0,13,11,12,10,10,12,10,14,8],
[12,14,13,13,0,11,15,11,13,11,14,16,12],
[15,16,17,15,15,0,18,14,18,12,15,22,15],
[14,9,15,14,11,8,0,8,10,14,14,13,8],
[17,10,17,16,15,12,18,0,18,9,16,16,17],
[13,13,13,16,13,8,16,8,0,12,15,14,13],
[15,15,15,14,15,14,12,17,14,0,14,15,15],
[17,12,11,16,12,11,12,10,11,12,0,14,12],
[9,13,14,12,10,4,13,10,12,11,12,0,10],
[19,14,14,18,14,11,18,9,13,11,14,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 180, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,17,11,17,8,10,17,7,13,13,14,14,17],
[9,0,14,10,11,7,14,8,7,8,10,11,12],
[15,12,0,16,12,14,16,11,12,13,15,16,15],
[9,16,10,0,10,11,13,8,6,12,12,12,14],
[18,15,14,16,0,18,17,14,9,15,21,20,19],
[16,19,12,15,8,0,18,10,8,15,17,12,16],
[9,12,10,13,9,8,0,6,6,14,7,7,10],
[19,18,15,18,12,16,20,0,12,17,19,20,23],
[13,19,14,20,17,18,20,14,0,14,17,19,18],
[13,18,13,14,11,11,12,9,12,0,14,15,12],
[12,16,11,14,5,9,19,7,9,12,0,14,15],
[12,15,10,14,6,14,19,6,7,11,12,0,16],
[9,14,11,12,7,10,16,3,8,14,11,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 181, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,14,13,14,15,9,15,9,11,8,13,11],
[11,0,12,14,15,10,10,18,11,10,9,12,8],
[12,14,0,13,16,13,10,17,15,11,9,13,16],
[13,12,13,0,13,8,11,10,8,8,9,12,10],
[12,11,10,13,0,7,10,15,7,9,10,13,10],
[11,16,13,18,19,0,12,19,13,13,13,15,14],
[17,16,16,15,16,14,0,18,10,13,8,13,15],
[11,8,9,16,11,7,8,0,9,9,8,6,11],
[17,15,11,18,19,13,16,17,0,8,11,13,14],
[15,16,15,18,17,13,13,17,18,0,13,15,15],
[18,17,17,17,16,13,18,18,15,13,0,14,16],
[13,14,13,14,13,11,13,20,13,11,12,0,12],
[15,18,10,16,16,12,11,15,12,11,10,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 182, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,14,16,13,12,12,13,14,14,14,17,12],
[12,0,12,15,15,13,10,10,12,16,11,14,11],
[12,14,0,18,18,14,16,13,17,14,16,16,14],
[10,11,8,0,11,15,10,11,14,9,11,12,12],
[13,11,8,15,0,13,9,10,11,13,12,13,11],
[14,13,12,11,13,0,11,13,12,13,15,16,12],
[14,16,10,16,17,15,0,14,17,19,15,14,13],
[13,16,13,15,16,13,12,0,14,12,12,13,13],
[12,14,9,12,15,14,9,12,0,16,12,12,12],
[12,10,12,17,13,13,7,14,10,0,12,12,9],
[12,15,10,15,14,11,11,14,14,14,0,13,13],
[9,12,10,14,13,10,12,13,14,14,13,0,10],
[14,15,12,14,15,14,13,13,14,17,13,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 183, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,16,15,14,15,12,15,16,15,16,16,16],
[10,0,15,15,12,16,16,17,16,12,15,17,13],
[10,11,0,13,7,14,12,15,13,12,18,14,16],
[11,11,13,0,11,14,15,14,14,13,17,17,13],
[12,14,19,15,0,18,17,16,15,13,17,20,15],
[11,10,12,12,8,0,10,13,13,14,15,13,14],
[14,10,14,11,9,16,0,16,13,13,14,16,15],
[11,9,11,12,10,13,10,0,9,10,12,12,11],
[10,10,13,12,11,13,13,17,0,12,12,16,12],
[11,14,14,13,13,12,13,16,14,0,15,16,14],
[10,11,8,9,9,11,12,14,14,11,0,17,16],
[10,9,12,9,6,13,10,14,10,10,9,0,10],
[10,13,10,13,11,12,11,15,14,12,10,16,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 184, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,13,14,12,12,11,14,10,18,13,15,16],
[12,0,10,7,8,9,10,10,9,12,7,14,11],
[13,16,0,12,12,10,9,11,10,15,12,12,17],
[12,19,14,0,13,16,16,12,12,19,15,17,15],
[14,18,14,13,0,16,16,16,12,19,16,16,17],
[14,17,16,10,10,0,13,16,14,19,16,17,14],
[15,16,17,10,10,13,0,18,8,20,16,16,16],
[12,16,15,14,10,10,8,0,11,18,14,15,14],
[16,17,16,14,14,12,18,15,0,19,16,16,15],
[8,14,11,7,7,7,6,8,7,0,10,10,14],
[13,19,14,11,10,10,10,12,10,16,0,12,13],
[11,12,14,9,10,9,10,11,10,16,14,0,11],
[10,15,9,11,9,12,10,12,11,12,13,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 185, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,18,21,12,14,17,12,23,22,17,13,20],
[8,0,11,8,0,5,12,13,15,8,9,3,3],
[8,15,0,18,9,9,14,12,15,14,14,10,17],
[5,18,8,0,4,10,17,17,17,19,7,5,11],
[14,26,17,22,0,14,20,13,21,22,18,19,17],
[12,21,17,16,12,0,15,17,21,20,12,11,15],
[9,14,12,9,6,11,0,13,26,6,13,9,12],
[14,13,14,9,13,9,13,0,18,18,13,9,9],
[3,11,11,9,5,5,0,8,0,5,5,5,8],
[4,18,12,7,4,6,20,8,21,0,8,12,7],
[9,17,12,19,8,14,13,13,21,18,0,13,16],
[13,23,16,21,7,15,17,17,21,14,13,0,21],
[6,23,9,15,9,11,14,17,18,19,10,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 186, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,9,14,1,8,6,11,5,10,3,8,13],
[10,0,10,12,4,9,6,13,5,7,7,4,8],
[17,16,0,6,1,10,6,8,8,8,1,3,8],
[12,14,20,0,1,7,6,17,11,14,3,11,13],
[25,22,25,25,0,21,14,19,17,22,13,21,21],
[18,17,16,19,5,0,7,14,13,9,3,9,12],
[20,20,20,20,12,19,0,17,10,16,6,18,23],
[15,13,18,9,7,12,9,0,8,15,6,15,17],
[21,21,18,15,9,13,16,18,0,19,8,12,17],
[16,19,18,12,4,17,10,11,7,0,1,14,19],
[23,19,25,23,13,23,20,20,18,25,0,23,23],
[18,22,23,15,5,17,8,11,14,12,3,0,12],
[13,18,18,13,5,14,3,9,9,7,3,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 187, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,14,15,16,11,11,9,17,13,11,12,11],
[18,0,16,10,17,16,11,13,16,13,9,10,18],
[12,10,0,12,19,16,8,12,18,13,9,15,17],
[11,16,14,0,13,13,6,10,15,9,13,11,14],
[10,9,7,13,0,10,4,7,16,13,11,10,12],
[15,10,10,13,16,0,12,11,16,11,8,7,14],
[15,15,18,20,22,14,0,13,22,13,16,14,19],
[17,13,14,16,19,15,13,0,19,13,14,15,19],
[9,10,8,11,10,10,4,7,0,6,8,9,12],
[13,13,13,17,13,15,13,13,20,0,11,14,15],
[15,17,17,13,15,18,10,12,18,15,0,13,16],
[14,16,11,15,16,19,12,11,17,12,13,0,12],
[15,8,9,12,14,12,7,7,14,11,10,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 188, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,17,11,12,10,14,11,6,14,14,11,17],
[11,0,18,12,12,13,12,21,9,14,20,14,16],
[9,8,0,18,7,15,1,9,10,8,14,12,9],
[15,14,8,0,14,15,8,14,10,12,13,8,15],
[14,14,19,12,0,12,11,14,12,10,19,8,19],
[16,13,11,11,14,0,10,9,6,8,17,13,19],
[12,14,25,18,15,16,0,14,9,14,14,14,20],
[15,5,17,12,12,17,12,0,8,4,17,14,14],
[20,17,16,16,14,20,17,18,0,17,13,17,20],
[12,12,18,14,16,18,12,22,9,0,20,14,21],
[12,6,12,13,7,9,12,9,13,6,0,15,15],
[15,12,14,18,18,13,12,12,9,12,11,0,17],
[9,10,17,11,7,7,6,12,6,5,11,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 189, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,13,17,13,16,14,15,10,13,15,8,19],
[13,0,15,20,14,19,17,14,22,20,18,15,22],
[13,11,0,17,11,21,11,14,20,20,21,13,18],
[9,6,9,0,10,13,7,9,12,13,13,11,15],
[13,12,15,16,0,19,15,11,12,14,23,14,17],
[10,7,5,13,7,0,13,11,11,13,13,8,13],
[12,9,15,19,11,13,0,16,15,15,19,11,16],
[11,12,12,17,15,15,10,0,13,15,16,11,13],
[16,4,6,14,14,15,11,13,0,10,18,13,18],
[13,6,6,13,12,13,11,11,16,0,18,10,18],
[11,8,5,13,3,13,7,10,8,8,0,5,11],
[18,11,13,15,12,18,15,15,13,16,21,0,20],
[7,4,8,11,9,13,10,13,8,8,15,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 190, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,13,18,16,12,17,16,20,13,23,20,14,12],
[13,0,10,15,9,15,16,18,14,18,16,10,9],
[8,16,0,9,11,10,15,14,9,12,9,6,13],
[10,11,17,0,17,13,14,15,10,19,14,7,12],
[14,17,15,9,0,13,16,17,13,20,17,10,12],
[9,11,16,13,13,0,14,14,14,18,18,11,9],
[10,10,11,12,10,12,0,14,9,14,8,5,13],
[6,8,12,11,9,12,12,0,9,14,11,11,9],
[13,12,17,16,13,12,17,17,0,18,21,14,9],
[3,8,14,7,6,8,12,12,8,0,15,5,7],
[6,10,17,12,9,8,18,15,5,11,0,9,12],
[12,16,20,19,16,15,21,15,12,21,17,0,9],
[14,17,13,14,14,17,13,17,17,19,14,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 191, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,13,12,16,17,19,11,14,9,15,15,20],
[10,0,15,5,11,13,11,5,8,8,5,11,18],
[13,11,0,9,11,14,17,9,10,13,11,16,15],
[14,21,17,0,18,19,17,18,12,17,15,21,19],
[10,15,15,8,0,16,15,7,12,11,10,11,15],
[9,13,12,7,10,0,19,6,13,12,12,7,13],
[7,15,9,9,11,7,0,8,7,11,3,11,13],
[15,21,17,8,19,20,18,0,14,13,11,17,23],
[12,18,16,14,14,13,19,12,0,9,16,16,19],
[17,18,13,9,15,14,15,13,17,0,14,16,17],
[11,21,15,11,16,14,23,15,10,12,0,13,19],
[11,15,10,5,15,19,15,9,10,10,13,0,15],
[6,8,11,7,11,13,13,3,7,9,7,11,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 192, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,14,14,10,10,10,10,0,10,10,14,0],
[16,0,16,4,16,12,4,26,4,12,0,16,12],
[12,10,0,14,10,10,10,10,0,10,10,14,0],
[12,22,12,0,12,12,22,22,12,22,22,12,12],
[16,10,16,14,0,10,10,10,0,22,10,16,12],
[16,14,16,14,16,0,14,14,4,22,10,16,16],
[16,22,16,4,16,12,0,26,4,12,10,16,12],
[16,0,16,4,16,12,0,0,4,12,0,16,12],
[26,22,26,14,26,22,22,22,0,22,10,26,12],
[16,14,16,4,4,4,14,14,4,0,10,4,4],
[16,26,16,4,16,16,16,26,16,16,0,16,16],
[12,10,12,14,10,10,10,10,0,22,10,0,12],
[26,14,26,14,14,10,14,14,14,22,10,14,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 193, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,13,12,12,14,15,17,12,8,13,13,12],
[11,0,11,21,16,17,15,17,14,17,12,16,14],
[13,15,0,20,12,14,15,19,16,16,17,16,12],
[14,5,6,0,10,12,8,10,10,6,9,12,6],
[14,10,14,16,0,13,14,14,10,15,12,17,8],
[12,9,12,14,13,0,8,13,13,9,9,20,10],
[11,11,11,18,12,18,0,14,13,11,12,16,12],
[9,9,7,16,12,13,12,0,10,13,12,13,7],
[14,12,10,16,16,13,13,16,0,10,8,15,11],
[18,9,10,20,11,17,15,13,16,0,13,19,12],
[13,14,9,17,14,17,14,14,18,13,0,21,14],
[13,10,10,14,9,6,10,13,11,7,5,0,11],
[14,12,14,20,18,16,14,19,15,14,12,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 194, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,20,20,17,20,20,23,13,13,13,20,10,16],
[6,0,10,13,16,16,9,6,12,16,9,13,12],
[6,16,0,20,26,16,12,3,12,16,6,16,12],
[9,13,6,0,13,9,9,9,9,6,9,13,6],
[6,10,0,13,0,10,6,3,9,7,3,16,9],
[6,10,10,17,16,0,16,6,6,6,13,13,9],
[3,17,14,17,20,10,0,10,3,13,17,13,13],
[13,20,23,17,23,20,16,0,16,16,13,13,9],
[13,14,14,17,17,20,23,10,0,10,17,13,10],
[13,10,10,20,19,20,13,10,16,0,10,16,16],
[6,17,20,17,23,13,9,13,9,16,0,13,16],
[16,13,10,13,10,13,13,13,13,10,13,0,16],
[10,14,14,20,17,17,13,17,16,10,10,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 195, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,25,1,18,5,13,14,4,18,14,26,9,11],
[1,0,1,5,1,14,1,5,6,14,17,5,12],
[25,25,0,18,25,13,18,4,25,13,26,18,20],
[8,21,8,0,8,14,10,5,22,14,26,1,8],
[21,25,1,18,0,14,19,5,19,14,26,5,12],
[13,12,13,12,12,0,6,4,12,10,13,6,13],
[12,25,8,16,7,20,0,11,16,14,26,12,11],
[22,21,22,21,21,22,15,0,21,10,22,15,22],
[8,20,1,4,7,14,10,5,0,14,21,5,12],
[12,12,13,12,12,16,12,16,12,0,13,12,12],
[0,9,0,0,0,13,0,4,5,13,0,0,0],
[17,21,8,25,21,20,14,11,21,14,26,0,11],
[15,14,6,18,14,13,15,4,14,14,26,15,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 196, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,18,19,11,10,14,16,15,17,16,18,18,14],
[8,0,14,9,7,9,12,17,10,12,14,10,3],
[7,12,0,12,10,15,15,5,12,12,14,11,11],
[15,17,14,0,12,7,16,15,15,16,15,16,10],
[16,19,16,14,0,15,15,14,15,14,15,18,13],
[12,17,11,19,11,0,11,13,17,15,15,15,12],
[10,14,11,10,11,15,0,11,10,10,13,15,7],
[11,9,21,11,12,13,15,0,11,13,17,13,11],
[9,16,14,11,11,9,16,15,0,12,12,12,9],
[10,14,14,10,12,11,16,13,14,0,15,12,9],
[8,12,12,11,11,11,13,9,14,11,0,13,11],
[8,16,15,10,8,11,11,13,14,14,13,0,9],
[12,23,15,16,13,14,19,15,17,17,15,17,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 197, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,15,9,14,14,12,19,17,13,11,7,12,13],
[11,0,11,8,11,7,14,17,7,11,8,7,14],
[17,15,0,14,13,13,20,16,19,11,14,12,8],
[12,18,12,0,17,14,16,21,16,9,12,10,16],
[12,15,13,9,0,9,13,12,15,3,9,8,9],
[14,19,13,12,17,0,18,22,17,11,18,10,18],
[7,12,6,10,13,8,0,12,6,9,4,6,8],
[9,9,10,5,14,4,14,0,7,12,8,6,14],
[13,19,7,10,11,9,20,19,0,10,4,9,10],
[15,15,15,17,23,15,17,14,16,0,17,16,11],
[19,18,12,14,17,8,22,18,22,9,0,13,13],
[14,19,14,16,18,16,20,20,17,10,13,0,16],
[13,12,18,10,17,8,18,12,16,15,13,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 198, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,14,18,13,17,18,13,15,11,16,18,20,18],
[12,0,14,11,16,11,8,18,7,10,16,18,14],
[8,12,0,11,11,12,7,11,8,13,15,16,11],
[13,15,15,0,14,13,14,17,15,12,17,19,15],
[9,10,15,12,0,15,10,7,10,12,14,16,12],
[8,15,14,13,11,0,7,14,10,15,19,19,13],
[13,18,19,12,16,19,0,16,12,15,19,18,15],
[11,8,15,9,19,12,10,0,12,12,14,19,14],
[15,19,18,11,16,16,14,14,0,16,17,17,16],
[10,16,13,14,14,11,11,14,10,0,19,16,14],
[8,10,11,9,12,7,7,12,9,7,0,17,12],
[6,8,10,7,10,7,8,7,9,10,9,0,8],
[8,12,15,11,14,13,11,12,10,12,14,18,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 199, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,16,18,16,20,13,15,13,14,18,11,15,14],
[10,0,14,13,12,13,12,16,16,15,14,11,11],
[8,12,0,10,10,5,11,13,10,11,9,10,9],
[10,13,16,0,19,16,13,14,15,18,14,15,11],
[6,14,16,7,0,11,9,10,15,14,11,11,9],
[13,13,21,10,15,0,14,19,15,16,10,13,14],
[11,14,15,13,17,12,0,13,15,16,12,15,16],
[13,10,13,12,16,7,13,0,11,14,12,11,9],
[12,10,16,11,11,11,11,15,0,11,11,8,13],
[8,11,15,8,12,10,10,12,15,0,11,10,9],
[15,12,17,12,15,16,14,14,15,15,0,13,15],
[11,15,16,11,15,13,11,15,18,16,13,0,14],
[12,15,17,15,17,12,10,17,13,17,11,12,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 26, 200, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbrcwd/mebbrcwd_13_26.csv", index=False, header=False)