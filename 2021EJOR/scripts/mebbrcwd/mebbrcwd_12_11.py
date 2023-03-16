
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg
from kemeny import sc

rep = 1
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,5,4,4,5,6,4,5,3,5,4,6],
[6,0,5,4,6,7,4,7,5,5,5,6],
[7,6,0,4,5,7,6,7,4,6,8,7],
[7,7,7,0,7,6,6,6,3,6,7,8],
[6,5,6,4,0,8,6,7,6,5,5,7],
[5,4,4,5,3,0,4,5,4,5,6,5],
[7,7,5,5,5,7,0,7,6,6,5,7],
[6,4,4,5,4,6,4,0,4,4,8,5],
[8,6,7,8,5,7,5,7,0,7,7,7],
[6,6,5,5,6,6,5,7,4,0,6,5],
[7,6,3,4,6,5,6,3,4,5,0,6],
[5,5,4,3,4,6,4,6,4,6,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 1, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,4,3,5,5,4,3,6,3,4,3],
[6,0,7,8,7,8,6,5,9,5,7,2],
[7,4,0,4,4,9,5,6,9,7,7,4],
[8,3,7,0,5,7,4,5,8,5,5,3],
[6,4,7,6,0,7,6,5,6,6,6,6],
[6,3,2,4,4,0,2,3,7,5,2,5],
[7,5,6,7,5,9,0,5,7,6,7,3],
[8,6,5,6,6,8,6,0,6,5,7,2],
[5,2,2,3,5,4,4,5,0,3,4,2],
[8,6,4,6,5,6,5,6,8,0,7,3],
[7,4,4,6,5,9,4,4,7,4,0,6],
[8,9,7,8,5,6,8,9,9,8,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 2, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,10,10,10,7,7,5,3,6,10,8],
[4,0,5,11,6,8,8,9,4,6,7,8],
[1,6,0,11,7,6,5,4,1,4,10,6],
[1,0,0,0,4,0,0,3,1,1,7,3],
[1,5,4,7,0,4,7,3,0,3,4,3],
[4,3,5,11,7,0,5,4,4,4,10,6],
[4,3,6,11,4,6,0,4,4,4,8,3],
[6,2,7,8,8,7,7,0,6,8,7,3],
[8,7,10,10,11,7,7,5,0,6,10,8],
[5,5,7,10,8,7,7,3,5,0,10,5],
[1,4,1,4,7,1,3,4,1,1,0,4],
[3,3,5,8,8,5,8,8,3,6,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 3, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,6,4,7,8,8,8,8,8,6,4],
[6,0,5,7,6,9,7,6,6,4,6,6],
[5,6,0,4,9,6,7,7,6,4,6,5],
[7,4,7,0,10,10,7,6,9,7,6,3],
[4,5,2,1,0,5,5,1,3,2,2,4],
[3,2,5,1,6,0,5,5,5,5,5,3],
[3,4,4,4,6,6,0,4,6,4,4,4],
[3,5,4,5,10,6,7,0,4,4,9,3],
[3,5,5,2,8,6,5,7,0,7,7,3],
[3,7,7,4,9,6,7,7,4,0,6,3],
[5,5,5,5,9,6,7,2,4,5,0,5],
[7,5,6,8,7,8,7,8,8,8,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 4, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,9,5,6,6,5,6,6,8,6,7],
[7,0,9,4,4,6,11,4,6,9,7,6],
[2,2,0,3,2,5,2,3,2,5,4,4],
[6,7,8,0,3,6,10,4,5,8,6,8],
[5,7,9,8,0,9,7,10,7,10,8,9],
[5,5,6,5,2,0,5,6,4,5,6,5],
[6,0,9,1,4,6,0,4,3,7,6,5],
[5,7,8,7,1,5,7,0,5,7,8,7],
[5,5,9,6,4,7,8,6,0,6,8,8],
[3,2,6,3,1,6,4,4,5,0,6,4],
[5,4,7,5,3,5,5,3,3,5,0,7],
[4,5,7,3,2,6,6,4,3,7,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 5, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,6,3,6,3,4,3,3,2,6,2],
[5,0,6,4,5,3,3,5,4,2,6,5],
[5,5,0,2,6,3,4,6,4,3,3,4],
[8,7,9,0,9,6,7,9,6,5,6,8],
[5,6,5,2,0,3,4,5,3,2,4,3],
[8,8,8,5,8,0,4,7,7,4,9,6],
[7,8,7,4,7,7,0,4,5,6,7,4],
[8,6,5,2,6,4,7,0,6,4,6,5],
[8,7,7,5,8,4,6,5,0,3,8,5],
[9,9,8,6,9,7,5,7,8,0,8,7],
[5,5,8,5,7,2,4,5,3,3,0,3],
[9,6,7,3,8,5,7,6,6,4,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 6, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,6,6,6,6,4,2,7,5,4,7],
[3,0,4,5,6,5,1,2,6,6,5,5],
[5,7,0,4,6,5,1,0,6,6,5,3],
[5,6,7,0,9,6,3,3,6,4,3,4],
[5,5,5,2,0,5,3,3,6,4,4,3],
[5,6,6,5,6,0,6,6,5,5,5,6],
[7,10,10,8,8,5,0,6,8,6,5,8],
[9,9,11,8,8,5,5,0,6,6,7,7],
[4,5,5,5,5,6,3,5,0,3,4,3],
[6,5,5,7,7,6,5,5,8,0,5,7],
[7,6,6,8,7,6,6,4,7,6,0,7],
[4,6,8,7,8,5,3,4,8,4,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 7, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,4,3,7,7,4,4,7,10,7,7],
[3,0,3,6,7,7,4,3,3,6,3,6],
[7,8,0,3,8,7,7,7,7,11,7,8],
[8,5,8,0,8,4,8,7,4,11,4,8],
[4,4,3,3,0,7,4,3,3,3,3,6],
[4,4,4,7,4,0,4,3,3,7,3,7],
[7,7,4,3,7,7,0,7,7,10,7,7],
[7,8,4,4,8,8,4,0,3,7,8,4],
[4,8,4,7,8,8,4,8,0,7,8,4],
[1,5,0,0,8,4,1,4,4,0,4,8],
[4,8,4,7,8,8,4,3,3,7,0,7],
[4,5,3,3,5,4,4,7,7,3,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 8, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,5,5,5,5,4,4,4,4,4,4],
[8,0,8,8,6,7,6,8,6,7,5,5],
[6,3,0,5,5,4,4,5,3,4,2,5],
[6,3,6,0,5,7,6,5,4,5,5,5],
[6,5,6,6,0,6,6,6,6,4,5,7],
[6,4,7,4,5,0,7,3,5,4,4,5],
[7,5,7,5,5,4,0,4,5,6,5,6],
[7,3,6,6,5,8,7,0,5,6,5,4],
[7,5,8,7,5,6,6,6,0,6,5,5],
[7,4,7,6,7,7,5,5,5,0,4,4],
[7,6,9,6,6,7,6,6,6,7,0,5],
[7,6,6,6,4,6,5,7,6,7,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 9, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,6,8,5,7,3,8,4,5,7,7],
[6,0,6,3,4,3,5,5,7,2,2,4],
[5,5,0,7,5,7,4,5,5,5,5,5],
[3,8,4,0,5,10,5,5,6,8,4,4],
[6,7,6,6,0,7,6,9,8,5,4,4],
[4,8,4,1,4,0,4,3,6,5,1,3],
[8,6,7,6,5,7,0,10,8,5,6,5],
[3,6,6,6,2,8,1,0,6,6,4,5],
[7,4,6,5,3,5,3,5,0,4,5,4],
[6,9,6,3,6,6,6,5,7,0,3,5],
[4,9,6,7,7,10,5,7,6,8,0,6],
[4,7,6,7,7,8,6,6,7,6,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 10, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,4,3,5,8,7,8,5,10,6,8],
[6,0,5,5,6,7,8,6,5,8,8,6],
[7,6,0,8,4,9,8,8,8,9,9,7],
[8,6,3,0,4,7,8,7,8,11,7,7],
[6,5,7,7,0,7,8,5,8,8,8,6],
[3,4,2,4,4,0,7,4,4,5,7,3],
[4,3,3,3,3,4,0,6,5,9,6,1],
[3,5,3,4,6,7,5,0,8,8,5,3],
[6,6,3,3,3,7,6,3,0,11,6,4],
[1,3,2,0,3,6,2,3,0,0,3,0],
[5,3,2,4,3,4,5,6,5,8,0,4],
[3,5,4,4,5,8,10,8,7,11,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 11, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,5,6,2,4,5,6,6,3,2,2],
[6,0,6,5,1,3,2,6,2,2,2,2],
[6,5,0,3,2,3,2,6,3,3,2,2],
[5,6,8,0,2,3,2,5,4,4,2,2],
[9,10,9,9,0,6,5,5,11,4,5,9],
[7,8,8,8,5,0,5,9,9,6,5,8],
[6,9,9,9,6,6,0,6,6,4,6,5],
[5,5,5,6,6,2,5,0,6,6,1,5],
[5,9,8,7,0,2,5,5,0,2,1,0],
[8,9,8,7,7,5,7,5,9,0,5,7],
[9,9,9,9,6,6,5,10,10,6,0,8],
[9,9,9,9,2,3,6,6,11,4,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 12, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,4,2,4,7,3,4,5,3,4,2],
[5,0,3,0,1,4,1,0,1,2,1,1],
[7,8,0,2,6,7,8,7,6,3,7,6],
[9,11,9,0,6,9,7,9,7,3,6,7],
[7,10,5,5,0,6,5,8,7,7,8,6],
[4,7,4,2,5,0,2,4,5,3,5,2],
[8,10,3,4,6,9,0,7,8,3,5,5],
[7,11,4,2,3,7,4,0,7,4,3,2],
[6,10,5,4,4,6,3,4,0,3,3,3],
[8,9,8,8,4,8,8,7,8,0,5,8],
[7,10,4,5,3,6,6,8,8,6,0,5],
[9,10,5,4,5,9,6,9,8,3,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 13, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,6,3,3,5,6,6,6,4,5,5],
[5,0,4,5,4,4,5,2,6,4,3,3],
[5,7,0,3,5,6,9,5,7,5,5,7],
[8,6,8,0,6,7,7,7,8,5,8,7],
[8,7,6,5,0,6,7,5,7,6,3,6],
[6,7,5,4,5,0,6,5,5,5,4,4],
[5,6,2,4,4,5,0,3,5,3,1,3],
[5,9,6,4,6,6,8,0,9,6,3,8],
[5,5,4,3,4,6,6,2,0,5,4,4],
[7,7,6,6,5,6,8,5,6,0,5,7],
[6,8,6,3,8,7,10,8,7,6,0,7],
[6,8,4,4,5,7,8,3,7,4,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 14, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,2,7,1,5,2,6,4,5,6,2],
[6,0,2,6,1,3,3,3,4,1,6,2],
[9,9,0,7,3,5,2,4,4,3,6,3],
[4,5,4,0,3,8,3,4,2,3,7,3],
[10,10,8,8,0,7,6,8,6,6,9,5],
[6,8,6,3,4,0,3,6,5,3,4,5],
[9,8,9,8,5,8,0,8,6,4,8,4],
[5,8,7,7,3,5,3,0,3,3,7,3],
[7,7,7,9,5,6,5,8,0,5,8,6],
[6,10,8,8,5,8,7,8,6,0,8,6],
[5,5,5,4,2,7,3,4,3,3,0,3],
[9,9,8,8,6,6,7,8,5,5,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 15, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,7,7,7,4,6,4,5,7,5,8],
[4,0,2,4,7,5,4,6,6,5,7,11],
[4,9,0,9,9,6,8,6,5,9,7,11],
[4,7,2,0,6,7,3,6,3,9,5,8],
[4,4,2,5,0,6,5,4,2,4,2,6],
[7,6,5,4,5,0,7,4,6,4,4,9],
[5,7,3,8,6,4,0,4,4,7,6,8],
[7,5,5,5,7,7,7,0,7,5,3,7],
[6,5,6,8,9,5,7,4,0,6,6,8],
[4,6,2,2,7,7,4,6,5,0,5,8],
[6,4,4,6,9,7,5,8,5,6,0,6],
[3,0,0,3,5,2,3,4,3,3,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 16, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,6,6,11,1,10,6,11,10,11,6],
[5,0,5,6,5,6,5,10,10,5,6,10],
[5,6,0,1,6,6,5,6,11,5,6,5],
[5,5,10,0,5,5,5,10,10,10,6,10],
[0,6,5,6,0,1,5,5,11,10,6,5],
[10,5,5,6,10,0,10,5,10,10,11,5],
[1,6,6,6,6,1,0,6,6,10,1,6],
[5,1,5,1,6,6,5,0,6,5,6,0],
[0,1,0,1,0,1,5,5,0,5,6,0],
[1,6,6,1,1,1,1,6,6,0,1,6],
[0,5,5,5,5,0,10,5,5,10,0,5],
[5,1,6,1,6,6,5,11,11,5,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 17, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,6,3,6,1,2,2,3,6,8,1],
[6,0,6,5,8,4,3,4,5,7,9,3],
[5,5,0,4,4,4,2,2,3,5,8,1],
[8,6,7,0,6,6,5,6,9,9,6,5],
[5,3,7,5,0,2,3,3,7,7,10,2],
[10,7,7,5,9,0,3,3,6,7,8,2],
[9,8,9,6,8,8,0,4,5,6,8,8],
[9,7,9,5,8,8,7,0,8,8,8,7],
[8,6,8,2,4,5,6,3,0,7,7,3],
[5,4,6,2,4,4,5,3,4,0,5,4],
[3,2,3,5,1,3,3,3,4,6,0,2],
[10,8,10,6,9,9,3,4,8,7,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 18, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,2,0,3,1,2,7,5,5,3,7],
[11,0,3,5,7,9,6,7,9,5,7,7],
[9,8,0,4,9,9,6,9,9,9,11,11],
[11,6,7,0,7,11,10,7,9,5,7,7],
[8,4,2,4,0,4,6,11,9,9,10,11],
[10,2,2,0,7,0,6,7,9,5,7,7],
[9,5,5,1,5,5,0,5,9,5,5,5],
[4,4,2,4,0,4,6,0,9,5,2,7],
[6,2,2,2,2,2,2,2,0,5,2,2],
[6,6,2,6,2,6,6,6,6,0,2,6],
[8,4,0,4,1,4,6,9,9,9,0,9],
[4,4,0,4,0,4,6,4,9,5,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 19, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,6,5,6,4,7,3,6,6,5,6],
[6,0,8,6,5,4,7,6,5,6,5,5],
[5,3,0,6,6,5,6,5,6,5,6,6],
[6,5,5,0,5,6,7,7,6,5,4,3],
[5,6,5,6,0,8,7,7,8,5,6,4],
[7,7,6,5,3,0,5,8,7,3,6,6],
[4,4,5,4,4,6,0,7,6,5,2,4],
[8,5,6,4,4,3,4,0,6,3,4,5],
[5,6,5,5,3,4,5,5,0,2,4,6],
[5,5,6,6,6,8,6,8,9,0,6,4],
[6,6,5,7,5,5,9,7,7,5,0,6],
[5,6,5,8,7,5,7,6,5,7,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 20, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,5,5,8,7,6,5,7,8,8,9],
[5,0,5,3,6,3,3,2,7,4,6,3],
[6,6,0,4,6,5,7,4,8,6,5,7],
[6,8,7,0,6,7,4,6,7,7,8,6],
[3,5,5,5,0,5,5,6,6,6,6,8],
[4,8,6,4,6,0,3,4,6,7,5,5],
[5,8,4,7,6,8,0,7,7,7,5,7],
[6,9,7,5,5,7,4,0,9,7,8,7],
[4,4,3,4,5,5,4,2,0,5,6,7],
[3,7,5,4,5,4,4,4,6,0,6,3],
[3,5,6,3,5,6,6,3,5,5,0,6],
[2,8,4,5,3,6,4,4,4,8,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 21, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,5,5,2,6,3,6,6,7,6,4],
[5,0,5,5,2,4,4,4,4,8,2,4],
[6,6,0,9,6,6,4,5,6,4,3,6],
[6,6,2,0,2,4,2,5,4,4,3,4],
[9,9,5,9,0,6,4,8,6,8,8,8],
[5,7,5,7,5,0,6,7,9,8,7,5],
[8,7,7,9,7,5,0,7,8,6,5,7],
[5,7,6,6,3,4,4,0,6,6,3,7],
[5,7,5,7,5,2,3,5,0,6,7,6],
[4,3,7,7,3,3,5,5,5,0,4,4],
[5,9,8,8,3,4,6,8,4,7,0,8],
[7,7,5,7,3,6,4,4,5,7,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 22, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,6,7,5,9,6,6,6,6,7,6],
[5,0,3,4,5,6,5,5,3,5,4,5],
[5,8,0,6,7,9,8,6,5,7,7,4],
[4,7,5,0,5,6,8,6,4,5,6,4],
[6,6,4,6,0,6,8,4,6,6,6,6],
[2,5,2,5,5,0,5,5,5,4,6,2],
[5,6,3,3,3,6,0,4,4,5,3,4],
[5,6,5,5,7,6,7,0,5,6,6,2],
[5,8,6,7,5,6,7,6,0,7,5,5],
[5,6,4,6,5,7,6,5,4,0,6,3],
[4,7,4,5,5,5,8,5,6,5,0,2],
[5,6,7,7,5,9,7,9,6,8,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 23, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,6,6,4,5,7,4,3,6,6,6],
[7,0,5,8,4,5,6,6,6,6,4,4],
[5,6,0,7,2,5,7,6,4,8,9,8],
[5,3,4,0,3,4,6,5,3,8,5,3],
[7,7,9,8,0,8,7,9,4,10,9,8],
[6,6,6,7,3,0,5,6,5,7,7,6],
[4,5,4,5,4,6,0,6,5,8,5,4],
[7,5,5,6,2,5,5,0,6,9,7,8],
[8,5,7,8,7,6,6,5,0,8,7,6],
[5,5,3,3,1,4,3,2,3,0,4,5],
[5,7,2,6,2,4,6,4,4,7,0,4],
[5,7,3,8,3,5,7,3,5,6,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 24, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,7,5,10,9,5,6,8,4,7,6],
[5,0,6,6,9,9,5,3,8,8,6,6],
[4,5,0,7,8,8,6,7,9,6,9,7],
[6,5,4,0,7,8,6,7,9,6,6,7],
[1,2,3,4,0,5,4,3,7,4,2,5],
[2,2,3,3,6,0,5,3,6,4,5,1],
[6,6,5,5,7,6,0,7,7,5,6,6],
[5,8,4,4,8,8,4,0,9,7,6,7],
[3,3,2,2,4,5,4,2,0,5,4,3],
[7,3,5,5,7,7,6,4,6,0,5,4],
[4,5,2,5,9,6,5,5,7,6,0,5],
[5,5,4,4,6,10,5,4,8,7,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 25, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,11,7,3,0,11,11,7,4,3,7],
[4,0,4,7,7,4,4,8,8,4,3,0],
[0,7,0,7,3,0,7,7,4,4,3,0],
[4,4,4,0,4,4,4,8,8,8,4,4],
[8,4,8,7,0,8,8,8,8,4,0,4],
[11,7,11,7,3,0,11,11,7,7,3,7],
[0,7,4,7,3,0,0,8,4,4,3,0],
[0,3,4,3,3,0,3,0,4,0,3,0],
[4,3,7,3,3,4,7,7,0,0,3,3],
[7,7,7,3,7,4,7,11,11,0,7,7],
[8,8,8,7,11,8,8,8,8,4,0,4],
[4,11,11,7,7,4,11,11,8,4,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 26, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,7,4,6,7,4,5,4,4,4,4],
[6,0,9,5,5,4,10,5,9,10,7,9],
[4,2,0,5,4,5,7,6,5,7,5,7],
[7,6,6,0,5,4,7,6,6,9,6,6],
[5,6,7,6,0,8,8,6,8,8,6,8],
[4,7,6,7,3,0,7,6,7,7,7,7],
[7,1,4,4,3,4,0,5,4,7,5,7],
[6,6,5,5,5,5,6,0,5,8,2,5],
[7,2,6,5,3,4,7,6,0,8,6,10],
[7,1,4,2,3,4,4,3,3,0,2,3],
[7,4,6,5,5,4,6,9,5,9,0,8],
[7,2,4,5,3,4,4,6,1,8,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 27, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,2,4,8,8,6,6,6,6,2,6],
[7,0,2,8,6,6,6,6,6,6,6,6],
[9,9,0,6,8,8,8,6,4,6,6,6],
[7,3,5,0,9,9,9,7,7,6,7,9],
[3,5,3,2,0,6,6,4,4,4,0,7],
[3,5,3,2,5,0,5,7,3,4,3,7],
[5,5,3,2,5,6,0,6,7,4,2,9],
[5,5,5,4,7,4,5,0,5,2,5,7],
[5,5,7,4,7,8,4,6,0,6,4,11],
[5,5,5,5,7,7,7,9,5,0,5,9],
[9,5,5,4,11,8,9,6,7,6,0,11],
[5,5,5,2,4,4,2,4,0,2,0,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 28, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,3,3,3,1,4,4,7,4,3,5],
[4,0,4,2,5,3,4,5,6,7,2,5],
[8,7,0,4,4,2,3,5,8,5,5,7],
[8,9,7,0,6,5,6,7,8,8,8,7],
[8,6,7,5,0,6,6,6,6,5,6,6],
[10,8,9,6,5,0,6,6,9,6,9,8],
[7,7,8,5,5,5,0,10,7,7,4,8],
[7,6,6,4,5,5,1,0,6,5,4,5],
[4,5,3,3,5,2,4,5,0,5,4,3],
[7,4,6,3,6,5,4,6,6,0,5,7],
[8,9,6,3,5,2,7,7,7,6,0,7],
[6,6,4,4,5,3,3,6,8,4,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 29, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,7,6,7,3,1,10,10,7,8,6],
[2,0,2,3,3,3,1,7,5,3,2,3],
[4,9,0,3,4,3,3,10,7,3,5,5],
[5,8,8,0,6,5,4,10,10,5,7,9],
[4,8,7,5,0,5,5,7,4,5,5,5],
[8,8,8,6,6,0,9,10,8,7,5,9],
[10,10,8,7,6,2,0,10,10,8,7,10],
[1,4,1,1,4,1,1,0,4,1,1,1],
[1,6,4,1,7,3,1,7,0,1,1,1],
[4,8,8,6,6,4,3,10,10,0,7,8],
[3,9,6,4,6,6,4,10,10,4,0,6],
[5,8,6,2,6,2,1,10,10,3,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 30, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,8,2,8,8,3,8,2,5,5,0],
[9,0,11,3,11,11,6,8,8,6,11,6],
[3,0,0,0,8,8,3,8,5,3,0,3],
[9,8,11,0,11,11,3,8,8,9,8,9],
[3,0,3,0,0,3,3,8,2,3,0,3],
[3,0,3,0,8,0,3,8,5,3,0,3],
[8,5,8,8,8,8,0,11,8,8,8,6],
[3,3,3,3,3,3,0,0,5,6,3,3],
[9,3,6,3,9,6,3,6,0,9,6,6],
[6,5,8,2,8,8,3,5,2,0,5,3],
[6,0,11,3,11,11,3,8,5,6,0,3],
[11,5,8,2,8,8,5,8,5,8,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 31, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,3,6,3,6,6,9,6,3,6,8],
[3,0,3,6,2,2,4,3,6,3,0,7],
[8,8,0,6,7,5,6,8,8,6,7,10],
[5,5,5,0,5,5,1,5,5,2,5,5],
[8,9,4,6,0,5,4,8,8,6,6,5],
[5,9,6,6,6,0,4,5,9,6,3,6],
[5,7,5,10,7,7,0,8,5,5,5,10],
[2,8,3,6,3,6,3,0,6,5,5,5],
[5,5,3,6,3,2,6,5,0,6,3,7],
[8,8,5,9,5,5,6,6,5,0,7,10],
[5,11,4,6,5,8,6,6,8,4,0,7],
[3,4,1,6,6,5,1,6,4,1,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 32, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,7,9,7,9,9,7,9,7,5,9],
[4,0,5,8,5,9,9,3,4,4,4,8],
[4,6,0,4,4,4,4,6,4,6,4,4],
[2,3,7,0,3,7,7,3,1,3,6,7],
[4,6,7,8,0,8,8,6,8,10,8,8],
[2,2,7,4,3,0,6,2,4,2,4,4],
[2,2,7,4,3,5,0,2,0,2,4,4],
[4,8,5,8,5,9,9,0,8,4,4,8],
[2,7,7,10,3,7,11,3,0,2,6,11],
[4,7,5,8,1,9,9,7,9,0,4,9],
[6,7,7,5,3,7,7,7,5,7,0,5],
[2,3,7,4,3,7,7,3,0,2,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 33, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,8,1,1,2,5,1,3,1,2,11],
[9,0,9,6,5,3,5,6,2,5,7,9],
[3,2,0,2,4,4,4,2,4,2,3,6],
[10,5,9,0,7,4,7,6,4,6,7,10],
[10,6,7,4,0,2,5,4,2,2,7,10],
[9,8,7,7,9,0,5,7,2,5,10,9],
[6,6,7,4,6,6,0,4,6,6,7,10],
[10,5,9,5,7,4,7,0,2,5,7,10],
[8,9,7,7,9,9,5,9,0,3,8,8],
[10,6,9,5,9,6,5,6,8,0,8,11],
[9,4,8,4,4,1,4,4,3,3,0,9],
[0,2,5,1,1,2,1,1,3,0,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 34, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,6,4,5,4,6,4,6,7,7,9],
[4,0,6,4,6,6,6,6,8,7,7,9],
[5,5,0,5,7,5,5,5,6,7,5,7],
[7,7,6,0,7,7,9,5,8,9,7,7],
[6,5,4,4,0,2,6,6,6,7,5,7],
[7,5,6,4,9,0,8,4,6,7,7,7],
[5,5,6,2,5,3,0,2,6,7,3,5],
[7,5,6,6,5,7,9,0,4,9,7,9],
[5,3,5,3,5,5,5,7,0,7,5,7],
[4,4,4,2,4,4,4,2,4,0,5,6],
[4,4,6,4,6,4,8,4,6,6,0,6],
[2,2,4,4,4,4,6,2,4,5,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 35, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,10,8,8,3,3,7,4,7,7,4],
[4,0,4,1,4,0,3,7,1,5,4,2],
[1,7,0,1,3,2,3,6,3,6,6,4],
[3,10,10,0,11,3,3,10,2,7,6,3],
[3,7,8,0,0,2,3,6,2,6,6,3],
[8,11,9,8,9,0,7,7,6,9,5,9],
[8,8,8,8,8,4,0,7,4,8,5,9],
[4,4,5,1,5,4,4,0,3,6,5,2],
[7,10,8,9,9,5,7,8,0,8,5,5],
[4,6,5,4,5,2,3,5,3,0,6,4],
[4,7,5,5,5,6,6,6,6,5,0,5],
[7,9,7,8,8,2,2,9,6,7,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 36, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,5,3,2,3,3,8,6,2,5,1],
[5,0,6,6,3,1,1,7,6,7,1,5],
[6,5,0,4,2,2,4,3,6,3,6,0],
[8,5,7,0,2,2,4,7,6,3,6,0],
[9,8,9,9,0,4,4,11,9,9,4,8],
[8,10,9,9,7,0,4,11,11,10,10,7],
[8,10,7,7,7,7,0,8,10,8,10,5],
[3,4,8,4,0,0,3,0,4,3,3,3],
[5,5,5,5,2,0,1,7,0,3,3,0],
[9,4,8,8,2,1,3,8,8,0,3,1],
[6,10,5,5,7,1,1,8,8,8,0,5],
[10,6,11,11,3,4,6,8,11,10,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 37, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,1,7,5,5,2,2,3,6,2,2],
[7,0,3,7,5,9,4,4,5,6,4,4],
[10,8,0,6,6,9,4,6,7,8,4,8],
[4,4,5,0,7,5,2,6,5,4,0,4],
[6,6,5,4,0,7,6,4,5,6,4,6],
[6,2,2,6,4,0,2,6,7,4,2,4],
[9,7,7,9,5,9,0,9,7,7,5,7],
[9,7,5,5,7,5,2,0,5,7,2,8],
[8,6,4,6,6,4,4,6,0,6,4,6],
[5,5,3,7,5,7,4,4,5,0,6,6],
[9,7,7,11,7,9,6,9,7,5,0,6],
[9,7,3,7,5,7,4,3,5,5,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 38, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,6,7,8,7,6,5,10,6,7,9],
[2,0,8,3,5,6,2,3,5,3,5,5],
[5,3,0,3,5,4,5,6,4,3,2,5],
[4,8,8,0,5,6,3,4,6,5,3,7],
[3,6,6,6,0,4,1,2,7,3,5,6],
[4,5,7,5,7,0,3,4,6,5,3,7],
[5,9,6,8,10,8,0,4,10,7,7,10],
[6,8,5,7,9,7,7,0,7,4,6,9],
[1,6,7,5,4,5,1,4,0,6,6,7],
[5,8,8,6,8,6,4,7,5,0,5,7],
[4,6,9,8,6,8,4,5,5,6,0,8],
[2,6,6,4,5,4,1,2,4,4,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 39, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,3,1,5,3,3,7,1,7,3,3],
[8,0,4,4,8,6,7,11,7,9,6,6],
[8,7,0,4,8,6,8,10,5,9,6,7],
[10,7,7,0,10,7,7,11,5,9,7,9],
[6,3,3,1,0,3,1,8,3,5,3,4],
[8,5,5,4,8,0,5,8,3,7,5,7],
[8,4,3,4,10,6,0,9,6,9,9,9],
[4,0,1,0,3,3,2,0,2,5,3,3],
[10,4,6,6,8,8,5,9,0,9,6,8],
[4,2,2,2,6,4,2,6,2,0,2,2],
[8,5,5,4,8,6,2,8,5,9,0,4],
[8,5,4,2,7,4,2,8,3,9,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 40, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,7,8,5,8,8,0,1,5,5,8],
[6,0,3,6,4,6,10,6,7,10,7,11],
[4,8,0,4,1,4,8,3,4,8,4,8],
[3,5,7,0,5,3,8,0,4,4,4,11],
[6,7,10,6,0,3,10,3,4,7,6,10],
[3,5,7,8,8,0,8,3,4,7,4,8],
[3,1,3,3,1,3,0,0,1,4,1,8],
[11,5,8,11,8,8,11,0,8,11,11,11],
[10,4,7,7,7,7,10,3,0,7,10,7],
[6,1,3,7,4,4,7,0,4,0,7,11],
[6,4,7,7,5,7,10,0,1,4,0,7],
[3,0,3,0,1,3,3,0,4,0,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 41, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,6,3,7,1,3,2,6,5,4,6],
[3,0,6,3,3,2,3,1,7,5,2,7],
[5,5,0,3,5,5,6,5,7,6,1,5],
[8,8,8,0,8,5,6,6,8,8,6,7],
[4,8,6,3,0,3,1,2,5,7,3,5],
[10,9,6,6,8,0,4,5,7,10,5,8],
[8,8,5,5,10,7,0,6,6,8,5,5],
[9,10,6,5,9,6,5,0,7,9,6,7],
[5,4,4,3,6,4,5,4,0,7,1,6],
[6,6,5,3,4,1,3,2,4,0,1,4],
[7,9,10,5,8,6,6,5,10,10,0,8],
[5,4,6,4,6,3,6,4,5,7,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 42, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,8,8,10,6,10,7,8,6,8,6],
[7,0,4,7,6,6,6,6,4,7,4,4],
[3,7,0,8,5,3,10,7,5,7,3,8],
[3,4,3,0,6,5,7,4,5,3,3,3],
[1,5,6,5,0,3,10,2,7,4,3,5],
[5,5,8,6,8,0,11,7,6,7,5,7],
[1,5,1,4,1,0,0,1,3,5,1,5],
[4,5,4,7,9,4,10,0,7,4,1,6],
[3,7,6,6,4,5,8,4,0,6,3,8],
[5,4,4,8,7,4,6,7,5,0,4,4],
[3,7,8,8,8,6,10,10,8,7,0,8],
[5,7,3,8,6,4,6,5,3,7,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 43, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,6,5,6,4,8,8,6,4,8,7],
[8,0,4,5,6,4,8,8,6,5,6,6],
[5,7,0,7,5,6,4,7,8,6,6,6],
[6,6,4,0,7,7,6,9,9,7,9,8],
[5,5,6,4,0,5,4,3,4,5,5,6],
[7,7,5,4,6,0,7,8,8,3,10,7],
[3,3,7,5,7,4,0,7,5,4,8,9],
[3,3,4,2,8,3,4,0,3,3,7,8],
[5,5,3,2,7,3,6,8,0,2,7,6],
[7,6,5,4,6,8,7,8,9,0,10,6],
[3,5,5,2,6,1,3,4,4,1,0,4],
[4,5,5,3,5,4,2,3,5,5,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 44, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,4,4,0,4,2,2,6,2,4,0],
[7,0,6,9,5,7,5,5,7,5,6,4],
[7,5,0,5,1,5,3,6,6,3,2,3],
[7,2,6,0,6,8,3,5,3,1,6,1],
[11,6,10,5,0,8,7,6,8,5,9,5],
[7,4,6,3,3,0,4,3,3,3,3,3],
[9,6,8,8,4,7,0,5,8,3,9,6],
[9,6,5,6,5,8,6,0,8,6,5,5],
[5,4,5,8,3,8,3,3,0,3,5,0],
[9,6,8,10,6,8,8,5,8,0,9,8],
[7,5,9,5,2,8,2,6,6,2,0,3],
[11,7,8,10,6,8,5,6,11,3,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 45, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,6,4,4,7,6,4,7,6,4,2],
[6,0,7,5,7,8,5,4,8,7,7,4],
[5,4,0,3,4,6,3,6,6,5,4,4],
[7,6,8,0,8,9,6,4,7,8,4,3],
[7,4,7,3,0,7,4,5,4,7,3,4],
[4,3,5,2,4,0,4,5,7,3,2,2],
[5,6,8,5,7,7,0,6,9,6,5,3],
[7,7,5,7,6,6,5,0,4,7,4,6],
[4,3,5,4,7,4,2,7,0,5,3,4],
[5,4,6,3,4,8,5,4,6,0,3,2],
[7,4,7,7,8,9,6,7,8,8,0,4],
[9,7,7,8,7,9,8,5,7,9,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 46, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,6,5,7,8,7,4,8,6,8,7],
[2,0,3,6,2,1,4,4,1,3,2,3],
[5,8,0,9,5,7,8,8,8,7,5,7],
[6,5,2,0,5,5,3,2,4,5,5,3],
[4,9,6,6,0,5,7,6,6,4,5,5],
[3,10,4,6,6,0,5,6,8,4,6,5],
[4,7,3,8,4,6,0,6,6,6,3,4],
[7,7,3,9,5,5,5,0,5,5,5,5],
[3,10,3,7,5,3,5,6,0,6,4,6],
[5,8,4,6,7,7,5,6,5,0,8,6],
[3,9,6,6,6,5,8,6,7,3,0,6],
[4,8,4,8,6,6,7,6,5,5,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 47, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,8,10,7,5,5,7,5,8,4,10],
[4,0,8,9,7,8,3,9,8,9,7,6],
[3,3,0,6,4,2,1,3,3,3,1,7],
[1,2,5,0,4,5,0,4,6,5,4,7],
[4,4,7,7,0,5,3,7,4,7,4,5],
[6,3,9,6,6,0,6,6,3,6,6,6],
[6,8,10,11,8,5,0,11,8,11,7,7],
[4,2,8,7,4,5,0,0,3,8,5,7],
[6,3,8,5,7,8,3,8,0,8,3,6],
[3,2,8,6,4,5,0,3,3,0,4,6],
[7,4,10,7,7,5,4,6,8,7,0,8],
[1,5,4,4,6,5,4,4,5,5,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 48, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,4,6,3,5,5,5,4,6,4,4],
[6,0,4,7,5,4,5,4,3,6,5,5],
[7,7,0,8,7,7,3,5,7,6,6,5],
[5,4,3,0,3,4,4,2,3,3,6,3],
[8,6,4,8,0,6,4,6,6,7,7,6],
[6,7,4,7,5,0,5,5,6,5,5,3],
[6,6,8,7,7,6,0,4,5,5,7,5],
[6,7,6,9,5,6,7,0,6,7,7,6],
[7,8,4,8,5,5,6,5,0,6,7,5],
[5,5,5,8,4,6,6,4,5,0,6,6],
[7,6,5,5,4,6,4,4,4,5,0,4],
[7,6,6,8,5,8,6,5,6,5,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 49, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,7,7,9,7,7,5,10,7,9,5],
[4,0,6,6,11,8,6,5,8,4,5,6],
[4,5,0,6,7,6,10,5,6,0,5,6],
[4,5,5,0,7,7,5,3,6,3,5,5],
[2,0,4,4,0,0,6,3,4,2,4,4],
[4,3,5,4,11,0,7,5,8,3,5,7],
[4,5,1,6,5,4,0,1,6,0,3,6],
[6,6,6,8,8,6,10,0,6,4,4,6],
[1,3,5,5,7,3,5,5,0,5,3,5],
[4,7,11,8,9,8,11,7,6,0,9,6],
[2,6,6,6,7,6,8,7,8,2,0,4],
[6,5,5,6,7,4,5,5,6,5,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 50, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,5,5,10,6,5,10,2,4,1,5],
[4,0,4,4,4,4,4,10,1,4,4,4],
[6,7,0,5,6,6,6,7,6,10,7,5],
[6,7,6,0,7,6,7,7,2,10,7,6],
[1,7,5,4,0,6,6,11,2,5,1,4],
[5,7,5,5,5,0,5,10,2,5,5,5],
[6,7,5,4,5,6,0,7,2,5,1,4],
[1,1,4,4,0,1,4,0,1,5,0,4],
[9,10,5,9,9,9,9,10,0,9,10,9],
[7,7,1,1,6,6,6,6,2,0,6,1],
[10,7,4,4,10,6,10,11,1,5,0,4],
[6,7,6,5,7,6,7,7,2,10,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 51, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,10,5,6,6,10,5,5,10,10,6],
[11,0,11,6,6,6,11,6,5,10,11,6],
[1,0,0,5,6,1,6,0,0,10,11,1],
[6,5,6,0,11,6,11,5,5,5,11,6],
[5,5,5,0,0,1,10,0,0,5,10,1],
[5,5,10,5,10,0,10,10,10,10,10,6],
[1,0,5,0,1,1,0,0,0,5,6,1],
[6,5,11,6,11,1,11,0,0,10,11,6],
[6,6,11,6,11,1,11,11,0,11,11,6],
[1,1,1,6,6,1,6,1,0,0,6,1],
[1,0,0,0,1,1,5,0,0,5,0,1],
[5,5,10,5,10,5,10,5,5,10,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 52, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,5,2,3,1,7,3,0,4,7,2],
[0,0,0,0,0,0,6,0,0,3,3,0],
[6,11,0,5,6,3,10,9,6,7,7,4],
[9,11,6,0,6,6,7,9,3,7,7,4],
[8,11,5,5,0,4,8,8,4,8,5,5],
[10,11,8,5,7,0,7,7,3,8,7,5],
[4,5,1,4,3,4,0,4,4,4,4,2],
[8,11,2,2,3,4,7,0,3,7,4,5],
[11,11,5,8,7,8,7,8,0,11,7,8],
[7,8,4,4,3,3,7,4,0,0,7,1],
[4,8,4,4,6,4,7,7,4,4,0,1],
[9,11,7,7,6,6,9,6,3,10,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 53, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,8,6,5,6,6,7,5,7,6,9],
[6,0,5,7,5,5,5,6,4,5,6,7],
[3,6,0,7,4,4,6,6,3,7,6,8],
[5,4,4,0,3,3,3,6,4,4,4,5],
[6,6,7,8,0,5,7,6,6,8,7,9],
[5,6,7,8,6,0,4,6,3,7,5,6],
[5,6,5,8,4,7,0,8,5,6,6,5],
[4,5,5,5,5,5,3,0,4,6,5,5],
[6,7,8,7,5,8,6,7,0,6,6,8],
[4,6,4,7,3,4,5,5,5,0,5,6],
[5,5,5,7,4,6,5,6,5,6,0,7],
[2,4,3,6,2,5,6,6,3,5,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 54, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,8,7,7,6,7,8,6,3,7,6],
[6,0,7,10,8,8,5,9,6,8,8,6],
[3,4,0,6,8,7,3,9,5,5,5,5],
[4,1,5,0,4,6,2,7,6,4,6,6],
[4,3,3,7,0,7,4,6,6,6,6,7],
[5,3,4,5,4,0,6,8,8,3,6,6],
[4,6,8,9,7,5,0,8,6,4,7,7],
[3,2,2,4,5,3,3,0,5,3,7,5],
[5,5,6,5,5,3,5,6,0,4,8,3],
[8,3,6,7,5,8,7,8,7,0,9,8],
[4,3,6,5,5,5,4,4,3,2,0,3],
[5,5,6,5,4,5,4,6,8,3,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 55, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,7,6,5,6,3,6,5,6,4,6],
[8,0,11,7,10,6,3,6,6,7,6,8],
[4,0,0,4,4,2,1,1,1,3,2,2],
[5,4,7,0,6,5,3,6,2,5,5,4],
[6,1,7,5,0,3,1,4,3,4,3,6],
[5,5,9,6,8,0,5,5,7,4,5,5],
[8,8,10,8,10,6,0,9,5,7,9,8],
[5,5,10,5,7,6,2,0,5,5,4,5],
[6,5,10,9,8,4,6,6,0,6,7,8],
[5,4,8,6,7,7,4,6,5,0,5,6],
[7,5,9,6,8,6,2,7,4,6,0,6],
[5,3,9,7,5,6,3,6,3,5,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 56, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,3,7,6,10,6,10,3,7,7],
[1,0,0,3,8,4,4,1,7,0,4,7],
[1,11,0,4,8,4,5,1,7,1,7,7],
[8,8,7,0,11,11,7,4,7,7,11,7],
[4,3,3,0,0,6,3,3,3,3,7,7],
[5,7,7,0,5,0,7,1,7,7,8,4],
[1,7,6,4,8,4,0,1,6,4,7,7],
[5,10,10,7,8,10,10,0,10,7,11,7],
[1,4,4,4,8,4,5,1,0,4,7,8],
[8,11,10,4,8,4,7,4,7,0,7,7],
[4,7,4,0,4,3,4,0,4,4,0,4],
[4,4,4,4,4,7,4,4,3,4,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 57, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,6,7,3,6,2,5,5,7,9,9],
[5,0,6,10,7,5,4,10,7,8,5,6],
[5,5,0,5,2,3,2,4,3,4,4,6],
[4,1,6,0,7,4,3,4,7,8,6,3],
[8,4,9,4,0,8,7,6,7,9,8,6],
[5,6,8,7,3,0,2,5,7,8,7,9],
[9,7,9,8,4,9,0,7,7,10,10,10],
[6,1,7,7,5,6,4,0,8,8,6,7],
[6,4,8,4,4,4,4,3,0,5,6,7],
[4,3,7,3,2,3,1,3,6,0,5,6],
[2,6,7,5,3,4,1,5,5,6,0,8],
[2,5,5,8,5,2,1,4,4,5,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 58, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,7,4,3,7,8,6,6,7,7,6],
[4,0,8,2,4,7,3,6,3,7,4,5],
[4,3,0,1,4,5,4,5,3,3,3,3],
[7,9,10,0,5,8,8,6,7,8,7,7],
[8,7,7,6,0,5,7,9,6,6,9,7],
[4,4,6,3,6,0,3,4,3,4,4,4],
[3,8,7,3,4,8,0,4,6,8,5,6],
[5,5,6,5,2,7,7,0,6,5,6,6],
[5,8,8,4,5,8,5,5,0,6,5,5],
[4,4,8,3,5,7,3,6,5,0,5,5],
[4,7,8,4,2,7,6,5,6,6,0,6],
[5,6,8,4,4,7,5,5,6,6,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 59, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,4,3,7,5,7,0,3,7,4,6],
[7,0,7,7,8,5,11,5,5,5,6,7],
[7,4,0,5,5,4,8,3,4,7,7,7],
[8,4,6,0,6,7,8,5,6,7,7,8],
[4,3,6,5,0,3,6,0,4,7,5,6],
[6,6,7,4,8,0,8,6,6,7,6,8],
[4,0,3,3,5,3,0,3,2,3,3,1],
[11,6,8,6,11,5,8,0,6,7,10,9],
[8,6,7,5,7,5,9,5,0,5,5,7],
[4,6,4,4,4,4,8,4,6,0,4,6],
[7,5,4,4,6,5,8,1,6,7,0,9],
[5,4,4,3,5,3,10,2,4,5,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 60, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,4,3,3,2,3,1,2,3,2,3],
[6,0,3,5,3,4,5,4,5,2,3,4],
[7,8,0,8,6,4,6,5,6,7,7,5],
[8,6,3,0,6,5,5,3,4,6,5,4],
[8,8,5,5,0,3,5,3,5,5,6,5],
[9,7,7,6,8,0,7,5,6,7,5,6],
[8,6,5,6,6,4,0,3,5,6,5,5],
[10,7,6,8,8,6,8,0,6,6,5,7],
[9,6,5,7,6,5,6,5,0,6,5,5],
[8,9,4,5,6,4,5,5,5,0,7,4],
[9,8,4,6,5,6,6,6,6,4,0,4],
[8,7,6,7,6,5,6,4,6,7,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 61, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,7,7,5,3,8,4,4,6,4,5],
[6,0,5,6,4,5,6,3,4,5,5,4],
[4,6,0,3,5,5,5,3,4,5,6,3],
[4,5,8,0,4,5,6,6,5,4,6,3],
[6,7,6,7,0,2,6,5,3,5,4,2],
[8,6,6,6,9,0,8,5,7,7,6,5],
[3,5,6,5,5,3,0,4,3,5,6,1],
[7,8,8,5,6,6,7,0,7,5,7,4],
[7,7,7,6,8,4,8,4,0,6,5,6],
[5,6,6,7,6,4,6,6,5,0,7,5],
[7,6,5,5,7,5,5,4,6,4,0,5],
[6,7,8,8,9,6,10,7,5,6,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 62, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,5,6,7,7,5,6,5,7,5,5],
[3,0,5,3,3,7,4,5,5,5,5,3],
[6,6,0,4,5,6,4,5,4,6,6,3],
[5,8,7,0,8,9,6,7,7,7,7,7],
[4,8,6,3,0,6,5,5,3,6,5,3],
[4,4,5,2,5,0,3,5,6,6,4,3],
[6,7,7,5,6,8,0,6,4,7,6,6],
[5,6,6,4,6,6,5,0,4,6,5,5],
[6,6,7,4,8,5,7,7,0,8,7,6],
[4,6,5,4,5,5,4,5,3,0,4,2],
[6,6,5,4,6,7,5,6,4,7,0,6],
[6,8,8,4,8,8,5,6,5,9,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 63, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,1,3,5,3,2,6,3,3,3,4],
[8,0,0,4,5,5,4,6,4,7,7,6],
[10,11,0,7,9,7,4,8,7,9,7,9],
[8,7,4,0,6,6,7,7,3,7,8,7],
[6,6,2,5,0,4,4,5,6,3,4,6],
[8,6,4,5,7,0,5,6,4,7,5,6],
[9,7,7,4,7,6,0,7,5,5,5,7],
[5,5,3,4,6,5,4,0,3,5,5,5],
[8,7,4,8,5,7,6,8,0,7,7,8],
[8,4,2,4,8,4,6,6,4,0,7,8],
[8,4,4,3,7,6,6,6,4,4,0,6],
[7,5,2,4,5,5,4,6,3,3,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 64, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,6,6,5,5,7,6,7,6,6,7],
[6,0,6,5,6,7,7,6,7,7,7,7],
[5,5,0,7,4,5,8,5,6,6,5,6],
[5,6,4,0,6,8,6,5,8,7,6,7],
[6,5,7,5,0,8,7,5,8,7,4,7],
[6,4,6,3,3,0,7,3,5,7,5,7],
[4,4,3,5,4,4,0,4,5,5,7,4],
[5,5,6,6,6,8,7,0,9,8,5,7],
[4,4,5,3,3,6,6,2,0,5,4,6],
[5,4,5,4,4,4,6,3,6,0,2,4],
[5,4,6,5,7,6,4,6,7,9,0,5],
[4,4,5,4,4,4,7,4,5,7,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 65, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,7,1,3,1,6,0,5,6,4,3],
[6,0,9,6,4,4,6,4,9,6,9,6],
[4,2,0,0,3,0,0,0,2,3,3,2],
[10,5,11,0,3,5,8,5,5,8,10,5],
[8,7,8,8,0,8,5,6,6,8,11,8],
[10,7,11,6,3,0,6,3,8,6,8,10],
[5,5,11,3,6,5,0,1,3,6,6,5],
[11,7,11,6,5,8,10,0,5,10,9,8],
[6,2,9,6,5,3,8,6,0,8,9,6],
[5,5,8,3,3,5,5,1,3,0,6,5],
[7,2,8,1,0,3,5,2,2,5,0,2],
[8,5,9,6,3,1,6,3,5,6,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 66, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,5,3,6,5,5,4,4,4,4,6],
[8,0,8,8,5,9,5,9,6,7,4,9],
[6,3,0,5,4,7,4,6,5,5,4,6],
[8,3,6,0,6,8,5,4,5,4,5,9],
[5,6,7,5,0,9,7,7,5,7,5,9],
[6,2,4,3,2,0,2,4,3,4,3,3],
[6,6,7,6,4,9,0,7,7,6,6,10],
[7,2,5,7,4,7,4,0,6,2,2,8],
[7,5,6,6,6,8,4,5,0,5,3,9],
[7,4,6,7,4,7,5,9,6,0,3,9],
[7,7,7,6,6,8,5,9,8,8,0,10],
[5,2,5,2,2,8,1,3,2,2,1,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 67, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,10,7,6,10,10,9,9,6,4,5],
[7,0,6,5,4,9,9,7,8,7,6,5],
[1,5,0,7,2,6,9,7,7,5,0,3],
[4,6,4,0,4,6,6,7,7,5,3,5],
[5,7,9,7,0,9,10,7,8,6,7,6],
[1,2,5,5,2,0,8,6,6,5,0,3],
[1,2,2,5,1,3,0,5,5,1,0,2],
[2,4,4,4,4,5,6,0,3,3,3,5],
[2,3,4,4,3,5,6,8,0,4,0,3],
[5,4,6,6,5,6,10,8,7,0,3,6],
[7,5,11,8,4,11,11,8,11,8,0,4],
[6,6,8,6,5,8,9,6,8,5,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 68, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,6,6,7,4,6,7,8,2,0,5],
[6,0,6,6,7,4,6,2,6,6,3,3],
[5,5,0,7,7,5,1,5,8,5,5,4],
[5,5,4,0,5,3,5,7,9,2,2,4],
[4,4,4,6,0,3,5,4,4,4,2,4],
[7,7,6,8,8,0,5,7,9,7,7,4],
[5,5,10,6,6,6,0,5,9,5,5,4],
[4,9,6,4,7,4,6,0,11,4,4,6],
[3,5,3,2,7,2,2,0,0,1,0,2],
[9,5,6,9,7,4,6,7,10,0,7,4],
[11,8,6,9,9,4,6,7,11,4,0,6],
[6,8,7,7,7,7,7,5,9,7,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 69, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,5,5,8,11,5,8,8,5,5,5],
[6,0,3,3,6,6,3,6,6,3,3,6],
[6,8,0,3,6,6,8,3,3,8,6,6],
[6,8,8,0,11,11,8,8,8,8,11,3],
[3,5,5,0,0,11,5,8,8,5,8,0],
[0,5,5,0,0,0,5,0,8,5,5,0],
[6,8,3,3,6,6,0,3,3,3,6,3],
[3,5,8,3,3,11,8,0,8,5,8,3],
[3,5,8,3,3,3,8,3,0,8,8,3],
[6,8,3,3,6,6,8,6,3,0,3,6],
[6,8,5,0,3,6,5,3,3,8,0,3],
[6,5,5,8,11,11,8,8,8,5,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 70, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,4,3,3,6,5,6,6,6,0,3],
[6,0,7,4,7,8,3,9,6,7,3,3],
[7,4,0,5,7,10,5,9,8,5,5,5],
[8,7,6,0,8,9,5,9,9,6,6,7],
[8,4,4,3,0,6,4,9,7,5,3,4],
[5,3,1,2,5,0,3,7,5,3,1,2],
[6,8,6,6,7,8,0,9,8,6,4,6],
[5,2,2,2,2,4,2,0,5,5,3,3],
[5,5,3,2,4,6,3,6,0,4,2,2],
[5,4,6,5,6,8,5,6,7,0,5,5],
[11,8,6,5,8,10,7,8,9,6,0,6],
[8,8,6,4,7,9,5,8,9,6,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 71, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,4,6,4,6,6,6,5,6,9,3],
[8,0,5,7,7,8,7,6,4,6,9,7],
[7,6,0,7,5,6,6,5,4,6,7,5],
[5,4,4,0,5,7,7,6,4,7,7,4],
[7,4,6,6,0,8,7,6,6,6,9,7],
[5,3,5,4,3,0,4,6,4,7,6,3],
[5,4,5,4,4,7,0,5,2,4,9,5],
[5,5,6,5,5,5,6,0,4,5,6,4],
[6,7,7,7,5,7,9,7,0,7,10,4],
[5,5,5,4,5,4,7,6,4,0,6,7],
[2,2,4,4,2,5,2,5,1,5,0,2],
[8,4,6,7,4,8,6,7,7,4,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 72, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,1,5,5,4,5,2,1,4,3,5],
[6,0,3,4,6,5,6,2,3,6,5,7],
[10,8,0,10,8,8,11,5,5,6,7,9],
[6,7,1,0,3,4,5,3,2,6,5,4],
[6,5,3,8,0,5,7,5,4,4,5,4],
[7,6,3,7,6,0,5,4,5,6,5,3],
[6,5,0,6,4,6,0,3,4,4,3,4],
[9,9,6,8,6,7,8,0,9,5,7,7],
[10,8,6,9,7,6,7,2,0,6,8,7],
[7,5,5,5,7,5,7,6,5,0,5,5],
[8,6,4,6,6,6,8,4,3,6,0,7],
[6,4,2,7,7,8,7,4,4,6,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 73, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,5,4,6,3,6,8,5,2,3,4],
[7,0,5,3,5,4,6,9,4,5,4,4],
[6,6,0,4,6,3,9,7,4,6,4,6],
[7,8,7,0,8,5,9,10,6,8,5,9],
[5,6,5,3,0,4,5,9,4,4,3,6],
[8,7,8,6,7,0,8,9,3,7,7,8],
[5,5,2,2,6,3,0,5,3,1,2,4],
[3,2,4,1,2,2,6,0,3,1,2,3],
[6,7,7,5,7,8,8,8,0,6,9,8],
[9,6,5,3,7,4,10,10,5,0,4,5],
[8,7,7,6,8,4,9,9,2,7,0,9],
[7,7,5,2,5,3,7,8,3,6,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 74, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,6,8,6,5,11,5,5,5,6,5],
[6,0,3,6,3,6,6,6,6,6,9,3],
[5,8,0,5,0,5,5,8,8,8,8,5],
[3,5,6,0,3,5,5,5,5,3,9,5],
[5,8,11,8,0,5,5,8,8,8,11,8],
[6,5,6,6,6,0,8,8,6,6,9,3],
[0,5,6,6,6,3,0,3,3,3,6,3],
[6,5,3,6,3,3,8,0,6,3,6,0],
[6,5,3,6,3,5,8,5,0,6,6,2],
[6,5,3,8,3,5,8,8,5,0,6,5],
[5,2,3,2,0,2,5,5,5,5,0,2],
[6,8,6,6,3,8,8,11,9,6,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 75, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1,0,3,6,1,1,1,3,3,0,1],
[10,0,8,8,10,6,6,7,6,6,5,6],
[11,3,0,6,7,1,2,6,5,5,1,1],
[8,3,5,0,10,1,4,6,7,5,6,6],
[5,1,4,1,0,1,2,1,5,5,1,5],
[10,5,10,10,10,0,7,8,7,8,6,11],
[10,5,9,7,9,4,0,8,4,8,3,5],
[10,4,5,5,10,3,3,0,6,6,2,6],
[8,5,6,4,6,4,7,5,0,5,5,7],
[8,5,6,6,6,3,3,5,6,0,2,4],
[11,6,10,5,10,5,8,9,6,9,0,9],
[10,5,10,5,6,0,6,5,4,7,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 76, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,6,7,6,6,5,6,6,6,8,6],
[4,0,7,7,5,6,5,3,5,4,6,5],
[5,4,0,6,4,6,4,4,4,4,6,4],
[4,4,5,0,5,8,5,4,4,5,5,5],
[5,6,7,6,0,6,5,5,6,6,4,7],
[5,5,5,3,5,0,2,3,5,4,5,5],
[6,6,7,6,6,9,0,4,7,5,5,7],
[5,8,7,7,6,8,7,0,8,7,7,6],
[5,6,7,7,5,6,4,3,0,5,6,6],
[5,7,7,6,5,7,6,4,6,0,7,7],
[3,5,5,6,7,6,6,4,5,4,0,5],
[5,6,7,6,4,6,4,5,5,4,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 77, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,4,4,7,1,7,4,7,11,3,1],
[7,0,4,8,10,0,8,0,7,11,7,0],
[7,7,0,4,6,1,4,3,3,11,7,0],
[7,3,7,0,10,0,4,3,7,11,7,0],
[4,1,5,1,0,1,1,0,0,8,4,1],
[10,11,10,11,10,0,11,7,10,11,10,4],
[4,3,7,7,10,0,0,3,4,11,7,0],
[7,11,8,8,11,4,8,0,8,11,10,8],
[4,4,8,4,11,1,7,3,0,11,7,1],
[0,0,0,0,3,0,0,0,0,0,0,0],
[8,4,4,4,7,1,4,1,4,11,0,1],
[10,11,11,11,10,7,11,3,10,11,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 78, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,3,6,6,8,3,8,8,3,8],
[0,0,0,0,3,0,5,0,0,0,0,0],
[0,11,0,3,6,6,8,3,3,3,3,8],
[8,11,8,0,8,8,5,5,8,8,11,8],
[5,8,5,3,0,0,5,5,5,8,3,8],
[5,11,5,3,11,0,8,8,8,8,3,8],
[3,6,3,6,6,3,0,0,6,3,6,6],
[8,11,8,6,6,3,11,0,11,8,6,11],
[3,11,8,3,6,3,5,0,0,3,3,11],
[3,11,8,3,3,3,8,3,8,0,3,8],
[8,11,8,0,8,8,5,5,8,8,0,8],
[3,11,3,3,3,3,5,0,0,3,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 79, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,5,6,6,5,8,7,7,7,8,9],
[5,0,7,5,6,8,7,5,6,5,5,7],
[6,4,0,3,3,8,5,4,5,4,3,5],
[5,6,8,0,6,7,7,7,6,8,8,7],
[5,5,8,5,0,6,6,6,6,6,7,6],
[6,3,3,4,5,0,6,5,4,5,5,4],
[3,4,6,4,5,5,0,5,6,6,3,6],
[4,6,7,4,5,6,6,0,4,6,5,7],
[4,5,6,5,5,7,5,7,0,6,5,7],
[4,6,7,3,5,6,5,5,5,0,6,6],
[3,6,8,3,4,6,8,6,6,5,0,6],
[2,4,6,4,5,7,5,4,4,5,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 80, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,6,5,6,6,7,7,6,8,7,6],
[4,0,5,3,7,4,6,5,6,6,6,5],
[5,6,0,3,6,4,5,6,4,7,7,3],
[6,8,8,0,7,5,5,7,7,8,9,8],
[5,4,5,4,0,3,5,5,6,6,6,6],
[5,7,7,6,8,0,5,7,7,8,9,7],
[4,5,6,6,6,6,0,4,6,6,8,4],
[4,6,5,4,6,4,7,0,6,8,7,5],
[5,5,7,4,5,4,5,5,0,5,7,3],
[3,5,4,3,5,3,5,3,6,0,8,5],
[4,5,4,2,5,2,3,4,4,3,0,5],
[5,6,8,3,5,4,7,6,8,6,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 81, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,6,5,5,4,4,5,4,8,2,5],
[7,0,7,6,7,6,4,7,7,10,5,7],
[5,4,0,8,7,6,6,9,7,5,7,8],
[6,5,3,0,4,3,2,7,5,7,4,6],
[6,4,4,7,0,4,5,6,6,7,6,8],
[7,5,5,8,7,0,6,6,6,7,6,7],
[7,7,5,9,6,5,0,7,10,8,7,10],
[6,4,2,4,5,5,4,0,6,6,4,6],
[7,4,4,6,5,5,1,5,0,7,6,6],
[3,1,6,4,4,4,3,5,4,0,2,5],
[9,6,4,7,5,5,4,7,5,9,0,7],
[6,4,3,5,3,4,1,5,5,6,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 82, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,5,4,4,4,4,5,2,6,5,5],
[7,0,6,5,3,6,5,5,5,6,5,7],
[6,5,0,4,5,5,5,6,6,5,6,8],
[7,6,7,0,4,7,6,6,5,8,9,9],
[7,8,6,7,0,7,5,7,5,6,7,9],
[7,5,6,4,4,0,4,7,5,5,5,7],
[7,6,6,5,6,7,0,7,5,6,6,8],
[6,6,5,5,4,4,4,0,4,4,6,9],
[9,6,5,6,6,6,6,7,0,5,6,8],
[5,5,6,3,5,6,5,7,6,0,4,8],
[6,6,5,2,4,6,5,5,5,7,0,6],
[6,4,3,2,2,4,3,2,3,3,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 83, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,4,8,6,9,8,6,7,7,7,7],
[4,0,4,6,7,7,4,6,7,5,8,5],
[7,7,0,7,5,8,6,4,7,6,5,5],
[3,5,4,0,4,10,5,5,4,2,5,6],
[5,4,6,7,0,8,5,7,9,6,7,5],
[2,4,3,1,3,0,3,4,3,2,3,0],
[3,7,5,6,6,8,0,6,5,5,6,4],
[5,5,7,6,4,7,5,0,7,5,5,3],
[4,4,4,7,2,8,6,4,0,4,6,5],
[4,6,5,9,5,9,6,6,7,0,5,5],
[4,3,6,6,4,8,5,6,5,6,0,6],
[4,6,6,5,6,11,7,8,6,6,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 84, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,6,2,5,3,4,2,3,5,2,5],
[5,0,8,3,6,7,4,5,5,5,5,3],
[5,3,0,3,5,5,6,3,2,5,3,2],
[9,8,8,0,8,7,8,6,5,7,5,5],
[6,5,6,3,0,6,5,5,5,5,6,6],
[8,4,6,4,5,0,7,3,5,5,4,4],
[7,7,5,3,6,4,0,3,3,5,4,4],
[9,6,8,5,6,8,8,0,7,6,7,5],
[8,6,9,6,6,6,8,4,0,6,5,5],
[6,6,6,4,6,6,6,5,5,0,4,5],
[9,6,8,6,5,7,7,4,6,7,0,5],
[6,8,9,6,5,7,7,6,6,6,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 85, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,6,7,6,5,6,7,1,5,4,3],
[6,0,8,6,7,5,5,6,3,6,4,4],
[5,3,0,1,4,2,2,5,2,2,2,4],
[4,5,10,0,7,4,5,6,5,5,3,4],
[5,4,7,4,0,3,5,7,6,4,2,5],
[6,6,9,7,8,0,8,5,6,8,6,3],
[5,6,9,6,6,3,0,4,4,4,3,6],
[4,5,6,5,4,6,7,0,4,5,6,6],
[10,8,9,6,5,5,7,7,0,7,5,5],
[6,5,9,6,7,3,7,6,4,0,3,6],
[7,7,9,8,9,5,8,5,6,8,0,6],
[8,7,7,7,6,8,5,5,6,5,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 86, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,2,3,3,2,3,2,1,3,2,5],
[9,0,5,7,7,7,6,3,5,7,6,8],
[9,6,0,6,8,5,4,3,3,7,5,6],
[8,4,5,0,7,5,5,4,2,6,6,7],
[8,4,3,4,0,5,4,3,4,5,5,6],
[9,4,6,6,6,0,7,5,6,8,8,6],
[8,5,7,6,7,4,0,4,1,6,5,6],
[9,8,8,7,8,6,7,0,6,8,5,8],
[10,6,8,9,7,5,10,5,0,8,6,7],
[8,4,4,5,6,3,5,3,3,0,6,6],
[9,5,6,5,6,3,6,6,5,5,0,5],
[6,3,5,4,5,5,5,3,4,5,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 87, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,3,7,6,3,7,6,3,6,1,5],
[8,0,3,7,9,3,7,6,4,5,2,7],
[8,8,0,5,7,4,9,7,4,6,4,5],
[4,4,6,0,4,4,5,5,4,2,2,0],
[5,2,4,7,0,2,4,3,5,3,3,0],
[8,8,7,7,9,0,9,6,4,5,4,7],
[4,4,2,6,7,2,0,5,3,7,1,4],
[5,5,4,6,8,5,6,0,5,4,1,5],
[8,7,7,7,6,7,8,6,0,5,5,4],
[5,6,5,9,8,6,4,7,6,0,4,8],
[10,9,7,9,8,7,10,10,6,7,0,5],
[6,4,6,11,11,4,7,6,7,3,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 88, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,6,1,5,3,3,5,2,5,4,8],
[8,0,7,5,9,7,6,9,7,8,7,9],
[5,4,0,4,4,4,4,5,3,4,4,7],
[10,6,7,0,8,6,7,7,5,7,7,9],
[6,2,7,3,0,3,5,6,3,6,4,6],
[8,4,7,5,8,0,6,6,5,6,6,10],
[8,5,7,4,6,5,0,8,5,6,8,10],
[6,2,6,4,5,5,3,0,4,5,7,6],
[9,4,8,6,8,6,6,7,0,6,5,10],
[6,3,7,4,5,5,5,6,5,0,6,8],
[7,4,7,4,7,5,3,4,6,5,0,7],
[3,2,4,2,5,1,1,5,1,3,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 89, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,6,4,9,8,6,7,8,6,5,6],
[7,0,8,5,8,7,4,7,7,6,4,5],
[5,3,0,3,6,3,1,2,7,3,4,4],
[7,6,8,0,9,8,5,7,7,6,5,6],
[2,3,5,2,0,2,2,3,6,2,3,3],
[3,4,8,3,9,0,5,5,7,6,4,5],
[5,7,10,6,9,6,0,9,9,6,6,8],
[4,4,9,4,8,6,2,0,8,4,5,6],
[3,4,4,4,5,4,2,3,0,3,2,3],
[5,5,8,5,9,5,5,7,8,0,4,6],
[6,7,7,6,8,7,5,6,9,7,0,5],
[5,6,7,5,8,6,3,5,8,5,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 90, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,3,4,4,3,2,3,4,4,8,2],
[7,0,6,6,5,3,6,4,4,3,7,2],
[8,5,0,6,6,4,8,5,5,4,9,2],
[7,5,5,0,5,4,5,3,3,2,8,1],
[7,6,5,6,0,4,4,4,6,3,8,4],
[8,8,7,7,7,0,6,6,8,5,10,5],
[9,5,3,6,7,5,0,5,6,4,8,4],
[8,7,6,8,7,5,6,0,5,5,10,4],
[7,7,6,8,5,3,5,6,0,7,7,7],
[7,8,7,9,8,6,7,6,4,0,7,6],
[3,4,2,3,3,1,3,1,4,4,0,2],
[9,9,9,10,7,6,7,7,4,5,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 91, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,4,3,5,7,7,6,8,7,7,5],
[4,0,4,5,5,5,7,5,6,7,6,5],
[7,7,0,3,6,8,6,7,8,7,6,5],
[8,6,8,0,6,8,7,6,5,7,7,6],
[6,6,5,5,0,7,7,6,6,6,5,4],
[4,6,3,3,4,0,6,5,6,5,4,4],
[4,4,5,4,4,5,0,5,5,5,6,5],
[5,6,4,5,5,6,6,0,5,8,5,4],
[3,5,3,6,5,5,6,6,0,6,5,6],
[4,4,4,4,5,6,6,3,5,0,4,4],
[4,5,5,4,6,7,5,6,6,7,0,5],
[6,6,6,5,7,7,6,7,5,7,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 92, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,2,4,5,4,4,4,7,6,7,6],
[3,0,4,4,2,4,3,3,4,6,4,6],
[9,7,0,6,7,6,8,3,6,8,8,6],
[7,7,5,0,8,4,7,6,9,6,8,4],
[6,9,4,3,0,2,4,2,3,6,6,6],
[7,7,5,7,9,0,9,3,7,8,8,6],
[7,8,3,4,7,2,0,4,7,5,8,6],
[7,8,8,5,9,8,7,0,7,8,8,5],
[4,7,5,2,8,4,4,4,0,4,8,4],
[5,5,3,5,5,3,6,3,7,0,6,4],
[4,7,3,3,5,3,3,3,3,5,0,6],
[5,5,5,7,5,5,5,6,7,7,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 93, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,6,6,5,5,5,5,5,7,5,7],
[8,0,8,7,6,5,6,7,7,6,6,6],
[5,3,0,3,5,1,2,5,4,3,2,3],
[5,4,8,0,5,4,5,3,5,5,4,4],
[6,5,6,6,0,5,3,5,4,5,4,4],
[6,6,10,7,6,0,6,5,8,8,5,5],
[6,5,9,6,8,5,0,6,7,8,7,5],
[6,4,6,8,6,6,5,0,6,6,5,7],
[6,4,7,6,7,3,4,5,0,5,5,4],
[4,5,8,6,6,3,3,5,6,0,3,5],
[6,5,9,7,7,6,4,6,6,8,0,6],
[4,5,8,7,7,6,6,4,7,6,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 94, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,6,6,7,8,5,8,4,10,5,5],
[4,0,4,3,4,6,4,5,4,8,6,5],
[5,7,0,7,5,7,6,9,7,9,7,8],
[5,8,4,0,7,7,7,7,7,9,7,4],
[4,7,6,4,0,6,8,5,7,7,7,4],
[3,5,4,4,5,0,3,6,6,6,5,4],
[6,7,5,4,3,8,0,7,5,6,7,5],
[3,6,2,4,6,5,4,0,4,7,6,2],
[7,7,4,4,4,5,6,7,0,7,7,4],
[1,3,2,2,4,5,5,4,4,0,3,2],
[6,5,4,4,4,6,4,5,4,8,0,3],
[6,6,3,7,7,7,6,9,7,9,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 95, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,4,4,6,6,7,5,4,6,7,7],
[6,0,5,3,6,10,5,3,4,4,8,6],
[7,6,0,6,7,9,8,5,4,6,7,8],
[7,8,5,0,7,9,6,3,5,7,9,7],
[5,5,4,4,0,5,7,2,5,6,6,5],
[5,1,2,2,6,0,4,2,3,4,6,5],
[4,6,3,5,4,7,0,5,6,6,6,5],
[6,8,6,8,9,9,6,0,4,8,8,7],
[7,7,7,6,6,8,5,7,0,9,8,8],
[5,7,5,4,5,7,5,3,2,0,8,8],
[4,3,4,2,5,5,5,3,3,3,0,5],
[4,5,3,4,6,6,6,4,3,3,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 96, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,5,8,3,6,4,3,5,4,3,5],
[7,0,7,9,8,5,7,9,7,7,5,6],
[6,4,0,7,4,6,5,6,5,5,3,3],
[3,2,4,0,3,3,4,3,2,4,2,3],
[8,3,7,8,0,7,8,5,7,6,4,5],
[5,6,5,8,4,0,7,5,8,5,4,3],
[7,4,6,7,3,4,0,4,4,5,3,3],
[8,2,5,8,6,6,7,0,5,6,5,5],
[6,4,6,9,4,3,7,6,0,3,2,3],
[7,4,6,7,5,6,6,5,8,0,5,5],
[8,6,8,9,7,7,8,6,9,6,0,5],
[6,5,8,8,6,8,8,6,8,6,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 97, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,8,8,5,8,3,9,7,8,9,6],
[6,0,8,8,5,8,6,9,6,8,7,6],
[3,3,0,4,4,5,2,5,4,6,6,3],
[3,3,7,0,3,5,4,6,5,6,5,4],
[6,6,7,8,0,6,5,9,8,7,10,7],
[3,3,6,6,5,0,1,7,5,5,4,4],
[8,5,9,7,6,10,0,8,7,8,7,5],
[2,2,6,5,2,4,3,0,5,5,4,2],
[4,5,7,6,3,6,4,6,0,8,6,4],
[3,3,5,5,4,6,3,6,3,0,4,4],
[2,4,5,6,1,7,4,7,5,7,0,4],
[5,5,8,7,4,7,6,9,7,7,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 98, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,6,3,2,2,3,3,7,6,2,8],
[9,0,7,7,4,6,7,4,7,9,8,6],
[5,4,0,1,1,1,3,4,1,5,3,2],
[8,4,10,0,8,5,7,4,8,10,7,5],
[9,7,10,3,0,8,7,6,11,10,8,6],
[9,5,10,6,3,0,6,6,10,9,10,6],
[8,4,8,4,4,5,0,5,8,8,5,5],
[8,7,7,7,5,5,6,0,7,7,7,5],
[4,4,10,3,0,1,3,4,0,10,3,6],
[5,2,6,1,1,2,3,4,1,0,2,2],
[9,3,8,4,3,1,6,4,8,9,0,6],
[3,5,9,6,5,5,6,6,5,9,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 99, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,5,6,3,5,5,9,9,5,7,2],
[5,0,0,6,5,7,5,3,6,7,3,7],
[6,11,0,6,6,7,5,4,6,8,4,8],
[5,5,5,0,5,5,5,5,8,5,8,2],
[8,6,5,6,0,7,7,9,11,6,9,2],
[6,4,4,6,4,0,5,4,6,4,4,6],
[6,6,6,6,4,6,0,6,7,9,4,6],
[2,8,7,6,2,7,5,0,6,7,7,4],
[2,5,5,3,0,5,4,5,0,2,3,2],
[6,4,3,6,5,7,2,4,9,0,4,2],
[4,8,7,3,2,7,7,4,8,7,0,4],
[9,4,3,9,9,5,5,7,9,9,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 100, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,4,9,6,8,6,8,6,7,6,8],
[7,0,6,8,5,7,5,9,5,8,6,8],
[7,5,0,8,6,10,5,10,6,6,6,8],
[2,3,3,0,1,6,6,6,5,2,4,5],
[5,6,5,10,0,10,6,10,7,7,7,8],
[3,4,1,5,1,0,4,6,4,4,3,6],
[5,6,6,5,5,7,0,10,4,6,5,9],
[3,2,1,5,1,5,1,0,1,2,3,4],
[5,6,5,6,4,7,7,10,0,5,3,10],
[4,3,5,9,4,7,5,9,6,0,6,8],
[5,5,5,7,4,8,6,8,8,5,0,7],
[3,3,3,6,3,5,2,7,1,3,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 101, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,5,5,8,6,7,4,6,5,3,4],
[5,0,8,8,8,5,5,5,6,5,4,6],
[6,3,0,7,6,6,7,7,3,5,5,4],
[6,3,4,0,4,5,6,3,2,1,2,2],
[3,3,5,7,0,6,7,3,3,2,2,3],
[5,6,5,6,5,0,3,3,6,4,4,3],
[4,6,4,5,4,8,0,4,6,4,4,7],
[7,6,4,8,8,8,7,0,5,7,4,6],
[5,5,8,9,8,5,5,6,0,4,4,6],
[6,6,6,10,9,7,7,4,7,0,2,4],
[8,7,6,9,9,7,7,7,7,9,0,5],
[7,5,7,9,8,8,4,5,5,7,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 102, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,8,8,7,7,8,7,7,8,6,5],
[4,0,6,9,7,8,9,6,8,8,6,5],
[3,5,0,9,5,5,8,7,4,5,5,3],
[3,2,2,0,4,3,4,5,2,4,3,2],
[4,4,6,7,0,6,8,7,4,3,7,5],
[4,3,6,8,5,0,6,7,6,3,7,6],
[3,2,3,7,3,5,0,5,2,3,3,1],
[4,5,4,6,4,4,6,0,5,4,6,2],
[4,3,7,9,7,5,9,6,0,4,7,4],
[3,3,6,7,8,8,8,7,7,0,6,5],
[5,5,6,8,4,4,8,5,4,5,0,3],
[6,6,8,9,6,5,10,9,7,6,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 103, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,1,4,5,0,7,4,7,8,0,4],
[8,0,4,7,8,5,7,4,4,8,4,5],
[10,7,0,7,5,7,7,8,7,8,4,8],
[7,4,4,0,4,4,7,7,3,4,3,4],
[6,3,6,7,0,3,7,4,3,7,0,3],
[11,6,4,7,8,0,7,4,10,11,4,8],
[4,4,4,4,4,4,0,4,3,4,0,1],
[7,7,3,4,7,7,7,0,7,7,4,7],
[4,7,4,8,8,1,8,4,0,8,1,4],
[3,3,3,7,4,0,7,4,3,0,0,1],
[11,7,7,8,11,7,11,7,10,11,0,4],
[7,6,3,7,8,3,10,4,7,10,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 104, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,8,6,6,2,7,4,6,6,1,9],
[3,0,7,6,6,4,8,6,8,7,3,8],
[3,4,0,5,7,2,3,3,5,6,3,10],
[5,5,6,0,9,6,5,6,7,7,5,7],
[5,5,4,2,0,3,5,4,6,4,5,6],
[9,7,9,5,8,0,8,9,10,7,7,10],
[4,3,8,6,6,3,0,5,6,7,4,9],
[7,5,8,5,7,2,6,0,7,8,6,8],
[5,3,6,4,5,1,5,4,0,7,1,9],
[5,4,5,4,7,4,4,3,4,0,4,5],
[10,8,8,6,6,4,7,5,10,7,0,10],
[2,3,1,4,5,1,2,3,2,6,1,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 105, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,6,9,5,9,7,6,7,10,7,9],
[4,0,7,8,8,8,10,9,7,9,9,9],
[5,4,0,4,8,3,4,5,5,5,4,4],
[2,3,7,0,6,9,2,3,6,5,6,5],
[6,3,3,5,0,5,3,3,8,6,6,5],
[2,3,8,2,6,0,2,2,6,5,6,6],
[4,1,7,9,8,9,0,4,6,6,9,9],
[5,2,6,8,8,9,7,0,6,8,8,7],
[4,4,6,5,3,5,5,5,0,6,5,5],
[1,2,6,6,5,6,5,3,5,0,5,4],
[4,2,7,5,5,5,2,3,6,6,0,10],
[2,2,7,6,6,5,2,4,6,7,1,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 106, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,5,0,1,4,4,5,9,1,1,1],
[6,0,1,4,5,8,4,10,8,4,5,5],
[6,10,0,6,7,10,6,10,10,4,7,7],
[11,7,5,0,3,11,7,7,11,9,11,3],
[10,6,4,8,0,10,4,6,10,8,11,2],
[7,3,1,0,1,0,0,7,7,1,3,3],
[7,7,5,4,7,11,0,7,11,5,7,3],
[6,1,1,4,5,4,4,0,4,5,5,1],
[2,3,1,0,1,4,0,7,0,1,3,3],
[10,7,7,2,3,10,6,6,10,0,7,3],
[10,6,4,0,0,8,4,6,8,4,0,2],
[10,6,4,8,9,8,8,10,8,8,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 107, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,3,7,6,7,4,5,6,5,8,4],
[4,0,5,8,6,6,6,4,8,7,5,3],
[8,6,0,6,7,9,5,8,6,9,8,4],
[4,3,5,0,7,6,5,3,5,6,3,2],
[5,5,4,4,0,5,5,1,6,4,6,3],
[4,5,2,5,6,0,3,5,5,5,6,4],
[7,5,6,6,6,8,0,5,9,7,6,6],
[6,7,3,8,10,6,6,0,7,5,8,6],
[5,3,5,6,5,6,2,4,0,7,6,3],
[6,4,2,5,7,6,4,6,4,0,7,5],
[3,6,3,8,5,5,5,3,5,4,0,3],
[7,8,7,9,8,7,5,5,8,6,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 108, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,2,3,1,3,3,3,3,2,4,4],
[8,0,5,5,1,3,6,6,8,4,7,4],
[9,6,0,8,3,4,6,6,6,6,7,7],
[8,6,3,0,4,4,5,8,8,6,10,10],
[10,10,8,7,0,6,5,10,10,10,10,10],
[8,8,7,7,5,0,8,8,8,10,10,10],
[8,5,5,6,6,3,0,5,5,5,7,5],
[8,5,5,3,1,3,6,0,6,5,7,4],
[8,3,5,3,1,3,6,5,0,2,10,7],
[9,7,5,5,1,1,6,6,9,0,10,7],
[7,4,4,1,1,1,4,4,1,1,0,1],
[7,7,4,1,1,1,6,7,4,4,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 109, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,5,8,7,6,8,9,7,6,4,4],
[7,0,4,5,3,5,5,5,10,2,6,5],
[6,7,0,6,4,6,4,4,7,4,6,6],
[3,6,5,0,9,6,6,2,7,8,2,6],
[4,8,7,2,0,4,3,2,7,6,4,4],
[5,6,5,5,7,0,8,4,7,6,4,5],
[3,6,7,5,8,3,0,3,6,7,2,2],
[2,6,7,9,9,7,8,0,6,7,2,5],
[4,1,4,4,4,4,5,5,0,3,2,3],
[5,9,7,3,5,5,4,4,8,0,4,6],
[7,5,5,9,7,7,9,9,9,7,0,5],
[7,6,5,5,7,6,9,6,8,5,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 110, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,5,4,8,10,3,6,6,10,8,8],
[4,0,4,3,7,6,2,5,5,6,5,5],
[6,7,0,7,10,7,4,6,5,7,7,6],
[7,8,4,0,8,9,4,6,4,8,6,8],
[3,4,1,3,0,4,1,4,4,6,4,4],
[1,5,4,2,7,0,1,2,4,3,6,2],
[8,9,7,7,10,10,0,5,6,9,6,9],
[5,6,5,5,7,9,6,0,6,9,8,7],
[5,6,6,7,7,7,5,5,0,6,5,7],
[1,5,4,3,5,8,2,2,5,0,5,3],
[3,6,4,5,7,5,5,3,6,6,0,3],
[3,6,5,3,7,9,2,4,4,8,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 111, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,8,7,6,7,5,6,9,8,7,7],
[6,0,4,5,3,5,2,3,4,5,5,5],
[3,7,0,6,8,6,4,4,6,7,5,7],
[4,6,5,0,6,6,5,4,6,5,5,6],
[5,8,3,5,0,6,3,3,4,8,5,5],
[4,6,5,5,5,0,4,3,6,5,5,4],
[6,9,7,6,8,7,0,5,7,9,8,7],
[5,8,7,7,8,8,6,0,7,8,8,6],
[2,7,5,5,7,5,4,4,0,5,4,3],
[3,6,4,6,3,6,2,3,6,0,4,5],
[4,6,6,6,6,6,3,3,7,7,0,6],
[4,6,4,5,6,7,4,5,8,6,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 112, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,7,3,4,7,4,6,4,4,4,4],
[4,0,10,0,3,9,4,6,3,3,4,7],
[4,1,0,1,4,3,2,4,0,4,5,5],
[8,11,10,0,5,10,11,10,7,8,10,7],
[7,8,7,6,0,7,8,6,7,8,7,4],
[4,2,8,1,4,0,2,7,1,5,5,5],
[7,7,9,0,3,9,0,6,3,4,6,6],
[5,5,7,1,5,4,5,0,4,5,4,4],
[7,8,11,4,4,10,8,7,0,11,11,8],
[7,8,7,3,3,6,7,6,0,0,4,7],
[7,7,6,1,4,6,5,7,0,7,0,7],
[7,4,6,4,7,6,5,7,3,4,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 113, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,7,7,4,7,6,0,5,4,6,7],
[2,0,2,6,2,6,4,2,2,4,4,6],
[4,9,0,8,4,6,6,2,4,6,8,6],
[4,5,3,0,4,4,0,2,4,2,8,6],
[7,9,7,7,0,7,5,2,5,7,9,5],
[4,5,5,7,4,0,4,2,2,4,6,7],
[5,7,5,11,6,7,0,2,7,7,9,9],
[11,9,9,9,9,9,9,0,5,9,9,9],
[6,9,7,7,6,9,4,6,0,6,8,7],
[7,7,5,9,4,7,4,2,5,0,7,7],
[5,7,3,3,2,5,2,2,3,4,0,3],
[4,5,5,5,6,4,2,2,4,4,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 114, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,8,6,8,7,6,6,8,5,7,8],
[4,0,4,5,7,3,2,3,2,5,3,4],
[3,7,0,6,8,8,7,5,5,6,4,5],
[5,6,5,0,8,6,4,6,7,6,7,6],
[3,4,3,3,0,4,3,3,2,5,3,3],
[4,8,3,5,7,0,5,6,3,7,3,6],
[5,9,4,7,8,6,0,6,6,8,6,7],
[5,8,6,5,8,5,5,0,7,5,4,5],
[3,9,6,4,9,8,5,4,0,7,6,6],
[6,6,5,5,6,4,3,6,4,0,5,6],
[4,8,7,4,8,8,5,7,5,6,0,6],
[3,7,6,5,8,5,4,6,5,5,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 115, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,4,6,3,3,8,7,7,4,4,5],
[8,0,5,5,6,10,7,9,9,8,5,8],
[7,6,0,5,8,10,8,9,8,8,5,7],
[5,6,6,0,6,8,9,9,9,6,6,8],
[8,5,3,5,0,8,7,4,11,6,6,7],
[8,1,1,3,3,0,5,4,6,1,1,5],
[3,4,3,2,4,6,0,7,4,3,3,3],
[4,2,2,2,7,7,4,0,7,5,2,4],
[4,2,3,2,0,5,7,4,0,3,2,4],
[7,3,3,5,5,10,8,6,8,0,0,7],
[7,6,6,5,5,10,8,9,9,11,0,10],
[6,3,4,3,4,6,8,7,7,4,1,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 116, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,7,5,6,6,5,8,8,4,6,5],
[4,0,5,5,5,3,5,4,5,5,6,6],
[4,6,0,7,5,5,4,9,6,5,7,8],
[6,6,4,0,4,3,3,9,5,2,6,7],
[5,6,6,7,0,6,4,8,6,4,4,7],
[5,8,6,8,5,0,7,10,7,6,8,8],
[6,6,7,8,7,4,0,8,7,6,7,8],
[3,7,2,2,3,1,3,0,3,1,5,3],
[3,6,5,6,5,4,4,8,0,4,6,5],
[7,6,6,9,7,5,5,10,7,0,7,7],
[5,5,4,5,7,3,4,6,5,4,0,6],
[6,5,3,4,4,3,3,8,6,4,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 117, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,7,5,5,5,6,6,5,7,6,4],
[6,0,9,7,4,8,7,6,6,8,9,7],
[4,2,0,5,2,2,2,3,3,3,8,6],
[6,4,6,0,3,6,4,5,4,6,7,6],
[6,7,9,8,0,7,5,8,4,8,8,7],
[6,3,9,5,4,0,4,6,5,6,8,7],
[5,4,9,7,6,7,0,7,6,9,7,8],
[5,5,8,6,3,5,4,0,5,7,7,7],
[6,5,8,7,7,6,5,6,0,9,7,7],
[4,3,8,5,3,5,2,4,2,0,6,5],
[5,2,3,4,3,3,4,4,4,5,0,7],
[7,4,5,5,4,4,3,4,4,6,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 118, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,7,5,4,4,6,4,7,2,4,4],
[6,0,4,5,3,3,4,2,4,3,3,3],
[4,7,0,7,7,5,6,6,6,5,5,5],
[6,6,4,0,4,6,6,6,6,4,5,5],
[7,8,4,7,0,7,5,8,6,7,6,6],
[7,8,6,5,4,0,6,6,7,5,6,3],
[5,7,5,5,6,5,0,6,5,5,4,4],
[7,9,5,5,3,5,5,0,5,4,5,2],
[4,7,5,5,5,4,6,6,0,3,7,2],
[9,8,6,7,4,6,6,7,8,0,5,5],
[7,8,6,6,5,5,7,6,4,6,0,5],
[7,8,6,6,5,8,7,9,9,6,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 119, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,8,6,5,8,6,4,5,5,6,8],
[4,0,7,4,4,6,6,4,5,5,4,6],
[3,4,0,2,6,9,4,5,4,5,3,4],
[5,7,9,0,7,7,7,6,6,7,6,8],
[6,7,5,4,0,4,8,4,5,6,3,7],
[3,5,2,4,7,0,6,5,5,6,4,5],
[5,5,7,4,3,5,0,3,6,3,4,5],
[7,7,6,5,7,6,8,0,6,6,6,7],
[6,6,7,5,6,6,5,5,0,6,7,7],
[6,6,6,4,5,5,8,5,5,0,4,5],
[5,7,8,5,8,7,7,5,4,7,0,7],
[3,5,7,3,4,6,6,4,4,6,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 120, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,3,3,11,7,1,7,3,7,7,7],
[4,0,4,4,6,4,4,0,5,8,4,6],
[8,7,0,6,10,7,4,7,7,11,6,11],
[8,7,5,0,10,7,5,7,7,7,7,7],
[0,5,1,1,0,5,1,1,1,5,5,1],
[4,7,4,4,6,0,4,7,5,6,8,7],
[10,7,7,6,10,7,0,7,3,7,6,7],
[4,11,4,4,10,4,4,0,5,10,4,6],
[8,6,4,4,10,6,8,6,0,10,4,10],
[4,3,0,4,6,5,4,1,1,0,4,3],
[4,7,5,4,6,3,5,7,7,7,0,7],
[4,5,0,4,10,4,4,5,1,8,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 121, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,7,4,1,5,2,3,3,2,2,3],
[2,0,7,2,2,6,2,3,2,2,3,4],
[4,4,0,4,2,5,2,4,1,3,2,3],
[7,9,7,0,1,5,4,6,2,2,2,3],
[10,9,9,10,0,10,4,6,6,5,6,3],
[6,5,6,6,1,0,4,6,3,4,5,4],
[9,9,9,7,7,7,0,6,6,4,5,6],
[8,8,7,5,5,5,5,0,6,2,3,7],
[8,9,10,9,5,8,5,5,0,4,5,3],
[9,9,8,9,6,7,7,9,7,0,4,7],
[9,8,9,9,5,6,6,8,6,7,0,6],
[8,7,8,8,8,7,5,4,8,4,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 122, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,5,6,6,6,5,7,8,3,4,5],
[7,0,7,7,7,4,5,6,8,5,5,6],
[6,4,0,9,8,6,8,7,8,6,5,7],
[5,4,2,0,7,5,4,5,9,4,4,5],
[5,4,3,4,0,4,4,5,5,3,2,5],
[5,7,5,6,7,0,5,6,7,5,5,6],
[6,6,3,7,7,6,0,6,8,7,3,7],
[4,5,4,6,6,5,5,0,7,3,4,6],
[3,3,3,2,6,4,3,4,0,3,4,2],
[8,6,5,7,8,6,4,8,8,0,6,6],
[7,6,6,7,9,6,8,7,7,5,0,7],
[6,5,4,6,6,5,4,5,9,5,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 123, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,5,8,6,9,5,7,6,7,8,7],
[4,0,5,5,5,8,3,7,5,5,5,5],
[6,6,0,6,6,9,5,8,7,4,6,4],
[3,6,5,0,5,7,4,6,5,5,4,5],
[5,6,5,6,0,7,6,5,4,6,7,7],
[2,3,2,4,4,0,2,4,3,3,5,3],
[6,8,6,7,5,9,0,6,7,8,6,8],
[4,4,3,5,6,7,5,0,4,5,5,5],
[5,6,4,6,7,8,4,7,0,6,6,7],
[4,6,7,6,5,8,3,6,5,0,7,7],
[3,6,5,7,4,6,5,6,5,4,0,6],
[4,6,7,6,4,8,3,6,4,4,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 124, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,5,5,3,7,6,5,6,6,8,5],
[5,0,6,5,5,8,7,6,7,6,7,6],
[6,5,0,4,3,8,7,7,6,6,5,6],
[6,6,7,0,7,6,7,5,7,3,6,5],
[8,6,8,4,0,9,8,7,5,4,6,6],
[4,3,3,5,2,0,3,4,5,4,5,3],
[5,4,4,4,3,8,0,6,5,5,6,5],
[6,5,4,6,4,7,5,0,5,5,8,4],
[5,4,5,4,6,6,6,6,0,4,8,6],
[5,5,5,8,7,7,6,6,7,0,8,5],
[3,4,6,5,5,6,5,3,3,3,0,3],
[6,5,5,6,5,8,6,7,5,6,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 125, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,7,5,9,7,5,4,6,3,7,7],
[6,0,8,5,8,7,7,4,8,6,3,7],
[4,3,0,4,5,3,6,2,4,2,4,4],
[6,6,7,0,9,7,6,4,8,5,6,7],
[2,3,6,2,0,6,6,4,7,4,4,3],
[4,4,8,4,5,0,4,6,8,4,7,4],
[6,4,5,5,5,7,0,7,6,5,7,4],
[7,7,9,7,7,5,4,0,8,6,8,7],
[5,3,7,3,4,3,5,3,0,3,2,3],
[8,5,9,6,7,7,6,5,8,0,5,6],
[4,8,7,5,7,4,4,3,9,6,0,7],
[4,4,7,4,8,7,7,4,8,5,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 126, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,11,4,7,3,8,7,8,7,4,8],
[11,0,11,4,11,7,8,7,8,11,8,8],
[0,0,0,0,3,0,0,3,0,3,0,0],
[7,7,11,0,7,7,7,7,7,7,7,4],
[4,0,8,4,0,0,4,7,4,4,4,4],
[8,4,11,4,11,0,8,7,8,7,8,8],
[3,3,11,4,7,3,0,7,4,7,0,0],
[4,4,8,4,4,4,4,0,4,4,4,4],
[3,3,11,4,7,3,7,7,0,7,7,4],
[4,0,8,4,7,4,4,7,4,0,4,4],
[7,3,11,4,7,3,11,7,4,7,0,4],
[3,3,11,7,7,3,11,7,7,7,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 127, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,6,6,6,6,6,3,3,6,6,6],
[5,0,3,8,5,3,5,2,3,3,3,5],
[5,8,0,8,8,5,5,5,8,8,2,5],
[5,3,3,0,5,0,2,5,0,3,0,5],
[5,6,3,6,0,3,3,6,6,3,3,3],
[5,8,6,11,8,0,8,8,6,8,5,8],
[5,6,6,9,8,3,0,6,6,6,3,6],
[8,9,6,6,5,3,5,0,6,3,3,5],
[8,8,3,11,5,5,5,5,0,5,5,5],
[5,8,3,8,8,3,5,8,6,0,5,5],
[5,8,9,11,8,6,8,8,6,6,0,11],
[5,6,6,6,8,3,5,6,6,6,0,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 128, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,7,8,9,5,5,9,7,10,5,8],
[4,0,6,5,4,3,3,4,0,4,3,5],
[4,5,0,8,4,4,6,4,3,7,3,3],
[3,6,3,0,3,0,0,4,0,3,3,3],
[2,7,7,8,0,4,4,6,2,5,7,5],
[6,8,7,11,7,0,10,7,6,6,3,8],
[6,8,5,11,7,1,0,7,6,6,3,6],
[2,7,7,7,5,4,4,0,7,8,2,8],
[4,11,8,11,9,5,5,4,0,7,5,9],
[1,7,4,8,6,5,5,3,4,0,2,2],
[6,8,8,8,4,8,8,9,6,9,0,9],
[3,6,8,8,6,3,5,3,2,9,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 129, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,4,7,4,5,5,7,6,4,5,4],
[7,0,6,8,10,4,8,11,9,9,6,6],
[7,5,0,9,9,7,9,9,7,9,9,5],
[4,3,2,0,5,2,5,6,5,4,5,2],
[7,1,2,6,0,4,6,6,5,8,3,2],
[6,7,4,9,7,0,5,9,7,8,6,5],
[6,3,2,6,5,6,0,7,5,8,6,2],
[4,0,2,5,5,2,4,0,7,5,2,0],
[5,2,4,6,6,4,6,4,0,7,4,4],
[7,2,2,7,3,3,3,6,4,0,2,4],
[6,5,2,6,8,5,5,9,7,9,0,3],
[7,5,6,9,9,6,9,11,7,7,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 130, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,5,6,4,4,1,3,4,4,6,3],
[6,0,6,5,6,7,6,8,7,5,5,6],
[6,5,0,6,4,6,6,7,6,2,3,3],
[5,6,5,0,6,7,5,8,8,7,5,6],
[7,5,7,5,0,6,5,8,8,6,5,5],
[7,4,5,4,5,0,4,6,6,2,2,6],
[10,5,5,6,6,7,0,7,7,5,6,5],
[8,3,4,3,3,5,4,0,5,4,3,3],
[7,4,5,3,3,5,4,6,0,3,4,6],
[7,6,9,4,5,9,6,7,8,0,5,7],
[5,6,8,6,6,9,5,8,7,6,0,6],
[8,5,8,5,6,5,6,8,5,4,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 131, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,5,4,4,5,5,8,5,4,8,6],
[2,0,6,3,6,2,6,6,3,2,7,4],
[6,5,0,3,6,6,6,10,4,2,7,3],
[7,8,8,0,10,8,8,7,6,4,5,7],
[7,5,5,1,0,5,4,5,5,2,4,5],
[6,9,5,3,6,0,7,10,4,2,8,4],
[6,5,5,3,7,4,0,4,4,6,7,6],
[3,5,1,4,6,1,7,0,5,3,7,4],
[6,8,7,5,6,7,7,6,0,6,8,7],
[7,9,9,7,9,9,5,8,5,0,11,10],
[3,4,4,6,7,3,4,4,3,0,0,4],
[5,7,8,4,6,7,5,7,4,1,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 132, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,2,3,3,4,2,3,3,5,4,3],
[11,0,4,4,3,6,6,5,5,8,6,6],
[9,7,0,8,6,6,5,5,6,8,7,8],
[8,7,3,0,5,6,3,3,4,7,5,3],
[8,8,5,6,0,4,6,5,3,7,5,7],
[7,5,5,5,7,0,4,4,4,8,6,5],
[9,5,6,8,5,7,0,7,6,7,6,6],
[8,6,6,8,6,7,4,0,6,6,6,6],
[8,6,5,7,8,7,5,5,0,8,6,6],
[6,3,3,4,4,3,4,5,3,0,5,3],
[7,5,4,6,6,5,5,5,5,6,0,5],
[8,5,3,8,4,6,5,5,5,8,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 133, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,8,8,9,6,11,11,5,8,8,8],
[5,0,8,8,9,9,8,11,8,8,8,8],
[3,3,0,8,6,9,6,9,6,9,5,3],
[3,3,3,0,6,9,6,9,6,9,5,3],
[2,2,5,5,0,8,8,11,5,5,5,2],
[5,2,2,2,3,0,8,8,5,5,5,5],
[0,3,5,5,3,3,0,3,0,5,5,3],
[0,0,2,2,0,3,8,0,5,2,5,2],
[6,3,5,5,6,6,11,6,0,5,8,3],
[3,3,2,2,6,6,6,9,6,0,5,3],
[3,3,6,6,6,6,6,6,3,6,0,6],
[3,3,8,8,9,6,8,9,8,8,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 134, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,5,10,10,9,5,5,9,7,8,11],
[1,0,4,9,8,7,4,4,7,4,5,2],
[6,7,0,10,7,8,9,5,5,7,6,7],
[1,2,1,0,6,5,3,4,4,5,1,2],
[1,3,4,5,0,4,5,6,3,5,2,1],
[2,4,3,6,7,0,4,5,4,6,4,4],
[6,7,2,8,6,7,0,6,5,5,5,7],
[6,7,6,7,5,6,5,0,5,8,5,6],
[2,4,6,7,8,7,6,6,0,5,3,3],
[4,7,4,6,6,5,6,3,6,0,5,5],
[3,6,5,10,9,7,6,6,8,6,0,4],
[0,9,4,9,10,7,4,5,8,6,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 135, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,6,7,6,7,7,9,6,4,9,5],
[5,0,0,3,3,5,3,3,0,4,3,3],
[5,11,0,5,11,9,5,11,6,6,9,5],
[4,8,6,0,6,9,0,9,6,4,9,7],
[5,8,0,5,0,9,5,9,0,6,3,5],
[4,6,2,2,2,0,2,5,2,6,5,5],
[4,8,6,11,6,9,0,9,6,8,9,7],
[2,8,0,2,2,6,2,0,0,6,3,2],
[5,11,5,5,11,9,5,11,0,6,9,5],
[7,7,5,7,5,5,3,5,5,0,5,7],
[2,8,2,2,8,6,2,8,2,6,0,4],
[6,8,6,4,6,6,4,9,6,4,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 136, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,7,7,7,7,7,7,2,7,5,7],
[4,0,9,7,9,4,4,4,4,11,4,6],
[4,2,0,7,7,6,6,6,6,6,4,2],
[4,4,4,0,9,4,4,4,4,4,4,4],
[4,2,4,2,0,4,4,4,4,6,4,6],
[4,7,5,7,7,0,9,4,6,11,4,7],
[4,7,5,7,7,2,0,0,2,7,0,7],
[4,7,5,7,7,7,11,0,6,11,4,7],
[9,7,5,7,7,5,9,5,0,7,9,7],
[4,0,5,7,5,0,4,0,4,0,4,2],
[6,7,7,7,7,7,11,7,2,7,0,7],
[4,5,9,7,5,4,4,4,4,9,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 137, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,5,10,10,5,10,10,6,10,6,10],
[0,0,0,5,5,0,10,10,6,5,6,10],
[6,11,0,6,6,6,11,11,6,5,11,11],
[1,6,5,0,6,5,10,10,6,5,6,11],
[1,6,5,5,0,5,5,5,1,5,6,6],
[6,11,5,6,6,0,11,11,6,5,6,11],
[1,1,0,1,6,0,0,6,6,0,1,11],
[1,1,0,1,6,0,5,0,6,0,1,6],
[5,5,5,5,10,5,5,5,0,5,6,5],
[1,6,6,6,6,6,11,11,6,0,6,11],
[5,5,0,5,5,5,10,10,5,5,0,10],
[1,1,0,0,5,0,0,5,6,0,1,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 138, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,5,3,4,4,6,5,4,4,7,4],
[4,0,2,3,2,3,1,3,1,5,5,4],
[6,9,0,3,6,3,5,5,7,4,9,3],
[8,8,8,0,7,3,4,6,7,5,8,3],
[7,9,5,4,0,5,4,8,8,6,10,5],
[7,8,8,8,6,0,4,6,5,6,10,5],
[5,10,6,7,7,7,0,6,5,8,8,7],
[6,8,6,5,3,5,5,0,5,3,9,4],
[7,10,4,4,3,6,6,6,0,7,8,5],
[7,6,7,6,5,5,3,8,4,0,7,3],
[4,6,2,3,1,1,3,2,3,4,0,3],
[7,7,8,8,6,6,4,7,6,8,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 139, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,2,7,6,8,7,6,2,3,5,8],
[4,0,5,7,6,7,4,5,5,7,6,7],
[9,6,0,6,5,6,6,6,6,3,9,9],
[4,4,5,0,4,5,3,5,5,4,4,8],
[5,5,6,7,0,4,1,5,5,1,7,7],
[3,4,5,6,7,0,4,5,5,0,5,7],
[4,7,5,8,10,7,0,5,5,7,7,7],
[5,6,5,6,6,6,6,0,5,5,6,5],
[9,6,5,6,6,6,6,6,0,3,6,6],
[8,4,8,7,10,11,4,6,8,0,10,11],
[6,5,2,7,4,6,4,5,5,1,0,10],
[3,4,2,3,4,4,4,6,5,0,1,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 140, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,4,9,4,2,4,4,4,7,6,7],
[6,0,4,6,6,2,4,6,4,4,6,6],
[7,7,0,7,6,4,7,7,6,7,7,7],
[2,5,4,0,4,4,2,4,4,2,4,4],
[7,5,5,7,0,4,3,7,2,5,9,9],
[9,9,7,7,7,0,5,9,4,7,9,11],
[7,7,4,9,8,6,0,9,6,9,9,9],
[7,5,4,7,4,2,2,0,6,5,4,9],
[7,7,5,7,9,7,5,5,0,7,7,7],
[4,7,4,9,6,4,2,6,4,0,6,4],
[5,5,4,7,2,2,2,7,4,5,0,7],
[4,5,4,7,2,0,2,2,4,7,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 141, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,3,2,5,3,3,3,3,5,4,3],
[8,0,7,2,5,3,6,2,2,9,4,2],
[8,4,0,4,5,7,4,4,4,9,6,4],
[9,9,7,0,9,5,7,7,7,9,9,7],
[6,6,6,2,0,2,4,2,2,4,6,2],
[8,8,4,6,9,0,8,6,8,8,6,6],
[8,5,7,4,7,3,0,5,3,9,4,7],
[8,9,7,4,9,5,6,0,2,9,4,5],
[8,9,7,4,9,3,8,9,0,9,4,7],
[6,2,2,2,7,3,2,2,2,0,6,2],
[7,7,5,2,5,5,7,7,7,5,0,5],
[8,9,7,4,9,5,4,6,4,9,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 142, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,6,6,4,6,7,6,4,5,3,6],
[6,0,7,7,8,6,9,7,6,5,4,6],
[5,4,0,6,6,5,7,5,4,6,4,6],
[5,4,5,0,6,3,5,4,3,4,4,7],
[7,3,5,5,0,4,7,6,4,5,5,4],
[5,5,6,8,7,0,8,4,4,6,6,6],
[4,2,4,6,4,3,0,3,1,4,1,5],
[5,4,6,7,5,7,8,0,5,5,3,6],
[7,5,7,8,7,7,10,6,0,6,7,6],
[6,6,5,7,6,5,7,6,5,0,6,5],
[8,7,7,7,6,5,10,8,4,5,0,7],
[5,5,5,4,7,5,6,5,5,6,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 143, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,4,4,6,7,6,3,4,3,6,3],
[5,0,3,2,3,6,4,5,1,3,6,2],
[7,8,0,5,7,8,9,9,5,6,8,6],
[7,9,6,0,8,8,9,6,5,7,8,5],
[5,8,4,3,0,4,6,6,2,3,8,5],
[4,5,3,3,7,0,8,5,3,0,6,6],
[5,7,2,2,5,3,0,6,4,2,7,4],
[8,6,2,5,5,6,5,0,5,5,8,3],
[7,10,6,6,9,8,7,6,0,7,8,5],
[8,8,5,4,8,11,9,6,4,0,7,8],
[5,5,3,3,3,5,4,3,3,4,0,2],
[8,9,5,6,6,5,7,8,6,3,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 144, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1,3,0,6,6,6,0,3,0,0,0],
[10,0,3,3,6,6,6,3,3,6,3,3],
[8,8,0,4,7,5,5,4,1,4,4,5],
[11,8,7,0,11,11,11,4,7,8,5,5],
[5,5,4,0,0,1,4,1,1,0,0,1],
[5,5,6,0,10,0,8,1,3,1,1,1],
[5,5,6,0,7,3,0,3,3,3,4,1],
[11,8,7,7,10,10,8,0,4,7,4,7],
[8,8,10,4,10,8,8,7,0,7,7,5],
[11,5,7,3,11,10,8,4,4,0,8,5],
[11,8,7,6,11,10,7,7,4,3,0,7],
[11,8,6,6,10,10,10,4,6,6,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 145, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,5,2,5,3,6,1,5,2,2,6],
[9,0,5,5,6,7,7,10,6,6,5,7],
[6,6,0,4,7,3,7,7,6,3,5,6],
[9,6,7,0,9,4,10,7,9,3,7,10],
[6,5,4,2,0,3,3,6,6,3,5,6],
[8,4,8,7,8,0,8,5,8,4,8,9],
[5,4,4,1,8,3,0,6,7,2,4,10],
[10,1,4,4,5,6,5,0,4,5,5,6],
[6,5,5,2,5,3,4,7,0,3,6,8],
[9,5,8,8,8,7,9,6,8,0,6,9],
[9,6,6,4,6,3,7,6,5,5,0,6],
[5,4,5,1,5,2,1,5,3,2,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 146, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,6,4,2,2,7,2,4,1,4,5],
[9,0,6,5,5,5,5,6,8,3,6,6],
[5,5,0,4,4,3,7,3,5,2,4,6],
[7,6,7,0,7,4,6,6,8,7,4,6],
[9,6,7,4,0,4,6,3,7,2,4,7],
[9,6,8,7,7,0,8,4,8,3,3,8],
[4,6,4,5,5,3,0,4,5,2,3,4],
[9,5,8,5,8,7,7,0,6,4,5,7],
[7,3,6,3,4,3,6,5,0,3,5,4],
[10,8,9,4,9,8,9,7,8,0,5,8],
[7,5,7,7,7,8,8,6,6,6,0,6],
[6,5,5,5,4,3,7,4,7,3,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 147, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,4,9,4,6,5,9,7,11,11,11],
[5,0,0,5,5,2,5,5,7,7,7,7],
[7,11,0,7,7,2,7,7,7,7,7,7],
[2,6,4,0,2,2,5,9,7,7,6,6],
[7,6,4,9,0,2,5,9,7,11,11,11],
[5,9,9,9,9,0,5,9,7,11,11,11],
[6,6,4,6,6,6,0,9,7,11,6,6],
[2,6,4,2,2,2,2,0,7,2,2,2],
[4,4,4,4,4,4,4,4,0,6,4,6],
[0,4,4,4,0,0,0,9,5,0,4,6],
[0,4,4,5,0,0,5,9,7,7,0,2],
[0,4,4,5,0,0,5,9,5,5,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 148, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,8,7,2,7,8,10,8,6,8,2],
[6,0,6,5,5,7,9,11,8,6,6,5],
[3,5,0,5,0,2,3,8,4,3,4,5],
[4,6,6,0,6,7,6,11,8,9,4,6],
[9,6,11,5,0,5,7,9,8,4,6,6],
[4,4,9,4,6,0,6,7,6,9,7,4],
[3,2,8,5,4,5,0,5,8,6,6,2],
[1,0,3,0,2,4,6,0,5,3,1,2],
[3,3,7,3,3,5,3,6,0,3,4,3],
[5,5,8,2,7,2,5,8,8,0,6,5],
[3,5,7,7,5,4,5,10,7,5,0,5],
[9,6,6,5,5,7,9,9,8,6,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 149, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,6,5,5,5,5,3,8,8,5,11],
[6,0,6,6,6,5,3,3,8,3,9,8],
[5,5,0,5,8,8,2,8,11,5,5,11],
[6,5,6,0,8,5,3,3,8,8,5,11],
[6,5,3,3,0,2,0,0,8,3,3,8],
[6,6,3,6,9,0,3,6,11,3,6,11],
[6,8,9,8,11,8,0,6,11,5,11,11],
[8,8,3,8,11,5,5,0,8,8,8,11],
[3,3,0,3,3,0,0,3,0,3,3,5],
[3,8,6,3,8,8,6,3,8,0,6,11],
[6,2,6,6,8,5,0,3,8,5,0,8],
[0,3,0,0,3,0,0,0,6,0,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 150, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,7,4,4,5,7,6,7,6,6,4],
[5,0,5,5,4,4,6,8,5,4,4,4],
[4,6,0,5,4,3,6,5,4,7,5,5],
[7,6,6,0,4,5,9,6,6,7,3,5],
[7,7,7,7,0,4,9,8,8,5,5,4],
[6,7,8,6,7,0,9,6,6,6,5,6],
[4,5,5,2,2,2,0,5,3,5,2,3],
[5,3,6,5,3,5,6,0,7,5,6,3],
[4,6,7,5,3,5,8,4,0,6,6,5],
[5,7,4,4,6,5,6,6,5,0,4,6],
[5,7,6,8,6,6,9,5,5,7,0,6],
[7,7,6,6,7,5,8,8,6,5,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 151, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,6,8,5,7,6,4,5,7,5,7],
[4,0,3,8,2,4,3,6,4,8,4,7],
[5,8,0,7,5,7,7,4,8,8,6,8],
[3,3,4,0,3,4,5,4,4,7,5,6],
[6,9,6,8,0,6,5,7,6,8,4,7],
[4,7,4,7,5,0,5,4,6,6,3,8],
[5,8,4,6,6,6,0,7,6,5,4,6],
[7,5,7,7,4,7,4,0,6,6,5,7],
[6,7,3,7,5,5,5,5,0,6,5,9],
[4,3,3,4,3,5,6,5,5,0,4,8],
[6,7,5,6,7,8,7,6,6,7,0,8],
[4,4,3,5,4,3,5,4,2,3,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 152, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,9,4,6,7,7,8,8,4,5,9],
[5,0,9,2,2,5,7,5,4,4,4,7],
[2,2,0,2,3,3,4,4,4,4,4,3],
[7,9,9,0,8,7,7,9,8,5,7,9],
[5,9,8,3,0,9,7,10,9,5,4,8],
[4,6,8,4,2,0,6,6,5,6,3,6],
[4,4,7,4,4,5,0,6,5,6,5,6],
[3,6,7,2,1,5,5,0,5,2,3,8],
[3,7,7,3,2,6,6,6,0,3,5,7],
[7,7,7,6,6,5,5,9,8,0,7,7],
[6,7,7,4,7,8,6,8,6,4,0,8],
[2,4,8,2,3,5,5,3,4,4,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 153, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,7,4,7,7,6,7,0,9,3,4],
[7,0,8,4,8,8,6,10,1,6,4,4],
[4,3,0,3,10,6,3,4,3,9,6,6],
[7,7,8,0,11,10,3,11,4,10,7,7],
[4,3,1,0,0,3,0,4,0,9,0,0],
[4,3,5,1,8,0,3,4,4,6,4,3],
[5,5,8,8,11,8,0,8,2,11,5,5],
[4,1,7,0,7,7,3,0,1,7,4,4],
[11,10,8,7,11,7,9,10,0,9,10,4],
[2,5,2,1,2,5,0,4,2,0,2,2],
[8,7,5,4,11,7,6,7,1,9,0,4],
[7,7,5,4,11,8,6,7,7,9,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 154, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,5,6,6,7,7,5,6,6,8,6],
[2,0,3,2,5,4,4,3,3,4,3,2],
[6,8,0,4,4,5,8,7,7,6,6,4],
[5,9,7,0,5,5,8,4,5,5,5,5],
[5,6,7,6,0,4,8,4,6,5,5,6],
[4,7,6,6,7,0,7,5,5,4,5,4],
[4,7,3,3,3,4,0,4,5,4,3,3],
[6,8,4,7,7,6,7,0,7,6,6,6],
[5,8,4,6,5,6,6,4,0,4,5,4],
[5,7,5,6,6,7,7,5,7,0,4,4],
[3,8,5,6,6,6,8,5,6,7,0,4],
[5,9,7,6,5,7,8,5,7,7,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 155, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,7,5,5,3,5,6,7,3,4,3],
[5,0,4,3,2,3,4,3,3,3,2,3],
[4,7,0,5,3,4,4,4,6,3,4,2],
[6,8,6,0,5,5,5,5,6,6,6,4],
[6,9,8,6,0,5,7,7,6,5,6,5],
[8,8,7,6,6,0,6,8,4,5,5,5],
[6,7,7,6,4,5,0,5,7,4,5,5],
[5,8,7,6,4,3,6,0,5,4,4,4],
[4,8,5,5,5,7,4,6,0,6,3,3],
[8,8,8,5,6,6,7,7,5,0,5,7],
[7,9,7,5,5,6,6,7,8,6,0,5],
[8,8,9,7,6,6,6,7,8,4,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 156, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,2,3,2,5,6,2,3,6,2,4],
[9,0,4,5,6,5,6,2,3,6,2,7],
[9,7,0,9,8,4,7,3,1,7,5,8],
[8,6,2,0,5,3,6,3,0,5,5,5],
[9,5,3,6,0,6,5,3,1,5,4,4],
[6,6,7,8,5,0,5,4,3,5,2,4],
[5,5,4,5,6,6,0,4,5,4,2,6],
[9,9,8,8,8,7,7,0,3,8,6,7],
[8,8,10,11,10,8,6,8,0,10,5,7],
[5,5,4,6,6,6,7,3,1,0,3,7],
[9,9,6,6,7,9,9,5,6,8,0,7],
[7,4,3,6,7,7,5,4,4,4,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 157, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,6,5,3,6,7,4,8,5,4,7],
[5,0,5,7,4,6,8,5,7,7,3,6],
[5,6,0,7,4,4,7,7,9,6,6,8],
[6,4,4,0,6,2,5,7,6,7,5,6],
[8,7,7,5,0,6,9,7,8,6,6,7],
[5,5,7,9,5,0,7,6,9,6,3,8],
[4,3,4,6,2,4,0,6,5,4,2,5],
[7,6,4,4,4,5,5,0,5,4,3,6],
[3,4,2,5,3,2,6,6,0,6,1,4],
[6,4,5,4,5,5,7,7,5,0,3,4],
[7,8,5,6,5,8,9,8,10,8,0,9],
[4,5,3,5,4,3,6,5,7,7,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 158, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,9,6,8,6,9,7,4,3,6,3],
[5,0,4,7,11,11,4,4,4,4,7,7],
[2,7,0,4,7,7,10,2,5,4,7,4],
[5,4,7,0,7,8,6,6,7,4,7,2],
[3,0,4,4,0,9,3,2,2,4,5,3],
[5,0,4,3,2,0,3,1,1,3,3,2],
[2,7,1,5,8,8,0,1,5,1,5,4],
[4,7,9,5,9,10,10,0,8,5,10,6],
[7,7,6,4,9,10,6,3,0,5,6,5],
[8,7,7,7,7,8,10,6,6,0,7,4],
[5,4,4,4,6,8,6,1,5,4,0,3],
[8,4,7,9,8,9,7,5,6,7,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 159, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,3,6,4,4,7,5,7,6,7,5],
[5,0,7,8,6,6,8,7,7,8,7,5],
[8,4,0,5,6,5,7,5,7,6,6,6],
[5,3,6,0,6,5,5,3,6,7,6,4],
[7,5,5,5,0,4,5,4,7,9,5,5],
[7,5,6,6,7,0,6,6,6,9,7,5],
[4,3,4,6,6,5,0,5,6,7,7,5],
[6,4,6,8,7,5,6,0,6,8,6,5],
[4,4,4,5,4,5,5,5,0,7,7,5],
[5,3,5,4,2,2,4,3,4,0,4,4],
[4,4,5,5,6,4,4,5,4,7,0,4],
[6,6,5,7,6,6,6,6,6,7,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 160, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,8,10,4,5,8,6,8,5,8,7],
[4,0,6,6,8,6,8,7,7,7,4,6],
[3,5,0,4,4,2,6,5,4,4,4,4],
[1,5,7,0,4,3,8,5,4,5,4,4],
[7,3,7,7,0,6,9,6,8,4,5,5],
[6,5,9,8,5,0,9,4,9,3,7,7],
[3,3,5,3,2,2,0,5,5,2,4,4],
[5,4,6,6,5,7,6,0,6,5,6,4],
[3,4,7,7,3,2,6,5,0,2,6,6],
[6,4,7,6,7,8,9,6,9,0,5,5],
[3,7,7,7,6,4,7,5,5,6,0,6],
[4,5,7,7,6,4,7,7,5,6,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 161, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,7,9,6,7,6,5,6,5,5,4],
[6,0,6,8,5,7,7,5,6,6,6,6],
[4,5,0,6,5,5,7,3,3,5,6,5],
[2,3,5,0,3,5,6,3,5,2,3,2],
[5,6,6,8,0,5,6,4,5,5,6,6],
[4,4,6,6,6,0,4,4,5,4,4,3],
[5,4,4,5,5,7,0,2,3,3,5,3],
[6,6,8,8,7,7,9,0,5,5,8,5],
[5,5,8,6,6,6,8,6,0,4,7,5],
[6,5,6,9,6,7,8,6,7,0,6,5],
[6,5,5,8,5,7,6,3,4,5,0,4],
[7,5,6,9,5,8,8,6,6,6,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 162, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,8,6,3,3,10,10,2,8,7,7],
[7,0,8,9,5,5,8,10,6,8,11,8],
[3,3,0,8,2,1,8,10,4,7,7,4],
[5,2,3,0,3,2,7,9,2,7,4,4],
[8,6,9,8,0,6,8,9,5,6,10,10],
[8,6,10,9,5,0,9,9,7,8,8,8],
[1,3,3,4,3,2,0,9,2,8,5,5],
[1,1,1,2,2,2,2,0,2,7,2,3],
[9,5,7,9,6,4,9,9,0,7,10,7],
[3,3,4,4,5,3,3,4,4,0,4,6],
[4,0,4,7,1,3,6,9,1,7,0,3],
[4,3,7,7,1,3,6,8,4,5,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 163, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,5,4,3,5,3,6,2,2,3,6],
[5,0,4,4,4,6,5,5,4,4,5,4],
[6,7,0,6,6,6,7,6,3,6,7,5],
[7,7,5,0,5,6,7,10,8,6,7,8],
[8,7,5,6,0,6,9,7,5,6,7,8],
[6,5,5,5,5,0,3,6,3,4,5,6],
[8,6,4,4,2,8,0,4,5,4,4,4],
[5,6,5,1,4,5,7,0,4,4,6,7],
[9,7,8,3,6,8,6,7,0,7,4,6],
[9,7,5,5,5,7,7,7,4,0,5,6],
[8,6,4,4,4,6,7,5,7,6,0,5],
[5,7,6,3,3,5,7,4,5,5,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 164, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,6,10,2,10,10,10,10,11,11,4],
[5,0,7,9,7,5,8,8,5,9,11,4],
[5,4,0,8,1,5,4,4,5,5,7,0],
[1,2,3,0,3,1,0,4,1,3,7,0],
[9,4,10,8,0,9,8,8,9,9,11,8],
[1,6,6,10,2,0,8,10,1,11,11,4],
[1,3,7,11,3,3,0,6,1,7,11,5],
[1,3,7,7,3,1,5,0,1,7,7,5],
[1,6,6,10,2,10,10,10,0,11,11,4],
[0,2,6,8,2,0,4,4,0,0,7,0],
[0,0,4,4,0,0,0,4,0,4,0,4],
[7,7,11,11,3,7,6,6,7,11,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 165, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,3,4,5,5,6,5,5,8,6,5],
[7,0,7,6,4,5,6,5,8,8,7,7],
[8,4,0,7,5,7,6,9,8,7,9,7],
[7,5,4,0,4,4,7,4,8,7,5,6],
[6,7,6,7,0,4,8,5,7,6,7,5],
[6,6,4,7,7,0,7,4,5,7,10,5],
[5,5,5,4,3,4,0,5,5,7,6,6],
[6,6,2,7,6,7,6,0,6,8,8,7],
[6,3,3,3,4,6,6,5,0,7,6,5],
[3,3,4,4,5,4,4,3,4,0,5,5],
[5,4,2,6,4,1,5,3,5,6,0,5],
[6,4,4,5,6,6,5,4,6,6,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 166, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,6,8,7,8,3,4,7,8,5,8],
[4,0,7,5,7,5,4,5,6,8,8,8],
[5,4,0,4,5,4,1,4,7,4,4,8],
[3,6,7,0,7,4,6,4,5,6,4,7],
[4,4,6,4,0,4,3,7,5,4,5,7],
[3,6,7,7,7,0,4,7,7,8,6,9],
[8,7,10,5,8,7,0,4,8,7,8,9],
[7,6,7,7,4,4,7,0,7,6,6,10],
[4,5,4,6,6,4,3,4,0,6,3,9],
[3,3,7,5,7,3,4,5,5,0,3,8],
[6,3,7,7,6,5,3,5,8,8,0,6],
[3,3,3,4,4,2,2,1,2,3,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 167, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,7,6,6,6,3,6,7,7,6,8],
[4,0,5,7,6,7,2,5,6,7,6,9],
[4,6,0,6,5,7,1,4,6,5,8,5],
[5,4,5,0,8,9,3,6,8,6,6,8],
[5,5,6,3,0,7,4,7,6,4,8,4],
[5,4,4,2,4,0,1,3,5,5,6,5],
[8,9,10,8,7,10,0,5,7,7,9,9],
[5,6,7,5,4,8,6,0,6,5,8,7],
[4,5,5,3,5,6,4,5,0,6,5,5],
[4,4,6,5,7,6,4,6,5,0,7,7],
[5,5,3,5,3,5,2,3,6,4,0,6],
[3,2,6,3,7,6,2,4,6,4,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 168, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,5,5,5,6,5,3,2,4,3,4],
[5,0,5,5,4,5,7,6,3,5,6,6],
[6,6,0,7,6,9,5,6,5,7,5,7],
[6,6,4,0,5,8,3,5,6,5,4,5],
[6,7,5,6,0,8,6,6,5,6,6,6],
[5,6,2,3,3,0,4,3,2,4,3,5],
[6,4,6,8,5,7,0,8,6,5,7,8],
[8,5,5,6,5,8,3,0,5,5,7,7],
[9,8,6,5,6,9,5,6,0,5,5,6],
[7,6,4,6,5,7,6,6,6,0,5,7],
[8,5,6,7,5,8,4,4,6,6,0,7],
[7,5,4,6,5,6,3,4,5,4,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 169, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,11,11,11,4,6,11,10,9,4,11,10],
[0,0,11,8,1,6,8,7,9,4,11,7],
[0,0,0,2,1,3,7,7,5,3,8,7],
[0,3,9,0,4,4,11,10,9,4,8,10],
[7,10,10,7,0,5,7,10,8,8,10,7],
[5,5,8,7,6,0,8,7,6,6,8,7],
[0,3,4,0,4,3,0,8,8,3,8,10],
[1,4,4,1,1,4,3,0,4,4,9,2],
[2,2,6,2,3,5,3,7,0,6,10,2],
[7,7,8,7,3,5,8,7,5,0,10,7],
[0,0,3,3,1,3,3,2,1,1,0,2],
[1,4,4,1,4,4,1,9,9,4,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 170, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,9,9,9,4,9,5,10,4,4,4],
[2,0,11,5,10,5,6,6,11,6,1,2],
[2,0,0,5,10,5,6,6,6,2,1,2],
[2,6,6,0,7,2,7,2,7,2,2,2],
[2,1,1,4,0,5,6,6,6,1,1,2],
[7,6,6,9,6,0,6,7,11,1,7,7],
[2,5,5,4,5,5,0,6,11,1,1,2],
[6,5,5,9,5,4,5,0,10,0,1,0],
[1,0,5,4,5,0,0,1,0,0,0,0],
[7,5,9,9,10,10,10,11,11,0,6,6],
[7,10,10,9,10,4,10,10,11,5,0,1],
[7,9,9,9,9,4,9,11,11,5,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 171, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,7,5,8,5,4,6,6,4,6,5],
[4,0,4,8,4,4,3,6,5,4,4,7],
[4,7,0,9,8,6,5,7,9,6,8,9],
[6,3,2,0,5,3,3,4,4,2,5,6],
[3,7,3,6,0,7,4,5,8,5,3,7],
[6,7,5,8,4,0,4,6,7,5,4,9],
[7,8,6,8,7,7,0,6,9,7,5,8],
[5,5,4,7,6,5,5,0,7,4,3,6],
[5,6,2,7,3,4,2,4,0,4,4,5],
[7,7,5,9,6,6,4,7,7,0,6,9],
[5,7,3,6,8,7,6,8,7,5,0,7],
[6,4,2,5,4,2,3,5,6,2,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 172, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,7,11,11,4,7,11,11,11,7,7],
[8,0,4,8,8,4,4,8,8,8,4,8],
[4,7,0,8,11,8,8,8,4,4,8,8],
[0,3,3,0,7,0,3,7,7,7,7,3],
[0,3,0,4,0,0,4,8,4,4,4,4],
[7,7,3,11,11,0,7,11,7,7,7,11],
[4,7,3,8,7,4,0,8,7,4,4,8],
[0,3,3,4,3,0,3,0,3,0,4,0],
[0,3,7,4,7,4,4,8,0,4,4,4],
[0,3,7,4,7,4,7,11,7,0,7,7],
[4,7,3,4,7,4,7,7,7,4,0,7],
[4,3,3,8,7,0,3,11,7,4,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 173, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,8,5,6,9,4,5,7,3,4,4],
[6,0,6,6,6,7,3,3,5,7,6,5],
[3,5,0,5,1,5,3,2,2,2,2,5],
[6,5,6,0,4,8,6,4,4,3,3,3],
[5,5,10,7,0,8,4,6,6,5,4,7],
[2,4,6,3,3,0,3,4,4,2,3,1],
[7,8,8,5,7,8,0,7,5,6,6,6],
[6,8,9,7,5,7,4,0,5,5,6,8],
[4,6,9,7,5,7,6,6,0,2,5,7],
[8,4,9,8,6,9,5,6,9,0,6,7],
[7,5,9,8,7,8,5,5,6,5,0,8],
[7,6,6,8,4,10,5,3,4,4,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 174, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,5,4,4,6,1,8,6,4,5,3],
[11,0,6,4,11,6,8,9,9,8,9,9],
[6,5,0,6,6,8,6,11,11,7,5,8],
[7,7,5,0,7,5,4,8,8,7,5,5],
[7,0,5,4,0,6,2,9,6,4,2,3],
[5,5,3,6,5,0,4,7,4,6,4,6],
[10,3,5,7,9,7,0,8,9,7,8,10],
[3,2,0,3,2,4,3,0,7,3,1,4],
[5,2,0,3,5,7,2,4,0,6,4,7],
[7,3,4,4,7,5,4,8,5,0,4,5],
[6,2,6,6,9,7,3,10,7,7,0,4],
[8,2,3,6,8,5,1,7,4,6,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 175, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,11,4,8,3,7,6,3,7,10,10],
[8,0,8,8,5,8,7,10,8,7,7,7],
[0,3,0,0,0,0,3,3,0,4,3,3],
[7,3,11,0,8,7,4,10,10,4,7,10],
[3,6,11,3,0,3,7,6,3,7,10,10],
[8,3,11,4,8,0,7,10,8,7,10,10],
[4,4,8,7,4,4,0,10,7,11,7,7],
[5,1,8,1,5,1,1,0,8,4,5,5],
[8,3,11,1,8,3,4,3,0,4,7,7],
[4,4,7,7,4,4,0,7,7,0,4,7],
[1,4,8,4,1,1,4,6,4,7,0,7],
[1,4,8,1,1,1,4,6,4,4,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 176, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,5,6,4,3,4,6,5,3,7,7],
[8,0,9,5,8,7,8,7,6,6,8,6],
[6,2,0,5,3,4,3,4,4,4,6,4],
[5,6,6,0,3,6,6,6,6,5,4,5],
[7,3,8,8,0,5,6,6,5,6,8,6],
[8,4,7,5,6,0,5,6,6,4,7,7],
[7,3,8,5,5,6,0,5,4,5,7,7],
[5,4,7,5,5,5,6,0,4,3,4,4],
[6,5,7,5,6,5,7,7,0,6,6,7],
[8,5,7,6,5,7,6,8,5,0,7,6],
[4,3,5,7,3,4,4,7,5,4,0,3],
[4,5,7,6,5,4,4,7,4,5,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 177, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,5,4,5,6,7,4,7,5,7,6],
[6,0,4,3,3,7,7,5,7,4,6,5],
[6,7,0,3,6,7,7,4,7,6,6,5],
[7,8,8,0,4,7,6,3,7,4,5,6],
[6,8,5,7,0,8,5,5,6,7,6,5],
[5,4,4,4,3,0,4,2,5,3,4,4],
[4,4,4,5,6,7,0,3,5,4,5,4],
[7,6,7,8,6,9,8,0,5,5,6,7],
[4,4,4,4,5,6,6,6,0,5,6,5],
[6,7,5,7,4,8,7,6,6,0,7,5],
[4,5,5,6,5,7,6,5,5,4,0,6],
[5,6,6,5,6,7,7,4,6,6,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 178, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,8,7,5,6,10,8,9,5,4,4],
[2,0,5,5,5,2,8,5,6,5,5,6],
[3,6,0,6,4,7,6,4,6,6,3,6],
[4,6,5,0,7,5,3,5,4,6,4,5],
[6,6,7,4,0,6,7,5,7,3,6,6],
[5,9,4,6,5,0,7,4,5,7,5,4],
[1,3,5,8,4,4,0,6,5,6,1,5],
[3,6,7,6,6,7,5,0,9,6,3,4],
[2,5,5,7,4,6,6,2,0,5,0,3],
[6,6,5,5,8,4,5,5,6,0,4,4],
[7,6,8,7,5,6,10,8,11,7,0,9],
[7,5,5,6,5,7,6,7,8,7,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 179, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,3,4,4,6,3,5,3,5,4,4],
[8,0,5,6,6,8,5,9,3,7,5,7],
[8,6,0,6,7,9,5,8,7,11,6,5],
[7,5,5,0,6,8,6,6,5,8,5,8],
[7,5,4,5,0,8,4,7,5,7,6,5],
[5,3,2,3,3,0,3,5,4,6,3,3],
[8,6,6,5,7,8,0,9,5,8,5,6],
[6,2,3,5,4,6,2,0,5,5,2,5],
[8,8,4,6,6,7,6,6,0,8,4,5],
[6,4,0,3,4,5,3,6,3,0,5,3],
[7,6,5,6,5,8,6,9,7,6,0,7],
[7,4,6,3,6,8,5,6,6,8,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 180, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,7,4,6,7,6,7,4,10,5,6],
[4,0,7,4,6,7,6,7,5,4,9,6],
[4,4,0,7,9,8,7,9,5,7,8,6],
[7,7,4,0,5,7,5,3,3,9,7,6],
[5,5,2,6,0,6,8,8,5,8,9,5],
[4,4,3,4,5,0,5,7,5,7,5,6],
[5,5,4,6,3,6,0,8,6,9,5,7],
[4,4,2,8,3,4,3,0,1,7,5,4],
[7,6,6,8,6,6,5,10,0,10,5,10],
[1,7,4,2,3,4,2,4,1,0,5,3],
[6,2,3,4,2,6,6,6,6,6,0,6],
[5,5,5,5,6,5,4,7,1,8,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 181, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,7,1,5,3,6,2,6,0,4,5],
[9,0,5,4,6,7,8,7,10,5,7,7],
[4,6,0,4,4,4,7,4,7,4,5,6],
[10,7,7,0,7,5,7,6,8,7,5,7],
[6,5,7,4,0,6,9,5,6,4,7,5],
[8,4,7,6,5,0,6,5,6,5,8,6],
[5,3,4,4,2,5,0,6,4,3,6,4],
[9,4,7,5,6,6,5,0,8,5,6,7],
[5,1,4,3,5,5,7,3,0,3,3,7],
[11,6,7,4,7,6,8,6,8,0,5,8],
[7,4,6,6,4,3,5,5,8,6,0,6],
[6,4,5,4,6,5,7,4,4,3,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 182, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1,4,9,10,6,10,9,4,6,6,9],
[10,0,4,9,10,6,11,9,7,6,6,10],
[7,7,0,10,10,5,8,10,6,4,7,7],
[2,2,1,0,7,6,7,5,2,2,3,4],
[1,1,1,4,0,6,2,3,1,1,0,1],
[5,5,6,5,5,0,6,5,5,2,5,5],
[1,0,3,4,9,5,0,3,3,3,3,4],
[2,2,1,6,8,6,8,0,2,2,4,5],
[7,4,5,9,10,6,8,9,0,6,6,9],
[5,5,7,9,10,9,8,9,5,0,6,8],
[5,5,4,8,11,6,8,7,5,5,0,8],
[2,1,4,7,10,6,7,6,2,3,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 183, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,8,6,4,4,11,8,7,8,9,6],
[2,0,2,6,2,6,6,6,3,2,4,2],
[3,9,0,7,2,7,7,6,3,3,5,3],
[5,5,4,0,4,9,5,4,5,4,5,7],
[7,9,9,7,0,5,11,11,11,11,9,7],
[7,5,4,2,6,0,7,6,7,6,5,6],
[0,5,4,6,0,4,0,0,1,0,1,2],
[3,5,5,7,0,5,11,0,3,1,1,3],
[4,8,8,6,0,4,10,8,0,4,4,2],
[3,9,8,7,0,5,11,10,7,0,5,3],
[2,7,6,6,2,6,10,10,7,6,0,2],
[5,9,8,4,4,5,9,8,9,8,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 184, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,5,5,7,6,7,6,5,9,7,5],
[4,0,4,5,8,8,5,5,9,3,6,4],
[6,7,0,6,8,9,6,5,9,5,7,5],
[6,6,5,0,4,6,2,5,6,5,6,2],
[4,3,3,7,0,4,3,6,3,6,4,7],
[5,3,2,5,7,0,3,5,6,4,7,5],
[4,6,5,9,8,8,0,8,5,3,8,4],
[5,6,6,6,5,6,3,0,5,4,5,2],
[6,2,2,5,8,5,6,6,0,5,7,5],
[2,8,6,6,5,7,8,7,6,0,7,6],
[4,5,4,5,7,4,3,6,4,4,0,5],
[6,7,6,9,4,6,7,9,6,5,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 185, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,7,7,5,9,6,4,7,6,7,7],
[3,0,3,5,4,8,4,3,7,4,3,4],
[4,8,0,6,3,7,5,4,4,5,5,5],
[4,6,5,0,3,6,6,3,7,5,4,6],
[6,7,8,8,0,8,5,6,7,5,8,7],
[2,3,4,5,3,0,3,1,3,3,3,3],
[5,7,6,5,6,8,0,5,7,5,5,6],
[7,8,7,8,5,10,6,0,9,7,6,8],
[4,4,7,4,4,8,4,2,0,3,3,7],
[5,7,6,6,6,8,6,4,8,0,6,6],
[4,8,6,7,3,8,6,5,8,5,0,6],
[4,7,6,5,4,8,5,3,4,5,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 186, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,8,9,11,9,5,11,8,11,11,6],
[7,0,5,7,10,8,4,9,9,7,9,5],
[3,6,0,3,8,7,4,9,8,6,7,4],
[2,4,8,0,9,9,4,11,8,9,9,6],
[0,1,3,2,0,4,1,4,3,6,7,1],
[2,3,4,2,7,0,3,6,5,6,9,4],
[6,7,7,7,10,8,0,11,10,6,11,5],
[0,2,2,0,7,5,0,0,4,5,3,1],
[3,2,3,3,8,6,1,7,0,3,7,1],
[0,4,5,2,5,5,5,6,8,0,9,5],
[0,2,4,2,4,2,0,8,4,2,0,3],
[5,6,7,5,10,7,6,10,10,6,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 187, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,8,5,8,5,10,8,9,4,9,3],
[3,0,5,0,4,5,7,1,5,1,8,3],
[3,6,0,5,8,5,7,5,6,1,6,1],
[6,11,6,0,6,10,10,5,11,6,11,6],
[3,7,3,5,0,7,7,1,8,4,8,3],
[6,6,6,1,4,0,10,4,10,6,10,6],
[1,4,4,1,4,1,0,4,6,5,9,3],
[3,10,6,6,10,7,7,0,7,3,8,6],
[2,6,5,0,3,1,5,4,0,6,7,5],
[7,10,10,5,7,5,6,8,5,0,8,9],
[2,3,5,0,3,1,2,3,4,3,0,3],
[8,8,10,5,8,5,8,5,6,2,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 188, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,7,6,7,6,5,6,6,6,5,8],
[9,0,7,6,5,7,4,5,6,8,5,9],
[4,4,0,4,2,5,4,2,3,4,3,6],
[5,5,7,0,7,6,6,4,5,3,6,5],
[4,6,9,4,0,5,5,3,4,5,8,7],
[5,4,6,5,6,0,4,3,7,5,5,7],
[6,7,7,5,6,7,0,3,5,6,6,8],
[5,6,9,7,8,8,8,0,6,4,7,5],
[5,5,8,6,7,4,6,5,0,4,7,7],
[5,3,7,8,6,6,5,7,7,0,6,9],
[6,6,8,5,3,6,5,4,4,5,0,8],
[3,2,5,6,4,4,3,6,4,2,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 189, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,7,3,5,2,0,6,6,2,2,4],
[2,0,2,1,1,3,1,1,3,0,0,3],
[4,9,0,7,9,2,4,10,6,6,3,5],
[8,10,4,0,6,3,2,7,7,1,6,8],
[6,10,2,5,0,4,6,8,7,5,3,3],
[9,8,9,8,7,0,8,8,10,4,4,9],
[11,10,7,9,5,3,0,9,10,5,5,8],
[5,10,1,4,3,3,2,0,7,2,3,5],
[5,8,5,4,4,1,1,4,0,0,4,6],
[9,11,5,10,6,7,6,9,11,0,6,8],
[9,11,8,5,8,7,6,8,7,5,0,6],
[7,8,6,3,8,2,3,6,5,3,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 190, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,6,8,5,6,8,8,6,7,7,5],
[6,0,6,8,6,6,9,6,6,7,10,4],
[5,5,0,7,5,3,8,5,6,5,7,3],
[3,3,4,0,4,0,8,4,4,3,5,5],
[6,5,6,7,0,3,8,5,8,5,8,6],
[5,5,8,11,8,0,11,7,8,8,7,7],
[3,2,3,3,3,0,0,6,5,2,5,0],
[3,5,6,7,6,4,5,0,5,3,5,4],
[5,5,5,7,3,3,6,6,0,4,7,2],
[4,4,6,8,6,3,9,8,7,0,5,4],
[4,1,4,6,3,4,6,6,4,6,0,2],
[6,7,8,6,5,4,11,7,9,7,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 191, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,5,6,6,5,3,4,6,8,3,5],
[6,0,10,10,6,6,6,5,5,6,6,8],
[6,1,0,3,3,4,2,4,6,5,6,5],
[5,1,8,0,6,3,1,4,4,4,4,4],
[5,5,8,5,0,4,4,5,5,5,5,5],
[6,5,7,8,7,0,2,6,5,9,4,6],
[8,5,9,10,7,9,0,5,6,10,6,8],
[7,6,7,7,6,5,6,0,7,6,4,5],
[5,6,5,7,6,6,5,4,0,5,7,5],
[3,5,6,7,6,2,1,5,6,0,3,5],
[8,5,5,7,6,7,5,7,4,8,0,5],
[6,3,6,7,6,5,3,6,6,6,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 192, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,2,7,6,4,2,5,4,4,3,6],
[7,0,5,7,6,5,6,6,5,5,4,6],
[9,6,0,7,8,6,5,7,7,7,6,7],
[4,4,4,0,5,6,5,6,4,5,4,8],
[5,5,3,6,0,4,5,7,3,4,3,7],
[7,6,5,5,7,0,6,6,6,6,3,8],
[9,5,6,6,6,5,0,7,7,5,5,7],
[6,5,4,5,4,5,4,0,6,7,5,6],
[7,6,4,7,8,5,4,5,0,4,3,6],
[7,6,4,6,7,5,6,4,7,0,4,7],
[8,7,5,7,8,8,6,6,8,7,0,8],
[5,5,4,3,4,3,4,5,5,4,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 193, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,7,6,5,6,5,5,5,5,5,5],
[6,0,9,5,8,8,8,8,9,7,7,8],
[4,2,0,5,5,3,4,1,3,2,4,1],
[5,6,6,0,7,6,7,7,6,4,6,7],
[6,3,6,4,0,7,5,5,4,5,7,4],
[5,3,8,5,4,0,7,6,3,8,6,4],
[6,3,7,4,6,4,0,5,3,4,7,4],
[6,3,10,4,6,5,6,0,4,4,5,5],
[6,2,8,5,7,8,8,7,0,9,7,7],
[6,4,9,7,6,3,7,7,2,0,9,6],
[6,4,7,5,4,5,4,6,4,2,0,4],
[6,3,10,4,7,7,7,6,4,5,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 194, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,2,2,4,2,2,5,3,4,2,3],
[9,0,8,6,10,6,8,7,3,10,10,7],
[9,3,0,6,9,7,5,7,3,6,6,6],
[9,5,5,0,7,6,7,11,6,4,5,4],
[7,1,2,4,0,1,3,6,3,4,1,4],
[9,5,4,5,10,0,5,7,5,7,5,6],
[9,3,6,4,8,6,0,6,2,5,5,6],
[6,4,4,0,5,4,5,0,0,4,5,1],
[8,8,8,5,8,6,9,11,0,8,8,7],
[7,1,5,7,7,4,6,7,3,0,4,8],
[9,1,5,6,10,6,6,6,3,7,0,7],
[8,4,5,7,7,5,5,10,4,3,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 195, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,10,7,6,8,9,7,8,6,5,6],
[3,0,8,6,4,5,8,6,5,5,4,5],
[1,3,0,3,2,3,6,6,2,4,3,4],
[4,5,8,0,5,9,9,7,4,4,5,6],
[5,7,9,6,0,7,9,8,6,4,8,7],
[3,6,8,2,4,0,9,7,5,3,5,6],
[2,3,5,2,2,2,0,5,3,5,3,2],
[4,5,5,4,3,4,6,0,4,3,4,4],
[3,6,9,7,5,6,8,7,0,4,4,6],
[5,6,7,7,7,8,6,8,7,0,6,6],
[6,7,8,6,3,6,8,7,7,5,0,7],
[5,6,7,5,4,5,9,7,5,5,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 196, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,4,7,7,3,7,4,3,4,4,0],
[11,0,8,11,11,7,11,4,3,8,11,8],
[7,3,0,7,3,3,7,0,3,7,3,0],
[4,0,4,0,0,3,7,0,3,4,0,4],
[4,0,8,11,0,3,7,4,3,4,0,4],
[8,4,8,8,8,0,8,8,7,8,8,8],
[4,0,4,4,4,3,0,0,3,4,4,4],
[7,7,11,11,7,3,11,0,7,7,7,7],
[8,8,8,8,8,4,8,4,0,8,8,8],
[7,3,4,7,7,3,7,4,3,0,3,0],
[7,0,8,11,11,3,7,4,3,8,0,4],
[11,3,11,7,7,3,7,4,3,11,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 197, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1,6,1,1,4,2,5,4,1,6,2],
[10,0,10,2,3,6,7,6,7,8,9,5],
[5,1,0,0,1,4,2,3,4,1,4,1],
[10,9,11,0,4,8,8,5,7,7,8,6],
[10,8,10,7,0,6,4,7,5,5,6,7],
[7,5,7,3,5,0,2,7,3,3,6,5],
[9,4,9,3,7,9,0,7,7,5,7,5],
[6,5,8,6,4,4,4,0,3,3,8,4],
[7,4,7,4,6,8,4,8,0,5,10,5],
[10,3,10,4,6,8,6,8,6,0,10,5],
[5,2,7,3,5,5,4,3,1,1,0,3],
[9,6,10,5,4,6,6,7,6,6,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 198, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,6,3,5,4,3,5,6,3,8,6],
[6,0,4,9,7,8,6,8,6,3,8,6],
[5,7,0,8,7,7,3,9,9,6,11,9],
[8,2,3,0,6,4,1,2,6,2,6,3],
[6,4,4,5,0,8,3,6,6,3,6,7],
[7,3,4,7,3,0,3,4,5,1,6,7],
[8,5,8,10,8,8,0,9,8,7,10,8],
[6,3,2,9,5,7,2,0,8,4,9,7],
[5,5,2,5,5,6,3,3,0,3,7,6],
[8,8,5,9,8,10,4,7,8,0,5,10],
[3,3,0,5,5,5,1,2,4,6,0,5],
[5,5,2,8,4,4,3,4,5,1,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 199, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,5,10,5,8,8,8,7,5,6,5],
[3,0,6,8,7,6,8,8,6,7,5,6],
[6,5,0,8,3,8,5,7,5,3,7,6],
[1,3,3,0,3,2,4,4,3,3,2,4],
[6,4,8,8,0,7,7,7,5,5,7,7],
[3,5,3,9,4,0,6,4,5,4,1,5],
[3,3,6,7,4,5,0,5,5,5,4,8],
[3,3,4,7,4,7,6,0,8,3,6,7],
[4,5,6,8,6,6,6,3,0,5,7,6],
[6,4,8,8,6,7,6,8,6,0,7,7],
[5,6,4,9,4,10,7,5,4,4,0,5],
[6,5,5,7,4,6,3,4,5,4,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 11, 200, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbrcwd/mebbrcwd_12_11.csv", index=False, header=False)