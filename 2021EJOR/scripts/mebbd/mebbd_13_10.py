
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg
from kemeny import sc

rep = 1
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,10,5,10,10,10,10,7,5,7,10,10,10],
[0,0,0,3,2,2,8,0,0,5,5,0,0],
[5,10,0,8,10,7,10,5,0,5,7,7,5],
[0,7,2,0,2,2,10,5,0,5,7,7,7],
[0,8,0,8,0,2,8,5,0,5,5,5,5],
[0,8,3,8,8,0,8,5,3,5,8,5,8],
[0,2,0,0,2,2,0,0,0,0,7,2,0],
[3,10,5,5,5,5,10,0,5,7,10,10,10],
[5,10,10,10,10,7,10,5,0,7,10,7,10],
[3,5,5,5,5,5,10,3,3,0,10,5,5],
[0,5,3,3,5,2,3,0,0,0,0,2,0],
[0,10,3,3,5,5,8,0,3,5,8,0,8],
[0,10,5,3,5,2,10,0,0,5,10,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 1, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,5,6,2,7,4,5,5,7,6,4,7],
[3,0,3,6,5,7,3,5,4,7,7,2,5],
[5,7,0,7,7,8,4,5,6,6,5,3,8],
[4,4,3,0,6,7,2,2,2,6,5,4,5],
[8,5,3,4,0,6,3,4,4,6,5,3,5],
[3,3,2,3,4,0,1,3,3,4,2,2,4],
[6,7,6,8,7,9,0,6,5,8,6,6,8],
[5,5,5,8,6,7,4,0,5,7,6,4,6],
[5,6,4,8,6,7,5,5,0,7,6,6,5],
[3,3,4,4,4,6,2,3,3,0,2,2,7],
[4,3,5,5,5,8,4,4,4,8,0,3,6],
[6,8,7,6,7,8,4,6,4,8,7,0,7],
[3,5,2,5,5,6,2,4,5,3,4,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 2, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,5,2,4,3,9,5,7,5,6,1,6],
[2,0,2,4,3,4,9,5,7,3,6,2,5],
[5,8,0,4,3,3,8,5,7,7,6,1,7],
[8,6,6,0,5,5,7,7,7,7,6,5,7],
[6,7,7,5,0,5,7,6,7,9,8,5,9],
[7,6,7,5,5,0,9,4,7,7,9,4,7],
[1,1,2,3,3,1,0,3,4,3,6,2,5],
[5,5,5,3,4,6,7,0,6,6,7,5,8],
[3,3,3,3,3,3,6,4,0,4,4,3,7],
[5,7,3,3,1,3,7,4,6,0,7,2,6],
[4,4,4,4,2,1,4,3,6,3,0,1,6],
[9,8,9,5,5,6,8,5,7,8,9,0,9],
[4,5,3,3,1,3,5,2,3,4,4,1,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 3, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,8,5,10,10,8,5,8,7,8,8,10],
[2,0,3,7,7,7,7,7,5,7,8,7,7],
[2,7,0,7,7,7,7,7,7,7,8,7,7],
[5,3,3,0,10,10,3,7,8,7,8,10,10],
[0,3,3,0,0,3,3,0,3,0,3,0,0],
[0,3,3,0,7,0,0,0,5,5,8,5,5],
[2,3,3,7,7,10,0,7,5,7,8,7,7],
[5,3,3,3,10,10,3,0,8,7,8,10,10],
[2,5,3,2,7,5,5,2,0,2,3,2,2],
[3,3,3,3,10,5,3,3,8,0,3,3,5],
[2,2,2,2,7,2,2,2,7,7,0,2,7],
[2,3,3,0,10,5,3,0,8,7,8,0,10],
[0,3,3,0,10,5,3,0,8,5,3,0,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 4, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,4,6,6,4,7,5,4,5,9,8,4],
[6,0,6,6,8,4,5,6,3,7,9,8,6],
[6,4,0,6,7,4,6,5,3,6,6,6,4],
[4,4,4,0,5,3,6,6,5,6,7,6,4],
[4,2,3,5,0,3,3,3,3,3,7,6,4],
[6,6,6,7,7,0,6,5,6,5,8,7,5],
[3,5,4,4,7,4,0,3,5,6,8,6,5],
[5,4,5,4,7,5,7,0,5,6,7,7,5],
[6,7,7,5,7,4,5,5,0,7,9,7,6],
[5,3,4,4,7,5,4,4,3,0,6,5,5],
[1,1,4,3,3,2,2,3,1,4,0,2,2],
[2,2,4,4,4,3,4,3,3,5,8,0,4],
[6,4,6,6,6,5,5,5,4,5,8,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 5, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,3,3,3,2,5,7,0,7,7,2,3],
[3,0,3,5,1,3,2,1,1,3,1,3,1],
[7,7,0,3,3,6,2,7,5,8,8,7,5],
[7,5,7,0,5,7,7,5,5,5,5,7,5],
[7,9,7,5,0,6,2,9,7,10,7,7,7],
[8,7,4,3,4,0,3,7,1,8,8,1,4],
[5,8,8,3,8,7,0,8,5,8,8,5,8],
[3,9,3,5,1,3,2,0,3,10,7,3,3],
[10,9,5,5,3,9,5,7,0,9,8,2,9],
[3,7,2,5,0,2,2,0,1,0,1,2,0],
[3,9,2,5,3,2,2,3,2,9,0,2,2],
[8,7,3,3,3,9,5,7,8,8,8,0,7],
[7,9,5,5,3,6,2,7,1,10,8,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 6, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,10,9,5,1,9,4,9,1,5,9,9],
[1,0,2,1,4,0,2,1,5,1,0,1,2],
[0,8,0,8,4,0,5,4,5,1,4,5,5],
[1,9,2,0,4,1,7,1,5,2,5,1,2],
[5,6,6,6,0,6,6,5,6,5,6,7,6],
[9,10,10,9,4,0,10,4,9,2,6,9,9],
[1,8,5,3,4,0,0,4,5,1,0,4,2],
[6,9,6,9,5,6,6,0,6,1,6,6,6],
[1,5,5,5,4,1,5,4,0,1,2,5,5],
[9,9,9,8,5,8,9,9,9,0,8,9,9],
[5,10,6,5,4,4,10,4,8,2,0,4,5],
[1,9,5,9,3,1,6,4,5,1,6,0,1],
[1,8,5,8,4,1,8,4,5,1,5,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 7, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,2,2,4,3,3,4,1,6,0,2,3],
[8,0,3,4,5,5,6,5,5,7,5,4,8],
[8,7,0,5,7,5,6,7,5,7,4,4,7],
[8,6,5,0,8,6,4,5,6,8,3,5,7],
[6,5,3,2,0,3,3,3,2,4,1,1,3],
[7,5,5,4,7,0,5,5,5,7,3,4,7],
[7,4,4,6,7,5,0,7,6,6,4,6,7],
[6,5,3,5,7,5,3,0,5,7,3,4,6],
[9,5,5,4,8,5,4,5,0,6,2,6,6],
[4,3,3,2,6,3,4,3,4,0,3,3,2],
[10,5,6,7,9,7,6,7,8,7,0,7,6],
[8,6,6,5,9,6,4,6,4,7,3,0,8],
[7,2,3,3,7,3,3,4,4,8,4,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 8, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,6,2,0,2,2,3,2,4,3,0,4],
[6,0,6,6,6,6,6,5,5,5,6,5,4],
[4,4,0,6,1,6,5,3,5,7,6,3,8],
[8,4,4,0,4,5,3,3,7,4,4,4,7],
[10,4,9,6,0,10,5,3,9,7,6,7,7],
[8,4,4,5,0,0,3,3,5,7,4,0,7],
[8,4,5,7,5,7,0,3,9,4,4,4,8],
[7,5,7,7,7,7,7,0,6,4,7,4,5],
[8,5,5,3,1,5,1,4,0,4,1,0,8],
[6,5,3,6,3,3,6,6,6,0,6,0,4],
[7,4,4,6,4,6,6,3,9,4,0,4,7],
[10,5,7,6,3,10,6,6,10,10,6,0,8],
[6,6,2,3,3,3,2,5,2,6,3,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 9, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,5,5,5,5,5,0,5,5,5,10,5],
[10,0,10,10,10,10,5,10,10,10,10,10,10],
[5,0,0,5,0,10,0,0,5,0,5,5,0],
[5,0,5,0,0,5,0,0,5,0,0,5,0],
[5,0,10,10,0,10,5,0,10,10,10,10,10],
[5,0,0,5,0,0,0,0,5,0,0,5,0],
[5,5,10,10,5,10,0,5,10,10,10,10,10],
[10,0,10,10,10,10,5,0,10,10,10,10,10],
[5,0,5,5,0,5,0,0,0,0,5,10,5],
[5,0,10,10,0,10,0,0,10,0,10,10,5],
[5,0,5,10,0,10,0,0,5,0,0,10,0],
[0,0,5,5,0,5,0,0,0,0,0,0,0],
[5,0,10,10,0,10,0,0,5,5,10,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 10, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,4,4,5,3,5,6,6,5,7,5,6],
[7,0,4,8,4,10,5,10,7,5,7,7,9],
[6,6,0,8,8,7,7,10,6,5,6,6,7],
[6,2,2,0,3,4,4,7,6,5,5,3,6],
[5,6,2,7,0,7,3,7,4,3,5,3,6],
[7,0,3,6,3,0,4,6,7,4,6,4,8],
[5,5,3,6,7,6,0,9,5,6,5,7,6],
[4,0,0,3,3,4,1,0,5,4,5,2,3],
[4,3,4,4,6,3,5,5,0,5,6,3,4],
[5,5,5,5,7,6,4,6,5,0,5,7,5],
[3,3,4,5,5,4,5,5,4,5,0,4,7],
[5,3,4,7,7,6,3,8,7,3,6,0,5],
[4,1,3,4,4,2,4,7,6,5,3,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 11, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,6,7,5,8,4,4,5,8,8,6,7],
[3,0,6,6,6,5,3,4,3,5,7,5,5],
[4,4,0,3,5,7,4,4,7,7,6,5,5],
[3,4,7,0,4,5,4,4,5,5,5,3,5],
[5,4,5,6,0,6,3,7,3,7,6,4,3],
[2,5,3,5,4,0,4,3,4,6,7,5,5],
[6,7,6,6,7,6,0,7,6,8,8,5,6],
[6,6,6,6,3,7,3,0,4,7,6,4,4],
[5,7,3,5,7,6,4,6,0,7,6,5,7],
[2,5,3,5,3,4,2,3,3,0,6,5,4],
[2,3,4,5,4,3,2,4,4,4,0,5,4],
[4,5,5,7,6,5,5,6,5,5,5,0,5],
[3,5,5,5,7,5,4,6,3,6,6,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 12, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,7,6,5,9,4,9,8,7,6,7,4],
[4,0,3,4,6,5,5,4,3,6,3,7,5],
[3,7,0,7,5,10,5,9,7,7,7,7,5],
[4,6,3,0,6,6,5,6,7,7,6,6,4],
[5,4,5,4,0,7,6,7,6,6,6,9,6],
[1,5,0,4,3,0,5,4,4,3,2,4,4],
[6,5,5,5,4,5,0,6,4,3,4,4,6],
[1,6,1,4,3,6,4,0,6,3,3,7,4],
[2,7,3,3,4,6,6,4,0,3,5,5,5],
[3,4,3,3,4,7,7,7,7,0,6,9,7],
[4,7,3,4,4,8,6,7,5,4,0,9,7],
[3,3,3,4,1,6,6,3,5,1,1,0,7],
[6,5,5,6,4,6,4,6,5,3,3,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 13, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,7,9,6,6,8,9,5,5,8,6,9],
[2,0,5,4,5,4,6,7,3,5,2,5,5],
[3,5,0,7,7,6,6,8,3,4,5,6,6],
[1,6,3,0,5,4,8,7,3,5,3,5,5],
[4,5,3,5,0,3,6,7,4,1,5,5,4],
[4,6,4,6,7,0,6,9,4,5,4,6,6],
[2,4,4,2,4,4,0,6,1,5,2,4,2],
[1,3,2,3,3,1,4,0,2,1,2,3,5],
[5,7,7,7,6,6,9,8,0,5,7,7,5],
[5,5,6,5,9,5,5,9,5,0,5,8,6],
[2,8,5,7,5,6,8,8,3,5,0,5,4],
[4,5,4,5,5,4,6,7,3,2,5,0,5],
[1,5,4,5,6,4,8,5,5,4,6,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 14, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,9,4,10,5,9,9,8,9,6,8,9],
[0,0,3,4,9,3,6,7,6,7,4,5,4],
[1,7,0,5,9,1,8,8,7,7,2,3,5],
[6,6,5,0,6,5,5,6,5,7,3,5,7],
[0,1,1,4,0,0,4,1,0,1,1,0,4],
[5,7,9,5,10,0,7,7,8,7,3,6,5],
[1,4,2,5,6,3,0,5,4,7,4,3,5],
[1,3,2,4,9,3,5,0,3,3,2,2,5],
[2,4,3,5,10,2,6,7,0,4,3,3,5],
[1,3,3,3,9,3,3,7,6,0,4,5,5],
[4,6,8,7,9,7,6,8,7,6,0,9,5],
[2,5,7,5,10,4,7,8,7,5,1,0,5],
[1,6,5,3,6,5,5,5,5,5,5,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 15, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,7,7,5,6,7,5,6,7,5,5,6],
[3,0,3,6,2,5,5,3,5,5,3,4,3],
[3,7,0,6,4,6,8,5,6,6,5,5,4],
[3,4,4,0,3,7,6,5,4,7,3,4,3],
[5,8,6,7,0,6,6,5,4,6,5,3,6],
[4,5,4,3,4,0,4,4,4,2,2,2,3],
[3,5,2,4,4,6,0,2,5,4,4,2,4],
[5,7,5,5,5,6,8,0,5,6,4,4,6],
[4,5,4,6,6,6,5,5,0,4,4,4,4],
[3,5,4,3,4,8,6,4,6,0,3,3,4],
[5,7,5,7,5,8,6,6,6,7,0,4,6],
[5,6,5,6,7,8,8,6,6,7,6,0,5],
[4,7,6,7,4,7,6,4,6,6,4,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 16, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,4,4,5,5,4,7,7,6,6,7,5],
[5,0,4,4,6,5,5,9,7,4,10,7,6],
[6,6,0,4,8,9,3,9,6,6,6,7,6],
[6,6,6,0,5,6,7,9,8,8,9,9,7],
[5,4,2,5,0,4,5,9,7,6,8,8,7],
[5,5,1,4,6,0,4,7,4,4,5,5,6],
[6,5,7,3,5,6,0,9,9,8,9,9,9],
[3,1,1,1,1,3,1,0,4,4,6,4,6],
[3,3,4,2,3,6,1,6,0,4,3,7,3],
[4,6,4,2,4,6,2,6,6,0,6,6,4],
[4,0,4,1,2,5,1,4,7,4,0,7,5],
[3,3,3,1,2,5,1,6,3,4,3,0,3],
[5,4,4,3,3,4,1,4,7,6,5,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 17, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,4,4,3,2,3,3,3,4,6,5,3],
[10,0,4,8,8,3,4,6,3,6,8,7,6],
[6,6,0,7,4,2,4,4,5,6,7,6,2],
[6,2,3,0,5,0,2,2,3,3,2,6,3],
[7,2,6,5,0,3,2,3,3,4,5,6,4],
[8,7,8,10,7,0,3,3,7,4,8,7,5],
[7,6,6,8,8,7,0,7,5,6,7,4,4],
[7,4,6,8,7,7,3,0,5,4,8,6,4],
[7,7,5,7,7,3,5,5,0,5,9,4,3],
[6,4,4,7,6,6,4,6,5,0,5,8,6],
[4,2,3,8,5,2,3,2,1,5,0,4,3],
[5,3,4,4,4,3,6,4,6,2,6,0,2],
[7,4,8,7,6,5,6,6,7,4,7,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 18, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,10,3,3,6,5,8,3,3,5,8,5],
[2,0,8,5,3,8,3,6,3,3,3,6,5],
[0,2,0,0,3,0,3,6,0,3,3,5,2],
[7,5,10,0,3,5,5,8,3,3,5,8,4],
[7,7,7,7,0,5,7,8,3,3,4,7,4],
[4,2,10,5,5,0,5,8,3,3,5,8,4],
[5,7,7,5,3,5,0,8,3,6,5,5,7],
[2,4,4,2,2,2,2,0,2,2,4,4,4],
[7,7,10,7,7,7,7,8,0,3,7,7,7],
[7,7,7,7,7,7,4,8,7,0,4,7,4],
[5,7,7,5,6,5,5,6,3,6,0,10,7],
[2,4,5,2,3,2,5,6,3,3,0,0,4],
[5,5,8,6,6,6,3,6,3,6,3,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 19, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,3,1,5,4,4,4,4,1,4,1,1],
[6,0,5,6,5,5,8,5,8,6,8,2,2],
[7,5,0,4,6,1,7,1,7,4,5,2,1],
[9,4,6,0,6,4,9,4,9,6,9,6,6],
[5,5,4,4,0,2,5,2,5,5,5,2,5],
[6,5,9,6,8,0,9,8,8,6,10,7,5],
[6,2,3,1,5,1,0,1,5,4,7,4,3],
[6,5,9,6,8,2,9,0,9,6,7,4,6],
[6,2,3,1,5,2,5,1,0,4,5,2,1],
[9,4,6,4,5,4,6,4,6,0,7,4,4],
[6,2,5,1,5,0,3,3,5,3,0,3,0],
[9,8,8,4,8,3,6,6,8,6,7,0,6],
[9,8,9,4,5,5,7,4,9,6,10,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 20, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,4,1,5,6,3,5,2,3,4,4,2],
[4,0,1,5,0,6,3,3,1,2,5,4,1],
[6,9,0,7,7,7,3,4,3,3,8,4,3],
[9,5,3,0,5,6,6,7,5,6,6,7,6],
[5,10,3,5,0,8,4,4,2,3,5,4,1],
[4,4,3,4,2,0,3,2,3,3,6,2,2],
[7,7,7,4,6,7,0,4,4,2,6,4,4],
[5,7,6,3,6,8,6,0,4,5,5,3,2],
[8,9,7,5,8,7,6,6,0,5,7,5,3],
[7,8,7,4,7,7,8,5,5,0,7,2,2],
[6,5,2,4,5,4,4,5,3,3,0,4,2],
[6,6,6,3,6,8,6,7,5,8,6,0,5],
[8,9,7,4,9,8,6,8,7,8,8,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 21, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,5,4,5,5,7,4,6,6,5,8,6],
[3,0,1,4,2,4,6,3,2,4,3,6,5],
[5,9,0,6,3,6,5,5,6,3,7,6,6],
[6,6,4,0,5,5,7,5,5,6,6,7,6],
[5,8,7,5,0,3,6,5,6,5,5,6,6],
[5,6,4,5,7,0,6,5,5,5,4,5,5],
[3,4,5,3,4,4,0,4,4,4,4,5,6],
[6,7,5,5,5,5,6,0,5,6,6,7,6],
[4,8,4,5,4,5,6,5,0,6,5,7,7],
[4,6,7,4,5,5,6,4,4,0,5,7,5],
[5,7,3,4,5,6,6,4,5,5,0,5,4],
[2,4,4,3,4,5,5,3,3,3,5,0,6],
[4,5,4,4,4,5,4,4,3,5,6,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 22, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,6,5,6,7,5,5,6,6,5,8,5],
[4,0,3,5,4,2,4,5,4,4,3,5,2],
[4,7,0,5,4,2,4,6,3,5,4,7,2],
[5,5,5,0,3,5,4,5,3,5,3,6,2],
[4,6,6,7,0,2,4,8,7,8,0,6,2],
[3,8,8,5,8,0,6,8,6,8,7,8,2],
[5,6,6,6,6,4,0,6,4,7,6,6,4],
[5,5,4,5,2,2,4,0,6,6,2,6,2],
[4,6,7,7,3,4,6,4,0,7,3,6,1],
[4,6,5,5,2,2,3,4,3,0,1,5,2],
[5,7,6,7,10,3,4,8,7,9,0,6,2],
[2,5,3,4,4,2,4,4,4,5,4,0,4],
[5,8,8,8,8,8,6,8,9,8,8,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 23, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,8,5,6,7,8,6,4,7,4,8,9],
[4,0,5,4,5,6,5,4,3,7,4,7,7],
[2,5,0,3,4,5,3,2,2,5,3,2,4],
[5,6,7,0,4,7,8,5,4,8,5,6,8],
[4,5,6,6,0,4,7,5,6,5,5,7,6],
[3,4,5,3,6,0,7,4,6,10,3,7,6],
[2,5,7,2,3,3,0,4,4,8,2,8,4],
[4,6,8,5,5,6,6,0,3,7,6,8,9],
[6,7,8,6,4,4,6,7,0,7,5,8,6],
[3,3,5,2,5,0,2,3,3,0,3,3,3],
[6,6,7,5,5,7,8,4,5,7,0,8,8],
[2,3,8,4,3,3,2,2,2,7,2,0,3],
[1,3,6,2,4,4,6,1,4,7,2,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 24, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,6,5,5,5,5,2,7,2,4,4,4],
[6,0,4,4,4,6,5,4,6,5,6,3,5],
[4,6,0,6,5,8,4,5,7,5,6,4,4],
[5,6,4,0,4,7,5,5,5,4,8,3,5],
[5,6,5,6,0,6,6,5,6,2,7,3,5],
[5,4,2,3,4,0,4,4,6,2,4,3,2],
[5,5,6,5,4,6,0,5,6,3,6,4,5],
[8,6,5,5,5,6,5,0,9,4,7,6,4],
[3,4,3,5,4,4,4,1,0,1,5,2,2],
[8,5,5,6,8,8,7,6,9,0,6,6,5],
[6,4,4,2,3,6,4,3,5,4,0,3,4],
[6,7,6,7,7,7,6,4,8,4,7,0,5],
[6,5,6,5,5,8,5,6,8,5,6,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 25, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,7,6,8,9,4,9,8,6,5,5,7],
[4,0,6,5,7,6,4,7,7,5,5,4,4],
[3,4,0,4,6,5,4,7,5,4,3,3,4],
[4,5,6,0,4,4,4,5,5,5,5,6,5],
[2,3,4,6,0,4,3,7,4,5,4,5,5],
[1,4,5,6,6,0,2,8,4,7,4,4,7],
[6,6,6,6,7,8,0,7,8,6,7,5,6],
[1,3,3,5,3,2,3,0,4,4,4,4,4],
[2,3,5,5,6,6,2,6,0,5,3,4,7],
[4,5,6,5,5,3,4,6,5,0,5,5,6],
[5,5,7,5,6,6,3,6,7,5,0,5,7],
[5,6,7,4,5,6,5,6,6,5,5,0,7],
[3,6,6,5,5,3,4,6,3,4,3,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 26, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,0,5,5,5,5,5,0,0,5,5,5],
[5,0,0,0,0,5,0,0,0,0,0,0,0],
[10,10,0,10,10,10,10,10,10,5,10,10,10],
[5,10,0,0,5,10,5,0,5,0,10,5,0],
[5,10,0,5,0,10,10,5,5,0,10,5,5],
[5,5,0,0,0,0,0,0,0,0,5,0,0],
[5,10,0,5,0,10,0,0,0,0,5,5,0],
[5,10,0,10,5,10,10,0,5,0,10,5,0],
[10,10,0,5,5,10,10,5,0,5,10,10,5],
[10,10,5,10,10,10,10,10,5,0,10,10,10],
[5,10,0,0,0,5,5,0,0,0,0,5,0],
[5,10,0,5,5,10,5,5,0,0,5,0,5],
[5,10,0,10,5,10,10,10,5,0,10,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 27, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,3,4,4,5,5,2,5,4,3,3,7],
[6,0,5,7,5,6,6,5,7,6,6,4,8],
[7,5,0,7,6,4,5,5,6,6,5,5,6],
[6,3,3,0,3,4,5,1,5,4,3,2,6],
[6,5,4,7,0,6,6,5,7,8,5,4,8],
[5,4,6,6,4,0,5,4,8,5,5,3,7],
[5,4,5,5,4,5,0,3,6,4,5,3,7],
[8,5,5,9,5,6,7,0,5,7,6,5,8],
[5,3,4,5,3,2,4,5,0,5,3,2,6],
[6,4,4,6,2,5,6,3,5,0,4,3,8],
[7,4,5,7,5,5,5,4,7,6,0,3,8],
[7,6,5,8,6,7,7,5,8,7,7,0,7],
[3,2,4,4,2,3,3,2,4,2,2,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 28, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,5,6,6,5,5,4,5,5,5,5,4],
[6,0,4,7,6,4,5,6,7,4,5,5,6],
[5,6,0,5,7,3,6,6,6,4,7,5,5],
[4,3,5,0,7,5,5,5,5,4,4,3,5],
[4,4,3,3,0,4,4,5,4,2,5,4,3],
[5,6,7,5,6,0,8,7,5,5,7,6,8],
[5,5,4,5,6,2,0,7,5,3,6,2,6],
[6,4,4,5,5,3,3,0,5,3,4,3,3],
[5,3,4,5,6,5,5,5,0,2,5,5,6],
[5,6,6,6,8,5,7,7,8,0,7,5,6],
[5,5,3,6,5,3,4,6,5,3,0,2,4],
[5,5,5,7,6,4,8,7,5,5,8,0,7],
[6,4,5,5,7,2,4,7,4,4,6,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 29, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,7,4,3,3,5,3,4,4,4,2,4],
[5,0,7,7,6,7,7,5,6,5,7,5,8],
[3,3,0,6,5,5,7,2,4,3,5,3,7],
[6,3,4,0,5,7,7,2,3,4,8,5,6],
[7,4,5,5,0,6,7,2,4,6,9,6,9],
[7,3,5,3,4,0,4,3,4,2,5,3,5],
[5,3,3,3,3,6,0,1,3,2,7,2,6],
[7,5,8,8,8,7,9,0,5,8,8,6,9],
[6,4,6,7,6,6,7,5,0,5,6,6,6],
[6,5,7,6,4,8,8,2,5,0,9,3,9],
[6,3,5,2,1,5,3,2,4,1,0,3,3],
[8,5,7,5,4,7,8,4,4,7,7,0,8],
[6,2,3,4,1,5,4,1,4,1,7,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 30, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,9,2,6,5,6,8,6,3,6,4,5],
[4,0,5,4,4,5,9,9,5,4,5,6,4],
[1,5,0,2,0,1,4,5,2,1,0,3,2],
[8,6,8,0,8,8,9,10,8,4,6,7,7],
[4,6,10,2,0,3,6,9,7,3,6,4,4],
[5,5,9,2,7,0,7,7,6,3,6,4,6],
[4,1,6,1,4,3,0,5,2,1,3,1,3],
[2,1,5,0,1,3,5,0,1,1,3,3,2],
[4,5,8,2,3,4,8,9,0,3,4,6,3],
[7,6,9,6,7,7,9,9,7,0,5,6,6],
[4,5,10,4,4,4,7,7,6,5,0,3,6],
[6,4,7,3,6,6,9,7,4,4,7,0,4],
[5,6,8,3,6,4,7,8,7,4,4,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 31, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,4,5,4,4,5,6,4,5,5,4,8],
[6,0,0,4,5,3,4,2,5,3,2,4,5],
[6,10,0,7,5,10,8,7,8,4,6,10,8],
[5,6,3,0,4,3,5,6,8,3,3,3,5],
[6,5,5,6,0,5,6,6,5,7,6,5,5],
[6,7,0,7,5,0,4,6,8,4,6,7,8],
[5,6,2,5,4,6,0,7,8,3,3,3,5],
[4,8,3,4,4,4,3,0,8,3,6,5,5],
[6,5,2,2,5,2,2,2,0,2,2,3,5],
[5,7,6,7,3,6,7,7,8,0,7,7,8],
[5,8,4,7,4,4,7,4,8,3,0,5,8],
[6,6,0,7,5,3,7,5,7,3,5,0,8],
[2,5,2,5,5,2,5,5,5,2,2,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 32, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,4,5,1,8,6,5,5,3,4,7,4],
[6,0,2,2,4,7,6,2,3,3,4,4,4],
[6,8,0,2,6,7,6,6,4,3,7,7,4],
[5,8,8,0,4,8,5,6,6,6,5,5,8],
[9,6,4,6,0,8,9,6,6,7,4,7,7],
[2,3,3,2,2,0,4,5,3,3,5,4,4],
[4,4,4,5,1,6,0,4,5,4,3,6,3],
[5,8,4,4,4,5,6,0,3,5,5,6,7],
[5,7,6,4,4,7,5,7,0,4,7,5,4],
[7,7,7,4,3,7,6,5,6,0,4,6,5],
[6,6,3,5,6,5,7,5,3,6,0,7,6],
[3,6,3,5,3,6,4,4,5,4,3,0,3],
[6,6,6,2,3,6,7,3,6,5,4,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 33, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,7,5,6,5,6,7,5,7,6,5,6],
[4,0,6,4,6,6,5,5,2,8,4,5,6],
[3,4,0,4,5,7,5,7,5,4,6,5,5],
[5,6,6,0,5,6,5,6,5,7,6,7,4],
[4,4,5,5,0,5,3,5,3,7,4,5,4],
[5,4,3,4,5,0,4,5,5,5,4,6,4],
[4,5,5,5,7,6,0,5,2,5,5,6,4],
[3,5,3,4,5,5,5,0,5,5,5,3,2],
[5,8,5,5,7,5,8,5,0,7,8,7,6],
[3,2,6,3,3,5,5,5,3,0,5,5,6],
[4,6,4,4,6,6,5,5,2,5,0,4,6],
[5,5,5,3,5,4,4,7,3,5,6,0,5],
[4,4,5,6,6,6,6,8,4,4,4,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 34, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,3,4,4,6,4,4,5,2,2,7,7],
[6,0,5,3,5,7,4,6,5,1,4,6,8],
[7,5,0,2,4,5,2,8,3,4,1,7,8],
[6,7,8,0,6,8,5,7,7,7,6,9,6],
[6,5,6,4,0,7,5,6,5,4,4,6,7],
[4,3,5,2,3,0,3,4,3,2,2,5,6],
[6,6,8,5,5,7,0,8,5,3,3,8,9],
[6,4,2,3,4,6,2,0,5,1,3,6,7],
[5,5,7,3,5,7,5,5,0,2,3,8,8],
[8,9,6,3,6,8,7,9,8,0,7,9,8],
[8,6,9,4,6,8,7,7,7,3,0,8,9],
[3,4,3,1,4,5,2,4,2,1,2,0,6],
[3,2,2,4,3,4,1,3,2,2,1,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 35, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,0,4,6,4,2,4,8,5,6,4,6],
[2,0,0,1,3,3,1,5,1,2,4,2,3],
[10,10,0,5,8,5,5,7,8,6,8,4,7],
[6,9,5,0,6,6,5,8,6,5,6,7,6],
[4,7,2,4,0,4,2,4,6,5,7,4,6],
[6,7,5,4,6,0,6,4,5,5,6,4,5],
[8,9,5,5,8,4,0,6,6,4,8,6,7],
[6,5,3,2,6,6,4,0,5,6,5,3,6],
[2,9,2,4,4,5,4,5,0,4,4,4,3],
[5,8,4,5,5,5,6,4,6,0,5,5,6],
[4,6,2,4,3,4,2,5,6,5,0,4,5],
[6,8,6,3,6,6,4,7,6,5,6,0,5],
[4,7,3,4,4,5,3,4,7,4,5,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 36, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1,3,2,4,4,4,2,4,3,1,3,4],
[9,0,7,7,6,7,5,5,6,5,5,6,7],
[7,3,0,3,4,5,4,3,5,5,5,5,5],
[8,3,7,0,7,3,4,4,6,6,3,4,4],
[6,4,6,3,0,3,3,3,5,4,4,3,4],
[6,3,5,7,7,0,4,4,4,4,4,4,7],
[6,5,6,6,7,6,0,7,6,6,5,7,6],
[8,5,7,6,7,6,3,0,5,5,4,6,7],
[6,4,5,4,5,6,4,5,0,4,4,5,5],
[7,5,5,4,6,6,4,5,6,0,5,6,6],
[9,5,5,7,6,6,5,6,6,5,0,6,6],
[7,4,5,6,7,6,3,4,5,4,4,0,7],
[6,3,5,6,6,3,4,3,5,4,4,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 37, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,5,4,5,4,6,7,7,4,4,6,5],
[4,0,5,6,8,8,8,5,4,6,7,6,4],
[5,5,0,5,7,7,8,6,8,6,8,6,5],
[6,4,5,0,8,6,5,5,5,7,6,6,4],
[5,2,3,2,0,5,5,5,3,3,4,5,2],
[6,2,3,4,5,0,5,6,3,3,5,6,3],
[4,2,2,5,5,5,0,5,3,2,5,4,3],
[3,5,4,5,5,4,5,0,5,5,5,7,6],
[3,6,2,5,7,7,7,5,0,3,6,5,3],
[6,4,4,3,7,7,8,5,7,0,7,5,2],
[6,3,2,4,6,5,5,5,4,3,0,6,3],
[4,4,4,4,5,4,6,3,5,5,4,0,5],
[5,6,5,6,8,7,7,4,7,8,7,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 38, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1,10,1,1,1,5,1,1,1,5,1,1],
[9,0,9,10,10,10,5,10,9,10,9,9,9],
[0,1,0,1,1,1,1,1,0,1,1,0,0],
[9,0,9,0,5,5,5,4,4,4,4,0,0],
[9,0,9,5,0,6,5,4,4,5,9,0,5],
[9,0,9,5,4,0,5,4,4,5,9,0,5],
[5,5,9,5,5,5,0,5,5,5,9,5,5],
[9,0,9,6,6,6,5,0,4,5,9,5,5],
[9,1,10,6,6,6,5,6,0,6,10,6,6],
[9,0,9,6,5,5,5,5,4,0,9,0,5],
[5,1,9,6,1,1,1,1,0,1,0,0,0],
[9,1,10,10,10,10,5,5,4,10,10,0,9],
[9,1,10,10,5,5,5,5,4,5,10,1,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 39, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,4,5,7,8,6,7,8,4,4,4,3],
[6,0,3,6,8,9,9,7,8,6,4,6,5],
[6,7,0,7,8,8,8,7,8,6,6,5,6],
[5,4,3,0,5,8,8,4,9,5,1,6,2],
[3,2,2,5,0,6,6,4,7,4,1,4,1],
[2,1,2,2,4,0,4,2,4,3,1,3,2],
[4,1,2,2,4,6,0,3,6,3,1,2,2],
[3,3,3,6,6,8,7,0,7,3,1,4,3],
[2,2,2,1,3,6,4,3,0,3,0,3,2],
[6,4,4,5,6,7,7,7,7,0,2,3,2],
[6,6,4,9,9,9,9,9,10,8,0,5,6],
[6,4,5,4,6,7,8,6,7,7,5,0,4],
[7,5,4,8,9,8,8,7,8,8,4,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 40, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,5,6,7,3,8,6,5,7,2,5,4],
[0,0,0,3,2,3,4,3,0,3,0,0,0],
[5,10,0,5,5,3,6,5,3,5,2,5,5],
[4,7,5,0,4,5,8,6,2,5,4,2,4],
[3,8,5,6,0,6,8,6,3,6,2,1,3],
[7,7,7,5,4,0,10,8,7,8,6,5,5],
[2,6,4,2,2,0,0,5,0,5,2,2,2],
[4,7,5,4,4,2,5,0,2,7,4,4,4],
[5,10,7,8,7,3,10,8,0,8,4,6,4],
[3,7,5,5,4,2,5,3,2,0,4,5,6],
[8,10,8,6,8,4,8,6,6,6,0,6,6],
[5,10,5,8,9,5,8,6,4,5,4,0,4],
[6,10,5,6,7,5,8,6,6,4,4,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 41, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,8,9,4,8,8,6,6,6,8,7,8],
[2,0,5,4,1,6,7,2,4,5,4,5,4],
[2,5,0,4,2,6,4,4,3,4,3,4,4],
[1,6,6,0,2,5,6,3,4,5,4,3,4],
[6,9,8,8,0,9,8,5,8,6,8,6,9],
[2,4,4,5,1,0,6,2,3,5,3,5,4],
[2,3,6,4,2,4,0,4,3,4,3,4,4],
[4,8,6,7,5,8,6,0,5,7,7,7,7],
[4,6,7,6,2,7,7,5,0,5,4,4,5],
[4,5,6,5,4,5,6,3,5,0,5,4,6],
[2,6,7,6,2,7,7,3,6,5,0,5,6],
[3,5,6,7,4,5,6,3,6,6,5,0,5],
[2,6,6,6,1,6,6,3,5,4,4,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 42, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,7,6,5,5,5,4,5,4,4,6,5],
[4,0,4,4,4,2,3,2,3,4,2,5,4],
[3,6,0,5,4,3,4,1,5,4,5,5,3],
[4,6,5,0,6,4,5,2,5,4,3,6,4],
[5,6,6,4,0,3,3,3,5,4,1,4,4],
[5,8,7,6,7,0,6,5,6,6,4,6,5],
[5,7,6,5,7,4,0,4,6,5,3,5,4],
[6,8,9,8,7,5,6,0,8,6,7,8,7],
[5,7,5,5,5,4,4,2,0,5,6,5,5],
[6,6,6,6,6,4,5,4,5,0,3,8,4],
[6,8,5,7,9,6,7,3,4,7,0,6,5],
[4,5,5,4,6,4,5,2,5,2,4,0,5],
[5,6,7,6,6,5,6,3,5,6,5,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 43, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,7,5,10,5,7,7,8,8,8,8,8],
[4,0,4,4,5,3,4,5,2,5,4,6,6],
[3,6,0,5,8,4,5,6,8,10,5,6,6],
[5,6,5,0,10,6,7,8,8,8,5,8,8],
[0,5,2,0,0,3,0,5,7,5,4,5,5],
[5,7,6,4,7,0,7,10,7,7,7,8,5],
[3,6,5,3,10,3,0,5,7,6,8,6,6],
[3,5,4,2,5,0,5,0,5,7,5,3,5],
[2,8,2,2,3,3,3,5,0,6,7,6,8],
[2,5,0,2,5,3,4,3,4,0,4,4,5],
[2,6,5,5,6,3,2,5,3,6,0,6,8],
[2,4,4,2,5,2,4,7,4,6,4,0,2],
[2,4,4,2,5,5,4,5,2,5,2,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 44, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,8,6,2,5,8,8,4,7,5,2,5],
[6,0,6,5,6,7,7,8,3,6,4,2,8],
[2,4,0,6,2,4,5,7,3,3,4,1,5],
[4,5,4,0,4,6,6,8,4,6,3,3,4],
[8,4,8,6,0,7,7,10,3,8,6,2,8],
[5,3,6,4,3,0,5,6,2,6,2,2,5],
[2,3,5,4,3,5,0,7,5,4,3,3,4],
[2,2,3,2,0,4,3,0,1,5,0,1,3],
[6,7,7,6,7,8,5,9,0,8,4,5,6],
[3,4,7,4,2,4,6,5,2,0,3,1,3],
[5,6,6,7,4,8,7,10,6,7,0,3,5],
[8,8,9,7,8,8,7,9,5,9,7,0,8],
[5,2,5,6,2,5,6,7,4,7,5,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 45, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,5,6,6,5,7,8,6,7,7,6,6],
[5,0,6,5,7,7,6,9,5,8,9,6,8],
[5,4,0,6,4,6,4,6,6,8,5,6,9],
[4,5,4,0,5,6,4,6,5,8,8,6,7],
[4,3,6,5,0,6,5,7,4,8,8,5,7],
[5,3,4,4,4,0,4,5,6,7,7,4,7],
[3,4,6,6,5,6,0,6,5,7,8,5,8],
[2,1,4,4,3,5,4,0,4,5,7,6,5],
[4,5,4,5,6,4,5,6,0,7,7,5,7],
[3,2,2,2,2,3,3,5,3,0,5,3,6],
[3,1,5,2,2,3,2,3,3,5,0,3,5],
[4,4,4,4,5,6,5,4,5,7,7,0,6],
[4,2,1,3,3,3,2,5,3,4,5,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 46, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,5,7,2,2,4,4,7,4,5,3,7],
[4,0,4,3,4,1,4,3,4,3,4,3,5],
[5,6,0,5,3,2,2,5,5,4,6,5,5],
[3,7,5,0,2,2,5,7,6,4,8,3,8],
[8,6,7,8,0,3,5,7,7,6,7,8,8],
[8,9,8,8,7,0,8,6,5,5,7,7,8],
[6,6,8,5,5,2,0,5,5,6,5,7,8],
[6,7,5,3,3,4,5,0,5,2,2,6,7],
[3,6,5,4,3,5,5,5,0,3,7,5,7],
[6,7,6,6,4,5,4,8,7,0,6,6,9],
[5,6,4,2,3,3,5,8,3,4,0,5,8],
[7,7,5,7,2,3,3,4,5,4,5,0,9],
[3,5,5,2,2,2,2,3,3,1,2,1,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 47, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,8,7,6,7,5,6,7,8,7,4,7],
[3,0,6,5,4,4,5,5,3,6,3,2,4],
[2,4,0,3,6,4,3,3,4,4,3,4,5],
[3,5,7,0,7,5,5,5,5,7,5,4,7],
[4,6,4,3,0,5,4,3,5,5,4,3,4],
[3,6,6,5,5,0,5,5,3,5,4,2,5],
[5,5,7,5,6,5,0,4,5,6,5,5,5],
[4,5,7,5,7,5,6,0,6,5,5,4,6],
[3,7,6,5,5,7,5,4,0,5,7,3,5],
[2,4,6,3,5,5,4,5,5,0,3,4,6],
[3,7,7,5,6,6,5,5,3,7,0,3,6],
[6,8,6,6,7,8,5,6,7,6,7,0,7],
[3,6,5,3,6,5,5,4,5,4,4,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 48, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,8,8,8,8,10,8,8,4,8,8,6],
[4,0,8,6,8,4,8,6,8,4,6,6,4],
[2,2,0,4,2,2,6,2,4,4,4,4,4],
[2,4,6,0,4,4,6,4,4,4,2,4,2],
[2,2,8,6,0,4,6,6,6,6,6,4,4],
[2,6,8,6,6,0,6,8,8,6,6,8,6],
[0,2,4,4,4,4,0,4,4,2,2,2,2],
[2,4,8,6,4,2,6,0,6,4,6,4,6],
[2,2,6,6,4,2,6,4,0,4,6,8,4],
[6,6,6,6,4,4,8,6,6,0,4,6,6],
[2,4,6,8,4,4,8,4,4,6,0,8,6],
[2,4,6,6,6,2,8,6,2,4,2,0,4],
[4,6,6,8,6,4,8,4,6,4,4,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 49, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,3,6,7,6,8,5,5,7,8,7,5],
[4,0,4,3,5,5,6,3,4,4,4,7,4],
[7,6,0,6,6,8,8,4,8,7,7,8,5],
[4,7,4,0,4,4,5,4,5,4,3,6,5],
[3,5,4,6,0,5,6,5,5,5,5,7,5],
[4,5,2,6,5,0,7,6,3,7,6,7,5],
[2,4,2,5,4,3,0,5,3,5,4,6,4],
[5,7,6,6,5,4,5,0,4,5,7,8,3],
[5,6,2,5,5,7,7,6,0,6,5,7,5],
[3,6,3,6,5,3,5,5,4,0,6,7,4],
[2,6,3,7,5,4,6,3,5,4,0,6,4],
[3,3,2,4,3,3,4,2,3,3,4,0,2],
[5,6,5,5,5,5,6,7,5,6,6,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 50, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,4,6,5,5,5,3,5,4,5,5,5],
[4,0,3,7,6,3,4,2,4,5,8,5,5],
[6,7,0,7,8,5,5,6,5,6,8,7,6],
[4,3,3,0,4,2,3,3,5,4,4,2,5],
[5,4,2,6,0,2,3,3,4,3,6,3,5],
[5,7,5,8,8,0,3,4,6,5,7,7,6],
[5,6,5,7,7,7,0,5,7,6,8,5,7],
[7,8,4,7,7,6,5,0,6,7,7,6,6],
[5,6,5,5,6,4,3,4,0,5,5,3,5],
[6,5,4,6,7,5,4,3,5,0,6,7,4],
[5,2,2,6,4,3,2,3,5,4,0,4,4],
[5,5,3,8,7,3,5,4,7,3,6,0,5],
[5,5,4,5,5,4,3,4,5,6,6,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 51, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,4,6,4,4,3,2,6,2,2,2,3],
[6,0,5,8,7,6,5,6,9,5,6,3,5],
[6,5,0,5,6,5,4,4,8,4,6,5,5],
[4,2,5,0,3,5,3,5,7,5,3,3,5],
[6,3,4,7,0,3,6,8,8,5,7,4,3],
[6,4,5,5,7,0,5,6,8,7,6,5,5],
[7,5,6,7,4,5,0,7,9,6,7,4,4],
[8,4,6,5,2,4,3,0,7,3,4,2,4],
[4,1,2,3,2,2,1,3,0,3,1,1,4],
[8,5,6,5,5,3,4,7,7,0,6,5,2],
[8,4,4,7,3,4,3,6,9,4,0,2,4],
[8,7,5,7,6,5,6,8,9,5,8,0,5],
[7,5,5,5,7,5,6,6,6,8,6,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 52, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,5,6,5,8,9,3,4,5,6,8,7],
[5,0,2,4,3,4,5,3,3,2,4,7,5],
[5,8,0,6,3,5,7,3,4,3,6,8,6],
[4,6,4,0,4,4,4,3,4,3,5,3,7],
[5,7,7,6,0,5,9,4,4,5,8,8,6],
[2,6,5,6,5,0,8,4,3,4,6,8,7],
[1,5,3,6,1,2,0,1,2,1,6,8,6],
[7,7,7,7,6,6,9,0,3,4,8,7,8],
[6,7,6,6,6,7,8,7,0,4,8,8,8],
[5,8,7,7,5,6,9,6,6,0,8,9,9],
[4,6,4,5,2,4,4,2,2,2,0,7,6],
[2,3,2,7,2,2,2,3,2,1,3,0,5],
[3,5,4,3,4,3,4,2,2,1,4,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 53, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,7,7,8,8,8,5,7,9,7,6,5],
[2,0,1,5,3,5,5,4,3,6,4,3,1],
[3,9,0,7,9,8,7,6,6,7,7,6,3],
[3,5,3,0,7,6,4,6,5,3,6,5,3],
[2,7,1,3,0,4,4,7,5,4,1,6,3],
[2,5,2,4,6,0,4,6,4,1,3,5,2],
[2,5,3,6,6,6,0,6,4,5,5,4,2],
[5,6,4,4,3,4,4,0,6,5,4,4,2],
[3,7,4,5,5,6,6,4,0,7,5,2,0],
[1,4,3,7,6,9,5,5,3,0,6,4,3],
[3,6,3,4,9,7,5,6,5,4,0,6,3],
[4,7,4,5,4,5,6,6,8,6,4,0,0],
[5,9,7,7,7,8,8,8,10,7,7,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 54, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,5,8,8,8,3,7,7,6,4,7,6],
[4,0,5,5,7,7,2,5,6,5,3,6,4],
[5,5,0,7,6,9,5,7,7,8,5,7,4],
[2,5,3,0,5,8,4,3,5,5,4,5,3],
[2,3,4,5,0,6,1,3,5,4,1,6,4],
[2,3,1,2,4,0,3,2,5,2,3,4,3],
[7,8,5,6,9,7,0,7,5,6,4,9,6],
[3,5,3,7,7,8,3,0,4,4,4,7,5],
[3,4,3,5,5,5,5,6,0,3,3,6,2],
[4,5,2,5,6,8,4,6,7,0,4,7,5],
[6,7,5,6,9,7,6,6,7,6,0,9,5],
[3,4,3,5,4,6,1,3,4,3,1,0,3],
[4,6,6,7,6,7,4,5,8,5,5,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 55, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,4,6,5,4,5,5,4,3,8,6,8],
[5,0,4,7,5,4,5,5,3,5,7,6,8],
[6,6,0,8,6,5,6,6,5,6,9,8,9],
[4,3,2,0,4,4,4,4,4,2,4,5,5],
[5,5,4,6,0,5,7,3,6,4,8,7,7],
[6,6,5,6,5,0,3,3,4,3,8,5,7],
[5,5,4,6,3,7,0,5,3,4,6,5,6],
[5,5,4,6,7,7,5,0,6,5,7,7,6],
[6,7,5,6,4,6,7,4,0,3,7,8,8],
[7,5,4,8,6,7,6,5,7,0,6,9,6],
[2,3,1,6,2,2,4,3,3,4,0,4,7],
[4,4,2,5,3,5,5,3,2,1,6,0,7],
[2,2,1,5,3,3,4,4,2,4,3,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 56, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,3,4,6,5,5,5,6,5,6,4,6],
[7,0,4,5,7,4,5,6,6,5,5,5,6],
[7,6,0,6,8,7,7,7,7,4,6,5,7],
[6,5,4,0,7,7,4,4,4,5,5,3,5],
[4,3,2,3,0,3,3,4,2,5,4,3,2],
[5,6,3,3,7,0,5,4,5,6,4,3,6],
[5,5,3,6,7,5,0,5,4,5,3,4,4],
[5,4,3,6,6,6,5,0,6,6,3,5,4],
[4,4,3,6,8,5,6,4,0,5,3,4,5],
[5,5,6,5,5,4,5,4,5,0,3,4,4],
[4,5,4,5,6,6,7,7,7,7,0,6,6],
[6,5,5,7,7,7,6,5,6,6,4,0,7],
[4,4,3,5,8,4,6,6,5,6,4,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 57, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,3,5,4,3,2,4,5,3,5,3,1],
[7,0,6,7,6,4,3,5,7,5,5,6,3],
[7,4,0,8,6,4,5,7,7,6,8,5,3],
[5,3,2,0,5,5,2,5,5,4,4,5,4],
[6,4,4,5,0,4,3,5,5,5,7,5,1],
[7,6,6,5,6,0,4,6,7,7,6,8,5],
[8,7,5,8,7,6,0,8,9,8,8,9,6],
[6,5,3,5,5,4,2,0,7,3,7,4,3],
[5,3,3,5,5,3,1,3,0,3,5,3,2],
[7,5,4,6,5,3,2,7,7,0,7,5,1],
[5,5,2,6,3,4,2,3,5,3,0,2,1],
[7,4,5,5,5,2,1,6,7,5,8,0,3],
[9,7,7,6,9,5,4,7,8,9,9,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 58, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,4,4,5,5,7,5,5,4,5,8,7],
[4,0,2,4,4,2,5,4,2,3,5,7,7],
[6,8,0,6,6,4,8,6,6,6,7,9,7],
[6,6,4,0,6,4,6,5,4,6,7,8,6],
[5,6,4,4,0,3,6,5,4,5,5,9,6],
[5,8,6,6,7,0,8,7,4,5,8,9,7],
[3,5,2,4,4,2,0,4,4,5,5,6,6],
[5,6,4,5,5,3,6,0,4,5,6,7,7],
[5,8,4,6,6,6,6,6,0,5,7,8,8],
[6,7,4,4,5,5,5,5,5,0,6,8,6],
[5,5,3,3,5,2,5,4,3,4,0,4,5],
[2,3,1,2,1,1,4,3,2,2,6,0,5],
[3,3,3,4,4,3,4,3,2,4,5,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 59, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,4,6,4,6,3,7,4,6,3,6,6],
[4,0,5,6,4,5,4,6,7,5,5,6,6],
[6,5,0,6,7,5,6,7,7,5,5,5,6],
[4,4,4,0,6,5,4,5,7,4,2,6,6],
[6,6,3,4,0,6,5,8,7,6,4,5,4],
[4,5,5,5,4,0,4,7,6,5,3,5,6],
[7,6,4,6,5,6,0,8,7,6,4,5,6],
[3,4,3,5,2,3,2,0,6,3,2,3,2],
[6,3,3,3,3,4,3,4,0,6,4,5,5],
[4,5,5,6,4,5,4,7,4,0,4,4,4],
[7,5,5,8,6,7,6,8,6,6,0,6,5],
[4,4,5,4,5,5,5,7,5,6,4,0,7],
[4,4,4,4,6,4,4,8,5,6,5,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 60, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,4,5,4,4,4,5,6,5,4,4,5],
[6,0,9,8,7,7,8,8,9,9,9,8,5],
[6,1,0,5,7,6,5,7,5,3,2,5,5],
[5,2,5,0,8,5,5,8,6,2,3,6,4],
[6,3,3,2,0,6,7,7,3,3,4,7,3],
[6,3,4,5,4,0,6,5,3,3,5,6,5],
[6,2,5,5,3,4,0,5,3,4,6,5,5],
[5,2,3,2,3,5,5,0,3,4,2,4,2],
[4,1,5,4,7,7,7,7,0,5,4,6,4],
[5,1,7,8,7,7,6,6,5,0,3,7,4],
[6,1,8,7,6,5,4,8,6,7,0,7,6],
[6,2,5,4,3,4,5,6,4,3,3,0,4],
[5,5,5,6,7,5,5,8,6,6,4,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 61, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,1,2,4,2,3,2,2,2,2,2,3],
[6,0,6,5,5,6,3,5,5,3,5,5,5],
[9,4,0,3,4,7,7,3,5,4,4,4,4],
[8,5,7,0,7,8,7,4,5,6,5,6,8],
[6,5,6,3,0,4,6,6,5,0,5,2,3],
[8,4,3,2,6,0,7,5,4,5,6,6,6],
[7,7,3,3,4,3,0,2,4,1,3,2,3],
[8,5,7,6,4,5,8,0,5,4,9,3,5],
[8,5,5,5,5,6,6,5,0,2,4,4,5],
[8,7,6,4,10,5,9,6,8,0,8,5,10],
[8,5,6,5,5,4,7,1,6,2,0,2,3],
[8,5,6,4,8,4,8,7,6,5,8,0,6],
[7,5,6,2,7,4,7,5,5,0,7,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 62, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1,2,1,1,0,1,5,1,4,7,0,3],
[9,0,6,6,1,7,1,5,3,6,7,0,6],
[8,4,0,3,4,6,4,4,1,4,5,3,6],
[9,4,7,0,2,7,3,6,3,7,8,2,8],
[9,9,6,8,0,9,5,9,5,10,9,5,9],
[10,3,4,3,1,0,1,7,3,6,9,0,8],
[9,9,6,7,5,9,0,8,5,8,8,3,7],
[5,5,6,4,1,3,2,0,3,9,5,0,3],
[9,7,9,7,5,7,5,7,0,8,7,5,7],
[6,4,6,3,0,4,2,1,2,0,3,0,3],
[3,3,5,2,1,1,2,5,3,7,0,1,4],
[10,10,7,8,5,10,7,10,5,10,9,0,9],
[7,4,4,2,1,2,3,7,3,7,6,1,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 63, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,5,1,1,4,5,5,2,5,2,6,4],
[4,0,5,3,3,5,8,5,5,6,3,6,6],
[5,5,0,3,4,4,5,4,5,4,4,5,3],
[9,7,7,0,6,7,7,7,6,7,5,7,7],
[9,7,6,4,0,5,8,7,2,7,6,6,5],
[6,5,6,3,5,0,5,5,7,7,3,6,5],
[5,2,5,3,2,5,0,3,3,5,3,6,6],
[5,5,6,3,3,5,7,0,3,7,1,6,7],
[8,5,5,4,8,3,7,7,0,8,5,6,6],
[5,4,6,3,3,3,5,3,2,0,2,5,6],
[8,7,6,5,4,7,7,9,5,8,0,7,7],
[4,4,5,3,4,4,4,4,4,5,3,0,4],
[6,4,7,3,5,5,4,3,4,4,3,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 64, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,8,7,5,6,6,6,8,4,5,8,6],
[3,0,5,4,4,5,4,5,4,3,5,5,5],
[2,5,0,4,4,4,5,4,4,5,4,4,3],
[3,6,6,0,3,4,6,5,5,4,5,5,4],
[5,6,6,7,0,8,6,8,8,6,5,7,7],
[4,5,6,6,2,0,4,4,6,3,4,4,5],
[4,6,5,4,4,6,0,5,7,3,4,5,5],
[4,5,6,5,2,6,5,0,6,4,5,5,6],
[2,6,6,5,2,4,3,4,0,2,3,6,4],
[6,7,5,6,4,7,7,6,8,0,5,7,8],
[5,5,6,5,5,6,6,5,7,5,0,5,6],
[2,5,6,5,3,6,5,5,4,3,5,0,6],
[4,5,7,6,3,5,5,4,6,2,4,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 65, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,8,8,8,10,6,4,2,6,8,6,6],
[2,0,4,6,6,4,8,2,2,2,6,4,2],
[2,6,0,6,6,4,6,2,0,0,6,4,4],
[2,4,4,0,8,4,6,4,2,2,4,6,6],
[2,4,4,2,0,4,4,4,4,4,4,8,4],
[0,6,6,6,6,0,6,2,2,4,6,6,4],
[4,2,4,4,6,4,0,4,4,4,2,4,2],
[6,8,8,6,6,8,6,0,2,4,6,4,4],
[8,8,10,8,6,8,6,8,0,4,6,6,6],
[4,8,10,8,6,6,6,6,6,0,8,6,6],
[2,4,4,6,6,4,8,4,4,2,0,6,4],
[4,6,6,4,2,4,6,6,4,4,4,0,4],
[4,8,6,4,6,6,8,6,4,4,6,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 66, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,4,5,3,5,4,3,3,5,5,6,4],
[5,0,2,4,2,4,4,4,3,6,3,5,2],
[6,8,0,7,6,7,6,4,4,6,3,7,5],
[5,6,3,0,3,2,6,4,3,4,4,8,7],
[7,8,4,7,0,6,7,6,3,7,4,8,7],
[5,6,3,8,4,0,7,5,2,5,3,8,5],
[6,6,4,4,3,3,0,4,3,4,4,4,4],
[7,6,6,6,4,5,6,0,2,7,7,6,5],
[7,7,6,7,7,8,7,8,0,8,5,8,5],
[5,4,4,6,3,5,6,3,2,0,4,6,4],
[5,7,7,6,6,7,6,3,5,6,0,6,5],
[4,5,3,2,2,2,6,4,2,4,4,0,5],
[6,8,5,3,3,5,6,5,5,6,5,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 67, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,6,5,4,7,5,3,4,7,3,4,5],
[7,0,7,5,4,6,5,6,6,6,3,5,7],
[4,3,0,3,3,6,2,2,4,6,2,3,5],
[5,5,7,0,6,5,6,5,5,7,5,8,8],
[6,6,7,4,0,6,6,6,6,7,3,4,6],
[3,4,4,5,4,0,4,3,4,8,5,4,5],
[5,5,8,4,4,6,0,5,6,7,3,3,6],
[7,4,8,5,4,7,5,0,5,8,5,5,7],
[6,4,6,5,4,6,4,5,0,5,2,3,6],
[3,4,4,3,3,2,3,2,5,0,3,4,4],
[7,7,8,5,7,5,7,5,8,7,0,6,8],
[6,5,7,2,6,6,7,5,7,6,4,0,8],
[5,3,5,2,4,5,4,3,4,6,2,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 68, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,4,4,3,5,6,5,5,5,7,4,3],
[4,0,2,3,3,5,4,5,5,5,8,3,3],
[6,8,0,7,6,6,6,5,7,8,8,5,7],
[6,7,3,0,4,6,5,5,7,7,8,3,5],
[7,7,4,6,0,5,7,5,7,8,6,3,6],
[5,5,4,4,5,0,5,5,5,5,7,5,4],
[4,6,4,5,3,5,0,5,5,4,6,2,5],
[5,5,5,5,5,5,5,0,5,6,8,3,4],
[5,5,3,3,3,5,5,5,0,5,5,1,5],
[5,5,2,3,2,5,6,4,5,0,6,1,4],
[3,2,2,2,4,3,4,2,5,4,0,2,3],
[6,7,5,7,7,5,8,7,9,9,8,0,6],
[7,7,3,5,4,6,5,6,5,6,7,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 69, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,7,6,4,3,2,4,6,5,7,3,4],
[7,0,6,8,5,3,4,3,8,6,7,5,6],
[3,4,0,5,4,3,2,1,7,3,5,2,4],
[4,2,5,0,3,0,2,1,5,3,5,1,4],
[6,5,6,7,0,5,5,4,7,8,7,5,5],
[7,7,7,10,5,0,5,5,9,4,8,6,8],
[8,6,8,8,5,5,0,4,9,6,8,6,5],
[6,7,9,9,6,5,6,0,8,5,8,5,7],
[4,2,3,5,3,1,1,2,0,4,5,2,5],
[5,4,7,7,2,6,4,5,6,0,7,6,5],
[3,3,5,5,3,2,2,2,5,3,0,2,4],
[7,5,8,9,5,4,4,5,8,4,8,0,6],
[6,4,6,6,5,2,5,3,5,5,6,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 70, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,7,3,3,7,9,10,10,4,9,8,9],
[8,0,8,10,5,9,10,8,10,7,7,10,9],
[3,2,0,5,5,4,4,10,5,4,4,5,4],
[7,0,5,0,5,7,9,8,10,7,7,8,9],
[7,5,5,5,0,5,7,8,8,7,7,5,7],
[3,1,6,3,5,0,5,8,5,3,2,5,4],
[1,0,6,1,3,5,0,8,8,2,7,8,7],
[0,2,0,2,2,2,2,0,3,2,2,2,2],
[0,0,5,0,2,5,2,7,0,2,7,7,7],
[6,3,6,3,3,7,8,8,8,0,5,8,7],
[1,3,6,3,3,8,3,8,3,5,0,3,2],
[2,0,5,2,5,5,2,8,3,2,7,0,7],
[1,1,6,1,3,6,3,8,3,3,8,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 71, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,3,4,3,4,2,4,4,4,5,2,5],
[4,0,2,4,3,4,2,3,2,3,4,2,2],
[7,8,0,8,7,7,6,8,6,7,6,4,6],
[6,6,2,0,2,5,5,5,4,4,5,4,5],
[7,7,3,8,0,6,3,4,5,6,6,4,7],
[6,6,3,5,4,0,2,4,4,4,3,1,5],
[8,8,4,5,7,8,0,4,5,7,8,6,8],
[6,7,2,5,6,6,6,0,4,7,8,5,6],
[6,8,4,6,5,6,5,6,0,5,6,6,6],
[6,7,3,6,4,6,3,3,5,0,7,4,5],
[5,6,4,5,4,7,2,2,4,3,0,2,4],
[8,8,6,6,6,9,4,5,4,6,8,0,5],
[5,8,4,5,3,5,2,4,4,5,6,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 72, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,4,4,7,3,7,6,5,4,8,5,6],
[3,0,2,4,6,4,7,5,6,4,8,4,5],
[6,8,0,6,6,3,7,9,7,7,9,5,5],
[6,6,4,0,6,5,6,6,5,6,7,6,4],
[3,4,4,4,0,3,4,4,2,5,8,5,3],
[7,6,7,5,7,0,6,7,5,9,8,6,4],
[3,3,3,4,6,4,0,2,5,4,6,4,2],
[4,5,1,4,6,3,8,0,6,5,8,5,4],
[5,4,3,5,8,5,5,4,0,4,7,5,2],
[6,6,3,4,5,1,6,5,6,0,8,4,3],
[2,2,1,3,2,2,4,2,3,2,0,1,2],
[5,6,5,4,5,4,6,5,5,6,9,0,5],
[4,5,5,6,7,6,8,6,8,7,8,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 73, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1,2,3,2,2,3,2,4,1,2,3,2],
[9,0,5,6,5,4,6,7,9,6,7,6,9],
[8,5,0,7,4,4,5,5,6,6,6,4,5],
[7,4,3,0,4,2,2,4,5,5,5,5,5],
[8,5,6,6,0,6,6,5,9,8,9,7,8],
[8,6,6,8,4,0,6,5,9,6,9,6,9],
[7,4,5,8,4,4,0,4,7,3,4,8,4],
[8,3,5,6,5,5,6,0,6,6,6,6,6],
[6,1,4,5,1,1,3,4,0,3,1,3,2],
[9,4,4,5,2,4,7,4,7,0,4,8,4],
[8,3,4,5,1,1,6,4,9,6,0,6,7],
[7,4,6,5,3,4,2,4,7,2,4,0,4],
[8,1,5,5,2,1,6,4,8,6,3,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 74, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,5,10,5,5,5,5,5,5,5,5,5],
[5,0,10,10,7,5,5,7,7,10,10,2,2],
[5,0,0,5,7,3,2,0,7,5,7,2,2],
[0,0,5,0,5,0,0,5,5,5,5,0,0],
[5,3,3,5,0,3,5,0,2,8,5,2,5],
[5,5,7,10,7,0,7,5,7,5,7,2,7],
[5,5,8,10,5,3,0,5,5,5,5,0,0],
[5,3,10,5,10,5,5,0,7,10,10,5,5],
[5,3,3,5,8,3,5,3,0,8,8,3,3],
[5,0,5,5,2,5,5,0,2,0,2,2,2],
[5,0,3,5,5,3,5,0,2,8,0,2,2],
[5,8,8,10,8,8,10,5,7,8,8,0,8],
[5,8,8,10,5,3,10,5,7,8,8,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 75, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,5,5,5,3,3,9,7,3,7,4,9],
[6,0,7,8,8,6,5,9,7,5,7,6,6],
[5,3,0,5,6,5,6,8,6,7,8,5,6],
[5,2,5,0,3,5,3,7,7,4,7,5,7],
[5,2,4,7,0,5,5,7,5,4,7,5,8],
[7,4,5,5,5,0,5,7,7,7,7,7,7],
[7,5,4,7,5,5,0,9,7,5,7,5,7],
[1,1,2,3,3,3,1,0,6,3,8,1,3],
[3,3,4,3,5,3,3,4,0,5,3,5,3],
[7,5,3,6,6,3,5,7,5,0,7,5,8],
[3,3,2,3,3,3,3,2,7,3,0,3,3],
[6,4,5,5,5,3,5,9,5,5,7,0,7],
[1,4,4,3,2,3,3,7,7,2,7,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 76, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,4,5,5,5,9,8,1,1,5,5,5],
[1,0,0,1,2,0,9,4,1,1,4,0,6],
[6,10,0,2,6,2,10,9,6,6,10,6,10],
[5,9,8,0,9,0,9,8,5,5,9,4,9],
[5,8,4,1,0,0,8,8,1,4,4,4,9],
[5,10,8,10,10,0,9,9,5,5,9,5,10],
[1,1,0,1,2,1,0,1,2,2,1,1,6],
[2,6,1,2,2,1,9,0,1,1,1,1,6],
[9,9,4,5,9,5,8,9,0,8,9,9,9],
[9,9,4,5,6,5,8,9,2,0,5,9,5],
[5,6,0,1,6,1,9,9,1,5,0,5,10],
[5,10,4,6,6,5,9,9,1,1,5,0,6],
[5,4,0,1,1,0,4,4,1,5,0,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 77, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,4,5,2,0,6,3,4,5,5,7,3],
[7,0,7,8,5,6,10,8,8,10,7,8,5],
[6,3,0,6,2,5,7,6,6,7,4,8,3],
[5,2,4,0,3,3,4,4,4,4,5,6,4],
[8,5,8,7,0,7,9,8,8,7,7,9,4],
[10,4,5,7,3,0,6,6,6,5,6,9,6],
[4,0,3,6,1,4,0,5,6,4,4,7,2],
[7,2,4,6,2,4,5,0,6,7,4,8,3],
[6,2,4,6,2,4,4,4,0,2,2,5,2],
[5,0,3,6,3,5,6,3,8,0,3,8,2],
[5,3,6,5,3,4,6,6,8,7,0,9,1],
[3,2,2,4,1,1,3,2,5,2,1,0,0],
[7,5,7,6,6,4,8,7,8,8,9,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 78, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,3,4,5,2,5,3,3,6,5,5,1],
[6,0,7,6,6,3,8,6,6,10,10,8,5],
[7,3,0,2,4,4,3,4,0,5,3,4,1],
[6,4,8,0,4,4,7,5,4,7,7,7,7],
[5,4,6,6,0,3,5,4,4,6,7,4,5],
[8,7,6,6,7,0,7,5,5,10,8,8,5],
[5,2,7,3,5,3,0,2,2,6,5,5,2],
[7,4,6,5,6,5,8,0,5,8,7,7,5],
[7,4,10,6,6,5,8,5,0,9,8,7,4],
[4,0,5,3,4,0,4,2,1,0,4,7,1],
[5,0,7,3,3,2,5,3,2,6,0,5,4],
[5,2,6,3,6,2,5,3,3,3,5,0,1],
[9,5,9,3,5,5,8,5,6,9,6,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 79, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,7,5,8,8,10,8,7,5,7,8,5],
[1,0,1,3,6,3,3,4,1,1,1,2,1],
[3,9,0,3,7,6,7,4,6,0,4,4,3],
[5,7,7,0,6,6,6,6,6,5,6,4,5],
[2,4,3,4,0,5,5,1,5,3,2,4,3],
[2,7,4,4,5,0,5,6,2,2,2,3,5],
[0,7,3,4,5,5,0,6,5,2,2,2,5],
[2,6,6,4,9,4,4,0,4,4,6,5,5],
[3,9,4,4,5,8,5,6,0,2,4,4,5],
[5,9,10,5,7,8,8,6,8,0,9,4,7],
[3,9,6,4,8,8,8,4,6,1,0,4,3],
[2,8,6,6,6,7,8,5,6,6,6,0,7],
[5,9,7,5,7,5,5,5,5,3,7,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 80, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,10,5,5,3,3,7,8,2,2,8,2],
[2,0,5,5,2,5,5,5,7,2,2,8,2],
[0,5,0,0,0,3,3,5,5,0,0,6,0],
[5,5,10,0,7,3,8,7,7,5,5,8,4],
[5,8,10,3,0,3,6,5,5,5,5,8,4],
[7,5,7,7,7,0,7,10,7,4,7,10,7],
[7,5,7,2,4,3,0,7,7,5,4,8,4],
[3,5,5,3,5,0,3,0,5,0,3,6,5],
[2,3,5,3,5,3,3,5,0,2,2,8,2],
[8,8,10,5,5,6,5,10,8,0,5,8,5],
[8,8,10,5,5,3,6,7,8,5,0,8,2],
[2,2,4,2,2,0,2,4,2,2,2,0,2],
[8,8,10,6,6,3,6,5,8,5,8,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 81, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,4,6,5,5,6,6,9,5,5,5,9],
[5,0,5,10,10,9,10,5,10,6,9,5,10],
[6,5,0,6,6,5,6,6,6,6,5,5,5],
[4,0,4,0,5,4,0,1,4,0,0,0,4],
[5,0,4,5,0,4,1,5,5,1,0,4,4],
[5,1,5,6,6,0,6,1,10,6,5,1,5],
[4,0,4,10,9,4,0,5,9,5,5,4,4],
[4,5,4,9,5,9,5,0,9,5,5,9,9],
[1,0,4,6,5,0,1,1,0,0,0,0,4],
[5,4,4,10,9,4,5,5,10,0,4,4,4],
[5,1,5,10,10,5,5,5,10,6,0,5,5],
[5,5,5,10,6,9,6,1,10,6,5,0,10],
[1,0,5,6,6,5,6,1,6,6,5,0,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 82, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,8,7,5,3,8,4,7,10,7,4,7],
[6,0,7,5,2,3,5,2,4,7,4,3,3],
[2,3,0,1,1,0,1,2,3,3,1,2,3],
[3,5,9,0,4,4,6,3,6,6,8,6,6],
[5,8,9,6,0,6,9,7,9,7,8,8,8],
[7,7,10,6,4,0,7,5,8,7,6,6,8],
[2,5,9,4,1,3,0,2,6,6,6,5,6],
[6,8,8,7,3,5,8,0,9,8,8,7,7],
[3,6,7,4,1,2,4,1,0,7,7,3,2],
[0,3,7,4,3,3,4,2,3,0,6,3,4],
[3,6,9,2,2,4,4,2,3,4,0,5,4],
[6,7,8,4,2,4,5,3,7,7,5,0,3],
[3,7,7,4,2,2,4,3,8,6,6,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 83, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,4,4,3,2,5,3,3,1,3,3,3],
[7,0,8,7,7,6,7,7,6,3,4,7,4],
[6,2,0,2,3,3,5,5,3,1,3,2,2],
[6,3,8,0,3,5,7,4,4,2,4,5,3],
[7,3,7,7,0,4,6,7,4,1,2,6,3],
[8,4,7,5,6,0,6,5,4,2,5,5,4],
[5,3,5,3,4,4,0,3,4,2,4,3,3],
[7,3,5,6,3,5,7,0,4,2,4,7,3],
[7,4,7,6,6,6,6,6,0,4,3,5,4],
[9,7,9,8,9,8,8,8,6,0,6,7,5],
[7,6,7,6,8,5,6,6,7,4,0,6,3],
[7,3,8,5,4,5,7,3,5,3,4,0,3],
[7,6,8,7,7,6,7,7,6,5,7,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 84, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,3,4,5,3,5,5,5,6,4,5,4],
[7,0,8,5,5,7,4,6,4,6,4,4,4],
[7,2,0,4,4,6,5,5,4,6,4,3,5],
[6,5,6,0,5,8,8,7,5,6,4,5,7],
[5,5,6,5,0,5,5,5,7,7,5,5,6],
[7,3,4,2,5,0,4,4,4,6,4,4,5],
[5,6,5,2,5,6,0,4,6,5,3,4,4],
[5,4,5,3,5,6,6,0,4,5,4,5,5],
[5,6,6,5,3,6,4,6,0,7,6,6,6],
[4,4,4,4,3,4,5,5,3,0,5,5,4],
[6,6,6,6,5,6,7,6,4,5,0,6,6],
[5,6,7,5,5,6,6,5,4,5,4,0,5],
[6,6,5,3,4,5,6,5,4,6,4,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 85, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,0,6,3,7,4,6,2,5,4,4,1],
[3,0,0,1,1,1,1,1,2,3,4,4,1],
[10,10,0,6,7,7,6,9,8,7,5,6,6],
[4,9,4,0,4,9,4,4,4,7,8,8,1],
[7,9,3,6,0,6,7,9,4,7,8,7,0],
[3,9,3,1,4,0,3,4,4,7,7,7,1],
[6,9,4,6,3,7,0,10,4,4,7,4,1],
[4,9,1,6,1,6,0,0,4,4,4,4,1],
[8,8,2,6,6,6,6,6,0,5,4,6,3],
[5,7,3,3,3,3,6,6,5,0,7,9,1],
[6,6,5,2,2,3,3,6,6,3,0,6,2],
[6,6,4,2,3,3,6,6,4,1,4,0,0],
[9,9,4,9,10,9,9,9,7,9,8,10,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 86, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,3,6,7,6,6,5,5,2,5,3,2],
[6,0,3,3,4,3,4,3,5,3,3,3,6],
[7,7,0,3,6,4,5,7,6,4,5,3,7],
[4,7,7,0,7,5,5,7,6,4,2,5,5],
[3,6,4,3,0,2,7,3,5,2,4,1,4],
[4,7,6,5,8,0,8,9,7,3,5,3,5],
[4,6,5,5,3,2,0,6,5,4,1,2,4],
[5,7,3,3,7,1,4,0,6,2,4,3,4],
[5,5,4,4,5,3,5,4,0,2,4,4,4],
[8,7,6,6,8,7,6,8,8,0,7,4,9],
[5,7,5,8,6,5,9,6,6,3,0,6,5],
[7,7,7,5,9,7,8,7,6,6,4,0,6],
[8,4,3,5,6,5,6,6,6,1,5,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 87, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,9,9,5,9,4,9,9,9,9,4,5],
[5,0,4,9,0,9,4,9,9,9,9,4,5],
[1,6,0,9,0,9,1,9,9,5,9,1,1],
[1,1,1,0,1,1,1,4,5,6,5,1,1],
[5,10,10,9,0,10,5,9,10,10,10,5,5],
[1,1,1,9,0,0,1,4,9,5,4,1,1],
[6,6,9,9,5,9,0,9,9,9,9,10,10],
[1,1,1,6,1,6,1,0,6,6,6,1,1],
[1,1,1,5,0,1,1,4,0,5,1,1,1],
[1,1,5,4,0,5,1,4,5,0,5,1,1],
[1,1,1,5,0,6,1,4,9,5,0,1,1],
[6,6,9,9,5,9,0,9,9,9,9,0,10],
[5,5,9,9,5,9,0,9,9,9,9,0,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 88, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,5,6,10,5,9,8,8,6,8,3,6],
[1,0,1,3,7,3,6,5,8,7,8,3,5],
[5,9,0,8,9,5,8,9,8,6,7,3,7],
[4,7,2,0,6,2,5,7,9,7,8,2,6],
[0,3,1,4,0,1,6,5,4,5,6,1,4],
[5,7,5,8,9,0,7,6,8,6,7,3,6],
[1,4,2,5,4,3,0,6,5,7,5,1,4],
[2,5,1,3,5,4,4,0,6,5,8,0,5],
[2,2,2,1,6,2,5,4,0,2,4,1,3],
[4,3,4,3,5,4,3,5,8,0,7,4,5],
[2,2,3,2,4,3,5,2,6,3,0,1,2],
[7,7,7,8,9,7,9,10,9,6,9,0,5],
[4,5,3,4,6,4,6,5,7,5,8,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 89, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,3,4,7,2,4,5,7,7,4,7,1],
[3,0,2,3,5,1,2,7,6,7,5,4,1],
[7,8,0,6,6,4,6,6,8,5,4,5,5],
[6,7,4,0,9,7,7,7,8,9,6,9,5],
[3,5,4,1,0,3,2,2,8,7,4,4,1],
[8,9,6,3,7,0,3,6,8,6,5,9,3],
[6,8,4,3,8,7,0,8,8,9,6,9,2],
[5,3,4,3,8,4,2,0,8,8,5,6,2],
[3,4,2,2,2,2,2,2,0,5,3,2,1],
[3,3,5,1,3,4,1,2,5,0,3,4,2],
[6,5,6,4,6,5,4,5,7,7,0,6,5],
[3,6,5,1,6,1,1,4,8,6,4,0,2],
[9,9,5,5,9,7,8,8,9,8,5,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 90, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,5,5,0,10,5,10,5,10,5,10,5],
[0,0,5,5,0,5,5,5,5,5,5,5,5],
[5,5,0,0,0,5,10,10,5,5,10,10,10],
[5,5,10,0,5,5,10,10,5,5,10,10,10],
[10,10,10,5,0,10,10,10,10,10,10,10,10],
[0,5,5,5,0,0,5,10,0,0,5,10,5],
[5,5,0,0,0,5,0,5,0,5,0,5,5],
[0,5,0,0,0,0,5,0,0,0,5,5,5],
[5,5,5,5,0,10,10,10,0,5,5,10,5],
[0,5,5,5,0,10,5,10,5,0,5,10,5],
[5,5,0,0,0,5,10,5,5,5,0,5,10],
[0,5,0,0,0,0,5,5,0,0,5,0,5],
[5,5,0,0,0,5,5,5,5,5,0,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 91, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,4,8,4,6,6,6,4,5,5,6,5],
[5,0,7,9,7,4,7,7,2,3,3,7,4],
[6,3,0,8,3,3,8,8,2,4,3,8,3],
[2,1,2,0,1,2,2,4,1,1,2,2,3],
[6,3,7,9,0,4,7,9,3,5,2,7,4],
[4,6,7,8,6,0,7,7,4,3,7,7,7],
[4,3,2,8,3,3,0,9,4,3,3,7,5],
[4,3,2,6,1,3,1,0,1,1,1,1,2],
[6,8,8,9,7,6,6,9,0,6,3,6,8],
[5,7,6,9,5,7,7,9,4,0,5,5,5],
[5,7,7,8,8,3,7,9,7,5,0,8,9],
[4,3,2,8,3,3,3,9,4,5,2,0,3],
[5,6,7,7,6,3,5,8,2,5,1,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 92, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,8,5,2,5,5,2,4,2,3,8,6],
[3,0,6,3,3,3,7,3,3,0,6,6,3],
[2,4,0,2,2,1,2,2,1,1,5,5,6],
[5,7,8,0,5,4,8,5,4,4,8,8,4],
[8,7,8,5,0,5,6,6,6,5,5,8,6],
[5,7,9,6,5,0,5,5,4,6,4,9,7],
[5,3,8,2,4,5,0,5,6,2,6,8,5],
[8,7,8,5,4,5,5,0,4,2,3,8,5],
[6,7,9,6,4,6,4,6,0,6,4,9,6],
[8,10,9,6,5,4,8,8,4,0,8,9,6],
[7,4,5,2,5,6,4,7,6,2,0,5,3],
[2,4,5,2,2,1,2,2,1,1,5,0,2],
[4,7,4,6,4,3,5,5,4,4,7,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 93, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,8,5,5,9,6,8,9,6,6,6,8],
[4,0,3,7,3,9,5,3,8,4,8,4,7],
[2,7,0,6,2,7,3,6,6,3,7,2,6],
[5,3,4,0,4,10,5,4,10,6,2,6,9],
[5,7,8,6,0,10,7,9,9,7,7,6,9],
[1,1,3,0,0,0,2,3,5,1,1,1,7],
[4,5,7,5,3,8,0,3,8,4,6,1,8],
[2,7,4,6,1,7,7,0,6,7,6,6,6],
[1,2,4,0,1,5,2,4,0,1,1,1,8],
[4,6,7,4,3,9,6,3,9,0,6,1,7],
[4,2,3,8,3,9,4,4,9,4,0,5,7],
[4,6,8,4,4,9,9,4,9,9,5,0,8],
[2,3,4,1,1,3,2,4,2,3,3,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 94, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,6,6,4,4,5,7,8,7,4,9,4],
[5,0,4,5,5,4,5,5,6,8,5,5,5],
[4,6,0,5,5,3,6,5,5,5,4,5,5],
[4,5,5,0,5,5,6,7,6,6,5,6,5],
[6,5,5,5,0,5,5,7,9,6,6,9,4],
[6,6,7,5,5,0,7,9,8,7,9,7,7],
[5,5,4,4,5,3,0,6,5,5,5,5,4],
[3,5,5,3,3,1,4,0,4,4,3,4,4],
[2,4,5,4,1,2,5,6,0,5,2,5,2],
[3,2,5,4,4,3,5,6,5,0,5,6,3],
[6,5,6,5,4,1,5,7,8,5,0,6,5],
[1,5,5,4,1,3,5,6,5,4,4,0,2],
[6,5,5,5,6,3,6,6,8,7,5,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 95, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,5,9,10,5,5,9,5,5,9,10,10],
[0,0,5,5,5,5,5,9,5,5,4,6,10],
[5,5,0,5,5,5,5,5,5,1,5,5,5],
[1,5,5,0,5,0,1,5,1,0,5,1,10],
[0,5,5,5,0,5,5,9,5,5,9,6,9],
[5,5,5,10,5,0,5,5,5,6,5,5,10],
[5,5,5,9,5,5,0,10,10,5,5,10,10],
[1,1,5,5,1,5,0,0,6,5,1,6,6],
[5,5,5,9,5,5,0,4,0,5,5,5,10],
[5,5,9,10,5,4,5,5,5,0,5,5,10],
[1,6,5,5,1,5,5,9,5,5,0,6,6],
[0,4,5,9,4,5,0,4,5,5,4,0,9],
[0,0,5,0,1,0,0,4,0,0,4,1,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 96, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,4,8,3,5,6,6,7,6,6,6,9],
[7,0,7,6,4,6,9,10,10,9,7,4,10],
[6,3,0,5,2,5,9,7,6,6,6,3,9],
[2,4,5,0,1,3,7,8,8,6,6,6,8],
[7,6,8,9,0,5,7,7,7,6,6,6,9],
[5,4,5,7,5,0,8,5,5,4,3,5,10],
[4,1,1,3,3,2,0,4,6,0,0,1,3],
[4,0,3,2,3,5,6,0,4,3,3,0,7],
[3,0,4,2,3,5,4,6,0,3,3,0,7],
[4,1,4,4,4,6,10,7,7,0,3,5,10],
[4,3,4,4,4,7,10,7,7,7,0,5,10],
[4,6,7,4,4,5,9,10,10,5,5,0,7],
[1,0,1,2,1,0,7,3,3,0,0,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 97, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,6,6,5,6,7,5,6,6,6,4,6],
[5,0,5,4,7,3,8,4,4,8,6,6,6],
[4,5,0,6,5,6,7,4,4,7,5,5,5],
[4,6,4,0,6,5,7,5,5,6,4,5,5],
[5,3,5,4,0,5,6,6,3,5,5,4,4],
[4,7,4,5,5,0,8,4,4,7,6,7,5],
[3,2,3,3,4,2,0,3,3,7,2,4,3],
[5,6,6,5,4,6,7,0,4,6,6,5,5],
[4,6,6,5,7,6,7,6,0,8,5,5,6],
[4,2,3,4,5,3,3,4,2,0,2,4,4],
[4,4,5,6,5,4,8,4,5,8,0,5,6],
[6,4,5,5,6,3,6,5,5,6,5,0,7],
[4,4,5,5,6,5,7,5,4,6,4,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 98, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,5,5,7,4,5,6,5,5,4,6,5],
[6,0,7,7,8,5,6,7,6,8,6,7,5],
[5,3,0,4,6,4,5,5,4,4,4,5,3],
[5,3,6,0,6,4,5,3,3,3,3,4,3],
[3,2,4,4,0,4,4,5,4,3,6,6,3],
[6,5,6,6,6,0,5,7,7,6,4,6,4],
[5,4,5,5,6,5,0,5,4,3,4,6,4],
[4,3,5,7,5,3,5,0,5,6,4,5,6],
[5,4,6,7,6,3,6,5,0,6,6,6,4],
[5,2,6,7,7,4,7,4,4,0,6,6,5],
[6,4,6,7,4,6,6,6,4,4,0,6,2],
[4,3,5,6,4,4,4,5,4,4,4,0,3],
[5,5,7,7,7,6,6,4,6,5,8,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 99, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,3,7,6,7,6,7,8,10,6,4,6],
[7,0,3,8,9,7,6,8,10,9,8,7,6],
[7,7,0,5,7,9,6,5,8,7,8,7,7],
[3,2,5,0,6,4,4,3,3,8,4,3,3],
[4,1,3,4,0,2,2,1,3,6,3,3,1],
[3,3,1,6,8,0,1,6,8,8,7,3,6],
[4,4,4,6,8,9,0,8,8,8,8,5,7],
[3,2,5,7,9,4,2,0,8,9,3,3,2],
[2,0,2,7,7,2,2,2,0,9,4,3,1],
[0,1,3,2,4,2,2,1,1,0,1,4,1],
[4,2,2,6,7,3,2,7,6,9,0,3,3],
[6,3,3,7,7,7,5,7,7,6,7,0,6],
[4,4,3,7,9,4,3,8,9,9,7,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 100, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,5,8,7,5,8,5,7,9,4,8,7],
[3,0,3,7,5,4,7,4,6,6,4,8,6],
[5,7,0,7,7,7,6,5,4,8,5,6,6],
[2,3,3,0,6,5,4,4,2,5,3,4,3],
[3,5,3,4,0,6,6,6,4,4,5,5,6],
[5,6,3,5,4,0,7,4,6,4,4,6,5],
[2,3,4,6,4,3,0,4,2,4,2,4,3],
[5,6,5,6,4,6,6,0,4,5,5,5,3],
[3,4,6,8,6,4,8,6,0,6,4,5,3],
[1,4,2,5,6,6,6,5,4,0,2,5,5],
[6,6,5,7,5,6,8,5,6,8,0,7,5],
[2,2,4,6,5,4,6,5,5,5,3,0,6],
[3,4,4,7,4,5,7,7,7,5,5,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 101, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,5,6,4,4,4,6,4,4,4,5,5],
[4,0,2,5,4,3,5,8,3,5,6,6,5],
[5,8,0,5,6,5,5,8,4,5,7,6,5],
[4,5,5,0,5,4,5,9,4,6,7,6,6],
[6,6,4,5,0,5,5,6,1,5,5,5,4],
[6,7,5,6,5,0,6,6,3,5,5,6,6],
[6,5,5,5,5,4,0,8,4,6,7,6,5],
[4,2,2,1,4,4,2,0,4,3,4,4,3],
[6,7,6,6,9,7,6,6,0,4,6,8,7],
[6,5,5,4,5,5,4,7,6,0,6,7,5],
[6,4,3,3,5,5,3,6,4,4,0,4,4],
[5,4,4,4,5,4,4,6,2,3,6,0,4],
[5,5,5,4,6,4,5,7,3,5,6,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 102, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,1,2,4,3,7,4,4,6,4,3,4],
[7,0,5,6,5,5,6,6,4,8,6,6,5],
[9,5,0,6,7,6,7,4,5,7,7,4,5],
[8,4,4,0,7,6,8,4,4,8,6,6,6],
[6,5,3,3,0,5,8,6,4,8,7,5,4],
[7,5,4,4,5,0,8,5,4,5,6,6,5],
[3,4,3,2,2,2,0,3,1,5,4,2,2],
[6,4,6,6,4,5,7,0,3,5,7,7,4],
[6,6,5,6,6,6,9,7,0,7,7,6,6],
[4,2,3,2,2,5,5,5,3,0,5,3,2],
[6,4,3,4,3,4,6,3,3,5,0,5,3],
[7,4,6,4,5,4,8,3,4,7,5,0,4],
[6,5,5,4,6,5,8,6,4,8,7,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 103, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,4,6,4,6,3,7,6,7,7,6,4],
[3,0,4,3,3,3,2,6,4,6,5,5,3],
[6,6,0,9,6,3,5,7,9,4,5,6,6],
[4,7,1,0,5,1,3,6,5,4,5,7,5],
[6,7,4,5,0,3,3,7,5,4,5,6,2],
[4,7,7,9,7,0,6,7,9,5,5,6,6],
[7,8,5,7,7,4,0,7,8,8,8,7,7],
[3,4,3,4,3,3,3,0,4,2,5,1,1],
[4,6,1,5,5,1,2,6,0,4,5,6,4],
[3,4,6,6,6,5,2,8,6,0,7,5,6],
[3,5,5,5,5,5,2,5,5,3,0,5,5],
[4,5,4,3,4,4,3,9,4,5,5,0,2],
[6,7,4,5,8,4,3,9,6,4,5,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 104, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,2,6,0,4,6,5,5,1,4,1,2],
[8,0,2,5,4,5,5,5,7,3,7,2,3],
[8,8,0,9,4,7,8,9,7,4,9,7,7],
[4,5,1,0,3,2,2,4,6,2,7,3,3],
[10,6,6,7,0,7,7,8,7,5,8,5,5],
[6,5,3,8,3,0,5,3,6,2,8,3,3],
[4,5,2,8,3,5,0,5,7,4,6,2,3],
[5,5,1,6,2,7,5,0,6,4,8,2,2],
[5,3,3,4,3,4,3,4,0,4,6,4,3],
[9,7,6,8,5,8,6,6,6,0,7,6,6],
[6,3,1,3,2,2,4,2,4,3,0,3,3],
[9,8,3,7,5,7,8,8,6,4,7,0,7],
[8,7,3,7,5,7,7,8,7,4,7,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 105, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,8,5,9,8,8,9,7,7,9,6,8],
[5,0,9,6,7,10,8,10,10,7,7,8,10],
[2,1,0,1,2,2,2,2,3,2,5,4,4],
[5,4,9,0,8,9,8,9,6,7,10,6,7],
[1,3,8,2,0,5,6,5,5,6,9,4,6],
[2,0,8,1,5,0,3,8,5,5,7,4,5],
[2,2,8,2,4,7,0,7,4,5,7,5,5],
[1,0,8,1,5,2,3,0,4,5,7,3,4],
[3,0,7,4,5,5,6,6,0,5,7,6,6],
[3,3,8,3,4,5,5,5,5,0,8,5,6],
[1,3,5,0,1,3,3,3,3,2,0,1,4],
[4,2,6,4,6,6,5,7,4,5,9,0,5],
[2,0,6,3,4,5,5,6,4,4,6,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 106, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,6,3,10,6,6,3,6,6,6,6],
[0,0,3,0,3,7,3,3,3,3,0,0,3],
[0,7,0,0,0,4,3,0,0,0,3,0,0],
[4,10,10,0,7,10,7,10,7,10,10,10,7],
[7,7,10,3,0,10,10,3,10,3,7,7,7],
[0,3,6,0,0,0,3,3,0,3,3,0,0],
[4,7,7,3,0,7,0,3,0,3,3,3,4],
[4,7,10,0,7,7,7,0,7,4,7,4,4],
[7,7,10,3,0,10,10,3,0,3,7,7,7],
[4,7,10,0,7,7,7,6,7,0,7,4,4],
[4,10,7,0,3,7,7,3,3,3,0,4,7],
[4,10,10,0,3,10,7,6,3,6,6,0,7],
[4,7,10,3,3,10,6,6,3,6,3,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 107, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,4,7,7,5,7,6,4,2,5,1,9],
[0,0,1,3,2,1,0,4,2,1,0,1,5],
[6,9,0,6,8,4,7,7,4,4,3,1,9],
[3,7,4,0,7,3,4,4,7,1,3,1,7],
[3,8,2,3,0,4,4,5,4,2,5,1,5],
[5,9,6,7,6,0,6,7,9,4,6,6,6],
[3,10,3,6,6,4,0,8,4,3,3,1,7],
[4,6,3,6,5,3,2,0,3,5,1,1,9],
[6,8,6,3,6,1,6,7,0,3,4,2,7],
[8,9,6,9,8,6,7,5,7,0,4,5,9],
[5,10,7,7,5,4,7,9,6,6,0,3,10],
[9,9,9,9,9,4,9,9,8,5,7,0,9],
[1,5,1,3,5,4,3,1,3,1,0,1,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 108, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,1,2,3,1,5,2,4,1,0,4,2],
[7,0,2,4,5,4,7,4,7,5,7,6,6],
[9,8,0,5,5,5,6,4,6,6,7,5,9],
[8,6,5,0,3,4,5,6,7,7,6,5,8],
[7,5,5,7,0,5,7,5,6,5,5,7,5],
[9,6,5,6,5,0,6,5,6,7,6,6,9],
[5,3,4,5,3,4,0,1,4,4,2,2,5],
[8,6,6,4,5,5,9,0,6,5,4,6,5],
[6,3,4,3,4,4,6,4,0,4,6,6,6],
[9,5,4,3,5,3,6,5,6,0,5,5,8],
[10,3,3,4,5,4,8,6,4,5,0,8,9],
[6,4,5,5,3,4,8,4,4,5,2,0,5],
[8,4,1,2,5,1,5,5,4,2,1,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 109, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,7,5,4,7,6,5,5,6,5,6,7],
[6,0,5,7,6,9,7,7,6,6,5,9,5],
[3,5,0,5,4,7,7,4,6,6,5,7,6],
[5,3,5,0,2,5,5,3,5,5,4,6,4],
[6,4,6,8,0,7,5,7,5,7,7,8,4],
[3,1,3,5,3,0,6,3,5,6,3,7,5],
[4,3,3,5,5,4,0,4,6,8,3,7,3],
[5,3,6,7,3,7,6,0,5,7,6,7,4],
[5,4,4,5,5,5,4,5,0,4,5,4,3],
[4,4,4,5,3,4,2,3,6,0,4,5,3],
[5,5,5,6,3,7,7,4,5,6,0,6,6],
[4,1,3,4,2,3,3,3,6,5,4,0,5],
[3,5,4,6,6,5,7,6,7,7,4,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 110, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,3,3,5,4,2,5,5,6,5,5,1],
[2,0,5,4,7,5,3,5,1,4,6,4,1],
[7,5,0,6,10,5,6,5,6,5,6,6,6],
[7,6,4,0,7,5,5,5,5,4,9,4,3],
[5,3,0,3,0,4,2,5,3,3,4,6,4],
[6,5,5,5,6,0,2,2,5,5,6,3,3],
[8,7,4,5,8,8,0,7,7,7,7,5,4],
[5,5,5,5,5,8,3,0,5,5,7,2,1],
[5,9,4,5,7,5,3,5,0,7,6,7,1],
[4,6,5,6,7,5,3,5,3,0,6,6,3],
[5,4,4,1,6,4,3,3,4,4,0,3,2],
[5,6,4,6,4,7,5,8,3,4,7,0,1],
[9,9,4,7,6,7,6,9,9,7,8,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 111, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,4,4,6,7,2,4,7,7,4,3,1],
[5,0,6,3,5,7,0,3,6,6,3,3,0],
[6,4,0,3,5,6,1,3,3,4,4,4,1],
[6,7,7,0,6,7,2,5,7,8,4,4,2],
[4,5,5,4,0,6,0,2,6,3,3,4,2],
[3,3,4,3,4,0,3,1,2,1,2,6,3],
[8,10,9,8,10,7,0,5,7,8,4,5,6],
[6,7,7,5,8,9,5,0,6,5,7,5,7],
[3,4,7,3,4,8,3,4,0,2,3,5,3],
[3,4,6,2,7,9,2,5,8,0,5,5,2],
[6,7,6,6,7,8,6,3,7,5,0,5,4],
[7,7,6,6,6,4,5,5,5,5,5,0,4],
[9,10,9,8,8,7,4,3,7,8,6,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 112, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,4,5,6,5,4,7,6,5,7,8,2],
[7,0,5,8,5,5,4,6,4,5,6,8,4],
[6,5,0,6,4,4,3,5,7,5,7,7,6],
[5,2,4,0,2,3,4,6,3,4,4,5,4],
[4,5,6,8,0,2,4,7,6,4,9,8,4],
[5,5,6,7,8,0,4,8,7,3,8,8,5],
[6,6,7,6,6,6,0,9,6,5,8,8,6],
[3,4,5,4,3,2,1,0,3,3,6,5,3],
[4,6,3,7,4,3,4,7,0,5,5,7,5],
[5,5,5,6,6,7,5,7,5,0,7,9,4],
[3,4,3,6,1,2,2,4,5,3,0,8,3],
[2,2,3,5,2,2,2,5,3,1,2,0,2],
[8,6,4,6,6,5,4,7,5,6,7,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 113, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,8,8,9,7,8,7,8,4,8,8,7],
[2,0,4,4,5,6,5,4,5,4,6,6,6],
[2,6,0,8,8,7,9,7,5,4,6,4,7],
[2,6,2,0,9,4,9,5,6,5,7,5,6],
[1,5,2,1,0,3,3,4,3,1,4,5,4],
[3,4,3,6,7,0,5,3,5,5,4,5,8],
[2,5,1,1,7,5,0,3,5,3,5,4,7],
[3,6,3,5,6,7,7,0,6,4,6,4,7],
[2,5,5,4,7,5,5,4,0,0,4,4,4],
[6,6,6,5,9,5,7,6,10,0,5,8,5],
[2,4,4,3,6,6,5,4,6,5,0,5,7],
[2,4,6,5,5,5,6,6,6,2,5,0,4],
[3,4,3,4,6,2,3,3,6,5,3,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 114, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,2,3,3,3,3,4,5,4,6,4,4],
[6,0,3,6,3,5,4,4,5,6,6,4,3],
[8,7,0,5,7,6,6,7,8,6,9,8,7],
[7,4,5,0,7,4,3,5,5,5,6,5,5],
[7,7,3,3,0,4,4,4,7,7,6,6,6],
[7,5,4,6,6,0,4,6,6,6,8,5,4],
[7,6,4,7,6,6,0,5,7,5,7,6,8],
[6,6,3,5,6,4,5,0,4,9,8,3,5],
[5,5,2,5,3,4,3,6,0,5,6,5,3],
[6,4,4,5,3,4,5,1,5,0,6,3,3],
[4,4,1,4,4,2,3,2,4,4,0,2,3],
[6,6,2,5,4,5,4,7,5,7,8,0,4],
[6,7,3,5,4,6,2,5,7,7,7,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 115, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,5,6,3,5,5,3,6,7,5,4,5],
[3,0,5,3,4,5,4,3,4,6,3,4,3],
[5,5,0,6,5,6,6,5,4,7,4,5,4],
[4,7,4,0,4,5,6,3,6,6,5,4,5],
[7,6,5,6,0,7,6,6,6,8,7,5,6],
[5,5,4,5,3,0,5,4,5,6,6,4,4],
[5,6,4,4,4,5,0,4,5,6,4,4,4],
[7,7,5,7,4,6,6,0,7,9,6,5,5],
[4,6,6,4,4,5,5,3,0,7,5,5,4],
[3,4,3,4,2,4,4,1,3,0,3,3,2],
[5,7,6,5,3,4,6,4,5,7,0,5,3],
[6,6,5,6,5,6,6,5,5,7,5,0,6],
[5,7,6,5,4,6,6,5,6,8,7,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 116, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,0,3,0,0,7,0,3,3,3,3,0],
[7,0,7,7,4,3,4,3,7,7,7,3,7],
[10,3,0,10,7,3,7,6,6,10,6,6,10],
[7,3,0,0,0,0,4,0,6,3,0,3,7],
[10,6,3,10,0,6,7,6,6,3,6,6,10],
[10,7,7,10,4,0,7,10,10,7,10,10,10],
[3,6,3,6,3,3,0,3,6,3,6,6,3],
[10,7,4,10,4,0,7,0,10,7,10,10,10],
[7,3,4,4,4,0,4,0,0,7,0,3,7],
[7,3,0,7,7,3,7,3,3,0,3,3,7],
[7,3,4,10,4,0,4,0,10,7,0,6,7],
[7,7,4,7,4,0,4,0,7,7,4,0,7],
[10,3,0,3,0,0,7,0,3,3,3,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 117, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,7,3,3,7,3,7,4,5,0,7,7],
[3,0,2,2,2,0,2,7,1,2,0,4,0],
[3,8,0,2,2,4,3,8,5,5,0,4,0],
[7,8,8,0,8,5,8,8,5,10,5,4,5],
[7,8,8,2,0,4,3,8,5,6,5,4,5],
[3,10,6,5,6,0,5,10,1,6,3,9,3],
[7,8,7,2,7,5,0,8,5,6,5,4,5],
[3,3,2,2,2,0,2,0,1,2,2,0,2],
[6,9,5,5,5,9,5,9,0,5,5,9,5],
[5,8,5,0,4,4,4,8,5,0,4,4,4],
[10,10,10,5,5,7,5,8,5,6,0,7,8],
[3,6,6,6,6,1,6,10,1,6,3,0,3],
[3,10,10,5,5,7,5,8,5,6,2,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 118, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,2,2,4,7,4,7,5,7,2,8,4],
[6,0,4,3,5,9,2,5,7,5,5,8,3],
[8,6,0,6,6,5,3,6,8,6,5,6,6],
[8,7,4,0,6,9,6,6,8,6,6,10,8],
[6,5,4,4,0,9,5,6,8,6,4,8,6],
[3,1,5,1,1,0,3,1,3,1,3,8,1],
[6,8,7,4,5,7,0,6,8,6,5,6,6],
[3,5,4,4,4,9,4,0,8,4,4,10,2],
[5,3,2,2,2,7,2,2,0,2,2,8,2],
[3,5,4,4,4,9,4,6,8,0,4,10,5],
[8,5,5,4,6,7,5,6,8,6,0,8,8],
[2,2,4,0,2,2,4,0,2,0,2,0,2],
[6,7,4,2,4,9,4,8,8,5,2,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 119, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,6,5,6,8,5,6,9,7,7,6,8],
[3,0,3,3,4,5,3,3,4,4,3,2,3],
[4,7,0,4,6,6,4,3,6,5,4,6,4],
[5,7,6,0,8,8,5,5,6,6,5,7,7],
[4,6,4,2,0,5,3,4,5,4,3,4,5],
[2,5,4,2,5,0,4,4,3,4,3,6,5],
[5,7,6,5,7,6,0,6,8,7,5,5,7],
[4,7,7,5,6,6,4,0,6,5,5,6,5],
[1,6,4,4,5,7,2,4,0,4,4,5,5],
[3,6,5,4,6,6,3,5,6,0,4,5,5],
[3,7,6,5,7,7,5,5,6,6,0,4,6],
[4,8,4,3,6,4,5,4,5,5,6,0,4],
[2,7,6,3,5,5,3,5,5,5,4,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 120, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,8,5,8,6,4,6,5,8,5,5,7],
[3,0,3,4,6,2,5,7,2,5,4,4,4],
[2,7,0,4,3,3,3,5,1,3,3,5,2],
[5,6,6,0,5,5,4,5,3,6,4,5,5],
[2,4,7,5,0,2,3,4,3,5,4,4,7],
[4,8,7,5,8,0,4,6,3,9,7,7,6],
[6,5,7,6,7,6,0,7,6,7,6,4,7],
[4,3,5,5,6,4,3,0,5,5,6,4,5],
[5,8,9,7,7,7,4,5,0,9,8,7,9],
[2,5,7,4,5,1,3,5,1,0,4,3,5],
[5,6,7,6,6,3,4,4,2,6,0,4,6],
[5,6,5,5,6,3,6,6,3,7,6,0,6],
[3,6,8,5,3,4,3,5,1,5,4,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 121, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,1,1,5,5,2,3,5,5,3,3,4],
[6,0,3,3,5,7,2,5,6,4,4,4,5],
[9,7,0,5,7,6,7,7,7,5,9,9,8],
[9,7,5,0,7,8,6,6,7,6,9,8,8],
[5,5,3,3,0,5,2,4,5,4,3,4,4],
[5,3,4,2,5,0,2,4,4,2,4,5,4],
[8,8,3,4,8,8,0,5,6,5,5,5,5],
[7,5,3,4,6,6,5,0,6,5,5,7,7],
[5,4,3,3,5,6,4,4,0,5,4,4,4],
[5,6,5,4,6,8,5,5,5,0,5,5,4],
[7,6,1,1,7,6,5,5,6,5,0,5,5],
[7,6,1,2,6,5,5,3,6,5,5,0,6],
[6,5,2,2,6,6,5,3,6,6,5,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 122, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,0,2,6,4,3,5,5,5,4,3,6],
[8,0,4,7,8,7,7,7,5,6,6,8,10],
[10,6,0,6,8,8,7,5,5,8,6,8,10],
[8,3,4,0,8,2,5,5,3,8,6,5,10],
[4,2,2,2,0,4,4,5,3,2,6,4,9],
[6,3,2,8,6,0,3,7,5,8,6,8,8],
[7,3,3,5,6,7,0,5,3,5,4,5,9],
[5,3,5,5,5,3,5,0,1,5,3,5,7],
[5,5,5,7,7,5,7,9,0,5,6,5,10],
[5,4,2,2,8,2,5,5,5,0,4,2,7],
[6,4,4,4,4,4,6,7,4,6,0,6,6],
[7,2,2,5,6,2,5,5,5,8,4,0,8],
[4,0,0,0,1,2,1,3,0,3,4,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 123, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,6,7,7,7,10,6,5,6,5,3,4],
[5,0,3,7,2,7,7,3,5,6,5,1,5],
[4,7,0,7,4,10,9,4,9,7,8,4,4],
[3,3,3,0,3,4,7,3,5,3,3,0,3],
[3,8,6,7,0,6,10,5,8,5,5,5,3],
[3,3,0,6,4,0,7,4,5,4,3,1,3],
[0,3,1,3,0,3,0,0,2,0,0,0,0],
[4,7,6,7,5,6,10,0,9,6,6,5,4],
[5,5,1,5,2,5,8,1,0,4,0,1,5],
[4,4,3,7,5,6,10,4,6,0,2,1,4],
[5,5,2,7,5,7,10,4,10,8,0,2,5],
[7,9,6,10,5,9,10,5,9,9,8,0,4],
[6,5,6,7,7,7,10,6,5,6,5,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 124, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,6,6,5,4,6,5,4,8,6,6,9],
[6,0,7,8,6,5,7,6,5,8,8,7,9],
[4,3,0,8,3,5,5,5,3,6,7,5,8],
[4,2,2,0,3,3,6,3,4,6,7,4,8],
[5,4,7,7,0,4,6,6,3,6,6,6,9],
[6,5,5,7,6,0,7,4,5,9,8,5,7],
[4,3,5,4,4,3,0,2,1,5,3,3,7],
[5,4,5,7,4,6,8,0,6,7,6,6,7],
[6,5,7,6,7,5,9,4,0,7,6,5,8],
[2,2,4,4,4,1,5,3,3,0,3,2,7],
[4,2,3,3,4,2,7,4,4,7,0,2,7],
[4,3,5,6,4,5,7,4,5,8,8,0,7],
[1,1,2,2,1,3,3,3,2,3,3,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 125, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,7,7,6,6,4,3,5,7,8,7,6],
[2,0,4,5,3,3,4,2,3,4,6,5,5],
[3,6,0,6,4,2,3,2,1,6,6,5,6],
[3,5,4,0,3,3,3,2,2,3,4,5,3],
[4,7,6,7,0,2,4,2,4,5,6,6,5],
[4,7,8,7,8,0,3,3,5,7,7,9,6],
[6,6,7,7,6,7,0,5,5,8,9,7,8],
[7,8,8,8,8,7,5,0,7,7,7,8,6],
[5,7,9,8,6,5,5,3,0,7,7,6,6],
[3,6,4,7,5,3,2,3,3,0,5,3,6],
[2,4,4,6,4,3,1,3,3,5,0,4,2],
[3,5,5,5,4,1,3,2,4,7,6,0,4],
[4,5,4,7,5,4,2,4,4,4,8,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 126, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,5,7,6,3,5,5,5,9,3,3,5],
[0,0,3,7,6,3,2,1,5,5,3,3,5],
[5,7,0,7,6,3,2,5,8,6,4,6,8],
[3,3,3,0,4,3,1,1,2,5,2,3,4],
[4,4,4,6,0,5,5,5,3,6,3,0,5],
[7,7,7,7,5,0,8,8,7,8,6,4,7],
[5,8,8,9,5,2,0,9,8,8,7,5,8],
[5,9,5,9,5,2,1,0,7,4,5,2,7],
[5,5,2,8,7,3,2,3,0,6,0,4,2],
[1,5,4,5,4,2,2,6,4,0,3,3,6],
[7,7,6,8,7,4,3,5,10,7,0,5,9],
[7,7,4,7,10,6,5,8,6,7,5,0,6],
[5,5,2,6,5,3,2,3,8,4,1,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 127, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,8,9,6,8,6,4,8,7,3,8,6],
[4,0,3,7,4,6,5,7,3,4,3,7,4],
[2,7,0,5,6,6,3,4,6,7,1,6,6],
[1,3,5,0,6,6,4,5,3,4,1,6,6],
[4,6,4,4,0,9,5,7,5,6,3,9,8],
[2,4,4,4,1,0,5,4,3,4,1,1,4],
[4,5,7,6,5,5,0,5,5,5,2,5,5],
[6,3,6,5,3,6,5,0,6,5,4,5,4],
[2,7,4,7,5,7,5,4,0,3,3,5,5],
[3,6,3,6,4,6,5,5,7,0,3,6,3],
[7,7,9,9,7,9,8,6,7,7,0,9,5],
[2,3,4,4,1,9,5,5,5,4,1,0,6],
[4,6,4,4,2,6,5,6,5,7,5,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 128, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,8,8,4,6,8,7,6,8,4,6,9],
[3,0,3,5,1,4,5,3,1,3,0,2,5],
[2,7,0,5,4,5,7,5,5,6,2,4,8],
[2,5,5,0,4,4,6,5,4,6,2,4,5],
[6,9,6,6,0,4,9,8,6,7,5,7,7],
[4,6,5,6,6,0,6,5,3,8,4,7,6],
[2,5,3,4,1,4,0,5,5,6,0,2,5],
[3,7,5,5,2,5,5,0,4,4,4,6,5],
[4,9,5,6,4,7,5,6,0,7,5,7,7],
[2,7,4,4,3,2,4,6,3,0,2,4,4],
[6,10,8,8,5,6,10,6,5,8,0,6,10],
[4,8,6,6,3,3,8,4,3,6,4,0,8],
[1,5,2,5,3,4,5,5,3,6,0,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 129, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,4,3,8,2,1,5,4,5,5,4,3],
[5,0,5,6,7,5,5,6,7,6,9,5,5],
[6,5,0,7,10,6,6,7,7,7,9,4,6],
[7,4,3,0,8,1,1,5,4,4,7,6,6],
[2,3,0,2,0,0,0,0,4,1,3,2,2],
[8,5,4,9,10,0,6,7,7,10,9,6,5],
[9,5,4,9,10,4,0,10,7,10,10,7,6],
[5,4,3,5,10,3,0,0,7,6,9,2,2],
[6,3,3,6,6,3,3,3,0,7,9,3,3],
[5,4,3,6,9,0,0,4,3,0,3,6,5],
[5,1,1,3,7,1,0,1,1,7,0,3,2],
[6,5,6,4,8,4,3,8,7,4,7,0,8],
[7,5,4,4,8,5,4,8,7,5,8,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 130, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,4,4,3,5,3,3,5,7,3,5,5],
[8,0,7,3,6,7,4,6,8,6,5,6,6],
[6,3,0,4,4,4,5,4,6,5,4,5,5],
[6,7,6,0,7,8,3,8,8,6,3,5,4],
[7,4,6,3,0,4,5,4,8,6,4,5,4],
[5,3,6,2,6,0,3,4,6,4,3,5,4],
[7,6,5,7,5,7,0,6,8,6,4,6,5],
[7,4,6,2,6,6,4,0,8,6,5,5,5],
[5,2,4,2,2,4,2,2,0,4,3,4,3],
[3,4,5,4,4,6,4,4,6,0,4,4,4],
[7,5,6,7,6,7,6,5,7,6,0,8,6],
[5,4,5,5,5,5,4,5,6,6,2,0,5],
[5,4,5,6,6,6,5,5,7,6,4,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 131, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,9,9,9,5,6,6,9,5,5,10,4],
[0,0,9,5,9,5,5,0,4,5,5,5,4],
[1,1,0,1,5,0,1,1,1,6,1,1,1],
[1,5,9,0,4,5,6,1,4,5,5,5,4],
[1,1,5,6,0,5,6,1,1,5,5,1,0],
[5,5,10,5,5,0,6,1,5,6,6,5,5],
[4,5,9,4,4,4,0,1,4,5,0,5,4],
[4,10,9,9,9,9,9,0,4,5,9,5,4],
[1,6,9,6,9,5,6,6,0,5,5,5,4],
[5,5,4,5,5,4,5,5,5,0,4,5,5],
[5,5,9,5,5,4,10,1,5,6,0,5,5],
[0,5,9,5,9,5,5,5,5,5,5,0,4],
[6,6,9,6,10,5,6,6,6,5,5,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 132, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,6,6,5,4,5,7,7,7,7,5,6],
[3,0,6,6,5,2,4,6,4,6,5,4,6],
[4,4,0,4,3,3,6,6,4,5,4,3,5],
[4,4,6,0,1,3,5,4,3,4,2,3,5],
[5,5,7,9,0,5,5,7,5,5,3,6,7],
[6,8,7,7,5,0,5,9,7,8,6,8,8],
[5,6,4,5,5,5,0,6,6,7,5,5,5],
[3,4,4,6,3,1,4,0,5,5,1,3,7],
[3,6,6,7,5,3,4,5,0,6,5,4,5],
[3,4,5,6,5,2,3,5,4,0,3,4,4],
[3,5,6,8,7,4,5,9,5,7,0,6,7],
[5,6,7,7,4,2,5,7,6,6,4,0,7],
[4,4,5,5,3,2,5,3,5,6,3,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 133, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,2,2,1,3,3,2,4,5,4,2,1],
[5,0,1,2,2,3,2,4,4,6,3,5,5],
[8,9,0,5,6,6,4,5,6,6,4,8,5],
[8,8,5,0,7,6,5,7,8,7,6,6,5],
[9,8,4,3,0,6,3,4,6,6,5,6,4],
[7,7,4,4,4,0,5,5,5,7,6,5,3],
[7,8,6,5,7,5,0,6,8,5,7,8,3],
[8,6,5,3,6,5,4,0,6,5,5,5,4],
[6,6,4,2,4,5,2,4,0,5,4,5,4],
[5,4,4,3,4,3,5,5,5,0,6,5,3],
[6,7,6,4,5,4,3,5,6,4,0,6,4],
[8,5,2,4,4,5,2,5,5,5,4,0,2],
[9,5,5,5,6,7,7,6,6,7,6,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 134, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,10,10,10,8,10,10,10,8,4,10],
[0,0,6,4,8,8,4,6,10,6,4,4,6],
[0,4,0,0,4,8,0,0,4,0,4,0,0],
[0,6,10,0,10,10,0,2,6,6,4,0,6],
[0,2,6,0,0,4,0,2,2,6,0,0,2],
[0,2,2,0,6,0,0,2,2,2,0,0,2],
[2,6,10,10,10,10,0,6,10,10,8,4,10],
[0,4,10,8,8,8,4,0,8,8,8,4,8],
[0,0,6,4,8,8,0,2,0,4,0,4,2],
[0,4,10,4,4,8,0,2,6,0,4,0,6],
[2,6,6,6,10,10,2,2,10,6,0,6,6],
[6,6,10,10,10,10,6,6,6,10,4,0,6],
[0,4,10,4,8,8,0,2,8,4,4,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 135, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,1,6,4,5,5,6,5,7,8,5,6],
[6,0,3,4,3,6,5,6,5,6,8,4,6],
[9,7,0,9,9,7,8,9,5,7,10,6,9],
[4,6,1,0,3,4,3,7,5,7,8,3,4],
[6,7,1,7,0,6,7,8,5,7,7,6,6],
[5,4,3,6,4,0,3,4,4,6,7,3,6],
[5,5,2,7,3,7,0,7,6,7,8,6,6],
[4,4,1,3,2,6,3,0,4,6,8,5,5],
[5,5,5,5,5,6,4,6,0,5,8,6,5],
[3,4,3,3,3,4,3,4,5,0,7,5,4],
[2,2,0,2,3,3,2,2,2,3,0,4,4],
[5,6,4,7,4,7,4,5,4,5,6,0,6],
[4,4,1,6,4,4,4,5,5,6,6,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 136, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,3,0,3,3,3,8,4,5,1,2,5],
[5,0,6,3,4,4,4,5,4,3,1,3,6],
[7,4,0,4,5,4,7,7,3,6,3,4,4],
[10,7,6,0,4,7,7,8,8,8,3,5,6],
[7,6,5,6,0,6,4,7,5,6,3,7,6],
[7,6,6,3,4,0,5,5,6,3,3,3,3],
[7,6,3,3,6,5,0,7,3,7,1,5,5],
[2,5,3,2,3,5,3,0,4,3,1,0,3],
[6,6,7,2,5,4,7,6,0,4,5,4,4],
[5,7,4,2,4,7,3,7,6,0,1,5,5],
[9,9,7,7,7,7,9,9,5,9,0,7,9],
[8,7,6,5,3,7,5,10,6,5,3,0,5],
[5,4,6,4,4,7,5,7,6,5,1,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 137, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,8,8,8,8,7,8,8,8,7,10,8],
[5,0,3,4,7,3,4,4,5,5,4,6,4],
[2,7,0,5,4,5,6,1,5,7,1,7,10],
[2,6,5,0,6,9,6,2,7,6,3,7,9],
[2,3,6,4,0,4,6,0,4,6,0,6,6],
[2,7,5,1,6,0,3,1,2,4,4,4,7],
[3,6,4,4,4,7,0,1,4,9,3,6,6],
[2,6,9,8,10,9,9,0,5,10,4,10,10],
[2,5,5,3,6,8,6,5,0,9,3,6,5],
[2,5,3,4,4,6,1,0,1,0,3,6,3],
[3,6,9,7,10,6,7,6,7,7,0,7,10],
[0,4,3,3,4,6,4,0,4,4,3,0,3],
[2,6,0,1,4,3,4,0,5,7,0,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 138, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,4,5,6,4,5,3,4,5,4,4,7],
[5,0,5,4,3,2,6,2,4,5,6,3,6],
[6,5,0,7,6,6,6,3,6,6,6,4,8],
[5,6,3,0,4,5,4,2,4,7,4,2,4],
[4,7,4,6,0,3,6,1,6,7,7,5,6],
[6,8,4,5,7,0,6,4,8,6,8,3,7],
[5,4,4,6,4,4,0,3,6,6,5,2,5],
[7,8,7,8,9,6,7,0,8,9,9,5,7],
[6,6,4,6,4,2,4,2,0,5,5,2,6],
[5,5,4,3,3,4,4,1,5,0,4,2,5],
[6,4,4,6,3,2,5,1,5,6,0,2,5],
[6,7,6,8,5,7,8,5,8,8,8,0,7],
[3,4,2,6,4,3,5,3,4,5,5,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 139, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,7,3,6,5,3,2,4,3,6,6,2],
[4,0,5,3,4,3,2,4,5,4,6,6,4],
[3,5,0,1,5,5,3,3,4,4,4,4,1],
[7,7,9,0,5,5,2,6,5,4,7,6,4],
[4,6,5,5,0,5,4,4,4,5,6,7,5],
[5,7,5,5,5,0,3,4,6,5,6,4,4],
[7,8,7,8,6,7,0,6,8,6,8,8,5],
[8,6,7,4,6,6,4,0,6,5,8,6,3],
[6,5,6,5,6,4,2,4,0,4,5,6,5],
[7,6,6,6,5,5,4,5,6,0,5,5,4],
[4,4,6,3,4,4,2,2,5,5,0,5,3],
[4,4,6,4,3,6,2,4,4,5,5,0,2],
[8,6,9,6,5,6,5,7,5,6,7,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 140, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,8,8,8,5,5,8,8,8,8,3,7],
[2,0,5,2,7,4,2,2,2,2,7,2,4],
[2,5,0,5,2,5,3,0,0,2,2,3,7],
[2,8,5,0,5,2,3,5,2,7,5,5,7],
[2,3,8,5,0,7,5,2,5,5,7,5,7],
[5,6,5,8,3,0,5,5,5,5,5,5,8],
[5,8,7,7,5,5,0,5,7,7,5,2,7],
[2,8,10,5,8,5,5,0,7,10,8,5,7],
[2,8,10,8,5,5,3,3,0,10,8,5,7],
[2,8,8,3,5,5,3,0,0,0,8,5,5],
[2,3,8,5,3,5,5,2,2,2,0,5,7],
[7,8,7,5,5,5,8,5,5,5,5,0,7],
[3,6,3,3,3,2,3,3,3,5,3,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 141, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,2,6,2,5,7,2,5,2,2,4,5],
[5,0,2,5,2,6,6,2,4,2,3,4,4],
[8,8,0,7,2,8,6,3,5,4,3,6,5],
[4,5,3,0,1,5,6,2,5,1,2,3,3],
[8,8,8,9,0,8,8,5,8,7,7,6,9],
[5,4,2,5,2,0,4,1,4,2,3,3,4],
[3,4,4,4,2,6,0,2,5,3,3,5,5],
[8,8,7,8,5,9,8,0,7,8,7,7,10],
[5,6,5,5,2,6,5,3,0,4,3,6,5],
[8,8,6,9,3,8,7,2,6,0,3,6,5],
[8,7,7,8,3,7,7,3,7,7,0,5,6],
[6,6,4,7,4,7,5,3,4,4,5,0,6],
[5,6,5,7,1,6,5,0,5,5,4,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 142, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,5,6,5,5,8,8,5,4,8,7,8],
[2,0,1,6,1,5,1,3,0,2,4,3,6],
[5,9,0,6,4,4,3,7,0,6,7,7,9],
[4,4,4,0,1,4,4,4,4,1,4,4,4],
[5,9,6,9,0,7,3,3,3,2,3,3,6],
[5,5,6,6,3,0,6,3,0,2,4,5,6],
[2,9,7,6,7,4,0,7,4,6,8,9,10],
[2,7,3,6,7,7,3,0,0,6,10,5,10],
[5,10,10,6,7,10,6,10,0,6,10,9,10],
[6,8,4,9,8,8,4,4,4,0,8,3,10],
[2,6,3,6,7,6,2,0,0,2,0,2,7],
[3,7,3,6,7,5,1,5,1,7,8,0,10],
[2,4,1,6,4,4,0,0,0,0,3,0,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 143, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,5,6,5,7,6,6,7,6,5,7,4],
[6,0,6,6,6,7,6,8,8,8,6,7,5],
[5,4,0,6,7,7,7,7,7,7,6,8,5],
[4,4,4,0,5,7,4,4,6,4,5,7,6],
[5,4,3,5,0,7,4,4,4,4,4,6,5],
[3,3,3,3,3,0,2,3,4,3,4,7,3],
[4,4,3,6,6,8,0,6,6,5,4,7,6],
[4,2,3,6,6,7,4,0,6,7,1,5,5],
[3,2,3,4,6,6,4,4,0,4,4,6,4],
[4,2,3,6,6,7,5,3,6,0,2,5,5],
[5,4,4,5,6,6,6,9,6,8,0,8,8],
[3,3,2,3,4,3,3,5,4,5,2,0,5],
[6,5,5,4,5,7,4,5,6,5,2,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 144, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,7,7,5,5,6,4,6,6,8,4,5],
[4,0,6,7,4,5,6,5,4,7,5,5,7],
[3,4,0,7,3,5,5,3,5,6,5,5,4],
[3,3,3,0,2,4,3,2,4,2,4,2,4],
[5,6,7,8,0,7,5,4,6,6,7,7,6],
[5,5,5,6,3,0,5,5,6,6,8,6,5],
[4,4,5,7,5,5,0,4,6,5,5,5,5],
[6,5,7,8,6,5,6,0,7,8,8,7,7],
[4,6,5,6,4,4,4,3,0,5,3,7,7],
[4,3,4,8,4,4,5,2,5,0,5,4,6],
[2,5,5,6,3,2,5,2,7,5,0,5,4],
[6,5,5,8,3,4,5,3,3,6,5,0,5],
[5,3,6,6,4,5,5,3,3,4,6,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 145, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,7,7,2,2,7,4,2,7,10,7,2],
[6,0,5,7,5,0,5,2,2,5,8,5,0],
[3,5,0,5,5,0,0,2,2,3,8,3,0],
[3,3,5,0,0,0,3,5,5,6,6,3,0],
[8,5,5,10,0,2,5,5,7,8,8,8,5],
[8,10,10,10,8,0,10,7,5,10,10,10,8],
[3,5,10,7,5,0,0,2,2,7,10,5,2],
[6,8,8,5,5,3,8,0,8,8,8,5,5],
[8,8,8,5,3,5,8,2,0,5,8,5,5],
[3,5,7,4,2,0,3,2,5,0,10,0,2],
[0,2,2,4,2,0,0,2,2,0,0,0,0],
[3,5,7,7,2,0,5,5,5,10,10,0,5],
[8,10,10,10,5,2,8,5,5,8,10,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 146, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,9,0,5,5,9,4,4,4,9,0,9],
[10,0,9,4,5,10,10,10,10,9,9,5,10],
[1,1,0,0,5,1,10,1,1,1,5,0,1],
[10,6,10,0,10,10,10,10,10,10,10,5,10],
[5,5,5,0,0,6,5,5,5,5,5,5,5],
[5,0,9,0,4,0,9,0,4,0,5,5,9],
[1,0,0,0,5,1,0,0,0,0,0,0,0],
[6,0,9,0,5,10,10,0,10,9,9,5,9],
[6,0,9,0,5,6,10,0,0,0,5,5,5],
[6,1,9,0,5,10,10,1,10,0,5,5,10],
[1,1,5,0,5,5,10,1,5,5,0,0,5],
[10,5,10,5,5,5,10,5,5,5,10,0,10],
[1,0,9,0,5,1,10,1,5,0,5,0,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 147, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,7,5,5,3,6,7,7,4,3,7,7],
[5,0,7,5,4,5,3,7,8,4,2,7,8],
[3,3,0,4,5,3,5,6,6,2,3,6,6],
[5,5,6,0,3,6,4,5,4,3,2,6,5],
[5,6,5,7,0,6,7,6,9,6,5,7,7],
[7,5,7,4,4,0,5,6,7,5,6,5,6],
[4,7,5,6,3,5,0,6,6,4,6,5,6],
[3,3,4,5,4,4,4,0,7,2,2,4,5],
[3,2,4,6,1,3,4,3,0,3,2,5,4],
[6,6,8,7,4,5,6,8,7,0,6,5,9],
[7,8,7,8,5,4,4,8,8,4,0,7,8],
[3,3,4,4,3,5,5,6,5,5,3,0,5],
[3,2,4,5,3,4,4,5,6,1,2,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 148, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,4,2,3,0,0,3,2,1,1,5,3],
[8,0,5,4,6,3,4,5,3,1,1,3,5],
[6,5,0,2,6,2,2,3,1,6,1,1,3],
[8,6,8,0,6,6,4,6,6,4,4,8,6],
[7,4,4,4,0,4,2,4,0,2,1,2,2],
[10,7,8,4,6,0,5,8,6,6,6,8,6],
[10,6,8,6,8,5,0,7,3,6,3,5,5],
[7,5,7,4,6,2,3,0,5,3,1,7,5],
[8,7,9,4,10,4,7,5,0,8,3,5,10],
[9,9,4,6,8,4,4,7,2,0,1,4,4],
[9,9,9,6,9,4,7,9,7,9,0,9,9],
[5,7,9,2,8,2,5,3,5,6,1,0,7],
[7,5,7,4,8,4,5,5,0,6,1,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 149, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,2,6,5,5,5,1,3,3,1,5,3],
[5,0,4,5,3,3,6,3,5,3,3,5,2],
[8,6,0,6,6,8,7,5,5,6,6,8,7],
[4,5,4,0,5,7,5,1,5,4,2,5,2],
[5,7,4,5,0,5,7,3,3,3,3,3,2],
[5,7,2,3,5,0,5,1,3,5,1,4,1],
[5,4,3,5,3,5,0,3,4,3,2,3,2],
[9,7,5,9,7,9,7,0,6,8,9,6,7],
[7,5,5,5,7,7,6,4,0,5,6,4,6],
[7,7,4,6,7,5,7,2,5,0,2,6,4],
[9,7,4,8,7,9,8,1,4,8,0,7,7],
[5,5,2,5,7,6,7,4,6,4,3,0,5],
[7,8,3,8,8,9,8,3,4,6,3,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 150, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,5,8,5,8,8,8,5,5,5,8,8],
[2,0,5,10,5,7,10,5,2,7,7,10,7],
[5,5,0,10,5,10,10,5,5,7,7,10,10],
[2,0,0,0,0,0,3,3,0,0,2,2,0],
[5,5,5,10,0,10,5,5,5,10,5,10,10],
[2,3,0,10,0,0,3,5,2,2,2,5,5],
[2,0,0,7,5,7,0,2,2,7,7,7,7],
[2,5,5,7,5,5,8,0,7,7,7,7,5],
[5,8,5,10,5,8,8,3,0,7,7,10,8],
[5,3,3,10,0,8,3,3,3,0,5,5,8],
[5,3,3,8,5,8,3,3,3,5,0,8,8],
[2,0,0,8,0,5,3,3,0,5,2,0,5],
[2,3,0,10,0,5,3,5,2,2,2,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 151, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,6,2,4,4,7,5,3,4,3,3,1],
[4,0,7,2,1,1,5,4,2,3,1,3,3],
[4,3,0,1,2,2,5,3,2,2,3,1,4],
[8,8,9,0,7,6,8,8,7,7,5,5,4],
[6,9,8,3,0,7,9,5,6,4,6,5,4],
[6,9,8,4,3,0,9,6,4,5,3,4,6],
[3,5,5,2,1,1,0,3,2,4,3,2,1],
[5,6,7,2,5,4,7,0,4,5,3,3,3],
[7,8,8,3,4,6,8,6,0,4,3,5,4],
[6,7,8,3,6,5,6,5,6,0,4,5,4],
[7,9,7,5,4,7,7,7,7,6,0,6,4],
[7,7,9,5,5,6,8,7,5,5,4,0,5],
[9,7,6,6,6,4,9,7,6,6,6,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 152, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,8,7,7,5,4,4,7,7,5,8,4],
[2,0,8,4,3,3,2,3,4,4,2,3,0],
[2,2,0,2,1,2,0,3,1,4,1,1,0],
[3,6,8,0,4,3,3,4,5,5,6,5,5],
[3,7,9,6,0,3,4,4,6,6,4,6,4],
[5,7,8,7,7,0,5,5,7,7,5,7,4],
[6,8,10,7,6,5,0,4,9,7,5,10,4],
[6,7,7,6,6,5,6,0,6,6,4,7,3],
[3,6,9,5,4,3,1,4,0,7,2,5,2],
[3,6,6,5,4,3,3,4,3,0,4,5,4],
[5,8,9,4,6,5,5,6,8,6,0,7,1],
[2,7,9,5,4,3,0,3,5,5,3,0,1],
[6,10,10,5,6,6,6,7,8,6,9,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 153, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,10,8,6,10,10,6,8,8,4,6,10],
[4,0,10,8,6,4,4,4,4,8,0,6,8],
[0,0,0,0,2,0,0,0,0,0,0,2,4],
[2,2,10,0,6,2,6,2,2,8,2,6,10],
[4,4,8,4,0,4,4,4,4,4,4,4,8],
[0,6,10,8,6,0,6,4,4,8,4,6,8],
[0,6,10,4,6,4,0,0,4,4,4,6,8],
[4,6,10,8,6,6,10,0,4,8,4,6,10],
[2,6,10,8,6,6,6,6,0,8,6,6,10],
[2,2,10,2,6,2,6,2,2,0,2,6,10],
[6,10,10,8,6,6,6,6,4,8,0,10,10],
[4,4,8,4,6,4,4,4,4,4,0,0,8],
[0,2,6,0,2,2,2,0,0,0,0,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 154, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,7,8,8,8,6,7,6,5,7,6,5],
[1,0,5,4,5,7,3,5,5,3,3,3,4],
[3,5,0,5,4,5,2,4,4,4,1,2,4],
[2,6,5,0,6,5,4,5,5,2,5,4,2],
[2,5,6,4,0,4,3,5,6,2,5,3,3],
[2,3,5,5,6,0,4,4,4,2,3,2,3],
[4,7,8,6,7,6,0,8,4,4,4,4,6],
[3,5,6,5,5,6,2,0,4,4,3,2,3],
[4,5,6,5,4,6,6,6,0,4,4,6,4],
[5,7,6,8,8,8,6,6,6,0,6,6,7],
[3,7,9,5,5,7,6,7,6,4,0,4,5],
[4,7,8,6,7,8,6,8,4,4,6,0,4],
[5,6,6,8,7,7,4,7,6,3,5,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 155, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,3,2,5,7,6,4,7,5,4,5,5],
[2,0,1,1,3,4,3,3,4,3,3,4,3],
[7,9,0,6,7,6,6,7,6,7,6,7,5],
[8,9,4,0,6,6,7,7,6,8,5,6,5],
[5,7,3,4,0,4,4,5,5,4,4,5,4],
[3,6,4,4,6,0,4,5,4,4,4,4,2],
[4,7,4,3,6,6,0,5,7,5,4,8,4],
[6,7,3,3,5,5,5,0,6,4,5,4,4],
[3,6,4,4,5,6,3,4,0,5,3,6,4],
[5,7,3,2,6,6,5,6,5,0,3,6,3],
[6,7,4,5,6,6,6,5,7,7,0,7,6],
[5,6,3,4,5,6,2,6,4,4,3,0,3],
[5,7,5,5,6,8,6,6,6,7,4,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 156, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,6,6,6,6,5,7,4,6,4,7,4],
[8,0,4,7,7,8,7,7,6,7,8,6,6],
[4,6,0,4,7,5,7,5,5,5,6,5,4],
[4,3,6,0,6,8,5,8,5,6,4,4,4],
[4,3,3,4,0,5,5,4,3,6,4,3,4],
[4,2,5,2,5,0,4,4,2,4,4,3,3],
[5,3,3,5,5,6,0,5,6,6,3,4,3],
[3,3,5,2,6,6,5,0,3,4,4,3,4],
[6,4,5,5,7,8,4,7,0,7,6,6,3],
[4,3,5,4,4,6,4,6,3,0,5,5,5],
[6,2,4,6,6,6,7,6,4,5,0,5,4],
[3,4,5,6,7,7,6,7,4,5,5,0,3],
[6,4,6,6,6,7,7,6,7,5,6,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 157, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,5,4,6,4,5,4,4,5,5,5,5],
[5,0,8,4,7,3,4,7,4,5,7,6,6],
[5,2,0,4,7,4,4,5,5,2,6,3,7],
[6,6,6,0,10,6,6,8,7,5,7,6,8],
[4,3,3,0,0,1,3,4,3,2,3,3,4],
[6,7,6,4,9,0,7,7,6,5,8,8,6],
[5,6,6,4,7,3,0,4,6,4,5,4,5],
[6,3,5,2,6,3,6,0,5,4,5,3,7],
[6,6,5,3,7,4,4,5,0,3,5,3,5],
[5,5,8,5,8,5,6,6,7,0,6,6,7],
[5,3,4,3,7,2,5,5,5,4,0,3,4],
[5,4,7,4,7,2,6,7,7,4,7,0,6],
[5,4,3,2,6,4,5,3,5,3,6,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 158, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,2,5,2,5,7,5,5,2,3,0,3],
[5,0,5,6,4,10,8,8,8,5,3,3,6],
[8,5,0,3,7,7,5,5,5,2,3,3,3],
[5,4,7,0,4,10,8,8,10,5,5,3,6],
[8,6,3,6,0,10,8,8,8,5,6,3,6],
[5,0,3,0,0,0,5,6,3,5,0,0,6],
[3,2,5,2,2,5,0,8,8,5,0,0,6],
[5,2,5,2,2,4,2,0,2,5,2,0,3],
[5,2,5,0,2,7,2,8,0,5,2,0,6],
[8,5,8,5,5,5,5,5,5,0,3,5,8],
[7,7,7,5,4,10,10,8,8,7,0,5,8],
[10,7,7,7,7,10,10,10,10,5,5,0,8],
[7,4,7,4,4,4,4,7,4,2,2,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 159, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,6,5,3,5,5,5,4,4,7,4,7],
[4,0,4,5,1,3,5,5,3,3,6,1,5],
[4,6,0,5,3,6,6,5,4,6,7,4,6],
[5,5,5,0,2,4,3,4,3,3,6,2,6],
[7,9,7,8,0,5,6,6,6,6,10,4,8],
[5,7,4,6,5,0,5,5,5,5,8,5,4],
[5,5,4,7,4,5,0,4,5,4,6,3,6],
[5,5,5,6,4,5,6,0,5,4,7,4,6],
[6,7,6,7,4,5,5,5,0,5,8,3,7],
[6,7,4,7,4,5,6,6,5,0,8,6,6],
[3,4,3,4,0,2,4,3,2,2,0,1,4],
[6,9,6,8,6,5,7,6,7,4,9,0,8],
[3,5,4,4,2,6,4,4,3,4,6,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 160, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,6,3,5,5,5,6,4,2,6,5,5],
[8,0,7,5,6,6,8,9,8,4,7,9,7],
[4,3,0,3,4,5,5,4,3,2,4,5,4],
[7,5,7,0,7,7,7,6,6,6,7,7,7],
[5,4,6,3,0,5,6,5,5,4,5,6,6],
[5,4,5,3,5,0,4,5,3,4,5,6,4],
[5,2,5,3,4,6,0,4,4,3,6,5,7],
[4,1,6,4,5,5,6,0,4,4,5,5,6],
[6,2,7,4,5,7,6,6,0,4,4,6,7],
[8,6,8,4,6,6,7,6,6,0,7,7,7],
[4,3,6,3,5,5,4,5,6,3,0,5,6],
[5,1,5,3,4,4,5,5,4,3,5,0,6],
[5,3,6,3,4,6,3,4,3,3,4,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 161, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,5,5,1,1,4,6,5,5,1,1,0],
[10,0,5,5,6,6,4,6,5,10,10,5,5],
[5,5,0,10,5,5,9,5,9,5,5,5,5],
[5,5,0,0,5,5,0,5,4,5,5,5,5],
[9,4,5,5,0,5,4,6,5,5,10,5,0],
[9,4,5,5,5,0,4,5,4,9,9,4,5],
[6,6,1,10,6,6,0,6,10,6,6,6,5],
[4,4,5,5,4,5,4,0,4,4,4,4,0],
[5,5,1,6,5,6,0,6,0,6,6,6,5],
[5,0,5,5,5,1,4,6,4,0,6,0,5],
[9,0,5,5,0,1,4,6,4,4,0,0,0],
[9,5,5,5,5,6,4,6,4,10,10,0,5],
[10,5,5,5,10,5,5,10,5,5,10,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 162, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,6,9,7,2,3,6,5,3,3,3,0],
[4,0,3,6,1,2,3,5,3,3,5,4,1],
[4,7,0,5,4,5,4,4,9,4,3,4,4],
[1,4,5,0,4,2,3,3,6,3,2,4,1],
[3,9,6,6,0,5,6,6,5,6,6,6,3],
[8,8,5,8,5,0,5,7,7,8,7,4,4],
[7,7,6,7,4,5,0,8,9,6,5,4,4],
[4,5,6,7,4,3,2,0,6,3,6,4,1],
[5,7,1,4,5,3,1,4,0,4,4,3,1],
[7,7,6,7,4,2,4,7,6,0,8,3,1],
[7,5,7,8,4,3,5,4,6,2,0,4,1],
[7,6,6,6,4,6,6,6,7,7,6,0,7],
[10,9,6,9,7,6,6,9,9,9,9,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 163, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,5,4,5,6,6,7,5,4,5,6,6],
[5,0,4,5,6,6,6,7,3,4,6,3,6],
[5,6,0,4,6,8,7,7,8,6,7,7,5],
[6,5,6,0,6,7,6,6,4,5,3,4,7],
[5,4,4,4,0,6,4,5,5,3,6,4,5],
[4,4,2,3,4,0,5,5,1,5,3,2,4],
[4,4,3,4,6,5,0,5,2,3,3,3,4],
[3,3,3,4,5,5,5,0,2,5,2,3,5],
[5,7,2,6,5,9,8,8,0,6,5,5,4],
[6,6,4,5,7,5,7,5,4,0,6,5,5],
[5,4,3,7,4,7,7,8,5,4,0,3,5],
[4,7,3,6,6,8,7,7,5,5,7,0,5],
[4,4,5,3,5,6,6,5,6,5,5,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 164, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,4,6,6,8,8,4,8,6,8,7,5],
[4,0,5,6,6,6,6,6,6,5,5,4,6],
[6,5,0,8,9,8,9,6,8,8,8,9,6],
[4,4,2,0,6,8,4,4,7,5,6,7,3],
[4,4,1,4,0,7,5,3,6,6,7,6,4],
[2,4,2,2,3,0,3,5,3,3,4,5,2],
[2,4,1,6,5,7,0,3,4,7,7,6,5],
[6,4,4,6,7,5,7,0,6,6,6,7,6],
[2,4,2,3,4,7,6,4,0,4,6,3,4],
[4,5,2,5,4,7,3,4,6,0,6,5,4],
[2,5,2,4,3,6,3,4,4,4,0,4,2],
[3,6,1,3,4,5,4,3,7,5,6,0,4],
[5,4,4,7,6,8,5,4,6,6,8,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 165, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,8,6,3,5,4,1,8,6,4,7,8],
[5,0,8,3,3,7,8,3,6,3,5,6,8],
[2,2,0,2,2,4,2,3,2,3,1,1,5],
[4,7,8,0,1,4,6,4,5,8,4,6,7],
[7,7,8,9,0,4,7,4,5,8,4,9,8],
[5,3,6,6,6,0,4,4,4,6,1,6,9],
[6,2,8,4,3,6,0,1,4,3,4,4,8],
[9,7,7,6,6,6,9,0,7,8,4,6,7],
[2,4,8,5,5,6,6,3,0,5,6,5,7],
[4,7,7,2,2,4,7,2,5,0,4,5,8],
[6,5,9,6,6,9,6,6,4,6,0,5,8],
[3,4,9,4,1,4,6,4,5,5,5,0,8],
[2,2,5,3,2,1,2,3,3,2,2,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 166, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,5,5,4,4,6,1,5,3,2,5,3],
[6,0,8,8,6,6,7,4,5,4,5,7,6],
[5,2,0,5,4,2,6,0,3,1,0,3,2],
[5,2,5,0,3,4,3,0,2,1,1,3,1],
[6,4,6,7,0,4,7,2,4,1,3,4,2],
[6,4,8,6,6,0,7,1,6,3,3,6,5],
[4,3,4,7,3,3,0,0,5,3,2,1,4],
[9,6,10,10,8,9,10,0,8,5,7,7,6],
[5,5,7,8,6,4,5,2,0,4,5,3,3],
[7,6,9,9,9,7,7,5,6,0,7,4,6],
[8,5,10,9,7,7,8,3,5,3,0,5,4],
[5,3,7,7,6,4,9,3,7,6,5,0,4],
[7,4,8,9,8,5,6,4,7,4,6,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 167, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,0,1,1,2,5,7,2,2,3,9,1],
[6,0,0,6,0,1,5,7,4,4,5,8,3],
[10,10,0,7,5,7,9,10,8,7,8,10,6],
[9,4,3,0,4,5,7,8,5,5,6,9,4],
[9,10,5,6,0,6,8,9,5,6,5,10,6],
[8,9,3,5,4,0,7,8,5,5,5,9,6],
[5,5,1,3,2,3,0,8,2,3,4,9,2],
[3,3,0,2,1,2,2,0,3,2,0,7,1],
[8,6,2,5,5,5,8,7,0,6,7,8,2],
[8,6,3,5,4,5,7,8,4,0,8,9,3],
[7,5,2,4,5,5,6,10,3,2,0,8,4],
[1,2,0,1,0,1,1,3,2,1,2,0,1],
[9,7,4,6,4,4,8,9,8,7,6,9,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 168, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,10,7,6,3,7,8,8,6,6,3,5],
[2,0,2,5,3,5,5,6,5,1,6,3,3],
[0,8,0,5,1,3,5,6,6,3,4,3,1],
[3,5,5,0,5,5,8,10,5,1,5,2,5],
[4,7,9,5,0,5,9,5,9,2,8,3,3],
[7,5,7,5,5,0,7,5,7,5,6,3,6],
[3,5,5,2,1,3,0,3,7,1,3,0,1],
[2,4,4,0,5,5,7,0,4,0,5,2,5],
[2,5,4,5,1,3,3,6,0,1,6,0,1],
[4,9,7,9,8,5,9,10,9,0,8,7,5],
[4,4,6,5,2,4,7,5,4,2,0,0,3],
[7,7,7,8,7,7,10,8,10,3,10,0,7],
[5,7,9,5,7,4,9,5,9,5,7,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 169, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,3,3,3,3,4,2,4,4,6,2,3],
[7,0,4,4,5,6,8,4,4,4,7,4,3],
[7,6,0,4,5,7,7,3,6,3,8,5,4],
[7,6,6,0,6,7,6,5,5,5,7,5,6],
[7,5,5,4,0,6,7,4,6,4,7,5,5],
[7,4,3,3,4,0,4,3,2,4,7,3,1],
[6,2,3,4,3,6,0,3,5,3,6,3,2],
[8,6,7,5,6,7,7,0,7,7,9,6,6],
[6,6,4,5,4,8,5,3,0,3,6,6,6],
[6,6,7,5,6,6,7,3,7,0,7,6,6],
[4,3,2,3,3,3,4,1,4,3,0,1,3],
[8,6,5,5,5,7,7,4,4,4,9,0,3],
[7,7,6,4,5,9,8,4,4,4,7,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 170, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,0,5,0,0,5,5,0,5,5,0,10],
[5,0,5,5,0,5,5,5,0,5,5,0,10],
[10,5,0,5,0,0,10,5,0,5,5,5,10],
[5,5,5,0,0,5,10,0,0,5,5,5,5],
[10,10,10,10,0,10,10,5,5,10,10,10,10],
[10,5,10,5,0,0,10,5,0,5,5,5,10],
[5,5,0,0,0,0,0,0,0,5,5,5,5],
[5,5,5,10,5,5,10,0,5,5,10,5,10],
[10,10,10,10,5,10,10,5,0,10,10,5,10],
[5,5,5,5,0,5,5,5,0,0,5,0,10],
[5,5,5,5,0,5,5,0,0,5,0,5,5],
[10,10,5,5,0,5,5,5,5,10,5,0,10],
[0,0,0,5,0,0,5,0,0,0,5,0,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 171, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,8,3,5,6,5,3,7,8,8,5,6,3],
[2,0,3,4,5,3,4,7,8,6,5,4,4],
[7,7,0,6,6,8,6,8,9,7,5,5,6],
[5,6,4,0,6,9,6,9,7,8,7,7,7],
[4,5,4,4,0,4,6,8,8,5,6,5,5],
[5,7,2,1,6,0,5,8,8,6,4,3,4],
[7,6,4,4,4,5,0,7,6,6,5,4,5],
[3,3,2,1,2,2,3,0,3,3,1,2,3],
[2,2,1,3,2,2,4,7,0,3,4,3,3],
[2,4,3,2,5,4,4,7,7,0,5,4,4],
[5,5,5,3,4,6,5,9,6,5,0,3,6],
[4,6,5,3,5,7,6,8,7,6,7,0,5],
[7,6,4,3,5,6,5,7,7,6,4,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 172, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,5,8,4,7,1,4,4,3,6,4,4],
[7,0,5,9,6,5,4,2,6,6,5,6,4],
[5,5,0,7,5,5,2,1,4,5,6,9,4],
[2,1,3,0,5,2,2,0,3,2,5,4,2],
[6,4,5,5,0,6,4,4,4,4,8,5,6],
[3,5,5,8,4,0,1,3,3,2,5,5,4],
[9,6,8,8,6,9,0,8,4,8,7,9,7],
[6,8,9,10,6,7,2,0,5,6,6,9,7],
[6,4,6,7,6,7,6,5,0,6,7,9,7],
[7,4,5,8,6,8,2,4,4,0,7,6,5],
[4,5,4,5,2,5,3,4,3,3,0,4,6],
[6,4,1,6,5,5,1,1,1,4,6,0,4],
[6,6,6,8,4,6,3,3,3,5,4,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 173, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,5,5,4,2,5,5,8,3,6,2,6],
[6,0,5,5,6,3,4,5,6,3,4,1,7],
[5,5,0,2,2,3,2,3,6,3,2,2,3],
[5,5,8,0,9,5,1,8,6,5,8,6,8],
[6,4,8,1,0,1,1,5,5,5,7,4,5],
[8,7,7,5,9,0,4,8,7,8,9,7,10],
[5,6,8,9,9,6,0,8,6,5,9,5,10],
[5,5,7,2,5,2,2,0,6,5,3,6,7],
[2,4,4,4,5,3,4,4,0,2,6,0,6],
[7,7,7,5,5,2,5,5,8,0,5,3,5],
[4,6,8,2,3,1,1,7,4,5,0,4,7],
[8,9,8,4,6,3,5,4,10,7,6,0,6],
[4,3,7,2,5,0,0,3,4,5,3,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 174, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,1,3,2,3,2,6,2,2,1,1,6],
[7,0,4,5,6,6,6,6,4,6,4,6,8],
[9,6,0,5,4,7,3,8,4,4,2,4,7],
[7,5,5,0,5,7,5,7,3,7,3,5,7],
[8,4,6,5,0,8,8,8,6,7,6,8,9],
[7,4,3,3,2,0,3,8,1,4,0,1,7],
[8,4,7,5,2,7,0,7,5,7,5,7,8],
[4,4,2,3,2,2,3,0,2,1,2,2,4],
[8,6,6,7,4,9,5,8,0,8,6,8,9],
[8,4,6,3,3,6,3,9,2,0,2,4,9],
[9,6,8,7,4,10,5,8,4,8,0,8,10],
[9,4,6,5,2,9,3,8,2,6,2,0,10],
[4,2,3,3,1,3,2,6,1,1,0,0,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 175, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,8,6,9,5,8,7,6,7,6,6,7],
[6,0,8,7,7,5,6,7,8,7,8,7,9],
[2,2,0,4,5,4,3,2,2,6,5,4,6],
[4,3,6,0,4,5,3,6,5,7,4,4,5],
[1,3,5,6,0,4,4,5,4,5,4,6,5],
[5,5,6,5,6,0,7,6,7,6,6,6,6],
[2,4,7,7,6,3,0,6,6,6,4,8,8],
[3,3,8,4,5,4,4,0,2,5,5,5,4],
[4,2,8,5,6,3,4,8,0,6,5,8,4],
[3,3,4,3,5,4,4,5,4,0,4,6,3],
[4,2,5,6,6,4,6,5,5,6,0,6,5],
[4,3,6,6,4,4,2,5,2,4,4,0,3],
[3,1,4,5,5,4,2,6,6,7,5,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 176, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,2,6,6,3,5,0,4,5,2,5,5,7],
[8,0,8,6,5,8,5,6,9,5,7,6,7],
[4,2,0,4,4,6,1,3,5,2,4,6,3],
[4,4,6,0,7,7,4,6,6,4,8,6,6],
[7,5,6,3,0,7,4,4,8,3,7,3,6],
[5,2,4,3,3,0,3,5,7,3,5,5,5],
[10,5,9,6,6,7,0,6,7,5,9,7,9],
[6,4,7,4,6,5,4,0,6,3,6,4,7],
[5,1,5,4,2,3,3,4,0,3,4,5,5],
[8,5,8,6,7,7,5,7,7,0,8,7,7],
[5,3,6,2,3,5,1,4,6,2,0,3,6],
[5,4,4,4,7,5,3,6,5,3,7,0,4],
[3,3,7,4,4,5,1,3,5,3,4,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 177, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,5,4,3,2,3,5,5,3,2,6,1],
[6,0,6,5,6,1,3,5,5,5,3,4,5],
[5,4,0,5,3,2,1,5,6,3,2,4,2],
[6,5,5,0,2,3,2,5,1,2,2,4,2],
[7,4,7,8,0,3,6,5,7,8,5,6,6],
[8,9,8,7,7,0,4,7,7,8,3,7,7],
[7,7,9,8,4,6,0,6,5,7,7,7,5],
[5,5,5,5,5,3,4,0,4,5,4,3,3],
[5,5,4,9,3,3,5,6,0,6,4,5,4],
[7,5,7,8,2,2,3,5,4,0,3,6,3],
[8,7,8,8,5,7,3,6,6,7,0,7,5],
[4,6,6,6,4,3,3,7,5,4,3,0,3],
[9,5,8,8,4,3,5,7,6,7,5,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 178, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,10,5,0,5,0,10,0,5,5,0,5],
[5,0,10,0,0,5,0,10,0,5,0,0,5],
[0,0,0,0,0,0,0,0,0,0,0,0,0],
[5,10,10,0,5,5,0,10,5,5,0,0,5],
[10,10,10,5,0,10,5,10,0,10,5,5,10],
[5,5,10,5,0,0,5,10,0,10,5,0,5],
[10,10,10,10,5,5,0,10,5,5,5,0,5],
[0,0,10,0,0,0,0,0,0,5,0,0,5],
[10,10,10,5,10,10,5,10,0,10,5,5,10],
[5,5,10,5,0,0,5,5,0,0,5,0,0],
[5,10,10,10,5,5,5,10,5,5,0,0,5],
[10,10,10,10,5,10,10,10,5,10,10,0,10],
[5,5,10,5,0,5,5,5,0,10,5,0,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 179, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,7,5,7,5,7,5,5,7,5,7,5],
[5,0,7,7,7,5,7,7,7,7,5,2,5],
[3,3,0,8,10,8,10,3,8,10,3,5,3],
[5,3,2,0,5,0,5,5,5,5,3,2,3],
[3,3,0,5,0,0,10,0,3,5,3,2,3],
[5,5,2,10,10,0,10,5,5,5,5,2,3],
[3,3,0,5,0,0,0,0,3,5,3,2,3],
[5,3,7,5,10,5,10,0,10,10,3,2,8],
[5,3,2,5,7,5,7,0,0,7,3,2,3],
[3,3,0,5,5,5,5,0,3,0,3,0,3],
[5,5,7,7,7,5,7,7,7,7,0,2,8],
[3,8,5,8,8,8,8,8,8,10,8,0,8],
[5,5,7,7,7,7,7,2,7,7,2,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 180, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,6,6,6,6,5,7,7,6,5,6,7],
[5,0,7,4,6,5,7,7,7,5,7,5,7],
[4,3,0,4,3,3,4,4,6,4,2,3,5],
[4,6,6,0,6,5,5,5,6,6,6,5,6],
[4,4,7,4,0,3,5,8,6,4,4,4,6],
[4,5,7,5,7,0,7,7,7,5,7,5,7],
[5,3,6,5,5,3,0,6,5,4,5,5,6],
[3,3,6,5,2,3,4,0,8,4,5,4,6],
[3,3,4,4,4,3,5,2,0,3,4,4,4],
[4,5,6,4,6,5,6,6,7,0,4,3,7],
[5,3,8,4,6,3,5,5,6,6,0,6,7],
[4,5,7,5,6,5,5,6,6,7,4,0,8],
[3,3,5,4,4,3,4,4,6,3,3,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 181, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,4,4,3,3,3,3,5,4,6,4,3,4],
[6,0,3,6,5,5,3,6,5,6,5,7,5],
[6,7,0,6,5,5,5,7,4,8,3,4,5],
[7,4,4,0,2,2,2,6,5,4,5,5,3],
[7,5,5,8,0,7,5,7,5,7,7,6,3],
[7,5,5,8,3,0,4,6,3,7,3,3,4],
[7,7,5,8,5,6,0,5,4,6,6,8,6],
[5,4,3,4,3,4,5,0,3,6,5,6,4],
[6,5,6,5,5,7,6,7,0,9,3,6,6],
[4,4,2,6,3,3,4,4,1,0,3,5,3],
[6,5,7,5,3,7,4,5,7,7,0,4,3],
[7,3,6,5,4,7,2,4,4,5,6,0,2],
[6,5,5,7,7,6,4,6,4,7,7,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 182, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,5,6,6,3,4,4,3,5,5,5,6],
[3,0,5,6,6,4,4,4,4,5,5,4,6],
[5,5,0,5,3,4,4,5,4,3,5,5,4],
[4,4,5,0,4,2,4,5,3,3,4,4,4],
[4,4,7,6,0,3,4,5,3,4,4,5,4],
[7,6,6,8,7,0,4,6,3,5,4,7,6],
[6,6,6,6,6,6,0,6,5,4,4,7,5],
[6,6,5,5,5,4,4,0,5,5,6,5,6],
[7,6,6,7,7,7,5,5,0,5,3,8,6],
[5,5,7,7,6,5,6,5,5,0,7,7,7],
[5,5,5,6,6,6,6,4,7,3,0,7,6],
[5,6,5,6,5,3,3,5,2,3,3,0,5],
[4,4,6,6,6,4,5,4,4,3,4,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 183, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,7,6,6,5,6,4,7,6,8,6,5],
[5,0,6,7,7,6,6,5,8,4,5,6,6],
[3,4,0,6,4,4,5,3,4,4,5,5,4],
[4,3,4,0,5,4,5,5,6,4,7,6,5],
[4,3,6,5,0,5,6,5,6,3,6,7,5],
[5,4,6,6,5,0,5,5,5,3,5,5,3],
[4,4,5,5,4,5,0,6,6,4,7,5,6],
[6,5,7,5,5,5,4,0,6,4,7,5,7],
[3,2,6,4,4,5,4,4,0,2,4,5,4],
[4,6,6,6,7,7,6,6,8,0,6,5,6],
[2,5,5,3,4,5,3,3,6,4,0,5,2],
[4,4,5,4,3,5,5,5,5,5,5,0,5],
[5,4,6,5,5,7,4,3,6,4,8,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 184, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,5,8,5,5,8,5,9,8,9,5,8],
[1,0,3,4,5,2,3,2,7,6,4,0,3],
[5,7,0,6,5,5,8,5,7,9,7,5,8],
[2,6,4,0,5,2,3,5,8,5,4,0,6],
[5,5,5,5,0,2,4,3,5,5,5,5,4],
[5,8,5,8,8,0,3,6,8,10,8,8,7],
[2,7,2,7,6,7,0,5,7,7,5,5,4],
[5,8,5,5,7,4,5,0,8,7,8,5,4],
[1,3,3,2,5,2,3,2,0,5,1,0,3],
[2,4,1,5,5,0,3,3,5,0,4,3,6],
[1,6,3,6,5,2,5,2,9,6,0,2,5],
[5,10,5,10,5,2,5,5,10,7,8,0,9],
[2,7,2,4,6,3,6,6,7,4,5,1,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 185, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,10,3,3,10,8,5,3,8,8,8,8],
[7,0,7,5,5,10,5,2,0,5,5,7,5],
[0,3,0,3,3,8,3,5,3,8,5,3,8],
[7,5,7,0,7,10,7,2,2,5,5,7,5],
[7,5,7,3,0,10,10,2,3,5,5,10,8],
[0,0,2,0,0,0,0,2,0,5,5,0,5],
[2,5,7,3,0,10,0,2,3,5,5,2,8],
[5,8,5,8,8,8,8,0,8,5,5,8,8],
[7,10,7,8,7,10,7,2,0,5,5,7,8],
[2,5,2,5,5,5,5,5,5,0,2,5,3],
[2,5,5,5,5,5,5,5,5,8,0,5,3],
[2,3,7,3,0,10,8,2,3,5,5,0,8],
[2,5,2,5,2,5,2,2,2,7,7,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 186, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,6,6,2,6,6,6,6,2,6,2,6],
[4,0,0,8,2,0,4,4,6,4,4,4,0],
[4,10,0,8,6,4,4,4,6,4,4,4,6],
[4,2,2,0,2,2,2,0,2,2,0,0,2],
[8,8,4,8,0,8,8,8,10,4,8,4,8],
[4,10,6,8,2,0,10,8,10,6,8,4,6],
[4,6,6,8,2,0,0,4,2,6,8,4,2],
[4,6,6,10,2,2,6,0,2,6,10,6,6],
[4,4,4,8,0,0,8,8,0,4,8,4,4],
[8,6,6,8,6,4,4,4,6,0,4,0,6],
[4,6,6,10,2,2,2,0,2,6,0,2,2],
[8,6,6,10,6,6,6,4,6,10,8,0,6],
[4,10,4,8,2,4,8,4,6,4,8,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 187, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,3,2,2,1,2,2,3,3,2,2,2],
[10,0,10,10,10,5,8,10,8,6,8,8,6],
[7,0,0,9,4,1,2,3,5,0,3,3,2],
[8,0,1,0,4,1,3,1,3,1,0,0,0],
[8,0,6,6,0,1,6,6,6,4,6,5,2],
[9,5,9,9,9,0,9,7,7,5,5,7,5],
[8,2,8,7,4,1,0,5,6,4,3,3,0],
[8,0,7,9,4,3,5,0,3,1,2,2,2],
[7,2,5,7,4,3,4,7,0,2,7,7,2],
[7,4,10,9,6,5,6,9,8,0,9,9,6],
[8,2,7,10,4,5,7,8,3,1,0,2,4],
[8,2,7,10,5,3,7,8,3,1,8,0,5],
[8,4,8,10,8,5,10,8,8,4,6,5,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 188, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,3,9,6,10,6,7,5,7,8,6,7],
[1,0,0,9,4,7,3,1,2,6,3,6,4],
[7,10,0,9,6,7,9,6,3,10,8,9,9],
[1,1,1,0,5,7,1,1,3,1,4,7,5],
[4,6,4,5,0,7,6,4,6,4,6,7,5],
[0,3,3,3,3,0,3,1,5,3,3,3,6],
[4,7,1,9,4,7,0,4,3,5,3,7,4],
[3,9,4,9,6,9,6,0,6,9,8,9,9],
[5,8,7,7,4,5,7,4,0,8,6,7,8],
[3,4,0,9,6,7,5,1,2,0,5,7,4],
[2,7,2,6,4,7,7,2,4,5,0,7,8],
[4,4,1,3,3,7,3,1,3,3,3,0,7],
[3,6,1,5,5,4,6,1,2,6,2,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 189, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,7,5,4,4,4,5,4,3,7,6,6,5],
[3,0,5,3,3,4,5,1,5,8,4,6,3],
[5,5,0,3,6,4,5,2,7,8,7,7,4],
[6,7,7,0,6,6,6,5,5,7,8,9,3],
[6,7,4,4,0,7,7,3,6,7,8,7,4],
[6,6,6,4,3,0,7,3,6,8,5,7,4],
[5,5,5,4,3,3,0,2,3,5,4,6,3],
[6,9,8,5,7,7,8,0,6,8,8,8,5],
[7,5,3,5,4,4,7,4,0,7,6,6,3],
[3,2,2,3,3,2,5,2,3,0,4,6,3],
[4,6,3,2,2,5,6,2,4,6,0,5,2],
[4,4,3,1,3,3,4,2,4,4,5,0,2],
[5,7,6,7,6,6,7,5,7,7,8,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 190, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1,3,3,4,4,1,5,5,4,5,1,5],
[9,0,9,6,6,6,6,9,7,7,5,9,8],
[7,1,0,3,4,5,0,5,4,3,5,7,9],
[7,4,7,0,7,6,5,8,7,8,4,6,6],
[6,4,6,3,0,5,3,7,5,5,5,6,7],
[6,4,5,4,5,0,0,7,7,6,5,3,5],
[9,4,10,5,7,10,0,9,8,8,6,8,10],
[5,1,5,2,3,3,1,0,1,3,4,5,6],
[5,3,6,3,5,3,2,9,0,5,5,5,7],
[6,3,7,2,5,4,2,7,5,0,4,5,6],
[5,5,5,6,5,5,4,6,5,6,0,5,6],
[9,1,3,4,4,7,2,5,5,5,5,0,7],
[5,2,1,4,3,5,0,4,3,4,4,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 191, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,0,0,5,5,5,0,0,5,0,0,2,0],
[10,0,0,7,5,7,0,10,5,0,5,2,2],
[10,10,0,10,7,10,5,10,10,2,5,2,2],
[5,3,0,0,0,2,3,5,0,0,5,2,0],
[5,5,3,10,0,10,5,5,5,5,5,5,5],
[5,3,0,8,0,0,3,3,3,0,3,2,0],
[10,10,5,7,5,7,0,10,7,2,5,2,2],
[10,0,0,5,5,7,0,0,5,0,2,2,0],
[5,5,0,10,5,7,3,5,0,0,5,2,2],
[10,10,8,10,5,10,8,10,10,0,10,7,10],
[10,5,5,5,5,7,5,8,5,0,0,7,5],
[8,8,8,8,5,8,8,8,8,3,3,0,8],
[10,8,8,10,5,10,8,10,8,0,5,2,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 192, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,9,6,9,6,4,4,9,6,9,9,9,6],
[1,0,2,5,4,1,4,4,2,9,2,4,1],
[4,8,0,8,5,4,7,6,5,8,9,7,6],
[1,5,2,0,5,5,5,4,4,8,5,8,2],
[4,6,5,5,0,4,8,4,5,6,5,4,4],
[6,9,6,5,6,0,7,6,6,8,7,6,7],
[6,6,3,5,2,3,0,6,5,5,6,5,5],
[1,6,4,6,6,4,4,0,2,9,3,7,3],
[4,8,5,6,5,4,5,8,0,9,5,7,5],
[1,1,2,2,4,2,5,1,1,0,2,5,2],
[1,8,1,5,5,3,4,7,5,8,0,7,1],
[1,6,3,2,6,4,5,3,3,5,3,0,4],
[4,9,4,8,6,3,5,7,5,8,9,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 193, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,4,6,3,4,4,4,7,4,4,6,4],
[5,0,4,4,3,4,4,5,8,6,3,7,6],
[6,6,0,8,5,7,6,7,8,6,6,8,5],
[4,6,2,0,4,3,5,4,5,2,4,4,3],
[7,7,5,6,0,6,8,5,7,5,5,7,6],
[6,6,3,7,4,0,6,7,7,6,5,8,5],
[6,6,4,5,2,4,0,4,4,3,3,4,4],
[6,5,3,6,5,3,6,0,5,2,5,5,4],
[3,2,2,5,3,3,6,5,0,4,4,5,3],
[6,4,4,8,5,4,7,8,6,0,5,7,5],
[6,7,4,6,5,5,7,5,6,5,0,7,7],
[4,3,2,6,3,2,6,5,5,3,3,0,2],
[6,4,5,7,4,5,6,6,7,5,3,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 194, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,10,10,8,6,7,10,9,6,10,9,4,10],
[0,0,4,3,2,4,5,7,3,5,7,1,6],
[0,6,0,4,5,2,10,9,4,5,6,3,7],
[2,7,6,0,2,6,6,8,5,6,8,4,7],
[4,8,5,8,0,5,5,7,4,9,8,3,6],
[3,6,8,4,5,0,8,7,7,5,4,5,5],
[0,5,0,4,5,2,0,6,4,5,4,2,5],
[1,3,1,2,3,3,4,0,5,6,4,3,4],
[4,7,6,5,6,3,6,5,0,6,5,7,7],
[0,5,5,4,1,5,5,4,4,0,4,2,5],
[1,3,4,2,2,6,6,6,5,6,0,3,5],
[6,9,7,6,7,5,8,7,3,8,7,0,9],
[0,4,3,3,4,5,5,6,3,5,5,1,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 195, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,2,5,3,6,6,4,5,4,5,6,2],
[7,0,2,6,5,5,4,4,4,4,4,4,1],
[8,8,0,8,7,8,7,5,6,5,8,8,7],
[5,4,2,0,6,7,7,6,7,4,6,7,2],
[7,5,3,4,0,7,5,3,8,6,8,8,5],
[4,5,2,3,3,0,6,3,4,1,4,5,4],
[4,6,3,3,5,4,0,2,7,4,8,5,3],
[6,6,5,4,7,7,8,0,7,5,8,7,5],
[5,6,4,3,2,6,3,3,0,3,5,2,3],
[6,6,5,6,4,9,6,5,7,0,4,5,4],
[5,6,2,4,2,6,2,2,5,6,0,4,0],
[4,6,2,3,2,5,5,3,8,5,6,0,4],
[8,9,3,8,5,6,7,5,7,6,10,6,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 196, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,3,5,10,5,10,8,6,6,5,5,3],
[4,0,3,5,10,7,10,8,6,8,5,5,3],
[7,7,0,7,10,7,10,8,8,10,8,10,5],
[5,5,3,0,10,7,10,5,8,5,8,7,6],
[0,0,0,0,0,3,3,3,3,3,0,0,3],
[5,3,3,3,7,0,5,8,6,6,5,3,3],
[0,0,0,0,7,5,0,5,3,3,0,2,3],
[2,2,2,5,7,2,5,0,8,8,3,5,3],
[4,4,2,2,7,4,7,2,0,2,5,2,3],
[4,2,0,5,7,4,7,2,8,0,5,4,3],
[5,5,2,2,10,5,10,7,5,5,0,5,3],
[5,5,0,3,10,7,8,5,8,6,5,0,3],
[7,7,5,4,7,7,7,7,7,7,7,7,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 197, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,3,3,4,6,4,6,5,5,5,5,7,7],
[7,0,6,3,7,7,8,5,6,6,7,8,6],
[7,4,0,5,5,6,6,5,5,6,7,6,7],
[6,7,5,0,6,6,8,6,5,6,7,8,8],
[4,3,5,4,0,4,7,5,5,7,5,6,7],
[6,3,4,4,6,0,7,6,4,6,5,8,7],
[4,2,4,2,3,3,0,4,3,5,2,5,6],
[5,5,5,4,5,4,6,0,3,5,5,5,6],
[5,4,5,5,5,6,7,7,0,5,5,6,7],
[5,4,4,4,3,4,5,5,5,0,4,5,3],
[5,3,3,3,5,5,8,5,5,6,0,6,7],
[3,2,4,2,4,2,5,5,4,5,4,0,6],
[3,4,3,2,3,3,4,4,3,7,3,4,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 198, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,5,2,5,7,2,2,5,4,5,6,3,5],
[5,0,2,5,7,7,5,5,7,5,5,3,7],
[8,8,0,6,5,8,5,6,5,3,6,6,8],
[5,5,4,0,4,2,2,5,4,2,5,2,2],
[3,3,5,6,0,3,3,8,2,3,6,6,6],
[8,3,2,8,7,0,0,8,2,5,6,6,8],
[8,5,5,8,7,10,0,8,2,5,8,6,10],
[5,5,4,5,2,2,2,0,2,2,8,5,2],
[6,3,5,6,8,8,8,8,0,3,6,6,8],
[5,5,7,8,7,5,5,8,7,0,8,8,8],
[4,5,4,5,4,4,2,2,4,2,0,0,2],
[7,7,4,8,4,4,4,5,4,2,10,0,7],
[5,3,2,8,4,2,0,8,2,2,8,3,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 199, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,6,6,8,6,7,4,6,5,7,5,8,7],
[4,0,1,4,7,3,3,5,7,5,5,8,4],
[4,9,0,5,8,4,3,6,7,6,6,9,4],
[2,6,5,0,5,4,5,4,4,5,5,8,6],
[4,3,2,5,0,4,4,5,3,4,5,7,5],
[3,7,6,6,6,0,5,4,6,5,6,6,5],
[6,7,7,5,6,5,0,8,6,8,6,8,7],
[4,5,4,6,5,6,2,0,4,6,6,7,8],
[5,3,3,6,7,4,4,6,0,5,5,6,5],
[3,5,4,5,6,5,2,4,5,0,6,8,8],
[5,5,4,5,5,4,4,4,5,4,0,5,5],
[2,2,1,2,3,4,2,3,4,2,5,0,2],
[3,6,6,4,5,5,3,2,5,2,5,8,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([13, 10, 200, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbd/mebbd_13_10.csv", index=False, header=False)